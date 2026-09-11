#!/usr/bin/env python3
"""Exact all-orders spectral cage for the four-parent source reference lattice."""
import sympy as s

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def C(p,a,q,b):
    p,a,q,b=map(s.Matrix,(p,a,q,b))
    return s.simplify(P(p+q)*((a.dot(q))*b+(b.dot(p))*a))
def ap(sig):
    return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); c=s.simplify(k[0]/k[2]); q=s.sqrt(1+c*c)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)

mu=s.Rational(3,5)
c=s.Rational(1,20); a=s.Rational(9,20); b=s.Rational(3,20)
tilts=[c+a,c-a,c+b,c-b]
check(tilts==[s.Rational(1,2),-s.Rational(2,5),s.Rational(1,5),-s.Rational(1,10)],
      'four parent tilts are exact lattice sites')
parents=[s.Matrix([x,0,1]) for x in tilts]
pols=[ap(x) for x in tilts]

# Two decompositions of one daughter; cancel its growing coordinate.
k=parents[0]+parents[1]
check(k==parents[2]+parents[3] and k==s.Matrix([s.Rational(1,10),0,2]),
      'designated pairs share target')
F1=C(parents[0],pols[0],parents[1],pols[1]); F2=C(parents[2],pols[2],parents[3],pols[3])
check(s.simplify(k.dot(F1))==0 and s.simplify(k.dot(F2))==0,
      'both Leray pair outputs are target-transverse')
bp1,bm1=eigcoords(k,F1); bp2,bm2=eigcoords(k,F2)
F=s.simplify(bp2*F1-bp1*F2); bp,bm=eigcoords(k,F)
check(bp==0,'target growing component cancels')
expected=81*(-3*s.sqrt(40501)-5*s.sqrt(2005)+2*s.sqrt(11629)+6*s.sqrt(10426))/8040050
check(s.simplify(bm-expected)==0 and bm>0,'target decaying component is nonzero positive')
aminus=s.Matrix([1,s.sqrt(s.Rational(401,400)),-s.Rational(1,20)])
check(all(s.simplify(x)==0 for x in F-bm*aminus),'target is pure negative eigenbranch')

# Linear positive-branch rate at k=z(s,0,1), lambda0=1.
def rate(z,ss):
    q=s.sqrt(1+ss*ss)
    return s.simplify(1/q-mu*z*z*q*q)
# Worst parent is |s|=1/2.
check(rate(1,s.Rational(1,2))>0,'all four parent positive branches grow')
# First new z=1 lattice site has |s|=7/10 and is already damped.
check(rate(1,s.Rational(7,10))<0,'nearest nonparent z=1 site is damped')
# Rate is strictly decreasing with |s| because q increases and 1/q-mu q^2 decreases.
q=s.symbols('q',positive=True)
check(s.diff(1/q-mu*q*q,q)<0,'positive-branch rate decreases with q')
# Any |z|>=2 mode is damped regardless of tilt: rate <=1-mu z^2 <=1-12/5.
check(1-4*mu<0,'every |z|>=2 lattice mode is linearly damped')

# Parent radial numerators in tenths are all -1 modulo 3:
# p_j=((3m_j-1)/10,0,1), m_j=-1,0,1,2.
ms=[-1,2,1,0]  # order matching tilts above: 1/2,-2/5,1/5,-1/10
for tilt,m in zip(tilts,ms):
    check(tilt==s.Rational(3*m-1,10),f'parent m={m} lies in affine lattice')
# Closure under addition is algebraic:
m1,m2,z1,z2=s.symbols('m1 m2 z1 z2',integer=True)
x1=s.Rational(1,10)*(3*m1-z1); x2=s.Rational(1,10)*(3*m2-z2)
check(s.expand(x1+x2-s.Rational(1,10)*(3*(m1+m2)-(z1+z2)))==0,
      'k_(m,z) lattice closed under convolution')
# For z=1 the tilt sites are (3m-1)/10. Exactly m=-1,0,1,2 lie between -1/2 and 1/2;
# outside them |s|>=7/10 (left) or 4/5 (right).
for m in (-1,0,1,2):
    check(abs(s.Rational(3*m-1,10))<=s.Rational(1,2),f'unstable parent site m={m}')
check(abs(s.Rational(3*(-2)-1,10))==s.Rational(7,10),'left next z=1 site is -7/10')
check(s.Rational(3*3-1,10)==s.Rational(4,5),'right next z=1 site is 4/5')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('The convolution lattice is k_(m,z)=((3m-z)/10,0,z).')
print('Its only linearly growing nonzero modes are the positive branches of the four parent sites and their reality partners.')
print('Scope: frozen source-reference linear spectrum plus exact convolution-frequency closure.')
