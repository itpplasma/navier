#!/usr/bin/env python3
"""Exact mode-specific affine polarization purifier checks.

This certifies a finite-time Kelvin-mode mechanism about an exact affine
unforced Navier--Stokes background.  It is NOT a finite-energy localization,
a multi-mode routed turnover, or a blowup proof.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp

CHECKS=[]

def check(ok,label):
    if not bool(ok):
        raise AssertionError(label)
    CHECKS.append(label)

z,nu,b,t=sp.symbols('z nu b t', positive=True, real=True)
k=sp.Matrix([0,1,0])
a=sp.Matrix([1,0,z])
w=sp.Matrix([-z,0,1])
D=1+z**2
S=sp.Matrix([
    [z**2-1,0,-2*z],
    [0,0,0],
    [-2*z,0,1-z**2],
])/D

check(S==S.T,'purifier strain symmetric')
check(sp.simplify(sp.trace(S))==0,'purifier strain trace free')
check(S*k==sp.zeros(3,1),'target wavevector is in purifier kernel')
check(sp.simplify(k.dot(a))==0 and sp.simplify(k.dot(w))==0,'desired and orthogonal directions transverse')
check(sp.simplify(a.dot(w))==0,'desired and pollutant directions orthogonal')
check(sp.simplify(S*a+a)==sp.zeros(3,1),'desired polarization eigenvalue minus one')
check(sp.simplify(S*w-w)==sp.zeros(3,1),'orthogonal polarization eigenvalue plus one')
check(sp.simplify(S*S-sp.diag(1,0,1))==sp.zeros(3),'purifier square is transverse projector')

# Constant affine background U=sigma S x is an exact steady unforced NS
# solution, with convection sigma^2 S^2 x absorbed by quadratic pressure.
sigma=sp.symbols('sigma', positive=True, real=True)
check(S*S==(S*S).T,'affine convection matrix is symmetric pressure Hessian')

# For physical target wavevector K=2 b k, k is fixed because S k=0.
K2=4*b**2
r_des=sp.factor(sigma-nu*K2)
r_orth=sp.factor(-sigma-nu*K2)
check(r_des==sigma-4*nu*b**2,'desired amplitude rate')
check(r_orth==-sigma-4*nu*b**2,'orthogonal amplitude rate')
check(sp.factor(r_orth-r_des)==-2*sigma,'exact polarization spectral gap')

# At sigma=5 nu b^2 the desired component grows while the orthogonal one
# decays strongly, without moving the target wavevector.
sigma5=5*nu*b**2
check(sp.simplify(r_des.subs(sigma,sigma5)-nu*b**2)==0,'sigma=5 gives desired rate plus nu b^2')
check(sp.simplify(r_orth.subs(sigma,sigma5)+9*nu*b**2)==0,'sigma=5 gives orthogonal rate minus 9 nu b^2')

# The premature clean-gate pollutant e3 at the doubled k2 frequency splits
# exactly into desired a2 plus its transverse orthogonal complement.
e3=sp.Matrix([0,0,1])
recon=sp.simplify(z/D*a+1/D*w)
check(recon==e3,'premature e3 pollutant exact desired/orthogonal decomposition')

# Exact finite-time purification formula at sigma=5 nu b^2.
# Overall viscosity cancels from the component ratio.
ratio=sp.exp(-2*sigma5*t)/z
check(sp.simplify(sp.diff(sp.log(ratio),t)+10*nu*b**2)==0,
      'orthogonal-to-desired coefficient ratio decays at 10 nu b^2')

# General coordinate-free construction calibration on a rational orthogonal
# triple: k0=e3, a0=e1, w0=e2 gives diag(-1,+1,0).
S0=sp.diag(-1,1,0)
check(sp.trace(S0)==0 and S0*sp.Matrix([0,0,1])==sp.zeros(3,1),
      'coordinate-free purifier normal form')

result={
    'status':'PASS_EXACT_MODE_SPECIFIC_PURIFIER',
    'exact_assertions':len(CHECKS),
    'target_clean_channel':'doubled k2 with desired polarization a2=(1,0,z)',
    'strain_matrix':[[str(sp.factor(S[i,j])) for j in range(3)] for i in range(3)],
    'physical_wavevector':'K=2 b (0,1,0)',
    'finite_time_rates_at_sigma_5_nu_b2':{
        'desired':'nu*b^2',
        'orthogonal':'-9*nu*b^2',
        'relative_decay':'exp(-10*nu*b^2*t)'
    },
    'pollutant_decomposition':'e3 = z/(1+z^2) a2 + 1/(1+z^2) w2, w2=(-z,0,1)',
    'scope':'Exact affine infinite-energy one-frequency mechanism; no localized multi-mode turnover certificate.'
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

if __name__=='__main__':
    main()
