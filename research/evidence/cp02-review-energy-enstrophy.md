# CP02 audit: energy, scaling, enstrophy (review of `cp02-energy-enstrophy.md`, round 1)

MODE: REVIEW (proof-audit discipline). Date: 2026-09-05. Lane owns this file only;
nothing else was edited and nothing was pushed.

## 0. Frozen candidate

| item | value |
|---|---|
| candidate file | `../navier/research/evidence/cp02-energy-enstrophy.md` |
| sha256 | `1859df86aec9589737e832388b6f19379ef2b6b94a7b4eac9bd35f13b56d3729` |
| `git -C ../navier rev-parse HEAD` | `715ce84ec78d64c510e150360a354b5d55648b9c` |
| manuscript reviewed against | `../navier-paper/main.tex`, HEAD `1ad73c2` (matches the candidate's recorded HEAD) |
| navier-formal HEAD | `9c8b37d` |
| Mathlib checkout | `../stafford38/.lake/packages/mathlib`, `git rev-parse --short HEAD` = `0df444a360` |
| author's summary | untrusted; used only to locate claims |

Reviewed scope: the whole fenced LaTeX block of §2 of the candidate, i.e. the
replacement for `main.tex` from `\section{Energy and scaling}` to the paragraph
after `prop:ode` — `lem:R-consequences`, `lem:div-zero`, `lem:plancherel`,
`def:sobolev-constant`, `lem:density`, `lem:sobolev`, `lem:interp`, `lem:GN`,
`prop:energy`, `prop:scaling`, `rem:scaling-pressure`, `rem:mismatch`,
`prop:enstrophy`, `prop:ode`, `rem:lean`, `rem:usage` — together with the
candidate's external-fact table F1–F8 and its obligation claims E-1, S-1, S-2,
N-1. Out of scope: `prop:pressure`, `prop:lowpressure`, the two pressure
hypotheses, `thm:continuation`, `thm:conditional`, `sec:quotient`,
`prop:localtheory` (assumed as package R per D2).

---

## 1. Verdict

**VERDICT: REPAIR.**

The mathematics of the lane is sound. Every identity, integration by parts,
limit, exponent and constant in the reviewed scope was reconstructed
independently and stands; I could not refute any analytic step (§4). The first
bad bridge is in the *import* layer, which decision D5 makes load-bearing: the
Conventions subsection attributes to `\cite[p.~14--15]{Tao2013}` three facts
that the cited text does not contain, two of which (Parseval on `L^2` and the
derivative rule `\widehat{\partial^\alpha u}=(2\pi i\xi)^\alpha\hat u`) carry
the entire analytic core of the section; the page numbers also belong to the
arXiv preprint rather than to the bibliography entry `Tao2013`; and the
candidate's fact F4 asserts `[DI]` for two Mathlib declaration names that do not
exist in the checkout it names. A complete replacement is supplied in §3; with
it, the whole reviewed scope passes.

---

## 2. First bad bridge

**FIRST BAD BRIDGE.** In the Conventions subsection of the LaTeX block, the
implication

> Tao 2013, pp. 14–15 ⟹ (a) `u ∈ H^k(R^3)` iff `u ∈ L^2` and every
> distributional derivative `∂^α u`, `|α| ≤ k`, lies in `L^2`;
> (b) `\widehat{∂^α u}(ξ) = (2πiξ)^α \hat u(ξ)`, hence
> `\widehat{∂_j u} = 2πiξ_j \hat u` and `\widehat{Δu} = −4π²|ξ|²\hat u`;
> (c) Parseval's identity `∫ f g dx = ∫ \hat f \overline{\hat g} dξ` for
> real-valued `f, g ∈ L^2`.

**EVIDENCE (direct inspection of the primary text).** I downloaded
`https://arxiv.org/pdf/1108.1165v4` (95 pages, pdfTeX 1.40.12) and read pp. 14–15
in full through `helpy_pdf` (`mode:"text"`, `pages:"14-15"`). Those two pages
contain, verbatim:

* the Euclidean tensor conventions `|u|² = u_i u_i`, `|∇u|² = (∂_i u_j)(∂_i u_j)`,
  `|∇²u|² = (∂_i∂_j u_k)(∂_i∂_j u_k)` (p. 14);
* `\hat f(ξ) := ∫_{R^3} e^{−2πix·ξ} f(x) dx` for `f ∈ L^1_x(R^3)`, "we then
  extend this Fourier transform to tempered distributions in the usual manner"
  (p. 14);
* the **classical** Sobolev norm `‖u‖_{H^k_x(Ω)} := (Σ_{j=0}^{k} ‖∇^j u‖²_{L^2_x(Ω)})^{1/2}`
  **defined only for smooth `u`**, with the explicit remark "to avoid technical
  issues we will not attempt to define these norms for non-smooth functions `u`"
  (pp. 14–15);
* the Fourier norm `‖u‖_{H^s_x(R^3)} := (∫(1+|ξ|²)^s |\hat u(ξ)|² dξ)^{1/2}` for
  tempered distributions, and "this conflicts slightly with the previous notation
  when `k` is a non-negative integer, but the two norms are **equivalent up to
  constants**" (p. 15).

Tao states **no** derivative rule for the Fourier transform, **no** Plancherel
or Parseval identity, and **no** characterisation of `H^k` by distributional
derivatives for non-smooth `u`. So (a), (b), (c) are unsupported by the cited
location. Two further confirmations:

* **Wrong pagination.** `references.bib` (inspected) has
  `@article{Tao2013, ... journal = {Analysis \& PDE}, volume = {6}, number = {1},
  year = {2013}, pages = {25--107}}`. The published article therefore has no
  pages 14 and 15; the material above is on **pp. 37–38** of the APDE version,
  exactly as the candidate's own fact table F1 records ("arXiv:1108.1165v4,
  pp. 14–15 … = APDE 6 (2013) pp. 37–38"). The LaTeX block ships the arXiv
  pagination against the published bibliography entry.
* **F4's `[DI]` claim is false as written.** F4 cites
  `Mathlib/Analysis/Fourier/FourierTransformDeriv.lean`,
  `Real.fourierIntegral_fderiv` and `Real.fourierIntegral_iteratedFDeriv`, `[DI]`.
  In the named checkout `0df444a360` those identifiers do not exist. The file has
  `namespace Real` on lines 97–152 and 670–836 and `namespace VectorFourier` on
  lines 156–668; the two theorems in question are at **lines 256 and 532**, i.e.
  inside `VectorFourier`, so their names are
  `VectorFourier.fourierIntegral_fderiv` and
  `VectorFourier.fourierIntegral_iteratedFDeriv` (the file's own module docstring,
  line 62, spells the first one that way). The `Real` namespace in that file
  contains `Real.fourier_fderiv` and `Real.fourier_iteratedFDeriv` instead. Two
  other local Mathlib trees (`/var/tmp/aa-clean-2fdc928`,
  `/var/tmp/stafford-algebraic-analysis-publication`) agree.

**Why this is load-bearing rather than cosmetic.** Fact (c) is used in
`lem:plancherel` (i), (ii), (iii) and in `lem:density` Step 2; fact (b) is used in
all three parts of `lem:plancherel` and in the `\hat\rho_\varepsilon(\xi)
= \hat\rho(\varepsilon\xi)` computation; fact (a) is used implicitly wherever
"`u(t) ∈ H^2`" is turned into "`Δu(t) ∈ L^2` and `|ξ|²\hat u ∈ L^2`". Through
`lem:plancherel` they carry `prop:energy` Step 2, `prop:enstrophy` Step 1,
`lem:GN`, and hence `eq:L4L3` and `eq:enstrophy`. Under D5 the section as
delivered therefore rests on an import that is misattributed in the manuscript
and, in one row, misstated in the evidence table.

---

## 3. Replacement argument (complete)

Two edits. Nothing downstream changes except the citation keys named below.

### 3.1 Replace the Conventions subsection

Delete the sentences beginning "Equivalently, `u ∈ L^2` and every distributional
derivative …" through "… `∫ f g dx = ∫ \hat f \overline{\hat g} dξ`" and the two
`\cite[p.~14]{Tao2013}` / `\cite[p.~15]{Tao2013}` calls, and use:

```latex
\subsection*{Conventions}

Throughout, $\hat f(\xi)=\int_{\R^3}e^{-2\pi i x\cdot\xi}f(x)\,dx$ for
$f\in L^1(\R^3)$, extended to tempered distributions in the usual way;
this is the convention of \cite[p.~37]{Tao2013}.  Tensor norms are Euclidean:
$|u|^2=\sum_ku_k^2$, $|\nabla u|^2=\sum_{j,k}(\partial_ju_k)^2$ and
$|\nabla^2u|^2=\sum_{i,j,k}(\partial_i\partial_ju_k)^2$, also as in
\cite[p.~37]{Tao2013}.  For $s\in\R$ we set
$\|u\|_{H^s}=\bigl(\int_{\R^3}(1+|\xi|^2)^s|\hat u(\xi)|^2\,d\xi\bigr)^{1/2}$
for tempered distributions $u$ on $\R^3$, and let $H^s(\R^3)$ be the space of
those with $\|u\|_{H^s}<\infty$ \cite[p.~38]{Tao2013}.  We write
$\|\cdot\|_q$ for $\|\cdot\|_{L^q(\R^3)}$.  A vector field lies in $H^s$ when
each component does, and then $\|u\|_{H^s}^2=\sum_l\|u_l\|_{H^s}^2$; likewise
for $L^q$, with $\|u\|_q=\|\,|u|\,\|_q$ for the Euclidean pointwise norm.
When $u$ is smooth, its distributional derivatives are its classical ones.

We fix once and for all $\chi\in C_c^\infty(\R^3)$ with $0\leq\chi\leq1$,
$\chi=1$ on $\{|x|\leq1\}$, $\chi=0$ on $\{|x|\geq2\}$, and set
$\chi_R(x)=\chi(x/R)$ for $R>0$, so that
$\|\nabla\chi_R\|_\infty=R^{-1}\|\nabla\chi\|_\infty$ and $\chi_R\to1$
pointwise as $R\to\infty$.

Exactly two facts about the Fourier transform are imported; every other
Fourier statement in this section is deduced from them.

\begin{lemma}[Imported Fourier facts]\label{lem:fourier}
\begin{enumerate}
\item[(P)] \emph{Plancherel--Parseval.}  The map $f\mapsto\hat f$, defined by
the integral above on $L^1\cap L^2(\R^3)$, extends to a unitary operator of
$L^2(\R^3;\C)$ onto itself.  Hence $\|\hat f\|_2=\|f\|_2$ and
$\int_{\R^3}f\bar g\,dx=\int_{\R^3}\hat f\,\overline{\hat g}\,d\xi$ for
$f,g\in L^2$; for real-valued $f,g\in L^2$ this reads
$\int_{\R^3}fg\,dx=\int_{\R^3}\hat f\,\overline{\hat g}\,d\xi$.  Moreover a
tempered distribution $u$ with $\hat u\in L^2(\R^3)$ lies in $L^2(\R^3)$, with
$\|u\|_2=\|\hat u\|_2$.
\item[(D)] \emph{Derivative rule.}  For every tempered distribution $u$ on
$\R^3$ and every multi-index $\alpha$ one has
$\widehat{\partial^\alpha u}=(2\pi i\xi)^\alpha\hat u$ as tempered
distributions.  In particular $\widehat{\partial_ju}=2\pi i\xi_j\hat u$ and
$\widehat{\Delta u}=-4\pi^2|\xi|^2\hat u$.
\end{enumerate}
Source for (P): Stein and Weiss \cite[Ch.~I, Theorems 2.1 and 2.3, and \S3]{SteinWeiss1971};
the $L^2$ statements are formalised in Mathlib as
\texttt{MeasureTheory.Lp.fourierTransform}$_{\text{l}i}$,
\texttt{MeasureTheory.Lp.norm\_fourier\_eq} and
\texttt{MeasureTheory.Lp.inner\_fourier\_eq} \cite{MathlibFourier}.
Source for (D): Stein and Weiss \cite[Ch.~I, Theorem 1.8 and \S3]{SteinWeiss1971};
the integrable-function case is formalised as
\texttt{VectorFourier.fourierIntegral\_fderiv} and
\texttt{VectorFourier.fourierIntegral\_iteratedFDeriv} \cite{MathlibFourier}.
\end{lemma}

\begin{lemma}[Sobolev spaces by derivatives]\label{lem:hk}
Let $k\geq0$ be an integer and let $u$ be a tempered distribution on $\R^3$.
Then $u\in H^k(\R^3)$ if and only if $u\in L^2(\R^3)$ and
$\partial^\alpha u\in L^2(\R^3)$ for every multi-index $\alpha$ with
$|\alpha|\leq k$.  In that case
$\|\partial^\alpha u\|_2=\|(2\pi\xi)^\alpha\hat u\|_2$ for all such $\alpha$;
in particular, if $u\in H^2(\R^3)$ then $|\xi|^2\hat u\in L^2$, and if
$p\in H^1(\R^3)$ then $|\xi|\hat p\in L^2$.
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:fourier}(D) the tempered distribution $\partial^\alpha u$ has
Fourier transform $(2\pi i\xi)^\alpha\hat u$, and by
Lemma~\ref{lem:fourier}(P) a tempered distribution lies in $L^2$ exactly when
its Fourier transform does, with equal norms; this gives the norm identity as
soon as either side is finite.

Suppose $u\in H^k$, i.e. $(1+|\xi|^2)^{k/2}\hat u\in L^2$.  For
$|\alpha|\leq k$ and every $\xi$,
$|(2\pi\xi)^\alpha|\leq(2\pi)^{|\alpha|}|\xi|^{|\alpha|}
\leq(2\pi)^{k}(1+|\xi|^2)^{k/2}$, so $(2\pi i\xi)^\alpha\hat u\in L^2$ and
hence $\partial^\alpha u\in L^2$; the case $\alpha=0$ gives $u\in L^2$.

Conversely, suppose $u\in L^2$ and $\partial^\alpha u\in L^2$ for all
$|\alpha|\leq k$.  Then $\xi^\alpha\hat u\in L^2$ for all $|\alpha|\leq k$.
Expanding $(1+|\xi|^2)^k=(1+\xi_1^2+\xi_2^2+\xi_3^2)^k$ by the multinomial
theorem produces finitely many terms $c_\beta\,\xi_1^{2\beta_1}\xi_2^{2\beta_2}
\xi_3^{2\beta_3}$ with $c_\beta$ a positive integer and $|\beta|\leq k$, so
\[
 \int_{\R^3}(1+|\xi|^2)^k|\hat u|^2\,d\xi
 =\sum_{|\beta|\leq k}c_\beta\int_{\R^3}|\xi^\beta\hat u|^2\,d\xi<\infty,
\]
i.e. $u\in H^k$.  The last two assertions are the cases $|\alpha|=2$ and
$|\alpha|=1$ combined with
$|\xi|^2=\bigl(\sum_i\xi_i^2\bigr)$ and
$\bigl\||\xi|^2\hat u\bigr\|_2\leq\sum_i\|\xi_i^2\hat u\|_2$,
$\bigl\||\xi|\hat p\bigr\|_2\leq\sum_i\|\xi_i\hat p\|_2$.
\end{proof}
```

### 3.2 Point the users at the two lemmas

Three one-phrase edits inside the existing proofs; no argument changes.

* `lem:plancherel`, proof, parts (i)–(iii): replace each bare "Parseval's
  identity" by "Parseval's identity (Lemma~\ref{lem:fourier}(P))", each use of
  `\widehat{\partial_j u}=2\pi i\xi_j\hat u` and
  `\widehat{\Delta u}=-4\pi^2|\xi|^2\hat u` by a reference to
  Lemma~\ref{lem:fourier}(D), and each use of "`|\xi|^2\hat u_k\in L^2` (as
  `u\in H^2`)" / "`|\xi|\hat p\in L^2`" by a reference to Lemma~\ref{lem:hk}.
