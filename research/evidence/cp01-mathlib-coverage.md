# CP01 — Mathlib v4.33.1 coverage survey for the CP1 analytic prerequisites

**Lane:** implementer survey (MODE: survey, not proof).
**Owner file:** `research/evidence/cp01-mathlib-coverage.md`. No other file was edited.

## 0. Scope, method, and what this note is not

This note answers exactly one question: for each analytic prerequisite of
**CP1** (the conditional checkpoint listed in the task: `prop:energy`,
`prop:scaling`, `prop:enstrophy`, `prop:ode`, `prop:pressure`,
`prop:lowpressure`, `thm:continuation`, `thm:conditional`, plus the audited
HF17 quotient-functional results of `sec:quotient`), **what already exists in
Mathlib at tag `v4.33.1`, under what exact hypotheses, and what must be
formalized from scratch.**

- Checkout inspected: `../stafford38/.lake/packages/mathlib`,
  `git describe`/`git log -1` → commit `0df444a360eaa60ab8c11dca51a86af692955474`,
  tag `v4.33.1`, `origin/stable`, dated 2026-08-21 12:04:53 +0000.
  `lean-toolchain` = `leanprover/lean4:v4.33.1`. **Directly inspected** by
  `grep`/`sed` on the working tree. Nothing was built; no elaboration was run,
  so every "available" claim below is a claim about *source text of a
  declaration*, not about a successfully type-checked application to CP1's
  concrete instantiation.
- Manuscript read in full: `../navier-paper/main.tex` (562 lines),
  **directly inspected**. `PLAN.md` frontier packet **directly inspected**.
- All file paths below are relative to
  `../stafford38/.lake/packages/mathlib/Mathlib/`.
  Line numbers are from this checkout.

**Disposal classes used.**

| Class | Meaning |
|---|---|
| **M** | Available in Mathlib in a form usable for CP1 (declaration cited). A hypothesis mismatch that is a routine specialization is still M, and is flagged. |
| **M‑** | Present but only in a weaker/adjacent form; CP1 needs a bridging lemma of small size (≤ ~10 lemmas). The bridge is itself F, but the hard mathematics is done. |
| **F** | Standard mathematics absent from Mathlib; must be formalized. Scale ≤ ~60 lemmas. |
| **F\*** | Absent and large: a multi-file development. Lemma-scale estimate given. |

**Non-claim.** Nothing here bears on the truth of `hyp:critical`,
`hyp:absorption`, `hyp:highpressure`, or `eq:quotient-gap`. A Mathlib gap is a
formalization cost, not a mathematical gap; a Mathlib hit is not a verified
applicability to the CP1 statement. The terminal Clay claim NS-R3 remains OPEN
and is not addressed here.

---

## 1. `L^p` spaces on `R^3`-valued functions

### 1.1 The space, the norm, Hölder, Minkowski — **M**

- `MeasureTheory.Lp` — `MeasureTheory/Function/LpSpace/Basic.lean:89`.
  `def Lp {α} (E : Type*) {m : MeasurableSpace α} [NormedAddCommGroup E] (p : ℝ≥0∞) (μ : Measure α := by volume_tac) : AddSubgroup (α →ₘ[μ] E)`.
  Any `NormedAddCommGroup E` works, so `E := EuclideanSpace ℝ (Fin 3)` is
  admissible with no extra work; the base is `α := EuclideanSpace ℝ (Fin 3)`
  with `volume`.
- Norm/normed-space/completeness:
  `MeasureTheory.Lp.instNormedSpace` (`LpSpace/Basic.lean:460`, needs
  `[Fact (1 ≤ p)]`), `MeasureTheory.Lp.instCompleteSpace`
  (`LpSpace/Complete.lean:378`). Seminorm layer: `MeasureTheory.eLpNorm`,
  `MeasureTheory.MemLp` in `MeasureTheory/Function/LpSeminorm/Defs.lean`.
- **Minkowski (triangle) inequality**: `MeasureTheory.eLpNorm_add_le`
  (`LpSeminorm/TriangleInequality.lean:52`), with `eLpNorm_sum_le` (:127),
  `MemLp.add` (:137). `ℝ≥0∞`-level Minkowski:
  `MeasureTheory.ENNReal.lintegral_Lp_add_le` region,
  `MeasureTheory/Integral/MeanInequalities.lean:378`.
- **Hölder**: `MeasureTheory.eLpNorm_le_eLpNorm_mul_eLpNorm_of_nnnorm`
  (`LpSeminorm/CompareExp.lean:228`),
  `eLpNorm_le_eLpNorm_mul_eLpNorm'_of_norm` (:257),
  `eLpNorm_smul_le_mul_eLpNorm` (:300), `MemLp.mul` (:319), all driven by the
  typeclass `ENNReal.HolderTriple` (`Data/ENNReal/Holder.lean:42`) and
  `ENNReal.HolderConjugate`. Endpoint cases:
  `eLpNorm_le_eLpNorm_mul_eLpNorm_top` (:193),
  `eLpNorm_le_eLpNorm_top_mul_eLpNorm` (:166). Discrete/scalar Hölder and
  Young: `Real.inner_le_Lp_mul_Lq` (`Analysis/MeanInequalities.lean:615`),
  `Real.young_inequality` (:507), `Real.young_inequality_of_nonneg` (:500),
  `NNReal.young_inequality` (:528).
- Bilinear Hölder pairing on `Lp` itself:
  `ContinuousLinearMap.holder`, `holderL`, `lpPairing`
  (`MeasureTheory/Function/Holder.lean:69,128,142`), with
  `lpPairing_eq_integral` (:145). This is exactly the pairing
  `Lp E p → Lp F q → G`; **it is not a duality theorem** (see §1.4).

**CP1 uses.** `prop:energy` (Cauchy–Schwarz), `prop:scaling` `eq:L4L3`,
`prop:enstrophy` (Hölder + Young with exponents 4/3, 4), `prop:pressure`
integrability bookkeeping, `prop:lowpressure` (`‖u⊗u‖₁ ≤ ‖u₀‖₂²`),
`sec:quotient` Hölder for `K_L`. All **M**.

### 1.2 Interpolation of `L^p` norms (Lyapunov) — **M‑**

Mathlib has the finite-measure monotonicity family
(`eLpNorm_le_eLpNorm_mul_rpow_measure_univ`, `CompareExp.lean:65;`
`MemLp.mono_exponent`, :115) but **no Lyapunov/log-convexity inequality**
`‖f‖_r ≤ ‖f‖_p^θ ‖f‖_q^{1-θ}` on an infinite measure space. Grep for
`interpolat` inside `MeasureTheory/` returns nothing relevant; there is no
`eLpNorm_le_eLpNorm_rpow_mul_eLpNorm_rpow` or similar.

This is exactly the step `‖u‖₃ ≤ ‖u‖₂^{1/2}‖u‖₆^{1/2}` used in
`prop:scaling` and `‖∇u‖₃ ≤ C‖∇u‖₂^{1/2}‖Δu‖₂^{1/2}` in `prop:enstrophy`.

**Disposal: M‑ / F(small).** Derivable from
`eLpNorm_le_eLpNorm_mul_eLpNorm_of_nnnorm` applied to `|f|^{θr}·|f|^{(1-θ)r}`
plus `ENNReal.rpow` algebra. **Estimate: 4–8 lemmas** (one general Lyapunov
lemma with `1/r = θ/p + (1-θ)/q`, plus the `ℝ≥0∞`/`ℝ` bridging and the two
concrete instances).

### 1.3 Density of smooth compactly supported functions in `L^p` — **M**

This is the single most useful recent addition for CP1.

- `SchwartzMap.denseRange_toLpCLM` —
  `Analysis/Distribution/SchwartzSpace/Basic.lean:1383`:
  ```
  theorem denseRange_toLpCLM [FiniteDimensional ℝ E] [BorelSpace E] {p : ℝ≥0∞} (hp : p ≠ ⊤)
      [hp' : Fact (1 ≤ p)] {μ : Measure E} [hμ : μ.HasTemperateGrowth] [IsFiniteMeasureOnCompacts μ] :
      DenseRange (SchwartzMap.toLpCLM ℝ F p μ)
  ```
  `volume` on `EuclideanSpace ℝ (Fin 3)` satisfies `HasTemperateGrowth` via
  `MeasureTheory.Measure.IsAddHaarMeasure.instHasTemperateGrowth`
  (`Analysis/Distribution/TemperateGrowth.lean:442`). So **Schwartz functions
  are dense in `L^p(R^3)` for `1 ≤ p < ∞`** — available for `p = 2, 3, 4, 6`.
- Supporting: `SchwartzMap.toLp` (:1321), `SchwartzMap.toLpCLM`,
  `SchwartzMap.memLp` (:1317), `SchwartzMap.eLpNorm_lt_top` (:1302),
  `SchwartzMap.injective_toLp` (:1351),
  `HasCompactSupport.toSchwartzMap` (:555).
