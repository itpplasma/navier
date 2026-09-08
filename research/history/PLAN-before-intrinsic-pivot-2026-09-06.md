# Navier–Stokes programme

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: formalization-reopened-2026-09-06
phase_i_status: reopened-2026-09-06-in-progress
phase_ii_status: reopened-2026-09-06-target
paper_status: active-paper-proof-work-2026-09-06
paper_repo: writable-authorized-2026-09-06
external_deps: permitted-if-no-axioms-beyond-mathlib
active_task: corotational-material-action-and-independent-audit
public_release: false
```

## Objective

Resolve Clay's unforced existence-and-smoothness alternative on R3: for every
smooth divergence-free rapidly decreasing initial velocity and every viscosity
nu > 0, construct a global smooth velocity and pressure satisfying the original
equation and a uniform finite kinetic-energy bound. The exact official data
class and alternatives are recorded in the literature dossier. The periodic
problem is a separate alternative, not an automatic corollary of the R3 proof.

## Authority

`docs/proof-graph.yaml` is the dependency map; `docs/proof.md` gives the
paper argument and exact open bridge. `literature/` holds source evidence.
`research/verify.py` checks structural consistency only. Independent review
of mathematical implications is required separately. The manuscript lives in
`../navier-paper`; the Lean development, its coverage manifest, and its
literature-assumption register live in `../navier-formal`. `AGENTS.md` holds
the repository split, model policy, and boundaries.

## Programme structure toward the Millennium result

Two tracks run under one controller. On 2026-09-05 (evening) the user
re-sequenced them: **paper proofs of everything come first**; Lean
formalization of any block waits until the complete paper route is proved
and audited, so that no effort is spent formalizing steps that a later
paper result might replace.

- **Track A, checkpoint CP1 on paper.** The reduction block is now written
  in full (gate 1, pending the integration audit). Its Lean phases I and II
  remain authorized but are deferred; the existing formal repository and
  the CP04 design note are kept as a resumable starting point and are not
  extended until the user reopens formalization.
- **Track B, closing the gap on paper.** The priority is now the missing
  arbitrary-data critical producer, HIGH-PRESSURE or its alternative
  HIGH-STRAIN, following the ordered research stages below. Every
  candidate is frozen and audited before integration into the manuscript
  and graph. When the full route to Clay alternative A is proved on paper
  and passes separate component and integration audits, formalization of
  the whole route begins, Phase I then Phase II.

CP1 is published, when the user decides, as a piece of the work. It is not
the Millennium result. The programme does not stop at CP1.

## Checkpoint CP1: the high-frequency / high-pressure reduction block

CP1 consists of the following nodes of `docs/proof-graph.yaml`, with the
manuscript labels of `../navier-paper/main.tex` at commit `909ff21`:

| Graph node | Manuscript label | Kind |
| --- | --- | --- |
| TAO-LOCAL, TAO-MAXIMAL, TAO-MILD | `thm:tao54`, `thm:tao58`, `thm:tao43` | imported: Tao 2013 Theorem 5.4, Corollaries 5.8 and 4.3 |
| ESS | `thm:ess` | imported: Escauriaza–Seregin–Šverák Theorem 1.3 |
| LERAY-L3 | `lem:leray` | imported: Leray projection bounded on L3 |
| LOCAL | `prop:localtheory` | paper: maximal development and regularity package |
| ENERGY, SCALE, ENSTROPHY, ODE | `prop:energy`, `prop:scaling`, `prop:enstrophy`, `prop:ode` | paper |
| PRESSURE, LOW-PRESSURE, EXISTENTIAL | `prop:pressure`, `prop:lowpressure`, `prop:existential-equivalence` | paper |
| LERAY-HOPF, SERRIN, CONTINUATION | `lem:leray-hopf`, `lem:serrin-enstrophy`, `thm:continuation` | paper |
| CONDITIONAL | `thm:conditional` | conditional on CRITICAL |
| QUOTIENT-FUNCTIONAL, QUOTIENT-EVOLUTION | `prop:quotient-derivative`, `prop:quotient-evolution` | paper (HF17, audited) |
| QUOTIENT-CONDITIONAL | `prop:quotient-conditional` | conditional on HIGH-STRAIN |

The open nodes CRITICAL, ABSORPTION, HIGH-PRESSURE, and the alternative
HIGH-STRAIN are not part of CP1's proved content. CP1 states them as explicit
hypotheses. A CP1 theorem in Lean therefore has the shape "literature inputs
and the open estimate imply the Clay conclusion", plus unconditional proofs
of every paper node.

Stage gates for CP1:

1. **Paper proof complete.** Every manuscript-owned step is written out in
   full, self-contained, with exact function spaces, regularization and limit
   arguments, and primary sources for every external fact. Each result has
   passed a within-family adversarial audit with a different tier or lens
   than its author. The quotient section is restructured into labelled
   propositions with complete proofs. Gate check: `cp02-review-*.md` PASS
   records, rebuilt manuscript and map, graph nodes updated.
2. **Phase I complete.** `../navier-formal` proves every paper node in Lean,
   with literature theorems as named axioms in `NavierFormal/Literature/`
   carrying verified source records, and Challenge/Solution state the
   conditional theorem with those literature inputs as explicit hypotheses.
   Gate check: `lake build` with zero sorries outside the deliberate
   Challenge holes, axiom reports listing only standard axioms plus the
   declared literature axioms, and a faithfulness audit comparing each Lean
   statement with the manuscript (`docs/paper-lean-specification.md`).
3. **Phase II complete.** Every literature axiom is proved from Mathlib, or
   decomposed into published lemmas that are proved from Mathlib. Gate
   check: standard axioms only, Palomar Comparator preflight passing
   locally, coverage manifest regenerated. Registration itself remains a
   separate user decision.

## Execution order

| Wave | Content | Evidence prefix |
| --- | --- | --- |
| CP01 | Understand and specify: manuscript obligations, exact literature statements, Mathlib coverage, Lean statement design, Palomar checklist, completeness critic | `cp01-` |
| CP02 | Paper proof: write complete proofs per obligation, adversarial audits, controller integration into the manuscript and graph | `cp02-` |
| CP03 | Lean statement surface and infrastructure in parallel with CP02: definitions, Challenge/Solution skeleton, calculus and Lp lemmas that CP1 needs regardless of proof details | `cp03-` |
| CP04 | Phase I modules per paper node (deferred until the full paper route is proved; design note `cp04-phase-i-design.md` kept) | `cp04-` |
| CP05 | Phase I faithfulness audit and axiom report; gate 2 | `cp05-` |
| CP06 | Phase II disposal: classify each literature axiom as M or F, decompose into published lemmas with sources, order by dependency | `cp06-` |
| CP07+ | Phase II modules until gate 3; Palomar preflight | `cp07-` |

Track B waves keep the `hf` prefix and continue from HF19; they now run ahead of CP04–CP07.

## Integration log

### CP01 outcome and binding decisions (2026-09-05)

The seven-lane specification wave is preserved at `cee98a7` (evidence
`cp01-*.md`). No manuscript step was found false; only `prop:ode` was at
full paper standard. Three items blocked a complete paper proof: the
maximal-development premise (Tao Theorem 5.4 alone does not state it), the
identification of the classical branch with the GKP maximal `L^3` solution
(no named uniqueness or persistence source), and the quotient section (a
summary of HF17, not a proof). The controller decided:

- **D1 conventions.** Tao's Fourier convention; `p = R_iR_j(u_iu_j)` equals
  Tao's normalised pressure; Littlewood–Paley low-pass is Tao's inhomogeneous
  `P_{<=N}` with a fixed bump, `S_J = P_{<=2^J}`, which coincides with the
  homogeneous sum on `L^2`.
- **D2 regularity package R.** The local-theory lane proves, from Tao
  Theorem 5.4 and Corollary 5.8 (maximal Cauchy development on R3, pp. 56–57,
  directly inspected) plus a manuscript-owned gluing lemma, that on every
  compact classical interval `u` and `p` lie in `C^j([0,T];H^k)` for all
  `j,k`, with enstrophy blow-up if `T_*` is finite. Every other lane assumes R.
- **D3 continuation route.** `thm:continuation` is restated as
  "`T_* < inf` implies `sup_{t<T_*}||u||_3 = inf`" and proved through
  ν-normalisation, membership of the classical branch in the Leray–Hopf
  class, Escauriaza–Seregin–Šverák Theorem 1.3 (numbered, directly inspected:
  Leray–Hopf plus `L^inf_t L^3_x` gives `L^5` in space-time), a
  manuscript-owned Serrin-type enstrophy bound, and the blow-up alternative.
  GKP Theorem 4 is corroboration. No `L^3` uniqueness theorem is imported.
- **D4 pressure balance** in integrated form with `D_3`, `P_3` defined
  through `(grad u)^T u` and zero integrands on the zero set; no `grad|u|`.
- **D5 standard.** Every external fact stated exactly with a primary source
  labelled directly inspected or metadata only.

Phase I literature axioms are therefore `AX-TAO-5.4`, `AX-TAO-5.8`, and
`AX-ESS-1.3`; Kato 1984 and FLRT uniqueness are not axioms. Palomar facts
that bind the formal repository: `permitted_axioms` is closed to the three
standard axioms, so Phase I results are registrable only with literature
theorems as explicit hypotheses; `Challenge.lean` must inline every
definition; `leanprover/lean4export` had no `v4.33.1` tag on 2026-09-05, so
the toolchain must be re-pinned to a tagged release before any preflight.
The critic's corrections to the Lean design are adopted: the Leray input is
needed only on `L^2 ∩ L^3`, the heat generator only for `H^m` data,
Bernstein is proved rather than assumed, the flow axiom must carry its
variational equation, and existing declaration names are reused. The bounded
prior-art search `cp01-prior-art-quotient.md` locates the mechanisms behind
the quotient functional: coset minimization with a coclosed nonlinear
representative is nonlinear Hodge theory (Sibner–Sibner 1970; Scott 1995;
Iwaniec–Scott–Stroffolini 1999), stated there for closed forms, whereas the
programme's shift `u` is divergence-free; `L^p` Lyapunov functions for
Navier–Stokes under critical smallness, the unshifted heat-generator
coercivity, and the `L^9` lower bound are Kato 1990 (LNM 1450, reproduced in
Manna–Sritharan 2007). The manuscript's quotient section therefore carries a
related-work remark and no novelty claim; the unlocated parts (the shifted
`L^3` gradient quotient as a Navier–Stokes functional, the pressure-free
evolution by inner variation, `D_Q = D_3(w)` for the shifted representative)
are recorded as unlocated, not as new.

### CP02 outcome (2026-09-05)

Seven proof lanes with independent audits and one repair round are
preserved at `c437355`. No lane contained an invalid mathematical bridge;
final verdicts are PASS for continuation, energy/enstrophy, quotient
evolution, low-frequency pressure, and quotient functional, and textual
REPAIR for local theory and pressure, applied at integration. The complete
manuscript was assembled from the audited fragments and committed at
`navier-paper` `909ff21` (81 pages, no undefined references, every graph
label exactly once). The claim graph now has 25 nodes: Tao Theorem 5.4,
Corollary 5.8 and Corollary 4.3, ESS Theorem 1.3 and the Leray projection
on L3 as imported nodes; the local-theory package, the Leray–Hopf
membership lemma, the Serrin-type enstrophy bound, the continuation theorem,
the existential equivalence, and the quotient functional, evolution and
conditional bound as paper or conditional nodes; HIGH-STRAIN as the
alternative gap. The map generator lays nodes out by dependency depth.
The cross-lane integration audit (`cp02-review-integration.md`) is the
remaining gate-1 check; gate 1 is declared only after it passes.

### Gate 1 declared (2026-09-05, navier-paper `0e0322c`)

The cross-lane integration audit `cp02-review-integration.md` passed with
ten editorial items, all applied. The user-supplied prior-art audit was
source-checked (`cp02-prior-art-related-work.md`) and woven into the
manuscript as the subsection "Related work and scope", into the literature
dossier, and into this plan; its over-claim audit
(`cp02-review-related-work.md`) returned eight precision corrections, all
applied. The manuscript at `0e0322c7ebe860810fe543dd61dbd246b474f65b` (83 pages) is the complete paper proof of
checkpoint CP1: every manuscript-owned step is proved in full, the imported
premises are Tao Theorem 5.4, Corollaries 4.3 and 5.8, ESS Theorem 1.3, and
the Leray projection on L3, and the only open content is the critical bound
with its two unproved sufficient conditions (HIGH-PRESSURE, HIGH-STRAIN).
Gate 1 of CP1 is closed. Formalization is deferred by the user's
re-sequencing; the programme continues on Track B.

### Lean progress (Track A, parallel infrastructure)

`navier-formal` at `9c8b37d` holds 70 standard-axiom declarations:
`prop:ode` complete (`scalar_obstruction_exists`), the norm half of
`prop:scaling` for every finite exponent (`eLpNorm_dilate`), the
interpolation-mismatch witness, and the pointwise regularisation calculus
and a.e. speed-gradient lemmas behind `prop:pressure`. Wave CP03c is
implementing the statement surface foundations (calculus objects, solution
class, Clay target, critical hypothesis, quotient objects, integration by
parts, interpolation). Wave CP02 (seven proof lanes with independent audits
and one repair round) is writing the complete paper proof.

## Beyond the checkpoint

Prior-art audit (2026-09-05): The 2026-09-05 audit's research priorities are
now sorted by `cp02-prior-art-related-work.md`. Done: the explicit
divergence-free profile with nonzero pressure work (HF02,
`hf02-r3-profile.md`). Folded into Track B: a partial HF theorem under a
natural Type-I or critical-concentration class; a telescoping law for the L3
pressure flux, to be built and stated as distinct from Yu's local
coarse-grained G^ell; and a constructive J_0 / A in named initial-data norms.
Out of scope: publication-strategy forecasts, workflow comparisons with public
AI proof labs, and any priority or "first" claim; the manuscript's related-work
subsection states distinctions by objects and quantifiers only, and the audit's
Zhou-2004 and Beirao-da-Veiga-1995 attributions are corrected there.

The first gap after CP1 is unchanged: an arbitrary-data signed high-output
pressure absorption estimate, or the alternative signed high-strain estimate
for the cubic gradient quotient. The reviewed obstructions of HF02–HF16 are
constraints on specific constructions, not on the target. Track B follows
the ordered research stages under the detailed research plan below; each
wave returns an actual inequality, identity, or obstruction, and every
promising candidate is frozen and audited before integration. Completion
is checked against the original target: every admissible datum, every
horizon, the original unforced equation, the strong branch selected by the
local theory, and no hidden smallness.

## Frontier packet

TERMINAL CLAIM: NS-R3, the unforced full-viscosity equation on R3 for arbitrary
Clay data, with global smoothness and finite energy.

ESTABLISHED: local classical solvability, energy dissipation, and published
continuation criteria, subject to exact source-hypothesis verification.

FIRST GAP: HIGH-PRESSURE in the graph. Prove a signed high-output pressure
absorption estimate for every arbitrary-data classical trajectory, uniform
for tau < min(H,Tstar), with a finite input-only remainder. The low-output
pressure work is already bounded by energy. Alternative producers of a
critical continuation bound remain possible.

FALSIFIER: an invalid norm interpolation, a hidden smallness hypothesis, a
bound that depends on the very norm it must control, or a change of equation.

FORBIDDEN INFERENCES: energy bounds imply critical control; an ODE upper bound
that can blow up proves PDE blowup; a conditional continuation theorem proves
its missing hypothesis; weak nonuniqueness refutes Clay smooth existence.

CHECK: direct proof and independent falsification of the proposed critical
bound, plus audit of every continuation-theorem hypothesis.

## Research history (HF01–HF17)

The sections below are the chronological record of the research waves that
produced the checkpoint. Status sentences inside them ("Phase I remains
unstarted", "neither Lean phase starts") describe the situation at the time
of each wave; the live status is the YAML header and the programme sections
above. Lane tables naming Luna or Sol record the models that ran historically.

## Paper preparation

Four Luna research lanes collected the official statement, foundational and
critical results, blowup barriers, and recent developments. Four Sol workers
developed the architecture, enstrophy and compactness evidence, a frequency
reduction, and the manuscript; distinct scopes received frozen independent
audits. The literature search is substantial but not exhaustive.

The manuscript at `navier-paper` source commit `d7563ef` contains complete written
arguments for the classical estimates, the cubic pressure balance, the
low-frequency pressure lemma, and the conditional continuation chain.
The source premises are Tao Theorem 5.4 and ESS Theorem 1.3, with GKP Theorem 4 as corroboration only, directly inspected
in the scope recorded in `literature/`. No new universal high-frequency
estimate or solution of the Millennium problem is claimed.

The evidence reviews use exact immutable revisions and distinguish valid
conditional conclusions from the unresolved terminal theorem. The final
integration review and its repair confirmation are in
`research/evidence/review-integration.md`: PASS for the conditional dossier,
FAIL WITH SCOPE for the terminal Clay claim. Its first unsupported bridge is
HIGH-PRESSURE. This is a prepared research handoff, not a completed proof of
the Millennium problem. No Lean files have been created.

## Private manuscript and verification

The manuscript authority is the private GitHub repository
`itpplasma/navier-paper`; the research repository is private `itpplasma/navier`.
Both use signed commits and local builds. On 2026-09-05 the owner requested
GitHub-only work and deletion of the Navier Overleaf project
`6a9bb675ea9d4d0d368d8ee6`. Its sources matched GitHub before deletion; the
project-list comparison confirmed that only this project was removed.
The Overleaf remote is removed. No collaborators were added or contacted.

Historical commit IDs in existing evidence resolve through each repository's
`docs/history-signing/2026-09-05-map.json`; source trees were preserved during
re-signing. Global signing defaults are managed through chezmoi.

Historical verification at the initial handoff (before Overleaf removal):

- Local manuscript and proof-map builds pass without undefined references or
  layout overflow; the manuscript is six pages and the map supplement four.
- The private Overleaf manuscript compiles successfully. Its fetched source
  matches the archive, and its rendered PDF was inspected.
- The manuscript has 49 resolved internal links, and the map has 43, including
  map-to-claim and claim-to-map directions. Color and grayscale map renderings
  were inspected.
- The structural verifier checks 13 acyclic claim records, source paths, and
  manuscript labels. It is a document-integrity check, not a mathematical test.
- Component and integration audits independently reconstruct the conditional
  mathematical implications at the frozen revisions recorded in their files.

## Detailed high-frequency research plan

The objective is to prove HIGH-PRESSURE for every original unforced R3
Schwartz-data trajectory, uniformly to any putative finite singular time.
A conditional consumer, a small-data theorem, a numerical trajectory, or
another statement of the same unknown finiteness does not complete this
objective. Phase I remains unstarted.

### Exact target and conventions

Write P3 = integral p u dot grad |u| and
D3 = integral (|u||grad u|^2 + |u||grad |u||^2). Fix a smooth real-even
low-pass multiplier S_J and Q_J = integral (p-S_J p) u dot grad |u|.
The target quantifier order is

```text
exists theta in [0,1), for every nu > 0, Schwartz solenoidal u0 and H > 0,
exists integer J and finite A >= 0, for every 0 < tau < min(H,Tstar):
  integral_0^tau Q_J <= theta nu integral_0^tau D3 + A.
