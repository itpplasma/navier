#!/usr/bin/env python3
"""Exact two-axis coupling-separation certificate for Raman spectral export.

For a slow carrier (k,a) and unit fast axis qhat, the leading Beltrami Raman
edge strength contains the carrier factor (a.qhat)(k.qhat).  We use the
scale-free squared coupling dose

    C_Q(k,a)=((a.Q)^2 (k.Q)^2)/(|a|^2 |k|^2 |Q|^4),

which is unchanged by rescaling Q.  Two simple rational axes with positive
weights separate the three desired second targets from four load-bearing old
carriers by more than an order of magnitude at the clean algebraic root.
"""
from __future__ import annotations
import sympy as sp

z=sp.symbols('z',real=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

QA=sp.Matrix([-1,-5,-6])
QB=sp.Matrix([10,-3,-1])
assert QA.dot(QA)==62
assert QB.dot(QB)==110

def dose(k,a,Q):
    return sp.factor((a.dot(Q)**2)*(k.dot(Q)**2)/(a.dot(a)*k.dot(k)*Q.dot(Q)**2))

def export_dose(k,a):
    return sp.factor(30*dose(k,a,QA)+10*dose(k,a,QB))

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

# Desired clean second-target carriers receive less than 13/200 export dose.
for h in [(0,1,1),(-2,-1,-1),(0,-1,1)]:
    W=export_dose(physk(h),vsel(h))
    assert_positive_on_clean(sp.Rational(13,200)-W,f'desired {h} dose < 13/200')

Dp=z**2+2*z+2; Dm=z**2-2*z+2
unwanted=[
 ('p1',sp.Matrix([1,0,0]),sp.Matrix([0,1,z])),
 ('g2',sp.Matrix([1+z,0,-1]),sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])),
 ('g3',sp.Matrix([1-z,0,1]),sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])),
 ('r1',sp.Matrix([-1,-1,0]),sp.Matrix([0,0,1])),
]
# The four load-bearing unwanted carriers all receive export dose >1.
for name,k,a in unwanted:
    W=export_dose(k,a)
    assert_positive_on_clean(W-1,f'{name} dose > 1')

print('PASS: exact two-axis Raman coupling separation on the clean-root interval.')
print('Axes QA=(-1,-5,-6), QB=(10,-3,-1), weights 30 and 10.')
print('All three desired target doses are <13/200; p1,g2,g3,r1 doses are >1.')
print('Scope: coupling geometry only; the skew-plus-viscosity hypocoercive spectral gap remains to be proved.')
