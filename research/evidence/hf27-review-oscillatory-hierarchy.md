# HF27 audit — Section 4 (oscillatory family) and Section 5 (approximation hierarchy)

Independent adversarial audit of the frozen candidate
`research/evidence/hf27-critical-residual-continuation.tex`
(SHA-256 `3898e9a020d31c4fc58c9f1289ea4794ec9f787b885086e411b98b0cb1f97488`).
Nothing is promoted. No file outside this one was written.

## Scope

Audited, in the frozen `.tex`:

- **Section 4** (`sec:oscillation`, lines 431–531): `cor:heat` (small critical heat
  orbit), the explicit divergence-free Schwartz family `eq:oscdata` /
  `eq:oscexplicit`, `thm:oscillation`, the frequency-localised heat estimate
  `eq:heatN`, and the explicit threshold `eq:etaN`–`eq:Nthreshold`.
- **Section 5** (`sec:hierarchy`, lines 532–672): the rectangular-cutoff
  subsection and `eq:Jbounds`, `prop:Galerkin`, `eq:ABN`/`eq:CN`, `cor:index`,
  `thm:complete` and `eq:equiv`, and the closing remark.

`thm:certificate` (Section 3) is **used as given**; it is another lane's scope.
Sections 6–8 and the appendix were read only where they interact with the above.

## Verdict

**REPAIR.**

Every mathematical step inside my scope is **correct**. I recomputed the
solenoidality, the Bernstein/Fourier-support estimate, all four constant chains
of `thm:oscillation`, the Galerkin construction, and every step of
`thm:complete`, independently and symbolically, and found no error. Twelve
refutation attempts against the mathematics all failed.

The repair is not to a proof. It is to the **claimed significance and the prior
art of Section 4**, which are wrong in a way that is decidable by a short
computation the document does not perform:

> The family `eq:oscdata` is **not** large data. Its `L^3` norm diverges, but its
> `BMO^{-1}` norm and its `\dot B^{-1+3/p}_{p,q}` norms for every admissible
> `p > 3/(1-α)` **tend to zero** as `N → ∞`. It is therefore a *small-data*
> family in the Koch–Tataru sense and in the sense of the 1994 Cannone–Meyer–
> Planchon/Planchon critical-Besov theory. Its global regularity was available
> in 2001 (in fact 1994), by a strictly easier route, on a **strictly larger**
> parameter range `0 < α < 1` than the certificate reaches (`0 < α < 1/2`).

So Section 4 is a correct proof of a known statement whose only novel element —
that a certificate with a large `L^3` norm can still certify — is an artefact of
choosing `L^3` as the norm in which to measure largeness. That must be said in
the document. It is not said. The one prior-art citation it does carry
(`\cite{CG}`, Chemin–Gallagher) points at the **opposite** regime and makes the
example look stronger than it is.

Section 5 is correct and honestly hedged, but under-reports one consequence of
its own `thm:complete` and under-cites the line of work it reproduces.

---

## 1. The prior-art question, answered first

### 1.1 The scale-invariant norms of `eq:oscdata`

Write, as in `eq:oscexplicit`,

```
U_N = ( N^{α-1} ∂_2φ sin(Nx_1),  −N^α φ cos(Nx_1) − N^{α-1} ∂_1φ sin(Nx_1),  0 ),
```

with `φ̂ ∈ C_c^∞(B_1)` real and even, `N ≥ 2`, `0 < α < 1/2` in the candidate.
`supp Û_N ⊂ B_1(Ne_1) ∪ B_1(−Ne_1)`, so `|ξ| ≥ N−1` on the support and the
support **measure** is `2|B_1|`, independent of `N` — the candidate's own
observation, and the whole engine of the computation below.

**(a) `L^3` (what the candidate measures).** By `eq:cosaverage`
(mean of `|cos|^3` is `4/(3π)`, verified symbolically),

```
‖U_N‖_3  =  (4/(3π))^{1/3} ‖φ‖_3 · N^α · (1 + o(1))  →  ∞ .
```

**(b) `BMO^{-1}` (Koch–Tataru).** With
`‖u_0‖²_{BMO^{-1}} = sup_{x,R} R^{-3} ∫_0^{R²} ∫_{B(x,R)} |e^{tΔ}u_0|² dy dt`,
use `(1/|B|)∫_B f ≤ ‖f‖_∞` and then the candidate's **own** Bernstein bound
`‖f‖_∞ ≤ B_∞‖f‖_2`, `B_∞ = (2π)^{-3/2}(2|B_1|)^{1/2} = 0.183776…`, together with
`‖e^{tΔ}U_N‖_2 ≤ e^{-t(N-1)²}‖U_N‖_2` and `‖U_N‖_2 ≤ L'_φ N^α`,
`L'_φ = ‖φ‖_2 + ‖∂_1φ‖_2 + ‖∂_2φ‖_2`:

```
‖U_N‖²_{BMO^{-1}}  ≤  (4π/3) ∫_0^∞ ‖e^{tΔ}U_N‖_∞² dt
                   ≤  (4π/3) B_∞² L'_φ² N^{2α} / (2(N−1)²)
                   ≤  (4π/3) B_∞² L'_φ² · 2 N^{2α−2}          (N ≥ 2),
```

that is

```
   ‖U_N‖_{BMO^{-1}}  ≤  0.532 · L'_φ · N^{α−1}   ⟶  0   for every α < 1.
```

