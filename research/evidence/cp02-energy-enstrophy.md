# CP02-5: energy, scaling, enstrophy (obligations E-1, S-1, S-2, N-1) — repair round 2

MODE: PROOF WRITING, REPAIR ROUND (wave CP02, lane 5). Date: 2026-09-05.
Owner file: this one. Nothing else was edited; nothing was pushed.

Inputs read in full: `../navier-paper/main.tex` (HEAD `1ad73c2`),
`references.bib`, `cp01-manuscript-obligations.md`,
`cp01-literature-statements.md`, and the round-1 audit
`cp02-review-energy-enstrophy.md` (verdict REPAIR, first bad bridge: the
Conventions subsection attributed Parseval, the Fourier derivative rule and
the distributional $H^k$ characterisation to `\cite[pp.~14--15]{Tao2013}`,
which contains none of them, with arXiv pagination cited against the
published bibliography entry; aggravation: fact F4 named two Mathlib
declarations that do not exist). Controller decisions D1–D5 are binding and
are followed below. The regularity package R of D2 is assumed and cited as
`Proposition~\ref{prop:localtheory}`; nothing about preserved Schwartz decay
in time is used.

## 0. What changed in this round

The first bad bridge is repaired by rebuilding the import layer, not by
re-pointing a citation:

1. **Import layer.** A labelled lemma `lem:fourier` now imports exactly two
   facts, both **[DI]** in a printed primary source read in this round
   (Grafakos, *Classical Fourier Analysis*, 3rd ed., GTM 249, 2014, PDF opened
   and pp. 105–131 read through `helpy_pdf`):
   (S) the Schwartz-level calculus — derivative rules, Parseval, Plancherel,
   inversion — Grafakos Prop. 2.2.11 (9)–(11) pp. 109–110 and Thm 2.2.14
   (2)–(4) p. 112, **with full proofs printed there**; and (L) the $L^2$
   theory — the isometric extension $\mathcal F$ of $f\mapsto\hat f$ from
   $L^1\cap L^2$ to a bijective isometry of $L^2$, agreeing with $\hat f$ a.e.
   on $L^1\cap L^2$ — Grafakos §2.2.4 pp. 113–114 (the $L^1\cap L^2$ isometry
   is Exercise 2.2.8 there, with a complete hint; recorded as a caveat), with
   Mathlib's fully checked $L^2$ theory as second source.
2. **Everything else about the Fourier transform is now proved in the
   manuscript** from (S), (L) and the definitions: the $\mathcal S'$
   derivative rule and inversion (`lem:duality`, two-line duality proofs, the
   proofs Grafakos omits for Prop. 2.3.22); polarised Parseval on $L^2$
   (`lem:parseval`); mollification in $L^2$ (`lem:mollify`); compatibility of
   the $L^2$ and $\mathcal S'$ transforms and the fundamental lemma for
   $L^2_{\rm loc}$ functions (`lem:compat`); the characterisation of $H^k$ by
   $L^2$ derivatives with the exact norm identities (`lem:hk`); and the
   identification of classical with distributional derivatives for smooth
   $H^k$ functions (`lem:classical`), which replaces the previously
   unproved sentence "when $u$ is smooth, its distributional derivatives are
   its classical ones".
3. **Tao pagination corrected against the published PDF** (read in this
   round: `scratchpad/tao/apde-full.pdf`, printed pp. 35–36): the Fourier
   convention and the Euclidean tensor norms are on **APDE p. 35**, the
   classical $H^k$ norm for smooth $u$ and the Fourier $H^s$ norm on
   **APDE p. 36**. Both the round-1 fact table ("pp. 37–38") and the
   audit's suggested `p.~37`/`p.~38` were wrong; the block now cites
   `\cite[p.~35]{Tao2013}` and `\cite[p.~36]{Tao2013}`.
4. **Mathlib names corrected and upgraded.** The non-existent
   `Real.fourierIntegral_fderiv`/`Real.fourierIntegral_iteratedFDeriv` are
   gone. The $\mathcal S'$ derivative rule is now cross-referenced to
   `TemperedDistribution.fourier_lineDerivOp_eq`
   (`Mathlib/Analysis/Distribution/TemperedDistribution.lean:568`), the
   $L^2$/$\mathcal S'$ compatibility to
   `MeasureTheory.Lp.fourier_toTemperedDistribution_eq`
   (`Analysis/Fourier/LpSpace.lean:120`), the $L^2$ theory to
   `MeasureTheory.Lp.fourierTransformₗᵢ`, `…norm_fourier_eq`,
   `…inner_fourier_eq` (lines 50, 89, 93), the $H^0=L^2$ characterisation to
   `TemperedDistribution.memSobolev_zero_iff_exists_fourier`
   (`Analysis/Distribution/Sobolev.lean:233`), and the fundamental lemma to
   `ae_eq_of_integral_contDiff_smul_eq`
   (`Analysis/Distribution/AEEqOfIntegralContDiff.lean:195`); all read in
   checkout `0df444a360`. Mathlib's convention
   `𝓕 f w = ∫ exp(−2πi⟪v,w⟫) f v` (`Analysis/Fourier/FourierTransform.lean:439`)
   and its distributional derivative `∂_{m} f g = f (−∂_{m} g)`
   (`TemperedDistribution.lean:367`) agree with D1 and with Grafakos
   Def. 2.3.6.
5. **All fourteen minor items of the audit (§9) addressed**: pagination (1);
   component index $l$ (2); grammar in `prop:scaling`(ii) (3); datum
   hypothesis stated inside `prop:scaling`(i) (4); Lean attribution in
   `rem:mismatch`(b) narrowed to what `L4L3_supercritical` proves (5); sharp
   form of `rem:mismatch`(a) (6); the label `sec:continuation` is no longer
   referenced — `rem:usage` now cites existing labels only (7, 12); F3/F4
   names (8, 9); F6 relabelled honestly — every Mathlib name in the table
   was read at its line in this round, so **[DI]** is now earned (10);
   Nirenberg's max-norm convention reconciled in `def:sobolev-constant` (11);
   `verify.py`/graph items need no action (13, 14).
6. No mathematical statement of round 1 was weakened. The only added
   hypothesis anywhere is explicit and harmless: `prop:scaling`(i) now says
   what datum it refers to. Result labels required by the structural verifier
   are unchanged.

New theorem environments used: `lemma` and `definition`. The integrator must
add to the preamble of `main.tex`

```latex
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
```

## 1. Obligations discharged

| id | obligation (from cp01-manuscript-obligations.md) | where discharged |
|---|---|---|
| E-1 | `prop:energy`: replace "strong-solution Sobolev bounds justify" by the exact memberships; prove $\tfrac{d}{dt}\tfrac12\|u\|_2^2=\int u\cdot u_t$ from $u\in C^1([0,T];L^2)$; prove $\int u\cdot\Delta u=-\|\nabla u\|_2^2$ for $u\in H^2$ (Plancherel route chosen); prove $\int u\cdot(u\cdot\nabla)u=0$ via $u_j\lvert u\rvert^2\in W^{1,1}$, $\operatorname{div}u=0$ and the $\int\partial_jg=0$ lemma; prove $\int u\cdot\nabla p=0$ from $p\in H^1$; time integration | `lem:R-consequences`, `lem:div-zero`, `lem:classical`, `lem:plancherel`, proof of `prop:energy` |
| S-1 | Sobolev inequality $\|u\|_6\le C_S\|\nabla u\|_2$ for $u\in H^1(\mathbb R^3)$ stated with a source (external fact F2) and the density extension from $C^1_c$ written out | `def:sobolev-constant`, `lem:mollify`, `lem:density`, `lem:sobolev` |
| S-2 | Move the meta-sentence out of the statement of `prop:scaling`; explicit scalar witness $g(t)=t^{-1/5}\in L^4(0,T)\setminus L^\infty(0,T)$ proved on paper; supercriticality arithmetic | `rem:mismatch` |
| N-1 | `prop:enstrophy`: identity $\tfrac12Y'+\nu\|\Delta u\|_2^2=\int(u\cdot\nabla)u\cdot\Delta u$ with every integration by parts justified from R; Gagliardo–Nirenberg step from Hölder, Sobolev on each $\partial_ju$, and $\|\nabla^2u\|_2=\|\Delta u\|_2$ (Plancherel identity written); Hölder with $1/6+1/3+1/2$; Young with $4/3,4$; explicit constant path | `lem:plancherel`, `lem:interp`, `lem:GN`, proof of `prop:enstrophy` |
| — | Import layer at D5 standard: every Fourier fact used is either imported [DI] with exact location (`lem:fourier`) or proved (`lem:parseval`, `lem:duality`, `lem:mollify`, `lem:compat`, `lem:hk`, `lem:classical`) | Conventions and the first eight lemmas of the block |
| — | `prop:scaling`: PDE invariance by chain rule for both equations with $p_\lambda=\lambda^2p$; norm identity for every $1\le q\le\infty$ including $q=\infty$; interpolation by Hölder; `eq:L4L3` with an explicit constant | proof of `prop:scaling`, `lem:interp`, `rem:scaling-pressure` |
| — | `prop:ode` unchanged; Lean cross-reference added | `rem:lean` |
| — | Mark which results are used in the conditional chain | `rem:usage` |

## 2. Replacement text for sections 2 and 3 of `main.tex`

The block below replaces everything from `\section{Energy and scaling}` to the
end of `\section{The enstrophy estimate}` (i.e. through the paragraph after
`prop:ode`). Labels `prop:energy`, `eq:energy`, `prop:scaling`, `eq:L4L3`,
`prop:enstrophy`, `eq:enstrophy`, `prop:ode` are retained. New labels:
`lem:fourier`, `lem:parseval`, `lem:duality`, `lem:mollify`, `lem:compat`,
`lem:hk`, `eq:h1-norm`, `lem:div-zero`, `lem:classical`,
`lem:R-consequences`, `lem:plancherel`, `def:sobolev-constant`,
`eq:sobolev-cc`, `lem:density`, `lem:sobolev`, `lem:interp`, `lem:GN`,
`eq:energy-derivative`, `eq:scaling-norm`, `eq:L4L3-constant`,
`rem:scaling-pressure`, `rem:mismatch`, `eq:LPS`, `eq:enstrophy-identity`,
`rem:lean`, `rem:usage`. Bibliography keys used that are not yet in
`references.bib`: `Grafakos2014`, `Nirenberg1959`, `MathlibSobolev`,
`MathlibFourier` (entries in the integrator notes after the block).

