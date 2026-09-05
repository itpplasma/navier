# CP02-4 REVIEW: audit of `cp02-lowpressure.md` (round 1)

MODE: REVIEW, proof-audit discipline. Date: 2026-09-05. This file asserts no
new mathematics about HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or
NS-R3.

## 0. Freeze

| Item | Value |
| --- | --- |
| Candidate file | `/home/ert/proj/navier/research/evidence/cp02-lowpressure.md` |
| `sha256sum` | `17b31df58db461bab404ecf6a4fd236cb48331c26367614f06b956f0f7adcdf3` |
| `git -C /home/ert/proj/navier rev-parse HEAD` | `715ce84ec78d64c510e150360a354b5d55648b9c` |
| Candidate length | 808 lines; LaTeX block 595 lines |
| Manuscript read in full | `/home/ert/proj/navier-paper/main.tex` (562 lines) |
| Records read in full | `cp01-manuscript-obligations.md`, `cp01-literature-statements.md` |

The author's own summary was treated as untrusted and was not used as
evidence for any conclusion below.

---

## 1. Obligations this review discharges

| Id | What the review establishes | Where |
| --- | --- | --- |
| F-1 (verification) | Every step of `def:lp`, `lem:lp-coincide`, `lem:fourier-tools`, `lem:lowpass-kernel`, `lem:riesz-kernel`, `prop:lowpressure` reconstructed independently; constants `C_φ ≤ 32π/3` and the Fourier-normalisation factor `1` recomputed and confirmed | §3.1–§3.5 |
| P-0 (verification) | `Γ(v) = Σv_iv_j∂_jv_i/|v|` (`:= 0` on `{v=0}`) confirmed index-convention-independent, `|Γ(v)| ≤ |v||∇v|` and `Lip(a↦a⊗a/|a|) ≤ 3` reconfirmed by independent derivation and by two explicit test pairs | §3.6 |
| Q-17 (verification) | `C_B = ‖∇κ‖₂ = 2π‖|ξ|φ‖₂ ≤ 2π(128π/5)^{1/2} = 16π(2π/5)^{1/2} ≈ 56.35` and the scaling `‖∇κ_L‖₂ = 2^{5L/2}‖∇κ‖₂` recomputed; exponent `5L/2` confirmed dimensionally | §3.7 |
| X-1 (verification) | Both directions of `prop:existential-equivalence` reconstructed; all Hölder exponents recomputed (`1/3+1/6+1/2=1`, `2/3=1/6+1/2`, `1=1/2+1/2`); quantifier order `∃θ ∀(ν,u_0,H) ∃(J,A) ∀τ` checked against `hyp:highpressure` as printed in `main.tex` | §3.8 |
| Source audit | All nine Grafakos [DI] claims fetched and inspected page by page in the actual third edition; edition, ISBN, DOI confirmed from the title/copyright pages | §4 |
| Compile check | LaTeX block compiled against the exact `amsthm` preamble of `main.tex` plus the two new `\newtheorem` lines; no errors, 18 overfull `\hbox`es located | §6 |

---

## 2. Review record

### VERDICT

**PASS** — with two mandatory one-line insertions and a list of editorial
repairs. No bridge in the candidate is invalid. The two insertions close
justification gaps (finiteness of `∫_0^τ D_3` before it is cancelled, and
the `θ=0` degenerate product) that are immediate consequences of hypotheses
the same sentences already invoke; they change no statement and no constant.

### REVIEWED SCOPE

The complete LaTeX block of `cp02-lowpressure.md` §2, i.e.
`def:lp`, `lem:lp-coincide`, `lem:fourier-tools`(i)–(iv),
`lem:lowpass-kernel`(a)–(d), `lem:riesz-kernel`(a)–(d),
`def:pressure-work`, `lem:gamma`(a)–(d), `prop:lowpressure`(i)–(iii),
`rem:lowpressure-constant`, `lem:bernstein`, `lem:absorption-split`,
`prop:existential-equivalence`, `rem:existential-scope`, and the supplied
`Grafakos2014` bib entry; plus the candidate's external-fact table §3, its
open-obligation list §4, and its frontier record §5.

Not in scope (owned elsewhere, assumed here exactly as the candidate assumes
them): `prop:localtheory` (package R of D2), `prop:pressure` in integrated
P-3 form with the P-0 integrand, `thm:continuation` in D3 form,
`prop:energy` as printed in `main.tex`.

### FIRST BAD BRIDGE

**None.** Every implication was reconstructed from its first nontrivial step
and holds as written, with the two exceptions below, which are *unjustified
as written* rather than false, and are repaired in one sentence each.

Ranked list of what was checked and survived, with the reconstruction:

