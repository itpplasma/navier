#!/usr/bin/env python3
"""Exact geometry for a common-line two-axis Raman Schur limit.

Choose two fast axes QA,QB and their common perpendicular slow-lattice vector
l=QA x QB.  Module A translates by +/- J l with strength J sqrt(30), while
module B translates by +/- 2J l with strength 2J sqrt(10).  Because both axes
are perpendicular to l, Q_i.(k+nJl)=Q_i.k at every lattice site.  Thus Raman
edges are O(J) while every nonzero lattice site's viscosity is O(J^2 n^2), the
regime needed for an adiabatic Schur elimination.

The exact leading center damping form is

 K0=(8/|l|^2) sum_i w_i (k.q_i)^2 (P_k q_i) tensor (P_k q_i),

where q_i=Q_i/|Q_i| and (w_A,w_B)=(30,10).  Its Rayleigh numerator on the
load-bearing selected carriers is <1/4 before the common factor 8/|l|^2 for all
three desired targets and >1 for p1,g2,g3,r1.
"""
from __future__ import annotations
import sympy as sp

z=sp.symbols('z',real=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

QA=sp.Matrix([-1,-5,-6]); QB=sp.Matrix([10,-3,-1])
ell=QA.cross(QB)
assert ell==sp.Matrix([-13,-61,53])
L2=ell.dot(ell)
assert L2==6699
assert QA.dot(ell)==0 and QB.dot(ell)==0

def assert_positive_on_clean(expr,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    mid=(lo+hi)/2
    assert p.count_roots(lo,hi)==0,label
    assert p.eval(mid)>0,label
    assert den.subs(z,mid)>0,label

def center_form(k,a):
    """Rayleigh numerator C with K0-Rayleigh=(8/L2) C."""
    out=0
    for Q,w in [(QA,30),(QB,10)]:
        out += sp.Rational(w)*(a.dot(Q)**2)*(k.dot(Q)**2)/(a.dot(a)*Q.dot(Q)**2)
    return sp.factor(out)

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

targets=[(physk(h),vsel(h)) for h in [(0,1,1),(-2,-1,-1),(0,-1,1)]]
Dp=z**2+2*z+2; Dm=z**2-2*z+2
unwanted=[
 ('p1',sp.Matrix([1,0,0]),sp.Matrix([0,1,z])),
 ('g2',sp.Matrix([1+z,0,-1]),sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])),
 ('g3',sp.Matrix([1-z,0,1]),sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])),
 ('r1',sp.Matrix([-1,-1,0]),sp.Matrix([0,0,1])),
]
all_sources=targets+[(k,a) for _,k,a in unwanted]

# The center n=0 is the unique viscosity minimum in its whole one-dimensional
# translated lattice for every integer J>=1.  Indeed
# |k+nJ ell|^2-|k|^2=(nJ)^2 L2+2(nJ) k.ell.
# It suffices that L2 +/- 2 k.ell >0, because |nJ|>=1.
for idx,(k,a) in enumerate(all_sources):
    assert_positive_on_clean(L2+2*k.dot(ell),f'source {idx}: + lattice gap')
    assert_positive_on_clean(L2-2*k.dot(ell),f'source {idx}: - lattice gap')
    for Q in (QA,QB):
        # Exact invariance of the fast-axis projection along the entire lattice.
        assert Q.dot(ell)==0

# Exact leading Schur selectivity.
for j,(k,a) in enumerate(targets):
    C=center_form(k,a)
    assert_positive_on_clean(sp.Rational(1,4)-C,f'desired {j}: C < 1/4')
for name,k,a in unwanted:
    C=center_form(k,a)
    assert_positive_on_clean(C-1,f'{name}: C > 1')

print('PASS: exact common-line two-axis Schur geometry on the clean-root interval.')
print('ell=(-13,-61,53), |ell|^2=6699, and n=0 is the unique viscosity minimum for all seven load-bearing sources and every integer J>=1.')
print('With shifts J ell and 2J ell and strengths J sqrt(30), 2J sqrt(10), off-center Raman edges are O(J) while viscosity is O(J^2 n^2).')
print('The leading center Schur Rayleigh form is (8/6699) C with C<1/4 on every desired target and C>1 on p1,g2,g3,r1.')
print('Scope: exact geometry and leading coefficient; the operator-norm Schur remainder and nonlinear realization are separate steps.')
