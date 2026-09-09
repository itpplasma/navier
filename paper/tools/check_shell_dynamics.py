#!/usr/bin/env python3
"""Finite regression only; not an independent mathematical audit."""
from pathlib import Path
from fractions import Fraction as Q
import argparse
import hashlib
import math
import random

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--integrated', action='store_true')
args = p.parse_args()
root = Path(__file__).resolve().parents[1]
text = (root/'sections/shell_dynamics.tex').read_text()
assert hashlib.sha256(text.encode()).hexdigest() == '66f3ff185f220e8be874ea2090bc982abe42b4208ee093dc6799b5ee015e5677'
for label in ['st:stability', 'st:time', 'st:residual', 'st:evolution']:
    assert text.count('\\label{'+label+'}') == 1
assert Q(3,2)**2 / 2 == Q(9,8)
assert Q(9,8)*2 == Q(9,4)
# Exact diagonal PSD contraction, including a zero eigendirection.
for diagonal in [(0,1,2), (1,1,2), (0,0,0)]:
    for d in [(1,2,3), (-2,0,1)]:
        assert sum(Q(diagonal[i])*d[i]**2 for i in range(3)) >= 0
# Deterministic pointwise natural-distance probes, including zeros and opposites.
rng = random.Random(2026090615)
dot = lambda a,b: sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def natural(a): return [math.sqrt(norm(a))*x for x in a]
def flux(a): return [norm(a)*x for x in a]
pairs = [([0.,0.,0.],[0.,0.,0.]), ([1.,0.,0.],[-1.,0.,0.]), ([0.,0.,0.],[2.,3.,4.])]
pairs += [([rng.uniform(-3,3) for _ in range(3)], [rng.uniform(-3,3) for _ in range(3)]) for _ in range(2000)]
for a,b in pairs:
    lhs = sum((x-y)**2 for x,y in zip(natural(a),natural(b)))
    rhs = 9/8*dot([x-y for x,y in zip(flux(a),flux(b))], [x-y for x,y in zip(a,b)])
    assert lhs <= rhs + 1e-11*max(1,lhs,rhs)
# Exact one-feature ridge envelope and derivative at rational times.
for t in [Q(-1,3),Q(0),Q(2,5)]:
    chi = [1+t, 2-t, 3+2*t]
    dc = [Q(1),Q(-1),Q(2)]
    phi = [1+2*t, 1-t, Q(2)]
    dp = [Q(2),Q(-1),Q(0)]
    eta = Q(3,7)
    G, b = dot(phi,phi), dot(chi,phi)
    dG, db = 2*dot(phi,dp), dot(dc,phi)+dot(chi,dp)
    a = b/(G+eta)
    residual = [x-a*y for x,y in zip(chi,phi)]
    R = dot(chi,chi)-b*a
    assert R == dot(residual,residual)+eta*a*a >= 0
    derivative = 2*dot(chi,dc)-2*a*db+a*a*dG
    assert derivative == 2*dot(residual,[x-a*y for x,y in zip(dc,dp)])
    assert dot(chi,chi)-b*b/(G+eta/2) <= R
if args.integrated:
    assert (root/'main.tex').read_text().count('\\input{sections/shell_dynamics}') == 1
    assert 'sections/shell_dynamics.tex' in (root/'Makefile').read_text()
print('PASS: frozen source, labels, exact constants and ridge identities, 2003 natural-distance probes.')
print('Scope: finite algebra/source regression only; no endpoint estimate, Lean proof or independent audit.')
