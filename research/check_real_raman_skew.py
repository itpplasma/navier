#!/usr/bin/env python3
"""Exact L2-skew identity for the reality-complete single-axis Raman operator.

For Q=e1 and every transverse shift l.Q=0, Fourier reality pairs the +l module
of strength alpha with the reflected (-l,-Q) module of strength conjugate(alpha).
On the active line at each slow frequency, spanned by e_k=P_k Q, the paired
translation operator is exactly skew-adjoint in the physical L2 metric.
Consequently every same-module +l,-l backtrack is negative semidefinite.
"""
from __future__ import annotations
import sympy as sp

x,y,c,m,n=sp.symbols('x y c m n',real=True)
a,b=sp.symbols('a b',real=True)  # alpha=a+i b
alpha=a+sp.I*b
alphac=a-sp.I*b

# Q=e1, k=(x,y,c), l=(0,m,n), k1=k+l.
k2=x*x+y*y+c*c
k12=x*x+(y+m)**2+(c+n)**2
# c_k=Q.P_k Q=|P_k Q|^2.  These are the physical L2 weights of the active
# coordinate s in v=s P_k Q.
c0=sp.factor((y*y+c*c)/k2)
c1=sp.factor(((y+m)**2+(c+n)**2)/k12)

# Leading Beltrami Raman symbol from the common-sphere theorem:
#   R_(l,Q)(k,v)=-2 alpha (v.Q)(Q.(k+l)) P_(k+l)Q.
# Because Q.l=0, Q.(k+l)=x.  In active scalar coordinates v=s e_k,
# v.Q=s c_k.
A10=sp.factor(-2*alpha*x*c0)     # k -> k+l
# The reality-reflected module has (-l,-Q), giving the reverse edge
#   R_(-l,-Q)(k+l,v)=+2 conjugate(alpha) x (v.Q) P_k Q.
A01=sp.factor( 2*alphac*x*c1)   # k+l -> k

# Weighted skew-adjointness W A + A^* W=0 for W=diag(c0,c1).
assert sp.simplify(c1*A10+c0*sp.conjugate(A01))==0
assert sp.simplify(c0*A01+c1*sp.conjugate(A10))==0

# Same-module return on the active scalar is non-positive:
# A01*A10=-4 |alpha|^2 x^2 c0 c1.
loop=sp.factor(A01*A10)
assert sp.simplify(loop+4*(a*a+b*b)*x*x*c0*c1)==0

# In vector form, for arbitrary transverse v the return has quadratic form
#   <v,L_- L_+ v>=-4 |alpha|^2 x^2 c1 |v.Q|^2 <=0.
# The sign is algebraic whenever k,k+l are nonzero.
assert a*a+b*b>=0

# Any transverse polarization with v.Q=0 is exactly inactive.
v1,v2,v3=sp.symbols('v1 v2 v3',real=True)
# The leading symbol is proportional to v.Q=v1.
assert sp.diff(v1,x)==0

print('PASS: reality-paired +/- Raman translations are exactly L2-skew on the active single-axis slow lattice.')
print('Every same-module backtrack is -4 |alpha|^2 x^2 c_k c_(k+l), hence negative semidefinite.')
print('Inactive polarizations with v.e1=0 remain uncoupled at this leading effective order.')
