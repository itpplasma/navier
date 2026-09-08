# Navier--Stokes: kinetic regularity and Newtonian-to-fluid programme

> **Public status (2026-09-08).** This repository was made public on the day
> OpenAI released a forced finite-time-blowup theorem (Clay alternatives C/D)
> with a Lean certificate, as a documented record of what this programme did
> before and after that release. It is a research notebook: every proof here
> is author-level unless a file is explicitly marked as an independent audit,
> nothing is promoted beyond the status recorded in `docs/proof-graph.yaml`,
> and no priority, prize or publication claim is made. **The arbitrary-data
> theorem (alternative A) is not proved, and no unforced counterexample is
> constructed.** Licences: Apache-2.0 for code, CC BY 4.0 for prose
> (`LICENSE`). Companion Lean repository: `itpplasma/navier-formal` (public).
> The manuscript repository `navier-paper` stays private for now.

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
`itpplasma/navier-formal` owns Lean and formal coverage. Existing Phase I/II status is unchanged.
No new paper theorem, Lean proof, priority result or independent audit is claimed.

On a full checkout, run `python3 research/verify.py --research-only` and
`git diff --check`. The default verifier additionally requires the paper and
formal checkouts. These are integrity checks, not mathematical certification.
Preserve concurrent work and use non-force updates; unsigned commits are
authorized; `navier` and `navier-formal` are public since 2026-09-08. No release, submission, outside
contact or recreation of the deleted Overleaf project is authorized.

## Blockers for anyone continuing this work (2026-09-08)

Read `PLAN.md` Sections 1, 1a, 1b, 3, 4 and 8 first. The concrete walls are:

1. **The critical estimate.** The positive route is fully reduced (paper and
   Lean) to one finite-horizon `L³` bound for arbitrary Schwartz data,
   `hyp:critical` (equivalently the signed high-frequency pressure or
   high-strain hypotheses). No producer exists. Any candidate must use
   unforcedness in an essential way: an argument that survives a smooth
   compactly supported force from zero datum is refuted by OpenAI's theorem
   (`research/evidence/2026-09-08-forced-insensitivity-falsifier.md`).
2. **Free-trace realization of the pulse family.** On the negative route,
   removing OpenAI's force from its concentrating architecture is excluded
   for every relabelling shortcut (compact support, exact patches, exact
   label separation, trapped preload; `PLAN.md` Section 1b) but not for an
   overlapping, continuously preloaded cascade. The first missing theorem is
   one Schwartz datum realizing all pulse traces with exponentially small,
   sign-controlled overlap seeding (Theorem C of
   `research/evidence/2026-09-08-forced-type-rigidity.md`); energy identities
   cannot decide it, so a sign or realizability argument is needed.
3. **Independent audits.** Every 2026-09-08 note except
   `2026-09-08-obstruction-audit.md` is an author proof with audit pending;
   the audit itself asks for two hypothesis repairs in the analyticity lemma.
4. **Verifier.** `python3 research/verify.py --research-only` passes on this
   checkout; the full three-repository mode needs the private manuscript
   checkout and currently fails on a pre-existing manuscript label
   (`dc:l9`), unrelated to the public content.
5. **Formal residuals** are listed in the README of `itpplasma/navier-formal`
   (Hessian--Laplacian identity, endpoint hypotheses, difference-quotient
   limit, Leray--Hopf class, local theory Phase II).
