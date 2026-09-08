# CP04 Phase I design: package R, energy/pressure statements, literature axioms, module plan

Status: DESIGN (design lane of wave CP04), 2026-09-05. Owner file: this one only.
Repository state read: `navier-formal` at `54f8e89` (Lean v4.33.1, Mathlib
`v4.33.1`); paper texts `cp02-local-theory.md`, `cp02-continuation.md`,
`cp02-energy-enstrophy.md`, `cp02-pressure.md`, `cp02-lowpressure.md`,
`cp02-quotient-*.md`; design/critic records `cp01-lean-statement-design.md`,
`cp01-critic.md` (K2, K4–K7, K14); `docs/paper-lean-specification.md`,
`docs/literature-assumptions.yaml`, `AGENTS.md`.

Every fenced Lean block below marked **[elaborated]** was checked verbatim (as
one file, imports `NavierFormal.SolutionClass`, `NavierFormal.IBP`,
`Mathlib.Analysis.Convolution`, `Mathlib.Analysis.Fourier.LpSpace`,
`Mathlib.Analysis.Distribution.SchwartzSpace.Basic`,
`Mathlib.MeasureTheory.Function.L2Space`,
`Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus`; opens
`MeasureTheory Filter Topology` and scoped `ENNReal ContDiff
RealInnerProductSpace Laplacian Convolution SchwartzMap`; `noncomputable
section`; `namespace NavierFormal`; `variable {F : Type*} [NormedAddCommGroup F]
[NormedSpace ℝ F]`) with `lake env lean` against the pinned Mathlib: zero
errors, zero `sorry` in any definition; the only `sorry`s are the five batch
*theorem statements* of §4, which are the proof obligations of the batch. Blocks
marked **[shape]** were not elaborated and are indicative. Mathlib names quoted
in prose were grepped in `.lake/packages/mathlib` at the pinned revision.

Nothing here asserts a Millennium-problem claim; nothing here changes the
manuscript. The Phase I rule applied throughout: every manuscript-owned step is
a Lean theorem; an axiom is a cited published theorem *stated as published*,
living in the non-default library, never in a Challenge import closure.

---

## 1. Package R: faithful encoding of `prop:localtheory`(iii)

### 1.1 What the paper states and what the lanes consume

`prop:localtheory`(iii) (cp02-local-theory §2.2): for every `0 < T < T_*` and
all `j,k ≥ 0`, `u ∈ C^j([0,T];H^k(ℝ³;ℝ³))`, `p ∈ C^j([0,T];H^k(ℝ³))`, *the
`H^k`-valued time derivatives being the classical ones*; all derivatives
`∂_t^j∂_x^α u`, `∂_t^j∂_x^α p` are bounded on `[0,T]×ℝ³`; and `∂_t^j u,
∂_t^j p ∈ L^∞_tH^k`. `cor:Lq` adds: `u, ∇u, Δu, ∂_tu, p, ∇p ∈ C([0,T];L^q)` for
every `2 ≤ q ≤ ∞` (for `q = ∞` with the functions themselves).

Consumers (exact memberships they cite):

| lane | membership used | where |
|---|---|---|
| energy (`lem:R-consequences`) | `u ∈ C¹([0,T];L²)` (difference quotients converge in `L²` to `u_t`, a.e. equal to `∂_tu`); `Δu, (u·∇)u, ∇p ∈ L²` at each `t`; `u(t) ∈ L³ ∩ L⁴ ∩ L^∞`, `∇u(t) ∈ L²`, `p(t) ∈ L²`, `∇p(t) ∈ L²`; `∇u ∈ C([0,T];L²)` (Step 5: continuity of `τ ↦ ‖∇u(τ)‖₂²`) | proof of `prop:energy` Steps 1–5 |
| pressure (R2)–(R3) | `u,p ∈ C^∞([0,T]×ℝ³)`, equation pointwise, `u(0) = u₀`; `u ∈ C([0,T];L^q)`, `q ∈ {2,3,4,∞}`; `∇u ∈ C([0,T];L²)`; `p ∈ C([0,T];L²) ∩ C([0,T];L^∞)` (section constants `K_q, G, Π_q`) | `prop:pressure` Step 1–4 |
| continuation (R1)–(R2) | `u,p ∈ C^j([0,T];H^k)` all `j,k`; `u,∇u,p,∇p,Δu,∂_tu ∈ C([0,T];L^q)`, `2 ≤ q ≤ ∞`; smoothness with bounded derivatives; `u ∈ C¹([0,T];H²)` hence `∇u ∈ C¹([0,T];L²)` with `∂_t∇u = ∇∂_tu` (Serrin Step 1); `t ↦ ‖u(t)‖₃` continuous | `lem:nu-normalisation`, `lem:leray-hopf`, `lem:serrin-enstrophy`, `thm:continuation` |

### 1.2 Evaluation of the proposal

Proposal: for each `j,k`, `t ↦ MemLp.toLp (iteratedFDeriv ℝ k (timeDerivIter j u t))`
into `Lp _ 2 volume` is continuous on `Set.Icc 0 T`.

Assessment.

1. **Mathematically right.** `H^k` membership is "all spatial derivatives of
   order `≤ k` in `L²`" (`lem:sobolev-norms`, `lem:hk`), and since the
   condition is imposed for every `k`, quantifying over the single order `k`
   per clause covers `H^k` for all `k`; continuity into `H^k` is continuity of
   each order into `L²` (the classical `H^k` norm is the finite sum). Mathlib's
   `Lp (Space [×k]→L[ℝ] Space) 2 volume` is a `NormedAddCommGroup` (via
   `Fact (1 ≤ 2)`), so `C([0,T];H^k)` is encodable without a Sobolev type.
   Mathlib's `TemperedDistribution.memSobolev` is not suitable: it needs a
   `NormedSpace ℂ` codomain and a tempered-distribution term for each field.
2. **Spelling defect.** `MemLp.toLp f hf` needs the proof `hf` inside the
   map; writing the curve as `fun t => (h t).toLp _` forces a dependent
   hypothesis `h : ∀ t, MemLp …` into the definition. Fix: quantify the curve
   existentially, `∃ f : ℝ → Lp F 2 volume, ContinuousOn f (Icc 0 T') ∧ ∀ t ∈
   Icc 0 T', ⇑(f t) =ᵐ g t`. This is equivalent (an `Lp` class representing
   `g t` exists iff `MemLp (g t) 2`, and is then `toLp`), and it is what every
   consumer needs (`MemLp.coeFn_toLp`-style a.e. identification).
3. **Missing content vs. (iii).** Continuity into `H^k` of every `∂_t^j u`
   does not *by itself* state that the `H^k`-valued derivative of `t ↦ u(t)`
   is `∂_tu`; the paper states it and `lem:R-consequences`(a) uses it. Add the
   `L²`-differentiability clause (`HasDerivWithinAt` of the `Lp`-curve with the
   derivative curve representing `∂_t^{j+1}u`). Also add (iii)'s "all
   derivatives bounded on `[0,T]×ℝ³`" and `cor:Lq`'s `q = ∞` case (uniform
   sup-norm continuity): both are paper conclusions, and without them the
   energy/pressure lanes would need the Sobolev embedding `H² ⊂ L^∞` (not in
   Mathlib; Fourier route, F item) to get `L^∞` and `L^q` control. With them,
   `L^q` continuity for `2 ≤ q < ∞` is a two-line interpolation with the
   existing `NavierFormal.eLpNorm_interpolate_top`.
4. **Comparison with the current `RegularityPackage`** (`SolutionClass.lean`):
   that predicate is a `t`-uniform bound on `eLpNorm (iteratedFDeriv ℝ k
   (timeDerivIter j ·)) 2` on `[0,T']`, i.e. `L^∞_tH^k` at every `t` and
   nothing else (fidelity gap R-REG in `paper-lean-specification.md`): no
   continuity, no differentiability, no measurability, no sup bounds. It is
   *implied* by the new package (a continuous `Lp`-curve on a compact interval
   is bounded) and is kept as a derived fact, not deleted (docs reference it).

Decision: **new name `RegularityPackage'`, structure with six fields**, old
`RegularityPackage` retained and derived. Joint smoothness on the closed slab
`Icc 0 T' ×ˢ univ` is included because (iii)+(R2) state it and because
`IsClassicalSolution` only gives smoothness on the open slab plus continuity
up to `t = 0`.

### 1.3 The definitions [elaborated]

