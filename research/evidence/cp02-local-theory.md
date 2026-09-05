# CP02 lane 1: local theory (L-1, C-0 shape, C-3, P-1)

Status: REPAIR round 2 / paper-proof text for wave CP02, 2026-09-05. Owner of
this file only. Nothing here asserts HIGH-PRESSURE, HIGH-STRAIN, CRITICAL,
ABSORPTION, or NS-R3. Controller decisions D1–D5 are binding and are
implemented below; the regularity package R of (D2) is the conclusion of
`Proposition prop:localtheory`.

This version incorporates the round-1 audit
(`cp02-review-local-theory.md`, verdict REPAIR): the first bad bridge R1
(the `δ<0` half of the difference quotient in `lem:mild-classical`), the
scope repairs R2 (`lem:pressure-convention`(a) restated for arbitrary
`L^2` tensors) and R3 (`a.e.` → everywhere for almost-smooth competitors in
`prop:localtheory`(ii)), the bibliographic repair R4, and every item of the
audit's §5. Section 6 below lists each change against the audit item.

Sources actually opened for this lane (round 2): the **complete published
PDF** of Tao, *Anal. PDE* 6 (2013) 25–107 (downloaded from the publisher
via the DOI; journal page = PDF page + 24), read as page images for
pp. 25–26 (Definition 1.1, (1)–(4)), 28 ((8)–(9), footnote 4), 29 ((10)–(12)),
30 (Theorem 1.12, the Schwartz sentence), 31 (almost smooth solutions, the
`R^3` `H^1` mild solution), 35–39 (Fourier convention, both `H^k` norms,
`C^k_tX_x`, (13), (14), the heat kernel), 41–42 (symmetries, footnote 12),
46–48 (Lemma 4.1 proof end, Corollary 4.3, start of §5), 51–52
(Theorem 5.4), 55–57 (end of Proposition 5.6, the incomplete mild
definition, Corollary 5.8, Remark 5.9); Tao's arXiv:1108.1165 LaTeX source
(round 1) for the §11 corollary "Unconditional uniqueness" and its
following remark; the CP01 records `cp01-manuscript-obligations.md` and
`cp01-literature-statements.md`. Textbook facts (Plancherel, Gaussian
Fourier transform, convolution theorem, density and separability of `L^2`,
fundamental lemma) remain [MO].

## 1. Obligations discharged

| id | content | where |
|---|---|---|
| L-1 | `R^3` maximal development: definition of `T_*(ν,u_0)`, gluing/supremum, uniqueness class stated exactly (`H^1` mild, Definition `def:nu-mild`; plus almost-smooth classical solutions with any pressure via Corollary 4.3), `H^1` blow-up alternative, `ν`-normalisation of Tao's `ν=1` theory | `lem:nu-scaling`, `def:nu-mild`, `prop:localtheory` (i),(ii),(v),(vi) |
| L-1 (regularity part), (D2) package R | `∂_t^j u, ∂_t^j p ∈ L^∞_t H^k` for all `j,k` (Tao 5.4(iv)) ⟹ `u,p ∈ C^j([0,T];H^k)` for all `j,k`, `u,p ∈ C^∞([0,T]×R^3)` with bounded derivatives, `u(0)=u_0`, the equation holds pointwise, `L^q` continuity for `2≤q≤∞` | `lem:upgrade`, `lem:mild-classical`, `prop:localtheory` (iii),(iv), `cor:Lq` |
| C-0 (statement shape) | `sup = ess sup` on `[0,T_*)` because `t ↦ ‖u(t)‖_3` is continuous; the recommended statement of `thm:continuation` (`T_*<∞ ⟹ sup_{t<T_*}‖u(t)‖_3=∞`) with the ingredients the continuation lane needs from this lane (`H^1` blow-up alternative, `ν`-scaling) and the caution that (iii) is uniform only on compact `[0,T]`, `T<T_*` | `lem:sup-esssup`, `rem:continuation-shape` |
| C-3 | replacement for "Persistence in Tao's local theorem preserves smoothness for every finite time, including at `t=0`": if `T_*=∞` then `u,p ∈ C^∞(R^3×[0,∞))` in Fefferman's sense, `u(0)=u_0`, the equation holds, `p=R_iR_j(u_iu_j)` | `lem:global-smooth` and the replacement sentences in §2.3 |
| P-1 | `p = R_iR_j(u_iu_j) = -Δ^{-1}∂_i∂_j(u_iu_j)` (Tao's normalised pressure), symbol computation under (D1), the operator `P[w]=R_iR_jw_{ij}` is a contraction of `L^2` and of every `H^k`, `‖p‖_2 ≤ ‖u‖_∞‖u‖_2`, `-Δp = ∂_i∂_j(u_iu_j)` in `S'`, and `p(t)=R_iR_j(u_iu_j)(t)` for **every** `t` | `lem:pressure-convention`, `prop:localtheory` (iv) |
| E-1/N-1/P-2 inputs | exact memberships (`u ∈ C^1_t H^k`, `p ∈ C_t H^k`, all `k`) that the energy, enstrophy and pressure lanes were told to cite | `prop:localtheory` (iii), `cor:Lq` |

No hypothesis was added and no statement was weakened in this round. The
one statement made more precise is the uniqueness clause in the preamble
of `prop:localtheory`: the pair `(u,p)` is unique *among smooth pairs
satisfying (i)*, which is exactly what Step 8 proves and what the previous
wording meant.

Also recorded (D5): an exact list of what Tao's Theorem 5.4 does **not**
state (`rem:tao-scope`).

## 2. Replacement text

Integrator notes. (a) `main.tex` defines `theorem`, `proposition`,
`hypothesis`, `remark`. This text also uses `lemma`, `definition`, and
`corollary`; add

```latex
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{plain}
```

after the existing `\newtheorem` lines. (b) It uses `\mathcal S` for the
Schwartz class, `\langle\cdot,\cdot\rangle` for the real `L^2` inner
product, `\widehat{\ }` for the Fourier transform; no new macros are
required beyond `\R` and `\norm` already defined. (c) §2.1 replaces the
paragraph carrying `\label{premise:local}` in Section 1 of `main.tex`
(the label is kept on the paragraph). §2.2 is a new section to be placed
immediately after Section 1 (before "Energy and scaling"). §2.3 gives the
two replacements inside the proof of `thm:conditional` (two insertion
points, stated exactly there). Existing labels are untouched; all labels
introduced here are new. (d) **Label ownership.** This lane owns
`lem:embedding` and `lem:pressure-convention`. The current
`cp02-pressure.md` still defines `\label{lem:pressure-convention}` (its
own `lem:embedding` was already removed in its round-1 repair); splicing
both lanes verbatim would produce a multiply-defined label and two
lemmas with overlapping content. The pressure lane's copy must be deleted
or relabelled, and its regularity list `(R2)–(R3)` should cite
`Proposition prop:localtheory(iii)` and `Corollary cor:Lq`. Where the two
copies overlap they agree (same symbol computation, same `L^2` bound), so
only deduplication is needed. (e) Bibliography entries to add:
`SteinWeiss1971`, `Rudin1987` (see §3).

### 2.1 Replacement for the paragraph `premise:local` (Section 1)

```latex
\phantomsection\label{premise:local}
The local theory used throughout is Proposition~\ref{prop:localtheory} in
Section~\ref{sec:localtheory}.  For every $\nu>0$ and every such $u_0$ it
supplies a maximal time $T_*=T_*(\nu,u_0)\in(0,\infty]$ and a unique
classical branch $(u,p)$ on $[0,T_*)\times\R^3$, smooth up to and including
$t=0$, with $u,p\in C^j([0,T];H^k(\R^3))$ for all $j,k\geq0$ and all
$T<T_*$, with normalised pressure $p=R_iR_j(u_iu_j)$, unique within the
class of $H^1$ mild solutions (Definition~\ref{def:nu-mild}), and with
$\norm{u(t)}_{H^1}\to\infty$ as $t\uparrow T_*$ whenever $T_*<\infty$.
Everything is derived from Tao's Theorem~5.4 and Corollaries~4.3 and~5.8
\cite{Tao2013}, which are stated for unit viscosity, through the rescaling
of Lemma~\ref{lem:nu-scaling}.  From now on $u$, $p$, and $T_*$ denote this
branch and this time.  No decay of $u(t)$ beyond membership in every
$H^k(\R^3)$ is ever used: the Schwartz property of $u_0$ is not preserved
in time (Remark~\ref{rem:tao-scope}).
```

### 2.2 New section: local theory

```latex
\section{Local theory: the classical branch and its maximal time}
\label{sec:localtheory}

This section proves Proposition~\ref{prop:localtheory}, the only local
existence, uniqueness and regularity statement used in this paper.  The
imported results are Theorem~5.4, Corollary~4.3 and Corollary~5.8 of Tao
\cite{Tao2013}; they are transcribed in \S\ref{subsec:tao} together with
the definitions they depend on.  Everything else is proved here.

\subsection{Conventions and four elementary lemmas}
\label{subsec:conventions}

\paragraph{Fourier transform, Sobolev spaces, multipliers.}
For $f\in L^1(\R^3)$ we write
\[
 \widehat f(\xi)=\int_{\R^3}e^{-2\pi ix\cdot\xi}f(x)\,dx ,
\]
extended to tempered distributions in the usual way; this is Tao's
convention \cite[\S2, p.~35]{Tao2013}.  We use the
Plancherel theorem in the following form: the Fourier transform restricted
to $L^1\cap L^2$ extends uniquely to a unitary operator of $L^2(\R^3)$
onto itself, whose inverse on $L^1\cap L^2$ is $g\mapsto\int
g(\xi)e^{2\pi ix\cdot\xi}\,d\xi$; and for a tempered distribution $f$ and
a multi-index $\alpha$ one has $\widehat{\partial^\alpha f}(\xi)=(2\pi
i\xi)^\alpha\widehat f(\xi)$ \cite[Ch.~I]{SteinWeiss1971}.  All of this is
applied componentwise to $\R^N$-valued functions ($N=1$, $3$, or $9$
below): for $f\in L^2(\R^3;\R^N)$, $\widehat f(\xi)\in\mathbb C^N$ and
$|\widehat f(\xi)|$ denotes its Euclidean norm, so that
\[
 \norm f_{L^2}^2=\sum_{n=1}^N\norm{f_n}_{L^2}^2=\int_{\R^3}|\widehat f(\xi)|^2
 \,d\xi .
\]
For real vector-valued $f,g\in L^2(\R^3;\R^N)$ we write $\langle
f,g\rangle=\int f\cdot g\,dx$; Parseval's identity reads $\langle
f,g\rangle=\int\widehat f\cdot\overline{\widehat g}\,d\xi$ (the right side
is real because $\widehat f(-\xi)=\overline{\widehat f(\xi)}$).
For $s\in\R$ the Sobolev space $H^s=H^s(\R^3;\R^N)$ is the space of
tempered distributions $f$ with $\widehat f$ locally integrable and
\[
 \norm f_{H^s}:=\Big(\int_{\R^3}(1+|\xi|^2)^s|\widehat f(\xi)|^2\,d\xi
 \Big)^{1/2}<\infty ;
\]
this is Tao's $H^s_x(\R^3)$ \cite[\S2, p.~36]{Tao2013} (Tao also uses a
classical $H^k$ norm for smooth functions; see transcription note~(6)
after Theorem~\ref{thm:tao54}).  We also write, for $k\geq0$ and
$\phi\in L^2$,
\[
 \norm\phi_{H^{-k}}:=\norm{(1+|\xi|^2)^{-k/2}\widehat\phi}_{L^2}
 \leq\norm\phi_{L^2}.
\]
A Fourier multiplier with a bounded measurable symbol $m$ is the operator
$f\mapsto\mathcal F^{-1}(m\widehat f)$ on $L^2$, of operator norm
$\norm m_{L^\infty}$ on $L^2$ and on every $H^s$; two such multipliers
commute.

\paragraph{Smoothness on a closed slab.}
A function $F$ on $[0,T]\times\R^3$ (or on $[0,\infty)\times\R^3$) is
\emph{smooth} if all partial derivatives $\partial_t^j\partial_x^\alpha F$
of all orders exist on the closed set (one-sided in $t$ at $t=0$ and
$t=T$) and are continuous there.  This is the meaning of ``smooth
functions on $[0,T]\times\R^3$'' in Tao's Definition~1.1
\cite[p.~26]{Tao2013} and of ``$C^\infty(\R^3\times[0,\infty))$'' in
Fefferman's condition (6) \cite{Fefferman2000}.  A function
$g:[0,T]\to X$ into a Banach space is in $C^j([0,T];X)$ if it is $j$ times
continuously differentiable (one-sided at the endpoints); this is Tao's
$C^j_tX_x$ \cite[p.~37]{Tao2013}.  For $u\in L^\infty_tH^k_x([0,T]\times
\R^3)$ we follow Tao \cite[p.~37]{Tao2013}: $u$ is a Lebesgue measurable
function on $[0,T]\times\R^3$, $u(t)\in H^k$ for almost every $t$, and
$\operatorname{ess\,sup}_t\norm{u(t)}_{H^k}<\infty$.

\begin{lemma}[Integer Sobolev norms]\label{lem:sobolev-norms}
Let $k\geq0$ be an integer.  A tempered distribution $f$ (with values in
$\R^N$) belongs to $H^k$ if and only if $f\in L^2$ and the distributional
derivatives $\partial^\beta f$ belong to $L^2$ for all $|\beta|\leq k$,
and
\[
 \norm f_{H^k}^2=\sum_{|\beta|\leq k}c_{k,\beta}(2\pi)^{-2|\beta|}
 \norm{\partial^\beta f}_{L^2}^2,
 \qquad c_{k,\beta}=\binom{k}{|\beta|}\frac{|\beta|!}{\beta!}\geq1 .
\]
Moreover $\norm{\partial^\alpha f}_{H^{m}}\leq(2\pi)^{|\alpha|}
\norm f_{H^{m+|\alpha|}}$ for all $m\geq0$ and all $\alpha$.
\end{lemma}

\begin{proof}
By the binomial and multinomial theorems,
$(1+|\xi|^2)^k=\sum_{m=0}^k\binom km|\xi|^{2m}$ and
$|\xi|^{2m}=\sum_{|\beta|=m}\frac{m!}{\beta!}\xi^{2\beta}$, so
$(1+|\xi|^2)^k=\sum_{|\beta|\leq k}c_{k,\beta}\xi^{2\beta}$.  Multiply by
$|\widehat f|^2$, integrate, and use $\widehat{\partial^\beta
f}=(2\pi i\xi)^\beta\widehat f$ with Plancherel:
$\norm{\partial^\beta f}_{L^2}^2=(2\pi)^{2|\beta|}\int\xi^{2\beta}
|\widehat f|^2$.  Both directions of the equivalence follow, since every
coefficient is positive.  For the last claim,
$|(2\pi i\xi)^\alpha|^2\leq(2\pi)^{2|\alpha|}|\xi|^{2|\alpha|}\leq
(2\pi)^{2|\alpha|}(1+|\xi|^2)^{|\alpha|}$.
\end{proof}

