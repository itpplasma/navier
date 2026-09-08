# CP02-7 AUDIT (round 1): review of `cp02-quotient-evolution.md`

MODE: REVIEW, proof-audit discipline. Date: 2026-09-05. Lane: audit of
`research/evidence/cp02-quotient-evolution.md` (obligations Q-8 .. Q-18,
`eq:quotient-evolution`, `eq:quotient-gap`).

## 0. Freeze record

| Item | Value |
| --- | --- |
| Candidate file | `../navier/research/evidence/cp02-quotient-evolution.md` |
| `sha256sum` | `cb117fe34d4d8c8f1f037fef5223e1691ca2fdf05bd37bf38016496c86c4171b` |
| `git -C ../navier rev-parse HEAD` | `715ce84ec78d64c510e150360a354b5d55648b9c` |
| Manuscript | `../navier-paper/main.tex`, 562 lines, read in full |
| Sibling lanes read | `cp02-quotient-functional.md`, `cp02-lowpressure.md`, `cp01-manuscript-obligations.md` §1.14, `cp01-literature-statements.md`, `cp01-quotient-section-structure.md` |
| Independent compile | LaTeX block extracted, spliced under an independent stub preamble, `latexmk -pdf` run twice: exit 0, **zero** undefined references, zero undefined citations, zero overfull boxes. The author's compile claim is confirmed. |

Nothing outside this file was written. Nothing here proves or claims
HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3.

---

## 1. VERDICT

**REPAIR.** Every mathematical bridge in the candidate reconstructs
correctly; I found no invalid mathematical step. The defect is in the
external-fact layer, where a directly checkable [DI]/[MO] citation
provably does not support the statement it is attached to, plus four wrong
sub-item cross-references into the functional lane and one notation
collision with the low-pressure lane and with D1. All are repaired below
with complete replacement text. No downstream structure is lost.

---

## 2. REVIEWED SCOPE

Reconstructed from first nontrivial implication, independently of the
candidate's prose, checking quantifiers, function spaces, exponents,
constants, decay at infinity, and legitimacy of every appeal to package R:

- `lem:qe-embedding`: the Cauchy--Schwarz bound `‖f̂‖₁ ≤ π‖f‖_{H²}`; the
  integral `∫_{R³}(1+|ξ|²)^{-2}dξ = 4π∫_0^∞ r²(1+r²)^{-2}dr = 4π·(π/4) = π²`
  (substitution `r = tanϑ` gives `∫_0^{π/2}sin²ϑ dϑ = π/4`) — **correct**;
  the uniform-continuity argument for `g(x)=∫e^{2πix·ξ}f̂dξ` — **correct**;
  `‖f‖₃ ≤ ‖f‖₂^{2/3}‖f‖_∞^{1/3} ≤ π^{1/3}‖f‖_{H²}` — **correct**;
  the derivative claim `‖∂^αf‖_∞ ≤ π(2π)^{|α|}‖f‖_{H^{k+2}}` with
  `|ξ|^{|α|} ≤ (1+|ξ|²)^{k/2}` for `|α| ≤ k` — **correct**.
- `lem:qe-average`: Hölder on `J` with `3, 3/2` giving
  `|∫_0^sF|³ ≤ |s|²∫_J|F|³`, then Tonelli — **correct**, valid for both
  signs of `s`.
- `lem:qe-gronwall`: `d/dt(e^{-Mt}Y) ≤ ae^{-Mt}`, `MY ≤ a(e^{Mt}-1)`,
  `y ≤ ae^{Mt}`; the negative-time reduction `ỹ(t)=y(-t)` with
  `|∫_0^{-t}y| = ∫_0^t ỹ` — **correct**.
- `lem:qe-mollify`, `lem:quotient-pressure`: the cutoff split
  `∇(χ_Rp)-∇p = (χ_R-1)∇p + p∇χ_R` and `eq:qe-cutoff-error` with
  `0 ≤ 1-χ_R ≤ 1_{|x|≥R}` and `|∇χ_R| ≤ R^{-1}‖∇χ‖_∞` — **correct**; both
  error terms vanish using only `p, ∇p ∈ L³`. **No spatial decay of `u(t)`
  is used anywhere in the block** (checked line by line); D2's prohibition
  on preserved Schwartz decay is respected.
- `lem:quotient-chainrule`: `C¹([0,T];H²) → C¹([0,T];L³)` via
  `eq:qe-embedding`; the difference quotient with `‖δ‖₃ ≤ K|h|`; the
  three-term continuity estimate; exact cancellation of `⟨A,∇p⟩` —
  **correct**.
- Heat block: `∂_rk_r = Δk_r` from
  `∂_rk_r = k_r(-3/2r+|z|²/4r²)`, `∂_jk_r = -(z_j/2r)k_r`,
  `Δk_r = k_r(|z|²/4r² - 3/2r)` — **correct**; the `L¹` dominant
  `eq:qe-kernel-dominant` — **correct**; the substitution
  `k_r(y)dy = k_1(z)dz`, `y = √r z`, giving `∫_{|y|>δ}k_r = η(δ/√r)` —
  **correct**; `lem:qe-heat-continuity`(a) with
  `|G_rf-f| ≤ ω_f(δ)+2‖f‖_∞η(δ/√r)` and the joint-continuity dominant
  `(4πa)^{-3/2}e^{-(|y|-R)_+²/4b}‖f‖_∞` — **correct**;
  `lem:qe-heat-continuity`(b) with `‖I₁‖₃ ≤ ω_g(δ)|K_δ|^{1/3}`,
  `‖I₂‖₃ ≤ 2η(δ/√r)‖g‖₃` — **correct**.
