#!/usr/bin/env python3
"""Exact cross-module high-high obstruction for the current Raman basis.

At the scaling needed for order-one effective Raman action, rho^2/R=O(1),
the independent-pump approximation requires cross-module high-high sidebands
to remain perturbative.  Two explicit modules violate this: their leading
Leray coefficient is nonzero and the second-Picard cross sideband is larger
than a parent by a factor asymptotic to rho.
"""
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def P(k,v): return sp.simplify(v-k*(k.dot(v))/k.dot(k))
def C(p,a,q,b): return P(p+q,(a.dot(q))*b+(b.dot(p))*a)

# First two modules of the all-orders-safe effective basis.  beta_0=l+Qxl is
the leading high polarization as N->infinity.
l1=sp.Matrix([-3,-3,1]); Q1=sp.Matrix([1,-2,-3]); b1=l1+Q1.cross(l1)
l2=sp.Matrix([-3,-2,2]); Q2=sp.Matrix([0,1,1]);  b2=l2+Q2.cross(l2)
check(Q1.dot(b1)==0,'module 1 leading parent transverse')
check(Q2.dot(b2)==0,'module 2 leading parent transverse')
check(b1==sp.Matrix([-14,5,-8]),'module 1 leading polarization')
check(b2==sp.Matrix([1,-5,5]),'module 2 leading polarization')

cross=sp.Matrix([sp.factor(x) for x in C(Q1,b1,Q2,b2)])
check(cross==sp.Matrix([49,-1,25]),'nonzero exact cross-module Leray coefficient')
check(Q1.dot(Q1)==14,'first parent heat exponent 14')
check(Q2.dot(Q2)==2,'second parent heat exponent 2')
K=Q1+Q2
check(K==sp.Matrix([1,-1,-2]),'cross sideband direction')
check(K.dot(K)==6,'cross sideband heat exponent 6')
Delta=Q1.dot(Q1)+Q2.dot(Q2)-K.dot(K)
check(Delta==10,'cross Duhamel heat gap 10')

# At t=tau/(nu N^2), parents of common physical velocity size P0 produce
# the exact Stokes-Duhamel second-Picard sideband
#   (P0^2/(nu N)) * cross * (e^{-6tau}-e^{-16tau})/10.
# Relative to P0 this is rho times a fixed nonzero vector, rho=P0/(nu N).
tau=sp.symbols('tau',positive=True)
shape=sp.simplify((sp.exp(-6*tau)-sp.exp(-16*tau))/10)
check(sp.limit(shape,tau,0,dir='+')==0,'cross sideband starts at zero')
check(sp.simplify(sp.diff(shape,tau).subs(tau,0)-1)==0,'cross sideband has nonzero initial slope')
check(shape.subs(tau,sp.Rational(1,10))>0,'fixed positive-time cross factor nonzero')

# Useful Raman coupling has gamma=rho^2/R bounded below.  Hence for R->infty,
# rho>=sqrt(gamma R)->infinity and this relative cross sideband is unbounded.
R,gamma=sp.symbols('R gamma',positive=True)
rho_lower=sp.sqrt(gamma*R)
check(sp.limit(rho_lower,R,sp.oo)==sp.oo,'order-one Raman scaling forces rho to infinity')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('Current five-module high background is not a perturbation of independent heat pumps at rho^2/R=O(1).')
print('Explicit cross sideband/parent ratio = rho*(e^{-6 tau}-e^{-16 tau})*(49,-1,25)/10.')
print('Scope: obstruction to the present independent-pump realization only; nonlinear-silent high backgrounds remain open.')
