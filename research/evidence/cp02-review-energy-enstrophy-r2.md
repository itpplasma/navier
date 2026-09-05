# CP02 audit round 2: energy, scaling, enstrophy (review of `cp02-energy-enstrophy.md`)

MODE: REVIEW (proof-audit discipline). Date: 2026-09-05. This lane owns this file
only; nothing else was edited and nothing was pushed.

## 0. Frozen candidate

| item | value |
|---|---|
| candidate file | `/home/ert/proj/navier/research/evidence/cp02-energy-enstrophy.md` |
| sha256 | `1fa71d15cac3870da924616c351d2848a7411ff309f4bcc95b3aabc16f2efb20` |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `f20e6bf579f74c3fef4e365fa5267929667f1228` |
| manuscript audited against | `/home/ert/proj/navier-paper/main.tex` (read in full) |
| Mathlib checkout | `/home/ert/proj/stafford38/.lake/packages/mathlib`, `git rev-parse --short HEAD` = `0df444a360` |
| navier-formal | HEAD now `e9519e9`; candidate records `9c8b37d` (its parent) |
| Grafakos PDF read | `scratchpad/graf.pdf` (3rd ed., GTM 249) |
| Tao PDF read | `scratchpad/tao/apde-full.pdf` (published APDE version) |
| Nirenberg PDF read | `scratchpad/nirenberg.pdf` (numdam) |
| author's summary | untrusted; used only to locate claims |

**Reviewed scope.** The whole fenced LaTeX block of §2 of the candidate (the
replacement for `main.tex` from `\section{Energy and scaling}` through the
paragraph after `prop:ode`): the Conventions subsection, `lem:fourier`,
`lem:parseval`, `lem:duality`, `lem:mollify`, `lem:compat`, `lem:hk`,
`lem:div-zero`, `lem:classical`, the "Consequences of the local theory"
subsection, `lem:R-consequences`, `lem:plancherel`, `def:sobolev-constant`,
`lem:density`, `lem:sobolev`, `lem:interp`, `lem:GN`, `prop:energy`,
`prop:scaling`, `rem:scaling-pressure`, `rem:mismatch`, `prop:enstrophy`,
`prop:ode`, `rem:lean`, `rem:usage`; together with the candidate's fact table
F1–F9, its integrator notes, and its obligation claims E-1, S-1, S-2, N-1.
Out of scope: `prop:pressure`, `prop:lowpressure`, the pressure hypotheses,
`thm:continuation`, `thm:conditional`, `sec:quotient`, and `prop:localtheory`
itself (assumed as package R per D2).

---

## 1. VERDICT

**VERDICT: PASS.**

The round-1 first bad bridge is closed at the root, not papered over. Every
Fourier fact the section uses is now either (a) imported in a single labelled
lemma with an exact primary location that I opened and read in this audit, or
(b) proved in the manuscript from those imports and the stated definitions. I
reconstructed every proof in the reviewed scope from its first nontrivial
implication and could not refute any step; every Hölder, Young, interpolation
and Plancherel exponent and every constant recomputes exactly as printed. All
twenty Mathlib declarations named in the tables exist at the cited lines of the
named checkout, so the `[DI]` labels that were unsupported in round 1 are now
earned. The block compiles standalone into `main.tex` with zero errors and zero
undefined references given exactly the integrator inputs the candidate lists.

Obligations E-1, S-1, S-2, N-1 are discharged.

Three defects remain, none of them a bad bridge, all for the integrator; the
first is **splice-blocking** and was not flagged by the candidate:

* **three cross-lane label collisions** (`lem:duality`, `lem:density`,
  `eq:enstrophy-identity`) with the local-theory, quotient-functional and
  continuation lanes (§6.1);
* one **over-assumption of R** that is never used (`∇²u ∈ C([0,T];L^q)` for
  `q>2`, §6.2);
* two **inaccurate statements inside the candidate's own evidence record**
  (§6.3), which do not touch the mathematics.

---

## 2. FIRST BAD BRIDGE

**None in the reviewed scope.**

