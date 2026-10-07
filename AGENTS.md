# Navier–Stokes research contract

Read `PLAN.md` first; it is the sole live task/status record. Then read the relevant terminal path in `docs/proof.md`, `docs/proof-graph.yaml`, the cited evidence, and `research/verify.py`. Load only the history needed for the active question. `docs/programme-graph.yaml` contains unproved specifications and is never proof evidence.

Preserve the original whole-space unforced incompressible Navier–Stokes terminal target. Forced, averaged, modified-dissipation, finite-moment, stochastic, periodic, microscopic or other companion equations require separate contracts.

State the exact estimate or construction, data/solution class, constant dependence, complete consumer chain and first uncontrolled term before substantial work. Attack arbitrary amplitude and limiting uniformity first. A criterion, representation, local estimate, known identity, new functional, simulation, build or documentation update is not terminal mathematical progress.

Keep evidence classes separate: exact analytic result, source-inspected theorem, author proof, independent audit, formal verification, rigorous numerics and ordinary numerical experiments are different. Numerical PDE evidence may discriminate or generate hypotheses but cannot prove universal regularity or blowup.

## Self-contained frontier method

This repository must remain usable by agents that cannot see any external prompt/skill repository. Use this method directly.

Before substantial work, freeze a compact working packet:

```text
TERMINAL CLAIM: exact target, data class, solution class and conclusion
ESTABLISHED: only facts needed by the proposed step
FIRST GAP: first uncontrolled estimate, implication or construction
FALSIFIER: what would defeat the proposed mechanism
FORBIDDEN INFERENCES: exact known errors relevant here
CHECK: analytic proof obligation, counterexample, source audit, or exact computation
```

Work backward from the terminal claim to the first load-bearing gap. For regularity routes, a continuation criterion is a consumer unless the route produces its arbitrary-data critical input. For blowup routes, a finite interaction model is not the terminal singular solution.

Use one mode at a time:

- **DISCOVER:** seek genuinely different regularity or blowup mechanisms. Current PLAN routes are priorities, never a whitelist.
- **FALSIFY:** attack the exact producer with the cheapest rigorous contradiction, scaling obstruction, packet counterexample, or other hostile control.
- **REPAIR:** identify the first failed implication and replace that bridge while preserving any sound downstream consequences conditionally.
- **REVIEW:** freeze the candidate statement and adversarially audit quantifiers, forcing status, solution class, uniformity, constants and limiting steps.
- **INTEGRATE:** after a durable mathematical delta, minimize dependencies, update PLAN/proof graph once, run directly relevant checks, commit/push, and recompute the terminal frontier.

Stop an argument at the first unsupported inference. Do not rename an equivalent criterion, local estimate, compactness statement, or missing critical norm and call it progress.

### Prediction before experiment

When a proposed mechanism has an exact computable consequence, state the prediction **before** testing it. If competing mechanisms predict different exact outcomes, choose the cheapest exact or rigorous test that separates them. Exact finite-mode/symbolic calculations can falsify an interaction mechanism; numerical simulations remain heuristic unless accompanied by a rigorous error enclosure at the exact needed scope.

When review defeats a route, blacklist the failed inference rather than the whole framework. Reopen it only if a new prerequisite directly addresses the obstruction. There is no fixed failure quota: a decisive falsifier can stop the first test, while a productive mechanism may justify many steps. When several variants return to the same exact loss, retrieve that common failure and continue only with a named new premise or a changed inference that pays that loss.

Evidence discipline:

```text
finite/numerical evidence != universal proof
formal proof != statement faithfulness
continuation criterion != production of its hypothesis
model interaction != NS blowup construction
special class != arbitrary-data theorem
literature theorem != verified applicability
review verdict != project promotion
```

## Win gate, exact-loss design, and model separation

Keep at most **one unsupported hard producer** in an active attempt. For a regularity route, a continuation criterion is a consumer until the original data are proved to produce its critical hypothesis. For a blow-up route, a profile, finite interaction model, forced history or singular ansatz is a consumer until an actual solution of the stated PDE with the stated data and forcing status is constructed. For a model-comparison route, analogy and formal limits do not count: the same physical state must be transported through a proved source/model adapter.

