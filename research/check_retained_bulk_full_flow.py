#!/usr/bin/env python3
"""Exact finite identities for retained-bulk full-flow approximation.

Not a PDE validator, independent audit, or simulated/certified turnover.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json
from math import comb
from pathlib import Path

import sympy as s


def main(output: Path | None = None) -> None:
    counts: Counter[str] = Counter()

    def require(condition: bool, group: str, label: str) -> None:
        if not condition:
            raise AssertionError(f"{group}: {label}")
        counts[group] += 1

    def equal(lhs: s.Expr, rhs: s.Expr, group: str, label: str) -> None:
        require(s.simplify(lhs-rhs) == 0, group, label)

    A, K, nu = s.symbols("A K nu", positive=True)
    r = s.symbols("r", real=True)
    equal((A*K)**(-1)*K**(s.Rational(3,2)-r),
          A**(-1)*K**(s.Rational(1,2)-r), "scaling", "bulk derivative")
    equal((A*K)**(-1)*K, 1/A, "scaling", "critical bulk amplitude")
    equal((A*K)**2/K**3, A**2/K, "scaling", "physical core energy")
    equal((A*K**2)**2/K**3/(A*K**2), A/K,
          "scaling", "whole physical enstrophy integral")
    equal(nu*A/K/(A**2/K), nu/A, "scaling", "normalized dissipation")
    equal(K/A**2*(A*K)**2/K**3, 1, "scaling", "energy inverse transform")
    equal(K**s.Rational(1,2)*(A*K)/K**s.Rational(3,2), A,
          "scaling", "measured annular amplitude")
    equal((A*K)**2*K/((A*K)*(A*K**2)), 1,
          "scaling", "time/convection ratio")
    equal(nu*(A*K)*K**2/((A*K)*(A*K**2)), nu/A,
          "scaling", "ordinary viscosity")

    full_normalized_energy = s.symbols("full_normalized_energy", positive=True)
    equal((A**2/K)/(A**2/K*full_normalized_energy),
          1/full_normalized_energy, "scaling", "exact annular energy fraction")

    # Exact expansion of the full equation, not selected interaction trees.
    t = s.symbols("t", real=True)
    x = s.symbols("x0:3", real=True)
    w = s.Matrix([s.Function(f"w{i}")(t,*x) for i in range(3)])
    z = s.Matrix([s.Function(f"z{i}")(t,*x) for i in range(3)])
    U = w+z
    lap = lambda f: sum(s.diff(f,q,2) for q in x)
    adv = lambda a,b: s.Matrix([sum(a[j]*s.diff(b[i],x[j])
                                    for j in range(3)) for i in range(3)])
    left = U.diff(t)-nu*U.applyfunc(lap)+adv(U,U)-(w.diff(t)+adv(w,w))
    right = z.diff(t)-nu*z.applyfunc(lap)+adv(U,z)+adv(z,w)-nu*w.applyfunc(lap)
    for i in range(3):
        equal(left[i], right[i], "full_difference_equation", f"component {i}")
        for j in range(3):
            equal(U[i]*U[j]-w[i]*w[j], w[i]*z[j]+z[i]*w[j]+z[i]*z[j],
                  "pressure_stress", f"all stress terms {i},{j}")

    def deriv(f: s.Expr, alpha: tuple[int, ...]) -> s.Expr:
        for q,n in zip(x,alpha):
            f = s.diff(f,q,n)
        return f

    b = s.Function("b")(*x)
    f = s.Function("f")(*x)
    for order in (1,3):
        for alpha in product(range(order+1), repeat=3):
            if sum(alpha) != order:
                continue
            counts_seen = set()
            for j in range(3):
                terms = 0
                for beta in product(*(range(n+1) for n in alpha)):
                    remainder = tuple(a-bb for a,bb in zip(alpha,beta))
                    coefficient = 1
                    for a,bb in zip(alpha,beta):
                        coefficient *= comb(a,bb)
                    terms += coefficient*deriv(b,beta)*deriv(s.diff(f,x[j]),remainder)
                    if sum(beta):
                        counts_seen.add((sum(beta),order+1-sum(beta)))
                equal(deriv(b*s.diff(f,x[j]),alpha), terms,
                      "leibniz", f"order={alpha}, transported derivative={j}")
            require(counts_seen == {(k,order+1-k) for k in range(1,order+1)},
                    "leibniz", "all commutator derivative counts")

    a0,a1,z0,z1 = s.symbols("a0 a1 z0 z1")
    equal(a0*z0-a1*z1, a0*(z0-z1)+z1*(a0-a1),
          "fractional", "Gagliardo product split")
    radius = s.sqrt(sum(q*q for q in x))
    kernel = radius**(-4)
    equal(sum(x[i]*s.diff(kernel,x[i]) for i in range(3)), -4*kernel,
          "fractional", "half-derivative transport kernel")
    require(F(3,4)/3 == F(1,4), "fractional", "L3/Linfinity to L4 interpolation")
    require(2-2 > -1 and 2-6 < -1,
            "fractional", "low/high Fourier Cauchy integrability")

    # Existence witness only: no PDE carrier truncation is used.
    k = s.Matrix([s.Rational(6,5),0,0])
    q = s.Matrix([0,s.Rational(6,5),0])
    a = s.Matrix([0,1,0]); bvec = s.Matrix([0,0,1]); m = k+q
    P = s.eye(3)-m*m.T/(m.dot(m))
    source = P*(a.dot(q)*bvec+bvec.dot(k)*a)
    for i in range(3):
        equal(source[i], s.Rational(6,5)*bvec[i], "carrier", "exact Leray numerator")
    equal(k.dot(a)+q.dot(bvec), 0, "carrier", "transverse inputs")
    require(F(9,16) < F(36,25) < F(9,4), "carrier", "Q1 plateau")
    require(F(9,4) < F(72,25) < 9, "carrier", "Q2 plateau")

    alpha_cases = [F(1,10),F(1,6),F(1,4),F(1,3),F(2,5),F(49,100)]
    for alpha in alpha_cases:
        require(alpha > 0, "exponent_signs", "large initial critical amplitude")
        require(2*alpha-1 < 0, "exponent_signs", "vanishing core energy")
        require(alpha-1 < 0, "exponent_signs", "vanishing physical dissipation")
        require(1-2*alpha > 0, "exponent_signs", "divergent normalized energy")
        require(-alpha < 0, "exponent_signs", "vanishing normalized critical bulk")
        for derivative in (1,2,3,5):
            require(F(1,2)-derivative-alpha < 0,
                    "exponent_signs", "small homogeneous derivative bulk")

    result = {
        "status": "PASS_EXACT_FINITE_IDENTITIES",
        "assertions": sum(counts.values()),
        "groups": dict(counts),
        "rational_exponent_cases": len(alpha_cases),
        "scope_exclusions": [
            "No certification of the analytic homogeneous stability inequalities",
            "No interval PDE validation or numerical reference-flow computation",
            "No positive regenerative turnover, scale-repeating orbit, or blowup",
            "No independent mathematical audit or arbitrary-data continuation bound",
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
