# Navier--Stokes: exact circuit and pressure-response obstructions

This is the sole live status record. The unchanged terminal target is the
original unforced incompressible equation on R3, every real solenoidal
Schwartz datum and every fixed positive viscosity. NS-R3 is NOT PROVED.
No singular solution or complete positive critical producer is established.

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: exact-original-operator-circuits-2026-09-08
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: conditional-manuscript-held-after-strategic-pivot
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: original-nonlinearity-critical-producer-unresolved
active_architecture: joint-comparable-frequency-source-and-response-unresolved
complete_terminal_route: none-established
terminal_status: not-proved
terminal_obstruction: input-only-critical-bound-not-produced
refinement_wave: reviewed-conditional-consumer-preserved
run_status: scoped-obstructions-committed-terminal-producer-unresolved
averaging_gate: exact-proof-assumptions-not-lane-names
averaging_audit: preceding-proof-repair-required
averaging_repair: author-proof-independent-audit-pending
incumbent_producer_class: averaging-invariant-budgets-remain-excluded
circuit_results: author-proof-independent-audit-pending
immediate_fractional_leakage: refuted-in-stated-varying-input-class
clean_six_carrier_embedding: refuted-in-stated-pairwise-clean-ring-class
side_ring_automatically_stabilizes: refuted-at-initial-critical-curvature
indefinite_original_ns_cascade: neither-constructed-nor-excluded
local_pressure_restoring_sign: refuted-with-arbitrary-remote-trace-free-hessian
pressure_results: author-proof-independent-audit-pending
secondary_goal: MIC-R3
secondary_goal_status: kinetic-and-microscopic-interfaces-remain-separately-gated
formal_work_this_run: deferred
public_release: false
```

## 1. New mathematical results, with exact scope

Evidence: `research/evidence/2026-09-08-exact-circuit-obstructions.md`.
These are mechanism obstructions, not an input-only critical estimate.
Independent mathematical review is pending; no canonical node is promoted.

**Critically large birth need not have an immediate fixed leakage fraction.**
For every nu>0, L>0 and eta>0, a real Schwartz datum and an actual time
exist for which the neighboring whole-space error e=u_(2N)-u_N, N=6/5,
has N^(1/2)||J e||2>=L but ||(I-J)e||2<=eta||J e||2.
J selects the forward pair of packets. All resolved response is counted
in I-J. The original unprojected NS nonlinear increment has the same
property. The proof uses an exact two-carrier cancellation, a solenoidal
Schwartz packet lift, and uniform input-only short-time estimates after
amplitude rescaling. The datum varies: this does not exclude a cost
depending on that full datum, a full-turnover result, or a many-cell theorem.

**A clean six-carrier NS gate has a stronger omitted ring.**
For the equal-amplitude conical hexagon, pairwise cancellation of every
difference daughter forces a common helical mixture (or pure azimuthal
polarization). Except at the Beltrami zeros, full Leray convolution creates
both an intended adjacent-sum ring and an omitted step-two ring, with

    ||Q_side||2^2/||Q_intended||2^2
       =3(z^2+3r^2/4)/(z^2+r^2/4)>3.

Individual phases and the common helical parameter cannot remove the side
ring while retaining the target. On Miller's iterative carrier geometry
the ratio decreases from 27/7 to 3. Narrow common Schwartz packets retain
this obstruction. This quantitatively forbids dropping those daughters;
it does not say that leakage dissipates their energy or blocks all cascades.

**The side ring initially contributes positively to critical curvature.**
For a spherical parent set of radius R, the exact nonlinear critical
curvature, including parent back reaction, is

    sum_k (|k|-R)|Q_k|^2.

Both daughter rings in the hexagon have |k|>R. The positive sign survives
the Schwartz lift, and large-amplitude original NS data have an actual
short interval of critical-norm growth at every fixed viscosity. Thus a
forcing-norm lower bound on leakage is not already a stabilizing signed
estimate. No sustained singular cascade follows from this short-time test.

**Three-carrier closure also fails explicitly.** The full second derivative
of the e1,e2,e3 meridional circuit contains 24 modes, including all parent
responses, repeated-index daughters, and mixed-sign daughters. Its intended
complementary-sum recurrence collapses angles toward a common axis, but
this recurrence alone is not the exact full trajectory.

**The complete local velocity germ does not determine a restoring pressure
sign.** `research/evidence/2026-09-08-remote-pressure-control.md` proves
that any symmetric trace-free perturbation H of the canonical pressure
Hessian at zero is realized EXACTLY by at most two disjoint remote compact
swirls, leaving all velocity derivatives near zero unchanged. Their energy
cost is O(L^5 lambda_max(H)) at distance L; no fixed-input estimate is
refuted. On actual fixed-viscosity local NS branches the corresponding
initial material vorticity acceleration changes by -H omega. This remains
true at maximal positive strain alignment. Only instantaneous local-germ
closure/restoring-sign mechanisms are excluded, not a nonlocal temporal
response theorem. This extends the existing compact-swirl kernel method,
not a claim of priority for remote pressure influence.

The previous live PLAN is preserved byte-for-byte at
`research/history/PLAN-before-exact-circuit-2026-09-08.md`, using original
Git blob `a2b12a98bd2b5b11dfb41e741d34297134150cf1`. The older history
and all preceding evidence remain in place, not overwritten.

## 2. Unchanged complete conditional consumer and first terminal gap

For N_j=2^j N0, e_j=u_(N_(j+1))-u_(N_j), a_j=N_j^(1/2)||e_j||2,
fix any one finite q>3. The reviewed sufficient output is

    sup_(0<=t<=H) sup_M sum_(j<M) a_j(t)^q < infinity,

with the bound depending arbitrarily on the full datum, nu, H, N0 and q.
The exact identity remains

    (1/q) Wq_M' + nu Dq_M = Piq_M,
    Piq_M=sum_j N_j^(q/2)||e_j||2^(q-2)
                  [<F_j,e_j>-b(e_j,u_j,e_j)].

The first TERMINAL lemma is still an input-only bound, for every upper
time t<=H and uniformly M, on

    integral_0^t Piq_M - nu integral_0^t Dq_M.

Its proof would give RF-q by integration, uniform L^{3,q} by
`2026-09-07-lorentz-synthesis.md`, the same bound on the classical branch
by compact-classical identification, and continuation by
`2026-09-07-lorentz-continuation.md`; LOCAL and ENERGY complete NS-R3.
No bound on an unknown future strain clock may be inserted into this chain.

The pressure and material lanes did not produce a competing terminal
estimate. The exact material vorticity equation preserves a nonlocal
Hessian term and leading viscous correlations; the remote-control theorem
prevents assigning that term a sign from local alignment alone. A metric
change that returns to unknown deformation/strain costs is not a new
producer, and the previously recorded conditioning obstruction remains
in force. No new Liouville class excluding the old shear tangents was
obtained. These limitations are not an exclusion of all remaining routes.

The more concrete next CIRCUIT question is the signed joint response of
the intended and side rings, with all cross-generation modes retained.
The forcing ratio above is not that response theorem. In addition, no
reduction of arbitrary blowup to symmetric hexagons is available. Solving
only this circuit question must not be advertised as closing NS-R3.
A general proof still requires a genuine trajectory mechanism operating
on the actual full refinement family, not a universality assumption.

## 3. Tao discriminator, prior art, and preserved exclusions

Use the exact k=p+q relation and full divergence-free Leray numerator.
The new ring coefficients and mandatory daughter sets are concrete
identities that Tao's assigned local-cascade coefficients need not obey.
A positive proof must additionally show how its discriminator controls
signed critical work; structural difference alone does not suffice.

The corrected averaged-only packet obstruction remains
`research/evidence/2026-09-08-tao-packet-audit-and-repair.md`, with its
independent audit pending. The superseded argument at
`2026-09-08-averaging-obstruction-rf-q.md` is explicitly a corrigendum.
In particular finite L^{3,q} is not silently upgraded to L3, independent
dilations belong to Tao's published averaging class, and no original-NS
continuation theorem is applied to his averaged equation.

The following earlier scopes remain unchanged: static C2 slaving fails
at a nonzero heat-rate resonance; a single zero-centered entire causal
series fails in the recorded closed Galerkin sector; polynomial moving
metric and source-linear response costs fail in the specified family;
shear/affine/inviscid tangents prevent the earlier blanket rigidity
suffixes; signed radial helicity misses common chiral production.
These exclusions do not refute nonlinear input-dependent costs, all
causal reconstruction, the kinetic programme, FEEC, or arbitrary-data RF-q.
Smooth-block low-transport repair and separated-scale feedback estimates
remain valid in their reviewed scopes; their comparable-frequency gap
has not been filled.

Direct primary-source inspection also checked Kishimoto--Yoneda's
finite-mode classification and Miller's exact carrier definitions,
ordinary-viscosity regularity result for his restricted model, and his
explicit non-invariance warning. Those are prior art, not new claims here.
The new work computes the omitted-source ratio and the scoped consequences
for the original operator; it never evolves the restricted model as NS.

MIC-R3 and kinetic/hydrodynamic/domain interfaces remain separately gated.
No advancement, retirement, or manuscript/formal change is asserted there.

## 4. Verification and commit discipline

`python3 research/check_exact_ns_circuits.py` passed 54 exact assertions:
full ordered convolution, complete first/second supports, reality,
solenoidality, energy/helicity, five exact hexagon levels, and symbolic
polarization identities. The reproducible script is committed with the proof.
`python3 research/check_remote_pressure.py` additionally passed 45 exact
assertions covering the Newton kernel, harmonic trace, swirl solenoidality,
spectral assembly, input-energy weights, affine extension, maximal alignment,
and material/Laplacian commutation. Both scripts were rerun successfully.
The combined count is 99 exact assertions, not an independent mathematical
review or numerical validation of a PDE theorem. No agent spawning or
external review is claimed.

The repository was accessed through the GitHub connector at immutable
revisions. A full local checkout was unavailable. The full command
`python3 research/verify.py --research-only` has NOT been run in this wave;
its status must not be inferred from the exact arithmetic checks.
Whitespace and PLAN YAML checks are performed in a changed-file local
snapshot; this is narrower than a checkout-wide regression. No Lean or
manuscript build is claimed. Prior-run counts in archived records are
historical, not tests rerun by this wave.

Refresh main before each remote write. Use the current base tree and
ordinary fast-forward updates only, retaining concurrent work. Commit
mathematical progress with this live record; do not promote a theorem
because the finite regression passes. Independent review is still needed
for the packet/Taylor arguments and the scope of every branch exclusion.
