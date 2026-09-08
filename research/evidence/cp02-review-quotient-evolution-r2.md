# CP02-7 AUDIT (round 2): review of `cp02-quotient-evolution.md` (version 2)

MODE: REVIEW, proof-audit discipline. Date: 2026-09-05. Lane: round-2 audit of
`research/evidence/cp02-quotient-evolution.md` (obligations Q-8 .. Q-18,
`eq:quotient-evolution`, `eq:quotient-gap`), after the round-1 audit
`cp02-review-quotient-evolution.md` (verdict REPAIR) and the author's
repair round.

## 0. Freeze record

| Item | Value |
| --- | --- |
| Candidate file | `../navier/research/evidence/cp02-quotient-evolution.md` |
| `sha256sum` | `799b3590e6163e0ebfb8cf15cd2ba9a8a297ffc7f116899a9a263b6307c5b46a` |
| `git -C ../navier rev-parse HEAD` | `fc1ee2bcc7afbbef43bb41a9c5070009034e603f` |
| Candidate length | 1501 lines; LaTeX block 1179 lines (extracted verbatim) |
| Manuscript | `../navier-paper/main.tex`, 562 lines, read in full |
| Round-1 audit | `cp02-review-quotient-evolution.md`, 593 lines, read in full |
| Sibling lanes read at source | `cp02-quotient-functional.md` (all cited labels and sub-item letters), `cp02-lowpressure.md` (`def:lp`, `eq:lp-symbol`, `lem:lp-coincide`, `lem:lowpass-kernel`, `lem:bernstein`), `cp02-local-theory.md` (`prop:localtheory`, `lem:sobolev-norms`, `lem:embedding`), `cp01-manuscript-obligations.md` §1.14, `cp01-literature-statements.md` §1.4/§6 |
| Independent compile | block extracted, spliced under a stub preamble written here (six theorem environments, `\R`, `\norm`, 26 label stubs), `latexmk -pdf` twice: exit 0, **0** undefined references, **0** overfull boxes |
| Independent source checks | Grafakos CFA 3rd ed. book pp. 110-115 and 20-21; Rudin RCA 3rd ed. book pp. 69, 153-156 (all opened in this session through `helpy_pdf`, text mode); Mathlib `0df444a` lines re-opened for E1, E7, E10 |

Nothing outside this file was written. Nothing here proves or claims
HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3.

---

## 1. VERDICT

**PASS.**

Every bridge of the candidate reconstructs correctly from its first
nontrivial implication. The round-1 first bad bridge (Grafakos Thm. 2.2.14
cited for an `L^2` statement) is repaired exactly as prescribed and the
replacement citation is **verified verbatim at the source** in this session;
all five REPAIRs and all thirteen minor items M1-M13 of round 1 are applied,
and I checked each against the round-1 text. All four textbook facts used in
the block (E7-E10) were opened here and support exactly the statements they
are attached to, so the block's `[DI]` claims are correct. The deepest step,
the transport identity `eq:qe-transport`, was attacked by an independent
route and **survived**: it is equivalent, by exact pointwise algebra plus
stationarity, to a hidden identity that I proved formally and confirmed
numerically (§4.3). No mathematical error, no unsupported external fact, no
circularity, and no illegitimate use of package (R) was found.

The residue is editorial: one internal display pointer aims at the wrong
equation inside the right lemma, six one-clause justification or notation
gaps that a strict reading of D5 wants written out, and a redundancy with
the local-theory lane that the integrator should collapse (§9, §7). None of
these invalidates or weakens any statement, so they are listed as minor
issues rather than repairs; the exact insertion texts are supplied in §5 so
the integrator need not re-derive them.

---

## 2. REVIEWED SCOPE

Reconstructed independently of the candidate's prose and of round 1,
checking quantifiers, function spaces, exponents, constants, decay at
infinity, measurability, and every appeal to package (R):

