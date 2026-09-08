#!/usr/bin/env python3
"""Exact finite algebra for the convex-cone linearity author proof.

This is NOT a PDE/continuum-cone certificate or independent mathematical audit.
Run from any directory. Requires SymPy, as do the existing research checks.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import sympy as s

checks = 0


def require(condition: bool, description: str) -> None:
    global checks
    if not bool(condition):
        raise AssertionError(description)
    checks += 1


def zero(expr: s.Expr, description: str) -> None:
    require(s.expand(expr) == 0, description)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, help='optional finite-check report')
    args = parser.parse_args()

    # Every homogeneous quadratic map, not just a selected NS calibration.
    x, y, z, t = s.symbols('x y z t', real=True)
    v = s.Matrix(s.symbols('v0:3', real=True))
    ell = s.Matrix(s.symbols('l0:3', real=True))
    coordinates = s.Matrix([x, y, z])
    monomials = s.Matrix([x*x, x*y, x*z, y*y, y*z, z*z])
    coefficients = s.Matrix(3, 6, s.symbols('c0:18', real=True))
    generic_q = coefficients * monomials

    def evaluate(field: s.Matrix, at: s.Matrix) -> s.Matrix:
        return field.subs(dict(zip(coordinates, at)), simultaneous=True)

    qv = evaluate(generic_q, v)
    ql = evaluate(generic_q, ell)
    cross = evaluate(generic_q, v+ell)-qv-ql
    qt = evaluate(generic_q, v+t*ell)
    for component in qt-(qv+t*cross+t*t*ql):
        zero(component, 'quadratic polarization has no extra factor two')
    energy_polynomial = s.Poly(s.expand((v+t*ell).dot(qt)), t)
    expected = [v.dot(qv), ell.dot(qv)+v.dot(cross),
                ell.dot(cross)+v.dot(ql), ell.dot(ql)]
    for power, value in enumerate(expected):
        zero(energy_polynomial.nth(power)-value,
             f'energy coefficient at degree {power}')

    # The two signs of t force the same pointed derivative into +/- C.
    bp, ap = s.symbols('b a', real=True)
    require(s.limit((t*bp+t*t*ap)/t, t, 0, dir='+') == bp,
            'positive one-sided tangent')
    require(s.limit((-t*bp+t*t*ap)/t, t, 0, dir='+') == -bp,
            'negative one-sided tangent')
    a, b, c, d, V = s.symbols('a b c d V', real=True)
    vz = s.Matrix([0, 0, V])
    zz = s.Matrix([a, b, 0])
    bz = s.Matrix([c, d, 0])
    zero(zz.dot(zz)+vz.dot(bz)-(a*a+b*b),
         'lineality output is killed by the linear energy coefficient')

    # Nonacute cones: their opening is strictly between pi/2 and pi.
    # Rational unit rays allow exact tests, with no trigonometric rounding.
    ratios = sorted({Fraction(p, q) for q in range(2, 19)
                     for p in range(1, q)})
    wide_cases = 0
    weights = [s.Rational(0), s.Rational(1, 7), s.Rational(1),
               s.Rational(5, 3), s.Rational(7)]
    for ratio in ratios:
        r = s.Rational(ratio.numerator, ratio.denominator)
        ca, si = (1-r*r)/(1+r*r), 2*r/(1+r*r)
        if ca*ca-si*si >= 0:
            continue
        wide_cases += 1
        plus, minus = s.Matrix([ca, si]), s.Matrix([ca, -si])
        w = (plus+minus)/2
        delta = ca*ca
        require(ca > 0 and delta > 0, 'pointed but nonuniform dual margin')
        require(plus.dot(minus) < 0, 'test cone is not acute')
        zero(plus.dot(plus)-1, 'first ray has exact unit length')
        zero(minus.dot(minus)-1, 'second ray has exact unit length')
        zero(w.dot(w)-delta, 'minimum-norm section margin')
        for alpha in weights:
            for beta in weights:
                if alpha == beta == 0:
                    continue
                output = alpha*plus+beta*minus
                require(w.dot(output) > 0, 'strict dual positivity')
                # Squared version of <w,z> >= delta |z|; both sides >=0.
                excess = w.dot(output)**2-delta**2*output.dot(output)
                zero(excess-4*ca**4*si**2*alpha*beta,
                     'exact nonacute-cone margin identity')
                require(excess >= 0, 'cone margin survives all tested loadings')
    require(wide_cases > 0, 'nonacute configurations were actually tested')

    n = s.symbols('n', positive=True, integer=True)
    zero(1/n-n/(2*n*n)-1/(2*n), 'spectral exhaustion epsilon power')
    r = n/(n+1)
    ca = (1-r*r)/(1+r*r)
    require(s.limit(ca**2, n, s.oo) == 0,
            'no uniform positive aperture can be inserted')

    # Sharpness checks: linear directions survive the convex algebra.
    halfspace_q = s.Matrix([y*z, -x*z, 0])
    zero(coordinates.dot(halfspace_q), 'lineality example conserves energy')
    require(halfspace_q[2] == 0, 'halfspace nonlinear output stays in halfspace')
    require(evaluate(halfspace_q, s.Matrix([0, 0, z])) == s.zeros(3, 1),
            'pointed component stationary in lineality example')
    require(evaluate(halfspace_q, s.Matrix([1, 1, 1])) != s.zeros(3, 1),
            'full cone output is not incorrectly asserted to vanish')
    require(s.simplify(-s.I*(s.I*s.I)) == s.I,
            'original quadratic phase preserves the imaginary real-vector line')

    # A correlated invariant flow is not invariant under independent deletion.
    triad = s.Matrix([-y*z, -x*z, 2*x*y])
    zero(coordinates.dot(triad), 'correlated triad energy cancellation')
    zero((triad[0]-triad[1]).subs(y, x), 'equal parents remain equal')
    require(evaluate(triad, s.Matrix([0, 1, 1]))[0] < 0,
            'deleting one parent creates an outgoing face')
    require(evaluate(triad, s.Matrix([1, 1, 1]))[0] < 0,
            'flow invariance does not imply Q(K) subset K without holes')
    zero((2*x*triad[0]-2*y*triad[1]), 'parent correlation integral')
    X, Y, alpha = s.symbols('X Y alpha', positive=True)
    pump = s.Matrix([-alpha*X*Y, alpha*X*X])
    zero(s.Matrix([X, Y]).dot(pump), 'averaged pump energy cancellation')
    require(pump[0] < 0 and pump[1] > 0,
            'energy cancellation alone allows a correlated positive pump')

    result = {
        'status': 'PASS',
        'exact_assertions': checks,
        'nonacute_rational_cones': wide_cases,
        'scope': 'finite symbolic and rational identities only',
        'not_certified': ['measurable cone representation',
                          'continuum Fourier-hole limit',
                          'Lebesgue differentiation', 'PDE local theory',
                          'independent mathematical audit', 'NS-R3'],
    }
    print(json.dumps(result, indent=2))
    if args.json is not None:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
