# CP02 audit (round 1): review of `cp02-quotient-functional.md` (Q-0 … Q-7)

MODE / RESULT: **REVIEW — VERDICT: PASS** (no invalid bridge found; a list of
editorial and integration fixes is attached).  Lane: audit of CP02-6.
Date 2026-09-05.  Nothing in this note proves `eq:quotient-gap`; HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL, ABSORPTION and NS-R3 remain open and are not asserted
here, and the reviewed note asserts none of them either.

## 0. Freeze

| Item | Value |
| --- | --- |
| Candidate file | `../navier/research/evidence/cp02-quotient-functional.md` |
| `sha256sum` of candidate | `2963d31a3faa6d176b80f7ff5295ae780c9399aa7ee13664f6640fb8d014fb84` |
| `git -C ../navier rev-parse HEAD` | `715ce84ec78d64c510e150360a354b5d55648b9c` |
| Manuscript audited against | `../navier-paper/main.tex`, HEAD `1ad73c2960ed5bc28958ce063b637fa28f603642`, `sha256(main.tex) = 2b2c072f0e461c5abb94d11430bdc2f4940dc4c3e2a93c999071e07a22c40012` |
| Records read in full | `cp01-manuscript-obligations.md` (§1.14 Q-0…Q-18), `cp01-literature-statements.md` (§1.4, §6, §7, §8) |

The candidate's own summary was treated as untrusted and was not used as
evidence for any step; every proof below was reconstructed from its first
nontrivial implication.

## 1. Reviewed scope

The whole LaTeX block of §2 of the candidate (40 745 characters), i.e. the
replacement text for the opening of `sec:quotient` through
`rem:quotient-scope`:

`subsec:quotient-conventions` (conventions; imported facts F1–F5),
`def:quotient`, `lem:cubic-pointwise` (eq:cp-lipschitz, eq:cp-taylor,
eq:cp-monotone, eq:cp-strict), `lem:cubic-frechet` (eq:cp-F-taylor,
eq:cp-F-lipschitz, eq:cp-F-monotone), `lem:density`,
`lem:quotient-minimizer`(a)–(d), `lem:gradient-closure`, `lem:leray`(a)–(d)
(eq:cp-sol-fourier, eq:cp-duality, eq:cp-gradient-rep), the sign remark on
Tao p. 38, `lem:quotient-coercive` (eq:cp-coercive), `lem:quotient-scaling`,
`lem:quotient-heat` (eq:cp-heat) and its remark, `lem:quotient-stability`
(eq:cp-contraction, eq:cp-strong, eq:cp-continuity),
`prop:quotient-derivative` (eq:cp-derivative, eq:cp-derivative-remainder),
`rem:quotient-scope`.

Also reviewed: consistency with D1–D5; the retained tail of `sec:quotient`
after the splice point; the label interface to the other lanes; the
candidate's source table; the candidate's compile claim.

Not in scope (and correctly declared out of scope by the candidate): Q-8 …
Q-18, `eq:quotient-evolution`, `eq:quotient-gap`, the pullback half of the
CP01 draft's `lem:gradient-closure`.

## 2. FIRST BAD BRIDGE

**None.**  Every implication in the reviewed block was reconstructed and
holds as written, with the quantifiers, function spaces and constants as
stated.  In particular the four steps flagged by the lane brief as the
hard ones check out:

