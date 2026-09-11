#!/usr/bin/env python3
"""Exact common-strain separation of clean second targets from inherited carriers.

At the isolated positive clean-circuit root, one rational trace-free symmetric
matrix has negative quadratic form on all three intended second-target
polarizations and positive quadratic form on: their transverse rejected
polarizations, all three original parents, all three first-generation selected
carriers, and the full vertical inherited-parent ladder.  At dimensionless
strength 2048, viscosity-retaining instantaneous Kelvin rates have the desired
strict signs.

This is a carrier-rate certificate, not an autonomous switch-on theorem or a
recursive Navier--Stokes turnover.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def assert_sign_on_interval(expr,z,a,b,sgn,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    check(p.count_roots(a,b)==0,f'{label}: numerator has no zero in clean-root interval')
    mid=(a+b)/2
    check(sp.sign(p.eval(mid))==sgn,f'{label}: numerator sign')
    check(den.subs(z,mid)>0,f'{label}: denominator positive calibration')

z=sp.symbols('z',real=True)
Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
check(Q.eval(lo)<0 and Q.eval(hi)>0 and Q.count_roots(lo,hi)==1,
      'unique positive clean root isolated')

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
check(H==H.T,'inheritance filter symmetric')
check(sp.trace(H)==0,'inheritance filter trace free')

def qform(v):
    v=sp.Matrix(v)
    return sp.factor((v.T*H*v)[0]/v.dot(v))
def physk(h):
    return sp.Matrix([sp.Integer(h[0])-z*sp.Integer(h[2]),sp.Integer(h[1]),sp.Integer(h[2])])
def vsel(h):
    h=tuple(h)
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

targets=[(0,1,1),(-2,-1,-1),(0,-1,1)]
M=sp.Integer(2048)
for h in targets:
    k=physk(h); v=vsel(h); f=sp.simplify(k.cross(v))
    check(sp.simplify(k.dot(v))==0,f'{h}: intended transverse')
    check(sp.simplify(k.dot(f))==0 and sp.simplify(v.dot(f))==0,
          f'{h}: rejected transverse orthogonal')
    qv=qform(v); qf=qform(f)
    assert_sign_on_interval(qv,z,lo,hi,-1,f'{h}: intended form negative')
    assert_sign_on_interval(qf,z,lo,hi, 1,f'{h}: rejected form positive')
    assert_sign_on_interval(sp.factor(-M*qv-k.dot(k)),z,lo,hi, 1,
                            f'{h}: intended viscous rate positive at M=2048')
    assert_sign_on_interval(sp.factor(-M*qf-k.dot(k)),z,lo,hi,-1,
                            f'{h}: rejected viscous rate negative at M=2048')

parents=[
 ('p1',sp.Matrix([1,0,0]),sp.Matrix([0,1,z])),
 ('p2',sp.Matrix([0,1,0]),sp.Matrix([1,0,z])),
 ('p3',sp.Matrix([-z,0,1]),sp.Matrix([1,0,z])),
]
Dp=z**2+2*z+2; Dm=z**2-2*z+2
first=[
 ('g1',sp.Matrix([-1,-1,0]),sp.Matrix([0,0,-2*z])),
 ('g2',sp.Matrix([1+z,0,-1]),sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])),
 ('g3',sp.Matrix([1-z,0,1]),sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])),
]
for name,k,v in parents+first:
    q=qform(v)
    assert_sign_on_interval(q,z,lo,hi,1,f'{name}: inherited form positive')
    assert_sign_on_interval(sp.factor(-M*q-k.dot(k)),z,lo,hi,-1,
                            f'{name}: inherited viscous rate negative at M=2048')

# The all-orders inherited-parent ladder r_n=(-n,-1,0) has polarization e3.
# Here e3.H.e3=1/200, so every n>=1 is strictly damped for every M>0.
n=sp.symbols('n',integer=True,positive=True)
e3=sp.Matrix([0,0,1]); rn=sp.Matrix([-n,-1,0])
ladder=sp.factor(-M*qform(e3)-rn.dot(rn))
check(ladder==-sp.Rational(256,25)-n**2-1,'exact M=2048 ladder rate')
check(ladder.subs(n,1)<0,'ladder rate already negative at n=1')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('At the positive clean root, H with M=2048 grows all intended second targets and damps rejected parts, original parents, first-generation carriers, and the full inherited ladder.')
print('Scope: instantaneous affine/Kelvin carrier separation only; autonomous strain generation and finite-time geometry control remain open.')
