# HF25 Scope B audit: the divergence-defect criterion and its producer

Independent proof audit, different lens from the HF25 Scope A review. Scope B
only: the sections "The attachment's unweighted div--curl theorem"
(`sec:divcurl`), "Weighted dissipation and the mixed-pressure identity"
(`sec:weighted`), "A quantitative divergence-defect criterion"
(`sec:criterion`), "Energy budgets, normalization, and the surviving
obstruction" (`sec:budgets`), and the conditional completion section
(`sec:continuation`).

## Freeze block

| Item | Value |
|---|---|
| Audit target | `research/evidence/hf25-beyond-hf21-continuation.tex` |
| Target SHA-256 | `3ce562bb59346fc700c522bf5e857e3500b318e283febed0c9db9b7f652c6d4f` |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `a3e85f2d75fb01f1421e95f51ec6f8eedab0ec50` |
| Manuscript | `/home/ert/proj/navier-paper/main.tex` at `34cdffd2fe2bd8a35068e96f907302e00c10850f` |
| Cross-check artifact | `research/evidence/hf23-divcurl-continuation.tex`, SHA-256 `abe74421ef6a8a7bacc108c0c08834e32f2a6116530fceb00368c8e67b129075` |
| Source drop | `~/Nextcloud/navier/navier-hf21-proof-continuation-2026-09-06.tex` (same hash as target) |
| Audit date | 2026-09-06 |

Nothing outside this file was edited. No commit, no push. The candidate,
`PLAN.md`, `docs/`, and the manuscript are untouched.

---

## VERDICT

**PASS WITH SCOPE** for the whole of Scope B. No invalid or unsupported bridge
was found in `sec:divcurl`, `sec:weighted`, `sec:criterion`, `sec:budgets` or
`sec:continuation`. Every constant, exponent, interpolation exponent, Young
maximisation, Gronwall step and scaling relation was recomputed independently
and agrees with the candidate. The three load-bearing pointwise inequalities
were additionally checked numerically (below); all attempted refutations
failed.

Six scope items must accompany any integration; two of them narrow claims the
controller has already recorded in `PLAN.md`. One sub-claim of the framing item
(6) is **refuted**: the assertion that the plan's earlier phrase was "too
strong" contradicts the audited HF22-D repair block R-A, which read that phrase
correctly and endorsed it.

The audit does **not** certify `thm:counter`, `thm:alpha` or `thm:Genergy`
(Scope A). `sec:budgets` cites `thm:counter` once; that citation is quarantined
below.

## REVIEWED SCOPE

Reconstructed from the first nontrivial implication and verified:

- `lem:minimum`, `lem:cubic`, `lem:derivative`, `eq:heatsign`, `eq:evolution`,
  `eq:scaling` (foundations consumed by Scope B).
- `thm:divcurl` and its four-step proof: the regularised problem in
  `X = L^2 ∩ L^3`, `eq:deltamono`/`eq:deltalip`, the difference-quotient bound
  `eq:deltadq`, the constrained trace inequality `eq:matrix`, the two Fourier
  div--curl identities `eq:globaldivcurl`, the `δ`-uniform constants, and the
  limit passage and `H^1` extension.
- `cor:sigma`, `thm:weighted` (including `eq:Vcompare`, `eq:weightedgrad`,
  the chain formula for `V`, and `eq:Dcoercive`).
- `thm:mixed` and `cor:Kbounds` (both bounds).
- `thm:sigmacriterion` (interpolation, Young, constant, Gronwall,
  measurability, integrability), `cor:Gproducer`, `prop:generalcriterion`
  (including `eq:defectscaling`), and the "precise missing positive step"
  remark.
- `eq:energy`--`eq:energy-Qq`, `eq:lowstrain`, `eq:signed`,
  `eq:distance-balance`, the bad-set measure bound, and the scalar comparison
  family `eq:scalarfamily`--`eq:scalarbounds`.
- `thm:completion`, the `L^5` endpoint remark, and "What has not been supplied".

Not reviewed: `sec:heatcounter`, `sec:sharp`, `sec:actual`, `sec:literature`.

## FIRST BAD BRIDGE

**None in Scope B.** The nearest defect is not a mathematical bridge but a
records claim, item (6d) below: the candidate's — and, following it, the plan's
— statement that this plan's phrase "the whole of the frozen gap" was *too
strong*. Under the audited reading fixed by the HF22-D repair block R-A that
phrase is correct, so the plan edit is a clarification, not a correction.

---

## EVIDENCE, in the order the controller asked

### (1) Div--curl theorem and weighted dissipation against audited HF23 Scope A, given the hash discrepancy

**The hash discrepancy is a file-format difference and nothing else. Resolved.**

- HF25 cites the attachment as a *23-page PDF* named
  `navier-divcurl-proof-continuation-2026-09-06.pdf`. Our repository holds the
  *LaTeX source* `navier-divcurl-proof-continuation-2026-09-06.tex`
  (`~/Nextcloud/navier/`, byte-identical to
  `research/evidence/hf23-divcurl-continuation.tex`). Two different files of the
  same document necessarily have different hashes. The PDF was never delivered
  here, so its hash cannot be reproduced.
- **Decisive corroboration computed in this audit:** our HF23 `.tex` compiles
  with `pdflatex` to *exactly 23 pages* ("Output written on t.pdf (23 pages,
  446827 bytes)").
- HF23 numbers theorems by section (`\newtheorem{theorem}{Theorem}[section]`).
  Its Section 3 is `sec:regularity` with `thm:main` = **Theorem 3.1**; Section 4
  is `sec:mixed` with `cor:sigma` = 4.1 and `thm:mixed` = **Theorem 4.2**;
  Section 7 is `sec:spacetime` with `thm:spacetime` = **Theorem 7.1**. HF25
  attributes to "Theorems 3.1, 4.2 and 7.1" precisely "a candidate unweighted
  div--curl estimate, a mixed-pressure identity, and a fixed-energy spacetime
  obstruction". **The map is exact.**

**Every Scope-B attribution matches what audited HF23 proves.** Statement-level
comparison, all verified verbatim:

