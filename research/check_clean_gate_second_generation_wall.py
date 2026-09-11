#!/usr/bin/env python3
"""Exact co-located second-generation ancestry wall for the clean dyadic gate.

The nominal second selected target h=(-2,-1,-1) first appears in the top
homogeneous Taylor coefficient at time order three.  Its intended child-child
polarization is contaminated at the same degree/order by inherited-parent
trees.  This checker freezes the two exact vectors and proves nonparallelism
at every projective-return root.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

z=sp.symbols('z',real=True)
Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)

# Pure selected child-child contribution to the t^3 Taylor coefficient at
# lattice target h=(-2,-1,-1), with the common leaf monomial suppressed.
pure=sp.Matrix([
 -2*sp.I*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
 -2*sp.I*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
 -2*sp.I*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
])

# All old-parent/second-jet contributions at the same target, degree and
# Taylor order, again with the same leaf monomial suppressed.
other=sp.Matrix([
 -sp.I*(5*z**10-32*z**9+89*z**8-120*z**7+67*z**6-12*z**5+159*z**4-396*z**3+412*z**2-176*z+20)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 -sp.I*(4*z**7-31*z**6+85*z**5-132*z**4+89*z**3-3*z**2-42*z+10)/(3*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
 -sp.I*(5*z**11-42*z**10+145*z**9-204*z**8-151*z**7+1108*z**6-1901*z**5+1324*z**4+374*z**3-1326*z**2+872*z-140)/(6*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)*(z**2-2*z+3)),
])

cross=sp.simplify(pure.cross(other))
P=sp.Poly(3*z**12-26*z**11+141*z**10-530*z**9+1481*z**8-3066*z**7+4547*z**6-4418*z**5+2024*z**4+896*z**3-1908*z**2+1048*z-160,z)
expected1=-z*P.as_expr()/(9*(z**2-4*z+5)*(z**2-4*z+6)*(z**2-2*z+2)**2*(z**2-2*z+3))
check(sp.factor(cross[1]-expected1)==0,'cross-product component freezes to obstruction polynomial')
check(sp.gcd(Q,P).degree()==0,'return polynomial and ancestry obstruction are coprime')
check(sp.gcd(Q,sp.Poly(z,z)).degree()==0,'return roots have z nonzero')

# Target h has L1 norm four, so a degree-four ancestry has exactly the unique
# leaf multiset 2*(-e1)+(-e2)+(-e3).  Finite enumeration freezes that fact.
h=(-2,-1,-1)
sol=[]
for p1 in range(5):
 for m1 in range(5-p1):
  for p2 in range(5-p1-m1):
   for m2 in range(5-p1-m1-p2):
    for p3 in range(5-p1-m1-p2-m2):
     m3=4-p1-m1-p2-m2-p3
     if (p1-m1,p2-m2,p3-m3)==h:
      sol.append((p1,m1,p2,m2,p3,m3))
check(sol==[(0,2,0,1,0,1)],'unique degree-four leaf multiset at target')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('At every Q-root, the intended second-gate polarization and inherited-parent contribution are nonparallel.')
print('Scope: top homogeneous co-located Fourier Taylor coefficient; routing/nonlinear auxiliary-state escapes remain open.')
