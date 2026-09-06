# Navier--Stokes: kinetic regularity and Newtonian-to-fluid programme

Private research on the original three-dimensional incompressible
Navier--Stokes problem. **The arbitrary-data theorem is not proved.**

Start with [PLAN.md](PLAN.md), the sole live allocation/status record, then
[the proof dossier](docs/proof.md). The programme now distinguishes three
endpoints: unchanged whole-space Clay regularity (NS-R3), a regular kinetic
hydrodynamic realization (KIN-R3), and a scoped dilute-gas Newtonian-particle
realization of that fluid limit (MIC-R3). The last has additional particle-
class and infinite-volume obligations; it is not all of Hilbert's sixth problem.

## Current mathematical task

Prove an input-derived critical bound on the limiting macroscopic momentum,
using the interaction of kinetic transport and momentum-conserving collisions.
The first attack is the nonlinear stress remainder after the known Maxwellian
correction. A limit-first, resolved-momentum estimate suffices; uniformly
smooth finite-Knudsen solutions are not a prerequisite for the Clay route.
Nonlinear dual observability and transport-coupled information are alternatives,
not extra unproved theorems silently appended to that route. Stafford/Weyl
geometry is useful only through a quantitative estimate consumed by this task.

The known local theory, energy identity and endpoint continuation are retained.
The old pressure/quotient/defect/shell/material-response family is retired as
the primary producer, not deleted or declared mathematically invalid.

## Programme and evidence

- [Endpoint and limit contracts](research/kinetic-clay-hilbert-contracts.md)
  specify quantifiers, observables, scaling, microscopic compatibility and
  acceptance tests.
- [Programme dependency map](docs/programme-graph.yaml) lists unproved tasks
  and conditional interfaces. It is NOT the audited proof graph.
- [Canonical proof graph](docs/proof-graph.yaml) retains all existing claim
  statuses. NS-R3 and CRITICAL remain gaps; no kinetic claim is promoted.
- [Preserved kinetic calculations and rejection tests](research/evidence/2026-09-06-kinetic-plan-contracts.md)
  define the nonlinear remainder, K_res and the operator/geometric safeguards.
- [Kinetic/Hilbert source-scope ledger](literature/kinetic-hilbert-scope.md)
  distinguishes weak limits, smooth-target limits and particle theorems.
  [Earlier literature dossier](literature/README.md) remains available.

The completed structural-obstructions paper is author-level work with its
independent-review and prior-art qualifications; see its
[audit](research/evidence/2026-09-06-structural-obstructions-paper-audit.md).
The [previous README](research/history/README-before-clay-hilbert-programme-2026-09-06.md)
retains the detailed earlier paper checkpoints. They are history, not the
current task queue.

## Repository and verification boundaries

`itpplasma/navier` owns research, contracts, evidence and claim status.
`itpplasma/navier-paper` owns manuscripts and generated paper maps;
`itpplasma/navier-formal` owns Lean and formal coverage. This programme update
changes only the research repository. Existing Phase I/II status is unchanged.
No new paper theorem, Lean proof, priority result or independent audit is claimed.

On a full checkout, run `python3 research/verify.py --research-only` and
`git diff --check`. The default verifier additionally requires the paper and
formal checkouts. These are integrity checks, not mathematical certification.
Keep all repositories private, preserve concurrent work and use non-force
updates; unsigned commits are authorized. No release, submission, outside
contact or recreation of the deleted Overleaf project is authorized.