- `lem:heat-generator` Step 2 (flagged by the author): the coordinatewise
  double integration by parts `∫_R(∂_j²k_r)(x-y)f dy_j = ∫_R k_r(x-y)∂_j²f dy_j`
  with Gaussian-times-bounded boundary terms, then Fubini on the remaining
  two coordinates — **correct**; only `f, ∂_jf ∈ L^∞` and `f ∈ C²` are
  needed. Steps 3--5 — **correct**; note the pleasing fact that
  `eq:qe-generator` needs `Δf ∈ L³` but not `f ∈ L³`.
- `lem:quotient-heatsign`: `0 ≥ (Q(G_su)-Q(u))/s = ⟨A,h_s/s⟩+r(h_s)/s`
  with `‖h_s‖₃ ≤ s‖Δu‖₃` — **correct**; `D_Q ≥ 0`.
- `lem:qe-jacobi`: Leibniz expansion, `C_{ki}` as the `(k,i)` cofactor,
  `adj(M)_{ik}=C_{ki}`, `tr(adj(M)BM)=tr(B)det M` — **correct**.
- `lem:flow` (flagged by the author): weighted-norm contraction
  `Λ∫_0^se^{2Λσ}dσ ≤ ½e^{2Λs}`; `|Φ_s(y)-Φ_s(y')| ≤ e^{Λ|s|}|y-y'|`;
  the variational equation with `|M_s| ≤ e^{Λ|s|}`; the `o(|h|)`
  differentiability estimate `|z(s)| ≤ |s|e^{2Λ|s|}ω(e^{Λ|s|}|h|)|h|` —
  **correct**; joint continuity of `M_s(y)` — **correct**; Liouville
  `det DΦ_s ≡ 1` — **correct**; expansions
  `|M_s-I| ≤ Λ|s|e^{Λ|s|}`,
  `|M_s-I-sDb| ≤ |s|e^{Λ|s|}(ω(|s|‖b‖_∞)+Λ²|s|)`,
  and, for `|s| ≤ 1/(4Λ)` (so `|N| ≤ ¼e^{1/4} ≈ 0.321 < ½`),
  `|(I+N)^{-1}-I| ≤ 2|N|`, `|(I+N)^{-1}-I+N| ≤ 2|N|²`, hence
  `eq:qe-flow-inverse` — **all constants recomputed and correct**.
- `lem:qe-pullback`: unit-Jacobian change of variables; the null-set
  argument making `f ↦ f∘Φ` well defined on equivalence classes;
  `‖T_Φf‖₃ ≤ Λ_Φ‖f‖₃` using `|M^{T}| = |M|`; `T_Φ∇φ = ∇(φ∘Φ)` with the
  index check `(DΦ^{T}v)_i = ∂_iΦ_j v_j` — **correct**.
- `lem:quotient-transport` (all five steps; Step 4 flagged by the author):
  the key change of variables at `x = Φ_s(y)`,
  `u_s(x)+q_s(x) = u(y)+DΦ_s(y)^{-T}q(y) = w(y)+E_s(y)q(y)` — **correct**;
  `eq:qe-envelope` with equality at `s=0` — **correct**;
  `‖h_s‖₃ = O(|s|)`, `eq:cp-F-taylor` giving `O(s²)`, and
  `‖E_s+sDu^{T}‖_∞ = o(|s|)` — **correct**;
  `d/dσ u(Φ_{-σ}(x)) = -g(Φ_{-σ}(x))`, `g = Du\,u` — **correct**;
  `L³` continuity along the flow by `C_c` approximation with the support
  set `K = supp g_ε + B̄_{s_0‖u‖_∞}` — **correct**; the two-sided
  division by `s > 0` and `s < 0` forcing equality of the linear
  coefficients — **correct**; the index contraction
  `⟨A,Du^{T}q⟩ = ∫A_i(∂_iu_j)q_j = ∫q·((A·∇)u)` — **correct** and
  agrees with `cp01-manuscript-obligations` Q-16.
- `prop:quotient-evolution`: signs match the manuscript's
  `eq:quotient-evolution` exactly; the three-term continuity estimate with
  exponents `∞, 3, 3/2` — **correct**.
- `lem:quotient-lowstrain`: `sup_x|Dv|_F ≤ (Σ_j‖∇S_Lu_j‖_∞²)^{1/2} ≤
  C_B2^{5L/2}‖u(t)‖₂ ≤ C_B2^{5L/2}‖u_0‖₂`; Hölder `∞,3,3/2`;
  `‖q‖₃ ≤ (1+C_ℙ)‖w‖₃`; `‖A‖_{3/2} = ‖w‖₃²`; `‖w‖₃³ = 3Q(u)`; hence
  `M_L = 3(1+C_ℙ)C_B2^{5L/2}‖u_0‖₂` — **correct**, and identical to the
  coefficient independently derived in `cp02-lowpressure.md` §5 and in
  Q-17. Dimensional check: `[2^{5L/2}‖u_0‖₂] = L^{-5/2}·L^{5/2}T^{-1} = T^{-1}` ✔.
- `prop:quotient-conditional`: the integrated inequality, absorption of
  `(1-θ)ν∫D_Q ≥ 0` (legitimate because `θ ≤ 1` **and** `D_Q ≥ 0` is proved,
  not assumed), Gronwall, and
  `sup‖u‖₃³ ≤ C_ℙ³(‖u_0‖₃³+3A_input)e^{M_LH}`, i.e.
  `M = C_ℙ(‖u_0‖₃³+3A_input)^{1/3}e^{M_LH/3}` — **correct**; matches
  `eq:qe-M`. The quantifier structure matches `hyp:critical` verbatim
  (same `M` for the whole interval, `M` a function of `(ν,u_0,H)` only).
