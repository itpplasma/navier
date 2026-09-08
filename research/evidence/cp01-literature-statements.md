# CP1 imported statements: exact texts, locations, and inspection status

Purpose: supply Phase I of the formalization plan with the *published* text of
every result CP1 imports, together with every definition those texts depend on,
so that a Lean 4 statement can be written that is faithful to the source rather
than to a paraphrase. Nothing here proves, weakens, or strengthens any project
claim. NS-R3 remains open; HIGH-PRESSURE and HIGH-STRAIN remain open.

Audit date: 5 September 2026. Files consulted locally:
`../navier-paper/main.tex`, `../navier/PLAN.md`,
`../navier/literature/{foundations,critical-criteria}.md`,
Mathlib checkout `../stafford38/.lake/packages/mathlib`.

## 0. Legend and method

* **[DI]** directly inspected: the primary text was opened and the quoted
  statement read in it. For each such item the exact location is given.
* **[MO]** metadata-only: bibliographic record, abstract, or table of contents
  was opened, but the theorem text was not read in the primary source.
* **[REC]** reconstructed: statement written from secondary attestations; must
  be re-checked against the primary text before it is encoded in Lean.

Primary texts inspected for this note:

| Source | Access route | Status |
|---|---|---|
| Tao, APDE 6 (2013) 25–107 | publisher PDF `https://msp.org/apde/2013/6-1/apde-v6-n1-p02-s.pdf` (page images read as text) **and** arXiv:1108.1165 LaTeX source (`arXiv e-print`, file `local_ns.tex`, last modified 31 May 2012) | [DI] both |
| Gallagher–Koch–Planchon, arXiv:1012.0145 | arXiv e-print LaTeX source (`GKPrevised_16_07_2012.tex`) | [DI] |
| Escauriaza–Seregin–Šverák, Russian Math. Surveys 58:2 (2003) 211–250 | `https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=609&what=fullteng&option_lang=eng` (English translation, pp. 211–220 available) | [DI] pp. 211–220 |
| Seregin, arXiv:1104.3615 | arXiv e-print LaTeX source (`wh2L3__1_.tex`, 19 Apr 2011) | [DI] |
| Kato, Math. Z. 187 (1984) 471–480 | GDZ scan `PPN266833020_0187/LOG_0054`, pages read as images | [DI] pp. 471–474 |
| Fefferman, Clay official problem description | `https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf` | [DI] |
| Stein, *Singular Integrals …* (1970) | published table of contents PDF (`https://www.gbv.de/dms/hebis-darmstadt/toc/83950494.pdf`) | [MO] for theorem text; [DI] for chapter/section pagination |
| Clarkson, Trans. AMS 40 (1936) 396–414 | AMS landing page returned HTTP 403 | [MO] |
| Bahouri–Chemin–Danchin, Grundlehren 343 (2011) | publisher record only | [MO]/[REC] |
| Furioli–Lemarié-Rieusset–Terraneo, Rev. Mat. Iberoam. 16 (2000) 605–667 | EMS Press record + abstract | [MO] |

Sign and normalisation conventions of the four principal sources were compared
term by term against `main.tex` equation `eq:NS`; the comparison is in §7.3.

---

## 1. Tao 2013 — local theory on R^3

Bibliographic identity. Terence Tao, "Localisation and compactness properties of
the Navier–Stokes global regularity problem", *Analysis & PDE* **6** (2013),
no. 1, 25–107, DOI 10.2140/apde.2013.6.25; preprint arXiv:1108.1165. The
manuscript cites this as `\cite{Tao2013}`; `references.bib` record is correct.

Tao normalises the viscosity: his equation is

> `∂_t u + (u · ∇) u = Δu − ∇p + f`   (his (3); arXiv `\label{ns}`)

with `∇ · u = 0` (his (4)) and `u(0,x) = u_0(x)` (his (5)). **ν = 1 throughout.**
He states explicitly (Remark following the smooth-solution definition):
"The viscosity parameter ν was not normalised in [Fefferman 2006] to equal 1, as
we are doing here, but one can easily reduce to the ν = 1 case by a simple
rescaling." He gives **no** rescaling formula; the manuscript's
`eq:nu-normalization` is therefore manuscript-owned, not imported. [DI]

### 1.1 Definitions Theorem 5.4 depends on

All quoted verbatim from the arXiv LaTeX source; the published text agrees
(spot-checked on the PDF).

**Smooth set of data.** "A *smooth set of data* for the Navier-Stokes system up
to time `T` is a triplet `(u_0,f,T)`, where `0 < T < ∞` is a time, the initial
velocity vector field `u_0 : R^3 → R^3` and the forcing term
`f : [0,T] × R^3 → R^3` are assumed to be smooth on `R^3` and `[0,T] × R^3`
respectively …, and `u_0` is furthermore required to be divergence-free:
`∇ · u_0 = 0`. If `f = 0`, we say that the data is *homogeneous*." [DI]

**H^1 norm of data / H^1 data.**
`H^1(u_0,f,T) := ‖u_0‖_{H^1_x(R^3)} + ‖f‖_{L^∞_t H^1_x(R^3)} < ∞`;
"`(u_0,f,T)` is `H^1` if `H^1(u_0,f,T) < ∞`". [DI]

**Schwartz data.** "We say that a smooth set of data `(u_0,f,T)` is *Schwartz*
if, for all integers `α, m, k ≥ 0`, one has
`sup_{x∈R^3} (1+|x|)^k |∇_x^α u_0(x)| < ∞` and
`sup_{(t,x)∈[0,T]×R^3} (1+|x|)^k |∇_x^α ∂_t^m f(x)| < ∞`." [DI]
(The second display's argument is printed as `f(x)`; it is `f(t,x)`. Typo in
both arXiv and published text.)

**Smooth solution.** "A *smooth solution to the Navier-Stokes system* … is a
quintuplet `(u,p,u_0,f,T)`, where `(u_0,f,T)` is a smooth set of data, and the
velocity vector field `u : [0,T] × R^3 → R^3` and pressure field
`p : [0,T] × R^3 → R` are smooth functions on `[0,T] × R^3` that obey" the
Navier–Stokes equation, incompressibility, and the initial condition "on all of
`[0,T] × R^3`". A smooth solution is *finite energy* if the data is and
`‖u‖_{L^∞_t L^2_x([0,T]×R^3)} < ∞`; it is *H^1* if the data is and
`‖u‖_{L^∞_t H^1_x} + ‖u‖_{L^2_t H^2_x} < ∞`. [DI]

**Normalised pressure** (published (9); arXiv `\label{pressure-point}`):
`p = −Δ^{-1} ∂_i ∂_j (u_i u_j) + Δ^{-1} ∇ · f`. [DI]
Here `Δ^{-1}` is the Fourier multiplier `−(4π²|ξ|²)^{-1}` (published (14), p. 38).

**H^1 mild solution on R^3** (verbatim): "define a *`H^1` mild solution*
`(u,p,u_0,f,T)` to be fields `u,f : [0,T] × R^3 → R^3`, `p : [0,T] × R^3 → R`,
`u_0 : R^3 → R^3` with `0 < T < ∞`, obeying the regularity hypotheses
`u_0 ∈ H^1_x(R^3)`, `f ∈ L^∞_t H^1_x([0,T]×R^3)`,
`u ∈ L^∞_t H^1_x ∩ L^2_t H^2_x([0,T]×R^3)` with `p` being given by
[normalised pressure], which obey [`∇·u = 0`], [`∇·u_0 = 0`], and [the Duhamel
identity]". [DI]

Duhamel identity (published (11); arXiv `duhamel-1`):
`u(t) = e^{tΔ} u_0 + ∫_0^t e^{(t−t')Δ} ( −(u·∇)u − ∇p + f )(t') dt'`,
equivalently `u(t) = e^{tΔ}u_0 + ∫_0^t e^{(t−t')Δ}(P B(u,u) + Pf)(t')dt'` with
`B(u,v)_i := −½ ∂_j(u_i v_j + u_j v_i)`. [DI]