```latex
\section{Energy and scaling}

\subsection*{Conventions}

Throughout, $\R^3$ carries Lebesgue measure and $\|\cdot\|_q$ denotes
$\|\cdot\|_{L^q(\R^3)}$; functions are complex-valued unless they are said
to be real.  Tensor norms are Euclidean: $|u|^2=\sum_ku_k^2$,
$|\nabla u|^2=\sum_{j,k}(\partial_ju_k)^2$ and
$|\nabla^2u|^2=\sum_{i,j,k}(\partial_i\partial_ju_k)^2$, as in
\cite[p.~35]{Tao2013}.  For $f\in L^1(\R^3)$ the Fourier transform is
\[
 \hat f(\xi)=\int_{\R^3}e^{-2\pi ix\cdot\xi}f(x)\,dx ,
\]
the convention of \cite[p.~35]{Tao2013} and of
\cite[Definition~2.2.8, p.~108]{Grafakos2014}.

$\mathcal S=\mathcal S(\R^3)$ is the Schwartz space
\cite[Definition~2.2.1, p.~105]{Grafakos2014}, and $\mathcal S'$ the space
of continuous linear functionals on it (tempered distributions)
\cite[Definition~2.3.3, p.~121]{Grafakos2014}; we write
$\langle u,\varphi\rangle$ for the pairing.  A measurable function $f$ for
which $f\varphi\in L^1$ for every $\varphi\in\mathcal S$ and
$\varphi\mapsto\int f\varphi\,dx$ is continuous on $\mathcal S$ defines
$u_f\in\mathcal S'$ by $\langle u_f,\varphi\rangle=\int_{\R^3}f\varphi\,dx$.
Two cases are used.  If $f\in L^2$, then
$|\int f\varphi|\le\|f\|_2\|\varphi\|_2\le
\|f\|_2\,\|(1+|x|^2)^{-1}\|_2\sup_x(1+|x|^2)|\varphi(x)|$, and the last
supremum is a finite sum of Schwartz seminorms.  If $f=hg$ with $g\in L^2$
and $h\in C^\infty(\R^3)$ \emph{slowly increasing}, meaning
$|\partial^\beta h(x)|\le C_\beta(1+|x|)^{N_\beta}$ for all $\beta$, then
$h\varphi\in\mathcal S$ and $|\int hg\varphi|\le\|g\|_2\|h\varphi\|_2$,
which is again controlled by Schwartz seminorms of $\varphi$.  We say that
$u\in\mathcal S'$ \emph{is in $L^2$}, and write $u\in L^2$, if $u=u_f$ for
some $f\in L^2$; by Lemma~\ref{lem:compat}(ii) below such $f$ is unique up
to a null set, and we then identify $u$ with $f$ and write $\|u\|_2=\|f\|_2$.

For $u\in\mathcal S'$, $\varphi\in\mathcal S$, a multi-index $\alpha$ and a
slowly increasing $h$ we use the definitions
\cite[Definitions~2.3.6, 2.3.7, 2.3.15, pp.~123 and~125]{Grafakos2014}
\[
 \langle\partial^\alpha u,\varphi\rangle=(-1)^{|\alpha|}\langle u,\partial^\alpha\varphi\rangle,\quad
 \langle hu,\varphi\rangle=\langle u,h\varphi\rangle,\quad
 \langle\hat u,\varphi\rangle=\langle u,\hat\varphi\rangle,\quad
 \langle u^\vee,\varphi\rangle=\langle u,\varphi^\vee\rangle,
\]
where $\varphi^\vee(x):=\hat\varphi(-x)$; these are meaningful because
$\partial^\alpha\varphi$, $h\varphi$, $\hat\varphi$, $\varphi^\vee$ lie in
$\mathcal S$ \cite[Remark~2.2.3, p.~105; Proposition~2.2.11(11), p.~110;
p.~125]{Grafakos2014}.  For $s\in\R$ the Sobolev space $H^s(\R^3)$ of
\cite[p.~36]{Tao2013} is the set of $u\in\mathcal S'$ with
$(1+|\xi|^2)^{s/2}\hat u\in L^2$ (the product being that of the slowly
increasing function $(1+|\xi|^2)^{s/2}$ with $\hat u$), normed by
$\|u\|_{H^s}=\|(1+|\xi|^2)^{s/2}\hat u\|_2$; Tao's phrase ``extend this
Fourier transform to tempered distributions in the usual manner''
\cite[p.~35]{Tao2013} is taken to mean the definition of $\hat u$ displayed
above.  A vector field lies in $H^s$ (or $L^q$) when each component does,
with $\|u\|_{H^s}^2=\sum_l\|u_l\|_{H^s}^2$ and $\|u\|_q=\|\,|u|\,\|_q$.

We fix once and for all $\chi\in C_c^\infty(\R^3)$ with $0\le\chi\le1$,
$\chi=1$ on $\{|x|\le1\}$, $\chi=0$ on $\{|x|\ge2\}$, and set
$\chi_R(x)=\chi(x/R)$ for $R>0$, so that
$\|\nabla\chi_R\|_\infty=R^{-1}\|\nabla\chi\|_\infty$ and $\chi_R\to1$
pointwise as $R\to\infty$; and $\rho\in C_c^\infty(\R^3)$ with $\rho\ge0$,
$\int\rho=1$, with $\rho_\varepsilon(x)=\varepsilon^{-3}\rho(x/\varepsilon)$
for $\varepsilon>0$.

Exactly two facts about the Fourier transform are imported.  Every other
Fourier statement in this paper is deduced from them and from the
definitions above.

\begin{lemma}[Imported Fourier facts]\label{lem:fourier}
\begin{enumerate}
\item[(S)] \emph{Schwartz calculus.}  For $f,h\in\mathcal S(\R^3)$ and every
multi-index $\alpha$: $\hat f\in\mathcal S$;
$\widehat{\partial^\alpha f}(\xi)=(2\pi i\xi)^\alpha\hat f(\xi)$;
$\partial^\alpha\hat f=\bigl((-2\pi ix)^\alpha f\bigr)^{\wedge}$;
$\int f\,\bar h\,dx=\int\hat f\,\overline{\hat h}\,d\xi$;
$\|\hat f\|_2=\|f\|_2$; and $(\hat f)^\vee=f=(f^\vee)^\wedge$.
\item[(L)] \emph{$L^2$ theory.}  For $f\in L^1\cap L^2(\R^3)$ one has
$\hat f\in L^2$ and $\|\hat f\|_2=\|f\|_2$.  The map $f\mapsto\hat f$ on
$L^1\cap L^2$ has a unique continuous extension
$\mathcal F\colon L^2(\R^3;\mathbb C)\to L^2(\R^3;\mathbb C)$; $\mathcal F$ is linear,
bijective and isometric, $\mathcal Ff=\hat f$ almost everywhere for
$f\in L^1\cap L^2$, and $\mathcal F^{-1}$ is the analogous continuous
extension of $f\mapsto f^\vee$, $f^\vee(x)=\hat f(-x)$, from $L^1\cap L^2$;
in particular $\|\mathcal F^{-1}g\|_2=\|g\|_2$ for $g\in L^2$.
\end{enumerate}
\end{lemma}

Source for (S): \cite[Proposition~2.2.11 (9), (10), (11), pp.~109--110,
and Theorem~2.2.14 (2), (3), (4), p.~112]{Grafakos2014}, where complete
proofs are printed.  Source for (L): \cite[\S2.2.4, pp.~113--114]{Grafakos2014};
there the isometry on $L^1\cap L^2$ is Exercise~2.2.8, and the extension,
its isometry, its agreement with $\hat f$ a.e.\ on $L^1\cap L^2$, its
bijectivity and the description of $\mathcal F^{-1}$ are stated in the text.
The $L^2$ theory is also formalised in Mathlib as
\texttt{MeasureTheory.Lp.fourierTransform}$_{\ell\mathrm i}$,
\texttt{MeasureTheory.Lp.norm\_fourier\_eq} and
\texttt{MeasureTheory.Lp.inner\_fourier\_eq} \cite{MathlibFourier}, with the
same convention $\mathcal Ff(w)=\int e^{-2\pi i\langle v,w\rangle}f(v)\,dv$.

\begin{lemma}[Parseval on $L^2$]\label{lem:parseval}
For $f,g\in L^2(\R^3;\mathbb C)$,
$\int_{\R^3}f\bar g\,dx=\int_{\R^3}\mathcal Ff\,\overline{\mathcal Fg}\,d\xi$.
For real-valued $f,g\in L^2$ this reads
$\int fg\,dx=\int\mathcal Ff\,\overline{\mathcal Fg}\,d\xi$.
\end{lemma}

\begin{proof}
Expanding the squares,
$\|f+g\|_2^2-\|f-g\|_2^2=4\operatorname{Re}\int f\bar g$ and
$\|f+ig\|_2^2-\|f-ig\|_2^2=4\operatorname{Im}\int f\bar g$, so
$4\int f\bar g=\|f+g\|_2^2-\|f-g\|_2^2+i\|f+ig\|_2^2-i\|f-ig\|_2^2$.
Apply this identity to $\mathcal Ff,\mathcal Fg$ as well; by linearity and
isometry of $\mathcal F$ (Lemma~\ref{lem:fourier}(L)) the four norms on the
right agree, hence so do the left sides.
\end{proof}

\begin{lemma}[Duality rules in $\mathcal S'$]\label{lem:duality}
Let $u\in\mathcal S'(\R^3)$.
\begin{enumerate}
\item[(a)] $(\hat u)^\vee=u$.
\item[(b)] $\widehat{\partial^\alpha u}=(2\pi i\xi)^\alpha\hat u$ for every
multi-index $\alpha$; in particular
$\widehat{\partial_ju}=2\pi i\xi_j\hat u$ and
$\widehat{\Delta u}=-4\pi^2|\xi|^2\hat u$.
\item[(c)] If $g\in L^2$ and $h,h_1,h_2$ are slowly increasing, then
$h\,u_g=u_{hg}$ and $h_1(h_2u)=(h_1h_2)u$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $\varphi\in\mathcal S$.  (a) By definition and
Lemma~\ref{lem:fourier}(S),
$\langle(\hat u)^\vee,\varphi\rangle=\langle\hat u,\varphi^\vee\rangle
=\langle u,(\varphi^\vee)^\wedge\rangle=\langle u,\varphi\rangle$.

(b) Using the definitions of $\widehat{\ }$ and $\partial^\alpha$ on
$\mathcal S'$, then Lemma~\ref{lem:fourier}(S) for
$\partial^\alpha\hat\varphi$, then the definition of multiplication by the
slowly increasing polynomial $(2\pi i\xi)^\alpha$,
\[
 \langle\widehat{\partial^\alpha u},\varphi\rangle
 =(-1)^{|\alpha|}\langle u,\partial^\alpha\hat\varphi\rangle
 =(-1)^{|\alpha|}\bigl\langle u,\bigl((-2\pi ix)^\alpha\varphi\bigr)^\wedge\bigr\rangle
 =\bigl\langle\hat u,(2\pi ix)^\alpha\varphi\bigr\rangle
 =\langle(2\pi i\xi)^\alpha\hat u,\varphi\rangle .
\]
The two special cases are $\alpha=e_j$ and
$\sum_j(2\pi i\xi_j)^2=-4\pi^2|\xi|^2$.

(c) $\langle hu_g,\varphi\rangle=\int g\,h\varphi\,dx=\int(hg)\varphi\,dx
=\langle u_{hg},\varphi\rangle$, and
$\langle h_1(h_2u),\varphi\rangle=\langle u,h_2h_1\varphi\rangle
=\langle(h_1h_2)u,\varphi\rangle$.
\end{proof}

\begin{lemma}[Mollification in $L^2$]\label{lem:mollify}
Let $w\in L^1\cap L^2(\R^3)$ and $\varepsilon>0$.  Then
$\rho_\varepsilon*w(x):=\int\rho_\varepsilon(x-y)w(y)\,dy$ is defined for
every $x$, belongs to $C^\infty(\R^3)$ with
$\partial^\alpha(\rho_\varepsilon*w)=(\partial^\alpha\rho_\varepsilon)*w$,
satisfies $\|\rho_\varepsilon*w\|_1\le\|w\|_1$ and
$\|\rho_\varepsilon*w\|_2\le\|w\|_2$, and
$\|\rho_\varepsilon*w-w\|_2\to0$ as $\varepsilon\to0$.  If $w$ vanishes
outside a compact set $K$, then $\rho_\varepsilon*w$ vanishes outside
$K+\{|x|\le\varepsilon\}$, so $\rho_\varepsilon*w\in C_c^\infty(\R^3)$.
\end{lemma}

\begin{proof}
The integral converges absolutely since $\rho_\varepsilon$ is bounded and
$w\in L^1$.  For the derivative in direction $e_j$, the difference quotients
$h^{-1}(\rho_\varepsilon(x+he_j-y)-\rho_\varepsilon(x-y))$ converge to
$\partial_j\rho_\varepsilon(x-y)$ and are bounded by
$\|\nabla\rho_\varepsilon\|_\infty$ (mean value theorem), so dominated
convergence with majorant $\|\nabla\rho_\varepsilon\|_\infty|w|\in L^1$
gives $\partial_j(\rho_\varepsilon*w)=(\partial_j\rho_\varepsilon)*w$;
iterating gives all $\alpha$, and continuity of each
$(\partial^\alpha\rho_\varepsilon)*w$ follows in the same way.  The support
statement is immediate from the formula.  By Tonelli,
$\int\!\!\int\rho_\varepsilon(x-y)|w(y)|\,dy\,dx=\|w\|_1$, so
$\|\rho_\varepsilon*w\|_1\le\|w\|_1$.  By the Cauchy--Schwarz inequality
applied to $\rho_\varepsilon^{1/2}\cdot\rho_\varepsilon^{1/2}|w|$ and then
Tonelli,
\[
 |\rho_\varepsilon*w(x)|^2\le\Bigl(\int\rho_\varepsilon(x-y)\,dy\Bigr)
 \int\rho_\varepsilon(x-y)|w(y)|^2\,dy,\qquad
 \|\rho_\varepsilon*w\|_2^2\le\int\!\!\int\rho_\varepsilon(x-y)\,dx\,|w(y)|^2\,dy
 =\|w\|_2^2 .
\]
Since $\rho_\varepsilon*w\in L^1$, Fubini's theorem (justified by the
absolute convergence $\int\!\!\int|\rho_\varepsilon(x-y)||w(y)|\,dy\,dx<\infty$)
gives
\[
 \widehat{\rho_\varepsilon*w}(\xi)
 =\int w(y)e^{-2\pi iy\cdot\xi}\int\rho_\varepsilon(x-y)e^{-2\pi i(x-y)\cdot\xi}\,dx\,dy
 =\hat\rho_\varepsilon(\xi)\hat w(\xi),
\]
and the substitution $x=\varepsilon z$ gives
$\hat\rho_\varepsilon(\xi)=\hat\rho(\varepsilon\xi)$.  Here $|\hat\rho|\le\|\rho\|_1=1$,
$\hat\rho(0)=1$, and $\hat\rho$ is continuous by dominated convergence
(majorant $\rho$).  Because $\rho_\varepsilon*w-w\in L^1\cap L^2$,
Lemma~\ref{lem:fourier}(L) gives
\[
 \|\rho_\varepsilon*w-w\|_2^2=\|\widehat{\rho_\varepsilon*w}-\hat w\|_2^2
 =\int|\hat\rho(\varepsilon\xi)-1|^2|\hat w(\xi)|^2\,d\xi\xrightarrow[\varepsilon\to0]{}0
\]
by dominated convergence: the integrand tends to $0$ pointwise and is
bounded by $4|\hat w|^2\in L^1$.
\end{proof}

\begin{lemma}[$L^2$ functions as tempered distributions]\label{lem:compat}
\begin{enumerate}
\item[(i)] For $f\in L^2(\R^3)$: $\widehat{u_f}=u_{\mathcal Ff}$ and
$(u_f)^\vee=u_{\mathcal F^{-1}f}$.
\item[(ii)] If $g$ is measurable with $\int_{|x|\le R}|g|^2\,dx<\infty$ for
every $R$ and $\int g\varphi\,dx=0$ for all $\varphi\in C_c^\infty(\R^3)$,
then $g=0$ almost everywhere.  Consequently $u_f=u_g$ with $f,g\in L^2$
implies $f=g$ a.e.
\item[(iii)] If $u\in\mathcal S'$ and $\hat u=u_g$ for some $g\in L^2$, then
$u=u_{\mathcal F^{-1}g}$; thus $u\in L^2$ and $\|u\|_2=\|g\|_2$.
\end{enumerate}
\end{lemma}

\begin{proof}
(i) Put $f_N=f\,\mathbf 1_{\{|x|\le N\}}$.  Then $f_N\in L^1$ (Cauchy--Schwarz
on the ball) and $f_N\to f$ in $L^2$ by dominated convergence (majorant
$|f|^2$).  For $\varphi\in\mathcal S$, Fubini's theorem (both
$f_N,\varphi\in L^1$) gives
$\int f_N\hat\varphi\,dx=\int\!\!\int f_N(x)\varphi(\xi)e^{-2\pi ix\cdot\xi}\,d\xi\,dx
=\int\hat f_N\varphi\,d\xi$.  As $N\to\infty$ the left side tends to
$\int f\hat\varphi$ (since $\hat\varphi\in L^2$) and, because
$\hat f_N=\mathcal Ff_N\to\mathcal Ff$ in $L^2$ by
Lemma~\ref{lem:fourier}(L), the right side tends to $\int\mathcal Ff\,\varphi$.
Hence $\langle\widehat{u_f},\varphi\rangle=\int f\hat\varphi=\int\mathcal Ff\,\varphi
=\langle u_{\mathcal Ff},\varphi\rangle$.  The same computation with
$\varphi^\vee(x)=\hat\varphi(-x)=\int\varphi(\xi)e^{2\pi ix\cdot\xi}\,d\xi$
gives $\int f_N\varphi^\vee=\int f_N^\vee\varphi$, and
$f_N^\vee=\mathcal F^{-1}f_N\to\mathcal F^{-1}f$ in $L^2$, whence
$(u_f)^\vee=u_{\mathcal F^{-1}f}$.

(ii) Fix $R>0$ and put $w=\chi_Rg$; $w$ vanishes outside $\{|x|\le2R\}$ and
lies in $L^1\cap L^2$.  For fixed $x$ and $\varepsilon>0$ the function
$y\mapsto\chi_R(y)\rho_\varepsilon(x-y)$ belongs to $C_c^\infty(\R^3)$, so
$(\rho_\varepsilon*w)(x)=\int g(y)\,\chi_R(y)\rho_\varepsilon(x-y)\,dy=0$.
By Lemma~\ref{lem:mollify}, $w=\lim_{\varepsilon\to0}\rho_\varepsilon*w=0$
in $L^2$, so $\chi_Rg=0$ a.e., hence $g=0$ a.e.\ on $\{|x|\le R\}$, where
$\chi_R=1$.  Letting $R\to\infty$ through the integers gives $g=0$ a.e.
The consequence follows with $g$ replaced by $f-g$, since
$C_c^\infty\subset\mathcal S$.

(iii) Put $f=\mathcal F^{-1}g\in L^2$.  By (i),
$\widehat{u_f}=u_{\mathcal F\mathcal F^{-1}g}=u_g=\hat u$.  By
Lemma~\ref{lem:duality}(a), $u=(\hat u)^\vee=(\widehat{u_f})^\vee=u_f$, and
$\|f\|_2=\|g\|_2$ by Lemma~\ref{lem:fourier}(L).
\end{proof}

By Lemma~\ref{lem:compat}(i), for $u\in L^2$ the distribution $\hat u$ is
in $L^2$ and is identified with $\mathcal Fu$; we write $\hat u$ for
$\mathcal Fu$ in that case.

\begin{lemma}[Sobolev spaces by derivatives]\label{lem:hk}
Let $k\ge0$ be an integer and $u\in\mathcal S'(\R^3)$.  Then $u\in H^k$ if
and only if $u\in L^2$ and $\partial^\alpha u\in L^2$ for every multi-index
$\alpha$ with $|\alpha|\le k$.  In that case, for all $|\alpha|\le k$,
\[
 \mathcal F(\partial^\alpha u)=(2\pi i\xi)^\alpha\,\mathcal Fu\ \text{ a.e.},\qquad
 \|\partial^\alpha u\|_2=\|(2\pi\xi)^\alpha\mathcal Fu\|_2\le(2\pi)^k\|u\|_{H^k},
 \qquad \|u\|_2\le\|u\|_{H^k}.
\]
In particular, for $u\in H^1$,
\begin{equation}\label{eq:h1-norm}
 \|u\|_{H^1}^2=\|u\|_2^2+(2\pi)^{-2}\|\nabla u\|_2^2 ,
\end{equation}
so a sequence converges in $H^1$ if and only if it and its gradient
converge in $L^2$; and if $u\in H^2$ then $|\xi|^2\mathcal Fu\in L^2$ and
$\partial_ju\in H^1$ with $\|\nabla(\partial_ju)\|_2^2=\sum_i\|\partial_i\partial_ju\|_2^2$.
\end{lemma}

\begin{proof}
Suppose $u\in H^k$: $(1+|\xi|^2)^{k/2}\hat u=u_g$ with $g\in L^2$,
$\|g\|_2=\|u\|_{H^k}$.  Multiplying by the slowly increasing function
$(1+|\xi|^2)^{-k/2}$ and using Lemma~\ref{lem:duality}(c) twice,
$\hat u=u_G$ with $G=(1+|\xi|^2)^{-k/2}g\in L^2$.  By
Lemma~\ref{lem:duality}(b),(c),
$\widehat{\partial^\alpha u}=(2\pi i\xi)^\alpha u_G=u_{(2\pi i\xi)^\alpha G}$,
and $|(2\pi\xi)^\alpha G|\le(2\pi)^{|\alpha|}|\xi|^{|\alpha|}|G|
\le(2\pi)^k(1+|\xi|^2)^{k/2}|G|=(2\pi)^k|g|\in L^2$.
Lemma~\ref{lem:compat}(iii) gives $\partial^\alpha u\in L^2$ with
$\partial^\alpha u=\mathcal F^{-1}\bigl((2\pi i\xi)^\alpha G\bigr)$ and
$\|\partial^\alpha u\|_2=\|(2\pi\xi)^\alpha G\|_2\le(2\pi)^k\|g\|_2$.  The
case $\alpha=0$ gives $u=\mathcal F^{-1}G\in L^2$, $\mathcal Fu=G$ and
$\|u\|_2=\|G\|_2\le\|g\|_2$; inserting $G=\mathcal Fu$ gives
$\mathcal F(\partial^\alpha u)=(2\pi i\xi)^\alpha\mathcal Fu$ a.e.

Conversely, suppose $u=u_f$ with $f\in L^2$ and $\partial^\alpha u=u_{g_\alpha}$
with $g_\alpha\in L^2$ for $|\alpha|\le k$.  By Lemma~\ref{lem:compat}(i),
$\widehat{\partial^\alpha u}=u_{\mathcal Fg_\alpha}$; by
Lemma~\ref{lem:duality}(b),(c) and Lemma~\ref{lem:compat}(i),
$\widehat{\partial^\alpha u}=(2\pi i\xi)^\alpha u_{\mathcal Ff}
=u_{(2\pi i\xi)^\alpha\mathcal Ff}$.  Both $\mathcal Fg_\alpha$ and
$(2\pi i\xi)^\alpha\mathcal Ff$ are square integrable on every ball, so
Lemma~\ref{lem:compat}(ii) gives $\mathcal Fg_\alpha=(2\pi i\xi)^\alpha\mathcal Ff$
a.e.; in particular $\xi^\alpha\mathcal Ff\in L^2$ for all $|\alpha|\le k$.
Expanding $(1+|\xi|^2)^k=(1+\xi_1^2+\xi_2^2+\xi_3^2)^k$ by the multinomial
theorem gives finitely many terms $c_\beta\xi^{2\beta}$ with positive
integer coefficients and $|\beta|\le k$, so
\[
 \int(1+|\xi|^2)^k|\mathcal Ff|^2\,d\xi
 =\sum_{|\beta|\le k}c_\beta\int|\xi^\beta\mathcal Ff|^2\,d\xi<\infty ,
\]
i.e.\ $(1+|\xi|^2)^{k/2}\hat u=u_{(1+|\xi|^2)^{k/2}\mathcal Ff}\in L^2$ and
$u\in H^k$.

For \eqref{eq:h1-norm}: $\int(1+|\xi|^2)|\mathcal Fu|^2=\|u\|_2^2
+\sum_j\int\xi_j^2|\mathcal Fu|^2=\|u\|_2^2+(2\pi)^{-2}\sum_j\|\partial_ju\|_2^2$.
If $u\in H^2$, then $\|\,|\xi|^2\mathcal Fu\|_2\le\sum_i\|\xi_i^2\mathcal Fu\|_2<\infty$,
and $\partial_ju\in L^2$, $\partial_i(\partial_ju)=\partial_i\partial_ju\in L^2$
for all $i$ (the operators $\partial^\alpha$ on $\mathcal S'$ compose as the
multi-indices add, directly from the definition), so $\partial_ju\in H^1$
by the case $k=1$ just proved, with the stated gradient norm.
\end{proof}

\begin{lemma}[Vanishing of total derivatives]\label{lem:div-zero}
Let $g\in C^1(\R^3)$ with $g,\partial_ig\in L^1(\R^3)$ for some
$i\in\{1,2,3\}$.  Then $\int_{\R^3}\partial_ig\,dx=0$.
\end{lemma}

\begin{proof}
Fix $R>0$.  The function $g\chi_R$ is $C^1$ with compact support, so by
Fubini's theorem and the fundamental theorem of calculus on each line
parallel to the $x_i$-axis, $\int_{\R^3}\partial_i(g\chi_R)\,dx=0$; since
$\partial_i(g\chi_R)=(\partial_ig)\chi_R+g\,\partial_i\chi_R$ with both
terms integrable,
\[
 \int_{\R^3}(\partial_ig)\chi_R\,dx=-\int_{\R^3}g\,\partial_i\chi_R\,dx,
 \qquad
 \Bigl|\int_{\R^3}g\,\partial_i\chi_R\,dx\Bigr|
 \le\frac{\|\nabla\chi\|_\infty}{R}\|g\|_1\xrightarrow[R\to\infty]{}0.
\]
On the left, $|(\partial_ig)\chi_R|\le|\partial_ig|\in L^1$ and
$\chi_R\to1$ pointwise, so dominated convergence gives
$\int(\partial_ig)\chi_R\,dx\to\int\partial_ig\,dx$.
\end{proof}

\begin{lemma}[Classical and distributional derivatives]\label{lem:classical}
Let $k\ge0$ and let $u\in C^\infty(\R^3)$ be real-valued with $u\in L^2$ and
$u_u\in H^k$.  Then for every $|\alpha|\le k$ the classical derivative
$\partial^\alpha u$ belongs to $L^2(\R^3)$ and
$\partial^\alpha(u_u)=u_{\partial^\alpha u}$; that is, the distributional
derivatives of $u$ of order $\le k$ are its classical derivatives.
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:hk}, $\partial^\alpha(u_u)=u_g$ for some $g\in L^2$.  Let
$\varphi\in C_c^\infty(\R^3)$.  For $v\in C^1(\R^3)$ and $\psi\in C_c^1(\R^3)$
the product $v\psi$ satisfies the hypotheses of Lemma~\ref{lem:div-zero}
for every $i$, so $\int v\,\partial_i\psi\,dx=-\int(\partial_iv)\psi\,dx$.
Applying this $|\alpha|$ times,
\[
 \int g\varphi\,dx=\langle\partial^\alpha(u_u),\varphi\rangle
 =(-1)^{|\alpha|}\int u\,\partial^\alpha\varphi\,dx
 =\int(\partial^\alpha u)\varphi\,dx .
\]
Thus $\int(g-\partial^\alpha u)\varphi\,dx=0$ for all $\varphi\in C_c^\infty$,
and $g-\partial^\alpha u$ is square integrable on every ball because
$\partial^\alpha u$ is continuous.  Lemma~\ref{lem:compat}(ii) gives
$g=\partial^\alpha u$ a.e., so $\partial^\alpha u\in L^2$ and
$u_{\partial^\alpha u}=u_g=\partial^\alpha(u_u)$.
\end{proof}

\subsection*{Consequences of the local theory used in this section}

Let $(u,p)$ be the classical branch of Proposition~\ref{prop:localtheory}
on $[0,T_*)$.  We use only the following part of that proposition: for every
$T<T_*$ and all $j,k\ge0$,
\[
 u\in C^j([0,T];H^k(\R^3)^3),\qquad p\in C^j([0,T];H^k(\R^3)),
\]
where $u(t)$ and $p(t)$ denote the tempered distributions induced by the
smooth functions $u(t,\cdot)$, $p(t,\cdot)$; $u,p\in C^\infty([0,T]\times\R^3)$
satisfy \eqref{eq:NS} pointwise; $u(0)=u_0$; and
$u,\nabla u,\nabla^2u,\Delta u,\partial_tu,p,\nabla p$ belong to
$C([0,T];L^q(\R^3))$ for every $2\le q\le\infty$.  By
Lemma~\ref{lem:classical}, for each $t$ the classical spatial derivatives
of $u(t,\cdot)$ and $p(t,\cdot)$ of every order lie in $L^2$ and are the
distributional ones, so Lemma~\ref{lem:hk} applies to them.  We write $u_t$
for the derivative of the curve $t\mapsto u(t)$ in $H^k$; it is independent
of $k$ because $\|v\|_{H^k}\le\|v\|_{H^{k+1}}$ for every $v$.

\begin{lemma}[Consequences of the local theory]\label{lem:R-consequences}
Let $T<T_*$ and $t\in[0,T]$.
\begin{enumerate}
\item[(a)] The difference quotients $h^{-1}(u(t+h)-u(t))$ converge in
$H^k(\R^3)^3$ for every $k$, hence in $L^2(\R^3)^3$, to $u_t(t)$ as $h\to0$
(one-sided at $t=0$ and $t=T$), and $u_t(t)$ coincides almost everywhere in
$x$ with the classical partial derivative $\partial_tu(t,\cdot)$.
\item[(b)] The identity
$u_t(t)=\nu\Delta u(t)-(u\cdot\nabla)u(t)-\nabla p(t)$ holds in
$L^2(\R^3)^3$; each of the four terms belongs to $L^2(\R^3)^3$.
\item[(c)] For each $j\in\{1,2,3\}$ the functions $g=u_j|u|^2$ and
$g=u_jp$ (evaluated at time $t$) are of class $C^1(\R^3)$ with
$g,\partial_ig\in L^1(\R^3)$ for $i=1,2,3$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) Convergence in $H^k$ is the statement $u\in C^1([0,T];H^k)$, and
$\|v\|_2\le\|v\|_{H^k}$ (Lemma~\ref{lem:hk}) gives convergence in $L^2$.
An $L^2$-convergent sequence has an almost everywhere convergent
subsequence; taking $h=h_n\to0$ along such a subsequence, the difference
quotients converge almost everywhere to $u_t(t)$, while they converge
everywhere to $\partial_tu(t,x)$ because $u$ is $C^1$ in $t$ pointwise.
The two limits agree almost everywhere.

(b) By (a) and the pointwise equation, $u_t(t)$ equals
$\nu\Delta u-(u\cdot\nabla)u-\nabla p$ almost everywhere.  Each term is in
$L^2$: $\Delta u(t),\nabla p(t)\in L^2$ by Lemma~\ref{lem:classical} (with
$k=2$ and $k=1$); and pointwise $|(u\cdot\nabla)u|\le|u|\,|\nabla u|$, since
for each $k$, $|\sum_ju_j\partial_ju_k|\le|u|\bigl(\sum_j(\partial_ju_k)^2\bigr)^{1/2}$
by the Cauchy--Schwarz inequality, so
$\|(u\cdot\nabla)u\|_2\le\|u\|_\infty\|\nabla u\|_2<\infty$.

(c) Both functions are smooth.  For $g=u_j|u|^2$: $|g|\le|u|^3\in L^1$
because $u(t)\in L^3$; and
$\partial_ig=(\partial_iu_j)|u|^2+2u_j\,u\cdot\partial_iu$, so
$|\partial_ig|\le3|u|^2|\nabla u|$ and
$\|\partial_ig\|_1\le3\|u\|_4^2\|\nabla u\|_2<\infty$ by H\"older's
inequality with exponents $2,2$.  For $g=u_jp$: $|g|\le|u|\,|p|$ with
$u(t),p(t)\in L^2$, so $g\in L^1$; and
$\partial_ig=(\partial_iu_j)p+u_j\partial_ip$ is a sum of products of two
$L^2$ functions, hence in $L^1$.
\end{proof}

\begin{lemma}[Plancherel identities]\label{lem:plancherel}
Let $m\ge1$ and let $u\in H^2(\R^3)^m$, $v\in H^1(\R^3)^m$ be real-valued,
with $\partial_ju$, $\Delta u$, $\partial_jv$ the $L^2$ functions of
Lemma~\ref{lem:hk}.
\begin{enumerate}
\item[(i)] $\displaystyle\int_{\R^3}\nabla u:\nabla v\,dx
 =-\int_{\R^3}\Delta u\cdot v\,dx$, where
 $\nabla u:\nabla v=\sum_{j,k}\partial_ju_k\,\partial_jv_k$.  In particular
 $\int u\cdot\Delta u\,dx=-\|\nabla u\|_2^2$.
\item[(ii)] $\|\nabla^2u\|_2=\|\Delta u\|_2$.
\item[(iii)] If $m=3$, $\operatorname{div}u=0$, and $p\in H^1(\R^3)$ is
 real-valued, then $\displaystyle\int_{\R^3}\nabla p\cdot\Delta u\,dx=0$.
\end{enumerate}
\end{lemma}

\begin{proof}
Write $\hat u_k=\mathcal Fu_k$, $\hat v_k=\mathcal Fv_k$, $\hat p=\mathcal Fp$.
By Lemma~\ref{lem:hk}, $\mathcal F(\partial_ju_k)=2\pi i\xi_j\hat u_k$,
$\mathcal F(\partial_jv_k)=2\pi i\xi_j\hat v_k$,
$\mathcal F(\partial_i\partial_ju_k)=(2\pi i)^2\xi_i\xi_j\hat u_k$,
$\mathcal F(\Delta u_k)=\sum_j(2\pi i\xi_j)^2\hat u_k=-4\pi^2|\xi|^2\hat u_k$,
$\mathcal F(\partial_ip)=2\pi i\xi_i\hat p$, all a.e., and
$|\xi|^2\hat u_k$, $|\xi|\hat p$, $\xi_j\hat v_k$ lie in $L^2$.

(i) For fixed $j,k$, Lemma~\ref{lem:parseval} gives
\[
 \int\partial_ju_k\,\partial_jv_k\,dx
 =\int(2\pi i\xi_j\hat u_k)\overline{(2\pi i\xi_j\hat v_k)}\,d\xi
 =4\pi^2\int\xi_j^2\,\hat u_k\overline{\hat v_k}\,d\xi.
\]
Summing over $j$ gives $4\pi^2\int|\xi|^2\hat u_k\overline{\hat v_k}\,d\xi$,
whose integrand is integrable because $|\xi|^2\hat u_k,\hat v_k\in L^2$.
Lemma~\ref{lem:parseval} again gives
$\int\Delta u_k\,v_k\,dx=\int(-4\pi^2|\xi|^2\hat u_k)\overline{\hat v_k}\,d\xi$.
Summing over $k$ proves (i); the special case is $v=u$.

(ii) By Lemma~\ref{lem:hk},
$\|\partial_i\partial_ju_k\|_2^2=\int(2\pi)^4\xi_i^2\xi_j^2|\hat u_k|^2\,d\xi$.
Summing over $i,j$ gives $\int(2\pi)^4|\xi|^4|\hat u_k|^2\,d\xi
=\|{-4\pi^2}|\xi|^2\hat u_k\|_2^2=\|\Delta u_k\|_2^2$, and summing over $k$
gives (ii).

(iii) Lemma~\ref{lem:parseval} gives
\[
 \int\partial_ip\,\Delta u_i\,dx
 =\int2\pi i\xi_i\hat p\;\overline{(-4\pi^2|\xi|^2\hat u_i)}\,d\xi
 =-4\pi^2\int|\xi|^2\hat p\;\bigl(2\pi i\xi_i\overline{\hat u_i}\bigr)\,d\xi;
\]
the integrand is integrable because $|\xi|\hat p\in L^2$ and
$|\xi|^2\hat u_i\in L^2$.  Since $2\pi i\xi_i\overline{\hat u_i}
=-\overline{2\pi i\xi_i\hat u_i}$, summing over $i$ gives
\[
 \int\nabla p\cdot\Delta u\,dx
 =4\pi^2\int|\xi|^2\hat p\;\overline{\sum_i2\pi i\xi_i\hat u_i}\,d\xi
 =4\pi^2\int|\xi|^2\hat p\;\overline{\mathcal F(\operatorname{div}u)}\,d\xi=0,
\]
because $\operatorname{div}u=\sum_i\partial_iu_i=0$.
\end{proof}

\begin{definition}[Sobolev constant]\label{def:sobolev-constant}
Let $C_S\in(0,\infty)$ be a constant such that
\begin{equation}\label{eq:sobolev-cc}
 \|f\|_6\le C_S\|\nabla f\|_2
 \qquad\text{for every real-valued }f\in C_c^1(\R^3).
\end{equation}
Such a constant exists.  (a) It is the case $n=3$, $j=0$, $m=1$, $r=q=2$,
$a=1$, $p=6$ of the theorem on p.~125 of Nirenberg \cite{Nirenberg1959}
(inequality (2.2) there, with
$\tfrac1p=\tfrac ar-\tfrac{am}n+\tfrac{1-a}q=\tfrac12-\tfrac13=\tfrac16$;
neither exceptional case applies, since $q=2<\infty$ and
$m-j-n/r=-\tfrac12$ is not a nonnegative integer).  Nirenberg's
$\|D^1f\|_2$ is the maximum over $j$ of $\|\partial_jf\|_2$, and
$\max_j\|\partial_jf\|_2\le\|\,|\nabla f|\,\|_2$, so his inequality implies
\eqref{eq:sobolev-cc} with his constant.  (b) It is the case $p=2$,
$p'=6$, $\dim E=3$, $F=\R$ of the Gagliardo--Nirenberg--Sobolev inequality
\texttt{MeasureTheory.eLpNorm\_le\_eLpNorm\_fderiv\_of\_eq} formalised in
Mathlib \cite{MathlibSobolev}, whose right side carries the operator norm
of the Fr\'echet derivative, which for scalar $f$ is $|\nabla f|$.  Only the
existence of $C_S$ is used; its value is not.
\end{definition}

\begin{lemma}[Density]\label{lem:density}
$C_c^\infty(\R^3)$ is dense in $H^1(\R^3)$: for every $u\in H^1(\R^3)$ there
are $u_n\in C_c^\infty(\R^3)$ with $\|u_n-u\|_2+\|\nabla u_n-\nabla u\|_2\to0$.
\end{lemma}

\begin{proof}
\emph{Step 1 (truncation).}  Let $u\in H^1(\R^3)$, so $u,\partial_ju\in L^2$
by Lemma~\ref{lem:hk}.  For $\varphi\in\mathcal S$, the definition of the
distributional derivative applied with the test function
$\chi_R\varphi\in C_c^\infty\subset\mathcal S$ gives
\[
 \langle\partial_j(\chi_Ru),\varphi\rangle=-\int\chi_Ru\,\partial_j\varphi\,dx
 =-\int u\,\partial_j(\chi_R\varphi)\,dx+\int u\varphi\,\partial_j\chi_R\,dx
 =\int(\chi_R\partial_ju+u\,\partial_j\chi_R)\varphi\,dx,
\]
so $\chi_Ru\in L^2$ has $\partial_j(\chi_Ru)=\chi_R\partial_ju+u\,\partial_j\chi_R\in L^2$
and $\chi_Ru\in H^1$ by Lemma~\ref{lem:hk}; it has compact support.
Moreover $\|\chi_Ru-u\|_2\to0$ and $\|(\chi_R-1)\partial_ju\|_2\to0$ as
$R\to\infty$ by dominated convergence (majorants $|u|^2$ and
$|\partial_ju|^2$), and
$\|u\,\partial_j\chi_R\|_2\le R^{-1}\|\nabla\chi\|_\infty\|u\|_2\to0$.
Hence $\chi_Ru\to u$ in $H^1$ by \eqref{eq:h1-norm}.

\emph{Step 2 (mollification).}  Let $v\in H^1(\R^3)$ vanish outside a
compact set $K$.  Then $v\in L^1\cap L^2$, and so does its distributional
derivative $g:=\partial_jv\in L^2$, because $g=0$ a.e.\ outside $K$: for
$\chi\in C_c^\infty(\R^3\setminus K)$ put $w=\chi g\in L^1\cap L^2$; for
fixed $x$ and $\varepsilon>0$ the function $y\mapsto\chi(y)\rho_\varepsilon(x-y)$
lies in $C_c^\infty(\R^3\setminus K)$, so
$(\rho_\varepsilon*w)(x)=\langle\partial_jv,\chi\rho_\varepsilon(x-\cdot)\rangle
=-\int v\,\partial_j[\chi\rho_\varepsilon(x-\cdot)]\,dy=0$ since $v=0$ off
$K$; Lemma~\ref{lem:mollify} gives $w=0$ in $L^2$, i.e.\ $g=0$ a.e.\ on
$\{\chi\ne0\}$, and $\R^3\setminus K$ is the union of countably many such
sets (take $\chi_n\in C_c^\infty(\R^3\setminus K)$ with $\chi_n=1$ on
$\{|x|\le n,\ \operatorname{dist}(x,K)\ge1/n\}$).  Put
$v_\varepsilon=\rho_\varepsilon*v$.  By Lemma~\ref{lem:mollify},
$v_\varepsilon\in C_c^\infty(\R^3)$.  Applying the definition of the
distributional derivative with the test function
$y\mapsto\rho_\varepsilon(x-y)\in C_c^\infty$,
\[
 \partial_jv_\varepsilon(x)
 =\int\partial_j\rho_\varepsilon(x-y)\,v(y)\,dy
 =-\int\partial_{y_j}\bigl[\rho_\varepsilon(x-y)\bigr]v(y)\,dy
 =\int\rho_\varepsilon(x-y)\,\partial_jv(y)\,dy
 =(\rho_\varepsilon*\partial_jv)(x).
\]
Lemma~\ref{lem:mollify} applied to $w=v$ and to $w=\partial_jv$ gives
$v_\varepsilon\to v$ and $\partial_jv_\varepsilon\to\partial_jv$ in $L^2$,
i.e.\ $v_\varepsilon\to v$ in $H^1$ by \eqref{eq:h1-norm}.

\emph{Conclusion.}  Given $u\in H^1$ and $n\ge1$, choose $R$ with
$\|\chi_Ru-u\|_{H^1}<1/(2n)$ by Step~1, then $\varepsilon$ with
$\|(\chi_Ru)_\varepsilon-\chi_Ru\|_{H^1}<1/(2n)$ by Step~2, and put
$u_n=(\chi_Ru)_\varepsilon\in C_c^\infty(\R^3)$; then $u_n\to u$ in $H^1$,
which by \eqref{eq:h1-norm} is the claim.
\end{proof}

\begin{lemma}[Sobolev inequality on $H^1$]\label{lem:sobolev}
Let $m\ge1$ and $f\in H^1(\R^3)^m$ be real-valued.  Then $f\in L^6(\R^3)^m$
and
\[
 \|f\|_6\le\sqrt m\,C_S\|\nabla f\|_2 .
\]
\end{lemma}

\begin{proof}
\emph{Scalar case $m=1$.}  Let $u_n\in C_c^\infty(\R^3)$ converge to $f$ in
$H^1$ (Lemma~\ref{lem:density}); replacing $u_n$ by its real part keeps
$u_n\in C_c^\infty$ and only decreases $\|u_n-f\|_2$ and
$\|\nabla u_n-\nabla f\|_2$; and $u_n\in H^1$ (indeed $\hat u_n\in\mathcal S$
by Lemma~\ref{lem:fourier}(S)), so for $u_n$ the distributional gradient is
the classical one by Lemma~\ref{lem:classical}.  By \eqref{eq:sobolev-cc},
$\|u_n\|_6\le C_S\|\nabla u_n\|_2\to C_S\|\nabla f\|_2$.  Since $u_n\to f$
in $L^2$, a subsequence $u_{n_l}$ converges to $f$ almost everywhere, and
Fatou's lemma gives
\[
 \int|f|^6\,dx\le\liminf_{l\to\infty}\int|u_{n_l}|^6\,dx
 \le\bigl(C_S\|\nabla f\|_2\bigr)^6 .
\]
\emph{Vector case.}  Pointwise $|f|\le\sum_{k=1}^m|f_k|$, so by
Minkowski's inequality, the scalar case, and the Cauchy--Schwarz inequality
in $\R^m$,
\[
 \|f\|_6\le\sum_{k=1}^m\|f_k\|_6\le C_S\sum_{k=1}^m\|\nabla f_k\|_2
 \le C_S\sqrt m\Bigl(\sum_{k=1}^m\|\nabla f_k\|_2^2\Bigr)^{1/2}
 =\sqrt m\,C_S\|\nabla f\|_2 .
 \qedhere
\]
\end{proof}

\begin{lemma}[Interpolation]\label{lem:interp}
If $f\in L^2(\R^3)^m\cap L^6(\R^3)^m$, then
$\|f\|_3\le\|f\|_2^{1/2}\|f\|_6^{1/2}$.  Consequently, for real-valued
$f\in H^1(\R^3)^m$,
\[
 \|f\|_3\le(\sqrt m\,C_S)^{1/2}\,\|f\|_2^{1/2}\|\nabla f\|_2^{1/2}.
\]
\end{lemma}

\begin{proof}
Write $|f|^3=|f|^{3/2}\cdot|f|^{3/2}$ and apply H\"older's inequality with
the conjugate exponents $4/3$ and $4$:
\[
 \int|f|^3\,dx\le\Bigl(\int|f|^2\,dx\Bigr)^{3/4}\Bigl(\int|f|^6\,dx\Bigr)^{1/4}
 =\|f\|_2^{3/2}\|f\|_6^{3/2}.
\]
Taking cube roots gives the first inequality; Lemma~\ref{lem:sobolev}
gives the second.
\end{proof}

\begin{lemma}[Gradient interpolation]\label{lem:GN}
For every real-valued $u\in H^2(\R^3)^3$,
\[
 \|\nabla u\|_3\le(3C_S)^{1/2}\,\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{1/2}.
\]
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:hk}, each $\partial_ju_k$ lies in $H^1$ with
$\|\nabla(\partial_ju_k)\|_2^2=\sum_i\|\partial_i\partial_ju_k\|_2^2$, so
$\nabla u=(\partial_ju_k)_{j,k}\in H^1(\R^3)^9$ with
$\|\nabla(\nabla u)\|_2=\|\nabla^2u\|_2$.  Lemma~\ref{lem:interp} with
$m=9$ gives $\|\nabla u\|_3\le\|\nabla u\|_2^{1/2}\|\nabla u\|_6^{1/2}$, and
Lemma~\ref{lem:sobolev} with $m=9$ gives
$\|\nabla u\|_6\le3C_S\|\nabla^2u\|_2$.  Finally
$\|\nabla^2u\|_2=\|\Delta u\|_2$ by Lemma~\ref{lem:plancherel}(ii).
\end{proof}

\begin{proposition}[Energy identity]\label{prop:energy}
For every $0\le s\le t<T_*$,
\begin{equation}\label{eq:energy}
 \frac12\norm{u(t)}_2^2
 +\nu\int_s^t\norm{\nabla u(\tau)}_2^2\,d\tau
 =\frac12\norm{u(s)}_2^2.
\end{equation}
In particular, $\sup_{t<T_*}\norm{u(t)}_2\le\norm{u_0}_2$ and
$\int_0^{T_*}\norm{\nabla u(t)}_2^2dt\le\norm{u_0}_2^2/(2\nu)$.
\end{proposition}

\begin{proof}
Fix $T$ with $t\le T<T_*$ and put $E(\tau)=\frac12\|u(\tau)\|_2^2$ for
$\tau\in[0,T]$.

\emph{Step 1: differentiation.}  For $\tau,\tau+h\in[0,T]$, $h\ne0$,
\[
 \frac{E(\tau+h)-E(\tau)}h
 =\frac12\Bigl\langle\frac{u(\tau+h)-u(\tau)}h,\;u(\tau+h)+u(\tau)\Bigr\rangle_{L^2}.
\]
As $h\to0$ the first argument converges in $L^2$ to $u_t(\tau)$
(Lemma~\ref{lem:R-consequences}(a)) and the second converges in $L^2$ to
$2u(\tau)$ (continuity of $u$ in $L^2$).  Since the $L^2$ inner product is
continuous on $L^2\times L^2$, $E$ is differentiable on $[0,T]$ (one-sided
at the endpoints) with
\begin{equation}\label{eq:energy-derivative}
 E'(\tau)=\int_{\R^3}u\cdot u_t\,dx
 =\nu\int_{\R^3}u\cdot\Delta u\,dx-\int_{\R^3}u\cdot(u\cdot\nabla)u\,dx
  -\int_{\R^3}u\cdot\nabla p\,dx,
\end{equation}
where the second equality inserts Lemma~\ref{lem:R-consequences}(b); all
three integrals converge absolutely because $u(\tau)\in L^2$ and each of
$\Delta u,(u\cdot\nabla)u,\nabla p$ is in $L^2$.

\emph{Step 2: the diffusion term.}  Since $u(\tau)\in H^2$,
Lemma~\ref{lem:plancherel}(i) with $v=u$ gives
$\int u\cdot\Delta u\,dx=-\|\nabla u(\tau)\|_2^2$.

\emph{Step 3: the convection term.}  Pointwise,
$u\cdot(u\cdot\nabla)u=\sum_{j,k}u_ju_k\partial_ju_k
=\frac12\sum_ju_j\partial_j|u|^2
=\frac12\sum_j\partial_j\bigl(u_j|u|^2\bigr)-\frac12(\operatorname{div}u)|u|^2$.
The last term vanishes because $\operatorname{div}u=0$.  By
Lemma~\ref{lem:R-consequences}(c), each $g=u_j|u|^2$ satisfies the
hypotheses of Lemma~\ref{lem:div-zero}, so $\int\partial_j(u_j|u|^2)\,dx=0$.
Hence $\int u\cdot(u\cdot\nabla)u\,dx=0$.

\emph{Step 4: the pressure term.}  Pointwise,
$u\cdot\nabla p=\sum_j\partial_j(u_jp)-(\operatorname{div}u)p
=\sum_j\partial_j(u_jp)$, and each $g=u_jp$ satisfies the hypotheses of
Lemma~\ref{lem:div-zero} by Lemma~\ref{lem:R-consequences}(c).  Hence
$\int u\cdot\nabla p\,dx=0$.

\emph{Step 5: time integration.}  Steps 1--4 give
$E'(\tau)=-\nu\|\nabla u(\tau)\|_2^2$ for every $\tau\in[0,T]$.  The right
side is continuous in $\tau$ because $\nabla u\in C([0,T];L^2)$, so
$E\in C^1([0,T])$ and the fundamental theorem of calculus gives
$E(t)-E(s)=-\nu\int_s^t\|\nabla u(\tau)\|_2^2\,d\tau$, which is
\eqref{eq:energy}.  For the two consequences take $s=0$ and use $u(0)=u_0$;
the bound $\int_0^T\|\nabla u\|_2^2\le\|u_0\|_2^2/(2\nu)$ holds for every
$T<T_*$, and the integral over $[0,T_*)$ is the supremum over such $T$.
\end{proof}

\begin{proposition}[Scaling and the energy-level spacetime bound]\label{prop:scaling}
\begin{enumerate}
\item[(i)] Let $u\colon\R^3\times[0,T)\to\R^3$ and
$p\colon\R^3\times[0,T)\to\R$ be smooth and satisfy the momentum and
divergence equations of \eqref{eq:NS} pointwise, with viscosity $\nu$.  For
$\lambda>0$ the fields
\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),\qquad
 p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t)
\]
are smooth on $\R^3\times[0,T/\lambda^2)$ and satisfy the same two
equations there with the same $\nu$, and $u_\lambda(\cdot,0)=\lambda u(\lambda\,\cdot,0)$.
If $u(\cdot,0)=u_0$ is a divergence-free Schwartz field, then so is
$u_\lambda(\cdot,0)=\lambda u_0(\lambda\,\cdot)$.
\item[(ii)] For every $1\le q\le\infty$, every $t\in[0,T/\lambda^2)$ and
every measurable $u$, with both sides allowed to be $+\infty$,
\begin{equation}\label{eq:scaling-norm}
 \norm{u_\lambda(t)}_q=\lambda^{1-3/q}\norm{u(\lambda^2t)}_q .
\end{equation}
Thus $L^3_x$ is invariant, whereas $\norm{u_\lambda(t)}_2^2
=\lambda^{-1}\norm{u(\lambda^2t)}_2^2$.
\item[(iii)] For the classical branch of Proposition~\ref{prop:localtheory}
and every $T<T_*$,
\begin{equation}\label{eq:L4L3}
 \int_0^T\norm{u(t)}_3^4dt
 \le 3C_S^2\Bigl(\sup_{0\le t\le T}\norm{u(t)}_2^2\Bigr)
      \int_0^T\norm{\nabla u(t)}_2^2dt
 \le\frac{3C_S^2\norm{u_0}_2^4}{2\nu}<\infty .
\end{equation}
\end{enumerate}
\end{proposition}

\begin{proof}
(i) By the chain rule, at the point $(x,t)$ and with all right-hand sides
evaluated at $(\lambda x,\lambda^2t)$,
\[
 \partial_tu_\lambda=\lambda\cdot\lambda^2\,\partial_tu=\lambda^3\partial_tu,\quad
 \partial_ju_\lambda=\lambda^2\partial_ju,\quad
 \Delta u_\lambda=\lambda^3\Delta u,\quad
 \nabla p_\lambda=\lambda^2\cdot\lambda\,\nabla p=\lambda^3\nabla p,
\]
and
$(u_\lambda\cdot\nabla)u_\lambda=\sum_j(\lambda u_j)(\lambda^2\partial_ju)
=\lambda^3(u\cdot\nabla)u$.  Hence
\[
 \partial_tu_\lambda+(u_\lambda\cdot\nabla)u_\lambda+\nabla p_\lambda-\nu\Delta u_\lambda
 =\lambda^3\bigl[\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u\bigr](\lambda x,\lambda^2t)=0,
\]
and $\operatorname{div}u_\lambda=\sum_j\lambda^2(\partial_ju_j)(\lambda x,\lambda^2t)=0$.
The formula for $u_\lambda(\cdot,0)$ is the definition at $t=0$; if $u_0$ is
Schwartz then $\lambda u_0(\lambda\,\cdot)$ is Schwartz (every seminorm
$\sup|x^\alpha\partial^\beta(\cdot)|$ is multiplied by a power of
$\lambda$), and it is divergence-free by the computation just made at $t=0$.

(ii) For $1\le q<\infty$, the change of variables $y=\lambda x$ (a linear
bijection of $\R^3$ with $dy=\lambda^3dx$) gives
\[
 \|u_\lambda(t)\|_q^q=\lambda^q\int_{\R^3}|u(\lambda x,\lambda^2t)|^q\,dx
 =\lambda^{q-3}\int_{\R^3}|u(y,\lambda^2t)|^q\,dy,
\]
and taking $q$-th roots gives \eqref{eq:scaling-norm}.  For $q=\infty$:
the map $x\mapsto\lambda x$ multiplies Lebesgue measure by $\lambda^3$, so
it maps null sets to null sets in both directions; for $M\ge0$ the set
$\{x:|u_\lambda(x,t)|>\lambda M\}=\lambda^{-1}\{y:|u(y,\lambda^2t)|>M\}$ is
therefore null if and only if $\{y:|u(y,\lambda^2t)|>M\}$ is null.  Hence
$\operatorname*{ess\,sup}|u_\lambda(t)|=\lambda\operatorname*{ess\,sup}|u(\lambda^2t)|$,
which is \eqref{eq:scaling-norm} with $1-3/q=1$.  The two consequences are
the cases $q=3$ and $q=2$.

(iii) For $t\le T<T_*$, $u(t)\in H^1(\R^3)^3$ is real-valued, so
Lemma~\ref{lem:interp} with $m=3$ gives
$\|u(t)\|_3\le(\sqrt3C_S)^{1/2}\|u(t)\|_2^{1/2}\|\nabla u(t)\|_2^{1/2}$;
raising to the fourth power,
\begin{equation}\label{eq:L4L3-constant}
 \|u(t)\|_3^4\le3C_S^2\,\|u(t)\|_2^2\,\|\nabla u(t)\|_2^2 .
\end{equation}
Both sides are continuous in $t$ ($u\in C([0,T];L^2\cap L^3)$,
$\nabla u\in C([0,T];L^2)$), so integrating over $[0,T]$ and bounding
$\|u(t)\|_2^2$ by its supremum gives the first inequality in
\eqref{eq:L4L3}; Proposition~\ref{prop:energy} bounds the supremum by
$\|u_0\|_2^2$ and the integral by $\|u_0\|_2^2/(2\nu)$.
\end{proof}

\begin{remark}[Normalised pressure under scaling]\label{rem:scaling-pressure}
With the Riesz transforms $R_j$ given by $\mathcal F(R_jf)=-i\xi_j|\xi|^{-1}\mathcal Ff$,
the operator $R_iR_j$ acts on $f\in L^2$ by
$\mathcal F(R_iR_jf)=m_{ij}\mathcal Ff$ with $m_{ij}(\xi)=-\xi_i\xi_j/|\xi|^2$;
this is also the multiplier of $-\Delta^{-1}\partial_i\partial_j$, since
$\Delta^{-1}$ has multiplier $-(4\pi^2|\xi|^2)^{-1}$ and
$\partial_i\partial_j$ has multiplier $(2\pi i\xi_i)(2\pi i\xi_j)=-4\pi^2\xi_i\xi_j$
(Lemma~\ref{lem:duality}(b)).  So $p=R_iR_j(u_iu_j)$ is Tao's normalised
pressure.  The rescaled pressure $p_\lambda$ is again the normalised
pressure $R_iR_j\bigl((u_\lambda)_i(u_\lambda)_j\bigr)$ of $u_\lambda$.
Indeed, for $f\in L^1\cap L^2$ and $f_\lambda:=f(\lambda\,\cdot)$, the
change of variables of Proposition~\ref{prop:scaling}(ii) gives
$\widehat{f_\lambda}(\xi)=\lambda^{-3}\hat f(\xi/\lambda)$, and this
extends to $f\in L^2$ by continuity of $\mathcal F$ and of $g\mapsto g(\cdot/\lambda)$
on $L^2$; since $m_{ij}(\xi/\lambda)=m_{ij}(\xi)$,
$\mathcal F(R_iR_jf_\lambda)=m_{ij}\widehat{f_\lambda}
=\lambda^{-3}(m_{ij}\hat f)(\cdot/\lambda)=\mathcal F\bigl((R_iR_jf)_\lambda\bigr)$.
Applying this with $f=u_iu_j(\cdot,\lambda^2t)\in L^2$ (as
$u(\lambda^2t)\in L^4$) and using $(u_\lambda)_i(u_\lambda)_j
=\lambda^2(u_iu_j)_\lambda$ gives
$R_iR_j\bigl((u_\lambda)_i(u_\lambda)_j\bigr)
=\lambda^2\bigl(R_iR_j(u_iu_j)\bigr)_\lambda=p_\lambda$.
Whether $(u_\lambda,p_\lambda)$ is the classical branch of the datum
$\lambda u_0(\lambda\,\cdot)$ is a uniqueness question for
Proposition~\ref{prop:localtheory}; it is not needed in this paper.
\end{remark}

\begin{remark}[The interpolation mismatch]\label{rem:mismatch}
Proposition~\ref{prop:scaling}(iii) controls $u$ in $L^4(0,T;L^3)$ only.
Two elementary facts show that this is weaker than what
Hypothesis~\ref{hyp:critical} asks for, and in which sense.

(a) \emph{$g\mapsto\|g\|_{L^4(0,T)}$ does not dominate
$\|g\|_{L^\infty(0,T)}$.}  For $T>0$ put $g(t)=t^{-1/5}$ on $(0,T)$.  Then
$\int_0^Tg(t)^4\,dt=\int_0^Tt^{-4/5}\,dt=5T^{1/5}<\infty$, while for every
$M>0$ the set $\{t\in(0,T):g(t)>M\}=(0,\min\{T,M^{-5}\})$ has positive
measure, so $\operatorname*{ess\,sup}_{(0,T)}g=\infty$.  Hence there is no
constant $K$ with $\|g\|_{L^\infty(0,T)}\le K\|g\|_{L^4(0,T)}$ for all
$g\in L^4(0,T)$, and in particular no inequality of that form passes from
the left side of \eqref{eq:L4L3} to $\sup_{t<T}\|u(t)\|_3$.  (This
witness is machine-checked as
\texttt{NavierFormal.exists\_memLp\_four\_not\_memLp\_top}.)

(b) \emph{Supercriticality.}  For $1\le r<\infty$, $1\le q\le\infty$,
\eqref{eq:scaling-norm} and the substitution $s=\lambda^2t$ give
\begin{equation}\label{eq:LPS}
 \int_0^{T/\lambda^2}\|u_\lambda(t)\|_q^r\,dt
 =\lambda^{r(1-3/q)}\int_0^{T/\lambda^2}\|u(\lambda^2t)\|_q^r\,dt
 =\lambda^{r(1-3/q)-2}\int_0^T\|u(s)\|_q^r\,ds,
\end{equation}
that is, $\|u_\lambda\|_{L^r(0,T/\lambda^2;L^q)}
=\lambda^{1-3/q-2/r}\|u\|_{L^r(0,T;L^q)}$.  The norm is invariant under the
scaling of Proposition~\ref{prop:scaling}(i) exactly when $2/r+3/q=1$; we
call it supercritical when $2/r+3/q>1$, in which case the exponent
$1-3/q-2/r$ is negative.  For the norm in \eqref{eq:L4L3}, $(r,q)=(4,3)$
and $2/4+3/3=3/2>1$ (this arithmetic is machine-checked as
\texttt{NavierFormal.L4L3\_supercritical}), so the exponent is
$1-1-\tfrac12=-\tfrac12$.  No bound on $\sup_{t<T_*}\|u(t)\|_3$ is deduced
here, and none is claimed.
\end{remark}

\section{The enstrophy estimate}

\begin{proposition}[Cubic differential inequality]\label{prop:enstrophy}
Let $Y(t)=\norm{\nabla u(t)}_2^2$ for $0\le t<T_*$.  Then $Y\in C^1([0,T])$
for every $T<T_*$, and with the constant
$C_E:=\tfrac{2187}{32}C_S^6$ one has, for every $0\le t<T_*$,
\begin{equation}\label{eq:enstrophy}
 \frac12Y'(t)+\frac\nu2\norm{\Delta u(t)}_2^2
 \le C_E\nu^{-3}Y(t)^3.
\end{equation}
\end{proposition}

\begin{proof}
Fix $T$ with $t\le T<T_*$.

\emph{Step 1: the identity.}  By Lemma~\ref{lem:hk},
$\|\partial_jv\|_2\le2\pi\|v\|_{H^1}$ for $v\in H^1$, so $\partial_j$ is a
bounded linear map $H^1\to L^2$ and commutes with $H^1$-limits of difference
quotients:
$h^{-1}(\nabla u(\tau+h)-\nabla u(\tau))=\nabla\bigl[h^{-1}(u(\tau+h)-u(\tau))\bigr]
\to\nabla u_t(\tau)$ in $L^2$ by Lemma~\ref{lem:R-consequences}(a).  Hence
$\tau\mapsto\nabla u(\tau)$ is $C^1([0,T];L^2)$ with derivative
$\nabla u_t$, and exactly as in Step~1 of the proof of
Proposition~\ref{prop:energy},
\[
 Y'(\tau)=2\int_{\R^3}\nabla u:\nabla u_t\,dx ,
\]
which is continuous in $\tau$; so $Y\in C^1([0,T])$.  Since
$u(\tau)\in H^2$ and $u_t(\tau)\in H^1$, Lemma~\ref{lem:plancherel}(i)
gives $\int\nabla u:\nabla u_t\,dx=-\int\Delta u\cdot u_t\,dx$.  Inserting
$u_t=\nu\Delta u-(u\cdot\nabla)u-\nabla p$ (Lemma~\ref{lem:R-consequences}(b);
every term is in $L^2$, and $\Delta u(\tau)\in L^2$),
\[
 -\int\Delta u\cdot u_t\,dx
 =-\nu\|\Delta u\|_2^2+\int(u\cdot\nabla)u\cdot\Delta u\,dx
  +\int\nabla p\cdot\Delta u\,dx ,
\]
and the last integral vanishes by Lemma~\ref{lem:plancherel}(iii), since
$p(\tau)\in H^1$, $u(\tau)\in H^2$, $\operatorname{div}u=0$.  Therefore
\begin{equation}\label{eq:enstrophy-identity}
 \frac12Y'(\tau)+\nu\norm{\Delta u(\tau)}_2^2
 =\int_{\R^3}(u\cdot\nabla)u\cdot\Delta u\,dx .
\end{equation}

\emph{Step 2: H\"older.}  Pointwise $|(u\cdot\nabla)u|\le|u|\,|\nabla u|$
(proof of Lemma~\ref{lem:R-consequences}(b)), so H\"older's inequality with
$\frac16+\frac13+\frac12=1$ (applied twice: first with exponents $6$ and
$6/5$ to $|u|$ and $|\nabla u|\,|\Delta u|$, then with exponents
$\frac{5}{2}$ and $\frac53$ to $|\nabla u|^{6/5}$ and $|\Delta u|^{6/5}$)
gives
\[
 \Bigl|\int(u\cdot\nabla)u\cdot\Delta u\,dx\Bigr|
 \le\|u\|_6\,\|\nabla u\|_3\,\|\Delta u\|_2 .
\]

\emph{Step 3: Sobolev and gradient interpolation.}  By
Lemma~\ref{lem:sobolev} with $m=3$, $\|u\|_6\le\sqrt3C_S\,Y^{1/2}$; by
Lemma~\ref{lem:GN}, $\|\nabla u\|_3\le(3C_S)^{1/2}Y^{1/4}\|\Delta u\|_2^{1/2}$.
Hence
\[
 \Bigl|\int(u\cdot\nabla)u\cdot\Delta u\,dx\Bigr|
 \le\sqrt3C_S\,(3C_S)^{1/2}\,Y^{3/4}\|\Delta u\|_2^{3/2}
 =3C_S^{3/2}\,Y^{3/4}\|\Delta u\|_2^{3/2}.
\]

\emph{Step 4: Young.}  For $a,b\ge0$ and $\delta>0$, Young's inequality
with the conjugate exponents $4/3$ and $4$, applied to $(\delta a)(b/\delta)$,
gives $ab\le\frac34\delta^{4/3}a^{4/3}+\frac14\delta^{-4}b^4$.  Take
$a=\|\Delta u\|_2^{3/2}$, $b=3C_S^{3/2}Y^{3/4}$, and $\delta^{4/3}=2\nu/3$,
so that $\frac34\delta^{4/3}=\nu/2$ and
$\delta^{-4}=(\delta^{4/3})^{-3}=(3/(2\nu))^3$.  Then
\[
 3C_S^{3/2}Y^{3/4}\|\Delta u\|_2^{3/2}
 \le\frac\nu2\|\Delta u\|_2^2+\frac14\Bigl(\frac3{2\nu}\Bigr)^3\,81\,C_S^6\,Y^3
 =\frac\nu2\|\Delta u\|_2^2+\frac{2187}{32}C_S^6\,\nu^{-3}Y^3 .
\]

\emph{Step 5.}  Combining \eqref{eq:enstrophy-identity} with Steps 2--4 and
moving $\frac\nu2\|\Delta u\|_2^2$ to the left proves \eqref{eq:enstrophy}
at $\tau=t$.
\end{proof}

The right side of \eqref{eq:enstrophy} has the wrong sign for an a priori
upper bound uniform in time.  Dropping dissipation and comparing with
$z'=C_\nu z^3$ gives a lower bound on a possible lifespan from the current
value of $Y$, but gives no bound beyond the comparison ODE's blowup time.

\begin{proposition}[Scalar obstruction]\label{prop:ode}
For every $C>0$ and $T>0$, there is a positive differentiable function
$y:[0,T)\to(0,\infty)$ such that
\[
 y'=Cy^3,\qquad \int_0^T y(t)\,dt<\infty,
 \qquad\text{and}\qquad \lim_{t\uparrow T}y(t)=\infty.
\]
\end{proposition}

\begin{proof}
Set $y(t)=(2C(T-t))^{-1/2}$.  Direct differentiation gives $y'=Cy^3$, while
\[
 \int_0^T y(t)dt=(2C)^{-1/2}\int_0^T(T-t)^{-1/2}dt
 =\sqrt{2T/C}<\infty.
\]
\end{proof}

Proposition~\ref{prop:ode} is not a model of a Navier--Stokes singularity.
It proves only the logical point needed here: the two scalar consequences
$\int_0^{T_*}Y<\infty$ and $Y'\le C_\nu Y^3$ do not rule out $Y\to\infty$.

\begin{remark}[Machine-checked statements]\label{rem:lean}
Proposition~\ref{prop:ode} is formalised as
\texttt{NavierFormal.scalar\_obstruction\_exists} (witness
\texttt{NavierFormal.scalarObstruction}, with
$\int_0^Ty=\sqrt{2T/C}$ as \texttt{NavierFormal.integral\_scalarObstruction}),
the norm identity \eqref{eq:scaling-norm} for $0<q<\infty$ as
\texttt{NavierFormal.eLpNorm\_dilate} and
\texttt{NavierFormal.eLpNorm\_dilateSpaceTime}, the witness of
Remark~\ref{rem:mismatch}(a) as
\texttt{NavierFormal.exists\_memLp\_four\_not\_memLp\_top}, and the
arithmetic $2/4+3/3=3/2>1$ of Remark~\ref{rem:mismatch}(b) as
\texttt{NavierFormal.L4L3\_supercritical}.  These are Lean~4 proofs from
Mathlib with no literature input; the PDE halves of
Propositions~\ref{prop:energy}, \ref{prop:scaling}, and
\ref{prop:enstrophy} are paper proofs only.
\end{remark}

\begin{remark}[Use in the conditional argument]\label{rem:usage}
Of the results of these two sections, only Proposition~\ref{prop:energy}
and Lemma~\ref{lem:sobolev} enter the conditional chain leading to
Theorem~\ref{thm:conditional}: the energy identity supplies the uniform
kinetic-energy bound in Theorem~\ref{thm:conditional} and the
$\|u\otimes u\|_1$ and $\int_0^\tau\|\nabla u\|_2$ bounds in
Proposition~\ref{prop:lowpressure}, and the Sobolev inequality is used in
the converse half of the existential-equivalence statement after
Hypothesis~\ref{hyp:absorption}.  Proposition~\ref{prop:scaling},
Proposition~\ref{prop:enstrophy}, and Proposition~\ref{prop:ode} are not
used in that chain; they explain why the energy-level and enstrophy-level
estimates do not by themselves supply Hypothesis~\ref{hyp:critical}.
\end{remark}
```

