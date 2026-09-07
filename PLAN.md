# Navier--Stokes: whole-space refinement and signed critical production

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: signed-transfer-research-stopped-by-owner-2026-09-08
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: RF3-signed-critical-production-on-actual-whole-space-flows
active_architecture: direct-whole-space-projected-family-with-reviewed-conditional-consumer
complete_terminal_route: none-established
terminal_status: not-proved
terminal_obstruction: input-only-critical-refinement-estimate-not-produced
refinement_wave: interrupted-author-candidates-unreviewed
run_status: stopped-at-owner-request
secondary_goal: MIC-R3
secondary_goal_status: kinetic-and-microscopic-interfaces-remain-separately-gated
formal_work_this_run: deferred
public_release: false
```

## Authority and frozen frontier

This is the sole live allocation. The exact target remains every real
solenoidal Schwartz datum on R3 and every fixed nu>0: the original unforced
incompressible NS equation has globally smooth velocity AND normalized
pressure, the prescribed initial trace, and energy no greater than initially.
A rigorous counterexample in this exact class is a separate terminal outcome.
Periodic, forced, modified, kinetic and microscopic claims retain their own
scopes. NS-R3 and CRITICAL remain gaps in the unchanged canonical proof graph.

The owner explicitly authorized available frontier models and concurrent
research on distinct mechanisms for this run, superseding Claude-only and
single-primary allocation. One controller owns state, integration and
promotion. Workers own only assigned evidence. No public release, outside
contact, manuscript/formal-repository write, authorship change, purchase or
force push is authorized. Unsigned commits and ordinary private-repo pushes
remain authorized. All repository writes belong to navier.

The wave began at main `ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`, with
origin/main identical and no tracked or untracked edits. The empty patch
SHA256 was `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The preceding PLAN is preserved byte-for-byte in
`research/history/PLAN-before-cubic-refinement-2026-09-07.md`, original blob
`5dae5bf243b3536d74001eba7488245f4d1e4c65`. Its archives preserve all earlier
results, audit qualifications and scoped exclusions.

Actual concurrency is eight agents including the controller, hence at most
seven workers. No fixed wall-time, token or monetary balance is exposed;
work assignments use bounded periods and no purchased services. Scratch is
under `.git/navier-wave-20260907`, under 0.5 MB at the latest check, on disk
rather than tmpfs. The filesystem has about 112 GB available; /tmp about
46 GB and /dev/shm about 47 GB. Recheck before large work; this programme
needs small text artifacts, not local PDF collections or build caches.

Read `docs/proof.md`, `docs/proof-graph.yaml`, `research/verify.py`,
`research/refinement-slow-manifold-contract.md`, the two refinement maps,
`research/kinetic-clay-hilbert-contracts.md` and
`literature/kinetic-hilbert-scope.md`. Load detailed sources/history only
for a concrete lane. Specification graphs and author candidates are not
theorems. The old manuscript/formal phase strings are preserved, with no
new formal coverage.

## Reviewed construction and conditional consumer

The complete proof is
`research/evidence/2026-09-07-whole-space-cubic-refinement.md`.
The actual fresh-context reviews are recorded in
`research/evidence/2026-09-07-cubic-refinement-audit.md`, including the full
independent integration report. These are component/adapter results;
there is no new arbitrary-data critical bound or singularity exclusion.

Fix N0>0 once, N_j=2^j N0, and orthogonal Fourier ball projections P_N.
The exact whole-space flows

    u_N,t = nu Delta u_N-P_N P((u_N.grad)u_N),
    u_N(0)=P_N d

exist globally in the infinite-dimensional bandlimited solenoidal L2 space.
A Hilbert-space ODE contraction plus exact energy proves this at each
cutoff. No finite-dimensional assertion, sharp L3 ball multiplier bound,
fixed-box spectral gap or expanding-domain limit is used.

