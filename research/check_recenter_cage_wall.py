#!/usr/bin/env python3
"""Exact obstruction to recentering a deformed four-parent source cage.

Scope: source-reference phase geometry.  This does not rule out a transition
through modes outside the z=1 four-growing-parent class.
"""
import sympy as s

c=s.Rational(1,20)
uA=s.Rational(9,20)
uB=s.Rational(3,20)
a=s.symbols('a', positive=True)

# At fast-time ratio tau=v/L, a=1+tau.  The four z=1 tilts are centered at c
# with deviations +/-a*uA and +/-a*uB.
def tilts(scale):
    return [c+scale*uA,c-scale*uA,c+scale*uB,c-scale*uB]

frozen=tilts(s.Integer(1))
deformed=tilts(a)

# Exact recenter into the SAME proved rational cage, allowing arbitrary
# permutation of the four parents.  Equality of multisets forces a^2=1 from
# the second centered moment; for a>0 this gives a=1.
M2_f=s.expand(sum((x-c)**2 for x in frozen))
M2_a=s.expand(sum((x-c)**2 for x in deformed))
assert s.factor(M2_a-a*a*M2_f)==0
assert M2_f>0
assert s.solve(s.Eq(M2_a,M2_f),a)==[1]

# The common daughter fixes the center: each symmetric pair sums to 2c.
assert s.simplify(deformed[0]+deformed[1]-2*c)==0
assert s.simplify(deformed[2]+deformed[3]-2*c)==0

# Even if the recentered geometry is allowed to inherit the enlarged
# separation, four-growing-parent hyperbolicity cannot persist indefinitely.
# The existing spectral-cage theorem certifies gamma_+(z=1,s=7/10)<0.
# The outer positive parent reaches exactly 7/10 at a=13/9.
a_wall=s.Rational(13,9)
s_outer=s.simplify(c+a_wall*uA)
assert s_outer==s.Rational(7,10)
mu=s.Rational(3,5)
gamma=lambda sig: 1/s.sqrt(1+sig*sig)-mu*(1+sig*sig)
wall_rate=s.simplify(gamma(s_outer))
# Exact sign by squaring positive quantities: 10/sqrt(149) < 447/500.
assert s.simplify(wall_rate-(10/s.sqrt(149)-s.Rational(447,500)))==0
assert 100*500 < 447*s.sqrt(149)  # equivalent after multiplying by positives
# SymPy can certify the sign directly as well.
assert wall_rate.is_negative

# For a>=13/9, s_outer increases and gamma_+ strictly decreases with |s|, so
# this parent remains stable.  Check derivative in q=sqrt(1+s^2):
q=s.symbols('q', positive=True)
f=1/q-mu*q*q
assert s.simplify(s.diff(f,q)) == -1/q**2-s.Rational(6,5)*q

print('PASS: exact recenter-cage obstruction.')
print('Same proved four-parent cage can be recentered exactly only at zero forward fast shift (a=1).')
print('Allowing the separations to follow the frame, the outer parent reaches tilt 7/10 at a=13/9 and is then linearly stable.')
print('Scope: excludes recentered propagation that stays in the z=1 four-growing-parent class; transitions through other grades/modes remain open.')