- **Package (R) legitimacy.** (R1)-(R3) are compared with D2 *and* with the
  actual `prop:localtheory` of `cp02-local-theory.md` (read at source,
  line 1021 ff.). (iii) there gives `u,p ∈ C^j([0,T];H^k)` for all `j,k`
  with the classical time derivatives, all `∂_t^j∂_x^α u`, `∂_t^j∂_x^α p`
  bounded on `[0,T]×R^3`; (iv) gives the pointwise equation and
  `p = R_iR_j(u_iu_j)`. The candidate's (R1) (`∂^α u ∈ C^1([0,T];H^k)`)
  follows from (iii) with the lane's own `lem:sobolev-norms`
  (`‖∂^αf‖_{H^m} ≤ (2π)^{|α|}‖f‖_{H^{m+|α|}}`) and `lem:embedding`(b)
  (classical = distributional derivatives for the smooth representative).
  (R3) follows from (iii) plus `lem:embedding`(a),(c). **Legitimate.** No
  spatial decay of `u(t)` beyond `H^k` membership is used anywhere in the
  block (re-checked line by line, independently of round 1's check): the
  only places where decay could enter are `lem:quotient-pressure` (uses
  `p,∇p ∈ L^3` only), `lem:heat-generator` (uses `f,∇f,∇^2f` bounded and
  `Δf ∈ L^3`, *not* `f ∈ L^3`), and the transport lemma (uses `u ∈ L^3`,
  `Du` bounded uniformly continuous). D2's prohibition is respected.
- `lem:qe-embedding`: `∫(1+|ξ|^2)^{-2}dξ = 4π∫_0^∞ r^2(1+r^2)^{-2}dr`,
  `r = tanϑ` gives `4π·(π/4) = π^2`, so `‖f̂‖_1 ≤ π‖f‖_{H^2}` for the norm
  `eq:qe-sobolev-norm` — **recomputed, correct**; uniform continuity of
  `g(x) = ∫e^{2πix·ξ}f̂dξ` by dominated convergence with dominant `2|f̂|` —
  correct; `‖f‖_3^3 ≤ ‖f‖_∞‖f‖_2^2` — correct; the derivative clause with
  `|ξ^α| ≤ |ξ|^{|α|} ≤ (1+|ξ|^2)^{k/2}` for `|α| ≤ k`, giving
  `‖∂^αf‖_∞ ≤ π(2π)^{|α|}‖f‖_{H^{k+2}}` and `4π^3‖u(t)‖_{H^4}` for second
  derivatives — **recomputed, correct**.
- `lem:qe-average`: Hölder on `J` with `3, 3/2` (`|∫_0^sF|^3 ≤ |s|^2∫_J|F|^3`),
  Tonelli on `J×R^3` — correct for both signs of `s`.
- `lem:qe-gronwall`: `d/dt(e^{-Mt}Y) ≤ ae^{-Mt}` ⇒ `MY ≤ a(e^{Mt}-1)` ⇒
  `y ≤ ae^{Mt}`; negative time by `ỹ(t) = y(-t)` with
  `|∫_0^{-t}y| = ∫_0^tỹ` (substitution rechecked) — correct.
- `lem:qe-mollify`, `lem:quotient-pressure`: mollification with
  `∇g_ε = ρ_ε*∇g`, `‖∇g_ε-∇g‖_3 ≤ ω(ε)|K|^{1/3}`; the cutoff split
  `∇(χ_Rp)-∇p = (χ_R-1)∇p + p∇χ_R` and `eq:qe-cutoff-error` with
  `0 ≤ 1-χ_R ≤ 1_{|x|≥R}`, `|∇χ_R| ≤ R^{-1}‖∇χ‖_∞` — correct; both error
  terms vanish from `p,∇p ∈ L^3` alone. Stationarity is now cited to
  `lem:quotient-minimizer`**(c)** — **verified at source**
  (`cp02-quotient-functional.md`, item (c) is `⟨A(u),g⟩ = 0` on `G_3`).
- `lem:quotient-chainrule`: `C^1([0,T];H^2) → C^1([0,T];L^3)` through
  `eq:qe-embedding`; `‖δ‖_3 ≤ K|h|`; the remainder now bounded through
  `eq:cp-derivative-remainder` (`|r(δ)/h| ≤ 6(‖w‖_3+K|h|)^{3/2}K^{3/2}|h|^{1/2}`,
  manifestly monotone, M2 discharged); the three-term continuity split
  `⟨A(t)-A(s),u_t(t)⟩ + ⟨A(s),u_t(t)-u_t(s)⟩`; exact cancellation of
  `⟨A,∇p⟩` — correct.
- Heat block: `∂_rk_r = k_r(-3/2r+|z|^2/4r^2)`, `∂_jk_r = -(z_j/2r)k_r`,
  `Δk_r = k_r(|z|^2/4r^2-3/2r)`, hence `∂_rk_r = Δk_r` — recomputed,
  correct; `eq:qe-kernel-dominant` in `L^1` — correct; the scaling
  `k_r(√r z)r^{3/2} = k_1(z)` giving `∫_{|y|>δ}k_r = η(δ/√r)` — correct;
  `lem:qe-heat-continuity`(a) `|G_rf-f| ≤ ω_f(δ)+2‖f‖_∞η(δ/√r)` and the
  joint-continuity dominant — correct; (b) `‖I_1‖_3 ≤ ω_g(δ)|K_δ|^{1/3}`,
  `‖I_2‖_3 ≤ 2η(δ/√r)‖g‖_3` by Minkowski — correct;
  `lem:heat-generator` Steps 1-5 (coordinatewise double integration by
  parts with Gaussian×bounded boundary terms, Fubini, differentiation under
  the integral, `a↓0`, then `lem:qe-average`) — correct, and
  `eq:qe-generator` indeed needs `Δf ∈ L^3` but not `f ∈ L^3`.
- `def:qe-dissipation` + `lem:quotient-heatsign` (M5 discharged):
  `0 ≥ (Q(G_su)-Q(u))/s = ⟨A,h_s/s⟩ + r(h_s)/s` with
  `‖h_s‖_3 ≤ s‖Δu‖_3`, remainder `≤ 6(‖w‖_3+s‖Δu‖_3)^{3/2}‖Δu‖_3^{3/2}s^{1/2}`
  — correct; `D_Q ≥ 0`; continuity from `A ∈ C_tL^{3/2}`, `Δu ∈ C_tL^3`.
- `lem:qe-jacobi`: Leibniz expansion, `C_{ki}` = determinant of `M` with
  the `i`-th column replaced by `e_k` = the `(k,i)` cofactor,
  `adj(M)_{ik} = C_{ki}`, `tr(adj(M)BM) = tr(B)det M` — correct.
- `lem:flow`: weighted-norm contraction `Λ∫_0^se^{2Λσ}dσ ≤ ½e^{2Λs}`;
  group property; `|Φ_s(y)-Φ_s(y')| ≤ e^{Λ|s|}|y-y'|`; the variational
  equation with `|M_s| ≤ e^{Λ|s|}`; joint continuity
  `|Z(s)| ≤ |s|e^{2Λ|s|}ω(e^{Λ|s|}|y-y'|)`; differentiability
  `|z(s)| ≤ |s|e^{2Λ|s|}ω(e^{Λ|s|}|h|)|h| = o(|h|)` uniformly in `y`;
  Liouville `det DΦ_s ≡ 1`; the expansions `|M_s-I| ≤ Λ|s|e^{Λ|s|}`,
  `|M_s-I-sDb| ≤ |s|e^{Λ|s|}(ω(|s|‖b‖_∞)+Λ^2|s|)`, and for
  `|s| ≤ 1/(4Λ)` (so `|N| ≤ ¼e^{1/4} ≈ 0.3210 < ½`) the Neumann bounds
  `|(I+N)^{-1}-I| ≤ 2|N|`, `|(I+N)^{-1}-I+N| ≤ 2|N|^2`, hence
  `eq:qe-flow-inverse` — **every constant recomputed independently,
  correct**. M3 is discharged: both Gronwall applications now say
  "on the interval with endpoints `0` and `s`" with a constant forcing.
  The `Λ = 0` case is handled separately before the estimates.
- `lem:qe-pullback`: Rudin 7.26 with `X = V = R^3` (hypotheses (i)-(iii)
  checked against the source, §4.1); the Borel-null-set argument making
  `f ↦ f∘Φ` well defined on classes; `‖T_Φf‖_3 ≤ Λ_Φ‖f‖_3` using
  `|M^T| = |M|`; `T_Φ∇φ = ∇(φ∘Φ)` with the index check
  `(DΦ^Tv)_i = ∂_iΦ_j v_j` against `eq:qe-jacobian` — correct. The
  candidate's null-set step is exactly the point Rudin flags on book p. 156
  ("we did not prove that `f∘T` is Lebesgue measurable for all Lebesgue
  measurable `f`"); the candidate anticipates it correctly.
- `lem:quotient-transport`, all five steps: the change of variables at
  `x = Φ_s(y)` giving `u_s+q_s = w + E_sq` with
  `E_s = DΦ_s^{-T}-I` — recomputed from the pullback definition, correct
  (the transposition is the 1-form pullback, so `T_Φ∇φ = ∇(φ∘Φ)` holds and
  `q_s ∈ G_3`); `eq:qe-envelope` with equality at `s=0`;
  `‖h_s‖_3 = O(|s|)`, `eq:cp-F-taylor` giving `O(s^2)`,
  `‖E_s+sDu^T‖_∞ = o(|s|)`; `d/dσ u(Φ_{-σ}(x)) = -g(Φ_{-σ}(x))`;
  the `L^3` continuity `‖g∘Φ_{-σ}-g‖_3 → 0` by `C_c` approximation with
  support in `K = supp g_ε + B̄_{s_0‖u‖_∞}`; the two-sided division by
  `s > 0` and `s < 0` (`f ≤ g`, `f(0) = g(0)`, both differentiable ⇒
  `f'(0) = g'(0)`); the index contraction
  `⟨A,Du^Tq⟩ = ∫A_i(∂_iu_j)q_j = ∫q·((A·∇)u)` — correct, and identical to
  Q-16 of `cp01-manuscript-obligations`. See §4.3 for the independent
  confirmation.
- `prop:quotient-evolution`: signs and the factor `ν` match the
  manuscript's `eq:quotient-evolution` exactly; the three-term continuity
  estimate with exponents `∞,3,3/2` and the pointwise bound
  `|q·(Dv A)| ≤ |q||Dv||A|` — correct. M13 discharged ("with the notation
  and package (R) of Section~\ref{subsec:qe-trajectories}").
- `lem:quotient-lowstrain`: `|q·((A·∇)v)| ≤ |q||Dv|_F|A|` via
  `eq:qe-frobenius` (M10 discharged: `|M| ≤ |M|_F` is now displayed and
  proved by Cauchy-Schwarz); Hölder `∞,3,3/2` (`1/∞+1/3+2/3 = 1`);
  `sup|Dv|_F ≤ C_B2^{5L/2}‖u(t)‖_2 ≤ C_B2^{5L/2}‖u_0‖_2` (`prop:energy`);
  `‖q‖_3 ≤ (1+C_P)‖w‖_3` (`lem:quotient-coercive`, verified at source);
  `‖A‖_{3/2} = ‖w‖_3^2`, `‖w‖_3^3 = 3Q(u)`
  (`lem:quotient-minimizer`**(b)**, verified at source); hence
  `M_L = 3(1+C_P)C_B2^{5L/2}‖u_0‖_2` — **recomputed, correct**, and equal
  to the coefficient of Q-17. `C_B = 2π‖|ξ|φ‖_2 ≤ 16π√(2π/5)`
  re-derived from `∫_{|ξ|≤2}|ξ|^2dξ = 128π/5` and
  `‖∇κ_L‖_2^2 = 2^{5L}‖∇κ‖_2^2` — correct (the exponent is `5L/2`).
- `hyp:highstrain` (M6 discharged: `K_L` restated inside), the paragraph
  after it, `prop:quotient-conditional`: the integrated identity, absorption
  of `(1-θ)ν∫D_Q ≥ 0` (legitimate because `θ ≤ 1` **and** `D_Q ≥ 0` is
  proved), Gronwall, and
  `sup‖u(τ)‖_3^3 ≤ C_P^3(‖u_0‖_3^3+3A_input)e^{M_LH}`, i.e.
  `eq:qe-M` with `exp(M_LH/3)` — **recomputed, correct**; the quantifier
  order matches `eq:missing` verbatim (one `M` per `(ν,u_0,H)`, valid on
  the whole interval).
- `rem:highstrain-scope`: forward direction and the `L = 0`, `θ = 0`,
  `A_input = ∫_0^H|K_0|` converse on a global branch — correct and
  structurally parallel to the manuscript's paragraph for
  `hyp:highpressure`.

---

## 3. FIRST BAD BRIDGE

**None.** No inference in the block fails as written.

Round 1's first bad bridge is closed. The sentence in `lem:qe-embedding`
now reads "both facts are part of Definition~\ref{def:lp}, and their source
is `\cite[\S2.2.4, pp.~113--114]{Grafakos2014}`", and `Thm.~2.2.14` occurs
nowhere in the lane (grep: zero hits). I re-opened the source: **Theorem
2.2.14 is on book p. 112 and is stated "Given `f`, `g`, and `h` in
`S(R^n)`"**, while §2.2.4 ("The Fourier Transform on `L^1+L^2`", book
pp. 113-115) contains verbatim "for `f` in `L^1(R^n) ∩ L^2(R^n)` the
expressions `f̂` and `F(f)` coincide pointwise a.e." and "`F'` coincides
with the inverse operator `F^{-1}` of `F : L^2 → L^2`, and Fourier
inversion `f = F^{-1}∘F(f) = F∘F^{-1}(f)` a.e. holds on `L^2`", plus "the
Fourier transform is an `L^2` isometry on `L^1∩L^2` … there is a unique
bounded extension … `F`" and "we let `F'` be the isometry on `L^2` that
extends the operator `f ↦ f^∨`". These are exactly the four facts the proof
uses, and exactly what `def:lp` records. The `[DI]` upgrade of E10 is
correct, and the pages are correct.

The closest thing to a defective bridge is editorial and is item 5 of §9:
in `prop:quotient-evolution` the claim "`q(t) = w(t)-u(t)` is continuous
into `L^3`" is attached to `\eqref{eq:cp-continuity}`, which bounds
`‖A'-A‖_{3/2}` and `|Q(u+h)-Q(u)|`; the `L^3` continuity of `u ↦ w` is
`\eqref{eq:cp-strong}` of the *same* lemma (`lem:quotient-stability`, whose
"In particular" clause states it explicitly). The cited lemma supports the
claim, so the inference is valid and nothing downstream moves; only the
display number is wrong. The second occurrence (`lem:quotient-chainrule`
Step 3, continuity of `t ↦ A(t)` into `L^{3/2}`) points at
`eq:cp-continuity` **correctly**.

---

## 4. EVIDENCE

### 4.1 Sources opened in this session (all `[DI]` here)

| Fact as the candidate uses it | Source opened | Result |
| --- | --- | --- |
| E10 `L^2` Fourier theory (coincidence on `L^1∩L^2`, `F` isometry, `F^{-1}` extending `·^∨`, inversion a.e. on `L^2`) | Grafakos, *Classical Fourier Analysis* 3rd ed., book pp. 110-115 (PDF pp. 127-132), text extraction | **CONFIRMED**, verbatim as quoted above. Thm. 2.2.14 (p. 112) is Schwartz-only, as round 1 said; the `L^1`-inversion caveat "This inversion is possible when `f̂` is also integrable; see Exercise 2.2.6" is on p. 113, exactly as the candidate's E10 records. |
| E9 Minkowski for convolution `‖g*f‖_p ≤ ‖g‖_1‖f‖_p` | same PDF, book pp. 20-21 | **CONFIRMED**: "Theorem 1.2.10. (Minkowski's inequality) Let `1 ≤ p ≤ ∞`. For `f` in `L^p(G)` and `g` in `L^1(G)` we have that `g∗f` exists `λ`-a.e. and satisfies `‖g∗f‖_{L^p(G)} ≤ ‖g‖_{L^1(G)}‖f‖_{L^p(G)}`." `R^3` with Lebesgue measure is the abelian instance; used with `p = 3`, `g = k_r` and `g = k_r1_{|y|>δ}`. |
| E7 change of variables | Rudin, *Real and Complex Analysis* 3rd ed., book pp. 153-156 | **CONFIRMED**: "7.26 Theorem Suppose that (i) `X ⊂ V ⊂ R^k`, `V` is open, `T : V → R^k` is continuous; (ii) `X` is Lebesgue measurable, `T` is one-to-one on `X`, and `T` is differentiable at every point of `X`; (iii) `m(T(V-X)) = 0`. Then, setting `Y = T(X)`, `∫_Y f dm = ∫_X (f∘T)|J_T| dm` for every measurable `f : R^k → [0,∞]`", and "The case `X = V` is perhaps the most interesting one." The candidate's use (`X = V = R^3`, `T = Φ`, `T(V∖X) = ∅`, `|det DΦ| ≡ 1`, `Φ(R^3) = R^3`) is exactly covered. Book p. 156 carries Rudin's warning that `f∘T` need not be Lebesgue measurable for Lebesgue measurable `f` — the candidate's Borel/null-set step is precisely the right response. |
| E8 density of `C_c` in `L^p` | Rudin, book p. 69 | **CONFIRMED**: "3.14 Theorem For `1 ≤ p < ∞`, `C_c(X)` is dense in `L^p(μ)`", under the standing hypotheses "`X` a locally compact Hausdorff space, `μ` a measure … with the properties stated in Theorem 2.14. For example, `X` might be `R^k` and `μ` might be Lebesgue measure on `R^k`." Matches the candidate's E8 sentence word for word in content. |
| E1 Hölder, E7 (Mathlib), E10 (Mathlib) | Mathlib `0df444a`: `MeasureTheory/Integral/Bochner/Basic.lean:1191`, `MeasureTheory/Function/Jacobian.lean:1213`, `Analysis/Fourier/LpSpace.lean:50,132` | **CONFIRMED**: `integral_mul_le_Lp_mul_Lq_of_nonneg` (conjugate exponents), `integral_image_eq_integral_abs_det_fderiv_smul` (`InjOn f s`, `∫_{f''s}g = ∫_s |det f'|•g∘f`), `Lp.fourierTransformₗᵢ` / `fourierInv_toTemperedDistribution_eq`. Grep/statement level, not type-checked (as the candidate says). |
| E12 `P_{≤N}` convention | `cp01-literature-statements.md` §1.4 (Tao 2013 p. 40, eq. (26), verbatim there) | **CONFIRMED** and identical to D1. |
| E13 `lem:bernstein`, E16 functional-lane labels, E18 `lem:lowpass-kernel`/`lem:lp-coincide` | sibling lane files at source | **CONFIRMED**, see §4.2. |

### 4.2 Cross-lane interface re-checked at source (independently of round 1)

`cp02-quotient-functional.md`: `def:quotient` (l. 189, with `G_3`, `F`, `j`,
`Q`, `G_s`, `k_s`), `lem:cubic-frechet` (l. 275) with `eq:cp-F-taylor`
(l. 281) exactly `|F(v+h)-F(v)-⟨j(v),h⟩| ≤ (‖v‖_3+‖h‖_3)‖h‖_3^2`;
`lem:quotient-minimizer` (l. 344) with **(b)** = uniqueness, `A ∈ L^{3/2}`,
`Q = ⅓‖w‖_3^3`, `‖A‖_{3/2} = ‖w‖_3^2` and **(c)** = stationarity — the two
letters the candidate now cites, and (d) is the unrelated invariance;
`lem:leray`(b) (l. 486 ff.) fixing `C_P := ‖P‖_{L^3→L^3}`;
`lem:quotient-coercive` (l. 674) with `eq:cp-coercive` (l. 678) giving both
`‖u‖_3^3 ≤ 3C_P^3Q(u)` and `‖q‖_3 ≤ (1+C_P)‖w‖_3`; `lem:quotient-heat`
(l. 738) with (d) `Q(G_su) ≤ Q(u)`; `lem:quotient-stability` (l. 803) with
`eq:cp-strong` (`‖w'-w‖_3 ≤ 2(‖w‖_3+‖h‖_3)^{1/2}‖h‖_3^{1/2}`) and
`eq:cp-continuity` (l. 816, the `A`-Lipschitz and `Q`-Lipschitz bounds);
`prop:quotient-derivative` (l. 863) with `eq:cp-derivative-remainder`
(l. 871) exactly `≤ 6(‖w‖_3+‖h‖_3)^{3/2}‖h‖_3^{3/2}`. Every citation in
the block matches except the display pointer of §3.

`cp02-lowpressure.md`: `def:lp` (l. 78) carries the Fourier convention, the
`L^2` Plancherel package REPAIR 1 relies on, the Riesz symbols, the
identification `p = R_iR_j(u_iu_j) = -Δ^{-1}∂_i∂_j(u_iu_j)`, and
`S_J := T_{φ(2^{-J}·)}` with `ψ(ξ) = φ(ξ)-φ(2ξ)`, `Δ_j` — so REPAIR 5's
`κ`/`ψ` split is now consistent with `eq:lp-symbol` (l. 104), and the
collision round 1 found is gone. `lem:lp-coincide` (l. 119),
`lem:lowpass-kernel` (l. 205), `lem:bernstein` (l. 491) with
`C_B := ‖∇κ‖_2 = 2π‖|ξ|φ‖_2 ≤ 16π√(2π/5)`, stated for scalar **or
vector-valued** `f ∈ L^2`, with the `C^∞` representative, the Lipschitz
form, and `t ↦ ∇S_Lu(t) ∈ C([0,T];L^∞)` — all as `eq:qe-bernstein` uses
them (see §9.10 for the one notational caveat).

`cp02-local-theory.md`: `prop:localtheory` (l. 1021) as summarised in §2;
its Sobolev norm (l. 150) is **exactly** `eq:qe-sobolev-norm`, and
`lem:embedding` (l. 205 ff.) already proves `‖f̂‖_1 ≤ π‖f‖_{H^2}`,
`sup|F| ≤ π‖f‖_{H^2}`, `sup|∂^αF| ≤ π(2π)^{|α|}‖f‖_{H^m}`, and the
`L^q`-interpolation, with the same constants as `lem:qe-embedding`.

### 4.3 Attempted refutation of `eq:qe-transport` (the deepest step)

I tried to break the transport identity
`⟨A,(u·∇)u⟩ = ⟨A,Du^Tq⟩` rather than to re-read its proof.

**Step 1 (exact pointwise algebra).** With `A_j = |w|w_j`, `w = u+q` and
`T_{ij} := ∂_iu_j`, the symmetry `A_jw_i = |w|w_jw_i = A_iw_j` gives, at
every point,
```
A_j u_i T_{ij} - A_i q_j T_{ij} + A_j q_i T_{ij} = A_i u_j T_{ij} = A_i ∂_i(|u|^2/2),
```
i.e. `⟨A,(u·∇)u⟩ - ⟨A,Du^Tq⟩ + ⟨A,Du\,q⟩ = ⟨A,∇(|u|^2/2)⟩`. Now
`|u|^2/2 ∈ L^3` (from `u ∈ L^6`, (R3)) and `∇(|u|^2/2) = Du^Tu ∈ L^3`, so
the cutoff-and-mollify argument of `lem:quotient-pressure` puts
`∇(|u|^2/2) ∈ G_3` and stationarity (`lem:quotient-minimizer`(c)) kills the
right side. **Hence `eq:qe-transport` is *equivalent* to the hidden identity
`J := ⟨A,(q·∇)u⟩ = ∫A_jq_i∂_iu_j = 0`.** That is not an identity anyone
would guess, so it is a sharp test.

**Step 2 (formal proof that `J = 0`).** Formally, with `q = ∇φ` and
`div A = 0`: `q_i∂_iq_j = q_i∂_i∂_jφ = ∂_j(|q|^2/2)`, so
`∫A_jq_i∂_iq_j = ⟨A,∇(|q|^2/2)⟩ = 0`, whence
`J = ∫A_jq_i∂_iw_j = ∫q_i∂_i(|w|^3/3) = -⅓∫(div q)|w|^3 = -⅓∫(div w)|w|^3`
(using `div u = 0`). And `div A = 0` reads `|w|div w + w·∇|w| = 0`;
multiplying by `|w|^2` and using `∇(|w|^3/3) = |w|^2∇|w|` gives
`∫|w|^3 div w + ∫w·∇(|w|^3/3) = 0`, while integrating the second term by
parts gives `∫w·∇(|w|^3/3) = -⅓∫(div w)|w|^3`; hence
`(2/3)∫(div w)|w|^3 = 0` and `J = 0`. **The identity is true.** Note this
formal route differentiates `w` and `q`, which the candidate is not allowed
to do — so it is a cross-check, not a shortcut (see §7.5).

**Step 3 (numerical test).** Independent 2D spectral test on the torus
(the lemma's proof is dimension-free): random band-limited solenoidal
`u = ∇^⊥ψ`, exact minimisation of `⅓∫|u+∇φ|^3` over all grid `φ` by
L-BFGS with the analytic gradient `-div(|w|w)` (adjoint-exact for spectral
`∇`), spectral derivatives, grid quadrature. Results (`s := ∫|w|^3`,
seed 7, `K = 4`, `‖q‖_3/‖u‖_3 = 0.140`):

| `n` | `I_1/s = ⟨A,(u·∇)u⟩/s` | `I_2/s = ⟨A,Du^Tq⟩/s` | `J/s` | `⟨q,∇(|u|^3/3)⟩/s` |
| --- | --- | --- | --- | --- |
| 48 | 2.1043e-02 | 2.0752e-02 | -2.91e-04 | -2.50e-03 |
| 64 | 2.1089e-02 | 2.1255e-02 | +1.66e-04 | -2.37e-03 |
| 96 | 2.1176e-02 | 2.1163e-02 | -1.30e-05 | -2.47e-03 |
| 128 | 2.1152e-02 | 2.1148e-02 | -4.45e-06 | -2.46e-03 |

`I_1` and `I_2` converge to the same nonzero value (`2.115e-2·s`, so the
identity is not vacuous), their difference `= -J` decays like the
discretisation error (`2.9e-4 → 4.4e-6`), and the *leading term of `J` in
`q`*, `⟨q,∇(|u|^3/3)⟩`, converges to a robust nonzero `-2.46e-3·s` —
so the vanishing of `J` is a genuine cancellation, not a smallness
artefact of `‖q‖_3`. The exact algebra of Step 1 was verified to
`1e-16`-`1e-18` relative residual at every grid, and the stationarity
residual `⟨A,∇(|u|^2/2)⟩/s` was `≤ 6e-7`. Three other seeds and
`K = 3, 6` behave identically. **No refutation; independent confirmation.**

**Second attempted refutation.** I looked for a `b` making the *general*
form of the argument fail. The proof of `lem:quotient-transport` uses `u`
only through: `div b = 0` (volume preservation), `b` bounded with `Db`
bounded and uniformly continuous (`lem:flow`), and `g = Db`-independent
membership `(b·∇)u ∈ L^3 ∩ C_{b,u}`. So it in fact proves
`⟨A,(b·∇)u⟩ = ⟨A,Db^Tq⟩` for every such `b`. Taking `b` a constant vector
(`Db = 0`) yields `⟨A,∂_iu⟩ = 0`, which is independently true because `Q`
is translation invariant (`lem:quotient-scaling` of the functional lane) —
consistent. Taking `q = 0` (`div(|u|u) = 0`) yields
`∫|u|u_jb_i∂_iu_j = ∫b·∇(|u|^3/3) = 0` by `div b = 0` — consistent, and
this reproduces round 1's degenerate check. No inconsistency found.

### 4.4 Repairs and minor items of round 1, checked one by one

R1 applied and re-sourced (§3); R2 `(b) → (c)` in `lem:quotient-pressure`
(l. 251 of the block) ✓; R3 both occurrences now
`lem:quotient-stability`/`eq:cp-continuity` (block ll. 307, 976) ✓ (with the
display caveat of §3); R4 `(a) → (b)` (l. 1058) and every `‖P‖` replaced by
`C_P` (only l. 76 keeps `C_P = ‖P‖_{L^3→L^3}` as the definition pointer to
`lem:leray`(b)) ✓, `M_L` and `eq:qe-M` as prescribed ✓; R5 the `κ_L`
paragraph verbatim, `ψ` used only for the homogeneous symbol, componentwise
reassembly deleted ✓. M1 `eq:qe-sobolev-norm` ✓; M2 all three remainder
uses now go through `eq:cp-derivative-remainder` ✓; M3 ✓; M4 "(R1)--(R3)" ✓;
M5 `def:qe-dissipation` ✓; M6 ✓; M7 `lem:heat-generator` and
`eq:qe-cutoff-error` are both referenced now (label/reference diff: only the
six remark labels and the four subsection labels are unreferenced, which is
intended) ✓; M8 all remarks titled and labelled ✓; M9 noted, `adj` inline ✓;
M10 `eq:qe-frobenius` displayed ✓; M11 `θ ∈ [0,1]` stated once, in the
hypothesis ✓; M12 four subsections ✓; M13 ✓. `Teschl2012` and the
corroboration remark are gone (grep: zero hits) ✓.

### 4.5 Compile and self-containedness

Block extracted verbatim (1179 lines), stub preamble written here from
scratch, `latexmk -pdf` twice: exit 0, `grep -c undefined` = 0,
`grep -c Overfull` = 0. The set of externally owned labels is exactly
`def:lp, def:quotient, def:target, eq:cp-coercive, eq:cp-continuity,
eq:cp-derivative-remainder, eq:cp-F-taylor, eq:missing, eq:NS, hyp:critical,
hyp:highpressure, lem:bernstein, lem:cubic-frechet, lem:leray,
lem:lowpass-kernel, lem:lp-coincide, lem:quotient-coercive,
lem:quotient-heat, lem:quotient-minimizer, lem:quotient-stability,
prop:energy, prop:localtheory, prop:pressure, prop:quotient-derivative,
thm:conditional, thm:continuation` — all of which exist in the drafted
lanes or the manuscript (each verified at source). No reference to any
evidence file is used as proof inside the block (grep for `hf1`, `evidence`,
`research/`, `.md`: zero hits). D1 (conventions, `S_L = P_{≤2^L}`), D2
(package (R), no preserved Schwartz decay), D4 (label list), D5 (external
facts sourced with `[DI]`/`[MO]`) are all respected.

---

## 5. REPLACEMENT ARGUMENT

Not required (verdict PASS). For the integrator's convenience, the seven
one-clause insertions of §9 that a strict D5 reading wants, and the one
display-pointer fix, are collected here as **editorial** replacements. They
change no statement, no constant, and no dependency.

```latex
%%% E1 (display pointer).  In prop:quotient-evolution, continuity paragraph:
%%%   "$q(t)=w(t)-u(t)$ is continuous into $L^3$ by
%%%    Lemma~\ref{lem:quotient-stability}, estimate \eqref{eq:cp-continuity},"
%%% becomes
%%%   "$q(t)=w(t)-u(t)$ is continuous into $L^3$ by
%%%    Lemma~\ref{lem:quotient-stability}, estimate \eqref{eq:cp-strong},"
%%% (the occurrence in lem:quotient-chainrule Step 3, which is about
%%% $A\in C_tL^{3/2}$, correctly stays with \eqref{eq:cp-continuity}).

%%% E2 (vector-valued embedding).  In the statement of lem:qe-embedding,
%%% replace "Let $f\in H^2(\R^3)$" by
%%%   "Let $f\in H^2(\R^3;\R^N)$, $N\ge1$"
%%% and add after the first Cauchy--Schwarz display:
%%%   "Here $|\hat f|$ is the Euclidean norm of the vector $\hat f(\xi)$, so
%%%    the estimate is the componentwise one summed as in
%%%    \eqref{eq:qe-sobolev-norm}."

%%% E3 (matrix-field $L^r$ norms).  In the notation paragraph, after
%%% "For a matrix field, $\norm{M}_\infty=\sup_x|M(x)|$", add:
%%%   "and $\norm M_r:=\bigl(\int_{\R^3}|M(x)|^r dx\bigr)^{1/r}$ for
%%%    $1\le r<\infty$, with $|\cdot|$ the operator norm; by
%%%    \eqref{eq:qe-frobenius} the Frobenius norm gives an equivalent
%%%    quantity."

%%% E4 (uniform continuity in lem:heat-generator).  In Step 4, replace
%%%   "applied to the bounded uniformly continuous $f$"
%%% by
%%%   "applied to $f$, which is bounded and, by the mean value inequality
%%%    $|f(x)-f(y)|\le\norm{\nabla f}_\infty|x-y|$, uniformly continuous"

%%% E5 (vector-valued density of $C_c$).  At both uses
%%% (lem:qe-heat-continuity(b) and lem:quotient-transport Step 4), replace
%%%   "(density of $C_c$ in $L^3$ \cite[Thm.~3.14]{Rudin1987})"
%%% by
%%%   "(density of $C_c$ in $L^3$ \cite[Thm.~3.14]{Rudin1987}, applied on
%%%    the locally compact Hausdorff space $\R^3\times\{1,2,3\}$ with the
%%%    product of Lebesgue and counting measure, whose $L^3$ is
%%%    $L^3(\R^3;\R^3)$ with an equivalent norm and whose compactly
%%%    supported continuous functions are the triples of elements of
%%%    $C_c(\R^3)$)"

%%% E6 (null sets in lem:qe-pullback(a)).  After
%%%   "so $f\circ\Phi$ depends only on the equivalence class of $f$"
%%% insert
%%%   "(every Lebesgue null set is contained in a Borel null set, so
%%%    $|\Phi^{-1}(N)|=0$ for every Lebesgue null $N$)"

%%% E7 (pointer for "solenoidal").  In the paragraph after
%%% lem:qe-embedding, replace
%%%   "solenoidal in the sense of Definition~\ref{def:quotient}"
%%% by
%%%   "solenoidal, i.e.\ $\int u(t)\cdot\nabla\phi\,dx=0$ for every
%%%    $\phi\in C_c^\infty(\R^3)$:"
%%% (the definition of "solenoidal" lives in the functional lane's notation
%%% paragraph, not inside Definition~\ref{def:quotient}).

%%% E8 (scope of $D_{\mathcal Q}$ and $K_L$).  At the end of
%%% def:qe-dissipation add:
%%%   "Since $T<T_*$ is arbitrary, $D_{\mathcal Q}(u(t))$ is defined for
%%%    every $t\in[0,T_*)$, and likewise for $K_L$ in
%%%    Lemma~\ref{lem:quotient-lowstrain}."
%%% and in hyp:highstrain, after "divergence-free Schwartz datum $u_0$",
%%% add "(with $(u,p)$ and $T_*$ the branch of that datum)".
```

An optional, larger simplification is §7.1: delete `lem:qe-embedding` and
cite the local-theory lane's `lem:embedding`. That would also delete the
`def:lp`/Grafakos dependence from this lane and close §4 items 1-2 of the
candidate outright. It is a choice for the integrator, not a defect.

---

## 6. CONDITIONAL SUFFIX THAT SURVIVES

Unchanged from round 1, and now audited twice. Unconditionally, for the
unforced equation on `R^3`, every `ν>0`, every divergence-free
`u_0 ∈ S(R^3)^3`, the maximal classical branch of `prop:localtheory`, and
every compact `[0,T] ⊂ [0,T_*)`:

1. `p(t), ∇p(t) ∈ L^3`, `∇p(t) ∈ G_3`, hence `DQ(u(t))[∇p(t)] = 0` (Q-8, Q-9);
2. `t ↦ Q(u(t)) ∈ C^1([0,T])` with
   `d/dt Q(u(t)) = ν⟨A,Δu⟩ - ⟨A,(u·∇)u⟩` (Q-10);
3. `D_Q(u(t)) = -⟨A(t),Δu(t)⟩ ≥ 0`, continuous in `t` (Q-11);
4. `∫A·((u·∇)u) = ∫q·((A·∇)u)` (Q-12 .. Q-16), hence the pressure-free,
   minimizer-derivative-free identity `eq:quotient-evolution` with
   continuous right side;
5. `|K_low(t)| ≤ M_L Q(u(t))`, `M_L = 3(1+C_P)C_B2^{5L/2}‖u_0‖_2` (Q-17).

Conditionally, and only conditionally:

6. `hyp:highstrain` (`eq:quotient-gap`) ⇒ `hyp:critical` with
   `M(ν,u_0,H) = C_P(‖u_0‖_3^3+3A_input)^{1/3}e^{M_LH/3}`, hence, by
   `thm:conditional`, ⇒ `def:target` (Q-18).

Items 1-6 are independent of every editorial item in §5 and §9.

---

## 7. UNNECESSARY DEPENDENCIES

1. **`lem:qe-embedding` is largely redundant.** The local-theory lane's
   `lem:embedding`(a),(b),(c) proves `‖f̂‖_1 ≤ π‖f‖_{H^2}`,
   `sup|F| ≤ π‖f‖_{H^2}`, `sup|∂^αF| ≤ π(2π)^{|α|}‖f‖_{H^m}` (with the
   classical/distributional identification) and the `L^q` interpolation,
   under exactly the norm `eq:qe-sobolev-norm`. Only the
   *uniform*-continuity clause is new here, and even that can be had from
   `|f(x)-f(y)| ≤ ‖∇f‖_∞|x-y|` for `f ∈ H^3` — which covers every use in
   the block (`u`, `Du`, `D^2u`, `Δu`, `g = Du\,u`). Collapsing this
   removes E10, the `def:lp` dependence, and the Grafakos citation from
   this lane.
2. **The candidate's §4 items 1 and 2 are stale.** The local-theory lane
   already fixes `‖f‖_{H^s} = (∫(1+|ξ|^2)^s|f̂|^2dξ)^{1/2}` (its notation
   paragraph) and owns the classical/weak identification; and `def:lp` is
   integrated by the low-pressure lane. Neither is an open seam.
3. **`\cite[Thm.~7.26]{Rudin1987}` and `\cite[Thm.~3.14]{Rudin1987}`
   duplicate the Mathlib E7/E8 entries.** For a paper the textbook citation
   is the right one to keep; the Mathlib lines are Lean-lane bookkeeping.
4. `lem:qe-jacobi`'s adjugate identity is used only through
   `tr(adj(M)M') = (tr B)det M`, which the text proves; no linear-algebra
   citation is needed.
5. **Not removable, and worth a remark:** the flow apparatus
   (`lem:qe-jacobi`, `lem:flow`, `lem:qe-pullback`) cannot be replaced by
   the formal computation of §4.3 Step 2, because that computation
   differentiates `w` and `q`. `rem:qe-transport-scope` says no derivative
   of the minimizer is used; a half-sentence recording *why* a shorter
   route is unavailable ("the formal identity
   `∫(div w)|w|^3 = 0` equivalent to \eqref{eq:qe-transport} presupposes
   derivatives of `w`, which are not available") would pre-empt the obvious
   referee question.

Dependencies that are necessary and correctly used: `prop:energy`,
`lem:quotient-coercive` (both directions), `lem:quotient-minimizer`(b),(c),
`lem:quotient-stability`, `lem:cubic-frechet`, `lem:quotient-heat`,
`prop:quotient-derivative`, `lem:bernstein`, `def:lp`, `prop:localtheory`,
`hyp:critical`, `thm:conditional`, `thm:continuation`.

---

## 8. NON-CLAIMS (checked as retained, and asserted here too)

Verified retained **verbatim** in version 2 by string comparison against
the manuscript: "Its sign follows by differentiating the heat contraction
at zero; `$\Delta u\in L^3$` justifies this generator limit."; "No
quantitative comparison with the original cubic dissipation is claimed.";
"Integration of \eqref{eq:quotient-evolution} and Gronwall would then bound
`$\mathcal Q$`, hence `$L^3$`, through the putative endpoint"; "Neither
\eqref{eq:quotient-gap} nor a quantitative dissipation mechanism for it has
been proved."; "This is an alternative to the pressure route; no novelty or
Millennium solution is asserted."

This review asserts, and the audited text asserts, none of the following:
no proof of `eq:quotient-gap` / `hyp:highstrain`; no sign, bound, or
dissipation mechanism for `K_L`; no quantitative comparison of `D_Q` with
`D_3` and no coercive lower bound for `D_Q` in any norm of `u`; no
smoothness or regularity of the minimizer `q` or of `w`; no HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3 result; no continuation bound;
no regularity theorem; no novelty claim for the quotient construction; no
solution of the Navier-Stokes Millennium problem.
`prop:quotient-conditional` is a conditional implication only, and
`rem:highstrain-scope` correctly records that at its quantifiers
`hyp:highstrain` is *equivalent* to global continuation, so it supplies no
method.

Status caveats carried forward: the Mathlib statements were read in the
`0df444a` checkout but not type-checked; `prop:localtheory` (package (R)) is
an assumed lane interface, verified against `cp02-local-theory.md` but not
re-audited here; the numerical experiment of §4.3 is a consistency test on
a 2D torus, not a proof, and is used only as a refutation attempt.

---

## 9. MINOR EDITORIAL ISSUES FOR THE INTEGRATOR

1. **`lem:qe-embedding` is stated for scalar `f ∈ H^2(R^3)`** but applied to
   the vector fields `u(t), ∇u(t), ∇^2u(t), Δu(t), u_t(t), ∇p(t)`. One
   clause fixes it (§5 E2).
2. **Matrix-field `L^r` norms are never defined**, although `‖Du-Dv‖_3`,
   `‖∇u‖_3`, `‖Du‖_∞` are used (paragraph after `lem:qe-embedding`,
   `lem:quotient-transport`'s absolute-convergence display). §5 E3.
3. **`lem:heat-generator` uses uniform continuity of `f`**, which follows
   from `‖∇f‖_∞ < ∞` but is not said. §5 E4.
4. **Density of `C_c` is quoted in scalar form** (Rudin Thm. 3.14) and used
   for `R^3`-valued fields, twice. §5 E5. (The functional lane's
   product-measure device makes the citation literally applicable.)
5. **Wrong display pointer** in `prop:quotient-evolution`: `L^3` continuity
   of `u ↦ w` is `eq:cp-strong`, not `eq:cp-continuity`. §5 E1. This is the
   only surviving instance of round 1's citation-precision defect class.
6. **`lem:qe-pullback`(a)** proves the null-set step for Borel null sets;
   the equivalence-class claim needs Lebesgue null sets. §5 E6.
7. **"solenoidal in the sense of Definition~\ref{def:quotient}"** points at
   the wrong place: the definition is in the functional lane's notation
   paragraph. §5 E7.
8. **`def:qe-dissipation` is stated on `[0,T]`** while `hyp:highstrain` and
   `eq:quotient-gap` use `D_Q(u(t))` and `K_L(t)` on `[0,T_*)`. §5 E8.
9. **`hyp:highstrain` re-quantifies over `(ν,u_0,H)`** while `u`, `T_*`,
   `q(t)`, `A(t)` are fixed by the standing convention of
   `subsec:qe-trajectories`. §5 E8 (second half). The manuscript's
   `hyp:highpressure` has the same looseness for `Q_J`; harmonise both.
10. **`lem:bernstein` vs `eq:qe-bernstein`**: the low-pressure lane states
    `‖∇S_Lf‖_∞ ≤ C_B2^{5L/2}‖f‖_2` while this lane restates it as
    `sup_x|∇S_Lf(x)|_F ≤ …`. The two agree by that lemma's proof (which
    computes `Σ_{k,m}|∂_k(κ_L*f_m)(x)|^2`), but the Frobenius norm should be
    explicit in `lem:bernstein` so the integrated text is unambiguous.
11. **`rem:qe-heatsign-scope` opens with "Its sign follows …"**, whose
    antecedent is now in the preceding lemma rather than in the remark. The
    sentence must stay verbatim (non-claim), so add a lead-in such as
    "Concerning Lemma~\ref{lem:quotient-heatsign}:".
12. **Six remark labels and four subsection labels are never referenced**
    (`rem:qe-*`, `subsec:qe-*`). Harmless; keep them only if the structural
    verifier counts them.
13. **Integrator actions the candidate lists are correct and still needed**:
    add `\newtheorem{lemma}[theorem]{Lemma}` and
    `\newtheorem{definition}[theorem]{Definition}`; **delete the
    manuscript's existing `eq:quotient-gap` display** (otherwise the label
    is defined twice) together with its `θ ≤ 1` annotation; add `Rudin1987`
    to `references.bib` (`Grafakos2014` is shared). The `bibtex` entries in
    the candidate's §3 are well formed.
14. **Cross-lane collision to check at integration** (not created by this
    lane): `q` is the minimizer here and the `ν`-normalised pressure in
    `eq:nu-normalization`; `S_J` (low-pressure) vs `S_L` (here). Both need
    a decision in the integrated section.

---

## 10. REOPENING CONDITION

Round 1's eight conditions all stand. In addition, this audit must be
reopened if:

9. **The local-theory lane changes its Sobolev norm or drops
   `lem:embedding`.** §4.2's verification that (R1) is derivable from
   `prop:localtheory`(iii) uses `lem:sobolev-norms` and `lem:embedding`(b)
   of that lane; the constant `π` in `eq:qe-embedding` and `4π^3` in the
   paragraph after it are tied to the norm `eq:qe-sobolev-norm`.
10. **`lem:quotient-stability`'s display numbering changes.** §5 E1 is keyed
    to `eq:cp-strong` (the `w`-continuity) versus `eq:cp-continuity` (the
    `A`- and `Q`-Lipschitz bounds).
11. **`lem:bernstein`'s norm convention changes** (operator versus Frobenius,
    or a different `φ` normalisation): `eq:qe-bernstein`, `M_L` and
    `eq:qe-M` all move.
12. **Anyone proposes to shorten Q-12 .. Q-16 using the formal identity of
    §4.3.** That derivation differentiates the minimizer and is therefore
    not admissible as a proof; the flow route must stay.

---

## 11. NEXT DISTINCT ACTION

Controller integration, in this order: (i) apply the eight editorial
insertions of §5 (or, preferably, §7.1 first, which removes three of them);
(ii) update the candidate's §4 items 1-2 to "closed" (§7.2); (iii) splice
the functional lane's first half, this lane's second half, and the
low-pressure lane's `def:lp` / `lem:bernstein` into `sec:quotient` and
`prop:lowpressure`, adding the two `\newtheorem` lines and deleting the
manuscript's duplicate `eq:quotient-gap` display; (iv) re-run the
structural verifier on the D4 label list; (v) audit the *integrated*
section for the cross-lane notation collisions of §9.14 — that, and not
this lane, is where the remaining integration risk lives. `hyp:highstrain`
(`eq:quotient-gap`) remains the first gap and is untouched by all of the
above.

---

## 12. Frontier record

**MODE / RESULT.** REVIEW (proof audit, round 2) of
`cp02-quotient-evolution.md` version 2. **VERDICT PASS.** No invalid step;
round 1's first bad bridge closed and its replacement citation verified at
the source; all five REPAIRs and thirteen minor items applied; all four
textbook facts (Grafakos Thm. 1.2.10 p. 21 and §2.2.4 pp. 113-114; Rudin
Thms. 3.14 p. 69 and 7.26 pp. 153-154) opened here and confirmed to support
exactly the statements they carry, so every `[DI]` in the block is correct;
the transport identity independently confirmed by exact algebra, a formal
proof of the equivalent hidden identity `⟨A,(q·∇)u⟩ = 0`, and a converging
2D spectral experiment. Fourteen minor editorial issues, eight of them with
ready insertion text.

**CLAIM AND SCOPE.** This review claims only that the audited block proves
Q-8 .. Q-18 and `eq:quotient-evolution` at the D5 standard for the original
unforced equation on `R^3`, arbitrary `ν>0`, divergence-free Schwartz data,
the maximal classical branch of `prop:localtheory`, and every compact
`[0,T] ⊂ [0,T_*)`; and that `hyp:highstrain ⇒ hyp:critical ⇒ def:target`
with the explicit constant `C_P(‖u_0‖_3^3+3A_input)^{1/3}e^{M_LH/3}`. No
decay of `u(t)` in `x` beyond `H^k` membership is used anywhere.

**EVIDENCE.** §§2, 4: bridge-by-bridge reconstruction with every constant
recomputed (`π`, `π^2`, `4π^3`, `¼e^{1/4}<½`, `2|N|`, `2|N|^2`,
`Λ|s|e^{Λ|s|}`, `2^{5L/2}`, `C_B ≤ 16π√(2π/5)`, `M_L`, `M_LH/3`); four
textbook sources opened as text; three Mathlib lines re-opened at `0df444a`;
all 26 external labels verified in the sibling lane files; independent
compile (exit 0, 0 undefined, 0 overfull); refutation attempt (§4.3) failed
in three separate ways.

**FIRST GAP.** Unchanged: Hypothesis `hyp:highstrain` (`eq:quotient-gap`),
a signed, input-only, finite-horizon bound for `∫_0^τ K_L` uniform up to
`min{H,T_*}`. Within the lane's deliverable, no open seam remains: the two
integration items the candidate lists are closed by the local-theory and
low-pressure lanes.

**SURVIVING CONDITIONAL SUFFIX.** §6, items 1-5 unconditionally, item 6
conditionally.

**NON-CLAIMS.** §8.

**NEXT DISTINCT ACTION.** §11.
