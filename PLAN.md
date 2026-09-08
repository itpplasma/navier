# Navier--Stokes: common-data realization after smooth-inverse and work-budget tests

This is the sole live task and status record. Owner-directed pivot: 2026-09-08.
Frozen integration input: `cb1faa311774f69a9e776483b695b6c0fe2c3681`; formal-core
update input: `fedb45a640ea8537aa90578f2cafda9adca01756`, merged on top of the
concurrent separated-pulse update `694be9648450dbb1528232e08d20ec07ace302d0`.
The complete preceding PLANs are preserved byte-for-byte in
`research/history/PLAN-before-unforced-exactification-2026-09-08.md` and
`research/history/PLAN-before-formal-core-2026-09-08.md`; their old
allocations are history, not a second active queue. All evidence files remain.
Current research integration input: `373bd3e0504df775434ad579607ded9481af624f`.
Its PLAN is preserved byte-for-byte in
`research/history/PLAN-before-smooth-trace-audit-2026-09-08.md`. Section 8,
including the concurrent kernel-replication and formal-core outcome, is
preserved byte-for-byte. The missing PLAN integration of `ececd70f` is
included below; none of its evidence is overwritten.

The objective is still to resolve the ORIGINAL UNFORCED whole-space problem:
prove NS-R3, or construct an admissible unforced counterexample. The new primary
experiment is to remove the dynamically effective forcing from a continuously
concentrating architecture. This is a research pivot, not a new theorem, an
endorsement of every step of an external manuscript, or a prize determination.

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: smooth-principal-inverse-after-connected-history-and-work-falsification-2026-09-08
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
terminal_status: not-proved
unforced_counterexample: not-constructed
complete_terminal_route: none-established
active_task: UE1-one-common-cauchy-trace-not-independent-pulse-traces
active_architecture: continuous-anisotropic-concentration-with-full-exterior
primary_direction: unforced-blowup-exactification-with-regularity-fallback
dominant_research_nut: specific-autonomous-coupled-history-with-one-schwartz-trace
source_forced_result: accepted-research-input-owner-checked-Lean
source_full_proof_audit: not-performed-by-this-research-run
source_unforced_implication: not-established
source_prize_outcome: not-determined-by-this-project
refinement_wave: reviewed-conditional-consumer-preserved
arbitrary_data_RFq_producer: not-produced
input_summable_critical_regeneration_cost: not-produced
blowup_event_extraction: not-produced
full_state_return_map: exact-partial-augmented-map-author-proof
regenerative_turnovers_certified: 0
unforced_singular_shadowing: not-proved
integrated_background_strain_cost: author-claim-scope-audit-pending
relative_endpoint_energy_automatic: refuted-by-mesoscopic-full-flow-family
legacy_discrete_cell_lane: retained-as-falsification-tool-not-default
separated_pulse_unforced_conversion: excluded-in-stated-full-state-class-author-proof
flat_principal_pulse_inverse: superalgebraic-loss-on-raw-flat-sources
autonomous_coupled_preparation: not-proved
smooth_principal_inverse: sharp-value-and-polynomial-parameter-bounds-on-regular-patches
clamped_trace_parameter_smoothness: false-with-explicit-one-sided-derivative-example
connected_two_pulse_inverse: no-polynomial-loss-even-with-free-initial-value-in-stated-class
normalized_angular_work_budget: refuted-by-globally-small-original-NS-solutions
nonzero_seed_work_budget: unbounded-on-Schwartz-compact-globally-small-family
new_results_audit: author-proofs-independent-mathematical-audit-pending
secondary_goal: MIC-R3
secondary_goal_status: separately-gated-and-not-primary
formal_work_this_run: route-invariant-core-authorized-2026-09-08
formal_core_task: FC0-FC7-see-section-8
source_lean_certificate: openai/NavierStokesAndEuler@8937a8f4-local-kernel-replication-standard-axioms-2026-09-08
formal_conditional_theorem: thm-conditional-proved-over-two-coarse-literature-axioms-2026-09-08
formal_core_landed: FC0-FC7-partial-plus-tao-split-ess-split-2026-09-08
forced_type_rigidity: author-theorem-A-assembled-plus-quantified-overlap-no-start-theorem-C
obstruction_independent_audit: 2026-09-08-different-tier-confirmed-with-repairs-no-start-subsumed-by-analyticity
source_lean_dependency: solution-only-pinned-toolchain-v4.34.0-rc2-authorized
run_status: positive-principal-repair-plus-full-PDE-work-falsification-no-terminal-resolution
public_release: false
```

## 1. Rigid terminal equation and unchanged positive consumer

For each fixed nu>0, the equation is

    partial_t u - nu Delta u + (u.grad)u + grad p = 0,
    div u = 0,  u(0)=d in S_sigma(R3;R3),
    p = sum_{i,j} R_i R_j(u_i u_j)

with the canonical whole-space pressure representative, not independently
prescribed local pressure. Positive resolution means global smoothness for
EVERY such datum. Negative resolution requires ONE nonzero real solenoidal
Schwartz datum, finite initial energy, and a genuine finite classical endpoint
for the unforced equation. Record viscosity dependence and any exact rescaling.
Periodic, forced, averaged, inviscid, truncated, and hyperdissipative results
remain discovery tools, not terminal substitutes.

The reviewed positive consumer remains available without modification. For
one fixed finite q>3 and the actual R3 projected-flow increments,

    (1/q) W_q,M' + nu D_q,M = Pi_q,M,
    integral_0^t Pi_q,M <= nu integral_0^t D_q,M + C(d,nu,H,N0,q)

for EVERY t<=H uniformly in M would give

    input-only producer -> RF-q -> RF-LQ-SYNTHESIS -> finite L^{3,q}
    -> RF-LOCAL-ID / Lorentz Fatou -> RF-LQ-CONTINUATION
    -> LOCAL / ENERGY / canonical pressure -> NS-R3.

No current result supplies that producer. The source manuscript's small
geometric variable q is unrelated to this Lorentz exponent. A negative route
instead needs an exact unforced solution and a proved singularity; it need not
pass through RF-q. Before pursuing any lemma, name its precise consumer in
one of these two complete chains.

## 1a. UE0/UE1 result: separated late pulses cannot start autonomously

Evidence: `research/evidence/2026-09-08-autonomous-pulse-obstruction.md`.
AUTHOR proof; independent audit pending. No terminal or graph promotion.
The source's complete nonzero-angular labels retain disjoint physical
spacetime supports, including all harmonics and curl/iteration corrections.
For any original-NS decomposition U=B+sum W_gamma with B axisymmetric,
M W_gamma=0, each W_gamma divergence-free, and those separated supports,
the ENTIRE equation gives the exact label identity

    (1/2) d||W_gamma||2^2/dt + nu ||grad W_gamma||2^2
       = -integral W_gamma . S(B) W_gamma + <P f,W_gamma>.

Hence a zero label stays zero on every compact classical unforced interval,
regardless of how large or dynamically coupled the axisymmetric background
is. The canonical pressure is retained in the full equation and cancels only
in this divergence-free pairing. This excludes ANY unforced exactification
preserving zero late-band initial values and exact label separation while
retaining nonzero late pulses, not merely an unchanged leading ansatz.
The source condition q>=T-t makes all sufficiently late labels initially
zero at any fixed t0<T. Taking a later initial time does not remove the issue.

A second, separately scoped theorem uses the actual principal pulse ODE.
For a homogeneous Gaussian pulse h and its cutoff psi, the exact raw-flat
source g=psi' h has zero-data response psi h, with order-one peak. At length
L comparable to ell^2 and Q=2^(-ell), every fixed derivative of g is flat in Q,
but the causal inverse norm grows at least exp(c L)/poly(L). No fixed
algebraic Q-loss bound extends to all raw-flat sources, even after finitely
many linear gauges in the decoupled amplitude system. This does NOT refute
the source's envelope-weighted inverse and is NOT a full-PDE inverse theorem.

The source's FORCED statement is not contradicted. The first unforced nut is
now actual autonomous nonaxisymmetric preparation: permit inherited overlap
or justify one continuous initial preload, retaining every resulting cross
term, pressure, mean, phase and viscous loss. Neither a fresh label reset
nor an axisymmetric mean correction can create an absent separated label.
Audit the prehistory of the ENTIRE countable pulse family before another
formal residual iteration. UE2--UE4 remain unproved. No critical budget,
blowup extraction, positive regenerative turnover, or recurrent set follows.

## 1b. Integrated predecessor results: what the last push actually proves

Evidence retained from `ececd70f`:
`research/evidence/2026-09-08-mixed-trace-principal-inverse.md`,
`research/evidence/2026-09-08-angular-preparation-obstruction.md`, and
`research/evidence/2026-09-08-unforced-support-and-pulse-audit.md`.
These remain AUTHOR proofs, not independently audited full-PDE exactification.

The principal system admits an O(sqrt(L)) mixed-trace inverse at value level,
uniform over all nonzero harmonics, with O(m^-2) control at high harmonics.
The exact scalar tail repair (1-psi)h cancels a seed without deleting its pulse
when the initial trace is free. This is not a causal zero-data inverse and
not one common Cauchy realization. The source's cutoff support identities are
lost when the tails are filled; their new interactions must be retained.

Positive-time spatial analyticity excludes an unchanged compactly supported
unforced snapshot or exact open z-independent/axisymmetric patches of the
stated types. Nonzero analytic leakage must be allowed. The angular preparation
inequality retains the whole exterior and exact nonlinear supply. It excludes
homogeneous high-angular-frequency preloads confined to a shrinking column;
otherwise it requires mostly exterior prehistory or large ENERGY-NORMALIZED
nonlinear work. That last quantity is not a physical-energy or critical budget.

## 1c. New positive inverse and a complete connected-history falsification

Evidence: `research/evidence/2026-09-08-smooth-pulse-inverse-and-history.md`.
AUTHOR proofs; independent audit pending. These are principal operators only.

For D_a=partial_v-a on [0,L], a'<=-kappa/L, solve

    (-partial_v^2+a^2-a')y=f, y(0)=y(L)=0,
    x=(-partial_v-a)y.

This gives the minimum-L2-norm right inverse, with integral x h_a=0,
where D_a h_a=0. Its L2 bound is sqrt(L/kappa), its L-infinity bound is
3 sqrt(pi L/(2kappa)), and sqrt(L) is sharp. The fixed Dirichlet problem
has smooth slow-parameter dependence and polynomial fixed-order derivative
bounds, even when the root of a crosses an endpoint. The old clamped trace
actually has a derivative jump for a_theta=theta-v/L, f=1. This repairs an
extension that the predecessor explicitly had not claimed.

The replacement extends to the entire nonzero-harmonic principal family,
with regular-patch parameter derivatives and the exact principal pressure.
It does not supply uniform control across singular collars, transverse/mean
PDE equations, or compatibility between independent pulse intervals.

Following it through gives a sharp negative result. Put

    h_L(v)=exp[-L cos^2(2pi v/L)], a_L=h_L'/h_L,
    g_L=(1/L)chi'(v/L)h_L,

where chi rises from zero to one in the valley between the two peaks.
The source and every fixed derivative are O(poly(L)exp(-L/2)), but every
solution of x'-a_L x=g_L, with ANY initial value, has supremum at least 1/2:
its two peak values are c and c+1. Thus a small independent pulse inverse
does NOT compose into a small connected-history inverse, even after freeing
the initial trace. This is not a claim that the actual source's multi-channel
NS history has that scalar obstruction; it proves that a composition shortcut
requires an additional theorem, not another formal order.

## 1d. New full-PDE falsifier: normalized angular work can be infinite in small flow

Evidence: `research/evidence/2026-09-08-normalized-work-falsification.md`.
AUTHOR proofs; independent audit pending. ORIGINAL unforced R3 NS, canonical
pressure, fixed positive viscosity, real Schwartz data, all modes retained.

Let F=exp(-|x|^2), psi=x1 F, d=(partial_2 psi,-partial_1 psi,0).
The parent has only vector rotation modes +/-1. For c=(d.grad)d,

    [curl c]_3=8 x1 x2 F^2,
    b=-Pi_2 P c != 0.

For arbitrarily small epsilon, the actual flow from epsilon d is globally
regular and uniformly small in L3, hence finite L^{3,q}. The whole PDE gives

    v_2(t)=epsilon^2 t b+O(t^2), G_2(t)=epsilon^2 b+O(t),
    [Re<G_2,v_2>]_+/||v_2||2^2 = 1/t+O(1).

Consequently the predecessor's W_2^+(t) is INFINITE for small positive t.
A seeded Schwartz-compact family, using the real part of
-Pi_2 curl curl c, has v_2 nonzero throughout a common interval and
W_2^+(t_*)>=log(1/delta)-C while every flow is uniformly globally small.
The global claim follows from the ordinary small-data energy/enstrophy
bootstrap, not a numerical trajectory or a merely formal time coefficient.

This does not retract the exact angular occupation inequality or its
homogeneous-preload corollaries. It kills promoting raw normalized work into
a finite arbitrary-input budget, including a locally bounded budget after
excluding exactly zero seeds. A genuinely large-amplitude event cost might
avoid this counterexample, but extraction and a finite budget would still
need proof. Do not infer critical growth from a logarithmic newborn gain.

## 1b. Forced-type rigidity and the independent obstruction audit (2026-09-08)

Evidence: `research/evidence/2026-09-08-forced-type-rigidity.md` (AUTHOR,
79 exact checks in `research/check_forced_type_rigidity.py`) and
`research/evidence/2026-09-08-obstruction-audit.md` (INDEPENDENT AUDIT,
different model tier, of the three obstruction notes of Sections 1a and
the support/pulse audit). No graph promotion.

Theorem A assembles the compact-support, exact-patch and separated-label
obstructions into one rigidity statement whose hypothesis class contains
[OA-LEAN]'s `CandidateProperties` verbatim: no unforced finite-energy
whole-space flow lies in that class unless it vanishes. The audit CONFIRMS
the analyticity lemma (with two hypothesis repairs: `s>3/2`, the uniqueness
class), the exact label energy identity, and the angular inequality, and
finds Corollary 3 STRONGER than stated: the actual global `P f` of the
localized source construction cannot vanish on ANY open time interval. It
also finds that the separated-label no-start conclusion is SUBSUMED by
analyticity (three lines), that the flat-seed "superalgebraic inverse cost"
is an unweighted-norm artifact with no obstructive content, and that the
angular exclusion reaches only the `q ~ tau` core sub-family.

The new component, Theorem C, replaces exact label separation by a
cross-coupling parameter `kappa` and proves a Groenwall bound
`A(t) <= e^{int m} A(s) + int e^{int m}(kappa+phi)`, `m = b + sigma - lambda`,
with every constant named. On net-damped windows the integrated seeding
must exceed the produced amplitude; on net-growth windows the required
seeding is only `a_1 e^{-Gamma}/(t_1-s)` with `Gamma ~ c l^2/4` for [OA]'s
pulses. CONSEQUENCE: no `L^2` identity of this shape can exclude
overlap-driven birth; a future exclusion must control the sign or
realizability of an exponentially small overlap, not its size.

Net verdict of both notes: the obstructions exclude every relabelling
shortcut (terminal slab, compact snapshot, exact patches, exact separation
with zero late data, zero-trace cancellation, trapped preload, and now U-8:
overlap confined to a net-damped window with `int kappa < a_1`). They do NOT
exclude removal of [OA]'s force by an overlapping, continuously preloaded,
analytically leaking autonomous cascade with a single Schwartz datum
realizing all pulse traces. That free-trace realization is the first
missing theorem of UE1; UE2--UE4 are unchanged behind it.

## 2. Primary-source gate: what was actually inspected

[OA] OpenAI, *Finite Time Blowup for Navier--Stokes*, accessed 2026-09-08
at the owner's supplied URL. The earlier planning record counted 165 pages;
the current retrieval reports 166 physical pages. This is a metadata record,
not an assertion that the theorem or its proof changed:

https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

[CMI] Charles L. Fefferman, official problem statement, alternatives A--D:

https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf

[OA, Theorem 1.1, p.1] claims bounded-energy velocity blowup from zero datum
with a smooth compactly supported force, for every positive viscosity, and
claims C/D. [CMI, p.2] states A with zero force and permits forcing in C.
The owner has checked the Lean proof and instructs this research to accept
the forced theorem. The concurrent kernel-replication record in Section 8
is preserved. Do not spend this lane re-litigating that input. Neither an
unforced implication nor a prize decision is inferred from it. Exact imported
coefficients and uniformity conditions still have to be checked at their source.

The source's local target is a residual flat at the singularity, not zero
[OA, Theorem 3.1(iii), (3.4), pp.14--16]. Its pulse description explicitly uses
small external seeds [Section 2.2, p.5]. The audit checkpoints are the residual
split and improvement [Propositions 9.3, 9.6], summation [Proposition 9.9], and
space/time localization and force extension [Section 10].

Inspection this update covered the main statements, physical description,
relevant outline, and those residual/cutoff passages; selected pages were
visually checked. It was NOT a line-by-line proof audit or independent review.
Before importing a lemma, inspect its exact hypotheses and proof, including
uniformity and all derivative/cutoff costs. Record any later source version
and correction. Store original notes and source metadata, not a vendored PDF.

## 3. One dominant mathematical challenge

Determine whether the anisotropic concentrating core and its coupled exterior
can arise from ONE unforced Schwartz Cauchy evolution, rather than repeated
external pulse seeding or a residual later declared to be a force.

The correct target is ZERO SOLENOIDAL RESIDUAL, with pressure reconstructed.
For a globally defined divergence-free trial field U, set

    F_U = partial_t U - nu Delta U + P div(U tensor U).

This equals P R(U,Phi) for any trial pressure Phi. A pure-gradient residual can
be absorbed into pressure; a nonzero P R cannot. Do not impose the stronger,
artificial requirement of keeping the source's chosen pressure unchanged.
For a general forced trial, pressure satisfies

    -Delta Phi = partial_i partial_j(U_i U_j) - div f.

Thus compactly supported trial pressure or the unforced double-Riesz formula
cannot simply be inherited from a forced construction. The latter must be
proved for the FINAL unforced flow, including its remote exterior.

Seek a real divergence-free correction w satisfying on the WHOLE interval
[t0,T) and ultimately the WHOLE space

    L_U w + P div(w tensor w) = -F_U,
    L_U w = partial_t w - nu Delta w
            + P div(U tensor w + w tensor U),
    d = U(t0) + w(t0) in S_sigma(R3;R3),  d != 0.

After a time translation, d is the initial datum at time zero. A local field
is not an input to the whole-space Leray projector until its global extension
and the associated pressure/error terms are specified.

The correction must preserve an explicit blowup lower bound, not merely
exist in an unnamed topology. For example, at specified points x(t), prove

    |U(x(t),t)| >= c (T-t)^(-A),
    |w(x(t),t)| <= (c/2) (T-t)^(-A),  A>0,

together with classical smoothness before T, initial trace, finite energy,
ordinary positive viscosity, and the canonical pressure. Other precise
singularity diagnostics are allowed. No such correction is currently proved.

## 4. Ordered theorem-sized tasks and decision gates

### UE0 -- Identify the first indispensable projected forcing

The separated-support conversion has been excluded in Section 1a. For any
new architecture, first audit whether the actual global P f vanishes on ANY terminal time slab.
If it does, taking a smooth Schwartz time slice at its start would already
supply an unforced segment; prove all its hypotheses rather than assuming it.
Flatness at one point, smallness, or compact time support does NOT imply such
a slab. Zero datum with zero force gives the zero solution and is not a route.

Track the exact residual through core profiles, core/exterior matching,
pulse preparation, transport and damping, mean and moment corrections,
summation cutoffs, spatial localization, and the initial time cutoff. For
each term specify its origin, support, solenoidal projection, derivative
bounds, scale dependence, and whether it is removed or only made flat.
Include every mixed product and newly generated mode. Audit the first
unsupported source inference before relying on its suffix; preserve valid
parts if an error is found.

Required output: an exact forcing/compatibility identity and the FIRST
unremoved P f term with a mathematical removal target. A catalogue alone is
not completion. Consumer: supplies the source and compatibility conditions
for UE1. Do not postpone pulse seeding until after a full reconstruction.

### UE1 -- Autonomous pulse preparation and a uniform linear inverse

Do not retain the now-excluded exact separation with zero late-label data.
Do not apply the causal envelope inverse to raw-flat errors with a polynomial
loss. The smooth principal inverse in Section 1c repairs the regular-fiber
parameter issue; it does not repair connected histories. The immediate task
is ONE COMPATIBLE ARRAY arising from ONE datum, not arbitrary independent
control of every trace. Retain the entire preparation history and analytic
leakage, or alter the profile/geometry if those requirements make it impossible.
Test whether the required pulses can be generated from a single admissible
initial perturbation, carrying their phases, polarizations, tails and all
feedback continuously, with no time-localized external starts or stops.
Compute the preparation cost under the actual viscous evolution. Formal
backward heat evolution is not an admissible initialization argument.

Derive a right inverse for the constrained L_U problem, or prove an exact
obstruction in a precisely specified class. Account for neutral/unstable
modes, pressure, moments, drift, and any modulation parameters. Allow changes
to the source profiles and geometry when necessary; do not insist that its
fixed inverse or support conventions remain optimal for zero forcing.

Specify spaces X,Y and prove a bound for the actual residual and inverse
that is uniform as T'<T approaches T. X must control the blowup-preserving
error, all coupled exterior terms and the regularity needed for the equation.
A bound depending on an uncontrolled future norm, an unestimated
exp(integral ||grad U||_infinity), or a cutoff-dependent inverse is not this
result. Finite-dimensional solvability or a source-only cycle is not enough.

First experiment: one complete pulse INCLUDING its preparation and cutoff
remainders, then its actual inherited output. Immediately extend a successful
estimate to the entire countable pulse family; do not stop at a finite birth.
Consumer: the uniform inverse and residual estimate feed UE2.

### UE2 -- Cancel the complete residual, not only its asymptotic series

Close the nonlinear correction equation from Section 3 by contraction,
Nash--Moser, a graph transform, validated PDE estimates, or another justified
method. Prove all tame or nonlinear estimates, compatibility conditions,
convergence, and derivative bounds needed for an exact solution.

All-orders decay, Borel realization, a flat remainder, or a formal expansion
is NOT zero forcing. A nonzero function can be flat at T. Quantify the actual
remainder relative to the singular propagator, including exponential versus
algebraic scales; do not infer stability from flatness alone. Keep summation
and support-commutator errors in the equation until they vanish exactly or
are absorbed by a proved convergent correction.

Output: a genuine exact local singular solution with a specified stability
class, or a uniform full-space correction theorem. All inherited exterior,
reverse channels, viscosity and pressure remain. Consumer: UE3 supplies any
missing whole-space Cauchy realization; UE4 certifies the terminal endpoint.

### UE3 -- Whole-space unforced embedding from nonzero Schwartz data

Solve this together with UE1/UE2 whenever the pressure or inverse is nonlocal.
Replace cutoff localization by an exact coupled exterior/inner matching
argument, or include EVERY localization defect in the global correction.
Do not trade local forcing for remote forcing or imposed boundary stresses.
A smooth externally driven exterior is not an unforced embedding.

Produce one specified t0<T and one d in S_sigma, not a sequence of different
data for successively longer finite intervals. Evolve forward at the fixed
positive viscosity; do not assert a backward parabolic gluing theorem.
Check the global pressure, energy identity, initial trace, smoothness through
t0 and all tails. Schwartz is required at the initial time; do not additionally
assume permanent compact support or permanent Schwartz decay of the flow.
Consumer: an exact full-space solution on [t0,T) with the UE2 lower bound.
The compact-support comparison adapter recorded in Section 8 is not by itself
sufficient for this noncompact unforced candidate. Use the full classical
uniqueness interface or prove the required noncompact adapter; do not reimpose
positive-time compact support merely to fit an available formal theorem.

### UE4 -- Terminal verification

Show the constructed field is the classical solution for that one datum,
that its maximal smooth lifespan is finite, and that a precise norm diverges
at the endpoint while energy remains admissible. Check the entire pressure
relation and ordinary viscosity. Rescale viscosity only with exact formulas.
This would refute NS-R3 by an UNFORCED counterexample, not merely reproduce
[OA]'s forced statement. Independent adversarial review is required before
canonical promotion. No numerical orbit or truncated certificate substitutes
for the continuum proof.

### UEF -- Sharp failure and positive fallback

If a gate fails, prove the strongest precise obstruction to THAT proposed
unforced conversion. A requirement for forcing in one ansatz does not prove
unforced global regularity, and a failure of one proof does not refute [OA].
Pivot to altered profiles, an autonomous exterior pump, or another complete
route when warranted. Do not assume exactification is possible or easier.

A positive use of a discovered forcing/strain cost must supply both extraction
from every hypothetical unforced blowup and an input-summable critical budget,
then feed Section 1 or prove a complete replacement continuation chain.
No adaptive-background reset is free: retain its comparison-change defect.
Do not use W_n^+ as the required finite resource: Section 1d refutes that on
arbitrarily small global unforced solutions. An amended cost must survive
both the zero-seed and Schwartz-compact nonzero-seed tests and still extract
all required concentrating events. Introducing another uncontrolled normalized
source does not meet the positive consumer.
Two serious returns to the same uncontrolled quantity require a different
mechanism, not a renamed norm or another formal correction order.

## 5. Preserve prior mathematics as tests, not as mandatory architecture

All existing proofs, counterexamples, checkers and audit qualifications remain.
The exact old scopes and reported checks are in the archived PLAN, not erased
or promoted. The following source files are the principal active falsifiers:

* `research/evidence/2026-09-08-narrow-packet-escape.md` and
  `research/evidence/2026-09-08-full-duration-mixing-cascade.md`:
  do not assume a perturbative critical exterior; spectral transfer alone
  is not concentrating regeneration.
* `research/evidence/2026-09-08-source-cycles-and-newborn-efficiency.md`,
  `research/evidence/2026-09-08-exact-circuit-obstructions.md`, and
  `research/evidence/2026-09-08-phase-locked-full-ring.md`:
  source composition is not the actual flow; retain all interaction trees,
  side modes, phase-compatible sectors and reverse feedback.
* `research/evidence/2026-09-08-convex-cone-linearity.md` and
  `research/evidence/2026-09-08-fourier-cone-obstruction.md`:
  independently selectable invariant Fourier cones are not a generic escape.
  A realizable stress-covariance cone is a different object; compare premises
  before applying the obstruction.
* `research/evidence/2026-09-08-remote-pressure-control.md` and
  `research/evidence/2026-09-08-tao-packet-audit-and-repair.md`:
  no instantaneous restoring pressure sign or averaging-invariant shortcut.
  Identify the exact original Leray/local-energy property used.
* `research/evidence/2026-09-08-full-state-vorticity-return.md`,
  `research/evidence/2026-09-08-no-atom-regenerative-blocks.md`,
  `research/evidence/2026-09-08-relative-background-return.md`, and
  `research/evidence/2026-09-08-integrated-background-strain-cost.md`:
  scoped author return/cost claims, not arbitrary-data extraction. Check every
  written hypothesis before use. In particular, growth of a_n K_n^2 alone
  does not imply shrinking spatial scales. A forced comparison introduces
  additional work terms; it is not an unforced pair for the old identities.
* `research/evidence/2026-09-08-retained-bulk-full-flow.md` and
  `research/evidence/2026-09-08-mesoscopic-relative-energy-obstruction.md`:
  full or fixed-background normalized L2 divergence is not automatically a
  required critical cost. Do not hide this failure in a new background choice.

Before applying Type-I/no-atom arguments, derive the ACTUAL gradient and
clock bounds for the anisotropic full field. Dimensional resemblance is not
membership in the theorem's class. A vanishing-energy core or essential
exterior is an admissible candidate, not evidence of blowup by itself.

The six-carrier benchmark, periodic ring and discrete K-to-2K return search
are now secondary diagnostics. Continuous anisotropic concentration need not
fit those coordinates. Their failure is neither evidence against all blowup
nor a reason to discard valid positive estimates. Full-state retention remains
mandatory even though the discrete return map is no longer the default route.

## 6. Execution, source discipline and validation

Read AGENTS, this PLAN, the canonical and refinement proof interfaces, and the
precise source passages required by the current gate. Prioritize UE0/UE1, with
whole-space pressure/matching checked from the beginning. Use distinct workers
only when genuinely available; independent review cannot be self-review.
Computations must test the original residual, compatibility, stability or an
actual continuum remainder. No broad finite-mode optimization campaign is
required by this pivot.

Keep the existing theorem/audit/formal statuses. Accept the forced theorem
as instructed by the owner; an unforced implication still requires its own
proof. Distinguish source verification, author proof of our new statements,
independent mathematical review, finite exact checking and formal coverage.
No prize, priority, journal, publication or outside-contact decision is made
here. No additional Lean build was run by the present research controller.

For every subsequent mathematical result: refresh main, preserve concurrent
work, record the precise theorem and first remaining gap, update this PLAN,
run applicable checks, and commit/push ordinary fast-forward changes. Never
force-push. Keep third-party PDFs and generated artifacts outside the repo.

Historical planning-only validation at fedb45a6 changed PLAN and its history
snapshot; its source tree was restored from the private CI artifact at
334ff7c8 plus the added cb1faa31 evidence and checked against tree
`bf1cbb722e0b338f2b5853c06c1135cf33d19bf9`.
The CURRENT mathematical integration instead restores the full ececd70f CI
source tree and preserves the subsequent 373bd3e0 PLAN changes; the refreshed
full source tree matches `cbbaecc114cfde96fc3cc8c7590b79521e451620`.
New evidence/checker and PLAN changes do not promote any canonical graph,
manuscript or Lean statement. Run

    python3 research/verify.py --research-only
    git diff --check
    git diff --cached --check

on the complete source checkout before pushing. Existing read-only GitHub CI
also triggers on PLAN changes and runs exact checks plus full-checkout
verification. Report observed outcomes, not anticipated success. These checks
do not audit [OA], prove exactification, or certify a regenerative turnover.

The source audit follow-through passed 86 finite exact assertions in
`research/check_autonomous_pulse_obstruction.py`. These concern algebra, not
continuum verification or independent review. Current full-checkout checks
are recorded with the integration commit; the earlier planning-only check
record above remains historical provenance.

The smooth-inverse/work follow-through passed all 75 finite exact assertions
in `research/check_smooth_inverse_and_work.py`. All 19 predecessor checkers
were rerun successfully, including the three older closed-feedback, resonant-
memory and Tao-packet checks outside the current CI list. One combined batch
timed out before the final ring result; the ring order-8 checker was rerun
separately and returned success. Full-checkout research-only verification,
Python syntax, link checks, archive identity, concurrent Section 8 identity,
and staged/unstaged whitespace checks pass. These are algebra/structure
checks, not continuum validation, an independent audit, or a new Lean proof.

## 7. Next handoff: one dominant nut

    Construct a specific continuously coupled concentrating pulse/exterior
    history whose ENTIRE countable trace array is realized by one nonzero
    Schwartz Cauchy datum for original unforced R3 NS, with a uniform
    full-PDE correction estimate that preserves its singular amplitude.

Accept [OA]'s forced result as the input. The first missing theorem is common
Cauchy-trace realization, not another independent principal inverse. Work with
one connected history, including preparation, analytic leakage, mean/transverse
transport, actual pressure, and every newly generated cross-label interaction.
Only one compatible orbit is needed; a right inverse for arbitrary trace arrays
is not required. A finite list of controls or dense trace range is insufficient
unless the common initial-data norms and all nonlinear errors are uniform and
summable through the singular endpoint.

Use the smooth minimum-norm fiber inverse as a local tool. Test any proposed
joining estimate against Section 1c's connected two-peak example. If actual
cross-mode coupling supplies compatibility, calculate it rather than resetting
the next pulse. If common-data preparation succeeds, proceed immediately to
the full nonlinear inverse, whole-space realization and endpoint verification
UE2--UE4. A failed ansatz is not a proof of regularity; a genuinely better
complete route may replace this one.

The alternative positive route must first replace the now-falsified raw angular
work budget by an input-summable critical cost and prove event extraction, then
feed Section 1. No new theorem here completes either terminal chain. Certified
regenerative turnovers remain zero; no full-state recurrent set is constructed.

## 8. Route-invariant formal core (Phase I / Phase II), authorized 2026-09-08

Owner instruction of 2026-09-08: fix what Lean must contain NO MATTER HOW the
remaining paper proof develops, and reach it in parallel with the research
gates above. Lean work lives in `itpplasma/navier-formal`; its live status is
this section plus `navier-formal/docs/verification-status.md`. Phase I means
manuscript-owned steps proved over precisely stated, source-recorded
literature axioms; Phase II means every such axiom discharged from Mathlib.
The phase status strings above are unchanged by this section.

### 8.1 Source Lean certificate: what was inspected, what is permitted

[OA-LEAN] `https://github.com/openai/NavierStokesAndEuler`, commit
`8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`, Apache-2.0, Lean `v4.34.0-rc2`,
Mathlib `85e3a25e006c35636f0e53b0e9296caca2685bc0`, inspected 2026-09-08.
It advertises `NavierStokes.Comparator.navier_stokes_breakdown_R3` (C) and
`navier_stokes_breakdown_periodic` (D) through a Comparator challenge adapted
from Formal Conjectures (`FormalConjectures/Millenium/NavierStokes.lean` at
`8bf45ed7`), self-reporting axioms `propext, Classical.choice, Quot.sound`,
review status `self-assessed`. The NavierStokes library is 580 modules,
about 20 MB of Lean; the whole-space comparison closure
(`NavierStokes.R3.WholeSpaceUniqueness`) is 67 modules, about 0.7 MB.
Observed 2026-09-08: a local `lake build NavierStokes` of the pinned commit
(32 cores, about 20 minutes, zero errors) printed
`[propext, Classical.choice, Quot.sound]` for both advertised breakdown
theorems, recorded in `navier-formal/docs/verification-status.md`. This is a
kernel replication of the axiom claim, not a Comparator/NanoDa replay, not a
statement-faithfulness certification beyond
`navier-formal/docs/external-openai-audit.md`, and not a mathematical review.
The adapter lane also printed the standard three axioms for the imported
whole-space comparison, Sobolev and pressure-recovery theorems.

