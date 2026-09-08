#!/usr/bin/env python3
"""Exact finite NS jet checks; no timestep, PDE certification or independent audit.

The infinite-order edge statement is proved in the companion evidence note.
This program checks its coefficients through --order using full convolution.
Only Python's standard library is required. No generated modes are truncated.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations
from math import factorial, isqrt
from pathlib import Path

Key = tuple[int, int, int]
Vec = tuple[F, F, F]
Field = dict[Key, Vec]
ZERO = (F(0), F(0), F(0))
SIGMA = (1, 1, 1)
checks: list[str] = []


def check(label: str, value: bool) -> None:
    if not value:
        raise AssertionError(label)
    checks.append(label)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c*x for x in a)


def neg(a):
    return tuple(-x for x in a)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def project(k: Key, v: Vec) -> Vec:
    assert k != (0, 0, 0)
    return add(v, scale(-dot(k, v)/dot(k, k), k))


def combine(*fields: Field) -> Field:
    result = defaultdict(lambda: ZERO)
    for field in fields:
        for k, v in field.items():
            result[k] = add(result[k], v)
    return {k: v for k, v in result.items() if v != ZERO}


def multiply(c: F, field: Field) -> Field:
    return {k: scale(c, v) for k, v in field.items() if c}


def bilinear(left: Field, right: Field) -> Field:
    """For u_hat=i*b: full ordered P_k sum (q.b_p)b_q, with no cutoff."""
    result = defaultdict(lambda: ZERO)
    for p, a in left.items():
        for q, b in right.items():
            k = add(p, q)
            if k == (0, 0, 0):
                continue  # Exact divergence-form zero mean.
            c = dot(q, a)
            if c:
                result[k] = add(result[k], scale(c, b))
    return {k: w for k, v in result.items() if (w := project(k, v)) != ZERO}


def rotational_quadratic(field: Field) -> Field:
    """Separate vector formula: P(u cross curl u), converted to b variables."""
    result = defaultdict(lambda: ZERO)
    for p, a in field.items():
        for q, b in field.items():
            k = add(p, q)
            if k != (0, 0, 0):
                result[k] = add(result[k], neg(cross(a, cross(q, b))))
    return {k: w for k, v in result.items() if (w := project(k, v)) != ZERO}


def inner(left: Field, right: Field) -> F:
    return sum((dot(v, right.get(k, ZERO)) for k, v in left.items()), F(0))


def initial_ring() -> Field:
    positive = {k: neg(project(k, SIGMA)) for k in set(permutations((2, 1, 0)))}
    return positive | {neg(k): neg(v) for k, v in positive.items()}


def squarefree(n: int) -> tuple[int, int]:
    factor, p = 1, 2
    while p*p <= n:
        while n % (p*p) == 0:
            factor *= p
            n //= p*p
        p += 1
    return factor, n


def critical_coefficient(coeff: list[Field], n: int) -> dict[int, F]:
    """Coefficient of t^n in (1/2) sum |k| |sum t^j b_j(k)|^2."""
    result = defaultdict(F)
    for j in range(n+1):
        for k, v in coeff[j].items():
            factor, radicand = squarefree(sum(x*x for x in k))
            result[radicand] += F(factor, 2)*dot(v, coeff[n-j].get(k, ZERO))
    return {r: c for r, c in sorted(result.items()) if c}


def radical_interval(values: dict[int, F], digits: int = 30) -> tuple[F, F]:
    denominator = 10**digits
    lo, hi = F(0), F(0)
    for r, c in values.items():
        n = isqrt(r*denominator**2)
        a = F(n, denominator)
        b = a if n*n == r*denominator**2 else F(n+1, denominator)
        assert a*a <= r <= b*b
        lo += c*(a if c >= 0 else b)
        hi += c*(b if c >= 0 else a)
    return lo, hi


def permute(a, indices):
    return tuple(a[i] for i in indices)


def mirror(a):
    return add(a, scale(-F(2, 3)*sum(a), SIGMA))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--order', type=int, default=6, choices=range(4, 9))
    parser.add_argument('--json', type=Path, help='Optional generated report, not a proof certificate')
    args = parser.parse_args()
    coeff = [initial_ring()]
    check('initial squared energy = 72/5', inner(coeff[0], coeff[0]) == F(72, 5))
    p, q = (0, 1, 2), (0, 2, 1)
    bp, bq = coeff[0][p], coeff[0][q]
    check('ordered edge terms: opposite tangential parts before summation',
          project(add(p, q), scale(dot(q, bp), bq)) == (F(3, 5), F(-9, 50), F(9, 50))
          and project(add(p, q), scale(dot(p, bq), bp)) == (F(3, 5), F(9, 50), F(-9, 50)))
    for n in range(args.order):
        coeff.append(multiply(F(1, n+1), combine(*(
            bilinear(coeff[j], coeff[n-j]) for j in range(n+1)))))
    expected_counts = [12, 24, 120, 240, 504, 792, 1296, 1824, 2640]
    for n, field in enumerate(coeff):
        check(f'order {n}: complete support count', len(field) == expected_counts[n])
        check(f'order {n}: divergence and odd reality', all(
            dot(k, v) == 0 and field.get(neg(k)) == neg(v) for k, v in field.items()))
        check(f'order {n}: leaf support enclosure and axial parity', all(
            max(abs(x) for x in k) <= 2*(n+1) and sum(k) % 3 == 0
            and (sum(k)//3-(n+1)) % 2 == 0 for k in field))
        check(f'order {n}: permutation covariance', all(
            field.get(permute(k, indices)) == permute(v, indices)
            for k, v in field.items() for indices in permutations(range(3))))
        check(f'order {n}: sigma-mirror covariance', all(
            field.get(mirror(k)) == mirror(v) for k, v in field.items()))
        if n:
            check(f'order {n}: full energy coefficient zero', sum(
                inner(coeff[j], coeff[n-j]) for j in range(n+1)) == 0)
            k = (0, n+2, 2*n+1)
            expected = (F(2*(-1)**(n+1), factorial(n))*F(3, 5)**n, F(0), F(0))
            check(f'order {n}: all-orders edge formula', field.get(k) == expected)
    mixed = combine(coeff[0], multiply(F(1, 7), coeff[1]), multiply(F(1, 11), coeff[2]))
    check('occupied network: advective and rotational formulas agree',
          bilinear(mixed, mixed) == rotational_quadratic(mixed))
    check('occupied network: exact energy cancellation', inner(mixed, bilinear(mixed, mixed)) == 0)
    check('occupied network: pointwise spectral helicity zero', all(
        dot(v, cross(k, v)) == 0 for k, v in mixed.items()))
    k = (4, 0, -1)
    check('second-order nonmeridional witness', coeff[2][k] == (F(141, 425), F(6, 5), F(564, 425))
          and dot(cross(SIGMA, k), coeff[2][k]) == F(9, 25))
    transverse = set().union(set(permutations((3, -2, -1))), set(permutations((-3, 2, 1))),
                             set(permutations((4, -3, -1))), set(permutations((-4, 3, 1))))
    check('no transverse output through order two', all(sum(k) != 0 for f in coeff[:3] for k in f))
    check('complete first transverse output: 24 carriers', {k for k in coeff[3] if sum(k) == 0} == transverse)
    check('transverse output perpendicular to sigma', all(dot(SIGMA, coeff[3][k]) == 0 for k in transverse))
    check('transverse 14 witness', coeff[3][(3, -2, -1)] ==
          (F(-98886, 1145375), F(-395544, 1145375), F(98886, 229075)))
    check('transverse 26 witness', coeff[3][(4, -3, -1)] ==
          (F(84, 2125), F(42, 425), F(-294, 2125)))
    brackets = {0: (16, 17), 2: (67, 68), 4: (49, 50), 6: (-2815, -2814), 8: (39739, 39740)}
    table = []
    for n in range(args.order+1):
        radical = critical_coefficient(coeff, n)
        lo, hi = radical_interval(radical)
        if n % 2:
            check(f'critical order {n}: zero', radical == {})
        else:
            a, b = brackets[n]
            check(f'critical order {n}: rational interval sign certificate', F(a) < lo <= hi < F(b))
        table.append({'order': n, 'radicals': {str(r): str(c) for r, c in radical.items()},
                      'lower': str(lo), 'upper': str(hi)})
    check('exact critical C2', critical_coefficient(coeff, 2) ==
          {2: F(648, 25), 5: F(-7344, 175), 14: F(5832, 175)})
    report = {'status': 'PASS', 'order': args.order, 'assertions': len(checks), 'checks': checks,
              'support_counts': [len(f) for f in coeff], 'critical_coefficients': table,
              'scope': 'Exact finite arithmetic only. No full-turnover remainder, continuum trajectory certification, RF-q estimate, independent audit or complete repository verification.'}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, indent=2)+'\n')
    print(f'PASS: {len(checks)} exact assertions through order {args.order}.')
    print(report['scope'])


if __name__ == '__main__':
    main()
