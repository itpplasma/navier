#!/usr/bin/env python3
"""Exact second-time-derivative pollution for the clean dyadic gate.

The calculation is for the original Fourier Navier--Stokes quadratic term.
It proves that first-derivative cleanliness does not give a closed history.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)
def zero(v):
    if isinstance(v,sp.MatrixBase): return all(sp.simplify(x)==0 for x in v)
    return sp.simplify(v)==0
def proj(k,v): return sp.simplify(v-k*k.dot(v)/k.dot(k))

z=sp.symbols('z',real=True)
c1,c2,c3,d1,d2,d3=sp.symbols('c1 c2 c3 d1 d2 d3')
K=[sp.Matrix([1,0,0]),sp.Matrix([0,1,0]),sp.Matrix([-z,0,1])]
A=[sp.Matrix([0,1,z]),sp.Matrix([1,0,z]),sp.Matrix([1,0,z])]

def phys(n):
    return sum((sp.Integer(n[j])*K[j] for j in range(3)),sp.zeros(3,1))

def bilin(U,V):
    out={}
    for n,u in U.items():
        p=phys(n)
        for m,v in V.items():
            r=tuple(n[j]+m[j] for j in range(3))
            if r==(0,0,0): continue
            q=phys(m); k=p+q
            term=-sp.I*proj(k,(u.dot(q))*v)
            if zero(term): continue
            out[r]=sp.simplify(out.get(r,sp.zeros(3,1))+term)
    return {r:v for r,v in out.items() if not zero(v)}

U0={
 (1,0,0):c1*A[0], (-1,0,0):d1*A[0],
 (0,1,0):c2*A[1], (0,-1,0):d2*A[1],
 (0,0,1):c3*A[2], (0,0,-1):d3*A[2],
}
U1=bilin(U0,U0)

selected1={(-1,-1,0),(1,0,-1),(1,0,1)}
selected1 |= {tuple(-x for x in n) for n in selected1}
check(set(U1)==selected1,'first nonlinear derivative has only the six selected/conjugate children')

# New support at second derivative is DN(U0)[U1].  The linear viscous term
# cannot contribute to a mode absent from both U0 and U1, so the coefficient
# below is viscosity-independent.
L=bilin(U0,U1); R=bilin(U1,U0)
target=(-2,-1,0)
second=sp.simplify(L.get(target,sp.zeros(3,1))+R.get(target,sp.zeros(3,1)))
expected=sp.Matrix([0,0,-2*d1**2*d2*z])
check(second==expected,'exact unique parent-child pollution coefficient')
check(target not in set(U0) and target not in set(U1),'pollution mode is genuinely new at second derivative')

# There is a unique support decomposition target=(-e1)+(-e1-e2), so no phase
# cancellation with another parent-child path is available.
decomps=[]
for n in U0:
    for m in U1:
        if tuple(n[j]+m[j] for j in range(3))==target:
            decomps.append((n,m))
check(decomps==[((-1,0,0),(-1,-1,0))],'unique parent-child support decomposition')

Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
check(Q.eval(sp.Rational(32,25))<0 and Q.eval(sp.Rational(129,100))>0,
      'positive projective-return root exists')
check(sp.gcd(Q,sp.Poly(z,z)).degree()==0,'every projective-return root is nonzero')

# Hence for any clean projective circuit root and nonzero first two parent
# amplitudes, the second-time-derivative pollutant cannot vanish.
print(f'PASS: {len(CHECKS)} exact assertions.')
print('u_ddot[-2 e1-e2](0) = (0,0,-2 d1^2 d2 z); nonzero on every Q-root for d1 d2 != 0.')
print('Scope: exact local Fourier jet obstruction only; no statement about localized routing or blowup.')