```

The existential assertion is nontrivial. A proof cannot assume finiteness
of the unknown trajectory supremum to produce its witness. An explicit
formula in declared initial norms would be stronger; it is not silently
required by the existing statement. Every candidate will declare whether it
addresses this exact target or a stronger sufficient mechanism.

### Ordered research stages

1. **Audit the reduction.** Determine whether finite-horizon existential HF
   is equivalent to global strong continuation, and identify exactly what
   additional information an effective estimate would provide. Check signs,
   amplitude scaling, viscosity, pressure gauge, endpoint uniformity, and
   the cutoff quantifiers before pursuing a mechanism.
2. **Derive distinct mechanisms.** Investigate weighted pressure absorption,
   an explicit modified-energy or temporal normal-form identity, and a
   concentration/time-scale budget. Each lane must return an actual
   inequality, identity, or obstruction. A proposal that only names the
   desired cancellation is incomplete evidence.
3. **Falsify before extending.** Test instantaneous assertions on declared
   divergence-free fields, spatial and amplitude rescalings, and local
   solution segments. Test time-integrated claims on actual trajectories or
   prove a relevant implication; arbitrary snapshots cannot refute them.
   Numerical examples require an independent formula and refinement checks
   and remain numerical until an analytic certificate is supplied.
4. **Repair and escalate.** Opus workers handle source extraction,
   arithmetic, reproducible probes, and already specified implementation.
   A failed Opus task with a mathematical ambiguity goes to a Fable analysis
   lane. Distinct hard analytic questions go directly to Fable lanes. The
   controller reconstructs every failed bridge, seeks an exact repair or a
   different intermediate functional, and chooses the next lane from that
   evidence rather than repeating the same question. Record the failed
   inference, not a ban on an entire field. All lanes are Claude models;
   see `AGENTS.md`.
5. **Audit coherent candidate blocks.** Freeze exact commits, or a base
   commit plus complete patch digest including new files. An independent
   reviewer reconstructs the argument and external premises. Repair findings
   are applied by the controller; workers never promote their own results.
6. **Integrate a mathematical change.** Update the paper, logical graph, and
   this plan after a verified lemma, obstruction, or repaired route changes
   the frontier. Keep the private GitHub repositories current;
   run structural checks, local paper compilation, PDF inspection,
   and explicit-path commits. None of these replaces mathematical review.
7. **Check completion against the original target.** A complete paper proof
   must cover every admissible datum and all horizons, discharge HF rather
   than postulate it, and pass separate estimate, endpoint/source, and final
   integration audits. If the exact HF mechanism is disproved, repair or
   replace it while preserving the Millennium objective. Do not declare the
   goal achieved merely because the current wave ends.

### Current wave HF01

Frozen starting research commit: `1240e98d78f1745f089efb9c6c282db520e00363`.
Frozen starting paper archive: `95cbf22885bb374cf83b6f485db97ce292e623f8`.
The controller owns all authoritative changes. Worker files are evidence.

| Lane | Model and role | Information target | Evidence file |
| --- | --- | --- | --- |
| Quantifier and producer audit | Controller | Exact relation of existential HF to continuation; identify noncircular mechanisms | `research/evidence/hf01-controller.md` |
| Weighted cubic estimate | Sol | Derive usable pressure bound; attempt amplitude/geometry repair for large data | `research/evidence/hf01-weighted.md` |
| Temporal modified energy | Sol | Construct one actual boundary functional or symbol and expose its remainder | `research/evidence/hf01-normal-form.md` |
| Concentration budget | Sol | Compute spike persistence and dissipation costs with the frequency scale retained | `research/evidence/hf01-concentration.md` |
| Primary-source table | Luna | Exact pressure criteria and their unproved input requirements | `research/evidence/hf01-source-table.md` |
| Pressure-work probe | Luna | Reproducible nonzero Fourier snapshot; independent pressure identities | `research/evidence/hf01-snapshot.md` and `.py` |

The next integration selects a surviving mechanism from these results.
Unproved HF remains the first mathematical gap. Formalization remains
reserved for the user's separate Phase I kickoff.

### External opinions and prior-art audit

The user's supplied analyses are research leads; the controller decides which
claims survive source checking and mathematical review. A Type-I lane tests
the localized cubic identity, harmonic pressure, and boundary errors. Its
one-point hypotheses must lead to one-point conclusions; neither general
Type-I exclusion nor universal HF has been proved. Publication forecasts do
not determine the mathematical target.

A separate source audit compares established pressure and frequency criteria
with the exact signed, fixed-cutoff, finite-horizon HF statement. It also
checks the suggested recent preprints and public AI-assisted repositories.
Record exact hypotheses, source revisions, proof status, and inaccessible
material. Similar terminology is not theorem equivalence; failure to find a
match is not evidence of priority. No claim of being first is authorized by
the current literature search. Clay's unsolved designation does not adjudicate
the correctness of any individual manuscript.

Luna handles source retrieval and exact extraction; Sol resolves mathematical
ambiguities. The controller integrates only verified comparisons that affect
the proof strategy or manuscript attribution. External repository rules are
comparison material, not instructions for this private programme. The
arbitrary-data Millennium objective and Phase I boundary remain unchanged.

### Reviewed mathematical checkpoint HF02

Commit `44786da` preserves the exact frozen candidates and their independent
audits. The subsequent corrections qualify the failed Type-I suffix and fix
profile notation; the original review inputs remain reproducible.

- The controller's source-amplitude split removes the artificial uncontrolled
  L4-time remainder. Its remaining uniform amplitude-tail condition already
  entails critical L3 control and is unproved.
- The corrected heat functional and its energy-controlled transport term
  pass review. The short-heat defect is equivalent to HF modulo explicit
  energy remainders; it supplies no missing absorption.
- At the current ordinary existential quantifiers, HF is equivalent to
  global continuation of the selected strong branch. This is not a method
  for proving either assertion. Strict absorption gives dissipation control
  forward, but does not make this existential statement logically stronger.
- The compactly supported R3 snapshot construction passes independent audit:
  pressure work has both signs. This excludes a universal pressure sign
  argument and completes the earlier conditional snapshot falsifier; it
  neither constructs PDE blowup nor refutes signed spacetime HF.
- The Type-I localization audit rejects the claimed regularity suffix:
  incoming cubic mass is not small, and no complete contraction was derived.
  A backward caloric/time-ramp repair is being examined as a separate
  mechanism test. Paper and graph integration of reviewed diagnostics is
  pending; no gap node is promoted by these findings.

### Current checkpoint HF03 and next trajectory test

The manuscript now contains the independently audited existential-equivalence
paragraph at source commit `d84950b`; archive `42742bf` includes the regenerated
map. At that checkpoint, Overleaf and GitHub were synchronized (Overleaf
has since been removed). Local and Overleaf manuscripts compiled to seven pages; the map remains four pages. Rendered
changes and 50 manuscript / 43 map internal links were checked. These are
document checks, separate from `hf03-review-paper.md`.

The fixed-energy snapshot obstruction in `hf03-fixed-energy-obstruction.md`
passes `hf03-review-fixed-energy.md`: for every exact positive kinetic energy,
fixed viscosity and cutoff, and finite nonnegative dissipation coefficient,
the instantaneous high-pressure excess has infinite supremum over smooth
compactly supported solenoidal fields. The proof controls the separated
reservoir's nonlocal pressure interactions. It excludes instantaneous
energy-only absorption, not the datum-dependent spacetime target.

The controller found that the attempted Type-I coefficient-one obstruction
was overbroad: a backward heat cutoff can reduce its incoming weighted cubic
mass by (r/R)^3. The repaired caloric ledger is under independent audit;
absolute transport bounds near the final scale remain order one. An upper
bound of that size is not a proof that signed cancellation is impossible.

Next, test an actual-trajectory energy-only spacetime obstruction using a
uniform short-time Sobolev bound at viscosity nu/a, followed by amplitude and
space-time scaling at fixed original kinetic energy. This would test a
strictly stronger uniform energy-only proposal; it must not be confused with
HF, whose remainder and cutoff may depend on the whole datum. The original
universal HF target remains open and Phase I remains unstarted.

### Audited HF04 consequences

The trajectory test succeeds after the interior-endpoint repair in
`hf04-review-spacetime.md`: actual smooth solution segments of fixed initial
kinetic energy have unbounded integrated high-pressure excess at a fixed
cutoff. Initial L3 norms diverge across the constructed sequence. Thus this
refutes an energy-only uniform spacetime remainder, but supplies neither a
counterexample to HF nor information about one fixed solution's endpoint.

The controller's full-heat inverse calculation passes
`hf04-review-coercivity.md`. Starting the heat inverse at zero gives a finite
functional on each Schwartz snapshot, but the direct additive modified
energy is unbounded below even at fixed kinetic energy. This prevents that
particular correction from controlling the critical norm through an
energy-only coercivity estimate.

The caloric audit preserves the incoming (r/R)^3 gain and corrects an
overclaim: uniform upper bounds for signed boundary flux do not establish
nonzero flux or rule out cancellation. The audited original and repairs
are preserved separately.

Next repair: test nonlinear saturation of the full-heat functional. The
controller's heat-flow calculation suggests |B(u)| <= C nu^-1 ||u||_3^4,
so saturation can restore cubic size. It must also preserve the required
pressure cancellation and control its new derivative terms. This is a
concrete mechanism test; the criterion for completion remains universal HF
or another independently verified arbitrary-data continuation producer.

### Saturation result and geometric test

The saturation calculation and its audit are in
`hf04-saturated-normal-form.md` and `hf04-review-saturation.md`; commit
`3d5642a` preserves the frozen candidate. Saturation restores cubic coercivity,
but leaves a pressure coefficient bounded below by 1/2 for the stated small
parameter choice. Coefficientwise exact pressure cancellation on the ambient
scalar domain forces F=f(X-B). The explicit fixed-energy family has X-B=0
and X tending to infinity, so that scalar cannot control the critical norm.
This is a restriction on a precisely specified class of functionals, not on
all cancellation possible along actual PDE trajectories.

A distinct geometric test writes full pressure work as a Lamb-vector
commutator and keeps the exact low-output correction after frequency
cutoff. Its candidate is under independent audit. The controller reduced
its proposed commutator norm bound to ordinary pressure Holder estimates:
the formula exposes speed increments but currently proves no stronger
bound. The remaining critical integral of speed-gradient depletion times
squared enstrophy is unproved. Further work must obtain an actual sharper
signed estimate; another equivalent identity alone will not discharge HF.

### Geometric identity audit and radial dynamics

`hf05-review-lamb.md` checks the Lamb-vector identity, the high-cutoff
correction, and its energy remainder. The frozen input is preserved at
`652b672`. Its wording corrections remove unsupported novelty language.
The speed-gradient estimate is classical Holder/Sobolev bookkeeping and
does not improve the available arbitrary-data bound.

The next test retains radial dissipation A=integral |u| |grad |u||^2 in
the pressure estimate |P3| <= C ||u||3 A, while total cubic dissipation is
2A plus angular dissipation. A Sol calculation is deriving the regularized
evolution of A to test whether the equation preserves or generates angular
dominance. The controller supplied an independent periodic-shear oracle:
constant initial speed need not remain spatially constant under diffusion
when its direction varies nonuniformly. This is a diagnostic for a proposed
mechanism, not a transfer of a torus result to the R3 terminal claim.

### Radial audit and whole-space transfer test

The radial audit in `hf05-review-radial.md` preserves all fixed-epsilon
identities and the periodic shear expansion. It rejects the inference that
positivity of the zero-set defect justifies passing every signed evolution
term to epsilon=0. The repaired note keeps those limits conditional; the
frozen candidate remains reproducible at `ef07bda`.

The controller has specified a whole-space version of the dynamic test:
localize a rapidly oscillating, constant-speed periodic shear with a curl
potential, evolve for its parabolic time, and compare the nonlinear solution
with its heat evolution. The required bounds are uniform initial L-infinity
control, global L2 errors of order 1/k, and gradient errors of order one.
These would test whether a vanishing initial speed-gradient ratio can become
positive on actual R3 trajectories. Envelope zeros and nonlocal pressure
must be included in the proof. This tests propagation of a proposed geometric
depletion mechanism, not existence of singularities or failure of HF.

### Whole-space transfer result and pressure geometry

The construction in `hf06-r3-speed-transfer.md` passes the repair audit
`hf06-review-speed-transfer.md`: use the full heat-evolved profile in the
speed-gradient comparison, rather than its normalized direction. The
localized curl fields have speed-gradient ratio tending to zero initially
and a positive limiting ratio at their parabolic times. Global L2/H1 errors
and envelope zeros are controlled. Initial L3 norms stay bounded, and the
solutions have a common regular interval. This rejects automatic propagation
of that particular depletion ratio, not regularity or HF.

The controller notes that the leading shear has zero pressure. Radial
variation is therefore too coarse a diagnostic to identify dangerous
pressure flux by itself. A separate calculation is testing the exact Fourier
pressure symbol: comparable near-parallel modes have an angular null factor,
whereas nearly opposite modes can lose that factor in pressure when their
output is small. The pressure gradient retains an output-frequency factor.
Its shell estimates and any claimed summation gain are under independent
audit. No angular-coherence hypothesis is assumed for arbitrary solutions.

### Angular audit and square-function energy

The angular audit in `hf06-review-angular.md` checks the pressure coefficient,
localized multipliers, and shell upper bounds, while rejecting an unsupported
sharpness claim. The controller supplies the missing *symbol-level* example
in `hf07-controller-symbol.md`, independently checked in
`hf07-review-symbol.md`: nearly opposite modes attain the output-frequency
gradient bound and preclude an additional uniform positive power of the
output/input ratio. This does not give a lower bound for the signed cubic
pressure pairing or its time integral.

The current distinct repair uses cubic Littlewood--Paley square-function
energy, rather than a scalar function of the earlier heat inverse. The
candidate `hf07-square-energy.md` is under audit for its finite-band
regularized identity, positive diffusion, frequency-boundary terms, limits,
and low-high pressure/transport grouping. Any linearized strain model must
be distinguished from the actual nonlinear cubic functional. No unspecified
strain or Carleson condition is accepted as an arbitrary-data producer.


### HF08–HF09: complete square-energy calculation

The square-energy audit's first invalid bridge was promotion of a frozen
unweighted strain term to the full nonlinear second variation. The repaired
`hf08-square-second-variation.md` includes low-mode feedback, evolution of the
weight, weighted Leray terms and finite-band defects, with the domain repair
from `hf08-review-second-variation.md`. The same review checks the controller's
exact periodic example: frozen strain is strictly positive while the full
constant-weight coefficient vanishes. The original failed candidate remains
recoverable at `f0196f75b2c8dd92e2ea32199baf608753e23aa5`.

The stronger variable-weight diagnostic in `hf09-bounded-carrier.md` passes
`hf09-review-bounded-carrier.md`. One fixed smooth tight frame and bounded-L2
periodic high carriers give a complete coefficient tending to a nonzero
constant with either sign; the retained Leray pressure correction is O(1/N).
This rules out a uniform positive power of frequency-separation gain for
that exact instantaneous coefficient. It does not refute viscous absorption,
whole-space HF, or any signed time-integrated mechanism. The earlier
unnormalized variable-weight example is superseded scratch and is not a new
load-bearing claim.

`hf09-square-limit.md` passes `hf09-review-square-limit.md`, conditional on its
explicit Littlewood–Paley L3 analysis-operator premise. Strong Hilbert-array
Sobolev convergence justifies the all-band and zero-regularization aggregate
identity on each compact classical interval. No preservation of Schwartz
spatial decay or separate paraproduct convergence is assumed. Its domination
uses trajectory Sobolev bounds on that compact interval and supplies no
input-only endpoint estimate.

Next distinct action: investigate the signed spacetime producer for balanced
high shells in the exact aggregate identity. Do not treat the periodic
instantaneous obstruction as a reason to abandon the whole square-energy
route, or spend a new wave merely localizing it to R3: fixed-background
high-carrier diffusion grows quadratically with frequency, so the diagnosed
order-one coefficient alone is no obstruction to absorption. A useful next
candidate must construct a coercive temporal shell correction or a derived
budget for the complete balanced-shell remainder on actual trajectories,
with every term displayed. The earlier scalar full-heat correction and
saturation obstructions remain constraints on those specific constructions.
HIGH-PRESSURE and the terminal claim remain open; neither Lean phase starts.


### HF10: pressure–speed cancellation and coercivity failure

A different critical cubic correction, B(u)=integral p|u|, has an exact
coefficient-one cancellation of the original pressure work in the integrated
F+B balance. The regularized formula and compact-interval limit in
`hf10-pressure-speed-evolution.md` pass the scoped review
`hf10-review-pressure-speed-evolution.md`. Its repair avoids claiming a
standalone two-sided derivative DB at velocity zeros; the surviving identity
includes every displayed nonlinear and viscous residual.

The coefficient-one functional is not coercive. The controller's planar swirl
oracle has F+B=-pi/6. The smooth compact R3 transfer in
`hf10-pressure-speed-coercivity.md` passes
`hf10-review-pressure-speed-coercivity.md` after the sign-of-kappa repair in
the optional planar bound. Anisotropic Riesz convergence controls the
nonlocal pressure during the long-cylinder lift. This excludes positive
critical-norm control by F+B alone, not the original HF target. Frozen
candidates and reviews are preserved at `f546d25`.

The bounded primary-source check `hf10-pressure-speed-sources.md` identifies
existing conditional Bernoulli-pressure regularity work and the standard Lq
pressure-work calculation. It supplies no arbitrary-data producer or novelty
claim for this correction.

Next repair: add integral (-p)_+^(3/2) to F+B. Pointwise Young inequality
suggests this restores critical cubic coercivity while retaining the exact
coefficient-one B term. The complete regularized pressure-entropy evolution
is being derived, including its pressure-source term, cross gradients and
zero-level behavior. No sign for its full heat part or endpoint bound may be
inferred from pointwise positivity of the functional. HIGH-PRESSURE remains
the first unsupported terminal bridge, and Phase I remains unstarted.

### HF11: coercivity survives, heat monotonicity fails

The pressure-entropy functional K = F + integral p|u| + integral p_-^(3/2)
obeys ||u||_3^3/6 <= K <= C||u||_3^3. Its fixed-regularizer evolution is
valid on compact classical Sobolev intervals after the applicability repair
in `hf11-review-pressure-entropy.md`. The candidate and audit were frozen
at `f3e7605`; the Sobolev repair was committed at `4338abe`.

The controller's remote-pressure construction now rules out universal heat
monotonicity of the original, unregularized K. A compact azimuthal field has
negative pressure in a ball where its velocity vanishes. Adding a small
solenoidal oscillatory packet there changes p|u| at first order in amplitude
and the pressure entropy only at second order. A short exact heat step
attenuates the packet and increases K. The proof uses L3 continuity and an
explicit heat residual estimate, avoiding derivatives at velocity zeros.
See `hf11-heat-finite-step.md` and its independent review
`hf11-review-heat-finite-step.md`, frozen at `3a5844d`; the only review repair
makes the viscosity quantifier explicit. This is a linear-heat obstruction,
not a Navier--Stokes trajectory counterexample or a failure of HF.

Next task: determine which pressure-only additions share this obstruction,
then change the pressure--speed coupling near zero velocity and identify
exactly which pressure-work cancellation is lost. A replacement must retain
critical-norm control and account for its entire evolution; positivity of
the functional alone is insufficient. No new terminal dependency is proved.


### HF12: pressure-only and fixed-scale repairs are insufficient

The centered-Holder pressure-only obstruction in `hf12-cusp-repair.md`
passes `hf12-review-cusp-repair.md` after replacing an unjustified moving-
argument continuity step by a direct estimate relative to the background
pressure. Every pressure-only correction with exponent greater than 1/2 in
that estimate changes too slowly to remove the linear negative-pressure
speed term. The general coupling condition is explicitly restricted to
uniform expansion hypotheses. The complete fixed-scale Euler identity now
retains the restored pressure work and every remaining pressure term.

For every fixed positive smoothing scale, the repaired functional can still
increase under a finite linear heat step. `hf12-fixed-scale-obstruction.md`
passes its independent review: choose the remote background amplitude,
then the packet amplitude, then its frequency. All nonlocal pressure and
entropy terms are included.

The homogeneous alternative in `hf12-homogeneous-coupling.md` has uniform
cubic coercivity and reviewed scalar derivatives. One Euler defect has a
square-root parameter coefficient multiplying an uncontrolled critical
integral; the other Euler terms are not small. The reviewed comparison with
HF11 transfers the heat obstruction to every sufficiently small parameter.
Original candidates and reviews are frozen at `7afbff8`; no HF producer is
obtained, and no Navier--Stokes trajectory counterexample is asserted.

Next test: inspect the far-field Riesz pressure-entropy contribution for a
compact azimuthal background. A negative directional quadratic coefficient
in a negative-pressure region would test the remaining parameter regime.
The angular sign, Riesz asymptotic, and conditional packet expansion are
separate obligations. Numerical angular coefficients can nominate a sign,
but require an analytic certificate before integration. HIGH-PRESSURE and
the Millennium claim remain open, and Phase I remains unstarted.


### HF13: full-pressure homogeneous heat monotonicity is excluded

The far-field sign in `hf13-entropy-far-field.md` passes its independent
review. An elementary Legendre/Parseval bound certifies the angular sign;
principal-value rescaling transfers it to the actual compact swirl pressure.
The numerical angular calculation only nominated this sign and is not part
of the proof. The entropy contribution decays like distance to the power
minus 3/2, while the remaining compact pressure derivative has a uniform
parameter-independent distance-to-the-power-minus-3 bound.

That comparison supplies the premise of the independently reviewed
`hf13-conditional-packet.md` on one common far ball. The controller's
`hf13-homogeneous-heat-obstruction.md` integrates the two audited inputs,
frozen at `59ccce3`: for every positive homogeneous coupling parameter,
some compact smooth solenoidal datum has a finite linear heat step on which
the functional increases. The datum and time may depend on the parameter.
Cubic coercivity survives; universal heat monotonicity for this entire
specific family does not. No input-controlled spacetime remainder is ruled
out, and no Navier--Stokes counterexample is asserted.

Next task is the original fixed high-output split. First quantify the
energy-controlled boundary difference between full-pressure and high-output
corrections. Then derive the complete high-output evolution using the full
Navier--Stokes pressure gradient in the velocity equation. The far-field
obstruction above does not itself survive removal of low outputs; do not
promote it to an HF obstruction. HIGH-PRESSURE remains the missing producer.


### HF14: high-output boundary control and a coherent remaining estimate

`hf14-high-output-boundary.md` passes its independent review: the difference
between the full-pressure and high-output functionals is bounded by an
arbitrarily small critical-norm term plus an energy-controlled boundary
remainder, uniformly in the coupling parameter. The actual low-pass Riesz
kernel has an algebraic tail; the proof does not assume it is Schwartz.

The scaling argument in `hf14-fixed-cutoff-heat-obstruction.md` also passes
review. Every fixed cutoff admits some datum with a heat increase of the
high-output functional. This has the order "for every cutoff, some datum";
it does not refute choosing the cutoff from the datum and does not refute HF.

The initial evolution candidate required repairs: unspecified scalar growth
was insufficient for its derivatives, it mixed regularized and unregularized
terms, and its proposed closure discarded the useful dissipation. The
reviewed construction in `hf14-regularization.md` supplies an actual radial
four-variable mollifier, rigorous fixed-regularizer Sobolev evolution, and
convergence of functional values. The revised evolution note keeps one
regularizer throughout and retains nonnegative cubic dissipation on the
left. Its remaining requirement is a uniform input-only bound for the
complete aggregate remainder. Functional-value convergence suffices for
that conditional closure; no differentiated limit is asserted. Frozen
inputs and reviews are at `6697f29` and `c63ce81`.

Next task: estimate the two residual appearances of the low-pressure
gradient, including their fixed-regularizer versions. The controller's
energy estimates use low-kernel gradient norms and time Holder bounds.
The resulting replacement velocity field is not divergence-free; do not
reuse Leray cancellations after that split. The complete high-output
aggregate remains unbounded, and neither formalization phase starts.


### HF15: the remaining low-pressure Euler gradients are energy-controlled

The instantaneous estimates in `hf15-low-pressure-gradient.md` pass review
after adding H1 and distinguishing the chosen bounded zero-set vector from
a derivative. The frozen candidate and review are at `156b2dc`.

`hf15-regularized-low-pressure.md` passes its independent review without a
scope repair. The pressure derivative is 1-Lipschitz in velocity, and centered
convolution gives a pressure derivative bound uniform in the regularizer.
Low-kernel gradient bounds in L1, L2, L6, and L-infinity then control both
low-pressure Euler terms by finite energy-level remainders on every finite
horizon. This is the actual fixed-regularizer identity, not an identification
of derivatives at velocity zeros.

After splitting V = W - grad(pL), where W = -(u dot grad)u - grad(pH), the
coherent balance is J_eta' + nu D_eta = E_eta^H + H_eta^rem - A_eta - B_eta.
The time integrals of |A_eta| and |B_eta| have input-only bounds, uniform in
eta. D_eta is nonnegative. W has divergence Delta(pL), so no solenoidal
cancellation is available for W. The complete remaining high-output sum
E_eta^H + H_eta^rem still needs a uniform absorption bound; none is proved.

Next task: rewrite the pressure source using the material derivative and
inspect its low-velocity transport commutator. Any Calderon commutator bound
must have verified hypotheses and cutoff constants before it is imported.
An input-controlled Gronwall term would remove that contribution, but would
not bound the remaining critical terms. HIGH-PRESSURE remains open.


### HF16–HF17: final paper checkpoint at the user's request

The user requested conclusion and signed pushes of the current work; no new
research wave is running. Phase I and Phase II remain unstarted.

HF16 removes the low-velocity transport commutator with Taylor's verified
order-one commutator theorem and explicit cutoff dilation. The input
coefficient is C_k(2^{J+3L/2}+2^{5L/2})E0^{1/2}. The stronger derivative-only
premise is unnecessary. Gronwall is justified only after the functional-value
limit, conditional on an unproved bound for the remaining high-output sum.
The candidate inputs and reviews are preserved at `174a79c` before repair.

HF17 changes the functional to the cubic distance from u to the closed L3
gradient subspace. Its unique minimizing representative w=u+q obeys
Q=||w||_3^3/3, Q comparable to ||u||_3^3 for solenoidal u, and
DQ(u)h=integral |w|w dot h. The independent functional audit passes:
pressure gradients are annihilated and linear heat cannot increase Q.
The evolution note uses a volume-preserving flow and gradient pullback;
it does not differentiate the L3 minimizer. Its independent review records
the exact scope of the strain rewrite and low-frequency bound.

The alternative missing producer is signed high-strain control. Define
D_Q=-DQ(u)[Delta u]>=0 and
K_L=-integral q dot ((|w|w dot grad)(u-S_Lu)). Then
Q'+nu D_Q=K_L+K_low, with |K_low|<=M_input Q.
A sufficient unproved estimate is integral K_L <= theta nu integral D_Q+A
uniformly for tau<min(H,Tstar), with theta<=1 and input-only finite A.
Integration and Gronwall would bound Q and hence L3. No such estimate is
proved, and no novelty claim is made for the quotient construction.

HIGH-PRESSURE remains the selected graph gap. HIGH-STRAIN is an alternative
route to the same missing critical bound, not an additional required lemma.
The paper remains conditional; no Millennium solution is claimed.

Checkpoint verification: the final manuscript builds to eight pages and the
map to four, with 52 and 43 resolved internal links respectively. No undefined
references or overfull boxes were reported; rendered argument and map pages
were inspected. The 13-node structural verifier passes. These are document
checks; the separate HF16/HF17 reviews supply the mathematical audit scope.


### HF18: nonlinear Hodge regularity of the quotient minimizer (Track B)

Two distinct lanes on the HF17 route, frozen at `cee98a7`. The regularity
note `hf18-hodge-regularity.md` passes `hf18-review-hodge-regularity.md`
after wording corrections S1–S3: at every fixed time of a classical `H^m`
solution, `m >= 4`, the minimizer satisfies `V = |w|^{1/2} w in H^1(R3)` and
`A = |w| w in W^{1,3/2}(R3)`, obtained by a global Bojarski–Iwaniec
difference-quotient argument against the whole closed gradient space; the
HF17 heat generator equals the coercive weighted cubic dissipation,
`D_Q(u) = int(|grad V|^2 - |grad|V||^2/9)`, with `D_Q >= c ||u||_9^3`; the
transport term has derivative-free forms and the scaling-sharp bound
`|K| <= C_* Q^{1/3} D_3(w)`, so `Q` is a Lyapunov functional under critical
smallness (recovering Kato's small-`L^3` theorem with ESS) and not
otherwise. The cited `C^{1,alpha}` p-Laplace theorems do not apply: the
ellipticity degenerates on `{u + grad phi = 0}` and the shift is not
removable. No `W^{1,1}_loc` regularity of `w`, no time-integrated absorption,
no HIGH-STRAIN or HIGH-PRESSURE result, and no novelty claim.

The divergence–speed-link note `hf18-divergence-speed-link.md` received a
REPAIR verdict (Riesz sign convention and weighted-inequality scope); the
repaired version passes `hf18-review-divergence-speed-link-r2.md` after the
controller applied its scope corrections (Lemma A identifying the weak
gradient under `w in W^{1,1}_loc`, Lemma B lower bounds for the witness
family, the second hypothesis `sigma in L^{3/2}` in both summaries, three
constant and label slips). Unconditionally: `div w = -ŵ·grad|w|` a.e. on
`{w != 0}` in the approximate-gradient sense, `int |w| sigma^2 <= D_3(w)/2`,
`int |q|^2 |w|^3 <= C Q^{2/3} D_3(w)`, and the transport term is the work of
a mixed pressure, `K_L = int q·grad Pi_L`. The classification of weighted
inequalities between the gradient part and the dissipation is recorded with
proofs or scaling counterexamples; the weighted Calderón–Zygmund inequality
and the `L^2` bound for the nonlinear projection remain open. Next distinct actions from the
audit: test whether `K` vanishes identically on `{u : div(|u|u) = 0}`, and
seek a cancellation inside `K = -int q·grad Pi_{u,A}` rather than a size
bound, since no monomial in `Q` and `D_3` can close by scaling.


### HF19: temporal normal forms, second-order behaviour, difference functional

The user stopped this wave before any audit ran, so **all three candidate
notes are UNAUDITED** and nothing in them is promoted; they are recorded as
research leads only. The fourth lane (regularity of the shifted 3-Laplace
minimizer) never wrote its note; its reviewer certified the absence and
that certificate is kept as `hf19-review-shifted-hodge-regularity.md`.

- `hf19-temporal-normal-form.md` (DISCOVER, negative). Claims that a temporal
  normal form for the transport term is exactly equivalent to a coercive
  critical Lyapunov functional, so the content of any such form lies wholly
  in the explicit corrector; computes three explicit classes and reports each
  failing, in one case only under a hidden smallness condition. Reports the
  route-level conclusion that temporal normal forms are exhausted on the
  quotient route as they were on the pressure route (HF01, HF04, HF10-HF13).
- `hf19-second-order-falsifier.md` (FALSIFY, target survived). Reports an
  exact first-order expansion of the transport term at the nonlinear-Hodge
  class that never differentiates the minimizer, and finds the favourable
  sign on an explicit swirl class, i.e. the intended refutation of a
  Lyapunov mechanism did not occur there. Its open sub-question is a
  minimizer-free weighted-potential inequality.
- `hf19-difference-functional.md` (DISCOVER, two claimed obstructions).
  Reports an exact evolution for the difference of the two cubic functionals
  in terms of the Hodge defect, and retires the difference route as a
  producer because that difference is not coercive and its balance carries
  the same critical absorption as the two audited balances.

None of this changes the graph. Before any of it is used, each note needs
the independent audit the wave did not run, and the numerics in them are
bounded evidence at finite resolution, not proof. HIGH-PRESSURE and
HIGH-STRAIN remain the open producers and NS-R3 remains open.


### HF20: a local harmonic-strain sign test (AUDITED: REPAIR, applied)

A typeset candidate arrived on the work capture surface rather than as a
repository note, written against research `30d715d` and paper `39ccb66`. It
is transcribed into `research/evidence/hf20-harmonic-strain-test.md`; the
PDF is frozen by SHA-256
`4be9a53b244ba385e7b1e18bf02bee9b10db44a4329438612742ac32b7e15009` at
`<work vault, not in this repository>/navier-hf20-candidate-proof.pdf` and is not committed,
because generated PDFs stay out of the repository.

It claims an analytic two-sign certificate for the transport term of the
cubic gradient quotient: an explicit swirl `U` on the nonlinear-Hodge class
and a compact solenoidal `h` that coincides with a harmonic gradient near
the swirl give `K(U + eps h) = -eps ||U||_3^3 + O(|eps|^{3/2})`, the gain
coming from a competitor gradient with disjoint exterior support, never
from a derivative of the minimizer. It then transfers this to actual
classical trajectories: for every viscosity and every prescribed squared L2
norm, some compact smooth solenoidal datum makes the quotient strictly
increase at time zero, and the fixed-energy supremum of
`K - beta nu D_Q` is infinite. Consequently no monotone function of the
quotient decreases along all trajectories, and no energy-only instantaneous
absorption bound exists.

Scope, as the candidate itself states: this refutes universal monotonicity
and one instantaneous energy-only estimate. It is not a singular solution,
gives no unbounded critical norm on a fixed trajectory, and does not touch
the datum-dependent spacetime hypotheses `hyp:highstrain` or
`hyp:highpressure`, which remain the open producers. Structurally it is the
quotient-route analogue of the audited HF03 and HF04 fixed-energy
obstructions on the pressure route.

**Audited and integrated, 2026-09-06.** `hf20-review-harmonic-strain-test.md`
returns REPAIR with no invalid mathematics; the sole defect is that
Theorem 1.1 was displayed one-sidedly and so did not literally entail the
two-sign conclusion its own proof gives. The controller applied the audit's
repair (two-sided display, same constant, proof unchanged) and its citation
action replacing the regularity sketch by `prop:localtheory`(iii),(iv) and
`lem:upgrade`. The auditor independently verified every remaining step,
attempted nine refutations including direct numerical checks of each
pointwise input, all of which failed, and confirmed consistency with the
audited HF18-A bound, which forces any increase to live at supercritical
quotient values, exactly where this construction puts it.

Integrated: the manuscript gains `rem:no-monotone` in `sec:quotient`
recording the exclusion with its limits, and the graph's HIGH-STRAIN review
records two further excluded mechanism classes. No node is promoted or
demoted and no lemma changes; the manuscript never asserted monotonicity, so
nothing is corrected, only narrowed.

## Ordered next actions

Rewritten 2026-09-06 after the HF24, HF25 and HF26 audit waves. The previous
list had duplicate numbering and described completed waves as running.

1. ~~HF27 audits~~ **done, 2026-09-06.** All three scopes returned; the
   mathematics is correct throughout and the failures are of significance and
   prior art. **Decision recorded: do not import.** See the HF27 section for the
   reasons and for the corrected prior-art map, which is the wave's lasting
   value.
2. ~~Blocked on an external dependency~~ **resolved 2026-09-06 and audited
   CONFIRMED WITH CORRECTION; it was not an access problem.** The lane recorded the 2024 metric-projection theorem's
   applicability as undetermined because it read the preprint through a
   text-extraction proxy, which is the wrong instrument for a mathematical
   definition. Read with a PDF reader, the definition and proof are plain, and
   the answer is decisive: the theorem **does not** subsume the linearization.
   Its hypothesis orders the convexity exponent below the smoothness exponent,
   whereas our space has convexity of power type three and smoothness of power
   type two, so the ordering fails and the proof's convergence factor diverges
   rather than vanishing. As stated in the preprint the hypothesis class is in
   fact empty, since Nordlander's theorem forces every Banach space to the
   opposite ordering, so the theorem is vacuous there; the preprint also
   attributes the condition to a renorming theorem that gives the opposite
   ordering. The programme still may not claim novelty for the linearization —
   every other ground in the prior-art lane's findings stands untouched, and
   those are the ones that matter — but this paper is not the reason.    The audit
   (`hf26-review-li-resolution.md`) verified the quotation as exact and
   strengthened the first ground — every admissible exponent pair fails, not
   only the sharp one, and in fact the proof's closing step is unavailable in
   *every* Banach space, so our space is merely a strict case. It corrected the
   second: my appeal to Nordlander's theorem was stated for every Banach space
   when that theorem needs dimension at least two, and the emptiness has a
   shorter proof needing no dimension hypothesis, since the modulus of convexity
   is at most one while the condition demands more than two at its endpoint. It
   also caught my framing: the printed text is still wanted before the
   comparison is written down as settled, and only the *preprint* is refuted.
   Against that, the audit supplied a branch-independent reason — Li's
   differentiability is a one-sided limit with no representation of the
   derivative, whereas the candidate's is two-sided and identifies its limit, so
   the theorem could not subsume it however the published version reads. All
   seven corrections are applied.
3. **Preconditions for any HF26 import**, all from its four audits: re-base the
   departure section on the audit's two-line argument so it does not inherit
   the linearization's risk; resolve the notation collision with HF22-B, which
   uses the same symbol for a different space; cite Nečas, Růžička and Šverák
   and Tsai for the comparison curve; cite the metric-projection and convex
   sensitivity line; and drop the "except possibly one amplitude" hedge, which
   the audit removed. Nothing from HF26 is in the manuscript.
4. **Track B continues** on what the excluded classes leave. The exclusions now
   are: size bounds in `Q` and `D_3` by scaling; temporal normal forms with
   correctors in the computed classes; the difference functional as a producer;
   universal monotonicity of the quotient; instantaneous energy-only absorption;
   fixed-cutoff energy-only spacetime remainders; and, from HF26, derivation of
   the absolute target from instantaneous structure with energy and any scalar
   modulus or crossing information under a bounded critical norm — the last
   leaving the signed route at the endpoint parameter untouched. What remains
   open is a genuine cancellation inside the transport term, the time-integrated
   sign structure along trajectories crossing the nonlinear-Hodge class, and the
   weighted Calderón–Zygmund and `L^2`-projection questions of HF18-B.
5. **The one hypothesis outside the equivalence class.** Every producer the
   programme has generated is equivalent to global continuation at the
   quantifiers except the HF24 corridor hypothesis, which by Proposition R1 is
   strictly weaker and whose whole content is the exclusion of a blow-up staying
   above the upper corridor wall on a final interval. That asymmetry is the most
   promising structural fact currently on the table. **Wave HF29 is now running
   on it**, as an adversarial pair on the question the HF24 audit named as the
   falsifiable form. By Proposition R1 the corridor hypothesis fails only if a
   finite-time singularity re-enters the corridor band at times accumulating at
   the singular time — it cannot stay *below* the band, since that forces the
   quotient to be nonincreasing and hence regularity. So the whole content of
   the hypothesis is the exclusion of oscillation across a band whose position
   is fixed by the viscosity and the free parameter. One lane attempts the proof
   directly; the other attacks it, with the discretely self-similar mechanism as
   its natural candidate, since the distance is scale-invariant and a
   log-periodic profile crossing the band would re-enter it infinitely often.
   The second lane is also asked to settle a question the record has left
   ambiguous: whether the hypothesis is meant for one, for some, or for all
   values of the free parameter, and whether the lane and its audit agree.
6. **Standing check for every incoming continuation, instituted 2026-09-06
   after the same prior-art defect recurred three times.** Before any wave is
   audited, grep the source for the self-similar literature's terms and authors
   whenever it contains a dilation family of the form
   `lambda(t) = (1 - t/T)^(-1/2)`, a profile residual, or a critical time tuned
   to an energy identity. Three continuations have now reproduced the Leray
   profile equation without citing it; the requirement was recorded twice as a
   per-wave repair and never as a check, which is why it recurred.

7. **Formalization stays deferred** until the full paper route is proved and
   audited, per the user's re-sequencing of 2026-09-05. `../navier-formal` is
   not to be extended until this plan reopens it.

### HF21: shifted-Hodge regularity and the crossing sign structure (AUDITED)

Two lanes, both delivered 2026-09-06, **both audited 2026-09-06**; the audit
outcomes and applied repairs are recorded below.

`hf21-shifted-hodge-regularity.md` delivers the lane HF19 never wrote and
reshapes the (H1) regularity question rather than settling it. It reports:
the curl of the minimizing representative equals the curl of the velocity in
the distributional sense, so the skew part of its gradient is as smooth as
the datum and (H1) is entirely a question about neighbourhoods of the zero
set; a Calderon-Zygmund equivalence making the minimizer locally Sobolev
exactly when the distribution `div w` is locally `L^p` for one `p > 1`,
which collapses the two hypotheses (H1) and (H2) of HF18-B into the single
scalar statement `div w in L^{3/2}`; a rigidity theorem excluding zeros with
nonvanishing derivative, which vetoes the mechanism every construction in
the programme has used and which the note verifies on the HF18-B witness
family by explicit computation; a circulation lower bound, the first
quantitative lower bound on the representative in the programme; and the
statement that Uhlenbeck's theorem is inapplicable while its mechanism still
yields a local Caccioppoli inequality from which Gehring provably cannot be
started. The lane records its own scope ceiling: even granted in full, (H1)
supplies no time-integrated absorption and would not close the gap.

`hf21-crossing-sign-structure.md` answers the wave's strategic question
affirmatively but with an exact obstruction. It reports an exact spacetime
identity for the integrated transport term in which two of the four
right-hand terms are signed, the sign structure the pointwise term lacks,
while the remainder is precisely the pressure-route flux; a refinement of the
audited size bound with the distance to the nonlinear-Hodge class as an
explicit factor; an input-only spacetime bound for that distance; and a
crossing theorem stating that the quotient can increase only on a set of
times whose measure is bounded by input data. It also reports a route-level
dictionary in which signed pressure absorption implies the quotient gap with
an explicit non-circular constant, so the high-strain route is not harder
than the high-pressure route, and a simplification removing the Gronwall
term and the frequency cutoff from the high-strain hypothesis. Two
obstructions are recorded against upgrading the crossing bound to
absorption, one of them a circularity that would assume the Serrin
conclusion the gap must produce.

Both lanes state that the first gap is unchanged and not closed.

**Audited 2026-09-06, both REPAIR, integration done.** The shifted-Hodge
audit found a genuine proof gap: the rigidity theorem's realized directions
range over the sphere intersected with the range of the derivative, which is
open only at full rank, so the argument failed exactly at the rank-two case
the witness family needs. The auditor supplied a rank-stratified replacement
lemma, verified it numerically over random matrices of each rank, and the
theorem and both corollaries survive with the corrected proof; it also
confirmed against the primary source that the object here is the canonical
primitive of Stern's lemma, for which no regularity is stated there, and
that the smoothness credited to Uhlenbeck attaches to additionally closed
forms. The crossing audit found the note's exponent claim logically
inverted, since a bound with exponent above one would force the nonlinear
projection to be non-Lipschitz rather than require it to be Lipschitz, and
found an omitted term of the same order in one expansion. It confirmed the
crux, that the two balances may legitimately be subtracted, and it
strengthened the crossing-measure bound from one growing in time to one
uniform in time.

Three manuscript edits were licensed and applied at `navier-paper`
`4478bde`: `rem:highstrain-normalisation`, showing the Gronwall term and the
frequency split in the high-strain hypothesis are cosmetic; a sentence in
`rem:highstrain-scope` recording that signed pressure absorption implies the
quotient gap with an explicit remainder, so the two open routes are ordered;
and `rem:distance-balance`, the exact difference of the two balances with
the warning that the two dissipations are distinct objects. The graph's
HIGH-STRAIN review records both. No node is promoted.


### HF23: an unweighted div–curl estimate for the minimizer (AUDITED: PASS, imported)

A second external candidate arrived on the work capture surface, this time as
LaTeX source, written against the current heads and quoting the HF20 hash
correctly. The source is committed verbatim as
`research/evidence/hf23-divcurl-continuation.tex` with an index note beside
it, so no transcription stands between the repository and the artifact; both
are frozen by SHA-256
`abe74421ef6a8a7bacc108c0c08834e32f2a6116530fceb00368c8e67b129075`.

It claims that for every solenoidal `H^1` field the cubic minimizing
representative has genuine unweighted weak derivatives, with
`||grad w||_2^2 <= (5/4)||grad u||_2^2` and
`||grad q||_2^2 = ||div w||_2^2 <= (1/4)||grad u||_2^2`, no smallness required.
If that survives audit it discharges hypothesis (H1), which HF18-B introduced
and HF21-A reduced but left open, in the stronger form `W^{1,2}_loc` and with
explicit constants. It further claims the divergence defect is in `L^2`, that
the mixed-pressure pairing is unconditional in `L^2 x L^2` without the
separate `L^{3/2}` hypothesis (H2), and spacetime budgets for the
representative and the defect. It reconstructs HF20 with explicit constants
and adds a fixed-energy spacetime obstruction. It states plainly that none of
this establishes the arbitrary-data signed spacetime bound, and that the
natural absolute estimate leaves the square of the enstrophy in time rather
than the energy integral.

**Audited 2026-09-06, both scopes PASS.** Scope A, the regularity core, passes
with three expository repairs that change no statement or constant, so
hypothesis (H1) is discharged unconditionally in the global form
`grad w in L^2(R^3)`, with the stated constants, for every solenoidal `H^1`
field and with no smallness. Every HF18-B item gated on it becomes
unconditional, and the mixed-pressure pairing holds in the `L^2 x L^2` form, so
(H2) is bypassed; the residual content of the old pair (H1) and (H2) is
therefore exactly (H2). The auditor ran nine refutation attempts, including
independent spectral minimisations on data whose minimizer genuinely vanishes,
all failing, and added a forced consequence the candidate had not stated: the
vorticity vanishes almost everywhere on the zero set of the representative.
That resolves the consistency question HF21 left open and was confirmed on an
explicit flow whose minimizer vanishes on a surface. Scope B passes with scope:
its spacetime obstruction is genuinely new relative to the audited HF20,
supplying precisely the two upgrades the HF20 audit had named as unsupported,
namely from instantaneous to time-integrated and from the full transport term
to the low-passed one for every fixed cutoff.

**Correction to the controller's own record.** The paragraph below claimed that
the audited HF21-A curl identity is a pillar of this candidate. The audit shows
otherwise: the candidate re-derives that identity itself for its regularized
problem, so it is logically self-contained and inherits no risk from the HF21-A
repair. The audited theorem corroborates rather than supports it.

Controller check of the core, not an audit: the mechanism is a Cordes-type
argument resting on a constrained matrix inequality and the two Fourier
div–curl identities. The matrix inequality is *not* the false unconstrained
statement it superficially resembles; it is conditioned on the Euler–Lagrange
relation, and under that constraint the proof is correct with equality exactly
at the endpoint. The identities and the combination giving the two constants
were verified. One pillar is the identity that the curl of the representative
equals the curl of the velocity, which is the audited HF21-A Theorem 1, so an
audited repository result supports the new candidate. What remains for the
audit is the regularized problem, the uniformity and passage to the limit, the
extension to `H^1` data, the behaviour across the zero set, and consistency
with HF21-A's two statements about that zero set.

**Integrated 2026-09-06.** The Scope A results are now manuscript theorems:
`prop:quotient-divcurl` with `lem:trace-control`, and the corollaries
`cor:quotient-defect`, `cor:quotient-vorticity-zero`,
`lem:quotient-mixed-pressure` and `cor:quotient-budgets`, at `navier-paper`
`80a62fd`, 95 pages. The section's opening no longer claims it proves no
regularity theorem, and `rem:quotient-scope` records the limits. The import
cites the section's existing lemmas instead of reproving them and avoids
uniform convexity, so the standing remark that no Clarkson inequality is used
remains true. The graph gains the node QUOTIENT-REGULARITY; no gap node is
promoted.

**Scope B integrated 2026-09-06** at `navier-paper` `2883cbd`, 97 pages, with
its four required repairs applied and an explicit list of claims declined. The
second paragraph of `rem:no-monotone` now excludes any remainder depending
only on viscosity, energy, horizon, coefficient and cutoff, for every fixed
cutoff, by a family whose time interval shrinks faster than its integrand
grows; it states that the hypotheses select their cutoff and remainder from
the whole datum, so nothing there bears on them. It also records that a bound
on the time integral of the squared enstrophy would itself be a classical
regularity criterion, so that route is unusable rather than merely
insufficient. No HF23 integration item remains.


### HF22: attacking (G) and its three sub-questions (AUDITED)

Four lanes, delivered 2026-09-06, **all unaudited**; nothing is promoted and
the manuscript is untouched. (G) is neither proved nor refuted, and each lane
says so.

- **Sub-question (a) is answered NO** (`hf22-dissipation-comparison.md`).
  Neither dissipation dominates the other: both signs occur, already settled in
  the audited HF19-D and here re-derived independently by a third route. The
  lane adds an exact minimizer-free inversion: the map taking a solenoidal
  field to its normalised square root is a bijection onto the nonlinear-Hodge
  class, so the velocity and the defect are recovered with no minimisation and
  no perturbation, and sub-question (a) becomes a question about that
  parametrisation. It also records that the affirmative branch would not have
  closed (G) anyway, since it would only have moved (G) onto the pressure
  route. **Its audit rejected that last reasoning**, on three counts: a dropped
  factor leaves the two integrals compared with different amplitude weights, a
  one-way implication was read as a biconditional, and non-derivability was
  read as falsity; a repaired, weaker form is supplied. The negative answer
  itself survives, so the corresponding term in the distance balance has no
  sign and may not be dropped, which confirms rather than corrects the
  manuscript.
- **Sub-question (c) is answered NO in a repaired, weaker form**
  (`hf22-good-set-dissipation.md`). Its audit found the load-bearing negative
  result FAILS as displayed: the constraint list was incomplete, and the
  explicit family violates an omitted but genuinely audited constraint on most
  of the time axis. The auditor supplied a repaired family and the two missing
  constraints, so the negative survives only as non-derivability from an
  explicitly enumerated constraint set, not from the audited record as such.
  Two further corrections: the headline confused falsity with non-derivability,
  and the realisation dichotomy is **not new**, being the manuscript's own
  scope remark. What survives verbatim, with every constant recomputed, is the
  master deficit inequality and the genuinely useful by-product that the good
  set is free in (G), so the gap reduces to its bad-set restriction.
- **Sub-question (b) is not decided** (`hf22-projection-regularity.md`), and
  its audit withdrew the lane's main structural claim: the assertion that this
  sub-question inherits the open weighted inequality of HF18-B is **not
  established**, since the two objects differ in every relevant respect,
  weighted against unweighted, one-point against two-point, and conditional
  against assuming no regularity, with no implication displayed either way.
  The lane's reduction is also only formal, presupposing a differentiability
  it does not justify. The interval of exponents it cuts survives.
- **The direct attack** (`hf22-direct-attack.md`) contributes the pressure-route
  mirror, the exact deficit of the natural interpolation attempt computed once
  and for all, and one conditional reduction resting on a new hypothesis. Its
  audit struck three claims: that the target is strictly stronger than the gap,
  which contradicts the note's own equivalence proposition; an endpoint
  supremum equivalence refuted by a swirl family the note itself cites; and an
  exhaustion claim that exactly two scalar functionals are differentiable in
  time, refuted by the kinetic energy, which the note lists among its own
  inputs.

**All four audited 2026-09-06, all REPAIR**, each with a real catch; repairs
are being applied. The pattern is worth recording: three of the four defects
were overclaims of the same species, treating a result as false when only its
derivability from a listed set had been shown, or as new when the manuscript
already contained it. The controller's own plan summary repeated three of
those overclaims before the audits returned and is corrected above.

**Repairs applied 2026-09-06.** Each note now carries its audit verdict and
the prescribed replacements, with every overclaim removed rather than patched.

**Convergence worth noting.** Two lanes that did not share a question arrive
independently at the same next target: an input-only modulus of continuity for
the distance along the trajectory at the critical level, equivalently an
input-only bound on the number of crossings of that level. It would upgrade the
audited crossing-measure bound to a crossing-count bound and, with the good-set
result above, reduce (G) to its bad-set part. It is a question about time
regularity of the nonlinear projection along the flow, distinct from every
sub-question posed so far. **This is now the next wave, HF24**, and the newly
proved regularity of the representative is a genuine new tool for it: the
representative's gradient and the divergence defect are now controlled in
`L^2` by the datum, with input-only spacetime budgets, which was not available
when the two lanes posed the question.


### HF25: dissipation comparison, sharp defect order, defect criterion (AUDITED, imported)

A second external continuation arrived 2026-09-06 as LaTeX source, 1293 lines,
committed verbatim as `research/evidence/hf25-beyond-hf21-continuation.tex`
with an index note, frozen by SHA-256
`3ce562bb59346fc700c522bf5e857e3500b318e283febed0c9db9b7f652c6d4f`. It pins
the current heads and compares against the **repaired** HF21 notes, not the
superseded ones.

It reports: a **quantitative early-time rate** for a compactly supported field
leaving the nonlinear-Hodge class under linear heat flow. The claim recorded
here earlier, that this supplies a witness the programme could not construct,
is **false and is withdrawn**: the audit found that the audited HF19-D already
constructs such a witness and refutes both directions, and that it was present
at the very revision HF25 pins. What is new is the rate and the computed
constant, and HF25 proves only one direction; exclusion of every
superlinear defect exponent, closing the interval HF21 and HF22-B left open;
a quantitative criterion bounding the quotient's growth by the fourth power of
the divergence defect in `L^2`; a conditional producer giving the target
inequality with explicit input-only constants whenever that fourth-power
defect integral is input-bounded; a critical family with the scaling relation
`2/s + 3/a = 2`, a Serrin-type line stated for the divergence defect rather
than the velocity gradient; and the failure of the energy-only version of the
target on actual trajectories.

Its own boundary, stated plainly: the defect is controlled in square
integrability in time by the energy identity and the new div–curl estimate,
while the criterion needs fourth power, and nothing in it supplies that
upgrade for arbitrary data, so it is not an unconditional regularity theorem.

**A correction, and a correction to that correction.** This plan described the
target inequality as "the whole of the frozen gap"; on HF25's prompting the
controller recorded that as too strong. **The audit refuted that edit as
stated.** The phrase is ambiguous, not wrong: the audited HF22-D repair block
already fixed its meaning as the sufficiency statement, that the target with
contraction factor zero suffices, with no cutoff and no Gronwall term, and
endorsed it. Two things are nevertheless right and are now recorded: the
target is reached by *two* discardings, the sign of the transport term and the
one-sided size estimate, not one; and a strictness claim at these quantifiers
must not re-enter through the plan's wording, since that is exactly what the
HF22-D audit struck as its first bad bridge. The correct phrasing is that the
target **suffices** to close the gap, and that the converse is not derivable
per trajectory.

**The hash discrepancy is resolved.** The audit established that our HF23
artifact is the LaTeX source and HF25 cites its PDF rendering, which is
exactly 23 pages; the theorems HF25 attributes to it match what our audited
HF23 proves, and no misattribution was found. Flagging it was right; it turned
out benign.


### HF24: modulus of continuity and the bad-set restriction (AUDITED: REPAIR)

Two lanes, delivered 2026-09-06, **both audited 2026-09-06, both REPAIR**. In
each case every load-bearing computation was recomputed and reproduced, and in
each case an overclaim was withdrawn. The audits are
`hf24-review-modulus-of-continuity.md` and `hf24-review-badset-restriction.md`.

`hf24-modulus-of-continuity.md` obtains a modulus, but in a different currency
than the question asked: the distance is Hölder with exponent one quarter with
respect to an input-only spacetime measure, with an explicit constant except
for a factor built from the enstrophy at the two endpoints. That yields a new
unconditional constraint on the bad set and a crossing count conditional on
one named scalar. Its gap is an input-only upper bound for the enstrophy
restricted to the corridor of times where the distance sits near the critical
level; the lane was right that the *unrestricted* form of that
bound is the critical hypothesis verbatim, and the audit decides the question
the lane left open: the corridor restriction **does** escape the circularity.
By the audit's Proposition R1 the corridor hypothesis holds if and only if
either the horizon precedes the maximal time, or a finite-time blow-up keeps
the distance strictly above the upper corridor wall on a final interval. The
second alternative is a blow-up satisfying the hypothesis, so the hypothesis is
implied by the Clay conclusion and does not imply it. It is therefore strictly
weaker than the critical hypothesis and, unlike the high-strain hypothesis, is
**not** of the existential-equivalence class; its whole content is the
exclusion of that final-interval branch. The audit also corrects the lane's
crossing count: only the components that reach the upper corridor wall are
counted, which is what the bad set needs, while components oscillating inside
the corridor are not countable from the record. And the lane's weighted
stability lemma is not new, being the audited HF22-B Theorem A verbatim; the
genuine novelty is pairing that weight against the new sixth-power bound,
which is what improves the modulus exponent from one eighth to one quarter.

`hf24-badset-restriction.md` returns a negative with a sharp accounting. The
route the lane was asked to try fails for a stated reason: by scaling the only
admissible inequality needs either the representative in `L^2`, which the
import explicitly does not assert, or the residual hypothesis (H2). Its
unconditional substitute reproduces the audited measure bound with the
identical constant. The valuable output is the exact deficit: the integrated
transport work is bounded by input-only quantities except for a single factor,
the supremum of the enstrophy on the bad set, and that shortfall is exactly
one power of the enstrophy and is sharp, with a plateau family showing it. In
Ladyzhenskaya–Prodi–Serrin bookkeeping the lane reports that the newly proved
regularity buys precisely the removal of an earlier overshoot: the older route
demanded a position one sixth past the Serrin line, while the route through
the new mixed-pressure estimate demands the Serrin line exactly.

**Convergence again.** Both lanes end at the same new question, which no
earlier lane posed: is the enstrophy bounded by input data on the set of times
where the trajectory is far from the nonlinear-Hodge class? **This plan previously called that question strictly
weaker than a Serrin bound. That claim is withdrawn as false.** The audit's
Lemma A establishes that the bad-set hypothesis is equivalent, at the
programme's quantifiers, to global continuation past the horizon for the datum,
hence to the critical hypothesis and to a Serrin bound; it belongs to the
existential-equivalence class, exactly like the HF25 defect hypothesis. It is
strictly weaker only pointwise, for a fixed trajectory and a fixed stopping
time, where it constrains the enstrophy on a set of input-bounded measure and
leaves the good set free. The narrowing is of the search surface, not of the
assumption. Earlier waves measured that set and then counted its
crossings; neither constrained the height of the enstrophy on it. Per the
audit's Proposition R1 the falsifiable form of the shared question is sharper
than the enstrophy phrasing: must a finite-time singularity re-enter the
corridor at times accumulating at the singular time?

**Controller adjudication of a conflict between the two audits.** The bad-set
audit, having proved its Lemma A, extrapolated it to the sibling lane and
concluded that both corridor and bad-set hypotheses are equivalent to global
continuation, on the general principle that "restricting the set of times does
not lower existential strength". **That extrapolation is refuted**, by the
Proposition R1 the other audit proved and this one did not have. The general
principle is false as stated, and the reason is precise. Lemma A's forward
direction needs the restricted hypothesis to force regularity, and whether it
does depends on whether the restricting set can be *escaped*. The bad set is
the set of times far from the nonlinear-Hodge class, which is upward closed in
the distance: a blow-up cannot leave it, so bounding the enstrophy there forces
regularity and the equivalence holds. The corridor is a *bounded band* around
the critical level: a blow-up can exit it upward and never return, leaving the
corridor empty near the maximal time, so the hypothesis is satisfied vacuously
and the forward direction fails. The two hypotheses therefore genuinely differ
in logical strength, and each audit is correct about its own object. What
distinguishes them is not that one restricts a set of times but the *shape* of
the set restricted.

**That last sentence was wrong, and the HF29 obstruction lane inverted it.**
I wrote that the corridor hypothesis is the only object whose refutation would
not amount to refuting the Clay statement. The opposite is true: by Proposition
R1 the hypothesis can only fail if a finite-time singularity exists, so
**refuting it requires settling Clay negatively**, and it is unfalsifiable
within this programme. Being outside the equivalence class does not make it
easier to attack; it makes it attackable from neither side. Its status is
recorded in the HF29 section below.

### The sharpened first gap (2026-09-06)

After the audited HF23 and HF25 results the missing step has a concrete
scalar form: upgrade the divergence defect of the minimizing representative
from square to fourth-power integrability in time, for arbitrary data, on the
critical line `2/s + 3/a = 2`. What is unconditional is the square-integrable
bound, with the explicit budget from the energy identity; the criterion needs
the fourth power.

Three cautions, all from the audits and all load-bearing. First, because the
defect is pointwise at most half the velocity gradient in `L^2`, that
hypothesis is **implied by** the classical Ladyzhenskaya–Prodi–Serrin and
Beirao da Veiga gradient criteria on the same line, so it is not a weaker
assumption than what the literature already knows; its interest is that it
constrains only the divergence of the representative rather than the full
gradient. Second, it belongs to the existential-equivalence class, so at the problem's
quantifiers it is equivalent to global continuation, like every other
formulation the programme has produced **except one**: the audited HF24 bad-set
hypothesis joins it in that class, while the HF24 corridor hypothesis is the
single exception, being strictly weaker by Proposition R1. Third, the bad-set accounting of
HF24 says the residue after the import is exactly one factor, the height of
the enstrophy on the set of times far from the nonlinear-Hodge class, and that
this shortfall is sharp. The value of the reformulation is as a different
mechanism, not as a weaker hypothesis, and nothing here is progress toward a
proof until one of these is discharged without a continuation norm.


### HF26: weighted linearization, actual-flow departure, temporal criterion (AUDITED: four scopes, all PASS WITH SCOPE)

A third external continuation arrived 2026-09-06 as LaTeX source, 1432 lines,
committed verbatim as `research/evidence/hf26-temporal-continuation.tex` with an
index note, frozen by SHA-256
`24b538280c8639b81a1f6f86d4c72370362625ca8a52d1d81a99b29236a540ab`. Unlike the
two earlier continuations, **all three of its pinned revisions were checked
with `git rev-parse` and match our commits exactly.** Four independent audits
are in flight, one per scope. Nothing below is promoted.

It offers four things. It replaces the *formal* linearization of the nonlinear
projection, which the repaired HF22 note could only treat formally, with a
strong-limit theorem in a fixed degenerate weighted Hilbert space, plus a strong
Hadamard derivative of the dual field into `L^{3/2}`. It upgrades the departure from the nonlinear-Hodge class from linear heat flow,
where HF19-D and HF25 both established it, to the **actual Navier–Stokes flow**
at every viscosity. That scope is **audited PASS WITH SCOPE**
(`hf26-review-actual-flow-departure.md`) and was *strengthened* by the auditor:
the document's hedge "except possibly one amplitude" is deleted, because an
exceptional amplitude would force an identity between an odd and an even field
and hence the identically zero case, which the explicit nonzero value
contradicts. The theorem therefore holds for every positive amplitude. The
value on which it rests was recomputed from scratch and agrees to forty digits.
Two qualifications belong with it. The strengthening is of the *departure* half
only: the field, the scalar and the constant are inherited from HF19-D and the
quadratic rate from HF25, so what is new is the actual flow in place of a heat
proxy, an exact coefficient, and explicit dependence on viscosity and
amplitude, while the dissipation-comparison half is untouched. And as written
the section inherits the risk of the linearization scope, though the auditor
supplied a two-line proof of the only half the conclusion needs, so it can be
re-based to stand alone. It
gives a one-scale temporal criterion producing the full target from a supremum
bound on the strong `L^3` temporal residual of the correction at a single
input-selected scale. And it proves unconditionally, from energy alone and with
no continuation norm, an *integrated* translation estimate for that residual,
together with a bound on the measure of the exceptional set.

Its own boundary is stated plainly and repeated: the integrated estimate does
not imply the supremum the criterion needs, the gap is exactly the dissipation
accumulated on a small-measure exceptional set, and no arbitrary-data witness
is supplied for any of the three alternatives it lists.

**The item that would change our own record.** Its concentrating comparison
curve is built from genuine solenoidal fields whose variational objects are the
actual ones. The controller verified its scaling algebra symbolically: the curve
satisfies the exact kinetic-energy identity, the exact quotient identity, has
constant scalar distance, and can be made to satisfy any prescribed cubic
enstrophy bound — while both the target quantity and HF25's fourth-power defect
integral diverge on it. It is not a Navier–Stokes solution.

**Audit of the countermodel scope, returned 2026-09-06: PASS WITH SCOPE**
(`hf26-review-countermodel-crossings.md`). Every row of the controller's table
was reproduced by independent derivation and quadrature, the seed field was
verified to exist with its constants computed two ways, and eight of nine
refutation attempts failed. The exclusion is real, and **materially narrower
than this plan first stated. Two claims written here are withdrawn.**

The first was that the curve violates nothing at the scalar level. It violates
three things: the enstrophy *identity*, which the audit computed explicitly and
which is a third scalar test that does see the residual; any vector modulus;
and it is *forced* to hold the scaled distance at or above the viscosity, so it
lives entirely in the bad set and excludes nothing about smallness. The second
was that the residual is invisible to both scalar tests as though that were an
independent fact: the audit shows those two vanishing projections simply *are*
the energy and quotient balances restated.

What survives, stated exactly. No derivation of the target, or of the signed
estimate below the endpoint value of its parameter, follows from genuine
variational objects with all instantaneous identities, the two scalar
projections of the residual, energy-level budgets, any scalar modulus or
crossing information, the cubic enstrophy inequality in either form, and a
bounded critical norm. Four things are not excluded, and one matters greatly:
**the signed estimate at the endpoint parameter value, which the curve itself
satisfies with zero remainder, and which already suffices for the programme.**
So the signed route is untouched by this construction. Also unexcluded are
scalar smallness thresholds, vector moduli, and the enstrophy identity. And
since the curve keeps both its critical norm and its quotient bounded, it
refutes a *certificate* rather than the target.

**Prior art, from the audit.** The curve is exactly the backward self-similar
ansatz, so Nečas, Růžička and Šverák and later Tsai must be cited before any
import. It is the rigorous realisation of the viscous-eddy family sketched in
the HF24 modulus lane, and the same species as the audited HF22-C construction,
which it strictly strengthens by closing two of that construction's three named
escapes and leaving only the actual equation.

**One claim of ours is refuted, and it is this plan's own sentence.** I first
recorded that HF26 challenged two of our claims. The audit narrows that to one.
The surviving correction is to the sentence above asserting that an input-only
modulus for the distance is *equivalently* an input-only bound on the number of
crossings of the critical level. That equivalence fails in both directions: a
modulus bounds excursions between *separated* thresholds, not crossings of a
single level, as a smooth function with a Lipschitz modulus crossing a fixed
level infinitely often shows; and conversely a crossing count supplies no
modulus. **The error was confined to this plan's summary.** The HF24 modulus
lane already stated its target in corridor form, and the HF24 audit had already
recorded that components oscillating inside the corridor are not countable from
the record. So HF26 *confirms* our HF24 audit rather than challenging it, and no
HF24 verdict changes. The scalar-versus-vector distinction I listed as a second
challenge is likewise not a challenge to HF24 but a property of HF26's own
producer, which observes the vector field in strong norm.

**Audit of the temporal scope, returned 2026-09-06: PASS WITH SCOPE**
(`hf26-review-temporal-producer.md`). Every inequality, constant and derivation
in the producer, the energy-level modulus and the exact remainder is correct as
written; no arithmetic error, no invalid bridge, and no continuation norm inside
any proof. The scope is logical rather than computational, and it is decisive:
**the proof is clean, the hypothesis is not.** The auditor proved that a
uniform bound on the enstrophy supplies the required vector modulus with an
explicit sixth-root rate, hence supplies the hypothesis; so the hypothesis is
equivalent to global continuation past the horizon, and so are all three
alternatives of the conditional theorem, which are therefore not three routes
but one. The document's own guard, that the scale be "justified without an
endpoint continuation norm", is a statement about a future proof and not a
condition on the scale, and is unenforceable as written. The temporal criterion
therefore joins the existential-equivalence class alongside the HF25 defect
hypothesis and the HF24 bad-set hypothesis, and against every classical
criterion it is neither weaker nor stronger but logically equivalent.

**Audit of the linearization scope, returned 2026-09-06: PASS WITH SCOPE**
(`hf26-review-weighted-linearization.md`). The mathematics is correct as
displayed, reconstructed independently including both signs of the
perturbation, the degenerate weight and the zero Hilbert space. The strong
convergence is a genuine Minty-Browder argument, and the auditor confirmed
what mattered most: no step uses unweighted convergence of the difference
quotients or unweighted control near the zero set, so the result does not
quietly restore the gap the weighted formulation exists to avoid. The zero set
contributes nothing to the dual limit for free, which is exactly why the
unweighted dual conclusion is compatible with the document's own warning. Nine
refutation attempts were made and seven failed outright, including a
finite-dimensional model reproducing the Hessian symmetry to fifteen digits.

Three scope repairs, all about claims *around* the result rather than the
proofs. The document over-reads its relation to HF22: that lane's formal ansatz
presupposed differentiability in the ambient norm, whereas what is proved here
is only the weighted version, so two of HF22's open questions are untouched
rather than resolved. One quantifier is wrong, the identities being asserted
near a first-order Sobolev hypothesis but proved only for much smoother data
with no extension supplied. And a constant in the appendix needs an extra
almost-everywhere convergence to reach the stated value rather than twice it.

**Two leads worth their own wave, both from that audit and both unaudited.**
The first is that the producer's own section re-derives the HF25 defect
criterion in two lines, so what HF26 adds there is not a new criterion but the
replacement of the sixth-power norm by a scale-averaged surrogate, with the
averaging cost paid in the exceptional-set residual. The second is sharper: the
same two-line argument appears to settle *negatively* the question the
manuscript's scope remark explicitly leaves open in both directions, namely
whether a branch can have divergent squared-enstrophy integral but finite
fourth-power defect integral. If that survives audit the manuscript's remark
stays true as written, since it claims only that the matter is not settled
there, but the graph's gap node would need its review text amended. Neither
lead is promoted.


### Prior art for the weighted linearization (2026-09-06, lane in progress)

Commissioned because HF26's own ledger says a comparison with convex
sensitivity theory would be required before claiming novelty for its main
analytic tool, and because the manuscript's related-work section covers
nonlinear Hodge theory but nothing on metric-projection differentiability. The
lane has reported (`hf26-prior-art-projection-differentiability.md`); five
sub-lanes are still refining individual areas.

**The headline is negative, which is the useful outcome.** The programme must
not claim novelty for the weighted linearization, on four separate grounds.
The shape of the derivative — a weighted least-squares projection with weight
built from the residual — is the classical linearization of an `L^p`
best-approximation problem and folklore in the iteratively-reweighted
least-squares literature. The proof template — bound the difference quotients
in a base-point-adapted space, take a weak limit, identify it from the
linearized optimality condition, upgrade by monotonicity — is standard convex
sensitivity analysis. The degenerate weighted space is the standard energy
space of a linearized `p`-Laplacian operator and its weight has established
names. And the failure of the weighted derivative to control the ambient norm,
which HF26 treats as its characteristic difficulty, is the **two-norm
discrepancy**, named and studied since 1979 and routine in PDE optimal control.

**That item is now settled, and the answer is no.** The lane flagged a refereed
2024 paper stating directional differentiability of the metric projection in a
class of spaces containing ours, which if applicable would have covered our
subspace with a *stronger* conclusion. Reading the preprint properly rather than
through a text proxy settles it: its hypothesis requires the convexity exponent
to be *below* the smoothness exponent, our space has convexity of power type
three against smoothness of power type two, and the proof's convergence factor
therefore diverges instead of vanishing. As the preprint states it the class is
empty outright, by Nordlander's theorem. The theorem subsumes nothing. HF26's bibliography also cites a
different, superseded preprint by the same author and calls it unpublished when
it has since appeared. Neither is a defect in our repository, since we have
imported none of this; both are blocking for any future import.

**An actionable gap in the committed manuscript, independent of HF26.** The
weighted dissipation lemma imported today uses the field `V = |w|^{1/2}w`,
which is exactly the object the `p`-Laplacian literature calls the natural
distance or shifted `N`-function and which has a standard citation line. The
manuscript currently cites none of it. This is a genuine prior-art omission in
committed work and is queued for repair once the two sub-lanes covering that
literature report.


### HF27: a full-equation critical residual certificate (AUDITED: three scopes; DO NOT IMPORT)

A fourth external continuation arrived 2026-09-06 as LaTeX source, 996 lines,
committed verbatim as `research/evidence/hf27-critical-residual-continuation.tex`
with an index note, frozen by SHA-256
`3898e9a020d31c4fc58c9f1289ea4794ec9f787b885086e411b98b0cb1f97488`. Both pinned
revisions verify with `git rev-parse`, one of them our own HF25 import from
earlier the same day. Three audits are in flight; nothing is promoted and the
manuscript is untouched.

**It changes direction, and says why in our own terms.** It abandons the
quotient of the solution for the quotient of the *error against a comparison
flow*, with the comparison supplied on the whole horizon and its equation defect
retained and estimated. Its stated reasons are our audited findings: the
temporal route needs a uniform bound that integration in time does not supply,
small measure of the exceptional set does not bound the dissipation there, and
the concentrating curve shows scalar balances can miss a nonzero residual.

**Audit of the oscillatory and hierarchy scope, returned 2026-09-06: REPAIR**
(`hf27-review-oscillatory-hierarchy.md`). Every mathematical step in that scope
is correct and twelve refutation attempts against the mathematics failed; the
repair is to claimed significance and prior art. **The headline positive result
is not what it appears.** The certified family's `L^3` norm does diverge, but
its `BMO^{-1}` and Besov norms tend sharply to *zero*, over a strictly wider
exponent range than the document's own theorem covers. It is a small-data case
in disguise, global since Koch–Tataru and the Cannone–Meyer–Planchon line, on a
larger range than the certificate reaches; the auditor derived that in three
lines from the document's own estimate and confirmed numerically that outside
the document's range its quantity grows while the critical norm still decays.
The exponent restriction is sharp for the method, not for the truth, and the
small-data corollary is the classical critical-Besov criterion with worse
constants. The Chemin–Gallagher citation is the wrong regime in the wrong
direction: their data are large in the norm where this family is small, so the
family sits strictly below their results, and the covering citations are absent.
The hierarchy results themselves verify step by step, are not vacuous and are
not circular.

The document claims a certificate producing continuation past the horizon from
one comparison flow whose critical residual stays below an absolute multiple of
the viscosity; the oscillatory family just described; a comparison hierarchy with global band-limited
comparisons for every datum and completeness in the regular case; unconditional
energy-level residual convergence; and two obstructions, that exact energy
balance does not control the critical residual and that an arbitrarily small
energy-level residual is still insufficient, together with a quantitative
dichotomy every certificate must satisfy if the solution is singular.

**Audit of the energy and concentration scope, returned 2026-09-06: REPAIR**
(`hf27-review-energy-concentration.md`). No invalid step exists anywhere in that
scope and every algebraic claim was re-derived independently, several to the
last constant. Two things block a pass.

The first is prior art, and it is worse than I recorded. I noted the curve is
the backward self-similar ansatz and needs the standard citations. The audit
found that understated: the curve's defining equation is *literally* the
Nečas–Růžička–Šverák and Tsai equation in the same normalisation, its profile
residual is character for character the Leray-projected Leray profile equation,
and the critical time the document tunes is exactly the energy identity every
Leray profile must satisfy. Neither author, the ansatz, nor the profile equation
appears anywhere in the 996 lines or the bibliography. The published theorem
that an integrable weak solution of the profile equation vanishes would give the
document's own nonzero-residual conclusion in one line, whereas it derives it
through a heavier route resting on a source it admits it could not fetch.

The second is a genuine logical gap: the unconditional convergence is available
only for exponents strictly above the one at which the obstruction is stated,
and homogeneous Sobolev spaces do not nest. The audit judges it repairable.

**Audit of the certificate scope, returned 2026-09-06: PASS WITH SCOPE**
(`hf27-review-certificate.md`). Every proof in that scope is correct as
displayed, with all constants, Hölder splits, Young maximisations and
interpolation exponents recomputed independently at sixty digits and over a
four-million-point sweep. The bootstrap is **not** circular, and the relative
identity is exact with the pressure genuinely cancelling before any estimate.
Eleven refutation attempts all failed mathematically; three succeeded against
claims *about* the results.

**The prior-art answer is yes.** The certificate *is* the robustness principle
of Chernyshenko, Constantin, Robinson and Titi, matched item for item: the
certificate is their Theorem 3, the index corollary their Corollary 5, the
completeness steps their Theorem 6, the equivalence their Theorem 8. The real
differences are the whole space in place of the torus, a critical norm in place
of high Sobolev regularity — carried by the quotient, which is the technically
substantive part and is what removes the pressure — explicit constants, and a
scale-invariant threshold, which the audit verified is genuinely scale
invariant. The document's own prior-art discipline is substantive but materially
incomplete: it names the right paper with the right identifier and disclaims
novelty, but the entire critical-norm branch of that literature is missing, and
one 2025 preprint already combines the critical norm, the endpoint theorem, the
same viscosity-cubed Gronwall exponent and a negative-Sobolev residual. The
residual novelty is about one sentence long.

**Its logical strength, stated correctly after two of my own errors.** I first
treated the question as open, then over-corrected to say the document proves its
criterion equivalent and "says so itself". Neither is right. The document proves
equivalence for the *hierarchy* only; the one-line witness for the general
criterion — take the comparison flow to be the solution, so the critical
quantity vanishes — appears nowhere in it, and its single mention of that
substitution warns against misusing it. Both auditors derived the witness
independently, which corroborates the mathematics and settles the attribution.
The certificate joins the existential-equivalence class with the HF25 defect
hypothesis, the HF24 bad-set hypothesis and the HF26 temporal criterion, and it
is not a second exception, since no branch lets it hold vacuously. **The
corollary the document never draws is that its stated missing implication is
logically equivalent to Clay alternative A**, so its final section restates the
target rather than reducing it.

**One genuine regression to record.** The audit found that this document drops a
zero-set fact its predecessor had, which must be restored before any import.
The dichotomy the document calls quantitative is genuine but not quantitative,
since the bound degenerates exactly in the regime its own estimate permits.

**One controller observation stands.** It reuses the dilation curve HF26 used,
which our countermodel audit identified, and that flag was confirmed correct. And its prior-art posture is
markedly better than its predecessors': it names the robustness and
conditional-Galerkin literature, notes that the version it read works on a
periodic cube in high regularity, explicitly declines to import a torus theorem
to the whole space, and names the oscillatory large-data literature while
calling its own family a test rather than a novelty claim. Whether that
discipline is substantive or decorative is the first audit question, not the
last. It also disclaims any claim to be logically weaker than regularity at the
existential level, which is the right posture but is a disclaimer rather than a
determination; the audit decides it.

**Import decision, 2026-09-06: do not import any part of HF27 into the
manuscript.** The three audits agree on why, and none of the reasons is a
mathematical error — the mathematics is correct throughout, with well over
thirty refutation attempts failing against it.

The certificate is the Chernyshenko–Constantin–Robinson–Titi robustness
principle matched item for item, and its residual novelty over that literature
is roughly one sentence. Its hypothesis is equivalent to the target, so the
final section restates Clay alternative A rather than reducing it. The positive
test certifies a family that is small on the critical scale and has been global
since 1994 and 2001, over a wider range than the certificate reaches. The
concentration test's curve is not merely the backward self-similar ansatz but
literally the Leray profile equation, uncited, and the published triviality
theorem yields its conclusion in one line. Its weighted appendix reconstructs
the audited HF18-A and is already in the manuscript as
`lem:qe-weighted-dissipation`, and it drops a zero-set fact its predecessor had.

What the wave is worth keeping for is the corrected prior-art map, now recorded
here and in the evidence notes: the robustness line and its critical-norm
branch, the small-data critical-Besov line, and the Leray profile literature.
Those bear on any future comparison-flow route the programme takes.


### HF28: a discounted spectral certificate (AUDITED: certificate scope PASS WITH SCOPE)

A fifth external continuation arrived 2026-09-06 as LaTeX source, 1078 lines,
committed verbatim as `research/evidence/hf28-weighted-spectral-continuation.tex`
with an index note, frozen by SHA-256
`80c6b1339704261d5540ce9620e5799f0e9c9ea7c78cd1af412d075ea8699055`. All three
pinned revisions verify; the research pin is our own commit from earlier the
same day. A second audit, on its countermodel and spectral scope, is in flight.

**It answers two of our own audit findings.** Our HF27 certificate audit found
the whole-space and critical-norm branch of the robustness literature missing;
this document cites a whole-space treatment and says it is more directly
relevant than the periodic result. Our prior-art lane found the weighted objects
already named in the `p`-Laplace literature; this document cites that framework
and states that our research record warns against novelty claims for the
weighted linearization. It disclaims novelty in the underlying mechanisms.

**Audit of the certificate scope: PASS WITH SCOPE**
(`hf28-review-certificate-status.md`). Every step is correct, every constant
reproduces under independent recomputation, and eleven refutation attempts
failed to break a stated result. The scope is severe.

**The structural novelty is real, and so is the equivalence.** The audit
confirmed what no previous wave achieved: the test quantity genuinely contains
no norm of the unknown solution, and the witness that defeated every earlier
certificate — taking the comparison flow to be the solution itself — is
unavailable here, because the comparison is canonically fixed by the datum and
the truncation index. Equivalence was re-established anyway, by theorem rather
than substitution: some index succeeds if and only if the branch continues past
the horizon. So this is a fifth member of the equivalence class, and the
corridor escape is unavailable, since every object is defined for every input
and there is no set a singularity can vacate. **The HF24 corridor hypothesis
remains the sole exception.**

**Two errors of mine, one load-bearing.** I called the gap arithmetic rather
than conceptual: a logarithmic bound needed where quadratic growth is available.
The audit computed the exact requirement and showed the inequality holds
precisely when continuation holds, so the gap is Clay alternative A itself, and
when it holds the integral is bounded rather than merely logarithmic. I also
repeated the document's own quadratic estimate as fact, which excludes its
spectral enstrophy inequality, and I framed the audit brief as needing to see
past a disclaimer when the document **concedes** rather than disclaims: it
states the equivalence and its own class membership, omitting only the final
quantifier step. It is the most honest of the five continuations on this point
and my framing implied the opposite.

**Its sharpest finding is one the document misses.** The certificate's
provably-firing region today is exactly the region where the same two estimates
applied directly to the solution already give global regularity, with the
identical constant, and the horizon it reduces to is the elementary local
existence time. As a proved matter it certifies nothing new. Its value is in the
*form* of the target, not its strength: for the first time the quantity to be
estimated is free of the unknown solution.

**All three dependency removals are real.** The endpoint critical-norm theorem
is genuinely removed rather than relocated, replaced by a non-endpoint Serrin
condition plus an alternative from local theory — a strictly weaker import. The
audited unweighted div–curl result is genuinely unused, at the price of the
divergence defect and the mixed-pressure pairing, neither needed here. The direct enstrophy estimate is proved outright with its constant verified.

**Audit of the countermodel and spectral scope: REPAIR**
(`hf28-review-countermodel-spectral.md`). No invalid mathematical step anywhere
in scope; twelve refutation attempts, one partial success. **The countermodel
stands**, with all five clauses verified independently: the joint between its
branches is exact rather than merely smooth, so the curves are genuinely defined
for all time; the band limit holds forever; the energy identity is exact and in
fact forced, its amplitude law being the unique solution; the enstrophy
threshold is exactly tight; and the logarithmic rate matches to six digits over
a wide range and analytically far beyond it.

**It is genuinely stronger than our two earlier audited countermodels**, on
three axes: those die at their concentration time while these are global, these
share one datum across the whole index family, which is what is needed to refute
an existential producer, and these are band-limited. Half of its own comparative
sentence is a strawman, since neither predecessor was an abstract blowing-up
scalar ODE. What it excludes is scalar-budget closures only — arguments bounding
the stress integral from energy, enstrophy, the spectral inequality and
band-limitation. It excludes nothing touching the vector equation, the residual's
decay in the index, cross-index coherence, or small data. The curves are
energy-blind but enstrophy-visible.

**The prior-art defect has now recurred three times, in its strongest form yet,
and that is a failure of mine to institutionalise.** This document's residual
equation is character for character the Leray-projected Leray profile equation,
its critical-time identity is symbolically that equation's own energy identity,
and the limit of its family *is* the object of the self-similar literature. It
contains zero occurrences of that literature's terms or authors. We required
those citations for HF26 and again for HF27; I recorded the requirement both
times but never carried it forward as a standing check, so a third document
reproduced the same object uncited. A standing item is added below.


## Phase II programme (opened 2026-09-06)

The user re-sequenced: paper proofs arrive externally, `../navier-paper` is
read-only and pulled only, work happens here and in `../navier-formal`, and the
goal is **Phase II everywhere**. External dependencies are allowed when they
introduce no axioms beyond Mathlib's.

**Starting state, measured not assumed.** The formal repository holds twenty
Lean files with roughly 238 proved theorems. A census of the sources finds
**exactly one real `sorry` in the whole repository**, the deliberate Palomar
placeholder in `Challenge.lean`, and **no axioms at all**. Two earlier apparent
`sorry`s and one apparent axiom in `Interpolation.lean` were backtick-quoted
words inside docstrings asserting the module is clean, which it is.

**Phase II frontier, from `docs/verification-status.md`.** Already Phase II
complete and needing no literature input: the norm-scaling half of
`prop:scaling`, including the critical `L^3` invariance and the two scalar
remarks of its proof, and `prop:ode`. Everything else is paper only:

| Target | State | Assessment |
|---|---|---|
| `prop:energy` | paper only | tractable; integration by parts is already in `IBP.lean` |
| `prop:scaling` PDE half and `eq:L4L3` | paper only | tractable; chain rule against the existing dilation machinery |
| `prop:pressure` | supporting lemmas only | tractable; the regularization, gradient-norm and density bridges exist, leaving the integral identities and a dominated-convergence limit |
| `sec:quotient` results | objects only | needs strict convexity and reflexivity of `L^3` for existence and uniqueness of the minimizer |
| `prop:enstrophy` | paper only | needs a Gagliardo–Nirenberg input |
| `prop:lowpressure` | paper only | needs Littlewood–Paley or Bernstein; the likeliest place an external dependency earns its keep |
| `thm:conditional` | paper only | assembly, once the above land |
| `thm:continuation` | paper only, imports ESS and GKP | **the one genuine obstacle**; see below |
| `Challenge.lean` surface | placeholder | the Palomar deliverable |

**Where "Phase II everywhere" meets a real wall, stated now rather than
discovered later.** `thm:continuation` imports the Escauriaza–Seregin–Šverák
endpoint theorem. Phase II for that node means formalizing ESS from Mathlib,
which needs backward uniqueness for parabolic operators and is a research
programme in its own right, not a lane. The honest plan is to carry it as a
clearly labelled Phase I literature axiom with its source record, reach Phase II
on every other node, and record ESS as the single remaining literature input. If
that changes the user's intent they can redirect; nothing else is blocked by it.

**Axiom hygiene is the gate for every lane.** `#print axioms` on each advertised
theorem must return a subset of `propext`, `Quot.sound`, `Classical.choice`.
This is checked per lane and again at integration; a dependency or tactic that
widens it is rejected.