* `lem:plancherel`, proof of (ii): "By Plancherel's theorem" becomes "By
  Lemma~\ref{lem:fourier}(P) and (D)".
* `lem:density`, Step 2: "By Plancherel's theorem on $L^1\cap L^2$" becomes "By
  Lemma~\ref{lem:fourier}(P)".

### 3.3 Bibliography and fact-table corrections

Add to `references.bib`, alongside the candidate's `Nirenberg1959` and
`MathlibSobolev`:

```bibtex
@book{SteinWeiss1971,
  author    = {Elias M. Stein and Guido Weiss},
  title     = {Introduction to Fourier Analysis on Euclidean Spaces},
  series    = {Princeton Mathematical Series},
  number    = {32},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {1971}
}

@misc{MathlibFourier,
  author       = {{The Mathlib Community}},
  title        = {Mathlib, files \texttt{Mathlib/Analysis/Fourier/LpSpace.lean}
                  (\texttt{MeasureTheory.Lp.fourierTransform}$_{\text{l}i}$,
                  \texttt{norm\_fourier\_eq}, \texttt{inner\_fourier\_eq}) and
                  \texttt{Mathlib/Analysis/Fourier/FourierTransformDeriv.lean}
                  (\texttt{VectorFourier.fourierIntegral\_fderiv},
                  \texttt{VectorFourier.fourierIntegral\_iteratedFDeriv})},
  howpublished = {Lean 4 library, commit \texttt{0df444a}},
  year         = {2026}
}
```

