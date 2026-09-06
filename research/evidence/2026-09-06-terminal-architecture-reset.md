# Terminal architecture reset: marked ancient limits and failed-bridge counterexamples

Date: 2026-09-06.

Status: research evidence, with derivations checked by their author; independent mathematical audit pending. This note does **not** prove arbitrary-data Navier–Stokes regularity. It establishes a scoped blow-up extraction bridge and explicit counterexamples to proposed intermediate inferences. The comparison fields and the polynomial ODE below are **not** Navier–Stokes counterexamples. No novelty claim is made for the arguments or their ingredients.

## 1. Frozen inputs and decision

The research input is `itpplasma/navier` at `c2c5f793d1e447a82dd99c7e434c76fc989ec316`. The manuscript input is `itpplasma/navier-paper` at `81f0cd1524e8a625e6ee46970d69e40e5a2e50bf`. The research head was refreshed and remained unchanged before preparing this patch. The inspected research files include `AGENTS.md`, the terminal dependency graph, `docs/proof.md`, the relevant historical and current portions of `PLAN.md`, `research/verify.py`, and the complete `research/evidence/compactness.md`. The manuscript abstract, equation, data class, target, and README were also inspected.

**Decision: retire the pressure/quotient/defect/speed-shell/material-response producer family as the primary arbitrary-data research route.** Preserve its valid conditional mathematics and its audit history. Retirement here is a research decision supported by repeated failures of closure, not a proof that no future theorem using pressure or a quotient can work. The spectral-reference hierarchy is also not an approved replacement: its existing success-index assertion was audited as equivalent to continuation.

No unconditional replacement architecture is approved by this note. The mathematical work retained is the marked-ancient extraction of Section 5, the minimal-initial-data obstruction of Section 4, and the energy-exact slow-growth/deformation countermodel of Section 6. No theorem in the main claim graph is promoted. No manuscript extension or formalization is justified by the present delta.

**Delivery reconciliation.** While this record was being transported, `main` advanced to `7425786324179a88dd83f5bff9f5da3f438b38e3`, which already performs the strategic retirement and selects intrinsic Hölder-record increments with fixed-input ancestry as the live architecture. This dossier therefore does **not** replace or modify the new PLAN. Its role is narrower: preserve independent falsifiers and a marked-velocity-record extraction showing exactly why several tempting predecessor routes still do not close the theorem.

## Detailed derivations

- [Terminal gap and common obstruction](terminal-reset/01-terminal-gap.md)
- [Architecture ledger: ten distinct routes](terminal-reset/02-architecture-ledger.md)
- [Minimal-data compactness falsifier](terminal-reset/03-minimal-data.md)
- [Two-time-marked ancient extraction](terminal-reset/04-marked-ancient.md)
- [Slow-record/deformation countermodel](terminal-reset/05-countermodel.md)
- [Decision, verification limits, and references](terminal-reset/06-decision-verification-references.md)

The split is organizational only; the linked files are the complete continuation of this record.