This is a complete rigorous proof, three lines, using nothing the candidate does
not already display. (`BMO^{-1}` is defined with the unit-viscosity semigroup, as
in Koch–Tataru; the viscosity enters only through the threshold, since
`u ↦ ν^{-1}u(·/ν, ·)` turns the `ν`-equation into the `ν = 1` equation and the
smallness condition into `‖u_0‖_{BMO^{-1}} < εν`.) The bound is **sharp in the
exponent**: since
`‖·‖_{Ḃ^{-1}_{∞,∞}} ≲ ‖·‖_{BMO^{-1}}` and
`sup_t t^{1/2}‖e^{tΔ}U_N‖_∞ ≍ N^α · N^{-1}(2e)^{-1/2}‖φ‖_∞`, the true size is
`‖U_N‖_{BMO^{-1}} ≍ N^{α−1}`.

**(c) The critical Besov ladder.** Using
`‖u_0‖_{Ḃ^{-s}_{p,r}} ≍ ‖ t^{s/2}‖e^{tΔ}u_0‖_p ‖_{L^r(dt/t)}` with
`s = 1 − 3/p`, and `‖e^{tΔ}U_N‖_p ≍ N^α e^{-tN²}` on `t ≲ N^{-2}`:

```
‖U_N‖_{Ḃ^{-1+3/p}_{p,r}}  ≍  c_{φ,p,r} · N^{α − 1 + 3/p}     (1 ≤ r ≤ ∞).
```

So the family is **small in `Ḃ^{-1+3/p}_{p,r}` as soon as `p > 3/(1−α)`**, for
every `0 < α < 1`. At `p = 6` the exponent is `α − 1/2`.

**(d) The candidate's own quantity `η`.** `eq:eta` is exactly a critical Besov
norm in disguise:

```
η = ν^{-3} ∫_0^∞ ‖e^{νtΔ}u_0‖_6^4 dt = ν^{-4} ‖u_0‖_{Ḃ^{-1/2}_{6,4}}^4 ,
```

so `cor:heat` says precisely *"`‖u_0‖_{Ḃ^{-1/2}_{6,4}} ≲ ν`"*. For the family,
`η_N ≍ c_φ ν^{-4} N^{4α−2}` — **two-sided**, not just the upper bound `eq:etaN`.

**Numerical confirmation.** A spectral computation of the heat orbit of the
**exact** vector field `eq:oscexplicit` (separable envelope `φ = φ_1φ_2φ_3`, so
the heat semigroup factorises and the 3-D `L^p` norms reduce to quadrature over
1-D arrays; a 1-D model on a much finer grid, `2^18` points, `N ≤ 256`, agrees)
reproduces every exponent to three decimals. Measured `log₂` slope per doubling
of `N`, `N ∈ {16,32,64,128}`:

| quantity | predicted | `α = 0.25` | `α = 0.70` |
|---|---|---|---|
| `‖U_N‖_3` | `+α` | `+0.250` | `+0.700` |
| `‖U_N‖_{Ḃ^{-1}_{∞,∞}}` | `α − 1` | `−0.750` | `−0.300` |
| `(∫_0^∞‖e^{tΔ}U_N‖_∞²dt)^{1/2}` (`BMO^{-1}` upper bd) | `α − 1` | `−0.750` | `−0.300` |
| `‖U_N‖_{Ḃ^{-1/2}_{6,∞}}` | `α − 1/2` | `−0.250` | **`+0.200`** |
| `‖U_N‖_{Ḃ^{-3/4}_{12,∞}}` | `α − 3/4` | `−0.500` | `−0.050` |
| `‖e^{tΔ}U_N‖_{L^4_tL^6_x} = ν η_N^{1/4}` | `α − 1/2` | `−0.250` | **`+0.200`** |

The `α = 0.70` column is the whole of R4 in one line: the candidate's own
quantity `η_N` **grows** (slope `+0.200 > 0`), so `cor:heat` and hence
`thm:oscillation` fail there — while the `BMO^{-1}` and `Ḃ^{-3/4}_{12,∞}` norms
still tend to zero, so Koch–Tataru and the `p = 12` Besov theorem still certify.

### 1.2 What is already known

- **Koch–Tataru (Adv. Math. 157 (2001) 22–35).** There is `ε > 0` such that
  `‖u_0‖_{BMO^{-1}} < εν` gives a global solution, regular for `t > 0`. Statement
  confirmed verbatim from Germain–Pavlović–Staffilani, arXiv:math/0609781
  (opening sentence of the abstract, directly inspected this session); the repo's
  own `literature/critical-criteria.md` records the same.
  → **covers `eq:oscdata` for every `0 < α < 1`.**
- **Cannone–Meyer–Planchon / Planchon (1994–96).** Small data in
  `Ḃ^{-1+3/p}_{p,q}`, `3 < p ≤ q < ∞`, gives `T* = ∞`. Bibliographic identity of
  Cannone–Meyer–Planchon, *Solutions auto-similaires des équations de
  Navier–Stokes*, Sém. Goulaouic–Schwartz 1993–94, exp. no. 8, pp. 1–10,
  confirmed on Numdam (`SEDP_1993-1994____A8_0`) — **metadata only**, the paper
  body was not retrieved. The theorem statement itself is recorded in the repo as
  a **directly inspected** source (Gallagher–Koch–Planchon preliminaries, per
  `literature/critical-criteria.md`, which also attributes the local theory to
  Cannone for `3 < p ≤ 6` and Planchon in general). *My own re-verification
  attempt against `arxiv.org/html/1012.0145` this session did not surface that
  passage; I therefore rest the `α < 1` claim on Koch–Tataru, which I did verify
  independently, and treat the Besov route as corroboration.*
  → **covers `eq:oscdata` for every `0 < α < 1`, taking `p = q > 3/(1−α)`;**
  and at `p = q = 6` it already covers the candidate's whole range `α < 1/2`.