The round-1 blacklisted implication ("Tao 2013 pp. 14–15 supplies Parseval, the
Fourier derivative rule, and the distributional `H^k` characterisation") is gone.
What replaced it is sound, and I checked it at the source rather than taking the
candidate's word:

* `lem:fourier`(S) is exactly Grafakos Prop. 2.2.11 (9), (10), (11) (printed
  pp. 109–110) and Thm 2.2.14 (2), (3), (4) (printed p. 112). I read both pages:
  (9) `(∂^α f)^∧ = (2πiξ)^α f̂` **with the integration-by-parts proof printed**,
  (10) `∂^α f̂ = ((−2πix)^α f)^∧` with the dominated-convergence proof, (11)
  `f̂ ∈ S`; and Thm 2.2.14 (2) Fourier inversion `(f̂)^∨ = f = (f^∨)^∧`,
  (3) Parseval, (4) Plancherel, with the proof printed on pp. 112–113. The
  hypotheses are `f, g, h ∈ S(R^n)`, exactly as the lemma states them.
* `lem:fourier`(L) is exactly §2.2.4, printed pp. 113–114. Verbatim there:
  "In view of the result in Exercise 2.2.8, the Fourier transform is an `L²`
  isometry on `L¹ ∩ L²`, which is a dense subspace of `L²`. By density, there is
  a unique bounded extension … Then `F` is also an isometry on `L²` …";
  "for `f` in `L¹(R^n) ∩ L²(R^n)` the expressions `f̂` and `F(f)` coincide
  pointwise a.e."; "`F` and `F'` are injective and surjective mappings from
  `L²` to itself; consequently `F'` coincides with the inverse operator `F^{-1}`",
  where `F'` is "the isometry on `L²` that extends the operator `f ↦ f^∨`". Every
  clause of the lemma is covered, including the description of `F^{-1}`.
* The candidate's own caveat is accurate and I confirmed it: the `L¹∩L²`
  isometry is **Exercise 2.2.8** (printed p. 117), with a complete hint that
  reduces it to Exercises 2.2.7(b) and 2.2.6(b) — I read the exercise and the
  hint. Declaring this in §4 rather than hiding it is the correct behaviour
  under D5.
* Everything else is proved in the manuscript. In particular Grafakos'
  Prop. 2.3.22 (8) and (10) — whose entire printed proof is the sentence "All the
  statements can be proved easily using duality and the corresponding statements
  for Schwartz functions" (I read it) — are **not** imported; they are re-proved
  as `lem:duality`(a),(b) from the definitions and (S). That is the right call
  under D5, and the two duality computations are correct (see §4).
* The Tao pagination is now right. Printed **p. 35** carries the Euclidean
  tensor norms `|u|² = u_i u_i`, `|∇u|² = (∂_i u_j)(∂_i u_j)`,
  `|∇²u|² = (∂_i∂_j u_k)(∂_i∂_j u_k)`, the `L¹` Fourier convention
  `f̂(ξ) = ∫ e^{−2πix·ξ} f(x) dx`, and "we then extend this Fourier transform to
  tempered distributions in the usual manner". Printed **p. 36** carries the
  classical `H^k` norm for smooth `u`, the Fourier `H^s` norm for tempered
  distributions, and "the two norms are equivalent up to constants". Both the
  round-1 table ("pp. 37–38") and the round-1 audit's suggested `p. 37`/`p. 38`
  were wrong; the candidate is right and its correction of my predecessor's
  correction is confirmed. Tao is cited in the block only at p. 35 (three times)
  and p. 36 (once), and only for conventions — no Parseval, no derivative rule,
  no `H^k` characterisation is attributed to him anywhere.

---

## 3. EVIDENCE

### 3.1 Source checks performed in this audit (all at the primary text)

| source | route | result |
|---|---|---|
| Grafakos, printed pp. 109–110 (Prop. 2.2.11 (9),(10),(11) + proofs) | `helpy_pdf` `mode:"text"`, PDF pp. 126–127 | `[DI]` confirmed verbatim; hypotheses `f,g ∈ S(R^n)` as stated |
| Grafakos, printed p. 112–113 (Thm 2.2.14 (2),(3),(4) + proof) | `helpy_pdf`, PDF pp. 129–130 | `[DI]` confirmed verbatim, incl. "(Parseval's relation)", "(Plancherel's identity)" |
| Grafakos, printed pp. 113–114 (§2.2.4, the whole `L²` theory) | `helpy_pdf`, PDF pp. 130–131 | `[DI]` confirmed verbatim, incl. the a.e. agreement clause and `F' = F^{-1}` |
| Grafakos, printed p. 117 (Exercise 2.2.8 + hint) | `helpy_pdf`, PDF p. 134 | `[DI]`; the candidate's exercise caveat is exactly right |
| Grafakos, printed pp. 122–125 (Ex. 2.3.5(4); Defs 2.3.6, 2.3.7, 2.3.15) | `helpy_pdf`, PDF pp. 139–142 | `[DI]`; `⟨∂^α u,f⟩=(−1)^{\|α\|}⟨u,∂^α f⟩`, `⟨û,f⟩=⟨u,f̂⟩`, `⟨u^∨,f⟩=⟨u,f^∨⟩`, `⟨hu,f⟩=⟨u,hf⟩` with Grafakos' slowly-increasing condition `\|∂^α h\| ≤ C_α(1+\|x\|)^{k_α}`, and "Functions in `L^p`, `1≤p≤∞`, are tempered distributions" |
| Grafakos, printed p. 105 (Def. 2.2.1, Rem. 2.2.3) | `helpy_pdf`, PDF p. 122 | `[DI]`; Schwartz seminorms; `∂^α f ∈ S`, `P(x)f ∈ S` |
| Grafakos, printed pp. 130–131 (Prop. 2.3.22 (8),(10) and its proof) | `helpy_pdf`, PDF pp. 147–148 | `[DI]`; proof is one sentence, as the candidate says. **Item (10) is on p. 131, not p. 130** (see §6.3) |
| Tao, APDE 6 (2013), printed pp. 35–36 | `helpy_pdf`, `apde-full.pdf` PDF pp. 12–13 | `[DI]`; F1 confirmed verbatim; pagination now correct |
| Nirenberg 1959, printed p. 125 | `helpy_pdf`, PDF p. 12 | `[DI]`; theorem, both exceptional cases, "We shall not give a complete proof … but shall indicate the main steps", and — the newly added item — "We define `\|D^j u\|_p` as the maximum of the `\|·\|_p` norms of all `j`-th order derivatives of `u`". Comment 2 ("For `a=1` the fact that `u` is contained in `L_q` does not enter") makes the `a=1` instance even cleaner than claimed |
| Mathlib `0df444a360`, 20 declarations at the 20 cited lines | `sed -n` at each `file:line` | **all present, all with the quoted signatures**: `LpSpace.lean:50,89,93,99,120`; `TemperedDistribution.lean:367,482,568`; `Sobolev.lean:233`; `AEEqOfIntegralContDiff.lean:195`; `SobolevInequality.lean:600`; `MeanInequalities.lean:500`; `CompareExp.lean:300`; `Integral/Prod.lean:444`; `Measure/Prod.lean:1006`; `DominatedConvergence.lean:57`; `Lebesgue/Add.lean:231`; `ConvergenceInMeasure.lean:464,330`; `FourierTransform.lean:439` |
| navier-formal | `Ode.lean:34,109,134`; `InterpolationMismatch.lean:32,114,136`; `Scaling.lean:48,84,125` | all present; `L4L3_supercritical` proves exactly `2/4+3/3 = 3/2 ∧ 1 < 3/2`, so the narrowed attribution in `rem:mismatch`(b) is now honest |
| compile check | spliced the block into `main.tex` in place of §§2–3, added only the two `\newtheorem` lines, a `\label{prop:localtheory}` stub and the four `.bib` entries | `pdflatex`+`bibtex`+`pdflatex`×2 exit 0; **17 pages, zero `!` errors, zero undefined references, zero undefined citations** — reproduces the candidate's claim |
| label/citation closure | scripted extraction of the block's `\label`/`\ref`/`\cite` | the only external `\ref` is `prop:localtheory`; the only external `\cite`s are the four new keys; **no reference to any evidence file** anywhere in the block; macros used from the preamble are `\R` (92×) and `\norm` (18×), both already in `main.tex` |

### 3.2 Independent reconstruction of the new import layer

Every one of the seven new lemmas was rederived from scratch.

**`lem:parseval` (polarisation).** `‖f+g‖² − ‖f−g‖² = 4 Re ∫f ḡ`; and
`⟨f, ig⟩ = −i∫f ḡ`, `Re(−iz) = Im z`, so `‖f+ig‖² − ‖f−ig‖² = 4 Im ∫f ḡ`.
Hence `4∫f ḡ = (‖f+g‖²−‖f−g‖²) + i(‖f+ig‖²−‖f−ig‖²)`, exactly as printed. The
transfer to `Ff, Fg` needs `F` to be `C`-linear and isometric, which is what
`lem:fourier`(L) asserts and what Mathlib's `≃ₗᵢ[ℂ]` provides. Correct.

**`lem:duality`(a).** `⟨(û)^∨,φ⟩ = ⟨û,φ^∨⟩ = ⟨u,(φ^∨)^∧⟩ = ⟨u,φ⟩` by
`lem:fourier`(S) inversion. Correct.

**`lem:duality`(b).** The sign is the delicate part and it is right:
`⟨(∂^α u)^∧,φ⟩ = (−1)^{|α|}⟨u,∂^α φ̂⟩ = (−1)^{|α|}⟨u,((−2πix)^α φ)^∧⟩
= (−1)^{|α|}⟨û,(−2πix)^α φ⟩ = ⟨û,(2πix)^α φ⟩`, since
`(−1)^{|α|}(−2πix)^α = (2πix)^α`. The two special cases use
`Σ_j(2πiξ_j)² = −4π²|ξ|²`. Correct.

**`lem:duality`(c).** `h u_g = u_{hg}` is legitimate even when `hg ∉ L²`, because
the Conventions admit `f = hg` (`g ∈ L²`, `h` slowly increasing) as a second
class of `L²`-based tempered distributions with the bound
`|∫hgφ| ≤ ‖g‖₂‖hφ‖₂`. I checked that this class is genuinely needed and genuinely
sufficient for `(1+|ξ|²)^{s/2}û` and for `(2πiξ)^α û`. The two Conventions
seminorm estimates are correct, including `‖(1+|x|²)^{-1}‖_{L²(R³)} < ∞`
(integrand `~|x|^{-4}` at infinity in three dimensions).

**`lem:mollify`.** Difference quotients dominated by `‖∇ρ_ε‖_∞|w| ∈ L¹`;
`‖ρ_ε*w‖₁ ≤ ‖w‖₁` by Tonelli; `‖ρ_ε*w‖₂ ≤ ‖w‖₂` by Cauchy–Schwarz against
`ρ_ε^{1/2}·ρ_ε^{1/2}|w|` then Tonelli; `(ρ_ε*w)^∧ = ρ̂_ε ŵ` by Fubini (absolute
convergence given); `ρ̂_ε(ξ) = ρ̂(εξ)` by `x = εz`; `|ρ̂| ≤ 1`, `ρ̂(0)=1`,
`ρ̂` continuous; then `lem:fourier`(L) on `ρ_ε*w − w ∈ L¹∩L²` and dominated
convergence with majorant `4|ŵ|²`. Every hypothesis is available. Correct.

**`lem:compat`.** (i) `f_N = f1_{|x|≤N} ∈ L¹∩L²`, `f_N → f` in `L²`;
`∫f_N φ̂ = ∫f̂_N φ` by Fubini; both sides pass to the limit against `φ̂, φ ∈ L²`.
The `F^{-1}` half uses `φ^∨(x) = ∫φ(ξ)e^{2πix·ξ}dξ` and `f_N^∨ = F^{-1}f_N`,
which is licit because `F^{-1}` is *the extension of* `f ↦ f^∨` from `L¹∩L²`.
(ii) The fundamental lemma: `w = χ_R g ∈ L¹∩L²`, `y ↦ χ_R(y)ρ_ε(x−y) ∈ C_c^∞`
kills `ρ_ε*w ≡ 0`, `lem:mollify` gives `w = 0`, then `R → ∞` through the
integers. (iii) `f = F^{-1}g`, `(û_f)^∨ = u_f` and `lem:duality`(a). Correct;
this is the honest replacement for the round-1 unproved sentence.

**`lem:hk`.** Forward: `(1+|ξ|²)^{k/2}û = u_g`, multiply by
`(1+|ξ|²)^{−k/2}` (slowly increasing, so admissible) to get `û = u_G`,
`G = (1+|ξ|²)^{−k/2}g ∈ L²`; then
`|(2πξ)^α G| ≤ (2π)^{|α|}|ξ|^{|α|}|G| ≤ (2π)^k(1+|ξ|²)^{k/2}|G| = (2π)^k|g|`,
so `lem:compat`(iii) applies. Converse: `Fg_α = (2πiξ)^α Ff` a.e. by
`lem:compat`(ii) (both sides square integrable on balls), then the multinomial
expansion of `(1+ξ_1²+ξ_2²+ξ_3²)^k` with positive integer coefficients. I
verified `eq:h1-norm`: `‖u‖²_{H^1} = ‖u‖₂² + ∫|ξ|²|Fu|²` and
`‖∇u‖₂² = 4π²∫|ξ|²|Fu|²`, so the factor is `(2π)^{−2}`. Correct.

**`lem:classical`.** `∫v ∂_iψ = −∫(∂_iv)ψ` for `v ∈ C¹`, `ψ ∈ C_c¹` follows from
`lem:div-zero` applied to `vψ` (which is `C¹` with compact support, so `vψ` and
`∂_i(vψ)` are in `L¹`); iterating `|α|` times gives
`(−1)^{|α|}∫u∂^αφ = ∫(∂^α u)φ`; `g − ∂^α u` is square integrable on balls because
`∂^α u` is continuous; `lem:compat`(ii) finishes. Correct. This closes the
round-1 unproved convention sentence "when `u` is smooth, its distributional
derivatives are its classical ones", which was load-bearing everywhere.

**Dependency graph is acyclic.** `mollify → fourier`;
`compat → mollify, duality, fourier`; `duality → fourier`; `hk → duality, compat`;
`classical → hk, div-zero, compat`; `density → mollify, hk, compat`;
`sobolev → density, classical, def:sobolev-constant`; `plancherel → parseval, hk`;
`R-consequences → classical, hk`. No lemma is used in the proof of an earlier
one, and nothing in the scope is used in the proof of `prop:localtheory`
(checked against `cp02-local-theory.md`: it consumes `prop:energy` only in a
scope remark about the Leray–Hopf class, i.e. downstream, not upstream). No
hidden circularity.

### 3.3 Independent reconstruction of the physics-facing results

**`lem:R-consequences`.** (a) `H^k`-convergence of the difference quotients is
`u ∈ C¹([0,T];H^k)`; `‖v‖₂ ≤ ‖v‖_{H^k}` gives `L²`; an a.e.-convergent
subsequence identifies the limit with the classical `∂_t u`. (b) The four terms
are in `L²` — `Δu, ∇p` by `lem:classical`, and
`|(u·∇)u| ≤ |u||∇u|` by componentwise Cauchy–Schwarz, so
`‖(u·∇)u‖₂ ≤ ‖u‖_∞‖∇u‖₂`, with `u ∈ L^∞` granted by D2. (c)
`∂_i(u_j|u|²) = (∂_iu_j)|u|² + 2u_j(u·∂_iu)`, `|∂_ig| ≤ 3|u|²|∇u|`,
`‖∂_ig‖₁ ≤ 3‖u‖₄²‖∇u‖₂`; and `u_jp` with two `L²` factors in each term. All
legitimate uses of R; no preserved Schwartz decay in time anywhere.

**`lem:div-zero`.** Correct, and it is the right device: it eliminates the
"radial cutoff" hand-wave E-1 complained about without needing any decay
beyond `g, ∂_i g ∈ L¹`. Refutation attempt: in one dimension, `g' ∈ L¹` forces
`g(±∞)` to exist and `g ∈ L¹` forces them to vanish, so `∫g' = 0` is forced. No
counterexample.

**`lem:plancherel`.** (i) `∫∂_ju_k∂_jv_k = 4π²∫ξ_j²Fu_k \overline{Fv_k}`; summing
`j` and comparing with `∫Δu_k v_k = −4π²∫|ξ|²Fu_k\overline{Fv_k}`. Integrability
is `(|ξ|²Fu_k)(Fv_k) ∈ L¹`, so the hypotheses `u ∈ H²`, `v ∈ H¹` are exactly
what is needed. (ii) `Σ_{i,j}ξ_i²ξ_j² = |ξ|^4`, so `‖∇²u‖₂ = ‖Δu‖₂` — a
whole-space identity, and `Ω = R³` is genuinely used. (iii) The conjugation sign
is right: `2πiξ_i\overline{Fu_i} = −\overline{2πiξ_i Fu_i}`, the two minus signs
cancel, and the sum is `4π²∫|ξ|²Fp\,\overline{F(\mathrm{div}\,u)} = 0`. Note that
this route needs only `p ∈ H¹`, `u ∈ H²` — strictly less than the obligation
sheet's suggested `∫∇p·Δu = −∫pΔ(\mathrm{div}\,u)` route, which would need
`u ∈ H³`. An improvement, correctly executed.

**`def:sobolev-constant`.** Nirenberg instance `n=3, j=0, m=1, r=q=2, a=1, p=6`:
`1/p = j/n + a(1/r − m/n) + (1−a)/q = 1/2 − 1/3 = 1/6` ✓; `j/m = 0 ≤ a = 1` ✓;
exceptional case 1 needs `q = ∞` (here `2`) ✓; exceptional case 2 needs
`m − j − n/r = −1/2` to be a nonnegative integer ✓. The max-norm reconciliation
`max_j‖∂_jf‖₂ ≤ ‖|∇f|‖₂` is correct and is the newly added repair. The Mathlib
instance `p = 2 ⇒ (p')^{-1} = 1/2 − 1/3 = 1/6 ⇒ p' = 6` ✓, with
`ContDiff ℝ 1` + `HasCompactSupport` matching `C_c^1` and the operator norm of
`fderiv ℝ u` equal to `|∇u|` for scalar targets.

**`lem:density`.** Step 1: `∂_j(χ_Ru) = χ_R∂_ju + u∂_jχ_R` derived from the
definition with test function `χ_Rφ`, plus three dominated-convergence limits
and `‖u∂_jχ_R‖₂ ≤ R^{-1}‖∇χ‖_∞‖u‖₂`. Step 2: the sub-argument that
`∂_jv = 0` a.e. off `supp v` is written out correctly (the test function
`y ↦ χ(y)ρ_ε(x−y) ∈ C_c^∞(R³∖K)`, then `lem:mollify`, then the countable
exhaustion `{|x| ≤ n, dist(x,K) ≥ 1/n}` whose union is `R³∖K` because `K` is
closed); and `∂_jv_ε = ρ_ε*∂_jv` with the correct sign
(`∂_{x_j}ρ_ε(x−y) = −∂_{y_j}ρ_ε(x−y)`). Correct.

**`lem:sobolev`.** Real parts do not increase either norm; `u_n ∈ C_c^∞ ⊂ S`, so
`lem:classical` licenses using the classical gradient in `eq:sobolev-cc`; Fatou
along an a.e.-convergent subsequence gives the `H^1` case; the vector constant
`√m C_S` is right via `|f| ≤ Σ_k|f_k|`, Minkowski, and Cauchy–Schwarz in `R^m`.

**`lem:interp`, `lem:GN`.** `∫|f|³ = ∫|f|^{3/2}|f|^{3/2} ≤ ‖f‖₂^{3/2}‖f‖₆^{3/2}`
by Hölder `(4/3, 4)`; cube roots give `‖f‖₃ ≤ ‖f‖₂^{1/2}‖f‖₆^{1/2}`. With
`m = 9`: `‖∇u‖₆ ≤ 3C_S‖∇²u‖₂ = 3C_S‖Δu‖₂`, hence
`‖∇u‖₃ ≤ (3C_S)^{1/2}‖∇u‖₂^{1/2}‖Δu‖₂^{1/2}`. Correct.

**`prop:energy`.** The difference-quotient identity plus continuity of the `L²`
inner product gives `E' = ∫u·u_t` with no cutoff at all; Step 2 is
`lem:plancherel`(i) with `v = u`; Step 3 is
`u·(u·∇)u = ½Σ_j∂_j(u_j|u|²) − ½(\mathrm{div}\,u)|u|²` plus `lem:div-zero`
(I verified the algebra `Σ_{j,k}u_ju_k∂_ju_k = ½Σ_ju_j∂_j|u|²`); Step 4 is the
same device on `u_jp`; Step 5 is the FTC with `∇u ∈ C([0,T];L²)`, and the
`[0,T_*)` integral is the monotone supremum. E-1 discharged, including the
removal of "strong-solution Sobolev bounds justify".

**`prop:scaling`.** (i) All five chain-rule factors are `λ³` and
`\mathrm{div}\,u_λ = λ²(\mathrm{div}\,u)(λx,λ²t)`; the datum hypothesis is now
stated inside the proposition (round-1 minor 4). (ii) `q < ∞` by `y = λx`;
`q = ∞` by `{|u_λ(t)| > λM} = λ^{-1}{|u(λ²t)| > M}` and preservation of null
sets in both directions. (iii) `((√3C_S)^{1/2})^4 = 3C_S²`, and the final
constant `3C_S²‖u_0‖₂^4/(2ν)` is right.

**`rem:scaling-pressure`.** `m_{ij}(ξ) = (−iξ_i/|ξ|)(−iξ_j/|ξ|) = −ξ_iξ_j/|ξ|²`;
and `−Δ^{-1}∂_i∂_j` has symbol
`−[−(4π²|ξ|²)^{-1}][−4π²ξ_iξ_j] = −ξ_iξ_j/|ξ|²`. Identical, so D1 is honoured
with the symbol computation printed rather than asserted.
`(f(λ·))^∧(ξ) = λ^{-3}f̂(ξ/λ)`, `m_{ij}` is `0`-homogeneous, and
`(u_λ)_i(u_λ)_j = λ²(u_iu_j)_λ`, giving `p_λ`. The non-claim about uniqueness of
the rescaled branch is correctly placed.

**`rem:mismatch`.** (a) `∫_0^T t^{-4/5}dt = 5T^{1/5}` and
`{t ∈ (0,T) : t^{-1/5} > M} = (0,\min\{T,M^{-5}\})`, of positive measure for
every `M`. (b) `∫_0^{T/λ²}‖u_λ‖_q^r dt = λ^{r(1−3/q)−2}∫_0^T‖u‖_q^r ds`, so the
norm scales by `λ^{1−3/q−2/r}`; invariance iff `2/r + 3/q = 1`; for `(r,q)=(4,3)`,
`2/4+3/3 = 3/2 > 1` and the exponent is `1 − 1 − 1/2 = −1/2`. S-2 discharged:
the meta-sentence is out of the proposition, the witness is proved, and the Lean
attribution is narrowed to the arithmetic the Lean theorem actually contains.

**`prop:enstrophy`.** `∂_j : H^1 → L²` bounded with norm `≤ 2π` (from `lem:hk`),
so it commutes with the `H^1`-limit of difference quotients and
`Y' = 2∫∇u:∇u_t`, continuous in `τ`. `lem:plancherel`(i) with `v = u_t ∈ H^1`
and (iii) with `p ∈ H^1`, `u ∈ H²` give `eq:enstrophy-identity`. The two-step
Hölder is exactly right: `(6, 6/5)` then `(5/2, 5/3)` on `|∇u|^{6/5}, |Δu|^{6/5}`
gives `(∫|∇u|³)^{2/5}(∫|Δu|²)^{3/5}`, and raising to `5/6` gives
`‖∇u‖₃‖Δu‖₂`. Then `√3C_S·(3C_S)^{1/2} = 3C_S^{3/2}` and
`Y^{1/2}·Y^{1/4} = Y^{3/4}`. Young on `(δa)(b/δ)` with `p=4/3, q=4` gives
`ab ≤ ¾δ^{4/3}a^{4/3} + ¼δ^{-4}b^4`; with `a = ‖Δu‖₂^{3/2}`,
`b = 3C_S^{3/2}Y^{3/4}`, `δ^{4/3} = 2ν/3`: `¾δ^{4/3} = ν/2`,
`δ^{-4} = 27/(8ν³)`, `b^4 = 81C_S^6Y³`, remainder
`¼·(27/8)·81 = 2187/32`. `C_E = (2187/32)C_S^6` confirmed. N-1 discharged.

**`prop:ode`, `rem:lean`, `rem:usage`.** `y = (2C(T−t))^{-1/2}` gives `y' = Cy³`
and `∫_0^T y = √(2T/C)`. All eight navier-formal names exist. `rem:usage` cites
only labels that exist in `main.tex` (round-1 minors 7 and 12 closed: no
`sec:continuation` is needed).

### 3.4 Refutation attempts (all failed)

1. **Weaken `lem:div-zero`.** Tried to build `g ∈ C¹` with `g, ∂_1g ∈ L¹` and
   `∫∂_1g ≠ 0`: impossible, the two `L¹` hypotheses force the boundary terms to
   vanish. No counterexample.
2. **Break `lem:duality`(c) by taking `hg ∉ L²`.** `h(ξ) = (1+|ξ|²)^{k/2}`,
   `g ∈ L²` with slowly decaying tails does give `hg ∉ L²` — but the Conventions
   admit exactly this case as a tempered distribution, and `lem:hk` only ever
   asserts `L²` membership after multiplying back down. No defect.
3. **Break `lem:hk`'s converse by local integrability.** `(2πiξ)^α Ff` is
   square integrable on every ball because `ξ^α` is bounded there, so
   `lem:compat`(ii) applies as invoked. No defect.
4. **Attack `lem:plancherel`(iii) with insufficient regularity.** The
   integrability of `(|ξ|Fp)(|ξ|²Fu_i)` is exactly Cauchy–Schwarz on
   `p ∈ H¹ × u ∈ H²`; nothing more is silently used. No defect.
5. **Attack the constant `C_E`.** For `ν = C_S = Y = 1`,
   `f(s) = ½s² − 3s^{3/2} + 2187/32` has `f'(s) = s − 4.5√s = 0` at `s = 20.25`
   and `f(20.25) = 0`: the constant is the exact optimum of the chosen Young
   split, not merely sufficient. No slack to exploit and no error.
6. **Attack the vector Sobolev constant `√m C_S`.** `|f| ≤ Σ|f_k|` then
   Minkowski then Cauchy–Schwarz in `R^m` is tight enough for the claim as
   stated; no smaller claim is made. No defect.
7. **Look for a use of `H^k ↪ L^∞` smuggled into the block.** Only
   `‖u‖_∞` in `lem:R-consequences`(b) and the `L^q` memberships for `q>2`, all
   explicitly consumed from R and declared as such in §4 of the candidate. No
   hidden Sobolev embedding.

---

## 4. REPLACEMENT ARGUMENT

Not applicable: the verdict is PASS and there is no bad bridge to replace. The
concrete integrator repairs are in §6.

---

## 5. CONDITIONAL SUFFIX THAT SURVIVES

**The entire reviewed scope survives unconditionally given package R (D2), i.e.
given `Proposition prop:localtheory` (with `Corollary cor:Lq`) from the
local-theory lane.** Explicitly:

* the import layer `lem:fourier`(S),(L) — two `[DI]` imports at verified
  locations, one of them (the `L¹∩L²` isometry) an exercise-with-complete-hint
  in the cited text and separately machine-checked in Mathlib in its `L²`
  form — and the manuscript-proved `lem:parseval`, `lem:duality`,
  `lem:mollify`, `lem:compat`, `lem:hk`, `lem:div-zero`, `lem:classical`;
* `lem:R-consequences`, `lem:plancherel`, `def:sobolev-constant`,
  `lem:density`, `lem:sobolev` (constant `√m C_S`), `lem:interp`, `lem:GN`;
* `prop:energy` with `eq:energy` and both consequences;
* `prop:scaling` (i)–(iii), `eq:scaling-norm` for all `1 ≤ q ≤ ∞`, `eq:L4L3`
  with constant `3C_S²` and bound `3C_S²‖u_0‖₂^4/(2ν)`; `rem:scaling-pressure`;
  `rem:mismatch`(a),(b);
* `prop:enstrophy` with `eq:enstrophy-identity`, `eq:enstrophy` and
  `C_E = (2187/32)C_S^6`; `prop:ode`; `rem:lean`; `rem:usage`.

Nothing in the scope is conditional on HIGH-PRESSURE, HIGH-STRAIN, ABSORPTION
or CRITICAL. Nothing in the scope survives the failure of R: every proof
consumes it. The only external proof-status residue is the F4 caveat, correctly
recorded by the candidate: the `L¹∩L²` isometry appears in Grafakos as
Exercise 2.2.8 (with a complete hint), and Mathlib's `fourierTransformₗᵢ`
proves the `L²` isometry formally but does not state the a.e. agreement with
the `L¹` integral, so that one clause rests on Grafakos' printed text alone.
This is a labelled import caveat, not a gap in a manuscript-owned proof.

---

## 6. Defects for the integrator

### 6.1 Cross-lane label collisions (splice-blocking; not flagged by the candidate)

Scripted comparison of this block's `\label`s against the LaTeX blocks of the
other CP02 lanes gives three collisions on **different** statements:

| label | this lane | other lane | fix |
|---|---|---|---|
| `lem:duality` | "Duality rules in `S'`" (`(û)^∨=u`, `(∂^α u)^∧=(2πiξ)^α û`, slowly-increasing products) | `cp02-local-theory.md`: "Duality characterisation of `H^k`" (`\|⟨g,φ⟩\| ≤ ‖g‖_{H^k}‖φ‖_{H^{-k}}`) | rename **this lane's** to `lem:sprime-rules` (7 `\ref` sites inside the block); the local-theory label is referenced from its own long proof chain |
| `lem:density` | "`C_c^∞` dense in `H^1`" | `cp02-quotient-functional.md`: "Two density facts" (`L^1_loc` test function lemma; `L²∩L³` dense in `L³`) | rename **this lane's** to `lem:h1-density` (1 `\ref` site) |
| `eq:enstrophy-identity` | `½Y' + ν‖Δu‖₂² = ∫(u·∇)u·Δu` inside `prop:enstrophy` | `cp02-continuation.md` derives the same identity under the same label | this lane owns `prop:enstrophy`, so keep the label here and have the continuation lane `\eqref` it instead of re-deriving; controller/integrator call |

Left unfixed, `pdflatex` emits "Label multiply defined" and one `\ref` in each
pair silently resolves to the wrong theorem. The local-theory lane flagged its
own analogous collision (`lem:pressure-convention` vs `cp02-pressure.md`); this
lane's integrator notes list only the two `\newtheorem` lines and the four
`.bib` entries, and miss all three of the above.

### 6.2 One over-assumption of R, unused

The "Consequences of the local theory" subsection states that it uses
"`u, ∇u, ∇²u, Δu, ∂_tu, p, ∇p ∈ C([0,T];L^q)` for every `2 ≤ q ≤ ∞`". Two
mismatches with the interface:

* **`∇²u` is not in that list anywhere upstream.** D2's parenthetical grants
  `u, ∇u, p, ∇p, Δu, u_t`; `cp02-local-theory.md`'s `cor:Lq` grants
  `u, ∇u, Δu, ∂_tu, p, ∇p`. Neither grants `∇²u ∈ C([0,T];L^q)`. I checked every
  use of `∇²u` in the block (Conventions, `lem:plancherel`(ii), `lem:GN`): all of
  them are `L²` only, and the `L²` membership is *derived* in the block from
  `lem:classical`+`lem:hk`. So the clause is an unnecessary dependency: delete
  `∇²u` from the list, or replace it by "and `∇²u(t) ∈ L²` by
  Lemma `lem:classical`".
* **The `L^q` clause lives in `cor:Lq`, not in `prop:localtheory`.** The
  local-theory lane says explicitly that the E-1/N-1 proofs "should now cite
  `prop:localtheory`(iii),(iv) and `cor:Lq` for the memberships they use". The
  block cites a bare `Proposition~\ref{prop:localtheory}`. D2 authorises that
  citation form, so this is not a bad bridge, but the integrator should upgrade
  it to `Proposition~\ref{prop:localtheory}(iii),(iv)` and
  `Corollary~\ref{cor:Lq}`.

### 6.3 Two inaccurate statements inside the candidate's own record

* §5 EVIDENCE claims the compile had "no overfull box above 20pt". False: the
  candidate's own `scratchpad/cp02r2/test.log` (and my independent splice)
  contain overfull `\hbox`es of **110.7pt, 100.3pt and 93.8pt**, all in
  `rem:lean`, caused by the long unbreakable `\texttt{NavierFormal.…}` names.
  Cosmetic, but the claim as written is not true; fix by wrapping `rem:lean`
  in `\sloppy` or inserting `\allowbreak`/`\-` in the Lean names, and correct
  the record.
* §5 EVIDENCE claims "the only macro the block needed from the preamble beyond
  the theorem environments is `\R`". The block also uses `\norm` 18 times. Both
  macros are already in `main.tex`, so nothing breaks; the statement is simply
  wrong.

### 6.4 Minor editorial issues

1. **F5 pagination.** Grafakos Prop. 2.3.22 spans printed pp. 130–131: item (8)
   is on p. 130, item **(10) is on p. 131** (with the one-sentence proof). The
   table says "p. 130" for both. Write "pp. 130–131".
2. **`lem:classical` notation.** `u_u` (the distribution induced by the function
   `u`) is unreadable. Use a different letter for the function, e.g.
   "let `v ∈ C^∞(R³)` … with `u_v ∈ H^k`".
3. **`lem:classical` hypothesis.** "real-valued" is not used in the proof; drop
   it or say why it is kept (`lem:sobolev` supplies real `u_n` anyway).
4. **`prop:scaling`(ii) "every measurable `u`".** For a merely jointly
   measurable `u`, the slice `u(·,λ²t)` need not be measurable at *every* `t`.
   The clean statement is slice-level: "for every measurable `v : R³ → R^3`,
   `λ > 0` and `1 ≤ q ≤ ∞`, `‖λv(λ·)‖_q = λ^{1−3/q}‖v‖_q`, both sides allowed to
   be `+∞`", then apply it to `v = u(·,λ²t)`.
5. **`def:sobolev-constant`(b).** Name the Mathlib ambient instance explicitly
   (`E = EuclideanSpace ℝ (Fin 3)`, `μ = volume`, `F = ℝ`) so that
   "operator norm of `fderiv ℝ u` = `|∇u|`" and "`eLpNorm … volume` = the
   Lebesgue `L²` norm on `R³`" are pinned rather than left to the reader.
6. **F6's `[DI]` is still only partly earned.** The row lists Hölder, Minkowski,
   Cauchy–Schwarz and Young, but gives verified locations only for Young
   (`MeanInequalities.lean:500`) and two-factor Hölder for `eLpNorm`
   (`CompareExp.lean:300`). Minkowski (the `L^6` triangle inequality in
   `lem:sobolev`) and Cauchy–Schwarz in `R^m`/`L²` have no location. Either add
   `eLpNorm_add_le` and the `L²` Cauchy–Schwarz name, or say in the row that
   these two are used only as the norm axiom and as the `p=q=2` case of the
   Hölder entry.
7. **Two unlocated elementary facts.** The fundamental theorem of calculus
   (`lem:div-zero`, `prop:energy` Step 5) and the mean value theorem
   (`lem:mollify`) are used without appearing in F6/F7. Add them to F7 or state
   that calculus on `R` is not itemised.
8. **`rem:scaling-pressure`.** "So `p = R_iR_j(u_iu_j)` is Tao's normalised
   pressure" is an assertion about Tao's convention with no citation in the
   LaTeX. D1 authorises stating it, and the local-theory lane owns
   `lem:pressure-convention`; point the sentence at that lemma (or add the Tao
   page) rather than leaving it uncited.
9. **`rem:scaling-pressure`, one phrase.** "the change of variables of
   Proposition~\ref{prop:scaling}(ii)" — (ii) is a norm identity; say "the
   substitution `y = λx` used in the proof of (ii)".
10. **`rem:usage` location phrase.** "the converse half of the
    existential-equivalence statement after Hypothesis~\ref{hyp:absorption}" —
    the converse argument is in the paragraph beginning "At these existential
    quantifiers", which follows `hyp:absorption` but concerns
    `hyp:highpressure`. Name `hyp:highpressure` to avoid ambiguity once X-1
    lands.
11. **Fourier/classical `H^k` norms.** The block uses Tao's *Fourier* `H^s`
    norm, while R and Tao's local theory state the *classical* `H^k` norm for
    smooth `u`; Tao says the two are "equivalent up to constants" and the
    block's `lem:hk` in effect proves the membership equivalence. Nothing breaks
    (only `‖v‖₂ ≤ ‖v‖_{H^k}` is used across the interface, valid for both), but
    one sentence saying which norm `C^j([0,T];H^k)` refers to would remove the
    ambiguity for the integrator.
12. **`φ^∨ ∈ S`.** The Conventions cite Rem. 2.2.3, Prop. 2.2.11(11) and p. 125
    for `∂^αφ, hφ, φ̂ ∈ S`; `φ^∨ ∈ S` follows from `φ̂ ∈ S` plus invariance of
    the Schwartz seminorms under `x ↦ −x`, which is not said. One clause.
13. **Unreferenced labels** (harmless; keep for downstream lanes or drop):
    `def:sobolev-constant`, `eq:L4L3-constant`, `eq:LPS`,
    `eq:energy-derivative`, `rem:lean`, `rem:scaling-pressure`, `rem:usage`.
14. **F9's recorded navier-formal HEAD** is `9c8b37d`; the repository is now at
    `e9519e9` (`9c8b37d` is its parent). All eight cited declarations still
    exist at the cited lines, so only the recorded commit is stale.
15. **`references.bib`.** The four new keys (`Grafakos2014`, `Nirenberg1959`,
    `MathlibSobolev`, `MathlibFourier`) are still absent from
    `navier-paper/references.bib`; the entries in the candidate's integrator
    notes are well formed and were used verbatim in my compile check.

---

## 7. UNNECESSARY DEPENDENCIES

* **`∇²u ∈ C([0,T];L^q)` for `q > 2`** (§6.2): assumed, not granted by D2 or
  `cor:Lq`, and never used. Delete.
* **`prop:scaling`(ii) at `q = ∞`**: nothing downstream uses it (only `q = 2, 3`
  and the `L^r_tL^q_x` computation at `q = 3`), and the Lean cross-reference
  `eLpNorm_dilate` covers only `0 < q < ∞`. Keep as completeness; it costs six
  lines and is correct.
* **`lem:hk`'s converse direction**: only the forward direction is consumed by
  `prop:energy`/`prop:enstrophy`, but the converse is what makes `lem:classical`
  and `lem:density` work, so it is load-bearing after all — keep.
* **`lem:fourier`(S) inversion `(f^∨)^∧ = f`**: used only through
  `lem:duality`(a); `(f̂)^∨ = f` alone would do for `lem:duality`(a), but both
  come from the same cited item. Harmless.
* **Nirenberg 1959**: mathematically redundant — the Mathlib statement alone
  establishes `eq:sobolev-cc` and is `[DI]`. Retained as a printed-source
  courtesy, with the "main steps" caveat correctly recorded. Keep.
* **`rem:scaling-pressure`**: feeds no result; retained for D1 consistency. Keep
  as a remark.
* No Calderón–Zygmund theory, no Riesz-transform `L^p` bound, no heat semigroup,
  no Littlewood–Paley theory, no `L^p` uniform convexity, no uniqueness theorem,
  and no Sobolev embedding into `L^∞` is used anywhere in the scope. I read the
  block for each; the candidate's statement to that effect is accurate. The
  `R_iR_j = −Δ^{-1}∂_i∂_j` identity appears only in `rem:scaling-pressure`, at
  the level of the `L²` multiplier symbol, with the computation printed.

---

## 8. NON-CLAIMS (verified, retained)

* No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL or NS-R3 result is asserted or
  approached anywhere in the reviewed scope.
* No bound on `sup_{t<T_*}‖u(t)‖₃` is deduced; `hyp:critical`,
  `hyp:absorption`, `hyp:highpressure` are referenced only as *not* supplied.
* The value of `C_S` is not asserted; only its existence is used.
* `(u_λ, p_λ)` is not asserted to be the classical branch of the rescaled datum.
* Preserved Schwartz decay in time is not used.
* The `L^q` memberships for `q > 2` are consumed from R as D2 states them, not
  proved here; the `L²` memberships of all spatial derivatives are derived.
* This audit certifies no mathematical correctness beyond the reviewed scope, and
  does not certify package R, which belongs to the local-theory lane.

---

## 9. REOPENING CONDITION

The PASS is reopened by any one of:

1. a demonstration that Grafakos' printed statements at pp. 109–110, 112, 113–114
   do not cover a clause of `lem:fourier`(S) or (L) as the lemma states it — I
   read those pages in full and matched clause by clause, so this requires an
   error in my reading, not a new source;
2. a change in the pinned Mathlib checkout (`0df444a360`) that removes or
   renames any of the twenty declarations in F2, F4–F7, since the `[DI]` labels
   are tied to `file:line` in that checkout;
3. the local-theory lane weakening `prop:localtheory`/`cor:Lq` below the D2
   package — in particular dropping `u ∈ C([0,T];L^∞)` (used in
   `lem:R-consequences`(b)) or `u ∈ C([0,T];L^3 ∩ L^4)` (used in
   `lem:R-consequences`(c)), each of which would break `prop:energy` Steps 3–4
   as written;
4. the integrator splicing the block without fixing §6.1, which would leave the
   compiled manuscript with mis-resolving `\ref`s — a defect of the assembled
   paper rather than of this lane's mathematics.

The round-1 blacklisted implication stays blacklisted: nothing beyond the
conventions of Tao pp. 35–36 may be attributed to `Tao2013` in this section.
