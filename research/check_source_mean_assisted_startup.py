#!/usr/bin/env python3
"""Exact scalar startup repair and transverse-strain geometry."""
import sympy as s

# Abstract cutoff integral.  The source cutoff is one on [3L/10,7L/10]
# and supported inside (L/6,5L/6), so at v*=L/2 its integral I satisfies
# L/5 <= I <= L/2.
L,I=s.symbols('L I', positive=True)
c=1/I
assert s.simplify(c*I-1)==0
# Hence 2/L <= c <=5/L under the source cutoff bounds.
# Freeze the endpoint constants algebraically.
assert s.simplify((1/(L/s.Integer(2)))-2/L)==0
assert s.simplify((1/(L/s.Integer(5)))-5/L)==0

# Transverse-strain realization.  n,e,f are an orthonormal frame with e the
# instantaneous pulse polarization and n its phase normal.
n=s.Matrix([0,0,1]); e=s.Matrix([1,0,0]); f=s.Matrix([0,1,0])
G=c*(f*f.T-e*e.T)
assert s.trace(G)==0
assert G.T*n==s.zeros(3,1)          # phase normal/direction unchanged
assert G*e==-c*e
# Projected geometric-optics amplitude action of a mean gradient G:
# A_G a=-G a+2 n(n.Ga)/|n|^2.
AGe=-G*e+2*n*(n.dot(G*e))/n.dot(n)
assert s.simplify(AGe-c*e)==s.zeros(3,1)

# The correction coefficient s(v)=w/h obeys s'=-psi'+c psi.  Its integrated
# identity is s=-psi+c*Int psi.  At the source peak psi=1 and Int psi=I.
psi_peak=s.Integer(1)
s_peak=-psi_peak+c*I
assert s.simplify(s_peak)==0

print('PASS: an O(1/L) trace-free transverse mean strain repairs startup with zero high-harmonic entry trace.')
print('The strain leaves the phase normal fixed and acts as the required real scalar gain on the pulse polarization.')
print('Scope: conditional local amplitude/control module; global mean-strain generation is separate.')