Permitted use: a SOLUTION-ONLY pinned dependency of `navier-formal`
(Palomar: `Challenge.lean` imports only Mathlib; proof dependencies may be any
publicly readable pinned Git repository; permitted axioms unchanged). This
required bumping `navier-formal` to the same toolchain and Mathlib pin.
Only modules under `NavierFormal/External/` may import [OA-LEAN]; every
imported declaration gets a statement-faithfulness row and an axiom report.
Importing (C) does not import an unforced theorem; its research use is the
forced-insensitivity falsifier in
`research/evidence/2026-09-08-forced-insensitivity-falsifier.md` (author
evidence, independent audit pending): any producer whose proof survives a
smooth compactly supported force from zero datum is refuted by (C).

Related public certificates, inspected only at the README/manifest level:
`tristanbuckmaster/fluid_lean` (Euler and Boussinesq forced blowup, Lean
`v4.32.2`, Palomar layout, no top-level licence file seen); they are not
dependencies. Statements of their `vendor/cm24-r2` transport/uniqueness
library may be consulted as designs, never copied without licence.

### 8.2 The invariant core: theorem-sized formal tasks

Every item below is consumed by BOTH complete chains of Section 1: the
positive chain needs it to identify the maximal branch and close at the
endpoint; a negative route needs it to prove that a constructed field is THE
solution of its Schwartz datum, has finite lifespan, and diverges. Items are
ordered by consumer distance from the terminal statements.