### HF29: the corridor hypothesis, attacked (obstruction lane returned, UNAUDITED)

The adversarial half of the wave returned 2026-09-06
(`hf29-corridor-obstruction.md`, 783 lines, unaudited; the proof half is still
running). Its verdict deflates the hypothesis this plan had called the most
promising structural fact on the table, and corrects my own framing of it.

**It cannot be refuted, and that is a theorem rather than a failure.** By
Proposition R1 a refutation requires exhibiting a finite-time singularity, so
the hypothesis is unfalsifiable here unless the Clay statement is settled
negatively. The honest adversarial verdicts available were therefore "not
derivable" and "instantaneously false", and the lane obtained both.

**Three constructions failed, each instructively.** Exact discretely
self-similar blowup — the natural candidate, and the one this plan named when
opening the wave — is **self-excluding**: the distance is scale-invariant, so
under exact self-similarity it is log-periodic, but so is the critical norm, and
a log-periodic critical norm is bounded, contradicting the continuation theorem.
Two by-products fall out: any such profile is *forced* to sit at or above the
upper wall, and an exactly self-similar singularity would **satisfy** the
hypothesis rather than refute it. Our own audited countermodels from HF26 and
HF27 likewise sit on the proof side: the HF26 audit already established that its
curve is forced above the wall at every time, so the corridor is empty along it.
And the crossing function from the HF24 audit cannot be adapted, since its
oscillation decays and a convergent distance forces the hypothesis outright.