A durable mathematical delta must do at least one of: complete the exact terminal claim; construct an exact counterexample in its stated model; exclude a nonempty surviving breakdown/regularity class by an unconditional theorem; or decisively refute a serious proposed bridge. State the BEFORE/AFTER surviving class when that language applies.

Design new machinery around the **exact loss**. Write the missing power, sign, derivative, compactness, source term or scale before introducing a representation. Temporary structure earns use only if it compensates for that named deficit. Preserve vector signs, coupled equations and common-source information until their loss is justified. Separate construction from closure/rigidity, record the order in which parameters and scales are chosen, and inspect equality/extremal profiles when a sharp estimate makes them informative.

Relativistic and kinetic companion problems live under separate contracts; see `docs/relativistic-viscous-programme.md`. BDNK, Müller--Israel--Stewart/DNMR, extended causal closures, classical Navier--Stokes and kinetic equations are not interchangeable. State the exact stress tensor, frame, equation of state, transport coefficients, forcing/source, domain, data class and admissibility regime before transferring a result. A nonrelativistic or hydrodynamic limit counts only with the uniform estimate needed by the proposed inference. Distinguish three conclusions: PDE regularity of a closure, remaining inside the closure's validity regime, and regularity of an underlying kinetic model.

OpenAI's forced Navier--Stokes construction is a source of mechanisms and hostile controls, not a solution of this repository's unforced `NS-R3` target. Likewise the archived OpenAI Vlasov--Maxwell result in `itpplasma/vlasov-maxwell` is an external claim under independent reconstruction; its exact-loss/signed-impulse strategy may motivate a test without importing its theorem.

Use symbolic/numerical/search/proof tools only against named information targets. Preserve tested scope, error control and non-claims. One controller owns authoritative promotion; parallel workers, when used, return evidence and should attack genuinely different mechanisms rather than correlated variants.

## Research waves, commits, and persistence

Work in **coherent research waves**, not bookkeeping steps. A wave is a sustained attack on one first-gap mechanism through its dependent estimates/lemmas until it advances, is repaired, is falsified, or reaches a new precise blocker.

Do **not** update PLAN/proof graph, add controls, or commit after every algebraic identity, local estimate, finite packet check, simulation or tiny lemma. Keep routine calculations, failed probes, exploratory numerics, temporary scripts and intermediate notes ephemeral unless independently reusable.

A durable checkpoint worth integrating and pushing is normally one of:

- an estimate/lemma materially advancing or closing the current first gap;
- an exact obstruction/counterexample killing a live mechanism;
- a reusable hostile control against a recurring invalid inference;
- a coherent cluster of dependent results closing a meaningful subdependency;
- a route-changing repair, verified external theorem interface, or frontier reassessment.

At such a checkpoint, integrate the mathematics and authoritative frontier change in **one coherent commit** where practical, run only the checks relevant to the changed claim, commit and push, then continue immediately. If a long wave produces several independent durable deltas, checkpoint between them so useful work is not left unpushed.

Do not make commits whose only purpose is mirroring, refreshing, serializing or restating state. Positive lemmas do not automatically need regression controls.

A theorem, obstruction, experiment or commit is a checkpoint, not a stopping condition. Continue toward the terminal mission while an executable distinct route remains.

## Keep machinery minimal

There is **no generic executable game layer**. Do not recreate `research/game/`, snapshots, baseline/refuted models, replay/discriminate commands, or game-specific CI.

Use existing project checker scripts directly. Add a checker/control only for a reusable exact obstruction, counterexample to an inference, evidence-class trap, or terminal-interface regression that future work is genuinely likely to violate.

Formalization remains downstream of reviewed mathematics. `navier-formal` contains formal interfaces/coverage; formal kernel success does not by itself establish statement faithfulness. Preserve source provenance and licensing rules in the existing repository documentation.
