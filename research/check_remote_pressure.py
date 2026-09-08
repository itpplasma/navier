#!/usr/bin/env python3
"""Exact algebra regressions for the remote-Hessian proof; no PDE certification."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as s

checks: list[str] = []

def check(label, condition):
    if not bool(condition):
        raise AssertionError(label)
    checks.append(label)

def zero(expr):
    return all(s.simplify(e) == 0 for e in expr) if isinstance(expr, s.MatrixBase) else s.simplify(expr) == 0

x,y,z,L=s.symbols('x y z L', real=True, positive=True)
X=s.Matrix([x,y,z]); coordinates=list(X)
I=s.eye(3); axis=s.Matrix([0,0,1])

def curl(v):
    return s.Matrix([s.diff(v[2],y)-s.diff(v[1],z),
                     s.diff(v[0],z)-s.diff(v[2],x),
                     s.diff(v[1],x)-s.diff(v[0],y)])

def lap(v):
    return v.applyfunc(lambda e:sum(s.diff(e,c,2) for c in coordinates))

def adv(u,v):
    return v.jacobian(coordinates)*u

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    args=parser.parse_args()
    G=1/(4*s.pi*s.sqrt(x*x+y*y+z*z))
    K=s.Matrix(3,3,lambda i,j:s.simplify(s.diff(G,coordinates[i],coordinates[j],z,z).subs({x:0,y:0,z:L})))
    check('axial D_ab33 Newton kernel',zero(K-12*(3*axis*axis.T-I)/(4*s.pi*L**5)))
    check('axial Hessian trace',s.trace(K)==0)
    Ktrans=s.Matrix(3,3,lambda i,j:s.simplify(sum(s.diff(G,coordinates[i],coordinates[j],coordinates[k],coordinates[k]) for k in [0,1]).subs({x:0,y:0,z:L})))
    check('transverse stress contraction',zero(Ktrans+K))
    f=s.Function('f')(x*x+y*y,z)
    w=f*s.Matrix([-y,x,0])
    check('general compact swirl divergence',zero(sum(s.diff(w[i],coordinates[i]) for i in range(3))))
    a,b,c=s.symbols('a b c',real=True)
    # Rational orthogonal Householder frames and trace-free spectra.
    frames=[I]+[I-2*v*v.T/(v.dot(v)) for v in [s.Matrix([1,2,3]),s.Matrix([2,-1,2]),s.Matrix([1,1,1])]]
    spectra=[[-2,-1,3],[1,1,-2],[0,0,0],[-5,7,-2]]
    for index,O in enumerate(frames):
        check(f'frame {index} orthogonal',zero(O.T*O-I))
        for hs in spectra:
            hmax=max(hs)
            weights=[s.Rational(hmax-h,3) for h in hs] # |c_L| normalized to one
            H=O*s.diag(*hs)*O.T
            result=s.zeros(3)
            for i in range(3):
                n=O[:,i]
                result-=weights[i]*(3*n*n.T-I)
            check(f'assembly {index} {hs}',zero(result-H))
            check(f'energy/positivity {index} {hs}',sum(weights)==hmax and min(weights)>=0 and sum(q!=0 for q in weights)<=2)
    A=s.Matrix([[a,2,3],[4,b,5],[6,7,-a-b]])
    check('affine solenoidal cutoff interior',zero(curl(-X.cross(A*X)/3)-A*X))
    rate,Omega=s.symbols('rate Omega',positive=True)
    A0=s.diag(-rate/2,-rate/2,rate)+s.Matrix([[0,-Omega/2,0],[Omega/2,0,0],[0,0,0]])
    om=curl(A0*X)
    check('affine vorticity',zero(om-Omega*axis))
    check('maximal positive strain alignment',zero(A0*om-rate*om))
    check('affine viscous spatial terms vanish',zero(lap(om)) and zero(lap(A0*X)))
    u=curl(s.Matrix([x*x*y*z,y*y*z*z,z*z*x*x*y]))
    omega=curl(u)
    rhs=-adv(lap(u),omega)-2*sum((omega.diff(coordinates[i]).jacobian(coordinates)*u.diff(coordinates[i]) for i in range(3)),s.zeros(3,1))
    check('material/Laplacian commutator',zero(adv(u,lap(omega))-lap(adv(u,omega))-rhs))
    report={'status':'PASS','assertions':len(checks),'checks':checks,
            'scope':'Exact finite algebra only; no PDE verification, full repository check or independent audit.'}
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(report,indent=2)+'\n')
    print(f'PASS: {len(checks)} exact pressure-kernel and material-identity assertions.')
    print(report['scope'])

if __name__=='__main__':
    main()
