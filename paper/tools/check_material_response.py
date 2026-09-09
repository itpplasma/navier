#!/usr/bin/env python3
"""Finite algebra/numerical regressions and source integrity, not a proof audit."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import math

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--integrated', action='store_true')
args = parser.parse_args()
source = root/'sections/material_response.tex'
text = source.read_text()
assert hashlib.sha256(source.read_bytes()).hexdigest() == '54eb89147a08ee4403d8278fbe844bf396fb2978962cf156a6c5e547f4b90034'
labels = ['mr:response', 'mr:hadamard', 'mr:material', 'mr:residual', 'mr:balance', 'mr:rigid']
for label in labels:
    assert text.count('\\label{'+label+'}') == 1, label
if args.integrated:
    main = (root/'main.tex').read_text()
    assert main.count('\\input{sections/material_response}') == 1
    assert 'ConstantinIyer2008' in (root/'references.bib').read_text()
    assert 'sections/material_response.tex' in (root/'Makefile').read_text()

# Exact radial/transverse ratios and the displayed upper-bound constants.
assert F(3, 2)**2/F(2) == F(9, 8)
assert F(1) - F(1, 9) == F(8, 9)
assert F(9, 8)*4 == F(9, 2)
assert F(9, 8)*F(9, 2) == F(81, 16)
assert 2*F(2) + F(1, 2) == F(9, 2)
assert 2*F(1) + F(1) == 3

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def add(a, b):
    return [x+y for x, y in zip(a, b)]

def scale(s, a):
    return [s*x for x in a]

def sub(a, b):
    return add(a, scale(-1, b))

def norm(a):
    return math.sqrt(dot(a, a))

def transpose(a):
    return [list(col) for col in zip(*a)]

def mv(a, b):
    return [dot(row, b) for row in a]

def solve(a, b):
    n = len(b)
    m = [list(row)+[rhs] for row, rhs in zip(a, b)]
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(m[i][j]))
        assert abs(m[k][j]) > 1e-14, 'singular regression matrix'
        m[j], m[k] = m[k], m[j]
        pivot = m[j][j]
        m[j] = [x/pivot for x in m[j]]
        for i in range(n):
            if i != j:
                s = m[i][j]
                m[i] = [x-s*y for x, y in zip(m[i], m[j])]
    return [row[-1] for row in m]

def inverse(a):
    return transpose([solve(a, [float(i == j) for i in range(len(a))])
                      for j in range(len(a))])

def outer(a, b):
    return [[x*y for y in b] for x in a]

def identity():
    return [[float(i == j) for j in range(3)] for i in range(3)]

def matrix_add(a, b):
    return [add(x, y) for x, y in zip(a, b)]

def matrix_scale(s, a):
    return [scale(s, row) for row in a]

def dual(a):
    return scale(norm(a), a)

def natural(a):
    return scale(math.sqrt(norm(a)), a)

def derivative(a, natural_variable=False):
    r = norm(a)
    if not r:
        return [[0.0]*3 for _ in range(3)]
    n = scale(1/r, a)
    if natural_variable:
        return matrix_scale(math.sqrt(r), matrix_add(identity(), matrix_scale(0.5, outer(n, n))))
    return matrix_scale(r, matrix_add(identity(), outer(n, n)))

# Three atoms, one with w=0; a two-dimensional closed subspace annihilated
# by A(w). This tests the abstract response, not a PDE trajectory.
w = [[1., 0., 0.], [0., 2., 0.], [0., 0., 0.]]
h = [[0.2, -0.5, 0.3], [0.7, 0.2, -0.2], [0.8, -0.4, 0.9]]
basis = [
    [[0., 1., 0.], [0., 0., 1.], [1., 0., 0.]],
    [[4., 0., 1.], [0., -1., 0.], [0., 1., 1.]],
]
G = [
    [[0.3, -0.8, 0.1], [0.4, -0.2, 0.5], [-0.3, 0.2, 0.1]],
    [[-0.4, 0.7, -0.2], [0.1, 0.3, 0.6], [0.2, -0.1, 0.1]],
    [[0.2, 0.5, -0.3], [-0.5, -0.1, 0.4], [0.3, -0.4, -0.1]],
]
M = [derivative(v) for v in w]
N = [derivative(v, True) for v in w]

def fdot(a, b):
    return sum(dot(x, y) for x, y in zip(a, b))

def fadd(a, b):
    return [add(x, y) for x, y in zip(a, b)]

def fsub(a, b):
    return [sub(x, y) for x, y in zip(a, b)]

def fscale(s, a):
    return [scale(s, x) for x in a]

def apply(matrices, a):
    return [mv(m, x) for m, x in zip(matrices, a)]

def wdot(a, b):
    return fdot(a, apply(M, b))

gram = [[wdot(a, b) for b in basis] for a in basis]
for g in basis:
    assert abs(fdot([dual(x) for x in w], g)) < 1e-14

def project(a):
    coeff = solve(gram, [wdot(g, a) for g in basis])
    answer = [[0.0]*3 for _ in w]
    for s, g in zip(coeff, basis):
        answer = fadd(answer, fscale(s, g))
    return answer

def project_complement(a):
    return fsub(a, project(a))

def c_field(matrices):
    answer = []
    for g, v in zip(matrices, w):
        r = norm(v)
        n = scale(1/r, v) if r else [0.0]*3
        gv = mv(g, v)
        answer.append(sub(gv, scale(0.5*dot(n, gv), n)))
    return answer

Gtw = apply([transpose(g) for g in G], w)
b = fadd(Gtw, c_field(G))
z = fadd(project_complement(h), project(b))
physical_target = apply(N, fsub(z, Gtw))

# Verify the strain/skew decomposition and orthogonal action on this space.
S = [matrix_scale(0.5, matrix_add(g, transpose(g))) for g in G]
Omega = [matrix_scale(0.5, matrix_add(g, matrix_scale(-1, transpose(g)))) for g in G]
left = project_complement(fsub(h, apply(S, w)))
right = project(c_field(S))
U = apply(N, fadd(left, right))
U_from_full = fsub(physical_target, apply(Omega, [natural(x) for x in w]))
assert math.sqrt(fdot(fsub(U, U_from_full), fsub(U, U_from_full))) < 1e-12
assert abs(wdot(left, right)) < 1e-12
act = wdot(left, left)+wdot(right, right)
u2 = fdot(U, U)
radial = sum(dot(scale(1/norm(v), v), x)**2 for v, x in zip(w, U) if norm(v))
assert abs(act-(u2-radial/9)) < 1e-12
assert act <= u2+1e-12 <= 9*act/8+1e-12

# Nonlinear minimization for both signs, retaining the zero atom. Newton
# solves only a finite-dimensional convex surrogate; it is not a proof.
def minimizer(eps):
    B = [matrix_add(identity(), matrix_scale(eps, g)) for g in G]
    Binv = [inverse(b) for b in B]
    Binvt = [transpose(b) for b in Binv]
    transformed_basis = [apply(Binvt, g) for g in basis]
    base = fadd(w, fscale(eps, h))
    coeff = [0.0, 0.0]
    def evaluate(c):
        a = base
        for s, g in zip(c, basis):
            a = fadd(a, fscale(s, g))
        v = apply(Binvt, a)
        return a, v, sum(norm(x)**3 for x in v)/3
    for _ in range(80):
        a, v, value = evaluate(coeff)
        av = [dual(x) for x in v]
        gradient = [fdot(g, av) for g in transformed_basis]
        if norm(gradient) < 2e-13:
            return a, v
        metrics = [derivative(x) for x in v]
        hessian = [[fdot(g, apply(metrics, k)) for k in transformed_basis]
                   for g in transformed_basis]
        direction = solve(hessian, gradient)
        step = 1.0
        for _ in range(50):
            trial = sub(coeff, scale(step, direction))
            _, _, trial_value = evaluate(trial)
            if trial_value <= value-1e-4*step*dot(gradient, direction)+1e-15:
                coeff = trial
                break
            step *= 0.5
        else:
            raise AssertionError('line search did not converge')
    raise AssertionError('Newton regression did not converge')

errors = []
for sign in (-1, 1):
    rows = []
    for magnitude in (1e-2, 1e-3, 1e-4):
        eps = sign*magnitude
        a, v = minimizer(eps)
        d = fsub(a, w)
        physical_difference = fscale(1/eps, fsub([natural(x) for x in v], [natural(x) for x in w]))
        error = fsub(physical_difference, physical_target)
        weighted_error = fsub(fscale(1/eps, d), z)
        row = (math.sqrt(fdot(error, error)),
               math.sqrt(wdot(weighted_error, weighted_error)),
               sum(norm(x)**3 for x in d)/(eps*eps))
        rows.append(row)
    assert all(rows[-1][j] < 0.2*rows[0][j] for j in range(3)), rows
    assert rows[-1][0] < 0.1
    errors.append((sign, rows))

# A rational rigid-rotation check of the double-Riesz contraction symbol.
rot = [[F(0), F(-1), F(0)], [F(1), F(0), F(0)], [F(0), F(0), F(1)]]
xi = [F(1), F(2), F(-3)]
tensor = [[F(2), F(1), F(3)], [F(1), F(-1), F(2)], [F(3), F(2), F(-1)]]
def mm(a, b):
    return [[dot(row, col) for col in transpose(b)] for row in a]
rotated_tensor = mm(mm(rot, tensor), transpose(rot))
rotated_xi = mv(rot, xi)
assert -dot(xi, mv(tensor, xi))/dot(xi, xi) == -dot(rotated_xi, mv(rotated_tensor, rotated_xi))/dot(rotated_xi, rotated_xi)
print('PASS: frozen source, labels, exact constants, weighted projection/action, rigid symbol, six nonlinear moving-metric probes including a zero atom.')
for sign, rows in errors:
    print('epsilon sign', sign, 'errors (natural L2, weighted, cubic/epsilon^2):', rows)
print('Scope: finite regressions and document integrity only; not an analytic proof, independent audit, endpoint estimate, or Lean check.')
