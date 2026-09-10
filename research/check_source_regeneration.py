#!/usr/bin/env python3
"""Source-inspired preparation/overlap checks; not an unforced blow-up proof.

Python 3.10+ and SymPy suffice for exact checks and reference tables.
--principal additionally uses NumPy/SciPy and the existing sibling
check_source_pulse_adjoint.py for finite-L principal-ODE calibrations.
No network, PDE trajectory, frequency truncation, or automatic file writes.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sympy as s

CHECKS: list[str] = []


def check(ok: bool, label: str) -> None:
    if not bool(ok):
        raise AssertionError(label)
    CHECKS.append(label)


def zero(expr) -> bool:
    if isinstance(expr, s.MatrixBase):
        return all(s.simplify(v) == 0 for v in expr)
    return s.simplify(expr) == 0


def projection(k):
    k = s.Matrix(k)
    return s.eye(3) - k*k.T/(k.dot(k))


def interaction(p, a, q, b):
    """Real coefficient before -i for the unordered Fourier pair p,q."""
    p, q, a, b = map(s.Matrix, (p,q,a,b))
    return s.simplify(projection(p+q)*(a.dot(q)*b+b.dot(p)*a))


def exact_preparation() -> None:
    W,L,B,u,lam,g = s.symbols('W L B u lam g', positive=True)
    v = s.symbols('v', real=True)
    n = s.Matrix([B*(u/2+u*v/L), -B*u/(L*g), B])
    I = s.integrate(n.dot(n), (v,-W,0))
    expected = B**2*(W*(1+u*u/4+u*u/(L*L*g*g))
                       -u*u*W*W/(2*L)+u*u*W**3/(3*L*L))
    check(zero(I-expected), 'exact cubic integrated squared phase gradient')
    check(s.limit(I.subs(W,L**2)/L**4,L,s.oo)==B**2*u*u/3,
          'L-squared preparation produces L-fourth viscous exponent')
    F,gt,gz,z = s.symbols('F gt gz z', real=True)
    K=s.Matrix([[0,-2*F,0],[2*F+gt,0,0],[gz,0,0]])
    S=(K+K.T)/2
    check(zero((z*s.eye(3)-S).det()-z*(z*z-(gt*gt+gz*gz)/4)),
          'symmetric connection/shear matrix has norm |g|/2')
    a=s.Matrix(s.symbols('a0:3',real=True)); n=s.Matrix(s.symbols('n0:3',real=True))
    np=s.Matrix(s.symbols('np0:3',real=True))
    A=-K+n*(n.T*K-np.T)/(n.dot(n))
    check(zero((n.T*A+np.T)), 'principal pressure projection preserves n dot a')
    check(zero(a.dot(A*a)+a.dot(K*a)-a.dot(n)*((n.T*K-np.T)*a)[0]/n.dot(n)),
          'normal pressure contributes zero to transverse amplitude energy')


def exact_overlap() -> None:
    b=s.symbols('b',positive=True)
    x,y,c0=s.symbols('x y c0', real=True)
    qx,qy=s.sqrt(1+x*x),s.sqrt(1+y*y)
    p=s.Matrix([b*x,0,b]); q=s.Matrix([b*y,0,b])
    a=s.Matrix([1,c0*qx,-x]); d=s.Matrix([1,c0*qy,-y])
    mean=(x+y)/2; diff=x-y; qmean=s.sqrt(1+mean*mean)
    out=interaction(p,a,q,d)
    expected=s.Matrix([b*diff**2*mean/(1+mean**2),
                       b*c0*diff*(qx-qy),
                       -b*diff**2*mean**2/(1+mean**2)])
    check(zero(p.dot(a)) and zero(q.dot(d)), 'both parent polarizations are transverse')
    check(zero(out-expected), 'complete projected sum-frequency coefficient')
    beta=(out[0]+out[1]/(c0*qmean))/2
    check(zero(beta-b*diff/2*(diff*mean/(1+mean*mean)+(qx-qy)/qmean)),
          'daughter growing-coordinate coefficient with pressure retained')
    check(zero((qx-qy)*(qx+qy)-2*mean*diff), 'rationalization determines exact sign of growing source')
    check(zero(out.subs(y,-x)), 'mirror-symmetric growing parents have zero leading sum output')
    opposite=interaction(p,a,-q,d)
    expected_d=s.Matrix([0,b*diff*c0*(qx+qy),-2*b*diff*mean])
    check(zero(opposite-expected_d), 'difference-frequency shear is retained exactly')
    check(zero(out.subs(y,x)), 'parallel equal-tilt parents have zero interaction')
    # General transverse polarizations: classify cancellation of the difference.
    c1,c2=s.symbols('c1 c2',real=True)
    a1=s.Matrix([1,c1,-x]); a2=s.Matrix([1,c2,-y])
    dgeneral=interaction(p,a1,-q,a2)
    check(zero(dgeneral-s.Matrix([0,b*diff*(c1+c2),-2*b*diff*mean])),
          'general-polarization difference cancellation conditions')
    mixed=interaction(p,a1,q,a2).subs({y:-x,c2:-c1})
    check(zero(mixed-s.Matrix([0,4*b*x*c1,0])),
          'opposite eigenbranches cancel difference but seed sum')
    # Exact reference eigenvectors in an orthonormal (radial,N,K) frame.
    lam,omega=s.symbols('lam omega',real=True)
    K=s.Matrix([[0,-lam/c0,-omega],[-lam*c0,0,0],[omega,0,0]])
    normal=s.Matrix([x,0,1])
    A=-K+normal*(normal.T*K)/(normal.dot(normal))
    check(zero(A*a-lam/qx*a), 'source growing polarization is actual reference eigenvector')
    minus=s.Matrix([1,-c0*qx,-x])
    check(zero(A*minus+lam/qx*minus), 'opposite polarization is decaying eigenbranch')
    # The actual finite-L ratio equation: common viscosity cancels exactly.
    v=s.symbols('v',real=True)
    zp,zm=s.symbols('zp zm',real=True)
    e11,e12,e21,e22,damp=s.symbols('e11 e12 e21 e22 damp',real=True)
    zp_dot=(lam+e11-damp)*zp+e12*zm
    zm_dot=e21*zp+(-lam+e22-damp)*zm
    riccati=(zm_dot*zp-zm*zp_dot)/zp**2
    r=zm/zp
    check(zero(riccati-(-2*lam*r+e21+(e22-e11)*r-e12*r*r)),
          'finite-L polarization ratio equation cancels common damping')
    u0=s.Integer(2); c=s.Rational(1,4)
    check(1/s.sqrt(1+c*c)-4*(1+c*c)/(1+u0*u0)**s.Rational(3,2)>0,
          'asymmetric reference daughter has strictly positive net rate')
    # A weak overlap can keep both outputs small. These frozen equations
    # calibrate sizes only; their prescribed pumps omit nonlinear feedback.
    gamma,kappa,delta,bd,bs=s.symbols('gamma kappa delta bd bs',positive=True)
    daughter=delta*bd*(s.exp(gamma*v)-1)/gamma
    sideband=delta*bs*(1-s.exp(-kappa*v))/kappa
    check(zero(s.diff(daughter,v)-gamma*daughter-delta*bd)
          and daughter.subs(v,0)==0, 'frozen weak-overlap daughter response')
    check(zero(s.diff(sideband,v)+kappa*sideband-delta*bs)
          and sideband.subs(v,0)==0, 'frozen weak-overlap sideband response')
    # One exact rational asymmetric pair used in all-output Fourier jets.
    xp,ym=s.Rational(12,5),-s.Rational(15,8)
    C=out.subs({b:40,x:xp,y:ym,c0:-1})
    check(C != s.zeros(3,1), 'rational asymmetric source pair produces nonzero sum')


def add_key(p,q): return tuple(p[i]+q[i] for i in range(3))

def bilinear(U,V):
    """All Fourier outputs, without spatial/Galerkin truncation."""
    out={}
    for p,a in U.items():
        for q,b in V.items():
            k=add_key(p,q)
            if k==(0,0,0):
                continue
            f=-s.I*projection(k)*(a.dot(s.Matrix(q))*b)
            out[k]=out.get(k,s.zeros(3,1))+f
    return {k:v.applyfunc(s.simplify) for k,v in out.items() if not zero(v)}


def exact_all_outputs() -> dict:
    p=(96,0,40);q=(-75,0,40)
    ap=s.Matrix([1,-s.Rational(13,5),-s.Rational(12,5)])
    aq=s.Matrix([1,-s.Rational(17,8),s.Rational(15,8)])
    initial={p:ap,q:aq,tuple(-i for i in p):ap,tuple(-i for i in q):aq}
    N1=bilinear(initial,initial)
    kp=add_key(p,q);km=add_key(p,tuple(-i for i in q))
    check(set(N1)=={kp,km,tuple(-i for i in kp),tuple(-i for i in km)},
          'all quadratic plane-wave outputs are exactly sum/difference and conjugates')
    check(all(zero(s.Matrix(k).dot(v)) for k,v in N1.items()),
          'every generated quadratic output is solenoidal')
    check(all(zero(N1[tuple(-i for i in k)]-s.conjugate(v)) for k,v in N1.items()),
          'real field conjugacy is retained')
    # Coefficient cubic in amplitude in the second time derivative of full NS.
    # Ordinary viscosity adds lower-amplitude terms; it cannot remove these
    # cubic coefficients. This computes all outputs, not a closed triad ODE.
    part1=bilinear(initial,N1);part2=bilinear(N1,initial)
    N2={k:(part1.get(k,s.zeros(3,1))+part2.get(k,s.zeros(3,1))).applyfunc(s.simplify)
        for k in set(part1)|set(part2)}
    N2={k:v for k,v in N2.items() if not zero(v)}
    new=set(N2)-set(initial)-set(N1)
    check(bool(new), 'second nonlinear jet creates modes beyond chosen parent/daughter set')
    check(p in N2 and not zero(N2[p]), 'second nonlinear jet feeds back on first parent')
    check(q in N2 and not zero(N2[q]), 'second nonlinear jet feeds back on second parent')
    check(all(zero(s.Matrix(k).dot(v)) for k,v in N2.items()),
          'all second-jet outputs remain transverse')
    return {'initial_carriers':[list(k) for k in sorted(initial)],
            'quadratic_outputs':{str(k):[str(v) for v in N1[k]] for k in sorted(N1)},
            'second_nonlinear_jet_carriers':[list(k) for k in sorted(N2)],
            'additional_second_jet_carriers':[list(k) for k in sorted(new)],
            'scope':'Exact NS nonlinear Taylor coefficients of plane waves; no PDE solution or autonomous cell.'}


def reference_tables() -> dict:
    u=2.;lam=1.;g=2.
    def J(y): return math.asinh(y)-(y+y**3/3)/(1+u*u)**1.5
    gamma=(J(u)-J(u/2))/u
    D=lam/(1+u*u)**1.5
    preparation=[]
    for L in (16.,32.,64.,128.):
        W=L*L
        I=D*(W*(1+u*u/4+u*u/(L*L*g*g))-u*u*W*W/(2*L)+u*u*W**3/(3*L*L))
        lower=(-gamma*L+I-g*W/2)/math.log(10)
        preparation.append({'L':L,'W':W,'log10_entry_envelope':-gamma*L/math.log(10),
                            'log10_lower_bound_earlier_norm_per_unit_frame_norm':lower})
    overlap=[]
    for c in (0.,.01,.25,.5):
        q1,q2,qd=math.sqrt(1+(u+c)**2),math.sqrt(1+(c-u)**2),math.sqrt(1+c*c)
        beta=2*u*u*c*(1/(1+c*c)+2/(qd*(q1+q2))) # b=1
        mean_norm=2*u*math.sqrt((q1+q2)**2+4*c*c) # c0=-1
        growth=1/qd-4*(1+c*c)/(1+u*u)**1.5
        overlap.append({'u':u,'center_tilt':c,'sum_growing_coefficient_per_b':beta,
                        'difference_norm_per_b_c0_minus_one':mean_norm,
                        'daughter_growth_per_lambda0':growth,
                        'difference_to_growing_ratio':None if beta==0 else mean_norm/abs(beta)})
    return {'preparation':preparation,'overlap':overlap,
            'scope':'Floating-point evaluations of proved formulas; no numerical PDE claims.'}


def principal_calibrations() -> list[dict]:
    import numpy as np
    from check_source_pulse_adjoint import Principal
    rows=[]
    for L in (128.,512.,1024.):
        plus,minus=Principal(L,2.,1),Principal(L,2.,-1)
        hp,_=plus.solve();hm,_=minus.solve()
        for c in (0.,L**(-.75),.25):
            xp,xm=.5+c/2,.5-c/2
            ap=hp(xp);am=hm(xm);ap=ap/ap[0];am=am/am[0]
            p,_=plus.normal(xp);q,_=minus.normal(xm)
            kd=p+q;ke=p-q
            P=lambda k:np.eye(3)-np.outer(k,k)/(k@k)
            out=P(kd)@((ap@q)*am+(am@p)*ap)
            diff=P(ke)@(-(ap@q)*am+(am@p)*ap)
            kt=kd[1:]/np.linalg.norm(kd[1:]);nt=np.array([kt[1],-kt[0]])
            sc=kd[0]/np.linalg.norm(kd[1:]);qd=math.sqrt(1+sc*sc)
            beta=.5*(out[0]+out[1:]@nt/(plus.c0*qd))
            qr=math.sqrt(1+c*c);qsum=math.sqrt(1+(2+c)**2)+math.sqrt(1+(c-2)**2)
            ref=plus.Bs*8*c*(1/(1+c*c)+2/(qr*qsum))
            if not np.isfinite(beta) or np.linalg.norm(diff)<1:
                raise AssertionError('invalid principal-ODE calibration')
            if c==.25 and abs(beta-ref)>.01:
                raise AssertionError('asymmetric symbol/reference disagreement')
            rows.append({'L':int(L),'center_tilt':c,'sum_growing_coordinate':float(beta),
                         'reference_sum_growing_coordinate':ref,
                         'sum_norm':float(np.linalg.norm(out)),'difference_norm':float(np.linalg.norm(diff)),
                         'parent_amplitudes_normalized_by_radial_component':True})
    return rows


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--principal',action='store_true',help='run finite-L source-form ODE calibrations')
    parser.add_argument('--output',type=Path,help='explicit optional JSON report path')
    args=parser.parse_args()
    exact_preparation();exact_overlap();jets=exact_all_outputs()
    result={'exact_checks':CHECKS,'exact_check_count':len(CHECKS),'all_output_jet':jets,
            'formula_tables':reference_tables(),
            'principal_ode_calibrations':principal_calibrations() if args.principal else [],
            'status':'No common Schwartz history, completed regeneration cell, endpoint estimate, or unforced blow-up.'}
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(CHECKS)} named exact checks.')
    print('All quadratic outputs:',sorted(jets['quadratic_outputs']))
    print('Additional second-jet modes:',jets['additional_second_jet_carriers'])
    if args.principal:
        print('Finite-L principal calibrations:',len(result['principal_ode_calibrations']),
              '(floating point; not simultaneous source dyadic parameters).')
    print(result['status'])

if __name__=='__main__':
    main()
