#!/usr/bin/env python3
from pathlib import Path
import json, subprocess

ROOT = Path.cwd()
EVID = ROOT / "research/evidence/2026-09-12-prefix-summability-wall.md"
CHECK = ROOT / "research/check_prefix_summability.py"
PLAN = ROOT / "PLAN.md"
SNAP = ROOT / "research/game/snapshot.json"


def replace_once(text, old, new, label):
    if text.count(old) != 1:
        raise SystemExit(f"{label}: expected exactly one replacement site, found {text.count(old)}")
    return text.replace(old, new, 1)


def write_new(path, content):
    if path.exists():
        if path.read_text() != content:
            raise SystemExit(f"refusing to overwrite differing {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def git_blob(path):
    p = subprocess.run(["git", "hash-object", str(path)], cwd=ROOT, text=True, capture_output=True, check=True)
    return p.stdout.strip()


evidence = r'''# Exponential unstable-site proliferation cannot force common-control divergence by counting alone

Date: 2026-09-12. Repository input before this checkpoint: current `main` at
integration time.

**Status: exact summability theorem / scoped obstruction to a naive complete-adjoint
argument. Independent mathematical audit and novelty assessment are pending.**
The theorem does not produce one physical initial trace and does not estimate the
complete source-history operator. It proves that the already established growth
in the number of unstable source-lattice coordinates is much too slow, by itself,
to force divergence of the minimum-prefix control norm at the source's local
`exp(-gamma L)` seed scale.

## 1. Prediction before the exact test

A tempting negative route after the rescaled-unstable-proliferation theorem is:
there are more and more unstable coordinates, the corresponding observations can
be regarded as independent or orthogonal, and therefore the Pythagorean prefix
cost must diverge.

The prediction tested here is the opposite. The source local-entry cost is
quasi-Gaussian in the scale label, while the number of unstable lattice sites is
only exponential. Therefore multiplicity and orthogonality alone cannot create a
divergent common-control norm. A successful full-adjoint obstruction must obtain
a genuinely larger **whole-prehistory** cost per observation, or a separate
nonlinear de-forcing obstruction.

## 2. Gaussian-versus-exponential prefix lemma

Let stages be indexed by `j>=1`. Suppose stage `j` contains at most

    M_j <= C_M exp(a j)                                      (2.1)

orthogonal control directions, and suppose a hypothetical control construction
or lower-scale calibration assigns each such direction a norm no larger than

    delta_j <= C_delta exp(-gamma j^2 + b j),               (2.2)

with `gamma>0` and finite `a,b`.

Then

    sum_j M_j delta_j^2 < infinity.                          (2.3)

Indeed

    M_j delta_j^2
      <= C exp[-2 gamma j^2 + (a+2b)j],                     (2.4)

and the ratio of consecutive right-hand sides has logarithm

    -4 gamma j - 2 gamma + a + 2b,                          (2.5)

which tends to `-infinity`. Hence the series converges.

The same conclusion survives every fixed polynomial Fourier/Sobolev weight.
If all relevant physical frequencies satisfy

    K_j <= C_K exp(kappa j),                                (2.6)

then for every fixed `N>=0`,

    sum_j M_j K_j^(2N) delta_j^2 < infinity,                (2.7)

because (2.4) merely gains the linear exponent `2N kappa j`.

This is an exact asymptotic statement. It does not assume that the actual source
controls attain (2.2); it says that **counting alone cannot prove they do not**.

## 3. Application to the live source frontier

The exact rescaled source spectrum in
`2026-09-11-source-rescaled-unstable-proliferation.md` has unstable-site count
of order

    M_j = O(2^(2j/3)).                                      (3.1)

The actual source primary-pulse adjoint in
`2026-09-10-source-pulse-adjoint.md` gives the local entry scale

    P_j(0) = exp(-gamma_- L_j),                             (3.2)

with `L_j` comparable to the square of the logarithmic scale label. Along any
factor-two or other geometric subsequence this is

    P_j(0) <= exp(-c j^2 + O(j)).                           (3.3)

The physical carrier and lattice frequencies on such a subsequence grow at
most exponentially in `j`, so every fixed Schwartz/Sobolev polynomial weight
fits (2.6).

Consequently, even in the deliberately hostile bookkeeping model in which
**every** unstable site at stage `j` required its own orthogonal control
component of size `exp(O(j)) P_j(0)`, both the squared Hilbert control norm and
every fixed polynomially weighted coefficient norm would remain summable.
The exponentially growing unstable dimension does not contradict a Schwartz
trace on static summability grounds.

The common-control criterion already proved in the repository says that a
single finite-norm control exists iff the minimum-norm prefix controls stay
uniformly bounded. The present lemma does **not** prove that boundedness for the
physical source. It proves that one cannot derive its failure merely from the
number of observations, their orthogonality, or the local seed scale.

## 4. What a complete physical adjoint must now prove

A negative UE1 proof through the adjoint must therefore exhibit a load-bearing
history effect absent from the counting argument. Examples that would suffice
include a source-specific lower bound showing that transporting the observation
back to physical time zero multiplies its local cost by a factor large enough
to destroy (2.3), or a coupled nonlinear budget identity forcing non-square-
summable prefix increments.

Pure passive heat has exactly such severe high-angular backward cost, but the
live frontier includes radial-exterior occupation and nonlinear/parametric
supply, so that passive cost cannot be substituted for the complete physical
adjoint.

Likewise, unstable-site proliferation remains an architectural complication for
a constructive cascade, but it is not by itself a norm-divergence theorem.

## 5. Exact checker and scope

`research/check_prefix_summability.py` checks the exponent arithmetic with
exact rational numbers over a grid of positive Gaussian rates and finite linear
multiplicity/frequency exponents. The analytic proof is equations (2.1)--(2.7);
the finite checker is regression evidence only.

No common physical initial trace, nonlinear de-forcing solution, singularity
preservation, arbitrary-data regularity bound, or `NS-R3` theorem is claimed.
The canonical proof graph and formal status are unchanged.
'''

checker = r'''#!/usr/bin/env python3
"""Exact regression checks for Gaussian-vs-exponential prefix summability."""
from fractions import Fraction

checks = 0

# For a term 2^E_j with E_j=-2*gamma*j^2 + c*j, the consecutive
# exponent difference is -4*gamma*j - 2*gamma + c.  Check exact
# eventual negativity for a broad rational grid, including extra fixed
# polynomial-frequency weights folded into c.
for gp in range(1, 8):
    for gq in range(1, 8):
        gamma = Fraction(gp, gq)
        for cp in range(-8, 17):
            for cq in range(1, 6):
                c = Fraction(cp, cq)
                threshold = max(1, int((c - 2*gamma) / (4*gamma)) + 2)
                for j in (threshold, threshold + 1, threshold + 7, threshold + 31):
                    diff = -4*gamma*j - 2*gamma + c
                    assert diff < 0
                    checks += 1

# Exact monomial exponent check with unstable multiplicity 2^(2j/3),
# seed 2^(-alpha*j^2+b*j), and a fixed frequency weight 2^(N*kappa*j).
for alpha_num in range(1, 6):
    alpha = Fraction(alpha_num, 5)
    for b_num in range(-3, 5):
        b = Fraction(b_num, 3)
        for N in range(0, 9):
            kappa = Fraction(5, 4)
            c = Fraction(2, 3) + 2*b + 2*N*kappa
            j = max(2, int((c - 2*alpha) / (4*alpha)) + 3)
            E_j = -2*alpha*j*j + c*j
            E_next = -2*alpha*(j+1)*(j+1) + c*(j+1)
            assert E_next < E_j
            checks += 1

print(f"prefix-summability exact checks: {checks} passed")
'''

write_new(EVID, evidence)
write_new(CHECK, checker)
CHECK.chmod(0o755)

plan = PLAN.read_text()
plan = replace_once(
    plan,
    "source_quadratic_far_pressure_budget: input-only-from-finite-energy-author\nsource_global_growing_parent_supply: not-produced",
    "source_quadratic_far_pressure_budget: input-only-from-finite-energy-author\nsource_prefix_counting_obstruction: exponential-multiplicity-does-not-force-prefix-divergence\nsource_global_growing_parent_supply: not-produced",
    "PLAN yaml prefix-counting status",
)
old = '''The next active test must therefore address actual correction-driven entry or
in-core nonlinear generation with the inherited angular hierarchy retained,
or estimate the complete physical adjoint including that hierarchy. No bound
on the collar stress or full-history gain has been obtained; direct far-field
quadratic pressure input now has the energy-only bound above. UE1 and the terminal claim remain open.
'''
new = '''A separate exact counting test closes a tempting shortcut on the complete-adjoint
side. The rescaled unstable family has only exponential multiplicity
`M_j=O(2^(2j/3))`, whereas the source local entry scale is
`exp(-gamma L_j)` with `L_j` comparable to `j^2` on a geometric subsequence.
Even if every unstable site demanded an orthogonal control component at any
`exp(O(j)) exp(-gamma j^2)` scale, the squared prefix norm and every fixed
polynomially frequency-weighted sum would converge. Thus unstable dimension,
orthogonality and the local seed scale alone cannot prove that the common-control
criterion fails. A complete physical adjoint must show genuine whole-prehistory
cost inflation or a nonlinear budget obstruction. See
`research/evidence/2026-09-12-prefix-summability-wall.md`.

The next active test must therefore address actual correction-driven entry or
in-core nonlinear generation with the inherited angular hierarchy retained,
or estimate the complete physical adjoint including that hierarchy. No bound
on the collar stress or full-history gain has been obtained; direct far-field
quadratic pressure input now has the energy-only bound above. UE1 and the terminal claim remain open.
'''
plan = replace_once(plan, old, new, "PLAN active-frontier paragraph")
PLAN.write_text(plan)

snap = json.loads(SNAP.read_text())
snap["authoritative_sources"]["PLAN.md"] = git_blob(PLAN)
snap["authoritative_sources"][str(EVID.relative_to(ROOT))] = git_blob(EVID)
snap["active_frontier"] = (
    "correction-driven thin-collar entry or in-core nonlinear parent generation with the inherited angular hierarchy, "
    "or a complete physical adjoint with genuine whole-prehistory cost inflation beyond exponential counting"
)
SNAP.write_text(json.dumps(snap, indent=2) + "\n")

print("prepared prefix-summability checkpoint")