**Two attacks succeeded.** An explicit scalar countermodel satisfies all
fourteen enumerated audited relations, including the coercivity of HF18-A and a
new strong-convexity link, while having finite maximal time and a corridor
accumulating at it; it was checked on a canonical instance and six hundred
randomised constant sets with no failures. So the hypothesis is **not derivable
from the record's scalar closure**, and its one open escape is the same one
HF22-C named, the actual equation. Second and sharper: **the instantaneous form
of the hypothesis is false.** For every viscosity, parameter, energy and bound
there is a divergence-free Schwartz field sitting in the corridor with arbitrarily
large enstrophy, built from a dilation-pinned field off the nonlinear-Hodge class
plus a high-frequency solenoidal packet. Taking it as datum makes time zero a
corridor time on an actual trajectory. **The corridor condition therefore carries
no upper information about the enstrophy at all**, which answers the HF24-A
lane's own next question negatively and means its constant is not effectivisable,
so the crossing count it feeds can never be made computable.

**The decisive structural point.** The hypothesis is equivalent to the corridor
being relatively compact in the lifespan, so its constant is always just a
maximum over a compact subinterval. **It is not an estimate**, and by the HF24-A
lane's own remark, even proving it closes no part of the target.

**The parameter question is settled and is a red herring.** The hypothesis is
monotone in its free parameter, and in the blowup branch reduces to a lower bound
on the inferior limit of the scaled distance: for all parameters it is the bound
at the viscosity, for some it is the bound at half the viscosity. The record
forces only the *superior* limit. Lane and audit agree on the operative
one-parameter reading and both are correct. The band's location is
scaling-invariant and not an artifact; only its width is free, with an interior
optimum at one quarter.