And in the candidate's fact table:

* **F1** must be narrowed to what Tao actually states (Fourier convention on
  `L^1` extended to `S'`; Euclidean tensor norms; classical `H^k` norm for
  *smooth* `u`; Fourier `H^s` norm; equivalence of the two *up to constants*),
  with location **APDE 6 (2013), pp. 37–38** (arXiv:1108.1165v4 pp. 14–15) —
  `[DI]`, re-verified in this audit.
* **F3** keeps its content but the Mathlib names are in namespace
  `MeasureTheory.Lp` (`Analysis/Fourier/LpSpace.lean`, lines 50, 89, 93) —
  `[DI]`; Stein–Weiss `[MO]`.
* **F4** must be restated as Lemma `lem:fourier`(D) with the corrected names
  `VectorFourier.fourierIntegral_fderiv` (line 256) and
  `VectorFourier.fourierIntegral_iteratedFDeriv` (line 532) — `[DI]` for the
  integrable-function case; Stein–Weiss `[MO]` for the `S'` case. The `H^k`
  characterisation moves out of the import table entirely: it is now
  Lemma `lem:hk`, proved in the manuscript.

---

## 4. Reconstruction of the rest, and refutation attempts

Everything below was rederived from scratch and agrees with the candidate.

**`lem:R-consequences`.** (a) The `H^1`-convergence of the difference quotients
is `u ∈ C^1([0,T];H^1)`, inside package R; the a.e. identification with the
classical `∂_t u` via an a.e.-convergent subsequence is correct and is used in
(b). (b) `‖(u·∇)u‖_2 ≤ ‖u‖_∞‖∇u‖_2` with the pointwise Cauchy–Schwarz bound
`|(u·∇)u|² ≤ |u|²|∇u|²` (summing the componentwise bound over `k`); `u ∈ L^∞`
is granted by D2. (c) `∂_i(u_j|u|²)=(∂_iu_j)|u|²+2u_j(u·∂_iu)`, so
`|∂_i g| ≤ 3|u|²|∇u|` and `‖∂_i g‖_1 ≤ 3‖u‖_4²‖∇u‖_2`; `u ∈ L^3 ∩ L^4` from D2.
All legitimate uses of R; no preserved Schwartz decay is used anywhere.

