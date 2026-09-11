#!/usr/bin/env python3
"""Exact symbolic checks for the inherited-parent Fourier ladder.

This certifies the carrier identity behind the all-orders Taylor-tree argument.
It does not certify a localized packet cascade or finite-time blowup.
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
def pair(p,a,q,b): return sp.simplify(proj(p+q,(a.dot(q))*b+(b.dot(p))*a))

z=sp.symbols('z',real=True)
n=sp.symbols('n',integer=True,positive=True)
k1=sp.Matrix([1,0,0]); k2=sp.Matrix([0,1,0])
a1=sp.Matrix([0,1,z]); a2=sp.Matrix([1,0,z]); e3=sp.Matrix([0,0,1])

base=pair(-k1,a1,-k2,a2)
check(base==-2*z*e3,'first clean child is exactly -2 z e3')

rn=-n*k1-k2
step=pair(-k1,a1,rn,e3)
check(step==-e3,'every inherited-parent ladder step has constant Leray factor -e3')

# At Taylor order n the homogeneous degree is n+1.  A sum of n+1 initial
# lattice leaves equal to (-n,-1,0) is forced to consist of exactly n copies
# of -e1 and one copy of -e2: any positive e1 or any +/-e3 pair would exceed
# the leaf budget.  The finite check below freezes that combinatorial fact.
for N in range(1,13):
    sols=[]
    # counts (p1,m1,p2,m2,p3,m3), total N+1
    for p1 in range(N+2):
      for m1 in range(N+2-p1):
       for p2 in range(N+2-p1-m1):
        for m2 in range(N+2-p1-m1-p2):
         for p3 in range(N+2-p1-m1-p2-m2):
          m3=N+1-p1-m1-p2-m2-p3
          if p1-m1==-N and p2-m2==-1 and p3-m3==0:
              sols.append((p1,m1,p2,m2,p3,m3))
    check(sols==[(0,N,0,1,0,0)],f'unique leaf multiset at order {N}')

Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
check(sp.gcd(Q,sp.Poly(z,z)).degree()==0,'projective-return roots have z nonzero')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('For r_n=-n k1-k2, the minimal Taylor-tree coefficient is 2 i^n z d1^n d2 e3.')
print('Scope: formal Fourier Taylor-tree ancestry only; no finite-energy or blowup claim.')
