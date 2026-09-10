#!/usr/bin/env python3
"""Exact algebraic checks for the adjoint de-forcing research note.

Requires Python 3.10+ and SymPy. These checks are finite-dimensional
calibrations, not a PDE simulation, a Lean proof, or an independent audit.
Run: python3 check_adjoint_deforcing.py
"""
from __future__ import annotations

import random
import sympy as sp

COUNT = 0


def check(condition: bool, name: str) -> None:
    global COUNT
    if not bool(condition):
        raise AssertionError(name)
    COUNT += 1


def sqnorm(v: sp.Matrix) -> sp.Expr:
    return (v.T * v)[0]


def selector(S: sp.Matrix, b: sp.Matrix, lam: sp.Rational) -> tuple[sp.Matrix, sp.Matrix]:
    if lam < 0 or S.rows != b.rows or b.cols != 1:
        raise ValueError("Require lambda >= 0 and compatible real dimensions")
    eta = -(sp.eye(S.rows) + lam * S * S.T).inv() * b
    return lam * S.T * eta, eta


def check_selectors() -> None:
    rng = random.Random(20260910)
    for case in range(24):
        m, n = 1 + case % 4, 1 + (case // 4) % 4
        S = sp.Matrix(m, n, lambda _i, _j: rng.randrange(-3, 4))
        D = sp.Matrix(m, n, lambda _i, _j: sp.Rational(rng.randrange(-2, 3), 7))
        b = sp.Matrix([rng.randrange(-4, 5) for _ in range(m)])
        db = sp.Matrix([sp.Rational(rng.randrange(-2, 3), 5) for _ in range(m)])
        for lam in map(sp.Rational, [0, sp.Rational(1, 4), 1, 4, 9]):
            a, eta = selector(S, b, lam)
            prefix = f"case={case}, lambda={lam}: "
            check(eta + S*a + b == sp.zeros(m, 1), prefix + "mixed compatibility")
            check(a == lam*S.T*eta, prefix + "adjoint initialization")
            check((sp.eye(n)+lam*S.T*S)*a == -lam*S.T*b,
                  prefix + "normal equation")
            check(sqnorm(eta) <= sqnorm(b), prefix + "displacement contraction")
            check(sqnorm(a) <= lam*sqnorm(b)/4, prefix + "sharp control bound")
            check(sqnorm(a)+lam*sqnorm(S*a+b) <= lam*sqnorm(b),
                  prefix + "least-squares comparison with zero")
            changed_b, _ = selector(S, b+db, lam)
            check(sqnorm(changed_b-a) <= lam*sqnorm(db)/4,
                  prefix + "data Lipschitz estimate")
            changed_S, _ = selector(S+D, b, lam)
            # Frobenius norm bounds the operator norm, making this exact test
            # rational. The theorem uses the sharper operator norm.
            check(sqnorm(changed_S-a) <= lam**2*sum(x*x for x in D)*sqnorm(b),
                  prefix + "operator Lipschitz estimate")
    H, A = -sp.eye(2), sp.eye(2)
    check((sp.eye(2)+H*A).det() == 0, "old feedback can resonate in a matrix calibration")
    check((sp.eye(2)+H*A*H.T).det() == 4, "new feedback removes that algebraic resonance")


def check_resolvent_identity() -> None:
    for S in [sp.Matrix([[1, 2], [-3, 0]]), sp.Matrix([[1, 2, -1]])]:
        n, m = S.cols, S.rows
        D = sp.zeros(n+m)
        D[:n, n:] = S.T
        D[n:, :n] = S
        for rho in [sp.Rational(1, 2), sp.Rational(1), sp.Rational(3)]:
            lam = rho**2
            exact = lam*D*(sp.eye(n+m)+lam*D**2).inv()
            resolvents = ((D-sp.I/rho*sp.eye(n+m)).inv()
                           +(D+sp.I/rho*sp.eye(n+m)).inv())/2
            check((exact-resolvents).applyfunc(sp.simplify) == sp.zeros(n+m),
                  "self-adjoint block resolvent identity")
            check(exact[:n, n:] == lam*S.T*(sp.eye(m)+lam*S*S.T).inv(),
                  "selector is an off-diagonal resolvent block")


def check_one_trace() -> None:
    dim = 12
    previous = sp.zeros(dim, 1)
    for N in range(1, dim+1):
        M = sp.zeros(N, dim)
        for j in range(N):
            M[j, j] = sp.Rational(1, 2**(j+1))
        d = sp.Matrix([M[j, j] for j in range(N)])
        a = M.T*(M*M.T).inv()*d
        check(M*a == d, "finite prefix exactly solvable")
        check(sqnorm(a) == N, "finite prefix cost diverges")
        check(sqnorm(a-previous) == sqnorm(a)-sqnorm(previous),
              "nested minimum-norm Pythagorean identity")
        previous = a
    for j in range(2, 7):
        s, d = sp.Rational(1, 2**(j**3)), sp.Rational(1, 2**(j**2))
        exact_control = -d/s
        regularized, eta = selector(sp.Matrix([[s]]), sp.Matrix([d]), sp.Rational(1))
        check(abs(exact_control) == 2**(j**3-j**2), "flat source can have huge exact seed cost")
        check(abs(regularized[0]) <= d/2, "regularized seed stays small")
        check(abs(s*regularized[0]+d) > d/2,
              "small regularized seed fails half-relative endpoint cancellation")
        q = 1/s
        check(abs(d*q) == abs(exact_control)*abs(s*q), "sharp adjoint lower bound")


def check_adjoint_signs() -> None:
    t = sp.symbols("t", real=True)
    A = sp.Matrix([[0, 1], [0, 0]])
    w = sp.Matrix([t+1, t*t+2])
    Q = sp.Matrix([w[0]*w[1], -w[0]**2])
    check(sp.expand((w.T*Q)[0]) == 0, "quadratic ODE calibration has energy cancellation")
    F = -(w.diff(t)+A*w+Q)
    for T in [sp.Rational(1, 2), sp.Rational(1), sp.Rational(2)]:
        for q in [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([2, -3])]:
            z = (sp.eye(2)+(t-T)*A.T)*q
            check(-z.diff(t)+A.T*z == sp.zeros(2, 1), "full adjoint sign")
            left = sp.integrate((F.T*z)[0], (t, 0, T))
            right = ((w.subs(t, 0).T*z.subs(t, 0))[0]
                     -(w.subs(t, T).T*q)[0]
                     -sp.integrate((Q.T*z)[0], (t, 0, T)))
            check(sp.simplify(left-right) == 0, "nonlinear integrated adjoint identity")


def main() -> None:
    check_selectors()
    check_resolvent_identity()
    check_one_trace()
    check_adjoint_signs()
    print(f"PASS: {COUNT} exact assertions.")
    print("Scope: rational matrix identities, prefix-cost examples, and an ODE sign calibration.")
    print("NOT CHECKED: full PDE estimates, source-specific propagators, nonlinear exactification,")
    print("one Schwartz trace for the OpenAI construction, or an unforced singular solution.")


if __name__ == "__main__":
    main()