- `rem:highstrain-scope`: forward direction
  `hyp:highstrain ⇒ hyp:critical ⇒ (thm:continuation) T_*=∞`; converse
  with `L=0`, `θ=0`, `A_input = ∫_0^H|K_0|` finite by continuity on the
  compact classical interval — **correct** and structurally parallel to
  the manuscript's existing paragraph for `hyp:highpressure`.

**Independent consistency test (attempted refutation).** I looked for a
configuration in which `eq:quotient-evolution` contradicts the manuscript's
proved `prop:pressure`. Take the degenerate case `q(u)=0`, i.e.
`div(|u|u)=0`. Then `w=u`, `A=|u|u`, the right side of
`eq:quotient-evolution` is `0`, and
`D_Q = -∫|u|u·Δu = D₃` (the identity `-∫Δu·|u|u = D₃` is exactly the one
proved inside `prop:pressure`). Independently, `P₃ = -∫∇p·|u|u = -⟨A,∇p⟩ = 0`
by stationarity, and the transport work
`∫|u|u·(u·∇)u = ⅓∫u·∇|u|³ = 0` by incompressibility. So
`prop:pressure` degenerates to `⅓X' + νD₃ = 0`, which is
`eq:quotient-evolution` with `Q = ⅓‖u‖₃³`. The two identities agree,
including all signs and the factor `3`. **No refutation.** I also
verified the sign of the transport coefficient against
`cp01-manuscript-obligations` Q-16 (`-∫A_i(∂_iu_j)q_j`) — agrees.

**Second attempted refutation.** I tested whether `lem:heat-generator`
could fail for a field that is bounded with bounded derivatives but not in
`L³` (e.g. `f` a bounded nonconstant harmonic-like profile): the lemma's
conclusion `‖G_sf-f‖₃ ≤ s‖Δf‖₃` is then still *true and nonvacuous*
because `G_sf-f = ∫_0^sG_rΔf dr` places the difference in `L³` even when
`f ∉ L³`. No hypothesis is missing.

---

## 3. FIRST BAD BRIDGE

**`lem:qe-embedding`, the sentence
"`it equals f by Fourier inversion on L² \cite[Thm.~2.2.14]{Grafakos2014}`".
The cited theorem does not support the cited statement.**

Grafakos, *Classical Fourier Analysis*, 3rd ed., GTM 249, **Theorem 2.2.14
is stated for `f, g, h ∈ 𝒮(Rⁿ)` only** (book p. 112). Its five items are:
(1) the multiplication formula, (2) Fourier inversion `(f̂)^∨ = f = (f^∨)^`,
(3) Parseval, (4) the Plancherel identity `‖f‖₂ = ‖f̂‖₂ = ‖f^∨‖₂`, (5) the
`h^∨` form of (1) — every one of them for Schwartz functions. The statement
the candidate needs is about `L²` and about `L¹∩L²`:

> for `f ∈ L²`, `F^{-1}∘F(f) = f` a.e., and for `f ∈ L¹∩L²` the `L²`
> transform coincides a.e. with the absolutely convergent integral.

