#!/usr/bin/env python3
"""Exact algebra for frame-independent Euler-prepared BDNK kinetic-cone exit.
Not a PDE solver or an independent theorem verifier.
"""
from collections import Counter
import sympy as s
C=Counter()
def eq(label,a,b=0):
    d=a-b
    entries=list(d) if isinstance(d,s.MatrixBase) else [d]
    if any(s.simplify(z)!=0 for z in entries): raise AssertionError((label,d))
    C[label]+=1

def tensor(u,j,ell,T,eta0,chi0,lam0):
    g=s.diag(-1,1,1,1);D=g+u*u.T;th=s.trace(j);du=j.T*u
    A=chi0*T**3*(3*u.dot(ell)+th); Q=lam0*T**3*(du+D*ell)
    sig=D*(j*g+g*j.T)*D/2-th*D/3
    Tmunu=(T**4+A)*(u*u.T+D/3)+u*Q.T+Q*u.T-2*eta0*T**3*sig
    return Tmunu,A,Q,sig
eta,chi,lam,T,d,Lx=s.symbols('eta chi lam T d Lx',positive=True)
for n in range(2,7):
    z=s.Rational(1,n); g=(1+z*z)/(1-z*z); p=2*z/(1-z*z); den=3+2*p*p
    Lt=(-d-2*g*p*Lx)/den;rt=(-2*g*p*d-3*Lx)/den
    th=3*(g*d-p*Lx)/den
    u=s.Matrix([g,p,0,0]);N=s.Matrix([p,g,0,0]);jet=s.zeros(4)
    jet[0,:]=(rt*N).T;jet[1,:]=(d*N).T
    out,A,Q,sigma=tensor(u,jet,s.Matrix([Lt,Lx,0,0]),T,eta,chi,lam)
    boost=s.Matrix([[g,p,0,0],[p,g,0,0],[0,0,1,0],[0,0,0,1]])
    pl=(T**4-4*eta*T**3*th)/3;pt=(T**4+2*eta*T**3*th)/3
    eq('full tensor',out,boost*s.diag(T**4,pl,pt,pt)*boost.T)
    eq('Euler energy preparation',A)
    eq('Euler momentum preparation',Q,s.zeros(4,1))
    eq('exact expansion',s.trace(jet),th)
# Two conserved PDE time jets at the reflection center.
a,H,delta=s.symbols('a H delta',real=True)
r,dd,lx=s.symbols('r dd lx',real=True)
den=3+2*s.sinh(r)**2
rt=(-2*s.cosh(r)*s.sinh(r)*dd-3*lx)/den
rxt=(s.diff(rt,r)*a+s.diff(rt,lx)*H).subs({r:0,dd:a,lx:0})
eq('rapidity mixed jet',rxt,-2*a*a/3-H)
E_t=-4*a/3+4*eta*a*a/3;eta_t=-eta*a
pl_t=E_t/3-s.Rational(4,3)*(eta_t*a+eta*rxt)
eq('full pressure time jet',pl_t,-4*a/9+8*eta*a*a/3+4*eta*H/3)
a0=(1-3*delta)/(4*eta);H0=-1/(12*eta**2)
eq('outward kinetic derivative',pl_t.subs({a:a0,H:H0}),(-1-12*delta+27*delta**2)/(18*eta))
eq('cone boundary derivative',pl_t.subs({a:1/(4*eta),H:H0}),-1/(18*eta))
# Spatial analytic preparation; K>=4, b=1/(12K^2), k=K/eta.
x,K=s.symbols('x K',real=True,positive=True);k=K/eta;b=1/(12*K*K)
ell=b*(s.cos(k*x)-1);rap=a0/k*s.sin(k*x)
eq('thermal curvature',s.diff(ell,x,2).subs(x,0),H0)
eq('velocity slope',s.diff(rap,x).subs(x,0),a0)
theta_profile=3*(s.cosh(rap)*s.diff(rap,x)-s.sinh(rap)*s.diff(ell,x))/(3+2*s.sinh(rap)**2)
eq('initial theta',theta_profile.subs(x,0),a0)
# Uniform elementary margin accounting.
c,bb=s.symbols('c bb',real=True)
expr=(1-bb*(1-c))-(1-3*delta)*(1-(1-4*bb)*(1-c))
eq('longitudinal margin',expr,3*delta+((1-3*delta)*(1-4*bb)-bb)*(1-c))
eq('minimum margin coefficient',s.Rational(1,2)-3*s.Rational(1,192),s.Rational(31,64))
eq('negative cosine margin',1-4*s.Rational(1,192),s.Rational(47,48))
eq('transverse margin',s.Rational(1,2)-2*s.Rational(1,192),s.Rational(47,96))
eq('exit integration',delta-72*eta*delta/(36*eta),-delta)
eq('initial entropy',s.Rational(4,3)*eta*(1/(4*eta))**2,1/(12*eta))
# Exact normal-time determinant of the two coupled equations.
z=s.symbols('z',positive=True);g=s.sqrt(z);p=s.sqrt(z-1)
CL0=g*(chi*(4*z-1)+2*lam*(z-1))
CR0=p*(chi*(4*z-1)/3+2*lam*z-4*eta*(z-1)/3)
CL1=p*(4*chi*z+lam*(2*z-1))
CR1=g*(4*(chi-eta)*(z-1)/3+lam*(2*z-1))
Dtime=s.expand(CL0*CR1-CR0*CL1)
Dchar=3*chi*lam*z*z-2*chi*(2*eta+lam)*z*(z-1)+lam*(chi-4*eta)*(z-1)**2/3
eq('noncharacteristic time block',Dtime,Dchar)
eq('frame A time block',Dtime.subs({chi:25*eta/2,lam:25*eta/3}),25*eta**2*(56*z*z+152*z+17)/18)
eq('frame B time block',Dtime.subs({chi:25*eta/4,lam:25*eta/7}),75*eta**2*(24*z+1)/28)
eq('observer ideal energy margin',(4*z-1)/3-z,(z-1)/3)
# Trace-defect extension of the virial identity.
t,sig,E,I0,F0,D0=s.symbols('t sig E I0 F0 D0',real=True)
I=I0+2*F0*t+E*t*t-2*s.integrate((t-sig)*D0,(sig,0,t))
eq('trace-defect virial',s.diff(I,t,2),2*(E-D0))
for k,n in C.items():print(f'PASS: {k}: {n}')
print(f'TOTAL: {sum(C.values())} exact checks passed')
print('SCOPE: full tensor, Euler preparation, initial pressure jet and cone margins.')
print('NOT CHECKED: independent review, analytic local-existence replay, Lean or CI.')