\begin{lemma}[Sobolev embedding]\label{lem:embedding}
\begin{itemize}
\item[(a)] If $f\in H^2(\R^3;\R^N)$ then $\widehat f\in L^1$ with
$\norm{\widehat f}_{L^1}\leq\pi\norm f_{H^2}$, and $f$ agrees almost
everywhere with the bounded continuous function
$F(x)=\int\widehat f(\xi)e^{2\pi ix\cdot\xi}\,d\xi$, which satisfies
$\sup_x|F(x)|\leq\pi\norm f_{H^2}$.
\item[(b)] If $f\in H^m$ with $m\geq2$, the continuous representative $F$
of $f$ is $m-2$ times continuously differentiable, its classical
derivatives $\partial^\alpha F$ ($|\alpha|\leq m-2$) are the continuous
representatives of the distributional derivatives $\partial^\alpha f$, and
$\sup_x|\partial^\alpha F(x)|\leq\pi(2\pi)^{|\alpha|}\norm f_{H^m}$.
\item[(c)] If $f\in L^2\cap L^\infty$ then $\norm f_{L^q}\leq
\norm f_{L^2}^{2/q}\norm f_{L^\infty}^{1-2/q}$ for $2\leq q\leq\infty$.
\end{itemize}
\end{lemma}

\begin{proof}
(a) By Cauchy--Schwarz (with $|\widehat f|$ the Euclidean norm),
$\int|\widehat f|\leq(\int(1+|\xi|^2)^{-2}d\xi)^{1/2}
(\int(1+|\xi|^2)^{2}|\widehat f|^2d\xi)^{1/2}$, and in polar coordinates
$\int_{\R^3}(1+|\xi|^2)^{-2}d\xi=4\pi\int_0^\infty r^2(1+r^2)^{-2}dr
=4\pi\cdot\frac\pi4=\pi^2$ (substitute $r=\tan\theta$).  Thus
$\widehat f\in L^1\cap L^2$, so by the Plancherel theorem $f$ agrees a.e.\
with $F=\int\widehat f(\xi)e^{2\pi ix\cdot\xi}d\xi$; $F$ is continuous by
dominated convergence and $|F|\leq\norm{\widehat f}_{L^1}$.
(b) For $|\alpha|\leq m-3$ and $1\leq i\leq3$, $\partial^\alpha f\in
H^3$ by Lemma~\ref{lem:sobolev-norms}, hence $\int|\xi||\widehat{\partial^\alpha
f}|\,d\xi\leq\pi\norm{\partial^\alpha f}_{H^3}<\infty$ by the same
Cauchy--Schwarz step (since $|\xi|^2(1+|\xi|^2)^2\leq(1+|\xi|^2)^3$).
Differentiating $\int\widehat{\partial^\alpha f}(\xi)e^{2\pi
ix\cdot\xi}d\xi$ under the integral sign (dominated by
$2\pi|\xi||\widehat{\partial^\alpha f}|\in L^1$) shows that the continuous
representative of $\partial^\alpha f$ is $C^1$ with $\partial_i$-derivative
$\int(2\pi i\xi_i)\widehat{\partial^\alpha f}e^{2\pi ix\cdot\xi}d\xi$,
which is the continuous representative of $\partial^{\alpha+e_i}f$.
Induction on $|\alpha|$ gives the differentiability claim; the bound is (a)
applied to $\partial^\alpha f\in H^2$ with
Lemma~\ref{lem:sobolev-norms}.
(c) $\int|f|^q\leq\norm f_{L^\infty}^{q-2}\int|f|^2$.
\end{proof}

\begin{lemma}[Duality characterisation of $H^k$]\label{lem:duality}
Let $k\geq0$ and $g\in L^2(\R^3;\R^N)$.  Then $|\langle g,\phi\rangle|
\leq\norm g_{H^k}\norm\phi_{H^{-k}}$ for all $\phi\in L^2$ when
$g\in H^k$; and conversely, if $|\langle g,\phi\rangle|\leq
C\norm\phi_{H^{-k}}$ for all $\phi\in L^2$, then $g\in H^k$ and
$\norm g_{H^k}\leq C$.
\end{lemma}

\begin{proof}
The first claim is Parseval and Cauchy--Schwarz with the weights
$(1+|\xi|^2)^{\pm k/2}$.  For the converse let $R>0$ and define
$\phi_R\in L^2$ by $\widehat{\phi_R}=\mathbf 1_{\{|\xi|\leq R\}}
(1+|\xi|^2)^k\widehat g$; $\phi_R$ is real-valued because the multiplier is
real and even and $\widehat g(-\xi)=\overline{\widehat g(\xi)}$.  By
Parseval, $\langle g,\phi_R\rangle=\int_{|\xi|\leq R}(1+|\xi|^2)^k
|\widehat g|^2d\xi=:I_R$, while $\norm{\phi_R}_{H^{-k}}^2=I_R$.  The
hypothesis gives $I_R\leq CI_R^{1/2}$, so $I_R\leq C^2$; let
$R\to\infty$ (monotone convergence).
\end{proof}

\begin{lemma}[Heat semigroup on $L^2$]\label{lem:heat}
For $s\geq0$ let $e^{s\Delta}$ be the Fourier multiplier with symbol
$e^{-4\pi^2s|\xi|^2}$ on $L^2(\R^3;\R^N)$.  Then:
\begin{itemize}
\item[(K0)] for $g\in L^2$ and $s>0$, $e^{s\Delta}g=K_s*g$ with
$K_s(x)=(4\pi s)^{-3/2}e^{-|x|^2/4s}$; that is, $e^{s\Delta}$ coincides on
$L^2$ with the heat semigroup of Tao \cite[\S2, p.~39]{Tao2013}, which is
defined there by this kernel formula;
\item[(K1)] $e^{s\Delta}$ is self-adjoint on $L^2$, real-valued functions
go to real-valued functions, $\norm{e^{s\Delta}g}_{H^m}\leq\norm g_{H^m}$
for all $m\geq0$, and
$\langle g,e^{s\Delta}\Delta\psi\rangle=\langle\Delta g,e^{s\Delta}\psi
\rangle$ for $g,\psi\in H^2$;
\item[(K2)] for $g\in L^2$ the map $s\mapsto e^{s\Delta}g$ is continuous
from $[0,\infty)$ into $L^2$;
\item[(K3)] for $\psi\in H^2$ the map $s\mapsto e^{s\Delta}\psi$ is
$C^1$ from $[0,\infty)$ into $L^2$ (one-sided at $s=0$) with derivative
$e^{s\Delta}\Delta\psi$.
\end{itemize}
\end{lemma}

\begin{proof}
(K0) $K_s\in L^1$ with $\widehat{K_s}(\xi)=e^{-4\pi^2s|\xi|^2}$ (Fourier
transform of a Gaussian), and $\widehat{K_s*g}=\widehat{K_s}\,\widehat g$
for $K_s\in L^1$, $g\in L^2$ \cite[Ch.~I]{SteinWeiss1971}.
(K1) The symbol is real, even, and bounded by $1$; the last identity is
Parseval with $\widehat{\Delta\psi}=-4\pi^2|\xi|^2\widehat\psi$ and the
same for $g$.
(K2) $\norm{e^{s\Delta}g-e^{r\Delta}g}_{L^2}^2=\int|e^{-4\pi^2s|\xi|^2}
-e^{-4\pi^2r|\xi|^2}|^2|\widehat g|^2d\xi\to0$ as $r\to s$ by dominated
convergence (dominant $4|\widehat g|^2$).
(K3) Put $a=4\pi^2|\xi|^2$.  For $s\geq0$ and $h\neq0$ with $s+h\geq0$
and $|h|\leq\max(s,1)$, the Fourier transform of
$h^{-1}(e^{(s+h)\Delta}\psi-e^{s\Delta}\psi)-e^{s\Delta}\Delta\psi$ is
$e^{-as}\big(\frac{e^{-ah}-1}{h}+a\big)\widehat\psi$.  For $h>0$,
$\frac{e^{-ah}-1}{h}\in[-a,0]$, so the bracket lies in $[0,a]$.  For
$h<0$ (hence $s>0$, $|h|\leq s$), $0\leq\frac{e^{a|h|}-1}{|h|}\leq
ae^{a|h|}$ by the mean value theorem, so $e^{-as}|\frac{e^{-ah}-1}{h}+a|
\leq e^{-as}(ae^{a|h|}+a)\leq2a$.  In both cases the transform is
dominated by $2a|\widehat\psi|\in L^2$ (because $\psi\in H^2$) and tends
to $0$ pointwise as $h\to0$; dominated convergence gives the derivative.
Its continuity in $s$ is (K2) applied to $g=\Delta\psi\in L^2$.
\end{proof}

\subsection{The imported statements}\label{subsec:tao}

All statements in this subsection are Tao's, for unit viscosity, quoted
from \cite{Tao2013}.  His equation is
\begin{equation}\label{eq:tao-ns}
 \partial_tu+(u\cdot\nabla)u=\Delta u-\nabla p+f,\qquad\nabla\cdot u=0,
 \qquad u(0,x)=u_0(x),
\end{equation}
\cite[(3)--(5), pp.~26--27]{Tao2013}, and he normalises $\nu=1$
\cite[footnote~3, p.~27]{Tao2013}: ``The viscosity parameter $\nu$ was not
normalised in [Fefferman 2006] to equal $1$, as we are doing here, but one
can easily reduce to the $\nu=1$ case by a simple rescaling.''  No
rescaling formula is given there; ours is Lemma~\ref{lem:nu-scaling}.
We only ever use the homogeneous case $f=0$, but we transcribe the
statements with $f$ to keep them exact.

