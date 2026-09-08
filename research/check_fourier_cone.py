#!/usr/bin/env python3
"""Exact algebra for Fourier-cone obstructions; NOT a continuum PDE certificate.

Checks original Leray pair coefficients, every generated quadratic carrier,
cyclic energy signs, all orthants, symbolic unequal-length polarizations,
and the correlated pump that invalidates an overbroad no-go. Requires SymPy.
The analytic cone/packet theorems are written in the companion evidence note.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sympy as s

from check_phase_locked_ring import (
    ZERO, add, bilinear, combine, cross, dot, multiply, neg, project, scale,
)

checks: list[str] = []


def check(label: str, value: bool) -> None:
    if not value:
        raise AssertionError(label)
    checks.append(label)


def equal(label: str, lhs, rhs=0) -> None:
    check(label, s.simplify(lhs-rhs) == 0)


def wave(k, a):
    """Real odd Fourier field u_hat=i*b with positive coefficient -i*a."""
    return {k: neg(a), neg(k): a}


def inner(v, w):
    return sum((dot(a, w.get(k, ZERO)) for k, a in v.items()), F(0))


def source(v, w):
    return combine(bilinear(v, w), bilinear(w, v))


def pair(p, q, a, b):
    return project(add(p, q), add(scale(dot(q, a), b), scale(dot(p, b), a)))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()

    # Symbolic complex coefficients, real nonparallel carrier geometry.
    P, Q, t = s.symbols('P Q t', positive=True)
    at, az, bt, bz = s.symbols('at az bt bz', complex=True)
    cs = (1-t*t)/(1+t*t)
    sn = 2*t/(1+t*t)
    p = s.Matrix([P, 0, 0])
    q = s.Matrix([Q*cs, Q*sn, 0])
    a = s.Matrix([0, at, az])
    b = s.Matrix([-bt*sn, bt*cs, bz])
    r = p+q
    raw = q.dot(a)*b+p.dot(b)*a
    projected = raw-r*r.dot(raw)/r.dot(r)
    transverse = s.Matrix([-r[1], r[0], 0])
    equal('symbolic p.a', p.dot(a))
    equal('symbolic q.b', q.dot(b))
    equal('symbolic projected divergence', r.dot(projected))
    equal('unequal-length tangential numerator', transverse.dot(projected),
          sn*(Q*Q-P*P)*at*bt)
    equal('normal polarization numerator', projected[2], sn*(Q*at*bz-P*bt*az))
    equal('normal-normal interaction vanishes', sum(
        z*z for z in projected.subs({at: 0, bt: 0})))

    # Exact independent recalculation using the rotational identity.
    # For complex carrier coefficients a,b the two cross terms of u x curl u
    # have i*(a x (q x b) + b x (p x a)); after P this equals -i*A.
    keys = [k for k in product(range(-1, 2), repeat=3) if any(k)]
    cases = 0
    for p in keys:
        for q in keys:
            if cross(p, q) == (0, 0, 0) or dot(p, p) == dot(q, q):
                continue
            for seed_a, seed_b in [((1, 2, -1), (2, -3, 1)),
                                   ((0, 0, 1), (1, 0, 0)),
                                   (cross(p, q), cross(p, q))]:
                a = project(p, tuple(F(x) for x in seed_a))
                b = project(q, tuple(F(x) for x in seed_b))
                out = pair(p, q, a, b)
                rotational = project(add(p, q), add(cross(a, cross(q, b)),
                                                     cross(b, cross(p, a))))
                check(f'rotational/advective {cases}', rotational == neg(out))
                if a != ZERO and b != ZERO:
                    normals = dot(q, a) == 0 and dot(p, b) == 0
                    check(f'unequal-length zero classification {cases}',
                          (out == ZERO) == normals)
                cases += 1

    p, q, r = (1, 0, 0), (0, 1, 0), (1, 1, 0)
    a, b, c = tuple(map(F, (0, 1, 1))), tuple(map(F, (-1, 0, -1))), tuple(map(F, (0, 0, 1)))
    fields = [wave(p, a), wave(q, b), wave(r, c)]
    coefficients = []
    e3 = (F(0), F(0), F(1))
    expected = [
        {(1, 0, 0): e3, (-1, 0, 0): neg(e3),
         (1, 2, 0): neg(e3), (-1, -2, 0): e3},
        {(0, 1, 0): neg(e3), (0, -1, 0): e3,
         (2, 1, 0): e3, (-2, -1, 0): neg(e3)},
        {(1, 1, 0): scale(F(-2), e3), (-1, -1, 0): scale(F(2), e3)},
    ]
    for i, j, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        result = source(fields[j], fields[k])
        check(f'complete cross output {i}', result == expected[i])
        coefficients.append(inner(fields[i], result))
        for mode, vec in result.items():
            check(f'output solenoidal {i} {mode}', dot(mode, vec) == 0)
            check(f'output odd reality {i} {mode}', result[neg(mode)] == neg(vec))
        for j0 in range(3):
            check(f'no measured self-pump {i} {j0}',
                  inner(fields[i], bilinear(fields[j0], fields[j0])) == 0)
    check('cyclic coefficients are (-2,-2,4)', coefficients == [-2, -2, 4])
    check('cyclic energy cancellation', sum(coefficients) == 0)
    check('normalization squared norms', [inner(f, f) for f in fields] == [4, 4, 2])
    full = combine(*fields)
    check('full occupied triple energy cancellation', inner(full, bilinear(full, full)) == 0)
    check('all ten full-vector outputs retained', len(bilinear(full, full)) == 10)
    for signs in product((-1, 1), repeat=3):
        factor = signs[0]*signs[1]*signs[2]
        values = [factor*v for v in coefficients]
        check(f'every orthant has an outgoing face {signs}', min(values) < 0 < max(values))

    # Exact separation margin for radius-delta tests vs self-sums of radius 2delta.
    carriers = [p, q, r]
    distances_squared = []
    for ki in carriers:
        for kj in carriers:
            for output in [(0, 0, 0), tuple(2*x for x in kj), tuple(-2*x for x in kj)]:
                diff = tuple(x-y for x, y in zip(ki, output))
                distances_squared.append(dot(diff, diff))
    check('every packet/self-sum center distance >= 1', min(distances_squared) == 1)
    check('delta < 1/4 is sufficient for three-radius gap', F(3, 4) < 1)

    x, y, z, beta, nu, A, T = s.symbols('x y z beta nu A T', real=True)
    vector = [-beta*y*z, -beta*z*x, 2*beta*x*y]
    equal('abstract triad energy identity', sum(v*w for v, w in zip([x, y, z], vector)))
    equal('correlated-parent difference invariant', 2*x*vector[0]-2*y*vector[1])
    equal('equal-parent subspace invariant', (vector[0]-vector[1]).subs(y, x))
    equal('equal-parent subspace survives correct viscous terms',
          (vector[0]-nu*x-vector[1]+nu*y).subs(y, x))
    Xsol = A/s.cosh(beta*A*T)
    Zsol = A*s.tanh(beta*A*T)
    equal('explicit correlated pump first equation', s.diff(Xsol, T)+beta*Xsol*Zsol)
    equal('explicit correlated pump second equation', s.diff(Zsol, T)-beta*Xsol**2)
    equal('explicit correlated pump energy', Xsol**2+Zsol**2, A*A)

    # Exponent regressions: L2-normalized spatial dilation of a packet.
    half = s.Rational(1, 2)
    equal('cyclic coefficient dilation', 3*(3*half)+1-3, 5*half)
    equal('gradient Linfinity dilation', 3*half+1, 5*half)
    equal('Laplacian L2 dilation', 3*half+2-3*half, 2)
    equal('amplitude-viscosity ratio dilation', 5*half-2, half)
    equal('packet cubic width exponent', 6-3*(3*half), 3*half)

    result = {'status': 'exact-algebra-passed', 'checks': len(checks),
              'rational_pair_cases': cases, 'cyclic_coefficients': coefficients,
              'scope': __doc__, 'labels': checks,
              'not_certified': ['continuum Fourier-hole cone theorem',
                                'Lebesgue differentiation argument',
                                'Schwartz packet asymptotic remainder',
                                'independent mathematical audit',
                                'two-turnover or infinite NS cascade',
                                'RF-q upper producer or NS-R3']}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2, default=str)+'\n')
    print(f'PASS: {len(checks)} exact assertions; {cases} rational pair cases.')
    print('NOT CERTIFIED: continuum PDE proof, independent audit, regeneration or RF-q.')


if __name__ == '__main__':
    main()