1. **Telescoping in `lem:lp-coincide`.**
   `ψ(2^{-j}ξ) = φ(2^{-j}ξ) − φ(2·2^{-j}ξ) = φ(2^{-j}ξ) − φ(2^{-(j-1)}ξ)`,
   so `Σ_{j=-N}^{J} ψ(2^{-j}ξ) = φ(2^{-J}ξ) − φ(2^{N+1}ξ)`. Confirmed.
   Plancherel gives
   `‖S_Jf − Σ_{j=-N}^J Δ_jf‖₂² = ∫φ(2^{N+1}ξ)²|f̂|²dξ`; for every `ξ ≠ 0`
   the factor vanishes once `2^{N+1}|ξ| ≥ 2`, and `|f̂|² ∈ L¹`. Dominated
   convergence applies. **Refutation attempt:** an atom of `f̂` at `ξ = 0`
   would break the pointwise limit — impossible, `f̂ ∈ L²`. The lemma is
   true, and it is exactly what D1's clause "on `L²` this coincides with the
   homogeneous sum" requires; it is also the direct repair of finding 8.4 of
   `cp01-literature-statements.md` ("Littlewood–Paley convention is
   unpinned … homogeneous vs inhomogeneous … not harmless for `S_Jp`"),
   since every use of `S_J` in the lane is on an `L²` function.
2. **`lem:fourier-tools`(iv), `L²∗L¹`.** `g_k = g1_{B(0,k)} ∈ L¹∩L²`;
   `g_k∗f ∈ L¹` (Minkowski, `q=1`) and `∈ L²` (Minkowski, `q=2`), so the
   `L¹` convolution theorem applies and `F` agrees with the `L¹` transform
   on `L¹∩L²`; `‖(g_k−g)∗f‖₂ ≤ ‖g_k−g‖₂‖f‖₁ → 0` and
   `‖(ĝ_k−ĝ)f̂‖₂ ≤ ‖f̂‖_∞‖g_k−g‖₂ → 0` with `‖f̂‖_∞ ≤ ‖f‖₁`. Both limits are
   in `L²`, `F` is an isometry, so the identity passes to the limit.
   Correct. This is the load-bearing step the candidate itself flagged for
   line-by-line review; it survives.
3. **`lem:lowpass-kernel`(a).** `κ = φ^∨ ∈ 𝒮` (Cor. 2.2.15 plus reflection),
   `κ̂ = φ` (Thm. 2.2.14(2)),
   `κ̂_J(ξ) = ∫e^{-2πi2^{-J}y·ξ}κ(y)dy = φ(2^{-J}ξ)` and
   `‖κ_J‖₁ = ‖κ‖₁` by `x = 2^{-J}y`. Recomputed; correct.
4. **`lem:lowpass-kernel`(c).** For `h ∈ 𝒮`, the difference quotient is
   majorised by `sup_{|σ|≤1}|∂_kh(x-y+σe_k)| ≤ C_h'(1+|x-y+σe_k|)^{-4}`; with
   `|z-w| ≤ 1 ⟹ 1+|z| ≤ 2(1+|w|)` this is `≤ 2^4C_h'(1+|x-y|)^{-4}`, and
   `(1+|·|)^{-4} ∈ L²(R³)` so the majorant is in `L¹` against `f ∈ L²` by
   Cauchy–Schwarz. Correct, including the `2^4`. The continuity of
   `(∂^ακ_J)∗f` is proved by the same majorant and **not** by
   `lem:fourier-tools`(ii)'s continuity clause (which needs `f ∈ L¹`) — the
   candidate does not make that error.
5. **`lem:riesz-kernel`(a),(b).** `|ξ_iξ_j| ≤ |ξ|²` gives
   `|m^{ij}_J| ≤ φ(2^{-J}·) ≤ 1_{\{|ξ|≤2^{J+1}\}}`, hence `m^{ij}_J ∈ L¹∩L²`
   and `‖m^{ij}_J‖₁ ≤ 2^{3J}‖φ‖₁ ≤ 2^{3J}|B(0,2)| = (32π/3)2^{3J}`.
   `(4π/3)2^{3(J+1)} = (4π/3)·8·2^{3J} = (32π/3)2^{3J}`: the two printed
   forms agree. Under `f^∨(x) = ∫e^{2πix·ξ}f(ξ)dξ` the bound
   `‖K_J‖_∞ ≤ ‖m_J‖₁` carries no `(2π)^{-3}`; recomputed and confirmed.
   Realness and evenness: `φ` real even and `ξ↦ξ_iξ_j/|ξ|²` real even.
6. **`lem:riesz-kernel`(c).** `R_j := T_{r_j}`, `r_j(ξ) = -iξ_j/|ξ|`,
   `r_j(0):=0`, so `r_ir_j = -ξ_iξ_j/|ξ|² = m^{ij}` off `0` **and at `0`**;
   `T_mT_{m'} = T_{mm'}` for bounded symbols; `S_JR_iR_j = T_{m^{ij}_J}`.
   `F(K_J∗f) = K̂_Jf̂ = m_Jf̂` by (iv) with `g = K_J ∈ L²`, `f ∈ L¹`.
   Correct. The lane never claims `K_J ∈ L¹` and never needs it.
7. **`lem:riesz-kernel`(d), the bilinear symbol bound.**
   `Σ_{ij}K^{ij}_J(z)c_id_j = -∫e^{2πiz·ξ}φ(2^{-J}ξ)(c·ξ)(d·ξ)/|ξ|²dξ`
   (finite sum of absolutely convergent integrals), and
   `|(c·ξ)(d·ξ)| ≤ |c||d||ξ|²`, so the modulus is `≤ 2^{3J}C_φ|c||d|`.
   Correct, and this is what removes the spurious factor `9` (or `3`) that a
   term-by-term `Σ_{ij}‖K^{ij}_J‖_∞‖u_iu_j‖₁` estimate would produce.
   **Refutation attempt:** at `z = 0`, `J = 0`, `c = d = e_1` the sum is
   `-∫φ(ξ)ξ_1²/|ξ|²dξ`, of modulus `C_φ/3 < C_φ`; no contradiction.
8. **`prop:lowpressure`(i).** `u(t) ∈ L²∩L^∞` (R) gives
   `f_{ij} = u_iu_j ∈ L¹∩L²` with `‖f_{ij}‖₁ ≤ ‖u‖₂²`; `p = ΣR_iR_jf_{ij}` in
   `L²`; `p_{≤J} = ΣK^{ij}_J∗f_{ij}` a.e.; pointwise in `y` apply (d) with
   `c = d = u(y)` and integrate:
   `‖p_{≤J}‖_∞ ≤ C_φ2^{3J}∫|u|² = C_φ2^{3J}‖u‖₂²`. Then `prop:energy`.
   Correct. Crucially **no** spatial decay of `u` beyond `L²` is used, so
   D2's prohibition on assuming preserved Schwartz decay is respected.
9. **`prop:lowpressure`(ii),(iii).**
   `|L_J| ≤ ‖p_{≤J}‖_∞‖u‖₂‖∇u‖₂ ≤ C2^{3J}‖u_0‖₂³‖∇u(t)‖₂`.
   Time continuity of `p_{≤J}` in `L^∞` via the bilinear bound on
   `u_i(t)u_j(t) - u_i(s)u_j(s) = (u_i(t)-u_i(s))u_j(t) + u_i(s)(u_j(t)-u_j(s))`:
   correct, giving `2^{3J}C_φ‖u(t)-u(s)‖₂(‖u(t)‖₂+‖u(s)‖₂)`.
   Time Cauchy–Schwarz: `∫_0^τ‖∇u‖₂ ≤ τ^{1/2}(∫_0^τ‖∇u‖₂²)^{1/2}`,
   `τ < H`, and `main.tex` `prop:energy` line 78 gives
   `∫_0^{T_*}‖∇u‖₂² ≤ ‖u_0‖₂²/(2ν)`, hence
   `≤ C2^{3J}‖u_0‖₂⁴(H/2ν)^{1/2}`. Recomputed; exactly `eq:lowpressure` as
   printed in `main.tex` line 268, with `C` now pinned. Correct.
10. **`lem:gamma`(a).** `|g(a)| = |a⊗a|_F/|a| = |a|`. Off `0`,
    `Dg(a)[h] = (h⊗a+a⊗h)/|a| - (a·h)a⊗a/|a|³` with
    `|Dg(a)[h]| ≤ 2|h| + |h| = 3|h|`; mean-value inequality on segments
    missing `0`; if `0 ∈ [a,b]` then `|a-b| = |a|+|b|` and
    `|g(a)-g(b)| ≤ |a|+|b| = |a-b|`. Correct, and the two-case split is
    necessary. **Refutation attempts:** `a=(1,0,0), b=(-1,0,0)` gives
    `g(a)=g(b)=E_{11}`, ratio `0`; `a=(1,0,0), b=(cosθ,sinθ,0)` gives ratio
    `→ √2` as `θ→0`. No violation of `3`.
11. **`lem:gamma`(b),(c),(d).** Two Cauchy–Schwarz steps give
    `|Γ(v)| ≤ |v||∇v|`; `g` is continuous at `0` because `|g(a)| = |a|`, so
    `Γ(u(t))` is continuous in `x` for `u(t) ∈ C¹`; Hölder `1 = 1/2+1/2` and
    `2/3 = 1/6+1/2` give the `L¹` and `L^{3/2}` bounds and, with (a), the
    `C([0,T];L¹) ∩ C([0,T];L^{3/2})` continuity from
    `u ∈ C([0,T];L²∩L⁶)`, `∇u ∈ C([0,T];L²)`. Absolute convergence and
    `P_3 = L_J + Q_J` follow from `p, p_{≤J}, p_{>J} ∈ L^∞` and
    `Γ(u) ∈ L¹`. All correct. `Γ(v) = (v⊗v):∇v/|v|` is invariant under the
    index convention `(∇v)_{ij} = ∂_iv_j` vs `∂_jv_i` (relabel `i ↔ j`), so
    the P-0 recommendation `P_3 = ∫_{u≠0}p(u⊗u):∇u/|u|` and the candidate's
    `eq:gamma` denote the same function. No ambiguity.
12. **`lem:bernstein`.** `‖∂_kκ_L‖₂² = 2^{8L}·2^{-3L}‖∂_kκ‖₂² = 2^{5L}‖∂_kκ‖₂²`;
    summing over `k` and over components of `f` gives
    `|∇S_Lf(x)|² ≤ ‖∇κ_L‖₂²‖f‖₂²`; Plancherel and Prop. 2.2.11(9) give
    `‖∇κ‖₂² = 4π²∫|ξ|²φ² ≤ 4π²∫_{|ξ|≤2}|ξ|²dξ = 4π²·4π∫_0^2r⁴dr = 4π²·128π/5`.
    `2π(128π/5)^{1/2} = 16π(2π/5)^{1/2} ≈ 56.35`: the two printed forms are
    equal (checked numerically). Exponent `5L/2 = L + 3L/2` matches Tao's
    `N^k·N^{3/p-3/q}` with `k=1, p=2, q=∞, N=2^L`. Correct.
13. **`lem:absorption-split`.** `∫_0^τP_3 = ∫_0^τL_J + ∫_0^τQ_J` is
    legitimate: `L_J` is continuous hence integrable by
    `prop:lowpressure`(ii), `P_3` is integrable by hypothesis, so
    `Q_J = P_3 - L_J` is integrable. Adding `eq:lowpressure` and
    `eq:highpressure` for the **same** `J` (the `J(ν,u_0,H)` that
    `hyp:highpressure` supplies) yields `eq:absorption` with
    `A = A_low + A_high`, and neither summand depends on `τ`, which is what
    `hyp:absorption`'s clause "with the same `A` for the entire interval"
    demands. Correct; this is exactly the sentence at `main.tex` 337–340
    that the obligations record marked "proved (addition); state that the
    `J` is the one supplied by `hyp:highpressure`". Discharged.
14. **`prop:existential-equivalence`, (A)⇒(B).** `H := T_*+1` is admissible
    because `hyp:highpressure` quantifies over all `0 < H < ∞` for each
    `(ν,u_0)`, and then `min{H,T_*} = T_*`. From the integrated
    `prop:pressure` and `eq:absorption`,
    `X(τ)/3 + (1-θ)ν∫_0^τD_3 ≤ X(0)/3 + A`, so
    `sup_{τ<T_*}‖u(τ)‖₃ ≤ (‖u_0‖₃³+3A)^{1/3} < ∞`, contradicting D3-form
    `thm:continuation`. Valid; see the one required insertion below.
15. **(B)⇒(A).** `θ := 0`, `J := 0` uniformly in `(ν,u_0,H)` — the correct
    quantifier order, since `hyp:highpressure` needs a *fixed* `θ`.
    `‖S_0p‖₃ ≤ ‖κ‖₁‖p‖₃` by `lem:lowpass-kernel`(b) with `q=3` (legitimate:
    `p(t) ∈ L²∩L³` by R), so `‖p_{>0}‖₃ ≤ (1+‖κ‖₁)‖p‖₃`, and the same bound
    on `p(t)-p(s)` gives `p_{>0} ∈ C([0,H];L³)`. Hölder
    `1/3+1/6+1/2 = 2/6+1/6+3/6 = 1` gives
    `|Q_0| ≤ (1+‖κ‖₁)‖p‖₃‖u‖₆‖∇u‖₂`, continuous on the compact `[0,H]`
    hence bounded; the `L³`–`L^{3/2}` pairing with `lem:gamma`(c) gives
    continuity of `Q_0`; `A_high := ∫_0^H|Q_0| < ∞` depends only on
    `(ν,u_0,H)` by uniqueness of the branch. Valid.

The two required insertions (neither is a refutation):

* **(R1)** In (A)⇒(B), the passage from
  `X(τ)/3 + ν∫_0^τD_3 ≤ X(0)/3 + θν∫_0^τD_3 + A` to
  `X(τ)/3 + (1-θ)ν∫_0^τD_3 ≤ X(0)/3 + A` cancels `θν∫_0^τD_3` on both
  sides. As written the finiteness of `∫_0^τD_3` is never stated. It is
  immediate from the identity itself, but D5 requires it in the text.
* **(R2)** In (B)⇒(A) Step 4 the display writes
  `A_high = θν∫_0^τD_3 + A_high` with `θ = 0`. If `∫_0^τD_3` were `+∞` the
  product `0·∞` would be undefined. One clause fixes this.

### EVIDENCE

* Independent rederivation of every displayed identity and constant listed
  in items 1–15 above; each numeric claim recomputed:
  `|B(0,2)| = (4π/3)·8 = 32π/3 ≈ 33.51`;
  `∫_{|ξ|≤2}|ξ|²dξ = 4π∫_0^2r⁴dr = 128π/5 ≈ 80.42`;
  `2π(128π/5)^{1/2} = 16π(2π/5)^{1/2} ≈ 56.35`;
  `(4π/3)2^{3(J+1)} = (32π/3)2^{3J}`;
  Hölder triples `1/3+1/6+1/2 = 1`, `2/3 = 1/6+1/2`, `1 = 1/2+1/2`;
  scaling `‖∇κ_L‖₂² = 2^{8L-3L}‖∇κ‖₂²`.
* Source audit: the third edition of Grafakos was downloaded and read
  through `helpy_pdf` text extraction (printed pages `19–22`, `103–115`,
  `326–330`, and the title/copyright pages). Every one of the candidate's
  nine Grafakos [DI] claims was located and its statement compared word for
  word. See §4; **all nine are correct**, including the wording "properties
  (1)–(8) as well as (12) and (13) … with `f, g` integrable" on p. 113.
  One page number is off by one (see minor issue M6).
* Cross-check of the pressure normalisation independently of the CP01
  record: Grafakos Prop. 5.1.17 (p. 328) states `∂_j∂_kφ = -R_jR_kΔφ` with
  the displayed symbol computation `-(-iξ_j/|ξ|)(-iξ_k/|ξ|)(-4π²|ξ|²)`.
  Substituting `φ = Δ^{-1}g` gives `R_jR_kg = -Δ^{-1}∂_j∂_kg`, so
  `p = R_iR_j(u_iu_j) = -Δ^{-1}∂_i∂_j(u_iu_j)`, confirming `def:lp`'s
  identity, `cp01-literature-statements.md` §7.3, and the Riesz symbol of
  D1 — from the primary source, not from the record.
* Compile check: the LaTeX block was extracted verbatim and compiled with
  `pdflatex` against a preamble identical to `main.tex` lines 1–11 plus
  `\newtheorem{lemma}[theorem]{Lemma}` and
  `\newtheorem{definition}[theorem]{Definition}`, with stub environments
  carrying the four cited external labels. Result: 11 pages, no errors, no
  undefined macros; 18 overfull `\hbox`es (see M8).
* Interface check against `main.tex` as frozen: labels `prop:energy`,
  `prop:pressure`, `thm:continuation`, `hyp:highpressure`,
  `hyp:absorption`, `eq:highpressure`, `eq:absorption`, `eq:lowpressure`,
  `prop:lowpressure` all exist; `prop:localtheory` does **not** yet exist
  (`main.tex` has only `premise:local`, a `\phantomsection` label at line
  46). The candidate declares this dependency.
* Quantifier check against the printed hypotheses: `hyp:highpressure`
  (`main.tex` 292–304) and `hyp:absorption` (306–315) both read
  `∃θ∈[0,1) ∀(ν,u_0,H) ∃(J,A) ∀τ<min{H,T_*}`, with "the same `J` and
  `A_high` must work for the entire interval". `lem:absorption-split` and
  both directions of `prop:existential-equivalence` respect this order.

### REPLACEMENT ARGUMENT (the two required insertions, complete)

New environments needed: none beyond the candidate's `lemma` and
`definition`. No label changes.

```latex
%% ---- REPAIR R1.  In the proof of Proposition~\ref{prop:existential-equivalence},
%% ---- direction (A)$\Rightarrow$(B), replace the sentence beginning
%% ---- "Since $D_3\ge0$ and $\theta<1$, the dissipation terms combine to"
%% ---- by the following two sentences.

Both sides of this chain are finite: by Proposition~\ref{prop:pressure} in
integrated form, $P_3$ is integrable on $[0,\tau]$ and
$\nu\int_0^\tau D_3\,dt=\tfrac13X(0)-\tfrac13X(\tau)+\int_0^\tau P_3\,dt<\infty$,
while $X(\tau)\ge0$ and $A<\infty$.  Hence the term
$\theta\nu\int_0^\tau D_3\,dt$ may be subtracted from both sides; since
$D_3\ge0$ and $\theta<1$, the dissipation contributions combine to
$(1-\theta)\nu\int_0^\tau D_3\,dt\ge0$ on the left, and therefore
$X(\tau)\le\norm{u_0}_3^3+3A$ for every $0<\tau<T_*$; that is,
\[
 \sup_{0<\tau<T_*}\norm{u(\tau)}_3\le\bigl(\norm{u_0}_3^3+3A\bigr)^{1/3}<\infty .
\]

%% ---- REPAIR R2.  In the proof of Proposition~\ref{prop:existential-equivalence},
%% ---- direction (B)$\Rightarrow$(A), insert immediately before the display of
%% ---- Step~4 the following sentence.

By Proposition~\ref{prop:localtheory} and Lemma~\ref{lem:gamma}(b),
$D_3(t)\le2\int_{\R^3}|u|\,|\nabla u|^2dx\le2\norm{u(t)}_\infty\norm{\nabla u(t)}_2^2$,
which is a continuous function of $t$ on the compact interval $[0,H]$;
hence $\int_0^\tau D_3\,dt<\infty$ for every $\tau\le H$ and the product
$\theta\nu\int_0^\tau D_3\,dt$ is $0$ for $\theta=0$.

%% ---- REPAIR R3 (editorial, recommended).  In the proof of
%% ---- Lemma~\ref{lem:lp-coincide}, replace the closing parenthetical
%% ---- "(At $\xi=0$ the symbols differ, ...)" by:

(The telescoped identity holds at $\xi=0$ as well, both sides being $0$
there.  What differs at the single point $\xi=0$ is the pointwise limit of
the symbols: $\varphi(2^{N+1}\xi)\to\mathbf 1_{\{0\}}(\xi)$, so the limiting
symbol is $\varphi(2^{-J}\xi)-\mathbf 1_{\{0\}}(\xi)$.  A point is a null
set, so this limiting symbol and $\varphi(2^{-J}\cdot)$ define the same
multiplier on $L^2$.)

%% ---- REPAIR R4 (editorial).  In Definition~\ref{def:lp}, replace
%% ---- "so that $S_J$ is Tao's projection $P_{\le 2^J}$ \cite[p.~40]{Tao2013}"
%% ---- by:

so that $S_J$ is the projection $P_{\le 2^J}$ of Tao \cite[p.~40]{Tao2013}
for this choice of bump $\varphi$ (Tao fixes only the support and normalisation
conditions on $\varphi$, which the above choice satisfies).

%% ---- REPAIR R5 (editorial).  In Lemma~\ref{lem:absorption-split}, replace the
%% ---- conclusion "Then Hypothesis~\ref{hyp:absorption} holds for these
%% ---- $\nu$, $u_0$, $H$ with the same $\theta$ and" by:

Then \eqref{eq:absorption} holds for these $\nu$, $u_0$, $H$, for every
$0<\tau<\min\{H,T_*\}$, with the same $\theta$ and with
```

### CONDITIONAL SUFFIX THAT SURVIVES

Unconditionally (given only package R of D2 and `prop:energy` as printed in
`main.tex`):

* `def:lp`, `lem:lp-coincide`, `lem:fourier-tools`, `lem:lowpass-kernel`,
  `lem:riesz-kernel`, `def:pressure-work`, `lem:gamma`, `prop:lowpressure`
  with `C = 32π/3` (sharper: `C_φ = ‖φ‖₁`), `rem:lowpressure-constant`,
  `lem:bernstein` with `C_B = 2π‖|ξ|φ‖₂ ≤ 16π(2π/5)^{1/2}`.
* In particular: `‖p_{≤J}(t)‖_∞ ≤ C_φ2^{3J}‖u_0‖₂²`,
  `|L_J(t)| ≤ C_φ2^{3J}‖u_0‖₂³‖∇u(t)‖₂`, `L_J ∈ C([0,T_*))`, and
  `|∫_0^τL_J| ≤ C_φ2^{3J}‖u_0‖₂⁴(H/2ν)^{1/2}` for `0 < τ < min{H,T_*}`.

Conditional on `prop:pressure` in integrated P-3 form with the P-0
integrand `Γ` of `def:pressure-work`:

* `lem:absorption-split`: `hyp:highpressure ⟹ hyp:absorption` with
  `A = A_low(ν,u_0,H,J) + A_high(ν,u_0,H,J)`, `J = J(ν,u_0,H)`;
* `eq:pressure-consequence`, i.e.
  `sup_{t<min{H,T_*}}‖u(t)‖₃³ ≤ ‖u_0‖₃³ + 3A`, after R1;
* `prop:existential-equivalence` (B)⇒(A) with `θ = 0`, `J = 0`,
  `A_high = ∫_0^H|Q_0|`.

Conditional additionally on `thm:continuation` in the D3 form
`T_* < ∞ ⟹ sup_{t<T_*}‖u(t)‖₃ = ∞`:

* `prop:existential-equivalence` (A)⇒(B), hence the full equivalence
  `hyp:highpressure ⟺ (∀ν,u_0: T_* = ∞)`.

Nothing here bounds `Q_J`, `A_high`, or `θ` without assuming global
continuation.

### UNNECESSARY DEPENDENCIES

1. `lem:lowpass-kernel`(d) and the clause `∇S_Lf = S_L∇f` in `lem:bernstein`
   are never used inside this lane. They exist only for the quotient lane.
   Keep, but the integrator should record that they are exported, not used.
2. External facts E7 (general Young), E8 (Grafakos Riesz definition/kernel),
   E9 (Prop. 5.1.17) are labelled "corroboration only" by the candidate and
   are indeed not cited in the LaTeX block. E14 (Calderón–Zygmund) is
   explicitly not used. All four may be dropped from the manuscript's
   citation list without weakening anything; E9 is nevertheless worth
   keeping as an independent primary-source anchor for the pressure
   normalisation, since it discharges P-1's "the source of `p ∈ L²∩L³` is
   not named" complaint without invoking Calderón–Zygmund.
3. `prop:lowpressure`(i)'s assertion that the representative is *real* is
   not used downstream. Harmless.
4. `lem:gamma`(a)'s Lipschitz constant `3` is genuinely needed (both
   continuity statements in (c) use it); it is **not** an unnecessary
   dependency.