| Object | HF25 | HF23 | Manuscript (audited) |
|---|---|---|---|
| `‖∇w‖₂² ≤ (5/4)Y` | `eq:divcurlbound` | `eq:mainw` | `eq:qdc-w` |
| `‖∇q‖₂² = ‖div w‖₂² ≤ (1/4)Y` | `eq:divcurlbound` | `eq:mainq` | `eq:qdc-q` |
| `σ = -div w` a.e. incl. across `{w=0}`, `‖σ‖₂ ≤ √Y/2` | `cor:sigma` | `cor:sigma`, `eq:sigma-bound` | `cor:quotient-defect` |
| `K_b = ∫q·∇Π_b = ∫σΠ_b`, `‖Π_b‖₂ ≤ ‖b‖₆‖w‖₆²` | `thm:mixed` | `thm:mixed` | `lem:quotient-mixed-pressure` |
| `|K| ≤ (5/8)S³Y²` | `eq:Kbounds` | `eq:KY` | `eq:qdc-KY` |
| budgets `5E₀/(8ν)`, `E₀/(8ν)` | `eq:energy-defect` | `cor:budgets` | `cor:quotient-budgets` |

**No mis-attribution found.** In particular the one place where a
mis-attribution would have been easy, HF25 gets right: HF23 line 262 states
explicitly that "Neither the stronger weighted identity `D_Q=D_3(w)` from HF18
nor a time derivative of `w` is required", and HF25 correspondingly does **not**
attribute `thm:weighted` to the attachment — it attributes it to HF18 and proves
it.

**Is the direct proof of the weighted heat dissipation genuine, or does it lean
on the attachment?** *Genuine, and it now leans on nothing unaudited.* Verified
line by line:

- `eq:weighted-dq`, `M_h := ∫δ_hA·δ_hw = ∫δ_hA·δ_hu`. I re-derived the
  annihilation independently rather than accepting "`δ_h q ∈ 𝒢`": expanding
  `∫δ_hA·δ_hq = h⁻²[∫τ_hA·τ_hq − ∫τ_hA·q − ∫A·τ_hq + ∫A·q]`, all four terms
  vanish by stationarity, because `𝒢₃` is translation invariant and `τ_{±h}q ∈
  𝒢₃`. Pairings absolutely convergent (`A ∈ L^{3/2}`, `q ∈ L³`).
- `M_h ≥ W_h/2` from `eq:monotone`; `|δ_hA| ≤ (|τ_hw|+|w|)|δ_hw|`; weighted
  Cauchy--Schwarz gives `W_h ≤ 4∫(|τ_hw|+|w|)|δ_hu|² ≤ 8‖w‖₃‖∂_ku‖₃²`. Fatou
  along an a.e. subsequence gives `∫ρ|∂_kw|² ≤ 4‖w‖₃‖∂_ku‖₃²` — this is
  `eq:weightedgrad`, recomputed and confirmed.
- `∂_kV = ρ^{1/2}(∂_kw + ½ŵ∂_kρ)` and `|∂_kV|² = ρ|∂_kw|² + (5/4)ρ|∂_kρ|²`:
  confirmed (`ŵ·∂_kw = ∂_kρ`). `|∇|V||² = (9/4)ρ|∇ρ|²`, so
  `|∇V|² − (1/9)|∇|V||² = ρ(|∇w|²+|∇ρ|²)`: **exact**, both displayed forms
  agree.
- `∂_kA·∂_kw = ρ(|∂_kw|²+|∂_kρ|²)` confirmed; summing and integrating by parts
  against `u` gives `−⟨A,Δu⟩ = D_Q`. Legitimate: `∇A ∈ L^{3/2}`, `∇u ∈ L³`,
  `Δu ∈ L³`, `A ∈ L^{3/2}` for `u ∈ H^m`, `m ≥ 4`.
- `eq:Vcompare`, `(8/9)|V(a)−V(b)|² ≤ (j(a)−j(b))·(a−b) ≤ 2|V(a)−V(b)|²`:
  both sides are affine in `cos∠(a,b)`, so the endpoint check suffices; I
  redid both endpoints. At `c=1` the lower bound is exactly Cauchy--Schwarz on
  `r^{3/2}−s^{3/2} = (3/2)∫_s^r t^{1/2}dt`, giving factor `8/9`; the upper uses
  `r^{3/2}−s^{3/2} ≥ √r(r−s)`. At `c=−1`,
  `(r+s)(r²+s²) − (r^{3/2}+s^{3/2})² = rs(√r−√s)² ≥ 0` and
  `(r+s)(r²+s²) ≤ 2(r³+s³) ≤ 2(r^{3/2}+s^{3/2})²`. Numerically (4·10⁵ random
  pairs) the ratio stayed in `[0.8895, 1.052] ⊂ [8/9, 2]`, with the lower
  constant nearly attained — **`8/9` is sharp, as the identity requires.**
- `D_Q ≥ (8/9)‖∇V‖₂²` and `‖w‖₉³ = ‖V‖₆² ≤ S²‖∇V‖₂² ≤ a₀D_Q`,
  `a₀ = 9S²/8`: confirmed.

**One dependency, and it is now audited.** `thm:weighted` uses the weak
derivatives supplied by `thm:divcurl`. That is not a lean on an unaudited
attachment: `thm:divcurl` is reproved in full in `sec:divcurl` *and* is the
manuscript's audited `prop:quotient-divcurl` with identical constants.

**The `sec:divcurl` reconstruction is itself correct**, and I checked it
independently rather than deferring to the manuscript's audit:
`Dj_δ(z) = r_δI + z⊗z/r_δ` has spectrum in `[r_δ, 2r_δ]`; the segment estimate
giving `∫₀¹r_δ ≥ max(δ,(|a|+|b|)/16)` and hence `eq:deltamono` with `1/32`;
`eq:deltadq`, whose `δ`-weighted left side gives `w_δ ∈ H^1` at fixed `δ` before
any division of the Euler--Lagrange equation; the pointwise relation
`d = −t e^TSe`, `t = |w|²/r_δ² ∈ [0,1]`, `S = sym∇w_δ`; and the constrained
trace inequality `|S|_F² ≥ d²(t²+2t+3)/(2t²) ≥ 3d²` since `3+2t−5t² ≥ 0` on
`[0,1]`. Combined with `‖curl w_δ‖₂ = ‖curl u‖₂ = √Y` and `eq:globaldivcurl`
this gives `B_δ ≤ (1/3)(B_δ + Y/2)`, hence `B_δ ≤ Y/4` and `‖∇w_δ‖₂² ≤ 5Y/4`,
uniformly in `δ`. Numerical check of the constrained trace inequality over
4·10⁵ random `(S,e,t)` triples with the constraint enforced by an identity
shift: maximum of `d²/|S|_F²` was `0.3259 < 1/3`, approaching but never
exceeding the bound.

