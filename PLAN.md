# Current research: forcing-status comparison and the relativistic PDE frontier

Updated 2026-10-07. This is the sole live task/status record. The active
allocation is the user-requested relativistic companion. The original unforced
whole-space NS-R3 target and its accepted proof graph are unchanged.

The forcing status is an explicit invariant of every comparison:

| Model | Forced smooth-data finite-time singularity | Unforced smooth-data finite-time singularity |
| --- | --- | --- |
| classical incompressible Navier--Stokes | **YES:** released OpenAI construction with smooth forcing | **OPEN here:** no unforced counterexample and no arbitrary-data regularity proof |
| conformal causal BDNK | **OPEN:** no relativistic finite-time singularity construction yet | **OPEN for actual PDE singularity:** author results show smooth closure/kinetic-cone failure and a virial breakdown-or-negative-energy disjunction |

The apples-to-apples sequel to the released classical theorem is therefore the
**forced BDNK problem**. The unforced BDNK problem remains important, but it is
not the relativistic analogue of a solved unforced classical theorem.

The complete earlier classical plan is preserved byte-for-byte at
[research/history/PLAN-before-bdnk-transfer-20261007.md](research/history/PLAN-before-bdnk-transfer-20261007.md).
Its evidence, controls, author statuses and formal provenance remain available.

```yaml
terminal_claim: NS-R3
terminal_status: not-proved
unforced_counterexample: not-constructed
complete_terminal_route: none-established
checkpoint: CP1
public_release: true
formal_status: "Unchanged: partial classical formal interfaces; arbitrary-data critical producer and stated regularity bridges remain open. No new Lean replay."
active_target: RNS-BDNK-companion
active_task: RNS-BDNK-F001-forced-singularity-or-exact-relativistic-no-go
companion_status: author-proofs-independent-review-pending
companion_results:
  - research/evidence/bdnk-virial-20261007.md
  - research/evidence/bdnk-kinetic-exit-20261007.md
  - research/evidence/bdnk-euler-prepared-exit-20261007.md
next_distinct_producer: smooth-forcing-BDNK-singularity-construction-or-exclusion-of-a-nonempty-forced-collapse-class
classical_ns_forced_status: released-external-smooth-forcing-breakdown
classical_ns_unforced_status: open
bdnk_forced_status: open
bdnk_unforced_pde_singularity_status: open
new_results_audit: author-only-no-independent-promotion
```

## Strongest constructive result

The [Euler-prepared exit theorem](research/evidence/bdnk-euler-prepared-exit-20261007.md)
constructs common analytic Cauchy data across conformal causal BDNK frames at
fixed positive shear viscosity. A0=Q0=0 everywhere; the initial full stress is
realized by a smooth positive massless particle distribution and has nonnegative
canonical entropy production. The full unforced solution becomes negative in
one directional pressure during its smooth local lifespan. Temperature and all
derivatives remain bounded; the dominant energy condition and positive entropy
production still hold at the exit point. This applies to frame A and luminal
frame B, with the stated fixed-frame/finite-frame-set quantifiers.

This completes an author proof of failure to preserve the positive CLASSICAL
KINETIC matter-stress cone. It does not prove PDE blow-up or global regularity.
The initial shear anisotropy is order one. Small velocity amplitude, Euler
preparation and A0=Q0=0 do not imply small inverse Reynolds number.

A globally smooth positive free-streaming massless model realizes the same
initial stress and never develops negative directional pressure. This is an
exact stress-level separation, NOT a finite-viscosity hydrodynamic derivation,
a Maxwell-Landau result, or a statement about all quantum/interacting matter.
Electromagnetic field tension lies outside the matter-stress test used here.

## Complementary global physical obstruction

The [virial packet](research/evidence/bdnk-virial-20261007.md) uses a DIFFERENT
initial family: an ideal-stress hot plateau, temperature 32 times background,
zero velocity and Euler-compatible derivatives. It has arbitrarily small
initial gradient measures after scaling. Trace-free conservation and a strictly
subluminal equilibrium front force breakdown OR negative laboratory energy by
time 20R in frame A. A torus version has finite total energy. The result applies
to strictly causal conformal frames, not the luminal case. The nonlinear
background-front adapter is a load-bearing independent-review item.

The new report also gives an explicit trace budget for a nonconformal repair,
and an observer-uniform constitutive-correction bound: a smooth hot-core
continuation must leave the regime Rcorr<1 before the deadline. Do not combine
the ideal hot-core data with the anisotropic kinetic-exit data into one theorem.

## Research frontier and verification

The [current contract](research/relativistic-breakdown-contract.md) now puts the
**forced BDNK singularity problem first**, because that matches the forcing
status of the released classical Navier--Stokes counterexample. The target is
to construct smooth BDNK data and a smooth covariant source producing finite-time
loss of classical regularity, or to prove an exact obstruction for a nonempty
forced-collapse class.

The existing transfer result already gives a substantial obstruction: the
direct proper-velocity lift of the OpenAI shrinking vortex is incompatible with
the full BDNK energy equation throughout a weighted-C2 slow-shrinking class
unless the relativistic completion cools at least at the stated power or leaves
the hypotheses. A bounded smooth source cannot repair the leading mismatch.
Independently, causal BDNK shear loses the parabolic high-frequency
`exp(-nu k^2 t)` suppression used by the classical pulse design: the exact
high-k damping rate saturates at a constant. Thus the classical forcing
architecture is not structurally robust under this causal relativistic
completion. This does **not** prove that no different smooth relativistic
forcing can produce singularity.

The previous unforced hot-core alternative remains a secondary target. Its
virial disjunction does not select singularity versus negative energy, while
the pressure-exit theorem proves smooth loss of kinetic realizability for a
different data family.

This round executed 117 distinct exact algebra checks (31+48+38), replayed all
three checkers, compiled them, and checked new-file integrity. Actual logs and
hash receipts accompany the proofs. No independent reviewer, repository-wide
tests, Lean, Comparator, LaTeX or CI run is claimed. Mathematical promotion
requires fresh reconstruction. No canonical proof-graph node is promoted.

The earlier [similarity-transfer packet](research/evidence/bdnk-transfer-20261007.md)
and its 121-check historical receipt remain unchanged and are not prerequisites
for the new theorems. The first heat-flux example remains a useful earlier stage;
a prose-only rest-frame heat-scalar typo was corrected with its hash receipt.

## Classical and sibling targets remain separate

NS-R3 remains unforced incompressible Navier-Stokes on R3 with Schwartz data.
Its critical/Lorentz producer and one-trace unforced blow-up construction remain
missing. No edits were made to jc2, navier-formal, or vlasov-maxwell. The neutral
conformal comparison has no proved massive Newtonian or collisional kinetic
adapter; it cannot settle those sibling targets by analogy.