Notes for the integrator.

* Four bibliography entries are needed in `references.bib`:

```bibtex
@book{Grafakos2014,
  author    = {Loukas Grafakos},
  title     = {Classical Fourier Analysis},
  edition   = {Third},
  series    = {Graduate Texts in Mathematics},
  volume    = {249},
  publisher = {Springer},
  address   = {New York},
  year      = {2014},
  doi       = {10.1007/978-1-4939-1194-3}
}

@article{Nirenberg1959,
  author  = {Louis Nirenberg},
  title   = {On elliptic partial differential equations},
  journal = {Annali della Scuola Normale Superiore di Pisa, Classe di Scienze, Serie 3},
  volume  = {13},
  number  = {2},
  year    = {1959},
  pages   = {115--162},
  url     = {http://www.numdam.org/item/ASNSP_1959_3_13_2_115_0/}
}

@misc{MathlibSobolev,
  author       = {{The Mathlib Community}},
  title        = {Mathlib, file \texttt{Mathlib/Analysis/FunctionalSpaces/SobolevInequality.lean}, declaration \texttt{MeasureTheory.eLpNorm\_le\_eLpNorm\_fderiv\_of\_eq}},
  howpublished = {Lean 4 library, commit \texttt{0df444a} (21 August 2026)},
  year         = {2026}
}

@misc{MathlibFourier,
  author       = {{The Mathlib Community}},
  title        = {Mathlib, files \texttt{Mathlib/Analysis/Fourier/LpSpace.lean}
                  (\texttt{MeasureTheory.Lp.fourierTransform}$_{\ell\mathrm i}$,
                  \texttt{MeasureTheory.Lp.norm\_fourier\_eq},
                  \texttt{MeasureTheory.Lp.inner\_fourier\_eq},
                  \texttt{MeasureTheory.Lp.fourier\_toTemperedDistribution\_eq}),
                  \texttt{Mathlib/Analysis/Distribution/TemperedDistribution.lean}
                  (\texttt{TemperedDistribution.fourier\_lineDerivOp\_eq}) and
                  \texttt{Mathlib/Analysis/Distribution/Sobolev.lean}
                  (\texttt{TemperedDistribution.memSobolev\_zero\_iff\_exists\_fourier})},
  howpublished = {Lean 4 library, commit \texttt{0df444a} (21 August 2026)},
  year         = {2026}
}
```

