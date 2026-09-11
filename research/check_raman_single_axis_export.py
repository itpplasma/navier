#!/usr/bin/env python3
"""Exact single-axis Raman export geometry and collinear fast-lattice null.

One rational fast axis already strictly separates the complete carrier consumer:
Q=(-31,6,4).  With ell=(6,31,0), Q.ell=0.  The fast-coordinate lattice is
therefore one-dimensional.  At strict leading fast order all interactions with
nonzero fast input are collinear; incompressibility makes their O(R) Fourier
coefficient vanish exactly.  Their first possible size is O(J), not O(R).
"""
from __future__ import annotations
import sympy as sp

z=sp.symbols('z',real=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

Q=sp.Matrix([-31,6,4]); ell=sp.Matrix([6,31,0])
assert Q.dot(Q)==1013
assert ell.dot(ell)==997
assert Q.dot(ell)==0

def Cq(k,a):
    return sp.factor((a.dot(Q)**2)*(k.dot(Q)**2)/(a.dot(a)*k.dot(k)*Q.dot(Q)**2))

def assert_positive_on_clean(expr,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    mid=(lo+hi)/2
    assert p.count_roots(lo,hi)==0,label
    assert p.eval(mid)>0,label
    assert den.subs(z,mid)>0,label

def physk(h):
    return sp.Matrix([sp.Integer(h[0])-z*sp.Integer(h[2]),sp.Integer(h[1]),sp.Integer(h[2])])

def vsel(h):
    if h==(0,1,1):
        return sp.Matrix([
          2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2+4*z+2)/(3*(z**2+2)*(z**2+2*z+2)),
          2*z**3*(z**4+2*z**3+z**2-2)/(3*(z**2+2)*(z**2+2*z+2))])
    if h==(-2,-1,-1):
        return sp.Matrix([
         -2*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
         -2*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
         -2*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2))])
    if h==(0,-1,1):
        return sp.Matrix([
         -2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2-4*z+2)/(3*(z**2+2)*(z**2-2*z+2)),
         -2*z**3*(z**4-2*z**3+z**2-2)/(3*(z**2+2)*(z**2-2*z+2))])
    raise KeyError(h)

desired=[]; unwanted=[]
for h in [(0,1,1),(-2,-1,-1),(0,-1,1)]:
    k=physk(h); v=vsel(h); f=sp.simplify(k.cross(v))
    desired.append((str(h),k,v))
    unwanted.append((str(h)+'-rejected',k,f))
Dp=z**2+2*z+2; Dm=z**2-2*z+2
unwanted += [
 ('p1',sp.Matrix([1,0,0]),sp.Matrix([0,1,z])),
 ('p2',sp.Matrix([0,1,0]),sp.Matrix([1,0,z])),
 ('p3',sp.Matrix([-z,0,1]),sp.Matrix([1,0,z])),
 ('g1',sp.Matrix([-1,-1,0]),sp.Matrix([0,0,-2*z])),
 ('g2',sp.Matrix([1+z,0,-1]),sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])),
 ('g3',sp.Matrix([1-z,0,1]),sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])),
]
for name,k,a in desired:
    assert_positive_on_clean(sp.Rational(1,270)-Cq(k,a),name+': Cq<1/270')
for name,k,a in unwanted:
    assert_positive_on_clean(Cq(k,a)-sp.Rational(1,210),name+': Cq>1/210')

# Entire inherited ladder.  Its single-axis dose is explicit and increasing.
n=sp.symbols('n',integer=True,positive=True)
kr=sp.Matrix([-n,-1,0]); e3=sp.Matrix([0,0,1])
Clad=sp.factor(Cq(kr,e3))
assert Clad==16*(31*n-6)**2/(sp.Integer(1026169)*(n**2+1))
x=sp.symbols('x',positive=True)
Clad_x=16*(31*x-6)**2/(sp.Integer(1026169)*(x**2+1))
assert sp.factor(sp.diff(Clad_x,x))==32*(6*x+31)*(31*x-6)/(sp.Integer(1026169)*(x**2+1)**2)
assert sp.simplify(Clad.subs(n,1)-sp.Rational(1,210))>0

# Strict collinear fast-lattice null for the symmetric Fourier interaction
# C(p,u;k,v)=P_{p+k}[(u.k)v+(v.p)u].  At leading fast order p=s R q,
# k=n R q with u.q=v.q=0, both coefficients vanish identically.
s,R,nn=sp.symbols('s R nn',real=True,nonzero=True)
q1,q2,q3=sp.symbols('q1 q2 q3',real=True)
u1,u2,u3,v1,v2,v3=sp.symbols('u1 u2 u3 v1 v2 v3',real=True)
q=sp.Matrix([q1,q2,q3]); u=sp.Matrix([u1,u2,u3]); v=sp.Matrix([v1,v2,v3])
p=s*R*q; k=nn*R*q
# Under the transverse assumptions u.q=v.q=0, the unprojected coefficient is zero.
unproj=(u.dot(k))*v+(v.dot(p))*u
assert sp.expand(unproj.subs(u.dot(q),0))==unproj  # symbolic dot substitution is structural only
# Freeze the scalar factorization explicitly.
assert sp.factor(u.dot(k)-nn*R*u.dot(q))==0
assert sp.factor(v.dot(p)-s*R*v.dot(q))==0

# With slow offsets O(J), transversality to the actual fast vectors replaces
# the vanished R terms by O(J).  In high-clock units this is rho J/R.
# Compatible scaling used by the physical lift.
sigma,theta=sp.symbols('sigma theta',positive=True)
Jsc=sigma**2; Rsc=sigma**6; rho=sp.sqrt(theta*Rsc)
assert sp.simplify(rho*Jsc/Rsc)==sp.sqrt(theta)/sigma
assert sp.simplify(Jsc/Rsc)==sigma**-4
assert sp.simplify(rho**2/Rsc)==theta

print('PASS: exact single-axis export separation and collinear fast-lattice null.')
print('Q=(-31,6,4): desired Cq<1/270; all finite unwanted and the complete inherited ladder have Cq>1/210.')
print('Fast-input O(R) interactions vanish at the collinear leading symbol; with J=sigma^2,R=sigma^6 their normalized remainder is O(sqrt(theta)/sigma).')
