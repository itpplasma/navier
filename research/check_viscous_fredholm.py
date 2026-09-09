#!/usr/bin/env python3
"""Exact finite identities for the viscous mixed-trace inverse.

NOT a continuum PDE, compactness, independent-audit or NS proof checker.
The paper proves the operator statements; these regressions test
noncommuting finite-rank inversion, boundary signs and smoothing powers.
"""
from __future__ import annotations

import json
from random import Random
import sympy as s


def main() -> None:
    labels: list[str] = []

    def equal(left, right, label: str) -> None:
        if isinstance(left, s.MatrixBase) or isinstance(right, s.MatrixBase):
            result = (left - right).applyfunc(s.simplify)
            passed = result == s.zeros(*result.shape)
        else:
            passed = s.simplify(left - right) == 0
        if not passed:
            raise AssertionError(label)
        labels.append(label)

    def check(condition: bool, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        labels.append(label)

    rng = Random(9032026)
    noncommuting = 0
    for dim in (2, 3, 4):
        for trial in range(5):
            C = s.Matrix(dim, dim, [s.Rational(rng.randint(-3, 3), 3)
                                    for _ in range(dim * dim)])
            D = s.Matrix(dim, dim, [s.Rational(rng.randint(-3, 3), 4)
                                    for _ in range(dim * dim)])
            A, G = C.T * C, D.T * D
            eye = s.eye(dim)
            if A * G != G * A:
                noncommuting += 1
            for penalty in (s.Rational(1, 5), s.Integer(1), s.Integer(7)):
                middle = eye + penalty * C * G * C.T
                inverse = eye - penalty * G * C.T * middle.inv() * C
                equal((eye + penalty * G * A) * inverse, eye,
                      f'heat left inverse d={dim} case={trial} L={penalty}')
                equal(inverse * (eye + penalty * G * A), eye,
                      f'heat right inverse d={dim} case={trial} L={penalty}')
                equal((eye + penalty * G * A).det(), middle.det(),
                      f'noncommuting determinant d={dim} case={trial} L={penalty}')
                check(middle.det() > 0, f'positive heat determinant {dim}/{trial}/{penalty}')
    check(noncommuting >= 10, 'genuinely noncommuting heat tests')

    # A nonnormal nilpotent calibration, NOT an affine finite-energy PDE solution.
    t, T, penalty = s.symbols('t T penalty', positive=True)
    M = s.Matrix([[0, 1], [0, 0]])
    eye = s.eye(2)
    A = s.Matrix([[2, 1], [1, 2]])
    forcing = s.Matrix([s.Rational(2, 3), -s.Rational(1, 5)])
    transport, pullback, evolution = eye + t*M, eye - t*M, eye - t*M
    equal(transport * pullback, eye, 'transport/pullback orientation')
    vf = (t * eye - t ** 2 * M / 2) * forcing
    equal(s.diff(vf, t) + M * vf, forcing, 'zero-initial forced forward solution')
    Kt = (t * eye - t ** 2 * M) * A
    bt = (t ** 2 * eye / 2 - t ** 3 * M / 2) * forcing
    equal(s.diff(Kt, t), pullback * evolution * A, 'trace-map integrand')
    equal(s.diff(bt, t), pullback * vf, 'forcing trace integrand')
    eta0 = -(eye + penalty * Kt.subs(t, T)).inv() * bt.subs(t, T)
    velocity = evolution * penalty * A * eta0 + vf
    eta = transport * ((eye + penalty * Kt) * eta0 + bt)
    equal(s.diff(eta, t) - M * eta, velocity, 'complete displacement equation')
    equal(s.diff(velocity, t) + M * velocity, forcing, 'complete velocity equation')
    equal(eta.subs(t, T), s.zeros(2, 1), 'terminal displacement exactly zero')
    equal(velocity.subs(t, 0), penalty * A * eta.subs(t, 0), 'initial velocity Robin sign')

    # Finite-rank resolvent with noncommuting remainder.
    z = s.symbols('z')
    for case in range(5):
        remainder = s.Matrix([[s.Rational(1, 25), s.Rational(case, 40), 0],
                              [0, -s.Rational(1, 30), 0], [0, 0, s.Rational(1, 50)]])
        X = s.Matrix([[1, 0], [s.Rational(case, 3), 1], [0, 1]])
        Y = s.Matrix([[s.Rational(1, 4), -s.Rational(1, 3), 0],
                      [0, s.Rational(1, 5), s.Rational(1, 2)]])
        B = (s.eye(3) + z * remainder).inv()
        finite = s.eye(2) + z * Y * B * X
        inverse = (s.eye(3) - z * B * X * finite.inv() * Y) * B
        equal((s.eye(3) + z * (remainder + X * Y)) * inverse,
              s.eye(3), f'finite-rank resolvent factorization {case}')
        equal(finite.subs(z, 0).det(), 1, f'analytic determinant not identically zero {case}')

    equal(s.Rational(3, 4), s.Rational(3, 2) / 2, 'heat HS norm time exponent')
    check(1 - s.Rational(3, 4) > 0, 'integrated localized heat is HS in dimension three')
    check(1 - s.Rational(4, 4) == 0, 'same argument is borderline in dimension four')
    equal(1 - s.Rational(3, 2) / 2, s.Rational(1, 4), 'sub-two-derivative gain integrable')

    # Invertibility at each horizon is NOT one identical initial trace.
    a = s.symbols('a', positive=True)
    g = (1 - s.exp(-a * T)) / a
    h = T / a - (1 - s.exp(-a * T)) / a ** 2
    equal(s.diff(h, T), g, 'forcing displacement primitive')
    initial_velocity = -penalty * h / (1 + penalty * g)
    equal(s.limit(initial_velocity / T ** 2, T, 0), -penalty / 2,
          'generic initial trace depends on the chosen horizon')
    print(json.dumps({'status': 'PASS', 'assertions': len(labels),
                      'noncommuting_cases': noncommuting,
                      'scope': 'exact finite identities; continuum inverse and compactness are paper proofs',
                      'independent_audit': False}, indent=2))


if __name__ == '__main__':
    main()
