#!/usr/bin/env python3
"""Finite algebra/source regressions. Not an independent mathematical audit."""
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
rng = random.Random(2026090617)

def norm(v):
    return math.sqrt(sum(z*z for z in v))

def transform(x, field):
    r = norm(x)
    n = [z/r for z in x]
    f = field([z/r**2 for z in x])
    a = sum(n[i]*f[i] for i in range(3))
    return [(f[i]-2*n[i]*a)/r**2 for i in range(3)]

# A smooth field with a known derivative: f(y) = A y + b.
for trial in range(300):
    x = [rng.uniform(-2, 2) for _ in range(3)]
    if norm(x) < .5:
        x[0] += 1
    r = norm(x)
    n = [z/r for z in x]
    matrix = [[rng.uniform(-1, 1) for j in range(3)] for i in range(3)]
    b = [rng.uniform(-1, 1) for _ in range(3)]
    def field(y):
        return [sum(matrix[i][j]*y[j] for j in range(3))+b[i] for i in range(3)]
    v = field([z/r**2 for z in x])
    a = sum(n[i]*v[i] for i in range(3))
    R = [[(1 if i == j else 0)-2*n[i]*n[j] for j in range(3)] for i in range(3)]
    B = [[-2*v[i]*n[j]-2*a*(i == j)-2*n[i]*v[j]+8*a*n[i]*n[j]
          for j in range(3)] for i in range(3)]
    assert math.isclose(sum(z*z for row in B for z in row),
                        8*norm(v)**2+4*a*a, rel_tol=2e-14, abs_tol=2e-14)
    twice = transform(x, lambda y: transform(y, field))
    assert max(abs(twice[i]-field(x)[i]) for i in range(3)) < 1e-12
    expected = [[sum(R[i][k]*matrix[k][l]*R[l][j] for k in range(3) for l in range(3))/r**4
                 + B[i][j]/r**3 for j in range(3)] for i in range(3)]
    eps = 1e-5
    for j in range(3):
        xp, xm = x[:], x[:]
        xp[j] += eps
        xm[j] -= eps
        fp, fm = transform(xp, field), transform(xm, field)
        for i in range(3):
            fd = (fp[i]-fm[i])/(2*eps)
            assert abs(fd-expected[i][j]) < 2e-6*(1+abs(expected[i][j]))

# Exact exponents and constants, rather than numerical time evolution.
assert F(3,4)+F(1,4) == 1
assert 4*F(5,4)*2 == 10
assert F(5,4)*F(1,3)*2 == F(5,6)
assert F(2,2)+F(3,1)/F(3,2) == 3  # supercritical, not the critical value 2
assert F(2,4)+F(3,2) == 2
for z in [0, .01, .1, 1, 3, 10, 1e6]:
    assert (6-2*z)/(1+z)**3 <= 6
    assert 1/(1+z)**2 <= 1/math.sqrt(1+z)
for _ in range(1000):
    K, I = 10**rng.uniform(-5, 5), 10**rng.uniform(-5, 5)
    L = .5*(I+math.sqrt(I*I+4*K))
    assert math.isclose(L*L, K+I*L, rel_tol=3e-15)

# Exact expression for div(|U|U) at (1,1,0), without a PDE simulation.
x, y, z = 1., 1., 0.
g = math.exp(-x*x-2*y*y-z*z)
speed = math.sqrt(16*y*y+4*x*x)*g
u = [4*y*g, -2*x*g, 0]
grad_speed = [speed*(4*x/(16*y*y+4*x*x)-2*x),
              speed*(16*y/(16*y*y+4*x*x)-4*y), -2*z*speed]
assert math.isclose(sum(u[i]*grad_speed[i] for i in range(3)),
                    -8*math.exp(-6)/math.sqrt(5), rel_tol=1e-14)
# E=E_U/lambda, Y=Y_U*lambda, lambda'=2 nu Y_U/E_U lambda^3.
for lam in (.1, 1., 10.):
    nu0, EU, YU = .3, 2., 7.
    derivative = 2*nu0*YU/EU*lam**3
    assert abs(-EU*derivative/lam**2+2*nu0*YU*lam) < 1e-12

source = (root/'sections/conformal_moment.tex').read_text()
labels = re.findall(r'\\label\{([^}]+)\}', source)
assert len(labels) == len(set(labels))
assert {'cm:covariance','cm:inverted-h1','cm:snapshot','cm:moment','cm:spacetime','cm:scaling-test'} <= set(labels)
assert 'audit pending' in source and 'remains unproved' in source
assert 'need not be solenoidal' in source
assert 'not a Navier--Stokes' in source
assert 'supercritical' in source
if args.integrated:
    main = (root/'main.tex').read_text()
    assert main.count(r'\input{sections/conformal_moment}') == 1
    assert 'No arbitrary-data critical bound is proved here.' in main
    assert 'asserted anywhere: what is proved' not in main
    assert 'No decay of $u(t)$ beyond membership in every' not in main
    assert 'LiimatainenSalo2014' in (root/'references.bib').read_text()
    alltex = main + '\n' + '\n'.join(p.read_text() for p in (root/'sections').glob('*.tex'))
    for label in labels:
        assert alltex.count('\\label{'+label+'}') == 1, label
    for ref in re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', source):
        assert '\\label{'+ref+'}' in alltex, ref
print('PASS: 300 conformal matrix/involution/derivative probes, 1000 barrier identities, exact exponents and source guards.')
print('Finite regression only; no independent mathematical audit, PDE simulation, or Lean proof.')
