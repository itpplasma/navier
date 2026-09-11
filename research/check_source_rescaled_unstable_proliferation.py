#!/usr/bin/env python3
"""Exact unstable-site growth under repeated factor-two source rescaling.

For the caged source lattice k_(m,z)=((3m-z)/10,0,z), the positive-branch
rate is r=1/sqrt(1+s^2)-mu z^2(1+s^2), s=(3m-z)/(10z).
This checker specializes to the relay slices z=2^{-j} with the inherited
x-lattice numerator convention s_m=(3m-1)/10 used after stage normalization.
It certifies exact unstable intervals for early j and the general unbounded
proliferation criterion.
"""
from fractions import Fraction

MU=Fraction(3,5)

def s_of(m):
    return Fraction(3*m-1,10)

def unstable(j,m):
    # r>0 iff q^3 < 1/(mu z^2), q^2=1+s^2, z=2^-j.
    # Squaring the positive inequality gives
    #   (1+s^2)^3 < 1/(mu^2 z^4) = (25/9) 16^j.
    ss=s_of(m)
    lhs=(1+ss*ss)**3
    rhs=Fraction(25,9)*(16**j)
    return lhs < rhs

expected={
    0:(-1,2,4),
    1:(-4,5,10),
    2:(-9,9,19),
    3:(-15,15,31),
    4:(-24,25,50),
}
for j,(lo,hi,count) in expected.items():
    got=[m for m in range(-100,101) if unstable(j,m)]
    assert got==list(range(lo,hi+1)), (j,got[:3],got[-3:])
    assert len(got)==count
    assert not unstable(j,lo-1)
    assert not unstable(j,hi+1)

# General finite-set proliferation: for every requested symmetric set
# |m|<=M, an explicit finite j makes every site unstable.
for M in range(1,101):
    qmax2=1+max(s_of(-M)**2,s_of(M)**2)
    # find a concrete j by exact rational arithmetic
    j=0
    while qmax2**3 >= Fraction(25,9)*(16**j):
        j+=1
    assert all(unstable(j,m) for m in range(-M,M+1))

# The first explicit pollutant m=5 is stable in the original cage but
# unstable after one factor-two rescaling.
assert not unstable(0,5)
assert unstable(1,5)

print('PASS: exact rescaled source spectrum has unbounded unstable-site proliferation.')
print('Early unstable intervals: j=0 [-1,2], j=1 [-4,5], j=2 [-9,9], j=3 [-15,15], j=4 [-24,25].')
print('For every finite M, all |m|<=M are unstable at some finite factor-two stage.')
print('Scope: linear source-reference spectrum only; amplitudes and nonlinear cascade closure are separate.')
