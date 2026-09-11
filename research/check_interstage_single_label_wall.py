#!/usr/bin/env python3
"""Exact scale/action obstruction to extending one finite-L source label across a factor-two interstage interval."""
from fractions import Fraction

# The factor-two normalization interval from the frozen reference theorem.
# rho=2^(-2/h), so rho^(-h)=4 and integral q^(-1-h)dq = 3 Q^(-h)/h.
# Use an exact repository-admissible subsequence h=1/200, ell=400*k:
# Q=2^(-ell), Q^(-h)=2^(2k)=4^k and L=ell^2.
h=Fraction(1,200)
rows=[]
for k in range(1,25):
    ell=400*k
    Qmh=4**k
    action=Fraction(3,1)*Qmh/h              # 3 Q^{-h}/h
    L=ell*ell
    tau=action/L
    rows.append((k,ell,action,tau))
assert all(rows[j+1][3]>rows[j][3] for j in range(2,len(rows)-1))
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

# Therefore any same-label extrapolation with normalized fast displacement tau
# satisfies |T k-k|/|k| >= sqrt(9/500)*|tau|.  Squared deformation diverges
# along the exact subsequence above.  The fixed-window O(1/L) perturbative cage
# cannot be extrapolated over this interval without recentering/changing labels.
for k,ell,action,tau in rows:
    lower2=Fraction(9,500)*tau*tau
    if k>=10:
        assert lower2>1

# Exponential action beats every polynomial in ell analytically.  On the exact
# finite regression subsequence certify growth against ell^2 and ell^4 once k
# is large enough; these checks calibrate, rather than prove, the asymptotic.
for k,ell,action,tau in rows[-5:]:
    assert action > ell**4
    assert tau > ell**2

print('PASS: exact single-label factor-two interstage deformation leaves the finite-L perturbative regime.')
print('Required reference fast action = 3 Q^(-h)/h; action/L -> infinity for L~ell^2.')
print('For every caged parent, |T k-k|/|k| >= sqrt(9/500)*|tau|, so a same-label extrapolation is not O(1/L)-close.')
print('Scope: rules out extending the existing fixed-reference/fixed-label theorem directly; recentered multi-label physical propagation remains open.')
