#!/usr/bin/env python3
"""Exact full-carrier rate separation for the common-line Raman Schur limit.

For QA=(-1,-5,-6), QB=(10,-3,-1), weights 30,10, common perpendicular
ell=QA x QB, and overall strength gain 4096, the leading center Schur damping
operator has selected-carrier Rayleigh contribution

  (32768/6699) C(k,a),

where
  C=sum_i w_i (a.Q_i)^2 (k.Q_i)^2/(|a|^2 |Q_i|^4).

At the clean root, all three desired second-target selected directions have
C<1/4, while their rejected directions, all original parents, all first selected
carriers, and the complete inherited ladder have C>1.  Including ordinary
viscosity gives decay rate <21/4 on every desired selected carrier and >47/8 on
every unwanted carrier, hence a uniform gap >5/8.
"""
from __future__ import annotations
import sympy as sp

z=sp.symbols('z',real=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

QA=sp.Matrix([-1,-5,-6]); QB=sp.Matrix([10,-3,-1]); ell=QA.cross(QB)
assert ell==sp.Matrix([-13,-61,53]) and ell.dot(ell)==6699
GAIN=sp.Integer(4096)
FACTOR=sp.Rational(8*GAIN,6699)

def Cform(k,a):
    return sp.factor(
        30*(a.dot(QA)**2)*(k.dot(QA)**2)/(a.dot(a)*QA.dot(QA)**2)
       +10*(a.dot(QB)**2)*(k.dot(QB)**2)/(a.dot(a)*QB.dot(QB)**2))

def assert_positive_on_clean(expr,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    mid=(lo+hi)/2
    assert p.count_roots(lo,hi)==0,label
    assert p.eval(mid)>0,label
    assert den.subs(z,mid)>0,label

def physk(h):
    return sp.Matrix([sp.Integer(h[0])-z*sp.Integer(h[2]),sp.Integer(h[1]),sp.Integer(h[2])])

def vsel(h):
    if h==(0,1,1):
        return sp.Matrix([
          2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2+4*z+2)/(3*(z**2+2)*(z**2+2*z+2)),
          2*z**3*(z**4+2*z**3+z**2-2)/(3*(z**2+2)*(z**2+2*z+2))])
    if h==(-2,-1,-1):
        return sp.Matrix([
         -2*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
         -2*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
         -2*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2))])
    if h==(0,-1,1):
        return sp.Matrix([
         -2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2-4*z+2)/(3*(z**2+2)*(z**2-2*z+2)),
         -2*z**3*(z**4-2*z**3+z**2-2)/(3*(z**2+2)*(z**2-2*z+2))])
    raise KeyError(h)

desired=[]; rejected=[]
for h in [(0,1,1),(-2,-1,-1),(0,-1,1)]:
    k=physk(h); v=vsel(h); f=sp.simplify(k.cross(v))
    assert sp.simplify(k.dot(v))==0 and sp.simplify(k.dot(f))==0
    desired.append((str(h),k,v))
    rejected.append((str(h)+'-rejected',k,f))

Dp=z**2+2*z+2; Dm=z**2-2*z+2
old=[
 ('p1',sp.Matrix([1,0,0]),sp.Matrix([0,1,z])),
 ('p2',sp.Matrix([0,1,0]),sp.Matrix([1,0,z])),
 ('p3',sp.Matrix([-z,0,1]),sp.Matrix([1,0,z])),
 ('g1',sp.Matrix([-1,-1,0]),sp.Matrix([0,0,-2*z])),
 ('g2',sp.Matrix([1+z,0,-1]),sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])),
 ('g3',sp.Matrix([1-z,0,1]),sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])),
]

# Desired selected directions: weak Schur damping C<1/4 and total rate <21/4.
for name,k,a in desired:
    C=Cform(k,a)
    assert_positive_on_clean(sp.Rational(1,4)-C,name+': C<1/4')
    # All desired |k|^2<4 on the clean interval.
    assert_positive_on_clean(4-k.dot(k),name+': |k|^2<4')
    rate=sp.factor(k.dot(k)+FACTOR*C)
    assert_positive_on_clean(sp.Rational(21,4)-rate,name+': total rate<21/4')

# Finite unwanted classes: strong Schur damping C>1 and total rate >47/8.
for name,k,a in rejected+old:
    C=Cform(k,a)
    assert_positive_on_clean(C-1,name+': C>1')
    assert_positive_on_clean(k.dot(k)-sp.Rational(999,1000),name+': |k|^2>=~1')
    rate=sp.factor(k.dot(k)+FACTOR*C)
    assert_positive_on_clean(rate-sp.Rational(47,8),name+': total rate>47/8')

# Full inherited ladder r_n=(-n,-1,0), polarization e3.
n=sp.symbols('n',integer=True,positive=True)
kn=sp.Matrix([-n,-1,0]); e3=sp.Matrix([0,0,1])
Cladder=sp.factor(Cform(kn,e3))
assert Cladder==(422800*n**2+3209340*n+8176149)/sp.Integer(1162810)
assert sp.factor(sp.together(Cladder-1)) == (422800*n**2+3209340*n+7013339)/sp.Integer(1162810)
# Every coefficient of the numerator is positive for n>=1, so C>1.
rate_ladder=sp.factor(kn.dot(kn)+FACTOR*Cladder)
assert sp.simplify(rate_ladder.subs(n,1)-sp.Rational(47,8))>0
# Both n^2 and Cladder are strictly increasing for n>=1, hence n=1 is the minimum.
assert sp.diff(rate_ladder,n).subs(n,1)>0

# Crude rational rate gap used by the effective consumer.
assert sp.Rational(47,8)-sp.Rational(21,4)==sp.Rational(5,8)
# The underlying inequalities have strict slack:
assert sp.Rational(4)+sp.Rational(8192,6699)<sp.Rational(21,4)
assert sp.Rational(1)+sp.Rational(32768,6699)>sp.Rational(47,8)

print('PASS: exact full-carrier common-line Schur rate separation.')
print('Desired selected targets: C<1/4 and total effective decay rate <21/4.')
print('Rejected targets, p1-p3, g1-g3, and every inherited r_n: C>1 and total rate >47/8.')
print('Uniform selected-carrier rate gap >5/8 before the O(1/J) Schur remainder.')