FC0 -- Statement alignment. A Mathlib-only reference module for Fefferman's
(A) and (C) in the Formal Conjectures form (Apache-2.0 header retained), and
proved bridges: `NavierFormal.ClayAlternativeA_all` versus the reference (A)
(curried versus uncurried fields, `derivWithin` at `t=0`, energy as a bound),
and Schwartz data versus Fefferman's decay condition (4) in both directions.
Consumer: any terminal Lean statement of this project must be comparable with
the community reference used by [OA-LEAN]. Phase II.

FC1 -- Local theory interface (`prop:localtheory`, Tao Theorem 5.4 with
Corollaries 4.3, 5.8). Phase I: an axiom module with the exact statement in
the project's classical class (existence of a maximal branch, uniqueness
among classical solutions with the regularity package, one-sided smoothness
at `t=0`, the `H^1` blow-up alternative, viscosity scaling) and a source
record. Consumer: `thm:continuation`, `thm:conditional`, and UE4's
identification of a constructed field with the branch. Phase II: class F,
to be scheduled after FC5; do not start it before the class bridges exist.

FC2 -- Endpoint interface (`thm:ess`, Escauriaza--Seregin--Sverak Theorem 1.3;
GKP corroboration only). Phase I: axiom module with the verbatim mixed-norm
hypothesis `L^\infty_t L^3_x` and the conclusion `L^5`, plus the manuscript's
`lem:leray-hopf`, `lem:l3-to-l5`, `lem:serrin-enstrophy` bridges proved or
listed as open. Consumer: `thm:continuation`. Phase II is route-dependent
(positive route only) and is NOT part of the invariant core.