**The reframing the lane recommends, and this plan adopts pending audit.** State
the target without the parameter: if the maximal time is finite then the inferior
limit of the scaled distance is at least the viscosity. That is exactly the
upgrade of a proved superior limit to an unproved inferior one at the same level.
One tension recorded: sharpening the transport constant widens the Lyapunov range
but strictly *strengthens* the hypothesis.



## Current paper task: dissipation-clock suffix (2026-09-06)


This dated entry and the live YAML supersede older read-only/signed-only
workflow paragraphs for this task. The user explicitly requested paper proof
work, main-document updates and commits/pushes in both private repositories,
including unsigned commits. Ongoing formalization stays authorized and its
phase fields are unchanged; this task does not claim Phase I or II completion.

The paper component `sections/dissipation_clock.tex` derives
`Y'+nu Z <= (4 S^3/(3 nu^2)) D3 Y`, hence a uniform cubic-dissipation budget
continues the original branch directly through the nonendpoint pair `(3,9)`.
Strict pressure absorption then gives exponent
`4 S^3 (X0+3A)/(9 (1-theta) nu^3)`. A single finite first-crossing barrier
also suffices; in particular a logarithmic deficit can replace a constant
fractional margin. The previous `(4,6)` suffix is not the shortest route.

These are full written derivations, author-checked and independently unaudited.
The graph records them as a separate pending supplement, NOT a promoted node.
The accepted graph and all open/terminal kinds stay unchanged. The bare
critical-norm continuation theorem still retains ESS; the strict-pressure
suffix does not. The old claim that ESS is unavoidable for every route to a
conditional theorem must not guide implementation of this alternative.

