#!/usr/bin/env python3
"""Discriminate the earliest doubled-parent degree and its frequency-scale law."""
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

# Exact full quadratic coefficient from the four positive parents at each
# doubled positive target. Reality partners cannot contribute to z=+2.
quad=[]
for j,target in enumerate([2*p for p in parents]):
    out=s.zeros(3,1)
    decomps=[]
    for i,p in enumerate(parents):
        for l,q in enumerate(parents):
            if p+q==target:
                decomps.append((i,l))
                out += amps[i]*amps[l]/2 * C(p,pols[i],q,pols[l])
    cp,_=eigcoords(target,s.simplify(out))
    quad.append(s.simplify(cp))
    print('target',j,'quadratic decompositions',decomps,'growing=',s.simplify(cp))

# The prediction that all four targets first occur at quartic degree is false
# precisely if any dual-tuned quadratic growing coefficient survives.
nonzero=[j for j,x in enumerate(quad) if s.simplify(x)!=0]
print('nonzero quadratic growing targets:',nonzero)

# Uniform frequency scaling alpha leaves projectors and polarizations unchanged
# and makes each Leray bilinear interaction exactly homogeneous of degree one.
a=s.symbols('alpha', positive=True)
for i in range(4):
    for j in range(4):
        lhs=C(a*parents[i],pols[i],a*parents[j],pols[j])
        rhs=a*C(parents[i],pols[i],parents[j],pols[j])
        assert all(s.simplify(x)==0 for x in lhs-rhs)

# Grade arithmetic: z=2 admits only even amplitude degree. If the degree-2
# coefficient vanishes at a target, any time-order-3 degree-4 contribution
# uses exactly three quadratic vertices and therefore scales alpha^3.
for d in range(1,5):
    grades={2*r-d for r in range(d+1)}
    assert ((2 in grades)==(d>=2 and d%2==0))

print('PASS: exact quadratic target audit and bilinear frequency homogeneity.')
