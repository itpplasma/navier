#!/usr/bin/env python3
"""Arithmetic and source regression only; not a mathematical proof checker."""
from fractions import Fraction as F
from pathlib import Path
import math
import re
import sys

root = Path(__file__).resolve().parents[1]
source = root / 'sections/dissipation_clock.tex'
text = source.read_text()
assert F(1, 9) + F(7, 18) + F(1, 2) == 1
assert F(2, 3) / 2 + F(1, 3) / 6 == F(7, 18)
assert F(32, 27) * F(9, 8) == F(4, 3)
assert F(4, 3) / 3 == F(4, 9)
assert F(2, 3) + F(3, 9) == 1  # Serrin scaling
samples = 0
for nu in (0.125, 0.5, 1.0, 3.0, 8.0):
    for a in (0.0, 0.01, 0.25, 1.0, 7.0):
        zstar = (4*a/(3*nu))**3
        for factor in (0.0, 0.001, 0.1, 0.5, 1.0, 2.0, 10.0, 1000.0):
            z = zstar*factor
            lhs = 2*a*z**(2/3)
            rhs = nu*z + 32*a**3/(27*nu**2)
            assert lhs <= rhs + 1e-11*max(1.0, abs(rhs))
            if factor == 1:
                assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)
            samples += 1
for nu in (0.2, 1.0, 5.0):
    for b0 in (0.3, 2.0):
        for eta in (0.1, 1.0):
            for budget in (0.0, 0.01, 0.1):
                barrier = b0*math.expm1(budget/(eta*nu*b0))
                recovered = eta*nu*b0*math.log1p(barrier/b0)
                assert math.isclose(recovered, budget, rel_tol=1e-12, abs_tol=1e-12)
                assert eta*nu*b0*math.log1p((barrier+b0)/b0) > budget
# Scalar obstruction with Phi(B)=1-exp(-B), K=2, nu=3.
for t in (0.0, 0.1, 0.5, 0.9, 0.99, 0.9999):
    b, d = -math.log1p(-t), 1/(1-t)
    phi, dphi = 1-math.exp(-b), math.exp(-b)
    x, xprime, p = 3*(2-phi), -3*dphi*d, (3-dphi)*d
    assert x > 0
    assert math.isclose(xprime/3+3*d, p, rel_tol=1e-12)
    assert math.isclose(x/3+3*b, 2+3*b-phi, rel_tol=1e-12)
labels = re.findall(r'\\label\{([^}]+)\}', text)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', text)
assert len(labels) == len(set(labels)), 'duplicate component labels'
assert set(refs) <= set(labels), 'unresolved internal component references'
assert 'No terminal or open estimate is discharged' in text
if '--integrated' in sys.argv:
    main = (root/'main.tex').read_text()
    assert main.count(r'\input{sections/dissipation_clock}') == 1
    assert 'review-pending extension' in main
    assert 'No arbitrary-data critical bound is proved here.' in main
print(f'PASS: exact exponents/constants, {samples} Young samples, logarithmic inversions, scalar boundary, {len(labels)} labels.')
print('Scope: arithmetic/source regression only; no PDE correctness or independent audit is certified.')
