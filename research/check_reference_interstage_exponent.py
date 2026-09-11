#!/usr/bin/env python3
"""Exact arithmetic for passive factor-two interstage carry in the source reference.

This checks the algebraic part only.  The physical-source adapter over the full
interstage interval is deliberately not assumed.
"""
from fractions import Fraction

checks = 0

# A doubled physical frequency born at native scale q0 has normalized
# z(x)=2*x^(h/2), x=q/q0.  It reaches z=1 at rho=2^(-2/h).
# Therefore rho^(-h)=4 and log(1/rho)=2 log(2)/h exactly.
for hp in range(1, 10):
    h = Fraction(hp, 1000)  # repository range sample 0<h<1/100
    log2_rho = -Fraction(2, 1) / h
    assert -h * log2_rho == 2
    checks += 1

# Reference positive-branch rate is r_+(z,s)=a-b z^2 with
# a=1/sqrt(1+s^2)<=1 and b=(3/5)(1+s^2)>=3/5.
# Integrating q^(-1-h) r_+(2(q/q0)^(h/2),s) from q0 down to rho*q0
# produces q0^(-h)/h * (3 a - 8 b log 2).
# Exact lower bound: log 2 = 2*atanh(1/3) > 2/3.
ln2_lower = Fraction(2, 3)
b_lower = Fraction(3, 5)
coefficient_upper = 3 - 8 * b_lower * ln2_lower
assert coefficient_upper == Fraction(-1, 5)
checks += 1

# Hence the coefficient is strictly below -1/5 for every real tilt s.
for y_num in range(1, 101):
    # y=1+s^2 >=1.  We avoid sqrt numerics: 3/sqrt(y)<=3 and
    # (24/5)y log2 > (24/5)*(2/3)y >=16/5.
    y = Fraction(y_num, 1)
    damping_lower = Fraction(24, 5) * y * ln2_lower
    assert damping_lower >= Fraction(16, 5)
    assert 3 - damping_lower <= Fraction(-1, 5)
    checks += 2

# Super-quasipolynomial comparison at exponent level:
# q0=2^-ell gives q0^-h=2^(h ell), which dominates every ell^p.
# Freeze exact dyadic ratios on a geometric subsequence where h*ell is integer.
for denom in (200, 500, 1000):
    h = Fraction(1, denom)
    previous = None
    for k in range(4, 13):
        ell = denom * k
        qinv_h = 2 ** k
        ratio = Fraction(qinv_h, ell * ell)
        if previous is not None and k >= 8:
            assert ratio > previous
        previous = ratio
        checks += 1

print(f'reference interstage exact checks: {checks} passed')
print('For the continuously self-similar frozen reference, passive z=2 -> z=1 carry has exponent <= -c q0^(-h).')
print('Scope: this does not supply the missing full-physical interstage propagator comparison.')
