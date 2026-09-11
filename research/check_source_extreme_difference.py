#!/usr/bin/env python3
"""Exact algebra for the extreme-difference obstruction in a finite growing source family."""
import sympy as sp

b,delta,c,c0,q1,qN=sp.symbols('b delta c c0 q1 qN', real=True)
C=sp.Matrix([0,b*delta*c0*(q1+qN),-2*b*delta*c])
norm2=sp.factor(C.dot(C))
assert norm2 == b**2*delta**2*(4*c**2+c0**2*(q1+qN)**2)

# Under the theorem hypotheses b>0, delta!=0, c0!=0 and q1,qN>0,
# the second summand is strictly positive independently of c.
print('PASS: extreme difference coefficient has norm^2 =', norm2)
print('It is nonzero whenever b>0, delta!=0, c0!=0 and q1,qN>0.')
