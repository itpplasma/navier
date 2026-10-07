#!/usr/bin/env python3
"""Exact algebra checks for the BDNK virial obstruction; not a PDE proof.
Run with Python 3 and SymPy. No network, numerical evolution, or Lean.
"""
from collections import Counter
import sympy as s

counts = Counter()
def check(group, a, b=0):
    d = a-b
    terms = list(d) if isinstance(d, s.MatrixBase) else [d]
    if any(s.simplify(z) != 0 for z in terms):
        raise AssertionError((group, d))
    counts[group] += 1

def positive(group, x):
    if not bool(x > 0):
        raise AssertionError((group,x))
    counts[group] += 1

def stress(u,j,ell,T,eta,chi,lam):
    g=s.diag(-1,1,1,1); delta=g+u*u.T
    theta=s.trace(j); Du=j.T*u
    A=chi*T**3*(3*u.dot(ell)+theta)
    Q=lam*T**3*(Du+delta*ell)
    sig=delta*(j*g+g*j.T)*delta/2-theta*delta/3
    out=(T**4+A)*(u*u.T+delta/3)+u*Q.T+Q*u.T-2*eta*T**3*sig
    return out,A,Q,sig

T,eta,chi,lam=s.symbols('T eta chi lam',positive=True)
# Exactly Euler-prepared Cauchy jets; arbitrary spatial thermal gradient.
ell=s.Matrix([0,*s.symbols('L1:4')]); u=s.Matrix([1,0,0,0]); j=s.zeros(4)
for i in range(1,4): j[0,i]=-ell[i]
out,A,Q,sig=stress(u,j,ell,T,eta,chi,lam)
check('prepared data',A)
check('prepared data',Q,s.zeros(4,1))
check('prepared data',sig,s.zeros(4))
check('prepared data',out,s.diag(T**4,T**4/3,T**4/3,T**4/3))
# Full 4D plane-wave principal tensor, not a scalar shear surrogate.
a=s.symbols('a'); c=s.symbols('c',real=True)
r=s.Matrix(s.symbols('r1:4')); L=s.symbols('L')
u=s.Matrix([1,*[a*v for v in r]])
k=s.Matrix([-c,1,0,0]); j=k*s.Matrix([0,*[a*v for v in r]]).T
ell=a*L*k
out,_,_,_=stress(u,j,ell,T,eta,chi,lam)
lin=out.applyfunc(lambda z:s.expand(z).coeff(a,1))
# Terms with one derivative only: remove the ideal part, keeping the principal flux.
ideal=(T**4)*(u*u.T+(s.diag(-1,1,1,1)+u*u.T)/3)
lin_der=(out-ideal).applyfunc(lambda z:s.expand(z).coeff(a,1)/T**3)
res=lin_der.T*k
mat=res.jacobian([L,*r])
expected=s.Matrix([[3*chi*c*c+lam,-(chi+lam)*c,0,0],[-(chi+lam)*c,lam*c*c+(chi-4*eta)/3,0,0],[0,0,lam*c*c-eta,0],[0,0,0,lam*c*c-eta]])
check('principal matrix',mat,expected)
z=s.symbols('z')
p=3*chi*lam*z*z-2*chi*(2*eta+lam)*z+lam*(chi-4*eta)/3
check('full determinant',s.factor(mat.det()),(lam*c*c-eta)**2*p.subs(z,c*c))
pa=s.factor(p.subs({eta:1,chi:s.Rational(25,2),lam:s.Rational(25,3)}))
check('frame A polynomial',pa,s.Rational(25,18)*(225*z*z-186*z+17))
for root in [(31-2*s.sqrt(134))/75,(31+2*s.sqrt(134))/75]:
    check('frame A roots',pa.subs(z,root))
    positive('frame A speed bound',root)
    positive('frame A speed bound',s.Rational(81,100)-root)
positive('frame A shear bound',s.Rational(81,100)-s.Rational(3,25))
pb=s.factor(p.subs({eta:1,chi:s.Rational(25,4),lam:s.Rational(25,7)}))
check('frame B light root',pb.subs(z,1))
check('frame B slow root',pb.subs(z,s.Rational(1,25)))
# Ball moment and positivity/negative-part bookkeeping constants.
r,R,bar=s.symbols('r R bar',positive=True)
ball=s.integrate(4*s.pi*r*r,(r,0,R))
second=s.integrate(4*s.pi*r**4,(r,0,R))
check('ball volume',ball,4*s.pi*R**3/3)
check('background allowance',R*R*ball-second,8*s.pi*R**5/15)
t,E,F,I0,v=s.symbols('t E F I0 v',real=True)
I=I0+2*F*t+E*t*t
check('virial acceleration',s.diff(I,t,2),2*E)
# Explicit frame A obstruction: c=9/10, t=20R, plateau radius R/2, T=32 Tbar.
L=19*R; E_min=s.pi*R**3*bar*(32**4-1)/6
margin=s.expand(E_min*((20*R)**2-L**2)-8*s.pi*bar*L**5/15)
check('explicit positive margin',margin,164854541*s.pi*bar*R**5/30)
positive('margin sign',s.Rational(164854541,30))
check('negative energy lower bound',margin/L**2,164854541*s.pi*bar*R**3/10830)
# General strict-front threshold and light-front degeneracy.
gap=s.factor((2*R/(1-v))**2-(R+v*2*R/(1-v))**2)
check('general strict-front gap',gap,R**2*(3+v)/(1-v))
check('luminal failure',s.expand(t*t-(R+t)**2),-R*R-2*R*t)
# Isotropic massless transport moments: exact second moment grows as t^2 E.
x,y,z=s.symbols('x y z',real=True)
mu,phi=s.symbols('mu phi',real=True)
n=s.Matrix([s.sqrt(1-mu*mu)*s.cos(phi),s.sqrt(1-mu*mu)*s.sin(phi),mu])
check('massless speed',n.dot(n),1)
for i in range(3):
    avg=s.integrate(s.integrate(n[i],(phi,0,2*s.pi)),(mu,-1,1))/(4*s.pi)
    check('isotropic first moment',avg)
    avg=s.integrate(s.integrate(n[i]**2,(phi,0,2*s.pi)),(mu,-1,1))/(4*s.pi)
    check('isotropic pressure',avg,s.Rational(1,3))
for k,v in counts.items(): print(f'PASS: {k}: {v}')
print(f'TOTAL: {sum(counts.values())} exact checks passed')
print('SCOPE: tensor/spectrum/virial constants and kinetic moments only.')
print('NOT CHECKED: nonlinear domain-of-dependence proof, independent review, Lean, or CI.')
