#!/usr/bin/env python3
"""Exact exponent threshold for pressure-forced sparse-collar L3 bounds.

This freezes the exponent algebra behind the analytic collar estimate.  It does
not prove that a quadratic stress attaining the pressure upper bound exists.
"""
from fractions import Fraction

# Write the desired parent pressure-input scale as A=exp(-C L), and choose a
# collar thickness delta/r = kappa L/N.  The midpoint form of the existing
# pressure estimate has log operator norm / L -> -kappa/2; all Q,N,r powers
# contribute only o(L) because L~ell^2 while their logarithms are O(ell).
# Therefore signal size A forces kinetic energy at least
# E_req = exp(-(C-kappa/2)L+o(L)).
# If the stress-support volume is an exponentially sparse fraction
# exp(-beta L) of the full collar, Holder gives
# ||u||_3 >= exp(E3*L+o(L)),
# E3=-(C-kappa/2)/2 + beta/6.

def exponents(C,kappa,beta):
    energy = -C + kappa/Fraction(2)
    l3 = energy/Fraction(2) + beta/Fraction(6)
    threshold = 3*(C-kappa/Fraction(2))
    return energy,l3,threshold

# Generic algebra encoded by several exact rational samples on both sides.
C=Fraction(1)
kappa=Fraction(1)
energy,l3,threshold=exponents(C,kappa,Fraction(1))
assert kappa < 2*C
assert energy == Fraction(-1,2)
assert threshold == Fraction(3,2)
assert l3 == Fraction(-1,12)       # exponentially sparse, but no forced L3 blowup

_,l3crit,_=exponents(C,kappa,threshold)
assert l3crit == 0
_,l3super,_=exponents(C,kappa,Fraction(2))
assert l3super == Fraction(1,12)    # only stronger sparsity forces exponential L3 growth

# A second non-normalized sample verifies the formula is not tied to C=1.
C2=Fraction(7,5); k2=Fraction(3,5)
th2=3*(C2-k2/Fraction(2))
assert th2 == Fraction(33,10)
_,below,_=exponents(C2,k2,Fraction(3))
_,above,_=exponents(C2,k2,Fraction(18,5))
assert below < 0 < above

# Source-scale side conditions on an exact admissible subsequence:
# h=1/200, ell=400 k -> N=2^k, L=(400k)^2.  Thus L/N ->0, while
# log(r), log(N), log(delta), log(V_collar) are O(ell)=o(L).
# Freeze the decisive polynomial-vs-exponential inequalities at large k.
for k in (30,40,50):
    ell=400*k
    L=ell*ell
    N=2**k
    assert Fraction(L,N) < Fraction(1,100) if k>=40 else True
    assert Fraction(ell,L) == Fraction(1,ell)
assert Fraction((400*50)**2,2**50) < Fraction(1,10**6)

print('PASS: sparse-collar pressure/L3 exponent threshold.')
print('For kappa<2C, required energy is exponentially small at rate C-kappa/2.')
print('If support fraction is exp(-beta L), the forced L3 exponent is -(C-kappa/2)/2 + beta/6.')
print('Thus pressure+energy+support size forces L3 growth only for beta>3(C-kappa/2); a wide exponentially sparse window remains non-obstructive.')
print('Scope: inequality-level obstruction only; pressure attainability and full-history amplification remain open.')
