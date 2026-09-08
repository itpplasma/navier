#!/usr/bin/env python3
"""Finite exact algebra for the autonomous separated-pulse obstruction.

Not a PDE validator, source-paper audit, or numerical turnover certificate.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

import sympy as s


def main(output: Path | None = None) -> None:
    counts: Counter[str] = Counter()

    def check(condition: bool, group: str, label: str) -> None:
        if not condition:
            raise AssertionError(f"{group}: {label}")
        counts[group] += 1

    def eq(left: s.Expr, right: s.Expr, group: str, label: str) -> None:
        check(s.simplify(s.expand(left-right)) == 0, group, label)

    t = s.symbols("t", real=True)
    x = s.symbols("x0:3", real=True)
    B = s.Matrix([s.Function(f"B{i}")(t, *x) for i in range(3)])
    w = s.Matrix([s.Function(f"w{i}")(t, *x) for i in range(3)])
    r = s.Matrix([s.Function(f"r{i}")(t, *x) for i in range(3)])
    p = s.Function("p")(t, *x)
    div = lambda v: sum(s.diff(v[i], x[i]) for i in range(3))
    grad = lambda f: s.Matrix([s.diff(f, z) for z in x])
    lap = lambda f: sum(s.diff(f, z, 2) for z in x)
    adv = lambda a, b: s.Matrix([sum(a[j]*s.diff(b[i], x[j])
                                   for j in range(3)) for i in range(3)])
    energy = w.dot(w)
    eq(w.dot(w.diff(t)), s.diff(energy, t)/2, "energy", "time derivative")
    eq(-w.dot(w.applyfunc(lap)),
       sum(s.diff(w[i], x[j])**2 for i in range(3) for j in range(3))
       -div(sum((w[i]*grad(w[i]) for i in range(3)), s.zeros(3, 1))),
       "energy", "full Laplacian and boundary divergence")
    eq(w.dot(grad(p)), div(p*w)-p*div(w), "pressure", "actual pressure pairing")
    for name, a in (("background", B), ("self", w)):
        eq(w.dot(adv(a, w)), div(a*energy/2)-div(a)*energy/2,
           "transport", name)
    J = B.jacobian(x)
    eq(w.dot(adv(w, B)), (w.T*((J+J.T)/2)*w)[0],
       "energy", "only symmetric strain remains")
    full = adv(B+w+r, B+w+r)
    expansion = sum((adv(a, b) for a in (B, w, r) for b in (B, w, r)),
                    s.zeros(3, 1))
    for i in range(3):
        eq(full[i], expansion[i], "full_nonlinearity", f"all nine terms {i}")

    # Angular orthogonality is for CYLINDRICAL coefficients, with the frame
    # rotated too. These exact Fourier integrals do not prove support claims.
    theta = s.symbols("theta", real=True)
    er = s.Matrix([s.cos(theta), s.sin(theta), 0])
    et = s.Matrix([-s.sin(theta), s.cos(theta), 0])
    ez = s.Matrix([0, 0, 1])
    frame = (er, et, ez)
    for i in range(3):
        for j in range(3):
            eq(frame[i].dot(frame[j]), int(i == j), "angular", f"frame {i},{j}")
    for m in range(1, 9):
        eq(s.integrate(s.cos(m*theta), (theta, 0, 2*s.pi)), 0,
           "angular", f"cosine mean {m}")
        eq(s.integrate(s.sin(m*theta), (theta, 0, 2*s.pi)), 0,
           "angular", f"sine mean {m}")
        eq(s.integrate(s.cos(m*theta)**2, (theta, 0, 2*s.pi)), s.pi,
           "angular", f"real conjugate pair {m}")

    v, L, c = s.symbols("v L c", positive=True)
    psi = s.Function("psi")(v)
    h = s.Matrix([s.Function(f"h{i}")(v) for i in range(2)])
    A = s.Matrix(2, 2, lambda i,j: s.Function(f"a{i}{j}")(v))
    residual = (psi*h).diff(v)-A*(psi*h)
    expected = psi*(h.diff(v)-A*h)+s.diff(psi,v)*h
    for i in range(2):
        eq(residual[i], expected[i], "cutoff", f"matrix product rule {i}")
    envelope = s.exp(-c*(v-L/2)**2/L)
    growth = s.diff(s.log(envelope), v)
    eq(s.diff(envelope,v), growth*envelope, "envelope", "exact Gaussian solution")
    eq(envelope.subs(v,L/2), 1, "envelope", "midpoint")
    for offset in (F(1,5), F(1,4), F(1,3)):
        q = s.Rational(offset.numerator, offset.denominator)
        eq(s.log(envelope.subs(v,L/2+q*L)), -c*q*q*L,
           "envelope", f"cutoff exponent {offset}")
        check(offset*offset >= F(1,25), "envelope", "uniform tail exponent")

    # Exact sufficient thresholds for the asymptotic comparison:
    # -c ell^2 + (M+N) ell log(2) + b log(ell) <= -c ell^2/2.
    # Use log(2)<=1 and log(ell)<=ell for ell>=1, then test the algebra.
    for cc in (F(1,100), F(1,25), F(1,4), F(1)):
        for M, N, b in ((0,1,0), (2,3,4), (7,9,5), (10,20,15)):
            threshold = max(F(1), 2*F(M+N+b)/cc)
            ell = threshold+1
            check(-cc*ell*ell+F(M+N+b)*ell <= -cc*ell*ell/2,
                  "flatness", f"c={cc}, M,N,b={M,N,b}")

    # Finite-gauge direct-sum examples: exact nullspaces, no numeric rank test.
    for d in range(1, 7):
        C = s.Matrix(d, d+1, lambda i,j: s.Integer(j+1)**i)
        null = C.nullspace()
        check(bool(null), "gauges", f"nonzero nullspace for {d} constraints")
        z = null[0]
        check(C*z == s.zeros(d,1), "gauges", f"gauge cancellation {d}")
        check(any(a != 0 for a in z), "gauges", f"response not eliminated {d}")

    report = {"status": "PASS", "exact_assertions": sum(counts.values()),
              "groups": dict(sorted(counts.items())),
              "scope": "finite algebra only; no continuum PDE certification"}
    text = json.dumps(report, indent=2, sort_keys=True)
    print(text)
    if output is not None:
        output.write_text(text+"\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    main(parser.parse_args().json)
