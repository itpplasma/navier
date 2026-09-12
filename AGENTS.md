# Navier–Stokes research contract

Read `PLAN.md` first; it is the sole live task/status record. Then read the relevant terminal path in `docs/proof.md`, `docs/proof-graph.yaml`, the cited evidence, and `research/verify.py`. `docs/programme-graph.yaml` contains unproved specifications and is never proof evidence.

Preserve the original whole-space unforced incompressible Navier–Stokes terminal target. Forced, averaged, modified-dissipation, finite-moment, stochastic, periodic, microscopic or other companion equations require separate contracts.

State the exact estimate or construction, data/solution class, constant dependence, complete consumer chain and first uncontrolled term before substantial work. Attack arbitrary amplitude and limiting uniformity first. A criterion, representation, local estimate, known identity, new functional, simulation, build or documentation update is not terminal mathematical progress.

Keep evidence classes separate: exact analytic result, source-inspected theorem, author proof, independent audit, formal verification, rigorous numerics and ordinary numerical experiments are different. Numerical PDE evidence may discriminate or generate hypotheses but cannot prove universal regularity or blowup.

Two serious returns to the same unknown critical quantity require a genuinely different mechanism. Do not rename an equivalent criterion and call it progress.

## Frontier game

Use DISCOVER / FALSIFY / REPAIR / REVIEW / INTEGRATE against the first unresolved terminal dependency.

- **DISCOVER:** seek genuinely different regularity or blowup mechanisms; current PLAN routes are priorities, never a whitelist.
- **FALSIFY:** attack the exact producer with the cheapest applicable analytic contradiction, scaling obstruction, packet counterexample, or other rigorous hostile control.
- **REPAIR:** change the first failed implication while preserving sound downstream consequences conditionally.
- **REVIEW:** freeze the candidate statement and audit quantifiers, solution class, forcing status, uniformity and all limiting steps.
- **INTEGRATE:** only after a genuine mathematical delta; update authoritative state once and preserve provenance.

For candidate blowup mechanisms, finite packet/symbolic calculations may falsify a proposed interaction law but never establish an actual NS singularity. For candidate regularity mechanisms, known continuation criteria are consumers unless the route supplies their arbitrary-data critical input.

After two serious cycles returning to the same critical obstruction, change mechanism materially: geometry, representation, scale decomposition, kinetic interface, pressure mechanism, material dynamics, rigorous computer-assisted route, or another genuinely distinct framework.

A theorem, obstruction, experiment or commit is a checkpoint, not a stopping condition. After each genuine delta: integrate it, run the directly relevant existing check(s), commit/push, recompute the terminal frontier, and continue.

## Keep the game lean

There is **no generic executable game layer**. Do not recreate `research/game/`, snapshots, baseline/refuted models, replay/discriminate commands, or game-specific CI.

Use existing project checker scripts directly. Add a new checker/control only for a reusable exact obstruction, counterexample to an inference, evidence-class trap, or terminal-interface regression that future work is likely to violate. Positive lemmas do not automatically need controls.

One mathematical delta should normally produce one coherent integration commit: proof/obstruction + PLAN/proof-graph update + any genuinely necessary reusable checker/control. Do not create separate bookkeeping commits merely to mirror, freeze or refresh the same result.

Formalization remains downstream of reviewed mathematics. `navier-formal` contains formal interfaces/coverage; formal kernel success does not by itself establish statement faithfulness. Preserve source provenance and licensing rules in the existing repository documentation.
