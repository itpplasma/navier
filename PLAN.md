# Navier--Stokes: structure-preserving refinement and resonant reduction

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: resonance-aware-refinement-research-2026-09-07
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: RF3-input-bounded-moving-metric-and-nonlinear-interlevel-feedback
active_architecture: compatible-refinement-with-defect-and-tracking-control-unproved
complete_terminal_route: none-established
terminal_status: not-proved
terminal_obstruction: input-only-critical-refinement-estimate-not-produced
secondary_goal: MIC-R3
secondary_goal_status: kinetic-and-microscopic-interfaces-remain-separately-gated
formal_work_this_run: deferred
public_release: false
```

## 1. Authority, unchanged target, and preserved state

This is the sole live allocation. The owner requests a research attack, not an
assertion that the proposed architecture will succeed. NS-R3 remains: for
EVERY solenoidal Schwartz datum on R3 and EVERY fixed nu>0, prove global smooth
velocity and normalized pressure for the ORIGINAL unforced incompressible
Navier--Stokes equation, with energy no greater than the initial energy.

The entire preceding PLAN is preserved byte-for-byte in
`research/history/PLAN-before-refinement-2026-09-07.md`, Git blob
`d1fbe9edcb0f097d6fc4b9c85a3f56b68928b8f9`, from refreshed main
`f0add720620a4e381c98bb6ed762bc2906f77e11`. Its claims, review qualifications,
exclusions, phase records and provenance are retained, not retracted or promoted.
The canonical `docs/proof-graph.yaml`, `docs/proof.md`, earlier evidence, paper
and formal repositories are unchanged by this planning wave. NS-R3 and CRITICAL
remain gaps. `docs/refinement-programme.yaml` is a research map, NOT an audited
proof graph or a substitute for the canonical terminal chain.

Read `research/refinement-slow-manifold-contract.md` for exact quantifiers,
interfaces, parameter costs and this wave's frontier packet. The separate
`research/kinetic-clay-hilbert-contracts.md`, its KPC source notes, and
`docs/programme-graph.yaml` still govern KIN-R3 and MIC-R3. A periodic experiment
is not the R3 theorem. No new formal coverage or literature axiom is introduced.
This allocation supersedes the historical K1-first ordering, not its contracts.

## 2. One primary mechanism, not a menu of analogies

Try to produce SUMMABLE CRITICAL ERRORS BETWEEN ACTUAL RESOLUTIONS by preserving
incompressibility, skew transfer, pressure projection and viscous dissipation;
use approximate invariant manifolds or causal memory to organize only those
interactions that can be eliminated with controlled cost. Retain resonant and
strongly coupled modes. The required output is not energy conservation at fixed
mesh, a formal all-orders expansion, or an AP limit at fixed spatial resolution.

For nested conforming reconstructions u_j on h_j=2^(-j)h_0, a sufficient
certificate on each finite horizon H is

    sum_j h_j^(-1/2) ||u_(j+1)-u_j||_(L-infinity(0,H;L2))
        <= C(u0,nu,H) < infinity.                          (RF-SUM)

Uniform inverse/Bernstein inequalities, a bounded coarse term, consistency,
whole-space/tail control, initial trace and the energy passage then give a
limit bounded in L-infinity L3. Weak--strong identification and the BANKED
CONTINUATION/ENERGY suffix give NS-R3. RF-SUM is a sufficient contract, not a
proved producer, not claimed equivalent to regularity, and not required to
hold for every possible discretization. A weaker proved critical-output
certificate is allowed when its complete consumer is supplied.

The promising mechanism to test is paired dissipative feedback with resonant
memory retained. Its ordinary energy sign is not a critical weighted sign.
The first genuinely new estimate must control reconstructed fine content AND
tracking error AND retained tangential dynamics. Small invariance defect or
fast normal attraction alone does not control motion along the manifold.

## 3. Ordered frontier and hard gates

RF0 -- Freeze a faithful spatially semidiscrete model. Start with an exact
Fourier--Galerkin calibration to isolate algebra; transfer only proved operator
identities and quantitative bounds to a specific conforming FEEC/mimetic model.
Require d_h^2=0, mass-matrix adjoints, appropriate uniformly bounded commuting
projections, exact solenoidality, consistent convection, and viscous energy
balance. Do not assume FEEC implies the Jacobi identity of a nonlinear bracket.
Finite-box constants must survive the large-domain limit for NS-R3.

RF1 -- Test the closure before building it. For dot x=f(x,y), dot y=g(x,y),
record R_Phi=g(x,Phi)-D Phi f(x,Phi) and the full normal operator
D_y g-D Phi D_y f. Inspect actual NS heat-rate resonances and their nonzero
interaction coefficients. No division by a vanishing spectral denominator,
no imaginary gyrofrequency substituted for diffusive decay, and no claim of a
near-identity change just because frequency is large. A failure of a C2 static
slaving graph must be repaired by retaining its resonant variable or by causal
memory, not broadened into a no-go for all slow manifolds.

RF2 -- Prove an elimination/reconstruction estimate uniform in the cutoff.
Keep initial layers, time ordering, the correct source/feedback pairing,
projection defects and any nonautonomous metric derivatives. Distinguish a
small residual from a small total high-mode reconstruction. A positive result
on an actual invariant NS sector tests this universal mechanism but is NOT a
strict singularity reduction or the arbitrary-data theorem.

RF3 -- The main analytic frontier: signed three-dimensional feedback across
resolutions. For two genuine Galerkin trajectories, the error contains both
resolved and unresolved corrections. Retain the strain term B(error,coarse)
and all projection residuals; do not replace the exact equation by a freely
forced stress system. Derive critical summability without an unknown strain
integral, small critical data or a supplied endpoint Sobolev norm. A surviving
algebraic identity with no such estimate is not terminal progress.

RF4 -- Prove RF-SUM, or a precisely specified weaker critical certificate,
including original datum preparation, mesh-independent constants, tails and
whole-space passage. RF5 -- instantiate consistency/uniqueness/continuation,
check all Clay clauses, and obtain independent audits before any promotion.
No implementation, theorem-library work or paper formatting precedes RF3 just
because it is easier. Code is used only for a named identity, counterexample
or numerical certificate with its actual quantifiers.

## 4. Kinetic, geometric and algebraic support: explicit consuming tasks

Kinetic theory is a support/alternative only with a faithful prepared family.
Keep the collision-invariant kernel exact, invert only on its complement, and
prove the discrete collision gap/entropy and velocity-tail bounds required by
the chosen observation. Track epsilon*|k|: kinetic hydrodynamic separation is
not uniform over arbitrary spatial frequencies. AP at fixed mesh does not
prove RF-SUM. Preserve the existing hard-sphere kernel unless BOTH fluid and
particle contracts are replaced explicitly. KIN-R3 and MIC-R3 are not solved
by a fluid-only discrete calculation.

Possanner/Burby-style reduction means a controlled change of variables and
reconstruction with retained resonances and explicit remainder, not an
uncontrolled Taylor truncation and not convergence inferred from all finite
orders. Hamiltonian oscillatory stability and dissipative normal attraction
are distinct mechanisms. Transform the metric/dissipation as well as the
Poisson structure; distinguish total thermodynamic from kinetic energy.

Stafford-style finite algebra supplies exact detection or identities only
with operator domains, cofactor bounds and cutoff remainder. Finite matrices
cannot satisfy [D,X]=I (trace obstruction); retain the truncation defect.
Bjoerk-style defect replacement needs a proved decreasing quantity and
preservation of the original dynamics. No Noetherian termination is assumed
for an infinite refinement hierarchy. Kleinian leading-defect analysis is a
methodological guide, not an ADE model for fluid singularities.

## 5. Binding exclusions and preserved positive consumers

The archived PLAN retains the exact hypotheses and review status of every
previous result. In particular preserve: equivalent critical-norm/clock
obstructions; the finite-energy versus critical-packet scaling; failed
instantaneous entropy/covariance signs; the L2-only FORCED Stokes stress
counterexample; the actual prepared-family Fisher counterexample; the
single-interaction (not sustained-cascade) branching test; and the distinct
inviscid/shear, scalar-model and weak-solution scopes.

The graph-lift test at f0add720 excludes exact positive finite-observable
Dirac graph lifts as finite-contact detectors of their artificial conormal
singularities. It does NOT exclude dynamical low/high invariant graphs,
actual kinetic distributions, FEEC, stochastic methods or genuine critical
defect measures. Do not conflate these two meanings of graph.

The planar, local-return, concentrating-return, temporal-Type-I-energy and
axial record-block results remain author-checked scoped consumers. None has
forced recurrence, axiality, Type I or bounded record blocks for arbitrary
singularities. Do not default to another unrelated symmetry exclusion.

Retire ONLY an inference defeated by a proof or a counterexample in its
stated premise class. A failed estimate, an experiment, or absence of a
proof is an OPEN obligation, not a theorem of impossibility.

## 6. Frontier-math workflow and persistence

Use `krystophny/prompts`, frozen revision
`2929639d8ed611917bd1086df002296a611a475b`,
`skills/math-frontier/SKILL.md`. Each wave declares the terminal claim,
established inputs, first gap, falsifier, forbidden inferences and check.
Choose one of DISCOVER/FALSIFY/REPAIR/REVIEW/INTEGRATE. Stop a candidate at its
first unsupported implication; retain valid consumers; attempt one concrete
repair before abandoning an architecture. No correlated worker delegation or
independent audit is invented. Existing delegation restrictions remain.

Checkpoint the requested plan revision, then a substantive mathematical wave
and its minimal live-state update. Preserve unrelated files and concurrent
commits; refresh main before each non-force push. No scratch dumps, repeated
status-only commits, public release, outside contact, manuscript recreation,
or writes to other repositories. Unsigned commits are authorized.

Run `python3 research/verify.py --research-only` on a complete research checkout
when available, plus the focused identity/oracle and `git diff --check`.
Report a snapshot-only validation as such. Tests never certify PDE proofs.
Terminal promotion requires separate mathematical, source and statement audits.

Every end-of-wave report states MODE / RESULT, CLAIM AND SCOPE, EVIDENCE,
FIRST GAP, SURVIVING CONDITIONAL SUFFIX, NON-CLAIMS and NEXT DISTINCT ACTION.
A benchmark success is not described as a breakthrough in arbitrary-data NS.

## 7. Current wave: a proved obstruction and a causal repair

Read `research/evidence/2026-09-07-resonant-slaving-and-causal-refinement.md`.
Theorem 1 excludes time-independent C2 invariant spectral graphs tangent to
all modes |k|<=K in the periodic Galerkin family when the fine cutoff includes
sqrt(2)K. A nonzero orthogonal-parent interaction is heat-rate resonant, so
its quadratic invariance equation has no solution. More Taylor orders with
that same graph and zero quadratic defect cannot repair it. This is not a
no-go for all slow manifolds or all compatible discretizations.

Theorems 2--3 repair the same interaction with exact causal memory in an
actual periodic shear/passive-component NS sector. The full time-ordered
series has remainder bounded by

    ||w0||2 exp(-nu K^2 t)
      [alpha(1-exp(-nu K^2 t))]^(M+1)/(M+1)!,
    alpha=|a0|/(nu K),

uniformly in the Galerkin cutoff and for every t>=0 and finite alpha. For
N_j=2^jK it yields the exact RF-SUM benchmark bound

    sum_j sqrt(N_j) sup_t ||u_(N_(j+1))-u_(N_j)||2
       <=2 sqrt(K)||w0||2 alpha exp(alpha).

This tests the nominated general mechanism but is NOT a strict singularity
reduction, a whole-space result or a general NS convergence theorem. The
absence of three-dimensional feedback in that sector is explicit. The next
question is the normal propagator and critically weighted signed feedback
in the full error equation of contract Section 5, not another passive model.
The exact rational oracle initially passed 469 finite checks. The strain/metric
extension below brings this to 631, including negative controls. These are
not independent mathematical audit; review remains pending.

## 8. Strain test completed; the remaining producer is explicit

Read `research/evidence/2026-09-07-normal-transient-and-metric-repair.md`.
An exact global unforced periodic NS shear has a high-frequency normal
variation whose L2 norm grows: for L=2K and |A0|=32 nu K, the explicit
variation is amplified at t=1/(5nu K^2). It is a derivative of an actual
nonlinear NS family, not a prescribed strain or forced-Stokes surrogate.
Thus universal normal contraction with prefactor one in the uncorrected
mass norm is PROVED FALSE in the test class. No conclusion about arbitrary
whole-space singularities is inferred.

The same strain-containing test is repaired: a triangular Duhamel formula
bounds its normal propagator by (1+alpha) exp[-nu L^2(t-s)],
alpha=|A0|/(nu K), uniformly in the fine cutoff. A two-mode moving metric
with correction h(t)=(A0 K/sqrt(2)) t exp(-nu K^2 t) is explicitly coercive,
with constants depending only on alpha, and has an exact dissipative law.
The metric derivative is essential. This is neither a fixed universal
Lyapunov functional nor an assumed bounded inverse fundamental matrix.

**Next distinct action:** work on the full coupled three-dimensional normal
propagator and paired forcing/feedback, including B(error,coarse), resolved
errors, pressure projection and critical interscale weights. Derive the
first off-diagonal correction and prove its coercivity and accumulated
reconstruction cost from inputs. A moving metric or propagator defined via
an unknown future solution does not count without these quantitative bounds.
Individual finite transient bounds do not control their infinite interlevel
accumulation. RF3, RF4 and NS-R3 remain OPEN, not disproved.

Do not restart the defeated static C2 or uncorrected-contraction premises.
Do not drop the resonant or strain terms; do not extend the passive-sector
factorial proof by renaming its explicit shear budget an unknown NS norm.
Further passive special cases, another solver, or normal-form infrastructure
are not the primary task. The periodic benchmark and transient metric are
completed tests; the remaining mathematical work must address actual feedback.

Verdict: one static-closure branch and one contraction premise were cut by
proofs; causal reconstruction and bounded nonnormal tracking survived in
specified actual NS tests. No general critical estimate, new strict singularity
reduction or terminal breakthrough was obtained. Independent audit, whole-space
and FEEC transfer, and the kinetic/microscopic programme remain separately open.
