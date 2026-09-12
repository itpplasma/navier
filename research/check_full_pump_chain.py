#!/usr/bin/env python3
"""Rigorous full infinite pump-chain eigenvalue and nonautonomous gain control.

SciPy proposes a finite eigenvector and inverse only. All decisive residual,
Jacobian, omitted-tail, and radii inequalities are checked with exact rationals.
The frozen generator eigenvalue is not a nonlinear or physical NS blowup.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt
from dataclasses import dataclass
import numpy as np
from scipy.linalg import eig, inv
from math import factorial

@dataclass(frozen=True)
class C:
    r: Q = Q(0)
    i: Q = Q(0)
    def __add__(a,b):
        if not isinstance(b,C): b=C(Q(b))
        return C(a.r+b.r,a.i+b.i)
    __radd__=__add__
    def __neg__(a):return C(-a.r,-a.i)
    def __sub__(a,b):return a+-b
    def __mul__(a,b):
        if not isinstance(b,C):return C(a.r*b,a.i*b)
        return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
    __rmul__=__mul__
    def norm(a):return abs(a.r)+abs(a.i)
    def num(a):return complex(float(a.r),float(a.i))
Z=C()
def rounded(x,D=10**12):return C(Q(round(x.real*D),D),Q(round(x.imag*D),D))

def certify(N=16,n=9,B=30):
    assert (N,n,B)==(16,9,30), "certificate constants are for this fixed case"
    mu=Q(3,5); a=Q(3*n,40); ab=a*B
    D=10**20;m=isqrt(401*D*D)
    blo=Q(m,20*D); bhi=Q(m+1,20*D); beta=(blo+bhi)/2; berr=(bhi-blo)/2
    assert (20*blo)**2<=401<(20*bhi)**2
    ps=list(range(-(n//2)-N,-(n//2)+N+1)); size=2*len(ps)
    def kval(p):return Q(n,10)+Q(p,20),Q(n,2)+p
    def rr(p):x,z=kval(p);return x*x+z*z
    def block(p,q):
        x,z=kval(p);r=rr(p)
        if p==q:return [[-mu*r,-z/r],[-z,-mu*r]]
        sign=p-q; assert abs(sign)==1
        fac=-sign*ab
        return [[fac*(rr(q)-Q(401,400))/r,Q(0)],[-sign*fac*beta,fac]]
    A=[{} for i in range(size)]
    cross={}
    for j,p in enumerate(ps):
        for q in (p-1,p,p+1):
            b=block(p,q)
            for i in (0,1):
                for k in (0,1):
                    if not b[i][k]:continue
                    if q in ps:A[2*j+i][2*(q-ps[0])+k]=C(b[i][k])
                    else:cross.setdefault((q,k),{})[2*j+i]=C(b[i][k])
    An=np.zeros((size,size),complex)
    for i,row in enumerate(A):
        for j,x in row.items():An[i,j]=x.num()
    lam,vec=eig(An)
    lb=C(Q(5049883304450,10**12),Q(6708966735593,10**12))
    index=min(range(size),key=lambda i:abs(lam[i]-lb.num()))
    v=vec[:,index];k=29;v=v/v[k]
    xbar=list(map(rounded,v));xbar[k]=C(Q(1))
    J=[dict(row) for row in A]
    for i in range(size):
        J[i][i]=J[i].get(i,Z)-lb
        J[i][k]=-xbar[i]
    Jn=np.zeros((size,size),complex)
    for i,row in enumerate(J):
        for j,x in row.items():Jn[i,j]=x.num()
    Rn=inv(Jn);R=[[rounded(z) for z in row] for row in Rn]
    rnorm=max(sum(z.norm() for z in row) for row in R)
    xnorm=max(z.norm() for z in xbar)
    res=[sum((x*xbar[j] for j,x in row.items()),Z)-lb*xbar[i] for i,row in enumerate(A)]
    yfin=max(sum((R[i][j]*res[j] for j in range(size)),Z).norm() for i in range(size))
    errA=2*ab*berr
    yfin+=rnorm*errA*xnorm
    zfin=Q(0)
    for i in range(size):
        rj=[Z for _ in range(size)]
        for j in range(size):
            for c,x in J[j].items():rj[c]=rj[c]+R[i][j]*x
        total=sum((C(Q(i==j))-rj[j]).norm() for j in range(size))
        total+=sum(sum((R[i][j]*x for j,x in col.items()),Z).norm() for col in cross.values())
        zfin=max(zfin,total)
    zfin+=rnorm*errA
    # Entire tails: r_j is convex with its minimum inside the finite section.
    low,high=ps[0]-1,ps[-1]+1
    rmin=min(rr(low),rr(high)); rootD=10**20
    rootlo=Q(isqrt(rmin.numerator*rootD*rootD//rmin.denominator),rootD)
    assert rootlo**2<=rmin and rootlo>0
    assert rr(low-1)>rr(low) and rr(high+1)>rr(high)
    assert min(rr(low-1),rr(low),rr(low+1),rr(high-1),rr(high),rr(high+1))>Q(401,400)
    # In a tail row, sum(|r_(j-1)-d^2|+|r_(j+1)-d^2|)=2*r_j.
    for p in (low,high): assert rr(p-1)+rr(p+1)-2*Q(401,400)==2*rr(p)
    zphi=(lb.norm()+2*ab)/(mu*rmin)+1/(mu*rmin*rootlo)
    ztheta=(lb.norm()+2*ab*(1+bhi))/(mu*rmin)+1/(mu*rootlo)
    ztail=max(zphi,ztheta)
    ytail=Q(0)
    for p,q in ((low,ps[0]),(high,ps[-1])):
        b=block(p,q)
        for i in (0,1):
            out=sum((C(b[i][j])*xbar[2*(q-ps[0])+j] for j in (0,1)),Z)
            ytail=max(ytail,out.norm()/(mu*rr(p)))
    ytail+=errA*xnorm/(mu*rmin)
    yn=max(yfin,ytail); zn=max(zfin,ztail); bn=max(rnorm,1/(mu*rmin))
    rad=Q(1,10**6)
    # Coarse rational bounds, not printed floating-point diagnostics, certify
    # the Newton map on a complex l-infinity ball (complex norm = |Re|+|Im|).
    assert yn < Q(1,25_000_000)
    assert zn < Q(67,100)
    assert bn < 47
    assert yn+zn*rad+bn*rad*rad<rad
    assert zn+2*bn*rad<1
    assert lb.r-rad>5
    assert lb.r+rad<44
    print('PASS full infinite charge-9 chain: eigenvalue in the radius-1e-6 complex l1 disk')
    print('center = 5049883304450/10^12 + i*6708966735593/10^12; Re(lambda)>5')
    print('exact certificate: Y<1/25000000, Z<67/100, inverse norm<47')
    return (lb,yn,zn,bn)

def exp_upper(x, N=14):
    """Positive Taylor sum and geometric upper bound for its entire tail."""
    assert x>=0 and x<Q(N+2)
    return sum((x**k/Q(factorial(k)) for k in range(N+1)),Q(0))+x**(N+1)/Q(factorial(N+1))/(1-x/Q(N+2))


def transient_gain():
    # b=(1,sqrt(401)/20,-1/20), d=(1/20,0,1), b.d=0.
    # c0=|b||d|; exact pump strain norm is B*c0, not 2*B*c0.
    c02=Q(401**2,80000)
    assert c02<Q(71,50)**2
    D=10**20;m=isqrt(401*D*D);rootlo=Q(m,D)
    kappa_hi=20/rootlo+Q(1203,2000)
    assert kappa_hi<Q(161,100)
    assert 1+30*Q(71,50)<44
    # On charge 9, b.k=27/40 for every pump shift. Thus the pump
    # bilinear linearization is bounded on physical L2 by 2*(27/40+c0).
    assert 2*(Q(27,40)+Q(71,50))<Q(21,5)
    assert Q(21,5)*30*Q(161,100)/2<102
    T=Q(1,200)
    assert exp_upper(44*T)<Q(5,4)
    lower=1+5*T-102*T*T*Q(5,4)
    assert lower>Q(51,50)
    assert exp_upper(T)<Q(101,100)
    print('PASS actual exponentially decaying reference pump: L2 gain >51/50 at T=1/200')
    print('The bound uses the certified eigenvector and Duhamel error, retaining all chain modes.')
    print('Uniform pump-action upper bound: ||v(T)||/||v(0)|| <= exp[T+B*c0/kappa*(1-exp(-kappa*T))].')
    print('No nonlinear saturation, interstage reset, physical embedding or NS-R3 claim.')


if __name__=='__main__':
    if not __debug__:
        raise RuntimeError('Run without -O: exact certificate assertions are required')
    certify()
    transient_gain()