**`lem:div-zero`.** Correct, and it is the right device: it removes the need for
spatial decay, which is exactly the E-1 complaint about "radial cutoff". I tried
to refute it by weakening the hypotheses (one dimension, `g ∈ C^1`, `g, g' ∈ L^1`):
`g' ∈ L^1` forces the limits `g(±∞)` to exist and `g ∈ L^1` forces them to be
`0`, so `∫g' = 0` necessarily. No refutation.

**`lem:plancherel`.** (i) `∫∂_ju_k∂_jv_k = 4π²∫ξ_j²\hat u_k\overline{\hat v_k}`;
summing over `j` and using `\widehat{Δu_k} = −4π²|ξ|²\hat u_k` gives
`∫∇u:∇v = −∫Δu·v`. (ii) `Σ_{i,j}(2π)^4ξ_i²ξ_j² = (2π)^4|ξ|^4` and
`‖Δu_k‖_2² = (4π²)²∫|ξ|^4|\hat u_k|²`, so `‖∇²u‖_2 = ‖Δu‖_2`. This is a
whole-space fact and would fail on a domain; the hypothesis `Ω = R^3` is used.
(iii) The conjugation sign is right: `2πiξ_i\overline{\hat u_i}
= −\overline{2πiξ_i\hat u_i}`, so the two minus signs give
`+4π²∫|ξ|²\hat p\,\overline{\widehat{\operatorname{div}u}} = 0`. Integrability of
the (iii) integrand is `(|ξ|\hat p)(|ξ|²\hat u_i) ∈ L^1` by Cauchy–Schwarz — the
hypotheses `p ∈ H^1`, `u ∈ H^2` are exactly what is needed, not more.

