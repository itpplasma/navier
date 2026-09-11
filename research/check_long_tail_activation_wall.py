#!/usr/bin/env python3
"""Exact scaling wall for a co-located perturbative long-tail purifier.

The matched clean gate/filter rate is S.  The clean birth time is t_g=c/S.
For the two-layer long-tail channel D=2N^2 and x=nu D t.  The exact-ladder
small parameter is mu=sqrt(S)/N.  Hence x_g*mu^2=2 c nu exactly.
"""
import sympy as sp

S,N,nu,c = sp.symbols("S N nu c", positive=True)
x = sp.symbols("x", positive=True)
mu2 = S/N**2
xg = 2*nu*N**2*c/S
assert sp.simplify(xg*mu2 - 2*c*nu) == 0

B = sp.Rational(3,4)-sp.exp(-x)+sp.Rational(1,4)*sp.exp(-4*x)
assert sp.simplify(sp.diff(B,x)-sp.exp(-4*x)*(sp.exp(3*x)-1)) == 0
assert sp.limit(B,x,0,dir='+') == 0
assert sp.limit(B,x,sp.oo) == sp.Rational(3,4)

# Gate-dormancy x_g -> 0 and perturbative accuracy mu^2 -> 0 cannot coexist,
# because their product is fixed positive.  Conversely mu^2 -> 0 forces x_g -> infinity.
print("PASS exact identity x_gate * mu^2 = 2 c nu")
print("PASS long-tail build factor monotone 0 -> 3/4")
print("CONSEQUENCE: perturbative ladder accuracy forces purifier fully on by matched gate time")
print("CONSEQUENCE: asymptotic gate dormancy forces nonperturbative ladder strength")
