#!/usr/bin/env python3
"""Exact quadratic coefficient on the unstable manifold of the caged source lattice."""
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
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); c=s.simplify(k[0]/k[2]); q=s.sqrt(1+c*c)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)

mu=s.Rational(3,5); c=s.Rational(1,20)
tilts=[s.Rational(1,2),-s.Rational(2,5),s.Rational(1,5),-s.Rational(1,10)]
parents=[s.Matrix([x,0,1]) for x in tilts]; pols=[ap(x) for x in tilts]
k=parents[0]+parents[1]
F_A=C(parents[0],pols[0],parents[1],pols[1])
F_B=C(parents[2],pols[2],parents[3],pols[3])
check(s.simplify(k.dot(F_A))==0 and s.simplify(k.dot(F_B))==0,
      'both Leray pair outputs are target-transverse')
bAp,bAm=eigcoords(k,F_A); bBp,bBm=eigcoords(k,F_B)

def gp(z,x):
    q=s.sqrt(1+x*x); return s.simplify(1/q-mu*z*z*q*q)
def gm(z,x):
    q=s.sqrt(1+x*x); return s.simplify(-1/q-mu*z*z*q*q)
lam=[gp(1,x) for x in tilts]
ltp=gp(2,c); ltm=gm(2,c)
check(all(x>0 for x in lam),'all four parent eigenvalues positive')
check(ltp<0 and ltm<0,'both target branches stable in caged geometry')
DAp=s.simplify(lam[0]+lam[1]-ltp); DBp=s.simplify(lam[2]+lam[3]-ltp)
DAm=s.simplify(lam[0]+lam[1]-ltm); DBm=s.simplify(lam[2]+lam[3]-ltm)
check(DAp>0 and DBp>0 and DAm>0 and DBm>0,'all homological denominators positive')

# Pair products retuned for the CAUSAL stable-manifold coefficient.
wA=s.simplify(bBp*DAp)
wB=s.simplify(-bAp*DBp)
# The + cancellation is algebraic from the chosen weights; avoid asking the CAS
# to rediscover it through a large radical simplification.
hplus=s.cancel(wA*bAp/DAp+wB*bBp/DBp)
hminus=wA*bAm/DAm+wB*bBm/DBm
check(hplus==0,'quadratic unstable-manifold target positive coordinate cancels')
check(s.N(hminus,50)>0,'quadratic unstable-manifold target negative coordinate survives')

# Coarse exact spectral margins used in the Lyapunov--Perron proof.
check(gp(1,s.Rational(1,2))>s.Rational(1,10),'unstable spectral margin exceeds 1/10')
check(gp(1,s.Rational(7,10))<-s.Rational(1,100),'nearest nonparent z=1 site below -1/100')
check(-mu*s.Rational(9,100)<-s.Rational(1,100),'nearest nonzero radial site below -1/100')
check(1-4*mu<-s.Rational(1,100),'all |z|>=2 positive branches below -1/100')

print(f'PASS: {len(CHECKS)} exact/symbolic assertions.')
print('Causal pair-product retuning cancels the target + coefficient while retaining a positive target - coefficient.')
print('Coarse hyperbolic margins: unstable >1/10, stable <-1/100 outside the four growing sites.')