**`def:sobolev-constant` and the Nirenberg import.** Verified `[DI]` from the
numdam PDF (`ASNSP_1959_3_13_2_115_0.pdf`, PDF page 12 = printed p. 125), read
through `helpy_pdf`. The theorem is there, with both exceptional cases, and the
candidate's quotations are faithful, including "We shall not give a complete
proof of the theorem here but shall indicate the main steps" (p. 125) and "The
proof of the theorem is elementary and contains in particular an elementary
proof for the Sobolev case `a = 1`" (p. 126). The instance is admissible:
exception 1 needs `q = ∞` (here `q = 2`), and exception 2 needs
`m − j − n/r` a nonnegative integer (here `1 − 0 − 3/2 = −1/2`). The exponent
arithmetic `1/p = j/n + a(1/r − m/n) + (1−a)/q = 1/2 − 1/3 = 1/6` is right.
Verified `[DI]` from the local Mathlib checkout `0df444a360`:
`eLpNorm_le_eLpNorm_fderiv_of_eq` at `SobolevInequality.lean:600`, with exactly
the hypotheses and conclusion the candidate quotes, and the ambient assumptions
`[FiniteDimensional ℝ E] (μ : Measure E) [IsAddHaarMeasure μ]` at line 353 —
satisfied by Lebesgue measure on `EuclideanSpace ℝ (Fin 3)`, where the operator
norm of `fderiv ℝ u` is the Euclidean `|∇u|`. So `eq:sobolev-cc` is genuinely
available.

**`lem:density`.** Truncation and mollification are both written out correctly,
including `∂_j(χ_R u) = χ_R ∂_j u + u ∂_j χ_R` from the definition of the weak
derivative, `\hat ρ_ε(ξ) = \hat ρ(εξ)`, and the dominated-convergence step with
majorant `4|\hat w|²`. `v` compactly supported and in `L^2` gives `v ∈ L^1`, and
`\operatorname{supp} ∂_j v ⊆ \operatorname{supp} v`. Sound.

**`lem:sobolev`.** Fatou plus `‖∇u_n‖_2 → ‖∇f‖_2` gives the scalar case; the
vector case constant `√m C_S` is correct via `|f| ≤ Σ_k|f_k|`, Minkowski and
Cauchy–Schwarz in `R^m`. No refutation.

**`lem:interp`, `lem:GN`.** Hölder with `4/3, 4` gives
`‖f‖_3³ ≤ ‖f‖_2^{3/2}‖f‖_6^{3/2}`, hence `‖f‖_3 ≤ ‖f‖_2^{1/2}‖f‖_6^{1/2}`.
With `m = 9`, `‖∇u‖_6 ≤ 3C_S‖∇²u‖_2 = 3C_S‖Δu‖_2`, so
`‖∇u‖_3 ≤ (3C_S)^{1/2}‖∇u‖_2^{1/2}‖Δu‖_2^{1/2}`. Correct.

**`prop:energy`.** The difference-quotient identity
`E(τ+h) − E(τ) = ½⟨h^{-1}(u(τ+h) − u(τ)), u(τ+h)+u(τ)⟩` and the continuity of
the `L^2` inner product give `E' = ∫u·u_t` with no cutoff; Steps 2–4 are the
three lemmas; Step 5 is the FTC with `∇u ∈ C([0,T];L^2)`. The two consequences
follow, and `∫_0^{T_*}‖∇u‖_2² ≤ ‖u_0‖_2²/(2ν)` by monotone exhaustion. E-1 is
fully discharged, including the replacement of "strong-solution Sobolev bounds".

**`prop:scaling`.** (i) All five chain-rule factors are `λ^3` and
`\operatorname{div}u_λ = λ^2(\operatorname{div}u)(λx,λ^2t)`; correct. (ii) The
`q < ∞` change of variables gives `λ^{q−3}`, i.e. `λ^{1−3/q}`; the `q = ∞`
argument via `{|u_λ(·,t)| > λM} = λ^{-1}{|u(·,λ^2t)| > M}` and the fact that
`x ↦ λx` preserves null sets in both directions is correct. (iii)
`‖u‖_3^4 ≤ 3C_S²‖u‖_2²‖∇u‖_2²` since `((√3 C_S)^{1/2})^4 = 3C_S²`; the final
constant `3C_S²‖u_0‖_2^4/(2ν)` is right.

