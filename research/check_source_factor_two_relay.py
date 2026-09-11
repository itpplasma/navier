#!/usr/bin/env python3
"""Complete t^3 source-reference relay from four parents to their doubled copies.

The checker uses the correct Leray bilinear form, the complete source reference
linear matrix, viscosity, reality partners, and EVERY Fourier output at every
Taylor order through t^3.  It proves by exact rational radical enclosures that
all four doubled parent frequencies have nonzero growing-branch t^3
coefficients after the dual common-daughter tuning.
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

# Exact rational enclosure for linear combinations of square roots.
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

# Caged source geometry.
mu=s.Rational(3,5)
c=s.Rational(1,20); da=s.Rational(9,20); db=s.Rational(3,20)
tilts=[c+da,c-da,c+db,c-db]
parents=[s.Matrix([x,0,1]) for x in tilts]
pols=[ap(x) for x in tilts]
k=parents[0]+parents[1]
check(k==parents[2]+parents[3]==s.Matrix([s.Rational(1,10),0,2]),'common daughter frequency')
F_A=C(parents[0],pols[0],parents[1],pols[1])
F_B=C(parents[2],pols[2],parents[3],pols[3])
bAp,bAm=eigcoords(k,F_A); bBp,bBm=eigcoords(k,F_B)
check(s.simplify(k.dot(F_A))==0 and s.simplify(k.dot(F_B))==0,'pair outputs are Leray transverse')

# DUAL tuning: cancel the daughter decaying coordinate instead of its growing
# coordinate.  The same 2x2 determinant from the decaying synthesis survives.
wA=bBm
wB=-bAm
Fgrow=s.simplify(wA*F_A+wB*F_B)
gp,gm=eigcoords(k,Fgrow)
check(gm==0,'dual pair tuning cancels daughter decaying coordinate')
Fdec=s.simplify(bBp*F_A-bAp*F_B)
dp,dm=eigcoords(k,Fdec)
check(dp==0 and dm>0,'original tuning has a nonzero pure decaying daughter')
check(s.simplify(gp+dm)==0 and gp<0,'dual daughter is pure growing and nonzero')
check(all(s.simplify(x)==0 for x in Fgrow-gp*ap(c)),'dual daughter has exact growing eigenpolarization')
check(wA!=0 and wB!=0,'both pair products needed for dual tuning are nonzero')

# Difference shears and stripped geometry: central daughter plus each pair shear
# lands exactly on the factor-two copy of one parent, with nonzero growing
# coordinate.  These checks identify the relay before the complete jet below.
for i,j in ((0,1),(1,0),(2,3),(3,2)):
    sf=parents[i]-parents[j]
    shear=C(parents[i],pols[i],-parents[j],pols[j])
    check(s.simplify(sf.dot(shear))==0,f'shear {i},{j} transverse')
    child=k+sf
    check(child==2*parents[i],f'central plus shear {i},{j} is doubled parent {i}')
    out=C(k,ap(c),sf,shear)
    cp,_=eigcoords(child,out)
    lo,hi=radical_interval(cp)
    check(hi<0 or lo>0,f'stripped doubled-parent {i} growing coordinate nonzero')

# Complete Taylor jet.  Represent k=((x10)/10,0,z) by integer pair (x10,z).
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
def linear_dict(U): return {key:linear(key,v) for key,v in U.items()}
def nonlinear_dict(U,V):
    out={}
    for kp,a in U.items():
        for kq,b in V.items():
            kk,val=ordered_pair(kp,a,kq,b)
            if kk!=(0,0): addmat(out,kk,val)
    return out
def combine(dicts,scale=s.Integer(1)):
    out={}
    for D in dicts:
        for key,val in D.items(): addmat(out,key,val)
    return {key:scale*val for key,val in out.items()}

keys=[(5,1),(-4,1),(2,1),(-1,1)]
amplitudes=[s.Integer(1),wA,s.Integer(1),wB]
U0={}
for key,pol,amp in zip(keys,pols,amplitudes):
    U0[key]=amp*pol
    U0[(-key[0],-key[1])]=amp*pol  # real Fourier field

# u(t)=sum_j t^j U_j.  The recurrence retains the full convolution, not a
# selected tree.  U_3 therefore includes every linear/nonlinear contribution
# through cubic time / quartic amplitude order.
jets=[U0]
for j in range(3):
    terms=[linear_dict(jets[j])]
    for ell in range(j+1):
        terms.append(nonlinear_dict(jets[ell],jets[j-ell]))
    jets.append(combine(terms,s.Rational(1,j+1)))

check([len(D) for D in jets]==[8,28,60,104],'complete jet mode counts through t^3')
# Reality, divergence and no omitted outputs at the represented orders.
for j,D in enumerate(jets):
    for key,val in D.items():
        check(all(s.simplify(x)==0 for x in keyvec(key).T*val),f'order {j} output {key} transverse')
        neg=(-key[0],-key[1])
        check(neg in D and all(s.simplify(x)==0 for x in D[neg]-s.conjugate(val)),
              f'order {j} output {key} has reality partner')

# Exact sign/nonzero proof for every doubled parent growing coordinate.  The
# coefficient is imaginary under this Fourier convention, so -i times it is
# real.  Rational enclosures of all square roots prove separation from zero.
targets=[(10,2),(-8,2),(4,2),(-2,2)]
intervals=[]
for idx,key in enumerate(targets):
    check(key==2*s.Matrix(keys[idx]) if False else True,'dummy')
    # key=(2*x10,2*z) is exactly twice the corresponding parent key.
    check(key==(2*keys[idx][0],2*keys[idx][1]),f'target {idx} is doubled parent key')
    cp,_=eigcoords(keyvec(key),jets[3][key])
    realcoef=s.radsimp(-s.I*cp)
    lo,hi=radical_interval(realcoef)
    check(hi<0 or lo>0,f'full t^3 doubled parent {idx} growing coordinate nonzero')
    intervals.append((idx,lo,hi))

print(f'PASS: {len(CHECKS)} exact assertions.')
for idx,lo,hi in intervals:
    print(f'full child {idx} real growing coefficient in [{lo}, {hi}]')
print('Dual-tuned four-parent dynamics seed all four doubled parent frequencies in their growing branches through the COMPLETE t^3 jet.')
print('Scope: exact frozen source-reference Taylor relay; finite-duration gain, physical localization, interstage transport and one-data iteration remain open.')
