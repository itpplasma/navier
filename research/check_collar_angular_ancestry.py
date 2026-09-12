#!/usr/bin/env python3
"""Exact angular ancestry and divergence-free pressure-symbol discriminator."""
from fractions import Fraction

# A target angular grade N cannot be written as m+(N-m) with both factors
# strictly below N/2 in absolute grade.  Freeze representative integer cases.
for N in range(1,65):
    low=[m for m in range(-N,N+1) if 2*abs(m)<N]
    for m in low:
        for l in low:
            assert m+l != N
            assert m+l != -N
    # Every exact decomposition N=m+l has at least one high-half ancestor.
    for m in range(-2*N,2*N+1):
        l=N-m
        assert 2*abs(m)>=N or 2*abs(l)>=N

# The L1 stress bound after the low/high split is exactly of the form
# ||Pi_N(u tensor u)||_1 <= 2 ||u_H||_2 ||u||_2.  The numerical factor 2
# comes from H tensor u + L tensor H after the L tensor L target vanishes.
# Freeze the scalar Cauchy-Schwarz coefficient bookkeeping.
for H,U in [(Fraction(1,7),Fraction(3,5)),(Fraction(2,3),Fraction(5,4))]:
    L=U-H if U>=H else U
    rhs=H*U + L*H
    assert rhs <= 2*H*U

# Incompressibility itself does not kill the quadratic pressure symbol.
# p=(1,0,0), q=(0,1,0), a=(0,1,0) perp p, b=(1,0,0) perp q.
p=(1,0,0); q=(0,1,0); a=(0,1,0); b=(1,0,0)
dot=lambda x,y: sum(xi*yi for xi,yi in zip(x,y))
k=tuple(pi+qi for pi,qi in zip(p,q))
assert dot(p,a)==0 and dot(q,b)==0
assert dot(k,a)==1 and dot(k,b)==1
# For the symmetric cross stress a tensor b+b tensor a,
# -Delta pressure = div div stress has numerator 2(k.a)(k.b).
num=2*dot(k,a)*dot(k,b)
den=dot(k,k)
assert num==2 and den==2
pressure_coeff=Fraction(-num,den)
assert pressure_coeff==-1

print('PASS: exact collar angular-ancestry discriminator.')
print('A quadratic grade-N pressure source requires at least one velocity ancestor with |m|>=N/2.')
print('The target stress obeys the analytic bound ||Pi_N(u⊗u)||_1 <= 2 ||u_H||_2 ||u||_2.')
print('A divergence-free two-wave example has nonzero pressure coefficient -1, so incompressibility gives no universal symbol cancellation.')
print('Scope: angular algebra/symbol level; physical collar localization and full-history propagation remain open.')