- Continuous-compactly-supported density (independent route):
  `MeasureTheory.MemLp.exists_hasCompactSupport_eLpNorm_sub_le`
  (`MeasureTheory/Function/ContinuousMapDense.lean:135`),
  `MemLp.exists_boundedContinuous_eLpNorm_sub_le` (:233),
  `MeasureTheory.Lp.boundedContinuousFunction_dense` (:321).
- Smoothing: `ContinuousMap.dense_setOfPred_contDiff`
  (`Analysis/Calculus/BumpFunction/SmoothApprox.lean:55`).

**Caveat for `sec:quotient`.** The quotient functional needs density of
`{∇φ : φ ∈ C_c^∞}` **inside the gradient subspace `𝒢₃ ⊆ L³`**, which is a
*definition* in the manuscript (closure), so no theorem is needed for the
definition itself; but the manuscript's step "cutting off `p` and mollifying
proves `∇p ∈ 𝒢₃`" is a genuine approximation lemma with a divergence
constraint and is **not** in Mathlib (see §5.3).

### 1.4 Strict/uniform convexity of `L^p` (Clarkson), reflexivity, weak compactness — the main hole

| Item | Class | Evidence |
|---|---|---|
| `UniformConvexSpace` class | M | `Analysis/Convex/Uniform.lean:44`; `UniformConvexSpace.toStrictConvexSpace` (:125) |
| `StrictConvexSpace` class | M | `Analysis/Convex/StrictConvexSpace.lean:67`, with constructors `of_strictConvex_unitClosedBall` (:85), `of_norm_combo_lt_one` (:92), `of_norm_add_ne_two` (:118) |
| **Clarkson's inequalities** | **F\*** | grep for `Clarkson`/`clarkson` over all of Mathlib returns **zero** hits |
| **`UniformConvexSpace (Lp E p μ)` instance** | **F\*** | grep `UniformConvexSpace` under `MeasureTheory/` returns **zero** hits. The only instances are for inner-product spaces (`Analysis/InnerProductSpace/Convex.lean`) |
| **`StrictConvexSpace ℝ (Lp E p μ)`** | **F\*** | grep `StrictConvexSpace` under `MeasureTheory/` returns **zero** hits |
| **Reflexivity of a Banach space** (any `IsReflexive`/`ReflexiveSpace` class) | **F\*** | no such class exists; grep `Reflexive` outside `CategoryTheory`/order returns nothing in `Analysis/`. Only `NormedSpace.inclusionInDoubleDual` / `inclusionInDoubleDualLi` (`Analysis/Normed/Module/DoubleDual.lean:58,87`) |
| **Riesz representation `(L^p)^* ≅ L^q`** | **F\*** | `lpPairing` exists but there is **no** surjectivity/isometry statement; grep `lpPairing` finds only 3 downstream uses in `Analysis/Distribution/TemperedDistribution.lean` |
| Banach–Alaoglu (weak‑\* on a dual) | M | `WeakDual.isCompact_polar` (`Analysis/Normed/Module/WeakDual.lean:314`), `WeakDual.isCompact_closedBall` (:270, needs `[ProperSpace 𝕜]`), `WeakDual.isSeqCompact_closedBall` (:370, separable predual) |
| **Weak (not weak‑\*) sequential compactness of bounded sets in a reflexive space** | **F\*** | needs reflexivity; absent |
| Weak lower semicontinuity of the norm | **F** | absent as such. Nearest: `NormedSpace.norm_le_dual_bound` (`DoubleDual.lean:97`), `WeakSpace` API in `Analysis/LocallyConvex/WeakSpace.lean` (`Convex.toWeakSpace_closure`, :42 — the Mazur-type statement that the weak closure of a convex set equals its norm closure) |
| a.e.-convergence lsc of `eLpNorm` (Fatou) | M | `MeasureTheory.eLpNorm'_lim_le_liminf_eLpNorm'` (`LpSpace/Complete.lean:38`), from `lintegral_liminf_le'` (`Integral/Lebesgue/Add.lean:214`) |
| Projection onto a closed convex set | M **only in Hilbert space** | `exists_norm_eq_iInf_of_complete_convex` (`Analysis/InnerProductSpace/Projection/Minimal.lean:34`, "Hilbert projection theorem"). No Banach/uniformly-convex analogue |

**This is the decisive finding for `sec:quotient`.** The manuscript's HF17
existence proof reads: *"The minimizer `q` exists by reflexivity and weak lower
semicontinuity, and is unique by strict convexity."* **Every one of the three
cited ingredients is absent from Mathlib v4.33.1.** Phase II would have to
build, in order: Clarkson's inequalities for `1 < p < ∞` → uniform convexity of
`L^p` → (Milman–Pettis or a direct argument) reflexivity of `L^p`, *or*
alternatively the `L^p` duality theorem and reflexivity from it. See §11 for
the ranked cost.

A cheaper Phase‑I route exists and should be considered: for the *specific*
functional `𝒬(u) = inf_{q∈𝒢₃} ⅓‖u+q‖₃³`, existence and uniqueness of the
minimizer can be proved directly from **uniform convexity of the cubic
functional** (i.e. the elementary inequality
`⅓‖a‖₃³ + ⅓‖b‖₃³ - 2·⅓‖(a+b)/2‖₃³ ≥ c‖a-b‖₃³`, a pointwise convexity
statement plus `lintegral_mono`) applied to a minimizing sequence, giving a
**Cauchy** minimizing sequence in the closed subspace `𝒢₃` — completeness of
`Lp` then supplies the limit and no reflexivity or weak compactness is used.
That reduces this item from **F\*** to **F(≈15–25 lemmas)**. This is a
formalization-strategy remark; it does not change the mathematics of the
manuscript and it must be independently checked against the HF17 audit before
being relied on.

---

## 2. Schwartz space, Fourier transform, Plancherel, multipliers

### 2.1 `SchwartzMap` — **M**

- `SchwartzMap` / `𝓢(E, F)`: `Analysis/Distribution/SchwartzSpace/Basic.lean`
  (whole file; seminorms `SchwartzMap.seminorm`, `norm_le_seminorm`).
  Requires `[NormedAddCommGroup E] [NormedSpace ℝ E]` — `EuclideanSpace ℝ (Fin 3)`
  qualifies; `FiniteDimensional ℝ E` and `BorelSpace E` hold.
- Derivatives: `SchwartzMap.fderivCLM`
  (`SchwartzSpace/Deriv.lean:84`), `fderivCLM_apply` (:93),
  `SchwartzMap.hasFDerivAt` (:96), `derivCLM` (:60), directional
  `∂_{m}` = `lineDerivOp` (:104,:126,:129),
  `iteratedLineDerivOp_eq_iteratedFDeriv` (:132).
- Laplacian on Schwartz: `SchwartzMap.instLaplacian`,
  `SchwartzMap.laplacianCLM_eq'` (:196), `laplacian_eq_sum` (:198),
  `laplacian_apply` (:208).
- **Integration by parts on Schwartz functions (whole space, no boundary
  term)** — directly usable for `prop:energy`, `prop:enstrophy`:
  - `SchwartzMap.integral_bilinear_lineDerivOp_right_eq_neg_left` (:271)
  - `SchwartzMap.integral_smul_lineDerivOp_right_eq_neg_left` (:293)
  - `SchwartzMap.integral_bilinear_laplacian_right_eq_left` (:322)
  - `SchwartzMap.integral_smul_laplacian_right_eq_left` (:345)
- `SchwartzMap.toLp` / `toLpCLM` / `denseRange_toLpCLM` (see §1.3).

### 2.2 Fourier transform on Schwartz and on `L^2` (Plancherel) — **M**

- `SchwartzMap.fourierTransformCLM : 𝓢(V,E) →L[𝕜] 𝓢(V,E)`
  (`Analysis/Distribution/SchwartzSpace/Fourier.lean:51`), notation `𝓕`, with
  `fourier_fderivCLM_eq` (:181), `fourier_lineDerivOp_eq` (:205),
  `integral_bilin_fourier_eq` (:239), `norm_fourier_toL2_eq` (:318),
  `inner_fourier_toL2_eq` (:324).
- **Plancherel on `L²`**: `MeasureTheory.Lp.fourierTransformₗᵢ :
  (Lp (α := E) F 2) ≃ₗᵢ[ℂ] (Lp (α := E) F 2)`
  (`Analysis/Fourier/LpSpace.lean:48`), with
  `MeasureTheory.Lp.norm_fourier_eq` (:88) and `Lp.inner_fourier_eq` (:93),
  and the compatibility `SchwartzMap.toLp_fourier_eq` (:98).
  **Hypotheses to note:** `F` must satisfy
  `[NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]` and the
  base `E` must be `[InnerProductSpace ℝ E] [FiniteDimensional ℝ E]`.
  For a *real* `R^3`-valued velocity field this means Phase II must
  complexify: `F := EuclideanSpace ℂ (Fin 3)` and carry a real-subspace
  argument, or work componentwise with `F := ℂ`. That bridging is **M‑ /
  F(small): ≈5–10 lemmas.**
