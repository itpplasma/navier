#!/usr/bin/env python3
"""Finite arithmetic and source regressions, not an independent proof audit."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import math
import random
import re

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--integrated', action='store_true')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
assert F(3,4)*F(2,3) == F(1,2)
assert F(32,27)*F(9,8) == F(4,3)
assert 2*F(4,3) == F(8,3)
assert F(1,2)**4 == F(1,16)
assert F(1,9)+F(7,18)+F(1,2) == 1
assert F(2,3)*F(1,2)+F(1,3)*F(1,6) == F(7,18)
rng = random.Random(20260906)
for _ in range(1000):
    n = [rng.uniform(-1,1) for _ in range(3)]
    norm = math.sqrt(sum(x*x for x in n))
    n = [x/norm for x in n]
    N = [[n[i]*n[j]-(1/3 if i==j else 0) for j in range(3)] for i in range(3)]
    assert abs(sum(N[i][i] for i in range(3))) < 2e-15
    assert abs(sum(x*x for row in N for x in row)-2/3) < 2e-15
    # Finite-dimensional identity only; not a PDE solution or a multiplier norm test.
    A = [[rng.uniform(-1,1) for j in range(3)] for i in range(3)]
    tr = sum(A[i][i] for i in range(3))/3
    for i in range(3): A[i][i] -= tr
    T = [[rng.uniform(-1,1) for j in range(3)] for i in range(3)]
    tr = sum(T[i][i] for i in range(3))/3
    for i in range(3): T[i][i] -= tr
    d = -.75*sum(N[i][j]*(A[i][j]+T[i][j]) for i in range(3) for j in range(3))
    B = [[A[i][j]+T[i][j]+(d/3 if i==j else 0) for j in range(3)] for i in range(3)]
    assert abs(d+sum(n[i]*B[i][j]*n[j] for i in range(3) for j in range(3))) < 2e-15
for M in (2,3,10,100,1e6):
    eps = min(.1, math.log(2)/(8*math.log(M)))
    for reciprocal in (.5-eps, .5, .5+eps):
        r = 1/reciprocal
        theta = 4*abs(1/r-.5)
        assert 4/3 < r < 4 and .5*M**theta < 1

section = (root/'sections/defect_extensions.tex').read_text()
labels = re.findall(r'\\label\{([^}]+)\}', section)
assert len(labels) == len(set(labels))
required = {'de:section','de:fixedpoint','de:near2','de:quotient-clock','de:no-separation'}
assert required <= set(labels)
assert 'independent' in section and 'audit pending' in section
assert 'original' in section and 'remain unproved' in section
assert 'must not be applied to $d$ before proving' in section
assert 'on $\\{w=0\\}$' in section and 'harmonic ambiguity' in section
if a.integrated:
    main = (root/'main.tex').read_text()
    assert main.count(r'\input{sections/defect_extensions}') == 1
    assert 'Whether a branch with' not in main
    assert 'Second, for $a\\ne2$ no' not in main
    assert 'No arbitrary-data critical bound is proved here.' in main
    assert 'HaaralaSarsa2022' in (root/'references.bib').read_text()
    alltex = main+'\n'+section+'\n'+(root/'sections/dissipation_clock.tex').read_text()
    for label in labels:
        assert alltex.count('\\label{'+label+'}') == 1
    for label in re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', section):
        assert '\\label{'+label+'}' in alltex, f'unresolved source reference: {label}'
print('PASS: exact constants, 1000 matrix identities, interpolation windows and source guards.')
print('Scope: finite regression only; no independent mathematical audit or Lean proof.')
