#!/usr/bin/env python3
"""Exact late half-grade regeneration from the complete dual-tuned cubic jet.

The returned current-stage z=1 modes become normalized z=1/2 after the
factor-two scale change.  This checker tests whether the unavoidable cubic
sidebands can then combine with surviving original parents to regenerate the
hard next-stage z=1 parents, and compares that mechanism with the easy
quadratic channels.
"""
import sympy as s

mu=s.Rational(3,5)
K0=s.Matrix([[0,1,0],[1,0,0],[0,0,0]])

def P(k):
    k=s.Matrix(k); return s.eye(3)-k*k.T/k.dot(k)
def ap(sig): return s.Matrix([1,-s.sqrt(1+sig*sig),-sig])
def C(p,a,q,b):
    p,a,q,b=map(s.Matrix,(p,a,q,b))
    return s.simplify(P(p+q)*((a.dot(q))*b+(b.dot(p))*a))
def keyvec(key): return s.Matrix([s.Rational(key[0],10),0,s.Integer(key[1])])
def proj_key(key):
    k=keyvec(key); return s.eye(3)-k*k.T/k.dot(k)
def addkey(a,b): return (a[0]+b[0],a[1]+b[1])
def linear(key,v):
    k=keyvec(key); A=-K0+k*(k.T*K0)/k.dot(k)
    return s.simplify(A*v-mu*k.dot(k)*v)
def ordered_pair(kp,a,kq,b):
    kk=addkey(kp,kq)
    if kk==(0,0): return kk,s.zeros(3,1)
    q=keyvec(kq)
    return kk,s.simplify(-s.I*proj_key(kk)*(a.dot(q))*b)
def add(D,k,v): D[k]=D.get(k,s.zeros(3,1))+v
def linear_dict(U): return {k:linear(k,v) for k,v in U.items()}
def nonlinear_dict(U,V):
    out={}
    for kp,a in U.items():
        for kq,b in V.items():
            kk,val=ordered_pair(kp,a,kq,b)
            if kk!=(0,0): add(out,kk,val)
    return out
def eigcoords_key(key,f):
    k=keyvec(key); c=s.simplify(k[0]/k[2]); q=s.sqrt(1+c*c)
    f=s.Matrix(f)
    return s.simplify((f[0]-f[1]/q)/2),s.simplify((f[0]+f[1]/q)/2)
def exact_nonzero(expr):
    expr=s.simplify(s.radsimp(expr))
    if expr==0: return False
    x=s.symbols('X')
    mp=s.Poly(s.minpoly(expr,x),x)
    return mp.eval(0)!=0

# Dual common-daughter tuning, as in the complete factor-two relay.
c=s.Rational(1,20); da=s.Rational(9,20); db=s.Rational(3,20)
tilts=[c+da,c-da,c+db,c-db]
keys=[(5,1),(-4,1),(2,1),(-1,1)]
parents=[keyvec(k) for k in keys]
pols=[ap(x) for x in tilts]
kstar=parents[0]+parents[1]
FA=C(parents[0],pols[0],parents[1],pols[1])
FB=C(parents[2],pols[2],parents[3],pols[3])
_,bAm=eigcoords_key((1,2),FA); _,bBm=eigcoords_key((1,2),FB)
wA=s.simplify(bBm); wB=s.simplify(-bAm)
assert wA!=0 and wB!=0
amps=[s.Integer(1),wA,s.Integer(1),wB]
U0={}
for key,pol,amp in zip(keys,pols,amps):
    U0[key]=s.simplify(amp*pol)
    U0[(-key[0],-key[1])]=s.simplify(amp*pol)

# Complete U1,U2 Taylor coefficients.
jets=[U0]
for j in range(2):
    tmp={}
    for k,v in linear_dict(jets[j]).items(): add(tmp,k,v)
    for ell in range(j+1):
        for k,v in nonlinear_dict(jets[ell],jets[j-ell]).items(): add(tmp,k,v)
    jets.append({k:s.simplify(v/s.Integer(j+1)) for k,v in tmp.items()})
U1,U2=jets[1],jets[2]
assert [len(U0),len(U1),len(U2)]==[8,28,60]

