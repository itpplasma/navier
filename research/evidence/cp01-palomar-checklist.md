# CP01 — Palomar compliance checklist and local verification recipe for `navier-formal`

Lane: Palomar compliance + reproducible local verification.
Scope: repository construction and mechanical/editorial preflight for the CP1
formalization target. **No mathematical claim is made or advanced here.** In
particular NS-R3 remains OPEN, and HIGH-PRESSURE / HIGH-STRAIN remain open; this
note only specifies how a *conditional* CP1 result could be encoded so that a
registry submission would be truthful. Nothing here authorizes creating a
repository, pushing, or submitting.

---

## 0. Sources inspected

All sources below were fetched on **2026-09-05** through WebFetch. "Directly
inspected" means the file body (or its full rendered text) was returned to me;
"metadata-only" means I saw only an API listing or a derived summary.

| Source | Location | Revision inspected | Status |
|---|---|---|---|
| Palomar submission standard | `https://github.com/PalomarRegistry/PalomarPolicy/blob/main/CONTRIBUTING.md` (raw fetched) | repo HEAD `4ed67de4fd69df383badb7857dff97e2fb734ab0`, 2026-08-31T22:47:57Z, "Document robot-authorized registry corrections (#94)" | directly-inspected, full text (sections 1–9.1) |
| Prior CONTRIBUTING commits | GitHub API `/commits?path=CONTRIBUTING.md` | `0f86ce126376c4a3af6a5a67364c0b3a492363ae` (2026-08-31T06:13:05Z), `a2ffea69be29b4f32cd2f31c32c838fdc0d8852b` (2026-08-31T05:00:40Z) | metadata-only |
| `toolchains.json` | `PalomarRegistry/PalomarSubmission/toolchains.json`, branch `main` | repo HEAD `c605f23466450a52999fcfb3c6d68ed8febc56bf`, 2026-09-03T04:48:24Z | directly-inspected (file body) |
| PalomarTemplate | `https://github.com/PalomarRegistry/PalomarTemplate` | repo HEAD `128a6c5ce5f48622e69927ccd639cbff401022e8`, 2026-08-18T06:15:09Z, "Document source contributor roles (#27)" | `comparator.json`, `formalization.yaml`, `lakefile.toml`, `lean-toolchain`, `scripts/verify-comparator.sh` directly-inspected; `README.md`, `CONTRIBUTING.md`, `Challenge.lean`, `Solution.lean`, `scripts/landrun-wrapper.sh` returned as model summaries only (metadata-only for exact bytes) |
| formalization.yaml standard | `https://github.com/mathlib-initiative/formalization.yaml`, `schema/v0.4.schema.json` | repo HEAD `99c678e569c7c4c0772db297c5ddd5e4c9b6322e`, 2026-08-25T17:06:01Z, "Add project.description to formalization.yaml v0.4 (#23)" | schema JSON directly-inspected and machine-enumerated |
| Comparator | `https://github.com/leanprover/comparator` | repo HEAD `2312244ac716564a61cc0bf4e107d9abf1757a61`, 2026-08-30T06:50:43Z | README summary only (metadata-only for exact bytes) |
| Registered example | `https://github.com/anthropics/formal-math` (`zeta23/`) | repo HEAD `2bafb8c88f177284a2123b5fefa2ff84e2365eb6`, 2026-08-28T21:37:34Z | `zeta23/comparator.json` directly-inspected; `zeta23/lakefile.toml`, `zeta23/Challenge.lean`, `zeta23/formalization.yaml`, `.github/scripts/comparator-check.sh`, root README returned as summaries (metadata-only for exact bytes) |
| Sibling project conventions | `/home/ert/proj/stafford38/PLAN.md` §"Repository restructuring and Palomar preparation"; `/home/ert/proj/stafford38/docs/literature-assumptions.yaml` | local working tree, 2026-09-05 | directly-inspected |
| lean4export tags | GitHub API `leanprover/lean4export/tags` | full tag list (43 tags) | directly-inspected |
| mathlib4 tags | GitHub API `leanprover-community/mathlib4/tags` | `v4.33.1` = `0df444a360eaa60ab8c11dca51a86af692955474` | directly-inspected; confirmed identical to the local checkout at `/home/ert/proj/stafford38/.lake/packages/mathlib` (tag `v4.33.1`, committed 2026-08-21T12:04:53Z) |

**Not accessed / could not verify** — recorded in §7.

---

## 1. File-by-file checklist for `navier-formal`

Ordinary layout (PalomarPolicy §2). Repository root **is** the Lean project;
do not nest, so that no explicit "selected project" path is needed. Everything
below is repository-root-relative.

### 1.1 `lean-toolchain`

```
leanprover/lean4:v4.33.0
```

Requirements (§2.1): must name a Lean release in the form
`leanprover/lean4:<version>`, no older than `minimum` in
`PalomarRegistry/PalomarSubmission/toolchains.json`, whose complete content is

```json
{
  "schema_version": 2,
  "minimum": "v4.28.0"
}
```

**Blocking toolchain finding.** The programme target is Lean **v4.33.1**.
Policy §2.1 says: "The verifier derives the `lean4export` release tag from the
submitted Lean version, resolves that tag once to an exact commit, and records
the commit." As of 2026-09-05 `leanprover/lean4export` has tags
`v4.33.0-rc1`, `v4.33.0-rc2`, `v4.33.0`, `v4.34.0-rc1`, `v4.34.0-rc2` — **there
is no `v4.33.1` tag**, although `leanprover/lean4` does have `v4.33.1`. The
template's own `scripts/verify-comparator.sh` hard-fails when the project
toolchain and the pinned lean4export toolchain differ. Consequences:

- Safe choice today: pin `leanprover/lean4:v4.33.0` with Mathlib
  `v4.33.0` (`db584cd6d46c92f209a44c0f1c829460d327499d`), for which
  lean4export tag `v4.33.0` = `15f6055e299ad5b89345e533cc2192f4cc00f659` exists.
- If v4.33.1 is required (it is what the sibling `stafford38` and its local
  Mathlib checkout use), re-check the lean4export tag list immediately before
  submission; do not assume derivation falls back to `v4.33.0`. This must be
  confirmed against Palomar behaviour, not guessed.
- Mathlib `v4.33.1` = `0df444a360eaa60ab8c11dca51a86af692955474` (2026-08-21),
  toolchain file `leanprover/lean4:v4.33.1` — matching pins are consistent, the
  only exposure is the export-tag derivation.

### 1.2 `lakefile.toml` (exactly one of `lakefile.toml` / `lakefile.lean`; TOML preferred)

Must be a regular file ≤ 1 MiB and valid TOML (§2.1). Prefer TOML because a
`lakefile.lean` is executable submitted code. Shape modelled on the template
(which pins Mathlib by tag) and on `zeta23` (which pins by SHA and separates
`ChallengeDeps`):

```toml
name = "NavierFormal"
version = "0.1.0"
defaultTargets = ["NavierFormal", "Challenge", "Solution"]

[[require]]
name = "mathlib"
git = "https://github.com/leanprover-community/mathlib4"
rev = "0df444a360eaa60ab8c11dca51a86af692955474"   # v4.33.1; use db584cd6… for v4.33.0

[[lean_lib]]
name = "NavierFormal"

[[lean_lib]]
name = "Challenge"
roots = ["Challenge"]

[[lean_lib]]
name = "Solution"
roots = ["Solution"]
```

Note the template writes `rev = "v4.32.0"` (a tag), while `zeta23` writes a full
SHA. §2.4 requires **every Git package in `lake-manifest.json`** to be pinned to
a full 40-character lowercase SHA with a credential-free public
`https://github.com/owner/repository` URL without query or fragment; the
Lakefile `rev` is resolved into the manifest, so pinning the SHA in the Lakefile
too removes any ambiguity.

### 1.3 `lake-manifest.json`

Committed. Mandatory for `lakefile.lean`; the only exception for a TOML project
is the narrow contained-path-dependency case of §6.3, which does not apply here
because Mathlib is a Git dependency. Requirements: every Git package pinned to a
full 40-char lowercase SHA, public HTTPS GitHub URL, no query/fragment, no Git
submodules, no Git LFS pointers.

### 1.4 `Challenge.lean`

Hard limits (§2.2): **100 KiB and 1,000 lines** maximum; a mechanical *warning*
above **32 KiB or 300 lines**. Inline display on the registry page requires
exactly one compared declaration and ≤ 100 lines / 32 KiB — with the CP1 result
family this will not qualify, and a dedicated rendered page is used instead.

Content rules: statements only, `sorry` proofs permitted (deliberate Challenge
holes are explicitly allowed, §2.3); prefer theorems to new definitions; every
definition needed by a compared theorem carries a precise docstring and its
ordinary mathematical meaning; hypotheses must not be hidden, quantifiers must
not be weakened, and a supporting lemma must not be presented as the advertised
theorem.