That statement lives in Grafakos **§2.2.4, book pp. 113–114**, in the
unnumbered development ("for `f` in `L¹(Rⁿ)∩L²(Rⁿ)` the expressions `f̂`
and `F(f)` coincide pointwise a.e."; "`F′` coincides with the inverse
operator `F^{-1}` … and Fourier inversion `f = F^{-1}∘F(f) = F∘F^{-1}(f)`
a.e. holds on `L²`"), together with Exercise 2.2.6 for the pointwise
`L¹`-inversion. Theorem 2.2.14 is one page earlier and is Schwartz-only.

This is a genuine D5 failure, not a typo: the candidate places a specific,
checkable theorem number in the manuscript text while its own §3 admits
the number was "not reopened in this session" ([MO]). The sibling
low-pressure lane already draws the distinction correctly
(`cp02-lowpressure.md` §3: **E3** = "Grafakos, Thm. 2.2.14 (2),(4), p. 112"
attached to the statement *on 𝒮*; **E5** = "Grafakos, §2.2.4, pp. 113–114"
attached to the `L²` theory) — so the candidate is inconsistent with a
lane it must integrate against.

**Mathematical status: the fact used is true**, so nothing downstream
fails. The bridge is defective as a *sourced* bridge only.

### Second-order defects (cross-references, all repairable)

Checked against `cp02-quotient-functional.md` (the actual owner):

| Candidate cites | Content it wants | Where it actually lives |
| --- | --- | --- |
| `lem:quotient-minimizer`(b), line 205 of the block | stationarity `⟨A,g⟩=0` on `G₃` | `lem:quotient-minimizer`**(c)** |
| `lem:quotient-minimizer`(a), line 980 | `‖A‖_{3/2}=‖w‖₃²`, `‖w‖₃³=3Q` | `lem:quotient-minimizer`**(b)** |
| `lem:quotient-minimizer`(d), lines 259 and 906 | continuity of `u↦w` (`L³→L³`) and `u↦A` (`L³→L^{3/2}`) | **`lem:quotient-stability`**, display `eq:cp-continuity`; item (d) of `lem:quotient-minimizer` is the unrelated invariance `Q(u+g)=Q(u)` |

Also: the candidate writes `‖ℙ‖_{L³→L³}` where the functional lane fixes
the symbol `C_ℙ := ‖ℙ‖_{L³→L³}` (`lem:leray`(b), `eq:cp-coercive`), and
the candidate writes the low-pass kernel as `ψ_L`, `ψ̂ = φ`, whereas **D1
and `cp02-lowpressure.md` `eq:lp-symbol` both reserve `ψ` for the
homogeneous symbol `ψ(ξ)=φ(ξ)-φ(2ξ)`** and call the kernel `κ`
(`κ̂ = φ`, `κ_L = 2^{3L}κ(2^L·)`). Left unrepaired, the integrated
manuscript would use `ψ` for two different objects in one section.

---

## 4. EVIDENCE

**Sources fetched and inspected in this session (all [DI] here).**

| Fact as the candidate uses it | Source opened | Result |
| --- | --- | --- |
| Fourier inversion / Plancherel on `L²`, coincidence on `L¹∩L²` (candidate E10) | Grafakos CFA 3rd ed., PDF mirror `math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf`, book pp. 110–115 (PDF pp. 127–132), read as text | **MISMATCH.** Thm. 2.2.14 is `f,g,h ∈ 𝒮(Rⁿ)`. The `L²` statement is §2.2.4, pp. 113–114 (unnumbered), with Exercise 2.2.6 for `L¹`-inversion. |
| Minkowski for convolution `‖k*f‖₃ ≤ ‖k‖₁‖f‖₃` (E9) | same PDF, book pp. 21–22 (PDF pp. 39–40) | **CONFIRMED.** "Theorem 1.2.10. (Minkowski's inequality) Let `1 ≤ p ≤ ∞`. For `f ∈ L^p(G)` and `g ∈ L¹(G)` … `‖g*f‖_{L^p} ≤ ‖g‖_{L¹}‖f‖_{L^p}`." `R³` with Lebesgue measure is the abelian instance. |
| Hölder (E1) | Mathlib `0df444a`, `Mathlib/MeasureTheory/Integral/Bochner/Basic.lean:1191` | **CONFIRMED**: `integral_mul_le_Lp_mul_Lq_of_nonneg`, conjugate exponents. |
| Tonelli (E2) | `Mathlib/MeasureTheory/Measure/Prod.lean:1006` | **CONFIRMED**: `lintegral_prod`, "**Tonelli's Theorem**". |
| Dominated convergence (E3) | `Mathlib/MeasureTheory/Integral/DominatedConvergence.lean:57` | **CONFIRMED**. |
| FTC (E4) | `.../IntervalIntegral/FundThmCalculus.lean:1148` | **CONFIRMED**: `integral_eq_sub_of_hasDerivAt`. |
| Differentiation under the integral (E5) | `Mathlib/Analysis/Calculus/ParametricIntegral.lean:288` | **CONFIRMED**: `hasDerivAt_integral_of_dominated_loc_of_deriv_le`, integrable dominant for the derivative. |
| Banach fixed point + completeness (E6) | `Mathlib/Topology/MetricSpace/Contracting.lean:95`; `Mathlib/Topology/ContinuousMap/Bounded/Basic.lean:296` | **CONFIRMED**: `ContractingWith.exists_fixedPoint`; `BoundedContinuousFunction.instCompleteSpace`. |
| Change of variables, injective `C¹` (E7) | `Mathlib/MeasureTheory/Function/Jacobian.lean:1213` | **CONFIRMED**: `integral_image_eq_integral_abs_det_fderiv_smul`, `∫_{f''s}g = ∫_s |det f'|•g∘f` for `InjOn f s`. |
| Density of `C_c` in `L³` (E8) | `Mathlib/MeasureTheory/Function/ContinuousMapDense.lean:135` | **CONFIRMED**: `MemLp.exists_hasCompactSupport_eLpNorm_sub_le`. |
| Leibniz `det`, adjugate (E11) | `.../Determinant/Basic.lean:63`, `.../Adjugate.lean:264` | **CONFIRMED**: `det_apply`, `mul_adjugate`. |
| Bernstein `‖∇S_Lf‖_∞ ≤ C_B2^{5L/2}‖f‖₂` (E13) | `cp02-lowpressure.md` `lem:bernstein` (read in full) | **CONFIRMED and stronger than assumed**: proved there for `f ∈ L²` *scalar or vector-valued* in the Frobenius form, with `C_B = ‖∇κ‖₂ = 2π‖|ξ|φ‖₂ ≤ 16π√(2π/5)`, with a `C^∞` representative and with `t↦∇S_Lu(t) ∈ C([0,T];L^∞)`. The label is literally `lem:bernstein`. |

**Recomputed exponents and constants** (each independently redone, not
copied): `∫(1+|ξ|²)^{-2} = π²`; `‖∇κ_L‖₂ = 2^{5L/2}‖∇κ‖₂` (so `5L/2`, not
`3L/2` or `7L/2`); Hölder triples `1/∞+1/3+2/3 = 1` and `2/3+1/3 = 1`;
`‖f‖₃ ≤ ‖f‖₂^{2/3}‖f‖_∞^{1/3}`; `¼e^{1/4} < ½`; `Λ|s|e^{Λ|s|}`,
`2|N|`, `2|N|²`; `M_L H/3` in the exponent of `eq:qe-M`; the factor `3`
relating `‖w‖₃³` and `Q`.

**Compile evidence.** Block extracted verbatim, stub preamble written
independently (only `amsmath/amssymb/amsthm/geometry/hyperref`, the six
theorem environments, `\R`, `\norm`, and label stubs for the nineteen
external labels): two `latexmk -pdf` passes, exit 0, `grep -c undefined`
= 0, `grep -c Overfull` = 0. The set of externally-owned labels the block
needs is exactly: `def:quotient`, `def:target`, `eq:cp-F-taylor`,
`eq:missing`, `eq:NS`, `hyp:critical`, `hyp:highpressure`, `lem:bernstein`,
`lem:cubic-frechet`, `lem:quotient-coercive`, `lem:quotient-heat`,
`lem:quotient-minimizer`, `prop:energy`, `prop:localtheory`,
`prop:lowpressure`, `prop:pressure`, `prop:quotient-derivative`,
`thm:conditional`, `thm:continuation`. All but `prop:localtheory` exist in
already-drafted lanes; `prop:localtheory` is D2's own interface. **No
reference to any evidence file is used as proof inside the block** (grepped
for `hf1*`, `evidence`, `.md`, `research/`: zero hits). The block is
self-contained.

---

## 5. REPLACEMENT ARGUMENT (complete)

Five surgical replacements. Nothing else in the block changes.

```latex
%%% REPAIR 1 (FIRST BAD BRIDGE).  In the proof of lem:qe-embedding, replace
%%% the sentence beginning "Since $\hat f\in L^1\cap L^2$" by:

Since $\hat f\in L^1\cap L^2$, the Fourier transform of $f$ in the
$L^2$ sense coincides almost everywhere with the absolutely convergent
integral defining $\hat f$, and the $L^2$ inverse transform
$\mathcal F^{-1}$ extends $h\mapsto h^\vee$, $h^\vee(x)=\int
e^{2\pi ix\cdot\xi}h(\xi)\,d\xi$, from $L^1\cap L^2$ to $L^2$ with
$\mathcal F^{-1}\mathcal Ff=f$ almost everywhere; both facts are part of
Definition~\ref{def:lp}, and their source is
\cite[\S2.2.4, pp.~113--114]{Grafakos2014}.  Applying this with
$h=\hat f\in L^1\cap L^2$ gives $g=(\hat f)^\vee=\mathcal F^{-1}\mathcal Ff=f$
almost everywhere; hence $g$ is a representative of $f$.

%%% Rationale: Grafakos Theorem 2.2.14 is stated for f,g,h in the Schwartz
%%% class only (book p. 112, verified by direct inspection); the L^2 and
%%% L^1\cap L^2 statements are the unnumbered development of \S2.2.4,
%%% pp. 113-114.  Definition~\ref{def:lp} of the low-frequency-pressure
%%% part already records exactly these two facts as project text, so the
%%% cleanest form cites that definition and sources it to \S2.2.4.
%%% In the external-fact table, E10 must read:
%%%   Source: Grafakos, CFA 3rd ed., \S2.2.4, pp. 113-114 (unnumbered
%%%   development; Exercise 2.2.6 for pointwise L^1 inversion) -- [DI];
%%%   Mathlib MeasureTheory.Lp.fourierTransformₗᵢ and fourierInv (Analysis/Fourier/LpSpace.lean:50,132) -- [DI].
%%% The citation "Thm. 2.2.14" must be deleted, or retained ONLY where a
%%% Schwartz-class statement is used.

%%% REPAIR 2.  In the proof of lem:quotient-pressure, last sentence:
%%%   "Lemma~\ref{lem:quotient-minimizer}(b) applied with $g=\nabla p$"
%%% becomes
%%%   "Lemma~\ref{lem:quotient-minimizer}(c) applied with $g=\nabla p$"

%%% REPAIR 3.  In lem:quotient-chainrule Step 3, and again in the
%%% continuity paragraph of prop:quotient-evolution:
%%%   "by Lemma~\ref{lem:quotient-minimizer}(d)"
%%% becomes
%%%   "by Lemma~\ref{lem:quotient-stability}, estimate \eqref{eq:cp-continuity}"
%%% (both occurrences; item (d) of lem:quotient-minimizer is the invariance
%%% $\mathcal Q(u+g)=\mathcal Q(u)$, not a continuity statement).

%%% REPAIR 4.  In lem:quotient-lowstrain:
%%%   "Lemma~\ref{lem:quotient-minimizer}(a) ($\norm A_{3/2}=\norm w_3^2$,
%%%    $\norm w_3^3=3\mathcal Q(u)$)"
%%% becomes
%%%   "Lemma~\ref{lem:quotient-minimizer}(b) ($\norm A_{3/2}=\norm w_3^2$,
%%%    $\norm w_3^3=3\mathcal Q(u)$)"
%%% and every occurrence of $\norm{\mathbb P}_{L^3\to L^3}$ and
%%% $\norm{\mathbb P}$ becomes $C_{\mathbb P}$, the symbol fixed in
%%% Lemma~\ref{lem:leray}(b).  In particular
%%%   M_L := 3\,(1+C_{\mathbb P})\,C_B\,2^{5L/2}\norm{u_0}_2
%%% and
%%%   M(\nu,u_0,H) = C_{\mathbb P}\bigl(\norm{u_0}_3^3+3A_{\rm input}\bigr)^{1/3}
%%%                  \exp\bigl(\tfrac13M_LH\bigr).

%%% REPAIR 5.  Replace the paragraph opening subsection
%%% subsec:qe-highstrain (the one fixing $S_L$) by:

Let $S_L$, $L\in\mathbb Z$, be the low-pass projection of
Definition~\ref{def:lp}, i.e.\ Tao's $P_{\le2^L}$ with symbol
$\varphi(\xi/2^L)$, so that $S_Lf=\kappa_L*f$ with
$\kappa_L=2^{3L}\kappa(2^L\,\cdot)$ and $\hat\kappa=\varphi$; the symbol
$\psi=\varphi-\varphi(2\,\cdot)$ and the homogeneous blocks $\Delta_j$ of
Definition~\ref{def:lp} are not used here, and
Lemma~\ref{lem:lp-coincide} reconciles $S_L$ with $\sum_{j\le L}\Delta_j$
on $L^2$.  Since $\kappa_L\in\mathcal S(\R^3)$, $S_L$ acts componentwise
on vector fields and $\partial_kS_Lf=(\partial_k\kappa_L)*f$
(Lemma~\ref{lem:lowpass-kernel}).  We use the Bernstein estimate of
Lemma~\ref{lem:bernstein}: for $f\in L^2(\R^3;\R^3)$, $S_Lf$ has a
$C^\infty$ representative and
\begin{equation}\label{eq:qe-bernstein}
 \sup_{x\in\R^3}\bigl|\nabla S_Lf(x)\bigr|_F\le C_B\,2^{5L/2}\norm f_2 ,
 \qquad C_B=2\pi\norm{\,|\xi|\varphi\,}_2\le16\pi\sqrt{2\pi/5},
\end{equation}
and $t\mapsto\nabla S_Lu(t)\in C([0,T];L^\infty)$ whenever
$u\in C([0,T];L^2)$.

%%% Consequence: the componentwise sum in the proof of
%%% lem:quotient-lowstrain and its continuity paragraph can be deleted,
%%% since \eqref{eq:qe-bernstein} is already the Frobenius form for vector
%%% fields and Lemma~\ref{lem:bernstein} already supplies the time
%%% continuity.  The constant $M_L$ is unchanged.
```

Bibliography: `Rudin1987` and `Teschl2012` are still needed;
`Grafakos2014` is shared with the functional and low-pressure lanes. After
REPAIR 1 the `\cite[Thm.~2.2.14]{Grafakos2014}` disappears from this
lane's text; the surviving Grafakos citations here are
`\cite[Thm.~1.2.10]{Grafakos2014}` (confirmed [DI] above) and
`\cite[\S2.2.4, pp.~113--114]{Grafakos2014}`.

---

## 6. CONDITIONAL SUFFIX THAT SURVIVES

After the five repairs, and **unconditionally on any hypothesis**, for the
original unforced equation on `R³`, every `ν>0`, every divergence-free
`u_0 ∈ 𝒮(R³)³`, the maximal classical branch of `prop:localtheory`, and
every compact `[0,T] ⊂ [0,T_*)`:

1. `p(t), ∇p(t) ∈ L³` and `∇p(t) ∈ G₃`, so `DQ(u(t))[∇p(t)] = 0` (Q-8, Q-9);
2. `t ↦ Q(u(t))` is `C¹([0,T])` with
   `d/dt Q(u(t)) = ν⟨A,Δu⟩ - ⟨A,(u·∇)u⟩` (Q-10);
3. `D_Q(u(t)) = -⟨A(t),Δu(t)⟩ ≥ 0` and is continuous in `t` (Q-11);
4. `∫A·((u·∇)u) = ∫q·((A·∇)u)` (Q-12 .. Q-16), whence the pressure-free
   and minimizer-derivative-free identity `eq:quotient-evolution`
   `d/dt Q(u) + νD_Q(u) = -∫q·((A·∇)u)` with continuous right side;
5. `|K_low(t)| ≤ M_L Q(u(t))` with
   `M_L = 3(1+C_ℙ)C_B2^{5L/2}‖u_0‖₂` (Q-17).

Conditionally, and only conditionally:

6. `hyp:highstrain` (`eq:quotient-gap`) `⇒ hyp:critical` with
   `M(ν,u_0,H) = C_ℙ(‖u_0‖₃³+3A_input)^{1/3}e^{M_LH/3}`, hence, by
   `thm:conditional`, `⇒ def:target` (Q-18).

The suffix survives the repair intact: nothing in items 1–6 depended on
the mis-sourced fact except the *justification* of `H² ↪ C_{b,u}`, which
REPAIR 1 re-sources without changing its statement.

---

## 7. UNNECESSARY DEPENDENCIES

Items the integrator can delete with no loss:

1. **`lem:qe-embedding` in its entirety** is avoidable if the local-theory
   lane states (R3) (as D2 asserts it does) and states `H^{k+2} ↪ C_{b,u}`
   for derivatives up to order `k`. The candidate's own §4 item 2 says
   this. Since D2 *does* assert (R3) for `2 ≤ q ≤ ∞`, and boundedness plus
   uniform continuity of `u, Du, D²u, Δu` is the only extra content used
   (in `lem:flow` and `lem:heat-generator`), the cleanest integration keeps
   `lem:qe-embedding` **only** for the uniform-continuity clause and drops
   its `L³` and `L^∞` interpolation halves. Then E10 (Fourier inversion)
   disappears from this lane altogether and the FIRST BAD BRIDGE becomes
   moot rather than repaired.
2. **`\cite[Thm.~2.2, Cor.~2.6, Thm.~2.10, Lemma~3.11]{Teschl2012}`** and
   the whole remark after `lem:flow` are explicitly corroboration only
   ("cited for orientation and not used"). Dropping the remark removes the
   `Teschl2012` bibliography entry.
3. **`\cite[Thm.~7.26]{Rudin1987}`** duplicates the Mathlib change-of-
   variables reference (E7, confirmed [DI]); one of the two suffices.
   Similarly `\cite[Thm.~3.14]{Rudin1987}` duplicates E8. Dropping both
   removes the `Rudin1987` entry.
4. **The componentwise Bernstein reassembly** in `lem:quotient-lowstrain`
   (see REPAIR 5): `lem:bernstein` already gives the vector-valued
   Frobenius form and the time continuity.
5. **The candidate's §4 open items 1 and 2 are stale.** Item 1 (Bernstein
   label is a "placeholder") is closed: `cp02-lowpressure.md` uses exactly
   the label `lem:bernstein` with exactly that inequality, for vector
   fields, with continuity, and with an explicit `C_B`. Item 2 is closed by
   `def:lp` of the same lane. Item 3 ((R3) as stated) is D2 verbatim and is
   not an open item at all. The lane therefore has **no** genuine open
   integration seam beyond the notation collisions repaired above.
