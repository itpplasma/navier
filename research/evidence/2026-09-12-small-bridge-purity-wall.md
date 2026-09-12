# A fixed-horizon small-data bridge cannot produce the required angular purity

Date: 2026-09-12. Input: `itpplasma/navier@3124ff9e94f05a44c93dd454ac71da8187b00b26`.

**Author analytic obstruction; independent audit pending.** This note connects
the proved fixed-horizon six-mode bridge to the new approximate-gap consumer.
It does not rule out a nonperturbative turnover, a long/seed-dependent stage,
or a different full-state consumer.

## Working packet

TERMINAL CLAIM: original unforced NS on R3 with one divergence-free Schwartz
datum, fixed positive viscosity and a genuine finite endpoint, or a proof of
global regularity for every such datum.

ESTABLISHED: on the complete frozen source-reference lattice, six small
half-grade ancestors generate the next four-parent quartet over every fixed
positive horizon, with a rank-four quadratic target map and all sidebands
retained. Physical phase grading says linear source/mean/localization terms
preserve the parent phase integer while products add phase integers. The
approximate-gap weighted consumer requires exponentially small old low-sector
leakage, for example `theta eta <= exp(-cL)`.

FIRST GAP: can the already-proved *small-data fixed-horizon* bridge itself both
generate the next grade and deplete the inherited old grade enough to enter
that consumer?

PREDICTION: no. The old grade is present at linear order in the ancestor
amplitude, whereas the new grade is absent linearly and begins quadratically.
Analytic nonlinear evolution cannot reverse these orders on a fixed horizon.

FALSIFIER: a linear contribution in the new physical grade, loss of the old
linear grade by a finite-time zero of the linear evolution, or a nonanalytic
fixed-horizon endpoint map.

## 1. Abstract analytic lemma

Let X be a Hilbert space with orthogonal grading and let P_old,P_new be two
grade projections. Suppose a semilinear parabolic flow on `[0,T]`, for fixed
`T>0`, depends real-analytically on a small scalar amplitude `epsilon` and
has initial data `epsilon a`, with `a` entirely in the old grade. Assume the
linearized evolution preserves that grade and is injective on `a` at time T.
Assume also that the new grade is absent in the linearized solution.

Then

    u_epsilon(T)=epsilon L_T a+epsilon^2 R(epsilon),       (1)

with `L_T a !=0` and `R` bounded for epsilon in a neighborhood of zero. Hence

    ||P_old u_epsilon(T)|| >= c_T |epsilon|,
    ||P_new u_epsilon(T)|| <= C_T epsilon^2,              (2)

for all sufficiently small nonzero epsilon. Moreover every grade which is
absent from the linear solution is `O(epsilon^2)`.

Since the entire first-order term lies in the old grade,

    ||P_<new u_epsilon(T)|| / ||u_epsilon(T)|| -> 1       (3)

whenever `P_<new` contains the old grade and excludes the new grade. In
particular the low fraction has a fixed positive lower bound, say `1/2`, for
all sufficiently small epsilon. It cannot be `exp(-cL)` along any sequence
with epsilon tending to zero.

Proof. Analyticity gives (1). The first-order coefficient is the derivative of
the flow at zero, namely the linear semigroup applied to `a`. Injectivity gives
its nonzero norm. Projection and the triangle inequality give (2). Orthogonal
decomposition gives (3). No spectral truncation or selected nonlinear tree is
used. QED.

The same statement holds for finitely many complex amplitudes scaled by one
common epsilon: take `a` to be their fixed nonzero vector and use the finite
minimum singular value of the linear endpoint map on that fixed input family.

## 2. Application to the proved six-mode bridge

The complete frozen half-grade lattice equation is

    partial_t u=L u+N(u),

with sectorial heat part, bounded source connection multiplier and full
quadratic incompressible convolution. The finite-time bridge theorem already
proves real-analytic dependence on the six input amplitudes in `H^r`, `r>2`,
on every fixed horizon.

Give all six positive ancestors and their reality partners one common physical
phase grade `m`; this is the grading used by the source harmonic-protection
module. At order one the equation is linear, so every component remains in
`+/-m`. The linear heat/source propagator on each nonzero Fourier key is
injective for every finite time. Thus a nonzero ancestor vector has a nonzero
old-grade endpoint.

Products add physical phase grade. Therefore the next-parent grade `2m` is
absent at order one and first appears at quadratic order. The exact bridge
coefficients show that it is genuinely nonzero and rank four, but that
positivity is not needed for the obstruction: order two is already enough.

Taking the approximate-gap cutoff for the next stage at angular magnitude
`2|m|`, all inherited `m` components lie in the low projection. Consequently,
for the exact complete fixed-horizon reference solution,

    theta_old(T,epsilon)
      := ||Pi_(|grade|<2|m|) u_epsilon(T)||_2
                               / ||u_epsilon(T)||_2
      -> 1                                                   (4)

as `epsilon ->0`, while the desired next-parent quartet is only
`O(epsilon^2)`.

The argument is insensitive to the stable/unstable sidebands generated at
higher order: every such sideband contributes at least quadratically unless it
belongs to the first-order ancestor evolution, in which case it is again old
grade. Reality partners are included in the orthogonal old sector.

## 3. Physical-local scope

The repository's physical harmonic-protection theorem proves that the actual
source's slow/background/mean coefficients, ordinary diffusion, axisymmetric
localization and linear pressure reconstruction preserve the physical phase
integer. Thus **any** fixed-window physical lift which has the same analytic
small-data dependence inherits the order separation above: linear errors
remain in grade `m`; grade `2m` starts quadratically.

A complete finite-L whole-space six-mode lift has not been proved, so this note
does not promote (4) to a new global physical theorem. Its load-bearing use is
more modest and exact: the *existing proved small-data bridge* cannot also be
the purity-producing stage required by the approximate-gap consumer. Any
physical realization that remains a perturbation of that fixed-horizon regime
has the same obstruction.

## 4. Consequence for the constructive frontier

The new approximate-gap consumer does not close the cascade by itself. In the
perturbative bridge regime the wrong grade dominates rather than becoming
exponentially pure. Therefore a successful source route needs an additional
operation before the next handoff:

1. a genuinely nonperturbative depletion/turnover that transfers old `m`
   content into the new `2m` state while retaining the complete inherited
   field; or
2. a seed-dependent/long stage outside the fixed-horizon small-data regime;
   or
3. a different full-state consumer which does not require low-grade purity.

Exact deletion is already excluded by rotational backward uniqueness. Passive
interstage reuse is also unavailable in the continuously self-similar reference:
the old parents are super-amplified. Hence the first constructive object is now
an **approximate nonperturbative turnover**, not another local Taylor/IFT
retuning.

The acceptance contract already frozen in
`2026-09-11-supercritical-turnover-contract.md` remains the terminal version:
for half-scale localization, a scale-repeating negative construction needs
amplitude gain `2<g<=2sqrt(2)`, exact original NS evolution, closure of the
entire output state and one-data iteration. The present theorem does not
construct such a turnover and does not prove it impossible.

The nonprincipal full-history adjoint and arbitrary-data positive producer
remain genuinely distinct alternatives. `NS-R3` remains open.

## Verification scope

This proof uses the analytic-flow theorem already proved in
`2026-09-12-half-grade-finite-time-bridge.md` and the exact grading rules in
`2026-09-11-source-physical-harmonic-protection.md`. The directly relevant
existing checkers are replayed at integration. No new finite checker is needed:
the new step is the analytic order comparison (1)--(4), not a new radical or
finite-lattice arithmetic identity. No canonical proof-graph or formal status
is promoted.
