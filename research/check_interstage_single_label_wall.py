#!/usr/bin/env python3
"""Exact scale/action obstruction to extending one finite-L source label across a factor-two interstage interval."""
from fractions import Fraction

# The factor-two normalization interval from the frozen reference theorem.
# rho=2^(-2/h), so rho^(-h)=4 and integral q^(-1-h)dq = 3 Q^(-h)/h.
# On the exact admissible subsequence h=1/200, ell=400*k:
# Q=2^(-ell), Q^(-h)=4^k and L=ell^2.
h=Fraction(1,200)
rows=[]
for k in range(1,25):
    ell=400*k
    Qmh=4**k
    action=Fraction(3,1)*Qmh/h
    L=ell*ell
    tau=action/L
    rows.append((k,ell,action,tau))

# Exact formula tau_k = 3*4^k/(800 k^2), hence
# tau_(k+1)/tau_k = 4 k^2/(k+1)^2 >=16/9 for k>=2.
for k,ell,action,tau in rows:
    assert tau == Fraction(3*4**k,800*k*k)
for j in range(1,len(rows)-1):
    k=rows[j][0]
    ratio=rows[j+1][3]/rows[j][3]
    assert ratio == Fraction(4*k*k,(k+1)*(k+1))
    assert ratio >= Fraction(16,9)
assert rows[-1][3] > 10**6

# Exact finite-L lattice deformation from the existing theorem:
# T(k)-k=(tau*d(k), -eta*d(k), 0), d(k)=k_x-c*k_z.
# On the four parents c=1/20 and |d| is 9/20,9/20,3/20,3/20.
# Also |k|^2<=5/4, so (|d|/|k|)^2 >= (3/20)^2/(5/4)=9/500.
c=Fraction(1,20)
tilts=[Fraction(1,2),Fraction(-2,5),Fraction(1,5),Fraction(-1,10)]
for s in tilts:
    d=s-c
    k2=1+s*s
    ratio2=d*d/k2
    assert ratio2 >= Fraction(9,500)

# Thus |T k-k|^2/|k|^2 >= (9/500) tau^2. Since tau grows at least
# geometrically, the same-label lattice embedding leaves every fixed
# perturbative neighbourhood of the frozen cage.
for k,ell,action,tau in rows:
    lower2=Fraction(9,500)*tau*tau
    if k>=10:
        assert lower2>1

print('PASS: exact single-label factor-two interstage deformation leaves the finite-L perturbative regime.')
print('Required reference fast action = 3 Q^(-h)/h and tau=action/L grows geometrically on an exact admissible subsequence.')
print('For every caged parent, |T k-k|/|k| >= sqrt(9/500)*|tau|, so same-label extrapolation cannot remain O(1/L)-close.')
print('Scope: rules out direct extension of the existing fixed-reference/fixed-label theorem; recentered multi-label physical propagation remains open.')
