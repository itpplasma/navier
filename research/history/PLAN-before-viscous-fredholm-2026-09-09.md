# Navier--Stokes: common-data realization after the pressure-curvature barrier

This is the sole live task/status record. NS-R3 remains NOT PROVED; no
unforced counterexample has been constructed. Current mathematical input:
`68cf0c6cea4aab2689ad8be1219f14a1764938ff`.
The complete preceding PLAN is preserved byte-for-byte in
`research/history/PLAN-before-pressure-curvature-2026-09-09.md`.
Its Section 8 is also retained verbatim below as the live formal-core record.
All earlier evidence and review qualifications remain; history is not a
second active queue. Manuscripts now live in this repository's `paper/`.

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: global-pressure-budget-transfer-exclusion-2026-09-09
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: integrated-in-navier-paper-directory
legacy_paper_repo: archived-private-2026-09-09
external_deps: permitted-if-no-axioms-beyond-mathlib
terminal_status: not-proved
unforced_counterexample: not-constructed
complete_terminal_route: none-established
active_task: UE1-viscosity-specific-common-Cauchy-trace-inverse
active_architecture: continuous-anisotropic-concentration-with-full-exterior
primary_direction: unforced-blowup-exactification-with-regularity-fallback
dominant_research_nut: common-trace-and-viscous-inverse-tolerating-unbounded-positive-pressure-curvature
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
global_upper_pressure_budget_transfer: excluded-by-full-original-NS-continuation-author-proof
positive_pressure_curvature_clock: complete-author-proof-independent-audit-pending
full_viscous_displacement_action: exact-author-identity
viscous_time_only_semiboundedness: equivalent-to-zero-finite-energy-background-author-proof
critical_curvature_hardy_repair: interior-Euler-form-only-not-a-viscous-inverse
run_status: pressure-budget-and-displacement-coercivity-transfers-excluded-no-terminal-resolution
public_release: true
repository_visibility: {navier: public, navier-formal: public, navier-paper: private}
external_contributions: pull-requests-welcome-owner-review-required
```

## 1. Rigid terminal equation and the existing positive consumer

For fixed nu>0, original unforced incompressible NS on R3 is

    u_t-nu Delta u+P div(u tensor u)=0, div u=0,
    u(0)=d in S_sigma(R3;R3), p=sum R_i R_j(u_i u_j).

A positive resolution concerns EVERY such datum. A negative resolution
requires ONE finite-energy Schwartz datum and a genuine finite endpoint
of its classical solution at the fixed positive viscosity. Forced, inviscid,
periodic, averaged and restricted models are not terminal substitutes.
Schwartz is an initial condition, not a claim about permanent spatial decay.

For the actual whole-space projected-flow increments and one fixed finite
q>3, the reviewed RF-q chain remains

    (1/q) W_q,M' + nu D_q,M = Pi_q,M,
    integral_0^t Pi_q,M <= nu integral_0^t D_q,M+C(d,nu,H,N0,q)
    -> RF-q -> RF-LQ-SYNTHESIS -> finite L^{3,q}
    -> RF-LOCAL-ID / Lorentz Fatou -> RF-LQ-CONTINUATION
    -> LOCAL / ENERGY / canonical pressure -> NS-R3.

The estimate must hold for EVERY upper t<=H uniformly in M. It is unproved.
No sharp projected flow is silently substituted into a pointwise speed
maximum principle. The new theorem below uses the ORIGINAL branch instead.

## 2. New full-PDE theorem: the global upper-pressure budget cannot transfer

Evidence: `research/evidence/2026-09-09-pressure-curvature-barrier.md`.
Complete proofs are immediately in `paper/sections/viscous_history.tex`,
subsection `pc:section`. AUTHOR proof; independent mathematical audit pending;
novelty undetermined. Canonical graphs and formal theorem statuses unchanged.

Set, for the actual canonical pressure,

    K(t)=max(0,sup_x lambda_max(Hess p(t,x))),
    A(t)=integral_0^t sqrt(K(s)) ds.

Global semiconcavity and the full pressure BMO estimate prove

    ||grad p||infinity <= C sqrt(K) ||u||infinity,
    ||u(t)||infinity <= ||d||infinity exp(C A(t)).

The semiconcavity lemma has explicit nonsharp constant 48 sqrt(2);
C=48 sqrt(2 C_p) with C_p a dimensional pressure-BMO constant. All negative
pressure eigenvalues, all modes and the entire exterior are retained.
If integral_0^T exp(2 C A(t))dt is finite, the viscous enstrophy estimate
and LOCAL exclude a finite endpoint. A finite A(T) also feeds
ENERGY -> bounded L3 -> canonical CONTINUATION. The clock is NS-scale
invariant. A sufficiently small one-sided type-I K<=c/(T-t)^2 is excluded.
There is NO arbitrary-input bound for either clock.

The exact family consequence is stronger than a ray obstruction. ANY
fixed-nu family of exact unforced solutions with uniformly bounded initial
H3 and L-infinity norms, bounded observation times and uniformly bounded
integral sqrt(K) has uniformly bounded final gradients. In particular,
summable Hm initial increments, one global Hess p_j<=K_plus I bound, and
diverging final gradients are incompatible. No assumption on support,
frequency scales, overlap, phases, polarizations or exterior smallness occurs.

This kills the proposed viscous transfer that RETAINS the Euler source's
global upper-Hessian budget, even after repairing pre-activation damping.
It does not contradict the inviscid theorem: bounded velocity alone does
not give Euler derivative continuation. Bounds on only one curve or a proper
core are not global semiconcavity and are outside this exclusion.

## 2a. Full viscous action: the next inverse shortcut is excluded

Integration input: `69cc6a45cf27f14d7ef0961a03df5245c23cdbfb`.
Evidence: `research/evidence/2026-09-09-viscous-packet-action.md`.
Full proofs are already in `paper/sections/viscous_history.tex`, labels
`va:identity`, `va:negative`, `va:classification`, and `va:hardy`.
AUTHOR PROOFS; independent mathematical audit pending; novelty undetermined.
Canonical graphs and formal status remain unchanged.

For an ACTUAL unforced NS background put G=grad u, H=Hess p,
D_t=partial_t+u.grad, w=D_t eta-G eta, and
L_u w=P[D_t w+G w-nu Delta w]. The exact displacement operator is

    L_u w=P[D_t^2 eta+H eta-nu Delta D_t eta
                  +nu G Delta eta+2nu sum_j(partial_j G)partial_j eta].

After the full solenoidal pairing, its negative quadratic form is the
Euler-shaped form integral(|D_t eta|^2-eta.H eta) PLUS

    nu integral[sum_j partial_j eta.G partial_j eta
          -sum_jk G_kj partial_j eta.partial_k eta
          -sum_j eta.(partial_j G)partial_j eta].

The two leading spatial terms at grad eta=a tensor xi give
|xi|^2 a.G a-|a|^2 xi.G xi, a strain eigenvalue DIFFERENCE of either sign.
They are not nonnegative viscous dissipation. Pressure was not discarded.

A complete continuum theorem classifies the failure: on any nonzero smooth
finite-energy unforced NS background, there is NO finite lower bound for
this form by -C(||eta||2^2+||D_t eta||2^2), even when C may depend on that
entire background. On a short fixed interval, compact solenoidal material
wave tests have ||D_t eta_N||2=1, Euler-shaped action >=1/2, and the full
viscous action tends to minus infinity. The background can in particular be
one arbitrarily small compact-datum, globally smooth R3 solution. All of its
actual exterior is retained. Test displacements are not nonlinear NS flows.
The only finite-energy background on which the stated semiboundedness holds
is zero. Endpoint penalties do not help because the tests vanish near both
endpoints. This does NOT make the parabolic Cauchy problem ill posed or
exclude a different inverse or a justified restricted displacement space.

The next constructive repair was tested too: the classical Hardy identity
gives an interior Euler-shaped form bound (1-4c)||D_t eta||2^2 under
H<=c/(T0-t)^2 I for c<1/4 and zero-endpoint tests. It tolerates a logarithmically
divergent majorant curvature clock, but does not control the indefinite
viscous terms above and is NOT a common free-trace NS inverse. Ordinary
velocity-linearization energy instead retains signed strain, whose endpoint
control on a concentrating common history is still missing. No critical
producer, unforced singular solution or certified regenerative turnover follows.

## 3. ONE dominant nut: one common trace with a different viscous inverse

Construct a specific continuously coupled concentrating history for original
unforced NS, with one nonzero Schwartz trace and a full-PDE correction which
preserves its singularity, while tolerating the NECESSARY unbounded positive-
pressure-curvature history. Do NOT preserve the now-excluded global pressure
budget merely because it supplies the Euler displacement inverse.

For a globally defined solenoidal trial U, the exact equation is

    F_U = partial_t U-nu Delta U+P div(U tensor U),
    L_U w+P div(w tensor w)=-F_U,
    L_U w=partial_t w-nu Delta w+P div(U tensor w+w tensor U),
    d=U(t0)+w(t0) in S_sigma, d!=0.

Only zero SOLENOIDAL residual is required: a pure gradient is absorbed into
the final canonical pressure. Flatness, all-order asymptotics, or smallness of
a nonzero residual is not zero force. Local trial fields need a global
extension before P is applied, including all extension and pressure defects.
A correction must preserve a stated singular lower bound, not just exist in
an unspecified norm. Neither an arbitrary trace-array inverse nor a reset
of each daughter is required or allowed: ONE compatible orbit is needed.

UE0: identify and remove the first indispensable projected forcing in the
entire core, preparation, mean, exterior and localization history. A zero
terminal-force slab must be proved, not inferred from endpoint flatness.

UE1: prove common Cauchy-trace realization and an actual viscous history
inverse, with endpoint-uniform estimates in spaces controlling the singular
amplitude and all mean/exterior couplings. The inverse must use a coercivity
mechanism compatible with Section 2: perhaps local/directional or weighted
form control, NOT a uniform global upper-Hessian bound. Section 2a additionally
rules out unrestricted Euler-shaped time-only displacement coercivity on any
nonzero finite-energy NS background. A new inverse must estimate its actual
viscous spatial terms or prove an invariant admissible restriction. The actual viscous
history and pressure equations must be derived. Formal backward heat is not
an admissible initialization. Include damping over the ENTIRE prehistory.

UE2: cancel the full nonlinear residual by a convergent argument, including
all tails, cross-label products, pressure and ordinary diffusion. A formal
or Borel reconstruction with a flat remainder does not suffice.

UE3: realize the exact field on all R3 from ONE Schwartz datum, with no remote
forcing or imposed boundary stresses. Prove pressure normalization, finite
energy, trace and pre-endpoint smoothness. Integrate this with UE1 whenever
the inverse or matching is nonlocal.

UE4: identify the constructed field with that datum's classical branch and
prove a finite endpoint. Independent adversarial review is required before
canonical promotion. No numerical orbit is a continuum certificate.

Follow a successful UE1 immediately through UE2--UE4. If the revised inverse
fails, prove its precise obstruction and pivot. A general input-only bound
for Section 2's exponential-history integral would instead close the positive
route, but writing that quantity introduces no new arbitrary-data estimate.
Two returns to the same uncontrolled critical norm require changing mechanism.

## 4. Retained exclusions and source gates

All detailed theorem hypotheses and earlier task boundaries are preserved in
the archived predecessor PLAN and their evidence, particularly:

* `2026-09-08-autonomous-pulse-obstruction.md`,
  `2026-09-08-unforced-support-and-pulse-audit.md`,
  `2026-09-08-forced-type-rigidity.md`, and the different-tier
  `2026-09-08-obstruction-audit.md` in `research/evidence/`.
  Zero separated labels cannot start autonomously; analyticity subsumes the
  exact no-start case. Exact compact patches/snapshots are unavailable.
  Tiny overlap on growth windows is NOT excluded by its size alone.
* `2026-09-08-smooth-pulse-inverse-and-history.md` and
  `2026-09-08-mixed-trace-principal-inverse.md`: the regular-fiber smooth
  minimum-norm inverse is a tool; independent pulse inverses do not compose
  into a small connected-history inverse with one Cauchy trace.
* `2026-09-08-normalized-work-falsification.md`: raw normalized angular work
  can diverge even in globally small unforced NS, including the nonzero-seed
  compact-data family. It is not a finite arbitrary-input resource.
* The narrow-packet, mixing, source-cycle, cone, full-return, relative-energy
  and remote-pressure evidence remains intact. Spectral growth is not
  regeneration; source composition is not time evolution; exterior is not
  automatically dissipative. The old six-carrier benchmark is secondary,
  not a universal representation of a singularity.

Accepted source input: the owner-checked forced OpenAI theorem remains accepted
at its recorded scope. It does not supply an unforced implication or decide
this project's terminal goal. The new Euler construction was inspected as an
inviscid proposed transfer, not independently audited or kernel-rebuilt here.
Its globally controlled positive pressure curvature is now a mathematically
excluded invariant for any successful fixed-viscosity transfer.

Source provenance: `literature/recent-progress-2026-09.md`,
`literature/openai-euler-transfer-2026-09-09.md`,
`literature/viscous-history-source-audit-2026-09-09.md`, and the new evidence's
primary-source ledger. Parsed/rendered Euler PDF pagination differs; inherited
fingerprints are not silently described as newly recomputed. The connected
source main was rechecked at `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`.
Palasek's pre-activation damping is model prior art. Caltech's recorded profile
has leading-order viscosity at exponent one half, and its complete stability
certificate was not newly obtained. Other recent criteria retain their gates.
No new source is claimed to provide the arbitrary unforced NS conclusion.

## 5. Manuscript, validation and operations

The manuscript and standalone papers live in public `paper/`, migrated from
`navier-paper@b6d0c6100ceba3783dc0c1bc8de4df3e1089396c`; the original fingerprints
remain in `paper/migration-source.json`. The old repository is a private
historical archive. This is one research project, not separate prior art.
No external submission, added authorship or release is made by this update.

The new checker passes 69 exact finite assertions: convex-average constants,
pressure-kernel derivatives, the speed diffusion sum of squares, interpolation
exponents, viscous Young absorption and the critical/type-I powers. It does
not certify the universal continuum proof, novelty or independent correctness.
Both full-checkout verifier modes pass (29 canonical records, 8 pending
supplements). `make -C paper documents check` and a forced complete main rebuild
passed after using the installed `bibtex.original` through a local PATH shim
for a broken system bibtex symlink. The final main PDF has resolved citations
and references; its changed pages were rendered and inspected. No PDF, cache,
font, shim or build product is committed. Exact and structural checks are not
mathematical audits. Independent review of the new theorem remains pending.

The displacement-action follow-up passes 27 new exact assertions and all 23
`research/check_*.py` programs (the full phase-ring checker at order eight).
Both verifier modes and whitespace checks pass on the complete checkout.
`make -C paper documents check` and a forced main rebuild pass; the main PDF
has 146 pages, with the new section on pages 139--143. All changed pages were
rendered and inspected. An unsupported `mathscr` macro was corrected to
`mathcal` before the successful rebuild. Section 8 below is preserved
byte-for-byte from the integration base. These are author algebra/source/build
checks, not independent audit or new Lean verification.

Before each write refresh main, inspect concurrent changes and preserve them.
Run applicable exact checks, `research/verify.py --research-only`,
`research/verify.py --paper-only`, manuscript checks and `git diff --check`.
Use only ordinary fast-forward updates. Never force-push. Do not promote
canonical graphs or author theorems on the basis of successful builds.

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
