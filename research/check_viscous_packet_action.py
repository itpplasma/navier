#!/usr/bin/env python3
"""Exact regressions for the full NS displacement action.

These finite identities do not certify the continuum oscillatory limit,
small-data global existence, an independent audit, or an unforced cascade.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as s


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    labels: list[str] = []

    def equal(actual: s.Expr, expected: s.Expr, label: str) -> None:
        if s.simplify(s.expand(actual-expected)) != 0:
            raise AssertionError(label)
        labels.append(label)

    x, y, z, t, nu = s.symbols('x y z t nu', real=True)
    coords = s.Matrix([x, y, z])

    def jac(v: s.Matrix) -> s.Matrix:
        return v.jacobian(coords)

    def grad(f: s.Expr) -> s.Matrix:
        return s.Matrix([s.diff(f, q) for q in coords])

    def lap(v: s.Matrix) -> s.Matrix:
        return v.applyfunc(lambda f: sum(s.diff(f, q, 2) for q in coords))

    def div(v: s.Matrix) -> s.Expr:
        return sum(s.diff(v[j], coords[j]) for j in range(3))

    def curl(v: s.Matrix) -> s.Matrix:
        return s.Matrix([s.diff(v[2], y)-s.diff(v[1], z),
                         s.diff(v[0], z)-s.diff(v[2], x),
                         s.diff(v[1], x)-s.diff(v[0], y)])

    # A nonconstant-gradient polynomial NS jet. It is an algebra test,
    # not the finite-energy background of the theorem.
    u0 = s.Matrix([y*y, x*z, 0])
    p0 = -s.Rational(2, 3)*y**3*z
    ut0 = -jac(u0)*u0 + nu*lap(u0)-grad(p0)
    equal(div(u0), 0, 'initial jet is solenoidal')
    equal(div(ut0), 0, 'NS time jet is solenoidal')
    equal(sum(s.diff(p0, q, 2) for q in coords)+div(jac(u0)*u0),
          0, 'pressure Poisson equation at the test jet')
    u = u0+t*ut0
    G = jac(u)
    phi = x*x*y*z
    eta = curl(s.Matrix([0, 0, phi]))*(1+t+t*t)

    def Dt(v: s.Matrix) -> s.Matrix:
        return s.diff(v, t)+jac(v)*u

    w = Dt(eta)-G*eta
    equal(div(w), 0, 'full deterministic displacement preserves divergence')
    actual = Dt(w)+G*w-nu*lap(w)
    cross = sum((s.diff(G, q)*s.diff(eta, q) for q in coords), s.zeros(3, 1))
    predicted = (Dt(Dt(eta))+s.hessian(p0, coords)*eta
                 -nu*lap(Dt(eta))+nu*G*lap(eta)+2*nu*cross)
    for i in range(3):
        equal((actual[i]-predicted[i]).subs(t, 0), 0,
              f'complete NS displacement operator component {i}')

    # Independent component integration-by-parts identity. The exact
    # divergences integrate to zero for the theorem's compact test fields.
    original = eta.dot(lap(Dt(eta))-G*lap(eta)-2*cross)
    spatial_div = sum(s.diff(eta.dot(s.diff(Dt(eta), q)-G*s.diff(eta, q)), q)
                      for q in coords)
    B = jac(eta)
    bnorm = sum(q*q for q in B)
    material = s.diff(bnorm, t)+grad(bnorm).dot(u)
    remainder = sum(s.diff(eta, q).dot(G*s.diff(eta, q))
                    -eta.dot(s.diff(G, q)*s.diff(eta, q)) for q in coords)
    remainder -= sum(G[k, j]*s.diff(eta, coords[j]).dot(s.diff(eta, coords[k]))
                     for j in range(3) for k in range(3))
    equal(original, spatial_div-material/2+remainder,
          'viscous action including its exact divergence currents')

    a = s.Matrix(s.symbols('a0:3', real=True))
    xi = s.Matrix(s.symbols('xi0:3', real=True))
    matrix = s.Matrix(3, 3, s.symbols('g0:9', real=True))
    rankone = a*xi.T
    contraction = s.trace(matrix*(rankone*rankone.T-rankone.T*rankone))
    equal(contraction, xi.dot(xi)*a.dot(matrix*a)-a.dot(a)*xi.dot(matrix*xi),
          'rank-one principal action symbol for all matrix entries')
    skew = (matrix-matrix.T)/2
    equal(xi.dot(xi)*a.dot(skew*a)-a.dot(a)*xi.dot(skew*xi), 0,
          'only symmetric strain enters the principal action symbol')

    sym = (matrix+matrix.T)/2
    equal(sum(v*v for v in sym),
          (sum(v*v for v in matrix)+s.trace(matrix*matrix))/2,
          'symmetric-gradient energy decomposition for all entries')
    low, high = s.symbols('lambda_low lambda_high', real=True)
    diag = s.diag(low, high, -low-high)
    e_min, e_max = s.Matrix([1, 0, 0]), s.Matrix([0, 1, 0])
    equal(e_min.dot(diag*e_min)-e_max.dot(diag*e_max), low-high,
          'minimum/maximum strain directions give their signed gap')
    equal(s.trace(diag), 0, 'classification uses the trace-free strain class')

    strain = s.diag(-1, 1, 0)
    potential = -coords.cross(strain*coords)/3
    for i in range(3):
        equal(curl(potential)[i], (strain*coords)[i],
              f'localized affine-germ vector potential component {i}')
    cutoff = s.Function('theta')(x, y, z)
    equal(div(curl(cutoff*potential)), 0, 'compact cutoff-curl datum is solenoidal')
    wave = s.symbols('N', positive=True)
    bump = s.Function('phi')(x, y, z)
    seed = curl(s.Matrix([0, 0, bump*s.sin(wave*y)/wave]))
    equal(div(seed), 0, 'complete oscillatory test seed is solenoidal')
    equal(seed[0], bump*s.cos(wave*y)+s.diff(bump, y)*s.sin(wave*y)/wave,
          'test seed includes envelope derivative correction')
    equal(seed[1], -s.diff(bump, x)*s.sin(wave*y)/wave,
          'test seed retains transverse envelope correction')

    epsilon = s.symbols('epsilon', positive=True)
    F = s.diag(s.exp(-epsilon*t), s.exp(epsilon*t), 1)
    e1, e2 = s.Matrix([1, 0, 0]), s.Matrix([0, 1, 0])
    av, xiv = F*e1, F.inv().T*e2
    equal(F.det(), 1, 'reference deformation preserves volume')
    equal(av.dot(xiv), 0, 'pushed polarization stays transverse')
    equal(xiv.dot(xiv)*av.dot(epsilon*strain*av)
          -av.dot(av)*xiv.dot(epsilon*strain*xiv),
          -2*epsilon*s.exp(-4*epsilon*t),
          'strict negative action symbol on the reference local strain')
    # This reference deformation locates the sign. The proof uses a genuine
    # compact-data NS flow and continuity on one fixed short interval.
    theta = s.symbols('theta', real=True)
    equal(s.integrate(s.sin(theta)**2, (theta, 0, 2*s.pi))/(2*s.pi),
          s.Rational(1, 2), 'oscillatory squared-sine mean')
    equal(s.integrate(s.cos(theta)**2, (theta, 0, 2*s.pi))/(2*s.pi),
          s.Rational(1, 2), 'oscillatory squared-cosine mean')

    # Hardy identity: integration removes the displayed boundary derivative.
    T = s.symbols('T', positive=True)
    h = s.Function('h')(t)
    eta_scalar = s.sqrt(T-t)*h
    equal(s.diff(eta_scalar, t)**2-eta_scalar**2/(4*(T-t)**2),
          (T-t)*s.diff(h, t)**2-s.diff(h*h, t)/2,
          'exact Hardy ground-state identity')
    c = s.symbols('c', nonnegative=True)
    equal(1-4*c, 4*(s.Rational(1, 4)-c), 'Hardy coercivity threshold')
    result = {'status': 'PASS', 'assertions': len(labels), 'labels': labels,
              'scope': 'finite algebra only; continuum proof and independent audit not certified'}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