5. `lem:lp-coincide` is not used by any later step in the lane, but it is
   *required* by F-1 and by D1's reconciliation clause and by finding 8.4 of
   the literature record. Keep.

### NON-CLAIMS

* This review asserts no HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION,
  or NS-R3 result, and no bound on `Q_J`, `A_high`, or `θ`.
* It does not certify `prop:pressure`, `thm:continuation`, or
  `prop:localtheory`; those are assumed exactly as the candidate assumes
  them and are audited in their own lanes.
* It does not certify the quotient lane's `M = 3(1+C_ℙ)C_B2^{5L/2}‖u_0‖₂`.
  The candidate's frontier record calls that constant "valid"; only the
  factor `C_B2^{5L/2}‖u_0‖₂` is established here. The remaining factor
  `3(1+‖ℙ‖_{L³→L³})` rests on `‖q‖₃ ≤ (1+‖ℙ‖)‖w‖₃` and
  `‖A‖_{3/2} = ‖w‖₃²`, neither of which is proved in this lane. See M5.
* The general Bernstein inequality (Tao (26)) is not proved here, only the
  instance `k=1, p=2, q=∞`; the candidate says so.
* No `L¹` bound on the kernel of `S_JR_iR_j` or of any untruncated Riesz
  transform is claimed anywhere, by the candidate or by this review.
