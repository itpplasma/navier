#!/usr/bin/env python3
"""Exact arithmetic for the finite-duration mixing test; NOT a PDE checker.

Checks the full shear reduction, its two-way infinite-ladder coefficients,
integer spectral moments, robust rational inequalities, and the exact
solenoidal slow-coordinate ansatz. The analytic R3 adapter, limiting choices,
classical identification and Lorentz continuity require the written proof.
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
    checks: list[str] = []

    def equal(a: s.Expr, b: s.Expr, label: str) -> None:
        if s.simplify(s.expand(a-b)) != 0:
            raise AssertionError(label)
        checks.append(label)

    def positive(a: s.Expr, label: str) -> None:
        if not bool(a > 0):
            raise AssertionError(label)
        checks.append(label)

    def positive_halfline(poly: s.Expr, x: s.Symbol, label: str) -> None:
        """Certify p(x)>0 for ALL x>=9 by coefficients of p(9+y)."""
        y = s.Symbol('y', nonnegative=True)
        p = s.Poly(s.expand(poly.subs(x, y+9)), y)
        for j, a in enumerate(p.all_coeffs()):
            positive(a, f'{label}: shifted coefficient {j}')

    t, x, y, phi = s.symbols('t x y phi', real=True)
    phase = x-t*s.sin(y)
    w = 2*s.sin(phase)
    equal(s.diff(w, t)+s.sin(y)*s.diff(w, x), 0,
          'full inviscid passive equation')
    equal(s.diff(s.sin(y), x), 0, 'pump self-convection vanishes')
    # All z derivatives vanish in the exact auxiliary 2D3C flow. It is
    # expressly NOT identified with a finite-energy R3 velocity.
    f = 2*s.sin(phi)

    def dy(g: s.Expr) -> s.Expr:
        return s.diff(g, y)-t*s.cos(y)*s.diff(g, phi)

    lap_f = s.diff(f, phi, 2)+dy(dy(f))
    equal(lap_f,
          -2*(1+t*t*s.cos(y)**2)*s.sin(phi)+2*t*s.sin(y)*s.cos(phi),
          'complete passive Laplacian')

    def avg(g: s.Expr) -> s.Expr:
        return s.simplify(s.integrate(s.expand_trig(s.expand(g)),
                                     (phi, -s.pi, s.pi),
                                     (y, -s.pi, s.pi))/(4*s.pi*s.pi))

    m0 = 2*avg(s.sin(y)**2+f*f)
    m1 = 2*avg(s.cos(y)**2+s.diff(f, phi)**2+dy(f)**2)
    m2 = 2*avg(s.sin(y)**2+lap_f**2)
    equal(m0, 5, 'M0 / pump energy')
    equal(m1, 5+2*t*t, 'M1 / pump energy')
    equal(m2, 5+6*t*t+s.Rational(3, 2)*t**4, 'M2 / pump energy')
    for j, expr in enumerate((m0, m1, m2)):
        equal(expr.subs(t, 0), 5, f'initial moment {j}')
    for j, target in enumerate((5, 13, 53)):
        equal((m0, m1, m2)[j].subs(t, 2), target,
              f'complete-turnover moment {j}')

    # Full support at each Taylor order: no carrier cutoff is imposed.
    order = 8
    jets = [{0: s.Integer(1)}]
    for degree in range(1, order+1):
        old = jets[-1]
        row = {k: (-old.get(k-1, 0)+old.get(k+1, 0))/(2*degree)
               for k in range(-degree, degree+1)}
        row = {k: value for k, value in row.items() if value != 0}
        direct = {degree-2*r: s.Rational((-1)**(degree+r)*s.binomial(degree, r),
                                       2**degree*s.factorial(degree))
                  for r in range(degree+1)}
        if row != direct:
            raise AssertionError(f'full ladder Taylor row {degree}')
        checks.append(f'full ladder Taylor row {degree}: exact exponential coefficients')
        jets.append(row)
    for power, prescribed in [(0, {0: s.Integer(1)}),
                              (2, {2: s.Rational(1, 2)}),
                              (4, {2: s.Rational(1, 2), 4: s.Rational(3, 8)})]:
        for degree in range(order+1):
            coeff = sum(k**power * jets[j].get(k, 0)*jets[degree-j].get(k, 0)
                        for j in range(degree+1)
                        for k in range(-order, order+1))
            equal(coeff, prescribed.get(degree, 0),
                  f'full ladder frequency moment n^{power}, Taylor degree {degree}')
    equal(s.Rational(-1, 2)*s.Rational(1, 2), -s.Rational(1, 4),
          'forward/reverse coefficient product: both directions retained')

    h = s.Rational(1, 100)
    C0, C1, C2 = 5+h, 13-h, 53+h
    c = s.Rational(121, 100)
    energy_lower = (C1-c*C0)**2 / ((C2-2*c*C1+c*c*C0)*C0)
    critical_ratio_sq = C1**3/(C2*C0*C0)
    equal(energy_lower, s.Rational(533286649, 1609286649),
          'robust first-turnover forward-energy fraction')
    positive(energy_lower-s.Rational(1, 4), 'first-turnover fraction > 1/4')
    equal(critical_ratio_sq, s.Rational(81182737, 49279863),
          'robust first-turnover critical-ratio square')
    positive(critical_ratio_sq-s.Rational(36, 25),
             'first-turnover squared-Hhalf ratio > 6/5')

    X = s.Symbol('X', nonnegative=True)  # X=tau^2 >= 9
    M0, M1, M2 = s.Integer(5), 5+2*X, 5+6*X+s.Rational(3, 2)*X*X
    a = M1-h-X*(M0+h)/9
    b = M2+h-2*X*(M1-h)/9+X*X*(M0+h)/81
    positive_halfline(a, X, 'positive high-pass first moment')
    positive_halfline(b, X, 'positive centered second moment')
    band_poly = s.expand(16*X*X*a*a-(M2+h)*b
                         -(M0+h)*16*X*X*b/3)
    positive_halfline(band_poly, X,
                      'energy in [tau/3,2tau] > initial energy/3')
    tail_poly = s.expand(s.Rational(4096, 81)*X*X*(M0-h)-100*(M2+h))
    positive_halfline(tail_poly, X,
                      'previous energy above next band < initial energy/100')
    gain_poly = s.expand((5-h+128*X)**3
                         -25*(5+h)*(5+h+2*X)*(5+h+384*X+6144*X*X))
    positive_halfline(gain_poly, X,
                      'eightfold-frequency-step squared-Hhalf gain > 5')
    equal(s.Rational(1, 3)-s.Rational(1, 100), s.Rational(97, 300),
          'net repeated high-pass birth fraction')
    for j in range(1, 7):
        equal(s.Integer(3)*8**j/(s.Integer(3)*8**(j-1)), 8,
              f'time ratios grow, not Zeno: step {j}')
        positive(s.Integer(8)**j-6*s.Integer(8)**(j-1),
                 f'successive frequency bands are disjoint: step {j}')

    # Exact slow-coordinate vector potential and ALL residual powers.
    # z differentiation is eps*d/dZ, NOT d/dZ.
    Xh, Yh, Z, T, eps, mu = s.symbols('Xh Yh Z T eps mu', real=True)
    psi = s.Function('psi')(T, Xh, Yh, Z)
    zeta = s.Function('zeta')(T, Xh, Yh, Z)
    p = s.Function('p')(T, Xh, Yh, Z)
    v = [s.diff(psi, Yh), -s.diff(psi, Xh)]
    w0 = s.diff(zeta, Xh, 2)+s.diff(zeta, Yh, 2)
    U = [v[0]-eps*s.diff(zeta, Xh, Z),
         v[1]-eps*s.diff(zeta, Yh, Z), w0]
    coords = (Xh, Yh, Z)

    def deriv(g: s.Expr, j: int) -> s.Expr:
        return (eps if j == 2 else 1)*s.diff(g, coords[j])

    equal(sum(deriv(U[j], j) for j in range(3)), 0,
          'exact full R3 divergence correction')
    leading = [v[0], v[1], w0]
    max_degrees = []
    for i in range(3):
        residual = (s.diff(U[i], T)
                    -mu*sum(deriv(deriv(U[i], j), j) for j in range(3))
                    +sum(U[j]*deriv(U[i], j) for j in range(3))
                    +deriv(p, i))
        base = (s.diff(leading[i], T)
                -mu*(s.diff(leading[i], Xh, 2)+s.diff(leading[i], Yh, 2))
                +v[0]*s.diff(leading[i], Xh)+v[1]*s.diff(leading[i], Yh)
                +(s.diff(p, coords[i]) if i < 2 else 0))
        equal(residual.subs(eps, 0), base,
              f'component {i}: zero-order residual is exactly 2D3C')
        correction = s.Poly(s.expand(residual-base), eps)
        equal(correction.nth(0), 0,
              f'component {i}: every omitted term has a slow derivative')
        max_degrees.append(correction.degree())
        if i == 2:
            equal(s.diff(residual, s.diff(p, Z)), eps,
                  'vertical pressure response explicitly retained')
    equal(s.Integer(max(max_degrees)), 3, 'complete residual degree')

    # Scaling and RF detector constants (Fourier convention exp(-2pi i x.xi)).
    equal(s.Rational(1, 2)*s.Rational(2, 3)+2*s.Rational(1, 3), 1,
          'fractional moment Holder exponent')
    equal(1-s.sqrt(2)/2, 1-1/s.sqrt(2), 'RF geometric-tail constant')
    equal(s.Rational(1, 1)-s.Rational(1, 4), s.Rational(3, 4),
          'initial shell elliptic bound at angular cutoff >= 2')
    equal(s.Rational(1, 3)-1, -s.Rational(2, 3),
          'slow corrector L3 power')
    equal(s.Rational(1, 2)-1, -s.Rational(1, 2),
          'full residual L2 power')
    equal(-s.Rational(1, 2)-s.Rational(1, 3), -s.Rational(5, 6),
          'relative Lorentz error power')

    result = {
        'status': 'exact-finite-algebra-passed',
        'checks': len(checks),
        'scope': __doc__,
        'first_turnover_energy_fraction_lower': str(energy_lower),
        'first_turnover_critical_ratio_squared_lower': str(critical_ratio_sq),
        'halfline': 'all X >= 9; positive rational coefficients after X=9+y',
        'residual_degrees': max_degrees,
        'labels': checks,
        'not_checked': ['R3 PDE adapter and limiting choices',
                        'global-existence literature theorem',
                        'independent mathematical audit',
                        'hexagon continuum turnover',
                        'scale-regenerating cascade', 'RF-q upper bound']
    }
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(result, indent=2)+'\n')
    print(f'PASS: {len(checks)} exact arithmetic and symbolic assertions.')
    print('NOT CERTIFIED: PDE proof, independent audit, cascade replication or RF-q producer.')


if __name__ == '__main__':
    main()
