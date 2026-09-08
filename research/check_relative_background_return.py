#!/usr/bin/env python3
"""Finite exact identities for full-state returns over an evolved NS background.

No PDE validation, event certification, or independent mathematical audit.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

import sympy as s


def main(output: Path | None = None) -> None:
    counts: Counter[str] = Counter()

    def require(condition: bool, group: str, label: str) -> None:
        if not condition:
            raise AssertionError(f"{group}: {label}")
        counts[group] += 1

    def equal(left: s.Expr, right: s.Expr, group: str, label: str) -> None:
        require(s.expand(left-right) == 0, group, label)

    x = s.symbols("x0:3", real=True)
    t, mu = s.symbols("t mu", real=True)
    B = s.Matrix([s.Function(f"B{i}")(t, *x) for i in range(3)])
    R = s.Matrix([s.Function(f"R{i}")(t, *x) for i in range(3)])
    U = B+R
    q = s.Function("q")(t, *x)
    lap = lambda f: sum(s.diff(f, y, 2) for y in x)
    div = lambda v: sum(s.diff(v[i], x[i]) for i in range(3))
    adv = lambda v, w: s.Matrix([sum(v[j]*s.diff(w[i], x[j])
                                    for j in range(3)) for i in range(3)])
    gradq = s.Matrix([s.diff(q,y) for y in x])
    diff = U.diff(t)-mu*U.applyfunc(lap)+adv(U,U) \
           -(B.diff(t)-mu*B.applyfunc(lap)+adv(B,B))+gradq
    eq = R.diff(t)-mu*R.applyfunc(lap)+adv(U,R)+adv(R,B)+gradq
    for i in range(3):
        equal(diff[i], eq[i], "difference", f"full component {i}")

    # Identity before imposing div R=0: the extra term is explicit.
    cross_div = sum(s.diff(B[i]*R[j]+R[i]*B[j], x[i], x[j])
                    for i in range(3) for j in range(3))
    equal(cross_div, 2*div(adv(R,B))+2*div(B*div(R)),
          "pressure", "complete double divergence with constraint term")
    c = s.Matrix(s.symbols("c0:3"))
    const_cross = sum(s.diff(c[i]*R[j]+R[i]*c[j], x[i], x[j])
                      for i in range(3) for j in range(3))
    equal(const_cross, 2*sum(c[i]*s.diff(div(R),x[i]) for i in range(3)),
          "pressure", "constant drift vanishes for solenoidal R")

    E = R.dot(R)
    flux = E*(B+R)+2*q*R
    lhs = s.diff(E,t)+div(flux)-mu*lap(E) \
          +2*mu*sum(s.diff(R[i],y)**2 for i in range(3) for y in x) \
          +2*R.dot(adv(R,B))
    equal(lhs, 2*R.dot(eq)+E*div(U)+2*q*div(R),
          "relative_energy", "all local terms and divergence constraints")
    for i in range(3):
        equal(adv(B-c+R,R)[i]+adv(c,R)[i], adv(B+R,R)[i],
              "moving_frame", f"transport cancellation {i}")

    # Fourier verification of the exact coefficient -2 and projection norm.
    for k in product((-2,0,1), repeat=3):
        if k == (0,0,0):
            continue
        kv = s.Matrix(k)
        Q = kv*kv.T/(kv.dot(kv))
        require(Q*Q == Q and Q.T == Q, "pressure_projection", "orthogonal")
        Fv = s.Matrix([1,-2,3])
        symbol = s.I*kv*2*s.I*(kv.dot(Fv))/(kv.dot(kv))
        require(symbol == -2*Q*Fv, "pressure_projection", "mixed gradient sign")
        require((Q*Fv).dot(Q*Fv) <= Fv.dot(Fv),
                "pressure_projection", "L2 contraction witness")

    a, K, T = s.symbols("a K T", positive=True)
    equal((a*K)**2/K**3, a*a/K, "scaling", "relative physical energy")
    equal((a*K**2)**2/K**3/(a*K**2), a/K,
          "scaling", "original full enstrophy integral")
    equal(1/(a*K)*K**s.Rational(1,2), 1/(a*s.sqrt(K)),
          "scaling", "background gradient L2")
    equal(1/(a*K)/K, 1/(a*K**2),
          "scaling", "background Lipschitz normalization")
    equal((T*mu)*T**2/T, T**2*mu,
          "scaling", "time-normalized relative dissipation")
    equal(T*T, T**2, "scaling", "time-normalized pressure")
    require(F(9,16)-F(1,8)-F(1,16) >= F(1,4),
            "constants", "remaining relative energy")
    require(F(3,2)*F(1,6) == F(1,4),
            "constants", "annular background tolerance")
    require(F(16,9)*2 == F(32,9) and F(64,9) < 8,
            "constants", "full dissipation majorant")
    require(4*F(1,8) == F(1,2),
            "constants", "relative-to-full dissipation error")
    b, G2, M0 = s.symbols("b G2 M0", positive=True)
    equal(G2*(b/(4*G2))+b/4, b/2,
          "constants", "local relative mass with both backgrounds retained")
    equal((b/(4*G2))**2/(4*M0*M0), b*b/(64*G2*G2*M0*M0),
          "constants", "physical localized mass")
    # Hilbert inequality converting relative dissipation to full dissipation.
    z, h = s.symbols("z h", real=True)
    equal(2*z*z+2*h*h-(z-h)**2, (z+h)**2,
          "relative_energy", "dissipation conversion nonnegative remainder")

    cases = 0
    for g0, l0, length in product((F(6,5),F(3,2),F(2)),
                                 (F(5,4),F(2)), (2,5,13)):
        cases += 1
        aa, kk = F(1), F(1)
        clocks, amplitudes, scales = [], [], []
        for n in range(length):
            clocks.append(aa*kk*kk)
            amplitudes.append(aa); scales.append(kk)
            aa *= g0+F(n%2,9)
            kk *= l0+F(n%3,11)
        for n in range(length):
            tail = sum(F(1)/clocks[j] for j in range(n,length))
            require(tail <= F(1)/(1-F(1)/(g0*l0*l0))/clocks[n],
                    "clock_sequences", "full remaining clock")
            require(amplitudes[n]*scales[n]**2 >= 1,
                    "clock_sequences", "background strain decreases")
            require(amplitudes[n]**2*scales[n] >= 1,
                    "clock_sequences", "background annular L2 decreases")
        require(sum(g0**(-n) for n in range(length)) < 1/(1-1/g0),
                "clock_sequences", "summed full viscous majorant")

    result = {
        "status": "PASS_EXACT_FINITE_IDENTITIES",
        "assertions": sum(counts.values()),
        "groups": dict(counts),
        "rational_clock_sequences": cases,
        "scope_exclusions": [
            "No continuum compactness or Chae--Wolf theorem certification",
            "No numerical N_*, viscosity threshold, or event locator",
            "No simulated or certified regenerative turnover",
            "No independent mathematical audit or NS-R3 resolution",
        ],
    }
    text = json.dumps(result, indent=2)+"\n"
    print(text, end="")
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path)
    main(parser.parse_args().json)