* The two `\newtheorem` lines (top of this file). No new section label is
  required: `rem:usage` now references only `thm:conditional`,
  `prop:lowpressure`, `hyp:absorption`, `hyp:critical`, all of which exist
  in `main.tex`.
* The `\cite[p.~14]{Tao2013}` / `\cite[p.~15]{Tao2013}` calls of round 1 are
  gone; the block cites APDE pp. 35–36, verified against the published PDF in
  this round (see §3, F1). Any other lane citing Tao's notation section by
  page should use the same numbers.
* The abstract's phrase "the energy, scaling, interpolation, and enstrophy
  estimates" remains accurate.  The old statement of `prop:scaling`
  contained the sentence "they do not imply $u\in L^\infty(0,T;L^3)$"; it is
  now Remark `rem:mismatch`(a), with a proof (S-2).
* The constant $C$ in the old `eq:L4L3` and `eq:enstrophy` is now explicit
  ($3C_S^2$ and $C_E=\tfrac{2187}{32}C_S^6$).  `docs/proof-graph.yaml` and
  `docs/proof.md` quote these only as "$C$"; no change is forced there.
* Compile check of this round: see §5, EVIDENCE.

## 3. External facts used

| # | Fact, exactly as used | Primary source and location | Status |
|---|---|---|---|
| F1 | Conventions: $\hat f(\xi)=\int e^{-2\pi ix\cdot\xi}f(x)\,dx$ for $f\in L^1$, "extended to tempered distributions in the usual manner"; Euclidean tensor norms $\|u\|^2=u_iu_i$, $\|\nabla u\|^2=(\partial_iu_j)(\partial_iu_j)$, $\|\nabla^2u\|^2=(\partial_i\partial_ju_k)(\partial_i\partial_ju_k)$; classical $\|u\|_{H^k}$ for smooth $u$; Fourier norm $\|u\|_{H^s}=(\int(1+\|\xi\|^2)^s\|\hat u\|^2)^{1/2}$ for tempered distributions, "equivalent up to constants" to the classical one for integer $k$ | Tao, APDE 6 (2013) 25–107: **p. 35** (tensor norms; Fourier convention on $L^1_x(\mathbb R^3)$ and extension to tempered distributions), **p. 36** (classical $H^k$ norm for smooth $u$; Fourier $H^s$ norm; equivalence remark). Read in this round from the publisher PDF (`scratchpad/tao/apde-full.pdf`, PDF pages 12–13 = printed 35–36) via `helpy_pdf`. The arXiv v4 pages are 14–15. Nothing else (no Parseval, no derivative rule, no distributional $H^k$ characterisation) is attributed to Tao | [DI] |
| F2 | Sobolev inequality, $C^1_c$ form: $\|f\|_6\le C_S\|\nabla f\|_2$ for real $f\in C^1_c(\mathbb R^3)$ | (a) Nirenberg, Ann. Sc. Norm. Sup. Pisa (3) 13 (1959) 115–162, Lecture II, p. 125, Theorem with inequality (2.2): "Let $u$ belong to $L_q$ in $E^n$ and its derivatives of order $m$, $D^mu$, belong to $L_r$, $1\le q,r\le\infty$. For the derivatives $D^ju$, $0\le j<m$, … $\|D^ju\|_p\le\text{constant}\,\|D^mu\|_r^a\|u\|_q^{1-a}$, $\frac1p=\frac jn+a(\frac1r-\frac mn)+(1-a)\frac1q$, $\frac jm\le a\le1$", with two exceptional cases (neither applies for $n=3$, $j=0$, $m=1$, $r=q=2$, $a=1$, $p=6$); $\|D^ju\|_p$ there is the maximum of the $\|\cdot\|_p$ norms of the $j$-th order derivatives (reconciled in `def:sobolev-constant`). Nirenberg: "We shall not give a complete proof of the theorem here but shall indicate the main steps" (p. 125); "The proof of the theorem is elementary and contains in particular an elementary proof for the Sobolev case $a=1$" (p. 126). Read in round 1 from the numdam PDF; re-verified by the round-1 audit. (b) Mathlib `Mathlib/Analysis/FunctionalSpaces/SobolevInequality.lean`, `theorem eLpNorm_le_eLpNorm_fderiv_of_eq` (line 600; hypotheses `ContDiff ℝ 1 u`, `HasCompactSupport u`, `1 ≤ p`, `0 < finrank ℝ E`, `(p')⁻¹ = p⁻¹ − (finrank ℝ E)⁻¹`; conclusion `eLpNorm u p' μ ≤ SNormLESNormFDerivOfEqConst F μ p * eLpNorm (fderiv ℝ u) p μ`; ambient `[FiniteDimensional ℝ E] (μ : Measure E) [IsAddHaarMeasure μ]`, line 353), checkout `0df444a360` | (a) [DI] (proof in source is "the main steps"); (b) [DI] |
| F3 | Lemma `lem:fourier`(S): for Schwartz $f,h$: $\hat f\in\mathcal S$; $\widehat{\partial^\alpha f}=(2\pi i\xi)^\alpha\hat f$; $\partial^\alpha\hat f=((-2\pi ix)^\alpha f)^\wedge$; Parseval $\int f\bar h=\int\hat f\overline{\hat h}$; Plancherel $\|\hat f\|_2=\|f\|_2$; inversion $(\hat f)^\vee=f=(f^\vee)^\wedge$ | Grafakos, *Classical Fourier Analysis*, 3rd ed., GTM 249, Springer 2014: Definition 2.2.8 (p. 108, the convention $\hat f(\xi)=\int f(x)e^{-2\pi ix\cdot\xi}dx$); Proposition 2.2.11 (9), (10), (11) (pp. 109–110, with proofs by integration by parts / dominated convergence); Theorem 2.2.14 (2) Fourier inversion, (3) Parseval, (4) Plancherel (p. 112, with proof on pp. 112–113). Read in this round from the PDF (`scratchpad/graf.pdf`, PDF pages 125–130) via `helpy_pdf` | [DI] |
| F4 | Lemma `lem:fourier`(L): $f\mapsto\hat f$ is an $L^2$-isometry on $L^1\cap L^2$; unique continuous extension $\mathcal F$ to $L^2$; $\mathcal F$ isometric and bijective; $\mathcal Ff=\hat f$ a.e. on $L^1\cap L^2$; $\mathcal F^{-1}$ is the extension of $f\mapsto f^\vee$ and is an isometry | Grafakos §2.2.4, pp. 113–114 (statements in the text; the $L^1\cap L^2$ isometry is Exercise 2.2.8 with a complete hint, p. 117; "for $f$ in $L^1\cap L^2$ the expressions $\hat f$ and $\mathcal F(f)$ coincide pointwise a.e." p. 114; "$\mathcal F$ and $\mathcal F'$ are injective and surjective … $\mathcal F'$ coincides with the inverse operator $\mathcal F^{-1}$" p. 114). Mathlib `Mathlib/Analysis/Fourier/LpSpace.lean`: `MeasureTheory.Lp.fourierTransformₗᵢ : Lp F 2 ≃ₗᵢ[ℂ] Lp F 2` (line 50, defined by isometric extension from Schwartz functions), `MeasureTheory.Lp.norm_fourier_eq` (line 89), `MeasureTheory.Lp.inner_fourier_eq` (line 93), `SchwartzMap.toLp_fourier_eq` (line 99); convention `𝓕 f w = ∫ v, Complex.exp (↑(-2 * π * ⟪v, w⟫) * Complex.I) • f v` (`Analysis/Fourier/FourierTransform.lean:439`). Read in this round | Grafakos [DI] (with the exercise caveat); Mathlib [DI] |
| F5 | Definitions on $\mathcal S'$: distributional derivative $\langle\partial^\alpha u,f\rangle=(-1)^{\|\alpha\|}\langle u,\partial^\alpha f\rangle$; Fourier transform $\langle\hat u,f\rangle=\langle u,\hat f\rangle$, $\langle u^\vee,f\rangle=\langle u,f^\vee\rangle$; product with a smooth function of polynomial growth $\langle hu,f\rangle=\langle u,hf\rangle$; $L^p$ functions ($1\le p\le\infty$) are tempered distributions | Grafakos Definition 2.2.1 (p. 105), Remark 2.2.3 (p. 105), Definition 2.3.3 (p. 121), Examples 2.3.5 (4) (p. 122), Definitions 2.3.6, 2.3.7 (p. 123), Definition 2.3.15 (p. 125). Read in this round. (The consequences used — Proposition 2.3.22 (8) derivative rule and (10) inversion on $\mathcal S'$, p. 130 — are **proved** in the manuscript as `lem:duality`, since Grafakos' proof there is the sentence "All the statements can be proved easily using duality".) Mathlib cross-references: `TemperedDistribution.lineDerivOp_apply_apply : ∂_{m} f g = f (−∂_{m} g)` (`TemperedDistribution.lean:367`), `TemperedDistribution.fourier_apply : 𝓕 f g = f (𝓕 g)` (line 482), `TemperedDistribution.fourier_lineDerivOp_eq : 𝓕 (∂_{m} f) = (2πI) • smulLeftCLM F (inner ℝ · m) (𝓕 f)` (line 568), `MeasureTheory.Lp.fourier_toTemperedDistribution_eq : 𝓕 (f : 𝓢'(E,F)) = (𝓕 f : Lp F 2)` (`LpSpace.lean:120`), `TemperedDistribution.memSobolev_zero_iff_exists_fourier` (`Sobolev.lean:233`), `ae_eq_of_integral_contDiff_smul_eq` (`AEEqOfIntegralContDiff.lean:195`, the fundamental lemma proved here as `lem:compat`(ii)) | Grafakos [DI]; Mathlib [DI] |
| F6 | Hölder, Minkowski, Cauchy–Schwarz; Young's inequality $ab\le\frac{a^{p}}p+\frac{b^{q}}q$ for $a,b\ge0$, $\frac1p+\frac1q=1$, used with $p=4/3$, $q=4$ | Mathlib `Mathlib/Analysis/MeanInequalities.lean`: `Real.young_inequality_of_nonneg {a b p q : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) (hpq : p.HolderConjugate q) : a * b ≤ a ^ p / p + b ^ q / q` (line 500, namespace `Real` opened at line 497); Hölder for `eLpNorm`: `MeasureTheory.eLpNorm_smul_le_mul_eLpNorm … [HolderTriple p q r] : eLpNorm (φ • f) r μ ≤ eLpNorm φ p μ * eLpNorm f q μ` (`MeasureTheory/Function/LpSeminorm/CompareExp.lean:300`). Statements read in this round | [DI] |
| F7 | Measure theory: Fubini–Tonelli; dominated convergence; Fatou; an $L^2$-convergent sequence has an a.e.-convergent subsequence; Lebesgue measure scales by $\lambda^3$ under $x\mapsto\lambda x$ | Mathlib, statements read in this round at the cited lines: `MeasureTheory.integral_prod (f : α × β → E) (hf : Integrable f (μ.prod ν)) : ∫ z, f z ∂μ.prod ν = ∫ x, ∫ y, f (x, y) ∂ν ∂μ` (`MeasureTheory/Integral/Prod.lean:444`), `MeasureTheory.lintegral_prod` (`Measure/Prod.lean:1006`, Tonelli); `MeasureTheory.tendsto_integral_of_dominated_convergence` (`Integral/DominatedConvergence.lean:57`); `MeasureTheory.lintegral_liminf_le` (`Integral/Lebesgue/Add.lean:231`, Fatou); `MeasureTheory.tendstoInMeasure_of_tendsto_eLpNorm` (`Function/ConvergenceInMeasure.lean:464`) followed by `MeasureTheory.TendstoInMeasure.exists_seq_tendsto_ae'` (line 330); `NavierFormal.map_smul_volume : Measure.map (fun x => lam • x) volume = ENNReal.ofReal (lam ^ (−3)) • volume` (`navier-formal/NavierFormal/Scaling.lean:48`) | [DI] |
| F8 | Regularity package R: $u,p\in C^j([0,T];H^k)$ for all $j,k$; $u,p\in C^\infty([0,T]\times\mathbb R^3)$ solving `eq:NS` pointwise; $u(0)=u_0$; $u,\nabla u,\nabla^2u,\Delta u,u_t,p,\nabla p\in C([0,T];L^q)$, $2\le q\le\infty$, for every $T<T_*$ | `Proposition prop:localtheory` (local-theory lane, CP02), per controller decision D2; ultimately Tao 2013 Theorem 5.4(iv) + Corollary 5.8, quoted in `cp01-literature-statements.md` §1.2–1.3 | assumed (D2) |
| F9 | Lean cross-references in `rem:lean`/`rem:mismatch`: `NavierFormal.scalar_obstruction_exists` (`Ode.lean:134`), `NavierFormal.scalarObstruction` (`:34`), `NavierFormal.integral_scalarObstruction` (`:109`), `NavierFormal.exists_memLp_four_not_memLp_top` (`InterpolationMismatch.lean:114`; witness `scalingWitness t = t ^ (−(1:ℝ)/5)`, line 32), `NavierFormal.L4L3_supercritical : (2:ℝ)/4 + (3:ℝ)/3 = 3/2 ∧ (1:ℝ) < 3/2` (line 136 — proves only this arithmetic, not the exponent $-1/2$; the manuscript attribution is narrowed accordingly), `NavierFormal.eLpNorm_dilate` (`Scaling.lean:84`, hypotheses `p ≠ 0`, `p ≠ ∞`), `NavierFormal.eLpNorm_dilateSpaceTime` (`:125`) | `../navier-formal` HEAD `9c8b37d`, statements read in this round | [DI] |

