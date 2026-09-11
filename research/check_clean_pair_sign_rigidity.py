#!/usr/bin/env python3
"""Exact signed-child rigidity for the clean k1,k3 parent pair.

For arbitrary transverse polarizations the sum and difference Leray outputs
share a rigid x/z factor.  In a real field (negative Fourier coefficient is
the conjugate of the positive one), one signed child can vanish only if the
other vanishes as well.  Thus the two clean 1--3 children cannot be born at
separate sites merely by retuning this parent pair's polarization.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def proj(k,v): return sp.simplify(v-k*k.dot(v)/k.dot(k))
def pair(p,a,q,b): return sp.Matrix([sp.factor(x) for x in proj(p+q,(a.dot(q))*b+(b.dot(p))*a)])

z,A,B,C,D=sp.symbols('z A B C D', nonzero=False)
k1=sp.Matrix([1,0,0]); k3=sp.Matrix([-z,0,1])
a=sp.Matrix([0,A,B]); b=sp.Matrix([C,D,z*C])
plus=pair(k1,a,k3,b)
minus_same=pair(k1,a,-k3,b) # algebraic same-polarization calibration

Dp=z**2-2*z+2; Dm=z**2+2*z+2
expected_plus=sp.Matrix([B*C*z**2/Dp,A*C+B*D,B*C*z**2*(z-1)/Dp])
expected_minus=sp.Matrix([-B*C*z**2/Dm,A*C-B*D,-B*C*z**2*(z+1)/Dm])
check(sp.simplify(plus-expected_plus)==sp.zeros(3,1),'exact sum-child formula')
check(sp.simplify(minus_same-expected_minus)==sp.zeros(3,1),'exact difference-child calibration')
check(sp.factor(Dp-(z-1)**2-1)==0 and sp.factor(Dm-(z+1)**2-1)==0,'both denominators strictly positive on real z')

# The full reality-compatible complex statement is by cases: for positive-mode
# b=(C,D,zC), the -k3 coefficient is conjugate(b), so a zero difference child
# implies B*conj(C)=0 and A*conj(C)-B*conj(D)=0.  For nonzero a,b, either case
# forces B=C=0 and hence the plus child also vanishes.  The converse is the
# identical argument without conjugates.  The symbolic formulas above freeze
# the only carrier algebra used in that case split.

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Reality-compatible rigidity: C_+=0 iff C_-=0 for nonzero transverse parents at the clean k1,k3 pair.')
print('Scope: one parent-wavevector pair only; auxiliary pairs or active nonlinear routing remain open.')