* Grafakos Cor. 5.2.8 and Stein 1970 were not inspected here ([MO],
  unused).

### REOPENING CONDITION

This PASS is void, and the named items must be re-audited, if any of the
following occurs.

1. The pressure lane delivers `prop:pressure` with a `P_3` integrand that is
   **not** pointwise equal to `Γ(u)` of `def:pressure-work` — for example
   one written through `∇|u|` with an a.e./Rademacher qualification, or one
   whose `D_3` is not pointwise nonnegative. Affected: `lem:gamma`(d),
   `lem:absorption-split`, both directions of
   `prop:existential-equivalence`, repair R1.
2. The pressure lane does not deliver integrability of `P_3` on compact
   subintervals of `[0,T_*)`. Affected: the same items plus repair R1, whose
   finiteness argument is exactly that hypothesis.
3. The continuation lane does not deliver `thm:continuation` in the D3 form
   `T_* < ∞ ⟹ sup_{t<T_*}‖u(t)‖₃ = ∞`. As printed in `main.tex`
   (lines 375–382) the conclusion is "extends as a classical solution beyond
   `T_*`", which the obligations record already flags as ill-formed;
   `prop:existential-equivalence` (A)⇒(B) cites the D3 form and nothing
   else. Affected: (A)⇒(B) only.
