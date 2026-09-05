# CP02-3: critical pressure balance in integrated form (prop:pressure, eq:pressure-consequence)

MODE: PROOF WRITING, round 2 (repair after `cp02-review-pressure.md`).
Date: 2026-09-05. Owner file: this one. Nothing else was edited; nothing
pushed.

Inputs read in full: `/home/ert/proj/navier-paper/main.tex` (562 lines),
`/home/ert/proj/navier-paper/references.bib`,
`research/evidence/cp01-manuscript-obligations.md`,
`research/evidence/cp01-literature-statements.md`,
`research/evidence/cp02-review-pressure.md` (the round-1 audit, verdict
REPAIR), the Conventions/regularity block of the sibling lane
`research/evidence/cp02-energy-enstrophy.md` (interface only), and
`/home/ert/proj/navier-formal/NavierFormal/Regularization.lean` (header and
the five lemmas named in Remark `rem:lean-majorant`). Primary source
re-opened **in this lane**: Tao, *Analysis & PDE* 6 (2013) 25–107, publisher
PDF (`msp.org/apde/2013/6-1/apde-v6-n1-p02-s.pdf`), printed pages 26–28 and
34–38 read as page images; the printed page numbers below are taken from the
running heads of those images.

Binding controller decisions used: (D1) conventions, (D2) regularity package
R = Proposition `prop:localtheory`, (D4) integrated form and the
`(∇u)^T u` convention, (D5) standard of proof. Nothing here touches (D3).

## 0. What changed in round 2 (summary; details in §6)

The audit found no invalid mathematical bridge. Every displayed formula,
constant, exponent and sign of round 1 is retained unchanged. The repairs:

1. **Citation layer** (the audit's first defective element). Tao's page
   numbers corrected and re-verified in this lane: Fourier convention
   **p. 35** (was 37), `Δ^{-1}` (14) **p. 38** (unchanged), vector/tensor
   extension **p. 38**, normalised pressure (9) **p. 28** with its periodic
   scoping and the remark that extends it to smooth finite-energy solutions
   on `R^3` (was cited bare, and the fact table said "p. 5"). The `H^s`
   definition (p. 36, was 38) is no longer needed and no longer cited.
2. **Sourcing of textbook facts** (the audit's second defective element).
   Plancherel, the distributional symbol of `∂_j`, Hölder, dominated
   convergence, Tonelli/Fubini, the mean value theorem and the fundamental
   theorem of calculus now carry `\cite` commands inside the LaTeX block
   (`SteinWeiss1971`, `RudinRCA`, `RudinPMA`, chapter-level, labelled [MO]
   in §3; bib records supplied in §2.3).
3. **`lem:pressure-convention`**: statement cites (9) with its scope; the
   identification of `R_iR_j(u_iu_j)` with the pressure of
   `prop:localtheory` is now an explicit almost-everywhere / continuous-
   representative step before `eq:NS` is used pointwise.
4. **Unnecessary dependencies removed**: `lem:embedding` deleted (R hands
   the lane `u,p ∈ C([0,T];L^q)` directly); (R1) deleted and (R3) narrowed
   to exactly the memberships consumed; the `L^2` Fourier inversion theorem
   and the `π^2` weight integral disappear with it.
5. **Notation**: the integrand functions are renamed `V` (dissipation
   density) and `W` (pressure-work density) to avoid the three-way collision
   `Θ`/`θ`/`ϑ`; `ϑ` in `lem:diff-under-integral` becomes `λ`.
6. **Editorial**: `prop:pressure`(i) bounds displayed with a label;
   `eq:constants` replaced by named "section constants"; the relation remark
   labelled `rem:old-form`; `rem:differential-form` names the subsequence
   principle; the cutoff `χ_R` constructed once, in the same form as the
   sibling lane, with an integration note.

## 1. Obligations discharged

| id | content | where |
|---|---|---|
| P-0 | `D_3`, `P_3` defined through `(∇u)^T u`; no `∇|u|`, no a.e. statement; the "integrand := 0 where u = 0" convention is the continuous extension (Lemma `lem:integrands`), so measurability follows from continuity | Definition `def:D3P3`, Lemma `lem:integrands`, Proposition `prop:pressure`(i) |
| P-1 | Fourier/Riesz convention fixed with sources; `R_iR_j(u_iu_j) = −Δ^{-1}∂_i∂_j(u_iu_j)` = Tao's normalised pressure (symbol computation, well-definedness in Tao's sense checked); identification with the pressure of `prop:localtheory` via the continuous representative; `p ∈ C([0,T];L^2∩L^∞)` from R (no Calderón–Zygmund) | Lemma `lem:pressure-convention` |
| P-2 | every cutoff error displayed and bounded by `C R^{-1} ×` a named quantity; both limits `R → ∞` and `ε ↓ 0` by dominated convergence with the exact memberships; the `ε`-uniform majorant `|H_ε(a)| ≤ 2(|a|^2+|a|^3)` proved on paper | Lemma `lem:reg-calculus`, proof of `prop:pressure`, Steps 3–6 |
| P-3 | balance stated and proved in integrated form for `0 ≤ s ≤ t < T_*`; differential form only as a remark with the missing continuity named | Proposition `prop:pressure`(ii), Remark `rem:differential-form` |
| eq:pressure-consequence | integrated corollary under `hyp:absorption`, with the `(1−θ)ν∫D_3` control, and `hyp:absorption ⟹ hyp:critical` with `M = (‖u_0‖_3^3 + 3A)^{1/3}` | Corollary `cor:absorption-consequence` |
| (P-invariance) | `P_3` unchanged under `p → p + c(t)`, proved without `L^1` of `u` (uses `ρ_ε = r_ε − √ε`) | Proposition `prop:pressure`(iv), Step 7 |

No hypothesis was added and no statement was weakened relative to round 1.

Labels retained: `prop:pressure`, `eq:pressure-balance`,
`eq:pressure-consequence`; `hyp:absorption`, `hyp:critical` are referenced,
not restated. New labels: `def:D3P3`, `lem:integrands`,
`lem:pressure-convention`, `lem:reg-calculus`, `lem:divergence`,
`lem:diff-under-integral`, `cor:absorption-consequence`, `rem:old-form`,
`rem:differential-form`, `rem:lean-majorant`, `eq:D3-def`, `eq:P3-def`,
`eq:D3P3-bounds`, `eq:HEps-majorant`, `eq:cutoff-identity`,
`eq:eps-identity`. Removed since round 1: `lem:embedding`, `lem:psi-theta`
(now `lem:integrands`), `eq:constants`.

## 2. Replacement text

### 2.1 Environments and placement

Environments used beyond `theorem/proposition/hypothesis/remark`:
`lemma`, `definition`, `corollary`. The integrator adds to the preamble
```latex
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
```
(the sibling lane `cp02-energy-enstrophy.md` already declares the first and
the third; only `corollary` is new).

Placement: the block in §2.2 replaces, in Section 4 of `main.tex`,
everything from `\section{A signed critical balance}` through the end of
the proof of `prop:pressure` (`main.tex` lines 199–254). The Littlewood–Paley
paragraph, `prop:lowpressure`, `hyp:highpressure`, `hyp:absorption` and the
two prose paragraphs after them are owned by other lanes and are not
reproduced; the minimal patch those lanes need is in §2.4. Corollary
`cor:absorption-consequence` (§2.2, second block) replaces the paragraph
"For later use, integrating \eqref{eq:pressure-balance} …" (`main.tex`
lines 345–353). In Section 5 the sentence "Hypothesis~\ref{hyp:absorption}
implies Hypothesis~\ref{hyp:critical}, with \[ M(\nu,u_0,H)=\dots \] by
\eqref{eq:pressure-consequence}." becomes "Hypothesis~\ref{hyp:absorption}
implies Hypothesis~\ref{hyp:critical} with
$M(\nu,u_0,H)=(\norm{u_0}_3^3+3A(\nu,u_0,H))^{1/3}$, by
Corollary~\ref{cor:absorption-consequence}(ii)."

Integration notes (interfaces with the sibling lane, not defects of either):

* The `\subsection*{Conventions}` below and the sibling lane's Conventions
  paragraph both fix the Fourier convention and the cutoff `χ_R`. Keep one
  merged paragraph; the sibling lane's `\cite[p.~14]{Tao2013}` and
  `\cite[p.~15]{Tao2013}` are arXiv pages and must become the printed
  APDE pages **35** and **36** (references.bib's `Tao2013` is the APDE
  article, pages 25–107).
* `lem:divergence` below (compactly supported `C^1` fields) is the special
  case of the sibling lane's `lem:div-zero` (`g ∈ C^1`, `g, ∂_ig ∈ L^1`) that
  this lane needs. If `lem:div-zero` is adopted, delete `lem:divergence` and
  read every "Lemma~\ref{lem:divergence}" below as "Lemma~\ref{lem:div-zero}
  applied to $fg$", noting that each $f$ below has compact support so
  $fg,\partial_j(fg)\in L^1$ trivially.
* At most one Lean remark (`rem:lean` of the sibling lane, or
  `rem:lean-majorant` below) should reach the manuscript, and the companion
  development needs a citable record (repository and commit) in
  `references.bib`.

### 2.2 The LaTeX block

```latex
\section{A signed critical balance}

\subsection*{Conventions}

Throughout this section $|\cdot|$ is the Euclidean norm on $\R^3$ and the
Frobenius norm on $3\times3$ matrices.  For a vector field $u$ we write
$(\nabla u)_{ij}=\partial_ju_i$, so that $|\nabla u|^2=\sum_{i,j}(\partial_ju_i)^2$,
and $(\nabla u)^{\mathsf T}u$ denotes the vector with components
\[
 \bigl((\nabla u)^{\mathsf T}u\bigr)_j=\sum_i u_i\,\partial_ju_i .
\]
With this notation $(u\otimes u):\nabla u:=\sum_{i,j}u_iu_j\partial_ju_i
=u\cdot(\nabla u)^{\mathsf T}u$.  Where $u\neq0$ one has
$(\nabla u)^{\mathsf T}u=|u|\nabla|u|$, but $\nabla|u|$ is never used below.
We write $\norm\cdot_q$ for $\norm\cdot_{L^q(\R^3)}$ and use H\"older's
inequality on $\R^3$ in the form
$\int|fg|\,dx\leq\norm f_r\norm g_{r'}$, $1\leq r\leq\infty$, $1/r+1/r'=1$
\cite[Ch.~3]{RudinRCA}; the case $r=r'=2$ is the Cauchy--Schwarz
inequality, and the Cauchy--Schwarz inequality on $\R^3$ and on
$\R^{3\times3}$ is the elementary one.

The Fourier transform is $\hat f(\xi)=\int_{\R^3}e^{-2\pi ix\cdot\xi}f(x)\,dx$
for $f\in L^1$, extended to tempered distributions in the usual manner; this
is the convention of \cite[p.~35]{Tao2013}.  On $L^2$ the transform is the
unitary extension given by Plancherel's theorem,
$\norm{\hat f}_2=\norm f_2$ \cite[Ch.~I, \S2]{SteinWeiss1971}.
Consequently, for a measurable $m$ defined almost everywhere on $\R^3$ with
$\norm m_\infty<\infty$, the multiplier $T_mf:=\mathcal F^{-1}(m\hat f)$
satisfies $\norm{T_mf}_2=\norm{m\hat f}_2\leq\norm m_\infty\norm f_2$, so
$T_m$ is bounded on $L^2$ with norm at most $\norm m_\infty$.  For a
tempered distribution $f$, $\widehat{\partial_jf}=2\pi i\xi_j\hat f$
\cite[Ch.~I, \S3]{SteinWeiss1971}; hence $\partial_i\partial_j$ has symbol
$-4\pi^2\xi_i\xi_j$ and $-\Delta$ has symbol $4\pi^2|\xi|^2$.  The Riesz
transforms are the multipliers $\widehat{R_jf}=-i\,\xi_j|\xi|^{-1}\hat f$
(the symbol is defined for $\xi\neq0$, hence almost everywhere, and is
bounded by $1$), so $R_iR_j$ is the $L^2$-bounded multiplier with symbol
$-\xi_i\xi_j/|\xi|^2$, of norm at most $1$.  The inverse Laplacian is the
multiplier of \cite[eq.~(14), p.~38]{Tao2013},
$\widehat{\Delta^{-1}f}(\xi)=-\bigl(4\pi^2|\xi|^2\bigr)^{-1}\hat f(\xi)$,
``well-defined for any tempered distribution $f$ for which the right-hand
side is locally integrable'' (loc.\ cit.).  Vector fields are measured
componentwise, $\norm u_q:=\norm{|u|}_q$, which is one of the equivalent
tensor-valued conventions of \cite[p.~38]{Tao2013}.

We fix once and for all a cutoff.  Let $g(s)=e^{-1/s}$ for $s>0$ and
$g(s)=0$ for $s\leq0$.  On $(0,\infty)$ each derivative $g^{(k)}$ has the
form $P_k(1/s)e^{-1/s}$ with a polynomial $P_k$ (induction on $k$), so
$g^{(k)}(s)\to0$ and $g^{(k)}(s)/s\to0$ as $s\downarrow0$; by induction on
$k$ this gives $g^{(k)}(0)=0$ for every $k$, i.e.\ $g\in C^\infty(\R)$.  Put
$\eta(r)=g(2-r)/\bigl(g(2-r)+g(r-1)\bigr)$; the denominator is positive for
every $r$ (at least one of $2-r$, $r-1$ is positive), so
$\eta\in C^\infty(\R)$, $0\leq\eta\leq1$, $\eta=1$ on $(-\infty,1]$ and
$\eta=0$ on $[2,\infty)$.  Set $\chi(x):=\eta(|x|)$; since $\eta$ is
constant on $(-\infty,1]$ and $x\mapsto|x|$ is smooth on $\R^3\setminus\{0\}$,
$\chi\in C_c^\infty(\R^3)$ with $0\leq\chi\leq1$, $\chi=1$ on $\{|x|\leq1\}$,
$\chi=0$ on $\{|x|\geq2\}$.  For $R>0$ let $\chi_R(x)=\chi(x/R)$.  Then
$\chi_R\in C_c^\infty(\R^3)$, $\chi_R=1$ on $\{|x|\leq R\}$,
$\operatorname{supp}\chi_R\subset\{|x|\leq2R\}$,
$\nabla\chi_R(x)=R^{-1}(\nabla\chi)(x/R)$ vanishes unless $R\leq|x|\leq2R$,
$\norm{\nabla\chi_R}_\infty=R^{-1}\norm{\nabla\chi}_\infty$, and
$\chi_R(x)\to1$ as $R\to\infty$ for every $x$.

\subsection*{The regularity used}

Let $u$ be the classical branch of Proposition~\ref{prop:localtheory} with
datum $u_0$ and maximal time $T_*$, and let $p$ be its normalised pressure.
We use exactly the following consequences of that proposition, valid for
every $0<T<T_*$:
\begin{enumerate}
\item[(R2)] $u\in C^\infty([0,T]\times\R^3)^3$ and $p\in C^\infty([0,T]\times\R^3)$,
 equation~\eqref{eq:NS} holds pointwise on $[0,T]\times\R^3$, and $u(0)=u_0$;
\item[(R3)] $u\in C([0,T];L^q)$ for $q\in\{2,3,4,\infty\}$,
 $\nabla u\in C([0,T];L^2)$, and $p\in C([0,T];L^2)\cap C([0,T];L^\infty)$.
\end{enumerate}
(Proposition~\ref{prop:localtheory} gives more: $u,p\in C^j([0,T];H^k)$
for all $j,k\geq0$, and $u,\nabla u,\Delta u,\partial_tu,p,\nabla p\in
C([0,T];L^q)$ for every $2\leq q\leq\infty$.  Nothing beyond (R2)--(R3) is
used in this section.)  Since a continuous curve in $L^q$ has a continuous
norm, for every $0<T<T_*$ the \emph{section constants}
\[
 K_q:=\max_{0\leq\tau\leq T}\norm{u(\tau)}_q\quad(q=2,3,4,\infty),\qquad
 G:=\max_{0\leq\tau\leq T}\norm{\nabla u(\tau)}_2,\qquad
 \Pi_q:=\max_{0\leq\tau\leq T}\norm{p(\tau)}_q\quad(q=2,\infty)
\]
are finite.  They depend on $T$, and $T$ is fixed wherever they are used.

\begin{lemma}[The normalised pressure]\label{lem:pressure-convention}
Fix $0<T<T_*$ and $t\in[0,T]$, and put
$\tilde p(t):=\sum_{i,j}R_iR_j\bigl(u_i(t)u_j(t)\bigr)$, the
$L^2$-multiplier with symbol $-\xi_i\xi_j/|\xi|^2$ applied to
$u_iu_j\in L^2$ and summed.  Then:
\begin{enumerate}
\item[(a)] $\Delta^{-1}\partial_i\partial_j(u_iu_j)$ is well defined in the
 sense of \cite[eq.~(14), p.~38]{Tao2013}, and
 $\tilde p(t)=-\sum_{i,j}\Delta^{-1}\partial_i\partial_j(u_iu_j)$ as
 elements of $L^2$; that is, $\tilde p$ is the normalised pressure in the
 sense of \cite[eq.~(9), p.~28, and the remark following it]{Tao2013} with
 $f=0$.  (Tao introduces (9) for periodic smooth solutions; the remark
 following it records that the same normalisation can be imposed for smooth
 finite-energy solutions on $\R^3$, because $\partial_i\partial_j(u_iu_j)$
 is a second derivative of an $L^1(\R^3)$ function.)
\item[(b)] $-\Delta\tilde p=\sum_{i,j}\partial_i\partial_j(u_iu_j)$ in the
 sense of tempered distributions.
\item[(c)] The normalised pressure $p$ of Proposition~\ref{prop:localtheory}
 is the smooth representative of $\tilde p$: $p(t,\cdot)=\tilde p(t)$
 almost everywhere for every $t$.  We write $p$ for both from now on; thus
 $p=R_iR_j(u_iu_j)$, $p$ satisfies (R2)--(R3), and in particular
 $p\in C([0,T];L^2)\cap C([0,T];L^\infty)$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) $u_iu_j\in L^2$ because $u(t)\in L^4$ by (R3) and
$\norm{u_iu_j}_2\leq\norm{|u|^2}_2=\norm u_4^2$.  With the symbol of
$\partial_i\partial_j$ from the Conventions,
$\widehat{\partial_i\partial_j(u_iu_j)}=-4\pi^2\xi_i\xi_j\,\widehat{u_iu_j}$
as tempered distributions, and this is an $L^2$ function.  The right-hand
side of \cite[eq.~(14)]{Tao2013} applied to
$f=\partial_i\partial_j(u_iu_j)$ is therefore
$-(4\pi^2|\xi|^2)^{-1}\cdot(-4\pi^2\xi_i\xi_j)\widehat{u_iu_j}
=\xi_i\xi_j|\xi|^{-2}\,\widehat{u_iu_j}$ for $\xi\neq0$, which is bounded by
$|\widehat{u_iu_j}|\in L^2$, hence locally integrable; so
$\Delta^{-1}\partial_i\partial_j(u_iu_j)$ is well defined in Tao's sense and
is the $L^2$ function with Fourier transform
$\xi_i\xi_j|\xi|^{-2}\widehat{u_iu_j}$.  Multiplying by $-1$ gives
$-\xi_i\xi_j|\xi|^{-2}\widehat{u_iu_j}$, which is exactly the symbol of
$R_iR_j$ times $\widehat{u_iu_j}$; by Plancherel two $L^2$ functions with the
same Fourier transform coincide, so
$-\Delta^{-1}\partial_i\partial_j(u_iu_j)=R_iR_j(u_iu_j)$ in $L^2$.  Summing
over $i,j$ gives (a).

(b) Multiplying the symbol $-\xi_i\xi_j/|\xi|^2$ of $R_iR_j$ by the symbol
$4\pi^2|\xi|^2$ of $-\Delta$ gives $-4\pi^2\xi_i\xi_j$, the symbol of
$\partial_i\partial_j$; since $R_iR_j(u_iu_j)\in L^2$ is a tempered
distribution, $-\Delta R_iR_j(u_iu_j)=\partial_i\partial_j(u_iu_j)$ as
tempered distributions.  Sum over $i,j$.

(c) Proposition~\ref{prop:localtheory} is stated for the normalised pressure,
i.e.\ for the $L^2$ class in (a); its conclusion (R2) supplies a
representative $p(t,\cdot)$ of that class which is smooth on
$[0,T]\times\R^3$ and satisfies \eqref{eq:NS} pointwise.  Two representatives
of one $L^2$ class agree almost everywhere, and at most one of them is
continuous (two continuous functions that agree almost everywhere agree
everywhere, since the set where they differ is open and a nonempty open set
has positive measure).  We therefore identify $\tilde p(t)$ with that smooth
representative; (R2)--(R3) apply to it by Proposition~\ref{prop:localtheory},
which gives the last statement.
\end{proof}

\subsection*{The two nonlinear integrands}

\begin{lemma}[Continuous extension across the zero set]\label{lem:integrands}
Define $V,W:\R^3\times\R^{3\times3}\to\R$ by
\[
 V(a,\mathsf G)=\frac{|\mathsf G^{\mathsf T}a|^2}{|a|},\qquad
 W(a,\mathsf G)=\frac{a\cdot\mathsf G^{\mathsf T}a}{|a|}\quad(a\neq0),
 \qquad V(0,\mathsf G)=W(0,\mathsf G)=0 .
\]
Then: (i) $|\mathsf G^{\mathsf T}a|\leq|\mathsf G|\,|a|$;
(ii) $0\leq V(a,\mathsf G)\leq|a|\,|\mathsf G|^2$ and
$|W(a,\mathsf G)|\leq|a|\,|\mathsf G|$;
(iii) $V$ and $W$ are continuous on $\R^3\times\R^{3\times3}$;
(iv) for $\varepsilon>0$ put $r_\varepsilon(a)=(|a|^2+\varepsilon)^{1/2}$; then
$|\mathsf G^{\mathsf T}a|^2/r_\varepsilon(a)\leq|a||\mathsf G|^2$,
$|a\cdot\mathsf G^{\mathsf T}a|/r_\varepsilon(a)\leq|a||\mathsf G|$, and as
$\varepsilon\downarrow0$,
$|\mathsf G^{\mathsf T}a|^2/r_\varepsilon(a)\uparrow V(a,\mathsf G)$ and
$a\cdot\mathsf G^{\mathsf T}a/r_\varepsilon(a)\to W(a,\mathsf G)$ for
every $(a,\mathsf G)$.
\end{lemma}

\begin{proof}
(i) $(\mathsf G^{\mathsf T}a)_j=\sum_i\mathsf G_{ij}a_i$, so by the
Cauchy--Schwarz inequality on $\R^3$,
$|(\mathsf G^{\mathsf T}a)_j|^2\leq(\sum_i\mathsf G_{ij}^2)|a|^2$; sum over $j$.
(ii) For $a\neq0$ divide (i) squared by $|a|$; and
$|a\cdot\mathsf G^{\mathsf T}a|\leq|a||\mathsf G^{\mathsf T}a|\leq|a|^2|\mathsf G|$.
For $a=0$ both sides vanish.
(iii) On the open set $\{a\neq0\}$ both functions are quotients of
polynomials by the nonvanishing continuous function $|a|$.  At a point
$(0,\mathsf G_0)$, (ii) gives $|V(a,\mathsf G)|\leq|a||\mathsf G|^2\to0$ and
$|W(a,\mathsf G)|\leq|a||\mathsf G|\to0$ as $(a,\mathsf G)\to(0,\mathsf G_0)$.
(iv) $r_\varepsilon(a)\geq|a|$ gives the two bounds via (i).  If $a\neq0$
then $r_\varepsilon(a)\downarrow|a|>0$, so the quotients converge to
$V,W$, the first one increasingly.  If $a=0$ then
$\mathsf G^{\mathsf T}a=0$ and every quantity is $0$.
\end{proof}

\begin{definition}[Weighted dissipation and pressure work]\label{def:D3P3}
For $0\leq t<T_*$ set $X(t)=\norm{u(t)}_3^3$ and
\begin{align}
 D_3(t)&:=\int_{\R^3}\Bigl(|u|\,|\nabla u|^2+V(u,\nabla u)\Bigr)(t,x)\,dx
 =\int_{\R^3}\Bigl(|u|\,|\nabla u|^2
   +\frac{|(\nabla u)^{\mathsf T}u|^2}{|u|}\Bigr)dx,\label{eq:D3-def}\\
 P_3(t)&:=\int_{\R^3}p\,W(u,\nabla u)(t,x)\,dx
 =\int_{\R^3}p\,\frac{(u\otimes u):\nabla u}{|u|}\,dx,\label{eq:P3-def}
\end{align}
where, by Lemma~\ref{lem:integrands}, the second integrand in
\eqref{eq:D3-def} and the integrand in \eqref{eq:P3-def} are understood as
$0$ at points where $u=0$; this is their unique continuous extension.
\end{definition}

\subsection*{Three elementary tools}

\begin{lemma}[Regularised speed and its primitive]\label{lem:reg-calculus}
For $\varepsilon>0$ and $a\in\R^3$ let
\[
 r_\varepsilon(a)=(|a|^2+\varepsilon)^{1/2},\qquad
 H_\varepsilon(a)=\tfrac13\bigl((|a|^2+\varepsilon)^{3/2}-\varepsilon^{3/2}\bigr).
\]
\begin{enumerate}
\item[(i)] $r_\varepsilon,H_\varepsilon\in C^\infty(\R^3)$ with
 $\nabla_aH_\varepsilon(a)=r_\varepsilon(a)\,a$ and
 $\nabla_ar_\varepsilon(a)=a/r_\varepsilon(a)$.
\item[(ii)] $|a|\leq r_\varepsilon(a)\leq|a|+\sqrt\varepsilon$ and
 $0\leq H_\varepsilon(a)\leq|a|^2r_\varepsilon(a)\leq|a|^2(|a|+\sqrt\varepsilon)$.
 In particular, for $0<\varepsilon\leq1$,
 \begin{equation}\label{eq:HEps-majorant}
  |H_\varepsilon(a)|\leq 2\bigl(|a|^2+|a|^3\bigr).
 \end{equation}
\item[(iii)] As $\varepsilon\downarrow0$: $r_\varepsilon(a)\downarrow|a|$ and
 $H_\varepsilon(a)\to|a|^3/3$, for every $a$.
\item[(iv)] $(r_\varepsilon(a)-\sqrt\varepsilon)\,|a|\leq|a|^2$.
\end{enumerate}
\end{lemma}

\begin{proof}
(i) $|a|^2+\varepsilon\geq\varepsilon>0$, so both functions are compositions
of smooth maps; the chain rule gives
$\nabla_ar_\varepsilon=\tfrac12(|a|^2+\varepsilon)^{-1/2}\cdot2a=a/r_\varepsilon$
and $\nabla_aH_\varepsilon=\tfrac13\cdot\tfrac32(|a|^2+\varepsilon)^{1/2}\cdot2a
=r_\varepsilon a$.
(ii) $|a|^2\leq|a|^2+\varepsilon\leq(|a|+\sqrt\varepsilon)^2$ gives the first
chain.  Write $r=r_\varepsilon(a)$, $s=\sqrt\varepsilon$, so $r\geq s\geq0$ and
$r^2-s^2=|a|^2$.  Then $H_\varepsilon(a)=\tfrac13(r^3-s^3)\geq0$ and
\[
 r^3-s^3=(r-s)(r^2+rs+s^2)\leq(r-s)\cdot3r^2
 =\frac{r^2-s^2}{r+s}\cdot3r^2\leq\frac{|a|^2}{r}\cdot3r^2=3r|a|^2,
\]
so $H_\varepsilon(a)\leq r|a|^2\leq|a|^2(|a|+\sqrt\varepsilon)$.  If
$\varepsilon\leq1$ this is at most $|a|^3+|a|^2\leq2(|a|^2+|a|^3)$, and
$H_\varepsilon\geq0$ gives \eqref{eq:HEps-majorant}.
(iii) $\varepsilon\mapsto r_\varepsilon(a)$ is increasing with limit
$(|a|^2)^{1/2}=|a|$; and $(x,\varepsilon)\mapsto(x+\varepsilon)^{3/2}-\varepsilon^{3/2}$
is continuous on $[0,\infty)^2$, so $H_\varepsilon(a)\to\tfrac13|a|^3$.
(iv) $r_\varepsilon(a)-\sqrt\varepsilon=|a|^2/(r_\varepsilon(a)+\sqrt\varepsilon)
\leq|a|^2/r_\varepsilon(a)\leq|a|$, by (ii).
\end{proof}

\begin{lemma}[Divergence theorem for compactly supported $C^1$ fields]
\label{lem:divergence}
If $F\in C^1(\R^3;\R^3)$ has compact support, then
$\int_{\R^3}\operatorname{div}F\,dx=0$.  Consequently, if $f\in C^1(\R^3)$
has compact support and $g\in C^1(\R^3)$, then
$\int f\,\partial_jg\,dx=-\int(\partial_jf)\,g\,dx$ for $j=1,2,3$, and for a
$C^1$ vector field $g$, $\int f\operatorname{div}g\,dx=-\int\nabla f\cdot g\,dx$.
\end{lemma}

\begin{proof}
Choose $L$ with $\operatorname{supp}F\subset[-L,L]^3$.  For $j=1$ (the other
indices are identical), the integrand $\partial_1F_1$ is continuous with
compact support, hence bounded and integrable, so Fubini's theorem
\cite[Ch.~8]{RudinRCA} applies and
\[
 \int_{\R^3}\partial_1F_1\,dx
 =\int_{\R^2}\Bigl(\int_{-L}^{L}\partial_1F_1(x_1,x')\,dx_1\Bigr)dx'
 =\int_{\R^2}\bigl(F_1(L,x')-F_1(-L,x')\bigr)dx'=0
\]
by the fundamental theorem of calculus \cite[Ch.~6]{RudinPMA} applied to
the $C^1$ function $x_1\mapsto F_1(x_1,x')$, which vanishes at $\pm L$.
Summing over $j$ gives the first claim.  For the second, apply it to
$F=fg\,e_j$, which is $C^1$ with compact support, and use
$\partial_j(fg)=(\partial_jf)g+f\partial_jg$; the third claim is the sum of
the second over $j$.
\end{proof}

\begin{lemma}[Differentiation under the integral sign]
\label{lem:diff-under-integral}
Let $K\subset\R^3$ be compact and let $F:[0,T]\times\R^3\to\R$ be continuous
with continuous partial derivative $\partial_tF$, and suppose
$F(t,x)=0$ for all $t$ whenever $x\notin K$.  Then
$\Phi(t):=\int_{\R^3}F(t,x)\,dx$ belongs to $C^1([0,T])$ and
$\Phi'(t)=\int_{\R^3}\partial_tF(t,x)\,dx$.
\end{lemma}

\begin{proof}
$\partial_tF$ vanishes off $K$ as well (it is the derivative of the zero
function there), and it is uniformly continuous on the compact set
$[0,T]\times K$.  Fix $t$ and $h\neq0$ with $t+h\in[0,T]$.  For each $x\in K$
the mean value theorem \cite[Ch.~5]{RudinPMA} applied to
$\tau\mapsto F(\tau,x)$ gives $F(t+h,x)-F(t,x)=h\,\partial_tF(t+\lambda h,x)$
for some $\lambda=\lambda(x,h)\in(0,1)$.  Hence
\[
 \Bigl|\frac{\Phi(t+h)-\Phi(t)}{h}-\int_K\partial_tF(t,x)\,dx\Bigr|
 \leq|K|\sup\bigl\{|\partial_tF(\sigma,x)-\partial_tF(t,x)|:
 x\in K,\ |\sigma-t|\leq|h|\bigr\},
\]
which tends to $0$ as $h\to0$ by uniform continuity.  The same uniform
continuity shows that $t\mapsto\int_K\partial_tF(t,x)\,dx$ is continuous.
\end{proof}

\subsection*{The balance}

\begin{proposition}[Exact pressure balance, integrated form]\label{prop:pressure}
Let $u$ be the classical branch of Proposition~\ref{prop:localtheory} with
normalised pressure $p=R_iR_j(u_iu_j)$ (Lemma~\ref{lem:pressure-convention}),
and let $X$, $D_3$, $P_3$ be as in Definition~\ref{def:D3P3}.
\begin{enumerate}
\item[(i)] For every $0<T<T_*$ the integrands in \eqref{eq:D3-def} and
 \eqref{eq:P3-def} are continuous on $[0,T]\times\R^3$; pointwise
 $0\leq V(u,\nabla u)\leq|u||\nabla u|^2$; and for every $t\in[0,T_*)$
 \begin{equation}\label{eq:D3P3-bounds}
  0\leq D_3(t)\leq2\int_{\R^3}|u||\nabla u|^2dx
  \leq2\norm{u(t)}_\infty\norm{\nabla u(t)}_2^2,\qquad
  |P_3(t)|\leq\norm{p(t)}_\infty\norm{u(t)}_2\norm{\nabla u(t)}_2 .
 \end{equation}
 The functions $t\mapsto D_3(t)$ and $t\mapsto P_3(t)$ are Lebesgue
 measurable and bounded on $[0,T]$, hence integrable on every
 $[s,t]\subset[0,T_*)$.
\item[(ii)] For every $0\leq s\leq t<T_*$,
 \begin{equation}\label{eq:pressure-balance}
  \frac13X(t)-\frac13X(s)+\nu\int_s^tD_3(\tau)\,d\tau=\int_s^tP_3(\tau)\,d\tau .
 \end{equation}
\item[(iii)] $X\in C([0,T_*))$.
\item[(iv)] For every $t\in[0,T_*)$, $\int_{\R^3}W(u,\nabla u)(t,x)\,dx=0$.
 Consequently $P_3(t)$ is unchanged if $p$ is replaced by $p+c(t)$ for any
 function $c:[0,T_*)\to\R$.
\end{enumerate}
\end{proposition}

\begin{proof}
\emph{Step 1 (regularity and (i)).}  Fix $0<T<T_*$.  By (R2), $u$ and
$\nabla u$ are continuous on $[0,T]\times\R^3$, and by
Lemma~\ref{lem:integrands}(iii) so are $|u||\nabla u|^2+V(u,\nabla u)$ and
$p\,W(u,\nabla u)$ (with $p$ continuous by (R2) and
Lemma~\ref{lem:pressure-convention}(c)).  Lemma~\ref{lem:integrands}(ii)
gives $0\leq V(u,\nabla u)\leq|u||\nabla u|^2$ and
$|p\,W(u,\nabla u)|\leq|p||u||\nabla u|$.  Hence, for each $t$,
$0\leq D_3(t)\leq2\int|u||\nabla u|^2\leq2\norm{u(t)}_\infty\norm{\nabla u(t)}_2^2\leq2K_\infty G^2$
and, bounding $|p|$ by $\norm{p(t)}_\infty$ and then applying the
Cauchy--Schwarz inequality to $|u||\nabla u|$,
$|P_3(t)|\leq\norm{p(t)}_\infty\norm{u(t)}_2\norm{\nabla u(t)}_2\leq\Pi_\infty K_2G$,
with the section constants.  This is \eqref{eq:D3P3-bounds}.  Both
integrands are continuous, hence Borel measurable on $[0,T]\times\R^3$; the
first is nonnegative and the second is bounded by $|p||u||\nabla u|$, whose
iterated integral is at most $T\,\Pi_\infty K_2G<\infty$.  Tonelli's theorem
(for $D_3$) and Fubini's theorem (for $P_3$) \cite[Ch.~8]{RudinRCA}
therefore give measurability of $t\mapsto D_3(t)$ and $t\mapsto P_3(t)$ on
$[0,T]$; boundedness was shown above.  This proves (i).

\emph{Step 2 (set-up).}  Fix $0\leq s\leq t<T_*$, choose $T$ with
$t<T<T_*$, and use the section constants for this $T$ and the cutoff
$\chi_R$, $R\geq1$, of the Conventions.  Fix $\varepsilon\in(0,1]$ and write
$r_\varepsilon=r_\varepsilon(u)$, $H_\varepsilon=H_\varepsilon(u)$
(Lemma~\ref{lem:reg-calculus}), functions of $(\tau,x)$ which by (R2) and
Lemma~\ref{lem:reg-calculus}(i) are $C^\infty$ on $[0,T]\times\R^3$.

\emph{Step 3 (time derivative).}  Let
$\Phi_{\varepsilon,R}(\tau):=\int_{\R^3}\chi_R(x)H_\varepsilon(u(\tau,x))\,dx$.
The integrand is continuous on $[0,T]\times\R^3$, vanishes for $|x|>2R$,
and by the chain rule and Lemma~\ref{lem:reg-calculus}(i) has the continuous
partial derivative
$\partial_\tau\bigl(\chi_RH_\varepsilon(u)\bigr)=\chi_R\,r_\varepsilon\,u\cdot\partial_\tau u$.
Lemma~\ref{lem:diff-under-integral} with $K=\{|x|\leq2R\}$ gives
$\Phi_{\varepsilon,R}\in C^1([0,T])$ and
\[
 \Phi_{\varepsilon,R}'(\tau)
 =\int\chi_R\,r_\varepsilon\,u\cdot\partial_\tau u\,dx
 =\nu\int\chi_Rr_\varepsilon\,u\cdot\Delta u\,dx
  -\int\chi_Rr_\varepsilon\,u\cdot(u\cdot\nabla)u\,dx
  -\int\chi_Rr_\varepsilon\,u\cdot\nabla p\,dx,
\]
where \eqref{eq:NS} was substituted pointwise (R2).  Each of the three
integrals is over the compact set $\{|x|\leq2R\}$ of a function continuous
in $(\tau,x)$, so each is a continuous function of $\tau\in[0,T]$ (uniform
continuity on $[0,T]\times\{|x|\leq2R\}$).

\emph{Step 4 (the three space integrals at fixed $\tau$).}  All fields
below are $C^\infty$ in $x$ (R2), and every integration by parts is
Lemma~\ref{lem:divergence} with $f$ the compactly supported factor
containing $\chi_R$.

\emph{Diffusion.}  With $f=\chi_Rr_\varepsilon u_i$ and $g=\partial_ju_i$,
summed over $i,j$,
\[
 \nu\int\chi_Rr_\varepsilon u_i\,\partial_j\partial_ju_i\,dx
 =-\nu\int\partial_j(\chi_Rr_\varepsilon u_i)\,\partial_ju_i\,dx
 =-\nu\int\chi_Rr_\varepsilon|\nabla u|^2dx
  -\nu\int\chi_R(\partial_jr_\varepsilon)\,u_i\partial_ju_i\,dx
  -\nu\int(\partial_j\chi_R)\,r_\varepsilon\,u_i\partial_ju_i\,dx .
\]
By Lemma~\ref{lem:reg-calculus}(i) and the chain rule,
$\partial_jr_\varepsilon=u_k\partial_ju_k/r_\varepsilon
=((\nabla u)^{\mathsf T}u)_j/r_\varepsilon$, while
$u_i\partial_ju_i=((\nabla u)^{\mathsf T}u)_j$.  Hence
\[
 \nu\int\chi_Rr_\varepsilon\,u\cdot\Delta u\,dx
 =-\nu D_{\varepsilon,R}(\tau)+E^{\rm d}_{\varepsilon,R}(\tau),
 \qquad
 D_{\varepsilon,R}:=\int\chi_R\Bigl(r_\varepsilon|\nabla u|^2
 +\frac{|(\nabla u)^{\mathsf T}u|^2}{r_\varepsilon}\Bigr)dx,
 \qquad
 E^{\rm d}_{\varepsilon,R}:=-\nu\int r_\varepsilon\,\nabla\chi_R\cdot(\nabla u)^{\mathsf T}u\,dx .
\]
By Lemma~\ref{lem:integrands}(i), Lemma~\ref{lem:reg-calculus}(ii) with
$\varepsilon\leq1$ (so $r_\varepsilon\leq|u|+1$), and the Cauchy--Schwarz
inequality (with $\norm{|u|^2}_2=\norm u_4^2$),
\[
 |E^{\rm d}_{\varepsilon,R}(\tau)|
 \leq\frac{\nu\norm{\nabla\chi}_\infty}{R}\int(|u|^2+|u|)|\nabla u|\,dx
 \leq\frac{\nu\norm{\nabla\chi}_\infty}{R}
 \bigl(\norm{u(\tau)}_4^2+\norm{u(\tau)}_2\bigr)\norm{\nabla u(\tau)}_2
 \leq\frac{\nu\norm{\nabla\chi}_\infty}{R}\,(K_4^2+K_2)\,G .
\]

\emph{Convection.}  By Lemma~\ref{lem:reg-calculus}(i) and the chain rule,
$\partial_j\bigl(H_\varepsilon(u)\bigr)=r_\varepsilon u_i\partial_ju_i$, so
$r_\varepsilon\,u\cdot(u\cdot\nabla)u=u_j\,\partial_j(H_\varepsilon(u))$.
With $f=\chi_Ru_j$, $g=H_\varepsilon(u)$, and $\operatorname{div}u=0$,
\[
 -\int\chi_Rr_\varepsilon\,u\cdot(u\cdot\nabla)u\,dx
 =\int\partial_j(\chi_Ru_j)\,H_\varepsilon(u)\,dx
 =\int H_\varepsilon(u)\,u\cdot\nabla\chi_R\,dx
 =:E^{\rm c}_{\varepsilon,R}(\tau),
\]
and by \eqref{eq:HEps-majorant}
\[
 |E^{\rm c}_{\varepsilon,R}(\tau)|
 \leq\frac{\norm{\nabla\chi}_\infty}{R}\int2(|u|^2+|u|^3)|u|\,dx
 =\frac{2\norm{\nabla\chi}_\infty}{R}\bigl(\norm{u(\tau)}_3^3+\norm{u(\tau)}_4^4\bigr)
 \leq\frac{2\norm{\nabla\chi}_\infty}{R}(K_3^3+K_4^4).
\]

\emph{Pressure.}  With $f=\chi_Rr_\varepsilon u_i$, $g=p$, summed over $i$,
and using $\operatorname{div}(r_\varepsilon u)=r_\varepsilon\operatorname{div}u
+u\cdot\nabla r_\varepsilon=u\cdot(\nabla u)^{\mathsf T}u/r_\varepsilon$,
\[
 -\int\chi_Rr_\varepsilon\,u\cdot\nabla p\,dx
 =\int p\operatorname{div}(\chi_Rr_\varepsilon u)\,dx
 =P_{\varepsilon,R}(\tau)+E^{\rm p}_{\varepsilon,R}(\tau),
 \qquad
 P_{\varepsilon,R}:=\int\chi_R\,p\,\frac{u\cdot(\nabla u)^{\mathsf T}u}{r_\varepsilon}\,dx,
 \qquad
 E^{\rm p}_{\varepsilon,R}:=\int p\,r_\varepsilon\,u\cdot\nabla\chi_R\,dx,
\]
and by Lemma~\ref{lem:reg-calculus}(ii) and the Cauchy--Schwarz inequality
\[
 |E^{\rm p}_{\varepsilon,R}(\tau)|
 \leq\frac{\norm{\nabla\chi}_\infty}{R}\int|p|(|u|^2+|u|)\,dx
 \leq\frac{\norm{\nabla\chi}_\infty}{R}\norm{p(\tau)}_2
 \bigl(\norm{u(\tau)}_4^2+\norm{u(\tau)}_2\bigr)
 \leq\frac{\norm{\nabla\chi}_\infty}{R}\,\Pi_2\,(K_4^2+K_2).
\]

\emph{Assembly.}  Writing
$E_{\varepsilon,R}:=E^{\rm c}_{\varepsilon,R}+E^{\rm d}_{\varepsilon,R}+E^{\rm p}_{\varepsilon,R}$,
Steps 3--4 give, for every $\tau\in[0,T]$,
$\Phi_{\varepsilon,R}'(\tau)=-\nu D_{\varepsilon,R}(\tau)+P_{\varepsilon,R}(\tau)+E_{\varepsilon,R}(\tau)$.
Each of $D_{\varepsilon,R}$, $P_{\varepsilon,R}$, $E_{\varepsilon,R}$ is an
integral over the compact set $\{|x|\leq2R\}$ of a function continuous in
$(\tau,x)$, hence continuous in $\tau$ (as in Step 3).  The fundamental
theorem of calculus \cite[Ch.~6]{RudinPMA} for the $C^1$ function
$\Phi_{\varepsilon,R}$ yields
\begin{equation}\label{eq:cutoff-identity}
 \Phi_{\varepsilon,R}(t)-\Phi_{\varepsilon,R}(s)
 +\nu\int_s^tD_{\varepsilon,R}\,d\tau
 =\int_s^tP_{\varepsilon,R}\,d\tau+\int_s^tE_{\varepsilon,R}\,d\tau,
 \qquad
 \Bigl|\int_s^tE_{\varepsilon,R}\,d\tau\Bigr|\leq\frac{(t-s)\,C_E}{R},
\end{equation}
with $C_E:=\norm{\nabla\chi}_\infty\bigl(2(K_3^3+K_4^4)+\nu(K_4^2+K_2)G+\Pi_2(K_4^2+K_2)\bigr)$
independent of $R$ and of $\varepsilon\in(0,1]$.

\emph{Step 5 ($R\to\infty$, $\varepsilon$ fixed).}  Let $R=n\to\infty$
through the integers.  For every $x$, $\chi_n(x)=1$ once $n\geq|x|$.  All
limits in this step and the next are taken by the dominated convergence
theorem \cite[Ch.~1]{RudinRCA}, on $\R^3$ or on $[s,t]\times\R^3$ with
Lebesgue measure.

(a) $|\chi_nH_\varepsilon(u(t))|\leq2(|u(t)|^2+|u(t)|^3)$ by
\eqref{eq:HEps-majorant}, and the majorant is integrable because
$u(t)\in L^2\cap L^3$ (R3).  Dominated convergence gives
$\Phi_{\varepsilon,n}(t)\to\int H_\varepsilon(u(t))\,dx$, and likewise at $s$.

(b) The integrand of $D_{\varepsilon,n}$ is
$g_n:=\chi_n\bigl(r_\varepsilon|\nabla u|^2+|(\nabla u)^{\mathsf T}u|^2/r_\varepsilon\bigr)$,
continuous and nonnegative on $[s,t]\times\R^3$, with
$0\leq g_n\leq g:=(2|u|+1)|\nabla u|^2$ by Lemma~\ref{lem:reg-calculus}(ii)
($\varepsilon\leq1$) and Lemma~\ref{lem:integrands}(iv).  By Tonelli's
theorem \cite[Ch.~8]{RudinRCA}
\[
 \int_s^t\!\!\int_{\R^3}g\,dx\,d\tau
 \leq\int_s^t(2\norm{u(\tau)}_\infty+1)\norm{\nabla u(\tau)}_2^2\,d\tau
 \leq(t-s)(2K_\infty+1)G^2<\infty .
\]
Dominated convergence on $[s,t]\times\R^3$ and Fubini's theorem give
$\int_s^tD_{\varepsilon,n}\,d\tau\to\int_s^tD_\varepsilon\,d\tau$, where
$D_\varepsilon(\tau):=\int\bigl(r_\varepsilon|\nabla u|^2+|(\nabla u)^{\mathsf T}u|^2/r_\varepsilon\bigr)dx$
is a measurable function of $\tau$ bounded by $(2K_\infty+1)G^2$.

(c) The integrand of $P_{\varepsilon,n}$ is
$h_n:=\chi_n\,p\,u\cdot(\nabla u)^{\mathsf T}u/r_\varepsilon$, continuous on
$[s,t]\times\R^3$, with $|h_n|\leq h:=|p||u||\nabla u|$ by
Lemma~\ref{lem:integrands}(iv), and
$\int_s^t\!\int h\,dx\,d\tau\leq(t-s)\Pi_\infty K_2G<\infty$ (Tonelli, as in
Step 1).  Dominated convergence and Fubini give
$\int_s^tP_{\varepsilon,n}\,d\tau\to\int_s^tP_\varepsilon\,d\tau$, where
$P_\varepsilon(\tau):=\int p\,u\cdot(\nabla u)^{\mathsf T}u/r_\varepsilon\,dx$
is measurable and bounded by $\Pi_\infty K_2G$.

(d) The error term in \eqref{eq:cutoff-identity} tends to $0$.

Hence, for every $\varepsilon\in(0,1]$,
\begin{equation}\label{eq:eps-identity}
 \int H_\varepsilon(u(t))\,dx-\int H_\varepsilon(u(s))\,dx
 +\nu\int_s^tD_\varepsilon\,d\tau=\int_s^tP_\varepsilon\,d\tau .
\end{equation}

\emph{Step 6 ($\varepsilon\downarrow0$).}  Let $\varepsilon=1/n\to0$.

(a) $H_{1/n}(u(t,x))\to|u(t,x)|^3/3$ for every $x$
(Lemma~\ref{lem:reg-calculus}(iii)), with the $n$-independent integrable
majorant $2(|u(t)|^2+|u(t)|^3)$ from \eqref{eq:HEps-majorant}.  Dominated
convergence gives $\int H_{1/n}(u(t))\,dx\to\frac13\int|u(t)|^3dx=\frac13X(t)$,
and likewise at $s$.

(b) On $[s,t]\times\R^3$, $r_{1/n}|\nabla u|^2\to|u||\nabla u|^2$ and
$|(\nabla u)^{\mathsf T}u|^2/r_{1/n}\to V(u,\nabla u)$ pointwise
(Lemma~\ref{lem:reg-calculus}(iii), Lemma~\ref{lem:integrands}(iv)), and the
sum is dominated by the integrable $g=(2|u|+1)|\nabla u|^2$ of Step 5(b).
Dominated convergence and Fubini give
$\int_s^tD_{1/n}\,d\tau\to\int_s^t\!\int\bigl(|u||\nabla u|^2+V(u,\nabla u)\bigr)dx\,d\tau
=\int_s^tD_3\,d\tau$, the last equality by Fubini and Step 1.

(c) On $[s,t]\times\R^3$, $p\,u\cdot(\nabla u)^{\mathsf T}u/r_{1/n}\to p\,W(u,\nabla u)$
pointwise (Lemma~\ref{lem:integrands}(iv)), dominated by the integrable
$h=|p||u||\nabla u|$ of Step 5(c).  Dominated convergence and Fubini give
$\int_s^tP_{1/n}\,d\tau\to\int_s^tP_3\,d\tau$.

Passing to the limit in \eqref{eq:eps-identity} proves
\eqref{eq:pressure-balance}, i.e.\ (ii).

\emph{Step 6$'$ ((iii)).}  $u\in C([0,T];L^3)$ by (R3), and
$X(t)=\norm{u(t)}_3^3$ is the composition with the continuous map
$v\mapsto\norm v_3^3$ on $L^3$.

\emph{Step 7 (invariance, (iv)).}  Fix $t$ and $\varepsilon\in(0,1]$, and put
$\rho_\varepsilon:=r_\varepsilon(u(t))-\sqrt\varepsilon$, a $C^\infty$
function of $x$ with $\rho_\varepsilon|u|\leq|u|^2$
(Lemma~\ref{lem:reg-calculus}(iv)).  Since $\nabla\rho_\varepsilon=\nabla r_\varepsilon$
and $\operatorname{div}u=0$,
$\operatorname{div}(\rho_\varepsilon u)=u\cdot\nabla r_\varepsilon
=u\cdot(\nabla u)^{\mathsf T}u/r_\varepsilon$.  Lemma~\ref{lem:divergence}
with $f=\chi_R$ and $g=\rho_\varepsilon u$ gives
\[
 \Bigl|\int\chi_R\,\frac{u\cdot(\nabla u)^{\mathsf T}u}{r_\varepsilon}\,dx\Bigr|
 =\Bigl|\int\rho_\varepsilon\,u\cdot\nabla\chi_R\,dx\Bigr|
 \leq\frac{\norm{\nabla\chi}_\infty}{R}\int|u|^2dx
 =\frac{\norm{\nabla\chi}_\infty}{R}\norm{u(t)}_2^2 .
\]
The left integrand is dominated by $|u||\nabla u|\in L^1(\R^3)$
(Lemma~\ref{lem:integrands}(iv); $u(t)\in L^2$, $\nabla u(t)\in L^2$), so
letting $R\to\infty$ by dominated convergence yields
$\int u\cdot(\nabla u)^{\mathsf T}u/r_\varepsilon\,dx=0$ for every
$\varepsilon\in(0,1]$.  Letting $\varepsilon\downarrow0$ with the same
majorant and Lemma~\ref{lem:integrands}(iv) gives
$\int W(u,\nabla u)(t,x)\,dx=0$.  Finally, for any $c(t)\in\R$,
$\int(p+c(t))W(u,\nabla u)\,dx=P_3(t)+c(t)\int W(u,\nabla u)\,dx=P_3(t)$,
both integrals being absolutely convergent by (i).
\end{proof}

\begin{remark}[Relation to the earlier formulation]\label{rem:old-form}
Where $u\neq0$ one has $V(u,\nabla u)=|u|\,|\nabla|u||^2$ and
$W(u,\nabla u)=u\cdot\nabla|u|$, so \eqref{eq:D3-def}--\eqref{eq:P3-def}
agree off the zero set of $u$ with the expressions
$\int(|u||\nabla u|^2+|u||\nabla|u||^2)$ and $\int p\,u\cdot\nabla|u|$.
The present definitions need no almost-everywhere statement about
$\nabla|u|$ on $\{u=0\}$: the convention ``integrand $=0$ where $u=0$'' is
the continuous extension of Lemma~\ref{lem:integrands}.
Lemma~\ref{lem:integrands}(ii) and the Cauchy--Schwarz inequality also give
$\norm{W(u,\nabla u)(t)}_1\leq\norm{u(t)}_2\norm{\nabla u(t)}_2$, which is
the estimate used for the frequency-localised pressure work below.
\end{remark}

\begin{remark}[Machine-checked majorant]\label{rem:lean-majorant}
The pointwise inequality \eqref{eq:HEps-majorant}, together with
Lemma~\ref{lem:reg-calculus}(i)--(iii), is formalised in the companion Lean
development (\texttt{NavierFormal.Regularization}: \texttt{abs\_HEps\_le\_two},
\texttt{HEps\_le\_norm\_sq\_mul\_rEps}, \texttt{rEps\_le\_norm\_add\_sqrt},
\texttt{hasFDerivAt\_HEps}, \texttt{tendsto\_HEps}) for a general real inner
product space.  The paper proof above is independent of that development.
\end{remark}

\begin{remark}[Differential form]\label{rem:differential-form}
Only the integrated identity \eqref{eq:pressure-balance} is used in this
paper.  If $t\mapsto D_3(t)$ and $t\mapsto P_3(t)$ are continuous on
$[0,T_*)$, then by the fundamental theorem of calculus $X\in C^1([0,T_*))$
and $\frac13X'(t)+\nu D_3(t)=P_3(t)$ for every $t$.  What would prove that
continuity: the integrands are $\Xi(u,\nabla u)$ and $p\,W(u,\nabla u)$
with $\Xi(a,\mathsf G)=|a||\mathsf G|^2+V(a,\mathsf G)$ and $W$ continuous
(Lemma~\ref{lem:integrands}) and bounded by $2|a||\mathsf G|^2$ and
$|a||\mathsf G|$.  Given $t_n\to t$, the $L^2$ convergences
$u(t_n)\to u(t)$, $\nabla u(t_n)\to\nabla u(t)$ (R3) yield a subsequence
converging almost everywhere, along which the integrands converge almost
everywhere; the majorants $2\norm{u(t_n)}_\infty|\nabla u(t_n)|^2$ and
$\norm{p(t_n)}_\infty|u(t_n)||\nabla u(t_n)|$ converge in $L^1$ (R3), so a
generalised dominated convergence theorem gives convergence of the integrals
along that subsequence; and since every sequence $t_n\to t$ has such a
subsequence, the subsequence principle upgrades this to continuity at $t$.
This argument is not carried out here, and the differential form is not
claimed.
\end{remark}
```

The following block replaces the paragraph "For later use, integrating
\eqref{eq:pressure-balance} under Hypothesis~\ref{hyp:absorption} yields …"
that stands after `hyp:absorption` and the two prose paragraphs following
it (those paragraphs are unchanged and belong to lane X-1).

```latex
\begin{corollary}[Consequences of finite-horizon absorption]
\label{cor:absorption-consequence}
Assume Hypothesis~\ref{hyp:absorption} with its $\theta\in[0,1)$, and fix
$\nu>0$, a divergence-free Schwartz datum $u_0$, $0<H<\infty$, and the
corresponding finite $A=A(\nu,u_0,H)\geq0$.  Then:
\begin{enumerate}
\item[(i)] for every $0\leq\tau<\min\{H,T_*\}$,
\[
 \norm{u(\tau)}_3^3+3(1-\theta)\nu\int_0^\tau D_3(t)\,dt
 \leq\norm{u_0}_3^3+3A(\nu,u_0,H);
\]
in particular
\begin{equation}\label{eq:pressure-consequence}
 \sup_{0\leq t<\min\{H,T_*\}}\norm{u(t)}_3^3
 \leq\norm{u_0}_3^3+3A(\nu,u_0,H)
\end{equation}
and $(1-\theta)\nu\int_0^\tau D_3\,dt\leq\frac13\bigl(\norm{u_0}_3^3+3A(\nu,u_0,H)\bigr)$
for every such $\tau$;
\item[(ii)] Hypothesis~\ref{hyp:critical} holds with
\[
 M(\nu,u_0,H)=\bigl(\norm{u_0}_3^3+3A(\nu,u_0,H)\bigr)^{1/3}.
\]
\end{enumerate}
\end{corollary}

\begin{proof}
(i) For $\tau=0$ the claim reads $\norm{u_0}_3^3\leq\norm{u_0}_3^3+3A$,
true since $A\geq0$ and $u(0)=u_0$ (R2).  For $0<\tau<\min\{H,T_*\}$ apply
\eqref{eq:pressure-balance} with $s=0$, $t=\tau$, and then
\eqref{eq:absorption}:
\[
 \frac13\norm{u(\tau)}_3^3
 =\frac13\norm{u_0}_3^3-\nu\int_0^\tau D_3\,dt+\int_0^\tau P_3\,dt
 \leq\frac13\norm{u_0}_3^3-(1-\theta)\nu\int_0^\tau D_3\,dt+A .
\]
Multiplying by $3$ gives the displayed inequality.  Both terms on its left
side are nonnegative ($D_3\geq0$ by \eqref{eq:D3P3-bounds}, $\theta<1$), so
each is bounded by the right side; taking the supremum over $\tau$ gives
\eqref{eq:pressure-consequence}.
(ii) Hypothesis~\ref{hyp:critical} asks for a finite
$M(\nu,u_0,H)$ with $\sup_{0<t<\min\{H,T_*\}}\norm{u(t)}_3\leq M(\nu,u_0,H)$.
Take cube roots in \eqref{eq:pressure-consequence}; $M$ is finite because
$A$ is finite and $u_0\in\mathcal S\subset L^3$.
\end{proof}

The critical bound \eqref{eq:pressure-consequence} would still follow if
$\theta=1$; strict inequality $\theta<1$ is retained only to express the
proposed absorption of part of the dissipation, i.e.\ the positive control
of $(1-\theta)\nu\int_0^\tau D_3$ in Corollary~\ref{cor:absorption-consequence}(i).
```

### 2.3 Bibliography records to add to `references.bib`

```bibtex
@book{SteinWeiss1971,
  author    = {Elias M. Stein and Guido Weiss},
  title     = {Introduction to {Fourier} Analysis on {Euclidean} Spaces},
  series    = {Princeton Mathematical Series},
  number    = {32},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {1971}
}

@book{RudinRCA,
  author    = {Walter Rudin},
  title     = {Real and Complex Analysis},
  edition   = {3},
  publisher = {McGraw--Hill},
  address   = {New York},
  year      = {1987}
}

@book{RudinPMA,
  author    = {Walter Rudin},
  title     = {Principles of Mathematical Analysis},
  edition   = {3},
  publisher = {McGraw--Hill},
  address   = {New York},
  year      = {1976}
}
```

These three books were not opened in this lane; the citations in §2.2 are
deliberately at chapter level (Rudin RCA Ch. 1 for dominated convergence,
Ch. 3 for Hölder, Ch. 8 for Fubini/Tonelli; Rudin PMA Ch. 5 for the mean
value theorem, Ch. 6 for the fundamental theorem of calculus; Stein–Weiss
Ch. I §2 for Plancherel, §3 for the distributional symbol of `∂_j`) so that
no unverified theorem number enters the manuscript. Status [MO] in §3.

### 2.4 Not this lane: the F-1 interface patch

`main.tex` lines 256–262 (lane F-1) still write `L_J`, `Q_J` with
`u·∇|u|`. After Definition `def:D3P3`, `P_3 = L_J + Q_J` holds only if those
displays are rewritten with the same integrand. The minimal patch, so that
no lane has to guess it (and with `S_J := P_{≤2^J}` per D1):

```latex
\[
 P_3=L_J+Q_J,
 \quad L_J=\int_{\R^3} p_{\leq J}\,W(u,\nabla u)\,dx,
 \quad Q_J=\int_{\R^3} p_{>J}\,W(u,\nabla u)\,dx,
\]
```

with the bound used in `prop:lowpressure`,
`‖W(u,∇u)(t)‖_1 ≤ ‖u(t)‖_2‖∇u(t)‖_2`, supplied by Remark `rem:old-form`
(Lemma `lem:integrands`(ii) and Cauchy–Schwarz). Both integrals are
absolutely convergent because `p_{≤J}(t), p_{>J}(t) ∈ L^∞` whenever
`p(t) ∈ L^2 ∩ L^∞` and the multiplier of `S_J` has an `L^1` kernel (lane
F-1's obligation).

## 3. External facts used

| # | Fact, as used | Source | Status |
|---|---|---|---|
| 1 | Regularity package R, of which only (R2)–(R3) are consumed: for `T<T_*`, `u,p ∈ C^∞([0,T]×R^3)`, `eq:NS` pointwise, `u(0)=u_0`; `u ∈ C([0,T];L^q)` for `q ∈ {2,3,4,∞}`, `∇u ∈ C([0,T];L^2)`, `p ∈ C([0,T];L^2∩L^∞)`, for the normalised pressure | Proposition `prop:localtheory` (local-theory lane, per D2); its literature inputs Tao 2013 Theorem 5.4(iv) and Corollary 5.8 are [DI] in `cp01-literature-statements` §1.2–1.3 (APDE pp. 52–53, 56–57) | assumed (D2) |
| 2 | Fourier convention `f̂(ξ) := ∫_{R^3} e^{−2πix·ξ}f(x)dx` for `f ∈ L^1_x(R^3)`; "we then extend this Fourier transform to tempered distributions in the usual manner" | Tao, APDE 6 (2013), printed **p. 35** (§2 "Notation and basic estimates", last paragraph) | **[DI]** (publisher PDF page image read in this lane) |
| 3 | `\widehat{Δ^{-1}f}(ξ) := −(4π²|ξ|²)^{-1} f̂(ξ)` (14), "well-defined for any tempered distribution `f : R^3 → R` for which the right-hand side of (14) is locally integrable. This is for instance the case if `f` lies in the `k`-th derivative of a function in `L^1_x(R^3)` for some `k ≥ 0`, or the `k`-th derivative of a function in `L^2_x(R^3)` for some `k ≥ 1`"; and "All of these above function spaces can of course be extended to functions that are vector or tensor-valued without difficulty (there are multiple ways to define the norms in these cases, but all such definitions will be equivalent up to constants)" | Tao, printed **p. 38** | **[DI]** (this lane) |
| 4 | `Δp = −∂_i∂_j(u_iu_j) + ∇·f` (8); "We then say that the periodic smooth solution `(u,p,u_0,f,T)` has normalised pressure if one has `p = −Δ^{-1}∂_i∂_j(u_iu_j) + Δ^{-1}∇·f`" (9); "We remark that this normalised pressure condition can also be imposed for smooth finite energy solutions (because `∂_i∂_j(u_iu_j)` is a second derivative of an `L^1_x(R^3)` function, and `∇·f` is the first derivative of an `L^2_x(R^3)` function), but it will turn out that normalised pressure is essentially automatic in that setting anyway; see Lemma 4.1"; footnote 4: "Up to the harmless freedom to add a constant to `p`, this normalisation is equivalent to requiring that the pressure be periodic with the same period as the solution `u`" | Tao, printed **p. 28** | **[DI]** (this lane); Lemma 4.1 itself not read |
| 5 | `‖u‖_{H^s_x(R^3)} := (∫(1+|ξ|²)^s|û(ξ)|²dξ)^{1/2}`, `H^s_x(R^3)` the space of tempered distributions with finite norm, equivalent up to constants to the classical `H^k` norm for integer `k` | Tao, printed **p. 36** | **[DI]** (this lane) — recorded to correct round 1's "p. 38"; **no longer used** in the block |
| 6 | Plancherel: the Fourier transform of `L^1∩L^2` extends to a unitary operator on `L^2(R^3)`; hence `‖T_m f‖_2 ≤ ‖m‖_∞‖f‖_2` for bounded measurable symbols, and two `L^2` functions with the same transform coincide | Stein–Weiss, *Introduction to Fourier Analysis on Euclidean Spaces*, Princeton 1971, Ch. I §2 | **[MO]** (book not opened; chapter-level citation only) |
| 7 | `\widehat{∂_j f} = 2πiξ_j f̂` for tempered distributions `f` (hence symbols of `∂_i∂_j` and `−Δ`) | Stein–Weiss, Ch. I §3; consistent with Tao p. 35 "extend … to tempered distributions in the usual manner" | **[MO]** |
| 8 | Dominated convergence theorem; Tonelli's and Fubini's theorems on `[s,t]×R^3` | Rudin, *Real and Complex Analysis*, 3rd ed., Ch. 1 and Ch. 8 | **[MO]** (chapter-level) |
| 9 | Hölder's inequality `∫|fg| ≤ ‖f‖_r‖g‖_{r'}` on `L^p(R^3)`; Cauchy–Schwarz as the case `r=2` | Rudin, *RCA*, Ch. 3; also `cp01-literature-statements` §6 S10 (Mathlib `eLpNorm_smul_le_mul_eLpNorm`) | **[MO]** for Rudin; **[DI]** for the Mathlib statement in the CP01 record |
| 10 | Mean value theorem; fundamental theorem of calculus for `C^1` functions on `[a,b]` | Rudin, *Principles of Mathematical Analysis*, 3rd ed., Ch. 5 and Ch. 6 | **[MO]** (chapter-level) |
| 11 | `|H_ε(a)| ≤ 2(|a|²+|a|³)` for `0 ≤ ε ≤ 1` (cited only as a remark; proved on paper in `lem:reg-calculus`(ii)); plus `rEps_le_norm_add_sqrt`, `HEps_le_norm_sq_mul_rEps`, `tendsto_HEps`, `hasFDerivAt_HEps`, stated "for a general real inner product space `E`" | `/home/ert/proj/navier-formal/NavierFormal/Regularization.lean` (module header; lemmas at lines 94, 141, 177, 202, 260) | **[DI]** (file read) |
| 12 | Verbatim `hyp:absorption` (`eq:absorption`, quantified over `0<τ<min{H,T_*}`), `hyp:critical` (`eq:missing`), the `M` formula, `L_J`/`Q_J` | `/home/ert/proj/navier-paper/main.tex` lines 199–353, 393–409 | **[DI]** |
| 13 | `R_iR_j = ∂_i∂_j(−Δ)^{-1} = −Δ^{-1}∂_i∂_j`; identity of the manuscript's `p` with Tao's normalised pressure; no sign error | `cp01-literature-statements` §7.3 | **[DI]** there; re-derived in `lem:pressure-convention` |
| 14 | `references.bib`: `Tao2013` is the APDE article, `pages = {25--107}`; printed pagination is therefore the one `\cite` must use | `/home/ert/proj/navier-paper/references.bib` | **[DI]** |

Elementary facts proved inline in the block (no source needed): the
smoothness of `g(s) = e^{−1/s}` extended by `0` and the cutoff construction;
all pointwise inequalities of `lem:integrands` and `lem:reg-calculus`. The
`π²` weight integral of round 1 is gone with `lem:embedding`.

No Calderón–Zygmund theory, no Riesz-transform `L^p` bounds for `p ≠ 2`, no
Rademacher theorem, no `W^{1,1}` chain rule, no `L^2` Fourier inversion
theorem, and no a.e. statement about `∇|u|` is used.

## 4. Obligations NOT discharged (exactly stated)

1. **Continuity of `t ↦ D_3(t)` and `t ↦ P_3(t)`**, hence the pointwise
   differential form `X'/3 + νD_3 = P_3`. Not needed by the manuscript;
   Remark `rem:differential-form` names the route (a.e.-convergent
   subsequences from `L^2` convergence, `L^1`-convergent majorants,
   generalised dominated convergence, subsequence principle) without
   carrying it out.
2. **Primary-source inspection of facts 6–10** (Plancherel, distributional
   symbol of `∂_j`, DCT/Tonelli/Fubini, Hölder, MVT/FTC). Cited [MO] at
   chapter level; the books were not opened in this lane. No mathematical
   content depends on them beyond their standard statements, and D5 is met
   by the source-plus-label form; promotion to [DI] requires opening the
   three books.
3. **Tao's Lemma 4.1** (which makes normalised pressure "essentially
   automatic" for smooth finite-energy solutions) was not read; it is not
   needed because the regularity and normalisation of `p` come from
   `prop:localtheory` (D2), not from Lemma 4.1.
4. **The Littlewood–Paley paragraph and `prop:lowpressure`** (lane F-1)
   currently define `L_J`, `Q_J` through `u·∇|u|`. The patch of §2.4 must
   land for `P_3 = L_J + Q_J` to hold for the `P_3` of Definition
   `def:D3P3`. Not this lane's file.
5. **Merging with the sibling lane**: one Conventions paragraph (with Tao
   pages 35/36 corrected there too), one `χ_R`, one divergence lemma
   (`lem:div-zero` or `lem:divergence`), one Lean remark with a citable
   record. Integrator's task; both variants are stated above so the merge is
   mechanical.
6. The bibliography keys `SteinWeiss1971`, `RudinRCA`, `RudinPMA` are new;
   records are supplied in §2.3 and must be added to `references.bib`.

## 5. Frontier record

**MODE / RESULT.** PROOF WRITING, round 2 — complete. The round-1 audit
found no invalid bridge; both of its source-layer defects are repaired and
every one of its twelve editorial items is addressed (§6). `prop:pressure`
is stated in integrated form and proved in seven displayed steps from
(R2)–(R3) alone, with every cutoff error bounded explicitly by
`C_E R^{-1}(t−s)` and both limits (`R → ∞`, `ε ↓ 0`) carried out by
dominated convergence on `[s,t]×R^3` with the named integrable majorants
`2(|u|²+|u|³)`, `(2|u|+1)|∇u|²`, `|p||u||∇u|`. The zero set of `u` is
handled by the continuous extension of `V, W` (Lemma `lem:integrands`).
`eq:pressure-consequence` and `hyp:absorption ⟹ hyp:critical` with
`M = (‖u_0‖_3³+3A)^{1/3}` are proved as Corollary
`cor:absorption-consequence`. Every external fact in the LaTeX block now
carries a `\cite`, and every Tao page number was verified against the
publisher PDF in this lane.

**CLAIM AND SCOPE.** For the Schwartz-data classical branch of
`prop:localtheory` on `R^3`, unforced, arbitrary `ν>0`, with the
normalised pressure `p = R_iR_j(u_iu_j) = −Δ^{-1}∂_i∂_j(u_iu_j)` under the
convention `f̂(ξ)=∫e^{−2πix·ξ}f`: for all `0≤s≤t<T_*`,
`X(t)/3 − X(s)/3 + ν∫_s^t D_3 = ∫_s^t P_3`, with `0 ≤ D_3 ≤ 2∫|u||∇u|²`,
`|P_3| ≤ ‖p‖_∞‖u‖_2‖∇u‖_2`, `∫W(u,∇u)dx = 0` (so `P_3` is invariant under
`p → p + c(t)`). Under `hyp:absorption`: `‖u(τ)‖_3³ + 3(1−θ)ν∫_0^τD_3 ≤
‖u_0‖_3³ + 3A` for `0 ≤ τ < min{H,T_*}`, hence `hyp:critical` with
`M = (‖u_0‖_3³+3A)^{1/3}`.

**EVIDENCE.** The round-1 audit's independent rederivation of every
identity, sign, constant and exponent (`cp02-review-pressure.md` §2.1, six
failed refutation attempts §2.2), none of which changed in round 2; direct
inspection in this lane of Tao APDE printed pp. 26–28 and 34–38 (page
images), confirming the content of every Tao fact used and fixing the page
numbers 28, 35, 38 (and 36 for the now-unused `H^s` definition); the Lean
lemmas of `Regularization.lean` re-checked by name and line; verbatim
comparison with `main.tex` lines 199–353, 393–409.

**FIRST GAP (for this lane's obligations).** None among P-0..P-3 and
`eq:pressure-consequence`. The nearest unwritten item is the continuity of
`D_3`, `P_3` in time (Remark `rem:differential-form`), which no result in
the manuscript needs. Behind it, outside this lane: the adaptation of
`L_J`, `Q_J` to `W(u,∇u)` (§2.4, lane F-1), and the merge of the two lanes'
Conventions paragraphs with the Tao pages corrected in the sibling lane.

**SURVIVING CONDITIONAL SUFFIX.** With this lane's `prop:pressure` and
`cor:absorption-consequence`, `hyp:absorption ⟹ hyp:critical` is a
complete, audited proof, unconditionally on the classical branch. The
programme suffix is unchanged: `hyp:highpressure` (with the proved
`prop:lowpressure`) `⟹ hyp:absorption ⟹ hyp:critical ⟹ def:target` via
`thm:continuation` and `thm:conditional`; the first unproved link remains
`hyp:highpressure`.

**NON-CLAIMS.** No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or
NS-R3 result is asserted or approached. `hyp:absorption` and
`hyp:critical` remain hypotheses; nothing here bears on their truth. The
differential form of the balance is not claimed. Facts 6–10 were not
inspected in their primary texts; Tao's Lemma 4.1 was not read.

**NEXT DISTINCT ACTION.** Round-2 audit of this file (citation layer and
the three changed passages: Conventions, `lem:pressure-convention`(c), the
narrowed (R3)); then integration with `cp02-energy-enstrophy.md` (one
Conventions paragraph, one `χ_R`, one divergence lemma, one Lean remark,
`corollary` environment added) and hand-off of §2.4 to lane F-1.
Independently: open Stein–Weiss Ch. I and Rudin RCA Ch. 1, 3, 8 / PMA
Ch. 5, 6 to promote facts 6–10 from [MO] to [DI].

## 6. Round-1 audit items and their disposition

| audit item | disposition |
|---|---|
| §3 first defect: `\cite[p.~37]` / `\cite[p.~38]{Tao2013}` wrong pages | Fixed and re-verified in this lane: p. 35 (Fourier), p. 38 ((14), tensor extension), p. 28 ((9) with scope). The `H^s` citation (p. 36) is dropped with `lem:embedding`. |
| §3 second defect: only `Tao2013` cited; textbook facts unsourced | Eleven `\cite` insertions (Hölder, Plancherel, symbol of `∂_j`, Fubini ×2, FTC ×2, MVT, Tonelli/Fubini ×2, DCT), all chapter-level to `SteinWeiss1971`, `RudinRCA`, `RudinPMA`; bib records in §2.3. |
| §5(b) `lem:pressure-convention`: (9) scoped to periodic; a.e./continuous representative step | Statement now cites "(9), p. 28, and the remark following it" and states the scoping; proof part (c) makes the identification explicit. |
| §6.1 `lem:embedding` unnecessary | Deleted; (R1) deleted; Plancherel retained once for the multiplier bound and once for uniqueness of the `L^2` function with a given transform. |
| §6.2 `lem:divergence` duplicates `lem:div-zero` | Kept (this file must be self-contained) with an integration note giving the mechanical replacement. |
| §6.3 (R3) over-declared | Narrowed to `u ∈ C([0,T];L^q)`, `q ∈ {2,3,4,∞}`; `∇u ∈ C([0,T];L^2)`; `p ∈ C([0,T];L^2∩L^∞)`; the rest of R noted as unused. |
| §6.4 monotonicity clause unused | Kept as documentation (harmless). |
| §6.5 `rem:lean-majorant` | Kept; integration note: at most one Lean remark, with a citable record. |
| §7.1 sibling lane's arXiv pages | Flagged in the integration note (pp. 14/15 → 35/36). |
| §7.2 theorem numbers unverified | Removed from the manuscript text; chapter-level citations, [MO] in §3. |
| §7.3 duplication with sibling lane | Integration note in §2.1; `χ_R` now constructed in the same form as the sibling's. |
| §7.4 F-1 interface break | §2.4, marked not this lane, with the `W` notation. |
| §7.5 `Θ`/`θ`/`ϑ` collision | `Ψ,Θ → V,W`; `ϑ → λ`; the weight-integral `ϑ` is gone. |
| §7.6 `\subsection*` style | Retained (sibling lane uses it); uniformity is the integrator's. |
| §7.7 fact table "APDE p. 5" | Corrected to p. 28 (row 4). |
| §7.8 `\eqref{eq:constants}` | Replaced by an unnumbered display and the name "section constants". |
| §7.9 unlabeled remark | `rem:old-form`. |
| §7.10 split bounds in (i) | `eq:D3P3-bounds`; the corollary cites it for `D_3 ≥ 0`. |
| §7.11 subsequence principle | Named in `rem:differential-form`. |
| §7.12 abstract | Controller item; untouched. |
