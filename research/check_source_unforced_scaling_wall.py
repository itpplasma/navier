#!/usr/bin/env python3
"""Exponent ledger for isotropic NS rescalings of the forced source core."""
from fractions import Fraction

h=Fraction(1,200)  # any fixed positive h works; one admissible calibration
# source: speed tau^(-1/2-h), radial tau^(1/2), axial tau^(1/2-h)
speed_exp=-Fraction(1,2)-h
volume_exp=Fraction(3,2)-h
energy_exp=2*speed_exp+volume_exp
l3cube_exp=3*speed_exp+volume_exp
assert energy_exp==Fraction(1,2)-3*h
assert l3cube_exp==-4*h

# endpoint-preserving isotropic NS scaling r=tau^(1/2)
alpha_time=Fraction(1,2)
assert alpha_time+speed_exp==-h                 # rescaled L-infinity diverges
assert energy_exp-alpha_time==-3*h             # rescaled L2^2 diverges

# velocity-normalizing scale r=tau^(1/2+h)
alpha_vel=Fraction(1,2)+h
assert alpha_vel+speed_exp==0
assert 1-2*alpha_vel==-2*h                     # endpoint time tends to infinity
assert energy_exp-alpha_vel==-4*h

# No alpha can simultaneously have finite nonzero endpoint time (alpha=1/2)
# and bounded velocity (alpha>=1/2+h) for h>0.
assert alpha_time < alpha_vel

print('PASS: source Type-II exponents obstruct a direct finite-time bounded isotropic unforced blowup limit.')
print('Endpoint-normalized scaling has diverging speed/L2; velocity-normalized scaling pushes the endpoint to infinite time.')
print('The scale-invariant L3^3 core size diverges like tau^(-4h).')