4. The local-theory lane's `prop:localtheory` omits any of
   `u ∈ C([0,T];L²∩L⁶∩L^∞)`, `∇u ∈ C([0,T];L²)`,
   `p ∈ C([0,T];L²∩L³∩L^∞)`, `u(t) ∈ C¹`, or uniqueness of the branch.
   Affected: `lem:gamma`(c),(d), `prop:lowpressure`, (B)⇒(A) Steps 1–4,
   repair R2.
5. The integrator changes the bump: dropping `0 ≤ φ ≤ 1` invalidates
   `C_φ ≤ 32π/3` and `C_B ≤ 16π(2π/5)^{1/2}`; dropping realness or evenness
   of `φ` invalidates the realness/evenness clauses of
   `lem:fourier-tools`(iii), `lem:lowpass-kernel`(a), `lem:riesz-kernel`(b),
   and `prop:lowpressure`(i). All other statements survive with `‖φ‖₁` and
   `‖∇κ‖₂` left symbolic.
6. Any lane applies `S_J = Σ_{j≤J}Δ_j` to a function that is not in `L²`.
   `lem:lp-coincide` is an `L²` statement only, and the `L^q` bound of
   `lem:lowpass-kernel`(b) is proved for the *inhomogeneous* `S_J` via
   `κ_J ∈ L¹`; the homogeneous partial sums have no such bound supplied.

---

## 3. Step-by-step reconstruction notes

### 3.1 Conventions (`def:lp`)

`f̂(ξ) = ∫e^{-2πix·ξ}f(x)dx`, `f^∨(x) = f̂(-x)`, Plancherel with constant `1`.
`Δ` has symbol `-4π²|ξ|²` because `∂_k` has symbol `2πiξ_k`; hence `Δ^{-1}`
has symbol `-(4π²|ξ|²)^{-1}` and `-Δ^{-1}∂_i∂_j` has symbol
`(4π²|ξ|²)^{-1}·4π²ξ_iξ_j·(-1) = -ξ_iξ_j/|ξ|²`, equal to `r_ir_j`. Verified.
Minor informality: the composite `-Δ^{-1}∂_i∂_j` is meaningful only as the
product symbol; the text should say so explicitly (M2).

### 3.2 `lem:lp-coincide`

See record item 1. The lemma is true and needed. Only the closing
parenthetical is misphrased (R3).

### 3.3 `lem:fourier-tools`

(i) is Grafakos Thm. 1.2.10 with `(p,f,g) ↦ (q,f,g)`; the printed statement
is `‖g∗f‖_{L^p} ≤ ‖g‖_{L^1}‖f‖_{L^p}` for `g ∈ L¹`, `f ∈ L^p`, `1 ≤ p ≤ ∞`,
"`g∗f` exists a.e." — exactly as used. (ii) is Hölder plus dominated
convergence; the continuity clause is stated only for `g` bounded continuous
and `f ∈ L¹`, and is used only in that case. (iii) and (iv) verified in
record items 1–2. (iv)'s proof is the only place in the lane where an `L²`
limit argument carries the conclusion; it is correct.