**Integration caveat found here (M1 below):** the note's limit passage invokes
**uniform convexity of `L³`** ("Uniform convexity therefore gives `w_δ → w`
strongly in `L³`"). The manuscript's integrated proof deliberately avoids
Clarkson-type inputs, and carries a standing remark to that effect. The note's
Section 3 is therefore a corroborating independent reconstruction, **not** a
drop-in replacement for `prop:quotient-divcurl`.

### (2) The mixed-pressure identity and the two estimates, against `lem:quotient-mixed-pressure`

**Agrees.** `thm:mixed` and `lem:quotient-mixed-pressure` state the same
theorem with the same constants. The note's proof is the manuscript's proof in
compressed form; I re-derived each step:

- `∫A·((u·∇)w) = ∫u·∇(|w|³/3) = 0` because `A_iu_j∂_jw_i = u_j∂_j(|w|³/3)` and
  `div u = 0`.
- `∫A_iu_j∂_ju_i = −∫A_iu_j∂_jq_i = −∫A_iu_j∂_iq_j = ∫q_jA_i∂_iu_j`, using
  `curl q = 0` and `div A = 0`; hence `K_u = K(u)`.
- `(I−ℙ)F_b = −∇Π_b` with the stated Riesz convention, and
  `∫q·ℙF_b = 0` by `ℙq = 0` and duality. Manuscript Step 4 does this by
  approximation; the note's one-line version is the same fact.
- `|Π̂_b| ≤ |T̂|_F` because `|e⊗e|_F = 1`, so `‖Π_b‖₂ ≤ ‖b⊗A‖₂ ≤ ‖b‖₆‖A‖₃ =
  ‖b‖₆‖w‖₆²`.
- The `R^{-1/2}` cutoff boundary term vanishes by Hölder `1 = 1/3+1/2+1/6`.

The note additionally asserts `Π_b ∈ W^{1,3/2}`, which the manuscript does not
state. **Checked and correct**, not an overclaim: `b, ∇b ∈ L^∞` for `b ∈ H^m`,
`m ≥ 4`, so `T = b⊗A ∈ W^{1,3/2}`, and Riesz transforms are bounded on
`L^{3/2}` and commute with derivatives. It is not used downstream.

`cor:Kbounds`, both bounds recomputed:

- `|K| ≤ (5/8)S³Y²`: `(√Y/2)·(S√Y)·((5/4)S²Y)`. **Identical to `eq:qdc-KY`.**
- `|K| ≤ C_♯‖q‖₃D`, `C_♯ = (3/2)C₉S`. Chain: `A = |V|^{1/3}V` gives
  `|∇A| ≤ (4/3)|w|^{1/2}|∇V|`; Hölder with `(3,9,18,2)`, whose reciprocals sum
  to `6/18+2/18+1/18+9/18 = 1`; Leray on `L⁹`; then
  `‖w‖₉^{3/2} ≤ S‖∇V‖₂` and `‖∇V‖₂² ≤ (9/8)D`, and
  `(4/3)(9/8) = 3/2`. **Confirmed.** The manuscript has no counterpart; this is
  a genuine addition (integration item M4).

The two estimates do have "different uses" as claimed: the first is quadratic
in enstrophy and useless in time (`∫Y²` is exactly what is not controlled); the
second is the one that makes `(G)` the relevant absolute observable.

### (3) THE CRUX: `thm:sigmacriterion`

Every step recomputed from scratch. **All correct.**

1. *Entry.* `|K| ≤ ‖σ‖₂‖Π_u‖₂ ≤ ‖σ‖₂‖u‖₆‖w‖₆² ≤ C₆‖σ‖₂‖w‖₆³`, the last step by
   `u = ℙw` and boundedness of `ℙ` on `L⁶`. Legitimate: `b = u ∈ H^m`, `m ≥ 4`,
   on a compact classical interval.
2. *Interpolation between the cubic and ninth-power norms.* `1/6 = θ/3 +
   (1−θ)/9` gives `θ = 1/4` exactly, so `‖w‖₆³ ≤ ‖w‖₃^{3/4}‖w‖₉^{9/4}`.
   With `‖w‖₃³ = 3Q` and `‖w‖₉³ ≤ a₀D` this is `(3Q)^{1/4}(a₀D)^{3/4}`, hence
   `eq:sigma-preyoung` with `B₀ = C₆3^{1/4}a₀^{3/4}`. **Confirmed.**
3. *The exact Young step with its maximisation.* Maximising `ax^{3/4} − εx`:
   `x = (3a/4ε)⁴`, value `27a⁴/(256ε³)`. I verified the closed form both
   symbolically and numerically (numerical max `0.87821952444` vs formula
   `0.87821952442` at `a=1.3, ε=0.7`; 2·10⁵ random `(a,x,ε)` gave zero
   violations). **Exact, not merely an upper bound — the note's word
   "exact" is justified.**
4. *The constant.* `a = B₀‖σ‖₂Q^{1/4}`, `x = D`, `ε = ν/2` gives
   `27B₀⁴‖σ‖₂⁴Q/(256(ν/2)³) = (27/32)B₀⁴ν^{-3}‖σ‖₂⁴Q`, and `B₀⁴ = 3C₆⁴a₀³`, so
   the coefficient is `(81/32)C₆⁴a₀³ = C_σ`. **Exactly `eq:Csigma`.**
   Subtracting `(ν/2)D` from `Q' + νD = K` gives `eq:sigma-diff`.
5. *Measurability and integrability of the coefficient.* `t ↦ ‖σ(t)‖₂` is a
   countable supremum of continuous pairings because `w(·)` is continuous into
   `L³` and `∫(div w)η = −∫w·∇η` with `∇η ∈ L^{3/2}`; this is the manuscript's
   own argument in `cor:quotient-budgets`, so the claim is **inside audited
   scope**. Integrability: `‖σ‖₂² ≤ Y/4` with `Y` continuous on a compact
   classical interval, so `Λ` is Lipschitz there, in particular absolutely
   continuous — which is what the Gronwall step needs. **Correct.**
6. *Gronwall.* `(Qe^{−Λ})' ≤ −(ν/2)De^{−Λ}` integrates to
   `Q(t) + (ν/2)∫₀^t e^{Λ(t)−Λ(s)}D(s)ds ≤ Q(0)e^{Λ(t)}`. `Λ` is nondecreasing
   because its integrand is `‖σ‖₂⁴ ≥ 0`, so `Λ(t) − Λ(s) ≥ 0` for `s ≤ t` and
   **the exponential under the integral is indeed at least one**, giving
   `eq:sigma-integral`. `Q ∈ C¹` by the manuscript's evolution identity, so the
   product rule is licensed. **Correct.**
7. *Use of the defect--enstrophy bound within audited scope.* `‖σ‖₂ ≤
   (1/2)‖∇u‖₂` is used only (i) for integrability of the coefficient and (ii)
   for the `L²`-in-time budget `eq:energy-defect`. Both uses are at fixed time
   on solenoidal `H^1` fields, exactly the hypothesis of
   `cor:quotient-defect`. **In scope.** It is nowhere used to bound
   `∫‖σ‖₂⁴`, which would be the illegitimate move.

*Refutation attempts, all failed:* scaling consistency (under
`u_λ = λu(λx,λ²t)` one has `Q_λ(t) = Q(λ²t)`, `D_λ = λ²D`, `‖σ_λ‖₂⁴ = λ²‖σ‖₂⁴`,
so both sides scale by `λ²` — the inequality is scale-covariant, so no dilation
family can break it); sign of `D_Q` (`≥ 0`, `lem:quotient-heatsign`); uniqueness
of `w` (strict convexity, so `Q'` is unambiguous); attempt to make the Young
constant non-optimal (it is the exact maximum); attempt to find a smaller `C_σ`
by a different Hölder split (the `(3,9)` interpolation is forced by
`‖w‖₉³ ≤ a₀D` being the only available `D`-to-norm conversion).

### (4) `cor:Gproducer`: genuinely conditional, non-circular

- `eq:Qpositive` and `eq:Dpositive` are immediate from `eq:sigma-integral`.
- `eq:Gpositive`: `G(τ) ≤ (sup_{t≤τ}‖q‖₃)∫₀^τD ≤ (1+C₃)(3Q₀e^{Λ_H})^{1/3} ·
  (2Q₀/ν)e^{Λ_H} = (2(1+C₃)3^{1/3}/ν)Q₀^{4/3}e^{4Λ_H/3}`. **Recomputed; the
  displayed constant and both exponents are exactly right.**
- The degenerate case is handled (`Q₀ = 0 ⟹ u₀ = 0` by coercivity).
- **Genuinely conditional.** The hypothesis `eq:Bmissing` is a bound on a
  quantity — `∫₀^τ‖σ‖₂⁴` — that appears nowhere in the conclusion and is not
  implied by it: `sup Q` and `∫D` bound weighted quantities
  (`D = ∫ρ(|∇w|²+|∇ρ|²)`), not the unweighted `‖div w‖₂`. So the corollary is
  not an identity in disguise.
- **Not circular in the sense the programme forbids.** No continuation norm
  appears on the right; `B_σ` is quantified before the trajectory is followed;
  the note explicitly forbids defining `B_σ` as the unknown supremum.
- **But it is a member of the audited existential-equivalence class, and the
  note does not say so.** I verified the missing direction: if `T_* = ∞` for
  every datum then on `[0,H]` the map `t ↦ ‖σ(t)‖₂` is Borel and bounded by
  `√(Y(t))/2` with `Y` continuous on the compact `[0,H]`, so
  `∫₀^H‖σ‖₂⁴dt < ∞` and depends only on `(ν,u₀,H)`. Hence `eq:Bmissing` is
  equivalent, at the quantifiers of `hyp:highstrain`, to items (A)--(F) of the
  audited HF22-D Proposition 1.8. **This must be recorded** (P4/G2 below), or
  the programme will drift into treating `eq:Bmissing` as logically weaker than
  the gap. Its value is that it is a *different and more concrete mechanism* —
  one scalar function of time on a known critical line — not that it is a
  weaker statement.

### (5) The critical family, the multiplier norm, and the scaling relation

`prop:generalcriterion`, recomputed independently:

- `k = 3a'` is forced by Hölder: `‖u_iA_j‖_{a'}` needs `1/a' = 1/k + 2/k`,
  since `|A| = |w|²`. **Correct.**
- Range: `a ∈ (3/2,∞) ⟹ a' ∈ (1,3) ⟹ k ∈ (3,9)`, so `w ∈ L^k` by
  interpolation between `L³` and `L⁹`, and both multiplier constants
  `C_{T,a'}` (tensor-to-scalar `T ↦ ΣR_iR_jT_{ij}` on `L^{a'}`) and `C_k`
  (Leray on `L^k`) are finite, since both exponents are strictly between `1`
  and `∞`. **Correct, and the endpoint `a = 3/2` is properly excluded** — there
  `α = 1`, `s = ∞`, and the Young step degenerates.
- Interpolation exponent: `1/k = (1−α)/3 + α/9` with `α = 3/(2a)` reduces to
  `1/(3a') = (a−1)/(3a)`, an identity. **Confirmed.**
- General Young: `max(Ax^α − εx) = (1−α)α^{α/(1−α)}ε^{−α/(1−α)}A^{1/(1−α)}`;
  verified symbolically and numerically (`α=0.63, A=2.1, ε=0.9`: numerical
  `1.49731335043`, formula `1.49731335044`). With `ε = ν/2` this gives exactly
  the displayed `C_a` and the power `ν^{−α/(1−α)}`.
- **Consistency with the `a = 2` case:** `a'=2, k=6, α=3/4, s=4, α/(1−α)=3`,
  `C_{T,2}=1` by Plancherel (matching the manuscript's `|Π̂_b| ≤ |T̂|_F`), so
  `B₂ = B₀` and `C₂ = (1/4)(3/4)³2³B₀⁴ = (27/32)B₀⁴ = C_σ`. **The general
  family specialises exactly to `thm:sigmacriterion`.** This is a strong
  internal cross-check and it passes.
- *Multiplier norm on the relevant exponent:* the note is right that the `L²`
  case has constant one, and right that for `a ≠ 2` the constant is a genuine
  unknown-but-finite `C_{T,a'}`; it does not silently reuse `1`.
- *Scaling.* `2/s + 3/a = 2` is an identity given `s = 2a/(2a−3)`. I verified
  it is the *correct criticality relation* independently rather than accepting
  the algebra: `σ` scales as `λ²σ(λx,λ²t)`, so
  `∫₀^{T/λ²}‖σ_λ(t)‖_a^s dt = λ^{s(2−3/a)−2}∫₀^T‖σ‖_a^s dt`, and invariance
  forces `s(2−3/a) = 2`, i.e. `2/s + 3/a = 2`. **Confirmed.**
- *Is it a Serrin-type line for the divergence defect rather than the velocity
  gradient?* **Yes, and the claim is correct as stated.** `2/s + 3/a = 2` is
  the classical Ladyzhenskaya--Prodi--Serrin line *for the gradient*
  (Beirão da Veiga form), and the note states it for `σ = −div w`. The
  refinement is real in the observed quantity: only one scalar derivative of
  the minimizing representative is measured, not `∇u`. **However** — and the
  note does not say this — for `a = 2` the criterion is *implied by* the
  classical gradient criterion, since `‖σ‖₂ ≤ (1/2)‖∇u‖₂` pointwise in time
  gives `∫‖σ‖₂⁴ ≤ (1/16)∫Y²`. So the `a=2` criterion is a **weakening** of a
  known criterion, hence a legitimate refinement, but **no strict improvement
  is proved**, and for `a ≠ 2` no bound `‖σ‖_a ≲ ‖∇u‖_a` is available at all
  (that is exactly the open weighted Calderón--Zygmund question of HF18-B),
  which the note correctly flags. The candidate's literature section never
  compares against the classical gradient-Serrin criterion; that comparison
  must be added on integration (M6).

### (6) THE FRAMING CLAIM already provisionally accepted in `PLAN.md`

Decomposed into four assertions, judged separately.

**(6a) "(G) is an absolute sufficient condition obtained by discarding the
sign." — CONFIRMED but INCOMPLETE.** `(G)` is obtained by *two* independent
discardings, not one: first `K → |K|`, and second the one-sided pointwise
estimate `|K| ≤ C_♯‖q‖₃D` of `cor:Kbounds`, which is an upper bound with no
matching lower bound. The candidate itself says both ("Signed work may cancel,
and `eq:Kbounds` is an upper estimate, not an equality"); the plan's paraphrase
mentions only the sign. Fix the plan wording (P1).

**(6b) "hence a stronger proof mechanism rather than an algebraic restatement."
— CONFIRMED, in the non-derivability reading only.** `(G) ⟹ eq:signed` with
`θ = 0`, `A = C_♯A_G` is immediate and correct. The converse is **not
derivable** from the audited record: only the one-sided estimate exists, and no
field with `K = 0 < ‖q‖₃D` has been exhibited by anyone. This is precisely the
distinction the HF22-D audit enforced. The candidate's own language is
correct ("does not follow merely by reversing this implication"). **The word
"stronger" in the plan is acceptable only as shorthand for this
non-derivability; it must never be read as strictness, and the plan must say
so** — a strictness claim at these quantifiers was struck as HF22-D's first bad
bridge and must not re-enter through this door.

**(6c) "the audited HF22-D equivalence holds only at the level of
quantifiers." — CONFIRMED, verbatim against the source.** HF22-D Proposition
1.8 establishes equivalence of (A) `(G)`, (B) `(G_P)`, (C) `hyp:highstrain`,
(D) `hyp:absorption`, (E) `hyp:highpressure`, (F) `T_* = ∞ for every datum`, at
the quantifiers of `hyp:highstrain` and not per trajectory. Its repair block
R-A says so explicitly. The candidate's reading is exact.

**(6d) "the plan's phrase 'the whole of the frozen gap' was too strong." —
REFUTED as stated.** The audited HF22-D repair block R-A already fixed the
meaning of that phrase: *"The PLAN's phrase 'the frozen gap is exactly (G)' is
the audited HF21-B statement: (G) with θ=0 suffices, and no cutoff or Gronwall
term is needed."* Under that audited reading the phrase is correct, not too
strong. What is true is that the phrase is **ambiguous**: read as sufficiency it
is audited and right; read as an equivalence or an algebraic restatement it
asserts something not derivable. The plan should therefore record a
*disambiguation*, not a *correction of an error*, and should not say the earlier
wording was wrong.

**Net for the controller: the plan edit stands on its mathematics, but its two
sentences need repair — the "too strong" verdict (6d) and the missing
non-derivability qualifier (6b).** Exact replacement text is given under
REPLACEMENT ARGUMENT.

### (7) The conditional completion section against the manuscript's own chain

`thm:completion` is **correct and consistent** with the manuscript's chain, and
in one respect sharper.

- Chain verified: `eq:Bmissing` `⟹` `(G)` (by `cor:Gproducer`) `⟹` `eq:signed`
  with `θ=0` (by `cor:Kbounds`) `⟹` `eq:finalQ` `⟹` `eq:finalL3` `⟹` endpoint
  contradiction `⟹` `T_* = ∞`; then `eq:energy` gives the uniform energy bound
  of `eq:target`. Each link recomputed.
- `eq:finalQ`: integrating `Q' + νD = K` and applying `eq:signed` gives
  `Q(τ) + (1−θ)ν∫D ≤ Q(0) + A`; with `θ ≤ 1` and `D ≥ 0` this yields
  `sup‖u‖₃³ ≤ 3C₃³(Q(0)+A)` by the coercivity `‖v‖₃³ ≤ 3C₃³Q(v)`.
  **Correct**, and correctly observed that no strict absorption margin is
  needed.
- The `K_L` ↔ `K` normalisation is handled exactly as the manuscript's
  `rem:highstrain-normalisation` does, with the additive `M_L A_Q`. I checked
  the two constants: `M_L = 3(1+C₃)C_B2^{5L/2}√E₀` matches `eq:qe-lowstrain`
  identically, and `C_B = 2π‖|ξ|φ‖₂` is right (the `2^{5L/2}` comes from
  `‖|ξ|φ(ξ/2^L)‖₂² = 2^{5L}‖|ξ|φ‖₂²`).
- `A_Q = (H^{1/4}/3)(S²E₀²/(2ν))^{3/4}` is the manuscript's bound with the
  spurious factor `3` removed; the note flags this openly as a
  vector-versus-componentwise Sobolev constant. **Checked: the note is right.**
  `‖u‖₃⁴ ≤ ‖u‖₂²‖u‖₆² ≤ S²E₀Y`, and the manuscript's own
  `eq:qdc-sobolev-field` already supplies the field bound with constant `C_S`,
  so `eq:L4L3-constant`'s `3C_S²` is a factor `3` loose. Adjacent, not
  required.
- **Sharper than the manuscript in one place.** `thm:completion` reaches
  `eq:finalL3` with a purely *additive* input-only remainder, whereas the
  manuscript's `prop:quotient-conditional` carries `exp(M_LH/3)` in `eq:qe-M`.
  The additive route is available inside the manuscript already, from its own
  `rem:highstrain-normalisation` plus `eq:L4L3`. Reported as optional item M5;
  it is adjacent work, not part of this audit's mandate.
- The `L⁵` endpoint remark is correct and correctly labelled as *not* replacing
  backward uniqueness: Hölder `1/5+3/10+1/2 = 1`, interpolation
  `‖∇u‖_{10/3} ≤ C‖∇u‖₂^{2/5}‖Δu‖₂^{3/5}`, Young with conjugates `(5/4,5)`
  giving `(ν/2)Z² + Cν^{−4}‖u‖₅⁵Y`, coefficient integrable since
  `u ∈ L⁵_{t,x}`. The viscosity normalisation `v(s) = ν^{−1}u(s/ν)` with
  pressure `ν^{−2}p(s/ν)` was verified by substitution.
- **No hidden circularity**: `A`, `A_G`, `B_σ` are all quantified before the
  trajectory, and the note states plainly that defining any of them by an
  unknown endpoint supremum would assume the conclusion.

### `sec:budgets`, remaining items

- `eq:energy-defect` matches `cor:quotient-budgets` exactly
  (`5E₀/(8ν)`, `E₀/(8ν)`); it is an instantaneous bound integrated against the
  audited energy identity, which is legitimate and is the manuscript's own
  move. **No instantaneous-to-integrated promotion occurs.**
- `eq:energy-Qq`: `‖q‖₃ ≤ 2‖u‖₃` (since `‖w‖₃ ≤ ‖u‖₃`) gives
  `∫‖q‖₃⁴ ≤ 8S²E₀²/ν`; and `∫Q ≤ A_Q` by Hölder in time with `(4/3,4)`.
  **Both recomputed and correct.**
- Bad-set measure bound `|{C_♯‖q‖₃ > ν}| ≤ 8S²C_♯⁴E₀²/ν⁵`: Chebyshev at power
  four. **Correct**, and it is the audited HF21-B crossing-measure statement in
  this note's normalisation, as claimed.
- `eq:distance-balance` reproduces the manuscript's own difference identity
  (`d/dt(F(u)−Q) = P₃ − K + ν(D_Q − D₃(u))`); I re-derived the integrated form
  and the sign bookkeeping is right.
  **Quarantine:** the sentence "Theorem `thm:counter` shows that the suggested
  pointwise sign of `D − D₃(u)` is false" imports a Scope A result this audit
  does not certify. Under Scope B alone the correct statement is the audited
  one: the sign of `D_Q − D₃(u)` is not available in either direction (audited
  HF19-D and HF22-A), so the term may not be dropped. **The conclusion of the
  subsection is unaffected either way.**
- The scalar comparison family: I verified every displayed relation
  (`∫₀¹Y = 4`, `E ≥ 1`, `z² = Y/4`, `Y' ≤ (3/4)Y³`, `d³ = Q`, `Q ≤ Y^{3/4}`,
  `∫d⁴ < ∞`, `∫Q^{4/3} < ∞`, `Q' + D = K`, and the three work bounds with the
  exponent comparisons `7/5 < 43/30`, `7/5 < 3/2`, `7/5 < 29/20`), and the
  three divergences (`∫dD = ∞` since `43/30 > 1`, `∫z⁴ = ∞` since `3/2 > 1`,
  `Q → ∞`). I also checked the constraints the family is *not* asked to
  satisfy but that a real trajectory does satisfy — `∫Y ≤ E₀/(2ν)` (`4 ≤ 4.5`),
  `∫z² ≤ E₀/(8ν)` (`1 ≤ 1.125`), `Q^{4/3} ≲ Y` — and found no violation, so the
  family is not the incomplete-constraint-list failure that the HF22-C audit
  caught. **Scope narrowing to record:** the constants are declared
  illustrative, so what the family establishes is non-derivability *at the
  level of the inequality shapes*, i.e. it defeats any argument using only
  these shapes with unspecified constants; it does not defeat an argument that
  exploits the sharp constants. The note's own framing ("this example does not
  show that such structure cannot be found") is honest and should be preserved
  verbatim on integration.

---

## REPLACEMENT ARGUMENT

No mathematics needs replacing. Two pieces of *recorded wording* do, both in
`PLAN.md`, and one scope sentence must be added to any manuscript import.

**R1. Replacement for the plan's framing paragraph (§HF25).** Replace

> This plan has described the target inequality as "the whole of the frozen
> gap". That is too strong. The target is an *absolute* sufficient condition
> obtained by discarding the sign, whereas the manuscript's hypothesis is
> signed and permits cancellation; it is therefore a stronger proof mechanism,
> not an algebraic restatement.

by

> This plan has described the target inequality as "the whole of the frozen
> gap". The phrase is **ambiguous, not wrong**: read as sufficiency it is the
> audited HF21-B statement, endorsed verbatim by the HF22-D repair block R-A —
> `(G)` with `θ=0` suffices, with no cutoff and no Gronwall term. Read as an
> equivalence it asserts something **not derivable**. Disambiguated: `(G)` is
> an *absolute* sufficient condition obtained by two discardings — the sign of
> `K`, and the one-sided estimate `|K| ≤ C_♯‖q‖₃D_Q`, which has no audited
> lower counterpart. `(G) ⟹ hyp:highstrain` with `θ=0` and
> `A = C_♯A_G`; the converse is **not derivable per trajectory** from the
> audited record, and **no strictness claim is available**, since no field with
> `K = 0 < ‖q‖₃D_Q` has been exhibited. That is a statement about the shape of
> the two estimates, not about their logical strength.

*Proof of R1.* `(G) ⟹ hyp:highstrain` with `θ=0`: pointwise
`K ≤ |K| ≤ C_♯‖q‖₃D_Q` by `cor:Kbounds`, integrate. Non-derivability of the
converse: `cor:Kbounds` is one-sided and no lower bound `|K| ≥ c‖q‖₃D_Q` is
audited or proved anywhere in HF18--HF25; and `S(u)`, `ŵ`, `‖q‖₃`, `D_Q` are
all determined by the same `u` and cannot be varied independently, which is
exactly why HF22-D's strictness claim was struck. Unavailability of a
strictness claim at the `hyp:highstrain` quantifiers: HF22-D Proposition 1.8
gives equivalence there. ∎

**R2. Replacement for the plan's "Ordered next actions" item 4.** Replace
"is the whole of the frozen gap with contraction factor zero" by "**suffices**
to close the frozen gap with contraction factor zero, with no Gronwall term and
no frequency cutoff (audited HF21-B; the converse is not derivable per
trajectory)".

**R3. Scope sentence required in any manuscript import of the criterion.**

> Because `‖σ‖₂ ≤ ½‖∇u‖₂` at each time, the hypothesis
> `∫₀^τ‖σ‖₂⁴dt ≤ B_σ` is implied by the classical gradient criterion
> `∇u ∈ L⁴_t L²_x` on the Ladyzhenskaya--Prodi--Serrin line `2/s + 3/a = 2`.
> The criterion is therefore a weakening of a known sufficient condition in the
> observed quantity; no strict improvement is proved, and for `a ≠ 2` no bound
> of `‖σ‖_a` by `‖∇u‖_a` is available at all. At the quantifiers of
> Hypothesis~\ref{hyp:highstrain} the hypothesis is equivalent to global
> continuation, like every other member of that class.

*Proof of the last sentence.* Sufficiency is `cor:Gproducer` plus
`prop:quotient-conditional`. Necessity: if `T_* = ∞` for every datum then on
`[0,H]` the map `t ↦ ‖σ(t)‖₂` is Borel (`cor:quotient-budgets`) and bounded by
`½√(Y(t))` with `Y` continuous on the compact `[0,H]`, so
`∫₀^H‖σ‖₂⁴dt < ∞` and depends only on `(ν,u₀,H)`. ∎

---

## CONDITIONAL SUFFIX THAT SURVIVES

All of it, with the scope sentences above attached:

1. `thm:divcurl` — survives; already the manuscript's audited
   `prop:quotient-divcurl`. Corroborating reconstruction only.
2. `cor:sigma` — survives; already `cor:quotient-defect`.
3. `thm:weighted` (`D_Q = D₃(w) = ∫ρ(|∇w|²+|∇ρ|²)`, `V ∈ H¹`,
   `D_Q ≥ (8/9)‖∇V‖₂²`, `‖w‖₉³ ≤ (9S²/8)D_Q`) — **survives, and is the one
   Scope-B result not yet in the manuscript.** Its proof here is complete and
   now rests only on manuscript theorems.
4. `thm:mixed` — survives; already `lem:quotient-mixed-pressure`.
5. `cor:Kbounds` — both bounds survive; the second
   (`|K| ≤ (3/2)C₉S‖q‖₃D_Q`) is new to the manuscript.
6. `thm:sigmacriterion` — **survives in full**, constant `C_σ` confirmed.
7. `cor:Gproducer` — survives, genuinely conditional, all three displayed
   consequences confirmed with the displayed constants.
8. `prop:generalcriterion` and `eq:defectscaling` — survive; the family
   specialises exactly to (6) at `a=2`, and the scaling line is correct.
9. `eq:energy-defect`, `eq:energy-Qq`, `eq:lowstrain`, `eq:signed`, the bad-set
   measure bound, `eq:distance-balance` — survive; all reproduce audited
   repository statements with recomputed constants.
10. The scalar family — survives as a **shape-level non-derivability witness**
    only.
11. `thm:completion` — survives, and is additively sharper than
    `prop:quotient-conditional`.

Not certified here: `thm:counter`, `thm:alpha`, `thm:Genergy`, and everything
in `sec:literature`.

## UNNECESSARY DEPENDENCIES

The criterion and its producer are logically independent of most of the note:

- `thm:sigmacriterion`, `cor:Gproducer`, `prop:generalcriterion` and
  `thm:completion` need **none** of `thm:counter`, `thm:alpha`, `thm:Genergy`,
  the distance balance, the scalar family, HF20, HF21-A, HF21-B, HF22, or the
  frequency split `S_L` (the criterion is stated for the full `K`).
- They need only: `prop:quotient-divcurl` + `cor:quotient-defect` +
  `lem:quotient-mixed-pressure` + the evolution identity (all audited
  manuscript results), `thm:weighted` (audited HF18-A, **not** in the
  manuscript), and boundedness of the Leray projection on `L⁶` (and `L⁹` for
  the second bound of `cor:Kbounds`).
- Conversely, `thm:weighted` does **not** need the `L²∩L³` regularisation of
  `sec:divcurl`; it needs only the *conclusion* `∇w ∈ L²`.
- `w ∈ L²(ℝ³)` and `σ ∈ L^{3/2}(ℝ³)` are used nowhere in Scope B, exactly as
  the note's remark asserts, and as `rem:quotient-divcurl-scope` requires.

## NON-CLAIMS

- No regularity theorem, no blowup, no proof of `hyp:highstrain`,
  `hyp:highpressure`, `hyp:critical` or NS-R3. `eq:Bmissing` remains unproved
  for arbitrary data, and is equivalent at the problem's quantifiers to the
  conclusion it produces.
- No node promotion, demotion, or graph edit is authorised by this audit.
- No claim that the two artifacts behind the differing hashes are byte-identical
  — only that every Scope-B attribution matches what audited HF23 proves, and
  that page count and theorem numbering coincide.
- No novelty or priority claim; the `a=2` criterion is a weakening of a
  classical gradient criterion.
- The numerics reported here (four random-sampling checks, `pdflatex` page
  count) are evidence, never proof.
- This audit does not certify `thm:counter`, `thm:alpha` or `thm:Genergy`.

## REOPENING CONDITION

Reopen this verdict if any of the following occurs:

1. The actual 23-page PDF is delivered and its Theorems 3.1, 4.2 or 7.1 differ
   in statement or constant from HF23's `thm:main`, `thm:mixed`,
   `thm:spacetime`.
2. `thm:weighted`'s coercivity `‖w‖₉³ ≤ (9S²/8)D_Q` is found to fail on a field
   whose minimizer vanishes on a set of positive measure — the chain-rule and
   level-set steps are where such a failure would live.
3. A Scope A audit refutes `thm:counter`; then the single sentence in
   `sec:budgets` citing it must be replaced by the audited two-sided
   non-availability statement (the subsection's conclusion is unaffected).
4. Any proof of `eq:Bmissing` appears; it must be re-audited for circularity
   against R3 above, since `eq:Bmissing` is equivalent at the quantifiers to
   global continuation.
5. A lower bound `|K| ≥ c‖q‖₃D_Q` is proved or a field with `K = 0 < ‖q‖₃D_Q`
   is exhibited; either would move item (6b) out of non-derivability, in one
   direction or the other.
6. The manuscript's `rem:qe-heatsign-scope` is left unamended while
   `thm:weighted` is imported — the two are then contradictory.

---

## EXACT EDITS THE CONTROLLER SHOULD MAKE IF THIS VERDICT STANDS

### Manuscript (`navier-paper/main.tex`)

- **M1. Do not replace `prop:quotient-divcurl`.** HF25 `sec:divcurl` invokes
  uniform convexity of `L³` in its limit passage; the manuscript's integrated
  proof deliberately avoids Clarkson-type inputs and carries a standing remark
  to that effect. Record HF25 `sec:divcurl` as an independent corroborating
  reconstruction in `rem:quotient-related` or the section notes, nothing more.
- **M2. Add the weighted dissipation identity and its coercivity**, in
  `subsec:qe-trajectories` after `def:qe-dissipation`: with `ρ=|w|`,
  `V=ρ^{1/2}w`, prove `V ∈ H¹`,
  `D_Q(u) = ∫ρ(|∇w|²+|∇ρ|²) = ∫(|∇V|² − (1/9)|∇|V||²)`, hence
  `D_Q ≥ (8/9)‖∇V‖₂²` and `‖w‖₉³ ≤ (9C_S²/8)D_Q`. HF25 `thm:weighted` supplies
  a complete proof that now rests only on `prop:quotient-divcurl` and
  `cor:quotient-defect`; the only external ingredient is the elementary
  two-sided comparison `eq:Vcompare`, whose endpoint verification is
  reproduced above and is sharp at `8/9`.
- **M3. Amend `rem:qe-heatsign-scope`.** Its sentence "no lower bound for
  `D_Q` … or in terms of any norm of `u`, is asserted" becomes false once M2
  lands. Replace by: no comparison with `D₃(u)` is claimed (which remains
  true, in both directions), while the lower bound `‖w‖₉³ ≤ (9C_S²/8)D_Q` is
  now proved.
- **M4. Extend (F5)** to `p = 6` and `p = 9` (currently "Only `p=3` and
  `p=3/2` are used"), needed for `‖u‖₆ ≤ C₆‖w‖₆` and `‖u‖₉ ≤ C₉‖w‖₉`.
- **M5. Add the criterion**, after `lem:quotient-mixed-pressure`:
  `|K_u| ≤ (3/2)C₉C_S‖q‖₃D_Q` (new); then
  `Q' + (ν/2)D_Q ≤ C_σν^{−3}‖σ‖₂⁴Q` with
  `C_σ = (81/32)C₆⁴(9C_S²/8)³`; then the Gronwall corollary
  `Q(t) + (ν/2)∫₀^tD_Q ≤ Q(0)e^{Λ(t)}`; then the conditional producer with
  `eq:Qpositive`/`eq:Dpositive`/`eq:Gpositive` and the constant
  `2(1+C_ℙ)3^{1/3}ν^{−1}Q₀^{4/3}e^{4Λ_H/3}`. Attach **R3** as the scope
  remark. State the general family `prop:generalcriterion` with the line
  `2/s + 3/a = 2` only if the manuscript is willing to carry the two extra
  multiplier constants; it is not needed for the `a=2` chain.
- **M6 (adjacent, optional, report rather than do).** `eq:L4L3-constant`'s
  factor `3` can be dropped using the manuscript's own
  `eq:qdc-sobolev-field`; and `prop:quotient-conditional`'s `exp(M_LH/3)` in
  `eq:qe-M` can be replaced by the additive `M_LA_Q` using
  `rem:highstrain-normalisation`. Both are improvements to existing audited
  text, outside the scope of this import.

### Claim graph

- **G1.** Under HIGH-STRAIN, record the conditional producer chain
  `eq:Bmissing ⟹ (G) ⟹ hyp:highstrain (θ=0)` with the explicit constants, and
  the new node QUOTIENT-DEFECT-CRITERION as a *conditional* producer. **No gap
  node is promoted.**
- **G2.** Record in the same review text that `eq:Bmissing` is a member of the
  audited HF22-D Proposition 1.8 existential-equivalence class (A)--(F), with
  the necessity proof of R3.

### `PLAN.md`

- **P1.** Apply **R1** to the HF25 framing paragraph.
- **P2.** Apply **R2** to "Ordered next actions" item 4.
- **P3.** Replace the "Note for the audit" hash paragraph in §HF25 by the
  resolved finding: the differing hash is the PDF rendering of the same
  document; our `.tex` compiles to exactly 23 pages, and HF23's Theorems 3.1,
  4.2, 7.1 are `thm:main`, `thm:mixed`, `thm:spacetime`; every Scope-B
  attribution matches what audited HF23 proves; HF25 correctly does *not*
  attribute the weighted identity to the attachment, which HF23 itself
  disclaims.
- **P4.** Record the sharpened FIRST GAP: upgrade the divergence defect from
  `L²_t L²_x` (unconditional, `E₀/(8ν)`) to `L⁴_t L²_x` for arbitrary data, on
  the critical line `2/s + 3/a = 2`; and record with it that this statement is
  equivalent at the problem's quantifiers to global continuation, so its value
  is as a *different mechanism*, not a weaker statement.
- **P5.** Record the two audit-scope narrowings: the scalar family is a
  shape-level non-derivability witness only, and `sec:budgets`' use of
  `thm:counter` is quarantined pending the Scope A verdict.

## Open Questions

- needs review: Scope A of HF25 (`thm:counter`, `thm:alpha`, `thm:Genergy`) is
  not audited here; `sec:budgets` cites `thm:counter` once.
- needs review: whether the `a=2` defect criterion is *strictly* weaker than
  the classical gradient criterion `∇u ∈ L⁴_tL²_x`, i.e. whether a trajectory
  with `∫Y² = ∞` but `∫‖σ‖₂⁴ < ∞` exists. Unknown; no witness either way.
- needs review: HF25's literature section makes no comparison with the
  Ladyzhenskaya--Prodi--Serrin / Beirão da Veiga gradient criterion, which is
  the exact classical statement on the same line `2/s + 3/a = 2`.
- needs review: the optional manuscript sharpenings M6 (`eq:L4L3-constant`
  factor 3; `eq:qe-M` exponential to additive).
