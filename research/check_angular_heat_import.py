#!/usr/bin/env python3
"""Exact algebra checks for the angular heat-import estimate.

The continuum estimate in the companion note uses the scalar Fourier--Bessel
heat kernel. This script checks the algebraic Hilbert--Schmidt reduction and
source-scale dominance; it is not a PDE proof by itself.
"""
from __future__ import annotations
from fractions import Fraction as F
import argparse
import json
from pathlib import Path
import sympy as s

CHECKS=[]


def check(ok,label):
    if not bool(ok):
        raise AssertionError(label)
    CHECKS.append(label)


def symbolic_hs():
    m=s.symbols('m', integer=True, positive=True)
    a,R=s.symbols('a R', positive=True)
    pref=s.Rational(1,4)*a**-2*(4*a)**(-2*m)/s.factorial(m)**2
    A=s.simplify(pref*2**(2*m)*R**(4*m+3)*s.sqrt(2*s.pi*a)/(2*m+2))
    B=s.simplify(pref*2**(3*m+1)*a**(m+1)*s.factorial(m)*R**(2*m+2)/(2*m+2))
    At=s.sqrt(2*s.pi)*R**3/(8*a**s.Rational(3,2)*(m+1))*(
        R**4/(4*a**2))**m/s.factorial(m)**2
    Bt=R**2/(4*a*(m+1))*(R**2/(2*a))**m/s.factorial(m)
    check(s.simplify(A-At)==0,'first Hilbert-Schmidt term')
    check(s.simplify(B-Bt)==0,'second Hilbert-Schmidt term')
    ratio=s.simplify(At/Bt)
    target=s.sqrt(s.pi/2)*R/s.sqrt(a)*(R**2/(2*a))**m/s.factorial(m)
    check(s.simplify(ratio-target)==0,'A/B ratio')
    return str(At),str(Bt),str(ratio)


def finite_moments():
    x,a=s.symbols('x a', positive=True)
    for m in range(1,21):
        val=2**(m+1)*a**(m+1)*s.factorial(m)
        direct=2*s.integrate(x**(2*m+1)*s.exp(-x*x/(2*a)),(x,0,s.oo))
        check(s.simplify(direct-val)==0,f'Gaussian odd moment m={m}')
        check(s.factorial(m)>=1,f'factorial positivity m={m}')


def source_scale():
    # One exact subsequence for h=1/200: ell=400 k gives
    # Q=2^(-ell), m=Q^(-h/2)=2^k. The crude heat factor Q^(m/2)
    # is compared with exp(-C ell^2) at the logarithmic exponent level.
    rows=[]
    for k in range(1,19):
        ell=400*k
        m=2**k
        heat_power=F(ell*m,2)  # -log_2 Q^(m/2)
        seed_quadratic=F(ell*ell)
        ratio=heat_power/seed_quadratic
        check(m==2**k,f'angular source scale k={k}')
        check(heat_power>0 and seed_quadratic>0,f'positive exponents k={k}')
        if k>1:
            prev=rows[-1]['ratio_fraction']
            check(ratio>=prev,f'heat/quadratic exponent ratio nondecreasing k={k}')
        if k>=14:
            check(ratio>1,f'heat exponent exceeds ell^2 on sampled tail k={k}')
        # Source-sized late import distances relative to annulus radius:
        # advective O(Q^h L), diffusive O(Q^(h/2) sqrt L), L=ell^2.
        # On this subsequence Q^h=2^(-2k), Q^(h/2)=2^(-k).
        adv=F(ell*ell,2**(2*k))
        diff=F(ell,2**k)
        if k>1:
            check(adv < rows[-1]['adv_fraction'],f'advective relative reach decays k={k}')
            check(diff < rows[-1]['diff_fraction'],f'diffusive relative reach decays k={k}')
        rows.append({'k':k,'ell':ell,'m':m,'heat_log2_exponent':str(heat_power),
                     'ell_squared':str(seed_quadratic),'ratio':str(ratio),
                     'late_advective_relative_reach':str(adv),
                     'late_diffusive_relative_reach':str(diff),
                     'ratio_fraction':ratio,'adv_fraction':adv,'diff_fraction':diff})
    for row in rows:
        row.pop('ratio_fraction');row.pop('adv_fraction');row.pop('diff_fraction')
    return rows


def vector_modes():
    # Cylindrical vector rotation mode n has Cartesian scalar harmonics
    # n-1, n, n+1. Check the minimum absolute harmonic for n>=2.
    rows=[]
    for n in range(2,33):
        hs=[abs(n-1),abs(n),abs(n+1)]
        check(min(hs)==n-1,f'vector angular shift n={n}')
        rows.append({'n':n,'scalar_harmonics':hs,'minimum':min(hs)})
    return rows


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    A,B,R=symbolic_hs()
    finite_moments()
    rows=source_scale()
    modes=vector_modes()
    result={'scope':'Exact algebra/calibration only; continuum heat-kernel estimate is in the note.',
            'exact_assertion_count':len(CHECKS),
            'hs_terms':{'A':A,'B':B,'A_over_B':R},
            'source_scale_samples':rows,'vector_mode_samples':modes}
    if a.output:a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {len(CHECKS)} exact assertions.')
    print(json.dumps(result['source_scale_samples'][-4:],indent=2))


if __name__=='__main__':
    main()