- Tempered distributions: `TemperedDistribution` / `𝓢'(E,F)`
  (`Analysis/Distribution/TemperedDistribution.lean:53`),
  `MeasureTheory.Lp.toTemperedDistributionCLM` (:195),
  `Lp.fourier_toTemperedDistribution_eq` (`Fourier/LpSpace.lean:126`).

### 2.3 Fourier multipliers — **M (on `𝓢` and `𝓢'`) / F (on `L^p`, `p ≠ 2`)**

- `SchwartzMap.fourierMultiplierCLM (g : E → 𝕜) : 𝓢(E,F) →L[𝕜] 𝓢(E,F)`
  (`Analysis/Distribution/FourierMultiplier.lean:50`), with composition law
  (:85,:91), `lineDeriv_eq_fourierMultiplierCLM` (:100),
  `laplacian_eq_fourierMultiplierCLM` (:107).
- `TemperedDistribution.fourierMultiplierCLM` (:143) with the analogous API
  (:161,:167,:190,:201,:208).
- **Missing:** any `L^p`-boundedness criterion for a multiplier
  (Mikhlin–Hörmander, Marcinkiewicz multiplier theorem). Not present.
  **F\*** — see §5.

**CP1 relevance.** `prop:lowpressure` normalizes `p = R_i R_j (u_i u_j)` and
uses the *band-limited* kernel bound `‖K_J‖_∞ ≤ C 2^{3J}`. The multiplier is
definable via `fourierMultiplierCLM`, but the passage to a convolution kernel
with an `L^∞` bound, and the `L^1 → L^∞` estimate
`‖p_{≤J}‖_∞ ≤ ‖K_J‖_∞ ‖u⊗u‖_1`, is **F** (see §8).

---

## 3. Heat kernel / heat semigroup / Gaussian convolution — **F\***

**Nothing.** Exhaustive greps over the checkout:

- `heatKernel` — 0 hits. `HeatKernel` — 0 hits. `heat equation` — 0 hits.
- `StronglyContinuousSemigroup` / `C0Semigroup` / `OneParameterSemigroup` — 0 hits.
  **Mathlib v4.33.1 has no `C₀`-semigroup theory at all.**
- Gaussians exist only as *functions/measures*, not as a semigroup:
  `Analysis/SpecialFunctions/Gaussian/GaussianIntegral.lean`,
  `Gaussian/FourierTransform.lean` (the Fourier transform of a Gaussian),
  `Gaussian/PoissonSummation.lean`,
  `Probability/Distributions/Gaussian/{Basic,Real,Multivariate,CharFun}.lean`.
- General convolution API exists (`Analysis/Convolution.lean`,
  `Analysis/LConvolution.lean`) — see §8.

**CP1 relevance.** `sec:quotient` uses: (i) *"Heat preserves `𝒢₃` and contracts
`L³`"*, (ii) `𝒬(e^{sΔ}u) ≤ 𝒬(u)`, (iii) the generator identity defining
`D_𝒬(u) = -∫A·Δu ≥ 0` *"by differentiating the heat contraction at zero"*.
All three require a heat semigroup on `L³(R³)` with its generator.

**Disposal: F\*.** Estimated scale to build what `sec:quotient` needs:
- Gaussian kernel `G_s(x) = (4πs)^{-3/2}e^{-|x|²/4s}`, mass 1, scaling,
  semigroup property `G_s * G_t = G_{s+t}`: ~15 lemmas (the mass and Fourier
  computations reuse `GaussianIntegral.lean`).
- `e^{sΔ}` as a CLM on `L^p`, `L^p` contraction via Young/Jensen: ~15 lemmas.
- Strong continuity at `s = 0` on `L^p`, `p < ∞` (uses §1.3 density): ~10.
- Generator: `s ↦ e^{sΔ}u` differentiable at `0` in `L³` when `Δu ∈ L³`,
  with derivative `Δu`: ~15–20 lemmas. This is the hardest piece and is
  exactly what the manuscript's phrase *"`Δu ∈ L³` justifies this generator
  limit"* asserts.
- Commutation with `∇` / preservation of the gradient subspace `𝒢₃`: ~10.

**Total ≈ 65–80 lemmas, one new file family.** Alternatively, if Phase I keeps
the heat facts as *labelled literature axioms* (which the CP1 plan permits),
this is a Phase II item only.

---

## 4. Sobolev spaces, Sobolev embedding, Gagliardo–Nirenberg, Bernstein, Littlewood–Paley

### 4.1 Gagliardo–Nirenberg–Sobolev — **M (compact support) / M‑ (general)**

`Analysis/FunctionalSpaces/SobolevInequality.lean`, namespace `MeasureTheory`:

- `MeasureTheory.eLpNorm_le_eLpNorm_fderiv_of_eq` (:600):
  ```
  theorem eLpNorm_le_eLpNorm_fderiv_of_eq [FiniteDimensional ℝ F]
      {u : E → F} (hu : ContDiff ℝ 1 u) (h2u : HasCompactSupport u)
      {p p' : ℝ≥0} (hp : 1 ≤ p) (hn : 0 < finrank ℝ E)
      (hp' : (p' : ℝ)⁻¹ = p⁻¹ - (finrank ℝ E : ℝ)⁻¹) :
      eLpNorm u p' μ ≤ SNormLESNormFDerivOfEqConst F μ p * eLpNorm (fderiv ℝ u) p μ
  ```
  With `E := EuclideanSpace ℝ (Fin 3)`, `p := 2`, `finrank = 3`, this gives
  `p' = 6`: **exactly `‖u‖₆ ≤ C‖∇u‖₂` on `R³`**, i.e. the Sobolev embedding
  `H¹(R³) ⊂ L⁶` used in `prop:scaling` and `prop:enstrophy`.
- Companions: `eLpNorm_le_eLpNorm_fderiv_one` (:442, `q = 1`, arbitrary Banach
  codomain), `eLpNorm_le_eLpNorm_fderiv_of_eq_inner` (:469, Hilbert codomain,
  no finite-dimensionality of the codomain),
  `eLpNorm_le_eLpNorm_fderiv_of_le` (:656, bounded support, `1 ≤ p < n`),
  `eLpNorm_le_eLpNorm_fderiv` (:707), plus the constants
  `SNormLESNormFDerivOfEqConst`, `eLpNormLESNormFDerivOfEqInnerConst`,
  `eLpNormLESNormFDerivOfLeConst`.

**Gap: `HasCompactSupport u` is required.** CP1 applies the embedding to a
Schwartz-class solution `u(t) ∈ 𝓢(R³)³`, which is *not* compactly supported.
Removing the hypothesis by cutoff + §1.3 density is **M‑ / F(small)**:
**estimate 6–12 lemmas** (cutoff `u·χ(x/R)`, `‖∇(uχ_R)‖₂ → ‖∇u‖₂`, Fatou for
the `L⁶` side). No new mathematics.

**Genuine Gagliardo–Nirenberg with two derivative orders**, e.g.
`‖∇u‖₃ ≤ C‖∇u‖₂^{1/2}‖Δu‖₂^{1/2}` (the *second* displayed estimate inside the
proof of `prop:enstrophy`): **F**. Mathlib has the first-order GNS above but
no interpolation-type GN inequality. Route: `‖∇u‖₃ ≤ ‖∇u‖₂^{1/2}‖∇u‖₆^{1/2}`
(§1.2 Lyapunov) then `‖∇u‖₆ ≤ C‖∇∇u‖₂` (the GNS above applied to `∇u`) then
`‖∇²u‖₂ = ‖Δu‖₂` for Schwartz fields (Plancherel).
**Estimate 10–15 lemmas** (of which the `‖∇²u‖₂ = ‖Δu‖₂` identity via §2.2 is
the fiddly part, needing the complexification bridge).

### 4.2 Sobolev spaces as spaces — **M for `H^{s,p}` as a predicate; F for a normed Sobolev space**

`Analysis/Distribution/Sobolev.lean` (new in this era, author M. Doll) defines
Bessel-potential Sobolev spaces on tempered distributions:

- `TemperedDistribution.besselPotential (s : ℝ) : 𝓢'(E,F) →L[ℂ] 𝓢'(E,F)` (:71)
  — the multiplier `(1+‖ξ‖²)^{s/2}`;
- `TemperedDistribution.MemSobolev (s : ℝ) (p : ℝ≥0∞) [Fact (1 ≤ p)] (f : 𝓢'(E,F)) : Prop` (:149);
- `SchwartzMap.memSobolev` (:201), `memSobolev_two_iff_fourier`,
  `MemSobolev.{add,sub,neg,smul,mono}` (:157–:298),
  `MemSobolev.fourierMultiplierCLM_of_bounded` (:281),
  `MemSobolev.lineDerivOp` (:316), `MemSobolev.laplacian` (:344),
  `MemSobolev.fourier_memL1` (:241),
  `besselPotential_neg_two_laplacian_eq` (:117).

