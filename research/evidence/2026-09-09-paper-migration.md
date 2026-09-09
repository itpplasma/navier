# Public manuscript migration and document verification

Owner request: 2026-09-09, move the manuscript into public `navier`, add a
useful README, archive `navier-paper`, and check the proof map and documents.
Research base: `177a5f2` (the fetched main revision). Manuscript input:
`itpplasma/navier-paper@b6d0c6100ceba3783dc0c1bc8de4df3e1089396c`.
Both working trees were clean before migration.

## Source preservation and ownership

All tracked manuscript-repository files were copied into `paper/`.
`paper/migration-source.json` records every original file's SHA-256 and the
exact source commit. Old instructions, README and workflow were moved into
`paper/history/`; the active documents now describe the consolidated layout.
All mathematical TeX sources other than the generated map, and the
bibliography, were checked byte-for-byte against the imported fingerprints.
No mathematical statement, author attribution or review status was changed.

The old repository retains its private historical commits. Its active editing
role ends after the verified public copy is pushed; a redirect is installed
before archival. Historical graph source commits and paths remain provenance,
with current manuscript/map locations recorded separately. The manuscripts
are internal project work, not an additional external literature premise.
Public hosting is authorized; submission and outside contact are not.

## Build and map checks

Observed local verification on 2026-09-09:

- `make -C paper documents check` passes, including all seven existing
  component checkers. Two README-phrase assertions were removed from migrated
  checkers; their source, constant and numerical/algebra checks remain.
- The five PDFs build: main manuscript 137 pages; proof map 19 pages;
  structural-obstructions paper 12 pages; dissipation clock 4 pages;
  dissipation-budget continuation 7 pages.
- No undefined-reference, undefined-citation or overfull-box warnings were
  found in the final five LaTeX logs.
- Both map sources were regenerated from `docs/proof-graph.yaml`. Edges now
  draw behind the nodes so that crossings do not obscure claim text. The
  graph retains the same 29 claims and eight pending components; no status
  or dependency was changed. Its generated fingerprint is current.
- All 65 manuscript labels cited by the graph and its pending supplements
  resolve through the built LaTeX auxiliary file into named PDF destinations.
  All 1,469 named links in the main PDF and 122 in the map resolve. The 29
  map-node anchors and map-return anchor are present. Map-to-description and
  description-to-map destinations were inspected.
- Rendered first pages of the main manuscript, structural-obstructions paper
  and final map were visually inspected. The overview is dense and intended
  for zooming; detailed claim descriptions follow it.
- `python3 research/verify.py` passes, including manuscript labels across
  eight TeX sources and the sibling formal repository's manifest.
  `--paper-only` checks a standalone public checkout without the formal repo;
  `--research-only` remains available for research-only structure checks.
- `git diff --check` and the prose heading checker pass.

The old README's `dc:l9` failure was stale: the refreshed source includes the
label, and the full verifier passed before migration as well. No mathematical
repair was needed. PDF/link inspection used temporary PyMuPDF/pypdf tooling;
PDFs, virtual environments and build products are not committed.

The previous workflow rewrote research state and pushed commits. It is
replaced by a read-only push/PR workflow that builds all papers, rejects stale
map sources and unresolved references, and uploads PDF artifacts. Legacy
integration scripts are retained as historical tools, not run during CI.

These checks establish source preservation, buildability and document/map
consistency. They are not a new mathematical audit, Lean build, axiom report,
proof of global regularity or construction of an unforced counterexample.

The first GitHub document build exposed a missing `lmodern` font package in
the minimal CI environment. The dependency list and installation step were
corrected; this required no manuscript change. The corrected
[GitHub build](https://github.com/itpplasma/navier/actions/runs/34317565484)
succeeded on `50bf66e`, including clean map regeneration and all five PDF
artifacts. GitHub emitted a non-blocking Node.js runtime deprecation warning
for the pinned checkout/upload actions; updating those pins is separate
maintenance. The formal repository's live manuscript pointers were also
updated to `navier/paper/`, preserving concurrent provenance clarifications;
no Lean source, axiom or coverage status was changed.

## Archive completion

Public migration commit: `57accaa65a10f1957e81b21695364cebc9af1467`.
GitHub served `paper/main.tex` from that public repository after the push.
The old repository then received redirect commit `d6ac1a0`, and the GitHub
API confirmed `archived: true`, `private: true` on 2026-09-09. New manuscript
work belongs in `navier/paper/`.
