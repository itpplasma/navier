#!/usr/bin/env python3
"""Exact Farkas obstruction to one common reality-complete Raman filter.

At the clean algebraic return root there is no real symmetric trace-free strain
S (with its strength absorbed into S) that simultaneously:
  * grows the required h_- selected carrier; and
  * damps p1, g2, g3, the n=1 inherited-ladder carrier, and the
    reality-generated h0+(2,0) active Raman sideband,
with ordinary viscosity retained.

The certificate is computed exactly in Q[z]/(Qclean). Six nonnegative Farkas
multipliers annihilate the five strain coordinates and have negative weighted
right-hand side throughout the isolated clean-root interval.
"""
from __future__ import annotations
import itertools
import sympy as sp

z=sp.symbols('z',real=True)
Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z,domain=sp.QQ)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Q.eval(lo)<0 and Q.eval(hi)>0 and Q.count_roots(lo,hi)==1

# Arithmetic in the exact algebraic number field represented as Q[z]/Qclean.
def red(expr):
    num,den=sp.cancel(expr).as_numer_denom()
    nump=sp.Poly(num,z,domain=sp.QQ)
    denp=sp.Poly(den,z,domain=sp.QQ)
    return (nump*sp.invert(denp,Q)).rem(Q)
def add(a,b): return (a+b).rem(Q)
def sub(a,b): return (a-b).rem(Q)
def mul(a,b): return (a*b).rem(Q)
def neg(a): return (-a).rem(Q)
ZERO=sp.Poly(0,z,domain=sp.QQ)
ONE=sp.Poly(1,z,domain=sp.QQ)

def det_field(A):
    n=len(A); out=ZERO
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=ONE
        for i,j in enumerate(p):
            term=mul(term,A[i][j])
        out=sub(out,term) if inv%2 else add(out,term)
    return out

def qcoords(v):
    """Coordinates of (v^T S v)/|v|^2 for
       S33=-S11-S22 and variables (S11,S22,S12,S13,S23)."""
    n=sp.expand(v.dot(v))
    return [
      (v[0]**2-v[2]**2)/n,
      (v[1]**2-v[2]**2)/n,
      2*v[0]*v[1]/n,
      2*v[0]*v[2]/n,
      2*v[1]*v[2]/n,
    ]

def k2(k): return sp.expand(k.dot(k))

# Required clean h_- target.
k_hm=sp.Matrix([-z,-1,1])
v_hm=sp.Matrix([
 -2*z**2*(z**2-2)/(3*(z**2+2)),
 -2*z**3*(z**2-4*z+2)/(3*(z**2+2)*(z**2-2*z+2)),
 -2*z**3*(z**4-2*z**3+z**2-2)/(3*(z**2+2)*(z**2-2*z+2)),
])

# Older carriers that the inheritance filter must suppress.
k_p1=sp.Matrix([1,0,0]); v_p1=sp.Matrix([0,1,z])
Dp=z**2+2*z+2; Dm=z**2-2*z+2
k_g2=sp.Matrix([1+z,0,-1])
v_g2=sp.Matrix([-z**3/Dp,1,-z**3*(z+1)/Dp])
k_g3=sp.Matrix([1-z,0,1])
v_g3=sp.Matrix([z**3/Dm,1,z**3*(z-1)/Dm])
k_r1=sp.Matrix([-1,-1,0]); v_r1=sp.Matrix([0,0,1])

# Reality-complete single-axis Raman lattice:
# l5=(0,1,-7) and -l4=(0,1,7) give the depth-two offset (0,2,0).
# From h0=(z-2,-1,-1) this reaches k_c=(z-2,1,-1).
# Every translated active polarization is P_k e1; denominator-free this is
# |k|^2 P_k e1=(y^2+c^2,-xy,-xc)=(2,-x,x).
x=z-2
k_c=sp.Matrix([x,1,-1]); v_c=sp.Matrix([2,-x,x])

# Inequalities a_i.S <= b_i.
# Growth: -q_S-|k|^2 >=0  -> q_S <= -|k|^2.
# Damping: -q_S-|k|^2 <=0 -> -q_S <= |k|^2.
rows=[
 ("grow-hminus", qcoords(v_hm), -k2(k_hm)),
 ("damp-p1",     [-u for u in qcoords(v_p1)], k2(k_p1)),
 ("damp-g2",     [-u for u in qcoords(v_g2)], k2(k_g2)),
 ("damp-g3",     [-u for u in qcoords(v_g3)], k2(k_g3)),
 ("damp-r1",     [-u for u in qcoords(v_r1)], k2(k_r1)),
 ("damp-real-depth2-h0",[-u for u in qcoords(v_c)], k2(k_c)),
]
Acols=[[red(u) for u in coeffs] for _,coeffs,_ in rows]
b=[red(rhs) for _,_,rhs in rows]
Arows=[[Acols[j][i] for j in range(6)] for i in range(5)]

# Cofactor null vector for the 5x6 constraint-normal matrix.
lam=[]
for j in range(6):
    minor=[[Arows[i][k] for k in range(6) if k!=j] for i in range(5)]
    c=det_field(minor)
    if j%2: c=neg(c)
    lam.append(neg(c))  # common orientation chosen positive at the clean root

# Exact annihilation in Q[z]/(Qclean).
for i in range(5):
    s=ZERO
    for j in range(6):
        s=add(s,mul(Arows[i][j],lam[j]))
    assert s.is_zero

# Every multiplier is strictly positive throughout the clean isolating interval.
mid=(lo+hi)/2
for name,mu in zip([r[0] for r in rows],lam):
    assert mu.count_roots(lo,hi)==0, name
    assert mu.eval(mid)>0, name

# Weighted RHS is strictly negative throughout the same interval.
F=ZERO
for mu,rhs in zip(lam,b):
    F=add(F,mul(mu,rhs))
assert F.count_roots(lo,hi)==0
assert F.eval(mid)<0

# At the actual clean root, summing the six inequalities with positive
# multipliers would give 0 <= F(z_*) < 0, impossible.
print("PASS: exact Farkas certificate in Q[z]/(Qclean).")
print("All six multipliers are positive on the clean-root interval and annihilate all five trace-free strain coordinates.")
print("Their weighted viscous right-hand side is strictly negative.")
print("Therefore no common symmetric trace-free strain of any strength can grow h_- while damping p1,g2,g3,r1 and the reality-generated depth-two h0 sideband.")
