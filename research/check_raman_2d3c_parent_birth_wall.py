#!/usr/bin/env python3
"""Exact leading cancellation for the first nonlinear Raman parent-birth repair.

Use the repository's exact 2D3C scalar/shear geometry to preload one scalar
Raman parent q=K e1+N e2 and a shear s=-2N e2.  The shear generates the missing
near-opposite scalar parent r=q+s=K e1-N e2 from zero.  This genuinely breaks
the initial q/r symmetry.

Nevertheless, after summing every cubic target-response tree at output
kappa=h+q+r=h+2K e1, the complete O(N) coefficient vanishes.  The cancellation
is proved directly in the leading fast-index symbol; it is not a numerical
Taylor fit.
"""
from __future__ import annotations
import sympy as sp

K,Ay,hx,hy,hz=sp.symbols('K Ay hx hy hz', nonzero=True, real=True)
e1=sp.Matrix([1,0,0]); e3=sp.Matrix([0,0,1])
h=sp.Matrix([hx,hy,hz])
a=e3
b=e1/K
q0=K*e1       # slow part of fast-index +1 scalar parent
s0=sp.zeros(3,1)  # slow part of fast-index -2 shear
r0=K*e1       # slow part of generated fast-index -1 scalar parent

def P(k,v):
    return sp.simplify(v-k*(k.dot(v))/k.dot(k))

def high_pair(n,k0,u,m,l0,v):
    """Leading N^0 coefficient of C(nNe2+k0,u;mNe2+l0,v).

    u,v are leading transverse polarizations with zero e2 component.  Exact
    transversality to the full high wavevectors supplies the longitudinal
    O(N^-1) corrections encoded by the two dot-product formulas below.
    If n+m=0 the output is slow and receives its exact final Leray projection.
    """
    n=sp.Integer(n); m=sp.Integer(m)
    uq=sp.simplify(u.dot(l0)-sp.Rational(m,n)*u.dot(k0))
    vp=sp.simplify(v.dot(k0)-sp.Rational(n,m)*v.dot(l0))
    w=sp.simplify(uq*v+vp*u)
    if n+m==0:
        return sp.simplify(P(k0+l0,w))
    return sp.simplify(w)

# Slow target -> high first-leg coefficients after dividing by N.
# For fast index m, N^-1 C(h,A;mNe2+k0,v) -> m A_y v.
Xq=Ay*a          # target + q, fast index +1
Xs=-2*Ay*b       # target + shear, fast index -2

# Background parent birth: C(q,a;s,b)=a at leading order, so r starts from zero
# with a nonzero linear-time coefficient.
U1r=high_pair(1,q0,a,-2,s0,b)
assert sp.simplify(U1r-a)==sp.zeros(3,1)

# Taylor coefficient V_2 at the target+r sideband.  It receives three pieces:
# q acting on the target+s sideband, s acting on target+q, and the newly born r
# acting directly on the target.  Their exact leading sum is -A_y e3.
V2r=sp.simplify((
    high_pair(1,q0,a,-2,h,Xs)
   +high_pair(-2,s0,b,1,h+q0,Xq)
   -Ay*a)/2)
assert sp.simplify(V2r+Ay*a)==sp.zeros(3,1)

# The double-q sideband has zero O(N) coefficient.
V22q=sp.simplify(high_pair(1,q0,a,1,h+q0,Xq)/2)
assert V22q==sp.zeros(3,1)

# Complete cubic coefficient at kappa=h+2K e1.  The three possible sources in
# the V_3 recurrence are q+V2r, s+V2(2q), and the born parent r+V1q.
T_q=high_pair(1,q0,a,-1,h+r0,V2r)
T_s=high_pair(-2,s0,b,2,h+2*q0,V22q)
T_r=high_pair(-1,r0,a,1,h+q0,Xq)
assert T_s==sp.zeros(3,1)
assert sp.simplify(T_q+T_r)==sp.zeros(3,1)
assert sp.simplify((T_q+T_s+T_r)/3)==sp.zeros(3,1)

# The cancellation is nontrivial when A_y h_z !=0: the two surviving trees are
# individually nonzero and exact negatives.
kappa=h+2*K*e1
expected=sp.simplify(-2*Ay*hz*P(kappa,a))
assert sp.simplify(T_q-expected)==sp.zeros(3,1)
assert sp.simplify(T_r+expected)==sp.zeros(3,1)

print('PASS: exact leading cancellation for 2D3C nonlinear parent birth.')
print('The missing -N parent is genuinely generated from zero, but the complete cubic target response has zero O(N) coefficient.')
print('The q+V2r and born-r+V1q trees are exact negatives; the double-q/shear tree vanishes at this order.')
print('Scope: leading high-frequency Taylor symbol.  A surviving residual is lower order and would require a new strong-scaling argument.')
