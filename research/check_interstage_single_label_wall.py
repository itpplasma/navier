#!/usr/bin/env python3
"""Exact scale obstruction to extending one finite-L source label across a factor-two interstage interval."""
from fractions import Fraction

# Use an exact repository-admissible subsequence h=1/200, ell=400*k:
# Q=2^(-ell), Q^(-h)=4^k, L=ell^2.  A doubled frequency becomes normalized
# z=1 when q contracts from Q to rho Q with rho=2^(-2/h)=2^-400.
h=Fraction(1,200)
rho=Fraction(1,2**400)
assert rho > 0 and rho < 1

# On the exact eta=0 self-similar ray, 1-t=q and hence Delta t=(1-rho)Q.
# The inspected fixed lifted-label identity is partial_t v=Q^(-1-h).
# Therefore the SAME label would have to traverse
#   Delta v=(1-rho) Q^(-h),
# so its finite-L deformation parameter tau=Delta v/L is
#   tau_k=(1-rho)4^k/(160000 k^2).
rows=[]
for k in range(1,25):
    ell=400*k
    Qmh=4**k
    L=ell*ell
    dv=(1-rho)*Qmh
    tau=dv/L
    rows.append((k,ell,dv,tau))
    assert tau == (1-rho)*Fraction(4**k,160000*k*k)

# Exact ratio tau_(k+1)/tau_k=4 k^2/(k+1)^2 >=16/9 for k>=2,
# so tau diverges geometrically despite L~ell^2.
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
for k,ell,dv,tau in rows:
    lower2=Fraction(9,500)*tau*tau
    if k>=15:
        assert lower2>1

print('PASS: exact same-label factor-two interstage deformation leaves the finite-L perturbative regime.')
print('On eta=0, Delta v=(1-rho)Q^(-h) with rho=2^(-2/h), so Delta(v/L) diverges for L~ell^2.')
print('For every caged parent, |T k-k|/|k| >= sqrt(9/500)*|Delta v|/L; same-label extrapolation cannot remain O(1/L)-close.')
print('Scope: rules out direct extension of the existing fixed-reference/fixed-label theorem; recentered multi-label physical propagation remains open.')