**X^s spaces** (published (13), p. 37):
`X^s(I × Ω) := L^∞_t H^s_x(I × Ω) ∩ L^2_x H^{s+1}_x(I × Ω)`.
The subscript on the second factor is a **typo in the published text and in the
arXiv source**: it must be `L^2_t H^{s+1}_x`. Every use in the paper is the
`L^2_t` one. A Lean statement must use `L^2_t`. [DI]

### 1.2 Theorem 5.4, verbatim

Location: *Analysis & PDE* 6 (2013), no. 1, **p. 52** (statement begins at the
foot of p. 52 and runs to the top of p. 53); proof on p. 53. In arXiv:1108.1165
it is the theorem labelled `lwp-h1-r3` in §"Local well-posedness theory in H^1".
[DI]

> **Theorem 5.4 (Local well-posedness in `H^1`).** Let `(u_0, f, T)` be `H^1`
> data.
>
> (i) *(Strong solution).* If `(u, p, u_0, f, T, 1)` is an `H^1` mild solution,
> then `u ∈ C^0_t H^1_x([0,T] × R^3)`.
>
> (ii) *(Local existence and regularity).* If
>
>   `( ‖u_0‖_{H^1_x(R^3)} + ‖f‖_{L^1_t H^1_x(R^3)} )^4 T ≤ c`   (46)
>
> for a sufficiently small absolute constant `c > 0`, then there exists a `H^1`
> mild solution `(u, p, u_0, f, T)` with the indicated data, with
> `‖u‖_{X^1([0,T]×R^3)} ≲ ‖u_0‖_{H^1_x(R^3)} + ‖f‖_{L^1_t H^1_x(R^3)}`,
> and more generally
> `‖u‖_{X^k([0,T]×R^3)} ≲_{k, ‖u_0‖_{H^k_x(R^3)}, ‖f‖_{L^1_t H^k_x(R^3)}} 1`
> for each `k ≥ 1`. In particular, one has local existence whenever `T` is
> sufficiently small depending on `H^1(u_0, f, T)`.
>
> (iii) *(Uniqueness).* There is at most one `H^1` mild solution
> `(u, p, u_0, f, T)` with the indicated data.
>
> (iv) *(Regularity).* If `(u, p, u_0, f, T, 1)` is an `H^1` mild solution, and
> `(u_0, f, T)` is Schwartz, then `u` and `p` are smooth; in fact, one has
> `∂_t^j u, ∂_t^j p ∈ L^∞_t H^k([0,T] × R^3)` for all `j, k ≥ 0`.
>
> (v) *(Lipschitz stability).* Let `(u,p,u_0,f,T)`, `(u',p',u'_0,f',T)` be `H^1`
> mild solutions with the bounds `0 < T ≤ T_0` and
> `‖u‖_{X^1}, ‖u'‖_{X^1} ≤ M`. Define
> `F(t) := e^{tΔ}(u'_0 − u_0) + ∫_0^t e^{(t−t')Δ}(f'(t') − f(t')) dt'`.
> If the quantity `‖F‖_{L^2_t L^2_x([0,T]×R^3)}` is sufficiently small depending
> on `T, M`, then `‖u − u'‖_{X^1([0,T]×R^3)} ≲_{T,M} ‖F‖_{L^2_t L^2_x}`.

Exactness notes for the Lean statement.

1. The `X^k` bound in (ii) is printed with an **empty right-hand side** in both
   the published text (`kuk X k .k,ku0k H k ,kf k L1 H k ,1`) and in the arXiv
   source (`\lesssim_{k,\|u_0\|_{H^k_x},\|f\|_{L^1_t H^k_x},1}` followed by
   nothing). The intended meaning is `‖u‖_{X^k} ≤ C(k, ‖u_0‖_{H^k}, ‖f‖_{L^1_tH^k})`,
   i.e. `≲ 1` with those dependencies. Encoding this literally is impossible; the
   axiom must state the intended form and say so.
2. The tuple in (i) and (iv) is written with a spurious sixth slot `,1` (a
   leftover from the periodic tuples `(u,p,u_0,f,T,L)`); on `R^3` there is no
   period parameter. Cosmetic, but it must not be copied into a Lean signature.
3. `H^1` *data* requires `f ∈ L^∞_t H^1_x` while the smallness condition (46)
   and the conclusion use `‖f‖_{L^1_t H^1_x}`. For CP1, `f ≡ 0`, so both are
   `0` and the discrepancy is inert. It is **not** inert for any forced variant.
4. (ii) is a **smallness-conditional local** existence statement. It does not by
   itself supply a maximal solution on `[0,T_*)`. See §1.3.
5. (iv) presupposes that an `H^1` mild solution exists on `[0,T]`; it upgrades
   regularity, it does not produce a solution. The manuscript's use ("smooth
   through the initial time … by the directly stated local theorem of Tao
   [Theorem 5.4]") is correct only after (ii)+(iii)+§1.3 have produced the
   solution on `[0,T]` for `T < T_*`.
6. In Tao's proof of (iv) he remarks: "these arguments did not require the full
   power of the hypothesis that `(u_0,f,T)` was Schwartz; it would have sufficed
   to have `u_0 ∈ H^k_x(R^3)` and `f ∈ C^j_t H^k_x(R^3)` for all `j,k ≥ 0`."
   This is a remark inside a proof, not part of the theorem statement; do not
   encode it as part of the axiom. [DI]

### 1.3 Corollary 5.8 — the maximal-time statement the manuscript actually needs

Location: *Analysis & PDE* 6 (2013), no. 1, **pp. 56–57** (Remark 5.9 is on
p. 57). arXiv label `max-cauchy`. [DI]

Preceding definition, verbatim: "Define an *incomplete mild `H^1` solution*
`(u,p,u_0,f,T_*^-)` from `H^1` data `(u_0,f,T_*)` to be fields
`u : [0,T_*) × R^3 → R^3` and `v : [0,T_*) × R^3 → R` such that for any
`0 < T < T_*`, the restriction `(u,p,u_0,f,T,1)` … to the slab `[0,T] × R^3`
is a mild `H^1` solution." (The letter `v` for the pressure field is a typo for
`p`, in both arXiv and published text.)

> **Corollary 5.8 (Maximal Cauchy development).** Let `(u_0,f,T)` be `H^1` data.
> Then at least one of the following two statements hold:
> * There exists a mild `H^1` solution `(u,p,u_0,f,T)` with the given data.
> * There exists a blowup time `0 < T_* < T` and an incomplete mild `H^1`
>   solution `(u,p,u_0,f,T_*^-)` up to time `T_*^-`, which blows up in the
>   enstrophy norm in the sense that
>   `lim_{t→T_*^-} ‖u(t)‖_{H^1_x(R^3)} = +∞`.

> **Remark 5.9.** In the second conclusion of Corollary 5.8, more information
> about the blowup is known. For instance, in [Iskauriaza et al. 2003] it was
> demonstrated that the `L^3_x(R^3)` norm must also blow up (in the homogeneous
> case `f = 0`, at least).

**Audit finding (blocking for Phase I, minor for the paper).** `main.tex` at
`premise:local` writes "Standard local theory gives a unique maximal classical
solution on `[0,T_*)`, where `0 < T_* ≤ ∞` … by the directly stated local
theorem of Tao [Theorem 5.4]". Theorem 5.4 alone does **not** state this.
The chain is: Theorem 5.4(ii)+(iii) → Corollary 5.8 (dichotomy on each finite
`T`) → a manuscript-owned gluing/supremum argument producing a single maximal
`T_*(u_0) ∈ (0,∞]` and an incomplete solution on `[0,T_*)` → Theorem 5.4(iv)
for smoothness on each `[0,T]`, `T < T_*`. Phase I must therefore import
**both** Theorem 5.4 and Corollary 5.8 as axioms, and prove the gluing step.
Remark 5.9 is a remark citing ESS, not an independent theorem, and must not be
imported as one.