* `lem:quotient-minimizer`(a): the product-measure detour is *necessary and
  correct*.  Brezis's `L^p` is a space of **real scalar** functions
  (Ch. 4 opening, p. 89: "integrable functions from Ω into R"), so
  Theorem 4.10 cannot be applied to `L^3(R^3;R^3)` directly; the candidate
  identifies `L^3(R^3;R^3)` with `L^3` of Lebesgue × counting measure on
  `{1,2,3}` (σ-finite, matching Brezis's standing assumption (iii)) and
  transfers weak convergence through norm equivalence.  Both norm-equivalence
  constants were recomputed: `‖v‖_X^3 ≤ 3‖v‖_3^3` (from `|v_i| ≤ |v|`) and
  `‖v‖_3^3 ≤ 9‖v‖_X^3` (from `(a_1+a_2+a_3)^3 ≤ 9Σa_i^3`, i.e. convexity of
  `t ↦ t^3`, constant `27·(1/3) = 9`) — both correct.  Prop. 3.5(iii) is then
  applied in `(L^3(R^3;R^3),‖·‖_3)`, which is legitimate because that space
  is Banach and has the same dual as `X`.
* `lem:leray`(d) Steps 2–3: correct, and the choice of estimate is the
  one that works.  With `g(ξ) = (ξ·ψ̂)/(2πi|ξ|²)` one has
  `|g| ≤ |ψ̂|/(2π|ξ|)`, which is in `L^1 ∩ L^2` near `ξ = 0` **because**
  `∫_{|ξ|≤1}|ξ|^{-2}dξ < ∞` in `R^3`; this is exactly what makes
  `Φ = ǧ ∈ C^∞ ∩ L^2` and hence makes the cutoff error
  `‖Φ∇χ_R‖_{3/2} ≤ ‖∇χ_R‖_6‖Φ‖_2 = R^{-1/2}‖∇χ‖_6‖Φ‖_2 → 0` available
  (Hölder `2/3 = 1/6 + 1/2` ✓; `‖∇χ_R‖_6 = R^{-1}·R^{1/2}‖∇χ‖_6 = R^{-1/2}‖∇χ‖_6` ✓).
  No decay of `u` is used anywhere, only `u ∈ L^3`; the argument therefore
  covers solenoidal `L^3` fields that are not in `L^2` (which is the point of
  Q-4).  Note in passing that the same construction fails in `R^2`
  (`|ξ|^{-2}` is not locally integrable there); the lemma is stated on `R^3`,
  so this is a scope remark, not a defect.
* `prop:quotient-derivative`: the two-competitor argument (`w+h` admissible
  for `u+h`, `w'-h = u + q(u+h)` admissible for `u`) is correct, and the
  remainder bookkeeping is correct: upper bound `(‖w‖+‖h‖)‖h‖²`; lower bound
  `⟨A'-A,h⟩ - (‖w‖+2‖h‖)‖h‖²`; then `|⟨A'-A,h⟩| ≤ 4(‖w‖+‖h‖)^{3/2}‖h‖^{3/2}`,
  `‖w‖+2‖h‖ ≤ 2(‖w‖+‖h‖)` and `‖h‖^{1/2} ≤ (‖w‖+‖h‖)^{1/2}` give
  `4 + 2 = 6`.  The remainder is `o(‖h‖_3)` because `‖h‖^{3/2}/‖h‖ → 0`.
* `lem:quotient-stability`: the cancellation
  `⟨A'-A, w'-w⟩ = ⟨A'-A, h⟩` uses `w'-w = h + (q(u+h)-q(u))` with
  `q(u+h)-q(u) ∈ G_3` and stationarity of **both** minimizers; both pairings
  are finite (`A, A' ∈ L^{3/2}`, `w'-w ∈ L^3`).  The division by `‖w'-w‖_3`
  is guarded by the trivial case `w' = w`.

Every Hölder/Cauchy–Schwarz exponent was recomputed independently:
`‖j(v)‖_{3/2} = ‖v‖_3²` (from `∫|j(v)|^{3/2} = ∫|v|^3`); `∫(|v|+|h|)|h|² ≤
‖|v|+|h|‖_3‖|h|²‖_{3/2}` with `1/3 + 2/3 = 1`; `∫(|v|+|v'|)^{3/2}|v-v'|^{3/2}
≤ (∫(|v|+|v'|)^3)^{1/2}(∫|v-v'|^3)^{1/2}` and the outer power `2/3`;
`∫(|w|+|g|)²|g| ≤ ‖|w|+|g|‖_3²‖g‖_3` with `2/3 + 1/3 = 1`; the heat
contraction split `k_s = k_s^{2/3}·k_s^{1/3}` with exponents `3/2, 3` giving
constant `‖k_s‖_1^{2/3} = 1`; `‖∇χ_R‖_∞ = R^{-1}‖∇χ‖_∞` and
`‖∇χ_R‖_6 = R^{-1/2}‖∇χ‖_6`.  All correct.

Integration by parts / limits on `R^3` with decay: the block never integrates
by parts against a non-compactly-supported test object without a stated
cutoff and a quantified cutoff error (`lem:gradient-closure`,
`lem:leray`(a) Schwartz extension, `lem:leray`(d) Step 3).  No preserved
Schwartz decay in time is assumed anywhere (D2 respected); indeed no
Navier–Stokes solution enters the block at all except in the scope remark.

Use of the regularity package R: the only use is `rem:quotient-scope`'s
sentence that `u(t)` of `prop:localtheory` lies in `L^2 ∩ L^3` and is
solenoidal.  Legitimate under D2 (`u ∈ C([0,T];L^q)` for `2 ≤ q ≤ ∞`,
`div u = 0`), and it is used only to say which hypotheses of
`lem:quotient-coercive` hold — no time regularity, no decay, no pressure
property is invoked.

Hidden circularity: none.  (F5) is stated as a property of the operator
defined in `lem:leray`(a), and `lem:leray`(a) is proved without (F5); the
`L^3`/`L^{3/2}` extension in (b) is the only consumer of (F5).  `lem:leray`(d)
uses (b), not (d).  No lemma in the block cites `prop:quotient-derivative` or
anything downstream of it.

Self-containedness of the LaTeX: the block cites only `Tao2013`, `Brezis2011`,
`Stein1970`, `Grafakos2014` and its own labels plus `prop:localtheory`; it
never refers to an evidence file, an HF note, or "the lane" as a proof.  ✓

## 3. Refutation attempts (all failed)

1. **Sharpness/validity of the monotonicity constant `1/2`
   (eq:cp-monotone).**  Tried to break `(j(a)-j(b))·(a-b) ≥ ½|a-b|³`.  The
   displayed identity `(|a|+|b|)(½(|a|-|b|)² + ½|a-b|²)` was verified
   symbolically and on the extreme configurations: at `b = -a` it gives
   `4|a|³ = ½|a-b|³`, so the constant `1/2` is attained and cannot be
   improved — the inequality is exactly sharp, not merely true.  No
   counterexample.
2. **Strict convexity (eq:cp-strict) equality case.**  Tried `a ≠ b` with
   `|a| = |b|` and `a·b` near `|a||b|`.  The two-step chain
   `|(a+b)/2|³ ≤ ((|a|+|b|)/2)³ ≤ ½(|a|³+|b|³)` forces
   `(|a|+|b|)(|a|-|b|)² = 0` and then Cauchy–Schwarz equality with equal
   norms, hence `a = b`.  No counterexample.
3. **Randomised numerical search in `R^3`** over 400 000 triples `(a,b,h)`
   with amplitudes spread over `10^{-3}…10`: max violation of
   eq:cp-lipschitz `-3.6e-11`, eq:cp-taylor `-2.1e-12`, eq:cp-monotone
   `-1.5e-12`, eq:cp-strict `-8.7e-13`; relative error of the eq:cp-monotone
   identity `2.1e-15`.  All four inequalities hold; the identity is exact.
4. **Finite-dimensional analogue of the whole quotient construction**
   (counting measure: `R^{3n}`, `n = 6`, `F(v) = ⅓Σ_i|v_i|³` with Euclidean
   blocks, `G` a random 7-dimensional subspace; minimiser computed by
   L-BFGS-B from several starts, 30 base points × 3 increment scales).  Tested
   the exact inequalities of the note.  Results: stationarity residual
   `‖G^T j(w)‖_∞ ≤ 1.8e-7` (optimiser tolerance); **no violation** of
   eq:cp-derivative-remainder (worst ratio `remainder/‖h‖^{3/2} = 0.82`
   against the claimed bound `6(‖w‖+‖h‖)^{3/2}`), of eq:cp-strong, or of the
   `|Q(u+h)-Q(u)| ≤ (‖w‖+‖h‖)²‖h‖` bound.  Independent consistency check of
   derivative + stationarity + cubic homogeneity via the Euler identity
   `⟨A(u),u⟩ = 3Q(u)`: relative error `2.9e-9`.  (This identity is a
   nontrivial cross-check: it holds only if `D𝒬(u)[h] = ⟨A,h⟩`, `⟨A,q⟩ = 0`
   and `𝒬(αu) = |α|³𝒬(u)` are simultaneously right.)
5. **Attempt to defeat `lem:leray`(d) with a solenoidal `u ∈ L^3 \ L^2`**
   (slowly decaying solenoidal field).  The proof survives: `u` is only ever
   paired against sequences converging in `L^{3/2}`, and all decay
   requirements fall on the potential `Φ` built from the compactly supported
   test field `ψ`.  No counterexample.
6. **Attempt to find a sign/normalisation error from D1's `2π` convention.**
   Recomputed: `F(∂_jφ) = 2πiξ_jφ̂` under `e^{-2πix·ξ}` ✓; symbol of
   `f_i + R_iR_jf_j` with `R̂_j = -iξ_j/|ξ|` is `δ_{ij} - ξ_iξ_j|ξ|^{-2}` ✓
   (the product of two Riesz symbols is sign-insensitive, so the (F5)
   identification survives either Riesz sign convention).  Independently
   recomputed Tao's printed `Pu := Δ^{-1}(∇×∇×u)` with his (14) multiplier
   `-(4π²|ξ|²)^{-1}`: `F(∇×∇×u) = 4π²|ξ|²Π(ξ)û`, so the printed formula gives
   `-Π`, i.e. the candidate's sign remark is **correct** (and Tao's own
   following sentence "`if u is square-integrable and divergence-free, then
   Pu = u`" confirms the printed formula carries a typo, not the operator).

## 4. Evidence

**Source verification (all [DI] claims of the candidate were re-fetched).**

| Fact | Candidate's claim | What I found | Status |
| --- | --- | --- | --- |
| F5 (Leray `L^p`) | Tao 2013 p. 38, verbatim | arXiv:1108.1165 e-print source (`local_ns.tex`) fetched and read: "We define the *Leray projection* `Pu` … by the formula `Pu := Δ^{-1}(∇×∇×u)`. If `u` is square-integrable, then `Pu` is the orthogonal projection of `u` onto the space of square-integrable divergence-free vector fields; from Calder\'on-Zygmund theory we know that the projection `P` is bounded on `L^p_x(R^3)` for every `1 < p < ∞`, …" | **[DI] confirmed verbatim** |
| Tao (14) | `Δ^{-1}` multiplier `-(4π²|ξ|²)^{-1}` | same source, `\label{fax}`: `\widehat{Δ^{-1}f}(ξ) := (-1/4π²|ξ|²) f̂(ξ)` | **[DI] confirmed** |
| Tao p. 39 | Gaussian heat kernel + Young | same source: `e^{tΔ}f(x) = (4πt)^{-3/2}∫e^{-|x-y|²/4t}f(y)dy` for `f ∈ L^p`, `1 ≤ p ≤ ∞`; "From Young's inequality we thus record the dispersive inequality" (18) | **[DI] confirmed** |
| F1(i) | Brezis Thm 4.10, p. 95 | Brezis PDF p. 95: "• **Theorem 4.10.** `L^p` is reflexive for any `p`, `1 < p < ∞`." | **[DI] confirmed** |
| F1 standing hypothesis | σ-finiteness, Ch. 4 opening p. 89 | p. 89, item (iii): "`Ω` is σ-finite, i.e. there exists a countable family `(Ω_n)` in `M` such that `Ω = ∪Ω_n` and `μ(Ω_n) < ∞ ∀n`" ("even though this is not essential") | **[DI] confirmed** |
| F1(ii) | Brezis Thm 3.18 | pp. 69–70: Thm 3.18 is the direct Eberlein–Šmulian statement (bounded sequences in a reflexive space have weakly convergent subsequences); Thm 3.19 is its converse, Remark 17 discusses "Theorems 3.17, 3.18, and 3.19" | **[DI] confirmed** (statement straddles pp. 69–70, see minor issue M10) |
| F2(i) | Brezis Thm 3.7, p. 60 | p. 60: "• **Theorem 3.7.** Let `C` be a convex subset of `E`. Then `C` is closed in the weak topology `σ(E,E')` if and only if it is closed in the strong topology." | **[DI] confirmed verbatim** |
| F2(ii) | Brezis Prop. 3.5(iii), p. 58 | p. 58: "(iii) If `x_n ⇀ x` weakly in `σ(E,E')`, then `(‖x_n‖)` is bounded and `‖x‖ ≤ lim inf‖x_n‖`." | **[DI] confirmed verbatim** |
| F3(i) | Brezis Thm 4.15 (Young), p. 104 | p. 104: "• **Theorem 4.15 (Young).** Let `f ∈ L^1(R^N)` and `g ∈ L^p(R^N)`, `1 ≤ p ≤ ∞`. Then for a.e. `x` the function `y ↦ f(x-y)g(y)` is integrable … `f*g ∈ L^p` and `‖f*g‖_p ≤ ‖f‖_1‖g‖_p`." | **[DI] confirmed verbatim** |
| F3(ii) | Brezis Prop. 4.20, p. 107 | statement on p. 107 with proof on p. 108 ending "It follows that `f*g` is differentiable at `x` and `∇(f*g)(x) = (∇f)*g(x)`" — the `C_c^k × L^1_loc` differentiation statement as used | **[DI] confirmed** |
| F3(iii) | Brezis Prop. 4.18, p. 106 | p. 106: "• **Proposition 4.18.** Let `f ∈ L^1(R^N)` and `g ∈ L^p(R^N)`, `1 ≤ p ≤ ∞`. Then `supp(f*g) ⊂ supp f + supp g`." Hypothesis is `g ∈ L^p`, not `g ∈ L^1_loc` (see minor issue M3) | **[DI] confirmed, hypothesis narrower than F3's wording** |
| F3(v) | Brezis Thm 4.12 (`C_c` dense in `L^p`) | p. 97–98: Thm 4.12 with the truncate-then-`C_c` proof — statement correct; **but the fact is never used in the block** (see §6) | **[DI] confirmed, unused** |
| F4 | Grafakos, CFA 3rd ed., §2.2.4 | published TOC (GBV 799245089): §2.2.4 "The Fourier Transform on `L^1 + L^2`", p. 113 — the section location and title are now confirmed; the theorem number remains unchecked.  Grafakos's own transform convention is `e^{-2πix·ξ}`, i.e. D1's, so the citation imports no `2π` factor | **[MO] for the theorem text; section title + page now [DI] from the published TOC** |
| F5' | Stein 1970, Ch. II §2, Ch. III §1 | not re-fetched; pagination as in `cp01-literature-statements` §6 (S1) | **[MO], unchanged** |

**Independent compile.**  I spliced the candidate's LaTeX block into a scratch
copy of `main.tex` myself (adding only the two `\newtheorem` lines, the three
BibTeX entries, a `\phantomsection\label{prop:localtheory}` stub, and keeping
the tail from "On compact classical intervals"), and ran `latexmk -pdf`:
exit 0, **17 pages**, no LaTeX errors, no `Undefined`/`multiply defined`
warnings, no `Overfull`/`Underfull` boxes.  The candidate's compile claim is
independently reproduced.  Environments used by the block: `definition`,
`lemma`, `proposition`, `remark`, `proof`, `equation`, `align`, `gather`,
`itemize`, `enumerate` — so exactly the two announced `\newtheorem`
declarations are needed, and no new macro is used (`\R`, `\norm` already
exist).

**Obligation coverage** (against `cp01-manuscript-obligations.md` §1.14).
Q-0 ✓ (`def:quotient`(a), with the closure-of-a-subspace argument written
out); Q-1 ✓; Q-2 ✓ (by pointwise strict convexity — a legitimate and
stronger-than-required substitute for the CP01 suggestion of Clarkson);
Q-3 ✓ (dominant `(|w|+|g|)²|g| ∈ L^1`, exactly the CP01 dominant up to the
harmless factor 3 coming from the `⅓` normalisation of `F`); Q-4 ✓ modulo the
single declared import (F5), including the duality proof of `Pu = u` that
CP01 explicitly demanded; Q-5 ✓; Q-6 ✓; Q-7 ✓ (all of (a)–(g) of the CP01
list, with `c = 1/2` explicit and sharp).  Nothing in Q-0…Q-7 is left
sketched.

## 5. Conditional suffix that survives

Unchanged and unaffected by this audit: the manuscript's only bridge to the
Clay conclusion remains `hyp:critical` (concretely `hyp:absorption` /
`hyp:highpressure` on the pressure route, and the unproved
`eq:quotient-gap` on this route).  What this half licenses downstream is
exactly:

> Assume the regularity package R (`prop:localtheory`).  Then for each fixed
> `t < T_*` the functional `𝒬` of `def:quotient` has a unique minimising
> representative `w(u(t))` with `div(|w|w) = 0` distributionally, `𝒬` is
> Fréchet differentiable at `u(t)` with derivative `h ↦ ⟨|w|w,h⟩` and
> remainder `≤ 6(‖w‖_3+‖h‖_3)^{3/2}‖h‖_3^{3/2}`, `𝒬` is cubically
> homogeneous, critically scale-invariant, translation-invariant, and
> nonincreasing under `e^{sΔ}`, and `‖u(t)‖_3³ ≤ 3C_ℙ³ 𝒬(u(t)) ≤ C_ℙ³‖u(t)‖_3³`.

CP02-7 may take `lem:quotient-minimizer`(c), `lem:gradient-closure`,
`lem:quotient-coercive`, `lem:quotient-heat`, `lem:quotient-stability` and
`prop:quotient-derivative` as proved inputs.  No `L^3` bound on any
Navier–Stokes solution follows from any of it.

## 6. Unnecessary dependencies

1. **(F3)(v) — Brezis Thm 4.12 (`C_c` dense in `L^p`) is never used.**
   Density of `L^2 ∩ L^3` in `L^3` is proved directly in `lem:density`(b) by
   truncation.  Delete the clause from (F3) (or the `Brezis2011` page
   reference for it) so the import list matches the proof.
2. **Stein1970 (F5′) is a courtesy citation.**  The operative import is
   Tao's sentence; Stein is named as the underlying theorem but no statement
   of Stein's is used as a step.  Keep it as attribution, but the Lean axiom
   should be phrased from the Tao sentence (as the candidate says), and the
   note should not suggest that two independent imports are being made.
3. `lem:cubic-pointwise` is never `\ref`'d (only its equations are
   `\eqref`'d); `eq:cp-coercive` and `eq:cp-heat` are labelled but never
   referenced.  Harmless, but they are dead labels.
4. The `‖·‖_X`/product-measure detour in `lem:quotient-minimizer`(a) is
   **not** unnecessary: it is forced by Brezis's scalar-real `L^p`.  Keep it.

## 7. Minor editorial and integration issues for the integrator

Recommended patches (all mechanical; none changes a proof):

* **M1 — two hard-coded section numbers.**  The block contains
  "avoids the explicit pressure work of Section~4" and "the Riesz transforms
  of Section~4".  `main.tex` §4 is currently "A signed critical balance", but
  CP02 inserts a local-theory section ahead of it, so both references will
  silently become wrong.  Add a `\label` to the pressure section (e.g.
  `\label{sec:pressure}`) and replace both by `Section~\ref{sec:pressure}`.
* **M2 — notation collision `Φ`.**  The block uses `\Phi` for the scalar
  Fourier-side potential in `lem:leray`(d) Step 2; the retained tail of the
  same section uses `\Phi_s` for the volume-preserving flow of `u`
  (`q_s = DΦ_{-s}^T(q∘Φ_{-s})`).  Rename one of them (suggestion: the
  potential to `Θ`), or CP02-7 will inherit the clash.
* **M3 — notation collision `S`.**  The block uses `\mathcal S(\R^3)` for the
  Schwartz class (as §1 of `main.tex` does) *and* `\mathcal S_\lambda` for
  the critical scaling; the retained tail uses `S_L` for the
  Littlewood–Paley projection, which under D1 is `S_J := P_{≤2^J}`.  Rename
  the scaling operator (suggestion: `\mathcal D_\lambda` for the dilation) so
  that `S`-symbols in `sec:quotient` mean only D1's projections.
* **M4 — (F3)(iii) hypothesis.**  Brezis Prop. 4.18 assumes `f ∈ L^1`,
  `g ∈ L^p`; F3 states it under `g ∈ L^1_loc`.  In the one place it is used
  (`ρ_ε * ψ_R`) the function `ψ_R` is in `L^3` with compact support, so the
  fact is true as used, but the imported statement should read
  "for `k ∈ C_c^∞` and `g ∈ L^1_loc` with compact support (hence `g ∈ L^1`)".
  D5 requires the import to be stated exactly as the source supports it.
* **M5 — prose overstatement.**  "a functional on `L^3(R^3;R^3)` whose
  derivative annihilates every gradient": what is proved is that it
  annihilates `G_3`, and `lem:gradient-closure` covers `∇ψ` only for
  potentials `ψ ∈ L^3` with `∇ψ ∈ L^3`.  (Every `L^3` gradient is in fact in
  `G_3` — the cutoff error is `‖ψ∇χ_R‖_3 ≤ ‖ψ‖_{9/2}‖∇χ_R‖_9 = O(R^{-2/3})`
  using the Gagliardo–Nirenberg embedding `Ẇ^{1,3}(R^3) ↪ L^{9/2}` — but that
  is not proved in the block, and importing GNS would add a new source.)
  Replace by "annihilates `G_3`", or state and prove the stronger closure
  lemma.
* **M6 — D5 gap in a remark.**  The remark after `lem:quotient-heat` says
  `G_{s+t}u = G_t(G_su)` "by the semigroup property of the Gaussian kernel"
  without an argument.  Either add the one-line verification
  (`k_s * k_t = k_{s+t}`, e.g. by completing the square, or via
  `k̂_s(ξ) = e^{-4π²s|ξ|²}`) or drop the monotonicity-in-`s` sentence, which
  nothing in the block uses.
* **M7 — D5 nit in `def:quotient`(d).**  "`k_s ∈ S(R^3)`" is asserted; add the
  half-line reason (every derivative is a polynomial times
  `e^{-|x|²/4s}`).  Likewise, `lem:leray`(a) should say that `Π` is defined
  for `ξ ≠ 0` and `{0}` is a null set, so `Π F f` is defined a.e.
* **M8 — attribution nit.**  The remark after `lem:quotient-minimizer` says
  "no uniform convexity of `L^3` and no Clarkson inequality is used anywhere
  in this section".  True of the block's own arguments, but Brezis's proof of
  the imported Theorem 4.10 *is* Clarkson's first inequality (p. 95).  Write
  "is used in our arguments" to avoid an overclaim about the import chain.
* **M9 — completeness clause.**  In `lem:quotient-minimizer`(a) add one
  clause noting that `(L^3(R^3;R^3),‖·‖_3)` is itself a Banach space
  (completeness transfers along the norm equivalence with `X`), since
  Prop. 3.5(iii) is then applied in that space rather than in `X`.
* **M10 — pagination.**  The source table gives "Thm. 3.18, p. 69"; the
  statement sits at the p. 69/70 boundary (Thm 3.19 opens p. 70).  Write
  "pp. 69–70".
* **M11 — F4 upgrade available.**  §2.2.4 of Grafakos 3rd ed. is
  "The Fourier Transform on `L^1 + L^2`", beginning p. 113 (verified from the
  published table of contents); this can be recorded in the source table, and
  it is worth stating explicitly that Grafakos uses the `e^{-2πix·ξ}`
  convention of D1, since a Plancherel citation in another normalisation
  would import a `2π` factor into `lem:leray`.  The theorem number is still
  unverified, so F4 stays [MO] for the statement.
* **M12 — quotation fidelity.**  The (F5) quote follows the arXiv source
  ("from Calder\'on-Zygmund theory we know"); the published page 38 has a
  comma after "theory".  If the citation is to the published page, restore
  the comma.
* **M13 — interface.**  `rem:quotient-scope` should say *why* `u(t) ∈ L^2 ∩
  L^3` (one clause: `prop:localtheory` gives `u ∈ C([0,T];L^q)` for
  `2 ≤ q ≤ ∞`), so the remark does not read as an assumption about R that R
  might not supply.
* **M14 — declared, still open handover.**  The CP01 draft's
  `lem:gradient-closure`(b) (pullback of compact gradients under the
  volume-preserving flow, Q-13) is *not* in the block; the integrator must
  either merge CP02-7's version as part (b) of this label or have CP02-7
  introduce a separate label.  The candidate declares this correctly.

## 8. Non-claims (restated, and confirmed to hold of the candidate)

* No estimate for any Navier–Stokes solution is proved in the reviewed block;
  no bound on transport or strain; no sign or quantitative dissipation for
  `D_𝒬`; no smoothness of `w` or `q` beyond `L^3` membership.
* `eq:quotient-gap` (HIGH-STRAIN) is neither proved nor addressed; nothing
  here bears on HIGH-PRESSURE, CRITICAL, ABSORPTION or NS-R3.
* The `L^p` boundedness of the Leray projection is **imported**, not proved:
  the directly inspected source is one sentence of Tao 2013 p. 38, which
  itself cites "Calderón–Zygmund theory" with no reference; Stein 1970 is
  [MO].  A Lean development must axiomatise exactly this (mathlib-absent per
  `cp01-mathlib-coverage`), and only for `p ∈ {3, 3/2}` restricted to
  `L^2 ∩ L^p`.
* Plancherel (F4) is cited at section level [MO].
* No novelty is claimed for the construction, and no Lean statement is
  claimed type-checked.

## 9. Reopening condition

This PASS is to be reopened if any of the following happens:

1. **F5 is weakened or withdrawn.**  If the `L^p` bound for `ℙ` cannot be
   imported in the stated form (`‖ℙf‖_p ≤ C_p‖f‖_p` for `f ∈ L^2 ∩ L^p`,
   `p = 3, 3/2`), then `lem:leray`(b),(d), `lem:quotient-coercive`
   (lower bound and `‖q‖_3 ≤ (1+C_ℙ)‖w‖_3`) and every downstream use of
   `‖u‖_3³ ≤ 3C_ℙ³𝒬(u)` fall; the rest of the block (existence, uniqueness,
   stationarity, scaling, heat monotonicity, the derivative) survives
   untouched, since none of it uses `ℙ`.
2. **The local-theory lane delivers a package weaker than D2** — in
   particular if `u(t) ∈ L^3` or `div u = 0` in the distributional sense is
   not available for every `t < T_*` — in which case `rem:quotient-scope`'s
   last sentence must be re-scoped.
3. **`prop:localtheory` is renamed** (one `\ref`), or the pressure section
   receives a different label than the one used to fix M1.
4. **CP02-7 uses any statement of this block outside its stated scope** —
   specifically if it applies `ℙw = u`, `q = (I-ℙ)w`, the coercive lower
   bound, or `‖q‖_3 ≤ (1+C_ℙ)‖w‖_3` to a field that is not distributionally
   solenoidal, or applies `lem:gradient-closure` to a potential not in `L^3`.
5. **A convention change under D1** (Fourier normalisation, Riesz sign, or
   the definition of `p`) would require re-checking `lem:leray`(a),(c) and the
   (F4)/(F5) citations, which are the only convention-sensitive places.

## 10. Frontier record

**MODE / RESULT.** REVIEW / PASS.  Round-1 audit of the CP02-6 deliverable
(Q-0 … Q-7 of `sec:quotient`); no invalid bridge found; 14 editorial and
integration fixes listed; two of them (M1 hard-coded section numbers,
M2/M3 notation collisions with the retained tail) must be applied before
integration or the section will be internally inconsistent.

**CLAIM AND SCOPE.** The claim being audited — and, after this audit, the
claim the manuscript may make — is a statement about a functional on
`L^3(R^3;R^3)` only: unique minimising representative, distributional
`div(|w|w) = 0`, gradient invariance, cubic homogeneity, critical scaling and
translation invariance, heat monotonicity, Lipschitz stability, Fréchet
differentiability with an `O(‖h‖_3^{3/2})` remainder, and — for
distributionally solenoidal `u` only — the two-sided coercivity
`‖u‖_3³/(3C_ℙ³) ≤ 𝒬(u) ≤ ‖u‖_3³/3`.  One import (F5) carries the whole
`ℙ`-dependent part.

**EVIDENCE.** Full reconstruction of all 11 lemma/proposition proofs; all
Hölder/Cauchy–Schwarz/Young exponents and all constants (1, ½, 2, 4, 6,
`3`, `9`, `R^{-1}`, `R^{-1/2}`) recomputed; 13 source statements re-fetched
(Tao arXiv e-print source; Brezis pp. 58, 60, 69–70, 89, 95, 97–98, 104,
106–108; Grafakos published TOC) with 12 confirmed [DI] and one upgraded
from bare [MO] to [MO]+TOC-[DI]; 400 000-sample randomised test of the four
pointwise inequalities; a finite-dimensional analogue of the entire
construction confirming stationarity, the derivative formula, the remainder
bound, the stability bound and the Euler identity `⟨A,u⟩ = 3𝒬(u)`;
independent `latexmk` compile of the spliced manuscript (17 pages, clean).

**FIRST GAP.** Unchanged by this audit: `eq:quotient-gap` (HIGH-STRAIN) is
unproved.  Within the audited scope the only non-self-contained step is the
import F5, whose primary Calderón–Zygmund source remains [MO].

**SURVIVING CONDITIONAL SUFFIX.** As in §5: with R assumed, the functional
facts hold at every `t < T_*`; the implication to a critical bound still
requires `eq:quotient-gap`, which is not proved.

**NON-CLAIMS.** As in §8; verbatim non-claims of `main.tex` are preserved by
the candidate's block and by the retained tail.

**NEXT DISTINCT ACTION.** Apply M1–M14 (mechanical), then audit CP02-7's
second half — priority targets there: the pullback lemma (Q-13) whose
`G_3`-membership claim is the only place where the flow interacts with the
closure, the `C^1`-in-time chain rule (Q-10), and the generator limit
`(G_su-u)/s → Δu` in `L^3` (Q-11), each of which needs a hypothesis that
this half deliberately does not supply.
