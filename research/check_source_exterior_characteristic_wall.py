#!/usr/bin/env python3
"""Exact material-X identity for the forced source similarity coordinates."""
import sympy as s

X,q,L,eta,D,d,U,AXU,Aeta=s.symbols(
    'X q L eta D d U AXU Aeta', positive=True, real=True)

# Source similarity identities:
#   X_t = X/(qL), X_r=r/q, X_z=-2 eta X/(q^D L),
#   u_r=V0/r, u_z=q^{-A} U, A+D=1.
# Hence u_z X_z=-2 eta X U/(q L).
V0=X/L*(2*eta*U-2*D*eta*AXU-d*Aeta)
DtX=s.factor(X/(q*L)+V0/q-2*eta*X*U/(q*L))
expected=X/(q*L)*(1-2*D*eta*AXU-d*Aeta)
assert s.simplify(DtX-expected)==0

# In the exact source exterior U=V0=0.  The support theorem also gives the
# averaged/eta derivative terms zero there, so W=1.
exterior=s.simplify(expected.subs({U:0,AXU:0,Aeta:0}))
assert exterior==X/(q*L)

print('PASS: D_t X = X W/(qL) with W=1 in the exact source exterior.')
print('Thus D_t X=X/(qL)>0 there: passive source characteristics move outward in similarity X.')
print('Scope: prescribed forced-source base characteristics; correction-driven nonlinear/diffusive transport remains open.')
