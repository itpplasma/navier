# CP01 completeness critic: what is still missing for CP1, where the lanes disagree, and what nobody owns

MODE: REVIEW (proof-audit / math-frontier discipline), cross-lane critic.
Date: 2026-09-05. Owner file: this note only; nothing else was edited.
NS-R3 remains OPEN. HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION remain
open. Nothing here proves, weakens, or promotes any claim; contradictions are
listed for the controller, not resolved (where a primary source was
re-inspected, the evidence is recorded and labelled "critic verification").

## 0. Inputs and what was independently checked

Read in full: `/home/ert/proj/navier-paper/main.tex` (HEAD `1ad73c2`, 562
lines), `PLAN.md`, `docs/proof-graph.yaml`, `docs/proof.md`, and the six lane
files `cp01-{manuscript-obligations,literature-statements,mathlib-coverage,
lean-statement-design,quotient-section-structure,palomar-checklist}.md`
(all untracked in git at research HEAD `fd1c20e`). Spot-read:
`hf17-review-quotient-functional.md` (lines 60–150), `hf17-quotient-
functional.md` (grep), `hf18-hodge-regularity.md` and
`hf18-divergence-speed-link.md` (headers and claim lines; both untracked, both
dated 2026-09-05 15:15–15:16), `AGENTS.md`, `research/verify.py` output (PASS,
13 records).

Critic verifications performed (all directly inspected unless marked):

| Item | Source | Result |
|---|---|---|
| Tao 2013 Corollary 5.2 and 5.8 | arXiv:1108.1165v4 PDF, pages 30–31 and 33–38 (rendered page images read) | Cor. 5.2 (p. 31) is **periodic** (`R³/Z³`, tuples `(…,1)`), followed by "A similar statement holds with 'H¹ data' and 'H¹ mild solution' replaced by 'smooth data' and 'smooth solution'". Cor. 5.8 (p. 38) is the **R³** "Maximal Cauchy development" for H¹ data, with the "incomplete mild H¹ solution `(u,p,u₀,f,T_*^-)`" definition immediately above it and Remark 5.9 citing [13] (ESS) for L³ blow-up. Theorem 5.4 (pp. 33–34) and the parenthetical in the proof of (iv) ("it would have sufficed to have `u₀ ∈ H^k_x(R³)` and `f ∈ C^j_t H^k_x(R³)` for all `j,k ≥ 0`") read exactly as both lanes transcribe. Prop. 5.6 (p. 35, "Almost regularity", R³, homogeneous H¹ mild solutions smooth on `[τ,T]×R³`) is also present. |
| lean4export tags | GitHub API `leanprover/lean4export/tags` (2026-09-05) | v4.33.0-rc1, v4.33.0-rc2, v4.33.0 (`15f6055e…`), v4.34.0-rc1, v4.34.0-rc2; **no v4.33.1**. Palomar lane's PAL-TOOLCHAIN stands. |
| formalization.yaml v0.4 schema | `mathlib-initiative/formalization.yaml`, `schema/v0.4.schema.json` (metadata-only: summarised by the fetch tool) | `sources[].type` is a **free string** with examples "article, book, web post, folklore, conversation, original-proof, …"; `sources[].relationship` enum `["", formalizes, adapts, independently-proves, background, other]`; `sources[].authors` and `sources[].license` permitted; `review.status` required; `project.description` **not** schema-required. |
| PalomarSubmission commit `c605f23` "Isolate the canonical Challenge module namespace (#132)" | GitHub API commit (metadata-only) | Verifier-internal: the protected Challenge is republished under an unpredictable per-run verifier-owned top-level alias. No new submitter-facing naming rule was found in the quoted patch lines. Resolves the Palomar lane's PAL-NAMESPACE-PENDING as far as the summary shows; raw patch not read. |
| Mathlib checkout | `/home/ert/proj/stafford38/.lake/packages/mathlib`, `git describe` = `v4.33.1` | Greps confirm: no `def divergence`/`def curl`; no `Clarkson`; no `heatKernel`; no `UniformConvexSpace (Lp …)` instance; no `eLpNorm` in `Analysis/Convolution.lean`; `SchwartzMap.denseRange_toLpCLM` at `Basic.lean:1383`; `Lp.fourierTransformₗᵢ` at `LpSpace.lean:50`; `integral_bilinear_fderiv_right_eq_neg_left_of_integrable` at `IntegrationByParts.lean:195`; `eLpNorm_le_eLpNorm_fderiv_of_eq` at `SobolevInequality.lean:600` with `HasCompactSupport`; `Analysis/Calculus/Rademacher.lean` exists. The mathlib lane's headline absences and hits are reproduced. |
| `/home/ert/proj/navier-formal` | local git, 3 commits by the owner, 2026-09-05 14:49–15:09 | **Exists**, contrary to the lean-design and Palomar lanes ("not created", "to be created"). Toolchain `leanprover/lean4:v4.33.1`; `lakefile.toml` `rev = "v4.33.1"` (tag) resolved in `lake-manifest.json` to `0df444a360eaa60ab8c11dca51a86af692955474`; `Challenge.lean` holds one labelled placeholder with `sorry`; `NavierFormal/{Basic,Scaling,Ode,InterpolationMismatch,Regularization,NormGradient}.lean` (1,020 lines) with 70 declarations reported axiom-clean in `docs/verification-status.md` (CP03a: `prop:ode`, `prop:scaling` norm half; CP03b: `r_ε`/`H_ε` calculus and a.e. `∇|u|` lemmas via Rademacher under `LipschitzWith`); `docs/paper-lean-specification.md` table is **empty ("(pending)")**; `formalization.yaml` present with `sources[].type` values `manuscript`, `book chapter`, `article`, MSC `35B65`, `review.reviewers: ["none"]`. |

