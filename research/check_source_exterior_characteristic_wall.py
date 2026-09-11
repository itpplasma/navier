#!/usr/bin/env python3
"""Exact material-X identity for the forced source similarity coordinates."""
import sympy as s

X,q,L,eta,D,d,U,AXU,Aeta=s.symbols(
    'X q L eta D d U AXU Aeta', positive=True, real=True)

# Verify the actual implicit coordinates q-z^2 q^(2h)=1-t.
# The earlier prose shortcut q=1-t/L was incorrect because q depends on z.
h,z=s.symbols('h z', positive=True, real=True)
D0=s.Rational(1,2)-h
F=q-z*z*q**(2*h)
Fq=s.diff(F,q).subs(z,eta*q**D0)
L0=1-2*h*eta**2
assert s.simplify(Fq-L0)==0
qt=-1/Fq
qz=s.simplify(-s.diff(F,z).subs(z,eta*q**D0)/Fq)
assert s.simplify(qt+1/L0)==0
assert s.simplify(qz-2*eta*q**(1-D0)/L0)==0
Xt=-X*qt/q
Xz=-X*qz/q
assert s.simplify(Xt-X/(q*L0))==0
assert s.simplify(Xz+2*eta*X/(q**D0*L0))==0
eta_t=-D0*eta*qt/q
eta_z=q**(-D0)-D0*eta*qz/q
assert s.simplify(eta_t-D0*eta/(q*L0))==0
assert s.simplify(eta_z-(1-eta**2)/(q**D0*L0))==0

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