```lean
/-- `g ∈ C([0,T'];L²)`: a continuous curve in `L²` represents `g t` for every `t ∈ [0,T']`. -/
def IsContL2On (T' : ℝ) (g : ℝ → Space → F) : Prop :=
  ∃ f : ℝ → Lp F 2 (volume : Measure Space),
    ContinuousOn f (Set.Icc 0 T') ∧ ∀ t ∈ Set.Icc 0 T', (⇑(f t) : Space → F) =ᵐ[volume] g t

/-- `g ∈ C¹([0,T'];L²)` with `L²`-derivative represented by `g'`. -/
def IsC1L2On (T' : ℝ) (g g' : ℝ → Space → F) : Prop :=
  ∃ f f' : ℝ → Lp F 2 (volume : Measure Space),
    ContinuousOn f' (Set.Icc 0 T') ∧
    (∀ t ∈ Set.Icc 0 T', HasDerivWithinAt f (f' t) (Set.Icc 0 T') t) ∧
    (∀ t ∈ Set.Icc 0 T', (⇑(f t) : Space → F) =ᵐ[volume] g t ∧
      (⇑(f' t) : Space → F) =ᵐ[volume] g' t)

/-- Uniform sup-norm continuity (`cor:Lq`, `q = ∞`) of a family of fields on `[0,T']`. -/
def IsUnifContOn (T' : ℝ) (g : ℝ → Space → F) : Prop :=
  ∀ t₀ ∈ Set.Icc 0 T', ∀ ε > 0, ∀ᶠ t in 𝓝[Set.Icc 0 T'] t₀, ∀ x, ‖g t x - g t₀ x‖ ≤ ε

/-- Package `R` (`prop:localtheory`(iii) and `cor:Lq`): `u, p ∈ C^j([0,T'];H^k)` for all
`j, k`, with the `H^k`-valued time derivatives the classical ones, all derivatives bounded
and uniformly continuous in time, and joint smoothness on the closed slab. -/
structure RegularityPackage' (T : ℝ) (u : ℝ → Space → Space) (p : ℝ → Space → ℝ) : Prop where
  c1_u : ∀ (j k : ℕ) (T' : ℝ), 0 ≤ T' → T' < T →
    IsC1L2On T' (fun t => iteratedFDeriv ℝ k (timeDerivIter j u t))
      (fun t => iteratedFDeriv ℝ k (timeDerivIter (j + 1) u t))
  c1_p : ∀ (j k : ℕ) (T' : ℝ), 0 ≤ T' → T' < T →
    IsC1L2On T' (fun t => iteratedFDeriv ℝ k (timeDerivIter j p t))
      (fun t => iteratedFDeriv ℝ k (timeDerivIter (j + 1) p t))
  bounded_u : ∀ (j k : ℕ) (T' : ℝ), 0 ≤ T' → T' < T → ∃ C : ℝ,
    ∀ t ∈ Set.Icc 0 T', ∀ x, ‖iteratedFDeriv ℝ k (timeDerivIter j u t) x‖ ≤ C
  bounded_p : ∀ (j k : ℕ) (T' : ℝ), 0 ≤ T' → T' < T → ∃ C : ℝ,
    ∀ t ∈ Set.Icc 0 T', ∀ x, ‖iteratedFDeriv ℝ k (timeDerivIter j p t) x‖ ≤ C
  smooth_u : ∀ T', 0 ≤ T' → T' < T →
    ContDiffOn ℝ ∞ (fun q : ℝ × Space => u q.1 q.2) (Set.Icc 0 T' ×ˢ (Set.univ : Set Space))
  smooth_p : ∀ T', 0 ≤ T' → T' < T →
    ContDiffOn ℝ ∞ (fun q : ℝ × Space => p q.1 q.2) (Set.Icc 0 T' ×ˢ (Set.univ : Set Space))
```

Amendment to the elaborated block (add two fields; same shape as `bounded_*`,
elaborates identically since `IsUnifContOn` elaborated in the same file):

```lean
  unifCont_u : ∀ (j k : ℕ) (T' : ℝ), 0 ≤ T' → T' < T →
    IsUnifContOn T' (fun t => iteratedFDeriv ℝ k (timeDerivIter j u t))
  unifCont_p : ∀ (j k : ℕ) (T' : ℝ), 0 ≤ T' → T' < T →
    IsUnifContOn T' (fun t => iteratedFDeriv ℝ k (timeDerivIter j p t))
```

`cor:Lq` target predicate [elaborated]:

```lean
/-- `cor:Lq`: continuity of `t ↦ g t` into `L^q` on `[0,T']`, `2 ≤ q < ∞`, in `eLpNorm` form. -/
def IsContLqOn (q : ℝ≥0∞) (T' : ℝ) (g : ℝ → Space → F) : Prop :=
  (∀ t ∈ Set.Icc 0 T', MemLp (g t) q volume) ∧
  ∀ t₀ ∈ Set.Icc 0 T',
    Tendsto (fun t => eLpNorm (fun x => g t x - g t₀ x) q volume) (𝓝[Set.Icc 0 T'] t₀) (𝓝 0)
```

Encoding notes. (a) `timeDerivIter j u` is the existing `derivWithin … (Ici
0)` iterate; on `[0,T']` with `T' < T` and `u` smooth on the open slab the
derivative within `Ici 0` is the ordinary derivative for `t > 0`
(`timeDeriv_eq_deriv`) and the right derivative at `0`, which is what
`C^j([0,T];·)` means one-sided (`lem:upgrade`(b), conventions paragraph). (b)
`iteratedFDeriv ℝ k` is the classical `k`-th derivative; on the classical
class it is the distributional one (`lem:classical`), so the derivative-form
`H^k` is Tao's Fourier-side `H^k` up to the constants of `lem:sobolev-norms`
(finiteness and continuity are norm-independent). (c) `HasDerivWithinAt … (Icc
0 T') t` is one-sided at both endpoints, as in the paper. (d) `F` is generic so
that `u : ℝ → Space → Space` and `p : ℝ → Space → ℝ` share the definitions.

### 1.4 Derived-facts lemma list (file `NavierFormal/PackageFacts.lean`, §4 batch item 1)

Each is Mathlib-provable from `RegularityPackage'` alone; the manuscript label
each serves is given.

| # | Lean statement (shape) | manuscript sentence | proof route |
|---|---|---|---|
| D1 | `RegularityPackage'.toRegularityPackage : RegularityPackage' T u p → RegularityPackage T u p` | (iii) `∂_t^ju ∈ L^∞_tH^k` | continuous curve on `Icc` is bounded (`IsCompact.exists_bound_of_continuousOn`); `eLpNorm (g t) 2 = ‖f t‖ₑ` via `Lp.norm_def`/`eLpNorm_congr_ae` |
| D2 | `memLp_two_of_package : ∀ j k, ∀ t ∈ Icc 0 T', MemLp (iteratedFDeriv ℝ k (timeDerivIter j u t)) 2 volume` (and for `p`) | `u(t),∇u(t),∇²u(t),∂_tu(t),p(t),∇p(t) ∈ L²` | `Lp.memLp (f t)` transported along `=ᵐ` (`MemLp.ae_eq`) |
| D3 | `isContL2On_of_package : IsContL2On T' (fun t => iteratedFDeriv ℝ k (timeDerivIter j u t))` | `u,∇u,Δu,∂_tu,p,∇p ∈ C_tL²` | projection of `IsC1L2On` (`f'` continuous gives the `j+1` case; `f` differentiable hence continuous gives the `j` case) |
| D4 | `isContLqOn_of_L2_sup : Continuous (g t) → IsContL2On T' g → (∃ C, ∀ t ∈ Icc 0 T', ∀ x, ‖g t x‖ ≤ C) → IsUnifContOn T' g → 2 ≤ q → q ≠ ∞ → IsContLqOn q T' g` | `cor:Lq`, `lem:embedding`(c) | `NavierFormal.eLpNorm_interpolate_top` on the difference `g t - g t₀` with `p = 2`, `r = q`: `‖·‖_q ≤ ‖·‖₂^{2/q}‖·‖_∞^{1−2/q}`; `eLpNorm_le_of_ae_bound` for the `∞` factor |
| D5 | `isContLqOn_velocity : ∀ q, 2 ≤ q → q ≠ ∞ → IsContLqOn q T' u`; likewise for `fun t => fderiv ℝ (u t)`, `fun t => Δ (u t)`, `timeDeriv u`, `p`, `fun t => gradient (p t)` | `cor:Lq` list | D3, `bounded_*`, `unifCont_*`, D4; `iteratedFDeriv ℝ 1 f x` vs `fderiv ℝ f x`: `‖iteratedFDeriv ℝ 1 f x‖ = ‖fderiv ℝ f x‖` (`norm_iteratedFDeriv_fderiv` with `n = 0`, `norm_iteratedFDeriv_zero`); `‖Δ f x‖ ≤ 3‖fderiv ℝ (fderiv ℝ f) x‖` (`IBP.norm_laplacian_le`) |
| D6 | `continuousOn_enstrophy : ContinuousOn (fun t => ∫ x, enstrophyDensity (u t) x) (Icc 0 T')` | `prop:energy` Step 5 "`∇u ∈ C([0,T];L²)`" | `enstrophyDensity = ∑ j ‖fderiv ℝ (u t) x (e j)‖²`; each `x ↦ fderiv ℝ (u t) x (e j)` is `ContinuousLinearMap.apply … (e j)` of the `k = 1` curve; `‖·‖₂²` is continuous on `Lp` |
| D7 | `hasDerivWithinAt_kineticEnergy : HasDerivWithinAt (fun t => kineticEnergy (u t)) (2 * ∫ x, ⟪u t x, timeDeriv u t x⟫) (Icc 0 T') t` | `prop:energy` Step 1 (`E'(τ) = ∫ u·u_t`) | `kineticEnergy (u t) = ‖f t‖²` (`MeasureTheory.L2.inner_def`, `inner_self_eq_norm_sq`); derivative of `‖f‖²` along `HasDerivWithinAt f (f' t)` (`HasDerivWithinAt.inner`); identify `∫ ⟪f t, f' t⟫` with `∫ ⟪u t, ∂_tu t⟫` by `integral_congr_ae` |
| D8 | IBP suppliers at fixed `t ∈ Icc 0 T'`: `Integrable (fun x => ‖p t x‖ * ‖u t x‖)`, `Integrable (fun x => ‖p t x‖ * ‖fderiv ℝ (u t) x‖)`, `Integrable (fun x => ‖fderiv ℝ (p t) x‖ * ‖u t x‖)`, `Integrable (fun x => ‖u t x‖ * ‖fderiv ℝ (u t) x‖)`, `Integrable (enstrophyDensity (u t))`, `Integrable (fun x => ‖u t x‖ * ‖fderiv ℝ (fderiv ℝ (u t)) x‖)`, `Integrable (fun x => ‖u t x‖ ^ 3)`, `Integrable (fun x => ‖u t x‖ ^ 2 * ‖fderiv ℝ (u t) x‖)` | `lem:R-consequences`(c), the integrability list of `IBP.lean` | products of two `L²` functions are `L¹` (`MemLp.integrable_mul`/`MemLp.mul` with `HolderTriple 2 2 1`); `‖u‖³ ∈ L¹` from `u ∈ L³` (`MemLp.integrable_norm_rpow`); `‖u‖²‖∇u‖` from `u ∈ L⁴`, `∇u ∈ L²`; Frobenius vs operator norm via `frobeniusNormSq_le_three_mul` |
| D9 | `RegularityPackage'.mono : RegularityPackage' T u p → T'' ≤ T → RegularityPackage' T'' u p` | restriction used in `thm:conditional` | as `RegularityPackage.mono` |
| D10 | `RegularityPackage'.nuNormalization` (§4 batch item 5) | `lem:nu-scaling`(a), `lem:nu-normalisation`(ii) | chain rule for the affine time change on `timeDerivIter` (`∂_s^j v(s) = ν^{-1-j}(∂_t^ju)(s/ν)`), composition of the `Lp` curves with `s ↦ s/ν`, `‖ν⁻¹•·‖` scaling of `eLpNorm` |

How each consumer need follows: `u ∈ C¹_tL²` = `c1_u 0 0`; `u_t ∈ C_tL²` =
D3 at `j = 1, k = 0` (or the `f'` of `c1_u 0 0`); `∇u ∈ C_tL²` = D3 at `k =
1`; `Δu ∈ C_tL²` = D3 at `k = 2` composed with the trace; `p ∈ C_t(L² ∩ L^∞)`
= D3 (`p`, `j = k = 0`) with `bounded_p`/`unifCont_p`; `u ∈ C_tL^q`, `2 ≤ q ≤
∞` = D5 (the `q = ∞` case is `unifCont_u`+`bounded_u` verbatim).

---

## 2. Statements of `prop:energy` and `prop:pressure`

### 2.1 Energy identity [elaborated]

The paper (cp02-energy-enstrophy, `prop:energy`): for every `0 ≤ s ≤ t < T_*`,
`½‖u(t)‖₂² + ν∫_s^t‖∇u(τ)‖₂²dτ = ½‖u(s)‖₂²`, with `|∇u|² = Σ_{i,j}|∂_ju_i|²`
(Frobenius; conventions paragraph). Its proof uses only (iii) memberships,
so the Lean hypothesis is the package, not the branch.

```lean
theorem energy_identity {ν T : ℝ} {u₀ : Space → Space} {u : ℝ → Space → Space}
    {p : ℝ → Space → ℝ} (hν : 0 < ν) (hs : IsClassicalSolution ν u₀ T u p)
    (hR : RegularityPackage' T u p) :
    ∀ s t : ℝ, 0 ≤ s → s ≤ t → t < T →
      (∀ τ ∈ Set.Icc 0 t, Integrable (fun x => ‖u τ x‖ ^ 2) volume ∧
        Integrable (enstrophyDensity (u τ)) volume) ∧
      IntervalIntegrable (fun τ => ∫ x, enstrophyDensity (u τ) x) volume s t ∧
      (1 / 2 : ℝ) * kineticEnergy (u t) + ν * ∫ τ in s..t, ∫ x, enstrophyDensity (u τ) x
        = (1 / 2 : ℝ) * kineticEnergy (u s)
```

(Elaborated as the `Prop` `EnergyIdentityStatement` quantifying the same
binders; the theorem form differs only by binder placement.) The two
integrability conclusions make the Bochner integrals non-junk (risk R-JUNK):
`kineticEnergy` is `∫ ‖v x‖²`, `∫ x, enstrophyDensity` is `‖∇u(τ)‖₂²` in the
Frobenius convention (`enstrophyDensity = frobeniusNormSq (fderiv ℝ v x)`),
exactly the identity with the norm the paper uses (R-NORM: the identity is
false with the operator norm; `IBP.integral_inner_laplacian_eq_neg_integral_enstrophyDensity`
already carries the Frobenius density). Consequences
(`prop:energy` second sentence), same file:

```lean
theorem energy_bound (hν) (hs) (hR) : ∀ t, 0 ≤ t → t < T → kineticEnergy (u t) ≤ kineticEnergy u₀
theorem enstrophy_integral_bound (hν) (hs) (hR) : ∀ t, 0 ≤ t → t < T →
    ∫ τ in (0:ℝ)..t, ∫ x, enstrophyDensity (u τ) x ≤ kineticEnergy u₀ / (2 * ν)
```

[shape]. The `∫_0^{T_*}` bound of the paper is the supremum over `t < T`,
stated per `t`; the `ℝ≥0∞`-valued `∫⁻ t in Ioo 0 T, …` version is derivable
by monotone convergence and is what `lem:leray-hopf` Step 0 needs on `Q_{S_*}`.

Proof plan (Steps 1–5 of the paper): D7 for `E'`, `hs.momentum` to substitute
`∂_tu` pointwise (`0 < τ`; at `τ = 0` use the right derivative and continuity,
or prove the identity on `Ioo` and extend by continuity), `IBP.integral_inner_laplacian_eq_neg_integral_enstrophyDensity`,
`IBP.integral_inner_convection_eq_zero`, `IBP.integral_fderiv_apply_eq_neg_integral_mul_divergence`
(with `inner_gradient_apply` to turn `⟪u,∇p⟫` into `fderiv ℝ p x (u x)`),
integrability suppliers D8, D6 for continuity of the right side, then
`intervalIntegral.integral_eq_sub_of_hasDeriv_right_of_le` (signature checked:
`ContinuousOn f (Icc a b)`, `∀ x ∈ Ioo a b, HasDerivWithinAt f (f' x) (Ioi x) x`,
`IntervalIntegrable f' volume a b`).

### 2.2 Pressure balance, integrated form [elaborated]

`prop:pressure`(ii): `⅓X(t) − ⅓X(s) + ν∫_s^tD₃ = ∫_s^tP₃`, `0 ≤ s ≤ t < T_*`.
The paper's proof uses only (R2)–(R3), i.e. the package, and (iv) shows `P₃`
is unchanged by `p ↦ p + c(t)`, so no pressure normalisation is a hypothesis.

```lean
theorem pressure_balance {ν T : ℝ} {u₀ : Space → Space} {u : ℝ → Space → Space}
    {p : ℝ → Space → ℝ} (hν : 0 < ν) (hs : IsClassicalSolution ν u₀ T u p)
    (hR : RegularityPackage' T u p) :
    ∀ s t : ℝ, 0 ≤ s → s ≤ t → t < T →
      IntervalIntegrable (fun τ => D3 (u τ)) volume s t ∧
      IntervalIntegrable (fun τ => P3 (p τ) (u τ)) volume s t ∧
      (1 / 3 : ℝ) * X3Real (u t) - (1 / 3 : ℝ) * X3Real (u s) + ν * ∫ τ in s..t, D3 (u τ)
        = ∫ τ in s..t, P3 (p τ) (u τ)
```

`D3`, `P3`, `X3Real` are those of `Calculus.lean` (amendment A2: `(∇u)ᵀu`
form, `a/0 = 0` at `u = 0`, matching `def:D3P3`'s `V, W` with the value `0` on
the zero set — `lem:integrands` is the same convention). Companion statements
of (i), (iii), (iv) [shape]:

```lean
theorem D3_nonneg_le (hs) (hR) (t) (ht : 0 ≤ t ∧ t < T) :
    0 ≤ D3 (u t) ∧ D3 (u t) ≤ 2 * ∫ x, ‖u t x‖ * enstrophyDensity (u t) x
theorem abs_P3_le (hs) (hR) (t) (ht) :
    |P3 (p t) (u t)| ≤ (eLpNorm (p t) ∞ volume).toReal * Real.sqrt (kineticEnergy (u t))
      * Real.sqrt (∫ x, enstrophyDensity (u t) x)
theorem continuousOn_X3Real (hs) (hR) (T') (hT' : T' < T) : ContinuousOn (fun t => X3Real (u t)) (Icc 0 T')
theorem P3_add_const (q : Space → ℝ) (c : ℝ) (v : Space → Space) (hv : ContDiff ℝ 1 v)
    (hdiv : ∀ x, divergence v x = 0) (h3 : Integrable (fun x => ‖v x‖ ^ 3) volume)
    (h2d : Integrable (fun x => ‖v x‖ ^ 2 * ‖fderiv ℝ v x‖) volume)
    (hq : Integrable (fun x => |P3density q v x|) volume) :
    P3 (fun x => q x + c) v = P3 q v
```

`P3_add_const` is (iv): `∫ W(u,∇u) = 0`, i.e. `∫ ⟪(v·∇)v, v⟫/‖v‖ …`; note the
paper's `W` is `⟪u,(∇u)ᵀu⟫/|u|` and `∫W = ∫ div(|u|u)` for solenoidal `u`, so
the cleanest Lean route is `IBP.integral_divergence_eq_zero` on `‖v‖ • v` (a
`C¹` field off the zero set — use the `ε`-regularised `rEps ε (v x) • v x`
and `divergence_rEps_smul` from `DensityBridge.lean`, then `ε ↓ 0` by
dominated convergence; this is exactly the paper's Step 4/6 device). The
`D₃`, `P₃` calculus of `Regularization.lean`, `Calculus.lean`,
`DensityBridge.lean` is already in place; what `Pressure.lean` adds is the
integral bookkeeping (cutoff `χ_R`, `ε ↓ 0`, `R → ∞`, `lem:diff-under-integral`
via `hasDerivAt_integral_of_dominated_loc_of_deriv_le`, and the
`intervalIntegral` FTC).

---

## 3. The three Phase I literature axioms

Every axiom is `axiom name : SomeProp` where `SomeProp` is a `def … : Prop`
in the default library `NavierFormal/Literature/Statements.lean`
(Mathlib-only, no axiom), and the `axiom` lives in the non-default library
`NavierFormalLiterature` (`NavierFormal/Literature/Axioms.lean`, never imported
by `Challenge.lean`/`Solution.lean`/`NavierFormal.lean`). Source records go in
`docs/literature-assumptions.yaml` (entries below).

### 3.0 Encoding decisions common to (a) and (b): Tao's objects

**Heat semigroup.** Tao defines `e^{tΔ}` on `ℝ³` by the kernel formula
`(4πt)^{-3/2}∫e^{-|x-y|²/4t}f(y)dy` (p. 39; `lem:heat`(K0)). Encode it exactly
so, as a Bochner convolution (Mathlib `MeasureTheory.convolution`, scoped
notation `⋆[L]`, `L = ContinuousLinearMap.lsmul ℝ ℝ`, `convolution_lsmul :
(f ⋆[lsmul 𝕜 𝕜, μ] g) x = ∫ t, f t • g (x - t) ∂μ`):

```lean
/-- Tao's heat kernel `K_s(x) = (4πs)^{-3/2} e^{-|x|²/4s}` (Tao 2013, p. 39). -/
def heatKernel (s : ℝ) (x : Space) : ℝ :=
  (4 * Real.pi * s) ^ (-(3 : ℝ) / 2) * Real.exp (-‖x‖ ^ 2 / (4 * s))

/-- `e^{sΔ}g := K_s ⋆ g` as a Bochner convolution (Tao's definition by the kernel formula). -/
def heat (s : ℝ) (g : Space → F) : Space → F :=
  heatKernel s ⋆[ContinuousLinearMap.lsmul ℝ ℝ] g
```

[elaborated]. Junk value `0` where the convolution integral does not exist;
in the axioms `heat` is only ever applied to Schwartz test fields (`𝓢(Space,
Space)`), for which the integral exists for every `s > 0` (Gaussian in `L¹`,
Schwartz bounded; Mathlib: `Integrable.integrable_convolution`,
`integral_rexp_neg_mul_sq_norm` for the normalisation), and at `s = 0` where
Tao's `e^{0Δ} = id` must be supplied by a `simp` lemma `heat_zero` (the kernel
formula degenerates: `(4π·0)^{-3/2} = 0` in Lean's `rpow`; define `heat 0 g := g`
by a case split in the definition — **amend `heat` to `if s = 0 then g else …`**
before landing; the elaborated block does not yet do this). Not a Fourier
multiplier: the Fourier-side definition would need the `NormedSpace ℂ`
codomain of `𝓢'`; the kernel form is Tao's own and is real-valued.

**Normalised pressure.** Tao's (9) with `f = 0`: `p = -Δ^{-1}∂_i∂_j(u_iu_j)`,
`Δ^{-1}` the Fourier multiplier `-(4π²|ξ|²)^{-1}` defined "for any tempered
distribution `F` for which the right-hand side is locally integrable" (14).
Composite symbol `-ξ_iξ_j/|ξ|²` (`lem:pressure-convention`(b), continuation
conventions).

*Checked:* `TemperedDistribution.fourierMultiplierCLM F g` is
`fourierInvCLM ∘L smulLeftCLM F g ∘L fourierCLM` and `smulLeftCLM` on `𝓢` is
defined (`SchwartzSpace/Basic.lean:738`) as `if hg : g.HasTemperateGrowth then
bilinLeftCLM … hg else 0`. `Function.HasTemperateGrowth g` requires `ContDiff ℝ
∞ g` with polynomially bounded derivatives (`TemperateGrowth.lean:40`). The
symbol `ξ ↦ -ξ_iξ_j/|ξ|²` is not continuous at `0`, hence not smooth, hence
**not admissible**: `fourierMultiplierCLM` with this symbol is the zero map,
silently. The same holds for Tao's `Δ^{-1}` symbol and for the Leray symbol
`δ_{ik} - ξ_iξ_k/|ξ|²` of the CP01 design (`IsMaximalL3Mild`, R-MILD); that
route is dead as written (confirms critic K4's hidden-import worry from a
different side).

*Decision:* use the **`L²` Fourier transform**, which Mathlib now has:
`MeasureTheory.Lp.fourierTransformₗᵢ E F : Lp F 2 ≃ₗᵢ[ℂ] Lp F 2` for `E` a
finite-dimensional real inner product space and `F` a complete complex inner
product space (`Analysis/Fourier/LpSpace.lean`; Plancherel `norm_fourier_eq`,
`inner_fourier_eq`; agreement with `𝓢` and `𝓢'` transforms
`SchwartzMap.toLp_fourier_eq`, `fourier_toTemperedDistribution_eq`). Tao's (14)
for `F = ∂_i∂_j(u_iu_j)` with `u_iu_j ∈ L²` is literally: take `𝓕(u_iu_j) ∈
L²`, multiply by the bounded measurable symbol (product in `L²`, locally
integrable), invert. So:

```lean
/-- The Riesz symbol `-ξ_i ξ_j / |ξ|²` of `R_iR_j` (Tao's `-Δ⁻¹∂_i∂_j`), as a complex-valued,
bounded, measurable function; `0` at `ξ = 0`. -/
def rieszSymbol (i j : Fin 3) (ξ : Space) : ℂ :=
  ((-(ξ i * ξ j) / ‖ξ‖ ^ 2 : ℝ) : ℂ)

/-- Multiplication of an `L²` class by a bounded measurable symbol. -/
def boundedMultiplier (m : Space → ℂ) (hm : MemLp m ∞ volume)
    (f : Lp ℂ 2 (volume : Measure Space)) : Lp ℂ 2 (volume : Measure Space) :=
  ((Lp.memLp f).smul hm (p := ∞) (q := 2) (r := 2)).toLp (m • ⇑f)

/-- `L⁴ · L⁴ ⊂ L²` for the complexified component products. -/
theorem memLp_componentProduct {v : Space → Space} (hv : MemLp v 4 volume) (i j : Fin 3) :
    MemLp (fun x => ((v x i * v x j : ℝ) : ℂ)) 2 volume := by
  have hi : MemLp (fun x => v x i) 4 volume :=
    (PiLp.proj (𝕜 := ℝ) 2 (fun _ : Fin 3 => ℝ) i).comp_memLp' hv
  have hj : MemLp (fun x => v x j) 4 volume :=
    (PiLp.proj (𝕜 := ℝ) 2 (fun _ : Fin 3 => ℝ) j).comp_memLp' hv
  have : ENNReal.HolderTriple 4 4 2 := ⟨by
    rw [show (4 : ℝ≥0∞) = 2 * 2 by norm_num,
      ENNReal.mul_inv (Or.inl two_ne_zero) (Or.inl ENNReal.ofNat_ne_top), ← two_mul,
      ← mul_assoc, ENNReal.mul_inv_cancel two_ne_zero ENNReal.ofNat_ne_top, one_mul]⟩
  have hprod : MemLp (fun x => v x i * v x j) 2 volume := hj.mul' hi
  exact (Complex.ofRealCLM.comp_memLp' hprod)

/-- The complexified component product `u_i u_j` as an `L²` class, for `u ∈ L⁴`. -/
def componentProductL2 (v : Space → Space) (hv : MemLp v 4 volume) (i j : Fin 3) :
    Lp ℂ 2 (volume : Measure Space) :=
  MemLp.toLp (fun x => ((v x i * v x j : ℝ) : ℂ)) (memLp_componentProduct hv i j)

/-- Tao's normalised pressure `P[v ⊗ v] = Σ_{i,j} R_iR_j(v_i v_j)` as an `L²` class, through the
`L²` Fourier transform `MeasureTheory.Lp.fourierTransformₗᵢ` (Tao (9), (14) with `f = 0`). -/
def normalizedPressureL2 (v : Space → Space) (hv : MemLp v 4 volume)
    (hm : ∀ i j, MemLp (rieszSymbol i j) ∞ volume) : Lp ℂ 2 (volume : Measure Space) :=
  (Lp.fourierTransformₗᵢ Space ℂ).symm
    (∑ i, ∑ j, boundedMultiplier (rieszSymbol i j) (hm i j)
      (Lp.fourierTransformₗᵢ Space ℂ (componentProductL2 v hv i j)))

/-- `q` is Tao's normalised pressure of `v`: the real part of `P[v ⊗ v]`, a.e. -/
def IsNormalizedPressure (v : Space → Space) (q : Space → ℝ) : Prop :=
  ∃ (hv : MemLp v 4 volume) (hm : ∀ i j, MemLp (rieszSymbol i j) ∞ volume),
    (fun x => q x) =ᵐ[volume] fun x => (normalizedPressureL2 v hv hm x).re
```

[elaborated, including the proof of `memLp_componentProduct`]. The `hm`
argument is a theorem (`|rieszSymbol i j ξ| ≤ 1`, measurable: polynomial over
`‖ξ‖²` with Lean's `x/0 = 0`), to be proved once as
`memLp_rieszSymbol : MemLp (rieszSymbol i j) ∞ volume` and then the `∃ hm`
collapses; it is kept as a binder so that the *definition* carries no proof
term. The real part is taken because the symbol is real and even, so `P[v⊗v]`
is real a.e. (paper (a); a Phase II lemma `normalizedPressureL2_im_eq_zero`,
recorded as a residue: until it is proved, `IsNormalizedPressure` says "the
real part of Tao's object", which for the true object is the object). Sign and
`2π` conventions: Mathlib's `𝓕` is `∫ e^{-2πi⟨x,ξ⟩}f(x)dx` (`Real.fourierIntegral`),
Tao's convention (p. 35, `lem:fourier` conventions paragraph) — no constant
mismatch; `Δ^{-1}∂_i∂_j` has symbol `+ξ_iξ_j/|ξ|²` so `-Δ^{-1}∂_i∂_j` has
`-ξ_iξ_j/|ξ|²` = `rieszSymbol` (continuation conventions paragraph).

**Weak derivatives and `H^k`.** For a general mild solution `u(t) ∈ H¹`
pointwise `fderiv` is junk. Tao's `H^k_x` is Fourier-side; the derivative form
is equivalent (`lem:sobolev-norms`, `lem:hk`), and only finiteness enters the
statements:

```lean
/-- Smooth compactly supported test fields. -/
def IsTestField (φ : Space → F) : Prop := ContDiff ℝ ∞ φ ∧ HasCompactSupport φ

/-- `G` is the weak (distributional) Fréchet derivative of `g`. -/
def HasWeakFDeriv (g : Space → F) (G : Space → Space →L[ℝ] F) : Prop :=
  ∀ φ : Space → ℝ, IsTestField φ → ∀ v : Space,
    ∫ x, φ x • G x v = -∫ x, fderiv ℝ φ x v • g x

/-- Distributional solenoidality of an `L²` field (Tao's `∇·u₀ = 0` for `H¹` data). -/
def IsWeakDivFree (g : Space → Space) : Prop :=
  ∀ φ : Space → ℝ, IsTestField φ → ∫ x, ⟪g x, gradient φ x⟫ = 0

/-- `g ∈ H¹(ℝ³)` (derivative form, equivalent to Tao's Fourier-side norm). -/
def MemH1 (g : Space → F) : Prop :=
  MemLp g 2 volume ∧ ∃ G : Space → Space →L[ℝ] F, MemLp G 2 volume ∧ HasWeakFDeriv g G

/-- `g ∈ H²(ℝ³)`. -/
def MemH2 (g : Space → F) : Prop :=
  MemLp g 2 volume ∧ ∃ G : Space → Space →L[ℝ] F, MemLp G 2 volume ∧ HasWeakFDeriv g G ∧
    ∃ G₂ : Space → Space →L[ℝ] Space →L[ℝ] F, MemLp G₂ 2 volume ∧ HasWeakFDeriv G G₂
```

[elaborated]. `IsWeakDivFree` replaces the pointwise `∀ x, divergence u₀ x =
0` for `H¹` data (for smooth `u₀ ∈ L²` with `∇u₀ ∈ L¹` the two agree by
`IBP.integral_fderiv_apply_eq_neg_integral_mul_divergence`; for a
`SchwartzDivFree` datum this is the bridge lemma `SchwartzDivFree.isWeakDivFree`).

**Tao's `H¹` mild solution** (p. 31, `def:tao-mild`(d), `f = 0`). The Duhamel
identity (10) is an identity of `L²`-valued (or `𝓢'`-valued) functions of
`t`; the paper reads it, for the solutions it evaluates it on, as a Riemann
integral in `L²` and notes it coincides with any weaker reading because bounded
linear maps commute with the integral (remark after `def:tao-mild`). We encode
the `𝓢'` reading: (10) paired with every Schwartz field `φ`, with
`⟨e^{sΔ}F, φ⟩ = ⟨F, e^{sΔ}φ⟩` (self-adjointness, `lem:heat`(K1)) and the
nonlinearity/pressure paired distributionally. This is verbatim the paper's
`eq:mild-paired` in `lem:mild-classical`, and it avoids convolving a
non-smooth `u` with the heat kernel. `(u·∇)u` is written through the weak
Jacobian `G` of `u(t)` (a parameter of the predicate, unique a.e. — Phase II
lemma `HasWeakFDeriv.ae_unique`), as in Tao where `(u·∇)u = u_j∂_ju` is an
`L²` function for a.e. `t`; `⟨-∇p, ψ⟩ = ∫ p ∇·ψ`.

```lean
/-- The distributional pairing of Tao's Duhamel integrand `-(u·∇)u - ∇p` with a test field `ψ`,
with `(u·∇)u = G(u)` through the weak Jacobian `G` and `⟨-∇p, ψ⟩ = ∫ p ∇·ψ`. -/
def duhamelPairing (v : Space → Space) (G : Space → Space →L[ℝ] Space) (q : Space → ℝ)
    (ψ : Space → Space) : ℝ :=
  -∫ x, ⟪G x (v x), ψ x⟫ + ∫ x, q x * divergence ψ x

/-- Tao's `H¹` mild solution on `[0,T]` (Tao 2013, p. 31; `f = 0`), with the Duhamel identity
(10) tested against Schwartz fields. -/
structure IsH1Mild (T : ℝ) (u₀ : Space → Space) (u : ℝ → Space → Space)
    (weakJac : ℝ → Space → Space →L[ℝ] Space) (p : ℝ → Space → ℝ) : Prop where
  T_pos : 0 < T
  meas : AEStronglyMeasurable (fun q : ℝ × Space => u q.1 q.2)
    (Measure.prod ((volume : Measure ℝ).restrict (Set.Icc 0 T)) (volume : Measure Space))
  data_H1 : MemH1 u₀
  data_div : IsWeakDivFree u₀
  hasWeakJac : ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), HasWeakFDeriv (u t) (weakJac t)
  LinfH1 : ∃ C : ℝ≥0∞, C < ⊤ ∧ ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)),
    eLpNorm (u t) 2 volume ≤ C ∧ eLpNorm (weakJac t) 2 volume ≤ C
  L2H2 : ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), MemH2 (u t)
  L2H2_int : ∀ G₂ : ℝ → Space → Space →L[ℝ] Space →L[ℝ] Space,
    (∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), HasWeakFDeriv (weakJac t) (G₂ t)) →
    ∫⁻ t in Set.Icc 0 T, eLpNorm (G₂ t) 2 volume ^ 2 < ⊤
  divFree : ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), IsWeakDivFree (u t)
  pressure : ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), IsNormalizedPressure (u t) (p t)
  duhamel_int : ∀ t ∈ Set.Icc 0 T, ∀ φ : 𝓢(Space, Space),
    IntervalIntegrable (fun t' => duhamelPairing (u t') (weakJac t') (p t') (heat (t - t') φ))
      volume 0 t
  duhamel : ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), ∀ φ : 𝓢(Space, Space),
    ∫ x, ⟪u t x, φ x⟫ = ∫ x, ⟪u₀ x, heat t φ x⟫ +
      ∫ t' in (0 : ℝ)..t, duhamelPairing (u t') (weakJac t') (p t') (heat (t - t') φ)

/-- Tao's incomplete mild `H¹` solution up to `T_*⁻` (Tao 2013, p. 56). -/
def IsIncompleteH1Mild (T₀ : ℝ) (u₀ : Space → Space) (u : ℝ → Space → Space)
    (G : ℝ → Space → Space →L[ℝ] Space) (p : ℝ → Space → ℝ) : Prop :=
  0 < T₀ ∧ ∀ T, 0 < T → T < T₀ → IsH1Mild T u₀ u G p
```

[elaborated]. Field-by-field against Tao p. 31 ("`u₀ ∈ H¹_x`, `f ∈
L^∞_tH¹_x`, `u ∈ L^∞_tH¹_x ∩ L²_tH²_x`, `p` given by (9), obeying (4) `∇·u =
0`, (1) `∇·u₀ = 0`, and (10)"): `data_H1`/`data_div` = `H¹` data; `LinfH1` =
`L^∞_tH¹_x` (ess sup in `t`, `H¹` norm as `L²` of `u` and of its weak
Jacobian); `L2H2` + `L2H2_int` = `L²_tH²_x` (second weak derivative in `L²`
for a.e. `t` with square-integrable-in-`t` norm — quantified over *any*
choice of second-derivative field, which is harmless since it is unique a.e.);
`divFree` = (4); `pressure` = (9)/(14); `duhamel` = (10) in the `𝓢'` reading,
a.e. in `t` (Tao's `u` is an `L^∞_t` function, so (10) is an a.e. identity);
`duhamel_int` records that the integral in (10) exists, which Tao's
definition presupposes. `meas` is Tao's "`u` is a Lebesgue measurable function
on `[0,T]×ℝ³`" (p. 37, conventions paragraph of the paper).

### 3.1 (a) Tao Theorem 5.4 (i), (iii), (iv) at `ν = 1` [elaborated]

```lean
/-- Tao's `L^∞_tH^k` conclusion of Theorem 5.4(iv): `∂_t^j u ∈ L^∞_t H^k([0,T] × ℝ³)` in the
derivative form, a.e. in `t`. -/
def MemLinfHk (T : ℝ) (j k : ℕ) (g : ℝ → Space → F) : Prop :=
  ∃ C : ℝ≥0∞, C < ⊤ ∧ ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)),
    ∀ k' ≤ k, eLpNorm (iteratedFDeriv ℝ k' (timeDerivIter j g t)) 2 volume ≤ C

/-- Tao Theorem 5.4(i): `u ∈ C⁰_tH¹_x`. -/
def TaoStrongSolution : Prop :=
  ∀ (T : ℝ) (u₀ : Space → Space) (u : ℝ → Space → Space) (G : ℝ → Space → Space →L[ℝ] Space)
    (p : ℝ → Space → ℝ), IsH1Mild T u₀ u G p →
    ∃ (v : ℝ → Space → Space) (G' : ℝ → Space → Space →L[ℝ] Space),
      (∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), v t =ᵐ[volume] u t) ∧
      IsH1Mild T u₀ v G' p ∧ IsContL2On T v ∧
      (∀ t ∈ Set.Icc 0 T, HasWeakFDeriv (v t) (G' t)) ∧ IsContL2On T G'

/-- Tao Theorem 5.4(iii): uniqueness of `H¹` mild solutions. -/
def TaoUniqueness : Prop :=
  ∀ (T : ℝ) (u₀ : Space → Space) (u₁ u₂ : ℝ → Space → Space)
    (G₁ G₂ : ℝ → Space → Space →L[ℝ] Space) (p₁ p₂ : ℝ → Space → ℝ),
    IsH1Mild T u₀ u₁ G₁ p₁ → IsH1Mild T u₀ u₂ G₂ p₂ →
    ∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), u₁ t =ᵐ[volume] u₂ t

/-- Tao Theorem 5.4(iv): regularity for Schwartz data. -/
def TaoRegularity : Prop :=
  ∀ (T : ℝ) (u₀ : SchwartzDivFree) (u : ℝ → Space → Space)
    (G : ℝ → Space → Space →L[ℝ] Space) (p : ℝ → Space → ℝ),
    IsH1Mild T (⇑u₀) u G p →
    ∃ (U : ℝ → Space → Space) (P : ℝ → Space → ℝ),
      (∀ᵐ t ∂(volume.restrict (Set.Icc 0 T)), U t =ᵐ[volume] u t ∧ P t =ᵐ[volume] p t) ∧
      ContDiffOn ℝ ∞ (fun q : ℝ × Space => U q.1 q.2) (Set.Icc 0 T ×ˢ (Set.univ : Set Space)) ∧
      ContDiffOn ℝ ∞ (fun q : ℝ × Space => P q.1 q.2) (Set.Icc 0 T ×ˢ (Set.univ : Set Space)) ∧
      ∀ j k : ℕ, MemLinfHk T j k U ∧ MemLinfHk T j k P
```

Axiom shape (non-default library) [shape]:

```lean
namespace NavierFormal.Literature

/-- Tao, Anal. PDE 6 (2013) 25–107, Theorem 5.4 (i), (iii), (iv), pp. 52–53, unit viscosity,
`f = 0`; transcribed in `cp02-local-theory.md` `thm:tao54` with transcription notes (1)–(6).
Source record: `docs/literature-assumptions.yaml` id `tao-2013-theorem-5-4`. -/
def TaoTheorem54 : Prop := TaoStrongSolution ∧ TaoUniqueness ∧ TaoRegularity

end NavierFormal.Literature

-- NavierFormal/Literature/Axioms.lean (library `NavierFormalLiterature`, not in any Challenge closure)
axiom NavierFormal.Literature.tao_theorem_5_4 : NavierFormal.Literature.TaoTheorem54
```

Part (ii) (local existence with the `X^k` bounds) is **not axiomatised**: the
paper's Step 1 uses Corollary 5.8 and remarks "(Theorem 5.4(ii) gives the same
conclusion)"; omitting (ii) shrinks the trust surface and removes the
smallness constant `c` and the `X^k` norms from the statement surface. If a
later node needs it, its shape is `∃ c > 0, ∀ T u₀, 0 < T → MemH1 u₀ →
IsWeakDivFree u₀ → (h1norm u₀)^4 * T ≤ c → ∃ u G p, IsH1Mild T u₀ u G p` with
the `X¹` bound as a further conjunct; recorded, not used.

Transcription decisions and faithfulness risks (each is a row for
`paper-lean-specification.md`):

| id | encoding | Tao's text | risk / direction | residue (proved by the paper, to be proved in Lean) |
|---|---|---|---|---|
| RT-1 | Duhamel tested against `𝓢(Space,Space)` with `⟨e^{sΔ}F,φ⟩ = ⟨F,e^{sΔ}φ⟩` | (10) as an identity of functions of `t` | the `𝓢'` reading; equals the `L²` reading whenever the integrand is `L²`-valued and integrable (bounded maps commute with the integral). Appears in hypothesis *and* conclusion positions, so it must be the same class: it is, as a *reading* of (10) | `lem:mild-classical` already works with this paired form (`eq:mild-paired`); no extra residue for the branch. Phase II: `heat` self-adjointness on `L² × 𝓢` (`lem:heat`(K1)) |
| RT-2 | `(u·∇)u` through the weak Jacobian parameter `G` | `(u·∇)u = u_j∂_ju` as an `L²` function for a.e. `t` | `G` is unique a.e. (`HasWeakFDeriv.ae_unique`, Phase II); quantification over all `G` in (iii) and `∃ G` in 5.8 is then harmless | for the branch `G t = fderiv ℝ (u t)` (`lem:classical`) |
| RT-3 | `⟨-∇p,ψ⟩ = ∫ p ∇·ψ` | `∇p` for `p ∈ L²` | distributional gradient, standard | none for the branch (`p` smooth, `IBP.integral_fderiv_apply_eq_neg_integral_mul_divergence`) |
| RT-4 | `IsNormalizedPressure` via `Lp.fourierTransformₗᵢ` and `rieszSymbol`, real part, a.e. | (9), (14) | needs `u(t) ∈ L⁴` so that `u_iu_j ∈ L²`; for `u(t) ∈ H¹` this is Sobolev `H¹ ⊂ L⁶` + `L²`, a fact about the class not stated by Tao (in conclusion position of 5.8 it must hold for Tao's solution — true, residue R-L4). Real part: Tao's object is real (`lem:pressure-convention`(a)); until `normalizedPressureL2_im_eq_zero` is proved the predicate reads "real part of" | `lem:pressure-convention`(a)–(d), `memLp_rieszSymbol`, `normalizedPressureL2_im_eq_zero`; `H¹ ⊂ L⁴` (`eLpNorm_six_le_eLpNorm_fderiv_two` is for `C¹`; weak version F) |
| RT-5 | `H^k` by weak derivatives; `MemLinfHk` a.e. in `t` with all orders `k' ≤ k` | Fourier-side `H^k_x`, `L^∞_tH^k` | equivalent norms (`lem:sobolev-norms`; only finiteness used); a.e. in `t` is Tao's `L^∞_t` | `lem:upgrade` turns a.e. bounds into `RegularityPackage'` |
| RT-6 | "smooth" = `ContDiffOn ℝ ∞ … (Icc 0 T ×ˢ univ)` on representatives `U, P` a.e. equal to `u, p` | "u and p are smooth" (Def. 1.1: smooth on the closed slab) | closed-slab reading (transcription note (5)); representatives because a mild `u` is only an a.e. object | none: this is the reading; `lem:upgrade` does not need it (note (5)) |
| RT-7 | (i) as existence of a representative `v` with `IsContL2On T v`, `IsContL2On T G'` | `u ∈ C⁰_tH¹_x` | `C⁰_tH¹` = `C⁰_tL²` of `u` and of `∇u`; representative form since `u` is a.e. | none |
| RT-8 | (iii) as `∀ᵐ t, u₁ t =ᵐ u₂ t` | "at most one `H¹` mild solution" (equality a.e. on `[0,T]×ℝ³`; `p` then determined by (9)) | equality of `u` only, as the paper reads it (remark after `def:tao-mild`) | `p₁ =ᵐ p₂` from `IsNormalizedPressure` uniqueness (Phase II; `Lp` classes are equal) |
| RT-9 | data: `SchwartzDivFree` in (iv); `MemH1 ∧ IsWeakDivFree` in (i),(iii) | Schwartz data (Def. 1.1); `H¹` data (p. 31) | exact (`SchwartzMap` seminorms = Tao's `sup(1+|x|)^k|∇^αu₀| < ∞`); distributional `∇·u₀ = 0` for `H¹` data, agreeing with pointwise for smooth data | bridge `SchwartzDivFree.memH1`, `SchwartzDivFree.isWeakDivFree` |
| RT-10 | integrability side conditions `duhamel_int`, `L2H2_int`, `meas` | implicit in "(10) holds", `L²_tH²_x`, "measurable" | strengthen the class; in hypothesis position safe, in conclusion position (5.8, (i)) they are properties every Tao solution has | Phase II lemma `IsH1Mild.duhamel_integrand_bounded` (bounded by `C‖φ‖`-type constants from `LinfH1`) |
| RT-11 | `heat 0 g = g` amendment | `e^{0Δ} = id` | `rpow` at `s = 0` gives junk without the case split | none |

Residue for feeding the axiom (what the manuscript proves; each becomes a
Lean theorem in `LocalTheory.lean`): `lem:restriction` (mild on `[0,T]` ⇒
mild on `[0,T']`, incomplete ⇒ mild on compacts); Steps 1–4 of
`prop:localtheory` (supremum-and-gluing, blow-up alternative, uniqueness in
the class) using only 5.8 + (i) + (iii); Step 5 (`lem:upgrade`: from
`TaoRegularity`'s a.e. `L^∞_tH^k` bounds and closed-slab smoothness to
`RegularityPackage'`); Step 6 (`lem:mild-classical`: paired Duhamel + package
⇒ `IsClassicalSolution 1 u₀ T u p`, `u(0) = u₀` pointwise, `p(t) =
R_iR_j(u_iu_j)` for every `t`); Step 9 (`ν`-scaling via
`IsClassicalSolution.nuNormalization`, `RegularityPackage'.nuNormalization`).
Corollary 4.3 (almost smooth `H¹` ⇒ mild with `p̃`) is needed only for
`prop:localtheory`(ii)'s second half (uniqueness against almost-smooth
competitors), which no CP1 theorem downstream uses: `CriticalBound` is
*instantiated* on the branch (a classical solution), never needs uniqueness
(R-CRIT is a documentation item, not a proof obligation). Recommendation:
state `TaoCorollary43` in `Statements.lean` [shape: `∀ T u₀ u p,
IsAlmostSmoothH1 T u₀ u p → ∃ G, IsH1Mild T u₀ u G (normalised p̃) ∧ ∀ᵐ t, ∃ c,
p t =ᵐ p̃ t + c`] but **do not axiomatise it in CP04**; record as deferred.

### 3.2 (b) Tao Corollary 5.8 with the incomplete mild notion [elaborated]

```lean
/-- Tao Corollary 5.8: existence or `H¹` blow-up before `T`. -/
def TaoDichotomy : Prop :=
  ∀ (T : ℝ) (u₀ : Space → Space), 0 < T → MemH1 u₀ → IsWeakDivFree u₀ →
    (∃ (u : ℝ → Space → Space) (G : ℝ → Space → Space →L[ℝ] Space) (p : ℝ → Space → ℝ),
      IsH1Mild T u₀ u G p) ∨
    ∃ (T₀ : ℝ) (u : ℝ → Space → Space) (G : ℝ → Space → Space →L[ℝ] Space)
      (p : ℝ → Space → ℝ), 0 < T₀ ∧ T₀ < T ∧ IsIncompleteH1Mild T₀ u₀ u G p ∧
      Tendsto (fun t => eLpNorm (u t) 2 volume + eLpNorm (G t) 2 volume) (𝓝[<] T₀) (𝓝 ⊤)
```

```lean
-- Statements.lean
/-- Tao 2013, Corollary 5.8, p. 56 (with the definition of incomplete mild `H¹` solution,
p. 56); transcribed as `thm:tao58` in `cp02-local-theory.md`. -/
def TaoCorollary58 : Prop := TaoDichotomy
-- Axioms.lean
axiom NavierFormal.Literature.tao_corollary_5_8 : NavierFormal.Literature.TaoCorollary58
```

Risks: RT-12 the `H¹` norm in the blow-up clause is `‖u(t)‖₂ + ‖G(t)‖₂` in
`ℝ≥0∞` (equivalent to Tao's norm up to constants; divergence to `+∞` is
norm-independent; `𝓝[<] T₀` is `t → T_*^-`); RT-13 `T₀ < T` strict as printed
(`0 < T_* < T`); RT-14 the disjunction is inclusive ("at least one"); RT-15
the incomplete solution's `p` is a single function on `[0,T₀)` (Tao: "`p :
[0,T_*)×ℝ³ → ℝ`"). Residue: none beyond RT-1–RT-11 (the class is shared).

### 3.3 (c) ESS Theorem 1.3 [elaborated]

ESS (Russian Math. Surveys 58:2 (2003)), pp. 211–214, transcribed verbatim in
`cp02-continuation.md` (`eq:ess-13`–`eq:ess-17`, `thm:ess`, `rem:ess-norm`).

```lean
/-- ESS's `J̊`: the `L²`-closure of smooth compactly supported solenoidal fields. -/
def solenoidalTestSet : Set (Lp Space 2 (volume : Measure Space)) :=
  {w | ∃ φ : Space → Space, IsTestField φ ∧ (∀ x, divergence φ x = 0) ∧ ⇑w =ᵐ[volume] φ}

def solenoidalL2 : Submodule ℝ (Lp Space 2 (volume : Measure Space)) :=
  (Submodule.span ℝ solenoidalTestSet).topologicalClosure

/-- `v ∈ J̊¹₂`: `W¹₂`-limit of solenoidal test fields, with `G` its weak gradient. -/
def MemSolenoidalH1 (v : Space → Space) : Prop :=
  ∃ G : Space → Space →L[ℝ] Space, HasWeakFDeriv v G ∧
    ∃ φ : ℕ → Space → Space, (∀ n, IsTestField (φ n) ∧ ∀ x, divergence (φ n) x = 0) ∧
      Tendsto (fun n => eLpNorm (fun x => φ n x - v x) 2 volume
        + eLpNorm (fun x => fderiv ℝ (φ n) x - G x) 2 volume) atTop (𝓝 0)

/-- Solenoidal test fields on `Q_T = ℝ³ × (0,T)`, ESS's `Ċ₀^∞(Q_T)`. -/
def IsSolenoidalTestQT (T : ℝ) (w : ℝ → Space → Space) : Prop :=
  ContDiff ℝ ∞ (fun q : ℝ × Space => w q.1 q.2) ∧
  HasCompactSupport (fun q : ℝ × Space => w q.1 q.2) ∧
  tsupport (fun q : ℝ × Space => w q.1 q.2) ⊆ Set.Ioo 0 T ×ˢ (Set.univ : Set Space) ∧
  ∀ t x, divergence (w t) x = 0

/-- ESS (1.3)–(1.7): Leray–Hopf weak solution in `Q_T` with datum `a`, and weak gradient `G`. -/
structure IsLerayHopf (T : ℝ) (a : Space → Space) (v : ℝ → Space → Space)
    (G : ℝ → Space → Space →L[ℝ] Space) : Prop where
  meas : AEStronglyMeasurable (fun q : ℝ × Space => v q.1 q.2)
    (Measure.prod ((volume : Measure ℝ).restrict (Set.Ioo 0 T)) (volume : Measure Space))
  weakGrad : ∀ᵐ t ∂(volume.restrict (Set.Ioo 0 T)), HasWeakFDeriv (v t) (G t)
  /-- (1.3), first half: `v ∈ L_∞(0,T; J̊)`. -/
  LinfJ : ∃ C : ℝ≥0∞, C < ⊤ ∧ ∀ᵐ t ∂(volume.restrict (Set.Ioo 0 T)),
    eLpNorm (v t) 2 volume ≤ C ∧
    ∃ h : MemLp (v t) 2 volume, h.toLp (v t) ∈ solenoidalL2
  /-- (1.3), second half: `v ∈ L_2(0,T; J̊¹₂)`. -/
  L2J12 : (∀ᵐ t ∂(volume.restrict (Set.Ioo 0 T)), MemSolenoidalH1 (v t)) ∧
    ∫⁻ t in Set.Ioo 0 T, (eLpNorm (v t) 2 volume ^ 2 + eLpNorm (G t) 2 volume ^ 2) < ⊤
  /-- (1.4). -/
  weakCont : ∀ w : Space → Space, MemLp w 2 volume →
    ContinuousOn (fun t => ∫ x, ⟪v t x, w x⟫) (Set.Icc 0 T)
  /-- (1.5). -/
  weakEq : ∀ w : ℝ → Space → Space, IsSolenoidalTestQT T w →
    ∫ t in Set.Ioo 0 T, ∫ x, (-⟪v t x, timeDeriv w t x⟫
      - ∑ i, ∑ j, v t x i * v t x j * fderiv ℝ (w t) x (e j) i
      + ∑ j, ⟪G t x (e j), fderiv ℝ (w t) x (e j)⟫) = 0
  /-- (1.6). -/
  energyIneq : ∀ t₀ ∈ Set.Icc 0 T,
    (1 / 2 : ℝ≥0∞) * ∫⁻ x, ‖v t₀ x‖ₑ ^ 2
      + ∫⁻ t in Set.Ioo 0 t₀, ∫⁻ x, ENNReal.ofReal (frobeniusNormSq (G t x))
      ≤ (1 / 2 : ℝ≥0∞) * ∫⁻ x, ‖a x‖ₑ ^ 2
  /-- (1.7). -/
  initial : Tendsto (fun t => eLpNorm (fun x => v t x - a x) 2 volume) (𝓝[>] 0) (𝓝 0)

/-- ESS (1.13): `v ∈ L_{3,∞}(Q_T)`. -/
def MemL3Inf (T : ℝ) (v : ℝ → Space → Space) : Prop :=
  ∃ M : ℝ≥0∞, M < ⊤ ∧ ∀ᵐ t ∂(volume.restrict (Set.Ioo 0 T)), eLpNorm (v t) 3 volume ≤ M

/-- ESS Theorem 1.3, conclusion `v ∈ L_5(Q_T)` only. -/
def EssTheorem13 : Prop :=
  ∀ (T : ℝ) (a : Space → Space) (v : ℝ → Space → Space) (G : ℝ → Space → Space →L[ℝ] Space),
    0 < T → IsLerayHopf T a v G → MemL3Inf T v →
    ∫⁻ t in Set.Ioo 0 T, ∫⁻ x, ‖v t x‖ₑ ^ 5 < ⊤
```

```lean
-- Axioms.lean
/-- Escauriaza–Seregin–Šverák, Russian Math. Surveys 58:2 (2003) 211–250, Theorem 1.3, p. 214,
with (1.3)–(1.7) p. 212, mixed norm and (1.13) p. 213; `thm:ess` in `cp02-continuation.md`.
Conclusion restricted to `v ∈ L_5(Q_T)`; "smooth and unique" dropped (weaker conclusion). -/
axiom NavierFormal.Literature.ess_theorem_1_3 : NavierFormal.Literature.EssTheorem13
```

Decisions and risks:

| id | encoding | ESS text | risk / direction | residue |
|---|---|---|---|---|
| RE-1 | `L^∞_tL²`, `L²_tH¹` via `eLpNorm` of the weak gradient `G` (parameter) | `L_∞(0,T;J̊) ∩ L_2(0,T;J̊¹₂)` | weak gradient chosen (v is only weakly differentiable in the class); `G` unique a.e.; for the branch `G t = fderiv ℝ (v t)` | `lem:leray-hopf` Step 0/2 |
| RE-2 | `J̊` = closure of span of a.e.-classes of solenoidal test fields in `Lp Space 2`; `J̊¹₂` membership = `W¹₂`-sequential closure (metric space: closure = sequential closure) | closures of `Ċ₀^∞` in `L₂`, `W¹₂` | `Submodule.span` before closure is harmless (`Ċ₀^∞` is a linear space) | `lem:solenoidal-density` (vector potential, Hardy, cutoff) — F item F-SOLDENS, needed for the branch |
| RE-3 | (1.5) as iterated integral `∫ t in Ioo 0 T, ∫ x, …` with `v ⊗ v : ∇w = Σ v_iv_j ∂_jw_i` and `∇v : ∇w = Σ_j ⟪G e_j, ∂_jw⟫` | `∫_{Q_T}` | Fubini (integrand compactly supported in `t`, bounded by `L²`-products): product-vs-iterated is a Phase II lemma; the test class `Ċ₀^∞(Q_T)` is read as the widest one (compact support in `Q_T`, solenoidal in `x` for each `t`), which strengthens the *hypothesis* of the axiom — safe (paper: "the strongest one possible") | `lem:leray-hopf` Step 4 (space-time IBP for smooth `v` against compactly supported `w`) |
| RE-4 | (1.6) in `ℝ≥0∞` with `|∇v|² = frobeniusNormSq (G t x)` | `∫|∇v|²` (Frobenius, ESS/paper conventions) | junk-free; Frobenius matches the paper's `|∇u|²` | Step 5 with the energy identity; endpoint `t₀ = T = S_*` via the weak limit (Step 1) |
| RE-5 | (1.7) as `Tendsto … (𝓝[>] 0) (𝓝 0)` | `‖v(·,t) − a‖₂ → 0` as `t → 0` | one-sided within `Q_T` | Step 6 |
| RE-6 | (1.13) as ess sup over `(0,T)` in `ℝ≥0∞` | `L_{3,∞}(Q_T)` norm, p. 213 | exact (`rem:ess-norm`); the paper's `sup ≥ ess sup` step is `lem:sup-esssup` | `lem:l3-to-l5` first display |
| RE-7 | conclusion `∫⁻_{(0,T)}∫⁻ ‖v‖⁵ < ⊤` only | "`v ∈ L₅(Q_T)`, and hence it is smooth and unique" | strictly weaker conclusion — safe | `lem:l3-to-l5` uses only this |
| RE-8 | `v : ℝ → Space → Space` total; ESS's `v : Q̄_T → ℝ³` | function on the closed cylinder | total functions carry the endpoint value; the paper's endpoint construction sets `v(·,S_*) := v_*` | Step 1 of `lem:leray-hopf` (weak limit via `InnerProductSpace.toDual`/`orthogonalProjection` onto `solenoidalL2`) |
| RE-9 | datum `a` unconstrained in the axiom (ESS Thm 1.3 does not restate (1.8) `a ∈ J̊`) | — | hypothesis-free on `a`, as printed; the paper notes our `a ∈ J̊¹₂` anyway | none |

Residue (paper-owned, to become Lean theorems in `LerayHopfClass.lean`,
`Serrin.lean`, `Continuation.lean`): `lem:nu-normalisation`(i)–(vi) (from
`IsClassicalSolution.nuNormalization`, `RegularityPackage'.nuNormalization`,
`energy_identity`); `lem:hardy`, `lem:solenoidal-density`; `lem:leray-hopf`
Steps 0–6 including the weak-limit endpoint; `lem:l3-to-l5`;
`lem:sobolev-h1` (available as `eLpNorm_six_le_eLpNorm_fderiv_two` for the
smooth branch); `lem:serrin-enstrophy` Steps 1–4; `thm:continuation`.

### 3.4 Source records to add (`docs/literature-assumptions.yaml`)

```yaml
  - id: tao-2013-theorem-5-4
    statement: Theorem 5.4 (i) strong solution, (iii) uniqueness, (iv) regularity for Schwartz data; nu = 1; f = 0
    source: Tao, Anal. PDE 6 (2013) 25-107, pp. 52-53; definitions pp. 26-31, 35-39
    lean: NavierFormal.Literature.TaoTheorem54 / NavierFormal.Literature.tao_theorem_5_4
    transcription: research/evidence/cp02-local-theory.md thm:tao54, notes (1)-(6); cp04-phase-i-design.md RT-1..RT-11
    status: LITERATURE-INPUT
  - id: tao-2013-corollary-5-8
    statement: existence of an H^1 mild solution on [0,T] or an incomplete mild solution blowing up in H^1 before T
    source: Tao, Anal. PDE 6 (2013), Corollary 5.8 and the incomplete-mild definition, p. 56
    lean: NavierFormal.Literature.TaoCorollary58 / tao_corollary_5_8
    status: LITERATURE-INPUT
  - id: ess-2003-theorem-1-3
    statement: a Leray-Hopf weak solution in Q_T with v in L_{3,infty}(Q_T) lies in L_5(Q_T)
    source: Escauriaza-Seregin-Sverak, Russian Math. Surveys 58:2 (2003), Theorem 1.3 p. 214; (1.3)-(1.7) p. 212; (1.13) p. 213
    lean: NavierFormal.Literature.EssTheorem13 / ess_theorem_1_3
    status: LITERATURE-INPUT
```

`gkp-2013-theorem-4` becomes `status: RETIRED (not used; rem:gkp)` — the paper
no longer imports GKP (critic K3/K4 resolved by the continuation lane's (D3)
route), and the CP01 design's `gkp_theorem4`, `classical_branch_identification`,
`IsMaximalL3Mild` are dropped (K4: the `C_tL³` uniqueness presupposition
disappears with them; K14: `Statements.lean` names below supersede the CP01
names).

---

## 4. Module plan for CP04 and the first parallel batch

### 4.1 Files, dependency order, classification

P = Phase I paper node (manuscript-owned, proved), F = infrastructure (Mathlib
gap, proved), L = literature statement (definitions only) or axiom.

| order | file | class | content | depends on |
|---|---|---|---|---|
| 0 | `NavierFormal/Package.lean` | F (definitions only) | §1.3 definitions verbatim (`IsContL2On`, `IsC1L2On`, `IsUnifContOn`, `IsContLqOn`, `RegularityPackage'` with the two `unifCont_*` fields), `IsTestField`, `HasWeakFDeriv`, `IsWeakDivFree`, `MemH1`, `MemH2`, `IsSolenoidalTestQT`, `heatKernel`, `heat` (with `s = 0` case) | `SolutionClass`, `IBP` |
| 1 | `NavierFormal/PackageFacts.lean` | F + P(`cor:Lq`) | D1–D9 of §1.4 | `Package` |
| 1 | `NavierFormal/Energy.lean` | P (`prop:energy`) | §2.1 theorems | `Package`, `IBP`, `Calculus` (imports `PackageFacts` once landed; until then inlines what it needs or is written against the D-lemma statements) |
| 1 | `NavierFormal/Literature/Statements.lean` | L (definitions) | `rieszSymbol`, `boundedMultiplier`, `memLp_componentProduct`, `componentProductL2`, `normalizedPressureL2`, `IsNormalizedPressure`, `duhamelPairing`, `IsH1Mild`, `IsIncompleteH1Mild`, `MemLinfHk`, `TaoStrongSolution`, `TaoUniqueness`, `TaoRegularity`, `TaoTheorem54`, `TaoDichotomy`, `TaoCorollary58`, `solenoidalTestSet`, `solenoidalL2`, `MemSolenoidalH1`, `IsLerayHopf`, `MemL3Inf`, `EssTheorem13`; `TaoCorollary43` shape as a docstring-only TODO | `Package`, `QuotientObjects` (for `IsTestPotential` reuse if wanted) |
| 1 | `NavierFormal/LerayHopfClauses.lean` | P (`lem:leray-hopf` clauses) | §4.2 item 4 | `Package` |
| 1 | `NavierFormal/PackageScaling.lean` | P (`lem:nu-scaling`(a)) | `RegularityPackage'.nuNormalization`, `timeDerivIter_timeScale` | `Package` |
| 1 | `NavierFormal/Serrin.lean` | P (`lem:serrin-enstrophy` Steps 3–4, scalar) | `serrin_gronwall`, absorption arithmetic | Mathlib, `Interpolation` (Young `5/4, 5`) |
| 2 | `NavierFormal/Pressure.lean` | P (`prop:pressure`) | §2.2 | `PackageFacts`, `Regularization`, `DensityBridge`, `IBP` |
| 2 | `NavierFormal/Literature/Sources.lean` | L (docstrings) | source records mirrored from the yaml | — |
| 2 | `NavierFormal/WeakDerivative.lean` | F | `HasWeakFDeriv.ae_unique`, smooth ⇒ weak = classical (`lem:classical`), `SchwartzDivFree.memH1`, `SchwartzDivFree.isWeakDivFree`, `memLp_rieszSymbol` | `Package`, `Statements` |
| 2 | `NavierFormal/Heat.lean` | F (`lem:heat`) | `heat_zero`, integrability of `heat s φ` for Schwartz `φ`, K1 self-adjointness on `L²×𝓢`, K2 continuity, K3 derivative | `Package` |
| 2 | `NavierFormal/NormalizedPressure.lean` | P (`lem:pressure-convention`) + F | (a) `L²`/`H^k` bounds, (b)–(c) Poisson identity in `𝓢'`, (d), `normalizedPressureL2_im_eq_zero`, smooth representative | `Statements`, `WeakDerivative` |
| 3 | `NavierFormal/SolenoidalDensity.lean` | P (`lem:hardy`, `lem:solenoidal-density`) — F-SOLDENS | vector potential via `Lp.fourierTransformₗᵢ`, Hardy along rays, cutoff | `Statements`, `Heat` |
| 3 | `NavierFormal/LerayHopf.lean` | P (`lem:leray-hopf` assembly, endpoint) | `isLerayHopf_of_classical` (interior), weak-limit endpoint `isLerayHopf_endpoint` | `LerayHopfClauses`, `SolenoidalDensity`, `Energy` |
| 3 | `NavierFormal/Upgrade.lean` | P (`lem:upgrade`, `lem:mild-classical`) — F-UPGRADE | a.e. `L^∞_tH^k` + closed-slab smoothness ⇒ `RegularityPackage'`; paired Duhamel + package ⇒ `IsClassicalSolution` | `Statements`, `Heat`, `PackageFacts` |
| 4 | `NavierFormal/LocalTheory.lean` | P (`prop:localtheory`, `cor:Lq`, `lem:sup-esssup`, `lem:global-smooth`) | gluing from `TaoTheorem54 ∧ TaoCorollary58` as *hypotheses* (Prop arguments), maximal time, blow-up alternative | `Upgrade`, `NormalizedPressure`, `PackageScaling` |
| 4 | `NavierFormal/Continuation.lean` | P (`lem:l3-to-l5`, `lem:serrin-enstrophy`, `thm:continuation`) | from `EssTheorem13` as hypothesis | `LerayHopf`, `Serrin`, `LocalTheory` |
| 5 | `NavierFormal/Conditional.lean` | P (`thm:conditional`) | `clay_alternative_A_of_critical_bound (hT : TaoTheorem54) (hC : TaoCorollary58) (hE : EssTheorem13) …` | `Continuation`, `Energy` |
| 5 | `NavierFormal/Literature/Axioms.lean` (lib `NavierFormalLiterature`) | axioms | the three `axiom`s; `clay_alternative_A_axiomatic := clay_alternative_A_of_critical_bound tao_theorem_5_4 tao_corollary_5_8 ess_theorem_1_3 …`; `#print axioms` recorded in `docs/verification-status.md` | `Conditional` |
| 6 | `Challenge.lean`, `Solution.lean`, `comparator.json`, docs | controller | Family A with the three literature `Prop`s as explicit hypotheses (Palomar route A), Family B unconditional (`energy_identity`, `pressure_balance`, …) | all |

The CP01 design's `Calculus/Sobolev.lean` (`AllSobolev`, `TaoRegular`,
`SobolevClass`), `Literature/MildSolution.lean` (`IsMaximalL3Mild`),
`gkp_theorem4`, `classical_branch_identification`, `leray_projection_L3`,
`heat_*_L3`, `bernstein_lowpass`, `divfree_flow` are superseded or out of CP04
scope (K5–K7: the quotient-section axioms are not CP1 conditional-chain items
and must be paper-proved before they reappear; none is listed here).

### 4.2 First parallelisable batch (six disjoint files, all importing only `Package.lean` and existing modules)

Pre-step (controller, zero proof content): land `NavierFormal/Package.lean`
from §1.3 and §3.0 (definitions only; every definition in this design
elaborated). Then, in parallel:

**B1 `NavierFormal/PackageFacts.lean`** — D1–D9 of §1.4 with the exact
statements

```lean
theorem RegularityPackage'.toRegularityPackage {T : ℝ} {u : ℝ → Space → Space}
    {p : ℝ → Space → ℝ} (h : RegularityPackage' T u p) : RegularityPackage T u p
theorem RegularityPackage'.mono {T T' : ℝ} {u} {p} (h : RegularityPackage' T u p) (hT : T' ≤ T) :
    RegularityPackage' T' u p
theorem isContLqOn_of_L2_sup {T' : ℝ} {g : ℝ → Space → F} (hmeas : ∀ t, Continuous (g t))
    (h2 : IsContL2On T' g) (hb : ∃ C : ℝ, ∀ t ∈ Set.Icc 0 T', ∀ x, ‖g t x‖ ≤ C)
    (hinf : IsUnifContOn T' g) {q : ℝ≥0∞} (hq : 2 ≤ q) (hqt : q ≠ (∞ : ℝ≥0∞)) :
    IsContLqOn q T' g
theorem RegularityPackage'.memLp_velocity (h : RegularityPackage' T u p) {T'} (h0 : 0 ≤ T')
    (hT : T' < T) {t} (ht : t ∈ Set.Icc 0 T') {q : ℝ≥0∞} (hq : 2 ≤ q) : MemLp (u t) q volume
theorem RegularityPackage'.continuousOn_enstrophy (h : RegularityPackage' T u p) {T'} (h0) (hT) :
    ContinuousOn (fun t => ∫ x, enstrophyDensity (u t) x) (Set.Icc 0 T')
theorem RegularityPackage'.hasDerivWithinAt_kineticEnergy (h : RegularityPackage' T u p) {T'} (h0) (hT)
    {t} (ht : t ∈ Set.Icc 0 T') :
    HasDerivWithinAt (fun τ => kineticEnergy (u τ)) (2 * ∫ x, ⟪u t x, timeDeriv u t x⟫) (Set.Icc 0 T') t
-- plus the eight IBP integrability suppliers D8 at fixed `t ∈ Icc 0 T'`
```

(the `isContLqOn_of_L2_sup` statement elaborated; the others are the same
shape with the package as hypothesis).

**B2 `NavierFormal/Energy.lean`** — `energy_identity`, `energy_bound`,
`enstrophy_integral_bound` of §2.1. It may import `PackageFacts` only if B1 has
landed; otherwise the implementer proves the D6/D7/D8 instances it needs as
private lemmas and the controller deduplicates at integration.

**B3 `NavierFormal/Literature/Statements.lean`** — definitions only (§3.0–3.3
blocks, verbatim; the one theorem `memLp_componentProduct` is included because
`componentProductL2` needs it; its proof is above and elaborated). No axiom in
this file. Docstrings name Tao's/ESS's page and equation numbers.

**B4 `NavierFormal/LerayHopfClauses.lean`** — the clause lemmas of
`lem:leray-hopf` for a classical solution with the package on an interior
cylinder, stated *without* the `IsLerayHopf` structure (so B3 and B4 are
independent):

```lean
theorem weakCont_of_package (hs : IsClassicalSolution 1 a T u p) (hR : RegularityPackage' T u p)
    {T'} (hT' : 0 < T') (hT'T : T' < T) (w : Space → Space) (hw : MemLp w 2 volume) :
    ContinuousOn (fun t => ∫ x, ⟪u t x, w x⟫) (Set.Icc 0 T')                       -- (1.4)
theorem initial_of_package (hs) (hR) :
    Tendsto (fun t => eLpNorm (fun x => u t x - a x) 2 volume) (𝓝[>] 0) (𝓝 0)      -- (1.7)
theorem weakEq_of_classical (hs) (hR) {T'} (hT') (hT'T) (w : ℝ → Space → Space)
    (hw : IsSolenoidalTestQT T' w) :
    ∫ t in Set.Ioo 0 T', ∫ x, (-⟪u t x, timeDeriv w t x⟫
      - ∑ i, ∑ j, u t x i * u t x j * fderiv ℝ (w t) x (e j) i
      + ∑ j, ⟪fderiv ℝ (u t) x (e j), fderiv ℝ (w t) x (e j)⟫) = 0                 -- (1.5)
theorem hasWeakFDeriv_of_smooth (hs) (hR) {T'} (hT') (hT'T) {t} (ht : t ∈ Set.Icc 0 T') :
    HasWeakFDeriv (u t) (fderiv ℝ (u t))                                              -- weakGrad
theorem measurable_of_classical (hs) {T'} (hT'T : T' ≤ T) :
    AEStronglyMeasurable (fun q : ℝ × Space => u q.1 q.2)
      (Measure.prod ((volume : Measure ℝ).restrict (Set.Ioo 0 T')) (volume : Measure Space))
```

Route for (1.5): Step 4 of the paper — pointwise equation on the support,
Fubini on the compact support, `IBP.integral_fderiv_apply_eq_zero`-style
vanishing in `t` and `x`. Out of scope for B4: `LinfJ`'s `solenoidalL2`
membership and `L2J12`'s `MemSolenoidalH1` (need `lem:solenoidal-density`,
F-SOLDENS, order 3) and the endpoint `T' = S_*` (weak limit).

**B5 `NavierFormal/PackageScaling.lean`** — `eq:nu-normalization` for the
package (`lem:nu-scaling`(a), `lem:nu-normalisation`(ii)):

```lean
theorem timeDerivIter_timeScale {ν : ℝ} (hν : 0 < ν) (u : ℝ → Space → F) (j : ℕ) (s : ℝ) (hs : 0 < s)
    (x : Space) (hsmooth : ContDiffAt ℝ ∞ (fun σ => u σ x) (s / ν)) :
    timeDerivIter j (fun σ y => u (σ / ν) y) s x = (ν⁻¹) ^ j • timeDerivIter j u (s / ν) x
theorem RegularityPackage'.nuNormalization {ν T : ℝ} {u : ℝ → Space → Space}
    {p : ℝ → Space → ℝ} (hν : 0 < ν) (h : RegularityPackage' T u p) :
    RegularityPackage' (ν * T) (fun s x => ν⁻¹ • u (s / ν) x)
      (fun s x => (ν ^ 2)⁻¹ * p (s / ν) x)
```

(second statement elaborated). Companion norm identities
`eLpNorm_nuNormalization (q)` generalising `eLpNorm_three_nuNormalization`.
The `t = 0` right derivative needs the one-sided chain rule
(`HasDerivWithinAt.scomp` with `Ici`), which is why the pointwise lemma is
stated for `s > 0` and the endpoint handled via `IsC1L2On` at the `Lp` level.

**B6 `NavierFormal/Serrin.lean`** — the scalar Serrin-type Gronwall step
(`lem:serrin-enstrophy` Steps 3–4), elaborated statement:

```lean
theorem serrin_gronwall {Y Y' g : ℝ → ℝ} {T : ℝ} (hT : 0 ≤ T)
    (hYc : ContinuousOn Y (Set.Icc 0 T))
    (hY' : ∀ t ∈ Set.Ico 0 T, HasDerivWithinAt Y (Y' t) (Set.Ici t) t)
    (hg : ContinuousOn g (Set.Icc 0 T)) (hg0 : ∀ t ∈ Set.Icc 0 T, 0 ≤ g t)
    (hY0 : ∀ t ∈ Set.Icc 0 T, 0 ≤ Y t)
    (hle : ∀ t ∈ Set.Ico 0 T, Y' t ≤ g t * Y t) :
    ∀ t ∈ Set.Icc 0 T, Y t ≤ Y 0 * Real.exp (∫ τ in (0 : ℝ)..t, g τ)
```

Route: `(Y e^{-G})' ≤ 0` with `G t = ∫_0^t g` (`intervalIntegral.integral_hasDerivWithinAt_right`),
then `image_le_of_deriv_right_le_deriv_boundary` (`MeanValue.lean:199`) or
`le_gronwallBound_of_liminf_deriv_right_le` (`Gronwall.lean:112`, constant
`K`; the variable-coefficient form is why the exponential-integrating-factor
route is preferred). Companion: the absorption inequality of Step 3 as a
pure real inequality, `serrin_absorption (ν C_S a b : ℝ) (hν : 0 < ν) … :
C_S^(3/5) * b * Y^(1/5) * a^(8/5) ≤ ν * a^2 + (256/3125) * C_S^3 * ν⁻¹^4 * b^5 * Y`
from `NavierFormal.young_five_fourths_eps`. The enstrophy identity Step 1–2
(needs Plancherel `‖∇²u‖₂ = ‖Δu‖₂` and `⟨Δu,∇p⟩ = 0` — F items via
`Lp.fourierTransformₗᵢ` or via IBP on the smooth branch) is order 4, not in
the batch.

Each batch file: docstrings name the manuscript label; check with
`cd ../navier-formal && lake env lean <file>`; zero errors, zero
`sorry`; `#print axioms` via a temporary trailer, then deleted; report the
axiom list (expected `[propext, Classical.choice, Quot.sound]`).

---

## 5. Risks and open items (for the controller)

1. **`heat` at `s = 0`.** The elaborated `heat` gives junk at `s = 0`
   (`rpow` of `0`); amend to `if s = 0 then g else …` before landing
   `Package.lean` (RT-11). The Duhamel clause evaluates `heat (t - t') φ` at
   `t' = t`, a single point of the interval (measure zero for the integral) but
   `heat t φ` at `t = 0` appears in the `u₀` term for `t = 0`, which is in the
   a.e.-`t` scope anyway; the amendment is still required for `heat_zero`.
2. **`IsNormalizedPressure` needs `u(t) ∈ L⁴` (RT-4).** For Tao's `H¹` class
   this is Sobolev; the Lean statement therefore carries `∃ hv : MemLp v 4` as
   part of Tao's definition (9)/(14) "where the right-hand side is locally
   integrable". In conclusion position (Corollary 5.8) this asserts a true
   property of Tao's solution not printed by Tao; recorded as residue R-L4.
   If the controller prefers a hypothesis-free pressure, the fallback is the
   characterisation "`q ∈ L²` and `-Δq = ∂_i∂_j(v_iv_j)` in `𝓢'`" (residue
   ID-P1: `L²` uniqueness for Poisson, provable by Plancherel with the same
   `Lp.fourierTransformₗᵢ`); the multiplier form was chosen because it *is*
   Tao's definition.
3. **Real part (RT-4).** Until `normalizedPressureL2_im_eq_zero` is proved,
   `IsNormalizedPressure` reads "real part of Tao's `P[v⊗v]`"; harmless for
   the true object, but a Phase II item.
4. **F-UPGRADE** (`lem:upgrade`, `lem:mild-classical`) is the heaviest
   infrastructure of the chain: pointwise-vs-`Lp` interchange of the time
   integral (Fubini with `Lp`-valued Bochner integrals), Sobolev embedding
   `H² ⊂ L^∞` for the sup bounds (Fourier route now feasible with
   `Lp.fourierTransformₗᵢ`, Cauchy–Schwarz with `∫(1+|ξ|²)^{-2} = π²`), heat
   semigroup calculus (K1–K3). Estimated size: 800–1500 lines. Scheduling it
   before `LocalTheory.lean` is the critical path; nothing in the batch above
   depends on it.
5. **F-SOLDENS** (`lem:solenoidal-density`): vector potential on the Fourier
   side, Hardy inequality along rays, cutoff; needed for ESS (1.3). Estimated
   500–900 lines. Alternative considered and rejected: weakening the Lean
   `IsLerayHopf` to drop `J̊`-membership would make the axiom stronger than
   ESS (unsafe direction).
6. **Endpoint of `lem:leray-hopf`** (weak limit at `S_*`): needs the Riesz
   representation (`InnerProductSpace.toDual`) and `orthogonalProjection`
   onto `solenoidalL2`; Mathlib has both. Required because `thm:continuation`
   applies ESS on the full cylinder `Q_{S_*}`.
7. **Tao (ii) and Corollary 4.3 not axiomatised.** Documented omissions;
   (ii) is unused by the paper's proof, 4.3 only serves `prop:localtheory`(ii)
   second half, which no downstream CP1 theorem uses (`CriticalBound` is
   instantiated on the branch; R-CRIT stays a documentation item).
8. **Class strengthening in both positions (RT-10).** `IsH1Mild` includes
   `meas`, `duhamel_int`, `L2H2_int`. In conclusion position (5.8, (i)) these
   assert properties Tao's solutions have but Tao does not print; the Phase II
   lemma `IsH1Mild.duhamel_integrand_bounded` and the equivalence with the
   integrability-free class should be recorded in `paper-lean-specification.md`
   as the one place where the Lean class is not letter-for-letter Tao's.
9. **`fourierMultiplierCLM` is unusable for singular symbols** (checked in
   source: `smulLeftCLM` is `0` unless `HasTemperateGrowth`). Any future
   design mentioning `TemperedDistribution.fourierMultiplierCLM` with a
   Riesz/Leray/`Δ⁻¹` symbol is wrong; use `Lp.fourierTransformₗᵢ` with
   `boundedMultiplier`.
10. **Names.** `RegularityPackage'` keeps the old name alive; once
    `LocalTheory.lean` lands and `docs/paper-lean-specification.md` is
    rewritten, rename to `RegularityPackage` and the old one to
    `UniformSobolevBounds` in one controller commit.
11. **`Fact (1 ≤ 3)`** instance already lives in `QuotientObjects.lean`;
    `Lp _ 4` and `Lp _ 5` are never formed as types here (only `MemLp`/`eLpNorm`
    with those exponents), so no new `Fact` instances are needed.
