#!/usr/bin/env python3
"""Exact hard/easy amplitude-balance obstruction for the four-parent relay."""
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
wA=s.simplify(bBm); wB=s.simplify(-bAm)
assert wA!=0 and wB!=0

# The easy doubled targets have only the cross-pair contributions that survive
# the self-pair incompressibility cancellation.
e3,_=eigcoords(2*parents[2],C(parents[0],pols[0],parents[3],pols[3]))
e4,_=eigcoords(2*parents[3],C(parents[1],pols[1],parents[2],pols[2]))
for e in (e3,e4):
    lo,hi=radical_interval(e)
    assert hi<0 or lo>0, (e,lo,hi)

A1,A2,A3,A4,E=s.symbols('A1 A2 A3 A4 E', nonzero=True)
Easy3=s.expand(e3*A1*A4)
Easy4=s.expand(e4*A2*A3)
assert s.simplify(Easy3*Easy4-e3*e4*(A1*A2)*(A3*A4))==0
fixed_product=s.simplify((Easy3*Easy4).subs(A2,wA*E**2/A1).subs(A4,wB*E**2/A3))
assert s.simplify(fixed_product-e3*e4*wA*wB*E**4)==0
assert s.simplify(e3*e4*wA*wB)!=0

# Linear positive-branch growth rate is strictly decreasing with |s| because
# f(x)=x^(-1/2)-(3/5)x has f'(x)<0 for x>0.  The easy tilts have smaller
# absolute value than both hard tilts, so every easy rate exceeds every hard rate.
mu=s.Rational(3,5)
def rate(sig): return 1/s.sqrt(1+sig*sig)-mu*(1+sig*sig)
r=[s.simplify(rate(x)) for x in tilts]
# Exact ordering can be certified by the monotone x=1+s^2 values.
x=[s.simplify(1+t*t) for t in tilts]
assert x[3] < x[2] < x[1] < x[0]
# SymPy can verify these radical comparisons exactly as well.
assert r[3] > r[2] > r[1] > r[0]
assert r[2] > r[1]  # slowest easy still beats fastest hard

print('PASS: exact four-parent hard/easy stage-balance obstruction.')
print('Dual pair products fix Easy3*Easy4 = const * epsilon^4 != 0; both easy channels cannot be suppressed together.')
print('For a balanced O(epsilon) parent class, at least one easy child is Omega(epsilon^2) while both hard first births are O(epsilon^4).')
print('All easy linear growth rates exceed all hard growth rates, so any common positive linear amplification interval worsens the imbalance.')
print('Scope: birth-then-linear-amplify four-parent stage map; genuinely nonlinear saturation/extra-mode interference remains open.')
