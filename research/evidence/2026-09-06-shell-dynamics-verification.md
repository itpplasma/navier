# Shell-dynamics checkpoint: execution and verification record

Date: 2026-09-06. Scope: source replay, finite regression and document
integrity. This is not an independent mathematical audit, a Lean proof,
or verification of the arbitrary-data critical bound.

## Pushed and replayed revisions

The frozen component was pushed through the GitHub connector to
`itpplasma/navier-paper`, commit
`a9993cccee0f9544c49f9c98524c6c4af4c0e080`.

After refreshing main and applying guarded source integration, the
research workflow committed and pushed
`b6acbd574b1ea5d2d887da84fe70f893e00b64fe`; the paper workflow committed
and pushed `a7dbeb54fcf4e966ae9b59196529c30988f7a36c`.
Both revisions were confirmed as their respective remote main heads
before this verification-record commit. Pushes were non-force; unsigned
commits were explicitly authorized by the owner.

Research run `34044385903` completed successfully, including integration,
structural checks, authoritative map regeneration and push. Its private
artifact `9992638584` was downloaded through the connector and extracted.
Paper run `34044468370` completed successfully, including all six component
regressions, builds, reference/overflow rejection, refreshed integration
checks and push. Its private artifact `9992683634` was likewise downloaded.
The archives' source-commit files match the integrated revisions above.

Eight affected paths in each archive were compared byte for byte against
the locally checked work. All matched, including both integration scripts,
workflows, the frozen section, live plan, evidence, main manuscript,
README files, Makefile, proof graph and generated maps.

## Frozen source and graph digests

- `sections/shell_dynamics.tex`: SHA-256
  `66f3ff185f220e8be874ea2090bc982abe42b4208ee093dc6799b5ee015e5677`.
- `docs/proof-graph.yaml`: SHA-256
  `c098f2a4d744c075a4352ecae6bf55a9927dd81ebc70294ef27612fe9a6e0f7e`.
- Generated research and paper map sources, identical: SHA-256
  `f9dff6f235a85db74f0fab2b5d0e294bfc1835fdb3eaa6671d92484cf7cb96fa`.
- Integrated `main.tex`: SHA-256
  `77e3ec57f2bb69881c09d206c0f9cd5f055330b3b53a7571b62254fe9bc4ce09`.

## Checks actually run

The default research verifier passed on the downloaded source snapshots:
29 acyclic claim records, existing evidence, statuses, manuscript labels
across seven included TeX sources, seven pending supplements, and the
actual formal repository manifest fetched read-only through the connector.
Checking that manifest is not a Lean build.

The new finite regression passed: frozen source and labels; exact rational
9/8 and 9/4 constants; degenerate PSD cases; exact rational ridge-envelope
and derivative identities; 2003 deterministic natural-distance probes.
All predecessor component regressions also passed. Both integrators passed
idempotent check mode on the downloaded integrated snapshots.

The main manuscript, generated proof map and standalone clock document
built locally and remotely. Their final logs contained no undefined
references, undefined citations or overfull boxes. The local BibTeX command
used the installed `bibtex.original` executable because the container's
`bibtex` alternatives symlink was broken; no repository build setting was
changed for this local environment issue.

The remote PDFs have respectively 131, 18 and 4 pages. Their 1435, 122 and
16 internal/named link annotations were checked for valid page targets;
none had an invalid target. The abstract, new Section 15 on pages 125--129,
and added map page were rendered and visually inspected. This is not a
claim of a new visual audit of all preceding manuscript pages.

## Mathematical status, unchanged by successful execution

The new component derives natural-variable time regularity, the
pressure-free local derivative estimate, and the exact evolution of finite
regularized speed-shell residuals. It does not establish endpoint control
of the evolution drivers or uniformity in vanishing regularization.
The bound on L_c from arbitrary data, the fourth-power defect producer,
HIGH-PRESSURE, HIGH-STRAIN, DEFECT-L4 and NS-R3 remain unproved.
The new component and its pending predecessors still require independent
mathematical review. No formal claim was promoted or formal source edited.
