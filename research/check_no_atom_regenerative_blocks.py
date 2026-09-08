#!/usr/bin/env python3
"""Finite exact identities supporting the no-atom full-state block proof.

These are not PDE certificates, a numerical event locator, a proof of the
Chae--Wolf theorem, or an independent mathematical audit. No floating-point
arithmetic is used. Output is JSON; an optional --json path stores it too.
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

    def require(condition: bool, group: str, label: str) -> None:
        if not condition:
            raise AssertionError(f"{group}: {label}")
        counts[group] += 1

    def equal(lhs: s.Expr, rhs: s.Expr, group: str, label: str) -> None:
        require(s.simplify(lhs - rhs) == 0, group, label)

    # u(t,x)=a K W(a K^2 t,Kx), with ordinary viscosity nu.
    a, K, nu, T, lam, gain = s.symbols("a K nu T lam gain", positive=True)
    equal((a*K)*(a*K**2), (a*K)**2*K, "scaling", "time equals convection")
    equal(nu*(a*K)*K**2/(a*a*K**3), nu/a,
          "scaling", "normalized viscosity")
    equal((a*K)**2/K**3, a**2/K, "scaling", "full energy")
    equal((a*K**2)**2/K**3, a**2*K, "scaling", "full enstrophy")
    equal((a**2*K)/(a*K**2), a/K, "scaling", "enstrophy time integral")
    equal((nu/a)/gain, nu/(a*gain), "scaling", "viscosity update")
    equal((a*gain)*(K*lam)**2/(a*K**2), gain*lam**2,
          "scaling", "clock update")
    equal(s.sqrt(K)*(a*K)/K**s.Rational(3,2), a,
          "scaling", "annular critical amplitude")
    # The actual temporal normalization v(s,x)=T u(T(s+1),x).
    equal(T*T, T**2, "temporal_normalization", "velocity time derivative")
    equal((T*nu)*T, T**2*nu, "temporal_normalization", "diffusion coefficient")
    equal((T*nu)*T**2/T, T**2*nu,
          "temporal_normalization", "total dissipation factor")
    E, grad = s.symbols("E grad", positive=True)
    equal(T**2*E, (T*s.sqrt(E))**2,
          "temporal_normalization", "energy factor")
    # Physical time remaining equals T*(-s), cancelling gradient factor T.
    equal((T*s.Symbol("remaining"))*grad,
          s.Symbol("remaining")*(T*grad),
          "temporal_normalization", "Type I constant")

    # Full local energy product rule; no pressure or heat term omitted.
    x = s.symbols("x0:3", real=True)
    t = s.symbols("t", real=True)
    u = [s.Function(f"u{i}")(t, *x) for i in range(3)]
    p = s.Function("p")(t, *x)
    speed2 = sum(z*z for z in u)
    divu = sum(s.diff(u[i], x[i]) for i in range(3))
    lap = lambda z: sum(s.diff(z, q, 2) for q in x)
    adv = [sum(u[j]*s.diff(u[i], x[j]) for j in range(3)) for i in range(3)]
    flux = sum(s.diff((speed2+2*p)*u[j], x[j]) for j in range(3))
    equal(flux, 2*sum(u[i]*(adv[i]+s.diff(p,x[i])) for i in range(3))
          +(speed2+2*p)*divu, "local_energy", "full cubic and pressure flux")
    equal(lap(speed2), 2*sum(u[i]*lap(u[i]) for i in range(3))
          +2*sum(s.diff(u[i], q)**2 for i in range(3) for q in x),
          "local_energy", "full viscous defect")
    equal(s.diff(speed2,t), 2*sum(u[i]*s.diff(u[i],t) for i in range(3)),
          "local_energy", "time derivative")
    # The far pressure kernel is second derivative of |x|^-1.
    require(-1-2 == -3 and -1-3 == -4,
            "local_energy", "far pressure and gradient homogeneities")

    # Endpoint trace exponents: energy/Lipschitz interpolation, integrable flux.
    equal(s.Rational(1,5)*2+s.Rational(3,5), 1,
          "trace_exponents", "velocity amplitude homogeneity")
    equal(-3*s.Rational(1,5)+s.Rational(3,5), 0,
          "trace_exponents", "spatial dilation for speed interpolation")
    h = s.symbols("h", positive=True)
    equal(s.integrate(h**(-s.Rational(3,5)),h),
          s.Rational(5,2)*h**s.Rational(2,5),
          "trace_exponents", "uniform temporal flux primitive")

    # gamma >= gamma_* and ||Q1 V||2=1 imply local full-state energy.
    gamma, G2 = s.symbols("gamma G2", positive=True)
    b = 3*gamma/10
    equal(s.Rational(5,3)*(3*gamma/5), gamma,
          "localization", "annular Bernstein constant")
    require(s.Rational(3,10)<s.Rational(3,5),
            "localization", "strict supremum slack")
    m0 = b*b/(4*G2*G2)
    equal(G2*s.sqrt(m0)+b/2, b,
          "localization", "retained-tail Cauchy Schwarz bound")
    equal(m0, (3*gamma/(20*G2))**2,
          "localization", "normalized ball mass")
    M0, theta0 = s.symbols("M0 theta0", positive=True)
    equal(theta0**2*m0/(2*M0**2),
          theta0**2*(s.Rational(1,2)/M0**2)*m0,
          "localization", "physical and time-normalized mass")

    # Deterministic rational parameter sequences: clocks only, NOT NS orbits.
    sequences = 0
    for g0 in [F(6,5),F(3,2),F(2)]:
        for l0 in [F(5,4),F(2)]:
            for length in [1,2,5,12]:
                sequences += 1
                theta_max = F(7,3)
                r = g0*l0*l0
                clocks = [F(1)]
                aa, kk = F(1), F(1)
                gains, scales = [], []
                for n in range(length):
                    g = g0+F(n%3,7)
                    ell = l0+F(n%2,5)
                    gains.append(g); scales.append(ell)
                    aa *= g; kk *= ell
                    clocks.append(aa*kk*kk)
                for n in range(length):
                    require(clocks[n+1]/clocks[n] == gains[n]*scales[n]**2,
                            "rational_clock_sequences", "exact clock ratio")
                    tail = sum(theta_max/clocks[j] for j in range(n,length))
                    require(tail <= theta_max/(1-1/r)/clocks[n],
                            "rational_clock_sequences", "full remaining time")
                require(aa >= g0**length and kk >= l0**length,
                        "rational_clock_sequences", "unbounded gain and scale")
                finite = sum(g0**(-n) for n in range(length))
                require(finite == (1-g0**(-length))/(1-1/g0),
                        "rational_clock_sequences", "exact dissipation weights")
                require(finite < 1/(1-1/g0),
                        "rational_clock_sequences", "infinite dissipation bound")

    # Positive normalized cost alone does NOT bound the number of events.
    for n in [1,2,8,32]:
        weights = [F(1,2)**j for j in range(n)]
        require(sum(weights) == 2*(1-F(1,2)**n) < 2,
                "budget_scope", "unit normalized costs can be physically summable")

    result = {
        "status": "PASS_EXACT_FINITE_IDENTITIES",
        "assertions": sum(counts.values()),
        "groups": dict(counts),
        "rational_parameter_sequences": sequences,
        "scope_exclusions": [
            "No certification of the Chae--Wolf theorem or compactness passage",
            "No PDE existence, continuity, or a posteriori interval validation",
            "No numerical values for N_*, mu_*, delta_*",
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