Bibliographic identity note: Tao's bibliography prints ESS as
"[Iskauriaza et al. 2003]" (a back-transliteration of Escauriaza from the
Russian original). Same paper, same DOI.

### 1.4 Facts from Tao §2 reusable as directly-inspected sources for standard analysis

These are in the same directly-inspected source and cover several of the
"standard harmonic analysis facts" of CP1 exactly.

* **Leray projection, definition and `L^p` boundedness**, p. 38, verbatim:
  "We define the Leray projection `Pu` of a (tempered distributional) vector
  field `u : R^3 → R^3` by the formula `Pu := Δ^{-1}(∇ × ∇ × u)`. If `u` is
  square-integrable, then `Pu` is the orthogonal projection of `u` onto the
  space of square-integrable divergence-free vector fields; from
  Calderón–Zygmund theory, we know that the projection `P` is bounded on
  `L^p_x(R^3)` for every `1 < p < ∞`, and from Fourier analysis we see that `P`
  is also `H^s_x(R^3)` for every `s ∈ R`." (The last clause is missing "bounded
  on".) [DI]
* **Heat semigroup and Young's inequality**, p. 39, verbatim: "we let `e^{tΔ}`
  for `t > 0` be the usual heat semigroup associated to the heat equation
  `u_t = Δu`. On `R^3`, this takes the explicit form
  `e^{tΔ}f(x) = (4πt)^{-3/2} ∫_{R^3} e^{-|x−y|²/4t} f(y) dy` for
  `f ∈ L^p_x(R^3)` for some `1 ≤ p ≤ ∞`. From Young's inequality, we thus record
  the dispersive inequality
  `‖e^{tΔ}f‖_{L^q(R^3)} ≲ t^{3/2q − 3/2p} ‖f‖_{L^p(R^3)}` (18)
  whenever `1 ≤ p ≤ q ≤ ∞` and `t > 0`." The `p = q` case is exactly the
  `L^p` contraction used in `sec:quotient` ("Heat … contracts `L^3`"), with
  implied constant `1`. [DI]
* **Littlewood–Paley projections and Bernstein estimates**, p. 40, equation
  (26), verbatim. `φ` is a fixed bump supported in `{|ξ| ≤ 2}`, equal to `1` on
  `{|ξ| ≤ 1}`; `N = 2^k` dyadic; `\hat{P_{≤N}f}(ξ) := φ(ξ/N)\hat f(ξ)`,
  `\hat{P_{>N}f} := (1 − φ(ξ/N))\hat f`,
  `\hat{P_N f} := ψ(ξ/N)\hat f := (φ(ξ/N) − φ(2ξ/N))\hat f`. Then
  ```
  ‖D^s P_N f‖_{L^p_x(R^3)} ≲_{p,s,D^s} N^s ‖P_N f‖_{L^p_x(R^3)},
  ‖∇^k P_N f‖_{L^p_x(R^3)} ∼_{k,s}   N^k ‖P_N f‖_{L^p_x(R^3)},
  ‖P_{≤N} f‖_{L^q_x(R^3)} ≲_{p,q} N^{3/p − 3/q} ‖P_{≤N} f‖_{L^p_x(R^3)},
  ‖P_N f‖_{L^q_x(R^3)}    ≲_{p,q} N^{3/p − 3/q} ‖P_N f‖_{L^p_x(R^3)}
  ```
  "for all `1 ≤ p ≤ q ≤ ∞`, `s ∈ R`, `k ≥ 0`, and pseudodifferential operators
  `D^s` of order `s`; see, for example, [Tao 2006, Appendix A]." [DI]
  The third line, combined with the second, is exactly what `sec:quotient` needs
  for `‖∇ S_L u‖_∞ ≤ C 2^{5L/2}‖u‖_2` (take `k = 1`, `p = 2`, `q = ∞`,
  `N ∼ 2^L`). Note the second line's subscript `∼_{k,s}` should be `∼_k`.
  Caution: Tao's `P_{≤N}` cutoff is a *smooth* bump; the manuscript's `S_J`
  (§ after `prop:pressure`) is defined from "a smooth homogeneous
  Littlewood–Paley partition" with `S_J = Σ_{j≤J} Δ_j`. These agree up to the
  choice of `φ`; the manuscript must fix one convention before Lean encoding,
  because `prop:lowpressure`'s constant `C2^{3J}` depends on it.

---

## 2. Gallagher–Koch–Planchon — the endpoint criterion in maximal-`L^3` form

Bibliographic identity. I. Gallagher, G. S. Koch, F. Planchon, "A profile
decomposition approach to the `L^∞_t(L^3_x)` Navier–Stokes regularity
criterion", *Math. Ann.* **355** (2013), 1527–1559, DOI 10.1007/s00208-012-0825-0;
preprint arXiv:1012.0145 (source file `GKPrevised_16_07_2012.tex`). The
manuscript's `\cite{GKP2013}` record is correct.

### 2.1 The equation and the solution concept

Verbatim from the arXiv source, Introduction:

> "We consider the incompressible Navier-Stokes equations in `R^d`,
> `(NS)  ∂u/∂t = Δu − ∇·(u⊗u) − ∇π,  ∇·u = 0,  u|_{t=0} = u_0`
> for `(x,t) ∈ R^d × (0,T)`, where `u = u(x,t)` is the velocity vector field and
> `π(x,t)` is the associated pressure function."

**Unit viscosity**, confirmed directly: `Δu` carries no `ν`. The manuscript's
remark "Gallagher, Koch, and Planchon state the theorem for unit viscosity" is
correct. [DI]

Verbatim from §1 (Preliminaries), definition of `NS(u_0)` and of the maximal
time:

> "For any `p` in `[1,∞)` we define `s_p := −1 + d/p`. For any initial datum
> `u_0 ∈ Ḃ^{s_p}_{p,q}`, with `d < p ≤ q < +∞`, we shall denote by `NS(u_0)` the
> local in time strong solution to the Navier-Stokes equation (NS). For clarity,
> by 'solution' to (NS) in the strong (sometimes called 'mild') sense, we mean a
> divergence-free solution `u` to
> `u_t = Δu − P ∇·(u⊗u),  u|_{t=0} = u_0`
> (equivalent to solving (NS) for the 'right' `π`) in the Duhamel sense, where
> `P` is the projection operator onto divergence-free vector fields. …
> The specific case of `L^d ( ↪ Ḃ^{−(1−d/p)}_{p,q})` data is included in such a
> result, as any additional 'regularity' is propagated along the flow …"
>
> "We define the function space
> `E_{p,q}(T) := L^∞([0,T]; Ḃ^{s_p}_{p,q}) ∩ L^{2p/(p+1)}([0,T]; Ḃ^{s_p+1+1/p}_{p,q})`
> [in the paper's `\mathcal{L}^ρ` time-Besov notation] … We recall … that
> `NS(u_0)` belongs to `E_{p,q}(T)` for some time `T`, and one may define a
> maximal time `T^* = T^*(u_0)` such that this holds for any `T < T^*` …
> If the initial datum is small enough then `T^* = ∞` (and under such a
> condition one may include `q = ∞`, although one cannot in general obtain local
> solutions for `q = ∞`). Moreover, `u` belongs to `E_{p,q}(T^*)` if and only if
> `T^* = ∞` … Finally recall that if `NS(u_0)` belongs to `E_{p,q}(T)` and if
> `u_0` belongs to `Ḃ^{s_a}_{a,b}` (resp. `L^d(R^d)`) with `a ≤ p` and `b ≤ q`,
> then `NS(u_0)` belongs to `E_{a,b}(T)` (resp. `C([0,T]; L^d(R^d))`) with the
> same life span." [DI]

The local theory is attributed to Cannone (for `3 < p ≤ 6`), Planchon (all
`p < ∞`), with a proof "taylored to our purposes" in the appendix of their
reference `[gip3]`; the Introduction cites "a long line of work on constructing
local in time solutions, from `[KF]` to `[KT]`" (Fujita–Kato to Koch–Tataru).
GKP do **not** reprove the local theory. [DI]

### 2.2 Theorem 4, verbatim

Location: arXiv:1012.0145, §"Serrin's endpoint regularity criterion",
subsection "Preliminaries and statement of the main result". The `thm`
environment is numbered sequentially from the start of the paper
(`\newtheorem{thm}{Theorem}`); the four preceding `thm`s are the two data
profile-decomposition theorems, the NSE evolution of profile decompositions,
and then this one — hence **Theorem 4**. In the published *Math. Ann.* version
it is §3.1. [DI]

> **Theorem 4 (Endpoint regularity criterion).** For any `u_0 ∈ L^3(R^3)`,
>
>   `sup_{t ∈ [0, T^*(u_0))} ‖NS(u_0)(t)‖_{L^3(R^3)} < ∞  ⟹  T^*(u_0) = +∞ .`

Immediately following, verbatim:

> "Note that due to the time-continuity in `L^3(R^3)` of strong solutions, the
> left-hand side is equivalent to
> `NS(u_0) ∈ L^∞((0,T^*(u_0)); L^3(R^3))`, or in the notation of [ess],
> `NS(u_0) ∈ L_{3,∞}(0, T^*(u_0))`."

And in the preceding paragraph: "Such a statement was proved in [ess] for
`X = L^3(R^3)` (in the context of Leray-Hopf weak solutions). … This will give
a different proof of the following, which was proved in [ess] and also extended
to `d > 3` in [dongdu2]". [DI]

Exactness notes for the Lean statement.

1. The theorem line says "for any `u_0 ∈ L^3(R^3)`" and does **not** repeat the
   divergence-free hypothesis; solenoidality is carried by the definition of
   `NS(u_0)` ("a divergence-free solution `u`"). A Lean statement must make
   `∇ · u_0 = 0` explicit.
2. `T^*(u_0)` is defined through `E_{p,q}` for a chosen pair `d < p ≤ q < ∞`;
   its independence of `(p,q)` and its agreement with the `L^3` life span is
   asserted in the Preliminaries ("with the same life span"), citing `[gip3]`.
   For Lean, `T^*` must be pinned by one definition and the independence either
   axiomatised alongside or avoided.
3. The theorem is stated for `d = 3` only. `[dongdu2]` for `d > 3` is not
   needed by CP1.
4. The manuscript's paraphrase in `main.tex` — "if `u_0 ∈ L^3(R^3)` and the
   maximal `L^3` solution has `sup_{t<T_*}‖u(t)‖_3 < ∞`, then `T_* = ∞`" — is
   faithful. The manuscript's remark that "`L_{3,∞}` in the original title does
   not mean the weak spatial Lorentz space `L^{3,∞}_x`" is **confirmed twice**:
   by GKP's own sentence above, and independently by ESS's definition of the
   mixed norm (§3.1 below).

---

## 3. Escauriaza–Seregin–Šverák 2003 — the original form

Bibliographic identity. L. Escauriaza, G. Seregin, V. Šverák,
"`L_{3,∞}`-solutions of the Navier–Stokes equations and backward uniqueness",
*Russian Mathematical Surveys* **58**:2 (2003), 211–250 (Russian original:
*Uspekhi Mat. Nauk* 58:2, 3–44), DOI 10.1070/RM2003v058n02ABEH000609.
Abstract, verbatim: "It is shown that the `L_{3,∞}`-solutions of the Cauchy
problem for the three-dimensional Navier–Stokes equations are smooth." [DI]

### 3.1 Setting, verbatim (pp. 211–213)

Equation (1.1)–(1.2), p. 211:

> `∂_t v(x,t) + div v(x,t) ⊗ v(x,t) − Δv(x,t) = −∇p(x,t)`,  `div v(x,t) = 0`,
> for `x ∈ R^3` and `t ⩾ 0`, with `v(x,0) = a(x)`, `x ∈ R^3`.

**Unit viscosity.** "To begin with, we assume that `a` is a smooth solenoidal
vector field on `R^3` decaying sufficiently fast as `x → ∞`." [DI]

`Ċ_0^∞` = infinitely differentiable solenoidal vector fields with compact
support in `R^3`; `J°`, `J°_{1/2}` their closures in `L^2` and `W^1_2`.
`Q_T = R^3 × ]0,T[`. A **Leray–Hopf weak solution** on `Q_T` is
`v : Q_T → R^3` with (1.3) `v ∈ L^∞(0,T; J°) ∩ L^2(0,T; J°_{1/2})`, (1.4) weak
time-continuity against every `w ∈ L^2`, (1.5) the distributional equation
against `w ∈ Ċ_0^∞(Q_T)`, (1.6) the global energy inequality
`½∫|v(x,t_0)|² dx + ∫_{R^3×]0,t_0[}|∇v|² ⩽ ½∫|a|²` for all `t_0 ∈ [0,T]`, and
(1.7) `‖v(·,t) − a(·)‖_2 → 0` as `t → 0`. [DI]

**Mixed Lebesgue norm** (p. 213), verbatim:
`‖f‖_{s,l,Q_T} = ( ∫_0^T ‖f(·,t)‖_s^l dt )^{1/l}` for `l ∈ [1,+∞[`, and
`= ess sup_{t ∈ ]0,T[} ‖f(·,t)‖_s` for `l = +∞`.
Hence **`L_{3,∞}(Q_T)` in this paper means `L^∞_t L^3_x`, not weak-`L^3`.** [DI]
This settles the manuscript's `L_{3,∞}` remark from the primary source.

### 3.2 The classical-solution formulation, verbatim (p. 214)

Immediately before Theorem 1.3, verbatim:

> "We prove that Leray's result in (iii) has the following analogue for `p = 3`.
> If `]0,T_*[` is the maximal interval on which a smooth solution of the problem
> (1.1), (1.2) exists and if `T_* < +∞`, then
>
>   `lim sup_{t ↑ T_*} ∫_{R^3} |v(x,t)|^3 dx = +∞`.
>
> In other words, the spatial `L^3`-norm of `v` must be infinite if the solution
> has a singularity. We can also interpret this result as an extension of
> Theorem 1.2 to the case `s = 3, l = +∞`." [DI]

This is exactly the statement CP1 wants in classical form. **It is stated as
running prose, not as a numbered theorem**; the numbered results are:

> **Theorem 1.3.** Suppose that `v` is a weak Leray–Hopf solution of the Cauchy
> problem (1.1), (1.2) in `Q_T` and `v` satisfies the additional condition
> `v ∈ L_{3,∞}(Q_T)`  (1.13). Then `v ∈ L^5(Q_T)` (1.14), and hence it is smooth
> and unique on `Q_T`.

> **Theorem 1.4.** Let `v` and `p` be two functions defined on the space-time
> cylinder `Q = B × ]0,1[`, where `B(r) ⊂ R^3` … and `B = B(1)`. Suppose that
> `v` and `p` satisfy the Navier–Stokes equations on `Q` in the sense of
> distributions and have the following differentiability properties:
> `v ∈ L_{2,∞}(Q) ∩ L^2(−1,0; W^1_2(B))`, `p ∈ L_{3/2}(Q)`  (1.15).
> If in addition `‖v‖_{3,∞,Q} < +∞`  (1.16), then the function `v` is Hölder
> continuous on the closure of the set `Q(1/2) = B(1/2) × ]−(1/2)²,0[`.

Also on p. 212, the Leray facts they quote, verbatim: "(i) There is a number
`T_* > 0` such that for `t < T_*` the Cauchy problem (1.1),(1.2) has a unique
smooth solution with 'reasonable' properties at `∞`." — the phrase
"'reasonable' properties at `∞`" is **not** made precise in the paper. This is
why CP1 should not use ESS as the local-theory source; Tao Theorem 5.4 is the
one with a stated solution class. [DI]

Additional definitions used (p. 215): **suitable weak solution** (Definition 2.1,
Lin's version) on `ω × ]−T_1, T[`: (2.1) `u ∈ L_{2,∞} ∩ L^2(−T_1,T;W^1_2(ω))`,
(2.2) `q ∈ L_{3/2}`, (2.3) the equations in the distribution sense, (2.4) the
local energy inequality
`∫_ω φ|u(x,t)|²dx + 2∫_{ω×]−T_1,t[}φ|∇u|² ⩽ ∫_{ω×]−T_1,t[}(|u|²(Δφ + ∂_tφ) + u·∇φ(|u|² + 2q))`
for a.e. `t` and all nonnegative `φ ∈ C_0^∞(R^3)` vanishing near the parabolic
boundary. [DI]

The Appendix (pp. 243–248) contains, per the paper's own §1 roadmap, "the
well-known theorem on short-time solubility in the class
`C([0,T_*]; L^3) ∩ L^5(Q_{T_*})` of the Cauchy problem with initial data in
`L^3 ∩ J°`". Text not inspected (the freely available portion ends at p. 220).
[MO for the Appendix]

### 3.3 Seregin's sharpening (used only as corroboration)

G. Seregin, "A certain necessary condition of potential blow up for
Navier-Stokes equations", arXiv:1104.3615 (19 Apr 2011); published *Comm. Math.
Phys.* **312** (2012), 833–845, DOI 10.1007/s00220-011-1391-x (publication data
[MO]; text [DI] from the arXiv source).

Setting: `∂_t v + v·∇v − Δv = −∇q`, `div v = 0` on `R^3 × ]0,∞[`, unit
viscosity, with `a ∈ C^∞_{0,0}(R^3) ≡ {v ∈ C^∞_0(R^3) : div v = 0}` (compactly
supported smooth solenoidal data); `v` an *energy solution* (global Leray
solution satisfying the global energy inequality); `T` a blow-up time =
"the first instant of time `T` when singularities occur", singularity defined
pointwise via essential boundedness on parabolic balls. Verbatim, his (1.6):

> "Here, we address the critical case `m = 3`, for which … a weaker statement
> `lim sup_{t → T−0} ‖v(·,t)‖_3 = ∞`  (1.6) has been proven in [ESS4]."

> **Theorem 1.1.** Let `v` be an energy solution to the Cauchy problem (1.1) and
> (1.2) with the initial data satisfying (1.3). Let `T > 0` be a finite blow up
> time. Then `lim_{t → T−0} ‖v(·,t)‖_3 = ∞` holds true.

Note the attribution: Seregin attributes the `lim sup` form (not the `lim`
form) to ESS, consistent with §3.2. CP1 needs only the `lim sup` /
`sup < ∞ ⟹ T_* = ∞` form. [DI]

---

## 4. Kato 1984 and `L^3` uniqueness

### 4.1 Kato, Math. Z. 187 (1984) 471–480

Bibliographic identity. Tosio Kato, "Strong `L^p`-Solutions of the
Navier-Stokes Equation in `R^m`, with Applications to Weak Solutions",
*Math. Z.* **187** (1984), 471–480, DOI 10.1007/BF01174182. Read from the GDZ
scan of the journal volume. [DI, pp. 471–474]

Setting, p. 471, verbatim:

> "(NS)  `∂_t u − Δu + (u·∂)u + ∂p = f(t)`, `t > 0, x ∈ R^m`;
> `∂·u = 0`, `u(0,x) = a(x)`.  (`∂ = ∇ = grad`)
>
> We are mainly interested in the strong solutions `u(t)` in
> `PL^m = PL^m(R^m; R^m)` (and its subspaces), since they exist locally in time
> if the initial velocity `a` is in `PL^m` (without any differentiability for
> `a`), and globally if `‖a‖_m` is sufficiently small. Here and in what follows
> we denote by `PL^p` the subspace of `L^p(R^m; R^m)` characterized by the
> divergence condition `div u = 0`, and by `‖·‖_p` the associated norm. As usual
> we talk about the solution `u` of (NS), disregarding the pressure field `p`,
> which is automatically determined by `u` via (NS) up to an inessential
> additive function of time."

**Unit viscosity.** `−Δu`, no `ν`. "Our main results are summarized in the
following theorems, in which we assume for simplicity that `f = 0`". [DI]

Solution concept, p. 473, verbatim: (NS) is rewritten as `∂_t u + Au + F(u) = 0`
(ABS) with `A = −PΔ = −ΔP`, `F(u) = F(u,u)`, `F(u,v) = P(u·∂)v` (2.1); "`P` is
the orthogonal projection of `L^2` onto the subspace `PL^2`; as is well known,
`P` is extended to a bounded operator on `L^p` to `PL^p`, `1 < p < ∞`". (ABS)
"is then converted into the integral equation `u = u_0 + Gu` (INT) where
`u_0(t) = e^{-tA}a`, `Gu(t) = −∫_0^t e^{-(t-s)A}F(u(s)) ds` (2.2)." [DI]

Statements, p. 472, verbatim:

> **Theorem 1.** Let `a ∈ PL^m`. Then there is `T > 0` and a unique solution `u`
> such that
>
>   `t^{(1−m/q)/2} u ∈ BC([0,T]; PL^q)   for m ≤ q ≤ ∞,`   (1.1)
>   `t^{1−m/2q} ∂u ∈ BC([0,T]; PL^q)     for m ≤ q < ∞,`   (1.1′)
>
> both with values zero at `t = 0` except for `q = m` in (1.1), in which
> `u(0) = a`. Moreover, `u` has the additional property
>
>   `u ∈ L^r(0,T_1); PL^q)  with 1/r = (1 − m/q)/2, m < q < m²/(m−2),`  (1.2)
>
> with some `0 < T_1 ≤ T`.

> **Theorem 2.** There is `λ > 0` such that if `‖a‖_m ≤ λ`, then the solution `u`
> in Theorem 1 is global, i.e. we may take `T = T_1 = ∞`. In particular,
> `‖u(t)‖_q` decays like `t^{−(1−m/q)/2}` as `t → ∞`, including `q = ∞`, and
> `‖∂u(t)‖_q` decays like `t^{−(1−m/2q)}`, including `q = m`.

(`BC` = "the class of bounded and continuous functions", stated on p. 472.
Theorems 2′, 3, 4, 4′ concern decay and `PL^m ∩ PL^p` data; not needed by CP1.)

Exactness notes.

1. **The uniqueness class is *not* `C([0,T]; L^3)`.** Kato's uniqueness in
   Theorem 1 is uniqueness *among solutions satisfying (1.1) and (1.1′)* — the
   Kato class with the auxiliary weighted norms `t^{(1−m/q)/2}‖u(t)‖_q` and
   `t^{1−m/2q}‖∂u(t)‖_q` finite, continuous, and vanishing at `t = 0`. This is
   the exact point CP1's brief asks about, and it must be encoded literally.
2. Relevant instance for CP1: `m = 3`, so `PL^3(R^3)`, and (1.2) reads
   `1/r = (1 − 3/q)/2`, `3 < q < 9`.
3. The manuscript uses Kato only in the sentence "Small initial `L^3` norm is
   covered by critical small-data theory `\cite{Kato1984}`". That use is
   Theorem 2 with `m = 3`, and is a remark, **not** load-bearing for
   `thm:conditional`. It need not become a Phase I axiom.
4. Remark 1.1(a), p. 472, verbatim: "As is well known, the solution `u` is
   smooth for `t > 0`." — a remark, not a theorem; do not import.

### 4.2 Uniqueness in `C([0,T]; L^3)`

G. Furioli, P. G. Lemarié-Rieusset, E. Terraneo, "Unicité dans `L^3(R^3)` et
d'autres espaces fonctionnels limites pour Navier-Stokes", *Revista Matemática
Iberoamericana* **16** (2000), no. 3, 605–667, DOI 10.4171/RMI/286. Abstract,
verbatim from the EMS Press record: "The main result of this paper is the proof
of uniqueness for mild solutions of the Navier-Stokes equations in `L^3(R^3)`.
This result is extended as well to some Morrey-Campanato spaces." [MO — the
theorem text was **not** inspected; the article is French-language and behind
the publisher.]

**Do not encode this as a Phase I axiom on the strength of the abstract.** The
statement usually attributed to it — *mild solutions of (NS) on `R^3` in
`C([0,T]; L^3(R^3))` with the same divergence-free `L^3` datum coincide* — is
[REC]. CP1 does **not** need it: the manuscript's uniqueness chain runs through
Tao Theorem 5.4(iii) (uniqueness of `H^1` mild solutions) plus GKP's own
maximal-`L^3` solution being the one whose life span Theorem 4 bounds. If a
later revision wants the `C_tL^3` uniqueness statement, the primary text must be
read first.

Related [MO] records that would have to be inspected if this route is taken:
ESS's own list of prior `L_{3,∞}` uniqueness results (their references
[22],[23],[26],[43], cited on p. 214 as "The uniqueness of `v` under the
condition (1.13) was already known").

---

## 5. Fefferman's Clay statement

Bibliographic identity. Charles L. Fefferman, "Existence and Smoothness of the
Navier–Stokes Equation", official problem description, Clay Mathematics
Institute; reprinted in *The Millennium Prize Problems*, CMI/AMS 2006, 57–67.
Text read from `https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf`
(standalone PDF, pp. 1–2 = volume pp. 57–58). [DI]

Verbatim, pp. 1–2:

> `(1)  ∂/∂t u_i + Σ_{j=1}^n u_j ∂u_i/∂x_j = ν Δu_i − ∂p/∂x_i + f_i(x,t)   (x ∈ R^n, t ≥ 0)`
> `(2)  div u = Σ_{i=1}^n ∂u_i/∂x_i = 0   (x ∈ R^n, t ≥ 0)`
> `(3)  u(x,0) = u°(x)   (x ∈ R^n)`
>
> "Here, `u°(x)` is a given, `C^∞` divergence-free vector field on `R^n`,
> `f_i(x,t)` are the components of a given, externally applied force …, `ν` is a
> positive coefficient (the viscosity) …"
>
> `(4)  |∂_x^α u°(x)| ≤ C_{αK}(1 + |x|)^{−K}   on R^n, for any α and K`
> `(5)  |∂_x^α ∂_t^m f(x,t)| ≤ C_{αmK}(1 + |x| + t)^{−K}   on R^n × [0,∞), for any α, m, K`
>
> "We accept a solution of (1), (2), (3) as physically reasonable only if it
> satisfies
> `(6)  p, u ∈ C^∞(R^n × [0,∞))`
> and
> `(7)  ∫_{R^n} |u(x,t)|² dx < C   for all t ≥ 0   (bounded energy).`"
>
> **"(A) Existence and smoothness of Navier–Stokes solutions on `R^3`.** Take
> `ν > 0` and `n = 3`. Let `u°(x)` be any smooth, divergence-free vector field
> satisfying (4). Take `f(x,t)` to be identically zero. Then there exist smooth
> functions `p(x,t)`, `u_i(x,t)` on `R^3 × [0,∞)` that satisfy (1), (2), (3),
> (6), (7)."

Exactness notes.

1. Hypothesis (4) with "for any `α` and `K`" is precisely the Schwartz
   condition on `u°`; so "Clay datum" = smooth, divergence-free, Schwartz. This
   matches Tao's Schwartz-data definition (§1.1) and the manuscript's
   `u_0 ∈ S(R^3)^3`. The two are interchangeable, and that equivalence is a
   manuscript-owned (trivial) step.
2. In (7) the bound is a **single constant `C` uniform in `t`**, i.e.
   `sup_{t≥0}‖u(t)‖_2² < ∞`. The manuscript's `def:target` states exactly this.
   ✓ faithful.
3. Fefferman requires (6) on the **closed** half-line `[0,∞)`, i.e. smoothness
   including `t = 0`. The manuscript's proof of `thm:conditional` handles this
   by invoking Tao Theorem 5.4(iv). ✓
4. The whole-space alternative (A) sets `f ≡ 0`. The manuscript's equation
   `eq:NS` is unforced. ✓
5. **(A) is a target to be *encoded*, not a theorem to be axiomatised.** It must
   appear in `Challenge.lean` as a `Prop`, with `ν` universally quantified.
6. Everything else on pp. 2–4 (blow-up-time discussion, Beale–Kato–Majda for
   Euler, the weak-solution definition (12)–(13), the rough CKN theorem) is
   expository background in Fefferman's own words and must not be cited as a
   theorem source with hypotheses. In particular Fefferman's sentence "For the
   Navier–Stokes equations (`ν > 0`), if there is a solution with a finite
   blowup time `T`, then the velocity … becomes unbounded near the blowup time"
   has no stated solution class and is unusable for Phase I.

---

## 6. Standard analysis facts: exact statement, source, and Mathlib status

Legend for the last column, checked against the local Mathlib checkout at
`../stafford38/.lake/packages/mathlib` (grep only, no build):
**present** = a usable statement exists; **partial** = a nearby statement exists
but not the one needed; **absent** = no such development.

| # | Fact, in the form the manuscript uses it | Best primary location | Status | Mathlib |
|---|---|---|---|---|
| S1 | Riesz transforms `R_j = ∂_j(−Δ)^{-1/2}` are bounded on `L^p(R^3)`, `1 < p < ∞`; hence `p = R_iR_j(u_iu_j) ∈ L^2 ∩ L^3` when `u ∈ L^4 ∩ L^6` (used in `prop:pressure`) | Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton UP 1970: Ch. II §2 "Singular integrals: the heart of the matter", pp. 28–34 (the `L^p` theorem) and Ch. III §1 "The Riesz transforms", pp. 54–60. Pagination confirmed from the published table of contents. | book text [MO]; TOC/pagination [DI] | **absent** (no Calderón–Zygmund theory, no Riesz transforms; `Mathlib/Analysis/Distribution/FourierMultiplier.lean` gives multipliers on `𝓢` and `𝓢'` only, with no `L^p` bounds) |
| S2 | Leray/Helmholtz projection `P` bounded on `L^p(R^3)`, `1 < p < ∞`; `P` annihilates gradients (used in `sec:quotient` for `‖P‖_{L^3→L^3}` and the `G_3` annihilation) | **Tao 2013, p. 38** (verbatim in §1.4 above) — same directly-inspected source already in CP1. Underlying: Stein as in S1. | **[DI]** | **absent** |
| S3 | `L^p` is uniformly convex (Clarkson) for `1 < p < ∞`; strict convexity gives uniqueness of the `L^3` quotient minimiser; "uniform monotonicity" of `z ↦ ‖z‖^{p-2}z` gives the `c‖w'−w‖_3^3 ≤ ∫(A'−A)·(w'−w)` step | J. A. Clarkson, "Uniformly convex spaces", *Trans. Amer. Math. Soc.* **40** (1936), 396–414 (Clarkson's inequalities; uniform convexity of `L^p`). AMS full text returned HTTP 403 on 5 Sep 2026. | **[MO]** | **absent** for `L^p` (`UniformConvexSpace` and `StrictConvexSpace` classes exist; the only instance is inner-product spaces). Clarkson's inequalities: not found. |
| S4 | Heat semigroup: `e^{tΔ}f = (4πt)^{-3/2}∫e^{-|x-y|²/4t}f(y)dy` is an `L^p → L^p` contraction, `1 ≤ p ≤ ∞`; more generally `‖e^{tΔ}f‖_q ≲ t^{3/2q-3/2p}‖f‖_p` | **Tao 2013, p. 39, eq. (18)** (verbatim in §1.4). Contraction is the `p=q` case with constant `1` via `‖Gaussian‖_{L^1}=1` and Young. | **[DI]** | **absent**: `Mathlib/Analysis/Convolution.lean` has no general Young `L^p * L^q → L^r` inequality (only `L^1*L^1`-type and bounded-times-integrable results); Gaussian heat kernel exists only in `Analysis/SpecialFunctions/Gaussian/*` for Fourier transform purposes |
| S5 | Generator domain / `D_Q ≥ 0` step: `d/ds|_{s=0} e^{sΔ}u = Δu` in `L^3` when `Δu ∈ L^3` (used in `sec:quotient` to sign `D_Q`) | Standard `C_0`-semigroup fact; no primary source located in this pass. Tao p. 39 gives the kernel only. | **[MO]/[REC]** | **absent** (no semigroup generator theory for the heat semigroup on `L^p`) |
| S6 | Bernstein: for `f` with `\hat f` supported in `{|ξ| ≤ 2N}`, `‖∇^k f‖_{L^q} ≲ N^{k+3(1/p-1/q)}‖f‖_{L^p}`, `1 ≤ p ≤ q ≤ ∞`; instance used: `‖∇S_Lu‖_∞ ≤ C2^{5L/2}‖u‖_2` | **Tao 2013, p. 40, eq. (26)** (verbatim in §1.4). Also Bahouri–Chemin–Danchin, *Fourier Analysis and Nonlinear PDE*, Grundlehren 343, Springer 2011, **Lemma 2.1** — statement not read in the book. | Tao **[DI]**; BCD **[MO]** (its content [REC]) | **absent** (no Littlewood–Paley theory, no Besov spaces) |
| S7 | Gagliardo–Nirenberg–Sobolev on `R^3`: `‖u‖_6 ≤ C‖∇u‖_2`; and the interpolations `‖u‖_3 ≤ ‖u‖_2^{1/2}‖u‖_6^{1/2}`, `‖∇u‖_3 ≤ C‖∇u‖_2^{1/2}‖Δu‖_2^{1/2}` (used in `prop:scaling`, `prop:enstrophy`) | Mathlib is itself the cleanest source for the first; classical source: Nirenberg 1959 / Gagliardo 1958. Sharp constant (Talenti 1976) is **not** used by the manuscript, which writes only `C`. | Mathlib statement **[DI]** | **partial**: `Mathlib/Analysis/FunctionalSpaces/SobolevInequality.lean`, `eLpNorm_le_eLpNorm_fderiv_of_eq` (and `…_of_le`, `…_of_eq_inner`) gives GNS for `ContDiff ℝ 1 u` with `HasCompactSupport u`, non-sharp constant `SNormLESNormFDerivOfEqConst`. Extension to `H^1(R^3)`/Schwartz needs a density argument that is **not** in Mathlib. `‖u‖_3 ≤ ‖u‖_2^{1/2}‖u‖_6^{1/2}` is Hölder/log-convexity; `LpSeminorm/CompareExp.lean` has the ingredients but not the named interpolation |
| S8 | Gronwall (used in `sec:quotient`'s low-strain bound and in `eq:quotient-gap`'s hypothetical consequence) | Mathlib | **[DI]** | **present**: `Mathlib/Analysis/ODE/Gronwall.lean`, `le_gronwallBound_of_liminf_deriv_right_le`, `norm_le_gronwallBound_of_norm_deriv_right_le`; also `Analysis/ODE/DiscreteGronwall.lean` |
| S9 | The flow `Φ_s` of a bounded Lipschitz divergence-free vector field on `R^3` is a complete volume-preserving diffeomorphism (`det ∇Φ_s ≡ 1` by Liouville's formula) — used in `sec:quotient`'s transport rewriting | Liouville's formula for `d/ds det ∇Φ_s = (div u)(Φ_s) det ∇Φ_s`. Classical; no primary source located in this pass (candidates: Hartman, *Ordinary Differential Equations*, Ch. V; Majda–Bertozzi, *Vorticity and Incompressible Flow*, Ch. 1). | **[MO]/[REC]** — must be pinned before encoding | **partial**: global existence/uniqueness for Lipschitz fields is reachable from `Analysis/ODE/PicardLindelof.lean` + `Analysis/ODE/ExistUnique.lean` + `Geometry/Manifold/IntegralCurve/*`; **volume preservation / Liouville's formula is absent** (`MeasurePreserving` exists as a definition, with no flow instance) |
| S10 | Hölder's inequality on `L^p(R^3)` | Mathlib | **[DI]** | **present**: `MeasureTheory/Function/LpSeminorm/CompareExp.lean` (`eLpNorm_smul_le_mul_eLpNorm`, `eLpNorm_le_eLpNorm_mul_eLpNorm_top`, …); `Analysis/MeanInequalities.lean` for the discrete/pointwise forms |
| S11 | Young's inequality with conjugate exponents `4/3, 4` (used in `prop:enstrophy`) | elementary | **[DI]** | **present** (`Analysis/MeanInequalities.lean` / `young_inequality`) |

**Consequence for the plan.** Of the eleven standard facts, only S8, S10, S11
are Phase-II-ready today; S7 is half-ready. S1, S2, S3, S4, S5, S6, S9 each
require a genuine new Mathlib development (Calderón–Zygmund `L^p` theory; `L^p`
uniform convexity; Young's convolution inequality for general exponents;
`C_0`-semigroup generators on `L^p`; Littlewood–Paley theory; Liouville's
formula for flows). These are textbook mathematics — they are **not** Phase I
axiom candidates in the sense of "literature theorem", but pretending they are
Phase-II-cheap would misstate the cost. The honest classification is a third
bucket: *textbook, Mathlib-absent, must be built*.

---

## 7. Classification for the formalization plan

### 7.1 Phase I axiom candidates (genuine literature theorems)

| id | Statement | Source, exact location | Status | Needed for |
|---|---|---|---|---|
| `AX-TAO-5.4` | Tao Theorem 5.4 (i)–(iv), `R^3`, `ν = 1`, with all definitions of §1.1 | APDE 6 (2013) 25–107, **pp. 52–53** | [DI] | `premise:local`, `thm:continuation`, `thm:conditional` |
| `AX-TAO-5.8` | Tao Corollary 5.8 (maximal Cauchy development, enstrophy blow-up dichotomy) plus the "incomplete mild `H^1` solution" definition | same, **pp. 56–57** | [DI] | the maximal time `T_*` used everywhere in `main.tex` |
| `AX-GKP-4` | GKP Theorem 4 (endpoint criterion in maximal-`L^3` form), with the `NS(u_0)`/`T^*` setup | arXiv:1012.0145 §"Serrin's endpoint regularity criterion" = *Math. Ann.* 355 (2013) §3.1 | [DI] | `thm:continuation` |
| `AX-ESS-1.3` | ESS Theorem 1.3 (Leray–Hopf + `L_{3,∞}(Q_T)` ⟹ `L^5(Q_T)`, smooth and unique on `Q_T`), with Definitions (1.3)–(1.7) and the `‖·‖_{s,l,Q_T}` convention | Russian Math. Surveys 58:2 (2003), **pp. 213–214** | [DI] | optional cross-check / alternative to `AX-GKP-4`; the manuscript's `\cite{ESS2003}` |
| `AX-ESS-classical` | "If `]0,T_*[` is the maximal interval on which a smooth solution of (1.1),(1.2) exists and `T_* < +∞`, then `lim sup_{t↑T_*}∫|v|³ = +∞`" | same, **p. 214**, running prose (unnumbered) | [DI] | the classical-solution form CP1 asked for |
| `AX-KATO-2` | Kato Theorem 2 (`m = 3`): small `‖a‖_3` ⟹ global | Math. Z. 187 (1984), **p. 472** | [DI] | only the manuscript's small-data *remark*; **not** load-bearing |

Recommendation: Phase I should import `AX-TAO-5.4`, `AX-TAO-5.8` and
`AX-GKP-4`, and record `AX-ESS-1.3`/`AX-ESS-classical` as the provenance of
`AX-GKP-4` rather than as a separate dependency, since `main.tex`'s
`thm:continuation` proof runs through the maximal-`L^3` form only.
`AX-KATO-2` should not be an axiom; delete or demote the Kato citation to a
non-load-bearing remark in the comparator.

### 7.2 Not axioms

* Fefferman (A): a **target statement to encode**, in `Challenge.lean`, with
  `ν` universally quantified and (4),(6),(7) written out.
* `eq:nu-normalization`: manuscript-owned. Verified correct in this audit: with
  `v(x,s) = ν^{-1}u(x,s/ν)`, `q(x,s) = ν^{-2}p(x,s/ν)` one gets
  `∂_s v + (v·∇)v + ∇q = ν^{-2}(∂_tu + (u·∇)u + ∇p) = ν^{-2}·νΔu = Δv`,
  `S_* = νT_*`, `‖v(s)‖_3 = ν^{-1}‖u(s/ν)‖_3`. ✓
* Tao's Remark 5.9 and Kato's Remark 1.1(a): remarks citing other work, not
  theorems.
* FLRT `C_tL^3` uniqueness: text not inspected; not needed; do not axiomatise.
* The eleven standard facts of §6: textbook material, Phase II, with the
  Mathlib-absence caveat above.

### 7.3 Normalisation and sign cross-check (all four principal sources vs `eq:NS`)

`main.tex` `eq:NS`: `∂_t u + (u·∇)u + ∇p = νΔu`, `∇·u = 0`.

| Source | Its equation | ν | Agrees with `eq:NS` after `ν → 1`? |
|---|---|---|---|
| Tao (3) | `∂_t u + (u·∇)u = Δu − ∇p + f` | 1 | ✓ (with `f = 0`) |
| GKP (NS) | `∂_t u = Δu − ∇·(u⊗u) − ∇π` | 1 | ✓ (`∇·(u⊗u) = (u·∇)u` for `∇·u = 0`) |
| ESS (1.1) | `∂_t v + div(v⊗v) − Δv = −∇p` | 1 | ✓ |
| Kato (NS) | `∂_t u − Δu + (u·∂)u + ∂p = f` | 1 | ✓ (with `f = 0`) |
| Fefferman (1) | `∂_t u_i + Σ_j u_j∂_j u_i = νΔu_i − ∂_i p + f_i` | ν | ✓ (with `f = 0`) |

Pressure normalisation. `main.tex` uses `p = R_iR_j(u_iu_j)`; Tao's normalised
pressure (published (9), `f = 0`) is `p = −Δ^{-1}∂_i∂_j(u_iu_j)`. Since
`R_iR_j = ∂_i∂_j(−Δ)^{-1} = −Δ^{-1}∂_i∂_j`, these are **identical**, and both
agree with `−Δp = ∂_i∂_j(u_iu_j)` used in `thm:conditional`. ✓ No sign error.

---

## 8. Audit findings that touch the manuscript

1. **`premise:local` under-cites.** "a unique maximal classical solution on
   `[0,T_*)` … by the directly stated local theorem of Tao [Theorem 5.4]".
   Theorem 5.4 gives smallness-conditional local existence, uniqueness, and
   Schwartz regularity; the maximal development is **Corollary 5.8** (pp. 56–57).
   Repair: cite Theorem 5.4 *and* Corollary 5.8, and state that the passage from
   Corollary 5.8's per-`T` dichotomy to a single maximal `T_*(u_0)` is a
   manuscript-owned gluing step. Severity: **major** for Phase I (the axiom set
   is otherwise incomplete), **minor** for the paper.
2. **`thm:continuation` proof phrase "uniqueness in the mild class identifies it
   with the maximal `L^3` solution"** is currently asserted without a stated
   uniqueness theorem covering both classes at once. Tao 5.4(iii) is uniqueness
   among `H^1` mild solutions; GKP's `NS(u_0)` is the strong solution in the
   `E_{p,q}`/`C_tL^3` class. The identification of the two branches is a real
   step. Options: (a) cite the `C_tL^3` uniqueness literature (FLRT — then its
   text must be inspected), or (b) prove the identification from Tao 5.4(iii)
   after showing the `L^3` branch is `H^1` on compacts of `(0,T_*)` for Schwartz
   data. Severity: **major** for Phase I; the manuscript should name which.
3. **`L_{3,∞}` remark is fully vindicated** by the primary text (ESS p. 213
   norm definition; GKP's own sentence). No repair needed. Recommend citing
   ESS p. 213 explicitly rather than asserting it.
4. **Littlewood–Paley convention is unpinned.** `main.tex` says "Fix a smooth
   homogeneous Littlewood–Paley partition" and then uses `‖K_J‖_∞ ≤ C2^{3J}`
   (`prop:lowpressure`) and `M = C2^{5L/2}‖u_0‖_2` (`sec:quotient`). Both
   constants depend on the bump `φ`. For Lean the convention must be fixed once;
   Tao's (p. 40) is a directly-inspected candidate but is **inhomogeneous**
   (`P_{≤N}` with `φ = 1` near the origin), whereas `main.tex` says
   *homogeneous*. These differ at low frequency and the difference is not
   harmless for `S_J p` when `p` is only in `L^2 ∩ L^3`. Severity: **major** for
   Phase I; flag to the pressure lane.
5. **Two typos in the imported source that must not be transcribed**: Tao's
   `X^s := L^∞_tH^s_x ∩ L^2_x H^{s+1}_x` (published (13), p. 37 — must be
   `L^2_t`), and the missing right-hand side of the `X^k` bound in Theorem
   5.4(ii). Both are present in the arXiv source as well, so they are the
   author's, not the typesetter's.
6. **HF16's outstanding `T(1)`/Calderón–Zygmund source obligation is not
   discharged by this pass.** `hf16-transport-commutator.md` records "verify a
   primary source for the exact `T(1)` and Calderón–Zygmund consequences". Tao
   p. 38 supplies only the Leray projection's `L^p` boundedness, which is
   strictly weaker than the `T(1)`-type statement HF16 uses. That obligation
   stands.

---

## Frontier record

**MODE / RESULT:** SOURCE AUDIT. Every literature statement CP1 imports was
located in a primary text and transcribed with its own definitions, quantifiers,
domain, viscosity normalisation, and solution class. Five of the six principal
sources were directly inspected (Tao APDE PDF and arXiv source; GKP arXiv
source; ESS Russian Math. Surveys pp. 211–220; Kato Math. Z. scan pp. 471–474;
Fefferman Clay PDF). The manuscript's `L_{3,∞}` remark and its
`eq:nu-normalization` were independently verified; the four sources' sign and
pressure-normalisation conventions were checked to agree with `eq:NS`.

**FIRST GAP:** the manuscript's `premise:local` cites Tao Theorem 5.4 for a
"unique maximal classical solution on `[0,T_*)`". Theorem 5.4 does not state
maximality; Corollary 5.8 (APDE 6 (2013), pp. 56–57) does, and a gluing step is
still manuscript-owned. Phase I's axiom set is incomplete until Corollary 5.8 is
added. The second, independent gap is `thm:continuation`'s identification of the
Tao `H^1` mild branch with GKP's maximal `L^3` branch, which currently rests on
an unnamed uniqueness theorem.

**SURVIVING CONDITIONAL SUFFIX:** with `AX-TAO-5.4`, `AX-TAO-5.8` and
`AX-GKP-4` as stated here, plus the two manuscript-owned steps just named,
`thm:continuation` and `thm:conditional` are exactly the statements CP1 claims,
under `hyp:critical`. Nothing in this note bears on `hyp:highpressure`,
`hyp:absorption`, `eq:quotient-gap`, HIGH-PRESSURE, HIGH-STRAIN, or NS-R3.

**NON-CLAIMS:** no regularity, no bound, no Millennium result is asserted. The
Furioli–Lemarié-Rieusset–Terraneo uniqueness theorem, Clarkson's inequalities,
Bahouri–Chemin–Danchin Lemma 2.1, Stein's Riesz-transform theorem numbers, the
`L^p` heat-semigroup generator statement, and Liouville's formula for flows were
**not** read in their primary sources and are marked [MO]/[REC]; none may be
encoded in Lean on the strength of this note.