6. `lem:qe-jacobi`'s adjugate identity is used only through
   `tr(adj(M)M') = (tr B)det M`; no linear-algebra citation is needed
   (the candidate already proves it).

Dependencies that are **necessary** and correctly used: `prop:energy`
(for `‖u(t)‖₂ ≤ ‖u_0‖₂`), `lem:quotient-coercive` (both directions),
`lem:quotient-minimizer`, `lem:quotient-stability`, `lem:cubic-frechet`,
`lem:quotient-heat`, `prop:quotient-derivative`, `lem:bernstein`,
`prop:localtheory`, `hyp:critical`, `thm:conditional`, `thm:continuation`.

---

## 8. NON-CLAIMS (checked as retained, and asserted here too)

Verified retained **verbatim** from the manuscript by string comparison:
"Its sign follows by differentiating the heat contraction at zero;
$\Delta u \in L^3$ justifies this generator limit."; "No quantitative
comparison with the original cubic dissipation is claimed."; "Integration
of \eqref{eq:quotient-evolution} and Gronwall would then bound
$\mathcal Q$, hence $L^3$, through the putative endpoint"; "Neither
\eqref{eq:quotient-gap} nor a quantitative dissipation mechanism for it
has been proved."; "This is an alternative to the pressure route; no
novelty or Millennium solution is asserted."

