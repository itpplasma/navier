#!/usr/bin/env python3
"""Exact viscous affine-strain router checks for the dyadic Leray gate.

Pure SymPy rational algebra.  This certifies instantaneous Kelvin-wave
energy rates about one exact affine unforced Navier--Stokes background.  It
does NOT certify a finite-time packet gate, a localized R3 embedding, a
multi-generation turnover, or blowup.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp

CHECKS=[]

def check(ok,label):
    if not bool(ok): raise AssertionError(label)
    CHECKS.append(label)

def V(*xs): return sp.Matrix([sp.Rational(x) for x in xs])

# Rational trace-free symmetric strain found by exactifying the sign-margin
# search.  For U=sigma*S*x, this is an exact steady affine unforced NS
# background with pressure -sigma^2 x.S^2.x/2 (infinite-energy scope).
S=sp.Matrix([
    [-1, 1, sp.Rational(-1,5)],
    [ 1,-1, sp.Rational( 3,5)],
    [sp.Rational(-1,5),sp.Rational(3,5),2],
])
check(S==S.T,'strain is symmetric')
check(sp.trace(S)==0,'strain is incompressible')

# Complete first quadratic generation of the real six-mode dyadic input.
OUTPUTS={
 (-2,-1,-1):V(sp.Rational(-10,9), sp.Rational(10,9), sp.Rational(10,9)),
 (-2,-1, 0):V(sp.Rational(-1,5),  sp.Rational( 2,5), sp.Rational( 1,6)),
 (-2, 0,-1):V(sp.Rational(-1,10), -1,                 sp.Rational( 1,5)),
 ( 0,-1, 0):V(-1,0,sp.Rational(7,6)),
 ( 0,-1, 1):V(sp.Rational(-2,3), sp.Rational( 2,3), sp.Rational( 2,3)),
 ( 0, 0,-1):V(sp.Rational(-1,2),1,0),
 ( 0, 0, 1):V(sp.Rational( 1,2),-1,0),
 ( 0, 1,-1):V(sp.Rational( 2,3),sp.Rational(-2,3),sp.Rational(-2,3)),
 ( 0, 1, 0):V(1,0,sp.Rational(-7,6)),
 ( 2, 0, 1):V(sp.Rational( 1,10),1,sp.Rational(-1,5)),
 ( 2, 1, 0):V(sp.Rational( 1,5),sp.Rational(-2,5),sp.Rational(-1,6)),
 ( 2, 1, 1):V(sp.Rational(10,9),sp.Rational(-10,9),sp.Rational(-10,9)),
}

# Desired first-generation outputs and ALL reality conjugates.  This also
# repairs the old validation-label omission of (-2,0,-1), the conjugate of
# (2,0,1).  That omission did not alter the old carrier algebra.
SELECTED={
 (-2,-1,0),(2,1,0),
 (0,0,-1),(0,0,1),
 (2,0,1),(-2,0,-1),
}
check(len(SELECTED)==6,'six selected outputs including reality conjugates')
check((-2,0,-1) in SELECTED,'missing conjugate label is restored')
check(set(SELECTED) < set(OUTPUTS),'selected outputs are in complete generation')

rho=sp.symbols('rho', positive=True, real=True) # rho=sigma/(nu*b^2)
rows={}
for ktuple,a in sorted(OUTPUTS.items()):
    k=sp.Matrix(ktuple)
    check(sp.simplify(k.dot(a))==0,f'transverse output {ktuple}')
    n2=sp.factor(a.dot(a))
    q=sp.factor((a.T*S*a)[0])
    qratio=sp.factor(q/n2)
    k2=sp.Integer(k.dot(k))
    # For carrier b*k and strain sigma*S, Kelvin-wave amplitude energy obeys
    # (1/2)d_t|a|^2 = -sigma a.S.a - nu*b^2|k|^2|a|^2.
    # Divide the logarithmic amplitude rate by nu*b^2.
    rate=sp.factor(-rho*qratio-k2)
    rows[ktuple]=(n2,q,qratio,k2,rate)

expected_qratio={
 (-2,-1,-1):sp.Rational(-2,15),
 (-2,-1, 0):sp.Rational(-38,41),
 (-2, 0,-1):sp.Rational(-481,525),
 ( 0,-1, 0):sp.Rational(394,425),
 ( 0,-1, 1):sp.Rational(-2,15),
 ( 0, 0,-1):sp.Rational(-9,5),
 ( 0, 0, 1):sp.Rational(-9,5),
 ( 0, 1,-1):sp.Rational(-2,15),
 ( 0, 1, 0):sp.Rational(394,425),
 ( 2, 0, 1):sp.Rational(-481,525),
 ( 2, 1, 0):sp.Rational(-38,41),
 ( 2, 1, 1):sp.Rational(-2,15),
}
for k,v in expected_qratio.items():
    check(rows[k][2]==v,f'exact normalized strain form {k}')

# Exact open window where every selected output has positive instantaneous
# amplitude rate and every genuine contaminant has negative rate.
lower=sp.Rational(2625,481)
upper=sp.Rational(15,1)
check(lower>sp.Rational(205,38),'g3 gives the active selected lower threshold')
check(lower>sp.Rational(5,9),'g3 threshold dominates vertical selected mode')
check(lower<upper,'nonempty viscous-router window')

# Validate signs at an interior rational point rho=6.
rho0=sp.Rational(6)
check(lower<rho0<upper,'rho=6 lies strictly inside router window')
rates6={k:sp.factor(row[4].subs(rho,rho0)) for k,row in rows.items()}
for k,r in rates6.items():
    check(r>0 if k in SELECTED else r<0,
          f'rho=6 strict selected/contaminant sign {k}')

expected_rates6={
 (-2,-1,-1):sp.Rational(-26,5),
 (-2,-1, 0):sp.Rational(23,41),
 (-2, 0,-1):sp.Rational(87,175),
 ( 0,-1, 0):sp.Rational(-2789,425),
 ( 0,-1, 1):sp.Rational(-6,5),
 ( 0, 0,-1):sp.Rational(49,5),
 ( 0, 0, 1):sp.Rational(49,5),
 ( 0, 1,-1):sp.Rational(-6,5),
 ( 0, 1, 0):sp.Rational(-2789,425),
 ( 2, 0, 1):sp.Rational(87,175),
 ( 2, 1, 0):sp.Rational(23,41),
 ( 2, 1, 1):sp.Rational(-26,5),
}
for k,v in expected_rates6.items():
    check(rates6[k]==v,f'exact rho=6 rate {k}')

check(min(rates6[k] for k in SELECTED)==sp.Rational(87,175),
      'selected positive margin at rho=6')
check(max(rates6[k] for k in OUTPUTS if k not in SELECTED)==sp.Rational(-6,5),
      'contaminant negative margin at rho=6')

# The affine field itself is an exact steady unforced NS solution: Delta U=0,
# div U=0, (U.grad)U=sigma^2 S^2 x is the gradient of
# sigma^2 x.S^2.x/2.  The checker records its algebraic prerequisites.
check((S*S)==(S*S).T,'S^2 is symmetric pressure Hessian')

result={
 'status':'PASS_EXACT_INSTANTANEOUS_VISCOUS_ROUTER',
 'exact_assertions':len(CHECKS),
 'strain_matrix':[[str(S[i,j]) for j in range(3)] for i in range(3)],
 'rho_definition':'rho=sigma/(nu*b^2)',
 'strict_router_window':{'lower':str(lower),'upper':str(upper)},
 'test_rho':'6',
 'selected_centers':[list(k) for k in sorted(SELECTED)],
 'rates_at_rho_6':{str(k):str(v) for k,v in sorted(rates6.items())},
 'selected_min_rate_at_rho_6':'87/175',
 'contaminant_max_rate_at_rho_6':'-6/5',
 'scope':'Instantaneous Kelvin-wave rates about an affine infinite-energy exact unforced NS background; no finite-time/localized/iterated gate certificate.'
}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    text=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    print(f"PASS: {len(CHECKS)} exact assertions.")
    print(text,end='')

if __name__=='__main__': main()