Not re-inspected here: GKP Theorem 4 (both lanes agree and record direct
inspection), ESS, Kato, Fefferman, Grafakos, Hartman, Lieb–Loss, PalomarPolicy
CONTRIBUTING.md.

## 1. Facts on disk that the lanes did not see

1. `navier-formal` already exists with CP03a/CP03b integrated (see table). The
   lean-design lane's module plan proposes names (`E`, `criticalScale`,
   `scalar_obstruction`, `divergence`, `jacobianSq`) that collide with or
   duplicate existing declarations (`Space`, `dilate`, `dilateSpaceTime`,
   `scalarObstruction`, `scalar_obstruction_exists`). Its lane L0 "creates
   `Basic.lean`" is already partially done with a different abbreviation.
2. CP03b formalized exactly the `∇|u|`/Rademacher/Sobolev-representative
   route (`NormGradient.lean`, hypotheses `LipschitzWith C u`) that the
   obligations lane (P-0) and the lean-design lane (R-P0, D7) recommend
   **removing** from the paper and never encoding. `verification-status.md`
   itself lists four fidelity gaps of these lemmas (Lipschitz class bridge,
   Sobolev vs Fréchet gradient, operator vs Frobenius norm, divergence
   identity). Whether these 42 declarations stay as supporting lemmas or are
   retired is undecided.
3. `docs/paper-lean-specification.md` is empty while 70 declarations are
   integrated. `navier-formal/AGENTS.md` says "faithfulness is a separate
   audit recorded in `docs/paper-lean-specification.md`"; no such record
   exists for CP03a/b.
4. Two untracked Track B notes `hf18-hodge-regularity.md` and
   `hf18-divergence-speed-link.md` appeared during the CP01 wave. They
   **disagree with each other**: `hf18-hodge-regularity.md` boxes
   `D_𝒬(u) = -∫A·Δu = ∫∇A:∇u = D₃(w)` (its (2.2)) and asserts
   `V = |w|^{1/2}w ∈ H¹`, `A ∈ W^{1,3/2}`; `hf18-divergence-speed-link.md`
   states "`D_𝒬 = D₃(w)` is *not* claimed" and that its use "would
   additionally require `D_𝒬 ≥ c D₃(w)`". Neither is reviewed. The quotient
   lane's rewritten section explicitly makes the non-claim "No comparison of
   `D_𝒬` with `D₃` is claimed" and "No smoothness of `w(u)` is used or
   asserted". CP1 must not absorb either HF18 claim before audit.
5. The graph's `source_revision.manuscript_commit` `d84950b…` is a commit
   object in `navier-paper` but not HEAD (`1ad73c2`); the recorded revision
   predates `sec:quotient` (obligations lane §2 item 7, confirmed).

## 2. (a) What is missing for a complete, self-contained paper proof of CP1

Ranking is by blocking weight for gate 1 (PLAN.md), after merging the lanes
and applying the critic verifications. IDs reuse the obligations lane.

### Blocking

- **C-2 — identification of the classical branch with GKP's `NS(v₀)` and
  `T*(v₀) = νT_*`.** Asserted in one sentence of `thm:continuation`. Needs:
  (a) membership of the ν-normalised classical solution in GKP's strong
  class and its Duhamel form with the normalised pressure; (b) a **named**
  uniqueness theorem covering both branches at once (Tao 5.4(iii) is
  uniqueness among H¹ mild solutions; GKP's uniqueness of `NS(u₀)` is in the
  `E_{p,q}`/`C_tL³` class and is not restated by them); (c) the case
  `T*(v₀) > νT_*`, closed by a **named** regularity/persistence theorem for
  the L³ strong solution against the H¹ blow-up alternative. **No lane
  pinned (b) or (c)** (obligations lane UNIQ-L3, PERSIST-L3 "not
  inspected"; literature lane §4.2 declares FLRT "not needed" and marks it
  [MO]; see contradiction K3). This is the first gap for gate 1.
- **Q-block — `sec:quotient` as labelled propositions.** Now **drafted in
  full** by `cp01-quotient-section-structure.md` §4 (≈860 lines of LaTeX,
  compiled on a scratch copy to 16 pages). It changes the proof route
  (pointwise cubic inequalities and a Cauchy minimizing sequence instead of
  reflexivity/weak lsc/strict convexity; Fourier-in-L² heat generator instead
  of semigroup domain theory; coercivity restricted to solenoidal L²∩L³). It
  is **unaudited** (its own O7) and not integrated. Critic spot-checks of
  `lem:cubic-pointwise`, `lem:quotient-minimizer`(d), the remainder algebra
  in `prop:quotient-derivative` (constant 10, exponent 4/3), the index
  contraction in `lem:quotient-transport`, the constant `M_L = 3(1+C_ℙ)‖∇ψ‖₂
  2^{5L/2}‖u₀‖₂`, and the Gronwall constant in `eq:cp-M` found no error.
  This is a spot-check, not the required independent audit.
- **L-1 — the R³ maximal development and its uniqueness class.** Downgraded
  from the obligations lane's "blocking; not in the cited Tao theorem" to
  **major**: Tao Cor. 5.8 (arXiv p. 38 = APDE pp. 56–57) states the R³
  dichotomy (critic verification). What remains manuscript-owned: the
  passage from Cor. 5.8's per-`T` dichotomy to a single `T_*(u₀) ∈ (0,∞]`
  (or the equivalent restart argument from 5.4(i)–(iii)), the statement of
  the uniqueness class (H¹ mild = classical with `u ∈ L^∞_tH¹ ∩ L²_tH²` and
  normalised pressure, via Cor. 4.3), the H¹ blow-up alternative, and the
  ν-normalisation applied **at this point** (the manuscript introduces
  `eq:nu-normalization` only in §5). `premise:local` must cite Thm 5.4
  **and** Cor. 5.8.

### Major (routine, but unwritten)