\begin{definition}[Tao's data classes {\cite[Definition~1.1, p.~26]{Tao2013}}]
\label{def:tao-data}
A \emph{smooth set of data} up to time $T$ is a triplet $(u_0,f,T)$ with
$0<T<\infty$, $u_0:\R^3\to\R^3$ smooth and divergence-free
($\nabla\cdot u_0=0$ is Tao's (1)), and $f:[0,T]\times\R^3\to\R^3$
smooth; it is \emph{homogeneous} if $f=0$.  It is \emph{$H^1$} if
$\mathcal H^1(u_0,f,T):=\norm{u_0}_{H^1_x(\R^3)}
+\norm f_{L^\infty_tH^1_x}<\infty$.  It is \emph{Schwartz} if, for all
integers $\alpha,m,k\geq0$,
\[
 \sup_{x\in\R^3}(1+|x|)^k|\nabla_x^\alpha u_0(x)|<\infty
 \quad\text{and}\quad
 \sup_{(t,x)\in[0,T]\times\R^3}(1+|x|)^k|\nabla_x^\alpha\partial_t^mf(t,x)|
 <\infty .
\]
(Tao also defines \emph{$H^1$ data} $(u_0,f,T)$ without smoothness: $u_0\in
H^1_x(\R^3)$ divergence-free, $f\in L^\infty_tH^1_x([0,T]\times\R^3)$,
$0<T<\infty$ \cite[p.~31]{Tao2013}.)  For $f=0$ the second display is
void, so $(u_0,0,T)$ is Schwartz data for every $0<T<\infty$ exactly when
$u_0$ is a divergence-free element of $\mathcal S(\R^3)^3$.
\end{definition}

\begin{definition}[Tao's solution classes {\cite[pp.~26--31]{Tao2013}}]
\label{def:tao-mild}
Throughout, $0<T<\infty$ and all fields are real-valued.
\begin{itemize}
\item[(a)] A \emph{smooth solution} is a quintuplet $(u,p,u_0,f,T)$ in
which $(u_0,f,T)$ is a smooth set of data and
\[
 u:[0,T]\times\R^3\to\R^3,\qquad p:[0,T]\times\R^3\to\R
\]
are smooth functions on $[0,T]\times\R^3$ obeying \eqref{eq:tao-ns} on all
of $[0,T]\times\R^3$ \cite[p.~26]{Tao2013}.  It is \emph{$H^1$} if the
data is $H^1$ and
\[
 \norm u_{L^\infty_tH^1_x([0,T]\times\R^3)}
 +\norm u_{L^2_tH^2_x([0,T]\times\R^3)}<\infty
\]
\cite[(7), p.~27]{Tao2013}.
\item[(b)] An \emph{almost smooth} solution is defined as a smooth one
except that $u,p$ are required to be smooth only on $(0,T]\times\R^3$,
while for each $k\geq0$ the functions $\nabla_x^ku$,
$\partial_t\nabla_x^ku$, $\nabla_x^kp$ exist and are continuous on
$[0,T]\times\R^3$ \cite[p.~31]{Tao2013}; the equation \eqref{eq:tao-ns} is
then still interpreted in the classical sense.  An \emph{almost smooth
$H^1$ solution} is an almost smooth solution satisfying the $H^1$
condition of (a).
\item[(c)] The \emph{normalised pressure} is
\begin{equation}\label{eq:tao-pressure}
 p=-\Delta^{-1}\partial_i\partial_j(u_iu_j)+\Delta^{-1}\nabla\cdot f
\end{equation}
\cite[(9), p.~28]{Tao2013}, where $\Delta^{-1}$ is the Fourier multiplier
$\widehat{\Delta^{-1}F}(\xi)=\frac{-1}{4\pi^2|\xi|^2}\widehat F(\xi)$,
``well-defined for any tempered distribution $F$ for which the right-hand
side is locally integrable'' \cite[(14), p.~38]{Tao2013}.
\item[(d)] An \emph{$H^1$ mild solution} $(u,p,u_0,f,T)$ consists of fields
$u,f:[0,T]\times\R^3\to\R^3$, $p:[0,T]\times\R^3\to\R$,
$u_0:\R^3\to\R^3$ with $0<T<\infty$, obeying
\[
 u_0\in H^1_x(\R^3),\qquad f\in L^\infty_tH^1_x([0,T]\times\R^3),\qquad
 u\in L^\infty_tH^1_x\cap L^2_tH^2_x([0,T]\times\R^3),
\]
with $p$ given by \eqref{eq:tao-pressure}, which obey $\nabla\cdot u=0$,
$\nabla\cdot u_0=0$, and the integral form
\begin{equation}\label{eq:tao-duhamel}
 u(t)=e^{t\Delta}u_0+\int_0^te^{(t-t')\Delta}
 \bigl(-(u\cdot\nabla)u-\nabla p+f\bigr)(t')\,dt'
\end{equation}
of \eqref{eq:tao-ns} \cite[p.~31]{Tao2013}; the integral form is Tao's
(10), displayed on p.~29 for the periodic setting and invoked verbatim for
$\R^3$ on p.~31.
\item[(e)] An \emph{incomplete mild $H^1$ solution} $(u,p,u_0,f,T_*^-)$
from $H^1$ data $(u_0,f,T_*)$ consists of fields $u:[0,T_*)\times\R^3\to
\R^3$ and $p:[0,T_*)\times\R^3\to\R$ such that for any $0<T<T_*$ the
restriction $(u,p,u_0,f,T)$ to the slab $[0,T]\times\R^3$ is a mild $H^1$
solution \cite[p.~56]{Tao2013}.
\end{itemize}
\end{definition}

Two remarks on (d).  First, uniqueness of $H^1$ mild solutions
(Theorem~\ref{thm:tao54}(iii)) is equality of $u$ almost everywhere on
$[0,T]\times\R^3$; $p$ is then determined by \eqref{eq:tao-pressure}.
Second, in this paper \eqref{eq:tao-duhamel} is only ever evaluated for
solutions whose integrand $t'\mapsto(-(u\cdot\nabla)u-\nabla p)(t')$ is
continuous into $L^2$ (Proposition~\ref{prop:localtheory}(iii)); for such
integrands the time integral is the Riemann integral of a continuous
$L^2$-valued function, which coincides with its value under any weaker
interpretation (Bochner integral in $H^{-1}$ or in $\mathcal S'$), because
the inclusions are bounded linear maps and bounded linear maps commute with
Riemann integrals.

\begin{theorem}[Tao {\cite[Theorem~5.4, pp.~52--53]{Tao2013}}]
\label{thm:tao54}
Let $(u_0,f,T)$ be $H^1$ data.
\begin{itemize}
\item[(i)] (Strong solution) If $(u,p,u_0,f,T)$ is an $H^1$ mild solution,
then $u\in C^0_tH^1_x([0,T]\times\R^3)$.
\item[(ii)] (Local existence and regularity) If
\[
 \bigl(\norm{u_0}_{H^1_x(\R^3)}+\norm f_{L^1_tH^1_x(\R^3)}\bigr)^4T\leq c
\]
for a sufficiently small absolute constant $c>0$, then there exists an
$H^1$ mild solution $(u,p,u_0,f,T)$ with the indicated data, with
$\norm u_{X^1([0,T]\times\R^3)}\lesssim\norm{u_0}_{H^1_x(\R^3)}+
\norm f_{L^1_tH^1_x(\R^3)}$ and more generally
$\norm u_{X^k([0,T]\times\R^3)}\leq C(k,\norm{u_0}_{H^k_x(\R^3)},
\norm f_{L^1_tH^k_x(\R^3)})$ for each $k\geq1$, where
$X^s=L^\infty_tH^s_x\cap L^2_tH^{s+1}_x$.  In particular, one has local
existence whenever $T$ is sufficiently small depending on
$\mathcal H^1(u_0,f,T)$.
\item[(iii)] (Uniqueness) There is at most one $H^1$ mild solution
$(u,p,u_0,f,T)$ with the indicated data.
\item[(iv)] (Regularity) If $(u,p,u_0,f,T)$ is an $H^1$ mild solution,
and $(u_0,f,T)$ is Schwartz, then $u$ and $p$ are smooth; in fact, one has
$\partial_t^ju,\partial_t^jp\in L^\infty_tH^k([0,T]\times\R^3)$ for all
$j,k\geq0$.
\end{itemize}
Part (v) (Lipschitz stability) is not used here and is omitted.
\end{theorem}

Transcription notes.  (1) The $X^k$ bound in (ii) is printed in both the
published and the preprint text as ``$\lesssim_{k,\norm{u_0}_{H^k_x},
\norm f_{L^1_tH^k_x},1}$'' with an empty right-hand side; the form given
above (a finite bound depending only on the indicated quantities) is the
evident intended meaning, and only the qualitative membership $u\in X^k$
is used below.  (2) Tao writes the tuples in (i) and (iv) with a spurious
sixth entry ``$,1$'' inherited from the periodic notation; it is omitted.
(3) $H^1$ data requires $f\in L^\infty_tH^1_x$ while (ii) uses
$\norm f_{L^1_tH^1_x}$; for $f=0$ both vanish.  (4) The space $X^s$ is
printed as $L^\infty_tH^s_x\cap L^2_xH^{s+1}_x$ in \cite[(13), p.~37]{Tao2013};
the second factor is $L^2_t$, as every use in that paper shows.
(5) ``Smooth'' in (iv) means smooth on the closed slab $[0,T]\times\R^3$
(Definition~\ref{def:tao-mild}(a)).  Lemma~\ref{lem:upgrade} below does
not depend on this closed-slab reading: it derives smoothness on the
closed slab from the assertion that the time derivatives $\partial_t^ju$
exist (as distributional derivatives which are functions) with the stated
$L^\infty_tH^k$ bounds, which is exactly the second half of (iv).
(6) Tao defines two norms called $H^k_x(\R^3)$ \cite[p.~36]{Tao2013}: the
classical norm $(\sum_{j\leq k}\norm{\nabla^ju}_{L^2}^2)^{1/2}$ for smooth
$u$, and the Fourier-side norm used in this paper; he notes that the
former ``conflicts slightly'' with the latter ``but the two norms are
equivalent up to constants''.  Lemma~\ref{lem:sobolev-norms} is this
equivalence with explicit constants, so the finiteness set is the same and
the membership $\partial_t^ju\in L^\infty_tH^k$ in (iv) is unambiguous.
Likewise Tao's displayed norm for $C^k_tX_x$ \cite[p.~37]{Tao2013} is
written with $\nabla^j$ where $\partial_t^j$ is meant; we use only the
defining clause ``$t\mapsto u(t)$ is $k$ times continuously
differentiable'', which is unaffected.

\begin{theorem}[Tao {\cite[Corollary~5.8, p.~56]{Tao2013}}]
\label{thm:tao58}
Let $(u_0,f,T)$ be $H^1$ data.  Then at least one of the following two
statements holds:
\begin{itemize}
\item There exists a mild $H^1$ solution $(u,p,u_0,f,T)$ with the given
data.
\item There exist a blowup time $0<T_*<T$ and an incomplete mild $H^1$
solution $(u,p,u_0,f,T_*^-)$ up to time $T_*^-$ that blows up in the
enstrophy norm in the sense that
$\lim_{t\to T_*^-}\norm{u(t)}_{H^1_x(\R^3)}=+\infty$.
\end{itemize}
\end{theorem}

\begin{theorem}[Tao {\cite[Corollary~4.3, p.~47]{Tao2013}}]\label{thm:tao43}
Let $(u,p,u_0,f,T)$ be an almost smooth $H^1$ solution.  Then
$(u,\tilde p,u_0,f,T)$ is a mild $H^1$ solution, where
$\tilde p(t,x):=-\Delta^{-1}\partial_i\partial_j(u_iu_j)(t,x)
+\Delta^{-1}\nabla\cdot f(t,x)$.  Furthermore, for almost every
$t\in[0,T]$, $p(t)$ and $\tilde p(t)$ differ by a constant (and thus
$\nabla p=\nabla\tilde p$).
\end{theorem}

\begin{remark}[What Theorem~\ref{thm:tao54} does not say]\label{rem:tao-scope}
\begin{itemize}
\item[(a)] It contains no maximal Cauchy development on $\R^3$.  Tao's
Corollary~5.2 is stated for the periodic case; Corollary~5.8
(Theorem~\ref{thm:tao58}) is a dichotomy for each fixed finite $T$.  The
passage from the per-$T$ dichotomy to a single maximal time
$T_*(u_0)\in(0,\infty]$ is the supremum-and-gluing argument of
Proposition~\ref{prop:localtheory}, Steps~1--4.
\item[(b)] Everything is for $\nu=1$; the reduction to $\nu=1$ is asserted
without a formula.  The reduction is Lemma~\ref{lem:nu-scaling}.
\item[(c)] (iv) asserts $\partial_t^ju\in L^\infty_tH^k$, not
$\partial_t^ju\in C^0_tH^k$; the upgrade is Lemma~\ref{lem:upgrade}.
\item[(d)] Nothing is said about $L^3$ or any critical norm; the
uniqueness in (iii) is uniqueness \emph{within the class of $H^1$ mild
solutions} (Definition~\ref{def:tao-mild}(d)).  The class matters: Tao's
Theorem~1.12 \cite[p.~30]{Tao2013} exhibits smooth $u_0\in H^1$ for which
no smooth finite energy solution exists for any $T>0$, and the remark
following his corollary ``Unconditional uniqueness'' \cite[\S11]{Tao2013}
conjectures, but does not prove, uniqueness for merely finite-energy data.
\item[(e)] The Schwartz property of the datum is not preserved:
``the incompressible nature of the fluid implies that the Schwartz
property need not be preserved over time'' \cite[p.~30]{Tao2013}; the
mechanism is recorded in \cite[\S3, footnote~12, p.~42]{Tao2013}, where
``time translation can instantly convert Schwartz data to non-Schwartz
data'' because moments such as $\int\omega_1(t,x)(x_2^2-x_3^2)\,dx$ are
not conserved but vanish whenever $u(t)$ is Schwartz.  Accordingly no
statement in this paper uses $u(t)\in\mathcal S$ for $t>0$; only
$u(t)\in H^k$ for all $k$ is available.
\end{itemize}
\end{remark}

\subsection{Restriction, regularity upgrade, and the classical equation}

\begin{lemma}[Restriction]\label{lem:restriction}
If $(u,p,u_0,0,T)$ is an $H^1$ mild solution and $0<T'<T$, then the
restrictions of $u,p$ to $[0,T']\times\R^3$ form an $H^1$ mild solution
$(u,p,u_0,0,T')$.  Consequently the restriction of an incomplete mild
$H^1$ solution $(u,p,u_0,0,T_*^-)$ to $[0,T']\times\R^3$, $T'<T_*$, is an
$H^1$ mild solution, and its restriction to $[0,T'')$, $T''\leq T_*$, is
an incomplete mild $H^1$ solution.
\end{lemma}

\begin{proof}
$(u_0,0,T')$ is $H^1$ data.  The memberships $u\in L^\infty_tH^1_x\cap
L^2_tH^2_x$ are inherited by restriction (an essential supremum over a
subset, an integral over a subset).  The conditions $\nabla\cdot u(t)=0$
and \eqref{eq:tao-pressure} are conditions at (almost) every fixed time.
The identity \eqref{eq:tao-duhamel} at a time $t\leq T'$ involves $u_0$
and the values of $u,p$ on $[0,t]\times\R^3$ only.  The second statement
is immediate from Definition~\ref{def:tao-mild}(e).
\end{proof}

\begin{lemma}[From $L^\infty_tH^k$ bounds to smoothness]\label{lem:upgrade}
Let $0<T<\infty$ and let $u:[0,T]\times\R^3\to\R^N$ be measurable.  Assume
that for every $j\geq0$ the $j$-th distributional time derivative of $u$
on $(0,T)\times\R^3$ is a measurable function $u^{(j)}$ (with
$u^{(0)}=u$) such that
\[
 M_{j,k}:=\norm{u^{(j)}}_{L^\infty_tH^k_x([0,T]\times\R^3)}<\infty
 \qquad\text{for all }j,k\geq0 .
\]
(If $u$ is smooth on $[0,T]\times\R^3$ with
$\partial_t^ju\in L^\infty_tH^k$ for all $j,k$, the classical derivatives
$u^{(j)}=\partial_t^ju$ satisfy this.)  Then there is a unique smooth
function $U$ on $[0,T]\times\R^3$ with $U=u$ almost everywhere, and $U$
has the following properties for all $j,k\geq0$ and all multi-indices
$\alpha$:
\begin{itemize}
\item[(a)] $\partial_t^jU(t)\in H^k$ with $\norm{\partial_t^jU(t)}_{H^k}
\leq M_{j,k}$ for every $t\in[0,T]$, and
$\norm{\partial_t^jU(t)-\partial_t^jU(s)}_{H^k}\leq M_{j+1,k}|t-s|$;
\item[(b)] $U\in C^j([0,T];H^k)$, the $H^k$-valued derivatives being the
classical $\partial_t^jU$;
\item[(c)] $\sup_{[0,T]\times\R^3}|\partial_t^j\partial_x^\alpha U|
\leq\pi(2\pi)^{|\alpha|}M_{j,|\alpha|+2}$; and
$\partial_t^j\partial_x^\alpha U(t,\cdot)$ is the continuous representative
of the distributional derivative $\partial_x^\alpha\partial_t^jU(t)$;
\item[(d)] $\partial_t^jU=u^{(j)}$ almost everywhere on $[0,T]\times\R^3$.
\end{itemize}
\end{lemma}

\begin{proof}
\emph{Step 1 (scalar pairings).}  Fix $\phi\in C_c^\infty(\R^3;\R^N)$ and
$j\geq0$.  Let $N_0\subset[0,T]$ be the null set of times $t$ at which
some $u^{(j)}(t)$ fails to lie in some $H^k$ or exceeds the bound
$M_{j,k}$ (a countable union of null sets).  For $t\notin N_0$ put
$a_j^\phi(t):=\langle u^{(j)}(t),\phi\rangle$; then $|a_j^\phi(t)|\leq
M_{j,k}\norm\phi_{H^{-k}}$ for every $k$ (Lemma~\ref{lem:duality}), and
$a_j^\phi$ is measurable by Fubini (the function $u^{(j)}\cdot\phi$ is
integrable on $[0,T]\times\R^3$ because $\int_0^T\int|u^{(j)}||\phi|
\leq TM_{j,0}\norm\phi_{L^2}$ by Tonelli and Cauchy--Schwarz).  Testing
the distributional identity $\partial_tu^{(j)}=u^{(j+1)}$ against
$\Phi(t,x)=\chi(t)\phi(x)$, $\chi\in C_c^\infty(0,T)$, and applying
Fubini gives
\begin{equation}\label{eq:weak-scalar}
 \int_0^Ta_j^\phi(t)\chi'(t)\,dt=-\int_0^Ta_{j+1}^\phi(t)\chi(t)\,dt .
\end{equation}
\emph{Claim:} if $a,b\in L^\infty(0,T)$ and $\int a\chi'=-\int b\chi$ for
all $\chi\in C_c^\infty(0,T)$, then there is $c\in\R$ with
$a(t)=c+\int_0^tb(\tau)d\tau$ for a.e.\ $t$.  Indeed $B(t):=\int_0^tb$
satisfies $\int_0^TB\chi'=\int_0^Tb(\tau)\int_\tau^T\chi'(t)\,dt\,d\tau
=-\int_0^Tb\chi$ (Fubini), so $d:=a-B$ satisfies $\int d\chi'=0$ for all
$\chi$.  Fix $\chi_0\in C_c^\infty(0,T)$ with $\int\chi_0=1$.  For any
$\eta\in C_c^\infty(0,T)$ the function $\chi(t):=\int_0^t(\eta-
(\int\eta)\chi_0)$ lies in $C_c^\infty(0,T)$ (its derivative has compact
support and integral zero), whence $0=\int d\chi'=\int d\eta-
(\int\eta)\int d\chi_0$; with $c:=\int d\chi_0$ this says
$\int(d-c)\eta=0$ for all $\eta$, so $d=c$ a.e.\ by the fundamental lemma
of the calculus of variations \cite[Ch.~7]{Rudin1987}.  Applying the claim
to \eqref{eq:weak-scalar}: there is a null set $N_{j,\phi}$ such that
\begin{equation}\label{eq:pair-fte}
 a_j^\phi(t)-a_j^\phi(s)=\int_s^ta_{j+1}^\phi(\tau)\,d\tau
 \qquad\text{for all }s,t\in[0,T]\setminus N_{j,\phi}.
\end{equation}

\emph{Step 2 (Lipschitz continuity in $H^k$ off a null set).}  Let
$D\subset C_c^\infty(\R^3;\R^N)$ be countable and dense in $L^2$
\cite[Ch.~3]{Rudin1987}, and $N:=N_0\cup\bigcup_{j,\phi\in D}N_{j,\phi}$,
a null set.  For $s,t\notin N$, $\phi\in D$, and every $k$,
\eqref{eq:pair-fte} and Lemma~\ref{lem:duality} give
$|\langle u^{(j)}(t)-u^{(j)}(s),\phi\rangle|\leq
M_{j+1,k}|t-s|\norm\phi_{H^{-k}}$.  Both sides are continuous in $\phi$
for the $L^2$ norm (recall $\norm\phi_{H^{-k}}\leq\norm\phi_{L^2}$), so
the inequality holds for all $\phi\in L^2$, and Lemma~\ref{lem:duality}
yields
\begin{equation}\label{eq:lip-offN}
 \norm{u^{(j)}(t)-u^{(j)}(s)}_{H^k}\leq M_{j+1,k}|t-s|
 \qquad(s,t\in[0,T]\setminus N,\ j,k\geq0).
\end{equation}

\emph{Step 3 (extension to all times).}  By \eqref{eq:lip-offN} with $k=0$,
$u^{(j)}$ is uniformly continuous from the dense set $[0,T]\setminus N$
into the complete space $L^2$, hence extends uniquely to a continuous map
$\tilde u^{(j)}:[0,T]\to L^2$.  For $t\in[0,T]$ choose $t_n\notin N$ with
$t_n\to t$; then for every $\phi\in L^2$, $|\langle\tilde u^{(j)}(t),\phi
\rangle|=\lim_n|\langle u^{(j)}(t_n),\phi\rangle|\leq M_{j,k}
\norm\phi_{H^{-k}}$, and likewise $|\langle\tilde u^{(j)}(t)-\tilde
u^{(j)}(s),\phi\rangle|\leq M_{j+1,k}|t-s|\norm\phi_{H^{-k}}$; by
Lemma~\ref{lem:duality}, $\tilde u^{(j)}(t)\in H^k$ with
$\norm{\tilde u^{(j)}(t)}_{H^k}\leq M_{j,k}$ and
$\norm{\tilde u^{(j)}(t)-\tilde u^{(j)}(s)}_{H^k}\leq M_{j+1,k}|t-s|$ for
all $s,t\in[0,T]$.  Moreover, for $\phi\in D$ and $s,t\notin N$ the
integrand in \eqref{eq:pair-fte} equals $\langle\tilde u^{(j+1)}(\tau),
\phi\rangle$ for $\tau\notin N$, i.e.\ almost everywhere; since both sides
of the resulting identity are continuous in $(s,t)$, we get
\begin{equation}\label{eq:pair-fte-all}
 \langle\tilde u^{(j)}(t)-\tilde u^{(j)}(s),\phi\rangle
 =\int_s^t\langle\tilde u^{(j+1)}(\tau),\phi\rangle\,d\tau
 \qquad\text{for all }s,t\in[0,T],\ \phi\in D .
\end{equation}

\emph{Step 4 ($H^k$-differentiability).}  Fix $j,k$, $t\in[0,T]$, and
$h\neq0$ with $t+h\in[0,T]$.  By \eqref{eq:pair-fte-all}, for $\phi\in D$,
\[
 \Bigl\langle\frac{\tilde u^{(j)}(t+h)-\tilde u^{(j)}(t)}{h}
 -\tilde u^{(j+1)}(t),\phi\Bigr\rangle
 =\frac1h\int_t^{t+h}\langle\tilde u^{(j+1)}(\tau)-\tilde u^{(j+1)}(t),
 \phi\rangle\,d\tau ,
\]
whose absolute value is at most $\sup_{|\tau-t|\leq|h|}\norm{\tilde
u^{(j+1)}(\tau)-\tilde u^{(j+1)}(t)}_{H^k}\norm\phi_{H^{-k}}\leq
M_{j+2,k}|h|\norm\phi_{H^{-k}}$ by Step~3.  Extending to $\phi\in L^2$ by
density and applying Lemma~\ref{lem:duality}, the $H^k$ norm of the
bracket is at most $M_{j+2,k}|h|\to0$.  Hence $\tilde u^{(j)}$ is
differentiable into $H^k$ with derivative $\tilde u^{(j+1)}$, which is
Lipschitz into $H^k$ by Step~3; so $\tilde u^{(j)}\in C^1([0,T];H^k)$ for
all $j,k$, and by induction $\tilde u:=\tilde u^{(0)}\in C^j([0,T];H^k)$
with $j$-th derivative $\tilde u^{(j)}$.

\emph{Step 5 (joint smoothness).}  For $j\geq0$ and a multi-index $\alpha$
let $U_{j,\alpha}(t,\cdot)$ be the continuous representative
(Lemma~\ref{lem:embedding}) of $\partial_x^\alpha\tilde u^{(j)}(t)\in
H^{2}$, and set $U:=U_{0,0}$.  By Lemma~\ref{lem:embedding}(a) and
Lemma~\ref{lem:sobolev-norms},
\begin{gather*}
 \sup_x|U_{j,\alpha}(t,x)|\leq\pi(2\pi)^{|\alpha|}
 \norm{\tilde u^{(j)}(t)}_{H^{|\alpha|+2}}\leq\pi(2\pi)^{|\alpha|}
 M_{j,|\alpha|+2},\\
 \sup_x|U_{j,\alpha}(t,x)-U_{j,\alpha}(s,x)|\leq\pi(2\pi)^{|\alpha|}
 M_{j+1,|\alpha|+2}|t-s|.
\end{gather*}
Each $U_{j,\alpha}$ is jointly continuous, because $|U_{j,\alpha}(t,x)-
U_{j,\alpha}(s,y)|\leq\sup_z|U_{j,\alpha}(t,z)-U_{j,\alpha}(s,z)|
+|U_{j,\alpha}(s,x)-U_{j,\alpha}(s,y)|$.  By Lemma~\ref{lem:embedding}(b)
(applied with $m=|\alpha|+3$), $U_{j,\alpha}(t,\cdot)$ is $C^1$ in $x$
with $\partial_{x_i}U_{j,\alpha}=U_{j,\alpha+e_i}$.  In $t$: by Step~4 the
difference quotient $h^{-1}(\tilde u^{(j)}(t+h)-\tilde u^{(j)}(t))-\tilde
u^{(j+1)}(t)$ tends to $0$ in $H^{|\alpha|+2}$, so by
Lemma~\ref{lem:embedding} and Lemma~\ref{lem:sobolev-norms}
\[
 \sup_x\bigl|h^{-1}(U_{j,\alpha}(t+h,x)-U_{j,\alpha}(t,x))
 -U_{j+1,\alpha}(t,x)\bigr|\to0 ;
\]
thus $\partial_tU_{j,\alpha}=U_{j+1,\alpha}$ (one-sided at the
endpoints).  By induction on $j+|\alpha|$ all partial derivatives of $U$
of all orders exist, are continuous, and equal
$\partial_t^j\partial_x^\alpha U=U_{j,\alpha}$; so $U$ is smooth on
$[0,T]\times\R^3$, and (a), (b), (c) follow from Steps~3--5.  Finally, for
$t\notin N$, $U_{j,0}(t)=\tilde u^{(j)}(t)=u^{(j)}(t)$ in $L^2$, so
$\partial_t^jU=u^{(j)}$ a.e.\ on $([0,T]\setminus N)\times\R^3$, hence a.e.\
on $[0,T]\times\R^3$ (Tonelli); this is (d), and uniqueness of $U$ holds
because two continuous functions that agree a.e.\ agree everywhere.
\end{proof}

\begin{lemma}[Mild solutions with this regularity are classical]
\label{lem:mild-classical}
Let $(u,p,u_0,0,T)$ be an $H^1$ mild solution (Definition~\ref{def:tao-mild}(d))
such that $u$ and $p$ have representatives, again denoted $u,p$, with
$u\in C^1([0,T];L^2)\cap C([0,T];H^2)$ and $p\in C([0,T];H^1)$.  Then
$u(0)=u_0$, and
\[
 \partial_tu+(u\cdot\nabla)u+\nabla p=\Delta u\qquad\text{in }L^2(\R^3)
 \text{ for every }t\in[0,T],
\]
where $\partial_tu$ is the $L^2$-valued derivative.  If moreover $u,p$ are
smooth on $[0,T]\times\R^3$, the equation and $u(0,x)=u_0(x)$ hold
pointwise on $[0,T]\times\R^3$.
\end{lemma}

\begin{proof}
Put $F:=-(u\cdot\nabla)u-\nabla p$ and $G:=\partial_tu-\Delta u$.  Both
lie in $C([0,T];L^2)$: $\nabla p\in C_tL^2$ since $p\in C_tH^1$;
$\Delta u\in C_tL^2$ since $u\in C_tH^2$; and, writing
$(u\cdot\nabla)u=u_j\partial_ju$,
\[
 \norm{u_j\partial_ju(t)-u_j\partial_ju(s)}_{L^2}\leq
 \norm{u(t)-u(s)}_{L^\infty}\norm{\nabla u(t)}_{L^2}
 +\norm{u(s)}_{L^\infty}\norm{\nabla u(t)-\nabla u(s)}_{L^2}\to0
\]
by Lemma~\ref{lem:embedding}(a) and Lemma~\ref{lem:sobolev-norms}.  In
particular the integrand of \eqref{eq:tao-duhamel} is continuous into
$L^2$ (Lemma~\ref{lem:heat}(K1),(K2)) and the integral is a Riemann
integral in $L^2$.

\emph{Mild representation.}  Fix $\phi\in H^2$ and $t\in[0,T]$ at which
\eqref{eq:tao-duhamel} holds.  Pairing with $\phi$, commuting the bounded
functional $\langle\cdot,\phi\rangle$ with the Riemann integral, and using
self-adjointness (K1),
\begin{equation}\label{eq:mild-paired}
 \langle u(t),\phi\rangle=\langle u_0,e^{t\Delta}\phi\rangle
 +\int_0^t\langle F(t'),e^{(t-t')\Delta}\phi\rangle\,dt' .
\end{equation}
Both sides are continuous in $t$ (the left by $u\in C_tL^2$, the right by
(K2) and the continuity of the integrand), so \eqref{eq:mild-paired} holds
for every $t\in[0,T]$ even if \eqref{eq:tao-duhamel} was given only for
almost every $t$.

\emph{Classical representation.}  For fixed $t$ and $t'\in[0,t]$ put
$a(t'):=\langle u(t'),e^{(t-t')\Delta}\phi\rangle$.  Both factors are
$C^1$ into $L^2$ (by hypothesis and (K3)), so $a\in C^1([0,t])$ with
\[
 a'(t')=\langle\partial_tu(t'),e^{(t-t')\Delta}\phi\rangle
 -\langle u(t'),e^{(t-t')\Delta}\Delta\phi\rangle
 =\langle G(t'),e^{(t-t')\Delta}\phi\rangle
\]
by (K1) (with $g=u(t')\in H^2$).  Integrating from $0$ to $t$,
\begin{equation}\label{eq:classical-paired}
 \langle u(t),\phi\rangle=\langle u(0),e^{t\Delta}\phi\rangle
 +\int_0^t\langle G(t'),e^{(t-t')\Delta}\phi\rangle\,dt' .
\end{equation}

\emph{Initial value.}  Subtracting \eqref{eq:mild-paired} from
\eqref{eq:classical-paired} and writing $H:=G-F\in C([0,T];L^2)$,
\begin{equation}\label{eq:difference}
 \langle u(0)-u_0,e^{t\Delta}\phi\rangle
 =-\int_0^t\langle H(t'),e^{(t-t')\Delta}\phi\rangle\,dt'
 \qquad(t\in[0,T],\ \phi\in H^2).
\end{equation}
The right side is bounded by $t\max_{[0,T]}\norm H_{L^2}\norm\phi_{L^2}$
and the left side tends to $\langle u(0)-u_0,\phi\rangle$ as $t\to0$
(K2).  Hence $\langle u(0)-u_0,\phi\rangle=0$ for all $\phi\in H^2\supset
C_c^\infty$, so $u(0)=u_0$ in $L^2$ by density of $C_c^\infty$ in $L^2$.

\emph{The equation.}  With $u(0)=u_0$, \eqref{eq:difference} says
$m_\phi(t):=\int_0^th_\phi(t',t)\,dt'=0$ for all $t\in[0,T]$ and all
$\phi\in H^2$, where $h_\phi(t',t):=\langle H(t'),e^{(t-t')\Delta}\phi
\rangle$ is defined on the closed triangle $\Sigma:=\{(t',t):0\leq t'\leq
t\leq T\}$ (and nowhere else: the heat semigroup is defined for
nonnegative times only).  Now let $\psi\in H^4$, so that $\Delta\psi\in
H^2$.  The function $h_\psi$ is continuous on $\Sigma$ (by $H\in C_tL^2$
and (K2)), and by (K3) it has on $\Sigma$ the continuous partial
derivative $\partial_th_\psi(t',t)=\langle H(t'),e^{(t-t')\Delta}\Delta
\psi\rangle=h_{\Delta\psi}(t',t)$ (one-sided at $t'=t$); both $h_\psi$
and $\partial_th_\psi$ are uniformly continuous on the compact set
$\Sigma$.  We claim that $m_\psi\in C^1([0,T])$ with
\begin{equation}\label{eq:m-derivative}
 m_\psi'(t)=h_\psi(t,t)+\int_0^t\partial_th_\psi(t',t)\,dt'
 =\langle H(t),\psi\rangle+m_{\Delta\psi}(t)
 \qquad(t\in[0,T]),
\end{equation}
one-sided at the endpoints.  Fix $t\in[0,T]$.  For $0<\delta\leq T-t$,
\[
 \frac{m_\psi(t+\delta)-m_\psi(t)}{\delta}
 =\frac1\delta\int_t^{t+\delta}h_\psi(t',t+\delta)\,dt'
 +\int_0^t\frac{h_\psi(t',t+\delta)-h_\psi(t',t)}{\delta}\,dt' ,
\]
in which every value of $h_\psi$ that occurs has $t'\leq t+\delta$, so all
terms are defined.  The first term tends to $h_\psi(t,t)$ by continuity of
$h_\psi$ at $(t,t)$.  In the second, for each $t'\leq t$ the function
$\tau\mapsto h_\psi(t',\tau)$ is $C^1$ on $[t,t+\delta]\subset[t',T]$, so
the mean value theorem gives a $\theta=\theta(t',\delta)\in(0,1)$ with
$(h_\psi(t',t+\delta)-h_\psi(t',t))/\delta=\partial_th_\psi(t',t+\theta
\delta)$; this converges to $\partial_th_\psi(t',t)$ uniformly in $t'$ as
$\delta\downarrow0$ by uniform continuity of $\partial_th_\psi$ on
$\Sigma$.  Hence the right derivative of $m_\psi$ at $t<T$ exists and
equals $h_\psi(t,t)+\int_0^t\partial_th_\psi(t',t)\,dt'$.  For
$-t\leq\delta<0$ the corresponding decomposition is
\[
 \frac{m_\psi(t+\delta)-m_\psi(t)}{\delta}
 =\int_0^{t+\delta}\frac{h_\psi(t',t+\delta)-h_\psi(t',t)}{\delta}\,dt'
 +\frac1{|\delta|}\int_{t+\delta}^{t}h_\psi(t',t)\,dt' ,
\]
in which every value of $h_\psi$ that occurs has $t'\leq t+\delta$ (first
integral) or $t'\leq t$ (second integral), so again all terms are defined.
The second term tends to $h_\psi(t,t)$ by continuity of $h_\psi$ at
$(t,t)$.  In the first, for each $t'\leq t+\delta$ the function
$\tau\mapsto h_\psi(t',\tau)$ is $C^1$ on $[t+\delta,t]\subset[t',T]$, so
the mean value theorem gives a $\theta\in(0,1)$ with
$(h_\psi(t',t+\delta)-h_\psi(t',t))/\delta=\partial_th_\psi(t',t+\theta
\delta)$, legitimate because $t'\leq t+\delta\leq t+\theta\delta\leq t$;
this converges to $\partial_th_\psi(t',t)$ uniformly in $t'\in[0,t+\delta]$
as $\delta\uparrow0$ by uniform continuity of $\partial_th_\psi$ on
$\Sigma$, and the missing slice $\int_{t+\delta}^t\partial_th_\psi(t',t)
\,dt'$ tends to $0$ because $\partial_th_\psi$ is bounded on $\Sigma$.
Hence the left derivative of $m_\psi$ at $t>0$ exists and equals
$h_\psi(t,t)+\int_0^t\partial_th_\psi(t',t)\,dt'$, the same value as the
right derivative.  So $m_\psi$ is differentiable on $[0,T]$ (one-sided at
$t=0$ and $t=T$) with the derivative \eqref{eq:m-derivative}, which is
continuous in $t$ by the continuity of $h_\psi$ and $\partial_th_\psi$ on
$\Sigma$; the second equality in \eqref{eq:m-derivative} is
$h_\psi(t,t)=\langle H(t),\psi\rangle$ ($e^{0\Delta}$ is the identity) and
$\partial_th_\psi=h_{\Delta\psi}$.  Since $m_\psi\equiv0$ and
$m_{\Delta\psi}\equiv0$ (the latter is the case $\phi=\Delta\psi\in H^2$
of \eqref{eq:difference}), \eqref{eq:m-derivative} yields $\langle H(t),
\psi\rangle=0$ for all $t\in[0,T]$ and all $\psi\in H^4\supset
C_c^\infty$; hence $H(t)=0$ in $L^2$, that is $\partial_tu-\Delta u=
-(u\cdot\nabla)u-\nabla p$ in $L^2$ for every $t\in[0,T]$.  If $u,p$ are
smooth, the $L^2$-valued derivative $\partial_tu(t)$ coincides with the
classical one (Lemma~\ref{lem:upgrade}(b) applied to $u$; or directly,
since both are the $L^2$-limit of the same difference quotients), every
term is continuous in $x$, and an identity in $L^2$ between continuous
functions holds pointwise; likewise $u(0,\cdot)=u_0$ pointwise, $u_0$
being continuous.
\end{proof}

\subsection{The pressure convention}

\begin{lemma}[Normalised pressure]\label{lem:pressure-convention}
Define the Riesz transforms $R_j$ ($j=1,2,3$) as the Fourier multipliers
with symbols $-i\xi_j/|\xi|$, and for $w\in L^2(\R^3;\R^{3\times3})$ put
\[
 P[w]:=\sum_{i,j=1}^3R_iR_jw_{ij},\qquad\text{i.e.}\qquad
 \widehat{P[w]}(\xi)=-\sum_{i,j}\frac{\xi_i\xi_j}{|\xi|^2}\,
 \widehat{w_{ij}}(\xi)\quad(\xi\neq0).
\]
For $u\in L^2\cap L^\infty(\R^3;\R^3)$, so that $u_iu_j\in L^1\cap L^2$,
set $p:=P[u\otimes u]=R_iR_j(u_iu_j)$ (summation over $i,j$).  Then:
\begin{itemize}
\item[(a)] For every $w\in L^2(\R^3;\R^{3\times3})$, $P[w]\in L^2$ with
$\norm{P[w]}_{L^2}\leq\norm w_{L^2}$, and $\norm{P[w]}_{H^k}\leq
\norm w_{H^k}$ whenever $w\in H^k$, $k\geq0$.  In particular
$p\in L^2$ with $\norm p_{L^2}\leq\norm{u\otimes u}_{L^2}\leq
\norm u_{L^\infty}\norm u_{L^2}$.
\item[(b)] $p=-\Delta^{-1}\partial_i\partial_j(u_iu_j)$, Tao's normalised
pressure \eqref{eq:tao-pressure} with $f=0$, and the right-hand side of
Tao's definition (14) is locally integrable for this argument, so the two
definitions produce the same $L^2$ function;
\item[(c)] $-\Delta p=\partial_i\partial_j(u_iu_j)$ in the sense of
tempered distributions;
\item[(d)] if in addition $u\in H^k$ for every $k$, then $u\otimes u\in
H^k$ for every $k$, hence $p\in H^k$ with $\norm p_{H^k}\leq
\norm{u\otimes u}_{H^k}$ for every $k$.
\end{itemize}
\end{lemma}

\begin{proof}
(a) Cauchy--Schwarz in the indices gives, for $\xi\neq0$,
\[
 |\widehat{P[w]}(\xi)|\leq\sum_{i,j}\frac{|\xi_i||\xi_j|}{|\xi|^2}
 |\widehat{w_{ij}}(\xi)|
 \leq\Bigl(\sum_{i,j}\frac{\xi_i^2\xi_j^2}{|\xi|^4}\Bigr)^{1/2}
 \Bigl(\sum_{i,j}|\widehat{w_{ij}}(\xi)|^2\Bigr)^{1/2}=|\widehat w(\xi)|,
\]
since $\sum_{i,j}\xi_i^2\xi_j^2=(\sum_i\xi_i^2)(\sum_j\xi_j^2)=|\xi|^4$.
Multiplying the square of this pointwise bound by $(1+|\xi|^2)^k$ and
integrating gives $\norm{P[w]}_{H^k}\leq\norm w_{H^k}$ for every $k\geq0$,
the case $k=0$ being the $L^2$ bound (Plancherel).  For $w=u\otimes u$,
$|u\otimes u|=(\sum_{i,j}u_i^2u_j^2)^{1/2}=|u|^2$, so $\norm{u\otimes u}
_{L^2}=\norm{|u|^2}_{L^2}\leq\norm u_{L^\infty}\norm u_{L^2}$.
(b) With $\widehat{\partial_i\partial_jF}=(2\pi i\xi_i)(2\pi i\xi_j)
\widehat F=-4\pi^2\xi_i\xi_j\widehat F$ and Tao's
$\widehat{\Delta^{-1}F}=-(4\pi^2|\xi|^2)^{-1}\widehat F$,
\[
 \widehat{-\Delta^{-1}\partial_i\partial_j(u_iu_j)}(\xi)
 =-\Bigl(\frac{-1}{4\pi^2|\xi|^2}\Bigr)(-4\pi^2\xi_i\xi_j)\,
 \widehat{u_iu_j}(\xi)
 =-\frac{\xi_i\xi_j}{|\xi|^2}\,\widehat{u_iu_j}(\xi)
 =\Bigl(\frac{-i\xi_i}{|\xi|}\Bigr)\Bigl(\frac{-i\xi_j}{|\xi|}\Bigr)
 \widehat{u_iu_j}(\xi),
\]
which is the symbol of $R_iR_j$.  The function
$\xi\mapsto\frac{\xi_i\xi_j}{|\xi|^2}\widehat{u_iu_j}(\xi)$ is bounded by
$\norm{u_iu_j}_{L^1}$, hence locally integrable, so Tao's (14) applies,
and both sides are the same element of $L^2$.  (c)
$\widehat{-\Delta p}=4\pi^2|\xi|^2\widehat p=-4\pi^2\xi_i\xi_j
\widehat{u_iu_j}=\widehat{\partial_i\partial_j(u_iu_j)}$.  (d) By
Lemma~\ref{lem:embedding}, $u$ and all its derivatives are bounded, so by
the Leibniz rule $\norm{\partial^\alpha(u_iu_j)}_{L^2}\leq\sum_{\beta\leq
\alpha}\binom\alpha\beta\norm{\partial^\beta u_i}_{L^\infty}
\norm{\partial^{\alpha-\beta}u_j}_{L^2}<\infty$; thus $u_iu_j\in H^k$ for
every $k$ by Lemma~\ref{lem:sobolev-norms}, and (a) applies with
$w=u\otimes u$.
\end{proof}

Thus the pressure $p=R_iR_j(u_iu_j)$ used throughout this paper is
literally Tao's normalised pressure, and $-\Delta p=\partial_i\partial_j
(u_iu_j)$.  Adding a function of time to $p$ would leave the Navier--Stokes
equation invariant; the normalisation removes this freedom, and no other
pressure is used anywhere below.

\subsection{Viscosity normalisation}

\begin{lemma}[$\nu$-normalisation]\label{lem:nu-scaling}
Let $\nu>0$ and $0<T\leq\infty$.  For functions $u:[0,T)\times\R^3\to\R^3$,
$p:[0,T)\times\R^3\to\R$ and $u_0:\R^3\to\R^3$ define
\begin{equation}\label{eq:nu-map}
 v(s,x):=\nu^{-1}u(s/\nu,x),\qquad q(s,x):=\nu^{-2}p(s/\nu,x),
 \qquad v_0(x):=\nu^{-1}u_0(x),\qquad 0\leq s<\nu T .
\end{equation}
The map $(u,p,u_0)\mapsto(v,q,v_0)$ is a bijection (with inverse
$u(t,x)=\nu v(\nu t,x)$, $p(t,x)=\nu^2q(\nu t,x)$, $u_0=\nu v_0$), and for
every $0<T'<T$, $j,k\geq0$, $1\leq r\leq\infty$:
\begin{itemize}
\item[(a)] $\norm{v(s)}_{H^k}=\nu^{-1}\norm{u(s/\nu)}_{H^k}$ and
$\norm{v(s)}_{L^r}=\nu^{-1}\norm{u(s/\nu)}_{L^r}$; $v_0$ is Schwartz
(resp.\ in $H^k$, divergence-free) iff $u_0$ is; moreover
\begin{gather*}
 v\in C^j([0,\nu T'];H^k)\iff u\in C^j([0,T'];H^k),\qquad
 \partial_s^jv(s)=\nu^{-1-j}(\partial_t^ju)(s/\nu);\\
 \norm v_{L^\infty_sH^k([0,\nu T']\times\R^3)}
 =\nu^{-1}\norm u_{L^\infty_tH^k([0,T']\times\R^3)},\qquad
 \norm v_{L^2_sH^2([0,\nu T']\times\R^3)}^2
 =\nu^{-1}\norm u_{L^2_tH^2([0,T']\times\R^3)}^2 ;
\end{gather*}
and $v$ is smooth on $[0,\nu T']\times\R^3$ iff $u$ is smooth on
$[0,T']\times\R^3$, with
\[
 \partial_s^j\partial_x^\alpha v(s,x)
 =\nu^{-1-j}\partial_t^j\partial_x^\alpha u(s/\nu,x);
\]
\item[(b)] $\nabla\cdot v=0$ iff $\nabla\cdot u=0$; $u$ satisfies
$\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u$ and $u(0)=u_0$
pointwise (or in $L^2$ for each time) iff $v$ satisfies
$\partial_sv+(v\cdot\nabla)v+\nabla q=\Delta v$ and $v(0)=v_0$ in the same
sense;
\item[(c)] $p(t)=R_iR_j(u_iu_j)(t)$ iff $q(\nu t)=R_iR_j(v_iv_j)(\nu t)$;
\item[(d)] if $T_1<\infty$ then $\norm{u(t)}_{H^1}\to\infty$ as
$t\uparrow T_1$ iff $\norm{v(s)}_{H^1}\to\infty$ as $s\uparrow\nu T_1$;
\item[(e)] $v$ satisfies \eqref{eq:tao-duhamel} (with $f=0$) for
$s\in[0,\nu T']$ iff $u$ satisfies
\begin{equation}\label{eq:nu-duhamel}
 u(t)=e^{\nu t\Delta}u_0+\int_0^te^{\nu(t-t')\Delta}
 \bigl(-(u\cdot\nabla)u-\nabla p\bigr)(t')\,dt',\qquad t\in[0,T'],
\end{equation}
whenever the integrals are Riemann integrals of continuous $L^2$-valued
functions.
\end{itemize}
\end{lemma}

\begin{proof}
(a) is the change of variables $s=\nu t$ in each norm, for instance
\[
 \norm v_{L^2_sH^2([0,\nu T']\times\R^3)}^2
 =\int_0^{\nu T'}\nu^{-2}\norm{u(s/\nu)}_{H^2}^2\,ds
 =\nu^{-1}\int_0^{T'}\norm{u(t)}_{H^2}^2\,dt ,
\]
together with the chain rule for the affine time change, which applies to classical derivatives, to
Banach-space-valued derivatives, and to Schwartz seminorms alike.  (b)
Chain rule: $\partial_sv(s,x)=\nu^{-2}(\partial_tu)(s/\nu,x)$,
$(v\cdot\nabla)v=\nu^{-2}((u\cdot\nabla)u)(s/\nu)$,
$\nabla q=\nu^{-2}(\nabla p)(s/\nu)$, $\Delta v=\nu^{-1}(\Delta u)(s/\nu)
=\nu^{-2}(\nu\Delta u)(s/\nu)$; therefore $\partial_sv+(v\cdot\nabla)v
+\nabla q-\Delta v=\nu^{-2}\bigl(\partial_tu+(u\cdot\nabla)u+\nabla p
-\nu\Delta u\bigr)(s/\nu)$, and $v(0)=\nu^{-1}u(0)$.  (c)
$v_iv_j(s)=\nu^{-2}(u_iu_j)(s/\nu)$ and $R_iR_j$ is linear.  (d) is (a)
with $k=1$.  (e) Substitute $s=\nu t$, $s'=\nu t'$ in
\eqref{eq:tao-duhamel} for $v$: $\nu^{-1}u(t)=e^{\nu t\Delta}\nu^{-1}u_0
+\int_0^te^{\nu(t-t')\Delta}\nu^{-2}\bigl(-(u\cdot\nabla)u-\nabla p
\bigr)(t')\,\nu\,dt'$; multiply by $\nu$.  The substitution rule for
Riemann integrals of continuous Banach-valued functions is the scalar one
applied after pairing with an arbitrary element of $L^2$.
\end{proof}

\begin{definition}[Solution classes with viscosity $\nu$]\label{def:nu-mild}
Let $\nu>0$, $0<T<\infty$, and $u_0\in H^1(\R^3;\R^3)$ with
$\nabla\cdot u_0=0$.  A pair $(u,p)$ of measurable functions on
$[0,T]\times\R^3$ is an \emph{$H^1$ mild solution of \eqref{eq:NS} with
viscosity $\nu$ and datum $u_0$ on $[0,T]$} if $(v,q,v_0,0,\nu T)$ defined
by \eqref{eq:nu-map} is an $H^1$ mild solution in the sense of
Definition~\ref{def:tao-mild}(d).  Explicitly, by
Lemma~\ref{lem:nu-scaling}: $u\in L^\infty_tH^1_x\cap L^2_tH^2_x([0,T]
\times\R^3)$, $\nabla\cdot u=0$, $p=R_iR_j(u_iu_j)$, and
\eqref{eq:nu-duhamel} holds (with the integral interpreted as in Tao).
Likewise $(u,p)$ is an \emph{almost smooth $H^1$ solution with viscosity
$\nu$ and datum $u_0$ on $[0,T]$} if $(v,q,v_0,0,\nu T)$ is an almost
smooth $H^1$ solution (Definition~\ref{def:tao-mild}(b)); explicitly,
$u_0$ is smooth (so that $(v_0,0,\nu T)$ is a smooth set of data, as
Definition~\ref{def:tao-mild}(a),(b) require), $u,p$ are smooth on
$(0,T]\times\R^3$, $\nabla_x^ku,\partial_t\nabla_x^ku,\nabla_x^kp$ are
continuous on $[0,T]\times\R^3$ for every $k$, $u\in L^\infty_tH^1_x\cap
L^2_tH^2_x$, and $\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u$,
$\nabla\cdot u=0$, $u(0)=u_0$ hold pointwise, with \emph{no} condition on
the normalisation of $p$.
\end{definition}

\subsection{The classical branch}

\begin{proposition}[Local theory; the classical branch and its maximal time]
\label{prop:localtheory}
Let $\nu>0$ and let $u_0\in\mathcal S(\R^3)^3$ with $\nabla\cdot u_0=0$.
There exist a unique $T_*=T_*(\nu,u_0)\in(0,\infty]$ and a pair $(u,p)$ of
smooth functions on $[0,T_*)\times\R^3$, unique among smooth pairs
satisfying (i), with the following properties.
\begin{itemize}
\item[(i)] (Existence and maximality) For every $0<T<T_*$ the restriction
of $(u,p)$ to $[0,T]\times\R^3$ is an $H^1$ mild solution of \eqref{eq:NS}
with viscosity $\nu$ and datum $u_0$ (Definition~\ref{def:nu-mild}); for
no $T\geq T_*$ does such a solution exist.  Thus
\[
 T_*=\sup\{T>0:\text{an $H^1$ mild solution with viscosity $\nu$ and
 datum $u_0$ exists on }[0,T]\}.
\]
\item[(ii)] (Uniqueness) If $(\tilde u,\tilde p)$ is an $H^1$ mild
solution with viscosity $\nu$ and datum $u_0$ on some $[0,T]$, then
$T<T_*$ and $\tilde u=u$, $\tilde p=p$ almost everywhere on
$[0,T]\times\R^3$.  If $(\tilde u,\tilde p)$ is an almost smooth $H^1$
solution with viscosity $\nu$ and datum $u_0$ on $[0,T]$, with any
pressure $\tilde p$, then $T<T_*$, $\tilde u=u$ everywhere on
$[0,T]\times\R^3$, and for almost every $t$ the function
$\tilde p(t)-p(t)$ is constant in $x$.
\item[(iii)] (Regularity) For every $0<T<T_*$ and all $j,k\geq0$:
$u\in C^j([0,T];H^k(\R^3;\R^3))$, $p\in C^j([0,T];H^k(\R^3))$, the
$H^k$-valued time derivatives being the classical ones; all derivatives
$\partial_t^j\partial_x^\alpha u$, $\partial_t^j\partial_x^\alpha p$ are
bounded on $[0,T]\times\R^3$; and $\partial_t^ju,\partial_t^jp\in
L^\infty_tH^k([0,T]\times\R^3)$.
\item[(iv)] (Classical equation and pressure) On $[0,T_*)\times\R^3$,
pointwise,
\[
 \partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u,\qquad\nabla\cdot u=0,
 \qquad u(0,x)=u_0(x),
\]
and for every $t\in[0,T_*)$, $p(t)=R_iR_j(u_iu_j)(t)$ is the normalised
pressure of Lemma~\ref{lem:pressure-convention}; in particular
$-\Delta p=\partial_i\partial_j(u_iu_j)$.
\item[(v)] (Enstrophy blow-up alternative) If $T_*<\infty$ then
$\lim_{t\uparrow T_*}\norm{u(t)}_{H^1(\R^3)}=+\infty$.
\item[(vi)] (Scaling) With $v_0=\nu^{-1}u_0$, the pair $(v,q)$ of
\eqref{eq:nu-map} is the branch of $v_0$ for $\nu=1$, and
$T_*(\nu,u_0)=\nu^{-1}T_*(1,\nu^{-1}u_0)$.
\end{itemize}
\end{proposition}

\begin{proof}
We first treat $\nu=1$ and an arbitrary divergence-free $v_0\in H^1$
(Steps~1--4), then add the Schwartz hypothesis (Steps~5--8), and finally
rescale (Step~9).  Throughout, ``mild solution on $[0,T]$'' means an
$H^1$ mild solution $(v,q,v_0,0,T)$ in the sense of
Definition~\ref{def:tao-mild}(d).

\emph{Step 1 (the set of existence times).}  Let $\mathcal T:=\{T\in
(0,\infty):\text{a mild solution on }[0,T]\text{ exists}\}$.  It is
nonempty: apply Theorem~\ref{thm:tao58} to the $H^1$ data $(v_0,0,1)$;
either $1\in\mathcal T$, or there is an incomplete mild solution on
$[0,T')$ with $0<T'<1$, whose restriction to $[0,T'/2]$ is a mild
solution (Lemma~\ref{lem:restriction}), so $T'/2\in\mathcal T$.  (Theorem
\ref{thm:tao54}(ii) gives the same conclusion.)  By
Lemma~\ref{lem:restriction}, $T\in\mathcal T$ and $0<T'<T$ imply
$T'\in\mathcal T$.  Put $S_*:=\sup\mathcal T\in(0,\infty]$; then
$(0,S_*)\subseteq\mathcal T$.

\emph{Step 2 (consistency and gluing).}  For $T\in\mathcal T$ let $v^T$
be a mild solution on $[0,T]$; by Theorem~\ref{thm:tao54}(i) we may and
do take the representative with $v^T\in C^0([0,T];H^1)$.  If $T<T'$ are in
$\mathcal T$, then $v^{T'}|_{[0,T]}$ is a mild solution on $[0,T]$
(Lemma~\ref{lem:restriction}), so by Theorem~\ref{thm:tao54}(iii)
$v^{T'}=v^T$ a.e.\ on $[0,T]\times\R^3$, hence $v^{T'}(t)=v^T(t)$ in $H^1$
for a.e.\ $t\in[0,T]$, hence for every $t\in[0,T]$ (both are continuous
into $H^1$).  Define $v(t):=v^T(t)$ for any $T\in\mathcal T$ with
$T>t$; this is well defined for all $t\in[0,S_*)$, and $q(t)$ is defined
from $v(t)$ by \eqref{eq:tao-pressure}.  For every $T<S_*$ the restriction
of $(v,q)$ to $[0,T]$ is the mild solution $v^T$; so $(v,q,v_0,0,S_*^-)$
is an incomplete mild $H^1$ solution when $S_*<\infty$, and a mild
solution on every $[0,T]$ when $S_*=\infty$.

\emph{Step 3 (blow-up alternative and $\mathcal T=(0,S_*)$).}  Suppose
$S_*<\infty$.  Apply Theorem~\ref{thm:tao58} to the $H^1$ data
$(v_0,0,S_*+1)$.  The first alternative would put $S_*+1$ in
$\mathcal T$, contradicting $S_*=\sup\mathcal T$.  So there are
$T'\in(0,S_*+1)$ and an incomplete mild solution $(w,\cdot,v_0,0,T'^-)$
with $\norm{w(t)}_{H^1}\to\infty$ as $t\uparrow T'$; again we use the
$C^0_tH^1$ representatives of its restrictions, which are consistent on
overlapping intervals.  By Lemma~\ref{lem:restriction},
$(0,T')\subseteq\mathcal T$, so $T'\leq S_*$.  If $T'<S_*$, pick
$T:=\frac12(T'+S_*)\in\mathcal T$; for every $T''<T'$ the restrictions of
$w$ and of $v^T$ to $[0,T'']$ are mild solutions on $[0,T'']$, so they
agree a.e.\ and hence for all $t\in[0,T'']$ (Theorem~\ref{thm:tao54}(iii),(i));
therefore $\norm{w(t)}_{H^1}=\norm{v^T(t)}_{H^1}\leq
\max_{[0,T]}\norm{v^T}_{H^1}<\infty$ for all $t<T'$, contradicting the
blow-up of $w$.  Hence $T'=S_*$, and the same argument shows $w(t)=v(t)$
for all $t<S_*$, so $\lim_{t\uparrow S_*}\norm{v(t)}_{H^1}=+\infty$.
Finally $S_*\notin\mathcal T$: otherwise $v^{S_*}\in C^0([0,S_*];H^1)$
would be bounded and would agree with $v$ on $[0,S_*)$.  Thus
$\mathcal T=(0,S_*)$ in all cases (trivially so if $S_*=\infty$).

\emph{Step 4 (uniqueness in the mild class).}  If $(\tilde v,\tilde q,
v_0,0,T)$ is a mild solution then $T\in\mathcal T$, so $T<S_*$, and
$\tilde v=v^T=v$ a.e.\ on $[0,T]\times\R^3$ by Theorem~\ref{thm:tao54}(iii);
$\tilde q=q$ a.e.\ because both are given by \eqref{eq:tao-pressure} from
a.e.\ equal velocities.  (Almost smooth competitors are treated in
Step~7, after the continuity of $v$ is available.)

\emph{Step 5 (Schwartz data: regularity).}  Now let $v_0\in\mathcal S
(\R^3)^3$ be divergence-free.  Then $v_0\in H^k$ for every $k$: for every
multi-index $\beta$, $|\partial^\beta v_0(x)|\leq C_\beta(1+|x|)^{-2}$ and
$\int_{\R^3}(1+|x|)^{-4}dx=4\pi\int_0^\infty r^2(1+r)^{-4}dr<\infty$, so
$\partial^\beta v_0\in L^2$, and Lemma~\ref{lem:sobolev-norms} applies.
In particular $v_0$ is $H^1$ data, Steps~1--4 apply, and for every
$0<T<\infty$ the triplet $(v_0,0,T)$ is Schwartz data
(Definition~\ref{def:tao-data}).  Fix $T<S_*$.  The restriction
$(v,q,v_0,0,T)$ is a mild solution with Schwartz data, so by
Theorem~\ref{thm:tao54}(iv) $\partial_s^jv,\partial_s^jq\in
L^\infty_sH^k([0,T]\times\R^3)$ for all $j,k\geq0$, where the time
derivatives are classical (Tao) and hence also distributional.
Lemma~\ref{lem:upgrade} applied to $v$ (with $N=3$) and to $q$ (with
$N=1$) yields smooth functions $V^T,Q^T$ on $[0,T]\times\R^3$, equal
a.e.\ to $v,q$, with $V^T\in C^j([0,T];H^k)$, $Q^T\in C^j([0,T];H^k)$ for
all $j,k$, with all space-time derivatives bounded on $[0,T]\times\R^3$,
and with $\partial_s^jV^T,\partial_s^jQ^T\in L^\infty_sH^k$.  For
$T<T'<S_*$, $V^{T'}|_{[0,T]}$ and $V^T$ are continuous and agree a.e., so
they agree everywhere; hence there is a single smooth pair on
$[0,S_*)\times\R^3$, again denoted $(v,q)$, whose restriction to each
$[0,T]\times\R^3$ is $(V^T,Q^T)$.  Since $V^T\in C^0([0,T];H^1)$ and
agrees a.e.\ in $t$ with the representative $v^T$ of Step~2, the two
agree for every $t$; so the smooth pair is the branch of Step~2, and
(i), (v) and the first half of (ii) hold for it (for $\nu=1$) by
Steps~1--4, while (iii) holds by Lemma~\ref{lem:upgrade}.

\emph{Step 6 (classical equation, initial value, pressure).}  Fix
$T<S_*$.  By Step~5, $v\in C^1([0,T];L^2)\cap C([0,T];H^2)$ and
$q\in C([0,T];H^1)$, so Lemma~\ref{lem:mild-classical} gives
$v(0,x)=v_0(x)$ and $\partial_sv+(v\cdot\nabla)v+\nabla q=\Delta v$
pointwise on $[0,T]\times\R^3$; $\nabla\cdot v(s)=0$ holds in $L^2$ for
a.e.\ $s$ by Definition~\ref{def:tao-mild}(d), hence for every $s$ by
continuity of $s\mapsto\nabla\cdot v(s)$ into $L^2$, hence pointwise
since $\nabla\cdot v$ is continuous.  For the pressure: by
Definition~\ref{def:tao-mild}(d) and Lemma~\ref{lem:pressure-convention}(b),
$q(s)=P[v\otimes v(s)]=R_iR_j(v_iv_j)(s)$ in $L^2$ for a.e.\ $s\in[0,T]$.
Both $s\mapsto q(s)$ and $s\mapsto P[v\otimes v(s)]$ are continuous into
$L^2$: the former by Step~5, the latter because, by
Lemma~\ref{lem:pressure-convention}(a) applied to
$w=v\otimes v(s)-v\otimes v(s')$ and the pointwise identity
$a\otimes a-b\otimes b=(a-b)\otimes a+b\otimes(a-b)$ with
$|x\otimes y|=|x||y|$,
\begin{align*}
 \norm{P[v\otimes v(s)]-P[v\otimes v(s')]}_{L^2}
 &\leq\norm{v\otimes v(s)-v\otimes v(s')}_{L^2}\\
 &\leq\norm{v(s)-v(s')}_{L^\infty}\norm{v(s)}_{L^2}
 +\norm{v(s')}_{L^\infty}\norm{v(s)-v(s')}_{L^2},
\end{align*}
which tends to $0$ as $s'\to s$ by $v\in C_s(H^2)$ with
Lemma~\ref{lem:embedding}(a).  Two continuous maps that agree a.e.\ agree
everywhere; so $q(s)=R_iR_j(v_iv_j)(s)$ for every $s\in[0,S_*)$.  This is
(iv) for $\nu=1$.

\emph{Step 7 (almost smooth competitors).}  Let $(\tilde v,\tilde q,
v_0,0,T)$ be an almost smooth $H^1$ solution with an arbitrary pressure
$\tilde q$.  By Theorem~\ref{thm:tao43}, $(\tilde v,\tilde q_{\rm n},
v_0,0,T)$ with $\tilde q_{\rm n}:=-\Delta^{-1}\partial_i\partial_j
(\tilde v_i\tilde v_j)$ is a mild solution, so $T\in\mathcal T$, $T<S_*$,
and $\tilde v=v$ a.e.\ on $[0,T]\times\R^3$ by Step~4.  Since $\tilde v$
is almost smooth, $\tilde v$ is continuous on $[0,T]\times\R^3$
(Definition~\ref{def:tao-mild}(b) with $k=0$: $\nabla_x^0\tilde v=\tilde v$
is continuous there), and $v$ is continuous on $[0,T]\times\R^3$ by
Step~5; two continuous functions that agree almost everywhere agree
everywhere, so $\tilde v=v$ on $[0,T]\times\R^3$.  Consequently
$\tilde q_{\rm n}(s)=P[\tilde v\otimes\tilde v(s)]=P[v\otimes v(s)]=q(s)$
for every $s\in[0,T]$ by Step~6, and Theorem~\ref{thm:tao43} says that for
a.e.\ $s$ the function $\tilde q(s)-\tilde q_{\rm n}(s)=\tilde q(s)-q(s)$
is constant in $x$.  This is the second half of (ii) for $\nu=1$.

\emph{Step 8 (uniqueness of the pair).}  Any smooth pair on
$[0,S_*)\times\R^3$ satisfying (i) agrees a.e.\ on each $[0,T]\times\R^3$
with $(v^T,q^T)$ by Theorem~\ref{thm:tao54}(iii) and
\eqref{eq:tao-pressure}, hence with the smooth pair of Step~5, hence
everywhere by continuity; and $S_*$ is determined by (i) as the supremum
of $\mathcal T$.  This proves the proposition for $\nu=1$, with
$T_*(1,v_0)=S_*$.

\emph{Step 9 (general $\nu$).}  Let $\nu>0$ and $u_0\in\mathcal S(\R^3)^3$
be divergence-free.  Put $v_0:=\nu^{-1}u_0$ (Schwartz, divergence-free),
let $(v,q)$ be its branch for $\nu=1$ on $[0,S_*)$, and define
$T_*:=S_*/\nu$ and $(u,p)$ on $[0,T_*)\times\R^3$ by $u(t,x):=\nu v(\nu
t,x)$, $p(t,x):=\nu^2q(\nu t,x)$, the inverse of \eqref{eq:nu-map}.  By
Definition~\ref{def:nu-mild}, $(u,p)|_{[0,T]}$ is an $H^1$ mild solution
with viscosity $\nu$ on $[0,T]$ exactly when $(v,q)|_{[0,\nu T]}$ is a
mild solution on $[0,\nu T]$, i.e.\ exactly when $\nu T<S_*$; this is (i),
and (v) follows from Step~3 by Lemma~\ref{lem:nu-scaling}(d).  For (ii):
a competitor $(\tilde u,\tilde p)$ of either kind on $[0,T]$ corresponds
under \eqref{eq:nu-map} to a competitor $(\tilde v,\tilde q)$ of the same
kind on $[0,\nu T]$ (Definition~\ref{def:nu-mild}), so Steps~4 and~7 give
$\nu T<S_*$, $\tilde v=v$ a.e.\ (resp.\ everywhere), and, in the almost
smooth case, $\tilde q(s)-q(s)$ constant in $x$ for a.e.\ $s$; pulling
back, $T<T_*$, $\tilde u=u$ a.e.\ (resp.\ everywhere), $\tilde p=p$ a.e.\
in the mild case, and $\tilde p(t)-p(t)=\nu^2(\tilde q-q)(\nu t)$ constant
in $x$ for a.e.\ $t$ in the almost smooth case.  Items (iii) and (iv)
follow from Steps~5--6 by Lemma~\ref{lem:nu-scaling}(a),(b),(c), and (vi)
is the construction.  Uniqueness of $(u,p)$ among smooth pairs satisfying
(i), and of $T_*$, follows from Step~8 through the bijection
\eqref{eq:nu-map}.
\end{proof}

\begin{corollary}[Lebesgue-space continuity]\label{cor:Lq}
Let $(u,p)$ be the branch of Proposition~\ref{prop:localtheory} and
$0<T<T_*$.  Then $u$, $\nabla u$, $\Delta u$, $\partial_tu$, $p$, and
$\nabla p$ belong to $C([0,T];L^q(\R^3))$ for every $2\leq q\leq\infty$
(for $q=\infty$ with the continuous representatives, which are the
functions themselves), and $\sup_{[0,T]}\norm{u(t)}_{L^q}<\infty$, etc.
In particular $t\mapsto\norm{u(t)}_{L^3}$ is continuous on $[0,T_*)$.
\end{corollary}

\begin{proof}
Each listed field $g$ lies in $C([0,T];H^k)$ for every $k$ by
Proposition~\ref{prop:localtheory}(iii) and Lemma~\ref{lem:sobolev-norms}.
By Lemma~\ref{lem:embedding}(a),(c), $\norm{g(t)-g(s)}_{L^q}\leq
\norm{g(t)-g(s)}_{L^2}^{2/q}\bigl(\pi\norm{g(t)-g(s)}_{H^2}\bigr)^{1-2/q}
\leq\pi^{1-2/q}\norm{g(t)-g(s)}_{H^2}\to0$ as $s\to t$.
\end{proof}

\begin{lemma}[Supremum versus essential supremum]\label{lem:sup-esssup}
For the branch of Proposition~\ref{prop:localtheory} and every
$0<T\leq T_*$,
\[
 \operatorname*{ess\,sup}_{0<t<T}\norm{u(t)}_{L^3}
 =\sup_{0<t<T}\norm{u(t)}_{L^3}=\sup_{0\leq t<T}\norm{u(t)}_{L^3},
\]
and if $T_*<\infty$ then
$\sup_{0\leq t<T_*}\norm{u(t)}_{L^3}<\infty$ is equivalent to
$\limsup_{t\uparrow T_*}\norm{u(t)}_{L^3}<\infty$.
\end{lemma}

\begin{proof}
The function $t\mapsto\norm{u(t)}_{L^3}$ is continuous on $[0,T_*)$
(Corollary~\ref{cor:Lq}).  A continuous function on an interval has the
same supremum over the interval, over its interior, and outside any null
set (every value is a limit of values at points outside the null set).
If $T_*<\infty$ the function is bounded on each compact $[0,T]$,
$T<T_*$, so boundedness on $[0,T_*)$ is a property of $t\uparrow T_*$
only.
\end{proof}

\begin{lemma}[Global smoothness when $T_*=\infty$]\label{lem:global-smooth}
Let $(u,p)$ be the branch of Proposition~\ref{prop:localtheory} and
suppose $T_*(\nu,u_0)=\infty$.  Then $u,p\in C^\infty(\R^3\times[0,\infty))$
in Fefferman's sense (all partial derivatives exist, one-sided in $t$ at
$t=0$, and are continuous on $\R^3\times[0,\infty)$); they satisfy
$\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u$ and $\nabla\cdot u=0$
pointwise on $\R^3\times[0,\infty)$ and $u(x,0)=u_0(x)$; for every
$t\geq0$, $p(t)=R_iR_j(u_iu_j)(t)$ and $u(t),p(t)\in H^k(\R^3)$ for every
$k$; and for every finite $T$ all derivatives of $u$ and $p$ are bounded
on $\R^3\times[0,T]$.
\end{lemma}

\begin{proof}
Let $(x_0,t_0)\in\R^3\times[0,\infty)$ and choose $T>t_0$; $T<T_*$.  By
Proposition~\ref{prop:localtheory}(iii),(iv), $u$ and $p$ are smooth on
$[0,T]\times\R^3$ with bounded derivatives and satisfy the equation, the
divergence condition, and the initial condition there.  The existence and
continuity of every partial derivative at $(x_0,t_0)$, and the equation
at $(x_0,t_0)$, are statements about the relatively open neighbourhood
$\R^3\times[0,T)$ of $(x_0,t_0)$ in $\R^3\times[0,\infty)$; the
derivatives computed on $[0,T]\times\R^3$ and on $[0,T']\times\R^3$,
$T<T'$, coincide since they are derivatives of one and the same function
$(u,p)$ on $[0,T_*)\times\R^3$.  The pressure identity and the $H^k$
memberships are Proposition~\ref{prop:localtheory}(iii),(iv) at the time
$t$.
\end{proof}

\begin{remark}[Statement shape for Theorem~\ref{thm:continuation}]
\label{rem:continuation-shape}
Since $T_*$ is maximal by Proposition~\ref{prop:localtheory}(i), a
conclusion of the form ``$u$ extends as a classical solution beyond
$T_*$'' can only be reached by contradiction.  The continuation theorem
is therefore stated as
\[
 T_*(\nu,u_0)<\infty\ \Longrightarrow\
 \sup_{0\leq t<T_*}\norm{u(t)}_{L^3(\R^3)}=\infty ;
\]
equivalently, the bound $\sup_{0\leq t<T_*}\norm{u(t)}_{L^3}<\infty$
implies $T_*=\infty$.  By
Lemma~\ref{lem:sup-esssup} the supremum may be replaced by an essential
supremum or a $\limsup$.  Its proof uses from this section: the
$\nu$-normalisation Lemma~\ref{lem:nu-scaling}, under which the branch
$(u,p)$ becomes the unit-viscosity branch $(v,q)$ of $v_0=\nu^{-1}u_0$
on $[0,\nu T_*)$ with $\norm{v(s)}_{L^3}=\nu^{-1}\norm{u(s/\nu)}_{L^3}$
and the same regularity; the enstrophy blow-up alternative
Proposition~\ref{prop:localtheory}(v), $\norm{u(t)}_{H^1}\to\infty$ as
$t\uparrow T_*<\infty$; and the regularity (iii) needed to verify that
the branch is a Leray--Hopf weak solution in the sense required by the
endpoint theorem.  One caution: (iii) is uniform only on compact
subintervals $[0,T]$, $T<T_*$, and gives no bound uniform up to $T_*$.
The memberships $u\in L^\infty(0,T_*;L^2)$ and $\nabla u\in
L^2((0,T_*)\times\R^3)$ that the Leray--Hopf class requires on the whole
cylinder $(0,T_*)\times\R^3$ come from the energy identity
(Proposition~\ref{prop:energy}), not from (iii).
\end{remark}
```

### 2.3 Replacements inside the proof of `thm:conditional` (C-3)

Two insertion points, because in `main.tex` the `prop:energy` sentence
sits between the two sentences being replaced.

**First insertion point.** Replace the sentence

> Persistence in Tao's local theorem preserves smoothness for every finite
> time, including at `t=0`.

(immediately after "Thus `T_*=∞`." and before "Proposition `prop:energy`
gives ...") by

```latex
Since $T_*=\infty$, Lemma~\ref{lem:global-smooth} gives
$u,p\in C^\infty(\R^3\times[0,\infty))$, the equation \eqref{eq:NS} and
$\nabla\cdot u=0$ pointwise on $\R^3\times[0,\infty)$, and $u(x,0)=u_0(x)$.
```

**Second insertion point.** Replace the two sentences

> The pressure may be recovered, up to a function of time, from
> `−Δp = ∂_i∂_j(u_iu_j)` and is smooth through `t=0` by the same local
> theorem. Hence all parts of Theorem `def:target` follow.

(immediately after "... which is the required uniform kinetic-energy
bound.") by

```latex
Here $p=R_iR_j(u_iu_j)$ is the normalised pressure of
Lemma~\ref{lem:pressure-convention}, which satisfies
$-\Delta p=\partial_i\partial_j(u_iu_j)$ and is smooth on
$\R^3\times[0,\infty)$ by Lemma~\ref{lem:global-smooth}; no freedom ``up to
a function of time'' remains to be fixed, and Fefferman's condition (6) is
met with this $p$.  Hence all parts of Theorem~\ref{def:target} follow.
```

(The `prop:energy` sentence between the two insertion points is
unchanged.)

## 3. External facts used

| # | Fact, exactly as used | Source and location | Status |
|---|---|---|---|
| 1 | Theorem 5.4 (i)–(iv), text as transcribed in `thm:tao54` (with the six transcription notes) | Tao, *Anal. PDE* 6 (2013), **pp. 52–53** | [DI] read on the published PDF in this round (pp. 51–52 as page images; (v) continues on p. 53 and is not used) |
| 2 | Corollary 5.8 and the definition of "incomplete mild `H^1` solution" (with `v` for `p` typo) | Tao, **p. 56** (Remark 5.9 on p. 57) | [DI] published PDF |
| 3 | Corollary 4.3 ("Almost smooth `H^1` solutions are essentially mild"), verbatim | Tao, **p. 47** (last result of §4, immediately before §5) | [DI] published PDF |
| 4 | Definition 1.1 (smooth set of data, (1) `∇·u_0=0`, `H^1` norm of data, Schwartz data, smooth solution, (3)–(4)); footnote 3 (`ν=1`); (7) `H^1` solution; (8)–(9) normalised pressure | Tao, **pp. 26–28** (footnote 3 and (7) on p. 27 per CP01 and the round-1 publisher sample) | [DI] |
| 5 | The `R^3` "almost smooth" definition and the `R^3` "`H^1` mild solution" definition ("obeying (4), (1), and (10)"); Theorem 1.12; the sentence "the Schwartz property need not be preserved over time" | Tao, **p. 31** (definitions), **p. 30** (Theorem 1.12, Schwartz sentence) | [DI] published PDF |
| 6 | Duhamel integral form (10) (displayed for the periodic setting), (11)–(12) | Tao, **p. 29** | [DI] published PDF |
| 7 | Footnote 12: moments `∫ω_1(t,x)(x_2^2−x_3^2)dx` not conserved but zero for Schwartz `u(t)`; "time translation can instantly convert Schwartz data to non-Schwartz data" | Tao, **§3, p. 42** (after the time-translation symmetry (30)) | [DI] published PDF |
| 8 | §2 notation: Fourier convention (p. 35); classical and Fourier-side `H^k` norms, "conflicts slightly ... equivalent up to constants" (p. 36); `L^p_tX_x`, `C^k_tX_x` (with the `∇^j` slip), (13) `X^s` with the `L^2_x` typo (p. 37); (14) `Δ^{-1}` multiplier and its domain (p. 38); heat semigroup by the kernel formula `(4πt)^{-3/2}∫e^{-|x-y|^2/4t}f(y)dy` (p. 39) | Tao, **pp. 35–39** | [DI] published PDF |
| 9 | Corollary "Unconditional uniqueness" (§11) and the remark following it, conjecturing uniqueness for finite-energy data | Tao, §11 (arXiv:1108.1165 source, labels `unconditional`, `uniq`; round 1) | [DI] source text; published page not pinned (used only in `rem:tao-scope`(d), not load-bearing) |
| 10 | Fefferman's (6): `p,u ∈ C^∞(R^n×[0,∞))`; (A) data class = Schwartz | Fefferman, Clay problem description, pp. 1–2 | [DI] in CP01 (`cp01-literature-statements` §5); not reopened here |
| 11 | Plancherel theorem on `L^2(R^3)`; inverse transform on `L^1∩L^2` given by the integral formula; `(∂^α f)^ = (2πiξ)^α f̂` for tempered distributions | Stein–Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (1971), Ch. I | [MO] (theorem numbers not verified; chapter-level) |
| 12 | Fourier transform of the Gaussian `K_s`, `K̂_s = e^{-4π²s|ξ|²}`; convolution theorem `(K*g)^ = K̂ ĝ` for `K ∈ L^1`, `g ∈ L^2` | Stein–Weiss, Ch. I | [MO] |
| 13 | `C_c^∞` dense in `L^2(R^3)`, `L^2` separable (countable dense subset of `C_c^∞`); fundamental lemma (`d ∈ L^1_loc`, `∫dη=0 ∀η ∈ C_c^∞` ⟹ `d=0` a.e.) | Rudin, *Real and Complex Analysis*, 3rd ed. (1987), Ch. 3 (density), Ch. 7 (Lebesgue differentiation / approximate identities) | [MO] |
| 14 | Tonelli/Fubini, dominated and monotone convergence, Cauchy–Schwarz, mean value theorem, Riemann integrals of continuous Banach-valued functions (linearity, `‖∫‖ ≤ ∫‖·‖`, commutation with bounded linear maps) | standard measure theory / calculus | [MO] |

Bibliography entries to add to `references.bib` (integrator): `SteinWeiss1971`
(E. M. Stein, G. Weiss, *Introduction to Fourier Analysis on Euclidean
Spaces*, Princeton Univ. Press, 1971) and `Rudin1987` (W. Rudin, *Real and
Complex Analysis*, 3rd ed., McGraw–Hill, 1987). Both are [MO] here.

Correction to be propagated to the CP01 record (not edited by this lane):
`cp01-literature-statements.md` §1.1 attributes the Duhamel identity
`u(t) = e^{tΔ}u_0 + ∫_0^t e^{(t−t')Δ}(−(u·∇)u − ∇p + f)(t')dt'` to Tao's
"(11)". On the published p. 29 it is **(10)**; (11) is the Leray-projected
form `u(t) = e^{tΔ}u_0 + ∫_0^t e^{(t−t')Δ}(PB(u,u)+Pf)(t')dt'`, and the `R^3`
mild-solution definition on p. 31 says "obey (4), (1), and (10) (and thus
(11))".

## 4. Obligations not discharged (exactly stated)

1. **Textbook facts remain [MO].** Items 11–14 of the table are cited at
   chapter level; no theorem numbers were verified against the books. This
   is within (D5) but is recorded so a later pass can pin exact theorem
   numbers.
2. **Theorem 5.4(v) not transcribed.** It is not used anywhere in CP1; the
   transcription in `thm:tao54` states this and omits it. If Phase I of the
   Lean plan wants the full statement, it is in `cp01-literature-statements`
   §1.2.
3. **Published page of Tao's §11 corollary "Unconditional uniqueness"** is
   not pinned (read in the arXiv source only). It appears only in
   `rem:tao-scope`(d) as a scope remark and carries no proof weight.
4. **Not in this lane's scope, flagged for the owners:** the identification
   of the branch with a Leray–Hopf weak solution in the ESS sense (D3,
   continuation lane) — Proposition `prop:localtheory`(iii),(iv) supplies
   `u ∈ C([0,T];H^k)`, `∂_t u ∈ C([0,T];H^k)`, `p ∈ C([0,T];H^k)` and the
   pointwise equation on compact `[0,T]`, `T<T_*`, and `prop:energy` must
   supply the `Q_{T_*}`-uniform memberships (`rem:continuation-shape`); the
   verification of ESS (1.3)–(1.7) is theirs. The energy identity (E-1),
   enstrophy (N-1) and pressure balance (P-2, P-3) proofs should now cite
   `prop:localtheory`(iii),(iv) and `cor:Lq` for the memberships they use.
5. **Cross-lane label collision (integrator, blocking for the splice):**
   `cp02-pressure.md` defines `\label{lem:pressure-convention}`; this lane
   owns that label (integrator note (d) in §2).

The round-1 open obligation "published page of Corollary 4.3" is closed:
the complete published PDF was read in this round and Corollary 4.3 is on
p. 47.

## 5. Frontier record

**MODE / RESULT.** REPAIR round 2 (paper-proof text). Obligations L-1, C-3,
P-1 and the C-0 statement shape are written out at the (D5) standard; the
regularity package R of (D2) is a proved conclusion
(`prop:localtheory`(iii),(iv),(v)) rather than an assumption. The round-1
audit's first bad bridge (R1) and the two scope defects (R2, R3) are
repaired with complete arguments; no hypothesis was added and no statement
was weakened.

**CLAIM AND SCOPE.** For the unforced equation on `R^3`, arbitrary `ν>0`,
and divergence-free Schwartz data: there is a unique maximal time
`T_*(ν,u_0) ∈ (0,∞]` and a classical branch `(u,p)`, unique among smooth
pairs satisfying `prop:localtheory`(i), smooth on each `[0,T]×R^3`,
`T<T_*`, with `u,p ∈ C^j([0,T];H^k)` for all `j,k`, bounded derivatives,
`u(0)=u_0`, the equation pointwise, `p = R_iR_j(u_iu_j)` = Tao's normalised
pressure for every `t`, uniqueness within the exactly stated `H^1` mild
class (a.e.) and, via Tao's Corollary 4.3, within almost smooth `H^1`
classical solutions with arbitrary pressure (everywhere, pressure equal up
to a constant for a.e. `t`), and `‖u(t)‖_{H^1} → ∞` as `t ↑ T_*` if
`T_* < ∞`. All of this is deduced from Tao's Theorem 5.4 (i)–(iv),
Corollary 5.8 and Corollary 4.3 (unit viscosity) by: a rescaling lemma
with explicit formulas, a supremum-and-gluing argument that uses only
restriction and Tao's uniqueness (no concatenation of Duhamel formulas is
needed), a regularity upgrade `∂_t^j u ∈ L^∞_tH^k ∀j,k ⟹ u ∈ C^j_tH^k ∀j,k
∧ C^∞` proved from the existence of the distributional time derivatives as
functions with those bounds (exactly the second half of Tao's (iv); what is
not load-bearing is the closed-slab reading of Tao's word "smooth"), and a
"mild ⟹ classical" lemma proved on the Fourier side, with both one-sided
difference quotients treated on the closed triangle where the heat kernel
pairing is defined. Nothing beyond `u(t) ∈ H^k ∀k` is used for `t>0`;
Schwartz decay is not assumed to persist. No Calderón–Zygmund theory, `L^p`
Riesz bound, Littlewood–Paley theory or `L^p` Leray projection is used.

**EVIDENCE.** The complete published PDF of Tao 2013 read as page images
for every quoted definition, theorem, equation number and page number
(§3, items 1–8); the §11 corollary from the arXiv source; the multiplier
identities (`R_iR_j = -Δ^{-1}∂_i∂_j`, `-Δp = ∂_i∂_j(u_iu_j)`, heat symbol
algebra, Gaussian normalisation `(4πs)^{-3/2}e^{-|x|²/4s} ↔ e^{-4π²s|ξ|²}`
matching Tao's kernel on p. 39 and his (14) on p. 38) and the numerical
constants (`∫(1+|ξ|²)^{-2}dξ = π²`, embedding constant `π`,
derivative-multiplier constant `(2π)^{|α|}`, `L^2_sH^2` scaling `ν^{-1}`,
`Σ_{i,j}ξ_i²ξ_j² = |ξ|⁴`) recomputed; the case analysis of Step 3
(`T' < S_*`, `T' = S_*`, `S_* ∈ 𝒯`) checked to be exhaustive; the
domination in (K3) checked for both signs of `h`; the `δ<0` decomposition
in `lem:mild-classical` checked term by term (`m_ψ(t) = ∫_0^{t+δ}h(t',t) +
∫_{t+δ}^t h(t',t)`, so the quotient is the stated sum, and every argument
of `h_ψ` lies in the triangle). The three LaTeX blocks were compiled
against the `main.tex` preamble plus the three `\newtheorem` lines (see §6
for the build result).

**FIRST GAP (for this lane's deliverable).** None mathematical. One
bibliographic: the textbook facts (Plancherel, Gaussian transform,
convolution theorem, density/separability of `L^2`, fundamental lemma) are
cited at chapter level only ([MO]), and the §11 corollary's published page
is not pinned (scope remark only).

**SURVIVING CONDITIONAL SUFFIX.** With `prop:localtheory` in place, the
chain of the paper reads: `hyp:highpressure ⟹ hyp:absorption ⟹
hyp:critical ⟹ (thm:continuation, via ν-scaling `lem:nu-scaling` + ESS
Theorem 1.3 + the manuscript-owned Serrin-type enstrophy bound + the
blow-up alternative `prop:localtheory`(v)) T_* = ∞ ⟹ (`lem:global-smooth`
+ `prop:energy`) Clay alternative (A)`. The two links that are not this
lane's — the Leray–Hopf verification (with the `Q_{T_*}`-uniform
memberships taken from `prop:energy`, not from (iii)) and the Serrin-type
bound — remain with the continuation lane.

**NON-CLAIMS.** No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or
NS-R3 statement is asserted or approached. No `L^3` uniqueness theorem is
imported. Tao's Theorem 5.4(v), Remark 5.9, Theorem 1.12, and the §11
corollary are mentioned only to delimit scope and are not used. No
statement about `u(t)` decay beyond `H^k` membership is made for `t>0`.

**NEXT DISTINCT ACTION.** Integrator: add the three `\newtheorem` lines and
the two `.bib` entries, splice §2.1, §2.2 and the two insertion points of
§2.3, delete or relabel the pressure lane's `lem:pressure-convention`, and
have the energy / enstrophy / pressure / continuation lanes cite
`prop:localtheory`(iii),(iv) and `cor:Lq` for their memberships.
Literature lane: correct CP01 §1.1's "(11)" to "(10)"; pin theorem numbers
for items 11–13 of the table.

## 6. Changes in this repair round (audit item → change)

| audit item | change in this file |
|---|---|
| FIRST BAD BRIDGE / R1 (`δ<0` in `lem:mild-classical`) | The paragraph *The equation* now defines the triangle `Σ` explicitly, states the claim as the displayed `eq:m-derivative`, treats `0<δ≤T−t` and `−t≤δ<0` separately with the two decompositions, checks in each that every argument of `h_ψ` lies in `Σ`, applies the mean value theorem on the correct interval `[t+δ,t] ⊂ [t',T]`, handles the missing slice, and concludes that both one-sided derivatives exist and agree, giving `m_ψ ∈ C^1([0,T])` with one-sided derivatives at the endpoints. |
| R2 (`lem:pressure-convention`(a) out of scope) | The lemma now defines `P[w] = Σ R_iR_j w_{ij}` for arbitrary `w ∈ L^2(R^3;R^{3×3})` and states (a) as `‖P[w]‖_2 ≤ ‖w‖_2`, `‖P[w]‖_{H^k} ≤ ‖w‖_{H^k}`, with `p = P[u⊗u]` as the particular case; (d) keeps only the Leibniz estimate and cites (a). Step 6 of `prop:localtheory` applies (a) to `w = v⊗v(s) − v⊗v(s')` with the tensor identity written out. |
| R3 (`a.e.` vs everywhere in (ii)) | The almost-smooth half of Step 4 is moved to a new Step 7, after Steps 5–6 supply continuity of `v`; it proves `ṽ = v` everywhere from continuity of both functions and identifies `q̃_n` with `q` for every `s`. Steps renumbered (uniqueness of the pair is Step 8, general `ν` is Step 9), and Step 9 spells out how (ii) is pulled back through `eq:nu-map`. |
| R4 / §5.1 / §5.2 (pages) | Corollary 4.3: `p.~47`; `R^3` mild and almost-smooth definitions: `p.~31`; (10): `p.~29`; Schwartz sentence and Theorem 1.12: `p.~30`; Corollary 5.8: `p.~56`; (14): `p.~38`; heat kernel: `p.~39`; Fourier convention: `p.~35`; `H^k` norms: `p.~36`; `C^k_tX_x`, (13): `p.~37`. All verified directly on the published PDF in this round. Round-1 open obligation 1 deleted; header and §3 table rewritten accordingly. |
| §5.3 (CP01 (11)→(10)) | Recorded at the end of §3 as a correction to propagate; CP01 file not edited (out of scope). |
| §5.4 (footnote misattributed) | `rem:tao-scope`(e) now cites p. 30 for the sentence and §3, footnote 12, p. 42 for the moment mechanism, with Tao's "instantly convert" phrase. |
| §5.5 (two `H^k` norms; `C^k_tX_x` slip) | New transcription note (6) after `thm:tao54`, pointing at `lem:sobolev-norms`; a forward pointer added in the conventions paragraph. |
| §5.6 (overfull boxes) | The `H^{-k}` definition, the two long inline bounds in `lem:upgrade` Step 5, the two norm identities in `lem:nu-scaling`(a), and the pressure-continuity bound in Step 6 are now displays. Build result recorded below. |
| §5.7 (label collision) | Integrator note (d) in §2 and item 5 of §4: this lane owns `lem:embedding` and `lem:pressure-convention`; the pressure lane's copy of the latter must be deleted or relabelled (its `lem:embedding` is already gone). |
| §5.8.1 (`u_0` smooth) | `def:nu-mild`, almost-smooth clause: "`u_0` is smooth (so that `(v_0,0,νT)` is a smooth set of data ...)". |
| §5.8.2 (uniqueness clause) | Preamble of `prop:localtheory`: "a pair `(u,p)` ..., unique among smooth pairs satisfying (i)"; Step 8 and Step 9 say the same. |
| §5.8.3 (environment vs label) | The two imported corollaries stay in the `theorem` environment (they are theorems of this paper's imports, not corollaries of anything here) and are relabelled `thm:tao58`, `thm:tao43`; all references updated. |
| §5.8.4 (splice ambiguity) | §2.3 now states two insertion points with the surrounding sentences quoted. |
| §5.8.5 (`Q_{T_*}` caution) | Added to `rem:continuation-shape` and to §4 item 4 and the frontier record. |
| §5.8.6 (frontier phrase) | CLAIM AND SCOPE now says what `lem:upgrade` assumes (existence of the distributional time derivatives as functions with the bounds) and what is not load-bearing (the closed-slab reading of "smooth"); transcription note (5) says the same. |
| §5.8.7 (`R^N`-valued `|f̂|`) | Conventions paragraph: componentwise application and Euclidean norm of `f̂(ξ) ∈ C^N` stated once; `lem:sobolev-norms` and `lem:embedding`(a) refer to it. |
| §5.8.8 ("arXiv" in LaTeX) | Transcription note (1): "in both the published and the preprint text". |
| UNNECESSARY DEPENDENCIES ((K1) semigroup identity) | Dropped from `lem:heat`(K1) and its proof; nothing used it. |

Build result (this round). The five fenced LaTeX blocks above were
extracted and compiled with `pdflatex` (three passes plus `bibtex`) against
the `main.tex` preamble (`article`, `amsmath,amssymb,amsthm`, `geometry`,
`hyperref`, the four existing `\newtheorem` lines and `\R`, `\norm`) plus
the three `\newtheorem` lines of integrator note (a), with stub
environments carrying the outside labels `eq:NS`, `def:target`,
`prop:energy`, `thm:continuation`, `thm:conditional` and a `.bib` holding
`Tao2013`, `Fefferman2000`, `SteinWeiss1971`, `Rudin1987`: 16 pages, no
undefined references or citations, no multiply-defined labels, **zero
overfull and zero underfull boxes**. The harness lives in the session
scratchpad only; nothing outside this file was written.
