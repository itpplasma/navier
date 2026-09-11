#!/usr/bin/env python3
"""Exact common-strain discrimination of all three clean second targets.

One rational trace-free symmetric strain has negative quadratic form on every
intended second-target polarization and positive form on each transverse
orthogonal direction.  At strength 10*nu*b^2 it beats viscosity on all desired
carriers at the isolated positive clean-circuit root.

This is carrier algebra/instantaneous rate information.  It is not by itself a
finite-time mixture purifier or a regenerative turnover.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def nozero_sign(expr,z,a,b,sgn,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    check(p.count_roots(a,b)==0,f'{label}: no numerator zero in clean-root interval')
    check(sp.sign(p.eval(a))==sgn,f'{label}: exact endpoint sign')
    check(den.subs(z,(a+b)/2)>0,f'{label}: denominator positive calibration')

z=sp.symbols('z',real=True)
Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
a=sp.Rational(12847,10000); b=sp.Rational(803,625)
check(Q.eval(a)<0 and Q.eval(b)>0 and Q.count_roots(a,b)==1,'unique positive clean root isolated')

S=sp.Matrix([
 [sp.Rational(9,8), sp.Rational(1,36), sp.Rational(1,4)],
 [sp.Rational(1,36),sp.Rational(-1,5), sp.Rational(1,14)],
 [sp.Rational(1,4), sp.Rational(1,14),sp.Rational(-37,40)],
])
check(S==S.T,'common strain symmetric')
check(sp.trace(S)==0,'common strain trace free')

def k_of(h): return sp.Matrix([h[0]-z*h[2],h[1],h[2]])
def v_of(h):
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
for h in targets:
    k=k_of(h); v=v_of(h); f=sp.simplify(k.cross(v))
    check(sp.simplify(k.dot(v))==0,f'{h}: intended vector transverse')
    check(sp.simplify(k.dot(f))==0 and sp.simplify(v.dot(f))==0,f'{h}: rejected direction transverse orthogonal')
    qv=sp.factor((v.T*S*v)[0])
    qf=sp.factor((f.T*S*f)[0])
    nozero_sign(qv,z,a,b,-1,f'{h}: intended strain form negative')
    nozero_sign(qf,z,a,b, 1,f'{h}: orthogonal strain form positive')
    # For affine strain 10*nu*b^2*S and physical wavevector b*k, divide the
    # logarithmic amplitude-energy rate by nu*b^2.  Positivity is equivalent
    # to -10 v.S.v-|k|^2|v|^2>0.
    grow=sp.factor(-10*qv-k.dot(k)*v.dot(v))
    nozero_sign(grow,z,a,b,1,f'{h}: desired rate positive at strength 10')
    # Rejected rate is automatically strictly negative because qf>0.

print(f'PASS: {len(CHECKS)} exact assertions.')
print('At the positive clean root, one rational S simultaneously grows all three intended second-target polarizations and damps all three transverse orthogonal directions at strength 10.')
print('Scope: exact common affine rate discriminator; finite-energy mixed-packet persistence and recursion remain to prove.')