This review asserts, and the audited text asserts, none of the following:
no proof of `eq:quotient-gap` / `hyp:highstrain`; no sign, bound, or
dissipation mechanism for `K_L`; no quantitative comparison of `D_Q` with
`D₃` and no coercive lower bound for `D_Q` in any norm of `u`; no
smoothness or regularity of the minimizer `q` or of `w`; no HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3 result; no continuation bound;
no regularity theorem; no novelty claim for the quotient construction; no
solution of the Navier--Stokes Millennium problem. `prop:quotient-
conditional` is a conditional implication only, and `rem:highstrain-scope`
correctly records that at its quantifiers `hyp:highstrain` is *equivalent*
to global continuation, so it supplies no method.

Source-status caveats carried forward: Rudin RCA Thms. 3.14 and 7.26 were
not reopened and remain [MO]; the Mathlib statements were read in the
`0df444a` checkout but not type-checked (grep/statement-read level);
`prop:localtheory` (package R) is an assumed lane interface, not proved
here.

---

## 9. MINOR EDITORIAL ISSUES FOR THE INTEGRATOR

1. **`H²` norm convention never stated.** `lem:qe-embedding` silently uses
   `‖f‖_{H²} := ‖(1+|ξ|²)f̂‖₂`. The constant `π` is norm-dependent. Add
   one sentence fixing the convention (and note it is equivalent to, but
   not equal to, `(∑_{|α|≤2}‖∂^αf‖₂²)^{1/2}` under the `e^{-2πix·ξ}`
   convention).