No Calderón–Zygmund theory, no Riesz-transform $L^p$ bound, no heat
semigroup, no Littlewood–Paley theory, no Sobolev embedding into $L^\infty$
(taken from R), and no uniqueness theorem is used in this section.  The
identity $R_iR_j=-\Delta^{-1}\partial_i\partial_j$ under D1 is used only in
Remark `rem:scaling-pressure`, at the level of the $L^2$ multiplier symbol,
where it is stated with the symbol computation.

## 4. Obligations not discharged

* None of E-1, S-1, S-2, N-1 is left open, and the round-1 first bad bridge
  is closed: no fact is attributed to a location that does not contain it,
  every Fourier fact is either imported [DI] with exact location or proved,
  and every Mathlib name in the tables exists at the cited line of checkout
  `0df444a360`.
* Residual caveats on the *imports* (not on manuscript-owned proofs),
  recorded exactly:
  1. F2(a): Nirenberg's theorem on p. 125 is stated with a proof that the
     source itself describes as "the main steps" (pp. 125–127); its
     compactly supported $a=1$, $m=1$ case has a complete machine-checked
     proof in F2(b). Both are cited.
  2. F4: in Grafakos the isometry $\|\hat f\|_2=\|f\|_2$ on $L^1\cap L^2$
     is Exercise 2.2.8 (p. 117, with a complete hint reducing it to
     Exercises 2.2.7(b) and 2.2.6(b)); the extension to $L^2$, its
     bijectivity and the a.e. agreement on $L^1\cap L^2$ are stated in the
     text (pp. 113–114). Mathlib's `fourierTransformₗᵢ` (extension from
     Schwartz functions) is a complete formal proof of the $L^2$ isometry,
     but Mathlib does not state the a.e. agreement with the $L^1$ integral
     on $L^1\cap L^2$; that clause rests on Grafakos p. 114 alone. A
     textbook with a fully printed proof of the $L^1\cap L^2$ isometry
     (e.g. Stein–Weiss Ch. I Thm 2.1; Rudin RCA Thm 9.13, in a different
     normalisation) was not opened in this lane and is not cited.
  3. F8: the $L^q$ memberships for $q>2$ ($u\in L^3\cap L^4\cap L^\infty$;
     $p\in L^2$ suffices) are taken from the "hence" clause of D2 as part of
     R, not re-derived here; the $L^2$ memberships of all spatial
     derivatives are re-derived (`lem:classical`).
