# CP01 — Lean statement surface design for `navier-formal`

Lane: Lean statement surface design (MODE: INTEGRATE design; nothing is
proved, nothing is compiled). Owner file: this note only. Date: 2026-09-05.

## 0. Scope, sources, and what this note is not

This note fixes the *statement surface* of the CP1 formalization: the
Mathlib-only definitions, the Challenge theorem list, the exact shape of every
Phase I literature axiom, the Palomar-compatible split between a
hypothesis-carrying conditional theorem and a Phase-II-complete one, the module
plan, and the definition-level fidelity risks. It does not prove anything, and
it does not decide any mathematical question. NS-R3 remains OPEN;
HIGH-PRESSURE and HIGH-STRAIN remain open; no Lean code below has been
elaborated.

Inputs, all directly inspected on this machine unless marked:

- `/home/ert/proj/navier-paper/main.tex` (562 lines, read in full; HEAD
  contains `sec:quotient`).
- `/home/ert/proj/navier/PLAN.md` (CP1 definition, gates 1–3, wave table),
  `docs/proof-graph.yaml`, `docs/proof.md`.
- `research/evidence/cp01-mathlib-coverage.md` (Mathlib survey, the prescribed
  input), `cp01-manuscript-obligations.md` (obligation IDs L-1, C-0, C-2, C-3,
  P-0…P-3, F-1, E-1, N-1, Q-0…Q-18 are reused verbatim below),
  `cp01-palomar-checklist.md` (routes A/B/C, PAL-TOOLCHAIN, PAL-AXIOMS).
- `research/evidence/hf17-quotient-functional.md`,
  `hf17-review-quotient-functional.md`, `hf17-quotient-evolution.md`,
  `hf17-review-quotient-evolution.md`.
- `literature/foundations.md`, `literature/critical-criteria.md`.
- Sibling conventions: `/home/ert/proj/stafford38/{AGENTS.md,PLAN.md,
  lakefile.toml,Stafford38.lean,Stafford38/Statement.lean,
  Stafford38/PaperInputs.lean,Stafford38/PaperAxioms.lean,
  docs/literature-assumptions.yaml,docs/paper-lean-specification.md}`.
- Mathlib at `/home/ert/proj/stafford38/.lake/packages/mathlib`, tag
  `v4.33.1`, commit `0df444a360eaa60ab8c11dca51a86af692955474`, toolchain
  `leanprover/lean4:v4.33.1`. Declarations cited below were located by
  `grep`/`sed` at the stated `file:line`; none was type-checked.
- Tao 2013 Theorem 5.4 / Corollary 4.3 and Gallagher–Koch–Planchon 2013
  Theorem 4: **not re-inspected here**; the exact statements are taken from
  `cp01-manuscript-obligations.md` §0.1–0.2, which records direct inspection
  of arXiv:1108.1165v4 pp. 3–36 and arXiv:1012.0145v3 pp. 1–20. Every axiom
  shape in §3 must be re-checked against those pages by the CP01 literature
  lane before it is frozen.
- Fefferman's Clay statement: metadata-only here; text from
  `literature/foundations.md` (which records direct inspection of Clay PDF
  pp. 63–64).

Conventions used in the Lean blocks: `open scoped ENNReal ContDiff
RealInnerProductSpace Convolution`, `open MeasureTheory InnerProductSpace
Laplacian`. `∞` is `((⊤ : ℕ∞) : WithTop ℕ∞)`
(`Analysis/Calculus/ContDiff/FTaylorSeries.lean:120`), `Δ` is
`Laplacian.laplacian` (`Analysis/Distribution/DerivNotation.lean:276`)
instantiated by `InnerProductSpace.instLaplacian`
(`Analysis/InnerProductSpace/Laplacian.lean:140` ff.), `⟪x, y⟫` is `inner ℝ x y`
(`Analysis/InnerProductSpace/Defs.lean:91`). `‖·‖ₑ` is `enorm`
(`Analysis/Normed/Group/Defs.lean:82`).

---

## 1. Design decisions (with justification)

| # | Decision | Why |
|---|---|---|
| D1 | State space `E := EuclideanSpace ℝ (Fin 3)`, fields `E → E`, time-dependent fields `ℝ → E → E` (curried). | `EuclideanSpace` carries `InnerProductSpace ℝ`, `FiniteDimensional`, `MeasureSpace` (Haar volume via `OfBasis.lean:25`), `BorelSpace` (`Analysis/Normed/Lp/MeasurableSpace.lean:52`), `SecondCountableTopology` (`PiLp.lean:564`), and the `CoeFun` `x i := ofLp x i` (`PiLp.lean:91`). Currying makes `u t : E → E` directly usable with `fderiv`, `Δ`, `eLpNorm`. |
| D2 | Divergence is defined (`∑ i, fderiv ℝ v x (EuclideanSpace.single i 1) i`); Laplacian is Mathlib's `Δ`. | Mathlib has no `divergence` (coverage §6); `Δ` exists and `laplacian_eq_iteratedFDeriv_stdOrthonormalBasis` (`Laplacian.lean:194`) exhibits it as the trace of the second derivative, which is the manuscript's meaning. |
| D3 | `(u·∇)u` is `fderiv ℝ (u t) x (u t x)`. | The Fréchet derivative applied to the direction `u(t,x)` is exactly `∑_j u_j ∂_j u`. No index gymnastics. |
| D4 | Pressure is normalized by the Poisson equation plus `MemLp (p t) 2`, not by the Riesz formula. | Mathlib has no Riesz transforms (coverage §5). For a classical solution `Δp = -∂_i∂_j(u_iu_j)` is automatic (divergence of the momentum equation), so only the decay condition carries information; an `L²` harmonic function on `ℝ³` is zero, so this pins the same `p` as `R_iR_j(u_iu_j)` = Tao's normalized pressure (obligation P-1). The identification is a Phase I lemma (ID-P1 below), not a definition. |
| D5 | "Classical solution" = jointly `C^∞` on the open time interval, jointly continuous to `t = 0`, pointwise equations for `0 < t < T`, plus the `L^∞_tH¹ ∩ L²_tH²`-type class bounds on compact subintervals. "Smooth through `t = 0`" and "Tao-regular" are separate predicates. | This is the task's specification; the class bounds make the notion coincide with Tao's uniqueness class after Corollary 4.3 (obligation L-1), which is what `hyp:critical` "quantified over all classical solutions" needs to be faithful (§6, R-CLASS). |
| D6 | `hyp:critical` quantifies over all classical solutions on `[0,T')`, `T' ≤ H`, with no maximal time. | Requested by the task; equivalent to the manuscript's `sup_{t<min(H,T_*)}` once uniqueness is available (§6, R-CRIT). The Lean statement is per `(ν, u₀)`; the manuscript's universal hypothesis is its `∀`-closure. |
| D7 | Norms in conclusions of *identities* use explicit Frobenius (Hilbert–Schmidt) sums, not `eLpNorm (fderiv ℝ u) 2`. | `eLpNorm (fderiv ℝ u) 2` uses the operator norm on `E →L[ℝ] E`, which differs from `∑_{ij}(∂_ju_i)²` by a constant; an identity (energy, pressure balance) is false with the wrong norm (§6, R-NORM). Inequalities may use either. |
| D8 | `L³` quantities are stated in `ℝ≥0∞` via `eLpNorm v 3 volume`; `ℝ`-valued versions only where finiteness is a hypothesis. | `ENNReal.toReal ⊤ = 0`; a bound `(eLpNorm …).toReal ≤ M` is vacuous for a non-`L³` field. `eLpNorm … ≤ ENNReal.ofReal M` is not (§6, R-JUNK). |
| D9 | Kinetic energy for the Clay target is the `lintegral` `∫⁻ x, ‖u t x‖ₑ ^ 2`. | Same junk-value reason: the Bochner `∫ ‖u‖²` is `0` for non-integrable integrands. |
| D10 | The quotient functional is defined on `Lp E 3 volume` with `𝒢₃` the topological closure of the span of `L³`-classes a.e.-equal to gradients of `C_c^∞` potentials; `𝒬` is an `iInf` over the subtype; minimizers are quantified (`IsQuotientMinimizer`) rather than chosen. | `Submodule.topologicalClosure` (`Topology/Algebra/Module/Basic.lean:157`) and `Lp` exist; quantifying over minimizers avoids `Classical.choose` on a `sorry`-holed Challenge theorem, which would make a Challenge *definition* depend on a Challenge *hole* (§6, R-CHOOSE). |
| D11 | Heat is Gaussian convolution defined with Mathlib's `convolution`; Leray on `L³` is *hypothesized* as the existence of a CLM `P` with `P q = 0` on `𝒢₃` and `P u = u` on solenoidal fields. | Both are Mathlib-only statable; Leray boundedness is Calderón–Zygmund literature (coverage §5, F\*), heat facts are `F*` (coverage §3). Only the coercivity theorem needs `P`; it is stated with `P` as an explicit hypothesis so that route B stays hypothesis-free where possible (§2.3). |
| D12 | Literature axioms are stated at `ν = 1` exactly as published; the viscosity is removed by a Phase I lemma (`eq:nu-normalization`). | An axiom must transcribe the published statement; both Tao and GKP fix `ν = 1`. |
| D13 | The composite "endpoint continuation at the classical level" is *not* labelled GKP. It is derived from `gkp_theorem4` (verbatim-shaped, over a Mathlib-only mild-solution predicate) and the identification obligation C-2, each carried separately. | "No unproved project step is literature." The identification (uniqueness class, membership in `E_{p,q}`, the case `T* > νT_*`) is a manuscript obligation with sources still to be pinned. |
| D14 | Palomar: one repository, one `Challenge.lean` containing both the unconditional quotient/estimate theorems and the hypothesis-carrying conditional theorem; two comparator configurations; literature axioms live in a **non-default** `lean_lib` that neither `Challenge` nor `Solution` imports. | PAL-AXIOMS: custom axioms are unregistrable in any form; the sibling project's `PaperInputs`/`PaperAxioms` split does exactly this. |

---

## 2. Mathlib-only definitions (to be inlined verbatim in `Challenge.lean`)

Everything in this section imports only `Mathlib`. Line references are to the
`v4.33.1` checkout. **Not elaborated**; identifier existence was verified by
grep, argument order and implicit-argument shapes were read from source, but
coercion and instance resolution at these exact types is unverified (see §6,
R-ELAB).

### 2.1 Basic objects

