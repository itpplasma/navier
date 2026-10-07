# Current research: relativistic closure failure versus actual PDE blow-up

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
active_task: RNS-BDNK-physical-admissibility-versus-singularity
companion_status: author-proofs-independent-review-pending
companion_results:
  - research/evidence/bdnk-virial-20261007.md
  - research/evidence/bdnk-kinetic-exit-20261007.md
next_distinct_producer: actual-PDE-breakdown-or-controlled-hot-core-continuation
new_results_audit: author-only-no-independent-promotion
```

## Full-PDE physical obstruction

The [virial packet](research/evidence/bdnk-virial-20261007.md) gives explicit
smooth unforced full-3D BDNK data in frame A: a temperature-32 hot plateau
inside radius R/2 returning to a positive constant background outside R,
with zero initial velocity and ideal-Euler-compatible time derivatives.
All first constitutive corrections vanish initially.

Trace-free stress conservation gives I(t)=I(0)+2F(0)t+E t^2. The background
characteristic speed is below 0.9, so a smooth perturbation remains inside
radius R+0.9t. By time 20R, positivity of laboratory energy contradicts this
virial identity. Classical/admissible continuation therefore fails OR negative
energy appears with the stated quantitative bound. This does not select a
shock. Initial gradient measures can be arbitrarily small; a large-flat-torus
version has finite total energy. The argument extends to strictly causal
conformal frames after adjusting amplitude, but not to luminal frame B.
The nonlinear background-front support adapter remains a review obligation.

## Actual smooth exit from the positive-particle stress cone

The [kinetic-exit packet](research/evidence/bdnk-kinetic-exit-20261007.md) now
constructs a different analytic periodic family. Its complete initial stress
is realized by a smooth nonnegative massless particle distribution, and its
canonical entropy production is nonnegative initially. All four unforced BDNK
conservation equations are retained. The local classical solution develops
negative directional pressure while temperature, timelike velocity and all
derivatives stay bounded. This applies to frame A AND luminal frame B; the
coefficient calculation extends across the stated positive causal family.

A global free-streaming kinetic solution has the same full initial stress
and always nonnegative directional pressure, giving a precise stress-level
model separation. It is NOT a finite-viscosity kinetic derivation of BDNK,
a Maxwell-Landau theorem, or a claim about every microscopic theory.
The new data have order-one shear anisotropy; they are not small-inverse-Reynolds
preparations. The hot-core and kinetic-exit families cannot be combined into
one stronger statement. Actual shock formation for the hot cores is unproved.

Executed this round: 31 + 48 exact SymPy checks, both Python compilations and
new-file integrity checks. Actual logs and source hashes accompany each result.
No independent reviewer, full repository tests, Lean, Comparator, LaTeX or CI.

## First unresolved implication

The physical claims are now separated: strict-front conformal BDNK cannot
preserve smooth positive-energy evolution for every ideal-prepared hot core;
even luminal BDNK can smoothly leave the positive classical kinetic stress cone
from physically realizable anisotropic data. Neither is an unconditional
BDNK PDE singularity theorem. Determine which alternative the actual hot-core
dynamics take, or derive an exact coupled steepening mechanism. Positivity
propagation cannot be assumed as a shortcut.

The [companion contract](research/relativistic-breakdown-contract.md) retains
the full nonlinear steepening problem and its falsifiers. This PLAN records
the newer pivots and allocation. Fresh independent reconstruction is required
before any mathematical promotion. No canonical graph node is promoted.

## Earlier transfer and classical targets

The [earlier transfer](research/evidence/bdnk-transfer-20261007.md) excludes a
weighted-C2 accelerating similarity class, derives causal shear damping and
rejects a scalar transverse-shear shortcut. Its 121-check receipt and pending
review status are unchanged; it is not used to prove the new results.

NS-R3 remains unforced incompressible Navier-Stokes on R3 with Schwartz data.
Its positive route lacks a critical/Lorentz estimate; its negative route lacks
one initial trace realizing an unforced viscous history and retaining a
singularity. No edits to jc2, navier-formal, or vlasov-maxwell were made.
