#!/usr/bin/env python3
"""Exact checks for smooth loss of kinetic stress realizability in BDNK.
No PDE integration. The uniform local-existence step remains analytic.
"""
from collections import Counter
import sympy as s
counts=Counter()
def check(label,a,b=0):
    d=a-b; entries=list(d) if isinstance(d,s.MatrixBase) else [d]
    if any(s.simplify(z)!=0 for z in entries):raise AssertionError((label,d))
    counts[label]+=1

def stress(u,j,ell,eta,chi,lam):
    metric=s.diag(-1,1,1,1); delta=metric+u*u.T
    theta=s.trace(j); Du=j.T*u
    A=chi*(3*u.dot(ell)+theta); Q=lam*(Du+delta*ell)
    sig=delta*(j*metric+metric*j.T)*delta/2-theta*delta/3
    out=(1+A)*(u*u.T+delta/3)+u*Q.T+Q*u.T-2*eta*sig
    return out,A,Q,sig

eta,chi,lam,q,d=s.symbols('eta chi lam q d',positive=True)
# Rational rapidity charts keep the direct tensor calculation exact and fast.
for n in range(2,8):
    z=s.Rational(1,n);g=(1+z*z)/(1-z*z);p=2*z/(1-z*z)
    f=3*g/(3+2*p*p)
    theta=f*(d+p*q/lam);rt=f*(q/lam-2*p*d/3);Lt=-theta/(3*g)
    u=s.Matrix([g,p,0,0]); normal=s.Matrix([p,g,0,0]);j=s.zeros(4)
    j[0,:]=(rt*normal).T;j[1,:]=(d*normal).T
    out,A,Q,sig=stress(u,j,s.Matrix([Lt,0,0,0]),eta,chi,lam)
    pl=(1-4*eta*theta)/3;pt=(1+2*eta*theta)/3
    boost=s.Matrix([[g,p,0,0],[p,g,0,0],[0,0,1,0],[0,0,0,1]])
    target=boost*s.Matrix([[1,q,0,0],[q,pl,0,0],[0,0,pt,0],[0,0,0,pt]])*boost.T
    check('full prepared tensor',out,target)
    check('zero scalar correction',A)
    check('prescribed heat flux',Q,q*normal)
    check('expansion identity',s.trace(j),theta)
# Origin time jet obtained from both conservation equations, not a shear truncation.
a,B,delta=s.symbols('a B delta',real=True)
Lt=-a/3; eta_t=3*eta*Lt;theta_t=B/lam-2*a*a/3
E_t=-(s.Rational(4,3)*a-s.Rational(4,3)*eta*a*a+B)
pl_t=E_t/3-s.Rational(4,3)*(eta_t*a+eta*theta_t)
check('origin pressure jet',pl_t,-4*a/9+8*eta*a*a/3-B*(lam+4*eta)/(3*lam))
Bchoice=lam/(3*eta*(lam+4*eta));achoice=(1-3*delta)/(4*eta)
check('negative origin derivative',pl_t.subs({a:achoice,B:Bchoice}),(-1-12*delta+27*delta**2)/(18*eta))
check('boundary derivative',pl_t.subs({a:1/(4*eta),B:Bchoice}),-1/(18*eta))
# Exact parameter checks for both causal frames, with k=4/eta.
for L in [s.Rational(25,3),s.Rational(25,7)]:
    b=s.factor(Bchoice.subs(lam,L*eta)); k=4/eta
    # |q|/|sin(kx)|=B/k is <1/8; cosh(|r|)<2 gives the other bound.
    assert s.simplify(b/k)<s.Rational(1,8);counts['small flux bound']+=1
    assert s.simplify(2*b/(L*eta*k*k))<s.Rational(1,4);counts['expansion upper bound']+=1
# Universal bounds hold for any positive lambda at k=4/eta.
y=s.symbols('y',positive=True)
qamp=y/(12*(y+4))
check('universal flux margin',s.Rational(1,12)-qamp,1/(3*(y+4)))
check('universal expansion margin',s.Rational(1,4)-1/(24*(y+4)),(6*y+23)/(24*(y+4)))
# Direct differentiation of the prescribed initial rapidity time derivative.
r,qq,dd=s.symbols('r qq dd',real=True)
f=3*s.cosh(r)/(3+2*s.sinh(r)**2)
rt=f*(qq/lam-s.Rational(2,3)*s.sinh(r)*dd)
rxt=(s.diff(rt,r)*a+s.diff(rt,qq)*B).subs({r:0,qq:0,dd:a})
check('differentiated Cauchy jet',rxt,B/lam-2*a*a/3)
# The scalar inequalities used uniformly over the spatial phase.
x=s.symbols('x',real=True)
check('positive-cosine deficit',1-x-(1-x*x)/4-(1-x)/2,(1-x)**2/4)
check('PSD margin',s.Rational(1,24)-s.Rational(1,64),s.Rational(5,192))
check('negative-cosine PSD margin',s.Rational(1,3)-s.Rational(1,64),s.Rational(61,192))
check('transverse pressure margin',(1-2*eta*s.Rational(5,4)*(1/(4*eta)))/3,s.Rational(1,8))
check('origin initial pressure',(1-4*eta*achoice)/3,delta)
check('exit time integration',delta-72*eta*delta/(36*eta),-delta)
# The added cosine preserves the origin jet and ensures initial entropy positivity.
x,k=s.symbols('x k',real=True)
check('heat profile derivative',s.diff((B/k)*s.sin(k*x)*s.cos(k*x),x).subs(x,0),B)
g=s.symbols('g',real=True)
check('rapidity factor lower bound',6*g-1-2*g*g,3+2*(g-1)*(2-g))
check('initial entropy margin',s.Rational(4,3)-s.Rational(16,27),s.Rational(20,27))
# Explicit positive two-circle angular measure realizing the initial moments.
z,m=s.symbols('z m',positive=True); wplus=(1+m/s.sqrt(z))/2;wminus=(1-m/s.sqrt(z))/2
check('kinetic total weight',wplus+wminus,1)
check('kinetic first moment',s.sqrt(z)*(wplus-wminus),m)
check('kinetic longitudinal pressure',z*(wplus+wminus),z)
check('kinetic transverse pressure',(1-z)/2*(wplus+wminus),(1-z)/2)
# Euclidean positive semidefiniteness is stronger than DEC.
check('DEC-only nonrealizable control',s.Rational(1,3)-s.Rational(5,8)**2,-s.Rational(11,192))
for label,n in counts.items():print(f'PASS: {label}: {n}')
print(f'TOTAL: {sum(counts.values())} exact checks passed')
print('SCOPE: full four-tensor, spatial cone margins, conserved time jets, positive moment representation.')
print('NOT CHECKED: local-existence theorem replay, independent review, Lean, or CI.')