2. **Monotonicity of the Fréchet remainder modulus.** In
   `lem:quotient-transport` Step 4 the bound
   `|r(δ_s)| ≤ ε(‖δ_s‖₃)‖δ_s‖₃ ≤ ε(|s|‖g‖₃)|s|‖g‖₃` substitutes an upper
   bound *inside* `ε`, which needs `ε` nondecreasing. Either say "`ε` may
   be taken nondecreasing" or, better, invoke
   `eq:cp-derivative-remainder` directly:
   `|r(h)| ≤ 6(‖w‖₃+‖h‖₃)^{3/2}‖h‖₃^{3/2}`, which is manifestly monotone.
   The same substitution is harmless in `lem:quotient-chainrule` Step 2 and
   `lem:quotient-heatsign`, where only `‖δ‖₃ → 0` is used.
3. **`lem:flow`(b),(d) Gronwall with an `s`-dependent constant.** The
   displays `|Z(s)| ≤ |s|e^{2Λ|s|}ω(e^{Λ|s|}|y-y'|)` and
   `|z(s)| ≤ |s|e^{2Λ|s|}ω(e^{Λ|s|}|h|)|h|` are obtained by running
   `lem:qe-gronwall` on `[0,s]` for each fixed `s` (the "`a`" is then
   constant). Add the clause "applying Lemma~\ref{lem:qe-gronwall} on the
   interval with endpoints `0` and `s`" so the reader does not read `a` as
   varying.
4. **Citation slip.** `lem:quotient-transport` Step 1 says "By (R2), (R3)
   and Lemma~\ref{lem:qe-embedding}, `b := u(t)` is `C^∞` with `u, Du, D²u`
   bounded". Boundedness of `D²u` comes from **(R1)** (`u(t) ∈ H⁴`) via
   `lem:qe-embedding`. Change to "(R1)--(R3)".
