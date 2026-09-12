#!/usr/bin/env python3
"""Exact six-mode half-grade bridge into the next four source parents."""
import math
import sympy as s

mu=s.Rational(3,5)
K0=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])

def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def keyvec(key): return s.Matrix([s.Rational(key[0],10),0,s.Integer(key[1])])
def proj_key(key):
    k=keyvec(key); return s.eye(3)-k*k.T/k.dot(k)
def addkey(a,b): return (a[0]+b[0],a[1]+b[1])
def linear(key,v):
    k=keyvec(key); A=-K0+k*(k.T*K0)/k.dot(k)
    return A*v-mu*k.dot(k)*v
def ordered_pair(kp,a,kq,b):
    kk=addkey(kp,kq)
    if kk==(0,0): return kk,s.zeros(3,1)
    q=keyvec(kq)
    return kk,-s.I*proj_key(kk)*(a.dot(q))*b
def add(D,k,v): D[k]=D.get(k,s.zeros(3,1))+v
def linear_dict(U): return {k:linear(k,v) for k,v in U.items()}
def nonlinear_dict(U,V):
    out={}
    for kp,a in U.items():
        for kq,b in V.items():
            kk,val=ordered_pair(kp,a,kq,b)
            if kk!=(0,0): add(out,kk,val)
    return out
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); sig=s.simplify(k[0]/k[2]); q=s.sqrt(1+sig*sig)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)
def C(p,a,q,b):
    p,a,q,b=map(s.Matrix,(p,a,q,b))
    return s.simplify(P(p+q)*((a.dot(q))*b+(b.dot(p))*a))
def halfvec(x): return s.Matrix([s.Rational(x,20),0,s.Rational(1,2)])
def halfpol(x): return ap(s.Rational(x,10))
def rate(z,sig):
    q2=1+sig*sig
    return s.simplify(1/s.sqrt(q2)-mu*z*z*q2)
def sqrt_bounds(n,D=10**9):
    m=math.isqrt(int(n)*D*D)
    return s.Rational(m,D),s.Rational(m+1,D)
def radical_interval(expr,D=10**9):
    lo=hi=s.Rational(0)
    expr=s.expand(s.radsimp(expr))
    for term in s.Add.make_args(expr):
        coeff,rest=term.as_coeff_Mul()
        if rest==1:
            lo+=coeff; hi+=coeff; continue
        if isinstance(rest,s.Pow) and rest.exp==s.Rational(1,2) and rest.base.is_Integer:
            a,b=sqrt_bounds(int(rest.base),D)
            if coeff>=0: lo+=coeff*a; hi+=coeff*b
            else: lo+=coeff*b; hi+=coeff*a
            continue
        raise AssertionError((expr,term,coeff,rest))
    return s.factor(lo),s.factor(hi)
def nonzero_interval(expr):
    lo,hi=radical_interval(expr)
    assert hi<0 or lo>0, (expr,lo,hi)
    return lo,hi

# Recompute both unavoidable cubic extremes from pair A in the complete Taylor
# coefficient U2.  This extends the frozen +14 control by checking the mirror
# -13 channel explicitly.
k1=(5,1); k2=(-4,1)
U0={k1:ap(s.Rational(1,2)), k2:ap(-s.Rational(2,5))}
U0[(-5,-1)]=U0[k1]; U0[(4,-1)]=U0[k2]
tmp={}
for k,v in linear_dict(U0).items(): add(tmp,k,v)
for k,v in nonlinear_dict(U0,U0).items(): add(tmp,k,v)
U1={k:s.simplify(v) for k,v in tmp.items()}
tmp={}
for k,v in linear_dict(U1).items(): add(tmp,k,v)
for A,B in ((U0,U1),(U1,U0)):
    for k,v in nonlinear_dict(A,B).items(): add(tmp,k,v)
U2={k:s.simplify(v/2) for k,v in tmp.items()}
extreme={}
for target in ((14,1),(-13,1)):
    cp,_=eigcoords(keyvec(target),U2[target])
    cp=s.simplify(cp)
    nonzero_interval(cp)
    extreme[target[0]]=cp

# Both extreme cubic frequencies are unique monomials in the complete positive
# four-parent set, hence neither can be removed by the other designated pair.
xs=[5,-4,2,-1]
for target,expected in ((14,{(0,0,1)}),(-13,{(1,1,0)})):
    reps=set()
    for i,x in enumerate(xs):
        for j,y in enumerate(xs):
            for h,z in enumerate(xs):
                if x+y-z==target: reps.add((i,j,h))
    assert reps==expected,(target,reps)

# At the next normalization the six relevant ancestors are z=1/2 modes with
# tilts x/10.  The two extremes are themselves linearly growing there.
for x in (14,-13,5,-4,2,-1):
    r=rate(s.Rational(1,2),s.Rational(x,10))
    assert r>0,(x,r)

# Exact grade-changing quadratic edges.  Half-grade keys a,b produce the next
# z=1 parent K when a+b=2K.  Check the full Leray growing coordinate at every
# required target; no selected unprojected numerator is used.
edges=[
    (14,-4,5),   # hard p1
    (-13,5,-4),  # hard p2
    (5,-1,2),    # easy p3
    (-4,2,-1),   # easy p4
]
coeff={}
for a,b,K in edges:
    assert a+b==2*K
    out=halfvec(a)+halfvec(b)
    target=s.Matrix([s.Rational(K,10),0,1])
    assert out==target,(a,b,K,out,target)
    F=C(halfvec(a),halfpol(a),halfvec(b),halfpol(b))
    cp,_=eigcoords(target,F)
    cp=s.simplify(cp)
    coeff[K]=cp
    nonzero_interval(cp)

# The leading target map from six complex ancestor amplitudes is
# (c1*x14*x-4, c2*x-13*x5, c3*x5*x-1, c4*x-4*x2).
# With x5,x-4 fixed nonzero, its Jacobian in the four remaining variables is
# diagonal with nonzero entries, hence rank four.  Thus arbitrary nearby
# nonzero target quartet coefficients can be tuned at leading quadratic order.
x14,xm13,x5,xm4,x2,xm1=s.symbols('x14 xm13 x5 xm4 x2 xm1', nonzero=True)
F=s.Matrix([
    coeff[5]*x14*xm4,
    coeff[-4]*xm13*x5,
    coeff[2]*x5*xm1,
    coeff[-1]*xm4*x2,
])
vars=s.Matrix([x14,xm13,xm1,x2])
J=F.jacobian(vars)
assert s.simplify(J.det()-coeff[5]*coeff[-4]*coeff[2]*coeff[-1]*xm4**2*x5**2)==0
assert s.simplify(J.det())!=0

print('PASS: exact six-mode half-grade bridge has four independent quadratic next-parent channels.')
print('Both cubic extremes +14 and -13 are nonzero and linearly growing at z=1/2.')
for K in (5,-4,2,-1):
    lo,hi=nonzero_interval(coeff[K])
    print(f'next parent key {K}: growing quadratic coefficient in [{lo}, {hi}]')
print('The leading four-target Jacobian has rank four once the shared x5 and x-4 ancestors are nonzero.')
print('Scope: frozen/local algebra with six freely available half-grade ancestors; late causal supply and full physical finite-duration persistence remain open.')