* Out of lane, noted for the integrator: the four `.bib` entries and the two
  `\newtheorem` lines above.

## 5. Frontier record

**MODE / RESULT.** PROOF WRITING, REPAIR ROUND; complete replacement text
for the manuscript's Sections 2 and 3 (energy, scaling, enstrophy, scalar
obstruction), discharging E-1, S-1, S-2, N-1 under the assumed regularity
package R, with the round-1 import defect repaired at the root: the
Fourier-analytic layer is now two labelled [DI] imports plus manuscript
proofs.

**CLAIM AND SCOPE.** On the unforced equation `eq:NS` on $\mathbb R^3$ with
$\nu>0$ and divergence-free Schwartz data, for the classical branch of
Proposition `prop:localtheory` and every $T<T_*$: the energy identity
`eq:energy` (all integrations by parts justified from R via
`lem:R-consequences`, `lem:div-zero`, `lem:classical`, `lem:plancherel`);
scaling invariance of `eq:NS` with $p_\lambda=\lambda^2p(\lambda\cdot,\lambda^2\cdot)$
and preservation of the normalised pressure; the norm identity for all
$1\le q\le\infty$; the Sobolev inequality on $H^1(\mathbb R^3)^m$ with
constant $\sqrt m\,C_S$ from the $C^1_c$ inequality by a written
density-plus-Fatou extension; $\|f\|_3\le\|f\|_2^{1/2}\|f\|_6^{1/2}$;
`eq:L4L3` with constant $3C_S^2$; the enstrophy identity and inequality
with $C_E=\frac{2187}{32}C_S^6$; the two facts of `rem:mismatch`. In
addition, the following general lemmas are proved from `lem:fourier`(S),(L)
and definitions only: `lem:parseval`, `lem:duality` ($\mathcal S'$
inversion and derivative rule), `lem:mollify`, `lem:compat` ($L^2$/$\mathcal S'$
compatibility, fundamental lemma for $L^2_{\rm loc}$), `lem:hk` ($H^k$ by
$L^2$ derivatives, with $\mathcal F(\partial^\alpha u)=(2\pi i\xi)^\alpha\mathcal Fu$
and the exact norm identities), `lem:classical`.