### 3.4 `lem:lowpass-kernel`

Verified in record items 3–4 and (d) by the symbol identity
`2πiξ_kφ(2^{-J}ξ)f̂ = φ(2^{-J}ξ)·2πiξ_kf̂`, valid in `L²` for `f ∈ H¹`.

### 3.5 `lem:riesz-kernel` and `prop:lowpressure`

Verified in record items 5–9. Note that the bilinear route is not a
convenience: the term-by-term route gives
`‖p_{≤J}‖_∞ ≤ Σ_{ij}‖K^{ij}_J‖_∞‖u_iu_j‖₁ ≤ 2^{3J}C_φΣ_{ij}‖u_iu_j‖₁`, and
`Σ_{ij}‖u_iu_j‖₁ ≤ 3‖u‖₂²` by Cauchy–Schwarz — a factor `3` worse. The
candidate's constant is the sharp one for this kernel path.

### 3.6 `def:pressure-work`, `lem:gamma`

Verified in record items 10–11. The one D4 friction: `def:pressure-work`
contains the clause "which on `{v≠0}` equals `v·∇|v|`". D4 says the
integrated `prop:pressure` is to be written "no `∇|u|`". On `{v≠0}` this is
a classical identity, not an a.e. claim, so it is not a violation, but the
clause reintroduces the notation the controller removed and should be
deleted or demoted to a remark (M1).

### 3.7 `lem:bernstein`

Verified in record item 12. `C_B` is `‖∇κ‖₂`, i.e. it depends on `φ` only.

### 3.8 `lem:absorption-split`, `prop:existential-equivalence`

Verified in record items 13–15, with insertions R1 and R2. No circularity:
(A)⇒(B) uses `thm:continuation` (which rests on ESS, an import) and
`prop:pressure`; (B)⇒(A) uses only package R. Neither direction uses
`prop:existential-equivalence` itself, `hyp:absorption` as an assumption, or
`hyp:critical`.

Structural observation, not a defect: because `prop:existential-equivalence`
proves `hyp:highpressure ⟺ (∀ν,u_0: T_* = ∞)`, and because
`prop:energy` supplies the remaining clause of `def:target`, the manuscript
now contains a *proof* that its "refined first new gap" is logically the
whole positive alternative for Schwartz data. `main.tex` already says this
in prose (lines 323–325) and the Proof-boundary section already disclaims
both hypotheses (lines 554–558), so the non-claims are intact; but the
abstract and §"Proof boundary" should be updated to say that the refinement
is a reformulation of equal strength, not a reduction (M9).

---

## 4. Source audit of the candidate's external facts

Source inspected: Loukas Grafakos, *Classical Fourier Analysis*, **Third
Edition**, Graduate Texts in Mathematics 249, Springer, New York 2014,
ISSN 0072-5285, ISBN 978-1-4939-1193-6, eBook ISBN 978-1-4939-1194-3,
DOI 10.1007/978-1-4939-1194-3, LCCN 2014946585, © 2000, 2008, 2014.
Edition, ISBN and DOI read from the title page and copyright page of the
copy at
`https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf`
(647 PDF pages; printed page `n` = PDF page `n+17`), read on 2026-09-05 via
`helpy_pdf` text extraction. **The candidate's bibliographic data are
exactly right.**

| # | Candidate's claim | Located at | Verdict |
| --- | --- | --- | --- |
| E1 | Def. 2.2.8, p. 108: `f̂(ξ) = ∫f(x)e^{-2πix·ξ}dx` on `𝒮` | printed p. 108 (PDF 125), Definition 2.2.8, verbatim | **[DI] confirmed** |
| E2 | Prop. 2.2.11, pp. 109–110, items (1),(8),(9),(12); p. 113 extension to `L¹` | statement opens on printed p. 109 (PDF 126) with item (1) `‖f̂‖_{L^∞} ≤ ‖f‖_{L^1}`; items (4)–(13) on printed p. 110 (PDF 127) with (8) `(δ^tf)^ = t^{-n}δ^{t^{-1}}f̂`, (9) `(∂^αf)^(ξ) = (2πiξ)^αf̂(ξ)`, (12) `(f∗g)^ = f̂ĝ`; printed p. 113 (PDF 130), §2.2.4: "this operator satisfies properties (1)–(8) as well as (12) and (13) in Proposition 2.2.11, with `f, g` integrable" | **[DI] confirmed**, wording matches |
| E3 | Thm. 2.2.14 (2),(4), p. 112: inversion and Plancherel on `𝒮` | printed p. 112 (PDF 129), Theorem 2.2.14, (2) "(Fourier Inversion) `(f̂)^∨ = f = (f^∨)^∧`", (4) "(Plancherel's identity) `‖f‖_{L²} = ‖f̂‖_{L²} = ‖f^∨‖_{L²}`" | **[DI] confirmed** |
| E4 | Cor. 2.2.15, p. 113: `F` is a homeomorphism of `𝒮` onto itself | printed p. 113 (PDF 130), Corollary 2.2.15, verbatim | **[DI] confirmed** |
| E5 | §2.2.4, pp. 113–114: `L²` isometry on `L¹∩L²`, unique extension `F`, `F′` extends `f↦f^∨`, `F′ = F^{-1}`, inversion a.e. on `L²` | printed pp. 113–114 (PDF 130–131). All five assertions present, including "`F′` coincides with the inverse operator `F^{-1}` of `F: L² → L²`, and Fourier inversion `f = F^{-1}∘F(f) = F∘F^{-1}(f)` a.e. holds on `L²`" | **[DI] confirmed**; the sub-assertion "for `f ∈ L¹∩L²` the expressions `f̂` and `F(f)` coincide pointwise a.e." sits on p. **114**, not 113 (M6) |
| E6 | Thm. 1.2.10, p. 21: Minkowski, `g ∈ L¹`, `f ∈ L^p`, `1 ≤ p ≤ ∞`, `‖g∗f‖_p ≤ ‖g‖₁‖f‖_p`, exists a.e. | printed p. 21 (PDF 39), Theorem 1.2.10 "(Minkowski's inequality)", verbatim | **[DI] confirmed** |
| E7 | Thm. 1.2.12, p. 22: Young, `1/q + 1 = 1/p + 1/r`, `‖f∗g‖_q ≤ ‖g‖_r‖f‖_p` | printed p. 22 (PDF 40), Theorem 1.2.12 "(Young's inequality)", (1.2.13)–(1.2.14), verbatim (with the group-theoretic side condition `‖g‖_{L^r} = ‖g̃‖_{L^r}`, automatic on `R^n`) | **[DI] confirmed**; unused |
| E8 | Def. 5.1.13 / Prop. 5.1.14, p. 325: `R_j` is the multiplier `-iξ_j/|ξ|`, kernel `c_n p.v. x_j/|x|^{n+1}` | Prop. 5.1.14's proof completes on printed p. 327 (PDF 343); the symbol `-iξ_j/|ξ|` is displayed there in Prop. 5.1.16's proof (`Σ_j(-iξ_j/|ξ|)² = -1`) and again on p. 328 | **[DI] confirmed** (numbering and symbol); the exact page of the *statement* of 5.1.13/5.1.14 was not printed in the extracted range, so "p. 325" is plausible but unverified — harmless, unused |
| E9 | Prop. 5.1.17, p. 328: `∂_j∂_kφ = -R_jR_kΔφ` on `𝒮` | printed p. 328 (PDF 344), Proposition 5.1.17, (5.1.47), verbatim, with the symbol computation displayed | **[DI] confirmed** |
| E10 | Tao 2013 p. 40 eq. (26): `P_{≤N}` with symbol `φ(ξ/N)`, `φ = 1` on `|ξ|≤1`, supported in `|ξ|≤2`; Bernstein estimates | matches `cp01-literature-statements.md` §1.4 verbatim transcription, including `‖∇^kP_Nf‖_p ∼ N^k‖P_Nf‖_p` and `‖P_{≤N}f‖_q ≲ N^{3/p-3/q}‖P_{≤N}f‖_p` | **[DI] via the CP01 record**; not re-fetched here. Note the record's own caution that Tao does not fix `φ` uniquely (M4) |
| E11 | Tao 2013 eq. (9)/(14): normalised pressure `-Δ^{-1}∂_i∂_j(u_iu_j)`, identical to `R_iR_j(u_iu_j)` | matches `cp01-literature-statements.md` §7.3; **independently confirmed from the primary source** via Grafakos Prop. 5.1.17 (see EVIDENCE) | **[DI] confirmed** |
| E12 | Hölder, Fubini–Tonelli, DCT, mean-value inequality; Folland 2nd ed. Thm. 6.2 / 2.37 / 2.24 | not inspected; declared [MO] by the candidate | **[MO], accepted** |
| E13 | `|B(0,r)| = (4π/3)r³`; `∫_{|ξ|≤2}|ξ|²dξ = 128π/5` | recomputed here | **confirmed** |
| E14 | Calderón–Zygmund `L³` bound | declared not used; not inspected | **[MO], unused** |