```lean
import Mathlib

open scoped ENNReal ContDiff RealInnerProductSpace Convolution
open MeasureTheory InnerProductSpace Laplacian

namespace NavierFormal

/-- Physical space `ℝ³` with its Euclidean structure and Lebesgue (Haar) volume. -/
abbrev E : Type := EuclideanSpace ℝ (Fin 3)

/-- The `i`-th standard basis vector of `ℝ³`. -/
noncomputable abbrev e (i : Fin 3) : E := EuclideanSpace.single i 1

/-- Divergence `∑ᵢ ∂ᵢvᵢ` of a vector field, via the Fréchet derivative.
Junk value `0` where `v` is not differentiable (as `fderiv` is). -/
noncomputable def divergence (v : E → E) (x : E) : ℝ :=
  ∑ i : Fin 3, (fderiv ℝ v x (e i)) i

/-- Frobenius (Hilbert–Schmidt) square norm `∑ᵢⱼ (∂ⱼvᵢ)²` of the Jacobian of `v` at `x`.
This is the pointwise density of the manuscript's `‖∇u‖₂²`; it is **not** the operator
norm `‖fderiv ℝ v x‖²`. -/
noncomputable def jacobianSq (v : E → E) (x : E) : ℝ :=
  ∑ j : Fin 3, ‖fderiv ℝ v x (e j)‖ ^ 2

/-- Enstrophy `Y = ∫ ∑ᵢⱼ (∂ⱼvᵢ)²` as an extended real. -/
noncomputable def enstrophy (v : E → E) : ℝ≥0∞ :=
  ∫⁻ x, ENNReal.ofReal (jacobianSq v x)

/-- Kinetic energy `∫ |v|²` as an extended real (Lebesgue integral; never a junk `0`). -/
noncomputable def kineticEnergy (v : E → E) : ℝ≥0∞ :=
  ∫⁻ x, ‖v x‖ₑ ^ 2

/-- The `L³(ℝ³;ℝ³)` norm as an extended real, `⊤` when `v ∉ L³`. -/
noncomputable def L3norm (v : E → E) : ℝ≥0∞ :=
  eLpNorm v 3 volume

instance : Fact ((1 : ℝ≥0∞) ≤ 3) := ⟨by norm_num⟩

/-- Convection term `(v·∇)v` at `x`: the derivative of `v` in the direction `v x`. -/
noncomputable def convection (v : E → E) (x : E) : E :=
  fderiv ℝ v x (v x)

/-- Time derivative of a time-dependent field, one-sided from the right at `t = 0`
(`derivWithin` on `Set.Ici 0`; equals `deriv` for `t > 0`). -/
noncomputable def timeDeriv (u : ℝ → E → E) (t : ℝ) (x : E) : E :=
  derivWithin (fun s => u s x) (Set.Ici 0) t

/-- Iterated time derivative `∂ₜʲ`. -/
noncomputable def timeDerivIter (j : ℕ) (u : ℝ → E → E) : ℝ → E → E :=
  Nat.iterate timeDeriv j u
```

Notes. `Δ f x` for `f : E → E` is available through `InnerProductSpace.instLaplacian`
(needs `[InnerProductSpace ℝ E] [FiniteDimensional ℝ E]`, satisfied) and equals
`∑ i, iteratedFDeriv ℝ 2 f x ![e i, e i]` (`Laplacian.lean:194`), i.e. the trace
of the second derivative. `enorm` on `E` is `‖x‖ₑ = ENNReal.ofReal ‖x‖`
(`Analysis/Normed/Group/Basic.lean:396`).

### 2.2 Divergence-free Schwartz datum

```lean
/-- Clay/Fefferman data class: a Schwartz vector field `u₀ : ℝ³ → ℝ³` with `∇·u₀ = 0`
pointwise. `SchwartzMap` (`Analysis/Distribution/SchwartzSpace/Basic.lean:78`) is
`ContDiff ℝ ∞` with `‖x‖^k ‖iteratedFDeriv ℝ n f x‖` bounded for all `k n`, which is
Fefferman's `|∂^α u₀(x)| ≤ C_{αK}(1+|x|)^{-K}` for all `α, K`. -/
structure SchwartzDivFree where
  toSchwartz : SchwartzMap E E
  div_free : ∀ x : E, divergence (⇑toSchwartz) x = 0

instance : CoeFun SchwartzDivFree (fun _ => E → E) := ⟨fun u₀ => ⇑u₀.toSchwartz⟩

/-- Data in `H^k` for every `k` (Tao's remark after Theorem 5.4). Schwartz data satisfy it. -/
def AllSobolev (v : E → E) : Prop :=
  ∀ k : ℕ, MemLp (iteratedFDeriv ℝ k v) 2 volume
```

### 2.3 Classical solution of unforced Navier–Stokes on `ℝ³ × [0,T)`

