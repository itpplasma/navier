# Navier–Stokes programme

```yaml
terminal_claim: NS-R3
checkpoint: CP1
phase: paper-proof-first
phase_i_status: authorized-2026-09-05-deferred-until-full-paper-proof
phase_ii_status: authorized-2026-09-05-not-started
paper_status: cp1-paper-proof-complete-conditional-on-one-open-estimate
active_task: HF24-modulus-of-continuity
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


### HF20: a local harmonic-strain sign test (arrived 2026-09-06, UNAUDITED)

A typeset candidate arrived on the work capture surface rather than as a
repository note, written against research `30d715d` and paper `39ccb66`. It
is transcribed into `research/evidence/hf20-harmonic-strain-test.md`; the
PDF is frozen by SHA-256
`4be9a53b244ba385e7b1e18bf02bee9b10db44a4329438612742ac32b7e15009` at
`~/Nextcloud/navier/navier-hf20-candidate-proof.pdf` and is not committed,
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

1. ~~Audit HF20~~ **done**: REPAIR, repair applied.
2. ~~Integrate the audited outcome~~ **done**: `rem:no-monotone` in the
   manuscript at `bdad8a1`, the HIGH-STRAIN review text in the graph, and the
   regenerated map.
3. ~~Apply the three HF19 audit repairs~~ **done, 2026-09-06.** All three
   returned REPAIR with no invalid mathematics, and each note now carries its
   audit status, the prescribed replacement text, and a weakened or removed
   version of every claim the audit found unsupported. Two by-products are
   recorded rather than hidden: the temporal-normal-form note's transfer
   corollary does not deliver `hyp:absorption` as the manuscript states it,
   since it carries a Gronwall term and no fixed `theta < 1`, and its
   Section 5 numerics are not reproducible because the probe script lived
   only in session scratch. The note records both as parsable
   `- needs review:` lines rather than quietly dropping them.
4. ~~Apply the two HF21 note repairs~~ **done**. **Audit HF23**, which if it
   stands discharges hypothesis (H1) and would let the quotient section drop a
   standing hypothesis. Then **attack (G)** (wave HF22 running):
   `int_0^tau ||q(t)||_3 D_3(w(t)) dt <= A_input(nu,u_0,H)` uniformly for
   `tau < min(H,T_*)`. By the audited normalisation this single joint
   spacetime statement about the pair (distance to the nonlinear-Hodge
   class, dissipation) is the whole of the frozen gap with contraction
   factor zero, with no Gronwall term and no frequency cutoff. It has the
   scaling of the quotient itself, so an input-only right side is
   scaling-consistent. Three sub-questions, in order: (a) is the quotient
   dissipation at most the velocity dissipation at fixed time, which is
   minimizer-free and scaling-consistent on both sides and whose affirmative
   deletes a term from the distance balance; (b) is the nonlinear projection
   Lipschitz at points of the nonlinear-Hodge class, noting that Lipschitz
   REFUTES an exponent above one rather than permitting it; (c) is any
   input-only bound available for the dissipation restricted to the good set
   where the distance is small, the only good-set statement that survived
   audit.
5. **Continue Track B** on whatever (G) leaves. After HF18-A,
   HF19 and HF20 the excluded classes are: size bounds in `Q` and `D_3` by
   scaling, temporal normal forms with correctors in the computed classes,
   the difference functional as a producer, universal monotonicity of the
   quotient, and instantaneous energy-only absorption of the transport term.
   Wave HF21 is running on two of the questions this leaves. What remains open is a genuine
   cancellation inside the transport term, the time-integrated sign
   structure along trajectories that cross the nonlinear-Hodge class, and
   the weighted Calderon-Zygmund and `L^2`-projection questions recorded in
   HF18-B.
5. **Formalization stays deferred** until the full paper route is proved and
   audited, per the user's re-sequencing of 2026-09-05.


### HF21: shifted-Hodge regularity and the crossing sign structure (UNAUDITED)

Two lanes, both delivered 2026-09-06, **both unaudited**; nothing is promoted
and the manuscript is untouched. Their audits are the next action.

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


### HF23: an unweighted div–curl estimate for the minimizer (arrived 2026-09-06, UNAUDITED)

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

**Held back.** The Scope B spacetime exclusion is not yet in the manuscript:
its audit requires four repairs first. That is the one outstanding integration
item from HF23.


### HF22: attacking (G) and its three sub-questions (UNAUDITED)

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