**EVIDENCE.** Every identity and exponent was rederived while writing
(polarisation identity of `lem:parseval`; the duality chain of
`lem:duality`(b) including the sign $(-1)^{|\alpha|}(-2\pi i x)^\alpha=(2\pi ix)^\alpha$;
the Fubini step $\widehat{\rho_\varepsilon*w}=\hat\rho_\varepsilon\hat w$;
the multinomial expansion in `lem:hk`; the conjugation sign in
`lem:plancherel`(iii); Hölder $4/3,4$; $\sqrt3C_S\cdot(3C_S)^{1/2}=3C_S^{3/2}$;
Young with $\delta^{4/3}=2\nu/3$ giving $\frac14(3/2\nu)^3\cdot81=\frac{2187}{32}\nu^{-3}$;
the scaling exponent $r(1-3/q)-2$). Primary sources read in this round:
Grafakos 3rd ed. pp. 105–107, 108–117, 119–131 (PDF via `helpy_pdf`);
Tao APDE pp. 35–36 (publisher PDF); Mathlib `0df444a360` files
`Analysis/Fourier/LpSpace.lean`, `Analysis/Fourier/FourierTransform.lean`,
`Analysis/Fourier/FourierTransformDeriv.lean` (namespace map confirming the
round-1 misnaming), `Analysis/Distribution/TemperedDistribution.lean`,
`Analysis/Distribution/Sobolev.lean`,
`Analysis/Distribution/AEEqOfIntegralContDiff.lean`,
`Analysis/MeanInequalities.lean`, `MeasureTheory/Integral/Prod.lean`,
`MeasureTheory/Integral/DominatedConvergence.lean`,
`MeasureTheory/Integral/Lebesgue/Add.lean`,
`MeasureTheory/Function/ConvergenceInMeasure.lean`,
`MeasureTheory/Function/LpSeminorm/CompareExp.lean`; navier-formal `9c8b37d`
`Ode.lean`, `InterpolationMismatch.lean`, `Scaling.lean`. Compile check
(`scratchpad/cp02r2/test.tex`): the block was spliced into a copy of
`main.tex` at HEAD `1ad73c2`, replacing `\section{Energy and scaling}`
through the paragraph before `\section{A signed critical balance}`, with
only the two `\newtheorem` lines, a stub
`\begin{proposition}\label{prop:localtheory}` after `premise:local`, and a
bibliography file consisting of `references.bib` plus the four entries
above; `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` all exit 0, 17 pages,
zero `!` errors, zero undefined references, zero undefined citations
(`grep` of `test.log`), nine `\bibitem`s in `test.bbl`, no overfull box
above 20pt. The only macro the block needed from the preamble beyond the
theorem environments is `\R`; `\mathbb C` is written out.

