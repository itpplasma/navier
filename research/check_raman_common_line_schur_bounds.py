#!/usr/bin/env python3
"""Exact constants behind the common-line Raman Schur-complement theorem.

For the finite load-bearing carrier frequencies, the common-line lattice
k_n=k+n J ell has a uniform viscous gap on every n!=0 sector.  With the
4096-strength two-axis modules, the D^{-1/2} S D^{-1/2} complement coupling is
O(J^{-1}), so the complement inverse differs from -D^{-1} by O(J^{-3}) and its
feedback to the center differs from the first-star Schur term by O(J^{-1}).

The full inherited ladder is handled separately: every translated frequency
has distance at least |r_n x ell|/|ell| from zero, which is > n/sqrt(2).
"""
from __future__ import annotations
import sympy as sp

z,J,n=sp.symbols('z J n',real=True,positive=True)
Qclean=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
lo=sp.Rational(12847,10000); hi=sp.Rational(803,625)
assert Qclean.eval(lo)<0 and Qclean.eval(hi)>0 and Qclean.count_roots(lo,hi)==1

ell=sp.Matrix([-13,-61,53]); L2=ell.dot(ell)
assert L2==6699
QA=sp.Matrix([-1,-5,-6]); QB=sp.Matrix([10,-3,-1])
assert QA.dot(ell)==0 and QB.dot(ell)==0

finite_k=[
 ('h+',sp.Matrix([-z,1,1])),
 ('h0',sp.Matrix([z-2,-1,-1])),
 ('h-',sp.Matrix([-z,-1,1])),
 ('p1',sp.Matrix([1,0,0])),
 ('p2',sp.Matrix([0,1,0])),
 ('p3',sp.Matrix([-z,0,1])),
 ('g1',sp.Matrix([-1,-1,0])),
 ('g2',sp.Matrix([1+z,0,-1])),
 ('g3',sp.Matrix([1-z,0,1])),
]

def assert_positive_on_clean(expr,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    p=sp.Poly(num,z)
    mid=(lo+hi)/2
    assert p.count_roots(lo,hi)==0,label
    assert p.eval(mid)>0,label
    assert den.subs(z,mid)>0,label

# Uniform elementary bounds for all finite carrier frequencies.
for name,k in finite_k:
    assert_positive_on_clean(9-k.dot(k),name+': |k|<3')
    s=sp.expand(k.dot(ell))
    assert_positive_on_clean(131-s,name+': k.ell<131')
    assert_positive_on_clean(131+s,name+': k.ell>-131')

# For r=nJ with integer |n|>=1,
# |k+r ell|^2=|k|^2+r^2 L2+2r k.ell
# >= |k|^2+(L2-2|k.ell|)r^2 >6437 r^2.
assert L2-2*131==6437

# Unit-axis projection obeys |q.k|<=|k|<3.  The two module strengths are
# alpha_A=64 J sqrt(30), alpha_B=128 J sqrt(10), both <405 J.
assert 64**2*30 < 405**2
assert 128**2*10 < 405**2
# Hence every unnormalized Raman edge has norm <2*405*3 J=2430 J.
assert 2*405*3==2430
assert sp.Rational(2430,6437)<sp.Rational(2,5)
# On the complement, after D^{-1/2} balancing, each of the at most four
# +/-1,+/-2 edges has norm <(2/5)/(J |n n'|), hence the row/column Schur bound
# is <=8/(5J).  For J>=4 this is <=2/5.
assert sp.Rational(8,5*4)<=sp.Rational(2,5)

# With T=D^{-1/2} S_cc D^{-1/2}, J>=4 gives
# ||(I-T)^{-1}-I|| <= ||T||/(1-||T||) <= 8/(3J).
# Since ||D_c^{-1/2}||^2 <=1/(6437 J^2),
# ||(-D_c+S_cc)^{-1}+D_c^{-1}|| <=8/(19311 J^3).
assert 3*6437==19311

# Center-to-complement has four destination blocks.  A crude exact bound is
# ||B||^2 <=72(alpha_A^2+alpha_B^2)<25,000,000 J^2.
B2=72*(64**2*30+128**2*10)
assert B2==20643840 and B2<25000000
# Therefore the correction caused by complement-complement Raman edges is at
# most (B2*8/19311)/J < 9000/J.
assert sp.Rational(B2*8,19311)<9000

# Full inherited ladder: k=(-N,-1,0).  Translation by any real multiple of
# ell preserves k x ell, so every point of the line has squared norm at least
# |k x ell|^2/|ell|^2.  This lower bound exceeds N^2/2 for every N>=1.
N=sp.symbols('N',integer=True,positive=True)
kr=sp.Matrix([-N,-1,0])
cross2=sp.factor(kr.cross(ell).dot(kr.cross(ell)))
assert cross2==2*(3265*N**2-793*N+1489)
margin=sp.expand(2*cross2-L2*N**2)  # equivalent to cross2/L2 > N^2/2
assert margin==6361*N**2-3172*N+5956
# Positive for all N>=1; derivative is already positive at 1 and value at 1>0.
assert margin.subs(N,1)>0
assert sp.diff(margin,N).subs(N,1)>0

print('PASS: exact common-line Schur scaling bounds.')
print('Finite carrier complements: D_n>6437 J^2 n^2, ||D^-1/2 S_cc D^-1/2||<=8/(5J), and complement-feedback remainder <9000/J.')
print('Inherited ladder: every translated frequency has |k|^2>N^2/2, uniformly over the whole common-line Raman lattice.')
