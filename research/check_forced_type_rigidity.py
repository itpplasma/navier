#!/usr/bin/env python3
"""Finite exact algebra for the forced-type rigidity note.

Companion to `research/evidence/2026-09-08-forced-type-rigidity.md`.

Checks ONLY exact symbolic and rational identities that the note's new
component (Lemma B, Theorem C, Corollaries C1/C2) actually uses. It is not a
PDE validator, not an audit of the external source manuscript, not a
numerical Navier-Stokes orbit, and not independent review.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

import sympy as s


def main(output: Path | None = None) -> int:
    passed: Counter[str] = Counter()
    failures: list[str] = []

    def check(condition: bool, group: str, label: str) -> None:
        if condition:
            passed[group] += 1
        else:
            failures.append(f"{group}: {label}")

    def eq(left, right, group: str, label: str) -> None:
        check(s.simplify(s.expand(left - right)) == 0, group, label)

    # ---------------------------------------------------------------- setup
    t = s.symbols("t", real=True)
    x = s.symbols("x0:3", real=True)
    nu = s.symbols("nu", positive=True)

    def field(name):
        return s.Matrix([s.Function(f"{name}{i}")(t, *x) for i in range(3)])

    B = field("B")          # axisymmetric mean, (1.1)
    W = field("W")          # the label W_gamma
    V = field("V")          # all other labels
    f = field("f")          # force
    p = s.Function("p")(t, *x)
    U = B + W + V

    div = lambda v: sum(s.diff(v[i], x[i]) for i in range(3))
    grad = lambda a: s.Matrix([s.diff(a, z) for z in x])
    lap = lambda a: sum(s.diff(a, z, 2) for z in x)
    vlap = lambda v: v.applyfunc(lap)
    adv = lambda a, b: s.Matrix([sum(a[j] * s.diff(b[i], x[j])
                                     for j in range(3)) for i in range(3)])

    def sym_strain(v):
        J = v.jacobian(x)
        return (J + J.T) / 2

    # -------------------------------------------- Lemma B: exact identity
    # Every term of the note's (2.2) carries V or a derivative of V.
    g = (V.diff(t) - nu * vlap(V) + adv(B, V) + adv(V, B) + adv(V, V))
    k_B = (B.diff(t) - nu * vlap(B) + adv(B, B))

    for i in range(3):
        eq(g[i].subs({V[j]: 0 for j in range(3)}), 0,
           "degeneration", f"g vanishes when V=0, component {i}")

    residual = U.diff(t) - nu * vlap(U) + adv(U, U) + grad(p) - f
    energy = W.dot(W)

    Psi = (-nu * sum((W[i] * grad(W[i]) for i in range(3)), s.zeros(3, 1))
           + (B + W + V) * energy / 2
           + p * W)

    rhs = (s.diff(energy, t) / 2
           + nu * sum(s.diff(W[i], x[j])**2 for i in range(3) for j in range(3))
           + (W.T * sym_strain(B) * W)[0]
           + (W.T * sym_strain(V) * W)[0]
           + W.dot(g)
           + W.dot(k_B)
           - W.dot(f)
           + div(Psi)
           - energy / 2 * (div(B) + div(W) + div(V))
           - p * div(W))

    eq(W.dot(residual), rhs, "lemma_B", "exact divergence-form pairing")

    # The three structural cancellations quoted inside the proof.
    eq(W.dot(adv(W, B)), (W.T * sym_strain(B) * W)[0],
       "lemma_B", "background strain: only symmetric part survives")
    eq(W.dot(adv(W, V)), (W.T * sym_strain(V) * W)[0],
       "lemma_B", "overlap strain: only symmetric part survives")
    for name, a in (("background", B), ("other_labels", V), ("self", W)):
        eq(W.dot(adv(a, W)), div(a * energy / 2) - div(a) * energy / 2,
           "lemma_B", f"transport cancellation, {name}")
    eq(W.dot(grad(p)), div(p * W) - p * div(W),
       "lemma_B", "canonical pressure pairing")
    eq(-W.dot(vlap(W)),
       sum(s.diff(W[i], x[j])**2 for i in range(3) for j in range(3))
       - div(sum((W[i] * grad(W[i]) for i in range(3)), s.zeros(3, 1))),
       "lemma_B", "full gradient norm plus boundary divergence")

    # The nine convection terms are exhausted (no term silently dropped).
    full = adv(U, U)
    parts = sum((adv(a, b) for a in (B, W, V) for b in (B, W, V)),
                s.zeros(3, 1))
    for i in range(3):
        eq(full[i], parts[i], "lemma_B", f"nine-term expansion, component {i}")

    # ------------------------------- (L2) angular constant: exact algebra
    # Vector rotation modes, NOT fixed Cartesian component projections.
    th, n = s.symbols("theta n", real=True)
    vr, vt, vz = s.symbols("v_r v_theta v_z")
    e_r = s.Matrix([s.cos(th), s.sin(th), 0])
    e_t = s.Matrix([-s.sin(th), s.cos(th), 0])
    e_z = s.Matrix([0, 0, 1])
    v = s.exp(s.I * n * th) * (vr * e_r + vt * e_t + vz * e_z)
    claimed = s.exp(s.I * n * th) * ((s.I * n * vr - vt) * e_r
                                     + (s.I * n * vt + vr) * e_t
                                     + s.I * n * vz * e_z)
    for i in range(3):
        eq(s.diff(v[i], th), claimed[i], "angular",
           f"angular derivative formula (1.2), component {i}")

    M = s.Matrix([[n**2 + 1, 2 * s.I * n, 0],
                  [-2 * s.I * n, n**2 + 1, 0],
                  [0, 0, n**2]])
    check(M.H == M, "angular", "quadratic form matrix is Hermitian")
    vec = s.Matrix([vr, vt, vz])
    form = s.expand(s.simplify((vec.H * M * vec)[0]))
    direct = s.expand(s.simplify(sum(s.diff(v[i], th) * s.conjugate(s.diff(v[i], th))
                                     for i in range(3))))
    eq(s.simplify(form - direct), 0, "angular",
       "|d_theta v|^2 equals the stated Hermitian form")
    eigs = set(s.simplify(e) for e in M.eigenvals())
    for want in ((n - 1)**2, (n + 1)**2, n**2):
        check(any(s.simplify(e - s.expand(want)) == 0 for e in eigs),
              "angular", f"eigenvalue {want}")
    # min over |n| >= N >= 2 of the three eigenvalues is (N-1)^2.
    for N in range(2, 9):
        vals = [(abs(k) - 1)**2 for k in range(N, N + 5)]
        vals += [(abs(k) + 1)**2 for k in range(N, N + 5)]
        vals += [k**2 for k in range(N, N + 5)]
        check(min(vals) == (N - 1)**2, "angular", f"gap (N-1)^2 at N={N}")

    # ------------------------------------ (L1) Faber-Krahn constant, exact
    Vol = s.symbols("Vol", positive=True)
    rho = (3 * Vol / (4 * s.pi))**s.Rational(1, 3)
    eq(s.pi**2 / rho**2,
       s.pi**2 * (4 * s.pi / 3)**s.Rational(2, 3) * Vol**s.Rational(-2, 3),
       "faber_krahn", "ball ground state rewritten in |Omega|^{-2/3}")

    # ------------------------------- Theorem C: regularization and Gronwall
    A, eps = s.symbols("A epsilon", positive=True)
    Aeps = s.sqrt(A**2 + eps**2)
    eq(A**2 / Aeps, Aeps - eps**2 / Aeps, "gronwall",
       "A^2/A_eps = A_eps - eps^2/A_eps")
    check(s.simplify(Aeps**2 - A**2 - eps**2) == 0, "gronwall",
          "A_eps^2 = A^2 + eps^2 (so A <= A_eps and A_eps >= eps)")

    # ---------------------- Corollary C2: weight comparison and exact integral
    h, C_B, beta, q, tau = s.symbols("h C_B beta q tau", positive=True)
    mu = (beta - C_B) * q**(-h)
    m_upper = tau**(-1) * (C_B * tau**(-h) - beta * q**(-h))
    eq(s.simplify(m_upper + mu / tau - C_B * (tau**(-1 - h) - q**(-h) / tau)),
       0, "weights", "m bound reduces to C_B(tau^{-h}-q^{-h})/tau")
    # tau^{-h} <= q^{-h} for tau >= q > 0, h > 0: exact rational instances.
    for hh in (s.Rational(1, 2), s.Rational(1, 4), s.Rational(1, 100)):
        for qq, tt in ((1, 1), (1, 4), (1, 100), (4, 9), (9, 16)):
            check(s.Rational(tt)**(-hh) <= s.Rational(qq)**(-hh),
                  "weights", f"tau^-h<=q^-h at h={hh}, q={qq}, tau={tt}")
    mu_s = s.symbols("mu", positive=True)
    integral = s.integrate((q / tau)**mu_s, (tau, q, s.oo),
                           conds="separate")[0]
    eq(s.simplify(integral - q / (mu_s - 1)), 0, "weights",
       "int_q^inf (q/tau)^mu dtau = q/(mu-1)")
    eq(q**mu_s * q**(1 - mu_s) / (mu_s - 1), q / (mu_s - 1), "weights",
       "Corollary C2 bookkeeping q^mu * q^{1-mu}/(mu-1)")
    # (2.15) is a rearrangement of a_1 <= sup_kappa * q/(mu-1).
    a1, sup_k = s.symbols("a_1 sup_kappa", positive=True)
    eq(s.solve(s.Eq(a1, sup_k * q / (mu_s - 1)), sup_k)[0],
       a1 * (mu_s - 1) / q, "weights", "(2.15) rearrangement")

    # ------- Section 2.4: exp(-c ell^2/4) beats every fixed power of Q=2^-ell
    # Use log 2 <= 1, so Q^{-N} = 2^{N ell} <= exp(N ell).
    for c in (s.Rational(1, 100), s.Rational(1, 8), s.Rational(1), s.Rational(4)):
        for N in (1, 3, 10, 50):
            ell = max(s.Rational(1), 8 * s.Rational(N) / c) + 1
            check(-c * ell**2 / 4 + N * ell <= -c * ell**2 / 8,
                  "flatness", f"superalgebraic flatness c={c}, N={N}")

    # -------------------- Corollary C1: weights <= 1 give the integrated cost
    # Exact finite surrogate: with 0 <= w_i <= 1, sum w_i kappa_i dt <= sum
    # kappa_i dt, so a_1 <= weighted sum forces a_1 <= unweighted sum (2.12).
    for kap in ([s.Rational(1, 3)] * 6, [s.Rational(k, 7) for k in range(1, 7)]):
        dt = s.Rational(1, len(kap))
        for w in (s.Rational(0), s.Rational(1, 2), s.Rational(1)):
            weighted = sum(k * dt * w for k in kap)
            unweighted = sum(k * dt for k in kap)
            check(weighted <= unweighted, "corollary_C1",
                  f"weight {w} <= 1 keeps the integrated cost")
            # contrapositive arithmetic of (2.12): a_1 = weighted => a_1 <= int
            check(weighted <= unweighted and weighted >= 0, "corollary_C1",
                  f"a_1 <= int kappa at weight {w}")

    report = {
        "status": "PASS" if not failures else "FAIL",
        "pass_count": sum(passed.values()),
        "fail_count": len(failures),
        "groups": dict(sorted(passed.items())),
        "failures": failures,
        "scope": ("finite exact algebra only; no continuum PDE certification, "
                  "no source-manuscript audit, no independent review"),
    }
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    print(f"PASS: {report['pass_count']}  FAIL: {report['fail_count']}")
    if output is not None:
        output.write_text(text + "\n", encoding="utf-8")
    return 0 if not failures else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    raise SystemExit(main(parser.parse_args().json))