# The two extreme cubic z=1 pollutants required for hard late regeneration.
# They are reality-reflected pair-A extremes and are nonzero in the COMPLETE U2.
for key in ((14,1),(-13,1)):
    assert key in U2
    cp,_=eigcoords_key(key,U2[key])
    # Remove the universal i phase before exact algebraic nonzero certification.
    realcp=s.radsimp(-s.I*cp)
    assert exact_nonzero(realcp), (key,realcp)

# Late hard regeneration: after rescaling by 1/2, these interactions produce
# next-stage parents p1 and p2.  Scaling all wavevectors by 1/2 only multiplies
# C by 1/2, so nonvanishing can be checked in current-stage coordinates.
late_hard=[
    ((-4,1),(14,1),(10,2)),
    ((5,1),(-13,1),(-8,2)),
]
for parent_key,cubic_key,target in late_hard:
    out=C(keyvec(parent_key),U0[parent_key],keyvec(cubic_key),U2[cubic_key])
    cp,_=eigcoords_key(target,out)
    realcp=s.radsimp(s.I*cp)  # phase convention may differ by one i; exact zero is invariant
    assert exact_nonzero(realcp), (parent_key,cubic_key,target,realcp)

# Easy next parents are still born directly from two degree-one originals.
late_easy=[
    ((5,1),(-1,1),(4,2)),
    ((-4,1),(2,1),(-2,2)),
]
for p,q,target in late_easy:
    out=C(keyvec(p),U0[p],keyvec(q),U0[q])
    cp,_=eigcoords_key(target,out)
    assert exact_nonzero(s.radsimp(cp)), (p,q,target,cp)

# Frequency arithmetic: among the genuinely new positive-phase cubic z=1
# sidebands, no pair produces either hard doubled target.  A degree-one
# original parent is required at the first late hard-generation order.
original_x={5,-4,2,-1}
cubic_x=set()
for key,val in U2.items():
    if key[1]!=1 or key[0] in original_x: continue
    if all(s.simplify(x)==0 for x in val): continue
    cubic_x.add(key[0])
for target in (10,-8):
    assert not any(x+y==target for x in cubic_x for y in cubic_x), (target,cubic_x)
    assert any(x+y==target for x in original_x for y in cubic_x), (target,cubic_x)
# The two easy targets already have original-original decompositions.
assert 5+(-1)==4 and (-4)+2==-2

# Half-scale linear rate after factor-two normalization.  It is strictly
# decreasing in |s|.  The hard-producing extreme cubic sidebands have tilts
# 7/5 and -13/10, while the corresponding easy partners have 1/5 and -1/10.
def rate_half(sig):
    q2=1+sig*sig
    return s.simplify(1/s.sqrt(q2)-s.Rational(3,20)*q2)
q=s.symbols('q',positive=True)
f=1/q-s.Rational(3,20)*q*q
assert s.simplify(s.diff(f,q)) == -1/q**2-s.Rational(3,10)*q
assert abs(s.Rational(1,5)) < abs(s.Rational(7,5))
assert abs(s.Rational(1,10)) < abs(s.Rational(13,10))
assert rate_half(s.Rational(1,5)) > rate_half(s.Rational(7,5))
assert rate_half(-s.Rational(1,10)) > rate_half(-s.Rational(13,10))
# All four relevant half-scale ancestors are growing, so this is a genuine late
# nonlinear-generation mechanism, not passive stable cargo.
for sig in (s.Rational(-2,5),s.Rational(7,5),s.Rational(1,2),-s.Rational(13,10)):
    assert rate_half(sig)>0

print('PASS: exact half-grade late-regeneration discriminator.')
print('Both hard next parents have nonzero late original-parent × cubic-pollutant generation channels.')
print('The easy next parents remain nonzero original × original quadratic channels.')
print('Thus hard late birth is amplitude degree 4 while easy birth is degree 2 at the first returned-state level.')
print('Half-scale linear growth also favors the easy-producing small-|s| ancestors over the extreme cubic hard producers.')
print('Scope: complete cubic returned jet and first late bilinear generation; extra inherited modes, nonlinear saturation/interference and physical localization remain open.')