The actual mathematical target remains an arbitrary-data producer, uniform
to a putative endpoint. The absolute-pressure attempt only gives growth of
order `B^(3/2)` and does not establish the needed signed deficit. The finite
barrier's existential formulation is again equivalent to continuation, not
a new proof of it. Full details and audit questions are in
`research/evidence/2026-09-06-dissipation-clock.md`.

Next substantive gate: independently reconstruct the dissipation-clock
component, then derive a signed pressure estimate from the vector equation
rather than assuming a critical budget. Do not report main-document builds,
regression checks, or this new sufficient condition as closure of NS-R3.

## Defect extensions: spatial interval and quantitative no-separation (2026-09-06)

The current paper task has produced full component proofs in
`navier-paper` `878dcff0d72c9b94e9bb344a0c8a96bf8fc37a19`, source
`sections/defect_extensions.tex`. These are author-checked and independently
unaudited; the separate candidate metadata does not promote graph nodes.

A uniform measurable-coefficient contraction now proves an unweighted
estimate `||sigma||_r <= A_r ||grad u||_r` on a fixed open interval around
2, for solenoidal H1 data with the additional Lr gradient hypothesis.
The proof handles the zero set without differentiating the unit direction,
uses the trace-free Hessian norm sqrt(2/3), and identifies the same Neumann
series in L2 and Lr. The sharp old L2 estimate is retained. This partially
answers the manuscript's beyond-L2 question; no all-exponent weighted
Calderon-Zygmund estimate is asserted.

