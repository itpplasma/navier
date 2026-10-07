#!/usr/bin/env python3
"""Exact algebraic regression for the BDNK transfer screen; not a PDE verifier.

Run: python3 research/check_bdnk_transfer.py
Requires SymPy. No network, simulation, floating-point proof, or Lean invocation.
"""
from __future__ import annotations
from collections import Counter
import sympy as s

counts: Counter[str] = Counter()

def equal(group: str, lhs: s.Expr | s.MatrixBase, rhs=0) -> None:
    difference = lhs-rhs if not isinstance(lhs, s.MatrixBase) else lhs-(rhs if isinstance(rhs, s.MatrixBase) else s.zeros(*lhs.shape))
    entries = list(difference) if isinstance(difference, s.MatrixBase) else [difference]
    if any(s.simplify(item) != 0 for item in entries):
        raise AssertionError(f'{group}: {difference}')
    counts[group] += 1


def stress(u: s.Matrix, jet: s.Matrix, logT: s.Matrix, T, eta0, chi0, lam0):
    """jet[alpha,mu]=partial_alpha u^mu; signature (-,+,+,+)."""
    metric = s.diag(-1,1,1,1)
    delta = metric+u*u.T
    theta = s.trace(jet)
    Du = jet.T*u
    A = chi0*T**3*(3*(u.dot(logT))+theta)
    Q = lam0*T**3*(Du+delta*logT)
    lower_jet = jet*metric
    sigma = delta*(lower_jet+lower_jet.T)/2*delta-theta*delta/3
    tensor = (T**4+A)*(u*u.T+delta/3)+u*Q.T+Q*u.T-2*eta0*T**3*sigma
    return tensor, A, Q, sigma


def rational_jet_tests() -> None:
    # Direct four-tensor construction is independent of the component formula.
    metric = s.diag(-1,1,1,1)
    for n in range(1,13):
        r=s.Matrix([s.Rational(1,n+4),s.Rational(1,n+5),s.Rational(-1,n+6)])
        norm=r.dot(r)
        u=s.Matrix([(1+norm)/(1-norm),*(2*r/(1-norm))])
        jet=s.zeros(4)
        for alpha in range(4):
            for mu in range(1,4):
                jet[alpha,mu]=s.Rational((-1)**(alpha+mu)*(n+alpha+mu),n+7+alpha*mu)
            jet[alpha,0]=sum(u[j]*jet[alpha,j] for j in range(1,4))/u[0]
        logT=s.Matrix([s.Rational(n,11),s.Rational(-2,7),s.Rational(3,13),s.Rational(1,17)])
        T=s.Rational(n+2,n+1)
        eta0=s.Rational(2,3); chi0=25*eta0/2; lam0=25*eta0/3
        tensor,A,Q,sigma=stress(u,jet,logT,T,eta0,chi0,lam0)
        equal('tensor invariants',u.dot(metric*u),-1)
        equal('tensor invariants',jet*metric*u)
        equal('tensor invariants',u.dot(metric*Q))
        equal('tensor invariants',sigma*metric*u)
        equal('tensor invariants',s.trace(metric*sigma))
        equal('tensor invariants',s.trace(metric*tensor))
        equal('tensor invariants',tensor,tensor.T)
        gamma=u[0]; dg=jet[0,0]; L=logT[0]
        divw=sum(jet[j,j] for j in range(1,4))
        wg=sum(u[j]*jet[j,0] for j in range(1,4))
        wL=sum(u[j]*logT[j] for j in range(1,4))
        eta,chi,lam=[c*T**3 for c in (eta0,chi0,lam0)]
        temporal=(T**4*(4*gamma**2-1)/3
            +(chi*(4*gamma**2-1)/3+2*lam*gamma**2-4*eta*(gamma**2-1)/3)*dg
            +(chi*gamma*(4*gamma**2-1)+2*lam*gamma*(gamma**2-1))*L)
        spatial=((chi*(4*gamma**2-1)/3+2*eta*(gamma**2-1)/3)*divw
            +2*(lam-eta)*gamma*wg
            +(chi*(4*gamma**2-1)+2*lam*gamma**2)*wL)
        equal('full energy component',tensor[0,0],temporal+spatial)


