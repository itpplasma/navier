#!/usr/bin/env python3
"""Exact parent-polarization obstruction for canceling both cubic extremes.

At the first designated source pair, write each parent polarization as
    a_+(s_j)+r_j a_-(s_j).
The complete cubic growing coefficients at the two extreme sidebands factor
as (r1+1)F1(r1,r2) and (r2+1)F2(r1,r2).  This checker proves the simultaneous
zeros are only the interaction-killing point (-1,-1) and one order-one stable
admixture point.
"""
import sympy as s

r1,r2=s.symbols('r1 r2', real=True)
A=s.sqrt(370); B=s.sqrt(2146); C=s.sqrt(1345); D=s.sqrt(7801)
F1=(11+20*A+9*B)*r1*r2+(-9*B+11+20*A)*r1+(-20*A+11+9*B)*r2+(-9*B-20*A+11)
F2=(-7+9*C+4*D)*r1*r2+(-4*D-7+9*C)*r1+(-9*C-7+4*D)*r2+(-4*D-9*C-7)

# Resultant in r2.  The exact factorization has only r1=-1 and one other
# real algebraic value.
R=s.factor(s.resultant(F1,F2,r2))
E=s.sqrt(2886370); G=63*s.sqrt(2146)+44*s.sqrt(7801)
expected=-2*(r1+1)*((-E+G)*r1+(E+G))
assert s.simplify(R-expected)==0
r1star=s.simplify(-(E+G)/(G-E))
# Recover r2 from the first bilinear equation.
r2star=s.simplify(-(( -9*B+11+20*A)*r1star+(-9*B-20*A+11)) /
                    ((11+20*A+9*B)*r1star+(-20*A+11+9*B)))
assert s.simplify(F1.subs({r1:r1star,r2:r2star}))==0
assert s.simplify(F2.subs({r1:r1star,r2:r2star}))==0

# Exact coarse size bounds for the nontrivial root.  SymPy's real radical
# comparisons are algebraic, not floating-point tests.
assert r1star < -s.Rational(3,2)
assert -s.Rational(3,4) < r2star < -s.Rational(1,2)

# The other simultaneous zero r1=r2=-1 makes both parent polarizations
# parallel to e_y: a_+-a_-=(0,-2q,0).  Since both wavevectors lie in the xz
# plane, every dot product driving their pair interaction is zero.
s1=s.Rational(1,2); s2=-s.Rational(2,5)
q1=s.sqrt(1+s1*s1); q2=s.sqrt(1+s2*s2)
p1=s.Matrix([s1,0,1]); p2=s.Matrix([s2,0,1])
a1=s.Matrix([0,-2*q1,0]); a2=s.Matrix([0,-2*q2,0])
assert a1.dot(p2)==0 and a2.dot(p1)==0

print('PASS: both cubic extreme pollutants cannot be canceled by a small stable-branch polarization tweak.')
print('Simultaneous zeros: the interaction-killing point r1=r2=-1, or one nontrivial point with r1<-3/2 and -3/4<r2<-1/2.')
print('Thus every nontrivial cancellation uses order-one decaying eigenbranch content at the parent frequencies.')
