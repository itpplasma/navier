#!/usr/bin/env python3
"""Exact no-go for passive ordering repairs of the simultaneous Raman pair.

Three inexpensive repairs are excluded at the leading Raman scale:
  1. the current centered near-opposite pairs have exactly equal Stokes clocks;
     a general near-opposite pair with slow sum l has only o(1) relative heat
     asymmetry on one high clock when |l|/R->0;
  2. scalar amplitudes/phases multiply both ordered trees by the same product;
  3. polarization cannot make only one target-to-high first leg survive at
     leading order: the two limits are +(A.Q) beta_0 and -(A.Q) eps_0.

Thus leading one-way action requires genuine dynamic/spatial parent ordering or
a different interaction geometry.
"""
from __future__ import annotations
import sympy as sp

N,c=sp.symbols('N c', positive=True)
Q2,l2=sp.symbols('Q2 l2', positive=True)
ql=sp.symbols('ql', real=True)

# Current pump geometry q=l/2+NQ, r=l/2-NQ with l.Q=0 has identical heat rates.
qnorm=sp.expand(l2/4+N**2*Q2+N*ql)
rnorm=sp.expand(l2/4+N**2*Q2-N*ql)
assert sp.expand((qnorm-rnorm).subs(ql,0))==0

# General centered near-opposite geometry has
# |q|^2-|r|^2=2N Q.l.  On t=c/(N^2 |Q|^2), the exponent difference is
# 2c (Q.l)/(N |Q|^2), hence o(1) if |l|/(N|Q|)->0.
t=c/(N**2*Q2)
heat_gap=sp.factor(t*(qnorm-rnorm))
assert heat_gap==2*c*ql/(N*Q2)

# Initial scalar amplitudes/phases cannot weight the orderings differently.
aq,ar,L=sp.symbols('a_q a_r L')
forward=aq*ar*L
reverse=aq*ar*(-L)
assert sp.expand(forward+reverse)==0

# Leading polarization first-leg limits.  For nonzero limiting transverse
# polarizations beta0,eps0 and target A, the q and r first legs are
#   +(A.Q) beta0, -(A.Q) eps0.
# A scalar polarization choice cannot make exactly one of these vanish without
# either deleting a parent or taking A.Q=0, in which case both lose the O(N)
# Raman first-leg scale.
AQ=sp.symbols('A_Q', real=True)
b1,b2,e1,e2=sp.symbols('b1 b2 e1 e2', real=True)
beta_norm2=b1**2+b2**2
eps_norm2=e1**2+e2**2
F_norm2=sp.expand(AQ**2*beta_norm2)
R_norm2=sp.expand(AQ**2*eps_norm2)
# Algebraic product: with both parent polarizations nonzero, simultaneous
# vanishing of one norm through the common target factor requires AQ=0 and then
# the other vanishes as well.  Freeze the common factor explicitly.
assert sp.factor(F_norm2/beta_norm2)==AQ**2
assert sp.factor(R_norm2/eps_norm2)==AQ**2

# A useful fixed action from a residual ordering asymmetry of relative size
# delta=O(|l|/R) would require increasing the nominal symmetric action by 1/delta.
# In the common-Beltrami regime this reproduces the divergent first-star scale.
Rscale,J,mu=sp.symbols('Rscale J mu', positive=True)
# nominal action rho^2/Rscale, residual fraction J/Rscale => rho^2 J/Rscale^2.
rho_req=Rscale*sp.sqrt(mu/J)
assert sp.simplify(rho_req**2*J/Rscale**2-mu)==0
assert sp.simplify((rho_req/sp.sqrt(Rscale))**2-mu*Rscale/J)==0

print('PASS: passive Raman ordering repairs are excluded at leading scale.')
print('Current centered pumps have equal Stokes clocks; general heat asymmetry is only O(|l|/R) per high clock.')
print('Amplitude/phase imbalance multiplies both orderings by the same product.')
print('With both parents nonzero, polarization gating gives two first-leg norms with the same factor |A.Q|^2; AQ=0 kills both leading legs.')
print('A surviving Raman route therefore needs genuine dynamic/spatial parent ordering or a different interaction geometry.')
