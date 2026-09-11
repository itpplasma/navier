#!/usr/bin/env python3
"""Exact instantaneous strain-filter inequalities for the clean dyadic gate.

The strain is an affine infinite-energy exact unforced NS background.  This
checker proves strict carrier-rate signs at the isolated positive circuit
root; it does not prove finite-time filtering, finite-energy localization,
or a regenerative turnover.
"""
from __future__ import annotations
import sympy as sp

CHECKS=[]
def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def rate(H,k,a):
    k=sp.Matrix(k); a=sp.Matrix(a)
    return sp.factor(-(a.T*H*a)[0]/a.dot(a)-k.dot(k))

def strict_sign_on_interval(expr,z,a,b,positive,label):
    num,den=map(sp.factor,sp.together(expr).as_numer_denom())
    pn=sp.Poly(num,z)
    check(pn.count_roots(a,b)==0,f'{label}: numerator has no zero in root interval')
    sgn=sp.sign(pn.eval(a))
    check(sgn==(1 if positive else -1),f'{label}: numerator endpoint sign')
    # Every denominator in this file is explicitly positive on R or on z>0;
    # the midpoint check is a regression guard, while positivity is recorded
    # analytically in the evidence note.
    check(den.subs(z,(a+b)/2)>0,f'{label}: denominator midpoint positive')

z=sp.symbols('z',real=True)
Q=sp.Poly(z**10-z**9+4*z**8+2*z**6-2*z**5-8*z**3-32*z**2+40*z-16,z)
a=sp.Rational(12847,10000); b=sp.Rational(803,625) # 1.2847, 1.2848
check(Q.eval(a)<0 and Q.eval(b)>0,'Q changes sign on exact rational interval')
check(Q.count_roots(a,b)==1,'root interval contains exactly one Q root')

H=sp.Matrix([
 [sp.Rational(11,2),sp.Rational(-33,4),-1],
 [sp.Rational(-33,4),-3,sp.Rational(33,4)],
 [-1,sp.Rational(33,4),sp.Rational(-5,2)],
])
check(H==H.T,'H symmetric')
check(sp.trace(H)==0,'H trace free')

Dplus=z**2+2*z+2; Dminus=z**2-2*z+2
parents=[
 ('p1',(1,0,0),(0,1,z)),
 ('p2',(0,1,0),(1,0,z)),
 ('p3',(-z,0,1),(1,0,z)),
]
selected=[
 ('s1',(-1,-1,0),(0,0,-2*z)),
 ('s2',(1+z,0,-1),(-z**3/Dplus,1,-z**3*(z+1)/Dplus)),
 ('s3',(1-z,0,1),( z**3/Dminus,1, z**3*(z-1)/Dminus)),
]
rates={name:rate(H,k,v) for name,k,v in selected+parents}
check(rates['s1']==sp.Rational(1,2),'selected vertical child has exact rate 1/2')
for name,_,_ in selected:
    strict_sign_on_interval(rates[name],z,a,b,True,name)
for name,_,_ in parents:
    strict_sign_on_interval(rates[name],z,a,b,False,name)

# Every inherited-parent ladder mode r_n=-n k1-k2 has polarization e3.
# Its normalized rate is 5/2-(n^2+1)=3/2-n^2.
n=sp.symbols('n',integer=True,positive=True)
e3=sp.Matrix([0,0,1])
rn=sp.Matrix([-n,-1,0])
ladder=sp.factor(-(e3.T*H*e3)[0]-rn.dot(rn))
check(ladder==sp.Rational(3,2)-n**2,'exact all-n ladder rate')
check(ladder.subs(n,2)==sp.Rational(-5,2),'first pollutant ladder rate -5/2')

# Freeze useful exact formulas.
check(rates['p1']==(3*z**2-33*z+4)/(2*(z**2+1)),'parent p1 exact rate')
check(rates['p2']==(3*z**2+4*z-13)/(2*(z**2+1)),'parent p2 exact rate')
check(rates['p3']==-(2*z**4-z**2-4*z+13)/(2*(z**2+1)),'parent p3 exact rate')

print(f'PASS: {len(CHECKS)} exact assertions.')
print('At the unique Q-root in (1.2847,1.2848): selected children grow, all parents decay, and every ladder n>=2 decays.')
print('Scope: instantaneous affine-strain spectral filter only; no finite-energy/localized turnover claim.')