- **Chemin–Gallagher — the citation the document actually carries.** From the
  arXiv abstract of `\cite{CG}` (arXiv:math/0508374), directly inspected:

  > "This condition is not a smallness condition on the initial data, as the data
  > is allowed to be **arbitrarily large in the scale invariant space
  > `B^{-1}_{∞,∞}`, which contains all the known spaces in which there is a
  > global solution for small data**."

  Their `\R^3` companion (arXiv:math/0611044, Ann. IHP 2009) makes the same point
  — data "arbitrarily large in `C^{-1}`" satisfying a **nonlinear** smallness
  condition — and Chemin–Gallagher–Paicu (arXiv:0807.1265, Ann. of Math. 173
  (2011)) extends it to slowly varying, ill-prepared data.

  The candidate's family is **the exact opposite**: `‖U_N‖_{Ḃ^{-1}_{∞,∞}} → 0`.
  It satisfies the *linear* smallness condition that Chemin–Gallagher's entire
  programme exists to escape.

### 1.3 Answer

1. **Is the family already covered by existing results?** **Yes**, and by results
   older and weaker in hypothesis than Chemin–Gallagher: Cannone–Meyer–Planchon/
   Planchon (1994–96) and Koch–Tataru (2001). Not by Chemin–Gallagher, but that
   is *worse* for the candidate, not better: the family sits strictly *below*
   Chemin–Gallagher on the small-data side.
2. **Is it global for a trivial reason — a large critical norm that is small in
   `BMO^{-1}`/Besov?** **Yes, exactly that.** `‖U_N‖_{BMO^{-1}} ≍ N^{α−1} → 0`.
   This is the single most important finding in my scope. The family is a
   textbook illustration that oscillation makes `L^3` a bad measure of size, not
   an example of large-data global existence.
3. **Is it global for a reason independent of the certificate?** **Yes.** The
   three-line `BMO^{-1}` bound in §1.1(b) uses only the candidate's own
   `eq:heatN` ingredients and then invokes a 2001 theorem. None of `thm:certificate`,
   `Q`, `D`, `r_*`, `c_b` or the quotient machinery is needed.
   *One caveat, stated honestly:* transferring "the Koch–Tataru solution is
   global" to "the selected maximal classical Schwartz branch has `T_* = ∞`"
   needs the standard uniqueness/identification of mild and strong solutions in
   `C([0,T);L^3)` — the same identification the manuscript already relies on to
   import `eq:endpoint`. I did not re-audit that identification; it is not in
   doubt, but it is an input, not a triviality.
4. **Comparative strength.** The certificate route, as demonstrated, is **strictly
   weaker on its own test family**: `cor:heat` needs `η_N → 0`, i.e. `α < 1/2`,
   because `η_N ≍ c_φ ν^{-4} N^{4α−2}` two-sidedly; Koch–Tataru and the
   large-`p` Besov theorem reach every `α < 1`. The band `1/2 ≤ α < 1` is
   certified by 1994/2001 theory and **not** by the candidate's demonstrated
   route at fixed `ν`.
5. **Is the document's disclaimer adequate?** Partly. It does disclaim novelty
   ("a test of this certificate, not a novelty claim") and it does say the result
   is "a smallness result in a different, critical heat-orbit quantity". It does
   **not** say that this quantity is a named critical Besov norm, that the family
   is small in *every* critical space where small-data theory exists, or that the
   test is strictly weaker than 1994 theory on the very family it tests. The
   remaining impression — a certificate with independent reach on large data — is
   not supported.

---

## 2. Per-question findings

### 2.1 `thm:oscillation` — mathematics: **correct**

- **Solenoidal.** `curl(0,0,ψ) = (∂_2ψ, −∂_1ψ, 0)`; `eq:oscexplicit` follows
  verbatim from `ψ = N^{α−1}φ sin(Nx_1)`. Divergence-free because it is a curl. ✓
- **Real and Schwartz.** `φ̂` real even `C_c^∞` ⇒ `φ` real Schwartz (and
  real-analytic); a Schwartz function times `sin/cos` and its derivatives are
  Schwartz. ✓
- **`‖U_N‖_3 → ∞`.** `eq:cosaverage`'s constant `4/(3π)` verified symbolically.
  The triangle-inequality split (leading term `≳ c_φ N^α`, derivative terms
  `≲ N^{α−1}(‖∂_1φ‖_3 + ‖∂_2φ‖_3)`) is valid. ✓
  *Minor precision point:* `eq:cosaverage` is a limit, so "bounded below by
  `c_φ N^α`" holds for `N ≥ N_0(φ)` only. The regularity threshold
  `eq:Nthreshold` does **not** also certify largeness; two different thresholds
  are involved. Harmless, since the theorem says "sufficiently large `N`".
