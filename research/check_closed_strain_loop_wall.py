#!/usr/bin/env python3
"""Exact quadratic-action wall for closed affine strain loops.

For a trace-free symmetric affine strain history with deformation gradient
F(T)=I, linearized vorticity returns to its initial carrier with scalar
attenuation exp(-nu J(k)), J(k)=k^T M k for an SPD matrix M.  This checker
freezes the parallelogram obstruction for the clean dyadic children k1+-k3.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

m11,m22,m33,m12,m13,m23=sp.symbols('m11 m22 m33 m12 m13 m23',real=True)
M=sp.Matrix([[m11,m12,m13],[m12,m22,m23],[m13,m23,m33]])
z=sp.symbols('z',real=True)
k1=sp.Matrix([1,0,0]); k3=sp.Matrix([-z,0,1])
def J(k): return sp.expand((k.T*M*k)[0])

jm=J(k1-k3); jp=J(k1+k3); j1=J(k1); j3=J(k3)
check(sp.expand(jm+jp-2*j1-2*j3)==0,'parallelogram identity')

# Under M positive definite, j1,j3>0.  If both selected children had smaller
# action than both parents, then jm<min(j1,j3), jp<min(j1,j3), contradicting
# jm+jp=2(j1+j3)>4 min(j1,j3).  The symbolic identity is the exact algebra;
# positivity is the analytic input from M=int F^-1 F^-T dt.

# The stronger average form used in the note:
avg=sp.factor((jm+jp)/2)
check(sp.expand(avg-j1-j3)==0,'selected mean action equals sum of parent actions')

print(f'PASS: {len(CHECKS)} exact symbolic assertions.')
print('For every SPD M, max(J(k1-k3),J(k1+k3)) >= J(k1)+J(k3) > max(J(k1),J(k3)).')
print('Scope: closed affine strain loops in the linearized problem only; open deformation/nonlinear/localized routes remain.')
