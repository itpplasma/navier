# Full-ring turnover discovery: a locator, not a continuum certificate

Date: 2026-09-08. Mathematical input main:
`7cd3444f10fa9f9780f4ef8ac1e73a0ebea689f9`.
Status: UNVALIDATED numerical experiments. No theorem, exact trajectory,
independent review, whole-space adapter, shadowing, or claimed breakthrough.
PLAN.md alone is the live allocation. The proved results are in
`2026-09-08-phase-locked-full-ring.md`.

## Equation, data and numerical boundary

Use the original periodic NS Fourier convolution followed by the SPHERICAL
Galerkin projector |k|<=N, at viscosity .01. Initially uhat=-i P_k sigma
on all six permutations of (2,1,0), sigma=(1,1,1), with conjugate negative
partners. The squared L2 energy is E0=72/5; S0=36 sqrt(5)/5, where
S=(1/2)sum |k||uhat(k)|^2 and spatial volume is normalized.

`research/discovery_phase_locked_ring.py` computes P(u cross curl u) on
an FFT grid of side L>3N. This prevents aliasing INTO the retained ball:
a quadratic sum has each coordinate <=2N, and wrapping such a coordinate
by L>3N cannot put it back into [-N,N]. All retained polarizations and
both directions of feedback are evolved. No phase, mirror, or meridional
constraint is imposed on the evolving coefficients. Reality is used when
forming the physical velocity. Classical RK4 advances time.

Modes above N are STILL discarded. Dealiasing does not repair this continuum
truncation. Small energy-balance error, agreement of resolutions, and a
small boundary energy fraction are NOT a bound for the nonlinear high-tail
residual or its amplified effect. No interval arithmetic is used.

## Completed runs and observations

The initial implementation used grids 31,43,55 for N=10,14,18, respectively,
dt=.00625. All reached time .25; N=10 also reached .5. At time .25:

| N | Squared L2 energy | S | Energy outside parents / E0 | Energy above .75N / E0 |
|---|---:|---:|---:|---:|
| 10 | 13.95409387 | 19.11582639 | .23804335 | .01040950 |
| 14 | 13.94905324 | 19.24787840 | .23917405 | .00274405 |
| 18 | 13.94814991 | 19.24619840 | .23877537 | .00162364 |

These are floating-point outputs, not rigorously enclosed numbers. An earlier
N=10 attempt with dt=.002 was interrupted; no completed result is attributed
to that run. No randomized optimization or exhaustive network search occurred.

The committed implementation uses the next FFT-friendly length above 3N.
A rerun at N=10, grid 32, dt=.003125, T=.25 completed. Selected energy fractions:

| time | Intended ring T / E0 | Mandatory side ring S / E0 | Total outside parents / E0 |
|---|---:|---:|---:|
| .05 | .00245540 | .01072388 | .01400843 |
| .10 | .00544595 | .03560957 | .05162132 |
| .15 | .00404458 | .06157242 | .10512408 |
| .20 | .00063326 | .07961375 | .16895414 |
| .25 | .00073492 | .08664088 | .23804341 |

Here T consists of permutations of (3,3,0),(4,1,1) and their negatives;
the side ring consists of permutations of (3,2,1) and their negatives.
Other generated modes are included in the total. At .25, S=19.11582924,
and the integrated viscous energy-ledger error was about -1.65e-8.
The largest real part of a Fourier coefficient was about 2.7e-17; no
invariant phase constraint was enforced by hand.

The intended channel first grows and then loses most of its energy while
the side ring and later daughters carry substantial energy and TOTAL critical
energy grows. Energy depletion alone does not prove a scalar sign crossing;
none is asserted here. This is the first concrete numerical reason not to
identify intended-channel restoration with restoration of the complete norm.
The corresponding continuum claim remains unproved.

A transverse second-moment diagnostic of nonparent energy grew from about
2.8716 at .05 to 5.1078 at .25 in this N=10 run. Thus a proposed bound copied
from the initial daughter geometry cannot simply be assumed to persist.
This is not a rigorous counterexample to a universal continuum inequality.

## Reproduction and the missing proof

Examples:

    python3 research/discovery_phase_locked_ring.py --N 10 --dt .003125 --T .25
    python3 research/discovery_phase_locked_ring.py --N 14 --dt .00625 --T .25
    python3 research/discovery_phase_locked_ring.py --N 18 --dt .00625 --T .25

The latter two commands use FFT-friendly grid lengths rather than the initial
43/55 choices; the first table records the actual initial runs, not falsely
labelled exact output of a different command. Numpy and Scipy are required.
Optional --json writes a generated diagnostic report, not a proof certificate.

The finite-event conjecture selected in PLAN asks for a genuine smooth
continuum periodic solution at nu=.01, some tau<=.25, at least E0/5 outside
parents, and S(tau)>=(11/10)S0. A proof requires a rigorous existence interval
and a bound for the complete unretained tail/response, not just a smaller RK
step. No such bound was obtained. The exact order-eight jets in the companion
proof likewise have no controlled remainder at .25.

A positive finite-event result would defeat a nonincreasing-critical-norm
claim at that transfer threshold. It would NOT prove a scale-repeating cell,
an infinite cascade, failure of a full-input RF-q bound, or a terminal NS
result. A subsequent cell must accept all inherited tails, phases, changed
polarizations and the correctly rescaled viscosity. A negative result about
this single initial ring would not exclude other original-NS mechanisms.
