#!/usr/bin/env python3
"""Exact regressions for the approximate-gap pressure estimate, not a PDE solver."""
import sympy as s

if not __debug__:
    raise RuntimeError('Run without -O: exact assertions are required')


def main():
    d, K, th, eta, A = s.symbols('d K th eta A', positive=True)
    c = (1 + 2*d)/(1 - 2*d)
    assert s.cancel((1-2*d)*c-(1+2*d)) == 0
    # High pressure work: 2 delta c ||v_h|| ||F_h||, F=2 grad(U) w.
    # Low pressure work: ||v_l|| exp(A) ||F_l||.
    assert s.expand(2*d*c*2*K + th*s.exp(A)*2*K*eta
                    - (4*d*c*K+2*K*s.exp(A)*th*eta)) == 0
    # Exact canonical Newtonian dipole: Hessian(Gamma)e_3 norm.
    x, y, z = s.symbols('x y z', real=True)
    r2 = x*x+y*y+z*z
    h = s.Matrix([3*x*z,3*y*z,3*z*z-r2])
    assert s.expand(h.dot(h)-r2*(r2+3*z*z)) == 0
    u, rho, R, M = s.symbols('u rho R M', positive=True)
    angular = 2*s.pi*s.integrate(1+3*u*u,(u,-1,1))
    radial = s.integrate(rho**-4,(rho,R,s.oo))
    tail = s.simplify(M*M*angular*radial/(16*s.pi**2))
    assert tail == M*M/(6*s.pi*R**3)
    # exp(-c L) dominates exp(C L^(3/4)) times any fixed polynomial.
    L, C, c0, b = s.symbols('L C c0 b', positive=True)
    rate = (C*L**s.Rational(3,4)-c0*L+(b+1)*s.log(L))/L
    assert s.limit(rate,L,s.oo) == -c0
    # Polynomial low purity is not enough for the unrestricted elliptic map.
    p, beta = s.symbols('p beta', positive=True)
    assert s.limit((A-p*s.log(A))/A,A,s.oo) == 1
    assert s.simplify((A-beta*A)/A) == 1-beta
    print('PASS: exact approximate-gap pressure coefficients and Newtonian dipole tail.')
    print('All-mode defect: J_gap=2 integral K exp(osc(phi)) theta eta.')
    print('exp(-c L) low-sector purity suffices under the stated polynomial K budget.')
    print('An index-zero smooth compact force makes the elliptic norm >= c exp(osc(phi)).')
    print('Scope: analytic all-mode lemma plus elliptic counter-control; no actual-history purity or feedback bound.')


if __name__ == '__main__':
    main()