5. **`D_Q` introduced inside a lemma statement.** `lem:quotient-heatsign`
   both defines `D_Q(u(t))` and proves its sign. Split into a
   `definition` (matching the manuscript's `D_{\mathcal Q}(u)=-\int A\cdot\Delta u`)
   plus the sign lemma, so that `hyp:highstrain` and `eq:quotient-gap` can
   cite a definition rather than a lemma.
6. **`hyp:highstrain` is not self-contained.** It uses `K_L` without
   restating `K_L(t) = -\int q\cdot((A\cdot\nabla)(u-S_Lu))`. Repeat the
   definition inside the hypothesis (the manuscript's `hyp:highpressure`
   likewise repeats `Q_J`'s role); a hypothesis a reader may want to
   attack should be readable alone.
7. **Dangling labels.** `\label{lem:heat-generator}` is defined but never
   referenced anywhere in the block (`lem:quotient-heatsign` cites
   `\eqref{eq:qe-generator}` instead), and `\label{eq:qe-cutoff-error}` is
   referenced only from the evidence file's §1 table, not from the LaTeX.
   Either reference them or drop the labels.
8. **Unnamed remarks.** Two `remark` environments (after
   `lem:quotient-heatsign` and after `lem:quotient-transport`) carry no
   label and no title; give them labels if the controller's structural
   verifier counts remarks.
9. **`\operatorname{div}`, `\operatorname{tr}`, `\operatorname{adj}`
   inline.** Consistent with `main.tex`'s `\operatorname{div}`, fine; but
   consider `\newcommand{\adj}{\operatorname{adj}}` since `adj` occurs
   eight times in one proof.
10. **`|M|` vs `|M|_F`.** The notation paragraph defines both, and the
    proofs switch between them (operator norm in `lem:flow`, Frobenius in
    `lem:quotient-lowstrain`). After REPAIR 5 the Frobenius norm appears
    only in `eq:qe-bernstein`; keep `|·|_F` there and `|·|` everywhere else,
    and state `|M| ≤ |M|_F` once (it is used but never displayed).
11. **`θ` range.** `hyp:highstrain` says `θ ∈ [0,1]`; the manuscript's
    existing `eq:quotient-gap` display says `θ ≤ 1`. Harmonise (the
    hypothesis's form is the better one; the manuscript display should then
    drop its own `θ ≤ 1` annotation to avoid stating the constraint twice).
12. **Subsection depth.** The block opens five `\subsection`s inside
    `sec:quotient`; the functional lane opens three more. Eight
    subsections in one section is a lot for an eight-page section — the
    controller may want `subsec:qe-trajectories` merged into the
    functional lane's last subsection.
13. **`prop:quotient-evolution`'s hypothesis restates D2.** "Let
    `[0,T] ⊂ [0,T_*)` be compact and let `(u,p)` be the maximal classical
    solution of `prop:localtheory` restricted to `[0,T]`" repeats the
    standing convention of `subsec:qe-trajectories`. Harmless, but the
    proposition should say "with the notation and package (R) of
    Section~\ref{subsec:qe-trajectories}".

---

## 10. REOPENING CONDITION

This audit must be reopened if any of the following changes:

1. **`prop:localtheory` weakens.** If the local-theory lane delivers only
   `∂_t^ju, ∂_t^jp ∈ L^∞_tH^k` (which is all Tao Theorem 5.4(iv) gives —
   see `cp01-manuscript-obligations` §0.1, item (b) of "what 5.4 does not
   state") instead of D2's `C^j([0,T];H^k)`, then `lem:quotient-chainrule`
   Step 1 (`u ∈ C¹([0,T];L³)`) and Step 3 (continuity of the derivative),
   `lem:quotient-heatsign`'s continuity claim, and the continuity of the
   right side of `eq:quotient-evolution` all lose their input, and with
   them the `C¹` regularity of `Q∘u` used by `prop:quotient-conditional`.
   The Gronwall step would then need absolute continuity proved from the
   `L^∞_t` package directly.
2. **`lem:quotient-stability` or `prop:quotient-derivative` changes shape.**
   If the functional lane's remainder estimate is weakened below
   `o(‖h‖₃)` (e.g. to a one-sided or Gâteaux statement), Step 2 of
   `lem:quotient-chainrule`, Step 4 of `lem:quotient-transport`, and
   `lem:quotient-heatsign` all break; the two-sided envelope comparison in
   particular needs a genuine Fréchet expansion on both sides.
3. **`lem:quotient-minimizer` sub-item lettering changes.** REPAIRS 2--4
   are keyed to the current (a)--(d) of `cp02-quotient-functional.md`.
4. **`lem:bernstein` moves or changes its constant.** REPAIR 5 and `M_L`
   are keyed to `cp02-lowpressure.md`'s `lem:bernstein` with
   `C_B = 2π‖|ξ|φ‖₂`. A different `φ` normalisation changes `C_B` and
   hence `M_L` and `eq:qe-M`.
5. **`def:lp` is not integrated.** REPAIR 1 cites `def:lp` for the `L²`
   Fourier facts. If the low-pressure lane's `def:lp` is dropped or
   renamed, REPAIR 1 must instead cite
   `\cite[\S2.2.4, pp.~113--114]{Grafakos2014}` directly, and that page
   range must be recorded as [DI] in the manuscript's source table.
6. **`hyp:critical` or `thm:conditional` is restated.** `eq:qe-M` is
   matched to `eq:missing`'s exact quantifier order
   (`sup_{0<t<min\{H,T_*\}}`, one `M` per `(ν,u_0,H)`).
7. **A claim about `K_L` appears anywhere.** Any asserted sign, bound, or
   dissipation mechanism for `K_L` — including one derived from a
   commutator, paraproduct, or frequency-localised energy estimate —
   changes the status of `hyp:highstrain` from hypothesis to theorem and
   requires a full re-audit of §§5--8 above, since the whole conditional
   architecture is then no longer the deliverable.
8. **`D_Q` is compared with `D₃`.** The current text's non-claim is
   load-bearing: `prop:quotient-conditional` works only because
   `(1-θ)ν∫D_Q` can be *discarded*. Any coercive lower bound for `D_Q`
   would let `θ < 1` do real work and would need re-derivation of `eq:qe-M`.

---

## 11. NEXT DISTINCT ACTION

Controller integration, in this order: (i) apply REPAIRS 1--5; (ii) drop
the stale open items 1--3 of the candidate's §4 and the `Teschl2012` /
`Rudin1987` bibliography entries per §7.2--7.3; (iii) splice the functional
lane's first half, this lane's second half, and the low-pressure lane's
`def:lp` / `lem:bernstein` into `sec:quotient` and `prop:lowpressure`,
adding `\newtheorem{lemma}[theorem]{Lemma}` and
`\newtheorem{definition}[theorem]{Definition}`; (iv) re-run the structural
verifier on the D4 label list; (v) a round-2 audit of the *integrated*
section, whose distinct new risk is label and notation collision across the
three lanes (`ψ`/`κ`, `C_ℙ`/`‖ℙ‖`, `S_J`/`S_L`, `q` as minimizer versus
`q` as the `ν`-normalised pressure in `eq:nu-normalization`) — the last of
these is a collision the present lane does not create but the integrated
manuscript will have.
