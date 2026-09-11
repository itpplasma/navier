#!/usr/bin/env python3
"""Exact leading stable-preload repair of the mixed-order factor-two relay."""
import math
import sympy as s


def kv(k): return s.Matrix([s.Rational(k[0],10),0,s.Integer(k[1])])
def proj(k):
    x=kv(k); return s.eye(3)-x*x.T/x.dot(x)
def addk(a,b): return (a[0]+b[0],a[1]+b[1])
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def Bpair(kp,a,kq,b):
    kk=addk(kp,kq)
    if kk==(0,0): return kk,s.zeros(3,1)
    return kk,-s.I*proj(kk)*(a.dot(kv(kq)))*b
def add(D,k,v):
    if k!=(0,0): D[k]=D.get(k,s.zeros(3,1))+v
def Bdict(U,V):
    out={}
    for kp,a in U.items():
        for kq,b in V.items():
            kk,v=Bpair(kp,a,kq,b)
            add(out,kk,v)
    return out
def combine(*Ds,scale=s.Integer(1)):
    out={}
    for D in Ds:
        for k,v in D.items(): add(out,k,scale*v)
    return out
def eigp(k,f):
    x=kv(k); c=x[0]/x[2]; q=s.sqrt(1+c*c)
    return (f[0]-f[1]/q)/2

def P(x):
    x=s.Matrix(x); return s.eye(3)-x*x.T/x.dot(x)
def C(p,a,q,b):
    p,a,q,b=map(s.Matrix,(p,a,q,b))
    return P(p+q)*((a.dot(q))*b+(b.dot(p))*a)
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); c=k[0]/k[2]; q=s.sqrt(1+c*c)
    return (f[0]-f[1]/q)/2,(f[0]+f[1]/q)/2

def sqrt_bounds(n,D=10**9):
    m=math.isqrt(int(n)*D*D)
    return s.Rational(m,D),s.Rational(m+1,D)
def radical_interval(expr,D=10**9):
    expr=s.expand(s.radsimp(expr))
    lo=hi=s.Rational(0)
    for term in s.Add.make_args(expr):
        coeff,rest=term.as_coeff_Mul()
        if rest==1:
            lo+=coeff; hi+=coeff; continue
        assert isinstance(rest,s.Pow) and rest.exp==s.Rational(1,2) and rest.base.is_Integer, term
        a,b=sqrt_bounds(int(rest.base),D)
        if coeff>=0: lo+=coeff*a; hi+=coeff*b
        else: lo+=coeff*b; hi+=coeff*a
    return s.factor(lo),s.factor(hi)

c=s.Rational(1,20); da=s.Rational(9,20); db=s.Rational(3,20)
tilts=[c+da,c-da,c+db,c-db]
keys=[(5,1),(-4,1),(2,1),(-1,1)]
pols=[ap(t) for t in tilts]
parents=[kv(k) for k in keys]
k=parents[0]+parents[1]
FA=C(parents[0],pols[0],parents[1],pols[1])
FB=C(parents[2],pols[2],parents[3],pols[3])
_,bAm=eigcoords(k,FA); _,bBm=eigcoords(k,FB)
wA=bBm; wB=-bAm
amps=[s.Integer(1),wA,s.Integer(1),wB]

# Parent field P1 carries amplitude degree one.  Its pure quadratic derivative
# supplies the leading easy births.
P1={}
for key,pol,amp in zip(keys,pols,amps):
    P1[key]=amp*pol
    P1[(-key[0],-key[1])]=amp*pol
U1=Bdict(P1,P1)
easy=[(4,2),(-2,2)]
q3=s.cancel(eigp(easy[0],U1[easy[0]]))
q4=s.cancel(eigp(easy[1],U1[easy[1]]))
assert q3!=0 and q4!=0

# For a stage of duration T, preload the stable positive branch at each easy
# target by -T*q_j*epsilon^2.  The endpoint easy growing coordinate therefore
# cancels at order epsilon^2 T exactly.
S={}
for ek,tilt,q in [(easy[0],tilts[2],q3),(easy[1],tilts[3],q4)]:
    b=-q
    S[ek]=b*ap(tilt)
    S[(-ek[0],-ek[1])]=s.conjugate(b)*ap(tilt)
    assert s.simplify(eigp(ek,S[ek])+q)==0

# These are genuinely stable current-stage modes: their z=2 positive-branch
# rates are strictly negative.
mu=s.Rational(3,5)
def rate(z,sig): return 1/s.sqrt(1+sig*sig)-mu*z*z*(1+sig*sig)
assert rate(2,tilts[2])<0 and rate(2,tilts[3])<0

# Leading hard degree-four/time-cubic coefficient without preloads.
# Since hard grade 2 has zero degree-two self-pair birth, the degree-four t^3
# coefficient contains only three quadratic vertices; linear terms cannot enter.
U2=combine(Bdict(P1,U1),Bdict(U1,P1),scale=s.Rational(1,2))
U3=combine(Bdict(P1,U2),Bdict(U1,U1),Bdict(U2,P1),scale=s.Rational(1,3))

# A preload is epsilon^2*T*S.  Its first possible hard-grade effect uses one
# preload plus two parents and two quadratic vertices.  It therefore contributes
# at exactly epsilon^4*T^3 through the degree-(2+1+1) part of U2.
UPS=combine(Bdict(P1,S),Bdict(S,P1))
U2corr=combine(Bdict(P1,UPS),Bdict(S,U1),Bdict(U1,S),Bdict(UPS,P1),scale=s.Rational(1,2))

hard=[(10,2),(-8,2)]
intervals=[]
for hk in hard:
    h0=eigp(hk,U3[hk])
    hc=eigp(hk,U2corr.get(hk,s.zeros(3,1)))
    total=s.radsimp(-s.I*(h0+hc))
    lo,hi=radical_interval(total)
    assert hi<0 or lo>0, (hk,lo,hi)
    intervals.append((hk,lo,hi))

# Phase/grade arithmetic explains why there is no lower hard contamination:
# parent grades are +/-1, preload grades +/-2.  A single preload plus one
# parent has odd grade; two preloads have grade 0 or +/-4.  Grade 2 at degree
# four first re-enters through one preload and two parents as computed above.
for gp in (-1,1):
    for gs in (-2,2):
        assert gp+gs in (-3,-1,1,3)
for a in (-2,2):
    for b in (-2,2):
        assert a+b in (-4,0,4)

print('PASS: exact stable-preload repair survives in both hard channels.')
print('The O(epsilon^2 T) stable easy-target counterterms cancel the leading easy endpoint births.')
for hk,lo,hi in intervals:
    print(f'corrected hard target {hk} epsilon^4*T^3 growing coefficient in [{lo}, {hi}]')
print('Both corrected hard coefficients remain strictly nonzero.')
print('Analytic endpoint dependence and D_preload F(0,0)=I then give an IFT family canceling the easy targets exactly on sufficiently short stages.')
print('Scope: frozen/local stage with freely supplied stable counterterms; recursive/global supply of those counterterms is still open.')