The direct quotient clock is
`Y'+nu Z <= (4 S^3 C9^3/(3 nu^2)) D_Q Y`. Combining it with the accepted
HF25 inequality and energy gives, with
`Astar=8 S^3 C9^3 Q0/(3 nu^3)` and
`Lambda_sigma=C_sigma nu^-3 integral ||sigma||_2^4`,

    integral_0^t Y^2 <= E0 Y0/(2 nu) exp(Astar exp(Lambda_sigma(t))).

Together with the old reverse inequality, this excludes finite fourth-power
defect integral with divergent squared-enstrophy integral on an actual
branch, including its full lifespan. It supplies a nonendpoint suffix,
without ESS or any comparison of D_Q and D3. The lead was already identified
in the HF26 audit; the explicit proof and constants are now supplied.

This entry supersedes the historical claim that the separation is unsettled
in both directions, subject to independent review. It also corrects the
old implication wording: a condition implied by a classical gradient
condition is not thereby 'not weaker'; the new actual-branch reverse
implication requires its own proof. A graph transcription saying ninth
power of the L9 norm is corrected to the cube, as in its existing source.

The arbitrary-data producer remains absent. Spatial near-2 regularity does
not upgrade the energy-level square time integral to a fourth power; the
new enstrophy bound explicitly depends on that unknown fourth power.
Next substantive gate: audit these components, then derive the required
signed spacetime estimate from the vector equation. Formal phase fields,
privacy, and every open/terminal graph kind are unchanged.