- **C-0** restate `thm:continuation` as "`T_* < ∞ ⟹ sup_{t<T_*}‖u(t)‖₃ = ∞`"
  (the current conclusion "extends beyond `T_*`" is ill-formed for a maximal
  time); replace `ess sup` by `sup` with the justification `u ∈ C([0,T_*);L³)`.
- **C-3** `thm:conditional`: replace "persistence" by Tao 5.4(iv) on every
  `[0,T]`, `T < T_* = ∞`, plus the lemma "`∂_t^j u, ∂_t^j p ∈ L^∞_tH^k` for all
  `j,k` ⟹ `u,p ∈ C^∞([0,T]×R³)`"; state that the pressure is Tao's
  normalised pressure. **The joint-smoothness lemma is written in no lane**
  (the quotient lane's `lem:sobolev-classical`(a) gives only the spatial
  embedding at fixed time).
- **P-1** fix the Fourier/Riesz convention; prove `R_iR_j(u_iu_j) =
  −Δ^{-1}∂_i∂_j(u_iu_j)` = Tao's (9); obtain `p ∈ L²∩L^∞` from Tao (iv)
  (no Calderón–Zygmund) or cite CZ exactly. Literature lane §7.3 verifies the
  symbol identity; quotient lane O6 the same. Text still absent from the
  manuscript.
- **P-2, P-3** display every cutoff/ε limit in `prop:pressure` with the exact
  memberships; state the balance in integrated form (all that
  `eq:pressure-consequence` uses).
- **F-1** `prop:lowpressure`: fix the Littlewood–Paley convention (real,
  even; homogeneous vs inhomogeneous — see K8), display
  `‖m_J‖_{L¹_ξ} ≤ (4π/3)2^{3(J+1)}`, `‖K_J‖_∞ ≤ ‖m_J‖₁`, the convolution
  representation for `f ∈ L¹∩L²`, measurability of `L_J`.
- **E-1, N-1, S-1** exact memberships and density/Plancherel arguments in
  `prop:energy`/`prop:enstrophy`; source for `‖u‖₆ ≤ C‖∇u‖₂` on `H¹(R³)`;
  the Gagliardo–Nirenberg step.
- **X-1** the existential-equivalence paragraph after `hyp:absorption`: make
  it a proposition or a remark; its converse needs `‖p_{>0}‖₃ ≤ C‖u‖₆²`. Not
  in PLAN's CP1 table, not among the Lean theorems T1–T20 (K-unowned U3).
- The quotient lane's `rem:highstrain-scope` reproduces the same
  equivalence for `hyp:highstrain`; both must be consistent with the graph
  note on ABSORPTION.
- **Proof boundary section** must name `hyp:highstrain` and
  `prop:quotient-conditional` (quotient lane §4 end). The abstract's "We prove
  the energy, scaling, interpolation, and enstrophy estimates in detail" is
  not yet true at gate-1 standard (only `prop:ode` is complete; obligations
  lane §1).

### Minor

P-0 (define `D₃`, `P₃` through `(∇u)ᵀu`, no `∇|u|`), S-2 (meta-clause in
`prop:scaling`), disambiguate "persistence", drop or demote Kato 1984,
`def:target` typeset as Theorem.

## 3. (b) What is missing for a faithful Phase I statement surface

The lean-design lane supplies a complete Mathlib-only surface (definitions
§2, T1–T20, eleven axioms, 19 risks). What is missing or wrong relative to
faithfulness:

1. **Axioms that are not literature.** `classical_branch_identification`
   (labelled "NOT literature" by the design itself), `leray_projection_L3`
   (composite: Riesz L^p bounds + the project step Q-4 "ℙu = u for every
   distributionally solenoidal L³ field"), `bernstein_lowpass` (provable in
   three lines, quotient lane `lem:lowpass`), `heat_generator_L3` (no primary
   source located; literature lane S5 [MO]/[REC]), `divfree_flow`. Under
   `navier-formal/AGENTS.md` ("A construction the manuscript performs itself
   is never relabelled as a literature axiom") and the programme rule "no
   unproved project step is literature", these cannot survive gate 2 as
   axioms. Each needs either a paper proof (CP02) or a pinned source.
2. **Axiom over-strength relative to the paper.** `heat_generator_L3` asks
   the generator limit for `v ∈ L³ ∩ C²` with `Δv ∈ L³` (true only through
   `W^{2,3}` regularity, i.e. CZ theory), whereas the paper needs and the
   quotient lane proves it for `u ∈ H^m` via L² Fourier plus L³ strong
   continuity. `leray_projection_L3` asks `Pu = u` on all of solenoidal L³
   (the L³ Helmholtz decomposition, which the quotient lane explicitly makes
   "not a dependency") whereas the paper needs it on `L²∩L³` where it is a
   Plancherel fact. The T12/T19 hypothesis `hP1 : ∀ u, IsSolenoidalL3 u → P u
   = u` inherits the over-strength.
3. **Axiom under-strength.** `divfree_flow` gives `Φ` with `ContDiff ℝ 1
   (Φ s)`, measure preservation and the group law, but not the variational
   equation `∂_sDΦ_s = Db(Φ_s)DΦ_s` nor the expansions
   `|DΦ_s − I − sDb| ≤ Cs²`, `|DΦ_s^{-T} − I + sDbᵀ| ≤ C's²` that
   `lem:quotient-transport` uses. T18 is not provable from the axiom as
   written.
4. **Tao (iv) remark encoded as theorem.** `local_existence` and
   `tao_regularity` take `AllSobolev u₀` (H^k for all k) and conclude
   `SmoothThroughZero ∧ TaoRegular`; Tao's theorem statement requires
   Schwartz data, the H^k version is a parenthetical inside the proof (critic
   verification p. 34), and the literature lane forbids encoding it. For CP1
   it is avoidable: apply (iv) once to the glued H¹ mild solution on `[0,T]`
   whose datum is the original Schwartz `u₀`; restart steps need only (ii)
   and (iii). The quotient lane's `rem:tao-class` also leans on the remark.
5. **Hidden dependency in `gkp_theorem4`.** `IsMaximalL3Mild` is a
   `C([0,T);L³)` Duhamel predicate with maximality. GKP define `NS(u₀)` in
   `E_{p,q}(T)` and obtain the `C_tL³` characterisation by a remark citing
   their [9]; "the" solution in the `C_tL³` class presupposes uniqueness
   there (FLRT 2000, [MO]). So the axiom silently imports the very
   uniqueness theorem the literature lane says CP1 does not need (K3).
   The design's own fallback (one composite axiom "GKP Thm 4 + C-2") is
   honest but not verbatim and hides C-2 inside a hypothesis — a Palomar
   "hidden material hypothesis" hazard for route A.
6. **R-CLASS unresolved.** Tao's "almost smooth H¹ solution" definition (the
   hypothesis of Cor. 4.3) was still not quoted by any lane; the four class
   fields of `IsClassicalSolution` cannot be frozen.