**What is missing:** `MemSobolev` is a `Prop`, not a normed space. There is
**no `H^m` norm, no completeness, no Sobolev embedding theorem `H^s ⊂ L^q`,
no product/algebra estimate, no trace, no compact embedding**. CP1 needs
"Schwartz data belong to `H^m ∩ L³` for every `m`" (`thm:continuation` proof)
and "persistence of higher Sobolev regularity" — the *statement* of the latter
belongs to the imported Tao Theorem 5.4 axiom, so the Sobolev-space
infrastructure needed inside CP1 is thin.

**Disposal:** predicate-level facts **M**; a genuine normed `H^m(R³)` with
completeness and the embedding chain **F, ≈30–50 lemmas** if CP1 elects to
state the local theory in `H^m` rather than in the Schwartz class. Keeping the
local theory in the Schwartz class (as the manuscript does) avoids this
entirely and is the recommended Phase‑I choice.

### 4.3 Bernstein inequalities — **F**

Grep `Bernstein` finds only `Analysis/SpecialFunctions/Bernstein.lean`
(Bernstein *polynomials*, Weierstrass approximation),
`Topology/ContinuousMap/Weierstrass.lean`, and unrelated
`MeasurableSpace/Embedding.lean` / `Constructions/Polish/Basic.lean` (Borel
isomorphism) and `CStarAlgebra` / `CategoryTheory` hits. **There is no
frequency-localized Bernstein inequality.**

CP1 uses Bernstein twice: `prop:lowpressure` (`‖K_J‖_∞ ≤ C2^{3J}`) and the
`sec:quotient` low-strain bound `M = C2^{5L/2}‖u₀‖₂`.

**Disposal: F. Estimate 12–20 lemmas** for the `S_L` (low-pass) form actually
needed: `‖S_L f‖_q ≤ C 2^{3L(1/p - 1/q)}‖f‖_p` and
`‖∇ S_L f‖_∞ ≤ C 2^{5L/2}‖f‖_2`, both provable directly from Young's
convolution inequality (§8) plus scaling of a fixed Schwartz kernel — i.e.
they do *not* require full Littlewood–Paley theory, only a fixed smooth
cutoff `χ(2^{-L}ξ)` and its inverse-Fourier kernel. That is the cheap route
and it is the one CP1 should take.

### 4.4 Littlewood–Paley decomposition, Besov spaces — **F\***

Grep `Littlewood`, `Paley`, `Besov` over all of Mathlib: **zero hits.**

CP1's `prop:lowpressure` and `hyp:highpressure` are stated with
"a smooth homogeneous Littlewood–Paley partition, `S_J = Σ_{j≤J} Δ_j`". For
`prop:lowpressure` alone, only `S_J` (a single smooth low-pass multiplier) is
used, and the argument never needs the dyadic partition-of-unity identity, the
almost-orthogonality, or Besov norms. So CP1 Phase II can define `S_J` as one
Fourier multiplier and never build Littlewood–Paley theory.

**Disposal: F\* if the full theory is wanted (≈150–250 lemmas: partition of
unity, `Σ Δ_j = id` in `𝓢'`, Bernstein, almost orthogonality, Besov spaces,
paraproducts). F(≈15) if CP1 restricts to the single low-pass projector `S_J`
that `prop:lowpressure` actually uses.** The manuscript's own scope supports
the cheap route; `hyp:highpressure` is unproved and therefore imposes no
formalization requirement at CP1.

---

## 5. Riesz transforms, Calderón–Zygmund, Leray projection — **F\***

Greps over the whole checkout, all returning **zero hits**:
`Riesz transform`, `rieszTransform`, `Calderon`, `Zygmund`, `CalderonZygmund`,
`Leray`, `HardyLittlewood`, `Marcinkiewicz`, `Hausdorff.*Young`, `Lorentz`,
`weakLp`/`WeakLp`, `maximalFunction`/`MaximalFunction`.
(`Analysis/InnerProductSpace/Dual.lean` is the Hilbert-space *Riesz
representation theorem* — an unrelated "Riesz".)

So Mathlib v4.33.1 has:

- **no Hardy–Littlewood maximal function** (the Vitali/Besicovitch covering
  machinery in `MeasureTheory/Covering/` exists, but no maximal operator);
- **no weak-type `L^{p,∞}` spaces, no Lorentz spaces**;
- **no Marcinkiewicz interpolation**; the only interpolation-flavoured result
  is the Hadamard three-lines theorem
  (`Analysis/Complex/Hadamard.lean:211,253`, `norm_le_interp_of_mem_verticalClosedStrip`),
  which is the analytic core of Riesz–Thorin but is not assembled into
  Riesz–Thorin;
- **no Calderón–Zygmund decomposition, no singular integral `L^p` theory**;
- **no Riesz transforms `R_j = ∂_j(-Δ)^{-1/2}`**;
- **no Leray/Helmholtz projection**, no `divergence-free` predicate, no
  `curl`, no `divergence` definition (grep `def curl`, `def divergence`:
  zero hits in `Analysis/`, `Geometry/`, `MeasureTheory/`).

**CP1 relevance.**

- `prop:pressure` fixes the normalization `p = R_iR_j(u_iu_j)`. In Phase I this
  can be *stated* as "`p` is the tempered-distribution solution of
  `-Δp = ∂_i∂_j(u_iu_j)` with `p ∈ L^{3/2}`", using
  `TemperedDistribution.fourierMultiplierCLM` — the Riesz-transform *operator*
  need never be `L^p`-bounded for the proof of `prop:pressure` as written,
  because the manuscript derives `p ∈ L² ∩ L³` from `u ∈ L²∩L⁶` by the
  standard Calderón–Zygmund bound. **That last step is the load-bearing use
  and it is F\*.**
- `sec:quotient` uses "the bounded Leray projection `ℙ` annihilates `𝒢₃`" and
  `‖ℙ‖_{L³→L³}`. **F\*.**

**Disposal and scale.**

| Sub-item | Class | Lemma estimate |
|---|---|---|
| Hardy–Littlewood maximal function + weak (1,1) | F\* | 40–60 |
| Weak-type spaces + Marcinkiewicz interpolation | F\* | 50–80 |
| Riesz–Thorin from Hadamard three lines | F | 25–40 (Hadamard already M) |
| Calderón–Zygmund decomposition + CZ operator `L^p` theory | F\* | 100–150 |
| Riesz transforms `R_j`: definition, `L²` via Plancherel, `L^p` via CZ | F\* | 40–60 |
| Leray projection `ℙ = I + ∇(-Δ)^{-1}div` on `L^p`, boundedness, annihilation of `𝒢_p` | F\* | 30–50 |

**Combined ≈ 300–440 lemmas.** This is the single largest Phase II block, and
it is unavoidable if `prop:pressure`/`prop:lowpressure`/`sec:quotient` are to
be discharged from Mathlib rather than axiomatized. **Recommendation:** in
Phase I, state the CZ/Riesz/Leray facts as clearly labelled axioms with source
records (they are genuine textbook literature, unlike the project's own open
hypotheses), and let Phase II either import the external Carleson project's
`ToMathlib` layer (§12) or build the block.

---

## 6. Vector calculus on `R³`, integration by parts, Fubini, differentiation under the integral