Bib entry supplied by the candidate: field-by-field agreement with the
title/copyright pages (author, title, edition, series, volume 249,
publisher, address, year 2014, DOI, ISBN). Accept as printed.

---

## 5. Minor editorial issues for the integrator

* **M1.** `def:pressure-work`: the clause "which on `{v≠0}` equals
  `v·∇|v|`" reintroduces `∇|u|`, which D4 removed. Delete it, or move it to
  a remark with the words "classically, on the open set `{v≠0}`".
* **M2.** `def:lp`: "the operator `-Δ^{-1}∂_i∂_j` has the same symbol
  `m^{ij}`" should be phrased through the product symbol
  `(4π²|ξ|²)^{-1}(2πiξ_i)(2πiξ_j)` to avoid composing two unbounded
  multipliers.
* **M3.** Preamble: add `\newtheorem{lemma}[theorem]{Lemma}` and
  `\newtheorem{definition}[theorem]{Definition}`, and precede the latter by
  `\theoremstyle{definition}` (otherwise `def:lp` and `def:pressure-work`
  typeset in italic body text, unlike every other definition-like item in
  the paper) followed by `\theoremstyle{plain}`. Add the `Grafakos2014`
  entry to `references.bib`.
* **M4.** `def:lp`: "so that `S_J` is Tao's projection `P_{≤2^J}`"
  over-identifies; Tao fixes only the support/normalisation of `φ`. Use
  repair R4.
* **M5.** Frontier record §5 "SURVIVING CONDITIONAL SUFFIX" claims
  `sec:quotient`'s `M = 3(1+C_ℙ)C_B2^{5L/2}‖u_0‖₂` "is valid". Only the
  `C_B2^{5L/2}‖u_0‖₂` factor is proved in this lane. Restate as "valid
  provided the quotient lane supplies `‖q‖₃ ≤ (1+‖ℙ‖_{L³→L³})‖w‖₃` and
  `‖A‖_{3/2} = ‖w‖₃²`".
