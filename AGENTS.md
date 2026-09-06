# Agent rules

`PLAN.md` is the sole live status and task record. Read it, the claim graph
`docs/proof-graph.yaml`, and `research/verify.py` before long-horizon work.
The controller alone integrates evidence, edits authoritative state, and
promotes claims. Workers own explicitly assigned evidence files only.

Use the math-frontier discipline. Stop at the first unsupported implication;
retain valid conditional conclusions. Distinguish the original unforced
three-dimensional equation from forced, averaged, hyperdissipative, Euler,
and weak nonunique variants. State domains, data, quantifiers, and solution
classes for every imported result. No unproved project step is literature.

## Repository split

| Content | Repository |
| --- | --- |
| Research history, evidence, reviews, claim graph, live status | private `itpplasma/navier` (this repository) |
| Manuscript, bibliography, generated proof map | private `itpplasma/navier-paper` |
| Lean 4 formalization, Palomar interface, formal coverage records | private `itpplasma/navier-formal` |

The split mirrors `../stafford38`, `../stafford38-paper`, and the planned
`stafford38-formal`. Reusable application-independent analysis may later move
to a separate library; until then it lives in `navier-formal` under a clearly
generic namespace. Never vendor Mathlib or copy third-party Lean code without
its licence.

## Models and parallel work

The parallel workflow uses Claude models exclusively. No OpenAI, Codex, local
or other-vendor model is delegated to. Historical evidence files that name
Luna or Sol workers record past runs and are not routing instructions.

| Role | Model | Use |
| --- | --- | --- |
| Controller | Fable 5.1 (session model) | integration, promotion, authoritative edits |
| Analysis, discovery, audit | Fable 5.1 | proofs, falsifiers, repairs, mathematical reviews |
| Extraction, probes, Lean implementation | Opus 5 | source extraction, arithmetic, reproducible scripts, specified Lean modules |
| Mechanical | Sonnet 5 or Haiku 4.5 | formatting, bounded searches, replay scripts |

One model cannot reliably see its own mistakes. Within the Claude family,
the reviewer of a candidate runs on a different tier than its author, or at
least in a fresh context with a distinct adversarial lens. Never ask several
workers the same unresolved question with cosmetic rewording; parallel lanes
are different mechanisms, falsifiers, repairs, or abstractions. Idle capacity
is preferable to correlated duplication. Workers never edit `PLAN.md`,
`docs/`, or the manuscript, and never promote their own results.

## Phases

Phase I proves every manuscript-owned step in Lean down to exactly stated,
directly verified published literature theorems, recorded as clearly labelled
axioms with source records. Phase II discharges those statements from Mathlib.
Both phases were authorized by the user on 2026-09-05 for the checkpoint
block CP1 defined in `PLAN.md`. The same day the user re-sequenced to
paper-proofs-first. **On 2026-09-06 the user re-sequenced again, and this
supersedes both: formalization is reopened, paper proofs are supplied
externally, and the goal is to reach Phase II everywhere.** A conditional
terminal theorem does not settle the Millennium problem, and no Lean result
is promoted in the claim graph without a faithfulness audit of its statement.

Work happens in **this repository and `../navier-formal` only**. `../navier-paper`
is now **read-only**: pull it to stay current, never edit or commit to it.
Pull all three repositories regularly and push often.

**External dependencies are permitted** when they introduce **no axioms beyond
Mathlib's**. The gate is mechanical and must be run before any dependency is
added and again before any result relying on it is recorded: `#print axioms` on
every downstream theorem must yield a subset of `propext`, `Quot.sound`,
`Classical.choice`. A dependency that fails this is rejected regardless of
convenience, since Palomar compatibility depends on it.

Freeze coherent review inputs by exact commits, or a base commit and patch
SHA-256 including new files. Obtain independent mathematical audits before
promoting proof claims. Structural checks are not mathematical tests.

## Boundaries

Keep this repository, `../navier-paper`, and `../navier-formal` private. No
contact with others, public release, submission, Palomar registration, or
invented authorship. Literature consists of source metadata and original
notes, not third-party PDFs. Do not commit generated PDFs, TeX auxiliaries,
Lean build products, caches, or credentials. Preserve unrelated edits, stage
explicit paths, and push verified checkpoints regularly.

Run `python3 research/verify.py` and `git diff --check` for graph/status edits.
Build the manuscript and map with `latexmk -pdf`, reject undefined references,
inspect rendered pages and link annotations. These check document integrity,
not mathematical truth. In `../navier-formal`, `lake build` and the axiom
reports check machine consistency, not statement faithfulness.

GitHub is the only remote workflow for all three repositories. Use signed
commits and tags with the global Git defaults managed by chezmoi; do not
bypass signing if ssh-agent is unavailable. The Navier Overleaf project was
deleted at the owner's request on 2026-09-05 and must not be recreated.
