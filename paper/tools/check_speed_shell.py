#!/usr/bin/env python3
"""Finite algebra and source regressions only; not a PDE or independent audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import random
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--integrated', action='store_true')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = root/'sections/speed_shell.tex'
text = source.read_text()
assert hashlib.sha256(source.read_bytes()).hexdigest() == '6d4ed41005c59d2734a1befc41779ec63e0bd6805c3178dc42b54c9a0efae4da'
labels = ['ss:shell', 'ss:residual', 'ss:clock', 'ss:gauge', 'ss:consumer']
for label in labels:
    assert text.count('\\label{'+label+'}') == 1, label
assert F(27,32)*F(2,3)**4*3 == F(1,2)
assert F(4,3)*2 == F(8,3)
assert F(1,16)*F(1,2) == F(1,32)
# Renormalized flux: rho*h'(rho)-h(rho) is the superlevel indicator.
for k in [F(1,8), F(1,2), F(1), F(7,2)]:
    for rho in [F(0), k/2, 2*k, 17*k]:
        h = max(rho/k-1, 0)
        dh = 1/k if rho > k else F(0)
        assert rho*dh-h == int(rho > k)
# Finite weighted Hilbert-space analogues of shell projection.
rng = random.Random(20260906)
for _ in range(400):
    size = 24
    weight = [F(rng.randint(1,7)) for _ in range(size)]
    shell = [i//4 for i in range(size)]
    chi = [F(rng.randint(-20,20),7) for _ in range(size)]
    raw = [F(rng.randint(-15,15),11) for _ in range(size)]
    mass = [sum(weight[i] for i in range(size) if shell[i] == j) for j in range(6)]
    avg = [sum(weight[i]*chi[i] for i in range(size) if shell[i] == j)/mass[j] for j in range(6)]
    sigavg = [sum(weight[i]*raw[i] for i in range(size) if shell[i] == j)/mass[j] for j in range(6)]
    sigma = [raw[i]-sigavg[shell[i]] for i in range(size)]
    residual = [chi[i]-avg[shell[i]] for i in range(size)]
    dot = lambda a,b: sum(weight[i]*a[i]*b[i] for i in range(size))
    assert dot(sigma,chi) == dot(sigma,residual)
    norm = dot(chi,chi)
    projected = sum(mass[j]*avg[j]**2 for j in range(6))
    assert norm-projected == dot(residual,residual) >= 0
    partial = F(0)
    for j in range(6):
        previous = norm-partial
        partial += mass[j]*avg[j]**2
        assert norm-partial <= previous
        assert norm-partial >= dot(residual,residual)
    profile = [F(rng.randint(-9,9)) for _ in range(6)]
    assert dot(sigma,[profile[shell[i]] for i in range(size)]) == 0
# Critical scaling: 4*(L2 defect scaling exponent 1/2)-time exponent 2=0.
assert 4*F(1,2)-2 == 0
if args.integrated:
    main = (root/'main.tex').read_text()
    assert main.count('\\input{sections/speed_shell}') == 1
    assert 'Section~\\ref{ss:section}' in main
    assert 'sections/speed_shell.tex' in (root/'Makefile').read_text()
    all_labels = re.findall(r'\\label\{([^}]+)\}', main+'\n'+text)
    for label in labels:
        assert all_labels.count(label) == 1
print('PASS: frozen source, labels, exact flux/Young/clock constants, 400 weighted projection probes, scaling.')
print('Scope: finite algebra/source regression only; no independent mathematical audit or arbitrary-data temporal bound.')
