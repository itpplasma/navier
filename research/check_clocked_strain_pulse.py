#!/usr/bin/env python3
"""Exact three-layer heat-Duhamel pulse for the autonomous common strain.

For each prescribed low child, three separated high-high pump pairs use
carrier radii R,2R,3R and source weights (5,-32,27). The weights cancel both
the instantaneous low source at t=0 and the slow low-frequency heat tail. The
remaining second-Picard low coefficient is a positive high-frequency pulse.
"""
from fractions import Fraction as F
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def scale(c,x): return tuple(c*a for a in x)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def norm2(x): return dot(x,x)
def cross(x,y):
    return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def proj(k,v): return sub(v,scale(dot(k,v)/norm2(k),k))
def pair(p,a,q,b):
    k=add(p,q)
    return proj(k,add(scale(dot(a,q),b),scale(dot(b,p),a)))

e1=(F(1),F(0),F(0)); e2=(F(0),F(1),F(0)); e3=(F(0),F(0),F(1))
H=((F(71,100),F(-1),F(147,200)),
   (F(-1),F(-143,200),F(7,25)),
   (F(147,200),F(7,25),F(1,200)))
A=F(143,400); B=F(-1,400)
modes=[
    (e2,scale(F(-1,2),e1)), (e1,scale(F(-1,2),e2)),
    (e3,scale(F(147,400),e1)), (e1,scale(F(147,400),e3)),
    (e3,scale(F(7,50),e2)), (e2,scale(F(7,50),e3)),
    (add(e1,e2),scale(A/2,sub(e1,e2))),
    (sub(e1,e2),scale(A/2,add(e1,e2))),
    (add(e1,e3),scale(B/2,sub(e1,e3))),
    (sub(e1,e3),scale(B/2,add(e1,e3))),
]
M=[[F(0) for _ in range(3)] for _ in range(3)]
for k,d in modes:
    check(dot(k,d)==0,"low mode transverse")
    for i in range(3):
        for j in range(3): M[i][j]+=d[i]*k[j]
for i in range(3):
    for j in range(3): check(2*M[i][j]==H[i][j],f"H synthesis {i}{j}")

# If D_m=m^2 D, these weights cancel both the initial source and the slow tail.
weights={1:F(5),2:F(-32),3:F(27)}
check(sum(weights.values())==0,"initial low source cancels")
check(sum(weights[m]/F(m*m) for m in (1,2,3))==0,"slow low heat tail cancels")

# For z=exp(-nu D t), the surviving pulse is strictly one-signed for t>0.
z=sp.symbols("z")
pulse=5*z-8*z**4+3*z**9
positive=z*(z-1)**2*(3*z**6+6*z**5+9*z**4+12*z**3+15*z**2+10*z+5)
check(sp.expand(pulse-positive)==0,"positive pulse factorization")
x=sp.symbols("x")
series=sp.series(5*sp.exp(-x)-8*sp.exp(-4*x)+3*sp.exp(-9*x),x,0,4).removeO()
check(sp.expand(series-60*x**2+280*x**3)==0,"quadratic pulse onset")

# Thirty pump pairs. R_j differ slightly to prevent cross-family cancellations;
# layers m=1,2,3 retain exact decay-gap ratio 1:4:9.
pumps=[]; centers=[]
for j,(kappa,d) in enumerate(modes):
    r=cross(kappa,d); nz=[v for v in r if v]
    check(len(nz)==1,f"mode {j} has axial cross direction")
    rho=abs(nz[0]); Rj=F(1_000_000+1000*j)
    for m in (1,2,3):
        N=F(m)*Rj/rho
        p=scale(N,r); q=sub(kappa,p); a=d
        b=add(scale(F(1,1)/norm2(kappa),kappa),scale(F(1,1)/(N*norm2(r)),r))
        check(add(p,q)==kappa,f"{j}/{m} frequency closure")
        check(dot(a,p)==0 and dot(a,q)==0,f"{j}/{m} a transverse")
        check(dot(b,q)==0 and dot(b,p)==1,f"{j}/{m} b transverse/normalized")
        check(pair(p,a,q,b)==d,f"{j}/{m} exact child")
        D=norm2(p)+norm2(q)-norm2(kappa)
        check(D==2*F(m*m)*Rj*Rj,f"{j}/{m} exact decay gap")
        pumps.append((j,m,kappa,d,p,a,q,b,D))
        for tag,k,pol in (("p",p,a),("q",q,b)):
            centers.append((j,m,tag,+1,k,pol))
            centers.append((j,m,tag,-1,scale(F(-1),k),pol))

low=[]; high=[]
for i in range(len(centers)):
    for j in range(i,len(centers)):
        ci,cj=centers[i],centers[j]
        s=add(ci[4],cj[4]); ns=norm2(s)
        if ns<=16:
            low.append((ci,cj,s))
            if ns==0:
                check(ci[0]==cj[0] and ci[1]==cj[1] and ci[2]==cj[2] and ci[3]==-cj[3],
                      "zero low center only same carrier conjugate")
            else:
                check(ci[0]==cj[0] and ci[1]==cj[1] and ci[2]!=cj[2] and ci[3]==cj[3],
                      "nonzero low center only matched same-layer pump")
                check(s==scale(F(ci[3]),modes[ci[0]][0]),"nonzero low center equals signed kappa")
        else: high.append(ns)
check(len(low)==120,"exactly 120 low centers for 30 reality-compatible pumps")
check(min(high)==F(1_000_000),"all other quadratic centers have |xi|>=1000")

print(f"PASS: {len(CHECKS)} exact assertions.")
print("Pulse identity: weights (5,-32,27) cancel onset and slow low heat tail.")
print("Residual factor: z(1-z)^2 times a positive polynomial, hence one-signed for t>0.")
print("Thirty pump pairs retain an exact spectral moat: every other nonzero center has |xi|>=1000.")
print("Scope: exact symbol + second-Picard heat-Duhamel timing; full nonlinear pulse integration remains separate.")