7. **Pressure normalisation is encoded three ways**: design D4 (`p(t) ∈ L²`
   + Poisson automatic, needing ID-P1 "L²-harmonic on R³ ⟹ 0"), quotient
   lane (`R_iR_j` as an L² multiplier on `u_iu_j ∈ H²`), manuscript/graph
   (`p = R_iR_j(u_iu_j)`), and `verification-status.md` ("`p = R_iR_j(u_iu_j)
   ∈ L²∩L³ … paper only"). One definition must be chosen for
   `Challenge.lean`; ID-P1 has neither source nor size estimate.
8. **Norm conventions.** Design D7/R-NORM demands Frobenius sums inside
   identities; the existing `NormGradient.lean` bounds use the operator norm
   of `fderiv`; the bridging lemma is unowned; `local_existence`'s smallness
   uses `eLpNorm (fderiv ℝ u₀) 2` (operator norm) where Tao uses the H¹
   norm — absorbed by the absolute `c` but must be stated.
9. **Repository sync.** Names and files in the design do not match the
   repository (§1 item 1); `paper-lean-specification.md` empty (§1 item 3).
10. **Statement-shape decisions still open**: `CriticalBound` per datum over
    all classical solutions (R-CRIT; equivalent only after uniqueness),
    `SmoothThroughZero` as `ContDiffOn … (Ici 0 ×ˢ univ)` (R-T0), `LowPassProfile`
    universally quantified (R-LP), `SobolevClass` boundedness-only (R-REG),
    T3 asserting class transport (R-SCALE). All are documented divergences,
    none is yet accepted by the controller.

## 4. (c) Phase II feasibility

1. **The lanes' Phase II totals exclude the literature theorems
   themselves.** The mathlib lane's ≈570–800 lemmas cover CZ/Riesz/Leray
   (320–480), heat (65–80), flow/Liouville (65–100), convexity (15–25 cheap
   route), Young/Bernstein/GN/etc. PLAN gate 3 says "every literature axiom
   is proved from Mathlib, or decomposed into published lemmas that are
   proved from Mathlib". For `AX-TAO-5.4`/`AX-TAO-5.8` that means an H¹
   contraction-mapping local theory with `X^k` regularity (heat semigroup on
   Sobolev spaces, Leray on `H^s`, product estimates); for `AX-GKP-4` it
   means the Escauriaza–Seregin–Šverák endpoint (backward uniqueness,
   Carleman inequalities, ε-regularity) or GKP's profile decomposition. **No
   lane estimated these**, and none of the mathlib-absent blocks even reaches
   them. Gate 3 as written has no credible size estimate; this is the
   largest unowned feasibility item.
2. Items with no estimate at all: ID-P1 (§3.7), the C-3 joint-smoothness
   lemma, the H¹ blow-up/gluing lemma, `eq:nu-normalization` transport of
   `IsClassicalSolution`, C-2 (if it is to be proved rather than axiomatised).
3. Two lanes independently recommend keeping the local theory in the
   Schwartz class to avoid a normed `H^m` (mathlib lane #16, design D5); the
   quotient lane's standing class `prem:classical-interval` is stated in
   `C([0,T];H^m) ∩ C¹([0,T];H^{m-2})` with `H^m` norms. Either the paper
   class or the Lean class must move.
4. The mathlib snapshot is fragile: `Analysis/Distribution/*` and
   `Analysis/Fourier/LpSpace.lean` are 2025/2026 single-author additions; a
   re-survey before Phase II is mandatory (mathlib lane §12).
5. External reuse candidates (Carleson `ToMathlib`, Apache-2.0, toolchain
   v4.34.0-rc2; uda-lab/leray-hopf, Apache-2.0, v4.31.0-rc2, weak-solution
   class) are recorded; nobody has assessed backport cost or licence
   attribution mechanics against `navier-formal/AGENTS.md`.

## 5. (d) Palomar registration

Standing blocking items from the Palomar lane (PAL-AXIOMS, PAL-TOOLCHAIN,
PAL-CHALLENGE-CLOSURE) are confirmed. Additional gaps found here:

1. **Toolchain conflict is live on disk**: `navier-formal` pins v4.33.1 and
   Mathlib `0df444a…`; lean4export has no v4.33.1 tag (re-verified today);
   `navier-formal/AGENTS.md` forbids bumping without the controller. A
   decision (v4.33.0 + Mathlib `db584cd6…`, or keep v4.33.1 and re-check
   tags at submission) is unowned.
2. `formalization.yaml` on disk: `sources[].type` values `manuscript`,
   `book chapter`, `article` — the Palomar lane says the vocabulary is
   closed (`paper`, `book`, `web discussion`, `folklore`, `original-proof`,
   `other`); the v0.4 schema (critic fetch) leaves `type` free-form with
   different examples. Whether Palomar's policy layer restricts it must be
   checked against CONTRIBUTING §3.2 raw text (K13). `review.reviewers:
   ["none"]` conflicts with the Palomar lane's "reviewers only for
   identifiable people/systems". `classification.msc2020` has `35B65` where
   the Palomar lane proposed `35B44`; neither was checked against the
   taxonomy snapshot. `fidelity.divergences` is a string; the design lane
   already lists 19 divergences that belong there.
3. Route B ("register only unconditional theorems") requires **proofs**, not
   axioms, of heat/flow/Bernstein/Leray-free statements before T14, T17–T20
   can be listed; the design says so. Route B's notability argument in the
   Palomar lane ("the quotient functional being a genuinely new object")
   contradicts the manuscript, PLAN and quotient lane ("no novelty …
   asserted"), and **no prior-art search for the L³ gradient-quotient /
   Helmholtz-quotient functional exists in the evidence** (K11).
4. Route A's hypothesis structure hides C-2 inside
   `LiteratureInputs.endpoint_continuation` (§3.5) — exactly the "hidden
   material hypothesis" the editorial check targets.
5. Disk: 42 GiB free at 96 %; a Mathlib `.lake` tree plus comparator,
   lean4export and nanoda builds do not comfortably fit (Palomar lane §3.1).
   `navier-formal` already has its own `.lake`; size not measured.
6. PalomarSubmission #132 is verifier-internal (critic fetch, metadata-only);
   no action, but the raw patch was not read.

## 6. Contradictions between lanes (to be resolved by the controller)

| ID | Lanes | Contradiction | Critic evidence |
|---|---|---|---|
| K1 | obligations §0.1/§1.1 vs literature §1.3 vs lean design §3.3 vs quotient `rem:tao-class` | Obligations: "Tao states Corollary 5.2 for the periodic case only; the R³ maximal development is not in the cited theorem" (L-1 blocking). Literature: Cor. 5.8 (pp. 56–57) **is** the R³ maximal Cauchy development, "Phase I must import both Thm 5.4 and Cor. 5.8 as axioms". Lean design: no Cor. 5.8 axiom; gluing proved from 5.4(ii)(iii). Quotient lane: iteration of (ii) from `u(T₁) ∈ ⋂H^k` using the in-proof remark. | Critic verification: arXiv v4 p. 31 = periodic Cor. 5.2; p. 38 = R³ Cor. 5.8 with the incomplete-solution definition. The obligations lane read only to p. 36. Open decision: axiomatise 5.8 or prove the gluing from 5.4(i)–(iii) (both are legitimate; the second avoids the remark). |
| K2 | literature §1.2 note 6 vs lean design `local_existence`/`tao_regularity` vs quotient `rem:tao-class` | Literature: the "H^k for all k suffices" sentence is a remark inside the proof of (iv), "do not encode it as part of the axiom". Lean design encodes `AllSobolev` data; quotient lane relies on it for restart steps. | p. 34 confirms it is parenthetical. Avoidable for CP1 (apply (iv) once to the glued solution with Schwartz datum). |
| K3 | obligations §1.10/C-2 (blocking; UNIQ-L3, PERSIST-L3 to be pinned) vs literature §4.2 ("CP1 does **not** need [FLRT]: the uniqueness chain runs through Tao 5.4(iii) plus GKP's own maximal-L³ solution") vs literature §8.2 ("The identification of the two branches is a real step. Severity: major") vs lean design (composite axiom `classical_branch_identification`, "NOT literature") vs `navier-formal/AGENTS.md` (no project construction may be an axiom) | Four incompatible positions on whether C-2 needs a named uniqueness/persistence theorem, and on severity (blocking vs major vs axiom). The literature lane is internally inconsistent (§4.2 vs §8.2). | Tao 5.4(iii) is uniqueness among H¹ mild solutions only; showing `NS(v₀)` is H¹ mild on compacts of `(0,T*)` is itself a persistence statement needing a source (Kato-class smoothing) — not inspected by anyone. Tao Prop. 5.6 (p. 35) is about H¹ mild data and does not close it. |
| K4 | lean design `gkp_theorem4`/`IsMaximalL3Mild` vs literature §2.1 note 2 and §4.2 | The `C([0,T);L³)`-Duhamel-maximal predicate presupposes uniqueness in `C_tL³` to be "the" solution; the literature lane records that class only through GKP's remark and reference [9], and marks FLRT [MO]. The design's R-MILD acknowledges Besov vs `C_tL³` but not the uniqueness presupposition. | Same primary-source gap as K3, appearing as a hidden import in an axiom. |
| K5 | obligations Q-4, lean design `leray_projection_L3`/T12/T19 vs quotient `lem:leray`(c) and its remark | Obligations/design require `ℙu = u` for every distributionally solenoidal **L³** field (general L³ Helmholtz decomposition, Galdi III.1.2 / Fujiwara–Morimoto, not inspected); quotient lane proves it only on `L²∩L³` by Plancherel and declares the L³ Helmholtz theorem "not a dependency". The manuscript's coercivity display says "for solenoidal u" without a class. | The paper's use is on Navier–Stokes velocities, which are in `L²∩L³`; the Lean axiom/hypothesis is stronger than the paper needs and mixes a literature fact with the project step Q-4. |
| K6 | lean design `heat_generator_L3` vs quotient `lem:heat-generator` vs literature S5 | Axiom hypotheses (`C²`, `v, Δv ∈ L³`) have no located primary source ([MO]/[REC]); the quotient lane proves the needed statement for `u ∈ H^m` from Fourier/L² plus L³ strong continuity. | Axiom over-strength; the paper's version is provable. |
| K7 | lean design `divfree_flow` vs quotient `lem:flow`(b)–(d) and `lem:quotient-transport` | The axiom lacks the variational equation and the `s²` expansions of `DΦ_s`, `DΦ_s^{-T}` that the transport proof uses; hypotheses differ (`ContDiff ∞`, bounded `v, Dv` vs `C²` with bounded `D²b`). T18 is not derivable from the axiom as stated. | Literature lane S9 and quotient lane F6b/F6c: Hartman theorem numbers [REC], never inspected. |
| K8 | literature §8 item 4 vs lean design `LowPassProfile` vs manuscript "smooth homogeneous Littlewood–Paley partition" | Literature: homogeneous vs inhomogeneous cutoffs "differ at low frequency and the difference is not harmless for `S_J p` when `p` is only in `L²∩L³`" (major). Design encodes Tao's inhomogeneous bump (`F K = 1` on the unit ball). | For the single low-pass operator `S_J` (all `prop:lowpressure` uses) the two symbols agree for `ξ ≠ 0`, a null set for `p ∈ L²`; the difference matters only for `Σ_j Δ_j = id` modulo polynomials. This is a critic observation, not a ruling; CP02 must fix one convention (F-1) and say why. |
| K9 | manuscript/HF17 note/HF17 review ("reflexivity and weak lower semicontinuity … strict convexity"; review's "direct derivative proof" still uses weak convergence, lsc and uniform convexity of L³ for `w_h → w`) vs mathlib lane MC-05 (all three ingredients absent; cheap route proposed, "change of proof, re-audit") vs quotient lane `lem:quotient-minimizer` (cheap route written) vs lean design T10 ("re-audit against `hf17-review-quotient-functional.md`, which itself already gives a direct envelope argument") | The design mischaracterises the HF17 review: its direct argument is for the derivative and still rests on uniform convexity/weak compactness (lines 70–90 of the review, read here). The quotient lane's route is new relative to both HF17 files and is the only one Mathlib can follow; it has not been audited. The manuscript sentence must change when it is adopted. Also the remainder exponent differs (obligations `O(‖h‖^{3/2})`, quotient lane `O(‖h‖^{4/3})`); both valid, the quotient lane's Hölder step is coarser. | — |
| K10 | quotient lane `hyp:highstrain` ("stated with the same quantifier order as `hyp:highpressure`") vs manuscript `hyp:highpressure` (`∃θ∈[0,1)` outermost) vs manuscript `eq:quotient-gap` and PLAN HF17 (`θ ≤ 1`) vs lean design T20 (`θ` a parameter) | The quotient lane puts `∃θ∈[0,1]` **inside** `∀(ν,u₀,H)` and permits `θ = 1`, so the order is not the same. Mathematically inert (θ = 1 allowed), but the graph's future HIGH-STRAIN node must pick one statement. | — |
| K11 | Palomar lane §2.3 route B ("notability rests on the quotient functional being a genuinely new object") vs manuscript `sec:quotient`, PLAN HF17, quotient lane (no novelty asserted) | Registration needs an affirmative notability case; the programme disclaims novelty and has no prior-art search on the functional. | `hf02-prior-art.md` and `hf10-pressure-speed-sources.md` contain no hit for "quotient", "distance to gradient", "Helmholtz" (grep). |
| K12 | task brief/PLAN/`navier-formal` (v4.33.1, Mathlib `0df444a…`) vs Palomar lane PAL-TOOLCHAIN (pin v4.33.0) vs lean design §4.6 (undecided) | Live conflict on disk. | lean4export tags re-checked 2026-09-05: no v4.33.1. |
| K13 | Palomar lane §1.7 (`sources[].type` closed list; `project.description` mechanically required) vs v0.4 schema (free-form `type`; `description` optional) vs `navier-formal/formalization.yaml` (`manuscript`, `book chapter`, `article`) | Either Palomar's policy adds constraints beyond the schema (possible; the lane read CONTRIBUTING directly) or the lane over-read. Must be checked against CONTRIBUTING raw text before the on-disk file is judged. | Schema fetched (metadata-only summary). |
| K14 | lean design §5 and Palomar lane §6 ("`lake init` … not created") vs `navier-formal` on disk (3 commits, 70 declarations) and design D7/R-P0/obligations P-0 vs CP03b `NormGradient.lean` (Rademacher/`∇|u|` route, operator norm, `LipschitzWith`) | The design and the repository diverge in names, in the chosen route for `prop:pressure`'s pointwise lemmas, and in the norm convention. | §1 items 1–3. |
| K15 | graph nodes vs manuscript (obligations §2): ESS node "maximal smooth finite-energy R³ solution" ≠ GKP's `NS(u₀)`; ABSORPTION θ inside `∀`; LOCAL uniqueness class absent; no QUOTIENT node; stale `source_revision`; graph CRITICAL `0 ≤ t` vs manuscript `0 < t` | Unchanged; `verify.py` PASS is structural only. | — |
| K16 | `hf18-hodge-regularity.md` (2.2) `D_𝒬(u) = D₃(w)` boxed vs `hf18-divergence-speed-link.md` ("not claimed") vs quotient lane non-claim O9 | Two Track B lanes disagree on an identity about a CP1 object. | Both untracked, unreviewed; outside CP1 until audited. |

## 7. Obligations no lane owns

| ID | Obligation | Nearest lane text | Why unowned |
|---|---|---|---|
| U1 | Pin primary sources for L³/`E_{p,q}` strong-solution **uniqueness** and for **regularity/persistence** of `NS(u₀)` past the classical time (C-2 (b),(c)); or prove the identification from Tao 5.4(iii) after a sourced smoothing statement for `NS(u₀)`. | obligations §1.10, literature §4.2/§8.2 | Obligations lane deferred to the literature lane; the literature lane declined ("not needed") and marked FLRT [MO]. |
| U2 | Written gluing/maximal-development lemma (L-1) with the choice "Cor. 5.8 as axiom" vs "proved from 5.4(i)–(iii)". | literature §1.3, lean design `Continuation.lean` | CP02 task not yet specified; the two lanes disagree on the axiom set (K1). |
| U3 | Decide whether the existential-equivalence paragraph (X-1) and `rem:highstrain-scope` are CP1 propositions; if so, write `‖p_{>0}‖₃ ≤ C‖u‖₆²` with a route and add Lean statements. | obligations §1.9, quotient lane §4 | Absent from PLAN's CP1 table and from T1–T20. |
| U4 | Lemma "`∂_t^j u, ∂_t^j p ∈ L^∞_t H^k ∀j,k ⟹ C^∞([0,T]×R³)`" (C-3), paper text and Lean. | lean design `Calculus/Sobolev.lean` (name only) | No proof text anywhere; Mathlib has no `H^k ↪ C^{k-2}_b`. |
| U5 | One pressure-normalisation encoding for `Challenge.lean`, and the lemma ID-P1 (L² + Poisson ⟹ Riesz representative) with size estimate and source. | lean design D4/R-PRESS, obligations P-1, quotient O6 | Three encodings, no owner (§3.7). |
| U6 | Independent audit (different tier) of `cp01-quotient-section-structure.md` §4, in particular `lem:quotient-minimizer` (new existence route, K9), `lem:heat-generator`, `lem:flow`, `lem:quotient-transport`, `prop:quotient-evolution`; then controller integration into `main.tex` with preamble and bibliography additions. | quotient lane O7 and "NEXT DISTINCT ACTION" | Gate 1 requires `cp02-review-*` PASS; not scheduled. |
| U7 | Primary-source inspection of the [REC] items the quotient lane imports: Hartman Ch. II Thm 1.1/3.1, Ch. V Thm 3.1, Ch. IV Thm 1.2; Lieb–Loss Thm 8.3; Grafakos 2.2.14/2.2.17; Brezis 4.10/3.32 (if used). | quotient lane §3, literature §6 | Literature lane's pass predates the quotient lane's citations. |
| U8 | Prior-art search for the L³ gradient-quotient functional (distance to `𝒢₃`, Helmholtz quotient norms, `p`-Laplace-type minimisers of `‖u+∇φ‖_p`). | Palomar §5, quotient lane non-claims | Needed both for route B notability and for the manuscript's "no novelty" wording to be evidence-based. |
| U9 | Reconcile `navier-formal` with the design: naming (`Space`/`E`, `dilate`/`criticalScale`), decision on `NormGradient.lean` (retain as supporting lemmas or retire under P-0), Frobenius/operator-norm bridge, and fill `docs/paper-lean-specification.md` for the 70 integrated declarations. | `verification-status.md` gap list, lean design §5–§6 | The design lane did not see the repository. |
| U10 | Toolchain decision (K12) and disk budget. | Palomar §1.1/§3.1 | Controller-only. |
| U11 | Graph/PLAN edits G-1 + QUOTIENT node + HIGH-STRAIN node with a fixed quantifier order (K10, K15) + refresh `source_revision`. | obligations §2 | Controller-only. |
| U12 | Quarantine of HF18 notes from CP1 and audit of their mutual contradiction (K16). | hf18-*.md | Track B; no CP1 lane may cite them. |
| U13 | Size estimate and gate-3 scope decision for Phase II discharge of `AX-TAO-5.4`, `AX-TAO-5.8`, `AX-GKP-4` themselves (§4.1). | PLAN gate 3, mathlib lane §11 | Not estimated by any lane. |
| U14 | Palomar metadata verification against CONTRIBUTING raw text: `sources[].type` vocabulary, `project.description`, `review.reviewers`, taxonomy codes (`35B65` vs `35B44`), `fidelity.divergences` shape (K13). | Palomar §1.7/§7, on-disk `formalization.yaml` | Palomar lane could not fetch the taxonomies; the on-disk file postdates its recommendations. |
| U15 | Statement of the LP/low-pass convention shared by `prop:lowpressure`, `sec:quotient`'s `S_L`, the Lean `LowPassProfile`, and the constants `C2^{3J}`, `‖∇ψ‖₂2^{5L/2}` (K8, F-1). | literature §8.4, quotient `def:quotient`(f), design R-LP | Three slightly different conventions in three lanes. |
| U16 | Correction of the abstract and Proof-boundary section for gate 1 (§2 major, last bullet). | quotient lane §4 end; obligations §1 | Manuscript-side; controller. |

## 8. Ranked next tasks for the controller

1. **Resolve K3/K4 (C-2) before any CP02 writing of `thm:continuation`.**
   Commission a literature lane (Opus, extraction) to pin and quote: (i) a
   uniqueness theorem covering the Tao H¹-mild branch and GKP's `NS(v₀)` on
   a common interval (candidates: Gallagher–Iftimie–Planchon 2003 = GKP's
   [9]; FLRT 2000; Kato 1984 Thm 1 with its weighted class), (ii) a
   regularity/persistence theorem for `NS(v₀)` (Kato-class smoothing to
   `H¹`/Serrin class), and (iii) Tao's "almost smooth H¹ solution"
   definition (R-CLASS). Motivating files: `cp01-manuscript-obligations.md`
   §1.10, `cp01-literature-statements.md` §4.2 and §8.2,
   `cp01-lean-statement-design.md` §3.3.
2. **Fix the Tao axiom set (K1, K2).** Decide "Cor. 5.8 as `AX-TAO-5.8`" vs
   "gluing lemma from 5.4(i)–(iii)"; restate `local_existence`/
   `tao_regularity` for Schwartz data without the in-proof remark; repair
   `premise:local` to cite Thm 5.4 **and** Cor. 5.8. Motivating files:
   `cp01-literature-statements.md` §1.3 and §8.1; critic verification §0.
3. **Audit and integrate the quotient section (Q-block, K9).** Schedule a
   Fable-tier adversarial audit of `cp01-quotient-section-structure.md` §4
   with the HF17 review as the comparison baseline and the new existence
   route as the declared change of proof; then integrate into `main.tex`,
   add `hyp:highstrain`/`prop:quotient-conditional` to the Proof boundary,
   and add the QUOTIENT and HIGH-STRAIN graph nodes with one quantifier order
   (K10). Motivating files: `cp01-quotient-section-structure.md` O7,
   `cp01-mathlib-coverage.md` MC-05.
4. **Reconcile `navier-formal` with the statement design (K14, U9).** Decide
   the fate of `NormGradient.lean` under P-0/R-P0; fix names; write the
   missing `paper-lean-specification.md` rows for the 70 declarations before
   any new module lands. Motivating files: `navier-formal/docs/
   verification-status.md`, `cp01-lean-statement-design.md` §5–§6.
5. **Repair the five non-literature or mis-sized axioms (K5–K7, §3.1–3.3).**
   Leray on `L²∩L³` with `‖ℙ‖_{3→3}` as the only literature input; heat
   generator for `H^m`; flow axiom carrying the variational equation and
   expansions or replaced by a proof plan; Bernstein proved; C-2 never an
   axiom. Motivating files: `cp01-quotient-section-structure.md` §3–§4,
   `cp01-lean-statement-design.md` §3.3, `navier-formal/AGENTS.md`.
6. **Unify the pressure normalisation (U5).** Choose D4 vs Riesz-multiplier
   encoding; estimate ID-P1; align `prop:pressure` P-1 text. Motivating
   files: `cp01-lean-statement-design.md` R-PRESS, `cp01-manuscript-
   obligations.md` P-1.
7. **Toolchain and disk (K12, U10).** Decide v4.33.0 vs v4.33.1 now; the
   repository already pins v4.33.1. Motivating file:
   `cp01-palomar-checklist.md` §1.1/§3.1; critic re-check §0.
8. **Define gate 3 honestly (U13).** Either estimate Phase II for Tao 5.4/5.8
   and GKP 4 or restate gate 3 so that those remain `LITERATURE-INPUT` with
   route-A explicit hypotheses while the standard-analysis blocks are
   discharged. Motivating files: `PLAN.md` gate 3, `cp01-mathlib-coverage.md`
   §11.
9. **Specify CP02 writing tasks** for C-0, C-3 (with U4), P-1…P-3, F-1 (with
   U15 fixing one LP convention), E-1, N-1, S-1, S-2, X-1 (U3), abstract and
   boundary edits (U16). Motivating file: `cp01-manuscript-obligations.md`
   §4.
10. **Graph/PLAN fidelity (K15, U11)** including `source_revision` refresh.
11. **Quarantine HF18 (K16, U12)** and route their D_𝒬 = D₃(w) disagreement
    to a Track B audit; forbid CP1 citations of them until then.
12. **Prior-art search on the quotient functional (K11, U8)** and Palomar
    metadata verification (K13, U14); check `PalomarSubmission/taxonomies`.
13. **Primary-source pass for the quotient lane's [REC] citations (U7)**
    before any Phase I source record cites Hartman, Lieb–Loss, or Grafakos
    §2.2 numbers.

## Frontier record

**MODE / RESULT:** REVIEW (cross-lane completeness critic). No mathematics was
proved, weakened or promoted. Every contradiction above is left to the
controller; where a primary source was re-inspected (Tao arXiv pp. 30–38,
lean4export tags, v0.4 schema, PalomarSubmission #132, Mathlib greps,
`navier-formal` working tree) the evidence is recorded in §0 and labelled.

**CLAIM AND SCOPE.** For the original unforced R³ equation with Schwartz
divergence-free data, ν > 0, in Tao's H¹-mild classical branch: the CP1
chain is complete in outline and no lane found a false step; it is not yet a
paper proof (§2), its Lean statement surface is designed but not faithful in
five axioms and one hidden import (§3), its Phase II cost excludes the
literature theorems themselves (§4), and registration is blocked by
toolchain, metadata, and notability items (§5).

**FIRST GAP (gate 1).** C-2: the sentence "uniqueness in the mild class
identifies it with the maximal L³ solution" in `thm:continuation` has no
named uniqueness or persistence source in any lane, and the lanes disagree on
whether one is needed (K3). Immediately behind it: the unaudited quotient
section rewrite (Q-block, K9) and the Tao axiom-set disagreement (K1, K2),
the latter settled at the source level by this note's inspection of Cor. 5.8.

**SURVIVING CONDITIONAL SUFFIX.** With C-2 sourced and L-1 written from Thm
5.4 + Cor. 5.8 (or 5.4(i)–(iii)), the chain `hyp:critical ⟹
thm:continuation ⟹ T_* = ∞ ⟹ (Tao 5.4(iv), prop:energy) Clay (A)` and the
quotient identities `eq:quotient-evolution`, `D_𝒬 ≥ 0`, `|K_low| ≤ M_L 𝒬`,
`hyp:highstrain ⟹ hyp:critical` stand as stated by the lanes, on compact
classical intervals.

**UNNECESSARY DEPENDENCIES (confirmed across lanes).** Calderón–Zygmund
theory except for `‖ℙ‖_{3→3}`; full Littlewood–Paley theory; reflexivity/
Clarkson (given K9's route); `∇|u|`/Rademacher (given P-0); the L³ Helmholtz
decomposition (given `L²∩L³`); the Tao in-proof remark (given K2's route);
`prop:enstrophy`, `prop:ode`, Kato 1984 for the conditional chain.

**NON-CLAIMS.** No statement about HIGH-PRESSURE, HIGH-STRAIN, CRITICAL,
ABSORPTION or NS-R3. No HF18 content is endorsed. No Palomar action, no
repository change, no push.

**NEXT DISTINCT ACTION.** Controller resolves K3 by commissioning the
uniqueness/persistence source pass (task 1) and K1/K2 by fixing the Tao
axiom set (task 2); only then does CP02 write `thm:continuation` and
`premise:local`.
