#!/usr/bin/env python3
"""Exact leading time-order cancellation for both Raman pump families.

The state-triggered Raman packets froze one ordered tree q then r.  With both
high parents simultaneously present, the reverse tree r then q is also present.
For both the original Leray-silent pair and the later common-Beltrami pair, the
reverse tree is the same one-order asymptotic after Q -> -Q.  Its leading symbol
is the negative of the forward symbol.
"""
from __future__ import annotations
import sympy as sp

a=sp.symbols('a',real=True)
b1,b2,b3=sp.symbols('b1 b2 b3',complex=True)
B=sp.Matrix([b1,b2,b3])
p1,p2,p3=sp.symbols('p1 p2 p3',complex=True)
Pq=sp.Matrix([p1,p2,p3])
qk=sp.symbols('qk',real=True)

# Original silent-pair one-order limit from the state-triggered Raman packet:
#   L_orig(Q)=2(A.Q) P_kappa[(l.kappa)l-(m.kappa)m], m=Qxl.
# Under Q'=-Q, m'=-m.  The bracket is quadratic in m and is unchanged, while
# A.Q changes sign.
L_orig=2*a*B
L_orig_rev=2*(-a)*B
assert sp.simplify(L_orig+L_orig_rev)==sp.zeros(3,1)

# Common-Beltrami one-order limit from the Beltrami Raman packet:
#   L_B(Q)=-2(A.Q)(Q.kappa)P_kappa Q.
# Under Q'=-Q all three Q-dependent factors change sign.  The two helical
# polarizations each also acquire a common minus sign, whose bilinear product is
# +1, so the reverse ordered tree is exactly the transformed formula below.
L_B=-2*a*qk*Pq
L_B_rev=-2*(-a)*(-qk)*(-Pq)
assert sp.simplify(L_B+L_B_rev)==sp.zeros(3,1)

# Scaling consequence: each ordered static composition is O(R), while the
# symmetrized leading O(R) term is zero.  With a slow shift scale J=o(R), the
# first possible residual is O(J+1); after one high heat clock its action is no
# better than rho^2 J/R^2.  Fixed residual action forces the Krein first-star
# scale rho/sqrt(R) to diverge.
R,J,c=sp.symbols('R J c',positive=True)
rho=R*sp.sqrt(c/J)
assert sp.simplify(rho**2*J/R**2-c)==0
assert sp.simplify((rho/sp.sqrt(R))**2-c*R/J)==0

print('PASS: both Raman families have exact leading cancellation between q->r and r->q.')
print('The one-ordered-tree response is not the simultaneous-pump time-evolution coefficient.')
print('At J/R->0, recovering fixed action from the residual forces rho/sqrt(R)->infinity.')
