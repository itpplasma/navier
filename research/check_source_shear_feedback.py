#!/usr/bin/env python3
"""Exact local shear-feedback checks and optional positive-lattice calibration.

Python 3.10+, SymPy; --lattice additionally requires NumPy/SciPy.
The time jets retain every Fourier output at each computed order. Lattice
runs are finite sections of an infinite LINEAR system about a prescribed
exact diffusing shear, not simulations of the completed OpenAI flow.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as s

CHECKS: list[str] = []

def check(ok: bool, label: str) -> None:
    if not bool(ok):
        raise AssertionError(label)
    CHECKS.append(label)

def zero(expr) -> bool:
    values = expr if isinstance(expr, s.MatrixBase) else [expr]
    return all(s.simplify(x) == 0 for x in values)

def symbolic_quartic() -> dict:
    u,b,c,Q,A,B=s.symbols('u b c Q A B', real=True, nonzero=True)
    zv=s.zeros(3,1)
    def kv(k): return s.Matrix([b*u*k[0],0,b*k[1]])
    def bil(U,V):
        out={}
        for p,a in U.items():
            for q,d in V.items():
                k=(p[0]+q[0],p[1]+q[1])
                if k==(0,0): continue
                n=kv(k); f=-s.I*a.dot(kv(q))*d
                f=f-n*n.dot(f)/n.dot(n)
                out[k]=out.get(k,zv)+f
        return {k:v.applyfunc(s.factor) for k,v in out.items() if not zero(v)}
    P={(1,1):A*s.Matrix([1,c*Q,-u]),(-1,1):B*s.Matrix([1,c*Q,u]),
       (-1,-1):A*s.Matrix([1,c*Q,-u]),(1,-1):B*s.Matrix([1,c*Q,u])}
    S=bil(P,P);D=bil(P,S);T=bil(P,D)
    check(set(S)=={(2,0),(-2,0)},'symmetric tilts: complete first nonlinear output is the shear pair')
    check(zero(S[(2,0)]-s.Matrix([0,-4*s.I*A*B*c*Q*b*u,0])), 'first shear coefficient')
    check(not bil(S,P) and not bil(S,S), 'shear acts by its gradient, not by y-advection')
    check(not bil(D,P), 'second scalar outputs have no y-advection')
    targets={(0,2):-s.I*s.Rational(8,3)*c*Q*(b*u)**3*A*B*(A*A-B*B),
             (2,2):s.I*s.Rational(16,3)*c*Q*(b*u)**3*A*A*B*B,
             (-2,2):-s.I*s.Rational(16,3)*c*Q*(b*u)**3*A*A*B*B}
    for k,value in targets.items():
        check(zero(T[k]/6-s.Matrix([0,value,0])),f'quartic feedback at label {k}')
    check(zero(targets[(0,2)].subs(B,A)), 'central daughter cancels at equal parent weights')
    check(not zero(targets[(2,2)].subs(B,A)), 'doubled parents survive equal parent weights')
    for k,v in T.items():
        check(zero(kv(k).dot(v)),f'quartic all-output transversality {k}')
    return {'targets_t_cubed':{str(k):str(v) for k,v in targets.items()},
            'first_output_labels':[list(k) for k in sorted(S)],
            'second_scalar_output_labels':[list(k) for k in sorted(D)],
            'third_nonlinear_output_labels':[list(k) for k in sorted(T)]}

# Complex rational vectors use (real_x,real_y,real_z,imag_x,imag_y,imag_z).
ZERO=(F(0),)*6

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def conj(a): return a[:3]+tuple(-x for x in a[3:])

class ExactJet:
    def __init__(self, nu: F, source_linear: bool):
        self.nu=nu; self.source_linear=source_linear
        self.u=F(12,5); self.Q=F(13,5)
    def wavevector(self,k): return (self.u*k[0],F(0),F(k[1]))
    def project(self,k,a):
        n=self.wavevector(k)
        return add(a,mul(-dot(n,a)/dot(n,n),n))
    def linear_real(self,k,a):
        n=self.wavevector(k)
        f=mul(-self.nu*dot(n,n),a)
        if self.source_linear:
            f=add(f,self.project(k,(-a[1],-a[0],F(0))))
        return f
    def linear(self,k,a): return self.linear_real(k,a[:3])+self.linear_real(k,a[3:])
    def pair(self,k,a,q,b):
        n=self.wavevector(q)
        ar,ai=dot(a[:3],n),dot(a[3:],n)
        real=add(mul(ar,b[:3]),mul(-ai,b[3:]))
        imag=add(mul(ar,b[3:]),mul(ai,b[:3]))
        return self.project(k,imag)+mul(F(-1),self.project(k,real))
    def run(self,A:F,B:F,order:int)->list[dict]:
        a=(F(1),-self.Q,-self.u,F(0),F(0),F(0))
        b=(F(1),-self.Q,self.u,F(0),F(0),F(0))
        jets=[{(1,1):mul(A,a),(-1,1):mul(B,b),
               (-1,-1):mul(A,conj(a)),(1,-1):mul(B,conj(b))}]
        for j in range(order):
            out={k:self.linear(k,a) for k,a in jets[j].items()}
            for l in range(j+1):
                for p,a in jets[l].items():
                    for q,b in jets[j-l].items():
                        k=(p[0]+q[0],p[1]+q[1])
                        if k!=(0,0):
                            out[k]=add(out.get(k,ZERO),self.pair(k,a,q,b))
            jets.append({k:mul(F(1,j+1),a) for k,a in out.items() if a!=ZERO})
        return jets

def exact_jets()->list[dict]:
    rows=[]
    for source in (True,False):
        for nu in (F(125,2197),F(1,17)):
            for A,B in ((F(1),F(1)),(F(1),F(2))):
                model=ExactJet(nu,source); J=model.run(A,B,8)
                desc=f'source={source},nu={nu},A={A},B={B}'
                values={(0,2):-F(8,3)*(-model.Q)*model.u**3*A*B*(A*A-B*B),
                        (2,2):F(16,3)*(-model.Q)*model.u**3*A*A*B*B,
                        (-2,2):-F(16,3)*(-model.Q)*model.u**3*A*A*B*B}
                for k,val in values.items():
                    check(all(J[j].get(k,ZERO)==ZERO for j in range(3)),desc+f': no earlier target {k}')
                    check(J[3].get(k,ZERO)==(F(0),F(0),F(0),F(0),val,F(0)),desc+f': full cubic-time target {k}')
                for j,D in enumerate(J):
                    check(all(dot(model.wavevector(k),a[:3])==0 and dot(model.wavevector(k),a[3:])==0
                              for k,a in D.items()),desc+f': all-output divergence order {j}')
                    check(all(D.get((-k[0],-k[1]),ZERO)==conj(a) for k,a in D.items()),
                          desc+f': all-output reality order {j}')
                    if A==B:
                        check(all(k[0]!=0 for k in D),desc+f': reflection forbids x-mean order {j}')
                        def reflected(a,k):
                            return mul(F((-1)**k[0]),(-a[0],-a[1],a[2],-a[3],-a[4],a[5]))
                        check(all(D.get((-k[0],k[1]),ZERO)==reflected(a,k) for k,a in D.items()),
                              desc+f': nonlinear reflection identity order {j}')
                if not source:
                    initial=set(J[0])
                    check(all(a[0]==a[2]==a[3]==a[5]==0 for D in J for k,a in D.items() if k not in initial),
                          desc+': smooth NS control generates no new poloidal modes')
                rows.append({'source_linear':source,'nu':str(nu),'A':str(A),'B':str(B),
                             'mode_counts':[len(d) for d in J],
                             'central_t3':[str(v) for v in J[3].get((0,2),ZERO)],
                             'doubled_t3':[str(v) for v in J[3][(2,2)]]})
    return rows

def exact_shear_and_rates()->None:
    t,x,nu,xi,k,kappa,G,H=s.symbols('t x nu xi k kappa G H', positive=True)
    V=H/xi*s.exp(-nu*xi**2*t)*s.sin(xi*x)
    check(zero(s.diff(V,t)-nu*s.diff(V,x,2)), 'sideband background follows ordinary diffusion exactly')
    U=G*x+V;pressure=-kappa*G*x*x/2+kappa*H/xi**2*s.exp(-nu*xi**2*t)*s.cos(xi*x)
    check(zero(s.diff(pressure,x)+kappa*U), 'rotating shear pressure sign')
    d0=nu*k*k; ds=nu*xi*xi; d1=d0+ds; P1=k*k/(k*k+xi*xi)
    y0=s.exp(-d0*t)
    a1=H*t*s.exp(-d1*t)/2
    y1=kappa*P1*H*t*t*s.exp(-d1*t)/4
    check(zero(s.diff(a1,t)+d1*a1-H*s.exp(-ds*t)*y0/2), 'first positive Duhamel path with exact diffusion resonance')
    check(zero(s.diff(y1,t)+d1*y1-kappa*P1*a1), 'second positive Duhamel path: radial tilted component')
    lam,Q=s.symbols('lam Q',positive=True)
    mu=lam/Q**3
    check(zero(lam/Q-4*mu*Q**2+3*lam/Q), 'doubled parent has negative isolated source-normalized growth')
    check(zero(y1.subs({t:2/d1})/y0.subs(t,0)-kappa*P1*H*s.exp(-2)/d1**2),
          'explicit finite-time tilted transmission lower bound')
    a=s.symbols('a',real=True)
    # Reflection (x,z)->(pi/(bu)-x,z), components ->(-r,-N,+z).
    R=s.diag(-1,-1,1); KK=s.Matrix([[0,kappa,0],[G,0,0],[0,0,0]])
    check(R*KK==KK*R,'linear source matrix respects reflected scalar/vector symmetry')
    c,b,delta=s.symbols('c b delta',real=True)
    C=s.Matrix([0,a,-2*c]);nd=s.Matrix([2*b*c,0,2*b])
    check(zero(nd.dot(C)+4*b*c), 'dominant N-directed sideband is invisible to passive daughter phase at c=0')


def lattice_calibrations()->list[dict]:
    import numpy as np
    from scipy.integrate import solve_ivp
    rows=[];nu=125/2197;k=2.;side=24/5; kappa=G=1.
    times=np.linspace(0,2,81)
    for H in (1.,16.,64.):
        previous=None
        for M in (4,8,16,32):
            m=np.arange(M+1);K2=k*k+(side*m)**2;d=nu*K2;P=k*k/K2;ds=nu*side**2
            initial=np.zeros(2*(M+1));initial[0]=1.;initial[M+1]=1.
            def rhs(t,state):
                y=state[:M+1];a=state[M+1:]
                neighbors=np.zeros(M+1);neighbors[0]=2*y[1]
                neighbors[1:]+=y[:-1];neighbors[1:-1]+=y[2:]
                return np.r_[-d*y+kappa*P*a,-d*a+G*y+.5*H*np.exp(-ds*t)*neighbors]
            sol=solve_ivp(rhs,(0,2),initial,t_eval=times,method='Radau',rtol=2e-10,atol=2e-12)
            if not sol.success: raise RuntimeError(sol.message)
            y1=sol.y[1];lower=kappa*P[1]*H/4*times**2*np.exp(-d[1]*times)
            if np.min(y1-lower)<-1e-9 or np.min(sol.y)<-1e-8:
                raise AssertionError(f'positive-lattice failure H={H}, M={M}, lower={np.min(y1-lower)}, min={np.min(sol.y)}')
            if previous is not None and np.min(y1-previous)<-1e-8:
                raise AssertionError('finite-section monotonicity check failed')
            rows.append({'H0':H,'radial_harmonics_each_side':M,'u1_at_t2':float(y1[-1]),
                         'exact_lower_at_t2':float(lower[-1]),
                         'maximum_u1_to_t2':float(np.max(y1)),
                         'maximum_difference_from_previous_section':None if previous is None else float(np.max(abs(y1-previous)))})
            previous=y1
    return rows


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lattice',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    symbolic=symbolic_quartic();jets=exact_jets();exact_shear_and_rates()
    rows=lattice_calibrations() if args.lattice else []
    result={'status':'Author results for an explicitly scoped local reference system; no unforced R3 singularity.',
            'exact_assertion_count':len(CHECKS),'symbolic_quartic':symbolic,
            'untruncated_time_jets':jets,'positive_linear_lattice_calibrations':rows,
            'numerical_scope':'Floating point finite sections; no interval bounds or nonlinear source-history computation.'}
    if args.output: args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(CHECKS)} exact assertions; {len(rows)} positive-linear-lattice numerical cases.')
    print(result['status'])
    if rows: print(json.dumps(rows,indent=2))

if __name__=='__main__': main()