- **`eq:heatN`.** `‖f‖_∞ ≤ (2π)^{-3/2}|supp f̂|^{1/2}‖f‖_2` (Cauchy–Schwarz +
  Plancherel, valid for vectors via the Euclidean modulus). `‖f‖_6 ≤
  ‖f‖_∞^{2/3}‖f‖_2^{1/3} ≤ B_∞^{2/3}‖f‖_2`. `‖U_N‖_2 ≤ N^α L'_φ`. Support in
  two unit balls about `±Ne_1`, disjoint for `N ≥ 2`, measure `2|B_1|`, `|ξ| ≥
  N−1`. Every step checks. `B_∞ = 0.183776`, `B_∞^{2/3} = 0.323241`. ✓
- **`eq:etaN`.** `η_N ≤ L_φ^4 N^{4α}/(4ν^4(N−1)²)`; the reduction to
  `L_φ^4 ν^{-4} N^{4α−2}` is exactly the condition `N ≥ 2` (sympy: `N² ≤ 4(N−1)²
  ⟺ N ≥ 2`). ✓
- **`eq:etastar`, `eq:Nthreshold`.** Verified symbolically:
  `exp(c_b·(3 log2/c_b)/3) = 2` and `4·3^{-1/3}·((3^{1/3}r_*/8)²)^{1/2} = r_*/2`,
  so the displayed chain `2·3^{-1/3}√η_N e^{c_bη_N/3} ≤ 4·3^{-1/3}√η_* ≤ r_*/2 <
  r_*` is exact. The inversion `N ≥ (L_φ^4ν^{-4}/η_*)^{1/(2−4α)}` is the exact
  solution of `L_φ^4ν^{-4}N^{4α−2} = η_*`. ✓
- **Where `α < 1/2` is used, and whether it is sharp.** Used at exactly one
  place: `4α − 2 < 0` in `eq:etaN`, so that `η_N → 0`. It is **sharp for the
  route** (`η_N ≍ ν^{-4}N^{4α−2}` from below as well, confirmed numerically:
  slope `α − 1/2` for `η^{1/4}`), and **not sharp for the conclusion** (all
  `α < 1` are globally regular by §1.2). The document neither claims nor denies
  sharpness; the omission is what lets the restriction read as intrinsic.
- **"Explicit" threshold.** `eq:Nthreshold` is explicit *modulo* `r_*` and `c_b`,
  which depend on `C_3, C_{9/2}, C_9` (Leray-projection `L^p` norms, sharp values
  unknown) and `S`. The document discloses this at `eq:constants2`/`eq:rstar`.
  No number is produced, and I did not produce one.

### 2.2 `cor:heat` — **correct, and a re-proof of classical theory**

Verified line by line: `v = e^{νtΔ}u_0` is an admissible comparison per
`def:comparison`; `v(0) = u_0` so `Q_0 = 0`; `R_v = ℙ div(v⊗v)` since
`v_t = νΔv` and `div v = 0`; `‖v⊗v‖_3 = ‖v‖_6²` (Frobenius); `M_H ≤ c_b η`;
`‖F‖²_{L²L³} ≤ ν³η`; hence

```
Z̄_H/ν ≤ e^{c_bη/3} · 2·3^{-1/3} · √η ,
```

which is `eq:heatcriterion` exactly. `sup_t‖v(t)‖_3 ≤ ‖u_0‖_3` by Young. ✓

**But** `η = ν^{-4}‖u_0‖^4_{Ḃ^{-1/2}_{6,4}}` (§1.1(d)), and
`Ḃ^{-1/2}_{6,4} ↪ Ḃ^{-1/2}_{6,6}` with constant `1`. So the hypothesis of
`cor:heat` **implies** the hypothesis of the classical small-data theorem in
`Ḃ^{-1+3/p}_{p,q}` at `p = q = 6`, with a **worse** constant (the candidate's
threshold carries `r_*`, `c_b` and an exponential; the classical one does not).
`cor:heat` is therefore a strictly weaker special case of a known theorem, proved
by a new mechanism. That is a legitimate thing to do; it must be labelled.

### 2.3 `prop:Galerkin` and the rectangular cutoff — **correct**

- **Existence for every datum: yes.** On the closed real solenoidal subspace of
  `L²` with `supp v̂ ⊂ [−N,N]³`, `Δ` is bounded (`|ξ|² ≤ 3N²`) and
  `‖J_Nℙdiv(v⊗v)‖_2 ≤ √3N‖v⊗v‖_2 ≤ CN^{5/2}‖v‖_2²` by Bernstein
  (`‖v‖_∞ ≤ (2π)^{-3/2}(2N)^{3/2}‖v‖_2`). Picard + the a-priori `L²` bound gives
  a **global** solution for every `N` and every `u_0`. Reality and solenoidality
  are preserved because `1_{[−N,N]³}` and the Leray symbol are real and even and
  `ℙ` maps into the divergence-free subspace. ✓
- **Energy `eq:Genergy`.** `⟨J_Nℙdiv(v⊗v),v⟩ = ⟨div(v⊗v), ℙJ_N v⟩ =
  −½∫ v_j∂_j|v|² = 0`. Equality, not inequality. ✓
- **Residual `eq:FN`.** `R_{v_N} = (I−J_N)ℙdiv(v_N⊗v_N) = ℙ div F_N` with
  `F_N = (I−J_N)(v_N⊗v_N)`, since `J_N, ℙ, div` are commuting Fourier
  multipliers. ✓
- **Admissibility as a comparison.** `v_N` is band-limited in `L²`, hence in
  every `H^k`; the vector field is a polynomial, hence `C^∞` in time; `H^1 ↪ L^3`
  gives the `L^3` continuity `thm:certificate` Step 4 needs. `A_N, B_N` are finite
  for fixed `N, H` by Bernstein (`‖v_N‖_6 ≤ CN^{1/2}E_0^{1/2}`). ✓
