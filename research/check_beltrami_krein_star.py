#!/usr/bin/env python3
"""Exact two-sector consequence of the Beltrami D-skew linearization.

For D=curl-Lambda, the inviscid linearization about curl U=Lambda U obeys
A*D+DA=0.  In a slow/near-shell helicity pair this forces the nominal O(rho)
forward coupling to have an O(rho/R) reverse partner.  The resulting spectral
scale is rho/sqrt(R), not rho.
"""
from __future__ import annotations
import sympy as sp

R,rho,d,lam=sp.symbols('R rho d lam', positive=True)
ds=-R
b=rho                       # slow -> near-shell sideband

# Same Krein sign: dh=-d.  D-skew fixes high -> slow entry.
dh_same=-d
a_same=sp.simplify(-dh_same/ds*b)
M_same=sp.Matrix([[0,a_same],[b,0]])
char_same=sp.factor(M_same.charpoly(lam).as_expr())
assert a_same == -d*rho/R
assert char_same == lam**2+d*rho**2/R

# Opposite Krein sign: dh=+d.  Hyperbolic, but only at rho/sqrt(R).
dh_opp=d
a_opp=sp.simplify(-dh_opp/ds*b)
M_opp=sp.Matrix([[0,a_opp],[b,0]])
char_opp=sp.factor(M_opp.charpoly(lam).as_expr())
assert a_opp == d*rho/R
assert char_opp == lam**2-d*rho**2/R

# The explicit shell-localization scaling used by the preceding checkpoint.
s=sp.symbols('s', positive=True)
subs={R:s**4,rho:s**2}
assert sp.simplify((rho/sp.sqrt(R)).subs(subs)-1)==0
assert sp.simplify((rho/R).subs(subs)-s**-2)==0
assert sp.simplify(sp.sqrt(R).subs(subs)-s**2)==0
# Raw shell defect/high-parent is s^-3; the worst first-star condition factor
# sqrt(R)=s^2 leaves s^-1, exactly the packet-width ratio delta/b.
assert sp.simplify(s**-3*sp.sqrt(R).subs(subs)-s**-1)==0

print('PASS: Beltrami D-skew forces O(rho/R) return and O(rho/sqrt(R)) spectral scale.')
print('At R=s^4, rho=s^2 the first-star spectral rate is O(1), not O(rho).')
print('Worst sqrt(R) nonnormal factor turns the raw s^-3 shell defect into s^-1.')
print('Scope: isolated slow/near-shell star; off-shell multi-step Krein channels remain open.')
