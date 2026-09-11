#!/usr/bin/env python3
"""Exact reality/reflection obstruction for the one-sided Raman lattice.

For the single-axis Beltrami purifier, a real Fourier field containing a module
(l,Q) also contains the reflected module (-l,-Q).  The leading Beltrami Raman
symbol therefore contains both +l and -l slow translations.  In particular the
actual middle target h0 has an unavoidable two-step return

    h0 -> h0+l -> h0

through every nonzero real module.  The return coefficient is proportional to
|alpha_l|^2 and a strictly positive geometric factor, so module phase cannot
remove it.

Scope: exact leading effective Raman symbol.  This invalidates the pointed
one-sided semigroup as a model of a real purifier; it does not by itself refute
a bidirectional/self-energy repair.
"""
from __future__ import annotations
import sympy as sp

z=sp.symbols('z', real=True)
lo=sp.Rational(12847,10000)
hi=sp.Rational(803,625)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

# Actual contaminated middle-target e1 coefficient.
pure0=2*z*(z**3+2*z-4)/(3*(z**2-4*z+6))
other0=(5*z**10-32*z**9+89*z**8-120*z**7+67*z**6-12*z**5+159*z**4-396*z**3+412*z**2-176*z+20)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3))
ax=sp.cancel(pure0+other0)
num_ax,den_ax=sp.together(ax).as_numer_denom()
assert sp.gcd(sp.Poly(num_ax,z),Qclean).degree()==0
# Every denominator factor is a positive quadratic on R.
assert sp.factor(den_ax)==6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)

Q=sp.Matrix([1,0,0])
h=sp.Matrix([z-2,-1,-1])
x=z-2
SHIFTS=[(0,-7,-1),(0,-7,1),(0,-5,-5),(0,-1,-7),(0,1,-7)]

# Reality: q=NQ+l/2 and r=-NQ+l/2 force -q,-r, which are exactly the
# (-l,-Q) module.  Hence both translation signs are present.
N=sp.symbols('N', positive=True)
for lt in SHIFTS:
    l=sp.Matrix(lt)
    q=N*Q+l/2
    r=-N*Q+l/2
    assert -q == N*(-Q)+(-l)/2
    assert -r == -N*(-Q)+(-l)/2
    assert l[0]==0

# Denominator-free P_k Q.
def pclear(k,qdir):
    return sp.expand((k.dot(k))*qdir-k*(k.dot(qdir)))

# Leading Beltrami Raman symbol, with the harmless common factor -2 removed:
#   (a.Q)(Q.(k+l)) P_{k+l}Q.
# For the return test, denominators are positive and irrelevant to nonvanishing.
return_factors=[]
for lt in SHIFTS:
    l=sp.Matrix(lt)
    k1=h+l

    # First h -> h+l leg.  Only the e1 component of the actual trigger is needed.
    d1=sp.expand(ax*x*pclear(k1,Q))
    first_x=sp.factor(d1[0])
    yz2=sp.Integer(k1[1]**2+k1[2]**2)
    assert yz2>0
    assert sp.factor(first_x-ax*x*yz2)==0

    # Reflected second leg uses (-l,-Q) and returns exactly to h.
    # The x component of the denominator-free return is enough to prove it is
    # nonzero.  Algebraically it is proportional to ax*x^2*yz2.
    ret=sp.expand((d1.dot(-Q))*((-Q).dot(h))*pclear(h,-Q))
    ret_x=sp.factor(ret[0])
    expected=sp.factor(-2*ax*x**2*yz2)
    assert sp.factor(ret_x-expected)==0
    ret_num=sp.together(ret_x).as_numer_denom()[0]
    assert sp.gcd(sp.Poly(ret_num,z),Qclean).degree()==0
    return_factors.append(yz2)

# All five same-module return weights have the same sign.  Restoring physical
# Leray denominators changes yz2 to yz2/(x^2+yz2)>0.  Reality fixes the reflected
# module strength to conjugate(alpha), so the two-step coefficient is
# -4 |alpha|^2 ax x^2 [yz2/(x^2+yz2)] P_h Q.
# Therefore phases cannot cancel an individual return, and sums over nonzero
# modules have a common sign factor.
assert return_factors == [68,64,72,68,64]
assert all(v>0 for v in return_factors)
assert hi<2  # x=z-2 is nonzero throughout the isolated clean interval.

# The one-sided pointed-semigroup statement is incompatible with reality even
# at depth two: each generator is accompanied by its negative and l+(-l)=0.
for lt in SHIFTS:
    l=sp.Matrix(lt)
    assert l+(-l)==sp.zeros(3,1)

print('PASS: real Fourier reflection forces both +/- Raman shifts.')
print('Each nonzero single-axis module has an exact phase-independent depth-two return h0 -> h0+l -> h0.')
print('The pointed one-sided Raman semigroup cannot be the all-orders real-field lattice.')
print('Scope: leading effective symbol; a bidirectional/self-energy normal form remains possible.')
