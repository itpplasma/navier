#!/usr/bin/env python3
"""Exact algebra for the two-layer long-tail purifier repair."""
import sympy as sp

x,z,nu,D,S,b,N,eta,M,k0,tau = sp.symbols(
    "x z nu D S b N eta M k0 tau", positive=True)

# Two-layer products c_1=c, c_2=-c with heat gaps D and 4D.
Bz = sp.Rational(3,4) - z + sp.Rational(1,4)*z**4
assert sp.expand(Bz - (z-1)**2*(z**2+2*z+3)/4) == 0

Bx = sp.Rational(3,4) - sp.exp(-x) + sp.Rational(1,4)*sp.exp(-4*x)
assert sp.simplify(sp.diff(Bx,x) - sp.exp(-4*x)*(sp.exp(3*x)-1)) == 0
ser = sp.series(Bx,x,0,5).removeO().expand()
assert ser.coeff(x,0) == 0
assert ser.coeff(x,1) == 0
assert ser.coeff(x,2) == sp.Rational(3,2)
assert ser.coeff(x,3) == -sp.Rational(5,2)
assert sp.limit(Bx,x,sp.oo) == sp.Rational(3,4)

# Tail calibration: F = c/(nu D) exp(-nu a0 t) B(x).
c = sp.Rational(4,3)*nu*D*S
assert sp.simplify(c/(nu*D)*sp.Rational(3,4) - S) == 0

# Strong clean-scale calibration S=M nu b^2 and lambda=eta/b.
Sstrong = M*nu*b**2
lam = eta/b
assert sp.simplify(lam*sp.sqrt(Sstrong)) == eta*sp.sqrt(M)*sp.sqrt(nu)
assert sp.simplify(sp.sqrt(Sstrong)/N) == sp.sqrt(M)*sp.sqrt(nu)*b/N

# Integrated tail action over one clean interval t in [0,tau/b^2].
kappa2 = k0**2/lam**2
Tclean = tau/b**2
I = sp.simplify(Sstrong*(1-sp.exp(-nu*kappa2*Tclean))/(nu*kappa2))
I_expected = M*eta**2/k0**2*(1-sp.exp(-nu*k0**2*tau/eta**2))
assert sp.simplify(I-I_expected) == 0
assert not I.has(b)

# The build-window action is lower order when N/b -> infinity.
assert sp.simplify(Sstrong/N**2/(M*nu)) == b**2/N**2

print("PASS two-layer source cancellation")
print("PASS positive monotone quadratic-onset plateau")
print("PASS tail calibration")
print("PASS bounded fast-parent velocity/frequency ratio")
print("PASS exact-ladder error parameter O(b/N)")
print("PASS clean-clock integrated action independent of b")
print("PASS build-window action O((b/N)^2)")
