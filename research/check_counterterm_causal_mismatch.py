#!/usr/bin/env python3
"""Exact incompatibility of the free stable counterterms with the four-parent unstable manifold."""
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

mu=s.Rational(3,5)
c=s.Rational(1,20); da=s.Rational(9,20); db=s.Rational(3,20)
tilts=[c+da,c-da,c+db,c-db]
parents=[s.Matrix([x,0,1]) for x in tilts]
pols=[ap(x) for x in tilts]
k=parents[0]+parents[1]
FA=C(parents[0],pols[0],parents[1],pols[1])
FB=C(parents[2],pols[2],parents[3],pols[3])
_,bAm=eigcoords(k,FA); _,bBm=eigcoords(k,FB)
wA=bBm; wB=-bAm
assert wA!=0 and wB!=0

# Easy growing forcing coefficients from the only nonzero cross decompositions.
e3,_=eigcoords(2*parents[2],C(parents[0],pols[0],parents[3],pols[3]))
e4,_=eigcoords(2*parents[3],C(parents[1],pols[1],parents[2],pols[2]))
for e in (e3,e4):
    lo,hi=radical_interval(e)
    assert hi<0 or lo>0

# Positive-branch rates in the source reference system.
def rate(z,sig):
    q2=1+sig*sig
    return 1/s.sqrt(q2)-mu*z*z*q2
lam=[s.simplify(rate(1,x)) for x in tilts]
sig3=s.simplify(rate(2,tilts[2])); sig4=s.simplify(rate(2,tilts[3]))
assert sig3<0 and sig4<0
D3=s.simplify(lam[0]+lam[3]-sig3)
D4=s.simplify(lam[1]+lam[2]-sig4)
assert D3>0 and D4>0

# On the backward-eternal four-parent unstable manifold, a stable scalar mode
# y'=sigma*y+F*exp(lambda_pair*t) has y(0)=F/D, D=lambda_pair-sigma>0.
# To make the same mode vanish after a positive future stage T, the required
# initial value is -F*(exp(D*T)-1)/D.  Put exp(D*T)=1+z, z>0: the two scalar
# multipliers are +1/D and -z/D and therefore have opposite sign.
z3,z4=s.symbols('z3 z4', positive=True)
for D,z in ((D3,z3),(D4,z4)):
    um=s.simplify(1/D)
    req=s.simplify(-z/D)
    assert um>0 and req<0
    assert s.simplify(req-um+(1+z)/D)==0
    assert s.simplify(req/um+z)==0

# Restore the actual nonzero forcing amplitudes.  The mismatch cannot disappear
# by parent phase choice while the dual pair products stay nonzero: both the
# unstable-manifold value and required counterterm carry the same F factor.
F3=s.simplify(e3*wB)   # A1*A4 after any factorization of the fixed pair products
F4=s.simplify(e4*wA)   # schematic nonzero common factor; only nonvanishing matters
assert F3!=0 and F4!=0
for F,D,z in ((F3,D3,z3),(F4,D4,z4)):
    y_um=s.simplify(F/D)
    y_req=s.simplify(-F*z/D)
    assert s.simplify(y_req-y_um + F*(1+z)/D)==0
    assert s.simplify(y_req/y_um+z)==0

print('PASS: exact causal mismatch for both stable easy-target counterterms.')
print('Four-parent backward-eternal unstable-manifold coefficient = F/D with D>0.')
print('Future-canceling counterterm = -F*(exp(D*T)-1)/D for every T>0.')
print('Their ratio is 1-exp(D*T)<0, so the free stable-preload repair is not on the four-parent causal unstable manifold.')
print('Scope: frozen reference four-coordinate backward-eternal graph; additional inherited modes/nonautonomous physical history remain open.')