def symbolic_tests() -> None:
    gamma,dg,L,eta,chi,lam=s.symbols('gamma dg L eta chi lam')
    T=s.symbols('T',positive=True)
    cG=chi*(4*gamma**2-1)/3+2*lam*gamma**2-4*eta*(gamma**2-1)/3
    cL=chi*gamma*(4*gamma**2-1)+2*lam*gamma*(gamma**2-1)
    C=4*chi/3+2*lam-4*eta/3
    D=4*chi+2*lam
    equal('leading coefficients',s.expand(cG).coeff(gamma,2),C)
    equal('leading coefficients',s.expand(cL).coeff(gamma,3),D)
    equal('leading coefficients',C.subs({chi:25*eta/2,lam:25*eta/3}),32*eta)
    equal('leading coefficients',(D/C).subs({chi:25*eta/2,lam:25*eta/3}),s.Rational(25,12))
    equal('leading coefficients',D-C,s.Rational(8,3)*chi+s.Rational(4,3)*eta)
    # Dilation integrating factor, using independent symbolic first derivatives.
    G,H,LG,LH,a,b,C0,kappa=s.symbols('G H LG LH a b C0 kappa', positive=True)
    F=H**3*G**2*(C0*(a*G+LG)+C0*kappa*G*(b+LH/H))
    Z=H**(3*kappa)*G**3
    LZ=s.diff(Z,G)*LG+s.diff(Z,H)*LH
    equal('dilation identity',F,C0*s.Rational(1,3)*H**(3-3*kappa)*(LZ+3*(a+kappa*b)*Z))
    equal('critical thermal branch',s.Rational(3,1)/C0*H**(3*kappa-3)*(s.Rational(4,3)*H**4*G**2),4/C0*H**(1+3*kappa)*G**2)
    # Uniform-profile leading residual includes the time derivative of transport.
    tau=s.symbols('tau',positive=True)
    c,d,A0=s.symbols('c d A0',positive=True)
    energy=A0*(c*a+d*b)*tau**(-3*a-3*b-1)
    equal('time scaling',-s.diff(energy,tau),A0*(c*a+d*b)*(3*a+3*b+1)*tau**(-3*a-3*b-2))
    # The smooth-profile source exponents beat every spatial derivative when beta<1.
    beta=s.symbols('beta',positive=True)
    equal('time scaling',(-3*b-3*a-1-beta)-(-3*b-3*a-2),1-beta)
    equal('time scaling',(4*b+2*a)-(3*b+3*a+1),b-a-1)
    # Linear transverse shear from the full tensor, to first order in amplitude.
    eps, vt, vx=s.symbols('eps vt vx')
    u=s.Matrix([1,0,eps,0]); jet=s.zeros(4);jet[0,2]=eps*vt;jet[1,2]=eps*vx
    tensor,_,_,_=stress(u,jet,s.zeros(4,1),T,eta,chi,lam)
    coefficient=lambda expr:s.expand(expr).coeff(eps,1)
    equal('linear shear',coefficient(tensor[0,2]),4*T**4/3+lam*T**3*vt)
    equal('linear shear',coefficient(tensor[1,2]),-eta*T**3*vx)
    h,k,z=s.symbols('h k z',positive=True)
    rootplus=(-h+s.sqrt(h*h-4*lam*eta*k*k))/(2*lam)
    rootminus=(-h-s.sqrt(h*h-4*lam*eta*k*k))/(2*lam)
    equal('shear spectrum',lam*rootplus**2+h*rootplus+eta*k*k)
    equal('shear spectrum',lam*rootminus**2+h*rootminus+eta*k*k)
    equal('shear spectrum',rootplus+rootminus,-h/lam)
    equal('shear spectrum',s.limit(rootplus/k**2,k,0),-eta/h)
    equal('shear spectrum',rootplus*rootminus,eta*k*k/lam)
    # MIS shear elimination: tau_pi v_tt+v_t-(eta/h)v_xx=0.
    tt,xx=s.symbols('tt xx',real=True)
    v=s.Function('v')(tt,xx); pi=s.Function('pi')(tt,xx)
    relax=s.symbols('relax',positive=True)
    momentum=h*s.diff(v,tt)+s.diff(pi,xx)
    relaxation=relax*s.diff(pi,tt)+pi+eta*s.diff(v,xx)
    eliminated=relax*s.diff(momentum,tt)+momentum-s.diff(relaxation,xx)
    equal('MIS matched shear',eliminated,h*relax*s.diff(v,tt,tt)+h*s.diff(v,tt)-eta*s.diff(v,xx,xx))
    equal('MIS matched shear',eliminated.subs(relax,lam/h),lam*s.diff(v,tt,tt)+h*s.diff(v,tt)-eta*s.diff(v,xx,xx))
    # Exact NONLINEAR constant-temperature transverse ansatz.
    t,x=s.symbols('t x',real=True)
    p=s.Function('p')(t,x); g=s.sqrt(1+p*p)
    u=s.Matrix([g,0,p,0]); jet=s.zeros(4)
    for mu in range(4):
        jet[0,mu]=s.diff(u[mu],t);jet[1,mu]=s.diff(u[mu],x)
    tensor,_,_,_=stress(u,jet,s.zeros(4,1),T,eta,chi,lam)
    equal('nonlinear transverse closure',tensor[0,1],-eta*T**3*s.diff(g,x))
    equal('nonlinear transverse closure',tensor[1,1],T**4/3+(chi+2*eta)*T**3*s.diff(g,t)/3)
    residual=s.diff(tensor[0,1],t)+s.diff(tensor[1,1],x)
    equal('nonlinear transverse closure',residual,(chi-eta)*T**3*s.diff(g,t,x)/3)
    # Known source exponents and finite-energy/validity incompatibility.
    hh=s.symbols('hh',positive=True)
    aa=s.Rational(1,2)+hh; volume=s.Rational(3,2)-hh
    equal('source scale', (volume-2*aa)/4,s.Rational(1,8)-3*hh/4)
    equal('source scale',aa+1-(volume-2*aa)/4,s.Rational(11,8)+7*hh/4)
    equal('source scale',-aa/s.Rational(25,12),-12*aa/25)


def main() -> None:
    rational_jet_tests()
    symbolic_tests()
    for group,count in counts.items():
        print(f'PASS: {group}: {count} exact identities')
    print(f'TOTAL: {sum(counts.values())} exact identities passed')
    print('SCOPE: algebraic regressions and an independent component construction only.')
    print('NOT CHECKED: universal PDE quantifiers, independent mathematical review, Lean, or repository CI.')

if __name__=='__main__':
    main()
