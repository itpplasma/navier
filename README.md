# Navier–Stokes research programme

This public repository contains research notes, manuscript sources and proof
maps for the original unforced three-dimensional Navier–Stokes problem on
whole space. **Global regularity for arbitrary Schwartz data is not proved,
and no unforced counterexample has been constructed.**

The main manuscript establishes a conditional route through a missing
critical estimate. Current research also investigates whether a continuously
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

The immediate research obstacle is one common Schwartz initial trace for an
entire coupled viscous history. Euler preparation and signed pressure control
provide useful clues; their positive-viscosity transfer is unproved. The
regularity route still lacks an input-derived critical bound. Contributions
should address the precise gates in PLAN rather than assume either gap away.

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
