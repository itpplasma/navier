#!/usr/bin/env python3
"""Exact identities for the energy-controlled exterior-pressure theorem.

The universal estimate is proved analytically in the accompanying evidence;
these finite checks are not a PDE regularity or blowup certificate.
"""
from fractions import Fraction as F
from itertools import product
import sympy as s


def main() -> None:
    xyz = s.symbols('x y z', real=True)
    radius = s.symbols('radius', positive=True)
    newton = 1/(4*s.pi*s.sqrt(sum(x*x for x in xyz)))
    third = [s.diff(newton, xyz[i], xyz[j], xyz[k])
             for i, j, k in product(range(3), repeat=3)]
    at_axis = {xyz[0]: radius, xyz[1]: 0, xyz[2]: 0}
    norm_squared = s.simplify(sum(d.subs(at_axis)**2 for d in third))
    assert norm_squared == 90/(16*s.pi**2*radius**8)
    # Frobenius norm is rotation invariant. The radial tail is the whole-space
    # upper bound used for every translated inner cylinder.
    gap = s.symbols('gap', positive=True)
    tail = s.integrate(norm_squared*4*s.pi*radius**2, (radius, gap, s.oo))
    assert s.simplify(tail-9/(2*s.pi*gap**5)) == 0
    # Off the source the third-derivative tensor is divergence-free in output.
    for j, k in product(range(3), repeat=2):
        assert s.simplify(sum(s.diff(newton, xyz[i], xyz[i], xyz[j], xyz[k])
                              for i in range(3))) == 0

    N, R, a = s.symbols('N R a', positive=True)
    log_bound = -N*s.log(a)-s.Rational(5, 2)*s.log(R-a)
    critical = 2*N*R/(2*N+5)
    assert s.simplify(s.diff(log_bound, a).subs(a, critical)) == 0
    assert s.simplify(s.diff(log_bound, a, 2)
                     - (N/a**2+s.Rational(5, 2)/(R-a)**2)) == 0
    # Squared radius-dependent factor has integer exponents for an exact test.
    count = 13
    for n in (1, 2, 5, 20, 100):
        q = F(2*n, 2*n+5)
        value = q**(-2*n)*(1-q)**(-5)
        formula = F(2*n+5, 2*n)**(2*n)*F(2*n+5, 5)**5
        assert value == formula
        for delta in (F(1, 100), F(1, 10)):
            for other in (q-delta, q+delta):
                if 0 < other < 1:
                    assert other**(-2*n)*(1-other)**(-5) >= value
                    count += 1
        count += 1
    # Critical spatial scaling of the operator L1 -> L2: R^-5/2.
    lam = s.symbols('lam', positive=True)
    assert s.simplify(lam**4*lam**(-s.Rational(3, 2))
                     - lam**s.Rational(5, 2)) == 0
    count += 1
    print(f'PASS: {count} exact exterior-pressure energy controls.')
    print('Kernel bound constant: 3/sqrt(2*pi); optimal inner radius: 2*N*R/(2*N+5).')
    print('Finite-energy quadratic stress supplies the far-pressure budget; full-history gain remains uncontrolled.')


if __name__ == '__main__':
    main()
