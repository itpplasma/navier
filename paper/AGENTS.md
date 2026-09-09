# Manuscript rules

The root `../PLAN.md` and `../AGENTS.md` own live status and policy. The owner
authorized moving these manuscripts into public `navier/paper/` on 2026-09-09.
The old `navier-paper` repository is a historical archive. Earlier instructions
in `history/` are retained for provenance and do not govern new work.

Keep all unproved hypotheses and review qualifications explicit. Mathematical
changes require a frozen candidate and an independent scoped audit before
claim promotion. A source move, build or proof-map update changes no theorem
status. Do not add authorship or submit the manuscripts without authorization.

Generate `proof_map.tex` from `../docs/proof-graph.yaml`; never edit generated
map claims by hand. Run `make documents check`, then from the repository root
run `python3 research/verify.py --paper-only` (or the full verifier when the
formal checkout is available). Inspect changed rendered pages and map links.
Do not commit PDFs, TeX auxiliaries or caches. Historical integration scripts
are provenance tools; do not run them to reset the current PLAN or README.