**FIRST GAP.** None within the lane's scope. The section is conditional
only on the assumed package R (D2), i.e. on `Proposition prop:localtheory`
from the local-theory lane; every statement here is unconditional given R.
The nearest external residue is the proof-status caveat on F4 (the
$L^1\cap L^2$ isometry is an exercise in the cited text; the $L^2$ isometry
itself is machine-checked in Mathlib).

**SURVIVING CONDITIONAL SUFFIX.** Not applicable to this lane: nothing here
is conditional on HIGH-PRESSURE, HIGH-STRAIN, ABSORPTION, or CRITICAL.
Downstream, `prop:energy` and `lem:sobolev` feed `prop:lowpressure`,
`thm:conditional`, and the existential-equivalence statement (X-1);
`prop:scaling`, `prop:enstrophy`, `prop:ode` feed nothing in the
conditional chain (Remark `rem:usage`). The Fourier lemmas
`lem:fourier`–`lem:classical` are general and available to the pressure and
low-pressure lanes (P-1, F-1) if they want a manuscript-internal source for
Parseval, the derivative rule, and $H^k$ memberships.

**NON-CLAIMS.** No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, or NS-R3 result is
asserted or approached. No bound on $\sup_{t<T_*}\|u(t)\|_3$ is deduced.
The value of $C_S$ is not asserted. The identification of
$(u_\lambda,p_\lambda)$ with the classical branch of the rescaled datum is
not asserted. Preserved Schwartz decay in time is not used. Sobolev
embedding $H^k\hookrightarrow L^\infty$ is not proved here; the $L^q$
memberships for $q>2$ are consumed from R as D2 states them.

**NEXT DISTINCT ACTION.** Integrator: splice the block into `main.tex`
(replacing old Sections 2–3), add the two `\newtheorem` lines and the four
`.bib` entries; run `research/verify.py`. Independent re-audit of this
round should start at `lem:compat`(ii) and `lem:classical`, the two lemmas
that carry the identification of classical with distributional
derivatives, and at the F4 caveat.