**`rem:scaling-pressure`.** `\widehat{f_λ}(ξ) = λ^{-3}\hat f(ξ/λ)`;
`m_{ij}(ξ) = −ξ_iξ_j/|ξ|²` is the symbol of `R_iR_j` and is homogeneous of
degree `0`; and `−Δ^{-1}∂_i∂_j` has the same symbol, so this is consistent with
D1. `(u_λ)_i(u_λ)_j = λ²(u_iu_j)_λ` gives `p_λ`. The disclaimer that this is not
a uniqueness statement is appropriate and correctly placed.

**`rem:mismatch`.** (a) `∫_0^T t^{-4/5} dt = 5T^{1/5}` and
`{g > M} ∩ (0,T) = (0,\min\{T, M^{-5}\})` are both right. (b)
`∫_0^{T/λ²}‖u_λ‖_q^r dt = λ^{r(1−3/q)−2}∫_0^T‖u‖_q^r ds`, so the norm scales by
`λ^{1−3/q−2/r}`; invariance iff `2/r + 3/q = 1`; for `(r,q) = (4,3)`,
`2/4 + 3/3 = 3/2 > 1` and the exponent is `1 − 1 − 1/2 = −1/2`. S-2 is
discharged: the meta-sentence is out of the statement of `prop:scaling` and the
witness is proved.

**`prop:enstrophy`.** `∂_j` commutes with the `L^2`-limit of difference
quotients, so `Y ∈ C^1` with `Y' = 2∫∇u:∇u_t`; `lem:plancherel`(i) with
`v = u_t ∈ H^1` and `lem:plancherel`(iii) give `eq:enstrophy-identity`. Hölder
`1/6 + 1/3 + 1/2 = 1`, then `√3 C_S · (3C_S)^{1/2} = 3C_S^{3/2}`, then Young
`(4/3, 4)` applied to `(δa)(b/δ)` with `a = ‖Δu‖_2^{3/2}`,
`b = 3C_S^{3/2}Y^{3/4}`, `δ^{4/3} = 2ν/3`: `¾δ^{4/3} = ν/2`,
`δ^{-4} = 27/(8ν³)`, `b^4 = 81C_S^6Y^3`, so the remainder is
`(1/4)(27/8)(81) C_S^6 ν^{-3} Y^3 = (2187/32)C_S^6ν^{-3}Y^3`. I attempted to
refute the constant by minimising the difference: for `ν = C_S = Y = 1`,
`f(s) = ½s² − 3s^{3/2} + 2187/32` has `f'(s) = s − 4.5s^{1/2} = 0` at `s = 20.25`
and `f(20.25) = 0` to rounding, so `C_E = 2187/32` is the exact optimum of the
chosen Young split, not merely a sufficient value. N-1 is discharged.

**`prop:ode`, `rem:lean`.** `y = (2C(T−t))^{-1/2}` gives `y' = Cy³` and
`∫_0^T y = √(2T/C)`. All six Lean names in `rem:lean` exist at
`navier-formal` HEAD `9c8b37d`: `Ode.lean:34,109,134`,
`InterpolationMismatch.lean:114,136`, `Scaling.lean:48,84,125`; and
`scalingWitness t = t ^ (−1/5)` (`InterpolationMismatch.lean:32`) is the
manuscript's witness. `eLpNorm_dilate`'s hypotheses `p ≠ 0`, `p ≠ ∞` match the
manuscript's "for `0 < q < ∞`".

**Self-containment and compilation.** I spliced the block into a copy of
`main.tex` (replacing `\section{Energy and scaling}` … up to
`\section{A signed critical balance}`), added only
`\newtheorem{lemma}[theorem]{Lemma}`, `\newtheorem{definition}[theorem]{Definition}`,
a stub `\begin{proposition}\label{prop:localtheory}` and
`\label{sec:continuation}`, and removed the bibliography. `pdflatex` exits `0`,
13 pages, **no** undefined internal references and no "Missing"/"Undefined
control sequence" errors; the only warnings are the six undefined `\cite` keys
caused by dropping the bibliography. So the two `\newtheorem` lines and the two
labels are exactly what the integrator must supply, and the block contains no
reference to any evidence file as proof.

**Hidden circularity.** None. `prop:energy` uses no Sobolev inequality;
`lem:sobolev` uses no PDE; `prop:localtheory` is used only as the assumed
package R, and nothing in the reviewed scope is used in the proof of R.
`hyp:critical`, `hyp:absorption`, `hyp:highpressure` are referenced only inside
`rem:mismatch` and `rem:usage` as *not* being supplied.

---

## 5. Conditional suffix that survives

With Lemma `lem:fourier` in place as a labelled import (§3.1), **the entire
reviewed scope survives unconditionally given package R (D2)**:

* `lem:R-consequences`, `lem:div-zero`, `lem:plancherel`, `lem:hk`,
  `def:sobolev-constant`, `lem:density`, `lem:sobolev`, `lem:interp`, `lem:GN`;
* `prop:energy` with `eq:energy` and both consequences;
* `prop:scaling` (i)–(iii) with `eq:scaling-norm`, `eq:L4L3` and the explicit
  constant `3C_S²‖u_0‖_2^4/(2ν)`; `rem:scaling-pressure`; `rem:mismatch`;
* `prop:enstrophy` with `eq:enstrophy-identity`, `eq:enstrophy` and
  `C_E = (2187/32)C_S^6`; `prop:ode`; `rem:lean`; `rem:usage`.

Obligations E-1, S-1, S-2 and N-1 are then discharged as claimed. Nothing in the
scope is conditional on HIGH-PRESSURE, HIGH-STRAIN, ABSORPTION or CRITICAL, and
nothing in the scope would survive the failure of R — every proof consumes R.

---

## 6. Unnecessary dependencies

* **`prop:scaling`(ii) at `q = ∞`** is never used downstream (only `q = 2, 3`
  and the `L^r_tL^q_x` computation at `q = 3`). It can be dropped or reduced to
  `1 ≤ q < ∞` without affecting anything; the candidate's own Lean
  cross-reference `eLpNorm_dilate` also covers only `0 < q < ∞`.
* **`rem:scaling-pressure`** feeds nothing; it is retained only for D1
  consistency. Keep it as a remark, but it is not a dependency of any result.
* **The Nirenberg citation** is mathematically unnecessary: the Mathlib
  statement alone establishes `eq:sobolev-cc` and is `[DI]`. Nirenberg is a
  printed-source courtesy, and the candidate is right to record that its proof
  there is "the main steps" only.
* **`lem:hk`'s full "iff"** is more than the section needs; only the forward
  direction (`u ∈ H^k ⟹ ∂^α u ∈ L^2` with the Fourier weights) is used. The
  converse costs two lines and makes the conventions self-contained; keep.
* **`lem:R-consequences`(a)'s a.e. identification with the classical `∂_t u`** is
  used only inside (b); it is not otherwise needed. Keep, it is the cheapest
  bridge from the pointwise equation to the `H^k` curve derivative.
* No Calderón–Zygmund theory, Riesz `L^p` bound, heat semigroup,
  Littlewood–Paley theory, `L^p` uniform convexity or uniqueness theorem is used
  anywhere in the scope. Confirmed by reading the block; the candidate's
  statement to that effect is accurate.

---

## 7. Non-claims (retained verbatim from the candidate, verified)

* No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL or NS-R3 result is asserted or
  approached anywhere in the reviewed scope.
* No bound on `sup_{t<T_*}‖u(t)‖_3` is deduced.
* The value of `C_S` is not asserted; only its existence is used.
* `(u_λ, p_λ)` is not asserted to be the classical branch of the rescaled datum.
* Preserved Schwartz decay in time is not used.
* This audit certifies no mathematical correctness beyond the reviewed scope and
  does not certify package R, which belongs to the local-theory lane.

---

## 8. Reopening condition

The blacklisted implication is exactly "Tao 2013 pp. 14–15 supplies Parseval, the
Fourier derivative rule, and the distributional `H^k` characterisation". It is
reopened only by one of:

1. a primary source, opened and read, that states Plancherel/Parseval on `L^2`
   and `\widehat{∂^α u} = (2πi\xi)^α\hat u` on `S'(R^3)` in the D1 convention —
   at which point `lem:fourier` becomes `[DI]` and §3.1 is final; or
2. a written manuscript proof of both facts from a lower-level import; or
3. a Mathlib development of the `S'` derivative rule under a name that is
   checked to exist in the pinned checkout, which would upgrade
   `lem:fourier`(D) beyond the integrable-function case.

Until then `lem:fourier` must ship with `[MO]` on the Stein–Weiss half, stated as
such, which is admissible under D5 because the label is explicit.

---

## 9. Minor editorial issues for the integrator

1. `\cite[p.~14]{Tao2013}` and `\cite[p.~15]{Tao2013}` → `p.~37`, `p.~38`.
   `Tao2013` in `references.bib` is APDE 6 (2013) no. 1, 25–107; pages 14–15 are
   arXiv v4 pagination.
2. Conventions: `\|u\|_{H^k}^2=\sum_k\|u_k\|_{H^k}^2` reuses `k` for both the
   Sobolev order and the component index. Use `\sum_l\|u_l\|_{H^k}^2`.
3. `prop:scaling`(ii): "every measurable `u(\cdot,\lambda^2t)`" is
   ungrammatical. Say "with both sides allowed to be `+\infty`".
4. `prop:scaling`(i): the hypothesis is "smooth and solves `\eqref{eq:NS}`", but
   `eq:NS` carries `u(0) = u_0` with `u_0` Schwartz. State the datum hypothesis
   in the proposition instead of relying on the ambient convention of §1.
5. `rem:mismatch`(b): the parenthesis "(machine-checked arithmetic:
   `NavierFormal.L4L3_supercritical`)" is attached to a sentence that also
   contains the exponent `−1/2`. The Lean theorem
   (`InterpolationMismatch.lean:136`) proves only `2/4 + 3/3 = 3/2` and
   `1 < 3/2`. Narrow the attribution or extend the Lean statement.
