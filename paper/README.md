# Manuscripts and proof map

These are the public manuscript sources for the Navier–Stokes research
programme. **Global regularity for arbitrary Schwartz data remains unproved,
and no unforced counterexample has been constructed.** The main manuscript
proves a conditional route and identifies the missing critical estimate.
The [live PLAN](../PLAN.md) also tracks newer research that has not been
promoted into manuscript theorems.

| Document | Scope | Build output |
| --- | --- | --- |
| [Main manuscript](main.tex) | Conditional critical-norm route, local theory, energy, pressure and quotient estimates; later components have explicit pending-review status | `main.pdf` |
| [Clickable proof map](proof_map.tex) | 29 canonical claims, their dependencies, evidence and review status; eight pending supplements are listed separately | `proof_map.pdf` |
| [Structural obstructions](structural-obstructions/README.md) | Scoped quadratic-form and matched-scalar obstructions, with author-proof and prior-art qualifications | `structural-obstructions/main.pdf` |
| [Dissipation clock](dissipation_clock.tex) | Standalone rendering of the component also included in the main manuscript | `dissipation_clock.pdf` |
| [Dissipation-budget continuation](dissipation_budget_continuation.tex) | Separate review-pending continuation component | `dissipation_budget_continuation.pdf` |

## Build and verify

From the repository root:

```sh
# Debian/Ubuntu dependencies:
sudo apt-get install latexmk texlive-latex-extra texlive-fonts-recommended texlive-science python3-yaml
make -C paper documents check
python3 research/verify.py --paper-only
```

The default verifier additionally checks the manifest in the sibling
`navier-formal` checkout. The Python component checks combine source checks
with finite arithmetic/algebra probes; neither they nor a successful LaTeX
build constitute mathematical certification or independent review.

`make -C paper documents` regenerates both `paper/proof_map.tex` and
`docs/proof_map.tex` from [the authoritative graph](../docs/proof-graph.yaml),
then builds all five PDFs. Map nodes link to claim descriptions, and each
claim description links back to the map. The manuscript label printed in each
entry locates its theorem in `main.pdf`. Pending supplements are not promoted
claim nodes. PDF files and auxiliaries remain local and are ignored by Git.
The [document workflow](../.github/workflows/dissipation-clock.yml) builds
these PDFs and offers them as downloadable GitHub Actions artifacts.

## Provenance and contributions

The sources were moved from `itpplasma/navier-paper` at commit
`b6d0c6100ceba3783dc0c1bc8de4df3e1089396c` on 2026-09-09. The
[migration manifest](migration-source.json) records the original tracked
files and their SHA-256 hashes. Historical instructions, workflow and component
summaries are retained in [history/](history/README-before-migration.md).
Historical source commits in the graph remain provenance records in the
archived repository; current editable sources are here.

These manuscripts and the research notebook belong to the same project;
internal chronology is not external literature or a priority claim. See the
[CP1 provenance clarification](../research/evidence/cp01-provenance-clarification-2026-09-09.md).
The repository [licences](../LICENSE) cover code (Apache-2.0) and prose and
mathematics (CC BY 4.0). Authorship and mathematical review status are unchanged.

PRs with source corrections, reproducibility fixes and scoped proof reviews
are welcome. Read [the manuscript rules](AGENTS.md) and preserve the distinction
between established premises, conditional conclusions and missing estimates.
