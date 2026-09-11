#!/usr/bin/env python3
"""Exact small-time wall for the pre-existing sequential two-shear purifier.

The earlier sequential theorem proves that its exact two-pulse Kelvin map has
first log-energy variation 2 R_H for every fixed input carrier.  A
reality-generated depth-two single-axis Raman sideband has R_H>0 throughout the
clean-root interval, so that same two-pulse schedule necessarily amplifies this
clutter mode for every sufficiently small positive duration.

The file also freezes the general commuting/frozen-carrier observation: any
finite sequence of strains reduces at log-rate level to its duration-weighted
average, so time alternation without geometric transport cannot evade the
Farkas obstruction.
"""
from __future__ import annotations
import sympy as sp

z=sp.symbols('z',real=True)
Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Q.eval(lo)<0 and Q.eval(hi)>0 and Q.count_roots(lo,hi)==1

H=sp.Matrix([
 [sp.Rational(71,100),-1,sp.Rational(147,200)],
 [-1,sp.Rational(-143,200),sp.Rational(7,25)],
 [sp.Rational(147,200),sp.Rational(7,25),sp.Rational(1,200)],
])
M=sp.Integer(2048)
x=z-2
k=sp.Matrix([x,1,-1])
v=sp.Matrix([2,-x,x])  # denominator-free P_k e1
qH=sp.factor((v.T*H*v)[0]/v.dot(v))
R=sp.factor(-M*qH-k.dot(k))

assert qH == -(127*z**2-1202*z+1612)/(200*(z**2-4*z+6))
assert R == -(25*z**4-200*z**3-31812*z**2+306512*z-411772)/(25*(z**2-4*z+6))
num,den=map(sp.factor,sp.together(R).as_numer_denom())
p=sp.Poly(num,z)
mid=(lo+hi)/2
assert p.count_roots(lo,hi)==0
assert p.eval(mid)>0
assert den.subs(z,mid)>0
# Therefore R_H(k,v)>0 throughout the clean-root interval.  By the already
# proved sequential theorem d/dtau log E_seq|_0=2 R_H, this carrier grows for
# all sufficiently small positive tau.

# Frozen-carrier multi-stage identity.  For any fixed carrier and stages with
# durations t_j, q is linear in the strain, hence
# sum_j t_j[-q_{S_j}(v)-|k|^2]
# = -q_{sum_j t_j S_j}(v) - (sum_j t_j)|k|^2.
t1,t2,k2,q1,q2=sp.symbols('t1 t2 k2 q1 q2',real=True)
lhs=t1*(-q1-k2)+t2*(-q2-k2)
rhs=-(t1*q1+t2*q2)-(t1+t2)*k2
assert sp.expand(lhs-rhs)==0

print('PASS: the reality-generated depth-two h0 sideband has R_H>0 on the entire clean-root interval.')
print('Hence the repository two-shear sequential purifier amplifies it for all sufficiently small positive durations.')
print('Frozen-carrier multistage alternation collapses exactly to the duration-weighted average strain and cannot evade the Farkas wall.')