Set e_j=u_(N_(j+1))-u_(N_j), a_j(t)=N_j^(1/2)||e_j(t)||2. The sufficient
cubic output is

    sup_(0<=t<=H) sup_M sum_(j<M) a_j(t)^3
         <= K(d,nu,H,N0)^3 < infinity.                      (RF-CUBE)

The sum is inside the time supremum. Full datum, viscosity and finite
horizon dependence is allowed; energy-only, polynomial or inviscid-uniform
costs are not required. RF-CUBE is unproved. It is weaker than RF-SUM in
the original contract and is not claimed equivalent to global regularity.

Sharp L2 shell estimates and a layer-cake argument prove the L3 synthesis
for overlapping ball-supported increments, including resolved corrections.
This gives a uniform finite-approximation L-infinity L3 bound under RF-CUBE.
On every compact classical lifespan, an H3 residual and energy comparison
identify u_N with the canonical classical branch in C_t L2. Those local
comparison constants may diverge at the endpoint; the conditional critical
constant comes only from RF-CUBE. Fatou transfers that same critical bound
to the classical branch, and canonical LOCAL/CONTINUATION/ENERGY finish the
original velocity, pressure, trace and energy target. No new weak-solution
uniqueness or approximate-pressure limit is needed for this selected route.

The generic time-family theorem was repaired to assume strong L2
measurability explicitly. RF-CUBE gives finite L^p_t L3_x convergence and
uniform L2 tails, but need not give uniform-in-time L3 tail convergence.
Actual projected paths satisfy measurability automatically. Independent
integration review accepted the complete repaired composition.

## First missing estimate

For each actual neighboring pair, v=u_j, U=u_(j+1), w=U-v on the common
fine space, retain the full equation

    w_t+nu A w+B(v,w)+B(w,v)+B(w,w)=F,
    F=-(I-P_j)B(v,v),
    (1/2)d||w||2^2/dt+nu||grad w||2^2
        =<F,w>-b(w,v,w).

Here b(a,b,c)=integral(a.grad)b.c and B includes fine Leray/Fourier
projection. Resolved corrections in w are not zero. For finite M,

    (1/3)W_M'+nu D_M=Pi_M,
    W_M=sum_(j<M)a_j^3,
    D_M=sum_(j<M)N_j^(3/2)||e_j||2||grad e_j||2^2,
    Pi_M=sum_(j<M)N_j^(3/2)||e_j||2
                         [<F_j,e_j>-b(e_j,u_j,e_j)].

A bound integral_0^t Pi_M <= nu integral_0^t D_M+C(inputs), uniformly
in M at EVERY upper time t<=H, would suffice. Strict absorption also
bounds accumulated D_M but is not necessary for RF-CUBE alone. The
initial W_M is uniformly finite for Schwartz data. This signed producer,
or a weaker adequate critical output with its full consumer, is the first
gap. Future strain, critical norms and separate worst-case source/feedback
bounds cannot stand in for it.

One actual positive transfer estimate is now proved: if U is a fine flow,
p=P_N U, q=(I-P_N)U and G=-P_N P div(p tensor q+q tensor p+q tensor q),
then for K<=N/2,

    integral_0^H ||P_K G||2
        <= C K^(5/2) N^(-2)||d||2^2/nu.

Low output forces both parents high, so dissipation pays for them. The
constant is independent of fine cutoff and horizon. The estimate controls
actual forcing, not its nonlinear response. At neighboring scales its
upper bound deteriorates; this is not an optimality obstruction. Signed
near-diagonal transfer and its correlated resolved response remain open.

## Interrupted signed-transfer run (2026-09-08)

The owner requested the terminal breakthrough after recovery of the completed
wave, then explicitly requested conclusion, a plan update, commit, push and
stop. This continuation started from clean main
`acc498daecc2a914d499019194e198bc658ebcf8`, refreshed against origin/main.
Research is stopped. No terminal breakthrough, critical producer or new
independent mathematical audit was completed. The reviewed preceding wave
remains intact; the canonical proof graph and verifier are unchanged.

