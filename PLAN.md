# Current research: relativistic physical breakdown and the retained NS-R3 target

Updated 2026-10-07. This is the sole live task/status record. The active
allocation is the user-requested relativistic companion. The original unforced
whole-space NS-R3 target and its accepted proof graph are unchanged.

The complete earlier classical plan is preserved byte-for-byte at
[research/history/PLAN-before-bdnk-transfer-20261007.md](research/history/PLAN-before-bdnk-transfer-20261007.md).
Its controls, author statuses, source adapters and formal provenance remain
available; the relativistic work neither completes nor retracts that work.

```yaml
terminal_claim: NS-R3
terminal_status: not-proved
unforced_counterexample: not-constructed
complete_terminal_route: none-established
checkpoint: CP1
public_release: true
formal_status: "Unchanged: partial classical formal interfaces; arbitrary-data critical producer and stated regularity bridges remain open. No new Lean replay."
active_target: RNS-BDNK-companion
active_task: RNS-BDNK-physical-breakdown-versus-actual-singularity
companion_status: author-proofs-independent-review-pending
companion_result: research/evidence/bdnk-virial-20261007.md
next_distinct_producer: distinguish-PDE-breakdown-from-smooth-energy-condition-exit
new_results_audit: author-only-no-independent-promotion
```

## New full-PDE physical obstruction

The [virial packet](research/evidence/bdnk-virial-20261007.md) gives explicit
smooth unforced full-3D BDNK data in frame A: a hot plateau of temperature
32 times a constant positive background inside radius R/2, smoothly returning
to background outside R, with zero initial velocity and ideal-Euler-compatible
time derivatives. All first constitutive corrections vanish initially.

Trace-free stress conservation gives I(t)=I(0)+2F(0)t+E t^2. The background
characteristic speed is below 0.9, so a smooth perturbation remains inside
radius R+0.9t. By time 20R, positivity of total laboratory energy contradicts
the virial identity. Thus classical/admissible continuation fails OR a
quantified amount of negative energy density appears. The latter is a real
alternative, not an already-proved shock. Initial gradient measures can be
arbitrarily small. A large-flat-torus version has finite total energy.

The argument applies to strictly causal conformal frames after adjusting the
amplitude. It does not exclude luminal frame B: its fastest characteristic is
exactly 1. This is a difference in the obstruction, not a proof of global
regularity for B. The nonlinear background-front support lemma, theorem
scope, and constitutive adapter require fresh independent reconstruction.

Executed: 31 exact SymPy checks, Python compilation, and new-file integrity
checks. The actual log and source hashes accompany the result. No independent
review, repository-wide tests, Lean, Comparator, LaTeX or CI were run.

## Earlier result retained

The [transfer packet](research/evidence/bdnk-transfer-20261007.md) excludes a
weighted-C2 slow-shrinking accelerating proper-velocity similarity class with
noncooling temperature, even under smooth forcing. It also derives the exact
causal shear spectrum and rejects a scalar nonlinear transverse-shear shortcut.
Its 121-check receipt and author-only status remain unchanged. The present
virial argument does not assume this earlier exclusion.

## First unresolved implication

The new disjunction settles failure of unrestricted globally smooth,
positive-energy evolution in its stated data class, but does not settle
unrestricted BDNK mathematical global regularity. Determine whether the actual
BDNK dynamics force a singularity, or instead permit smooth passage into
negative energy. Do not infer positivity propagation from the initial data,
entropy language, or causal hyperbolicity. Luminal frames and a kinetic
completion need their own exact equations and adapters.

The next calculations should test this distinction, not merely sharpen a
conditional continuation criterion. The companion contract remains at
[research/relativistic-breakdown-contract.md](research/relativistic-breakdown-contract.md);
this PLAN records the newer virial pivot and current allocation.

## Classical and sibling targets

For fixed nu>0, NS-R3 remains unforced incompressible Navier--Stokes on R3
with divergence-free Schwartz data. The positive route lacks an input-derived
critical/Lorentz bound; the negative route lacks one initial trace realizing
an entire unforced viscous history and preserving its singular observation.
Neither was supplied here. No canonical graph node or formal theorem is promoted.
No edits were made to jc2, navier-formal, or vlasov-maxwell. The kinetic sibling
owns the independent collisionless RVM reconstruction and collisional work;
it is not a proved kinetic realization of BDNK.