| Item | Class | Declarations |
|---|---|---|
| `fderiv`, `HasFDerivAt`, `ContDiff` | M | `Analysis/Calculus/FDeriv/*`, `Analysis/Calculus/ContDiff/*` |
| `gradient` (`∇`) for scalar functions on an inner-product space | M | `gradient`, `gradientWithin`, `HasGradientAt`, `toDual_gradient` — `Analysis/Calculus/Gradient/Basic.lean:74,82,127` |
| **Laplacian** | M | `InnerProductSpace.laplacian` (instance `InnerProductSpace.instLaplacian`, notation `Δ`) and `InnerProductSpace.laplacianWithin` (notation `Δ[s]`) — `Analysis/InnerProductSpace/Laplacian.lean:132` ff.; `laplacian_eq_iteratedFDeriv_orthonormalBasis` (:172), `laplacian_eq_iteratedFDeriv_stdOrthonormalBasis` (:194), linearity `ContDiffAt.laplacian_add` (:278), `laplacian_smul` (:350), `laplacian_CLM_comp_left` (:382) |
| **`divergence`** | **F** | no definition anywhere. Must be defined (`∑ i, fderiv ℝ u x (e i) i`), as the divergence theorem file does ad hoc |
| **`curl`** | **F** | no definition anywhere. Not needed by CP1 as written |
| **Divergence theorem on a box** | M | `MeasureTheory.integral_divergence_of_hasFDerivAt_off_countable` (`MeasureTheory/Integral/DivergenceTheorem.lean:266`), `…_off_countable'` (:296), `…_of_equiv` (:313), 2‑D variants (:427,:482,:503,:550). Rectangular boxes only, with faces |
| **Integration by parts on all of `R^n` (no boundary term)** | **M — key hit** | `Analysis/Calculus/LineDeriv/IntegrationByParts.lean`: `integral_bilinear_hasLineDerivAt_right_eq_neg_left_of_integrable` (:114), `integral_bilinear_hasFDerivAt_right_eq_neg_left_of_integrable` (:179), `integral_bilinear_fderiv_right_eq_neg_left_of_integrable` (:195), `integral_smul_fderiv_eq_neg_fderiv_smul_of_integrable` (:212), `integral_mul_fderiv_eq_neg_fderiv_mul_of_integrable` (:226) |
| Differentiation under the integral sign | M | `hasFDerivAt_integral_of_dominated_loc_of_lip` (`Analysis/Calculus/ParametricIntegral.lean:165`), `hasFDerivAt_integral_of_dominated_of_fderiv_le` (:210), `hasDerivAt_integral_of_dominated_loc_of_deriv_le` (:288); interval version `Analysis/Calculus/ParametricIntervalIntegral.lean:97` |
| Dominated convergence | M | `MeasureTheory.tendsto_integral_of_dominated_convergence` (`MeasureTheory/Integral/DominatedConvergence.lean:57`), `tendsto_integral_filter_of_dominated_convergence` (:67); Fatou `lintegral_liminf_le'` (`Integral/Lebesgue/Add.lean:214`) |
| Fubini on `R³ × [0,T]` | M | `MeasureTheory.integral_prod` (`Integral/Prod.lean:444`), `integral_integral` (:472), `integral_integral_swap` (:482), `integral_prod_symm` (:467); `lintegral` versions in `Lebesgue/`; `Measure.prod` |
| FTC (time integration of the energy identity) | M | `intervalIntegral.integral_eq_sub_of_hasDerivAt` (`MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean:1148`) |
| `‖∫ f‖ ≤ ∫ ‖f‖` | M | `MeasureTheory.norm_integral_le_integral_norm` (`Integral/Bochner/Basic.lean`, doc line 41) |
| **Minkowski's integral inequality** `‖∫ f(·,t) dt‖_p ≤ ∫ ‖f(·,t)‖_p dt` | **F** | absent; only the two-function Minkowski. Estimate 8–12 lemmas (duality-free proof via `lintegral` + Hölder, or via §1.4 duality once available) |
| `EuclideanSpace` measure infrastructure | M | `EuclideanSpace.volume_preserving_measurableEquiv` (`MeasureTheory/Measure/Haar/InnerProductSpace.lean:124,132,137`), `EuclideanSpace.volume_ball` (`Measure/Lebesgue/VolumeOfBalls.lean`), `isAddHaarMeasure_volume_pi` (`Measure/Lebesgue/EqHaar.lean:123`) |

**Assessment for `prop:energy` and `prop:enstrophy`.** The whole-space
integration-by-parts theorems in `LineDeriv/IntegrationByParts.lean` take
exactly the hypothesis shape the manuscript needs (integrability of `B f g`,
`B f' g`, `B f g'`, plus differentiability *on the other function's
`tsupport`*), and they were derived by Fubini from the one-dimensional case.
That means the manuscript's proof device *"first multiply by a radial cutoff,
integrate, and pass to the limit"* can be replaced by a direct application of
these theorems whenever the three integrability side conditions can be
checked — which they can, for a Schwartz-class solution. **This removes what I
expected to be a significant Phase-I cost.** For the `sec:quotient` and
`prop:pressure` arguments (which involve `|u|u`, not Schwartz functions), the
integrability conditions must still be established by hand; that is the real
work and it is **F**, ≈20–30 lemmas.

---

## 7. ODE, comparison, Grönwall — **M**

- `gronwallBound` (`Analysis/ODE/Gronwall.lean:43`), `gronwallBound_K0` (:46),
  `gronwallBound_of_K_ne_0` (:49), `hasDerivAt_gronwallBound` (:53),
  `gronwallBound_x0` (:72), `gronwallBound_ε0` (:78).
- `le_gronwallBound_of_liminf_deriv_right_le` (:112) — the scalar form used by
  CP1: `f` continuous on `Icc a b`, one-sided liminf-slope bound,
  `f a ≤ δ`, `f' x ≤ K f x + ε` ⟹ `f x ≤ gronwallBound δ K ε (x-a)`.
- `norm_le_gronwallBound_of_norm_deriv_right_le` (:134) — Banach-valued form.
- `eq_zero_of_abs_deriv_le_mul_abs_self_of_eq_zero_right` (:143).
- Trajectory comparison: `dist_le_of_trajectories_ODE` (:228),
  `dist_le_of_approx_trajectories_ODE` (:188), `..._of_mem` (:162,:208).
- Discrete Grönwall: `Analysis/ODE/DiscreteGronwall.lean`.
- **Picard–Lindelöf**: `IsPicardLindelof` (`Analysis/ODE/PicardLindelof.lean:79`),
  `ODE.FunSpace` (:143), `exists_eq_forall_mem_Icc_eq_picard` (:720);
  existence/uniqueness API in `Analysis/ODE/ExistUnique.lean`:
  `exists_eq_forall_mem_Icc_hasDerivWithinAt` (:57),
  `exists_forall_mem_closedBall_exists_eq_forall_mem_Ioo_hasDerivAt` (:145),
  `exists_eventually_eq_hasDerivAt` (:168),
  `ODE_solution_unique` (:327), `ODE_solution_unique_univ` (:341),
  `ODE_solution_unique_of_mem_Icc` (:252).
- `Analysis/ODE/Transform.lean`, `Analysis/ODE/Basic.lean`.

**CP1 relevance.** `prop:ode` is a two-line explicit computation
(`y(t)=(2C(T-t))^{-1/2}`) and needs only `HasDerivAt` and an improper
integral; **M**. The `sec:quotient` "Integration of `eq:quotient-evolution`
and Grönwall would then bound `𝒬`" step is **M** given the (unproved)
`eq:quotient-gap`. `prop:enstrophy`'s cubic comparison remark is prose, not a
proved claim, and needs nothing.

**Note.** These ODE results are for Banach-valued ODEs with locally Lipschitz
right-hand sides; they do **not** give the Navier–Stokes local theory, which
CP1 correctly imports as Tao Theorem 5.4.

---

## 8. Young's inequalities and convolution

