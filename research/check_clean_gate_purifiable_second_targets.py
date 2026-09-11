#!/usr/bin/env python3
"""Exact intended-polarization projection test at all second clean-gate targets.

The full leading quartic/order-three coefficient at each nominal second-gate
frequency is ancestry-contaminated.  These exact obstruction polynomials prove
that, at the isolated positive clean-circuit root, each full coefficient still
has a nonzero component along the intended selected polarization.  This is the
necessary algebraic input for the repository's mode-specific affine purifier.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

z=sp.symbols('z',real=True)
Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
a=sp.Rational(12847,10000); b=sp.Rational(803,625)
check(Q.eval(a)<0 and Q.eval(b)>0,'positive clean root is bracketed')
check(Q.count_roots(a,b)==1,'exactly one clean root in bracket')

# Numerators of <V_sel,V_full> after removal of nonzero rational denominator
# and harmless powers of z.  They were obtained from the exact Taylor
# recurrence for the three nominal second-gate targets.
Rp=sp.Poly(3*z**15+8*z**14+7*z**13+8*z**12+25*z**11+76*z**10+53*z**9-2*z**8+76*z**7+162*z**6+256*z**5-44*z**4+128*z**3+120*z**2+48*z-176,z)
R0=sp.Poly(9*z**15-82*z**14+351*z**13-912*z**12+1701*z**11-2876*z**10+5547*z**9-11084*z**8+19174*z**7-27222*z**6+32442*z**5-31712*z**4+23456*z**3-11360*z**2+2744*z-80,z)
Rm=sp.Poly(3*z**15-8*z**14+7*z**13-8*z**12+25*z**11-76*z**10+53*z**9+2*z**8+76*z**7-162*z**6+256*z**5+44*z**4+128*z**3-120*z**2+48*z+176,z)

for name,R in [('h_plus',Rp),('h_middle',R0),('h_minus',Rm)]:
    check(sp.gcd(Q,R).degree()==0,f'{name}: projection obstruction coprime to Q')
    check(R.count_roots(a,b)==0,f'{name}: projection numerator has no zero in positive-root bracket')
    check(R.eval((a+b)/2)!=0,f'{name}: projection midpoint calibration nonzero')

# The intended selected vectors themselves are nonzero at clean return roots;
# this follows from the already frozen nonzero projective multipliers.  The
# powers of z removed above are harmless because Q(0)!=0.
check(Q.eval(0)!=0,'clean return roots have z nonzero')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('At the positive clean-circuit root, all three ancestry-contaminated second targets retain nonzero intended polarization components.')
print('Scope: algebraic projection condition only; simultaneous spatial purification/localization is not proved.')
