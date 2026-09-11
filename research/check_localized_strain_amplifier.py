#!/usr/bin/env python3
"""Exact algebraic checks for the localized strain-amplifier note.

The analytic short-time amplification theorem also uses standard local smooth
Navier--Stokes well-posedness and continuity.  This checker freezes the curl
extension identity, relative-energy sign algebra, and fixed-viscosity scaling;
it is not a PDE solver or an iterated-turnover certificate.
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

# Generic symmetric trace-free linear strain.
x,y,z=sp.symbols('x y z',real=True)
a,b,c,d,e=sp.symbols('a b c d e',real=True)
S=sp.Matrix([[a,b,c],[b,d,e],[c,e,-a-d]])
X=sp.Matrix([x,y,z])
L=S*X
A=-X.cross(L)/3
curlA=sp.Matrix([
    sp.diff(A[2],y)-sp.diff(A[1],z),
    sp.diff(A[0],z)-sp.diff(A[2],x),
    sp.diff(A[1],x)-sp.diff(A[0],y),
])
check(sp.simplify(curlA-L)==sp.zeros(3,1),'curl[-x cross (Sx)/3] equals Sx')
check(S==S.T,'generic strain symmetric')
check(sp.trace(S)==0,'generic strain trace free')

# Normal-form purifier: desired e1, rejected e2, fixed carrier e3.
S0=sp.diag(-1,1,0)
e1=sp.Matrix([1,0,0]); e2=sp.Matrix([0,1,0]); e3=sp.Matrix([0,0,1])
check(S0*e1==-e1,'desired eigenvalue minus one')
check(S0*e2== e2,'rejected eigenvalue plus one')
check(S0*e3==sp.zeros(3,1),'carrier direction fixed')

# Strict Rayleigh/gradient margins used after taking the packet envelope large.
c0=sp.Rational(5)
r_des=sp.Rational(-9,10) # upper bound for <w,S w>/||w||^2
q_des=sp.Rational(9,2)   # upper bound for ||grad w||^2/||w||^2
half_growth=-c0*r_des-q_des
check(half_growth==0,'chosen coarse margins are threshold')
# The analytic proof takes strict inequalities: form < -9/10 and quotient < 9/2.
# Freeze a rational interior calibration with 19/20 and 17/4.
r_des2=sp.Rational(-19,20); q_des2=sp.Rational(17,4)
r_orth2=sp.Rational(19,20); q_orth2=sp.Rational(15,4)
G=-c0*r_des2-q_des2
D=-c0*r_orth2-q_orth2
check(G==sp.Rational(1,2),'desired strict half-energy growth margin calibration')
check(D==sp.Rational(-17,2),'orthogonal strict half-energy decay margin calibration')

# Fixed-viscosity NS scaling: if V(s,y) solves viscosity one, then
# u(t,x)=nu*b*V(nu*b^2*t,b*x) solves viscosity nu.
nu,B=sp.symbols('nu B',positive=True,real=True)
amp=nu*B
time_scale=nu*B**2
space_jac=B**-3
L2sq=sp.factor(amp**2*space_jac)
check(L2sq==nu**2/B,'L2 squared scaling nu^2/b')
L3=sp.factor(amp**3*space_jac)
check(L3==nu**3,'L3 cubed scaling is frequency independent')
check(sp.factor(time_scale**-1)==1/(nu*B**2),'parabolic physical clock')
# Gradient scale of the scaled velocity.
grad_scale=sp.factor(amp*B)
check(grad_scale==nu*B**2,'strain scale nu*b^2')

# Relative energy identity sign algebra for an affine germ c S0.
# 1/2 E' = -c <z,S0 z> - ||grad z||^2.
q1,q2,gq=sp.symbols('q1 q2 gq',nonnegative=True,real=True)
form=-q1+q2
rhs=sp.expand(-c0*form-gq)
check(rhs==5*q1-5*q2-gq,'relative energy production decomposition')

result={
  'status':'PASS_EXACT_LOCALIZED_STRAIN_SCALING',
  'exact_assertions':len(CHECKS),
  'curl_extension_identity':'curl[-x cross (Sx)/3]=Sx for symmetric trace-free S',
  'normal_form_strain':'diag(-1,1,0)',
  'strict_margin_calibration':{'desired_half_energy_rate':'1/2','orthogonal_half_energy_rate':'-17/2'},
  'fixed_viscosity_scaling':{
      'u_b':'nu*b*V(nu*b^2*t,b*x)',
      'L2_squared':'nu^2/b times dimensionless L2 squared',
      'L3_cubed':'nu^3 times dimensionless L3 cubed',
      'gradient':'nu*b^2 times dimensionless gradient',
      'clock':'1/(nu*b^2) times dimensionless time'
  },
  'scope':'Algebra/scaling only; short-time continuum persistence uses local NS theory and is proved in the evidence note.'
}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    text=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    print(f'PASS: {len(CHECKS)} exact assertions.')
    print(text,end='')

if __name__=='__main__': main()
