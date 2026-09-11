# Navier--Stokes: the viscous mixed-trace inverse and its endpoint gap

This is the sole live task/status record. NS-R3 remains NOT PROVED; no
unforced counterexample has been constructed. Mathematical input:
`75ca907cad70b7ced4469d8492e7e5dc27cc7444`.
The entire preceding PLAN is preserved byte-for-byte in
`research/history/PLAN-before-viscous-fredholm-2026-09-09.md`.
Its formal-core Section 8 is retained verbatim below. The archive preserves
all earlier hypotheses and provenance; it is not a second active queue.
Manuscripts live in this repository's `paper/`.

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: finite-horizon-viscous-mixed-trace-repair-2026-09-09
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
finite_viscous_mixed_trace_inverse: proved-for-generic-positive-penalty-author-audit-pending
finite_inverse_initial_velocity: compact-smooth-in-fixed-trace-support
finite_inverse_endpoint_uniformity: not-proved
finite_inverse_common_trace: not-produced
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
run_status: finite-interval-viscous-inverse-constructed-no-terminal-resolution
public_release: true
repository_visibility: {navier: public, navier-formal: public, navier-paper: private}
external_contributions: pull-requests-welcome-owner-review-required
```

## 1. Rigid target and complete positive consumer

For fixed nu>0, original unforced incompressible NS on R3 is

    u_t-nu Delta u+P div(u tensor u)=0, div u=0,
    u(0)=d in S_sigma(R3;R3), p=sum R_i R_j(u_i u_j).

The positive target concerns EVERY such datum. A negative solution needs
ONE finite-energy Schwartz datum and a genuine finite endpoint of its
classical branch. Forced, inviscid, periodic, averaged and restricted models
are not substitutes. Schwartz is an initial condition, not permanent decay.

The reviewed positive consumer, for one fixed finite q>3, remains

    (1/q) W_q,M' + nu D_q,M = Pi_q,M,
    integral_0^t Pi_q,M <= nu integral_0^t D_q,M+C(d,nu,H,N0,q)
    -> RF-q -> RF-LQ-SYNTHESIS -> finite L^{3,q}
    -> RF-LOCAL-ID / Lorentz Fatou -> RF-LQ-CONTINUATION
    -> LOCAL / ENERGY / canonical pressure -> NS-R3.

The estimate is required for EVERY upper t<=H uniformly in M. It remains
unproved. The new inverse is not an arbitrary-data critical producer.

## 2. Constructive result: full-PDE finite-horizon mixed-trace solvability

Evidence: `research/evidence/2026-09-09-viscous-fredholm-inverse.md`.
Complete author proof: `paper/sections/viscous_fredholm.tex`, included from
`viscous_history.tex`. The preceding history/action manuscript is preserved
byte-for-byte as `viscous_history_core.tex`. Independent audit and novelty
remain undetermined. Neither canonical graph nor formal status is promoted.

For any specified smooth all-Sobolev solenoidal background U on [0,T], fixed
nu>0, let E(t,s) be the FULL forward linearized viscous evolution, T(t,s)
the solenoidal Piola transport, and A=curl chi(-Delta)^(-1)chi curl. Then

    K=integral_0^T T(0,s) E(s,0) A ds

is compact on L2_sigma(R3) and gains every spatial order below two.
The mixed problem

    L_U v=f, D_U eta-(grad U)eta=v,
    v(0)=lambda A eta(0), eta(T)=0

reduces EXACTLY to (I+lambda K)eta(0)=-b_f. Every positive lambda outside
a locally finite exceptional set gives a unique smooth solution with
compact smooth initial velocity correction; arbitrarily large such lambda
exist. At U=0 every positive lambda works, even though A does not commute
with heat. The proof uses the full forward parabolic propagator and a
finite-rank determinant, not a pressure-coercive displacement action.
All Leray, mean, exterior and return interactions remain in the operator.

This closes finite-interval existence for THIS mean-type mixed condition,
not arbitrary final velocity assignment, singular endpoint estimates, or
one shared trace across horizons. The next step is quantitative spectral
selection and nonlinear exactification. UE1 is not complete.

## 3. Preserved exact exclusions: what the new inverse must not assume

The full statements are retained in the preceding PLAN and linked evidence.
The two newest exclusions are complete author proofs, audit pending:

**Global upper pressure curvature.** `2026-09-09-pressure-curvature-barrier.md`
proves for the ACTUAL canonical pressure, K=max(0,sup_x lambda_max Hess p),

    ||grad p||infinity <= C sqrt(K)||u||infinity,
    ||u(t)||infinity <= ||d||infinity exp(C integral_0^t sqrt(K)).

The full viscous enstrophy identity excludes a finite endpoint if the
squared exponential is time integrable. Thus fixed-nu families with bounded
initial H3 and velocity supremum, bounded observation times, and a uniform
global integral sqrt(K) cannot have diverging final gradients. It excludes
transferring the Euler source's GLOBAL upper-Hessian budget to a singular
fixed-viscosity family. It does not exclude local/directional constraints;
no input-only curvature bound was proved.

**Full viscous displacement action.** `2026-09-09-viscous-packet-action.md`
proves, with G=grad u, H=Hess p, D_t=partial_t+u.grad, w=D_t eta-G eta,

    L_u w=P[D_t^2 eta+H eta-nu Delta D_t eta
                  +nu G Delta eta+2nu sum_j(partial_j G)partial_j eta].

The complete action includes the signed principal spatial symbol
|xi|^2 a.G a-|a|^2 xi.G xi. It has a finite lower bound in the material-time
norm on all compact solenoidal tests if and only if the finite-energy
background is zero. On every nonzero background a localized transported
high-frequency test defeats the pressure-only coercivity shortcut. A Hardy
bound under H<=c/(T-t)^2, c<1/4, controls only the Euler-shaped form, not
this viscous action. These are form obstructions, not parabolic ill-posedness.
Section 2 supplies an inverse that does not use that failed form.

Other preserved scopes: separated zero pulses cannot start autonomously;
flatness does not imply zero forcing; regular-fiber inverses do not provide
small common-trace connected-history inverses; raw normalized angular work
is unbounded even on globally small unforced solutions; narrow singular
replicas need a nonperturbative exterior; many spectral transfers can be
harmless mixing; source composition is not time evolution; decomposable
convex cones do not supply one-sided nonlinear traps. Their evidence and
audit qualifications remain unchanged. The old symmetric six-carrier test
is secondary, not a universal singularity ansatz.

## 4. ONE dominant nut: nonlinear amplification with a common viscous trace

Construct ONE continuously coupled concentrating full history with a
nonzero Schwartz trace and a full-PDE correction preserving its singularity.
It must tolerate the necessary unbounded positive-pressure-curvature history.
For a globally defined trial U, retain the exact residual and correction:

    F_U=partial_t U-nu Delta U+P div(U tensor U),
    L_U w+P div(w tensor w)=-F_U,
    d=U(t0)+w(t0) in S_sigma, d!=0.

UE0: remove the first indispensable SOLENOIDAL forcing from the entire
preparation, core, means, exterior and localization history. Pure gradients
are absorbed into canonical pressure; a nonzero flat remainder is not.

UE1: strengthen Section 2 to quantitative inverse bounds in spaces detecting
singular amplitude and compatible Cauchy traces on a concentrating sequence.
The full prehistory damping is required. Arbitrary backward heat or resetting
each daughter is not initialization. A common lambda avoiding all resonances
does not make the resulting initial traces equal or summable.

UE2: cancel the FULL nonlinear residual by a convergent argument, with all
cross-label products, pressure, tails and ordinary diffusion. Follow any
successful quantitative inverse immediately into this step.

UE3: obtain ONE Schwartz datum on all R3, canonical pressure, finite energy,
initial trace and pre-endpoint smoothness. No remote forcing or imposed
boundary stress is permitted. Nonlocal matching belongs inside the proof.

UE4: identify the exact field with its datum's classical branch and prove
its finite endpoint by a preserved singular lower bound. Independent review
is required before canonical promotion. No numerical orbit is a certificate.

A successful positive mechanism may instead feed Section 1. Two returns to
an uncontrolled future critical/strain norm require changing mechanism.
The finite inverse's constants concern a KNOWN smooth trial, not a bound
for arbitrary unknown solutions. No terminal breakthrough is claimed.

## 5. Provenance, manuscript and checks

Accepted source input: the owner-checked forced OpenAI theorem stays accepted
at its recorded forced scope; no unforced implication or prize decision is
inferred. The proposed unforced Euler construction was inspected for its
history/mean operator, not independently audited or kernel rebuilt here.
The current source ref was rechecked at
`openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`.
Its inviscid pressure-controlled inverse is not a viscous theorem.

Keep `literature/recent-progress-2026-09.md`,
`literature/openai-euler-transfer-2026-09-09.md`, and
`literature/viscous-history-source-audit-2026-09-09.md` as source records.
Parsed/rendered Euler PDF pagination differs; inherited fingerprints are
not newly recomputed fingerprints. Palasek's pre-activation damping is
model prior art, not unforced NS. The Caltech half-exponent profile has
leading-order viscosity; its complete stability certificate was not newly
obtained. Other recent regularity/extraction theorems retain their assumptions.
Project manuscripts are internal work, not separate external prior art.

The new checker passes 205 exact finite assertions, including 14 genuinely
noncommuting heat-matrix cases and all mixed-boundary signs. All 24 research
check programs passed, phase ring through order eight. Both full-checkout
verifier modes passed: 29 canonical records, 8 pending supplements. Nested
TeX includes now resolve relative to the manuscript build working directory,
matching latexmk. `make -C paper documents check` and whitespace passed.
The new section on pages 143--146 of the 148-page main PDF was rendered and
inspected. No PDF, cache, local bibtex shim or generated log is committed.
These are exact/structural checks, not independent mathematical certification.

The public manuscript migration remains recorded in `paper/migration-source.json`.
The legacy `navier-paper` repository remains a private archive. Before every
write refresh main and preserve concurrent changes. Run applicable checks,
`research/verify.py --research-only`, `--paper-only`, manuscript checks and
`git diff --check`. Use ordinary fast-forward updates only. No external
submission, new authorship, release or formal claim promotion is authorized.

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
