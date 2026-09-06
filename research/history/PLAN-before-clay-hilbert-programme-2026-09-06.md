# Navier--Stokes: kinetic macroscopic-control research plan

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: kinetic-macroscopic-control-exploration-2026-09-06
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: test-nonlinear-kinetic-stress-remainders-for-resolved-momentum-control
active_architecture: kinetic-macro-transfer-candidate-not-established
complete_terminal_route: none-established
kinetic_interface_status: source-scoped-not-integrated-as-graph-theorem
kinetic_terminal_certificate: limit-first-resolved-momentum-bound-unproved
structural_paper_status: complete-author-level-primary-source-compared
retired_primary_route: pressure-quotient-defect-shell-material-response
intrinsic_bridge_status: author-checked-independent-audit-pending
single-profile-rigidity_status: falsified-for-the-normalized-package
two_balance_falsification_status: author-checked-independent-audit-pending
quadratic_lyapunov_status: author-checked-independent-audit-pending
local_energy_only_status: source-statement-checked-consequence-author-checked
pointwise_helical_falsification_status: author-checked-independent-audit-pending
terminal_status: not-proved
terminal_obstruction: unchanged
formal_work_this_run: deferred
public_release: false
```

## 1. Decision, target and allocation

The owner's new instruction is to reopen creative TERMINAL research, using
the completed obstruction paper and the supplied kinetic/geometric synthesis.
The standalone paper task is complete at author-proof level; waiting for
external review is not the remaining research plan. Neither that paper nor
this plan has proved arbitrary-data regularity.

The target is unchanged: for every solenoidal Schwartz datum on R3 and every
fixed nu>0, the ORIGINAL unforced incompressible Navier--Stokes equation has
a global smooth solution with energy bounded by its initial value.

**First exploration: nonlinear transfer from collision-damped kinetic modes
to resolved fluid momentum.** Kinetic geometry is a candidate source of
estimates, not a declaration that the obstruction has become easier. Keep
one main mechanism active. Stafford-inspired quantitative operator algebra
is a supporting lane; geometric concentration exclusion is a reserve, not a
second unproved theorem silently appended to the first.

The exact mathematical contracts, calculations, rejection examples and
primary references are in
`research/evidence/2026-09-06-kinetic-plan-contracts.md` (KPC below).
That note is not a second live task list. It adds no promoted graph claims.
The scheduling labels K0, K1, K2, A and G below are NOT formalization phases.

## 2. Work backward: a less demanding sufficient kinetic certificate

The established terminal suffix is LOCAL + ENERGY + CONTINUATION, once an
input-derived finite bound on the classical branch's L-infinity_t L3_x norm
is proved on every finite horizon. A direct contradiction at finite Tstar
may bypass this suffix; there is no requirement to retain it.

Use a genuine kinetic initial-value problem, rather than an inverse force
constructed from an assumed smooth fluid solution:

    epsilon^2 partial_t F_epsilon + epsilon v.grad_x F_epsilon
        = Q_nu(F_epsilon,F_epsilon),
    F_epsilon^in(x,v) = M(v-epsilon u0(x)).

Start with one hard-cutoff Boltzmann kernel in the whole-space
Golse--Saint-Raymond framework, scaled to the prescribed viscosity. The
initial relative entropy is exactly epsilon^2 ||u0||_2^2/2. The resulting
well-prepared weak limit supplies a Leray NS velocity, NOT its smoothness.
KPC Section 1 specifies the source and the compatibility checks.

The supplied proposal, a uniform finite-epsilon L-infinity_t L3 bound on
projected momentum, would suffice but is unnecessarily demanding. Prefer
**limit-first, momentum-only control**. Let delta>0 be half a guaranteed local
existence time from u0,nu, let H>delta, and let S_J be the compact spatial
mollifiers defined in KPC. Let m_tilde_epsilon be a justified renormalized
projected momentum with the same distributional fluid limit. The target is

    sup_{J>=0} liminf_{k->infinity}
      ||S_J m_tilde_epsilon_k||_{L-infinity(delta,H;L3_x)}
        <= C(u0,nu,H,delta) < infinity.                  (K_res)

All J refer to one hydrodynamically convergent sequence and the same limit.
The constant must be independent of J. Raw moments may be used when their
function spaces are justified; no full-phase-space Sobolev estimate is
required merely for convenience. The preparation cannot depend on an unknown
future fluid solution. One admissible family for each datum/horizon suffices;
there is no need to prove estimates for all possible kinetic weak solutions.

**Explicit closure:** K_res + distributional convergence imply a global-in-x
L-infinity(delta,H;L3) bound on the Leray velocity by duality and removal of
spatial smoothing. Weak--strong uniqueness identifies it with the classical
branch before Tstar. LOCAL handles [0,delta]. CONTINUATION then excludes any
Tstar<H; arbitrary H and ENERGY finish NS-R3. KPC gives the duality argument
and states where the hydrodynamic and weak--strong interfaces must be checked.

This is a reduced DEMAND ON THE KINETIC APPROXIMANTS, not a proof or a strict
reduction of the terminal NS obstruction. K_res without a producer is a
reformulation, not the research achievement sought.

Keep the order epsilon -> 0 at fixed J, then J -> infinity. The proof need
not control all kinetic-scale frequencies simultaneously. Conversely,
constants C_J growing with resolution, an epsilon-dependent diagonal with
no convergence justification, or bounds on separate dyadic blocks without
summability do not prove K_res. Even the elementary energy smoothing bound
grows as 2^(J/2) and fails this certificate.

## 3. First main attack: K1, nonlinear collision-stress memory

**Proposed mechanism.** Eliminate the damped microscopic component with its
retarded propagator, retain the signed transport/collision coupling, and
estimate only the resolved momentum output. Do not bound the full kinetic
solution first unless that bound genuinely closes the same output estimate.

Use Pi for collision invariants, P for the spatial Leray projection, and
Qmic=I-Pi. For smooth weighted fluctuations, put a=Pi g, h=Qmic g and

    partial_t g + T g/epsilon + Lg/epsilon^2 = Gamma(g,g)/epsilon,
    T=v.grad_x,   ker L=span{1,v1,v2,v3,|v|^2}.

The micro propagator has formal generator
A_epsilon=L/epsilon^2+Qmic T Qmic/epsilon. Its exact elimination retains
both its initial layer and Gamma(g,g). In particular the known identity

    Gamma(a,a) = (1/2)L(a^2),  a in ker L,

suggests the microscopic variable

    r_epsilon = h - (epsilon/2) Qmic(a^2).

This removes the leading pure-macroscopic collision source, not the NS
nonlinearity. Its differentiated equation introduces derivatives of a^2,
transport of a^2 and mixed Gamma terms. The convective macroscopic flux must
still survive. KPC Section 3 gives the conventions and source of this identity.

**FIRST HARD TASK:** attack the actual remainder terms in the momentum
Duhamel pairing at arbitrary amplitude. Seek an input-only estimate uniform
in resolution AFTER the kinetic limit, rather than another formula for r.
A successful bound must feed directly into K_res or an explicitly proved
alternative terminal suffix. Retain signs/correlations long enough to test
whether transport memory supplies information lost by absolute energy bounds.
A blockwise calculation must include interscale interactions and the final
L3 summation or duality step.

**Advance only if:** the nonlinear remainder estimate has no unknown critical
fluid/kinetic norm on its right side; every coefficient cost and approximation
limit is paid for; and the estimate is valid for the chosen kinetic family.
A permitted intermediate result must remove a specific previously uncontrolled
term and leave a demonstrably smaller obligation, not just rename it.

**Kill or switch if:** the argument needs small a in a critical norm,
exp(integral ||grad u||_infinity), an uncontrolled fourth-power strain budget,
prior uniform high Sobolev regularity, or a bound equivalent to the old signed
pressure remainder. Recovering only L-infinity L2 and L2 H1, recovering
Newtonian stress, or showing the normal-form identity again is not advancement.
The identity is already in the hydrodynamic-limit literature.

## 4. K0: a bounded compatibility check, not a research detour

Before a candidate estimate is used, check the following once against KPC [R1].
Do not build a new general kinetic well-posedness theory or reprove GSR.

- Fix the collision class, viscosity normalization, positive preparation,
  entropy normalization, initial trace and the precise Leray conclusion.
  The general NSF energy statement is not automatically the required Leray
  statement without the preparation. The source explicitly addresses it.
- Decide raw versus density/velocity-truncated momentum. Justify the Leray
  projection's domain, convergence of the chosen observable and removal of
  conservation/renormalization defects. Verify the weak--strong identification
  used in Section 2; it does not require an endpoint strain bound.
- Write a parameter ledger for epsilon, J, velocity cutoff, Hermite order,
  collision constants, amplitude, delta and H. State which limits commute
  and prove every commutation actually used.

For renormalized F, finite entropy does not imply the weighted smoothness
needed to differentiate the formal micro equation. An approximation or
renormalized argument must bridge this. If K1 works only for globally smooth
kinetic approximants whose existence requires the same unknown bound, it has
not passed K0. Do not change collision kernel or introduce forcing silently.

## 5. Alternative K2: macroscopic observability with adaptive entropy tests

This is a switch from an operator-norm bound on a microscopic propagator to
a nonlinear, finite-time dual estimate. It is not approved as merely a new
notation for the failed K1 remainder.

**Proposed mechanism.** For a terminal momentum test phi, transport a kinetic
test/entropy dual variable backwards and use the collision dissipation in
its pairing with the forward distribution. Only the momentum output is
observed; undamped acoustic/thermal variables are retained but need not all
satisfy a stronger regularity theorem. Allow genuinely nonlinear entropy
weights, dependence on the prescribed datum, and finite-window signed
estimates, rather than a universal monotone quadratic energy.

**Closure target:** for every smooth compact spacetime phi, an estimate

    limsup_{k->infinity}|<S_J m_tilde_epsilon_k,phi>|
      <= C(u0,nu,H,delta) ||phi||_{L1_t L^(3/2)_x},

uniform in J, implies the same limiting L3 bound by the Section 2 argument.
This output-duality target does not demand control of the supremum of all
finite-epsilon outputs. It remains unproved and is not progress by itself.

**Hardest step first:** bound the pairing of the TRUE nonlinear collision
source and the adaptive test, including commutators and changes of the
weight. Prove an observability inequality with controlled coefficient costs;
do not infer it from entropy production or a bracket-generation rank test.
If the backward test coefficients use the unknown future fluid strain,
that dependence has to cancel exactly or have an input-only bound.

**Switch test:** failure through exactly the same uncontrolled term as K1
requires a genuinely new mathematical mechanism before further investment.
No repeated rebranding as a clock, metriplectic metric, entropy correction,
least-action functional or adjoint certificate. A new functional alone does
not pass the gate.

## 6. Supporting lane A: quantitative Stafford-to-hypocoercivity adapter

The concrete bridge is differential-operator algebra, not the common word
"symplectic". Use [partial_v_i,T]=partial_x_i and Gaussian creation/annihilation
relations to search for QUANTITATIVE transfer of microscopic control to the
specific macro output missing in K1 or K2. The existing Stafford38 formal
README supplies an algebraic certificate and support architecture; it is
not an analytic estimate for these kinetic solutions.

An acceptable adapter returns an inequality on stated Hilbert/Banach spaces
with adjoints, domains, coefficient bounds, derivative loss and dependence
on epsilon/frequency/truncation. Frozen quadratic/Kramers--Fokker--Planck
models are calibration only. Compare with Hitrik--Pravda-Starov and Villani
before claiming novelty or rebuilding known machinery. Ordinary OU damping
can remove momentum, unlike Boltzmann: check the nullspace before transfer.

**Concrete first test:** compute the macro-to-micro observation Gramian for
transverse momentum and identify its degenerate directions, then check the
proposed estimate against KPC's small-drift Gramian. Full algebraic rank can
coexist with an arbitrarily bad coercivity constant. The identity
Qmic T(U.v)=(v tensor v-|v|^2 I/3):D U already shows that symmetric strain,
not only vorticity, is the coupling to the stress modes. Its squared Gaussian L2 norm
is 2|D U|^2. This is a calibration identity, not a terminal bound.

Only request an A-lane result after specifying the exact output estimate
in K1/K2 that consumes it. Full Hermite hierarchy infrastructure, generic
symbol classification or a proof of familiar linear smoothing is not the
main task. A polynomial representation of the integral collision operator
or a convergent controlled approximation must be supplied, not presumed.
If no quantitative nonlinear transfer is proved, keep any algebraic result
separate from NS progress. No edits to Stafford repositories are authorized
by this plan update.

## 7. Reserve G and permission to abandon the kinetic route

A structurally different reserve is a critical-concentration contradiction:
from a hypothetical finite-time singularity, construct a correctly normalized
kinetic/macro defect that must both propagate under transport and lie in a
collision-compatible null set, then prove these properties incompatible with
its nonzero normalization and fixed-input ancestry.

This reserve is NOT enabled by just obtaining a defect measure. KPC's
strong-L2/large-L3 field test shows why an unnormalized quadratic defect can
miss the entire critical concentration. No D-module, characteristic variety,
coisotropicity, compactness or rigidity is inherited merely from phase-space
terminology. Physical T*R3 and microlocal T*R6 are different spaces. A valid
G proposal must give both the selection AND the incompatible support/
propagation mechanism with an explicit terminal suffix before extraction work.

After K1 and a genuinely distinct K2 test fail, do not make kinetic geometry
the next permanent default. Record the exact failed implication and return
to cross-architecture search. Direct nonlinear/data-adapted/nonmonotone
fluid methods remain allowed by the obstruction paper. No theorem says a
successful proof must use kinetic geometry or all of nonlocality, spacetime
structure and full-datum dependence simultaneously. An appealing synthesis
is not evidence that it will close.

## 8. Mandatory falsifiers and model-fidelity checks

Run the relevant exact test BEFORE developing substantial machinery.

| Tempting inference | Required test or correction |
| --- | --- |
| Entropy + instantaneous collisions control momentum L3 | KPC's shifted-Maxwellian family has fixed scaled entropy, zero collision production and unbounded L3. It is a snapshot test, not a kinetic trajectory. |
| Small F-M means a perturbative fluid regime | Divide by epsilon in the fluctuation equation; the limiting arbitrary u0 need not be small. Cao--Carrapatoso's small-data thresholds are on scaled fluctuation norms. |
| Collisions damp all dangerous variables | Momentum is in ker L; test macro modes and the nonlinear source explicitly. |
| A moment or GENERIC derivation establishes closure | The stress is an unknown moment; identify its Newtonian limit and every error. Thermodynamic total energy includes heat; NS kinetic energy decreases. |
| A fixed quadratic kinetic metric escapes Theorem Q | Check its pullback and limiting evolution. Theorem Q applies only if it really induces the excluded datum-independent continuous quadratic fluid form and monotonicity; it does not ban all quadratic kinetic estimates. |
| Centering the Maxwellian removes geometry | Peculiar-velocity brackets retain curl U; in low-Mach variables the factor epsilon is present. Moving-frame derivatives also retain D U and partial_t U. |
| An algebraic certificate gives uniform coercivity | KPC's Gramian degenerates despite full rank. Record operator norms, domains, sign and derivative losses. |
| A fixed Hermite/Grad closure proves Boltzmann control | Its tail and nonlinear truncation defects require uniform estimates; full Boltzmann is not a finite Weyl polynomial. |
| Symplecticity forbids spatial collapse | (x,v)->(lambda x,lambda^(-1)v) is symplectic. Spatial squeezing alone contradicts nothing. |
| A quadratic defect or compact L2 limit rules out L3 concentration | Use the r^(-5/4) concentrating pulse in KPC and the preserved exact two-balance countermodel. Do not merge their premise classes. |
| Pointwise scalar vorticity damping follows from a kinetic lift | The globally smooth fixed-E,Y,Omega family and its constant local vorticity jet still test the actual fluid limit. Large initial growth does not imply sustained growth. |
| Inverse kinetic or modified dissipation proves original NS | Smoothness-dependent inverse forces are representations. A changed stress, force, viscosity law or momentum nullspace changes the target unless equivalence is proved. |

## 9. Binding progress and commit discipline

Before investing in a candidate, write its exact input-output estimate and
why it closes K_res/the dual target, or identify the specific plausible
architecture it decisively falsifies. A sufficient certificate itself is not
a producer. Attack nonlinear amplitude and resolution uniformity first.

The next substantive run should start with K1's remainder after the
Maxwellian correction, not another literature survey, brackets-only
construction, generic kinetic regularity proof, or extension of the paper.
Finish that investigation with an actual closing estimate, a demonstrably
smaller nonlinear obligation, or a precise falsification and genuine switch.
Success on linear, small-data, finite-mode, confined or periodic models is
calibration unless its missing transfer to the target is proved.

Do not spend the run accumulating related counterexamples to already retired
claims. A new no-go result is worth committing as mathematical progress only
when it eliminates a genuinely live option or materially strengthens its
premise class. Keeping PLAN current is an authorized planning deliverable,
not terminal mathematical progress.

Leave the conditional manuscript, the completed standalone obstruction paper,
the terminal proof graph and formalization unchanged during this exploration.
Promote claims only after proof and appropriate audit. Preserve all earlier
valid results; retiring their role in an architecture is not retracting them.
External review/priority questions for the paper remain separate and are not
a reason to stop research or permission to contact anyone.

## 10. Retained evidence, prior art and historical authority

The previous live PLAN is preserved verbatim in Git at
`1383040bbb775826c6d78674852f8ba89f25b353:PLAN.md`, blob
`ea7095b2084a3b1dcd1dbc035fedbfe1a991ae4b`. This replacement changes allocation,
not the mathematical status of any result. The older archived PLAN files
under `research/history/` remain unchanged.

Mandatory retained research evidence (all under `research/evidence/`):

- `2026-09-06-structural-obstructions-paper-audit.md` and
  `2026-09-06-global-smooth-vorticity-falsifier.md`: the completed Theorem Q/GS
  paper, its exact scope and pending independent review. The broad energy-only
  quadratic principle has prior art; priority for exact formulations is not
  certified. No further no-go manuscript work is the default terminal task.
- `2026-09-06-two-balance-falsification.md`,
  `2026-09-06-quadratic-local-energy-exclusions.md`, and
  `2026-09-06-pointwise-vorticity-helicity-exclusions.md`: retain the two-scalar,
  exact-balance, quadratic, local-energy-only, pointwise-jet and helical-parity
  exclusions with their DIFFERENT premise classes. They do not exclude every
  nonlinear, nonmonotone or nonlocal approach.
- `2026-09-06-intrinsic-record-tangents.md`,
  `2026-09-06-viscous-mixing-falsifier.md`, and
  `2026-09-06-terminal-architecture-reset.md` with `terminal-reset/`: preserve
  extraction and fixed-input warnings. Blanket ancient rigidity stays retired.

The pressure/quotient/defect/speed-shell/material-response family stays retired
as the primary arbitrary-data route. Reopening requires an actual input-only
endpoint argument; a kinetic re-expression of its unknown clock does not qualify.

KPC [R1--R9] records the new source checks: GSR for the large-data weak limit;
Cao--Carrapatoso for perturbative strong limits; Gibbons--Holm--Tronci and
Grmela et al. for moment geometry; Morrison--Updike and Zaidni--Morrison for
metriplectic structure; Villani and Hitrik--Pravda-Starov for quantitative
analysis; inverse kinetic and Stafford sources with exact limits on transfer.
These citations are leads or scoped existing results, not new graph imports.
The synthesis and K_res producer are not claimed novel or established.

PLAN.md remains the sole live task record. Keep all repositories private;
preserve concurrent edits, refresh before non-force writes, and stage explicit
paths. Unsigned commits are authorized. Run `python3 research/verify.py
--research-only` and `git diff --check` for these research-only status edits,
recording any checkout/overlay limitations. Do not claim builds certify math.
No public release, submission, added authorship, outside contact or Overleaf
recreation is authorized. Existing Phase I/II strings preserve formalization
status; they are not new Lean coverage or a reason to replace terminal research
by infrastructure work.
