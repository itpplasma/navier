#!/usr/bin/env python3
"""Exact reference exponent for carrying the old z=1 parents to z=1/2."""
import sympy as s

h=s.symbols('h', positive=True)
x=s.symbols('x', positive=True)
mu=s.Rational(3,5)
parents=[s.Rational(1,2),-s.Rational(2,5),s.Rational(1,5),-s.Rational(1,10)]

# One factor-two normalization interval: rho^(-h)=4.
rho=s.symbols('rho', positive=True)
# For an old physical parent, normalized z(x)=x^(h/2), so z^2=x^h.
# Integral x^(-1-h)[a-b*x^h] from rho to 1 with rho^(-h)=4 and
# log(1/rho)=2 log(2)/h equals [3a-2b log 2]/h.
for sig in parents:
    a=s.simplify(1/s.sqrt(1+sig*sig))
    b=s.simplify(mu*(1+sig*sig))
    B=s.simplify(3*a-2*b*s.log(2))
    # Uniform exact lower bound for |sig|<=1/2:
    # a>=2/sqrt(5), b<=3/4, log2<1, hence B>6/sqrt5-3/2>9/10.
    assert abs(sig)<=s.Rational(1,2)
    assert s.simplify(a-2/s.sqrt(5))>=0
    assert s.simplify(s.Rational(3,4)-b)>=0
    assert s.log(2)<1
    assert 6/s.sqrt(5)-s.Rational(3,2)>s.Rational(9,10)
    assert B>s.Rational(9,10)

# Exact geometric subsequence certifying Q^(-h)/L -> infinity for an
# admissible fixed h.  Let h=1/200, ell=400 k, Q=2^-ell, L=ell^2.
# Then Q^-h=4^k and the ratio to L grows geometrically eventually.
rows=[]
for k in range(2,30):
    ell=400*k
    qmh=4**k
    L=ell*ell
    R=s.Rational(qmh,L)
    rows.append(R)
for i in range(len(rows)-1):
    k=i+2
    # R_(k+1)/R_k = 4 k^2/(k+1)^2 >=16/9 for k>=2.
    ratio=s.simplify(rows[i+1]/rows[i])
    assert ratio==s.Rational(4*k*k,(k+1)*(k+1))
    assert ratio>=s.Rational(16,9)
assert rows[-1]>10**8

# Therefore any quasi-Gaussian stage amplitude exp(-C L) is overwhelmed by
# passive parent carry exp(+c Q^-h).  The checker freezes only the exact
# exponent/sign and scale separation; the amplitude consequence is analytic.
print('PASS: old parent carry to half-grade has uniformly positive reference exponent.')
print('For every caged parent, I >= (9/(10 h)) Q^(-h) up to the fixed positive source-coordinate factor.')
print('Since Q^(-h)/L -> infinity for L~ell^2, exp(-C L) parent scales cannot remain small under passive factor-two carry.')
print('Scope: continuously self-similar reference carry; nonlinear cancellation/regeneration and the full physical adapter remain open.')