The interrupted worker returns are preserved in
`research/evidence/2026-09-08-signed-transfer-interrupted.md`, with their
original file digests and unfinished obligations. They are author working
notes, not promoted claims. The original frontier packet and scratch remain
under `.git/navier-wave-20260908`.

The common target is RF-q for one fixed finite q>3, with full datum, fixed
positive viscosity and finite-horizon dependence allowed, uniformly over
all cutoffs and every upper time. A single-flow smooth-block bound with a
complete consumer may replace paired RF-q. The first uncontrolled term is
the signed comparable-frequency part of the smooth-block commutator.

- The direct worker began an angularly resolved vector-transfer factorization;
  it produced no signed spacetime bound.
- The falsification worker identified central oddness as a mechanism fixing
  Cartesian Fourier phases and drafted a smooth-block positive-transfer test.
  The complete test and its quantitative persistence remain unaudited.
- The correction worker examined a correction adapted to Euler transport;
  arbitrary-amplitude coercivity and the viscous remainder remain open.

No worker is assigned continuing research. Any future owner-authorized
resumption should first check the saved exact formulas and scope, then seek
signed comparable-frequency control retaining vector polarization dynamics.
Fixed Cartesian phases alone do not freeze polarization. Returning to an
uncontrolled critical amplitude times dissipation or to the squared-enstrophy
integral does not supply the missing estimate.

Closeout checks: research-only integrity, the existing 652-assertion exact
closed-feedback regression, the prose checker and whitespace checks passed.
These checks do not certify the interrupted derivations. Manuscript/formal
checks and Lean builds were not run.

## Previous refinement checkpoint and discriminating results

RF3 remains incumbent, with independent alternatives and a smaller fresh
exploration allocation. The initial allocation was roughly half direct
refinement, one quarter competing mechanisms, one quarter fresh ideas;
reviewers were added as concrete candidates appeared. Slots are not filled
with duplicate estimates. The completed second period found these shared
unknowns:

- A shared-advector history comparison removes strain Gronwall and has an
  additive dissipation bound at each cutoff. Returning to the actual coarse
  flow leaves integral ||v w||2^2/nu and a cutoff cost. A new proof must
  control that actual mismatch jointly with source work.
- Full single-flow cubic band accounting retains triad cancellations but
  its present bound returns to integral ||grad U||2^4. Energy provides only
  the squared-gradient integral. A sharp-projector boundary example blocks
  one proposed low-strain estimate; smooth-filter implementations remain
  distinct repair candidates.
- A kinetic initial-layer corrector retains collision invariants and
  epsilon transport. Its relaxed production returns to the macroscopic
  cubic-gradient term. This coefficient calculation is not an actual
  kinetic trajectory theorem or a new critical estimate.
- Fresh heat-cubic and speed-superlevel pressure projections supplied
  exact testable objects. Present implementations lose coercivity or
  retain moving-boundary pressure; global reconstruction returns to the
  existing gradient quotient's signed defect. The broader mechanisms
  remain open at that additional obligation.
- A remote-pressure slow-record family is an unaudited candidate involving
  different smooth data and fixed record ratios near one. It does not
  extract a singularity from one datum or establish a dyadic-record
  obstruction. Universal nonrecurrent three-dimensional extraction and
  rigidity remain missing.

Restart-relevant derivations and scope qualifications are retained as
explicitly unaudited snapshots: paired history alignment, single-flow
cubic accounting, kinetic initial-layer production, slow finite records,
speed-level pressure and large-q production, all dated 2026-09-07 in
research/evidence. They are not canonical theorems. Routine exploratory
scratch is not canonical evidence.
Two returns to the same critical clock do not count as distinct progress.

The selected weaker target is now RF-q: sup_t sum a_j(t)^q for ONE fixed
finite q>3, say q=6, on every finite horizon. The complete synthesis and
classical continuation adapter are independently reviewed, including Phuc's
actual local hypotheses, normalized pressure, closed upper-time boundary
and control of spatial escape. See the Lorentz synthesis, continuation and
audit records in research/evidence. This removes an unnecessary ell3 demand
but produces no critical bound. q=infinity is not an accepted endpoint.