Evidence, source checks, failed closure and independent-review obligations:
`research/evidence/2026-09-06-defect-extensions.md`.


## Conformal moment component: spatial blockers resolved for the branch (2026-09-06)

Frozen paper proof: `navier-paper` `464a13d1c99318431cba1ed5d954528d1a31c95b`,
`sections/conformal_moment.tex`. Status: author-checked, independent audit
pending; no graph node or formal result is promoted.

Conformal pullback of one-forms is an L3 isometric involution preserving the
closed gradient cosets. Thus `w(Ku)=K w(u)`. Applying the accepted div-curl
estimate to `P K u`, then Hardy, proves `w,q in H1` and `sigma in L^(3/2)`
whenever `u in H1` is solenoidal and `|x| grad u in L2`. The projection is
essential: inversion does not preserve solenoidality or the NS equation.
The proof also controls `|x| grad w` and `|x| sigma` in L2 without assuming
w in L2 at any earlier step.

The extra hypothesis holds at every classical time for Schwartz data.
With `M=|| |x|u ||2^2` and `W=|| |x|grad u ||2^2`, bounded radial weights
and the actual equation give `M(t)+2nu integral W <= L_H^2`, with explicit
`L_H` depending only on viscosity, horizon, initial energy and initial second
moment. A separate local differentiated estimate proves pointwise W
finiteness; only the integrated budget is claimed uniform at Tstar.
Combining the spatial result with energy gives input-only time-square
budgets for w in L2, weighted sigma in L2, and sigma in L^(3/2).

This supersedes the old unproved spatial-membership statements for the
Schwartz-data branch, not for every bare H1 snapshot. The new time-space
pair `(2,3/2)` for the defect is supercritical, not on the critical line.
The explicit self-similar non-solution diagnostic satisfies the finiteness
budgets and the energy identity while its fourth-power L2 defect integral
diverges. It refutes only that inference, not the PDE target.

Next mathematical gate: independent audit of the conformal/moment component,
then use additional vector-dynamical information to establish the critical
temporal producer. HIGH-PRESSURE, HIGH-STRAIN, DEFECT-L4 and NS-R3 remain
unproved. Do not repeat the two spatial questions as unresolved on the
selected branch, and do not report their resolution as global regularity.
Formal phases, the privacy boundary and all graph node kinds are unchanged.
Full derivations, source checks and audit obligations are indexed in
`research/evidence/2026-09-06-conformal-moment.md`.


## Signed defect: exact cancellation and one-sided missing-bound target (2026-09-06)

Frozen source: `navier-paper` `a14114b8527630a469e7afdea1d2ec53bacfe8f5`,
`sections/signed_defect.tex`. Status: author-checked; independent audit
pending. Evidence: `research/evidence/2026-09-06-signed-defect.md`.

The cutoff identity `integral sigma |w|^3 = 0` gives
`K = -integral V^T S(u) V = integral V^T B0 V`, where
`B0=(R_i R_j sigma)+sigma I/3`. Trace-free algebra gives the direct bound
`|K| <= (2/3) ||sigma||2 ||w||6^3` and improves the defect Gronwall
coefficient from `(81/32) C6^4 a0^3` to `a0^3/2`, `a0=9 C_S^2/8`.
The exponent four remains; no critical estimate follows just by shrinking
this coefficient. These proofs do not need the moment extension.

A one-sided variational rate is the positive part of the supremum of
`[integral psi^T B0 psi - (4 nu/9) integral |grad psi|^2]/integral |psi|^2`.
The source proves its measurability, finiteness and exact bounds. It gives
`Q'+nu D/2 <= 3 b_nu Q` and hence the explicit missing-integral consumer

    integral_0^t ||sigma||2^4
    <= E0 Y0/(32 nu) exp(Astar exp(3 integral_0^t b_nu)),
    Astar = 8 C_S^3 C9^3 Q0/(3 nu^3).

The last implication uses the separately pending direct quotient clock.
An integrable amplitude cutoff for the positive largest eigenvalue of B0,
with an L^(3/2)-small excess tail, is also sufficient. Both form and
amplitude clocks are critical. No eigenfunction or spectral theorem is
assumed, and no theorem about the velocity strain is applied to B0.

**Next positive producer:** derive an input-only bound on
`sup_{t<min(H,Tstar)} integral_0^t b_nu(B0(s)) ds`, or an explicit integrable
amplitude certificate, from the vector equation. The existing upper bound
`b_nu <= a0^3 ||sigma||2^4/(6 nu^3)` runs in the wrong direction to supply
that producer from energy. The evidence records the exact stopping point
and a bare-budget scalar diagnostic, not a singular PDE solution.

This replaces the active task with signed-form evolution and independent
component audit; it does not declare the earlier moment audit complete.
The terminal claim and HIGH-PRESSURE, HIGH-STRAIN and DEFECT-L4 stay open.
All 29 existing graph nodes and formal statuses are preserved; the new
result is recorded only as a pending supplement. A classical-gradient
bound remains a legitimate research target, not an "unusable" route merely
because it would suffice for continuation.


## Speed-shell checkpoint and remaining temporal producer (2026-09-06)

Frozen paper source: `5643f3e53ce837896fdd69247c3972ba4180ebfa`,
`sections/speed_shell.tex`; evidence:
`research/evidence/2026-09-06-speed-shell.md`. Author-checked, independently
unaudited; no graph node or formal phase is promoted.

The defect now has a proved zero average on every positive speed shell,
not only against the cubic speed. Removing all L2 functions of speed from
the scalar signed-work field yields a measurable delta in [0,1] and the
bound `|K| <= (2/3) delta ||sigma||2 ||w||6^3`. Finite shell averages give
explicit residual upper bounds. Scalar corrections `h(|w|)sigma I` leave
signed work unchanged, giving a measurable form infimum beta<=b_nu(B0).
The minimum rate
`c_nu=min(3 beta, a0^3 delta^4 ||sigma||2^4/(2 nu^3))` therefore suffices;
its integral L_c gives the explicit original-defect consumer
`integral ||sigma||2^4 <= E0 Y0/(32 nu) exp(Astar exp(L_c))`.
The final implication still uses the independently pending quotient clock.

The missing positive producer is an input-only bound on L_c uniformly below
min(H,Tstar), or a bound on one of the earlier sufficient rates. This has
not been obtained. Replacing delta by one returns the original unknown;
the energy/moment comparison does not upgrade its time exponent. The speed
projection and minimizing correction must not be differentiated without a
new regularity theorem. Critical scaling is unchanged. The source provides
full spatial proofs and a conditional suffix, not a completed Navier--Stokes
proof or a strict separation of actual-branch finiteness conditions.

Next mathematical work: independently audit this and predecessor components,
then derive an actual vector-evolution bound exploiting the shell cancellation.
HIGH-PRESSURE, HIGH-STRAIN, DEFECT-L4 and NS-R3 remain open. Preserve all
existing formal authorizations, privacy restrictions and historical evidence.


## Natural-variable dynamics checkpoint (2026-09-06; audit pending)

Frozen paper source: `a9993cccee0f9544c49f9c98524c6c4af4c0e080`,
`sections/shell_dynamics.tex`; evidence:
`research/evidence/2026-09-06-shell-dynamics.md`. This is an author-checked
component derivation, not an independent audit or an arbitrary-data bound.

For every gradient increment g the natural variable V=|w|^(1/2)w obeys
`||V1-V0||2^2 <= (9/8) integral (|w0|+|w1|)|f1-f0+g|^2`.
Consequently V is W^(1,infinity) into L2 on each compact classical interval,
with pressure-free bound
`||V_t||2^2 <= (9/4) integral |w| |nu Delta u-(u dot grad)u|^2`.
Finite smooth speed features and a positive ridge penalty then have an
exact absolutely continuous residual evolution, in L3--L^(3/2) and L2
pairings. This justifies a regularized temporal calculation that the
previous checkpoint could not assume. It does not differentiate the full
moving projection. The source proves the fixed-regularization estimates
and the pointwise-in-time monotone approximation separately.

**Next positive producer:** control the explicit residual-evolution drivers
uniformly below min(H,Tstar) and control the losses in feature refinement
and vanishing ridge penalty, or find a different signed time estimate.
The weighted acceleration bound contains an uncontrolled nonlinear and
second-derivative term; the current energy budget does not close it.
No input-only bound on L_c or the fourth-power defect integral is supplied.
Independent audits of this and the predecessor components remain required.
All 29 existing graph nodes and formal statuses are unchanged; HIGH-PRESSURE,
HIGH-STRAIN, DEFECT-L4 and NS-R3 remain open. This checkpoint replaces the
active task, not the historical record of prior unsuccessful approaches.

## Corotational material checkpoint (2026-09-06)

The new source `sections/material_response.tex` in `navier-paper`, frozen at
`2959003806907fa4742518bff741f24c592921e6`, proves a strong moving-metric
response for the cubic gradient minimizer. A cubic little-o remainder, not
just the earlier big-O estimate, justifies the natural-variable derivative
in L2 including velocity zeros. No unweighted L3 derivative of w is assumed.

Pullback by the actual volume-preserving flow gives, with N=DJ(w),
P the fixed weighted gradient projection, L=I-P and S the velocity strain,

    U=(partial_t+u dot grad)V-Omega V
      =N[L(nu Delta u-Sw)+P(I-n tensor n/2)Sw].

The two weighted responses are orthogonal and their squared action obeys
`action <= ||U||2^2 <= 9 action/8`. Its explicit upper bound is
`(9/2)nu^2 integral rho|Delta u|^2 +(81/16) integral rho^3 ||S||op^2`.
This removes pressure, bulk transport and rigid rotation from the driver,
not strain or diffusion. The material finite-ridge residual equation keeps
the complete Riesz/rotation commutator and its correct dual-space pairing.
The accepted quotient balance is recovered exactly as a consistency check.

The endpoint bound is still unproved. Weighted acceleration, strain action,
the full commutator and uniform refinement losses are not controlled by
the available energy/moment budgets. Differentiating dissipation did not
establish the signed estimate needed to pay for this action. No heat
convexity or differentiation of a moving weighted projection is assumed.
See `research/evidence/2026-09-06-material-response.md` for the complete
source trail, attempted closure, author checks and independent-audit list.
This and predecessor supplements remain independently unaudited. No main
graph node or formal status is promoted; NS-R3, HIGH-PRESSURE, HIGH-STRAIN
and DEFECT-L4 remain open.

Next positive producer: exploit the exact combined action or derive a
signed temporal estimate for the complete residual on actual trajectories.
Do not replace it by independent absolute estimates without checking the
lost cancellation. Independently audit the component before any promotion.
The new active task replaces the last driver target, not historical work.