* **M6.** In `lem:fourier-tools`(iv)'s proof the citation
  "`on $L^1\cap L^2$ the $L^1$ transform and $\mathcal F$ agree
  \cite[p.~113]{Grafakos2014}`" should read `p.~114`. The other
  `\cite[p.~113]` (for "(1)–(8),(12),(13) hold for integrable `f,g`") is
  correct as printed.
* **M7.** External-fact table E2 lists item (8) (dilation) as used in
  `lem:lowpass-kernel`(a) and `lem:bernstein`; the LaTeX derives both
  dilation identities by direct substitution and cites (8) nowhere. Either
  cite it or drop it from the "Used in" column.
* **M8.** 18 overfull `\hbox`es in a `margin=1in` layout, the widest
  `29.3pt`. The worst offenders are the three-term displays in
  `lem:gamma`(c) (`|Γ(u(t))-Γ(u(s))| ≤ …`), the two inline `\norm{...}`
  chains that follow it, and the displays in `lem:riesz-kernel`(b),
  `prop:lowpressure`(i) and (B)⇒(A) Step 2. Break them with `align` or
  `split`.
* **M9.** Placement: the candidate leaves the sentence
  "`prop:lowpressure` and `hyp:highpressure` imply `hyp:absorption` with
  `A = A_low + A_high`" inside `rem:existential-scope`, i.e. *after*
  `prop:existential-equivalence`, whereas `eq:pressure-consequence`
  (`main.tex` 345–353) depends on it and comes later in the section. Move
  that sentence out of the remark and back to its original position, citing
  `lem:absorption-split`. Also, after the deletion of the "At these
  existential quantifiers, …" paragraph, the surviving sentences beginning
  "The high-frequency hypothesis is the refined first new gap" form an
  orphan paragraph; attach them to the sentence just moved. Finally,
  consider updating the abstract and §"Proof boundary" per §3.8.
* **M10.** `lem:absorption-split`'s conclusion is phrased as
  "Hypothesis~\ref{hyp:absorption} holds for these `ν, u_0, H`", but a
  Hypothesis is a globally quantified statement. Use repair R5 and add a
  closing sentence: "Consequently, if Hypothesis~\ref{hyp:highpressure}
  holds, then Hypothesis~\ref{hyp:absorption} holds with the same `θ`."
* **M11.** `prop:existential-equivalence` (B)⇒(A) silently drops
  `main.tex`'s prose estimate `|Q_0| ≤ C‖u‖₆³‖∇u‖₂` in favour of
  `|Q_0| ≤ (1+‖κ‖₁)‖p‖₃‖u‖₆‖∇u‖₂`. This is the honest route (it avoids
  Calderón–Zygmund) and `rem:existential-scope` says so, but the change of
  the displayed estimate relative to the frozen manuscript prose should be
  called out to the controller explicitly, not only inside a remark.
* **M12.** Notation clash flagged by the candidate is real: D1 assigns `ψ`
  to the annular symbol `φ(ξ)-φ(2ξ)` (used in `def:lp`/`lem:lp-coincide`),
  while `cp01-quotient-section-structure.md`'s `lem:lowpass` uses `ψ` for
  the *kernel* of `S_L`. This lane's kernel is `κ = φ^∨`. Recommendation:
  keep `ψ` for the annular symbol (D1 binds) and require the quotient lane
  to adopt `κ`; `lem:bernstein` then replaces `lem:lowpass` verbatim.
* **M13.** `prop:lowpressure` is stated "For every integer `J` and every
  `0 ≤ t < T_*`" but item (iii) has no `t`; move (iii) to its own sentence
  quantified over `H` and `τ` only.
* **M14.** `lem:fourier-tools` opens with "Let `n = 3`." but (i)–(iv) are
  dimension-free and Grafakos Thm. 1.2.10 is stated on general groups.
  Harmless; either drop the line or say "we use `n = 3` throughout".

---

## 6. Obligations this review could NOT discharge

Stated exactly.

1. **`prop:pressure` in integrated P-3 form** with
   `X(τ)/3 + ν∫_0^τD_3 = X(0)/3 + ∫_0^τP_3`, `D_3 ≥ 0` pointwise, `P_3`
   integrable on compact subintervals of `[0,T_*)`, and
   `P_3 = ∫p Γ(u)` with `Γ` as in `def:pressure-work`. Owner: pressure lane.
   Not audited here; assumed. Used by `lem:absorption-split`, both
   directions of `prop:existential-equivalence`, and repair R1.
2. **`thm:continuation` in the D3 form** `T_* < ∞ ⟹ sup_{t<T_*}‖u(t)‖₃ = ∞`.
   Owner: continuation lane. As frozen, `main.tex` states a different (and
   per the obligations record ill-formed) conclusion. Used by (A)⇒(B) only.
3. **`prop:localtheory`** with the D2 memberships and uniqueness of the
   branch. Owner: local-theory lane. Used throughout.
4. **The general Bernstein inequality** (Tao 2013 eq. (26)) remains
   unproved; only the instance `k=1, p=2, q=∞` is proved, which is all Q-17
   consumes. This review does not close the general statement either.
5. **E8's exact page** for Grafakos Def. 5.1.13 / Prop. 5.1.14 (claimed
   p. 325) was not printed in the extracted range; the numbering and the
   symbol `-iξ_j/|ξ|` are confirmed, the page is not. Unused fact.
6. **E12** (Folland page/theorem numbers) and **E14** (Grafakos Cor. 5.2.8,
   Stein 1970) were not inspected; both remain [MO]. E14 is unused.
7. The candidate's claim that `lem:bernstein` "can replace `lem:lowpass`
   verbatim" in the quotient section was not verified against the quotient
   lane's actual text, which is not part of this lane's frozen input.

---

## 7. Frontier record

**MODE / RESULT.** REVIEW (round 1) of `cp02-lowpressure.md`. Result:
**PASS**, with two mandatory one-sentence insertions (R1, R2), three
recommended editorial rewrites (R3, R4, R5), and fourteen integrator items
(M1–M14). No invalid bridge was found in fifteen reconstructed steps, and
three separate refutation attempts (an atom of `f̂` at the origin in
`lem:lp-coincide`; the `z=0, c=d=e_1` instance of the bilinear kernel bound;
two near-degenerate pairs for the Lipschitz constant `3`) all failed to
refute.

**CLAIM AND SCOPE.** On the unforced equation on `R³`, arbitrary `ν>0`,
divergence-free Schwartz data, in the classical branch of `prop:localtheory`
(assumed): the candidate's `def:lp`, `lem:lp-coincide`, `lem:fourier-tools`,
`lem:lowpass-kernel`, `lem:riesz-kernel`, `def:pressure-work`, `lem:gamma`,
`prop:lowpressure` (with `C = 32π/3`, sharper `‖φ‖₁`), and `lem:bernstein`
(with `C_B = 2π‖|ξ|φ‖₂ ≤ 16π(2π/5)^{1/2}`) are correct as written and rest
only on package R, `prop:energy`, and nine directly inspected Grafakos
facts. `lem:absorption-split` and `prop:existential-equivalence` are correct
after insertions R1 and R2, conditional on the three cross-lane items in §6.
F-1, P-0 (this lane's share), Q-17's Bernstein input, and X-1 are
discharged at the CP02 standard.

**EVIDENCE.** See §2 EVIDENCE and §3–§4: fifteen reconstructed bridges;
every constant and every Hölder/Young/interpolation exponent recomputed
(`32π/3`, `128π/5`, `16π(2π/5)^{1/2} ≈ 56.35`, `2^{5L/2}`,
`1/3+1/6+1/2 = 1`, `2/3 = 1/6+1/2`); nine Grafakos [DI] claims located in
the third edition by printed page with the edition, ISBN and DOI read from
the copyright page; the pressure normalisation `p = R_iR_j(u_iu_j) =
-Δ^{-1}∂_i∂_j(u_iu_j)` re-derived from Grafakos Prop. 5.1.17 independently
of the CP01 record; the LaTeX block compiled clean against `main.tex`'s
`amsthm` preamble plus two `\newtheorem` lines.

**FIRST GAP.** Within the reviewed text: none. The two justification gaps
R1 and R2 are closed by the insertions supplied above. For the chain the
lane feeds, the first gap is unchanged and is now *provably* the whole
problem for Schwartz data: `hyp:highpressure` is not proved, and
`prop:existential-equivalence` shows it is equivalent to global continuation
of every branch.

**SURVIVING CONDITIONAL SUFFIX.** Unconditional (given R and
`prop:energy`): `prop:lowpressure` and `lem:bernstein` with the explicit
constants above. Given `prop:pressure` (P-3 form, P-0 integrand):
`hyp:highpressure ⟹ hyp:absorption` with `A = A_low + A_high` and
`sup_{t<min(H,T_*)}‖u(t)‖₃³ ≤ ‖u_0‖₃³ + 3A`. Given in addition
`thm:continuation` (D3 form): `hyp:highpressure ⟺ (∀ν,u_0: T_* = ∞)`.

**NON-CLAIMS.** No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or
NS-R3 result is asserted or approached. No bound on `Q_J`, `A_high`, or `θ`
is claimed without assuming global continuation. The general Bernstein
inequality, Calderón–Zygmund theory, `L¹` integrability of any Riesz-type
kernel, and the quotient lane's constant `3(1+C_ℙ)` are neither claimed nor
verified here. `prop:pressure`, `thm:continuation`, `prop:localtheory` are
assumed, not certified.

**NEXT DISTINCT ACTION.** Controller: apply R1–R5 and M1–M14 to
`cp02-lowpressure.md`, then integrate. Two cross-lane confirmations must
precede integration: (a) that the pressure lane's `P_3` integrand is
pointwise `Γ(u)` of `def:pressure-work` and that it delivers `P_3`
integrability on compacts of `[0,T_*)`; (b) that the continuation lane
delivers `thm:continuation` in the D3 form. Then a round-2 review is
warranted only for the *repaired* `prop:existential-equivalence` in the
presence of the actual `prop:pressure` and `prop:localtheory` texts, since
this round audited those two only as interfaces.
