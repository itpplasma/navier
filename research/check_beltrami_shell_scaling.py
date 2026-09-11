#!/usr/bin/env python3
"""Exact exponent ledger for finite-energy thin-shell Beltrami localization.

This checker does not certify nonlinear stability.  It freezes one explicit
parameter sequence showing that order-one Raman strength is compatible with a
vanishing raw thin-shell Beltrami defect, small heat dephasing, long pump
lifetime, and high-parent amplitude small relative to the clean stage.
"""
from __future__ import annotations
import sympy as sp

s=sp.symbols('s', positive=True)
Re=s**12
R=s**4                 # N/b
rho=s**2               # P/(nu N)
eps=s**-1              # delta/b

checks={
    'order-one Raman strength': sp.simplify(rho**2/R-1)==0,
    'pump lifetime margin R^2/Re': sp.simplify(R**2/Re-s**-4)==0,
    'high-parent/clean amplitude': sp.simplify(R**sp.Rational(3,2)/Re-s**-6)==0,
    'raw shell defect / high parent': sp.simplify(rho*eps/R-s**-3)==0,
    'high-time heat dephasing': sp.simplify(eps/R-s**-5)==0,
    'raw shell defect / clean amplitude':
        sp.simplify((R**sp.Rational(3,2)/Re)*(rho*eps/R)-s**-9)==0,
    'envelope broader than clean wavelength': sp.simplify(1/eps-s)==0,
}
for label,ok in checks.items():
    if not bool(ok): raise AssertionError(label)

print(f'PASS: {len(checks)} exact scaling identities.')
print('Re=s^12, R=s^4, rho=s^2, delta/b=s^-1 keeps rho^2/R=1.')
print('Raw shell-defect/high-parent ratio=s^-3; heat dephasing=s^-5; raw defect/clean=s^-9.')
print('Scope: source and scale compatibility only; large high-slow linearized stability is not proved.')