| Item | Class | Evidence |
|---|---|---|
| Young for products (scalars) | M | `Real.young_inequality` (`Analysis/MeanInequalities.lean:507`), `Real.young_inequality_of_nonneg` (:500), `young_inequality_eq_iff_of_nonneg` (:516), `NNReal.young_inequality` (:528), `NNReal.young_inequality_real` (:533), `ENNReal` variants in the same file |
| Convolution definition and calculus | M | `MeasureTheory.convolution` (`Analysis/Convolution.lean`, notation `⋆[L,μ]`), `convolution_def` (:421), `convolution_flip` (:642), `support_convolution_subset` (:631), `ConvolutionExistsAt` API (:169–:390) |
| `L¹ * L¹ ⊂ L¹` | M | `MeasureTheory.Integrable.integrable_convolution` (`Analysis/Convolution.lean:520`), `Integrable.convolution_integrand` (:272) |
| **Young's convolution inequality `‖f*g‖_r ≤ ‖f‖_p‖g‖_q`, `1/r = 1/p+1/q-1`** | **F** | grep `eLpNorm` inside `Analysis/Convolution.lean`: **zero hits**. Only the `L¹` case and pointwise/`L^∞` bounds (`dist_convolution_le'` :725, `BddAbove.convolutionExistsAt` :353) exist |
| `L¹ * L^∞ → L^∞` (the case `prop:lowpressure` needs) | M‑ | derivable in 2–3 lemmas from `BddAbove.convolutionExistsAt` + `norm_integral_le_integral_norm` |
| Lebesgue-valued convolution | M | `MeasureTheory.mlconvolution` (`Analysis/LConvolution.lean:50`), `mlconvolution_assoc` (:130), `mlconvolution_comm` (:143) |
| Convolution smoothness (mollifiers) | M | `HasCompactSupport.contDiff_convolution_right` (`Analysis/Calculus/ContDiff/Convolution.lean:423`), `contDiffOn_convolution_right_with_param` (:333), `HasCompactSupport.hasFDerivAt_convolution_right` (:63) |
| `ContDiffBump` (mollifier family) | M | `Analysis/Calculus/BumpFunction/{Basic,Normed,InnerProduct,Convolution}.lean`; instance `hasContDiffBump_of_innerProductSpace` (`InnerProduct.lean:57`) covers `EuclideanSpace ℝ (Fin 3)`; `ContDiffBump.normed`, `contDiff_normed` (`Normed.lean:40`), `ContDiffBump.convolution_tendsto_right_of_continuous` (`Convolution.lean:98`), `ae_convolution_tendsto_right_of_locallyIntegrable` (:107) |
| Interpolation of `L^p` norms | M‑ / F(small) | §1.2 |

**Young's convolution inequality: F, estimate 12–20 lemmas.** The standard
proof needs Minkowski's integral inequality (§6, also F) or a three-fold
Hölder + Fubini argument; the latter is self-contained given the Mathlib
Hölder API and `integral_integral_swap`. This unlocks §4.3 Bernstein cheaply.

---

## 9. `ContDiff` for `ℝ × EuclideanSpace → EuclideanSpace`, chain rule for `|u|`, `∇|u|` a.e.

| Item | Class | Evidence |
|---|---|---|
| `ContDiff` on product domains, `ContDiff.comp` chain rule | M | `ContDiff.comp` (`Analysis/Calculus/ContDiff/Comp.lean:155`), `comp₂` (:425), `comp₃` (:457), `ContDiff.prodMk`, `contDiff_fst/snd` in `ContDiff/Basic.lean`. `ℝ × EuclideanSpace ℝ (Fin 3)` is a normed space; no obstacle |
| Smoothness of `x ↦ ‖x‖` away from `0` | M | `contDiffAt_norm` (`Analysis/InnerProductSpace/Calculus.lean:154`), `ContDiffAt.norm` (:158), `ContDiff.norm` (:185, hypothesis `∀ x, f x ≠ 0`), `contDiff_norm_sq` (:140), `ContDiff.norm_sq` (:144) |
| `ContDiff` of `‖x‖^p`, `p > 1` | M | `contDiff_norm_rpow` (`Analysis/InnerProductSpace/NormPow.lean:108`), `ContDiff.norm_rpow` (:124) — **exactly the `C¹` regularity of `x ↦ |x|³` / `|x|x` needed by `prop:pressure` and `sec:quotient`** |
| Smoothness of `(‖u‖²+ε)^{1/2}` (the manuscript's `r_ε`) | M | `contDiff_norm_sq` + `ContDiff.sqrt` (`InnerProductSpace/Calculus.lean:356` uses this pattern) |
| `\|·\|` in one variable | M | `Analysis/Calculus/Deriv/Abs.lean`: `contDiffAt_abs` (:30), `hasDerivAt_abs` (:73), `HasFDerivAt.abs` (:106) |
| **`∇\|u\| = 0` a.e. on `{u = 0}` for a Sobolev representative** | **F** | grep `Stampacchia`: zero hits; no a.e.-vanishing-of-gradient-on-a-level-set theorem anywhere. This is the manuscript's explicit device in the proof of `prop:pressure` |
| **`\|∇\|u\|\| ≤ \|∇u\|` a.e.** | **F** | absent |
| Mollifiers | M | §8 |

**`∇|u|` items: F, estimate 15–25 lemmas.** For CP1 as written the situation is
better than it looks: `prop:pressure` is stated for the *classical maximal
solution from Schwartz data*, so `u(t)` is smooth; the a.e. statement is only
needed on the closed zero set. For a `C¹` field, `|∇|u|| ≤ |∇u|` off the zero
set is the Cauchy–Schwarz identity `∇|u| = (u/|u|)·∇u`, and the zero-set
statement follows because `|u|` attains its minimum there. Formalizing that
(rather than the general Sobolev Stampacchia theorem) is **F, ≈10–15 lemmas**.
The manuscript's phrase *"the zero set of its Sobolev representative"* is a
strictly stronger framing than the classical solution needs; Phase I should
record which version is being encoded, because *"formal proof is not
faithfulness of the encoded statement."*

---

## 10. Flows of vector fields, volume preservation, change of variables

| Item | Class | Evidence |
|---|---|---|
| Abstract flow (`Flow τ α`) | M‑ | `Dynamics/Flow.lean:82` — a *topological* flow (`map_add`, `map_zero`), with no relation to an ODE, no smoothness, no measure |
| **Existence of the flow of a `C¹` vector field on `R³` as a family of diffeomorphisms** | **F\*** | `Analysis/ODE/ExistUnique.lean` gives pointwise integral curves and uniqueness; there is **no** assembly into a flow map `Φ_s`, no smooth dependence on the initial point, no `Φ_s ∘ Φ_t = Φ_{s+t}` for an ODE-generated flow |
| Smooth dependence on initial conditions | **F\*** | absent |
| **Volume preservation of a divergence-free flow (Liouville)** | **F\*** | grep `MeasurePreserving` inside `MeasureTheory/Function/Jacobian.lean`: zero hits. No Liouville theorem anywhere |
| Change of variables under a diffeomorphism | M | `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul` (`MeasureTheory/Function/Jacobian.lean:1213`), `lintegral_image_eq_lintegral_abs_det_fderiv_mul` (:1183), `integral_target_eq_integral_abs_det_fderiv_smul` (:1226) — hypotheses: `MeasurableSet s`, `HasFDerivWithinAt f (f' x) s x` on `s`, `InjOn f s` |
| Vector-field API on manifolds | M‑ | `Analysis/Calculus/VectorField.lean`, `Geometry/Manifold/VectorField/` (Lie bracket, pullback) — not measure-theoretic |

**CP1 relevance.** `sec:quotient`'s transport-rewriting step is stated as:
*"Freeze `u` and let `Φ_s` be its volume-preserving flow. The competitor
`q_s = DΦ_{-s}^T(q ∘ Φ_{-s})` remains in `𝒢₃` … change of variables gives …
Differentiate for both signs of `s`."* This needs, in order: (i) existence and
`C¹` smoothness of `Φ_s` for a frozen `C¹` bounded-gradient field, (ii)
`det DΦ_s = 1` from `div u = 0` (Liouville), (iii) the change-of-variables
formula (M), (iv) the fact that `q_s ∈ 𝒢₃` (an approximation statement, F),
(v) one-sided differentiability of `s ↦ ⅓∫|w + (DΦ_s^{-T} - I)q|³` at `0`.

**Disposal: F\*.** Estimate: (i) 30–45 lemmas, (ii) 15–25 (Liouville via
Jacobi's formula `∂_s det DΦ = (div u ∘ Φ) det DΦ`; the determinant derivative
`Matrix.det` differentiability exists in `Analysis/Calculus/…`/`LinearAlgebra`
but not in this packaged form), (iii) M, (iv) 10–15, (v) 10–15.
**Total ≈ 65–100 lemmas.** This is the second-largest CP1-specific block after
§5 and it is entirely in service of `sec:quotient`.

---

## 11. Ranked list of F / F\* items that CP1 Phase II would need

Ranking is by *blocking weight for CP1* — how much of the checkpoint fails to
close without it — then by cost. "Owner" names the CP1 result that needs it.

| # | Item | Class | Lemma est. | Owner in CP1 | Note |
|---|---|---|---|---|---|
| 1 | Calderón–Zygmund `L^p` theory: maximal function, weak-type spaces, Marcinkiewicz, CZ decomposition, CZ operator boundedness | F\* | 190–290 | `prop:pressure` (`p ∈ L²∩L³`), `prop:lowpressure`, `sec:quotient` (`‖ℙ‖_{L³→L³}`) | Largest block. External reuse available (§12, Carleson `ToMathlib`) |
| 2 | Riesz transforms `R_j`; the pressure normalization `p = R_iR_j(u_iu_j)`; `L^p` bounds | F\* | 40–60 | `prop:pressure`, `prop:lowpressure` | Sits on #1 |
| 3 | Leray/Helmholtz projection on `L^p`, boundedness, `ℙ|_{𝒢_p} = 0` | F\* | 30–50 | `sec:quotient` coercivity bound | Sits on #2. Partial external reuse: `uda-lab/leray-hopf` (L² only) |
| 4 | Heat semigroup `e^{sΔ}` on `L^p(R³)`: kernel, contraction, strong continuity, generator on `L³` | F\* | 65–80 | `sec:quotient` heat monotonicity and `D_𝒬 ≥ 0` | No `C₀`-semigroup theory in Mathlib at all |
| 5 | Flow of a frozen `C¹` divergence-free field + Liouville volume preservation | F\* | 65–100 | `sec:quotient` `eq:quotient-evolution` transport identity | Change of variables itself is M |
| 6 | Uniform/strict convexity of `L^p` (Clarkson) → reflexivity, weak compactness | F\* | 90–140 | `sec:quotient` existence/uniqueness of the minimizer | **Reducible to F ≈15–25** via the direct Cauchy-minimizing-sequence route (§1.4) — recommended |
| 7 | Whole-space integrability bookkeeping for `prop:pressure`: `ε`-regularization `r_ε`, cutoff removal, dominated convergence for `|u|u`, `∇\|u\|` chain rule and its zero-set behaviour | F | 30–45 | `prop:pressure` | The IBP engine is M (§6); this is the side conditions |
| 8 | Young's convolution inequality on `L^p` | F | 12–20 | `prop:lowpressure` kernel bound; Bernstein | Enables #9 |
| 9 | Low-pass multiplier `S_J` on `R³`: kernel, `‖K_J‖_∞ ≤ C2^{3J}`, Bernstein `‖∇S_Lu‖_∞ ≤ C2^{5L/2}‖u‖₂` | F | 15–25 | `prop:lowpressure`, `sec:quotient` `M = C2^{5L/2}‖u₀‖₂` | Do **not** build full Littlewood–Paley (F\*, 150–250); CP1 needs only `S_J` |
| 10 | Gagliardo–Nirenberg `‖∇u‖₃ ≤ C‖∇u‖₂^{1/2}‖Δu‖₂^{1/2}` and `‖∇²u‖₂ = ‖Δu‖₂` | F | 10–15 | `prop:enstrophy` | Sits on #11 and the GNS hit (M) |
| 11 | Lyapunov interpolation `‖f‖_r ≤ ‖f‖_p^θ‖f‖_q^{1-θ}` | F | 4–8 | `prop:scaling` `eq:L4L3`, `prop:enstrophy` | Pure Hölder algebra |
| 12 | Removing `HasCompactSupport` from `eLpNorm_le_eLpNorm_fderiv_of_eq` (Sobolev `H¹⊂L⁶` for Schwartz fields) | F | 6–12 | `prop:scaling`, `prop:enstrophy` | Cutoff + Fatou |
| 13 | `divergence` definition on `R^n` and its basic identities (`∫div F = 0` for Schwartz `F`, `div(fu) = ∇f·u + f div u`) | F | 8–15 | `prop:energy`, `prop:pressure` | No `divergence` exists in Mathlib |
| 14 | Complexification bridge for Plancherel on real `R³`-valued fields | F | 5–10 | `prop:enstrophy` (`‖∇²u‖₂=‖Δu‖₂`), any Fourier step | `Lp.fourierTransformₗᵢ` needs `InnerProductSpace ℂ F` |
| 15 | Minkowski's integral inequality | F | 8–12 | convenience for #4, #8 | Avoidable |
| 16 | Normed Sobolev space `H^m(R³)` with completeness and embeddings | F | 30–50 | only if CP1 states local theory in `H^m` | **Avoidable** by keeping the Schwartz-class formulation the manuscript already uses |

**Totals.** Taking the recommended cheap routes (#6 direct, #9 `S_J` only, #16
avoided): **≈ 570–800 lemmas** for a full Phase II discharge, of which
**≈ 320–480 (items 1–3) is the Calderón–Zygmund/Riesz/Leray block**. Excluding
that block (i.e. keeping CZ/Riesz/Leray as labelled literature axioms, which
the CP1 Phase‑I plan explicitly permits): **≈ 250–320 lemmas.**

**Phase-I-only cost** (proving manuscript-owned steps down to labelled
literature axioms, no Phase II discharge): items 7, 8, 9, 10, 11, 12, 13, 14 —
**≈ 100–160 lemmas** — plus the `sec:quotient` items 4, 5, 6, which are *not*
literature theorems in the CP1 sense but manuscript-owned analysis, so they
must be proved: **+ 145–205** (or +80–120 with the cheap #6 route).
**Phase I realistic total ≈ 250–380 lemmas.**

---

## 12. Mathlib PRs and external Lean projects that could be reused

All repository metadata below is **directly inspected** via the GitHub REST API
on 2026-09-05 (licence field, default branch, `lean-toolchain`, file tree).
Mathematical content descriptions from repository READMEs are **metadata-only**
unless marked otherwise; no external repository was cloned, built, or
audited, and **a README claim of sorry-freeness is not verification.**

| Project | URL | Licence | Toolchain | Relevance |
|---|---|---|---|---|
| **Carleson** (F. van Doorn et al.) | https://github.com/fpvandoorn/carleson | Apache-2.0 | `leanprover/lean4:v4.34.0-rc2` (pushed 2026-09-03, 110 stars) | **Highest-value reuse for block #1.** Its `Carleson/ToMathlib/` contains `HardyLittlewood.lean`, `WeakType.lean`, `LorentzType.lean`, `Rearrangement.lean`, `RealInterpolation/` (Marcinkiewicz), `Distribution.lean`, `BoundedCompactSupport.lean`, `Annulus.lean`, `DoublingMeasure.lean`, and `TwoSidedCarleson/` (CZ-kernel machinery). File tree directly inspected via the API. Toolchain is one minor version ahead of CP1's target — a backport or a target bump would be needed |
| **Leray–Hopf** (Tomoki Uda) | https://github.com/uda-lab/leray-hopf | Apache-2.0 (© 2026 Tomoki Uda; README states the licence "does not purport to license mathematical facts or theorems themselves") | `leanprover/lean4:v4.31.0-rc2`, `lakefile.toml` pins mathlib `rev = "master"` with the commit in `lake-manifest.json` (pushed 2026-08-08, 11 stars) | 117 Lean files. Directly relevant file names (tree inspected via API): `LerayHopf/R3/SobolevEmbedding.lean`, `R3/StokesFourier.lean`, `R3/DivergenceFree.lean`, `R3/SchwartzDivFreeBasis.lean`, `R3/CurlDensity*.lean`, `R3/TrilinearEstimate.lean`, `R3/FrechetKolmogorov.lean`, `R3/RellichBall.lean`, `R3/AubinLions*.lean`, `R3/EnergyWeakLsc.lean`, `Torus/Leray.lean`, `Analysis/LpInterpolation.lean`, `Analysis/FourierParseval.lean`, `Analysis/BoundedMultiplier.lean`, `Bochner/GelfandTriple.lean`, `Bochner/TimeSobolev*.lean`. **Critical scope caveat:** this formalizes *Leray–Hopf weak* solutions with the energy *inequality*, on 𝕋³ and ℝ³, homogeneous. That is a **different solution class** from CP1's maximal classical/mild branch, and the project README explicitly disclaims smoothness, regularity, and uniqueness. Reuse is **infrastructure only** (`LpInterpolation`, `BoundedMultiplier`, `SobolevEmbedding`, the `L²` Leray projector); no CP1 statement may be imported from it |
| **DeGiorgi** (S. Armstrong) | https://github.com/scottnarmstrong/DeGiorgi | Apache-2.0 | `leanprover/lean4:v4.29.0-rc6` (pushed 2026-04-08, 39 stars) | De Giorgi–Nash–Moser theory, ~56k lines per the accompanying paper arXiv:2604.05984 (**metadata-only**: I did not fetch the paper). Contains weak derivatives and Sobolev-space infrastructure defined by integration by parts against `C_c^∞` test functions. Relevant to block #16 and to a weak-derivative formulation of `∇\|u\|` (block #7/#9) |
| **sqg-lean-proofs-fourier** (Brsanch) | https://github.com/Brsanch/sqg-lean-proofs-fourier | MIT | `leanprover/lean4:v4.29.0` (pushed 2026-07-05, 0 stars) | README: "Classical Fourier analysis in Lean 4: Littlewood–Paley, paraproducts, Kato–Ponce commutator, Sobolev embeddings for 𝕋²." **Directly on the 2-torus, not `R³`**, 0 stars, unreviewed. Relevant in principle to block #9/Littlewood–Paley but the domain mismatch and the absence of any review make this **not recommended for reuse without a full audit** |
| **SobolevSlobodeckij** (M. Grunweg) | https://github.com/grunweg/SobolevSlobodeckij | **no licence file** | `leanprover/lean4:v4.30.0` (pushed 2026-06-04) | Fractional Sobolev spaces, explicitly "for mathlib". No licence ⇒ **not reusable** as-is |
| **rellich-kondrachov** (A. Benenson) | https://github.com/abenenson/rellich-kondrachov | Apache-2.0 | (pushed 2026-05-14) | Compact `H¹→L²` embedding on compact Riemannian manifolds — **compact manifolds, not `R³`**; not applicable to CP1 |
| **LeanMillenniumPrizeProblems** (lean-dojo) | https://github.com/lean-dojo/LeanMillenniumPrizeProblems | Apache-2.0 | not inspected | Contains `Problems/NavierStokes/Millennium.lean` with `MillenniumNavierStokes.clay_prize_navier_stokes`, marked **Open**, ending in `sorry`, following the Clay PDF. Useful **only** as a comparator for the statement of `def:target` in a Palomar `Challenge.lean`; it proves nothing |

**Repositories found by GitHub search that must NOT be used.** The search for
`Navier-Stokes language:Lean` also returns
`MAGNAKA-DIBA-MBOUDY/magnaka_ns3d` (no licence),
`AEjonanonymous/Navier-Stokes` (MIT), `DavidFox998/navier-stokes` (no licence;
README claims an "unconditional proof of Navier-Stokes global regularity
**and** mass gap for SU(3)"), `BenFrohman/NS_Millennium_Proof`,
`theadamsfamily1981-max/proof_foundry`, `jcamlin/iDNS-Lean4-Mathlib4`,
`navindutta/navier-stokes-3d-bkm-lean4`. Each claims a regularity result the
literature does not contain; several claim several unrelated Millennium
problems at once. **These are claim-bearing artefacts, not verified sources,
and none may be cited, imported, or treated as evidence.** Recorded here so
that a later worker does not rediscover them as apparent prior art.

**Mathlib PRs.** I did not query the Mathlib PR queue (no primary source was
fetched), so I record **no** PR claims. The one strong signal from the
checkout itself is that `Analysis/Distribution/{Sobolev,FourierMultiplier,
TemperedDistribution}.lean` and `Analysis/Fourier/LpSpace.lean` are recent,
single-author (M. Doll) additions with `Copyright (c) 2025/2026` headers,
i.e. this area of Mathlib is under active development and the Bessel-potential
Sobolev API is likely to grow before Phase II starts. **A re-survey
immediately before Phase II begins is required; this note is a snapshot of
`v4.33.1` and nothing else.**

---

## 13. Summary table

| Item (task numbering) | Class | One-line disposition |
|---|---|---|
| (1) `Lp`, norms, Hölder, Minkowski | **M** | `MeasureTheory.Lp`, `eLpNorm_add_le`, `HolderTriple` family |
| (1) density of smooth cpt supp in `L^p` | **M** | `SchwartzMap.denseRange_toLpCLM` (Schwartz dense in `L^p`, `p<∞`) |
| (1) strict/uniform convexity (Clarkson) | **F\*** | zero hits; no `Lp` convexity instance |
| (1) reflexivity | **F\*** | no reflexivity class at all in Mathlib |
| (1) Banach–Alaoglu | **M** | `WeakDual.isCompact_closedBall`, `isSeqCompact_closedBall` |
| (1) weak lsc of norms | **F** | only a.e.-Fatou version `eLpNorm'_lim_le_liminf_eLpNorm'` |
| (1) projection onto closed convex sets | **M in Hilbert / F\* in `L^p`** | `exists_norm_eq_iInf_of_complete_convex` |
| (2) `SchwartzMap`, derivatives | **M** | `SchwartzSpace/{Basic,Deriv}.lean`, incl. Schwartz IBP |
| (2) Fourier on `𝓢` and `L²` (Plancherel) | **M** | `Lp.fourierTransformₗᵢ`, `Lp.norm_fourier_eq` (needs ℂ-inner-product codomain) |
| (2) Fourier multipliers | **M on `𝓢`/`𝓢'` / F on `L^p`** | `fourierMultiplierCLM`; no `L^p` multiplier theorem |
| (3) heat kernel / semigroup / generator | **F\*** | nothing; no `C₀`-semigroup theory |
| (4) Sobolev spaces | **M as a predicate / F as a normed space** | `TemperedDistribution.MemSobolev` |
| (4) Sobolev embedding `H¹(R³)⊂L⁶` | **M** (compact support) / **M‑** (general) | `MeasureTheory.eLpNorm_le_eLpNorm_fderiv_of_eq` |
| (4) Gagliardo–Nirenberg (interpolation type) | **F** | first-order GNS only |
| (4) Bernstein | **F** | no frequency-localized Bernstein |
| (4) Littlewood–Paley | **F\*** | zero hits |
| (5) Riesz transforms | **F\*** | zero hits |
| (5) Calderón–Zygmund | **F\*** | zero hits; no maximal function, no Marcinkiewicz |
| (5) Leray projection | **F\*** | zero hits |
| (6) `fderiv`, laplacian | **M** | `InnerProductSpace.laplacian` (`Δ`) |
| (6) divergence, curl | **F** | no definitions |
| (6) divergence theorem on boxes | **M** | `integral_divergence_of_hasFDerivAt_off_countable` |
| (6) IBP on all of `R^n` | **M** | `integral_bilinear_fderiv_right_eq_neg_left_of_integrable` |
| (6) differentiation under the integral | **M** | `hasFDerivAt_integral_of_dominated_of_fderiv_le` |
| (6) dominated convergence, Fubini | **M** | `tendsto_integral_of_dominated_convergence`, `integral_integral_swap` |
| (7) Grönwall | **M** | `gronwallBound`, `norm_le_gronwallBound_of_norm_deriv_right_le` |
| (7) Picard–Lindelöf, ODE uniqueness | **M** | `IsPicardLindelof`, `ODE_solution_unique` |
| (8) Young for products | **M** | `Real.young_inequality` |
| (8) Young for convolution | **F** | only `L¹*L¹⊂L¹` |
| (8) interpolation of `L^p` norms | **F(small)** | no Lyapunov inequality |
| (9) `ContDiff` on `ℝ×EuclideanSpace`, chain rule | **M** | `ContDiff.comp` |
| (9) chain rule for `\|u\|` away from `0` | **M** | `contDiffAt_norm`, `ContDiff.norm_rpow` |
| (9) a.e. gradient of `\|u\|` on its zero set | **F** | no Stampacchia-type theorem |
| (9) mollifiers, convolution smoothness | **M** | `ContDiffBump`, `HasCompactSupport.contDiff_convolution_right` |
| (10) flows of vector fields | **F\*** | only topological `Flow`; no ODE flow map |
| (10) volume preservation (Liouville) | **F\*** | zero hits |
| (10) change of variables under diffeomorphisms | **M** | `integral_image_eq_integral_abs_det_fderiv_smul` |

---

## Frontier record

**MODE / RESULT:** SURVEY. Mathlib `v4.33.1`
(commit `0df444a360eaa60ab8c11dca51a86af692955474`) was searched declaration by
declaration against the CP1 prerequisite list. Every item was disposed as M,
M‑, F, or F\* with cited declarations and file:line locations. No mathematical
claim about Navier–Stokes was made, tested, or repaired.

**HEADLINE:** CP1's *classical* estimates are much better served by
`v4.33.1` than expected — whole-space integration by parts
(`Analysis/Calculus/LineDeriv/IntegrationByParts.lean`), density of Schwartz
functions in `L^p` (`SchwartzMap.denseRange_toLpCLM`), Gagliardo–Nirenberg–Sobolev
(`MeasureTheory.eLpNorm_le_eLpNorm_fderiv_of_eq`), Plancherel on `L²`
(`MeasureTheory.Lp.fourierTransformₗᵢ`), the Laplacian
(`InnerProductSpace.laplacian`), Grönwall, and Picard–Lindelöf are all present.
The *critical-space* machinery is absent wholesale: **no Riesz transform, no
Calderón–Zygmund theory, no Hardy–Littlewood maximal function, no Marcinkiewicz
interpolation, no Leray projection, no heat semigroup, no `L^p` reflexivity or
uniform convexity, no Littlewood–Paley, no ODE flow map, no Liouville theorem.**

**FIRST GAP (for this lane):** the three ingredients the manuscript names in
`sec:quotient` for existence and uniqueness of the `L³` gradient-quotient
minimizer — reflexivity, weak lower semicontinuity, strict convexity — are
*each* absent from Mathlib v4.33.1. A Phase II that discharges `sec:quotient`
from Mathlib must either build Clarkson → uniform convexity → reflexivity
(≈90–140 lemmas) or replace the direct-method argument by the uniform-convexity
Cauchy-sequence argument sketched in §1.4 (≈15–25 lemmas). **The second route
is a change of proof, not of statement, and must be re-audited against the
HF17 review before it is adopted.**

**SURVIVING CONDITIONAL SUFFIX:** conditional on (a) the CZ/Riesz/Leray block
being carried as labelled literature axioms in Phase I, and (b) the local
theory being kept in the Schwartz class rather than in `H^m`, Phase I for CP1
is estimated at **≈250–380 lemmas** of new Lean, and a full Phase II discharge
at **≈570–800**. These are engineering estimates from declaration counts and
standard textbook proof lengths; they carry no confidence interval and are not
evidence about the mathematics.

**FALSIFIERS for this note:** (i) any declaration cited above that does not
elaborate when actually applied to `EuclideanSpace ℝ (Fin 3)` — nothing here
was compiled; (ii) a Mathlib declaration I failed to find by keyword, in
particular anything named without the English word I grepped for; (iii) a
version drift — `Analysis/Distribution/*` is under active single-author
development and a re-survey is mandatory before Phase II starts; (iv) any
external repository above whose README claims exceed its verified content.

**NON-CLAIMS:** no claim that any CP1 step is true, provable, or formalizable
as stated; no claim that `hyp:critical`, `hyp:absorption`, `hyp:highpressure`,
or `eq:quotient-gap` is provable; no claim about NS-R3, which remains OPEN; no
claim that any external Lean project's content is correct, sorry-free, or
importable; no claim that a Mathlib hit constitutes verified applicability.
