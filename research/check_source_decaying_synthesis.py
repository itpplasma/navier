#!/usr/bin/env python3
"""Exact four-growing-parent synthesis of a pure decaying source eigenbranch.

This freezes the reference-frame algebra and exact rate inequalities.  It is a
first-quadratic-order source-prehistory module, not a closed NS turnover.
"""
import sympy as s

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def C(p,a,q,b):
    p,q,a,b=map(s.Matrix,(p,a,q,b))
    return s.simplify(P(p+q)*((a.dot(q))*b+(b.dot(p))*a))

def ap(sig):
    q=s.sqrt(1+sig*sig)
    return s.Matrix([1,-q,-sig]) # c0=-1 growing branch

def eigcoords(k,f):
    # k=b(c,0,1), f transverse. a_+=(1,-q,-c), a_-=(1,+q,-c)
    k=s.Matrix(k); f=s.Matrix(f)
    c=s.simplify(k[0]/k[2]); q=s.sqrt(1+c*c)
    bp=s.simplify((f[0]-f[1]/q)/2)
    bm=s.simplify((f[0]+f[1]/q)/2)
    return bp,bm

# One common reference background: lambda0=1, viscous coefficient mu=6/25.
mu=s.Rational(6,25)
tilts=[s.Rational(11,10),s.Rational(-9,10),s.Rational(7,20),s.Rational(-3,20)]
parents=[s.Matrix([x,0,1]) for x in tilts]
pols=[ap(x) for x in tilts]
for j,(p,a) in enumerate(zip(parents,pols)):
    check(s.simplify(p.dot(a))==0,f'parent {j} transverse')

# Designated pairs have the same target k=(1/5,0,2), c=1/10.
k=parents[0]+parents[1]
check(k==parents[2]+parents[3] and k==s.Matrix([s.Rational(1,5),0,2]),
      'two decompositions share target')
F1=C(parents[0],pols[0],parents[1],pols[1])
F2=C(parents[2],pols[2],parents[3],pols[3])
bp1,bm1=eigcoords(k,F1); bp2,bm2=eigcoords(k,F2)
check(bp1>0 and bp2>0,'both designated pairs have positive growing coordinate')

# Weight pair products by bp2 and -bp1.  Growing target coordinate cancels.
F=s.simplify(bp2*F1-bp1*F2)
bp,bm=eigcoords(k,F)
check(s.simplify(bp)==0,'target growing eigencomponent cancels exactly')
# Strict convexity q''>0 implies the minus/plus ratio grows with symmetric
# pair half-separation d.  Here d=1 versus d=1/4, so bm is nonzero.  Freeze the
# exact radical as an additional algebra check.
expected=5*(-2*s.sqrt(41309)-s.sqrt(22321)+s.sqrt(18281)+2*s.sqrt(45349))/20402
check(s.simplify(bm-expected)==0 and bm>0,'pure decaying target coefficient is strictly positive')
aminus=s.Matrix([1,s.sqrt(s.Rational(101,100)),-s.Rational(1,10)])
check(all(s.simplify(x)==0 for x in F-bm*aminus),'combined target is pure decaying eigenvector')

# Linear reference rate for b(c,0,1): + branch = 1/q(c)-mu*b^2*q(c)^2.
def plus_rate(b,c):
    q=s.sqrt(1+c*c)
    return s.simplify(1/q-mu*b*b*q*q)
# Parent rate is minimized at the largest |tilt|=11/10.
check(plus_rate(1,s.Rational(11,10))>0,'all four parents are linearly growing')
# Target positive branch at b=2,c=1/10 also grows; only the generated minus
# coordinate is selected at quadratic order.
check(plus_rate(2,s.Rational(1,10))>0,'target positive branch is available for later mixed-branch use')

# Every non-designated sum of distinct parents has b=2 and mean tilt in this set.
cross=[s.Rational(29,40),s.Rational(19,40),s.Rational(-11,40),s.Rational(-21,40)]
for c in cross:
    check(plus_rate(2,c)<0,f'cross-sum c={c} is linearly damped in both branches')
# All differences have axial component zero, hence no +/-lambda/q growth and
# strictly negative viscous rate for every nonzero difference.
for i in range(4):
    for j in range(i):
        d=parents[i]-parents[j]
        check(d[2]==0 and d.dot(d)>0,f'difference {j},{i} radial and viscously damped')
# Self-interactions vanish for transverse single Fourier modes.
for j in range(4):
    check(C(parents[j],pols[j],parents[j],pols[j])==s.zeros(3,1),f'parent {j} self interaction zero')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Four growing source parents synthesize a pure decaying target; every other first quadratic output is linearly damped.')
print('Scope: reference principal geometry through first quadratic order only.')
