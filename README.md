# Navier–Stokes research programme

This public repository contains research notes, manuscript sources and proof
maps for the original unforced three-dimensional Navier–Stokes problem on
whole space. **Global regularity for arbitrary Schwartz data is not proved,
and no unforced counterexample has been constructed.**

The main manuscript establishes a conditional route through a missing
critical estimate. Classical research also investigates whether a continuously
prepared pulse family can arise from one smooth initial datum at fixed
positive viscosity. [PLAN.md](PLAN.md) is the sole live task and status record.

## Reading guide

| Start here | Contents |
| --- | --- |
| [Manuscripts](paper/README.md) | Main conditional argument, structural-obstructions paper, standalone components and build instructions |
| [Proof graph](docs/proof-graph.yaml) and [dossier](docs/proof.md) | Canonical claims, dependencies, hypotheses and review status |
| [Current plan](PLAN.md) | Active research question, failed mechanisms and acceptance conditions |
| [Research evidence](research/evidence/) | Derivations, falsification examples and explicitly scoped audits |
| [Literature](literature/README.md) | Inspected source statements and applicability limits |
| [September source search](literature/recent-progress-2026-09.md) | Recent Euler/NS results, including the [OpenAI Euler transfer inspection](literature/openai-euler-transfer-2026-09-09.md) |
| [Formalization](https://github.com/itpplasma/navier-formal) | Public Lean sources, axiom reports and formal coverage |

The canonical graph retains 29 claims and eight separately listed
review-pending components. A `paper` entry means a written argument with the
review scope recorded in that entry. An author proof, independent audit and
Lean verification are different evidence statuses. The
[programme graph](docs/programme-graph.yaml) describes additional unproved
kinetic and microscopic specifications; it is not the canonical proof graph.

## Relativistic viscous companion programme

This programme asks whether causal relativistic viscosity prevents singularity
or instead loses physical validity. Its model, literature and initial motivation
are in [the programme](docs/relativistic-viscous-programme.md) and
[the source ledger](literature/relativistic-viscous-status-2026-10-07.md).
The original unforced NS-R3 contract is not replaced by a relativistic equation.

Current forcing-status comparison:

| Model | Forced | Unforced |
| --- | --- | --- |
| classical incompressible Navier--Stokes | released finite-time breakdown construction | unresolved |
| causal conformal BDNK | unresolved | unresolved for actual PDE singularity |

The first relativistic target is therefore the **forced** BDNK analogue. The
direct OpenAI-vortex lift has already failed a nontrivial robustness test:
the full BDNK energy equation forbids the tested noncooling slow-shrinking
proper-velocity profile even with bounded smooth forcing, while causal shear
has damped-wave rather than heat-semigroup high-frequency behavior. See
[the mechanism note](docs/openai-forcing-relativistic-failure.md). This is
evidence that the released forcing is tailored to the classical parabolic
equations; it is not a theorem that all smooth relativistic forcing fails.

Executed author results, all pending fresh independent reconstruction:

- [Strict-front virial obstruction](research/evidence/bdnk-virial-20261007.md):
  explicit initially ideal hot cores force breakdown or negative energy by a
  finite deadline; the result does not select a PDE singularity.
- [Euler-prepared kinetic-cone exit](research/evidence/bdnk-euler-prepared-exit-20261007.md):
  common smooth data across causal conformal BDNK frames develop negative matter
  directional pressure while the solution remains smooth. Initial stress has
  a positive particle realization; the shear anisotropy is order one.
- [Earlier similarity transfer](research/evidence/bdnk-transfer-20261007.md):
  a specified normalized collapse class is excluded, and classical heat damping
  does not transfer to causal shear modes.

The [current contract](research/relativistic-breakdown-contract.md) keeps actual
PDE blow-up distinct from smooth loss of kinetic realizability. A positive free
kinetic comparator is not a finite-viscosity derivation of BDNK, and negative
matter pressure must not be confused with electromagnetic field tension.
The independent OpenAI RVM reconstruction belongs to
[`itpplasma/vlasov-maxwell`](https://github.com/itpplasma/vlasov-maxwell).

Run the focused algebra checks from the repository root (requires SymPy):

```sh
python3 research/check_bdnk_virial.py
python3 research/check_bdnk_kinetic_exit.py
python3 research/check_bdnk_euler_prepared_exit.py
```

They check exact tensor and scalar identities, not the universal PDE arguments
or independent mathematical acceptance. Logs and hash receipts are beside the
research reports. No complete BDNK global regularity or shock theorem is claimed.

## Build the papers and check the repository

On Debian/Ubuntu, install `latexmk`, `texlive-latex-extra`,
`texlive-fonts-recommended`, `texlive-science`, `lmodern` and `python3-yaml`. Then run:

```sh
make -C paper documents check
python3 research/verify.py --paper-only
git diff --check
```

This generates the main paper, clickable proof map, structural-obstructions
paper and two standalone component PDFs. See [paper/README.md](paper/README.md)
for filenames. The [document workflow](.github/workflows/dissipation-clock.yml)
also builds downloadable PDF artifacts on GitHub Actions. Generated PDFs are
not committed.

Use `python3 research/verify.py` when the sibling `navier-formal` checkout is
available; it additionally checks that repository's manifest, without running
Lean. `--research-only` checks just the research structure. These are document
integrity checks, not certification of mathematical correctness.

## Contribute

Pull requests are welcome for research contributions, source corrections,
proof audits, manuscript fixes and reproducibility improvements. Describe the
exact claim and hypotheses, cite source versions, and report the checks you
actually ran. Read [AGENTS.md](AGENTS.md); manuscript edits also follow
[paper/AGENTS.md](paper/AGENTS.md). Claim promotion requires the existing
independent-review process and owner integration. Lean changes belong in
[navier-formal](https://github.com/itpplasma/navier-formal).

For classical NS-R3 the immediate obstacle remains one common Schwartz initial
trace for an entire coupled viscous history, or an input-derived critical bound
on the regularity route. The relativistic current allocation is in PLAN.
Neither gap may be replaced by a criterion that assumes the needed estimate.

## Public status and provenance

`navier` and `navier-formal` became public on 2026-09-08. On 2026-09-09 the
owner authorized moving the manuscript sources into [paper/](paper/) and
archiving the former `navier-paper` repository. The old private repository
retains historical commits; the manuscript content is now public here. The
[migration record](research/evidence/2026-09-09-paper-migration.md) identifies
the imported revision and verification performed.

The manuscript, research notebook and formalization are parts of the same
project, not separate prior presentations. See the
[CP1 provenance clarification](research/evidence/cp01-provenance-clarification-2026-09-09.md).
Public hosting makes no priority, prize or submission claim. The former
Overleaf project remains retired. Code is licensed under Apache-2.0; prose
and mathematics, including the papers, under CC BY 4.0. See [LICENSE](LICENSE).
