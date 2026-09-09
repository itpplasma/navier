#!/usr/bin/env python3
"""Finite exact checks for the positive pressure-curvature barrier.

Not a PDE proof, a proof of the universal BMO interpolation, an independent
mathematical audit, or a check of the external Euler construction.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from itertools import product

import sympy as s


def main() -> None:
    checks: list[str] = []

    def eq(left: s.Expr, right: s.Expr, label: str) -> None:
        if s.simplify(left - right) != 0:
            raise AssertionError(label)
        checks.append(label)

    def truth(value: bool, label: str) -> None:
        if not value:
            raise AssertionError(label)
        checks.append(label)

    b, k, r = s.symbols('b k r', positive=True)
    expression = 48*(b/r+k*r/2)
    optimum = s.sqrt(2*b/k)
    eq(s.diff(expression, r).subs(r, optimum), 0,
       'semiconcavity radius is stationary')
    eq(expression.subs(r, optimum), 48*s.sqrt(2*b*k),
       'semiconcavity optimized constant')
    for dim in range(1, 7):
        local_upper = 2**dim
        central_lower = 2**(dim+1)
        truth(2*(local_upper+central_lower) == 3*2**(dim+1),
              f'convex supporting-plane ball constants, dimension {dim}')
    truth(3*2**4 == 48, 'three-dimensional gradient factor')

    x = s.symbols('x0:3', real=True)
    radius2 = sum(z*z for z in x)
    kernel_base = radius2**s.Rational(-1, 2)  # omit common factor 1/(4*pi)
    for i, j in product(range(3), repeat=2):
        delta = s.Integer(i == j)
        kernel = (3*x[i]*x[j]-delta*radius2)/radius2**s.Rational(5, 2)
        eq(s.diff(kernel_base, x[i], x[j]), kernel,
           f'canonical pressure kernel {i}{j}')
        for ell in range(3):
            expected = (3*(s.Integer(i == ell)*x[j]
                           +s.Integer(j == ell)*x[i]
                           +delta*x[ell])/radius2**s.Rational(5, 2)
                        -15*x[i]*x[j]*x[ell]/radius2**s.Rational(7, 2))
            eq(s.diff(kernel, x[ell]), expected,
               f'far-field pressure-kernel derivative {i}{j}{ell}')
    eq(sum(x[i]**2*x[j]**2 for i, j in product(range(3), repeat=2)),
       radius2**2, 'Frobenius norm of double-Riesz symbol numerator')
    eq(s.integrate(r*s.Symbol('rho', positive=True)**(-2),
                   (s.Symbol('rho', positive=True), 2*r, s.oo)),
       s.Rational(1, 2), 'far-oscillation radial integral is scale independent')

    u = s.symbols('u0:3', real=True)
    eps = s.symbols('eps', nonnegative=True)
    grad = [[s.Symbol(f'g{i}{j}', real=True) for j in range(3)]
            for i in range(3)]
    norm_grad2 = sum(grad[i][j]**2 for i, j in product(range(3), repeat=2))
    defect = ((sum(v*v for v in u)+eps**2)*norm_grad2
              -sum(sum(u[i]*grad[i][j] for i in range(3))**2
                   for j in range(3)))
    squares = eps**2*norm_grad2 + sum(
        (u[i]*grad[ell][j]-u[ell]*grad[i][j])**2
        for j in range(3) for i in range(3) for ell in range(i+1, 3))
    eq(s.expand(defect), s.expand(squares),
       'regularized-speed diffusion defect is a sum of squares')

    # Complete intermediate product exponents for the H3 tame estimate.
    truth(F(1, 6)+F(1, 3) == F(1, 2), 'D1-D2 product Holder exponents')
    truth(F(2, 3)+F(1, 3) == 1, 'D1-D2 product M exponent')
    truth(F(1, 3)+F(2, 3) == 1, 'D1-D2 product D3 exponent')
    truth(1-3*F(1, 6) == F(1, 3)*(3-3*F(1, 2)),
          'D1-L6 interpolation scaling')
    truth(2-3*F(1, 3) == F(2, 3)*(3-3*F(1, 2)),
          'D2-L3 interpolation scaling')
    truth(1-3*F(1, 4) == F(1, 2)*(2-3*F(1, 2)),
          'D1-L4 interpolation scaling')
    truth(4*F(1, 6)+F(1, 3) == 1,
          'first H3 integration-by-parts Holder sum')
    truth(F(1, 6)+F(1, 3)+F(1, 2) == 1,
          'second H3 integration-by-parts Holder sum')

    nu, m, y, z = s.symbols('nu m y z', positive=True)
    eq(nu*z*z/2 + m*m*y*y/(2*nu)-m*y*z,
       (s.sqrt(nu)*z-m*y/s.sqrt(nu))**2/2,
       'viscous Young absorption, with correct nu inverse')
    truth(F(1, 2)*4-2 == 0, 'positive curvature clock NS invariance')
    truth(2*1-2 == 0, 'squared-velocity time integral NS invariance')
    truth(2+2 == 4, 'pressure Hessian scales to degree four')
    truth(2+1-2 == 1, 'pressure gradient integrated in time scales as velocity')
    truth(2+2-6 == -2, 'H3-to-gradient Fourier radial tail is integrable')

    tau, alpha = s.symbols('tau alpha', positive=True)
    eq(s.diff(tau**(1-2*alpha)/(1-2*alpha), tau), tau**(-2*alpha),
       'type-I squared-speed primitive')
    c = s.symbols('c', positive=True)
    eq(s.diff(-s.sqrt(c)*s.log(tau), tau), -s.sqrt(c)/tau,
       'type-I positive curvature clock')
    C = s.symbols('C', positive=True)
    eq(2*C*s.sqrt(1/(4*C*C)), 1, 'one-sided type-I threshold is strict')
    for level in (1, 2, 10, 1000):
        hess = s.diag(-level, 1, 0)
        truth(max(hess.eigenvals()) == 1,
              f'upper eigenvalue does not bound negative curvature: {level}')

    print(json.dumps({'status': 'PASS', 'assertions': len(checks),
                      'scope': __doc__, 'checks': checks}, indent=2))


if __name__ == '__main__':
    main()
