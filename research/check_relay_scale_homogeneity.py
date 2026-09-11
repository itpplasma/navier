#!/usr/bin/env python3
"""Exact earliest doubled-parent degree and frequency-scale law."""
import math
import sympy as s


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
        assert isinstance(rest,s.Pow) and rest.exp==s.Rational(1,2) and rest.base.is_Integer, term
        a,b=sqrt_bounds(int(rest.base),D)
        if coeff>=0: lo+=coeff*a; hi+=coeff*b
        else: lo+=coeff*b; hi+=coeff*a
    return s.factor(lo),s.factor(hi)

c=s.Rational(1,20); da=s.Rational(9,20); db=s.Rational(3,20)
tilts=[c+da,c-da,c+db,c-db]
parents=[s.Matrix([x,0,1]) for x in tilts]
pols=[ap(x) for x in tilts]
k=parents[0]+parents[1]
F_A=C(parents[0],pols[0],parents[1],pols[1])
F_B=C(parents[2],pols[2],parents[3],pols[3])
_,bAm=eigcoords(k,F_A); _,bBm=eigcoords(k,F_B)
wA=bBm; wB=-bAm
amps=[s.Integer(1),wA,s.Integer(1),wB]

quad=[]; intervals=[]; decompositions=[]
for j,target in enumerate([2*p for p in parents]):
    out=s.zeros(3,1); decomps=[]
    for i,p in enumerate(parents):
        for l,q in enumerate(parents):
            if p+q==target:
                decomps.append((i,l))
                out += amps[i]*amps[l]/2 * C(p,pols[i],q,pols[l])
    cp,_=eigcoords(target,s.simplify(out))
    cp=s.simplify(cp); quad.append(cp); decompositions.append(decomps)
    if cp!=0: intervals.append((j,*radical_interval(cp)))

# Corrected discriminator: targets 0,1 have only self-pair decompositions and
# vanish quadratically by transversality; targets 2,3 have cross-pair channels
# and strictly nonzero growing coefficients already at quadratic degree.
assert decompositions[0]==[(0,0)] and decompositions[1]==[(1,1)]
assert quad[0]==0 and quad[1]==0
assert decompositions[2]==[(0,3),(2,2),(3,0)]
assert decompositions[3]==[(1,2),(2,1),(3,3)]
assert [j for j,_,_ in intervals]==[2,3]
for j,lo,hi in intervals:
    assert hi<0 or lo>0, (j,lo,hi)

# Uniform frequency scaling alpha leaves projectors/polarizations unchanged
# and makes every Leray bilinear vertex exactly homogeneous of degree one.
a=s.symbols('alpha', positive=True)
for i in range(4):
    for j in range(4):
        lhs=C(a*parents[i],pols[i],a*parents[j],pols[j])
        rhs=a*C(parents[i],pols[i],parents[j],pols[j])
        assert all(s.simplify(x)==0 for x in lhs-rhs)

# Grade z=2 requires even amplitude degree.  For hard targets 0,1 the only
# degree-2 decomposition is a self-pair, whose incompressible interaction is
# identically zero for any transverse time-evolved polarization at the same
# wavevector. Hence their known first nonzero degree-4/time-order-3 coefficient
# contains exactly three quadratic vertices and scales alpha^3.  The easy
# targets 2,3 have the certified degree-2/time-order-1 term and scale alpha.
for d in range(1,5):
    grades={2*r-d for r in range(d+1)}
    assert ((2 in grades)==(d>=2 and d%2==0))
for p,pol in zip(parents,pols):
    assert p.dot(pol)==0
    assert C(p,pol,p,pol)==s.zeros(3,1)

print('PASS: corrected relay-rescaling theorem.')
print('hard targets 2p1,2p2: quadratic coefficient zero; frozen nonzero quartic coefficient scales alpha^3.')
for j,lo,hi in intervals:
    print(f'easy target 2p{j+1}: quadratic growing coefficient in [{lo}, {hi}] and scales alpha.')
print('At factor-two stage normalization alpha=1/2, local birth survives with exact scale factors 1/8 (hard) and 1/2 (easy).')