6. `rem:mismatch`(a): "no scalar inequality can pass from the left side of
   `\eqref{eq:L4L3}` to `\sup_{t<T}\|u(t)\|_3`" is still a meta-sentence. It is
   admissible in a remark, but the sharp form is "`g \mapsto \|g\|_{L^4(0,T)}`
   does not dominate `\|g\|_{L^\infty(0,T)}`", which is what the witness proves.
7. Unreferenced labels: `def:sobolev-constant`, `rem:lean`,
   `rem:scaling-pressure`, `eq:energy-derivative`, `eq:L4L3-constant`,
   `eq:LPS`. Harmless; keep for downstream lanes or drop.
8. Fact table F3: qualify the Mathlib names as `MeasureTheory.Lp.norm_fourier_eq`
   and `MeasureTheory.Lp.inner_fourier_eq` (namespace `MeasureTheory.Lp`,
   `Analysis/Fourier/LpSpace.lean:50, 89, 93`).
9. Fact table F4: names corrected in §3.3; as shipped they do not exist in the
   named checkout, so the `[DI]` label is unsupported.
10. Fact table F6 is labelled "`[DI]` (grep-level)". Per the legend of
    `cp01-literature-statements.md` §0, `[DI]` means the statement was read in
    the primary text; grep-level location is not that. Relabel, or read the
    statements (I did not re-verify F6's six Mathlib names in this audit).
11. Nirenberg defines `|D^j u|_p` as the maximum of the `|\cdot|_p` norms of the
    `j`-th order derivatives (p. 125, verified). His `a = 1`, `m = 1`, `j = 0`
    instance therefore reads `\|u\|_6 \le C\max_j\|\partial_j u\|_2
    \le C\|\,|\nabla u|\,\|_2`. Add that one-line reconciliation in
    `def:sobolev-constant`, or note that the Mathlib form is already in the
    Euclidean gradient norm and carries the inequality as stated.
12. Integrator items the candidate already flagged and that I confirm are
    necessary and sufficient: `\newtheorem{lemma}[theorem]{Lemma}`,
    `\newtheorem{definition}[theorem]{Definition}`, `\label{sec:continuation}`
    on the section containing `thm:continuation` (or reference
    `Theorem~\ref{thm:continuation}` instead), and the `Nirenberg1959` /
    `MathlibSobolev` bib entries — plus `SteinWeiss1971` and `MathlibFourier`
    from §3.3.
13. `research/verify.py` is unaffected: all thirteen `paper_label` values in
    `docs/proof-graph.yaml` (`def:target`, `hyp:absorption`, `hyp:critical`,
    `hyp:highpressure`, `premise:local`, `prop:energy`, `prop:enstrophy`,
    `prop:lowpressure`, `prop:ode`, `prop:pressure`, `prop:scaling`,
    `thm:conditional`, `thm:continuation`) survive the splice.
14. `docs/proof-graph.yaml` and `docs/proof.md` quote the `eq:L4L3` and
    `eq:enstrophy` constants only as "`C`", so the newly explicit `3C_S^2` and
    `C_E = (2187/32)C_S^6` force no change there, as the candidate says. Worth a
    one-line note in the graph's `mechanism` field for `prop:enstrophy` all the
    same.

---

## 10. Source checks performed in this audit

| source | route | result |
|---|---|---|
| Tao, arXiv:1108.1165v4, pp. 14–15 | PDF downloaded, read via `helpy_pdf` `mode:"text"` | `[DI]`; F1 content confirmed, F1 over-attribution and page-number defect found |
| Nirenberg 1959, printed p. 125 (PDF p. 12) | numdam PDF, read via `helpy_pdf` `mode:"text"` | `[DI]`; theorem, both exceptional cases and both "main steps" quotations confirmed; the `n=3, j=0, m=1, r=q=2, a=1` instance is admissible |
| Mathlib `SobolevInequality.lean` | local checkout `0df444a360`, lines 353, 587, 600–604 | `[DI]`; F2(b) confirmed verbatim, including the Haar-measure and finite-dimensionality assumptions |
| Mathlib `Analysis/Fourier/LpSpace.lean` | local checkout, lines 50, 89, 93 | `[DI]`; F3's Mathlib side confirmed, namespace `MeasureTheory.Lp` |
| Mathlib `Analysis/Fourier/FourierTransformDeriv.lean` | local checkout, namespace map + lines 62, 256, 532 | F4 **refuted as stated**; correct names are in `VectorFourier` |
| `navier-formal` HEAD `9c8b37d` | `Ode.lean`, `InterpolationMismatch.lean`, `Scaling.lean` | all six `rem:lean` names exist; `scalingWitness = t^{-1/5}` confirmed |
| `navier-paper/references.bib`, HEAD `1ad73c2` | read | `Tao2013` = APDE 25–107, confirming the pagination defect |
| compile check | spliced `main.tex` + block + 2 `\newtheorem` + 2 stub labels, `pdflatex` twice | exit `0`, 13 pages, zero undefined internal references |
