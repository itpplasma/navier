#!/usr/bin/env python3
"""Complete phase-graded source-reference factor-two relay through t^3.

Prediction before test: the unavoidable cubic pollutant occupies physical phase
grade m, whereas the desired doubled parents occupy grade 2m.  Track the phase
grade as an exact extra integer through every linear and quadratic term and
check the complete quartic 2m target coefficients.
"""
from __future__ import annotations
import math
import sympy as s

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def C(p,a,q,b):
    p,a,q,b=map(s.Matrix,(p,a,q,b))
    return s.simplify(P(p+q)*((a.dot(q))*b+(b.dot(p))*a))
def eigcoords(k,f):
    k,f=s.Matrix(k),s.Matrix(f); c=s.simplify(k[0]/k[2]); q=s.sqrt(1+c*c)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)
def sqrt_bounds(n,D=10**8):
    m=math.isqrt(int(n)*D*D)
    return s.Rational(m,D),s.Rational(m+1,D)
def radical_interval(expr,D=10**8):
    lo=hi=s.Rational(0)
    for term in s.Add.make_args(s.expand(s.radsimp(expr))):
        coeff,rest=term.as_coeff_Mul()
        if rest==1:
            lo+=coeff; hi+=coeff; continue
        if isinstance(rest,s.Pow) and rest.exp==s.Rational(1,2) and rest.base.is_Integer:
            a,b=sqrt_bounds(int(rest.base),D)
            if coeff>=0: lo+=coeff*a; hi+=coeff*b
            else: lo+=coeff*b; hi+=coeff*a
        else:
            raise AssertionError(f'nonlinear radical term: {term}')
    return s.factor(lo),s.factor(hi)

mu=s.Rational(3,5)
c=s.Rational(1,20); da=s.Rational(9,20); db=s.Rational(3,20)
tilts=[c+da,c-da,c+db,c-db]
parents=[s.Matrix([x,0,1]) for x in tilts]
pols=[ap(x) for x in tilts]
k=parents[0]+parents[1]
F_A=C(parents[0],pols[0],parents[1],pols[1])
F_B=C(parents[2],pols[2],parents[3],pols[3])
_,bAm=eigcoords(k,F_A); _,bBm=eigcoords(k,F_B)
wA=bBm; wB=-bAm

K0=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])
def keyvec(key): return s.Matrix([s.Rational(key[0],10),0,s.Integer(key[1])])
def proj_key(key):
    kk=keyvec(key); return s.eye(3)-kk*kk.T/kk.dot(kk)
def addkey(a,b): return (a[0]+b[0],a[1]+b[1])
def linear(key,v):
    kk=keyvec(key)
    A=-K0+kk*(kk.T*K0)/kk.dot(kk)
    return A*v-mu*kk.dot(kk)*v
def ordered_pair(kp,a,kq,b):
    kk=addkey(kp,kq)
    if kk==(0,0): return kk,s.zeros(3,1)
    q=keyvec(kq)
    return kk,-s.I*proj_key(kk)*(a.dot(q))*b

def addmat(D,key,val): D[key]=D.get(key,s.zeros(3,1))+val

def linear_dict(U):
    # state key is (x,z,grade); the physical source linear operator preserves grade.
    return {(x,z,g):linear((x,z),v) for (x,z,g),v in U.items()}

def nonlinear_dict(U,V):
    out={}
    for (xp,zp,gp),a in U.items():
        for (xq,zq,gq),b in V.items():
            kk,val=ordered_pair((xp,zp),a,(xq,zq),b)
            if kk!=(0,0): addmat(out,(kk[0],kk[1],gp+gq),val)
    return out

def combine(dicts,scale=s.Integer(1)):
    out={}
    for D in dicts:
        for key,val in D.items(): addmat(out,key,val)
    return {key:s.simplify(scale*val) for key,val in out.items() if val!=s.zeros(3,1)}

keys=[(5,1),(-4,1),(2,1),(-1,1)]
amplitudes=[s.Integer(1),wA,s.Integer(1),wB]
U0={}
for key,pol,amp in zip(keys,pols,amplitudes):
    U0[(key[0],key[1],1)]=amp*pol
    U0[(-key[0],-key[1],-1)]=amp*pol

jets=[U0]
for j in range(3):
    terms=[linear_dict(jets[j])]
    for ell in range(j+1):
        terms.append(nonlinear_dict(jets[ell],jets[j-ell]))
    jets.append(combine(terms,s.Rational(1,j+1)))

# Reality and transversality hold grade by grade.
for j,D in enumerate(jets):
    for (x,z,g),val in D.items():
        kv=keyvec((x,z))
        check(s.simplify((kv.T*val)[0])==0,f'order {j} {(x,z,g)} transverse')
        neg=(-x,-z,-g)
        check(neg in D and all(s.simplify(q)==0 for q in D[neg]-s.conjugate(val)),
              f'order {j} {(x,z,g)} reality partner')

# Complete quartic coefficients in the desired doubled physical phase grade 2m.
targets=[(10,2,2),(-8,2,2),(4,2,2),(-2,2,2)]
intervals=[]
for idx,t in enumerate(targets):
    check(t in jets[3],f'grade-2 doubled target {idx} present in complete U3')
    cp,_=eigcoords(keyvec(t[:2]),jets[3][t])
    realcoef=s.radsimp(-s.I*cp)
    lo,hi=radical_interval(realcoef)
    check(hi<0 or lo>0,f'grade-2 doubled target {idx} growing coordinate nonzero')
    intervals.append((idx,lo,hi))

# The known extreme cubic pollutant 14=5+5-(-4) has physical grade 1+1-1=1.
poll=(14,1,1)
check(poll in jets[2],'extreme cubic pollutant is in grade 1')
check((14,1,2) not in jets[2],'no cubic grade-2 component at pollutant frequency')
cp,_=eigcoords(keyvec(poll[:2]),jets[2][poll])
expected=-s.Rational(9,29600)*(-11+20*s.sqrt(370)+9*s.sqrt(2146))
check(s.simplify(cp-expected)==0,'phase-resolved pollutant coefficient matches frozen theorem')

# Exact combinatorial degree/grade lemma for base grades +/-1.
for d in range(1,17):
    grades={2*k-d for k in range(d+1)}
    check(all(abs(g)<=d and (d-g)%2==0 for g in grades),f'degree {d} grade parity/bound')
    for q in range(-d-2,d+3):
        reachable=(abs(q)<=d and (d-q)%2==0)
        check((q in grades)==reachable,f'degree {d} exact grade reachability q={q}')
for j in range(0,8):
    q=2**j
    for d in range(q):
        assert q not in {2*k-d for k in range(d+1)}
        CHECKS.append(f'grade {q} absent below degree {q}: d={d}')

print(f'PASS: {len(CHECKS)} exact assertions.')
for idx,lo,hi in intervals:
    print(f'phase-grade 2 child {idx} growing coefficient in [{lo}, {hi}]')
print('Cubic pollutant is phase grade 1; all four doubled-parent targets survive in grade 2 through the complete t^3 jet.')
print('A grade 2^j descendant cannot occur below amplitude degree 2^j from the original +/-m parents.')