```lean
/-- A classical solution of `∂ₜu + (u·∇)u + ∇p = νΔu, ∇·u = 0, u(0) = u₀` on `ℝ³ × [0,T)`.

* `u p` are jointly `C^∞` on `(0,T) × ℝ³` and jointly continuous on `[0,T) × ℝ³`;
* the momentum equation and incompressibility hold pointwise for `0 < t < T`;
* the pressure is normalized by `p(t) ∈ L²(ℝ³)` (D4): together with the Poisson
  equation, automatic for classical solutions, this pins the representative
  `p = R_iR_j(u_iu_j)` used in the manuscript (Phase I lemma ID-P1);
* on every compact `[0,T'] ⊂ [0,T)` the velocity has bounded `L²` norm and
  Frobenius-`L²` gradient and square-integrable-in-time second derivatives.
  These class bounds make the notion agree with Tao's `H¹` mild uniqueness class
  after Tao Corollary 4.3 (obligation L-1; see §6 R-CLASS).

The pointwise time derivative at `0 < t` is the ordinary derivative, because
`derivWithin … (Set.Ici 0) t = deriv … t` for `t > 0`. -/
structure IsClassicalSolution (ν : ℝ) (u₀ : E → E) (T : ℝ)
    (u : ℝ → E → E) (p : ℝ → E → ℝ) : Prop where
  smooth_u : ContDiffOn ℝ ∞ (fun q : ℝ × E => u q.1 q.2) (Set.Ioo 0 T ×ˢ Set.univ)
  smooth_p : ContDiffOn ℝ ∞ (fun q : ℝ × E => p q.1 q.2) (Set.Ioo 0 T ×ˢ Set.univ)
  cont_u : ContinuousOn (fun q : ℝ × E => u q.1 q.2) (Set.Ico 0 T ×ˢ Set.univ)
  cont_p : ContinuousOn (fun q : ℝ × E => p q.1 q.2) (Set.Ico 0 T ×ˢ Set.univ)
  initial : ∀ x, u 0 x = u₀ x
  momentum : ∀ t x, 0 < t → t < T →
    timeDeriv u t x + convection (u t) x + gradient (p t) x = ν • Δ (u t) x
  incompressible : ∀ t x, 0 < t → t < T → divergence (u t) x = 0
  pressure_L2 : ∀ t, 0 < t → t < T → MemLp (p t) 2 volume
  energy_class : ∀ T', T' < T → ∃ C : ℝ≥0∞, C < ⊤ ∧ ∀ t, 0 ≤ t → t ≤ T' →
    kineticEnergy (u t) ≤ C ∧ enstrophy (u t) ≤ C
  L2H2_class : ∀ T', T' < T →
    ∫⁻ t in Set.Ioc 0 T', eLpNorm (iteratedFDeriv ℝ 2 (u t)) 2 volume ^ 2 < ⊤

/-- Fefferman's `C^∞(ℝ³ × [0,T))` including the initial time: joint smoothness on the
closed-in-time set, in Mathlib's `ContDiffOn` sense (Taylor expansions within the set). -/
def SmoothThroughZero (T : ℝ) (u : ℝ → E → E) (p : ℝ → E → ℝ) : Prop :=
  ContDiffOn ℝ ∞ (fun q : ℝ × E => u q.1 q.2) (Set.Ico 0 T ×ˢ Set.univ) ∧
  ContDiffOn ℝ ∞ (fun q : ℝ × E => p q.1 q.2) (Set.Ico 0 T ×ˢ Set.univ)

/-- Tao 5.4(iv) regularity on every compact subinterval: `∂ₜʲu, ∂ₜʲp ∈ L^∞_t H^k_x` for all
`j k`. This is the hypothesis class of the quotient-evolution theorems and the conclusion
class of the local theory. -/
def TaoRegular (T : ℝ) (u : ℝ → E → E) (p : ℝ → E → ℝ) : Prop :=
  ∀ (j k : ℕ) (T' : ℝ), T' < T → ∃ C : ℝ≥0∞, C < ⊤ ∧ ∀ t, 0 ≤ t → t ≤ T' →
    eLpNorm (iteratedFDeriv ℝ k (timeDerivIter j u t)) 2 volume ≤ C ∧
    eLpNorm (iteratedFDeriv ℝ k
      (Nat.iterate (fun (q : ℝ → E → ℝ) t x => derivWithin (fun s => q s x) (Set.Ici 0) t)
        j p t)) 2 volume ≤ C

/-- The manuscript's `sec:quotient` class `u ∈ C H^m, u_t ∈ C H^{m-2}` on `[0,T']`
(boundedness form; the continuity-in-time part is R-REG in §6). -/
def SobolevClass (m : ℕ) (T : ℝ) (u : ℝ → E → E) : Prop :=
  ∀ T', T' < T → ∃ C : ℝ≥0∞, C < ⊤ ∧ ∀ t, 0 ≤ t → t ≤ T' →
    (∀ k, k ≤ m → eLpNorm (iteratedFDeriv ℝ k (u t)) 2 volume ≤ C) ∧
    (∀ k, k + 2 ≤ m → eLpNorm (iteratedFDeriv ℝ k (timeDeriv u t)) 2 volume ≤ C)
```

### 2.4 The Clay target (Fefferman alternative A, unforced, `ℝ³`)

```lean
/-- Fefferman's alternative (A) for one datum and one viscosity: there exist
`u, p ∈ C^∞(ℝ³ × [0,∞))` solving the unforced system with `u(0) = u₀`, `∇·u = 0`, and
one constant `C` with `∫ |u(x,t)|² dx < C` for every `t ≥ 0`. The time derivative is the
right derivative at `t = 0` (`derivWithin … (Set.Ici 0)`), so the equation is required on
all of `[0,∞)` as in the official statement. -/
def ClayAlternativeA (ν : ℝ) (u₀ : SchwartzDivFree) : Prop :=
  ∃ (u : ℝ → E → E) (p : ℝ → E → ℝ),
    ContDiffOn ℝ ∞ (fun q : ℝ × E => u q.1 q.2) (Set.Ici 0 ×ˢ Set.univ) ∧
    ContDiffOn ℝ ∞ (fun q : ℝ × E => p q.1 q.2) (Set.Ici 0 ×ˢ Set.univ) ∧
    (∀ x, u 0 x = u₀ x) ∧
    (∀ t x, 0 ≤ t →
      timeDeriv u t x + convection (u t) x + gradient (p t) x = ν • Δ (u t) x) ∧
    (∀ t x, 0 ≤ t → divergence (u t) x = 0) ∧
    ∃ C : ℝ, ∀ t, 0 ≤ t → kineticEnergy (u t) < ENNReal.ofReal C

/-- The full whole-space positive alternative: every admissible datum, every `ν > 0`. -/
def ClayAlternativeA_all : Prop :=
  ∀ (ν : ℝ), 0 < ν → ∀ u₀ : SchwartzDivFree, ClayAlternativeA ν u₀
```

Quantifier check against `def:target`: "For every such `u₀` and every `ν > 0`,
equation (1) has a solution `u,p ∈ C^∞(ℝ³×[0,∞))`, and `sup_{t≥0}∫|u|² < ∞`." The
`sup < ∞` is the single constant `C`. Fefferman does not normalize `p`; none is
imposed here. Match: exact, modulo R-T0 (§6).

### 2.5 The finite-horizon critical hypothesis (`hyp:critical`), no maximal time

```lean
/-- `hyp:critical` for one `(ν, u₀)`: for every finite horizon `H` there is a finite
`M = M(ν,u₀,H)` bounding `‖u(t)‖₃` for every classical solution on any `[0,T')` with
`T' ≤ H` and every `0 < t < T'`. No maximal solution is mentioned. The manuscript's
`sup_{0<t<min(H,T_*)} ‖u(t)‖₃ ≤ M` is recovered by taking the maximal branch restricted
to `[0, min(H,T_*))`; conversely, uniqueness (Tao 5.4(iii)) makes every such solution a
restriction of that branch, so the two forms are equivalent once uniqueness is
available (R-CRIT). The bound is stated in `ℝ≥0∞`, so a non-`L³` state violates it. -/
def CriticalBound (ν : ℝ) (u₀ : SchwartzDivFree) : Prop :=
  ∀ H : ℝ, 0 < H → ∃ M : ℝ, 0 ≤ M ∧
    ∀ (T' : ℝ) (u : ℝ → E → E) (p : ℝ → E → ℝ),
      T' ≤ H → IsClassicalSolution ν (⇑u₀) T' u p →
      ∀ t, 0 < t → t < T' → L3norm (u t) ≤ ENNReal.ofReal M

/-- The manuscript's universally quantified Hypothesis 5.3. -/
def CriticalHypothesis : Prop :=
  ∀ (ν : ℝ), 0 < ν → ∀ u₀ : SchwartzDivFree, CriticalBound ν u₀
```

### 2.6 Pressure-route quantities (`prop:pressure`, `prop:lowpressure`, `hyp:absorption`)

Adopting obligation P-0 (no `∇|u|`): with `(∇u)ᵀu` written through `⟪u, ∂ⱼu⟫` and
Lean's `x / 0 = 0` supplying the manuscript's "zero at `u = 0`" convention.

```lean
/-- `∂ⱼ|u|·|u| = ⟪u, ∂ⱼu⟫`; the vector `(∇u)ᵀu`. -/
noncomputable def gradAbsNum (v : E → E) (x : E) : Fin 3 → ℝ :=
  fun j => ⟪v x, fderiv ℝ v x (e j)⟫

/-- Density of `D₃`: `|u||∇u|² + |(∇u)ᵀu|²/|u|`, zero where `u = 0` (Lean's `a / 0 = 0`). -/
noncomputable def D3density (v : E → E) (x : E) : ℝ :=
  ‖v x‖ * jacobianSq v x + (∑ j, gradAbsNum v x j ^ 2) / ‖v x‖

noncomputable def D3 (v : E → E) : ℝ := ∫ x, D3density v x

/-- `u·∇|u| = ⟪u, (u·∇)u⟫ / |u|`, zero where `u = 0`. -/
noncomputable def uGradAbs (v : E → E) (x : E) : ℝ :=
  ⟪v x, convection v x⟫ / ‖v x‖

/-- Signed pressure work `P₃ = ∫ p u·∇|u|`. -/
noncomputable def P3 (q : E → ℝ) (v : E → E) : ℝ := ∫ x, q x * uGradAbs v x

/-- `X = ‖u‖₃³` as a real number (finite on the classical class). -/
noncomputable def X3 (v : E → E) : ℝ := ∫ x, ‖v x‖ ^ 3
```

Low-pass projector `S_J`. The manuscript fixes "a smooth homogeneous
Littlewood–Paley partition"; `prop:lowpressure` uses only `S_J`. Mathlib has no
Littlewood–Paley theory (coverage §4.4), so the profile is a parameter and the
theorem is stated for **every** admissible profile (stronger than the manuscript,
which fixes one).

```lean
/-- A low-pass profile: a real Schwartz kernel `K` whose Fourier transform (Mathlib's
`Real.fourierIntegral`, `e^{-2πi⟨x,ξ⟩}` convention, on the complexification) is real,
even, equal to `1` on the unit ball and `0` outside the ball of radius `2`. `S_J f := K_J ⋆ f`
with `K_J(x) = 2^{3J} K(2^J x)`. -/
structure LowPassProfile where
  K : SchwartzMap E ℝ
  fourier_real : ∀ ξ, (Real.fourierIntegral (fun x => (K x : ℂ)) ξ).im = 0
  fourier_even : ∀ ξ, Real.fourierIntegral (fun x => (K x : ℂ)) (-ξ)
    = Real.fourierIntegral (fun x => (K x : ℂ)) ξ
  fourier_one : ∀ ξ, ‖ξ‖ ≤ 1 → Real.fourierIntegral (fun x => (K x : ℂ)) ξ = 1
  fourier_supp : ∀ ξ, 2 ≤ ‖ξ‖ → Real.fourierIntegral (fun x => (K x : ℂ)) ξ = 0

/-- Dilated kernel `K_J`. -/
noncomputable def LowPassProfile.kernel (P : LowPassProfile) (J : ℤ) (x : E) : ℝ :=
  (2 : ℝ) ^ (3 * J) * P.K ((2 : ℝ) ^ J • x)

/-- `S_J f = K_J ⋆ f` (Mathlib convolution `Analysis/Convolution.lean:403`). -/
noncomputable def lowPass (P : LowPassProfile) (J : ℤ) (f : E → ℝ) : E → ℝ :=
  P.kernel J ⋆[ContinuousLinearMap.lsmul ℝ ℝ] f

/-- Vector version, componentwise. -/
noncomputable def lowPassVec (P : LowPassProfile) (J : ℤ) (v : E → E) : E → E :=
  fun x => ∑ i, (lowPass P J (fun y => v y i) x) • e i

/-- `L_J(t) = ∫ p_{≤J} u·∇|u|` and `Q_J(t) = ∫ (p - p_{≤J}) u·∇|u|`. -/
noncomputable def lowPressureWork (P : LowPassProfile) (J : ℤ)
    (q : E → ℝ) (v : E → E) : ℝ := P3 (lowPass P J q) v
noncomputable def highPressureWork (P : LowPassProfile) (J : ℤ)
    (q : E → ℝ) (v : E → E) : ℝ := P3 (fun x => q x - lowPass P J q x) v
```

Hypotheses `hyp:highpressure` and `hyp:absorption` (statements only; never proved):

```lean
/-- `hyp:absorption`, quantifier order `∃θ ∀(ν,u₀,H) ∃A ∀(sol,τ)`. -/
def AbsorptionHypothesis : Prop :=
  ∃ θ : ℝ, 0 ≤ θ ∧ θ < 1 ∧
    ∀ (ν : ℝ), 0 < ν → ∀ (u₀ : SchwartzDivFree) (H : ℝ), 0 < H →
      ∃ A : ℝ, 0 ≤ A ∧
        ∀ (T' : ℝ) (u : ℝ → E → E) (p : ℝ → E → ℝ), T' ≤ H →
          IsClassicalSolution ν (⇑u₀) T' u p → ∀ τ, 0 < τ → τ < T' →
            ∫ t in (0:ℝ)..τ, P3 (p t) (u t) ≤ θ * ν * ∫ t in (0:ℝ)..τ, D3 (u t) + A

/-- `hyp:highpressure`, with the profile universally quantified and `J, A_high` existential. -/
def HighPressureHypothesis (P : LowPassProfile) : Prop :=
  ∃ θ : ℝ, 0 ≤ θ ∧ θ < 1 ∧
    ∀ (ν : ℝ), 0 < ν → ∀ (u₀ : SchwartzDivFree) (H : ℝ), 0 < H →
      ∃ (J : ℤ) (A : ℝ), 0 ≤ A ∧
        ∀ (T' : ℝ) (u : ℝ → E → E) (p : ℝ → E → ℝ), T' ≤ H →
          IsClassicalSolution ν (⇑u₀) T' u p → ∀ τ, 0 < τ → τ < T' →
            ∫ t in (0:ℝ)..τ, highPressureWork P J (p t) (u t)
              ≤ θ * ν * ∫ t in (0:ℝ)..τ, D3 (u t) + A
```

### 2.7 Quotient-functional objects (`sec:quotient`)

```lean
/-- `L³(ℝ³;ℝ³)` as Mathlib's `Lp`. -/
abbrev L3 : Type := Lp E 3 (volume : Measure E)

/-- Compactly supported smooth scalar potentials. -/
def IsTestPotential (φ : E → ℝ) : Prop := ContDiff ℝ ∞ φ ∧ HasCompactSupport φ

/-- Generating set: `L³`-classes a.e. equal to `∇φ`, `φ ∈ C_c^∞`. -/
def gradientGenerators : Set L3 :=
  {g | ∃ φ : E → ℝ, IsTestPotential φ ∧ (g : E → E) =ᵐ[volume] gradient φ}

/-- `𝒢₃`: the `L³`-closure of `{∇φ : φ ∈ C_c^∞}` (a closed linear subspace). -/
noncomputable def gradientSubspace : Submodule ℝ L3 :=
  (Submodule.span ℝ gradientGenerators).topologicalClosure

/-- `𝒬(u) = inf_{q ∈ 𝒢₃} ⅓‖u+q‖₃³`. The infimum is over a nonempty set bounded below
by `0`, so `Real.iInf` is the true infimum (R-INF). -/
noncomputable def quotientFunctional (u : L3) : ℝ :=
  ⨅ q : gradientSubspace, (1 / 3 : ℝ) * ‖u + (q : L3)‖ ^ 3

/-- `w` is the minimizing representative of `u`: `w - u ∈ 𝒢₃` and `⅓‖w‖³ = 𝒬(u)`. -/
def IsQuotientMinimizer (u w : L3) : Prop :=
  w - u ∈ gradientSubspace ∧ (1 / 3 : ℝ) * ‖w‖ ^ 3 = quotientFunctional u

/-- `A = |w|w` as a function (lies in `L^{3/2}`). -/
noncomputable def cubicMap (w : L3) (x : E) : E := ‖(w : E → E) x‖ • (w : E → E) x

/-- Distributionally solenoidal `L³` field: `∫ ⟪u, ∇φ⟫ = 0` for every test potential. -/
def IsSolenoidalL3 (u : L3) : Prop :=
  ∀ φ : E → ℝ, IsTestPotential φ → ∫ x, ⟪(u : E → E) x, gradient φ x⟫ = 0

/-- Critical spatial scaling `(S_λ v)(x) = λ v(λx)` on functions. -/
noncomputable def criticalScale (l : ℝ) (v : E → E) : E → E := fun x => l • v (l • x)

/-- Heat kernel `G_s(x) = (4πs)^{-3/2} e^{-|x|²/4s}`, `s > 0`. -/
noncomputable def heatKernel (s : ℝ) (x : E) : ℝ :=
  (4 * Real.pi * s) ^ (-(3 : ℝ) / 2) * Real.exp (-‖x‖ ^ 2 / (4 * s))

/-- `e^{sΔ} v = G_s ⋆ v` (Mathlib convolution with scalar action). -/
noncomputable def heat (s : ℝ) (v : E → E) : E → E :=
  heatKernel s ⋆[ContinuousLinearMap.lsmul ℝ E] v

/-- Quotient heat dissipation `D_𝒬(u) = -∫ A·Δu` for a chosen minimizer `w`. -/
noncomputable def quotientDissipation (w : L3) (v : E → E) : ℝ :=
  -∫ x, ⟪cubicMap w x, Δ v x⟫

/-- Strain flux `∫ ⟪q, (A·∇)v⟫` with `q = w - u` and `(A·∇)v x = fderiv ℝ v x (A x)`. -/
noncomputable def strainFlux (w : L3) (q : E → E) (v : E → E) : ℝ :=
  ∫ x, ⟪q x, fderiv ℝ v x (cubicMap w x)⟫

end NavierFormal
```

Remarks. `Lp` elements coerce to functions (`α →ₘ[μ] E` then `⇑`); a.e. statements
are the honest way to relate them to pointwise gradients (R-AE). `gradient`
(`Analysis/Calculus/Gradient/Basic.lean:82`) is `(toDual ℝ E).symm (fderiv ℝ φ x)`,
i.e. the Riesz representative of `dφ`, which on `EuclideanSpace` is the usual `∇φ`.
`heat` requires `MemLp v 3` for the convolution to exist; existence and the `L³`
contraction are Phase I facts, not definitional.

---

## 3. `Challenge.lean` theorem list and the Phase I literature axioms

### 3.1 The literature inputs as one explicit `Prop`-structure

All at `ν = 1` (D12). Each field is documented with the published statement it
transcribes and the exact residue that is *not* literature.

```lean
namespace NavierFormal

/-- The literature premises of CP1, as explicit hypotheses (Palomar route A). Every field
is a statement in Mathlib terms only. Fields 1–3 transcribe Tao 2013, Theorem 5.4 (ii),
(iii), (iv) with the remark after its proof and Corollary 4.3; field 4 transcribes
Gallagher–Koch–Planchon 2013, Theorem 4 **composed with** the identification lemma C-2
(uniqueness class, membership of the classical branch in the strong-solution class, the
case `T* > T_*`), which is a manuscript obligation and not literature. See §3.3. -/
structure LiteratureInputs : Prop where
  /-- Tao Thm 5.4(ii)+(iv), ν = 1: there is an absolute `c > 0` such that every
  divergence-free datum in `H^k` for all `k` with `T·(‖u₀‖₂ + ‖∇u₀‖₂)⁴ ≤ c` has a classical
  solution on `[0,T)` (in the class of `IsClassicalSolution`), smooth through `t = 0` and
  Tao-regular. (The "mild ⇒ classical" step for smooth mild solutions is residue ID-M.) -/
  local_existence : ∃ c : ℝ, 0 < c ∧
    ∀ (u₀ : E → E), AllSobolev u₀ → (∀ x, divergence u₀ x = 0) →
      ∀ T : ℝ, 0 < T →
        ENNReal.ofReal T * (eLpNorm u₀ 2 volume + eLpNorm (fderiv ℝ u₀) 2 volume) ^ 4
          ≤ ENNReal.ofReal c →
        ∃ (u : ℝ → E → E) (p : ℝ → E → ℝ),
          IsClassicalSolution 1 u₀ T u p ∧ SmoothThroughZero T u p ∧ TaoRegular T u p
  /-- Tao Thm 5.4(iii) + Cor 4.3, ν = 1: two classical solutions (in the class) with the
  same datum agree on their common interval. -/
  uniqueness : ∀ (u₀ : E → E) (T₁ T₂ : ℝ) (u₁ u₂ : ℝ → E → E) (p₁ p₂ : ℝ → E → ℝ),
    IsClassicalSolution 1 u₀ T₁ u₁ p₁ → IsClassicalSolution 1 u₀ T₂ u₂ p₂ →
    ∀ t x, 0 ≤ t → t < min T₁ T₂ → u₁ t x = u₂ t x
  /-- Tao Thm 5.4(iv) + remark, ν = 1: a classical solution (in the class) from data in
  `H^k` for all `k` is smooth through `t = 0` and Tao-regular on `[0,T)`. -/
  regularity : ∀ (u₀ : E → E) (T : ℝ) (u : ℝ → E → E) (p : ℝ → E → ℝ),
    AllSobolev u₀ → IsClassicalSolution 1 u₀ T u p →
    SmoothThroughZero T u p ∧ TaoRegular T u p
  /-- GKP Thm 4 (ESS endpoint) ∘ identification C-2, ν = 1: a classical solution on a
  finite `[0,T)` from `H^∞ ∩ L³` data with `sup_{t<T} ‖u(t)‖₃ < ∞` extends to a classical
  solution on `[0,T+δ)`. -/
  endpoint_continuation : ∀ (u₀ : E → E) (T : ℝ) (u : ℝ → E → E) (p : ℝ → E → ℝ),
    AllSobolev u₀ → MemLp u₀ 3 volume → 0 < T →
    IsClassicalSolution 1 u₀ T u p →
    (∃ M : ℝ, ∀ t, 0 < t → t < T → L3norm (u t) ≤ ENNReal.ofReal M) →
    ∃ (δ : ℝ) (u' : ℝ → E → E) (p' : ℝ → E → ℝ), 0 < δ ∧
      IsClassicalSolution 1 u₀ (T + δ) u' p' ∧ ∀ t x, 0 ≤ t → t < T → u' t x = u t x

end NavierFormal
```

### 3.2 Challenge theorems (all stated with `sorry`; `Solution.lean` proves the same types)

Naming: `NavierFormal.<name>`. "Needs" lists the literature fields (or the
Phase I axioms of §3.3, when the theorem is stated *without* explicit
hypotheses in the non-default axiomatic library) and the Mathlib-absent
infrastructure the Solution must supply.

| # | Declaration | Statement (informal, exact quantifiers) | Manuscript | Needs |
|---|---|---|---|---|
| T1 | `clay_alternative_A_of_critical_bound (L : LiteratureInputs) {ν} (hν : 0 < ν) (u₀ : SchwartzDivFree) (h : CriticalBound ν u₀) : ClayAlternativeA ν u₀` | The conditional theorem, per datum. | `thm:conditional` (+ `thm:continuation`, `premise:local`) | `L.local_existence`, `L.uniqueness`, `L.regularity`, `L.endpoint_continuation`; Phase I: maximal development L-1, `ν`-normalization lemma (`eq:nu-normalization`), Schwartz ⇒ `AllSobolev ∩ L³`, "`∂ₜʲu ∈ L^∞_tH^k ∀j,k` ⇒ jointly `C^∞`" (C-3), T2 for the energy bound. |
| T1' | `clay_alternative_A_all_of_critical_hypothesis (L : LiteratureInputs) (h : CriticalHypothesis) : ClayAlternativeA_all` | `∀`-closure of T1. | `thm:conditional` verbatim | T1. |
| T2 | `energy_identity {ν u₀ T u p} (hν : 0 < ν) (hs : IsClassicalSolution ν u₀ T u p) (hr : TaoRegular T u p) : ∀ s t, 0 ≤ s → s ≤ t → t < T → IntervalIntegrable (fun τ => (enstrophy (u τ)).toReal) volume s t ∧ (1/2) * (kineticEnergy (u t)).toReal + ν * ∫ τ in s..t, (enstrophy (u τ)).toReal = (1/2) * (kineticEnergy (u s)).toReal` | Exact identity with Frobenius enstrophy (D7). | `prop:energy` | Mathlib IBP `integral_bilinear_fderiv_right_eq_neg_left_of_integrable` (`LineDeriv/IntegrationByParts.lean:195`); `divergence` product rule (F, coverage #13); differentiation under the integral (`ParametricIntegral.lean:165`); FTC (`FundThmCalculus.lean:1148`). No literature axiom. |
| T2' | `energy_bounds … : (∀ t, 0 ≤ t → t < T → kineticEnergy (u t) ≤ kineticEnergy u₀) ∧ ∫⁻ t in Set.Ioo 0 T, enstrophy (u t) ≤ kineticEnergy u₀ / (2 * ENNReal.ofReal ν)` | The two consequences. | `prop:energy` | T2. |
| T3 | `scaling_invariance {ν u₀ T u p} (hs : IsClassicalSolution ν u₀ T u p) (l : ℝ) (hl : 0 < l) : IsClassicalSolution ν (criticalScale l u₀) (T / l^2) (fun t => criticalScale l (u (l^2 * t))) (fun t x => l^2 * p (l^2 * t) (l • x))` and `scaling_norm (v : E → E) (l : ℝ) (hl : 0 < l) (q : ℝ≥0∞) : eLpNorm (criticalScale l v) q volume = ENNReal.ofReal (l ^ (1 - 3 / q.toReal)) * eLpNorm v q volume` | Scaling of the system and of `L^q` norms. | `prop:scaling` (first two claims) | Change of variables under dilation (`Jacobian.lean:1213`), `IsClassicalSolution` transport. The class bounds transform with explicit powers of `l` (R-SCALE). |
| T3' | `L4L3_bound … : ∃ C : ℝ, 0 < C ∧ ∀ T' < T, ∫ t in (0:ℝ)..T', (L3norm (u t)).toReal ^ 4 ≤ C * (⨆ t ∈ Set.Ioo 0 T', (kineticEnergy (u t)).toReal) * ∫ t in (0:ℝ)..T', (enstrophy (u t)).toReal` | `eq:L4L3`. | `prop:scaling` | Lyapunov interpolation (F, #11), Sobolev `H¹ ⊂ L⁶` without compact support (`SobolevInequality.lean:600` + cutoff, F #12). The manuscript's meta-clause "they do not imply `L^∞_tL³`" is not a proposition and is not encoded (S-2). |
| T4 | `enstrophy_inequality … (hs) (hr) : ∃ C : ℝ, 0 < C ∧ ∀ t, 0 < t → t < T → HasDerivAt (fun τ => (enstrophy (u τ)).toReal) (Y' t) t ∧ (1/2) * Y' t + (ν/2) * ∫ x, ‖Δ (u t) x‖^2 ≤ C * ν⁻¹^3 * ((enstrophy (u t)).toReal)^3` (with `Y'` existentially bound) | Cubic differential inequality. | `prop:enstrophy` | Gagliardo–Nirenberg two-derivative step (F #10, via `‖∇²u‖₂ = ‖Δu‖₂`, Plancherel `Analysis/Fourier/LpSpace.lean:48` + complexification F #14), Young (`MeanInequalities.lean:507`). Not in the conditional chain. |
| T5 | `scalar_obstruction (C T : ℝ) (hC : 0 < C) (hT : 0 < T) : ∃ y : ℝ → ℝ, (∀ t ∈ Set.Ico 0 T, 0 < y t) ∧ (∀ t ∈ Set.Ico 0 T, HasDerivAt y (C * y t ^ 3) t) ∧ IntegrableOn y (Set.Ico 0 T) ∧ Tendsto y (𝓝[<] T) atTop` | Explicit `y = (2C(T-t))^{-1/2}`. | `prop:ode` | Mathlib only. |
| T6 | `pressure_balance … (hs) (hr) : ∀ s t, 0 < s → s ≤ t → t < T → IntervalIntegrable (fun τ => D3 (u τ)) volume s t ∧ IntervalIntegrable (fun τ => P3 (p τ) (u τ)) volume s t ∧ (1/3) * X3 (u t) + ν * ∫ τ in s..t, D3 (u τ) = (1/3) * X3 (u s) + ∫ τ in s..t, P3 (p τ) (u τ)` | Integrated form (obligation P-3), P-0 definitions. | `prop:pressure` | IBP with `‖·‖^p` calculus (`NormPow.lean:32,108`), `ε`-regularization and dominated convergence (`DominatedConvergence.lean:57`), integrability bookkeeping (F #7); pressure in `L² ∩ L^∞` from `TaoRegular` (P-1 route, no CZ). |
| T6' | `pressure_work_shift_invariant (q : E → ℝ) (c : ℝ) (v) (hv : …) : P3 (fun x => q x + c) v = P3 q v` | `P₃` unchanged under `p ↦ p + c(t)`. | `prop:pressure` last sentence | `∫ div(|u|u) = 0`. |
| T7 | `low_frequency_pressure_bound (P : LowPassProfile) : ∃ C : ℝ, 0 < C ∧ ∀ {ν} (hν : 0 < ν) (u₀ : SchwartzDivFree) {T u p} (hs : IsClassicalSolution ν u₀ T u p) (hr : TaoRegular T u p) (H : ℝ) (J : ℤ) (τ : ℝ), 0 < τ → τ < min H T → \|∫ t in (0:ℝ)..τ, lowPressureWork P J (p t) (u t)\| ≤ C * 2^(3*J) * ((kineticEnergy u₀).toReal)^2 * Real.sqrt (H / (2*ν))` | `A_low` with `‖u₀‖₂⁴ = E₀²`; `C` depends only on the profile. | `prop:lowpressure` | Kernel bound `‖K_J ⋆ R_iR_j‖_∞ ≤ C2^{3J}` — with D4 the composite is `S_J p` directly, and the needed estimate is `‖S_J p‖_∞ ≤ C2^{3J}‖u⊗u‖₁`, which needs the Fourier representation of `p` (ID-P1) and `L¹ * L^∞` Young (M‑, coverage §8); time Cauchy–Schwarz; T2'. |
| T8 | `absorption_of_low_and_high (P) (h : HighPressureHypothesis P) : AbsorptionHypothesis` | `A = A_low + A_high`. | text after `hyp:absorption` | T7. |
| T9 | `critical_of_absorption (h : AbsorptionHypothesis) : CriticalHypothesis` with `M = (‖u₀‖₃³ + 3A)^{1/3}` | `eq:pressure-consequence`. | text after `hyp:critical` | T6, `L.regularity`-free (the class alone suffices for T6 if `TaoRegular` is derived — see R-REG). |
| T10 | `quotient_minimizer_exists_unique (u : L3) : ∃! w, IsQuotientMinimizer u w` | Existence and uniqueness. | `sec:quotient` ¶1; Q-1, Q-2 | Route: uniform convexity of the cubic functional ⇒ Cauchy minimizing sequence ⇒ `Lp.instCompleteSpace` (coverage §1.4, flagged as a change of proof; re-audit against `hf17-review-quotient-functional.md`, which itself already gives a direct envelope argument). No literature axiom. |
| T11 | `quotient_stationarity {u w} (hw : IsQuotientMinimizer u w) : ∀ q ∈ gradientSubspace, ∫ x, ⟪cubicMap w x, (q : E → E) x⟫ = 0` | Euler–Lagrange, `div A = 0`. | Q-3 | `hasFDerivAt_norm_rpow` (`NormPow.lean:32`), differentiation under the integral. |
| T12 | `quotient_coercive (P : L3 →L[ℝ] L3) (hP0 : ∀ q ∈ gradientSubspace, P q = 0) (hP1 : ∀ u, IsSolenoidalL3 u → P u = u) (u : L3) (hu : IsSolenoidalL3 u) : ‖u‖^3 / (3 * ‖P‖^3) ≤ quotientFunctional u ∧ quotientFunctional u ≤ (1/3) * ‖u‖^3` | Coercivity with the Leray projection as an explicit hypothesis (D11). | `sec:quotient` coercivity display; Q-4 | Mathlib only given `P`. The *existence* of such `P` is the Phase I axiom A-LERAY (§3.3) and is not needed for this statement. |
| T13 | `quotient_scaling (u : L3) (l : ℝ) (hl : 0 < l) (hu' : MemLp (criticalScale l u) 3 volume) : quotientFunctional (hu'.toLp _) = quotientFunctional u` and `quotient_homogeneous (a : ℝ) : quotientFunctional (a • u) = \|a\|^3 * quotientFunctional u` | Scaling invariance and cubic homogeneity. | Q-5 | Dilation change of variables; `S_λ 𝒢₃ = 𝒢₃`. |
| T14 | `quotient_heat_monotone (u : L3) (s : ℝ) (hs : 0 < s) (h : MemLp (heat s u) 3 volume) : quotientFunctional (h.toLp _) ≤ quotientFunctional u`, plus `heat_memLp_three (u : L3) (s) (hs) : MemLp (heat s u) 3 volume` | Heat monotonicity. | Q-6 | Phase I axioms A-HEAT-1 (`L³` contraction), A-HEAT-2 (`G_s ∇φ = ∇ G_s φ`, closure invariance) or their proofs (coverage §3, F\*). |
| T15 | `quotient_hasFDerivAt (u w : L3) (hw : IsQuotientMinimizer u w) : ∃ L : L3 →L[ℝ] ℝ, (∀ h : L3, L h = ∫ x, ⟪cubicMap w x, (h : E → E) x⟫) ∧ HasFDerivAt quotientFunctional L u` | Fréchet derivative `D𝒬(u)[h] = ∫ A·h`. | `sec:quotient` "Fréchet differentiable …"; Q-7 | Uniform monotonicity of `z ↦ |z|z` in `ℝ³`, Hölder pairing `ContinuousLinearMap.lpPairing` (`MeasureTheory/Function/Holder.lean:142`). |
| T16 | `quotient_annihilates_gradients (u w) (hw) (q ∈ gradientSubspace) : (the `L` of T15) q = 0` and `pressure_gradient_mem {ν u₀ T u p} (hs) (hr : TaoRegular T u p) (t) (ht : 0 < t ∧ t < T) : ∃ hg : MemLp (gradient (p t)) 3 volume, hg.toLp _ ∈ gradientSubspace` | Gradient annihilation; `∇p ∈ 𝒢₃` on the classical class. | (16)–(17) of HF17; Q-9 | Cutoff + mollifier (`ContDiffBump` family, M). |
| T17 | `quotient_dissipation_nonneg {ν u₀ T u p} (hs) (hm : SobolevClass m T u) (hm4 : 4 ≤ m) (t) (ht) (hu3 : MemLp (u t) 3 volume) (w) (hw : IsQuotientMinimizer (hu3.toLp _) w) : 0 ≤ quotientDissipation w (u t)` | `D_𝒬 ≥ 0` from the heat generator. | "Its sign follows by differentiating the heat contraction at zero"; Q-11 | A-HEAT-3 (generator limit in `L³` when `u, Δu ∈ L³`), T14, T15. |
| T18 | `quotient_evolution {ν u₀ T u p} (hs : IsClassicalSolution ν u₀ T u p) (hm : SobolevClass m T u) (hm4 : 4 ≤ m) (t) (ht : 0 < t ∧ t < T) : ∀ (hu3 : ∀ τ, MemLp (u τ) 3 volume) (w : L3) (hw : IsQuotientMinimizer ((hu3 t).toLp _) w), HasDerivAt (fun τ => quotientFunctional ((hu3 τ).toLp _)) (-(ν * quotientDissipation w (u t)) - strainFlux w (fun x => (w : E → E) x - u t x) (u t)) t` | `eq:quotient-evolution`, pressure-free. | `eq:quotient-evolution`; Q-10, Q-12…Q-16 | T15, T16, chain rule along `C¹_tL³` curves; the inner-variation identity (Q-12…Q-16) needs flow of a frozen `C¹` divergence-free field with Liouville volume preservation (coverage §10, F\* ≈65–100) or a Phase I axiom A-FLOW; change of variables (`Jacobian.lean:1213`, M). |
| T19 | `low_strain_bound (P : LowPassProfile) : ∃ C, 0 < C ∧ ∀ … (L : ℤ) (t) (w) (hw) …, \|strainFlux w q (lowPassVec P L (u t))\| ≤ C * 2^((5*L)/2 : ℝ) * Real.sqrt ((kineticEnergy u₀).toReal) * quotientFunctional ((hu3 t).toLp _)` (with `q = w - u(t)` and `‖q‖₃ ≤ C'‖w‖₃` coming from T12's `P`) | `|K_L^{low}| ≤ M𝒬(u)`, `M = C2^{5L/2}‖u₀‖₂`. | `sec:quotient` last paragraph; Q-17 | Bernstein `‖∇S_Lf‖_∞ ≤ C2^{5L/2}‖f‖₂` (F #9 or axiom A-BERN), T2', T12 (so the Leray `P` reappears as a hypothesis, or its existence axiom is used). |
| T20 | `quotient_gronwall_of_high_strain (P) (θ A : ℝ) (hθ : θ ≤ 1) … (hgap : ∀ τ, 0 < τ → τ < min H T → ∫ t in (0:ℝ)..τ, K_L t ≤ θ * ν * ∫ t in (0:ℝ)..τ, D_𝒬 t + A) : ∀ τ, … quotientFunctional (u τ) ≤ (quotientFunctional u₀ + A) * Real.exp (M * H)` and the `L³` corollary via T12 | The conditional Grönwall corollary (`eq:quotient-gap` ⇒ critical quotient bound). | "Integration of (eq:quotient-evolution) and Gronwall would then bound 𝒬" | T18, T19, `le_gronwallBound_of_liminf_deriv_right_le` (`Analysis/ODE/Gronwall.lean:112`). `eq:quotient-gap` is a hypothesis, never proved. |

Auxiliary Challenge declarations needed so the compared theorems are
self-contained: everything in §2, plus `IsQuotientMinimizer`, `LiteratureInputs`.
Total estimated size: ≈ 420–520 lines, i.e. above Palomar's 300-line warning
threshold but below the 1,000-line hard limit; keep docstrings terse or split
route B and route A into two Challenge modules (`ChallengeQuotient.lean`,
`ChallengeConditional.lean`) with two configurations (§4).

### 3.3 Phase I axioms (non-default library `NavierFormal/Literature/Axioms.lean`) — exact shapes

Each axiom is a *named constant of a `Prop` already defined in Mathlib-only
terms*, so that "the axiom transcribes the published statement" can be audited
by reading one `def` and one source record. Sources: `S` = directly inspected
(by the cited CP01 note), `M` = metadata-only, `P` = to be pinned.

```lean
namespace NavierFormal.Literature

/-- Tao 2013 Thm 5.4(ii)+(iv) at ν = 1, for data in `H^k ∀k` (remark after the proof),
as `LiteratureInputs.local_existence`. Source: arXiv:1108.1165v4 pp. 33–34 (S, via
cp01-manuscript-obligations §0.1). Residue ID-M: "smooth H¹ mild solution ⇒ classical
pointwise equation" (Tao's Duhamel formulation (10)/(11) plus smoothness). -/
axiom tao_local_existence :
  ∃ c : ℝ, 0 < c ∧ ∀ (u₀ : E → E), AllSobolev u₀ → (∀ x, divergence u₀ x = 0) →
    ∀ T : ℝ, 0 < T →
      ENNReal.ofReal T * (eLpNorm u₀ 2 volume + eLpNorm (fderiv ℝ u₀) 2 volume) ^ 4
        ≤ ENNReal.ofReal c →
      ∃ u p, IsClassicalSolution 1 u₀ T u p ∧ SmoothThroughZero T u p ∧ TaoRegular T u p

/-- Tao 2013 Thm 5.4(iii) + Cor 4.3 at ν = 1 (S). Residue ID-C: `IsClassicalSolution`'s
class bounds must be shown to be Tao's "almost smooth H¹ solution" hypotheses of Cor 4.3
(R-CLASS). -/
axiom tao_uniqueness : ∀ (u₀ : E → E) (T₁ T₂ : ℝ) u₁ u₂ p₁ p₂,
  IsClassicalSolution 1 u₀ T₁ u₁ p₁ → IsClassicalSolution 1 u₀ T₂ u₂ p₂ →
  ∀ t x, 0 ≤ t → t < min T₁ T₂ → u₁ t x = u₂ t x

/-- Tao 2013 Thm 5.4(iv) + remark, at ν = 1 (S). -/
axiom tao_regularity : ∀ (u₀ : E → E) (T : ℝ) u p,
  AllSobolev u₀ → IsClassicalSolution 1 u₀ T u p → SmoothThroughZero T u p ∧ TaoRegular T u p

/-- Gallagher–Koch–Planchon 2013 Thm 4, verbatim shape, ν = 1 (S, arXiv:1012.0145v3 p. 18):
for `u₀ ∈ L³`, `sup_{t<T*} ‖NS(u₀)(t)‖₃ < ∞ ⇒ T* = ∞`. `IsMaximalL3Mild u₀ T v` is the
Mathlib-only predicate "v is the maximal strong solution NS(u₀)" defined in
`Literature/MildSolution.lean` (Duhamel identity with Gaussian convolution and the Leray
multiplier on tempered distributions, `v ∈ C([0,T);L³)`, maximality). Its faithfulness
to GKP's `E_{p,q}(T)` class is R-MILD. -/
axiom gkp_theorem4 : ∀ (u₀ : E → E) (T : ℝ≥0∞) (v : ℝ → E → E),
  MemLp u₀ 3 volume → IsMaximalL3Mild u₀ T v →
  (∃ M : ℝ, ∀ t : ℝ, 0 ≤ t → (t : ℝ≥0∞) < T → L3norm (v t) ≤ ENNReal.ofReal M) → T = ⊤

/-- Obligation C-2 (NOT literature; sources to be pinned: uniqueness in `C([0,T];L³)`
(Furioli–Lemarié-Rieusset–Terraneo 2000, P) and persistence/regularity of the `L³` strong
solution (P)): the classical branch from `H^∞ ∩ L³` data at ν = 1 is the restriction of
`NS(u₀)`, and if `NS(u₀)` lives past `T` then so does a classical solution. -/
axiom classical_branch_identification : ∀ (u₀ : E → E) (T : ℝ) u p,
  AllSobolev u₀ → MemLp u₀ 3 volume → 0 < T → IsClassicalSolution 1 u₀ T u p →
  ∃ (T' : ℝ≥0∞) (v : ℝ → E → E), IsMaximalL3Mild u₀ T' v ∧ (T : ℝ≥0∞) ≤ T' ∧
    (∀ t x, 0 ≤ t → t < T → v t x = u t x) ∧
    ((T : ℝ≥0∞) < T' → ∃ (δ : ℝ) u' p', 0 < δ ∧ IsClassicalSolution 1 u₀ (T + δ) u' p' ∧
      ∀ t x, 0 ≤ t → t < T → u' t x = u t x)

/-- Leray projection on `L³(ℝ³)`: a bounded idempotent annihilating `𝒢₃` and fixing
distributionally solenoidal fields. Source: Riesz transforms bounded on `L^p`, `1<p<∞`
(Stein, *Singular Integrals*, Ch. II §4 / Grafakos CFA Cor. 5.2.8; P), plus the
`L³`-fixing argument Q-4 (project obligation, not literature). Composite. -/
axiom leray_projection_L3 : ∃ P : L3 →L[ℝ] L3,
  (∀ q ∈ gradientSubspace, P q = 0) ∧ (∀ u, IsSolenoidalL3 u → P u = u)

/-- Heat semigroup facts on `L³` (textbook: e.g. Stein *Singular Integrals* Ch. III §2;
Pazy *Semigroups* Ch. 1; P). Separately: contraction, gradient-space invariance, generator. -/
axiom heat_contraction_L3 : ∀ (v : E → E), MemLp v 3 volume → ∀ s, 0 < s →
  MemLp (heat s v) 3 volume ∧ eLpNorm (heat s v) 3 volume ≤ eLpNorm v 3 volume
axiom heat_preserves_gradientSubspace : ∀ (q : L3), q ∈ gradientSubspace → ∀ s, 0 < s →
  ∀ h : MemLp (heat s q) 3 volume, h.toLp _ ∈ gradientSubspace
axiom heat_generator_L3 : ∀ (v : E → E), ContDiff ℝ 2 v → MemLp v 3 volume →
  MemLp (Δ v) 3 volume → ∀ h : ∀ s, MemLp (heat s v) 3 volume,
  Tendsto (fun s : ℝ => (eLpNorm (fun x => (heat s v x - v x) / s - Δ v x) 3 volume))
    (𝓝[>] 0) (𝓝 0)

/-- Bernstein for the low-pass projector (provable from Young's convolution inequality,
F ≈15–25 lemmas; carried as an axiom only until proved): `‖∇S_L f‖_∞ ≤ C 2^{5L/2} ‖f‖₂`. -/
axiom bernstein_lowpass : ∀ (P : LowPassProfile), ∃ C : ℝ, 0 < C ∧
  ∀ (f : E → E) (L : ℤ) (x : E), MemLp f 2 volume →
    ‖fderiv ℝ (lowPassVec P L f) x‖ ≤ C * 2 ^ ((5 * L : ℤ) / 2 : ℝ) * (eLpNorm f 2 volume).toReal

/-- Volume-preserving flow of a frozen bounded smooth divergence-free field (Picard–Lindelöf
is M, `ExistUnique.lean:57`; assembly into a `C¹` flow map with `det DΦ_s = 1` is F\*,
coverage §10). Only needed by T18's inner variation. -/
axiom divfree_flow : ∀ (v : E → E), ContDiff ℝ ∞ v → (∀ x, divergence v x = 0) →
  (∃ B, ∀ x, ‖v x‖ ≤ B ∧ ‖fderiv ℝ v x‖ ≤ B) →
  ∃ Φ : ℝ → E → E, (∀ x, Φ 0 x = x) ∧ (∀ s x, HasDerivAt (fun r => Φ r x) (v (Φ s x)) s) ∧
    (∀ s, MeasurePreserving (Φ s) volume volume) ∧
    (∀ s, ContDiff ℝ 1 (Φ s)) ∧ (∀ s t, Φ s ∘ Φ t = Φ (s + t))

end NavierFormal.Literature
```

`IsMaximalL3Mild` (in `Literature/MildSolution.lean`, Mathlib-only): `v t ∈ L³`
for `t < T`, `t ↦ (v t).toLp` continuous into `L3` on `[0,T)`, `v 0 = u₀`, and
for each `t`, the Duhamel identity `v(t) = heat t u₀ - ∫₀ᵗ heat (t-s) (ℙ div(v⊗v))(s) ds`
holds a.e., where `ℙ div(v ⊗ v)` is defined on tempered distributions through
`TemperedDistribution.fourierMultiplierCLM` with symbol
`ξ ↦ (δ_{ik} - ξ_iξ_k/|ξ|²)(2πi ξ_j)` applied to `v_j v_k ∈ L^{3/2} ⊂ 𝓢'`
(`Lp.toTemperedDistribution`, `TemperedDistribution.lean:158`), and maximality
means no such `v'` exists on a strictly larger interval. This is the heaviest
definition in the design and the largest single faithfulness exposure (R-MILD).
If the CP02 literature lane cannot pin GKP's class to `C([0,T);L³)` with a named
uniqueness theorem, the fallback is to drop `gkp_theorem4` + `classical_branch_identification`
and carry the composite `endpoint_continuation` field of §3.1 directly as one
axiom labelled `composite: GKP Thm 4 + C-2`, which is honest but not verbatim.

Axiom report expectation for the axiomatic root (Phase I gate 2):
`propext, Classical.choice, Quot.sound` plus exactly the named constants above
that the proof uses. Any other name is a gate failure.

---

## 4. Palomar structure: hypothesis-carrying vs Phase-II-complete, and coexistence

Constraint (PAL-AXIOMS, `cp01-palomar-checklist.md` §2.2): `permitted_axioms ⊆
{propext, Quot.sound, Classical.choice}`; Comparator rejects any Solution
declaration depending on a custom axiom. Decision (D14):

1. **`Challenge.lean` states two families.**
   - *Family B (unconditional):* T2–T7, T10–T20 exactly as in §3.2. None mentions
     `LiteratureInputs`; the only "hypotheses" are the mathematical ones the
     manuscript itself imposes (class membership, `MemLp`, the explicit Leray
     `P` in T12/T19, the explicit gap `hgap` in T20). Registrable now (route B)
     once the Solution proves them **without** the §3.3 axioms — which for T14,
     T17, T18, T19 means the heat, flow, and Bernstein facts must be *proved*
     (F/F\*), not axiomatized. Until then those four are stated in the Challenge
     but excluded from `comparator-quotient.json`'s `theorem_names`.
   - *Family A (conditional):* T1, T1', T8, T9 with `LiteratureInputs` (and the
     manuscript hypotheses) as explicit arguments. Registrable as route A; every
     field of `LiteratureInputs` is Mathlib-only by construction (§3.1).
2. **`Solution.lean`** imports `NavierFormal` (default `lean_lib`, no axioms) and
   proves both families. The Family A proofs consume the `L : LiteratureInputs`
   argument; they never touch `NavierFormal.Literature.Axioms`.
3. **`NavierFormal/Literature/Axioms.lean` and `NavierFormal/Literature/Instances.lean`**
   belong to a second, non-default `lean_lib` (`NavierFormalLiterature`), exactly
   like `Stafford38/PaperInputs.lean` and `PaperAxioms.lean` in the sibling.
   `Instances.lean` proves `literatureInputs_of_axioms : LiteratureInputs` from
   the axioms (this is where the `ν = 1 → ν` scaling, the `gkp_theorem4 ∘
   classical_branch_identification` composition, and ID-M/ID-C are discharged in
   Phase I) and exports the axiomatic root theorem
   `clay_alternative_A_of_critical_bound_axiomatic {ν} hν u₀ (h : CriticalBound ν u₀) :
   ClayAlternativeA ν u₀ := clay_alternative_A_of_critical_bound literatureInputs_of_axioms hν u₀ h`
   with `set_option pp.fullNames true in #print axioms …` (sibling convention,
   `PaperAxioms.lean:76`). This file is the Phase I gate-2 artefact and is never
   in any Challenge import closure.
4. **Phase II** replaces each axiom by a theorem of the same name and type in
   `NavierFormal/Literature/*.lean` (default library), after which
   `literatureInputs : LiteratureInputs` is a theorem and `Challenge.lean` gains
   `clay_alternative_A_of_critical_bound' {ν} hν u₀ (h : CriticalBound ν u₀) : ClayAlternativeA ν u₀`
   with no `L` argument. Both versions coexist: the `L`-carrying one remains the
   registered route-A statement; the primed one is added to a third configuration
   only when its axiom report is clean. Nothing about `hCritical` changes: it is
   the open node and stays an explicit hypothesis in every version.
5. **Configurations.** `comparator-quotient.json` (route B: T2–T7, T10–T13, T15,
   T16; extend with T14, T17–T20 when heat/flow/Bernstein are proved);
   `comparator-conditional.json` (route A: T1, T1', T8, T9). Submit B first;
   A only after the narrative states in its first sentence that the Millennium
   problem is not solved (checklist §5). `formalization.yaml`
   `status.main_results[].literature_dependencies` lists Tao 5.4 and GKP 4 with
   the exact pages, mirroring `stafford38/docs/literature-assumptions.yaml`.
6. **Toolchain.** PAL-TOOLCHAIN is unresolved: no `lean4export` tag for `v4.33.1`
   as of 2026-09-05. The statement surface is toolchain-independent between
   `v4.33.0` and `v4.33.1` as far as the declarations cited here (all present at
   `0df444a`; the checklist records `db584cd6…` for `v4.33.0` but that tree was
   not inspected). Decide before `lake init`.

What is registered when: route B after Phase I *and* the proofs of the F/F\*
infrastructure it needs (no axiom may remain in its Solution path); route A
after Phase I (its Solution path is axiom-free by construction); the primed
Phase-II theorem after Phase II.

---

## 5. Module plan for `/home/ert/proj/navier-formal`

Mirrors the sibling: repository root is the Lake project; default library
`NavierFormal` with root `NavierFormal.lean` importing every default module;
`Challenge.lean`/`Solution.lean` as separate `lean_lib`s (checklist §1.2).

| Order | Module | Content | Depends on | Lane |
|---|---|---|---|---|
| 0 | `NavierFormal/Basic.lean` | §2.1: `E`, `e`, `divergence`, `jacobianSq`, `enstrophy`, `kineticEnergy`, `L3norm`, `convection`, `timeDeriv`; lemmas: `Δ` as trace, `divergence` product rule, Frobenius vs operator norm equivalence, `PiLp` component lemmas | Mathlib | L0 (blocking) |
| 0 | `NavierFormal/Solution.lean` | §2.2–2.5: `SchwartzDivFree`, `AllSobolev`, `IsClassicalSolution`, `SmoothThroughZero`, `TaoRegular`, `SobolevClass`, `ClayAlternativeA`, `CriticalBound`; restriction/extension lemmas; `derivWithin = deriv` for `t > 0` | Basic | L0 |
| 1 | `NavierFormal/Calculus/IBP.lean` | wrappers of `integral_bilinear_fderiv_right_eq_neg_left_of_integrable` for `E`-valued fields, `∫ div F = 0`, `∫ ⟪u, ∇p⟫ = -∫ p div u` | Basic | L1 |
| 1 | `NavierFormal/Calculus/Interpolation.lean` | Lyapunov `‖f‖_r ≤ ‖f‖_p^θ‖f‖_q^{1-θ}` (F #11); Sobolev `‖u‖₆ ≤ C‖∇u‖₂` without compact support (F #12) | Basic | L1 |
| 1 | `NavierFormal/Calculus/Sobolev.lean` | `AllSobolev` for Schwartz data; `TaoRegular ⇒ u(t), p(t) ∈ L^q` for all `q`, `∇p ∈ L³`, boundedness of `u, ∇u`; "`∂ₜʲu ∈ L^∞_tH^k ∀j,k ⇒` jointly `C^∞`" (C-3) | Basic, Solution | L1 |
| 1 | `NavierFormal/Literature/Statements.lean` | `LiteratureInputs`; `IsMaximalL3Mild` (`MildSolution.lean`) | Solution, Quotient/Space (for `L3`) | L1' (parallel with L1) |
| 1 | `NavierFormal/Literature/Sources.lean` | docstring-only source records (title, arXiv id, page, theorem number, inspection status) per axiom; `docs/literature-assumptions.yaml` mirrors it | — | L1' |
| 2 | `NavierFormal/Energy.lean` | T2, T2' | Calculus/IBP, Sobolev | L2a |
| 2 | `NavierFormal/Scaling.lean` | T3, T3', `ν`-normalization lemma (`eq:nu-normalization`) | Calculus/Interpolation, Solution | L2a |
| 2 | `NavierFormal/Enstrophy.lean` | T4 (needs Plancherel bridge F #14, GN F #10) | Calculus/* | L2b |
| 2 | `NavierFormal/Ode.lean` | T5 | Mathlib | L2b |
| 2 | `NavierFormal/Pressure.lean` | §2.6 definitions, ID-P1 (Poisson + `L²` ⇒ Riesz representative; needs `L²`-harmonic Liouville, F), T6, T6' | Calculus/*, Sobolev | L2c |
| 2 | `NavierFormal/Quotient/Space.lean` | `L3`, `gradientSubspace`, `IsSolenoidalL3`, closedness, Schwartz-gradient membership | Basic | L2d |
| 3 | `NavierFormal/LittlewoodPaley.lean` | `LowPassProfile`, `lowPass`, kernel `L^∞`/`L²` bounds, Young `L¹ * L^∞`, Bernstein (or axiom) | Calculus/* | L3a |
| 3 | `NavierFormal/LowPressure.lean` | T7, T8, T9 | LittlewoodPaley, Pressure, Energy | L3a (after L2c) |
| 3 | `NavierFormal/Quotient/Minimizer.lean` | T10, T11 (uniform convexity route) | Quotient/Space | L3b |
| 3 | `NavierFormal/Quotient/Coercivity.lean` | T12 | Quotient/Space | L3b |
| 3 | `NavierFormal/Quotient/Scaling.lean` | T13 | Quotient/Minimizer | L3b |
| 3 | `NavierFormal/Quotient/Heat.lean` | `heatKernel`, `heat`, T14, `heat_memLp_three` (from axioms or proofs) | Quotient/Minimizer, Literature/Statements | L3c |
| 3 | `NavierFormal/Quotient/Derivative.lean` | T15, T16 | Quotient/Minimizer, Sobolev | L3d |
| 4 | `NavierFormal/Quotient/Evolution.lean` | T17, T18 (inner variation; flow axiom or proof) | Quotient/Heat, Quotient/Derivative, Pressure (ID-P1 for `∇p ∈ L³`) | L4a |
| 4 | `NavierFormal/Quotient/Gronwall.lean` | T19, T20 | Quotient/Evolution, LittlewoodPaley, Energy | L4a |
| 4 | `NavierFormal/Continuation.lean` | maximal development L-1 (`T_*`, gluing, `H¹` blow-up alternative), `thm:continuation` in the C-0 shape from `LiteratureInputs` | Solution, Scaling, Literature/Statements | L4b |
| 5 | `NavierFormal/Conditional.lean` | T1, T1' | Continuation, Energy, Calculus/Sobolev | L5 |
| 5 | `NavierFormal/Literature/Axioms.lean`, `Instances.lean` | §3.3 axioms; `literatureInputs_of_axioms`; axiomatic root with `#print axioms` (non-default lib) | Literature/Statements, Conditional | L5' |
| 6 | `Challenge.lean`, `Solution.lean`, `comparator-*.json`, `formalization.yaml`, `docs/paper-lean-specification.md` | §3.2, §4 | all | controller |

Parallelism: L0 must land first (two files, one agent). Then L1, L1' in
parallel (four agents, disjoint files). Then L2a–L2d in parallel (four agents).
Then L3a–L3d (four agents). L4a and L4b in parallel. L5 and L5' sequentially.
No two lanes share a file; every lane's public names are fixed by this note so
that downstream lanes can be written against `sorry` stubs before upstream
proofs land (`lake env lean <file>` single-file checks, PLAN wave CP04).

---

## 6. Definition-level fidelity risks

Each risk names the encoded object, the manuscript object, the discrepancy, and
the action. "Action" is a Phase I lemma or a documented divergence in
`formalization.yaml` `fidelity.divergences`.

| ID | Encoding | Manuscript | Risk | Action |
|---|---|---|---|---|
| R-LAP | `Δ v x` = Mathlib `InnerProductSpace.laplacian` (sum of `iteratedFDeriv ℝ 2 v x ![e i, e i]`), junk when `v` is not `C²` at `x` | `Δu = ∑ᵢ ∂ᵢ²u` | Convention agrees (no sign, no `1/2`); junk values are harmless inside `IsClassicalSolution` where `u(t)` is `C^∞`, but any theorem stated for a bare `v : E → E` must carry `ContDiff ℝ 2 v`. | Lemma `laplacian_eq_sum_second_partials` for `C²` fields; audit every use of `Δ` outside the class. |
| R-PRESS | `p(t) ∈ L²` + Poisson (automatic) | `p = R_iR_j(u_iu_j)` | The two agree iff `L²`-harmonic functions on `ℝ³` vanish and the Riesz representative is in `L²` (true for `u(t) ∈ H^k`). Neither is in Mathlib. If ID-P1 is not proved, `prop:lowpressure` cannot be stated as the manuscript states it. | Phase I lemma ID-P1 (needs Fourier characterization of `L²` solutions of Poisson: Plancherel `Fourier/LpSpace.lean:48` + tempered-distribution multiplier `FourierMultiplier.lean:143`). Record as a divergence until proved. |
| R-NORM | `enstrophy` uses Frobenius `jacobianSq`; `eLpNorm (fderiv ℝ v) 2` uses the operator norm | `‖∇u‖₂² = ∫∑ᵢⱼ(∂ⱼuᵢ)²` | Identities (T2, T6) are false with the operator norm; `TaoRegular`/`energy_class` are finiteness conditions and may use either. Mathlib's GNS constant is for the operator norm. | Lemma `opNorm_sq_le_jacobianSq ∧ jacobianSq ≤ 3 * opNorm_sq` in Basic; never mix inside an identity. |
| R-JUNK | `L3norm`, `kineticEnergy`, `enstrophy` in `ℝ≥0∞`; `.toReal` only under finiteness | `‖u‖₃`, `∫|u|²` | `ENNReal.toReal ⊤ = 0`, Bochner `∫ = 0` for non-integrable integrands. A hypothesis `(…).toReal ≤ M` would be vacuous. | `CriticalBound`, `ClayAlternativeA` energy bound, and `gkp_theorem4` are stated in `ℝ≥0∞` (done). T2/T6 use `.toReal` only with `IntervalIntegrable` in the conclusion and class finiteness in the hypotheses. |
| R-ESS | `∀ t, 0 < t → t < T' → …` (pointwise sup) | `ess sup_{0<t<T_*}‖u(t)‖₃` in `thm:continuation`; `sup` in `hyp:critical` | Identical because `t ↦ u(t)` is continuous into `L³` on the class (obligation C-0), but the Lean statement is the pointwise one. | Lemma `continuous_L3_of_class` (from `TaoRegular`); note in `paper-lean-specification.md`. |
| R-CRIT | `CriticalBound` quantifies over all classical solutions on `[0,T')`, `T' ≤ H` | `sup_{0<t<min(H,T_*)}` on the maximal branch | Equivalent given `tao_uniqueness`; without uniqueness the Lean hypothesis is at least as strong, making T1 at most weaker — the safe direction. Per-datum form is stronger than the manuscript's `∀`-closed hypothesis, i.e. T1 is a finer theorem than `thm:conditional`; T1' restores the exact shape. | Phase I lemma `criticalBound_iff_maximal_form` once L-1 lands. |
| R-CLASS | `IsClassicalSolution` class bounds (`L^∞_t(L² ∩ Ḣ¹)`, `L²_tH²`, `p ∈ L²`) | "the maximal classical solution" from Tao's `H¹` mild class via Cor 4.3 | Tao's definition of "almost smooth `H¹` solution" (input to Cor 4.3) was not re-read here; the class bounds must be matched field by field (ID-C). Too weak a class makes `tao_uniqueness` false-to-source; too strong a class makes `tao_local_existence` claim more than Tao proves. | CP01 literature lane: quote Tao's Definition (p. 3 and p. 9) verbatim and adjust the four class fields before freezing. |
| R-T0 | `IsClassicalSolution`: smooth on `(0,T)`, continuous on `[0,T)`; `SmoothThroughZero` and `ClayAlternativeA` use `ContDiffOn … (Set.Ici 0 ×ˢ univ)`; time derivative `derivWithin … (Set.Ici 0)` | "`u,p ∈ C^∞(ℝ³×[0,∞))`", "smooth through the initial time" | Mathlib's `ContDiffOn` on a set with boundary is the "Taylor series within the set" notion (`ContDiffWithinAt`); for the half-space this is the standard `C^∞` up to the boundary but is not literally "extends smoothly across `t = 0`" (Seeley extension is not in Mathlib). The equation at `t = 0` uses the right derivative. | Document as the interpretation of `C^∞(ℝ³×[0,∞))`; optional Phase II lemma: extendability. |
| R-MEAS | `IsSolenoidalL3`, `gradientGenerators`, `IsQuotientMinimizer` are a.e./`Lp`-level; `divergence`, `momentum` are pointwise | mixed | Pointwise statements on the class imply the a.e. ones (`u(t)` is continuous), never conversely. T18 relates a pointwise classical field to an `L³` class through `MemLp.toLp`; every such coercion needs `AEStronglyMeasurable` (automatic from continuity) and the a.e. equality `⇑(hv.toLp v) =ᵐ v` (`MemLp.coeFn_toLp`). | Bridge lemmas in Quotient/Space. |
| R-AE | `gradientGenerators` uses `=ᵐ[volume] gradient φ` | `{∇φ : φ ∈ C_c^∞}` | Faithful; `gradient φ` is continuous so a.e. equality is the only sensible relation to an `Lp` class. | none |
| R-INF | `quotientFunctional` is `Real.iInf` over the subtype `gradientSubspace` | `inf_{q∈𝒢₃}` | `Real.iInf` is `0` when the set is not bounded below; here it is bounded below by `0` and nonempty (`q = 0`), so it is the true infimum. | Lemma `quotientFunctional_eq_sInf`, `quotientFunctional_nonneg`, `quotientFunctional_le_cube`. |
| R-CHOOSE | Minimizers are quantified (`IsQuotientMinimizer`), not defined by `Classical.choose` of T10 | "the minimizer `q`", "`w = u + q`", "`A = |w|w`" | If a Challenge `def` used `Classical.choose (T10 …)` it would depend on a `sorry` hole; the comparator compares Solution definitions to Challenge definitions by type, but the editorial vacuity check would flag it. Quantifying over `w` with `hw` is equivalent given T10 (uniqueness). | Keep; add `quotientMinimizer` as a `noncomputable def` in `NavierFormal/Quotient/Minimizer.lean` only (Solution side), never in Challenge. |
| R-LERAY | T12/T19 take a Leray `P` as an explicit hypothesis | "the bounded Leray projection `ℙ`" | Faithful as a conditional statement; the constant `‖P‖` is the manuscript's `‖ℙ‖_{L³→L³}`. Without `leray_projection_L3` (axiom or Phase II theorem) the unconditional coercivity is not available. | Keep explicit in route B; discharge with the axiom in the axiomatic root. |
| R-HEAT | `heat s v` is Mathlib's `convolution` with `heatKernel s`, which is `0` when the convolution integral does not exist | `e^{sΔ}` | For `v ∈ L³` the integral exists (Young); the definition is faithful on `L³`. The generator axiom is stated with the difference quotient in `L³`, matching "`Δu ∈ L³` justifies this generator limit". | `heat_memLp_three` before any use. |
| R-LP | `LowPassProfile` is a parameter; `prop:lowpressure` is stated for every profile | one fixed "smooth homogeneous Littlewood–Paley partition" | Stronger than the manuscript (universal in the profile); `Real.fourierIntegral` uses the `e^{-2πi⟨x,ξ⟩}` convention (`Analysis/Fourier/FourierTransform.lean`), so the constants in T7 depend on that convention (F-1). The "real, even" requirement of `review-frequency.md` is encoded. | Record the convention in the docstring; T7's `C` is existential so no numeric convention leaks into the statement. |
| R-P0 | `D3density`, `uGradAbs` via `⟪u, ∂ⱼu⟫/‖u‖` with Lean's `a/0 = 0` | `|u||∇|u||²`, `u·∇|u|` with "the second integrand is zero at `u = 0`" and "`∇|u| = 0` a.e. on the zero set of its Sobolev representative" | P-0 of the obligations audit: the encoded quantities are the ones the `ε`-regularization actually produces; they equal the manuscript's a.e. on `{u ≠ 0}` and satisfy the stated convention on `{u = 0}` by definition. The manuscript's Sobolev-representative phrasing is not encoded. | Document as a definitional choice; prove `D3density_eq_of_ne_zero`. |
| R-REG | T17–T20 hypothesize `SobolevClass m T u` with `4 ≤ m`; T6/T7 hypothesize `TaoRegular` | `sec:quotient`: "`u ∈ CH^m, u_t ∈ CH^{m-2}, m ≥ 4`"; `prop:pressure`: "on each compact time interval `u ∈ L² ∩ L⁶`, `∇u ∈ L²`, `p ∈ L² ∩ L³`" | `SobolevClass` encodes boundedness, not continuity in time; the inner-variation argument uses bounded uniformly continuous `∇u` (from `H^m`, `m ≥ 4`) and `u ∈ C¹_tL³` (from `u_t ∈ CH^{m-2}`), both derivable from the boundedness form plus the pointwise equation. `TaoRegular` is stronger than what T6 needs (P-2 lists exact memberships); using it makes T6 a weaker theorem than `prop:pressure`. | State T6 with the P-2 memberships instead of `TaoRegular` once P-2 is written (CP02); keep `TaoRegular` as the default until then and record the divergence. |
| R-SCALE | T3's transported solution must satisfy the class bounds with rescaled constants | `prop:scaling` says only "solves the same equation" | The class bounds scale (`‖u_λ‖₂² = λ^{-1}‖u‖₂²` etc.), so T3 is provable, but it asserts more than the manuscript. | Prove; note the strengthening. |
| R-MILD | `IsMaximalL3Mild` (Duhamel with Gaussian convolution and tempered-distribution Leray multiplier, `C([0,T);L³)`, maximality) | GKP's `NS(u₀)` in `E_{p,q}(T)`, `3 < p ≤ q < ∞`, with the `L³` remark | GKP define `NS(u₀)` in Besov classes; the `C_tL³` characterization rests on their remark and reference [9]. Encoding `E_{p,q}` needs Besov spaces (F\*). The Fourier-multiplier Leray on `𝓢'` requires a complex codomain (complexification, F #14) and the symbol is singular at `ξ = 0` (measurable, bounded, so `fourierMultiplierCLM` applies if its hypotheses allow merely bounded symbols — to be checked: `FourierMultiplier.lean:50` takes `g : E → 𝕜` with a growth hypothesis on the Schwartz side). | CP01 literature lane pins the uniqueness class; if `C_tL³` cannot be justified from a named theorem, fall back to the composite axiom (§3.3 last paragraph) and label it composite. |
| R-NU | Axioms at `ν = 1`; theorems for `ν > 0` | Tao/GKP at `ν = 1`; manuscript `ν > 0` with `eq:nu-normalization` | The scaling lemma must transport `IsClassicalSolution`, `TaoRegular`, `SmoothThroughZero`, `L3norm` exactly as displayed (`‖v(s)‖₃ = ν^{-1}‖u(s/ν)‖₃`). | `Scaling.lean` lemma `nu_normalization`. |
| R-ELAB | None of §2–§3 has been elaborated | — | Implicit-argument shapes (`eLpNorm` default `volume` via `volume_tac`, `Lp` coercions, `ContDiffOn` on product sets, `Nat.iterate` on curried functions, `⋆[L]` notation scope, `EuclideanSpace.single`'s `𝕜` argument) may need adjustment. The *meaning* of each definition is fixed by this note; the *spelling* is provisional. | CP03 lane: first commit is `lake env lean` on `Basic.lean` and `Solution.lean` with every definition and no theorem. |

---

## 7. Cross-check against the manuscript's exact quantifiers (summary)

| Manuscript | Lean | Match |
|---|---|---|
| `def:target`: `∀u₀ ∀ν>0 ∃(u,p) ∈ C^∞(ℝ³×[0,∞)) … ∧ sup_t∫|u|²<∞` | `ClayAlternativeA_all` | exact (R-T0) |
| `hyp:critical`: `∀ν>0 ∀u₀ ∀H ∃M ∀t<min(H,T_*)` | `CriticalHypothesis` | exact modulo uniqueness (R-CRIT), sup vs pointwise (R-ESS) |
| `thm:conditional`: `hyp:critical ⇒ def:target` | T1' (and finer per-datum T1) | exact |
| `thm:continuation` (C-0 shape): `T_*<∞ ∧ sup<∞ ⇒ False` | `LiteratureInputs.endpoint_continuation` + `Continuation.lean` | composite (D13) |
| `hyp:absorption`: `∃θ ∀(ν,u₀,H) ∃A ∀τ` | `AbsorptionHypothesis` | exact; θ outside `∀` as in the manuscript (graph ABSORPTION wording differs, obligations §2 item 2) |
| `hyp:highpressure`: `∃θ ∀(ν,u₀,H) ∃(J,A) ∀τ` | `HighPressureHypothesis P` | exact, plus `∀P` |
| `prop:lowpressure`: `∀J ∀H ∀τ<min(H,T_*)`, constant `C` absolute | T7 with `C` after `P` | exact given profile parametrization (R-LP) |
| `sec:quotient` results | T10–T20 | exact modulo D10/D11 choices and R-REG |

---

## Frontier record

**MODE / RESULT:** INTEGRATE design. A complete Mathlib-only statement
surface for CP1 is specified: definitions (§2), Challenge theorem list T1–T20
with docstrings and dependencies (§3.2), eleven Phase I axioms with exact Lean
shapes and source labels (§3.3), the Palomar coexistence structure (§4), a
26-module plan with lanes (§5), and 19 fidelity risks (§6). Nothing was
compiled or proved.

**CLAIM AND SCOPE:** the design covers the original unforced equation on `ℝ³`
with `ν > 0`, Schwartz divergence-free data, and the classical branch in Tao's
uniqueness class; no forced, periodic, hyperdissipative, Euler, averaged, or
weak-nonunique variant appears in any compared statement.

**EVIDENCE:** manuscript read in full; every Mathlib identifier located at
`v4.33.1` `0df444a` by grep with `file:line`; obligations, coverage, Palomar,
and HF17 notes read in full; sibling `PaperInputs`/`PaperAxioms` structure
inspected and copied.

**FIRST GAP (for this lane):** R-MILD/R-CLASS — the two literature axioms whose
*hypotheses* are solution-class predicates (`IsClassicalSolution` for Tao,
`IsMaximalL3Mild` for GKP) cannot be frozen until Tao's "almost smooth `H¹`
solution" definition and GKP's `E_{p,q}`-versus-`C_tL³` class are quoted
verbatim by the CP01 literature lane. Immediately behind it: ID-P1 (pressure
normalization by `L²` + Poisson must be proved equal to the Riesz
representative before `prop:lowpressure` is stated faithfully).

**SURVIVING CONDITIONAL SUFFIX:** with the four `LiteratureInputs` fields as
explicit hypotheses, T1/T1' are Mathlib-only, axiom-free, Palomar-route-A
statable today; T2, T3, T5, T10–T13, T15, T16 are route-B statable with no
literature input at all; T6, T7 need only ID-P1 (project lemma); T14, T17–T20
need heat/flow/Bernstein facts as axioms (Phase I) or proofs (route B).

**UNNECESSARY DEPENDENCIES:** Calderón–Zygmund theory is not needed for any
compared statement (Leray is an explicit hypothesis in T12/T19; pressure is
pinned by decay, D4); Littlewood–Paley theory beyond one low-pass kernel is not
needed; reflexivity/Clarkson are not needed if T10 takes the uniform-convexity
route (re-audit required); `∇|u|` and Rademacher are not needed (P-0).

**NON-CLAIMS:** no claim that any theorem T1–T20 is provable as spelled; no
claim that the Lean text elaborates; no claim that `hyp:critical`,
`hyp:absorption`, `hyp:highpressure`, or `eq:quotient-gap` is provable; no
claim about NS-R3, which remains OPEN; no Palomar submission, repository, or
identifier is created or authorized.

**NEXT DISTINCT ACTION:** CP03 lane creates `NavierFormal/Basic.lean` and
`NavierFormal/Solution.lean` from §2.1–2.5 verbatim and runs
`lake env lean` on them (definitions only), reporting every spelling fix as a
diff against this note; CP01 literature lane resolves R-CLASS and R-MILD.
