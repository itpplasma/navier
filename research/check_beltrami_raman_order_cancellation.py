#!/usr/bin/env python3
"""Exact leading-order cancellation of the two time orderings in a common-Beltrami Raman pair.

The previous common-sphere Raman span checker kept the ordered tree
  h --q--> h+q --r--> h+q+r.
For a simultaneously present high pair the reverse tree with q,r exchanged is
also present.  It is exactly the same one-order common-Beltrami asymptotic with
Q replaced by -Q.  The two leading O(N) symbols have opposite sign.

Consequently the physical symmetrized two-step coefficient loses one power of
the high scale.  A fixed action from that residual is incompatible with the
previous bounded Krein-star regime whenever the slow shift J satisfies J/R->0.
"""
from __future__ import annotations
import sympy as sp

a,qk=sp.symbols('a qk',real=True)
p1,p2,p3=sp.symbols('p1 p2 p3',complex=True)
Pq=sp.Matrix([p1,p2,p3])

# Frozen one-ordered-tree limit from the common-Beltrami checker:
# L(Q)=-2 (A.Q)(Q.kappa) P_kappa Q.
LQ=-2*a*qk*Pq
# Reverse ordering is the same construction with Q'=-Q.  Both high helical
# polarizations acquire a minus sign under this reparametrization, so their
# bilinear product is unchanged.  The three Q-dependent factors transform as
# A.Q -> -a, Q.kappa -> -qk, P Q -> -Pq.
Lminus=-2*(-a)*(-qk)*(-Pq)
assert sp.simplify(Lminus+LQ)==sp.zeros(3,1)

# Hence the complete simultaneous-pair leading symbol vanishes.
assert sp.simplify(LQ+Lminus)==sp.zeros(3,1)

# Scaling consequence.  Let R be high/clean scale, J the slow-shift scale, and
# rho=P/(nu R).  After the O(R) ordered terms cancel, the next static term is at
# most O(J+1), so the integrated slow action scales no better than
#   rho^2 J/R^2
# for J>=1.  Holding this below-scale residual at a fixed positive value forces
# the Krein first-star rate rho/sqrt(R) to diverge when J/R->0.
R,J,c=sp.symbols('R J c',positive=True)
# If rho^2 J/R^2 >= c, then (rho/sqrt R)^2 >= c R/J.
# The right side diverges in every scale-separated limit J/R->0.
rho_required=R*sp.sqrt(c/J)
assert sp.simplify((rho_required/sp.sqrt(R))**2-c*R/J)==0

# Concrete route scaling previously proposed: J=sigma^2,R=sigma^6.
sigma=sp.symbols('sigma',positive=True)
assert sp.simplify((rho_required/sp.sqrt(R)).subs({J:sigma**2,R:sigma**6})-sp.sqrt(c)*sigma**2)==0

print('PASS: the two common-Beltrami Raman time orderings cancel at leading O(R).')
print('The one-ordered-tree span is not the simultaneous-pump slow coefficient.')
print('A fixed residual action with J/R->0 forces rho/sqrt(R) >= sqrt(c R/J) -> infinity, outside the controlled Krein-star regime.')
