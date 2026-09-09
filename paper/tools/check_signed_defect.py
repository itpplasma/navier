#!/usr/bin/env python3
"""Finite algebra/source regressions; not a mathematical audit or PDE test."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import math
import random
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--integrated', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
rng = random.Random(2026090631)

# All factors in the two Young maxima, including the factor 3 from ||V||2^2.
assert F(27,32)*F(2,3)**4*3 == F(1,2)
assert F(27,256)*F(2,3)**4/F(4,9)**3 == F(9,8)**3/6
assert F(27,256)/F(4,9)**3*F(16,81) == F(9,8)**3/6
assert F(3,1)*F(9,8)**3/6 == F(9,8)**3/2
assert F(1,16)*F(1,2) == F(1,32)
assert F(4,9)*F(9,8) == F(1,2)

for _ in range(1000):
    nu, sigma, sob = (10**rng.uniform(-2,2) for _ in range(3))
    alpha = (2/3)*sigma*sob**1.5
    eps = 4*nu/9
    xmax = (3*alpha/(4*eps))**4
    maximum = 27*alpha**4/(256*eps**3)
    assert math.isclose(alpha*xmax**.75-eps*xmax, maximum, rel_tol=1e-12)
    # Optimal scalar tail inequality, equality at x/k=4.
    y = 10**rng.uniform(-2,5)
    assert max(y-1,0)**1.5 <= (3*math.sqrt(3)/16)*y*y*(1+1e-14)
assert math.isclose(3**1.5/16, 3*math.sqrt(3)/16)

for _ in range(1000):
    z = [rng.uniform(-3,3) for _ in range(3)]
    zz = sum(a*a for a in z)
    tf = [[z[i]*z[j]-(zz/3 if i==j else 0) for j in range(3)] for i in range(3)]
    assert math.isclose(sum(a*a for row in tf for a in row), (2/3)*zz*zz,
                        rel_tol=1e-12, abs_tol=1e-12)
    a,b = rng.uniform(-3,3),rng.uniform(-3,3)
    eig = [a,b,-a-b]
    assert max(eig) >= 0
    assert max(eig)**2 <= (2/3)*sum(v*v for v in eig)+1e-12

source = (root/'sections/signed_defect.tex').read_text()
labels = re.findall(r'\\label\{([^}]+)\}', source)
assert len(labels) == len(set(labels))
assert {'sd:cancellation','sd:improved','sd:form-clock',
        'sd:missing-bound-consumer','sd:tail'} <= set(labels)
assert 'independent mathematical audit' in source
assert 'remains unproved' in source and 'No open claim has been promoted.' in source
assert 'No weighted moment hypothesis is needed.' in source
if args.integrated:
    main = (root/'main.tex').read_text()
    assert main.count(r'\input{sections/signed_defect}') == 1
    assert 'No arbitrary-data critical bound is proved here.' in main
    assert 'Miller2021Sum' in (root/'references.bib').read_text()
    tex = main+'\n'+'\n'.join(p.read_text() for p in (root/'sections').glob('*.tex'))
    for label in labels:
        assert tex.count('\\label{'+label+'}') == 1, label
    for ref in re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', source):
        assert '\\label{'+ref+'}' in tex, ref
print('PASS: exact Young/tail constants, 2000 finite algebra probes, source and label checks.')
print('Not an independent audit, a PDE trajectory test, or a Lean proof.')