Mechanical naming: Challenge and Solution must be **distinct dotted module
names**, each component matching `[A-Za-z_][A-Za-z0-9_']*`, both resolved by
Lake to a regular, non-symlink source file inside the project. Note
`PalomarSubmission` commit `c605f23466450a52999fcfb3c6d68ed8febc56bf`
(2026-09-03) is titled "Isolate the canonical Challenge module namespace
(#132)" — a change I could not read; re-read the policy before freezing module
names.

### 1.5 `Solution.lean`

Declarations with the **same types** as the compared Challenge declarations,
supplying proofs. May import the full private development (`NavierFormal/…`).
Comparator must confirm no proved Solution declaration depends on `sorryAx`,
`Lean.ofReduceBool`, a **custom axiom**, or an unnamed missing definition.

### 1.6 `comparator.json`

Regular JSON, one object, ≤ 1 MiB. Exactly four required keys, plus at most the
two optional keys `definition_names` and `enable_nanoda`; **no other keys are
accepted**. Verbatim required field names:

```json
{
  "challenge_module": "Challenge",
  "solution_module": "Solution",
  "theorem_names": ["NavierFormal.cp1_conditional_global_regularity"],
  "definition_names": [],
  "permitted_axioms": ["propext", "Quot.sound", "Classical.choice"],
  "enable_nanoda": true
}
```

- `theorem_names`: nonempty array of nonempty strings.
- `definition_names`: optional, defaults to empty. Prefer `[]` for CP1 — a
  definition hole invites an editorial vacuity check and, per the Comparator
  README, additional human verification.
- `permitted_axioms`: **may contain only** `propext`, `Quot.sound`,
  `Classical.choice`.
- `enable_nanoda`: accepted for Comparator compatibility but **ignored** by
  Palomar, which always writes its own protected NanoDa-enabled configuration.
  Set it to `true` anyway: the template's `scripts/verify-comparator.sh`
  refuses to run unless it is exactly `true`.

One submission ↔ one Comparator configuration. If CP1 (a) manuscript estimates
and CP1 (b) quotient-functional results were to be registered as separate
records, they need separate configuration files and separate submissions.

### 1.7 `formalization.yaml`

UTF-8 YAML ≤ 256 KiB, one top-level mapping, **no duplicate keys, no YAML merge
keys**. Declare `version: "v0.4"`.

Mechanically required fields, verbatim names (PalomarPolicy §3.1/§3.2, cross-checked
against `schema/v0.4.schema.json`):

- `project.name` — nonempty string, ≤ 300 characters; this is the public entry title.
- `project.description` — nonempty string, ≤ 10,000 characters; this **is** the
  registry abstract.
- `project.authors` — nonempty list of nonempty name strings; **humans only**.
- `project.license` — exact SPDX identifier, matching the detected root licence.
- `project.responsible_maintainers` — nonempty list of nonempty name strings;
  **humans only**. (Singular `project.responsible_maintainer` is a legacy alias
  accepted only when the plural key is entirely absent; do not use it.)
- `classification.arxiv` — 1–8 distinct codes from
  `PalomarSubmission/taxonomies/arxiv-categories.json`.
- `classification.msc2020` — up to 8 distinct codes from
  `PalomarSubmission/taxonomies/msc2020-codes.json`; may be empty/absent.
- `automation.methods` — nonempty list of mappings, each with a nonempty
  `method`. Portable values: `manual`, `copilot`, `agent`, `autonomous`, `other`.
- `review.status` — nonempty string, describing review **before** submission
  (e.g. `unchecked`, `agent-reviewed`, `self-assessed`, `peer-reviewed`,
  `author-verified`).
- `sources` — nonempty list; every entry needs a nonempty `title` and a
  `relationship` in exactly {`formalizes`, `adapts`, `independently-proves`,
  `background`, `other`}. `sources[].type`, when present, must be one of
  `paper`, `book`, `web discussion` (with a space), `folklore`,
  `original-proof`, `other`.
- `repository` — **omit** (the submitted repository is the substantive
  development). Only a thin wrapper supplies
  `repository.substantive_formalization.id` and `.revision` (full 40-char
  lowercase SHA).

Result-origin rule: the source list must satisfy **exactly one** alternative.
For CP1 as currently constituted the correct choice is **source-based**: no
entry has `type: original-proof`, and the manuscript-owned estimates are
recorded against the arXiv/manuscript source with `relationship: formalizes`
(or `adapts` where the Lean statement changes the manuscript's), with Tao 2013
and Gallagher–Koch–Planchon 2013 as `background`. Do **not** mix
`type: original-proof` with any substantive relationship — that fails
mechanically.

Optional but strongly indicated for CP1 (the v0.4 schema supports it and it is
the honest place for the conditional structure):

- `status.scope` — state exactly what is and is not formalized.
- `status.sorry_count`, `status.sorry_in_definitions` — unquoted integers,
  counting the proof development and excluding `Challenge.lean`'s deliberate
  `sorry`. For a compliant submission both must be `0` in the Solution path.
- `status.axioms` — list; for a compliant submission `[]` beyond the three
  permitted foundational axioms.
- `status.main_results[].literature_dependencies[].statement` and
  `.source` — **this is the schema-native slot for the CP1 literature premises**
  (Tao Thm 5.4; GKP Thm 4), and it should be used in addition to their appearance
  as explicit Lean hypotheses (§2 below).
- `fidelity.divergences` — every known divergence from the cited manuscript.
- `alignment` — freeform; the template's `namespace` / `statements[]`
  (`source`, `lean`, `module`, `status`, `note`) shape maps well onto the
  project's paper-label ↔ declaration table.
- `related_formalizations[]` with `id` (required) and `relationship` in
  {`builds-on`, `adapts`, `independent`, `supersedes`, `other`}.

Human-authorship rule (§3.1, citing the Leiden Declaration's human-authorship
principle): **no AI model, agent, system, session, or tool may be listed** in
`project.authors` or `project.responsible_maintainers`. Model contributions go
in `automation.methods` and the narrative production account. This rule is
enforced editorially, not by the schema.

### 1.8 `LICENSE`

Exactly **one** conventional licence file at repository root. Case-insensitive
name from {`LICENSE`, `LICENCE`, `COPYING`, `UNLICENSE`, `OFL`}, optionally with
`.md`, `.markdown`, or `.txt`. Regular, non-symlink, nonempty UTF-8 text, ≤ 1
MiB. Palomar's detector must find exactly one unambiguous SPDX identifier, and
it must equal `project.license` exactly. Use `Apache-2.0`, matching
PalomarTemplate, `anthropics/formal-math`, and the sibling `stafford38` plan.

### 1.9 `README.md`

Not mechanically required, but it is one of the eligible locations for the
narrative account (§3.4). Across README + Challenge module docs/docstrings +
`formalization.yaml`, the submission must include: a plain-language account of
**every** compared theorem; every known mismatch with the cited source, extra
assumption, permitted axiom, scope restriction and degenerate case; the
mathematical sources and how they were used; what is original vs adapted vs
still missing; relation to previous formalizations; authorship and production
process including AI involvement and human review; and the repository licence.
Novelty must not be claimed without a credible literature search — if unknown,
say it is unknown.

### 1.10 `NavierFormal/` and `NavierFormal.lean`

The substantive development. Imported only by `Solution.lean`. Solution-only
dependencies may come from any public GitHub repository meeting §2.4.

### 1.11 `scripts/`

Copy `verify-comparator.sh` and `landrun-wrapper.sh` from PalomarTemplate
(§3 below). Not required by policy; required in practice for local preflight.

### 1.12 `.github/workflows/`

Optional for submission (Palomar runs its own public mechanical workflow). A
CI job mirroring §3 is useful. Note that Palomar's mechanical verification runs
in a **public** GitHub Actions workflow, so the repository, the commit, and the
fact of the check become public at submission time.

### 1.13 Files that must NOT exist

- Compiled artifacts outside `.lake`: `.olean`, `.ilean`, `.a`, `.bc`, `.dll`,
  `.dylib`, `.o`, `.obj`, `.so`, `.trace` — the verifier rejects them.
- Git submodules in the submitted repository.
- Git LFS pointers anywhere in the submitted repository or dependencies.
- Symbolic links on any selected path (Challenge/Solution source, metadata,
  comparator config, licence must all be regular non-symlink files). Symlinks
  are excluded from the size measurement but a symlinked *selected* file fails.
- Challenge or Solution source held inside `.lake` — submitted `.lake` state is
  discarded before verification.

---

## 2. Import closure of `Challenge.lean`, and what "Phase I axioms" mean for Palomar

### 2.1 The import-closure rule (verbatim substance, §2.4)

The Challenge's **transitive import closure** is the Challenge source plus every
Lean source file reached by recursively following imports. Every file in that
closure must be one of:

1. Lean core;
2. **Mathlib** at a verified revision in its canonical repository, with the
   exact dependencies pinned by Mathlib's manifest;
3. **Tau Ceti** at a verified revision in its canonical repository, with its
   manifest's pins;
4. **CSLib** at a verified revision in its canonical repository, with its
   manifest's pins.

No other project-specific source may occur in that closure. Recursive imports
count exactly like direct imports. Previous Palomar registration of a repository
does **not** make it an approved Challenge dependency. Tau Ceti and CSLib are
permitted but recorded as *qualified dependencies* with a displayed warning, so
for `navier-formal` the Challenge should import **Mathlib only** (`zeta23`
literally uses `import Mathlib` and inlines its definitions into
`Challenge.lean`; this is the pattern to copy).

Practical consequence for CP1: every notion appearing in a compared statement —
Leray/Schwartz data class, divergence-free vector fields on `ℝ³`, the
Navier–Stokes system itself, the `L³` gradient-quotient functional of the HF17
work — must be written out of Mathlib primitives inside `Challenge.lean`. It may
not be imported from `NavierFormal/`. The sibling project states the same rule
for itself: "Its Challenge import closure excludes AlgebraicAnalysis… Never
vendor the library to evade that restriction"
(`/home/ert/proj/stafford38/PLAN.md`, §"Repository restructuring and Palomar
preparation", item 5). Vendoring library sources into the Challenge to dodge the
rule is an explicit anti-pattern there and would in any case be caught by the
verifier's record of "every Lean source file used by that compilation".

### 2.2 Phase I axioms are NOT registrable

`permitted_axioms` **may contain only** `propext`, `Quot.sound`,
`Classical.choice`. Comparator additionally requires that no proved Solution
declaration depend on `sorryAx`, `Lean.ofReduceBool`, a custom axiom, or an
unnamed missing definition. Therefore:

> A Phase-I-style Lean development, in which Tao 2013 Theorem 5.4 and
> Gallagher–Koch–Planchon 2013 Theorem 4 appear as clearly-labelled `axiom`
> declarations, **cannot be registered with Palomar at all**. It is not a matter
> of disclosure or of an editorial warning; the mechanical check fails.

This matches the sibling project's own gate: "Only `propext`,
`Classical.choice` and `Quot.sound` are allowed; reject project/literature
axioms, `sorryAx`, `Lean.ofReduceBool` and unverified placeholders"
(`stafford38/PLAN.md` item 2).

### 2.3 The three registrable encodings

**(A) Hypothesis-carrying Challenge theorem — recommended for CP1.**
Turn each Phase I literature premise into an explicit hypothesis argument of the
compared theorem. The theorem then has the shape

```
theorem cp1_conditional_global_regularity
    (hLocal  : <Mathlib-only statement of the local theory premise>)
    (hEndpoint : <Mathlib-only statement of the L³ endpoint continuation premise>)
    (hCritical : <Mathlib-only statement of hyp:critical>)
    : <Clay alternative A conclusion> := sorry
```

and the Solution proves it with **no** axioms beyond the permitted three,
because every import is discharged by an explicit argument. `zeta23` uses
exactly this device at a smaller scale: its Dirichlet theorems carry `hq : 1 < q`
and `hχ : χ.IsPrimitive` as explicit arguments (`zeta23/Challenge.lean`).

Requirements and hazards of (A):

- Each hypothesis must itself be *statable in Mathlib terms only* — the
  literature theorems have to be spelled out, not named. This is real work and
  is precisely where "formal proof is not faithfulness of the encoded statement"
  bites: an over-strong or subtly wrong `hLocal` makes the theorem vacuous or
  false-to-source.
- §2.2 forbids hiding material hypotheses or presenting a supporting lemma as
  the advertised theorem. A hypothesis-laden theorem is legitimate **only** if
  the narrative account says plainly, in `project.description`,
  `status.scope`, `fidelity.divergences`, and the Challenge docstrings, that the
  result is conditional and on exactly what.
- The editorial notability check is applied to the statement **as actually
  written in the Challenge**. A conditional statement whose hypothesis is
  `hyp:critical` (the still-open CRITICAL node) is at risk of reading as
  assuming what is to be proved. Policy §1 explicitly lists "purported solutions
  of famous open problems without a careful comparison with the standard
  conjecture, a serious literature account, and an honest statement of any gap"
  among the things Palomar does not index, and a notability score below 4 forces
  `rejected`. This is the single largest editorial risk for CP1 and it is not a
  compliance detail that can be papered over: the abstract must state, in the
  first sentence, that the Millennium problem is not solved and that the theorem
  is conditional on an unproved critical bound.

**(B) Register only Phase-II-complete theorems.**
Split the development. Register a configuration whose `theorem_names` list only
those CP1 items that are unconditionally proved from Mathlib alone — the
manuscript-owned analytic propositions (`prop:energy`, `prop:scaling`,
`prop:enstrophy`, `prop:ode`, `prop:pressure`, `prop:lowpressure`) and the
audited HF17 quotient-functional results (existence/uniqueness of the minimizer,
coercivity on solenoidal fields, scaling invariance, heat monotonicity, the
Fréchet derivative, pressure-gradient annihilation, the evolution identity
`eq:quotient-evolution`, the low-strain Gronwall bound). These need no
literature premise at all. They are self-contained analysis results, they carry
no risk of being read as a Millennium claim, and their notability rests on the
quotient functional being a genuinely new object. This is the **lowest-risk**
route and can be done first.

**(C) Combination — the recommended structure.**

1. Build one repository `navier-formal` with the full development.
2. Ship **two** Comparator configurations, and therefore **two** submissions
   (one submission ↔ one configuration ↔ one registry entry):
   - `comparator-quotient.json`: route (B). Unconditional theorems only.
     `permitted_axioms` = the three; `status.axioms: []`.
   - `comparator-conditional.json`: route (A). The single hypothesis-carrying
     conditional continuation theorem, with `hLocal`, `hEndpoint`, `hCritical`
     as explicit arguments.
   Under §6.2, the Comparator configuration path is always selected explicitly,
   must lie inside the selected project and end in `.json`; the ordinary
   `comparator.json` basename is a convention, not a requirement.
3. Submit (B) first. Only submit (A) after the narrative account has been
   written to make the conditionality unmissable, and after an independent
   internal review specifically of whether the encoded `hCritical` is a faithful
   rendering of `hyp:critical` and not something stronger.
4. In both `formalization.yaml` files, populate
   `status.main_results[].literature_dependencies[]` with
   `statement`/`source` pairs for Tao 2013 Thm 5.4 and GKP 2013 Thm 4, mirroring
   the `inputs:` records in
   `/home/ert/proj/stafford38/docs/literature-assumptions.yaml`. That file's
   status vocabulary (`FORMALIZED`, `LITERATURE-INPUT`, `CONDITIONAL`, `OPEN`)
   is directly reusable and its `phase_i` / `phase_ii` split is the right shape
   for a `navier-formal/docs/literature-assumptions.yaml`.

**Not permitted, for the record:** setting `permitted_axioms` to include a
project axiom (the field's vocabulary is closed); leaving `sorry` in the
Solution (Challenge holes only); using a `definition_names` hole to smuggle in
an unproved object (Comparator would accept it and editorial review would
reject it as vacuous).

---

## 3. Exact commands to run Comparator locally on this machine

### 3.1 Preconditions verified on this machine, 2026-09-05

| Requirement | Present | Note |
|---|---|---|
| `git` | 2.55.0 | ok |
| `python3` | 3.14.7 | ok |
| `cargo` / `rustc` | 1.94.1 | needed for NanoDa |
| `go` | go1.27.0 | needed for landrun (`go version`, not `go --version`) |
| `elan` | 4.1.2 | `leanprover/lean4:v4.33.1` and `v4.33.0-rc1` already installed; **`v4.33.0` is not installed** and elan will fetch it if the toolchain is pinned there |
| `lake` on PATH | 5.0.0 (Lean 4.14.0) | this is the *default* toolchain shim; inside the project directory elan resolves the project's `lean-toolchain` instead |
| `jq` | not checked | required by the `anthropics/formal-math` variant script, not by the PalomarTemplate script |
| Free disk | **42 GiB on `/` (96 % full)** | a Mathlib `.lake` tree costs ~10–15 GiB (the sibling `stafford38/.lake` is 15 GiB), plus comparator/lean4export/nanoda build trees. **Free space before running.** |
| Network | required for `lake exe cache get`, `go install`, `git clone` | Comparator itself runs sandboxed without network |

### 3.2 Recipe A — the PalomarTemplate script (authoritative; copy it verbatim)

`PalomarTemplate/scripts/verify-comparator.sh` at `128a6c5c…`, directly
inspected. Copy it and `scripts/landrun-wrapper.sh` into `navier-formal`
unchanged, then:

```bash
cd /home/ert/proj/navier-formal
bash scripts/verify-comparator.sh
```

What it does, in order (exact pins as written in the script):

```
comparator_commit=68a064109f01c08f47c8edc9f51d6a2bbffaa188
lean4export_commit=4e7915201d3f9f04470d9eae002fa695f7cdc589
landrun_commit=811cfff51ceaf3d9843708aa6d22e9b84ccac8b4
nanoda_commit=68d5ca9db226849b41a6fff59d796ff19d0a8840
```

1. Requires `cargo git go lake python3` on PATH.
2. Asserts `comparator.json` parses and has `enable_nanoda` **exactly** `true`.
3. Clones/updates into `${PALOMAR_COMPARATOR_CACHE:-<repo>/.cache/palomar-comparator}`:
   `https://github.com/leanprover/lean4export.git`,
   `https://github.com/leanprover/comparator.git`,
   `https://github.com/robsimmons/nanoda_lib.git`, each `git fetch --depth 1`
   + `git checkout --detach <commit>`.
4. **Fails hard** unless the project's `lean-toolchain` (whitespace-stripped)
   equals the pinned lean4export's `lean-toolchain`. Note
   `lean4export_commit=4e79152…` is tag **`v4.32.0`**, so with a v4.33.x project
   toolchain this pin must be updated — to `15f6055e299ad5b89345e533cc2192f4cc00f659`
   (lean4export `v4.33.0`) if the project pins `leanprover/lean4:v4.33.0`. There
   is currently no lean4export revision declaring `v4.33.1` (see §1.1).
5. `GOBIN="$bin_dir" go install github.com/zouuup/landrun/cmd/landrun@$landrun_commit`
6. `(cd "$comparator_dir" && lake build comparator)`,
   `(cd "$lean4export_dir" && lake build lean4export)`,
   `(cd "$nanoda_dir" && cargo build --release --locked)`
7. In the repository root: `lake exe cache get`, then

```bash
PALOMAR_LANDRUN_BIN="$bin_dir/landrun" \
COMPARATOR_LEAN4EXPORT="$lean4export_dir/.lake/build/bin/lean4export" \
COMPARATOR_NANODA="$nanoda_dir/target/release/nanoda_bin" \
COMPARATOR_LANDRUN="$repository_root/scripts/landrun-wrapper.sh" \
  lake env "$comparator_dir/.lake/build/bin/comparator" comparator.json
```

`scripts/landrun-wrapper.sh` refuses any `--unrestricted-*` flag ("Landrun
option switches off part of the sandbox. Comparator must not request it"),
allowlists the option set, and appends the `--` delimiter Comparator omits.
Do not weaken it.

To check a second configuration, run the same final command with
`comparator-quotient.json` (the script hardcodes `comparator.json` for its
`enable_nanoda` precheck; parameterize that if two configs are used).

### 3.3 Recipe B — running Comparator by hand (no template script)

Per the Comparator README (metadata-only): Comparator needs `landrun` (from
`main`), `lean4export` matching the Lean version, and optionally `nanoda`,
either on `PATH` or via `COMPARATOR_LANDRUN`, `COMPARATOR_LEAN4EXPORT`,
`COMPARATOR_NANODA`. Build with `lake build lean4export comparator`, and run
sandboxed, e.g.

```bash
systemd-run --property=RestrictAddressFamilies=~AF_UNIX --user --pty \
  -E PATH="$PATH" --working-directory "$(pwd)" -- bash -c \
  'lake env /path/to/comparator/.lake/build/bin/comparator /path/to/comparator.json'
```

External kernels are registered in the config's `external_kernels` field;
NanoDa is auto-detected by `"enable_nanoda": true` or a kernel name containing
`noda`. **Do not add `external_kernels` to a submitted `comparator.json`** —
Palomar accepts no keys beyond the six listed in §1.6.

### 3.4 Recipe C — the `anthropics/formal-math` variant

Registered-example CI script `.github/scripts/comparator-check.sh` (summary
only): pins `comparator=575674928e239f5bc452aab72d1dd7b0f1326494`,
`nanoda=68d5ca9db226849b41a6fff59d796ff19d0a8840`,
`landrun=811cfff51ceaf3d9843708aa6d22e9b84ccac8b4`, derives the lean4export
revision from the project toolchain, caches tools in `~/.cache/lean-ci-tools`,
requires `git go cargo jq lean lake`, accepts config paths matching
`comparator*.json` or `comparator/config*.json`, enforces that
`permitted_axioms ⊆ {propext, Quot.sound, Classical.choice}`, and demands the
comparator print exactly `Your solution is okay!` with exit status 0. Invoked as

```bash
cd zeta23 && bash ../.github/scripts/comparator-check.sh
```

Note its comparator pin differs from PalomarTemplate's; the template pin is the
one to follow, since Palomar's own verifier uses fixed verifier pins that the
submitter does not control.

### 3.5 Additional local preflight (not Comparator)

- `lake build` — full project.
- No-`sorry` scan outside `Challenge.lean`.
- `#print axioms <each compared declaration>` in the Solution namespace;
  every report must contain only `propext`, `Classical.choice`, `Quot.sound`.
- `ruby scripts/validate-formalization.rb` — the template's metadata validator,
  which parses `formalization.yaml` and flags remaining `TEMPLATE` sentinels
  (requires Ruby; the template ships a `Gemfile`).
- Size/shape: `Challenge.lean` line count and byte size against 1,000 / 100 KiB
  (and the 300 / 32 KiB warning thresholds); repository size excluding `.git`
  against 500 MiB; `comparator.json` and `lakefile.toml` against 1 MiB;
  `formalization.yaml` against 256 KiB.
- Clean-clone build in a fresh directory with no access to local package caches
  or symlinks, as the sibling plan requires (item 6).

---

## 4. Constraints: size, symlinks, artifacts, licences, authorship, automation disclosure

| Constraint | Exact rule | Source |
|---|---|---|
| Repository size | Checked-out repository, **excluding `.git` and symbolic links**, ≤ **500 MiB** | §2 |
| Challenge size | ≤ **100 KiB** and ≤ **1,000 lines** (hard); warning above **32 KiB** or **300 lines**; inline rendering only if exactly one compared declaration and ≤ 100 lines / 32 KiB | §2.2, §8 |
| `formalization.yaml` size | ≤ **256 KiB**, UTF-8, one top-level mapping, no duplicate keys, no merge keys | §3 |
| `comparator.json` size | regular JSON file, one object, ≤ **1 MiB** | §2.3 |
| Lakefile size | regular file ≤ **1 MiB**; exactly one of `lakefile.toml` / `lakefile.lean` at project root | §2.1 |
| Licence file size | regular, non-symlink, nonempty UTF-8, ≤ **1 MiB** | §2.5 |
| Symlinks | excluded from the size measurement; every *selected* path (project dir, Challenge/Solution source, metadata, comparator config, licence) must resolve to a regular, **non-symlink** file inside the checkout; supplied paths must not contain a symbolic-link component, `.`, `..`, empty component, backslash, query/fragment, control character, drive prefix, or be absolute | §2, §2.2, §2.5, §6.2, §6.4 |
| Compiled artifacts | must not be committed outside `.lake`; the verifier rejects `.olean`, `.ilean`, `.a`, `.bc`, `.dll`, `.dylib`, `.o`, `.obj`, `.so`, `.trace`; submitted `.lake` state is discarded and replaced | §2.4 |
| Submodules | the submitted repository and any separately named substantive formalisation must contain **no Git submodules**; an inert gitlink is tolerated only inside a dependency | §2.4 |
| Git LFS | LFS pointers rejected in the submitted repository, every dependency, and any substantive formalisation | §2.4 |
| Dependency pins | every Git package in `lake-manifest.json`: credential-free public `https://github.com/owner/repository`, no query or fragment, full 40-character **lowercase** commit SHA | §2.4 |
| Commit identification | submit `owner/name` + the **full 40-character SHA**; branches and tags are not accepted | §2 |
| Toolchain | `leanprover/lean4:<version>`, not older than `toolchains.json` `minimum` = `v4.28.0` (`schema_version: 2`) | §2.1 |
| Licence | exactly one root file named (case-insensitively) `LICENSE`/`LICENCE`/`COPYING`/`UNLICENSE`/`OFL`, optionally `+ .md/.markdown/.txt`; detector must find exactly one unambiguous SPDX id; must equal `project.license` **exactly**. Missing, multiple, custom, ambiguous or mismatched fails mechanically before editorial review | §2.5 |
| Human-only authorship | `project.authors` and `project.responsible_maintainers` are reserved for **humans**; no AI model, agent, system, session or tool may be listed. Enforced editorially (per the Leiden Declaration human-authorship principle). Credit AI in `automation.methods` and the narrative | §3.1 |
| Automation disclosure | `automation.methods` nonempty, each entry with a nonempty `method` (portable: `manual`, `copilot`, `agent`, `autonomous`, `other`); record each material automated method and model role honestly; optional `models`, `framework`, `tool_setup`, `cost.{wall_time,spend_usd,hardware}`, `prompting_notes`, `automation.spend_usd`, `automation.notes`. Costs/hardware/wall time/prompt logs are useful but not required to be reconstructed after the fact; a concise disclosure may point to a fuller pinned account in the reviewed commit | §3.1 |
| Review disclosure | `review.status` describes review completed **before** submission, not Palomar's own review; use `unchecked` when none; `review.reviewers` only for identifiable people/systems that performed a distinct review; do not imply review merely because authors checked their own work | §3.1 |
| Authorisation | submitter must be a responsible author/maintainer of the substantive formalisation, or have approval from one. Write access, shared owner, org membership, a fork, or a transfer are **not** that basis. Answering falsely is material misrepresentation. Write access is proved separately (browser sign-in, or, for an agent, a tag at the submitted commit plus a gist) | §4 |
| Publicity | mechanical verification runs in a public GitHub Actions workflow, so repository, commit, the fact of the check, the declared authorization relationship and any approval evidence are public from submission. The review text and outcome stay non-public unless the submitter registers | §8 |
| Permanence | registration creates immutable preservation tags and native public forks in `PalomarArchive` for the submitted repository, every pinned Git dependency, and any substantive formalisation. The append-only record guarantee has been in force since 2026-08-10 | §8 |
| Identifiers | `PALOMAR-YYYY-MM-DD-NNNNNN`, six-digit serial from `000001`, sequential since 2026-08-07. **Do not invent one.** Updates cite the existing identifier and require the same repository, selected project path and comparator config path | §9 |

---

## 5. Editorial-review exposure specific to CP1

Not a compliance checklist item, but it determines whether a compliant
submission is registrable at all.

- Review is performed by a language model over a fixed prompt sequence. No
  person reads an ordinary submission before the outcome. It is not peer review.
- Required checks: classification off-topic-ness; clarity/accuracy/completeness
  of structured metadata, provenance and narrative; **alignment between every
  compared theorem and its informal account** including definitions,
  quantifiers, hypotheses, coercions, degenerate cases and claimed scope;
  fidelity and auditability of every material definition and imported concept;
  literature account and research interest. If an informal proof account is
  present anywhere eligible, an extra check compares it against the actual
  Solution source and imports — "a plausible proof of the same theorem is not
  enough".
- Every substantive check returns a coverage manifest listing **every** name in
  `theorem_names` then **every** name in `definition_names`, in order; an
  incomplete or reordered manifest is rejected.
- Scores 1–5 per dimension; rubric minimum **4**; a clean check must reach 4 on
  every score it owns. Notability below 4 is a fundamental failure forcing
  `rejected`. Notability 3 = "borderline interest, where paper-worthiness or a
  credible research audience has not been affirmatively established" — the
  burden is affirmative.
- Outcomes: `neutral` (no blocking problem; permits registration, is not
  approval or endorsement), `revision_required`, `rejected`. No appeals, no
  human sign-off.
- For CP1 specifically, the three exposures are: (i) reading a conditional Clay
  statement as a purported solution of a famous open problem — §1's explicit
  exclusion; (ii) alignment failure if the Lean `hCritical` is not exactly
  `hyp:critical`; (iii) notability of the HF17 quotient functional needing an
  affirmatively identified research audience. All three are addressed by route
  (B)-first plus an abstract whose first sentence states the problem is not
  solved.

---

## 6. Ordered build sequence for `navier-formal`

1. Decide the toolchain: `leanprover/lean4:v4.33.0` + Mathlib
   `db584cd6d46c92f209a44c0f1c829460d327499d`, **or** v4.33.1 + Mathlib
   `0df444a360eaa60ab8c11dca51a86af692955474` after re-checking lean4export tags.
2. `lake init` at repository root; write `lakefile.toml`, `lean-toolchain`;
   `lake update`; commit `lake-manifest.json` with a full lowercase SHA pin.
3. Add `LICENSE` (Apache-2.0) and `README.md`.
4. Develop `NavierFormal/**` (Phase I structure internally is fine as *design*,
   but no `axiom` may survive into the compared Solution path).
5. Write `Challenge.lean` with `import Mathlib` only; inline every needed
   definition with docstrings; state the compared theorems with `sorry`.
6. Write `Solution.lean` proving the same types.
7. `comparator-quotient.json` (route B) and, later, `comparator-conditional.json`
   (route A).
8. `formalization.yaml` v0.4 with all mechanically required fields plus
   `status.scope`, `status.axioms`, `status.main_results[].literature_dependencies`,
   `fidelity.divergences`, `alignment`.
9. Copy `scripts/verify-comparator.sh` and `scripts/landrun-wrapper.sh`; update
   the lean4export pin to match the chosen toolchain.
10. Run §3.2 and §3.5 locally; fix; re-run on a clean clone.
11. Stop. Do not submit, do not register, do not reserve an identifier.

---

## 7. What I could not access or verify

- **Exact bytes** of PalomarTemplate `README.md`, `CONTRIBUTING.md`,
  `Challenge.lean`, `Solution.lean`, `scripts/landrun-wrapper.sh`, and of
  `zeta23/Challenge.lean`, `zeta23/formalization.yaml`, `zeta23/lakefile.toml`,
  `.github/scripts/comparator-check.sh`, `leanprover/comparator/README.md`.
  WebFetch returned model-generated summaries of these rather than raw text.
  Treat every quoted detail from them as **metadata-only** and re-read raw
  before implementation.
- `PalomarPolicy/docs/specification.md` (the *binding* statement where
  CONTRIBUTING summarises), `docs/lawful-requests.md`,
  `docs/maintainer-corrections.md` — not fetched.
- `https://submit.palomar-registry.org/llms.txt` and the submission server —
  not fetched (and must not be exercised: submission is not authorized).
- `PalomarSubmission/taxonomies/arxiv-categories.json` and
  `taxonomies/msc2020-codes.json` — not fetched; the exact accepted code lists
  for `classification.arxiv` / `classification.msc2020` were not verified. The
  intended codes (`math.AP` primary; MSC `35Q30`, `76D05`, `35B44`, `76D03`) are
  standard but unconfirmed against Palomar's snapshots.
- `PalomarSubmission` commit `c605f23466450a52999fcfb3c6d68ed8febc56bf`,
  "Isolate the canonical Challenge module namespace (#132)" (2026-09-03) —
  **not read**. It postdates the CONTRIBUTING revision inspected and may change
  Challenge module naming rules. Re-check before freezing module names.
- Whether Palomar's lean4export tag derivation has a fallback when the exact
  Lean patch version has no lean4export tag (the `v4.33.1` gap in §1.1) — not
  determined.
- `jq` presence on this machine was not checked (needed only for recipe C).
- No Lean build, no Comparator run, and no repository creation was performed.

---

## Frontier record

```yaml
lane: cp01-palomar-compliance
date: 2026-09-05
kind: infrastructure-audit
mathematical_claim: none
terminal_claim_status: NS-R3 OPEN (unchanged by this note)
open_nodes_untouched: [HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, NS-R3]
target_repository: navier-formal (not created)
policy_revisions_inspected:
  palomar_policy_head: 4ed67de4fd69df383badb7857dff97e2fb734ab0  # 2026-08-31
  palomar_template_head: 128a6c5ce5f48622e69927ccd639cbff401022e8  # 2026-08-18
  palomar_submission_head: c605f23466450a52999fcfb3c6d68ed8febc56bf  # 2026-09-03, contents unread
  formalization_yaml_head: 99c678e569c7c4c0772db297c5ddd5e4c9b6322e  # 2026-08-25
  comparator_head: 2312244ac716564a61cc0bf4e107d9abf1757a61  # 2026-08-30
  formal_math_head: 2bafb8c88f177284a2123b5fefa2ff84e2365eb6  # 2026-08-28
pinned_verifier_tools:
  comparator: 68a064109f01c08f47c8edc9f51d6a2bbffaa188
  lean4export: 4e7915201d3f9f04470d9eae002fa695f7cdc589  # tag v4.32.0
  landrun: 811cfff51ceaf3d9843708aa6d22e9b84ccac8b4
  nanoda: 68d5ca9db226849b41a6fff59d796ff19d0a8840
blocking_findings:
  - id: PAL-TOOLCHAIN
    severity: blocking
    statement: >-
      Lean v4.33.1 has no corresponding leanprover/lean4export tag as of
      2026-09-05 (tags jump v4.33.0 -> v4.34.0-rc1), while PalomarPolicy
      section 2.1 derives the lean4export release tag from the submitted Lean
      version and the template script hard-fails on a toolchain mismatch.
    remedy: pin leanprover/lean4:v4.33.0 with Mathlib db584cd6…, or re-check tags.
  - id: PAL-AXIOMS
    severity: blocking
    statement: >-
      permitted_axioms may contain only propext, Quot.sound, Classical.choice,
      and Comparator rejects any Solution declaration depending on a custom
      axiom or sorryAx. A Phase-I development with literature axioms is
      therefore not registrable in any form.
    remedy: >-
      route A (literature theorems as explicit Mathlib-only hypotheses of the
      Challenge theorem) or route B (register only Phase-II-complete theorems);
      recommended structure is B first, then A as a separate configuration.
non_blocking_findings:
  - Challenge transitive import closure must be Mathlib-only; every CP1 notion
    must be restated inside Challenge.lean, not imported from NavierFormal/.
  - Editorial notability check is applied to the Challenge statement as written;
    a conditional Clay theorem risks the "famous open problem" exclusion unless
    the abstract states the conditionality first.
  - Local free disk is 42 GiB at 96 percent; a Mathlib .lake tree plus verifier
    build trees will not comfortably fit.
authorizations_used: none
actions_not_taken: [repository creation, push, submission, identifier reservation]
```