- **Why rectangular, not radial: the reason given is right but understated.**
  `1_{[−N,N]³}` is a tensor product of three one-dimensional interval multipliers,
  each a combination of modulated Hilbert transforms, hence bounded on `L^p`,
  `1<p<∞`, with a constant independent of `N` (by dilation invariance, in fact
  equal to the `N = 1` constant). `J_Nf → f` in `L^p` by density. All correct.
  The document says of the ball cutoff only that "its `L^p` behavior cannot be
  inferred from its orthogonality on `L²`". The truth is stronger and is a
  theorem: **Fefferman (1971) proved the ball multiplier is unbounded on `L^p`
  for every `p ≠ 2`.** As written the sentence reads as an ignorance claim about
  a possibly-true statement. See R5.
- **The infinite-dimensionality remark** is correct and important, and it is the
  document's own. It is also the point at which the `\R^3` transplant becomes
  strictly *less* operational than CCRT's torus version — see R6.

### 2.4 `cor:index` — **correct**

`Q_0^{2/3} ≤ 3^{-2/3}d_N²` from `Q(a) ≤ ‖a‖_3³/3`; `M_H = c_bν^{-3}A_N(H)`;
`‖F‖²_{L²L³} = B_N(H)`; hence `Z̄_H² ≤ 𝔠_N` and `𝔠_N < r_*²ν²` gives
`Z̄_H < r_*ν`, and `Z_H ≤ Z̄_H` because `e^{-2M(s)/3} ≤ 1`. ✓
The initial error is `(I−J_N)u_0`, solenoidal and in `L^3`. ✓

### 2.5 `thm:complete` — **correct; both of the document's self-assessments hold**

Every step recomputed:

- `eq:product`: `(a·∇)a − (b·∇)b = ((a−b)·∇)a + (b·∇)(a−b)` with the `H^{m-1}`
  algebra property (`m ≥ 3 ⇒ m−1 > 3/2`). ✓
- `h_N(0) = J_Nu_0 − J_Nu_0 = 0`; `eq:hPDE` is the correct subtraction; `h_N` is
  divergence-free and band-limited, so `ℙh_N = J_Nh_N = h_N` and the duality
  pairing `|⟨J_Nℙg, h_N⟩_{H^m}| ≤ ‖g‖_{H^{m-1}}‖h_N‖_{H^{m+1}}` is legitimate. ✓
- `‖h_N‖²_{H^{m+1}} = W + X` exactly, with `X = ‖∇h_N‖²_{H^m}`. ✓
- `eq:tail`: outside `[−N,N]³` one has `|ξ| ≥ N` (max-coordinate ⇒ Euclidean), so
  `(1+|ξ|²)^{-k/2} ≤ N^{-k}`. ✓
- Young with `ε = ν/2` and `(√W + θ)² ≤ 2(W + θ²)` gives exactly
  `W' ≤ AW + (2B²/ν)‖θ_N‖²`, `A = ν + 2B²/ν`; Grönwall from `W(0)=0` gives
  `eq:convergence`; the first-exit closes the `W ≤ 1` bootstrap. ✓
- Step 3: `H^m ↪ L^6` gives `A_N → ∫‖u‖_6^4`; the `F_N` split with `(1+B_3)` is
  correct; `t ↦ u⊗u` is continuous `[0,H] → L^3` hence has compact image, and
  uniformly bounded operators converging strongly to `0` converge uniformly on
  compacta; `d_N → 0` from `eq:Jbounds`. Hence `B_N → 0`, `d_N → 0`, `A_N →`
  finite, so `𝔠_N → 0`. ✓

**Claim A — "eventual certification is proved only in the regular case": TRUE.**
Step 2 uses `U_m = sup_{t≤H}‖u(t)‖_{H^m}` and `U_{m+k}`, finite only because
`T_* > H` puts `[0,H]` inside a compact subinterval of `[0,T_*)`. Remove that and
`B`, `A`, and the right-hand side of `eq:convergence` are undefined. There is no
disguised unconditional bound anywhere in the proof.

**Claim B — "the high-regularity convergence proof is unavailable at a
hypothetical singular endpoint": TRUE, and in the strongest possible sense.**
`eq:equiv` is a genuine two-way equivalence (⟸ is `cor:index`, ⟹ is
`eq:CNzero`). Hence any unconditional proof that some `𝔠_N` is small would prove
`T_* > H` for every Schwartz datum and every horizon, i.e. would settle NS-R³.
The unavailability is therefore not a gap in the write-up but a restatement of
the open problem.

**Vacuity: no.** The hypothesis `T_* > H` is satisfiable for every Schwartz datum
(small `H`), and the conclusion `𝔠_N → 0` is a non-trivial quantitative
statement. `thm:complete` is a real theorem.

**The consequence the document does not state.** Combining `cor:index` and
`thm:complete`: for the selected classical branch, for every `ν, u_0, H`,

```
   T_* > H   ⟺   ∃ admissible comparison v on [0,H] with a stress
                 representation and Z_H < r_* ν .
```

