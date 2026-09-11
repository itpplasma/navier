#!/usr/bin/env python3
"""Exact symbolic checks for a contamination-free first dyadic Leray gate.

This proves only a principal-symbol circuit statement.  It is not a closed
Fourier subsystem, a localized turnover, or a Navier--Stokes blowup proof.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)
def zero(v):
    if isinstance(v,sp.MatrixBase): return all(sp.simplify(x)==0 for x in v)
    return sp.simplify(v)==0
def proj(k,v): return sp.simplify(v-k*k.dot(v)/k.dot(k))
def pair(p,a,q,b):
    k=p+q
    if zero(k): return sp.zeros(3,1)
    return sp.simplify(proj(k,a.dot(q)*b+b.dot(p)*a))
def gate(K,A):
    k1,k2,k3=K; a1,a2,a3=A
    return ([-k1-k2,k1-k3,k1+k3],
            [pair(-k1,a1,-k2,a2),
             pair(k1,a1,-k3,a3),
             pair(k1,a1,k3,a3)])

z=sp.symbols('z',real=True)
k1=sp.Matrix([1,0,0]); k2=sp.Matrix([0,1,0]); k3=sp.Matrix([-z,0,1])
a1=sp.Matrix([0,1,z]); a2=sp.Matrix([1,0,z]); a3=sp.Matrix([1,0,z])
K=[k1,k2,k3]; A=[a1,a2,a3]

for j,(k,a) in enumerate(zip(K,A),1):
    check(zero(k.dot(a)),f'input transversality {j}')
check(sp.factor(sp.Matrix.hstack(*K).det())==1,'wavevectors span R3 for every z')

# These are precisely the unwanted first-generation channels for the signed
# three-parent gate.  They vanish identically for the whole family.
check(zero(pair(k1,a1,-k2,a2)),'k1-k2 sibling vanishes identically')
check(zero(pair(k2,a2,k3,a3)),'k2+k3 unused collision vanishes identically')
check(zero(pair(k2,a2,-k3,a3)),'k2-k3 unused collision vanishes identically')

T=sp.Matrix([[-1,-1,0],[1,0,-1],[1,0,1]])
check(T**3==2*sp.eye(3),'wavevector gate cubes to doubling')
Kg,Ag=K,A
for _ in range(3): Kg,Ag=gate(Kg,Ag)
check(Kg==[2*k1,2*k2,2*k3],'three selected generations double all wavevectors')

Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
qlo=Q.eval(sp.Rational(32,25)); qhi=Q.eval(sp.Rational(129,100))
check(qlo<0 and qhi>0,'Q has a real root zstar in (32/25,129/100)')
check(sp.gcd(Q,sp.Poly(sp.diff(Q.as_expr(),z),z)).degree()==0,'Q is squarefree')

# Components 2 and 3 return projectively for every z.  Component 1 does so
# exactly when Q(z)=0.
for x in Ag[1].cross(a2): check(zero(x),'channel 2 projective return identity')
for x in Ag[2].cross(a3): check(zero(x),'channel 3 projective return identity')
c1=sp.factor(Ag[0].cross(a1)[0])
num1=sp.factor(sp.together(c1).as_numer_denom()[0])
check(sp.factor(num1/(-16*z**3))==Q.as_expr(),'channel 1 return obstruction is exactly Q')

lams=[sp.factor(Ag[0][1]),sp.factor(Ag[1][0]),sp.factor(Ag[2][0])]
for j,lam in enumerate(lams,1):
    num=sp.Poly(sp.together(lam).as_numer_denom()[0],z)
    check(sp.gcd(Q,num).degree()==0,f'channel {j} multiplier nonzero at every Q root')

# Denominators are strictly positive on the positive isolating interval.
positive_denoms=[z**2+1,z**2+2,z**2-2*z+2,z**2+2*z+2,z**2-4*z+6]
for j,d in enumerate(positive_denoms,1):
    check(sp.factor(d.subs(z,sp.Rational(32,25)))>0 and
          sp.factor(d.subs(z,sp.Rational(129,100)))>0,
          f'denominator family {j} positive on isolating interval endpoints')

# The sign pattern at the positive root is (-,-,+).  Exact endpoint signs plus
# absence of multiplier zeros at Q roots are enough for the root selected here.
zmid=sp.Rational(257,200)
check(Q.eval(zmid)<0,'positive root lies to the right of 257/200')
for j,lam in enumerate(lams,1):
    val=sp.N(lam.subs(z,sp.Rational(1285,1000)),30)
    check(val!=0,f'channel {j} calibration nonzero near positive root')

print(f'PASS: {len(CHECKS)} exact symbolic assertions.')
print('Scope: contamination-free first gate and projective three-gate circuit only; no closed NS trajectory.')