The large-q experiment supplies an actual high-component threshold
occupation bound and a bound on the rate of record crossings. It still
leaves exceptional-time concentration and resolved corrections; the energy
cost of a higher-scale crossing decays as N_j^(-1). The resulting geometric
sum cannot exclude infinitely many records by this argument. An actual
common-data family shows that one dominant increment can grow well above
nu for every finite q. Full-input-dependent barriers remain allowed.
These new producer derivations are retained with audit pending; they are
not promoted as obstructions to RF-q.

The smooth-block repair has passed independent review after two scope
corrections: its multiplier is smooth away from zero, and exact fixed-grid
scale invariance is dyadic. It retains the full projected equation even
when blocks cross the cutoff. Low/high transport now costs low strain
with an additional frequency-separation factor. Its comparable-scale
remainder still has no small factor and the current absolute estimate
returns to integral ||grad U||2^4. The full derivation and repair audit are
`2026-09-07-smooth-block-repair.md` and `2026-09-07-smooth-block-audit.md`.

The fresh helical lane also completed review after explicitly adding the
Leray projection to the Fourier-packet construction. Actual compact data
produce growth of both chiral energies while every radial signed-helicity
history vanishes. Actual pure-positive Schwartz data create negative
chirality at order t squared. These are scoped closure exclusions, not a
failure of all helical geometry or of an additional full-input bound.
See `2026-09-07-helical-production.md` and its audit record.

At the preceding checkpoint the bounded worker assignments were complete.
The selected next analytic assignment was a signed, phase-sensitive comparable-scale
commutator estimate in the smooth-block formulation, tested first on the
reflection-symmetric and chiral-birth families above. It must retain
angularly resolved vector correlations that signed radial budgets discard.
An estimate that merely returns to sup a times D or the squared-enstrophy
clock is not a new mechanism. The full-input finite-q producer remains the
terminal consumer; independent source review and mathematical audits do
not substitute for producing it.

Keep alternative mechanisms alive only when the next lemma offers a
structural gain, missing hypothesis or different proof attack. Temporal
reconstruction accuracy is not spatial refinement control. Staff kinetic,
representation or whole-space adapters only for a named advancing consumer;
microscopic completion and formalization remain downstream.

## Preserved exclusions and verification

The preceding wave's causal-series and metric results retain their original
pending independent-audit status. Preserve the exact exclusions for static
C2 slaving, mass-norm prefactor-one contraction, universal entire causal
series, polynomial metric conditioning and polynomial paired source-linear
costs. Real causal restart remains a finite-cutoff repair with nonuniform
costs. None refutes nonlinear input-dependent refinement or NS-R3.
The earlier entropy, covariance, Fisher, resonance, packet-scaling and
graph-lift obstructions retain their separate premises and reopening
conditions. No new symmetry, recurrence, Type-I or record-frequency
hypothesis is imposed on a general hypothetical singularity.

Freeze each complete candidate and its patch before fresh adversarial
review. Distinguish author proof, actual source inspection, independent
mathematical audit and formal verification. Refresh main, stage explicit
paths and use ordinary pushes; preserve concurrent edits. Run
`python3 research/verify.py --research-only`, `git diff --check`, and the
relevant existing finite algebra oracle. Structural checks and finite
regressions certify neither the new PDE implication nor terminal regularity.
The canonical graph and its status guard stay unchanged while the critical
producer remains missing.

The completed checkpoint checks passed: research-only integrity (29 canonical
records and eight historical pending supplements), both research graph
DAG/reference checks, the 652-assertion exact closed-feedback regression,
new proof/plan prose checks and whitespace. The verbatim smooth-block audit
retains one nonblocking phrase-checker finding; its original wording is
preserved for review provenance. The original PLAN is archived byte-for-byte;
the canonical graph and verifier are unchanged. Manuscript includes/labels,
formal manifests and Lean builds were outside the executed research-only
check. These check scopes do not certify the new mathematics.