FC3 -- Conditional theorem `thm:conditional` in Lean from FC1 and FC2 axioms:
`CriticalHypothesis -> ClayAlternativeA_all`. This is the first end-to-end
Phase I theorem of the project; record its axiom report (exactly the FC1/FC2
axioms plus the three standard ones). Consumer: Section 1 positive chain.

FC4 -- Energy identity `prop:energy` and the PDE half of `prop:scaling`.
Phase II: derivative form and integrated form for the classical class with
explicit integrability hypotheses, then the bridge from the regularity
package to those hypotheses; the dilation `(u_lambda,p_lambda)` is a
classical solution. Consumer: every energy or scaling statement in either
chain, and UE4's finite-energy clause.

FC5 -- Class bridges. Phase II: bounded gradient implies global Lipschitz
(feeds the Rademacher lemmas of `prop:pressure`); regularity package plus
boundedness implies every `L^1` hypothesis used by the integration-by-parts
lemmas; Frobenius/operator norm bookkeeping is closed. Consumer: FC4, FC6.

FC6 -- Uniqueness and comparison on the whole space. Phase I via
[OA-LEAN] `NavierStokesR3.WholeSpaceUniqueness.classical_uniqueness_on_Icc`
(compactly supported smooth reference versus any smooth finite-energy
competitor at viscosity 1), adapted to the project's classical class with the
viscosity normalization `eq:nu-normalization`. Record the exact obstacle: the
reference must be compactly supported at every time, which an unforced
Schwartz-data flow is not; so this covers the [OA]-type candidate of UE3/UE4
but not the identification of the maximal branch, which stays with FC1.
Phase II: the imported theorem is already Mathlib-only if the replication
axiom report confirms it. Consumer: UE4; positive-route class identification
remains FC1.

