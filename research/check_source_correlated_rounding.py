#!/usr/bin/env python3
"""Exact pair-sum-preserving integer rounding lemma for source carriers."""
from fractions import Fraction

# Desired scalar periodic carrier offsets.  The proof below is general for
# a1+a2=a3+a4; these rational values calibrate the four-parent cage.
a1=Fraction(1,2); a2=Fraction(-2,5); a3=Fraction(1,5); a4=Fraction(-1,10)
assert a1+a2==a3+a4

def nearest(x):
    # deterministic nearest integer, ties irrelevant for the error bound
    n=x.numerator//x.denominator
    if 2*(x-n)>=1: n+=1
    return n

for K in range(20,201):
    x1=K*a1; x2=K*a2; x3=K*a3; x4=K*a4
    n1=nearest(x1); n2=nearest(x2); n3=nearest(x3)
    n4=n1+n2-n3
    e1=Fraction(n1)-x1; e2=Fraction(n2)-x2
    e3=Fraction(n3)-x3; e4=Fraction(n4)-x4
    assert abs(e1)<=Fraction(1,2)
    assert abs(e2)<=Fraction(1,2)
    assert abs(e3)<=Fraction(1,2)
    assert e4==e1+e2-e3
    assert abs(e4)<=Fraction(3,2)
    assert n1+n2==n3+n4

print('PASS: correlated integer rounding preserves the two-decomposition daughter exactly.')
print('Three rounding errors are <=1/2 and the forced fourth error is <=3/2.')
print('Scope: arithmetic carrier rounding only; localization and physical PDE leakage are separate.')