Both directions are proved *inside the document*. So `eq:certsmall` is
**existentially equivalent** to the target, not a weaker hypothesis. The
document's Section-5 remark says this for the index criterion ("Existence of a
successful index is equivalent to continuation, not an already proved weaker
hypothesis") but the corresponding statement about `eq:certsmall` itself is left
implicit. Note the ⟹ direction does not even need `prop:Galerkin` or
`thm:complete`: if `T_* > H` then `v = u` is admissible on the closed `[0,H]` and
gives `Z_H = 0`. `thm:complete`'s real added content is only that the *canonical
band-limited* hierarchy realises the equivalence — which is exactly the CCRT
content. (The document's own remark after `thm:certificate` correctly blocks the
illegitimate variant, `v = u` on a *shorter* interval.)

### 2.6 Circularity — **none found in my scope**

- `cor:index` is unconditional: `v_N` exists for every datum with no regularity
  assumption (`prop:Galerkin`), `A_N, B_N, d_N` are determined by `v_N` alone, and
  `thm:certificate` is applied to `v_N` with no input about `u` beyond the
  imported local theory and `eq:endpoint`. The certification does **not** assume
  the regularity it certifies.
- `thm:complete` assumes regularity, but says so in its hypothesis, its title, its
  subsection heading, and its closing remark. That is conditionality, not
  circularity.
- The bootstrap in `thm:complete` Step 2 is a first-exit argument on `W ≤ 1` with
  `W(0) = 0` and a bound independent of the bootstrap assumption — sound.
- The residual circularity risk in the programme is not logical but *rhetorical*:
  because `eq:certsmall ⟺ T_* > H`, the hierarchy cannot be a reduction. The
  document says this; the audit confirms it.

---

## 3. Repairs

**R1 (required, Section 4).** Add the scale-invariant norm computation of
§1.1 to Section 4 and state its conclusion: `‖U_N‖_{BMO^{-1}} ≍ N^{α−1} → 0` and
`‖U_N‖_{Ḃ^{-1+3/p}_{p,q}} ≍ N^{α−1+3/p} → 0` for `p > 3/(1−α)`. Replace the
framing "arbitrarily large oscillatory data" with the accurate one: *large in
`L^3`, small in every critical space in which a small-data global theorem is
known*. Three lines from `eq:heatN` suffice (§1.1(b)).

**R2 (required, Section 4 and bibliography).** `\cite{CG}` is the wrong prior-art
pointer for this family: Chemin–Gallagher's data are *arbitrarily large in
`B^{-1}_{∞,∞}`* and their smallness condition is nonlinear; `eq:oscdata` is small
in `B^{-1}_{∞,∞}` and satisfies the *linear* condition. Cite Koch–Tataru,
*Well-posedness for the Navier–Stokes equations*, Adv. Math. 157 (2001) 22–35,
and the Cannone–Meyer–Planchon/Planchon critical-Besov small-data theory, and say
that these already give the family. Keep `\cite{CG}` only where the document
discusses genuinely large data.

**R3 (required, `cor:heat`).** State that `η = ν^{-4}‖u_0‖^4_{Ḃ^{-1/2}_{6,4}}`,
so `eq:heatcriterion` is a (constant-wise weaker) special case of the classical
`Ḃ^{-1+3/p}_{p,q}` small-data theorem at `p = q = 6`. Present `cor:heat` as a
re-derivation of a known criterion by the quotient mechanism, not as a new
criterion.

**R4 (required, `thm:oscillation`).** Say where `α < 1/2` comes from and that it
is sharp only for the route: `η_N ≍ c_φ ν^{-4}N^{4α−2}` two-sidedly, so `cor:heat`
fails at fixed `ν` for `α ≥ 1/2`, whereas Koch–Tataru (and the large-`p` Besov
theorem) certify the whole range `0 < α < 1`. State plainly that on its own test
family the certificate's *demonstrated route* (`cor:heat` with the heat
comparison) is **strictly weaker** than 1994/2001 theory. (`thm:certificate`
itself is not weaker — but only because `v = u` certifies everything once
regularity is known, which is precisely why it has no independent reach.) Without this,
the section's status as "a complete positive test" is misleading.

**R5 (recommended, Section 5).** In "Why the cutoff is rectangular", replace "its
`L^p` behavior cannot be inferred from its orthogonality on `L²`" with the
theorem: the ball multiplier is **unbounded** on `L^p` for every `p ≠ 2`
(C. Fefferman, *The multiplier problem for the ball*, Ann. of Math. 94 (1971)
330–336). The current wording claims ignorance where a known negative result
applies. *(I confirmed the attribution from memory and the standard record; I did
not fetch the paper this session — see §6.)*