FC7 -- Blow-up statement surface. Definitions of maximal lifespan, unbounded
speed, `L^3` divergence, and the unforced counterexample statement
(nonzero Schwartz datum, classical on `[0,T)`, no global smooth bounded-energy
solution), with the trivial theorem that it refutes `ClayAlternativeA_all`.
Consumer: UE4 terminal statement, Comparator comparability with FC0.

Remaining `prop:pressure`, `prop:enstrophy`, `prop:lowpressure` and the
quotient-section results are positive-route Phase II work; they continue as
supporting lemmas but are not in the invariant core. `sec:quotient` stays
paper only.

### 8.2a Observed outcome of the first formal-core run (2026-09-08)

Eleven Sonnet lanes on disjoint files; nine landed, one landed truncated,
one discarded. `navier-formal` main now builds at the new pin with 130 new
checked declarations. Landed: FC0 (`ClayReference`, `SchwartzDecay`: (A) is
proved equivalent to the Formal Conjectures shape, Schwartz data equivalent
to Fefferman's condition (4)); FC1/FC2 as COARSE axioms
(`Literature.localTheory`, `Literature.endpointContinuation`, each folding
manuscript-owned bridges into the cited theorem, with the deviations listed
in their docstrings); FC3 (`conditional_clay_A : CriticalHypothesis ->
ClayAlternativeA_all`, axioms exactly those two plus the standard three);
FC4 (`IsClassicalSolution.dilate`; `EnergyIdentity.energy_identity` under an
explicit hypothesis bundle; the enstrophy identity under explicit
hypotheses, cubic inequality NOT landed); FC5 (`ClassBridges`: bounded
derivatives, Lipschitz, all IBP integrability facts at fixed time); FC6
(`External.classical_uniqueness_of_compact_support(_nu)` over the imported
theorem, needing closed-slab smoothness and a compactly supported
reference); FC7 (`Blowup`: `UnforcedCounterexample` refutes
`ClayAlternativeA_all`; viscosity rescaling of the counterexample statement
incomplete). Not landed: `‖D²u‖₂ = ‖Δu‖₂` and the gradient interpolation.

Second run, same day (navier-formal, 34 more checked declarations):
`Literature.taoLocalTheory` is now a pure Tao interface, and
`lem:global-smooth` plus the energy bound are PROVED from it
(`localTheory_of_tao`); `conditional_clay_A_of_tao` depends exactly on
`taoLocalTheory` and the coarse `endpointContinuation`. `Literature.essL3ToL5`
(ESS Theorem 1.3 plus `lem:leray-hopf`) is the purer endpoint axiom;
`lem:serrin-enstrophy` is proved with the manuscript's constant under explicit
hypotheses, and `endpointContinuation_of_ess` derives the coarse axiom from
it under four explicit analytic hypotheses, so the coarse axiom stays the
consumer until those are discharged. The cubic inequality `eq:enstrophy`,
the viscosity rescaling of `UnforcedCounterexample` (both directions), and
three of five `EnergyHypotheses` fields are proved. Still not landed:
`‖D²u‖₂ = ‖Δu‖₂` (two failed attempts), the gradient interpolation, the
`L²` difference-quotient limit `lem:R-consequences`(a) from the package
alone. Nothing here changes any research claim status.

### 8.3 Execution rules for the formal core

Distinct workers own disjoint new files; the controller integrates, runs the
single `lake build`, records `#print axioms` for every new declaration in
`verification-status.md`, and audits statement fidelity row by row in
`paper-lean-specification.md`. A zero-sorry file with a weaker statement is
not the manuscript result. No formal step promotes a research claim in
`docs/proof-graph.yaml`; `machine_checked` entries require the axiom report
and the fidelity row. Report observed build and axiom outcomes only.
