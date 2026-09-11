#!/usr/bin/env python3
"""Exact no-go for a single-axis dark-state Raman export filter.

For the leading Beltrami Raman symbol, a desired carrier (k_j,v_j) is exactly
dark for fast axis Q only if (v_j.Q)(k_j.Q)=0.  Thus for each of the three
clean second targets one must choose Q perpendicular to either k_j or v_j.
There are 2^3 choices.  At the clean algebraic return root, every corresponding
triple of chosen vectors is linearly independent, so no nonzero Q is orthogonal
to all three.  A single Raman axis therefore cannot exactly protect all desired
targets while exporting other carriers.
"""
from __future__ import annotations
import itertools
import sympy as sp

z=sp.symbols('z',real=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

def physk(h):
    return sp.Matrix([sp.Integer(h[0])-z*sp.Integer(h[2]),sp.Integer(h[1]),sp.Integer(h[2])])

def vsel(h):
    if h==(0,1,1):
        return sp.Matrix([
          2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2+4*z+2)/(3*(z**2+2)*(z**2+2*z+2)),
          2*z**3*(z**4+2*z**3+z**2-2)/(3*(z**2+2)*(z**2+2*z+2))])
    if h==(-2,-1,-1):
        return sp.Matrix([
         -2*z*(z**3+2*z-4)/(3*(z**2-4*z+6)),
         -2*z*(z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2)),
         -2*z*(z**6-4*z**5+7*z**4-8*z**3+14*z**2-16*z+8)/(3*(z**2-4*z+6)*(z**2-2*z+2))])
    if h==(0,-1,1):
        return sp.Matrix([
         -2*z**2*(z**2-2)/(3*(z**2+2)),
         -2*z**3*(z**2-4*z+2)/(3*(z**2+2)*(z**2-2*z+2)),
         -2*z**3*(z**4-2*z**3+z**2-2)/(3*(z**2+2)*(z**2-2*z+2))])
    raise KeyError(h)

targets=[(0,1,1),(-2,-1,-1),(0,-1,1)]
pairs=[(physk(h),vsel(h)) for h in targets]

# For darkness of target j, either Q.k_j=0 or Q.v_j=0.  If a nonzero Q made
# all three targets dark, one of the eight selected triples below would have a
# common nonzero orthogonal vector, hence determinant zero at z_*.
checks=0
for bits in itertools.product((0,1),repeat=3):
    W=sp.Matrix.hstack(*[pairs[j][bits[j]] for j in range(3)])
    det=sp.factor(W.det())
    num,den=map(sp.factor,sp.together(det).as_numer_denom())
    p=sp.Poly(num,z)
    # Coprimality with the clean polynomial proves det !=0 at every clean root.
    assert sp.gcd(p,Qclean).degree()==0, bits
    # Denominators are products of positive quadratics on the real line; a
    # midpoint calibration also excludes a hidden zero denominator here.
    assert den.subs(z,(lo+hi)/2)!=0, bits
    checks+=1

assert checks==8
print('PASS: all 8 darkness-choice determinants are coprime to Qclean.')
print('No nonzero single fast axis Q can make all three desired clean second targets exactly Raman-dark at the clean root.')
print('Scope: exact single-axis dark-state no-go; multi-axis/time-dependent export remains open.')
