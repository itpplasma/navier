# Speed-shell checkpoint: mechanical validation (2026-09-06)

This is a document/build record, not an independent mathematical audit.
The component proof and its exact unproved temporal step are recorded in
`2026-09-06-speed-shell.md` and in the manuscript's Section 14.

## Verified integrated revisions

- Research integration: `07ded1c45a45ee69a548ab1a3515b8abfba0093d`.
- Paper integration: `f01941b2e964be64a357f925f835afba1384f1c5`.
- Frozen new proof: `5643f3e53ce837896fdd69247c3972ba4180ebfa`,
  `sections/speed_shell.tex`, SHA-256
  `6d4ed41005c59d2734a1befc41779ec63e0bd6805c3178dc42b54c9a0efae4da`.

GitHub Actions research run `34041807209` and paper run `34041828181`
completed successfully. Both refreshed main, applied guarded integration,
checked the changes, committed explicit paths, refreshed before non-force
pushes, and retained private artifacts. Research artifact `9991895152`
and paper artifact `9991922312` were downloaded and replayed locally.
The source archives identify the integrated revisions above, not merely
the workflow-triggering commits.

## Replayed checks

The downloaded research status files, graph, evidence and integration script
match the locally tested sources byte for byte. The downloaded manuscript,
README, Makefile, proof map, new section, regression and integration scripts
also match their locally tested sources byte for byte. The paper map equals
the map generated from the authoritative research graph.

`python3 research/verify.py` passes on the matched research and paper trees:
29 acyclic claim records, 6 explicitly pending supplements, evidence files,
all manuscript labels across 6 TeX sources, and formal manifest presence.
Only the actual `navier-formal/lakefile.toml` was fetched for that final
presence check; no Lean compilation, coverage check or axiom audit was run.
Both guarded integration scripts pass `--check` after integration.

All five paper regression targets pass: `check-clock`, `check-defect`,
`check-conformal`, `check-signed`, and `check-shell`. The new regression
checks frozen source, labels, exact flux and Young/clock constants, critical
scaling and 400 finite weighted projection examples. These are finite
algebra/source regressions, not PDE trajectory tests or independent audits.
`git diff --check` and the remote undefined-reference/overflow gates pass.

Both local and remote manuscript builds have 127 pages; the proof map has
17 pages. The new component is Section 14, manuscript pages 121--125.
Changed manuscript pages and map pages were rendered and visually inspected.
All 1414 manuscript and 122 map link targets resolve, in both builds.
The new section's extracted text agrees between the local and remote builds.
The complete PDFs are not claimed byte-identical: fonts and build metadata
differ. Remote Type-3 font extraction also differs for an old bullet and
some map characters, while rendering is intact. The supplied downloadable
PDFs use the local builds of the byte-matched committed sources.

## Mathematical boundary unchanged

No independent reviewer has audited the new component or the earlier
review-pending signed-work and quotient-clock components. No open graph node
was promoted. In particular the input-only bound on the accumulated combined
rate L_c remains unproved, as does the arbitrary-data fourth-power defect
bound. Successful integration and builds do not supply that missing estimate.