**R6 (recommended, Section 5 prior art).** The document cites `\cite{CCRT}` for
"robustness and conditional eventual verification". CCRT's abstract, directly
inspected, also contains the *third* result the candidate reproduces: "if a strong
solution of the exact problem exists then this can be verified numerically using
an algorithm that can be guaranteed to terminate in a finite time" — i.e.
`cor:index` + `thm:complete` combined. Say so. Add the follow-up line
(Dashti–Robinson 2008 at minimum; located this session only through the abstract
of Hajduk–Robinson–Sadowski, arXiv 2019, which names "Chernyshenko et al. (2007)
and Dashti & Robinson (2008)"). Also draw the comparative conclusion the
infinite-dimensionality remark implies but does not state: because the `\R^3`
band-limited space is infinite-dimensional, this version is **strictly less
operational** than CCRT's, which is a finite-dimensional computable check.

**R7 (recommended, Section 5).** State the equivalence explicitly as a corollary:
`eq:certsmall` holds for some admissible comparison `⟺ T_* > H`, both directions
proved in the document, and the ⟹ direction is immediate from `v = u`. This is
the honest reading of the document's own results and should not be left to the
reader. It also settles, in the affirmative, the controller note's "existential
status of `eq:certsmall`" question.

**R8 (minor, `thm:oscillation`).** `eq:cosaverage` is asymptotic, so the `L^3`
lower bound `c_φ N^α` needs its own `N_0(φ)`, distinct from the regularity
threshold `eq:Nthreshold`. Either give both thresholds or say that
`eq:Nthreshold` certifies regularity only.

**R9 (minor, wording).** The claim that `eq:Nthreshold` is "determined explicitly
… in terms of `ν, φ, α` and the fixed analytic constants" is accurate but should
not be read as numerical: `r_*` and `c_b` depend on the unknown sharp
`L^p` norms of the Leray projection. The document already says this at
`eq:constants2`; a cross-reference from `thm:oscillation` would prevent misreading.

---

## 4. Refutation attempts and outcomes

| # | Attempt | Outcome |
|---|---|---|
| A1 | `eq:oscdata` is not solenoidal / not real / not Schwartz | **Failed.** `curl(0,0,ψ)` is exactly `eq:oscexplicit`; `φ̂` real even `C_c^∞` ⇒ real Schwartz; Schwartz × bounded-smooth-with-bounded-derivatives is Schwartz. |
| A2 | The Bernstein constant `B_∞` or the `L^6` interpolation in `eq:heatN` is wrong, or the Fourier support/measure claim fails | **Failed.** Recomputed: `B_∞ = (2π)^{-3/2}(2|B_1|)^{1/2} = 0.183776`, `B_∞^{2/3} = 0.323241`; `‖f‖_6 ≤ ‖f‖_∞^{2/3}‖f‖_2^{1/3}`; supports disjoint for `N ≥ 2`, measure `2|B_1|`, `|ξ| ≥ N−1`. |
| A3 | The constant chain `eq:etaN → eq:etastar → eq:Nthreshold` breaks | **Failed.** sympy-verified: `N² ≤ 4(N−1)² ⟺ N ≥ 2`; `exp(c_b(3log2/c_b)/3) = 2`; `4·3^{-1/3}(3^{1/3}r_*/8) = r_*/2`; the threshold is the exact inversion. |
| A4 | The periodic-average constant in `eq:cosaverage` is wrong | **Failed.** `(1/2π)∫_0^{2π}|cos|³ = 4/(3π)` (sympy). |
| A5 | **The family is small in a scale-invariant norm, so it is a disguised small-data case** | **SUCCEEDED.** `‖U_N‖_{BMO^{-1}} ≤ 0.532 L'_φ N^{α−1} → 0`, `≍ N^{α−1}`; `‖U_N‖_{Ḃ^{-1+3/p}_{p,q}} ≍ N^{α−1+3/p}`. Proved from the candidate's own `eq:heatN` ingredients; confirmed numerically on the exact field for `α ∈ {0.25, 0.70}`, `N ≤ 128` (3-D) and `α ∈ {0.25,0.49,0.75,0.95}`, `N ≤ 256` (1-D model). |
| A6 | **`α < 1/2` is not sharp for the conclusion** | **SUCCEEDED.** `η_N ≍ ν^{-4}N^{4α−2}` two-sidedly (measured slope of `η_N^{1/4}`: `−0.250` at `α = 0.25`, `+0.200` at `α = 0.70`) ⇒ the route dies at `α = 1/2`; Koch–Tataru covers `α < 1` (measured `BMO^{-1}` slope `−0.300` at `α = 0.70`). `[1/2,1)` is known-regular and not reached by the demonstrated route. |
| A7 | `prop:Galerkin` fails for some datum, or `v_N` is not an admissible comparison, or `A_N/B_N` are infinite | **Failed.** Global existence for every `u_0` and `N`; band-limitation gives every `H^k` and `L^3` continuity; `A_N, B_N ≤ C N²E_0²H`. |
| A8 | `thm:complete` Step 2 or 3 has a hole (product estimate, tail bound, Grönwall, uniform convergence on the compact image) | **Failed.** Every step recomputed and correct, including `‖h‖²_{H^{m+1}} = W+X` and the `ε/3` uniform-convergence argument. |
| A9 | `cor:index` secretly needs the regularity it certifies | **Failed.** `v_N` is unconditional; no quantity in `𝔠_N` refers to `u`. |
| A10 | `thm:complete` is vacuous, or `eq:equiv` is not a genuine equivalence | **Failed** on vacuity (hypothesis satisfiable, conclusion non-trivial); **succeeded** in the weaker sense that the equivalence makes the criterion existentially equivalent to the target and hence not a reduction — which the document itself concedes. |
| A11 | The cube multiplier is not uniformly `L^p`-bounded, or `J_Nf → f` fails | **Failed.** Tensor product of modulated Hilbert transforms; constant independent of `N` by dilation invariance; density + uniform bound gives strong convergence. |
| A12 | `Z_H ≤ Z̄_H` fails so `cor:index` may not feed `thm:certificate` | **Failed.** `M` is non-decreasing so `e^{-2M(s)/3} ≤ 1`. |

---

## 5. Controller errors in `hf27-critical-residual-continuation.md`

1. **"an explicit real solenoidal Schwartz family with *unbounded* critical
   norm"** ("What it claims", item 2; repeated in the Frontier record as "one
   positive certification of an unbounded-critical-norm data family"). This is
   true only of `L^3`. The family's `BMO^{-1}` and `Ḃ^{-1}_{∞,∞}` norms tend to
   **zero**, and so do its `Ḃ^{-1+3/p}_{p,q}` norms for `p > 3/(1−α)`. As written
   the note asserts largeness on the critical scale, which is false. Fix: "large
   in the critical `L^3` norm, small in `BMO^{-1}`".
2. **"Its prior-art posture is better than its predecessors'… It names Chemin and
   Gallagher for oscillatory large data … the audit should verify it is
   substantive rather than decorative."** Verified: on this point it is
   **decorative**. The cited paper is in the opposite regime, and the two
   citations that do cover the family (Koch–Tataru; Cannone–Meyer–Planchon /
   Planchon) are absent from the bibliography. The CCRT citation, by contrast, is
   substantive — though incomplete (R6).
3. **"how it stands against Chemin–Gallagher, whose oscillatory global existence
   results may already cover it"** (audit question). Answer: Chemin–Gallagher do
   **not** cover it, and that is a negative finding, not a positive one — the
   family lies strictly on the small-data side that Chemin–Gallagher's programme
   was built to leave behind. The note should record the corrected question.
4. **The "existential status" question is settled by material in my scope.**
   `cor:index` + `thm:complete` prove `eq:certsmall ⟺ T_* > H`. The note's newer
   paragraph ("it *proves* the certificate hypothesis equivalent to the target …
   taking the comparison flow to be the solution itself makes the critical
   quantity vanish") is **correct**, and I confirm it independently; note only
   that the `v = u` step is legitimate exactly because the ⟹ direction assumes
   `T_* > H` — the document's own remark correctly forbids the shorter-interval
   variant.
5. **No error found** in the note's statements about `thm:complete`/`cor:index`
   being conditional; both of the document's self-assessments hold (§2.5).

---

## 6. What I did **not** check

- `thm:certificate` and all of Section 3 (`prop:identity`, `lem:three`, the Young
  step, the first-exit argument, the constants `Ĉ_♯, c_q, b, c_b, r_*`) — used as
  given; another lane's scope. If that theorem is wrong, `cor:heat`,
  `thm:oscillation` and `cor:index` all fall with it.
- Section 2 (`lem:basic`, `lem:import`, `prop:weighted`) and the appendix.
- Sections 6–8 (`prop:weakresidual`, `thm:concentration`, `cor:weaksmall`,
  `cor:necessary`) beyond reading them for interaction with my scope.
- **Primary texts.** I read only abstract/metadata pages, per the no-PDF
  constraint: Chemin–Gallagher arXiv:math/0508374 and math/0611044,
  Chemin–Gallagher–Paicu arXiv:0807.1265, CCRT arXiv:math/0607181,
  Germain–Pavlović–Staffilani arXiv:math/0609781, Numdam `SEDP_1993-1994____A8_0`.
  I did **not** read Koch–Tataru, Cannone–Meyer–Planchon, CCRT, or Fefferman in
  full, and I did not verify the candidate's assertion that the CCRT version it
  inspected "works on a periodic cube in high Sobolev regularity" (the abstract
  does not state the domain).
- Whether `eq:oscdata` appears verbatim in the literature as a named example. I
  established that it is *covered* by known theorems, not that the specific
  formula is published. Raugel–Sell, Iftimie, and Gallagher–Iftimie–Planchon (thin
  domains / large data by anisotropy) were **not** examined: the session's
  WebSearch budget was exhausted before I could reach them, and they are a
  different mechanism (anisotropy, not oscillation) from the one that settles
  this family.
- Numerical values for `S, C_3, C_{9/2}, C_9, r_*, c_b`, and hence no concrete
  number for `eq:Nthreshold`.
- No Lean/formal check; no attempt to reproduce `v_N` numerically.
- The 3-D norm computation used a **separable** envelope `φ = φ_1φ_2φ_3` (Fourier
  support in the unit cube rather than the unit ball). This changes constants
  only, not the `N`-exponents, because the heat semigroup factorises and the
  transverse factors are `N`-independent for `t ≲ N^{-2}`. The rigorous
  `BMO^{-1}` bound in §1.1(b) is for the exact `eq:oscdata` and needs no such
  assumption.

## 7. Method note

Algebra verified independently with `sympy` (the `eq:cosaverage` constant, the
`N ≥ 2` reduction in `eq:etaN`, the `eq:etastar` chain, the `eq:Nthreshold`
inversion). Norm asymptotics verified by spectral computation (`numpy` FFT):
a 1-D model at `2^18` points, `N ≤ 256`, `α ∈ {0.25,0.49,0.75,0.95}`; and the
exact 3-D field `eq:oscexplicit` with a separable envelope at `2^14 × 2^8`
points, `N ≤ 128`, `α ∈ {0.25,0.70}`, `32` heat times per `N`. The decisive
`BMO^{-1}` bound of §1.1(b) is a proof, not a numerical result; the numerics only
confirm that its exponent is sharp and that the same exponents hold for the
`Ḃ^{-1+3/p}_{p,∞}` ladder. No third-party PDF was downloaded or retained. No
contact was made with any person. No file other than this one was written, and
nothing was committed.

*Self-check note.* My first 3-D script carried a spurious `M/L` factor on the
spectral derivative `∂_1φ`, which inflated the subleading term of
`eq:oscexplicit` by ~160× and produced nonsense slopes (a *decreasing* `L^3`
norm). It was found by comparing against the analytic prediction and fixed; the
numbers reported above are from the corrected run, and they agree with the 1-D
model and with the closed-form asymptotics.
