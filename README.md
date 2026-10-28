# Navier-Stokes research programme

Research notes, manuscript sources and proof maps on the global regularity
problem for the unforced three-dimensional incompressible Navier-Stokes
equations on whole space (Clay problem, alternative A).

Status: global regularity for arbitrary Schwartz data is **not** proved, and
no unforced counterexample has been constructed. The main manuscript gives a
conditional route that reduces the problem to one missing critical estimate.

## Contents

- `paper/`: manuscript sources. The main manuscript (conditional
  critical-norm route: local theory, energy, pressure and quotient
  estimates), a paper on structural obstructions, two standalone components
  and a clickable proof map. See [paper/README.md](paper/README.md).
- [docs/proof-graph.yaml](docs/proof-graph.yaml) and
  [docs/proof.md](docs/proof.md): the claims of the conditional route, their
  dependencies, hypotheses and review status. A claim marked `paper` has a
  written argument; author proofs, independent audits and Lean checks are
  recorded as different kinds of evidence.
- `research/`: derivations, falsification examples and scoped audits
  ([research/evidence/](research/evidence/)), and Python/SymPy checks of
  individual algebraic identities.
- [literature/](literature/README.md): inspected source statements and their
  applicability limits.
- [docs/relativistic-viscous-programme.md](docs/relativistic-viscous-programme.md):
  a companion programme asking whether causal relativistic viscosity (BDNK)
  prevents or changes finite-time breakdown, with results so far.
- [PLAN.md](PLAN.md): the current research question and open gaps.

The Lean formalization of parts of the argument is in
[navier-formal](https://github.com/itpplasma/navier-formal).

## Building the papers

On Debian/Ubuntu install `latexmk`, `texlive-latex-extra`,
`texlive-fonts-recommended`, `texlive-science`, `lmodern` and `python3-yaml`,
then run from the repository root:

```sh
make -C paper documents check
python3 research/verify.py --paper-only
```

This builds `main.pdf`, `proof_map.pdf`, `structural-obstructions/main.pdf`,
`dissipation_clock.pdf` and `dissipation_budget_continuation.pdf` in `paper/`
(PDFs are not committed; the GitHub Actions document workflow provides them
as artifacts). `research/verify.py` checks document and graph consistency;
without `--paper-only` it also checks the manifest of a sibling
`navier-formal` checkout, and `--research-only` checks only the research
structure. These are integrity checks, not certification of the mathematics.

## Contributing

Pull requests with source corrections, proof audits, manuscript fixes and
reproducibility improvements are welcome. State the exact claim and its
hypotheses, cite source versions, and report the checks you ran. Manuscript
edits follow [paper/AGENTS.md](paper/AGENTS.md); Lean changes belong in
navier-formal.

## License

Code (Python checks, workflows, machine-readable files) is under Apache-2.0;
prose and mathematics, including the papers, under CC BY 4.0. See
[LICENSE](LICENSE). The manuscripts, research notes and formalization are
parts of one project; public hosting makes no priority claim (see the
[provenance note](research/evidence/cp01-provenance-clarification-2026-09-09.md)).
