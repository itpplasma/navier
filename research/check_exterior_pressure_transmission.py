#!/usr/bin/env python3
"""Exact finite controls for the analytic exterior-pressure cylinder theorem.

The arbitrary-order proof is in the evidence packet. These controls cannot
certify a universal theorem, a full adjoint estimate, or Navier--Stokes blowup.
"""
from fractions import Fraction as F
from math import factorial
import sympy as s


def main() -> None:
    r, n, k = s.symbols('r n k', positive=True)
    f = s.Function('f')(r)
    boundary = r*f*s.diff(f, r)
    ode_second = (n*n/r**2+k*k)*f-s.diff(f, r)/r
    derivative = s.diff(boundary, r).subs(s.diff(f, r, 2), ode_second)
    density = r*(s.diff(f, r)**2+(n*n/r**2+k*k)*f**2)
    assert s.simplify(derivative-density) == 0

    count = 1
    # I_n(r) coefficients (k=1); compare both exact convolution formulas.
    for order in range(1, 17):
        a = [F(1, 2**(order+2*j)*factorial(j)*factorial(order+j))
             for j in range(17)]
        coefficients = []
        for m in range(17):
            direct = sum((order+2*j)*a[j]*a[m-j] for j in range(m+1))
            symmetric = (order+m)*sum(a[j]*a[m-j] for j in range(m+1))
            assert direct == symmetric and direct > 0
            coefficients.append(direct)
            count += 1
        for ratio in (F(1, 2), F(2, 3), F(9, 10)):
            outer = sum(coefficients)
            inner = sum(c*ratio**(2*order+2*m)
                        for m, c in enumerate(coefficients))
            assert inner <= ratio**(2*order)*outer
            # The low-axial-frequency monomial saturates the correct exponent.
            energy_ratio = ratio**(2*order)
            assert energy_ratio > ratio**(2*order+2)  # hostile N+1 claim
            count += 2

    # Vector grading: p=(x+i y)^N; complex Cartesian derivatives have N-1,
    # but the natural vector rotation action restores grade N.
    x, y, theta = s.symbols('x y theta', real=True)
    rot = s.Matrix([[s.cos(theta), -s.sin(theta)],
                    [s.sin(theta), s.cos(theta)]])
    grad_linear_pressure = s.Matrix([1, s.I])
    assert all(s.simplify(v) == 0 for v in
               rot.T*grad_linear_pressure
               - (s.cos(theta)+s.I*s.sin(theta))*grad_linear_pressure)
    count += 1

    # A singular radial branch has a nonzero/infinite axis boundary term:
    # it cannot be inserted into the regular-cylinder energy identity.
    bad = r**(-n)
    assert s.simplify(r*bad*s.diff(bad, r)) == -n*r**(-2*n)
    assert s.simplify(r*r**n*s.diff(r**n, r)) == n*r**(2*n)
    count += 2

    # Exact subsequence of the source growth comparison, h=1/100 and
    # j=200*m: N=2^m, j^2=40000*m^2. This is a control, not its limit proof.
    m = 40
    assert 2**m > 40000*m*m
    ratio_next = F(2*m*m, (m+1)**2)
    assert ratio_next > 1
    count += 2
    print(f'PASS: {count} exact exterior-pressure controls.')
    print('Analytic statement: ||grad p||_C_r <= (r/R)^|n| ||grad p||_C_R.')
    print('Scope: harmonic Leray tail; full physical adjoint and UE1 remain open.')


if __name__ == '__main__':
    main()
