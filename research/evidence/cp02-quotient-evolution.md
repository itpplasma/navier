# CP02-7: quotient evolution (obligations Q-8 .. Q-18)

MODE: INTEGRATE (paper proof), REPAIR ROUND 1. Lane CP02-7 of wave CP02.
Date: 2026-09-05. Version 2 (complete rewrite in place after the audit
`cp02-review-quotient-evolution.md`, verdict REPAIR).

Base texts: `research/evidence/cp01-quotient-section-structure.md` (§4, second
half, from "The classical trajectory class" onward), `hf17-quotient-evolution.md`
with `hf17-review-quotient-evolution.md` (PASS), obligations Q-8 .. Q-18 of
`cp01-manuscript-obligations.md` §1.14, the source record
`cp01-literature-statements.md`, and the audit
`cp02-review-quotient-evolution.md` (read in full). Manuscript read in full
(`../navier-paper/main.tex`, 562 lines). Sibling lanes read for the
interface: `cp02-quotient-functional.md` (labels and sub-item letters checked
at the source), `cp02-lowpressure.md` (`def:lp`, `eq:lp-symbol`,
`lem:lp-coincide`, `lem:lowpass-kernel`, `lem:bernstein` read).

## 0. Repair record (what changed relative to version 1)

The audit found no invalid mathematical step. All repairs are in the
external-fact layer, the cross-reference layer, and the editorial layer.

| # | Audit item | Action in this version |
| --- | --- | --- |
| R1 | **First bad bridge**: `lem:qe-embedding` cited Grafakos Thm. 2.2.14 for Fourier inversion on `L^2`; that theorem is stated for `S(R^n)` only | Sentence replaced by the audit's REPAIR 1 text: the `L^1 ∩ L^2` coincidence and the a.e. inversion on `L^2` are cited to `Definition~\ref{def:lp}` (project text of the low-pressure lane) with source Grafakos §2.2.4, pp. 113–114. **Independently re-inspected in this session** (PDF mirror, book pp. 112–114 read as page images): Thm. 2.2.14 begins "Given f, g, and h in S(R^n)"; §2.2.4 p. 114 reads "for f in L^1(R^n) ∩ L^2(R^n) the expressions f-hat and F(f) coincide pointwise a.e." and "F' coincides with the inverse operator F^{-1} of F: L^2 → L^2, and Fourier inversion f = F^{-1}∘F(f) = F∘F^{-1}(f) a.e. holds on L^2." E10 is now [DI]. The citation "Thm. 2.2.14" no longer appears in this lane. |
| R2 | `lem:quotient-pressure` cited `lem:quotient-minimizer`(b) for stationarity | now (c) (checked at `cp02-quotient-functional.md` line 344 ff.) |
| R3 | continuity of `u ↦ w`, `u ↦ A` cited to `lem:quotient-minimizer`(d) (twice) | now `Lemma~\ref{lem:quotient-stability}`, estimate `\eqref{eq:cp-continuity}` (both occurrences) |
| R4 | `lem:quotient-lowstrain` cited `lem:quotient-minimizer`(a) for the norm identities; `‖P‖_{L^3→L^3}` used where the functional lane fixes `C_P` | now (b); every `‖P‖` is `C_{\mathbb P}` (the symbol of `lem:leray`(b)); `M_L = 3(1+C_P)C_B 2^{5L/2}‖u_0‖_2`, `M = C_P(‖u_0‖_3^3+3A_input)^{1/3}e^{M_L H/3}` |
| R5 | low-pass kernel written `ψ_L`, `ψ̂ = φ`, colliding with D1's and `eq:lp-symbol`'s `ψ = φ − φ(2·)` | paragraph replaced by the audit's REPAIR 5 text: kernel `κ_L`, `κ̂ = φ`, `S_L` of `def:lp`, `lem:lp-coincide`, `lem:lowpass-kernel`; `eq:qe-bernstein` is now the vector-valued Frobenius form of `lem:bernstein`; the componentwise reassembly and the separate continuity paragraph in `lem:quotient-lowstrain` are deleted |
| M1 | `H^2` norm convention unstated | fixed in the notation paragraph: `‖f‖_{H^m} := ‖(1+|ξ|^2)^{m/2} f̂‖_2`; the constant `π` in `eq:qe-embedding` is stated to depend on it |
| M2 | Fréchet remainder used through an unspecified modulus `ε(·)` substituted with an upper bound | all three uses (`lem:quotient-chainrule` Step 2, `lem:quotient-heatsign`, `lem:quotient-transport` Step 4) now invoke `\eqref{eq:cp-derivative-remainder}` directly: `|r(h)| ≤ 6(‖w‖_3+‖h‖_3)^{3/2}‖h‖_3^{3/2}`, manifestly monotone |
| M3 | Gronwall with an `s`-dependent constant in `lem:flow`(b) | both places now say: fix `s`, bound the forcing by its value at `s` (the modulus `ω` is nondecreasing), apply `lem:qe-gronwall` on the interval with endpoints `0` and `s` |
| M4 | `lem:quotient-transport` Step 1 cited (R2), (R3) for boundedness of `D^2u` | now (R1)–(R3) |
| M5 | `D_Q` defined inside a lemma | new `Definition~\ref{def:qe-dissipation}`; `lem:quotient-heatsign` is the sign lemma only; `hyp:highstrain` cites the definition |
| M6 | `hyp:highstrain` not self-contained | `K_L` restated inside the hypothesis |
| M7 | dangling labels `lem:heat-generator`, `eq:qe-cutoff-error` | both now referenced from the text |
| M8 | unnamed remarks | all remarks carry labels and titles |
| M9 | `\operatorname{adj}` eight times | kept inline (no new macro, so no preamble seam); noted |
| M10 | `|M|` vs `|M|_F` | `|M| ≤ |M|_F` displayed once in the notation; Frobenius norm used only in `eq:qe-bernstein` and the pointwise bound in `lem:quotient-lowstrain` |
| M11 | `θ` range stated twice (hypothesis and display) | the display `eq:quotient-gap` carries no `θ ≤ 1` annotation; the hypothesis says `θ ∈ [0,1]`; the integrator drops the manuscript display's annotation |
| M12 | five subsections | reduced to four: the evolution proposition is placed in the transport subsection |
| M13 | `prop:quotient-evolution` restated D2 | now "with the notation and package (R) of Section~\ref{subsec:qe-trajectories}" |
| §7.2 | `Teschl2012` corroboration remark | dropped, together with the bibliography entry (it was never used) |
| §7.3 | Rudin RCA Thms. 3.14, 7.26 [MO] | **upgraded to [DI]** in this session (PDF read as page images: Thm. 3.14 p. 69, Thm. 7.26 pp. 153–154); kept as the textbook source beside the Mathlib statements |
| §7.5 | §4 open items 1–3 stale | §4 rewritten; the only remaining seams are listed there |

Controller decisions D1-D5 are followed. In particular:

- D1: `S_L := P_{\le 2^L}` is the operator `S_J` of `Definition~\ref{def:lp}`
  (Tao's smooth bump `φ`; `S_L f = κ_L * f`, `κ_L = 2^{3L}κ(2^L·)`, `\hat κ = φ`,
  `Lemma~\ref{lem:lowpass-kernel}`); Fourier convention
  `\hat f(ξ) = ∫ e^{-2πi x·ξ} f`; pressure `p = R_iR_j(u_iu_j)` = Tao's
  normalised pressure (stated, not re-derived; `Definition~\ref{def:lp}`).
- D2: regularity package R is assumed by citing `Proposition~\ref{prop:localtheory}`.
  No preserved Schwartz decay in time is used anywhere (checked line by line
  by the audit and again here).
- D4: labels `sec:quotient`, `eq:quotient-evolution`, `eq:quotient-gap`,
  `hyp:highstrain`, `prop:energy`, `hyp:critical`, `thm:conditional`,
  `def:target` are used as required; new labels carry the prefix `qe-` or
  the CP01 draft names (`lem:quotient-pressure`, `lem:heat-generator`,
  `lem:quotient-heatsign`, `lem:flow`, `lem:quotient-transport`,
  `prop:quotient-evolution`, `lem:quotient-lowstrain`,
  `prop:quotient-conditional`, `rem:highstrain-scope`).
- D5: every external fact is listed in §3 with source and [DI]/[MO]; after
  this round every textbook fact used in the block is [DI].

Labels of other lanes that this text cites (they must exist in the
integrated manuscript; all were checked against the current lane files):

| Label | Owner | Content used here |
| --- | --- | --- |
| `prop:localtheory` | local-theory lane | package R (D2) |
| `def:lp` | low-pressure lane (`cp02-lowpressure.md`) | Fourier convention; `L^2` Plancherel theory (isometry on `L^1∩L^2`, unitary extension `F`, inverse extending `f ↦ f^∨`); Riesz symbols; `S_J = T_{φ(2^{-J}·)}`, `ψ`, `Δ_j` |
| `lem:lp-coincide` | low-pressure lane | `S_J = Σ_{j≤J}Δ_j` on `L^2` (mentioned for reconciliation only) |
| `lem:lowpass-kernel` | low-pressure lane | `κ = φ^∨ ∈ S`, `S_Jf = κ_J*f`, `∂_k S_J f = (∂_kκ_J)*f` |
| `lem:bernstein` | low-pressure lane | `‖∇S_Lf‖_∞ ≤ C_B2^{5L/2}‖f‖_2` for scalar or vector `f ∈ L^2` (Frobenius form), `C_B = 2π‖|ξ|φ‖_2 ≤ 16π√(2π/5)`, `C^∞` representative, `t ↦ ∇S_Lu(t) ∈ C([0,T];L^∞)` for `u ∈ C([0,T];L^2)` |
| `def:quotient` | functional lane | `\mathcal G_3`, `F(v)=\frac13\int|v|^3`, `j(v)=|v|v`, `\mathcal Q`, `G_t` (heat kernel `k_t`) |
| `lem:cubic-frechet`, eq. `eq:cp-F-taylor` | functional lane | `|F(v+h)-F(v)-\langle j(v),h\rangle|\le(\|v\|_3+\|h\|_3)\|h\|_3^2` |
| `lem:quotient-minimizer` (b),(c) | functional lane | (b) minimizer `q(u)`, `w=u+q`, `A=|w|w ∈ L^{3/2}`, `\mathcal Q=\frac13\|w\|_3^3`, `\|A\|_{3/2}=\|w\|_3^2`; (c) stationarity `\langle A,g\rangle=0` on `\mathcal G_3` |
| `lem:quotient-stability`, eq. `eq:cp-continuity` | functional lane | `\|A'-A\|_{3/2}\le4(\|w\|_3+\|h\|_3)^{3/2}\|h\|_3^{1/2}`; continuity of `u\mapsto w(u)` (`L^3\to L^3`) and `u\mapsto A(u)` (`L^3\to L^{3/2}`) |
| `lem:leray` (b) | functional lane | `C_{\mathbb P}:=\|\mathbb P\|_{L^3\to L^3}` |
| `lem:quotient-coercive`, eq. `eq:cp-coercive` | functional lane | `\|u\|_3^3\le3C_{\mathbb P}^3\mathcal Q(u)`, `\|q\|_3\le(1+C_{\mathbb P})\|w\|_3` for solenoidal `u\in L^3`; `\mathcal Q(u)\le\frac13\|u\|_3^3` |
| `lem:quotient-heat` | functional lane | `\|G_tf\|_3\le\|f\|_3`, `\mathcal Q(G_tu)\le\mathcal Q(u)` |
| `prop:quotient-derivative`, eq. `eq:cp-derivative-remainder` | functional lane | `D\mathcal Q(u)[h]=\langle A(u),h\rangle`; `|\mathcal Q(u+h)-\mathcal Q(u)-\langle A(u),h\rangle|\le6(\|w\|_3+\|h\|_3)^{3/2}\|h\|_3^{3/2}` |
| `prop:energy`, `prop:pressure`, `prop:lowpressure`, `hyp:highpressure`, `hyp:critical`, `eq:missing`, `thm:conditional`, `thm:continuation`, `def:target`, `eq:NS` | manuscript | as in `main.tex` |

Environments used: `lemma`, `definition` (in addition to `proposition`,
`hypothesis`, `remark`, `theorem` of `main.tex`). The integrator must add
`\newtheorem{lemma}[theorem]{Lemma}` and
`\newtheorem{definition}[theorem]{Definition}` to the preamble (the
functional and low-pressure lanes need the same two). No new macros are used:
the text writes `\mathcal Q`, `\mathcal G_3`, `\mathbb P`, `C_{\mathbb P}`
explicitly and uses `\norm` and `\R` from `main.tex`. `\operatorname{div}`,
`\operatorname{tr}`, `\operatorname{adj}` are inline.

Compile check (this version): the block of §2 was extracted verbatim and
compiled under a stub preamble (`amsmath`, `amssymb`, `amsthm`, `hyperref`,
the six theorem environments, `\R`, `\norm`, label stubs for the
externally-owned labels of the table above, and a stub bibliography with
`Grafakos2014`, `Rudin1987`) with `latexmk -pdf`: exit 0, no undefined
references, no undefined citations, no overfull boxes. The paper repository
was not modified.

---

## 1. Obligations discharged

| ID | Statement (from `cp01-manuscript-obligations.md` §1.14) | Where |
| --- | --- | --- |
| Q-8 | `p,\nabla p\in L^3` on compact classical intervals, from R; pressure normalisation stated | Lemma `lem:quotient-pressure`, Remark `rem:qe-pressure-normalisation` |
| Q-9 | `\nabla p\in\mathcal G_3` by cutoff and mollification, `L^3` error terms displayed | Lemma `lem:qe-mollify`, Lemma `lem:quotient-pressure` (display `eq:qe-cutoff-error`) |
| Q-10 | chain rule along the `C^1([0,T];L^3)` curve, each term of `u_t` in `L^3`, exact pressure cancellation | Lemma `lem:quotient-chainrule` |
| Q-11 | generator limit `(G_su-u)/s\to\Delta u` in `L^3` via `G_su-u=\int_0^sG_r\Delta u\,dr` and strong continuity of `G_r` (proved from density of `C_c` and the `L^3` contraction); sign `D_{\mathcal Q}\ge0` | Lemmas `lem:qe-heat-continuity`, `lem:heat-generator`, Definition `def:qe-dissipation`, Lemma `lem:quotient-heatsign` |
| Q-12 | flow lemma: global flow, `C^1` diffeomorphism, Liouville's formula proved from the variational ODE and Jacobi's formula (Jacobi proved), `D\Phi_s\to I`, `(D\Phi_s^{-\mathsf T}-I)/s\to-(Du)^{\mathsf T}` uniformly, using only bounded uniformly continuous `Du` | Lemmas `lem:qe-jacobi`, `lem:flow` |
| Q-13 | pullback of compact gradients is a compact gradient; pullback bounded on `L^3`; `q_s\in\mathcal G_3` | Lemma `lem:qe-pullback` |
| Q-14 | envelope inequality by change of variables | Lemma `lem:quotient-transport`, display `eq:qe-envelope` |
| Q-15 | continuity of `g\mapsto g\circ\Phi_{-r}` in `L^3` at `r=0` for `g\in L^3`; `(u\circ\Phi_{-s}-u)/s\to-(u\cdot\nabla)u` in `L^3` | Lemma `lem:quotient-transport`, steps 3-4 |
| Q-16 | two-sided expansion; identity `\int A\cdot((u\cdot\nabla)u)=\int q\cdot((A\cdot\nabla)u)` with index contraction displayed | Lemma `lem:quotient-transport`, display `eq:qe-contraction`, step 5 |
| `eq:quotient-evolution` | pressure-free evolution identity with `D_{\mathcal Q}\ge0` | Proposition `prop:quotient-evolution` |
| Q-17 | low-strain bound `|K_{\rm low}|\le M_L\mathcal Q(u)`, `M_L=3(1+C_{\mathbb P})C_B2^{5L/2}\|u_0\|_2`, via Hölder, `\|q\|_3\le(1+C_{\mathbb P})\|w\|_3`, the Bernstein lemma of the low-pressure lane, and energy | Lemma `lem:quotient-lowstrain` |
| `hyp:highstrain` | stated as a self-contained hypothesis with `eq:quotient-gap` | Hypothesis `hyp:highstrain` |
| Q-18 | conditional Gronwall proposition with absolute continuity of `t\mapsto\mathcal Q(u(t))` from Q-10; explicit `M(\nu,u_0,H)` | Lemma `lem:qe-gronwall`, Proposition `prop:quotient-conditional` |

Auxiliary results proved in full because the text uses them and no other
lane owns them: `lem:qe-embedding` (`H^2(\R^3)\hookrightarrow C_{b,u}\cap L^3`
with constant `\pi` for the stated norm), `lem:qe-average` (Hölder/Tonelli
averaging in `L^3`), `lem:qe-gronwall`, `lem:qe-mollify`, `lem:qe-jacobi`.

No hypothesis was added or weakened in this round. The statements of all
lemmas and propositions are those of version 1, except that `D_{\mathcal Q}`
is now introduced in a definition and `hyp:highstrain` restates `K_L`.

---

## 2. Replacement text (second half of `sec:quotient`)

```latex
%%% CP02-7: second half of \section{...}\label{sec:quotient}.
%%% Requires in the preamble:
%%%   \newtheorem{lemma}[theorem]{Lemma}
%%%   \newtheorem{definition}[theorem]{Definition}
%%% Cites labels of other lanes: prop:localtheory; def:lp, lem:lp-coincide,
%%% lem:lowpass-kernel, lem:bernstein (low-pressure lane); def:quotient,
%%% lem:cubic-frechet (eq:cp-F-taylor), lem:quotient-minimizer,
%%% lem:quotient-stability (eq:cp-continuity), lem:leray,
%%% lem:quotient-coercive (eq:cp-coercive), lem:quotient-heat,
%%% prop:quotient-derivative (eq:cp-derivative-remainder) (functional lane).
%%% The display eq:quotient-gap below replaces the manuscript's display of the
%%% same label; the annotation "\theta\le1" moves into hyp:highstrain.

\subsection{Trajectories of the classical solution}
\label{subsec:qe-trajectories}

The rest of this section applies the functional $\mathcal Q$ of
Definition~\ref{def:quotient} along the classical solution.  Throughout,
$u_0\in\mathcal S(\R^3)^3$ is divergence-free, $\nu>0$, $(u,p)$ is the
maximal classical solution of \eqref{eq:NS} on $[0,T_*)$ selected by
Proposition~\ref{prop:localtheory}, and $[0,T]\subset[0,T_*)$ is a compact
interval.  We use only the following consequences of
Proposition~\ref{prop:localtheory}, referred to as the package~(R):
\begin{enumerate}
\item[(R1)] For every multi-index $\alpha$ and every integer $k\ge0$,
 \[
  \partial^\alpha u\in C^1([0,T];H^k(\R^3;\R^3)),
  \qquad
  \partial^\alpha p\in C([0,T];H^k(\R^3)),
 \]
 where $\partial^\alpha$ is the classical derivative of the smooth
 functions in (R2) and $H^k$ is the Sobolev space with the norm fixed
 below; the time derivative of $u$ is denoted $u_t$.
\item[(R2)] $u,p\in C^\infty([0,T]\times\R^3)$, $\operatorname{div}u(t)=0$
 pointwise, $p(t)=R_iR_j(u_i(t)u_j(t))$, and
 $u_t=\nu\Delta u-(u\cdot\nabla)u-\nabla p$ pointwise on $[0,T]\times\R^3$.
\item[(R3)] $u,\ \nabla u,\ \Delta u,\ u_t,\ p,\ \nabla p\in C([0,T];L^q(\R^3))$
 for every $2\le q\le\infty$.
\end{enumerate}
No decay of $u(t)$ beyond membership in $H^k$ is used, and no preserved
Schwartz property in time is assumed.

\emph{Notation.}  The Fourier transform, its $L^2$ extension $\mathcal F$
and the inverse transform $h\mapsto h^\vee$ are those of
Definition~\ref{def:lp}; we write $\hat f=\mathcal Ff$ for $f\in L^2$.
For an integer $m\ge0$ and $f\in L^2(\R^3)$ put
\begin{equation}\label{eq:qe-sobolev-norm}
 \norm f_{H^m}:=\norm{(1+|\xi|^2)^{m/2}\hat f}_{L^2(\R^3)},
 \qquad H^m(\R^3):=\{f\in L^2:\norm f_{H^m}<\infty\},
\end{equation}
componentwise for vector fields; Proposition~\ref{prop:localtheory} is read
with this norm, and passing to any equivalent norm on $H^m$ changes only the
constants in \eqref{eq:qe-embedding} below, not the memberships (R1).
$\langle f,g\rangle=\int_{\R^3}f\cdot g\,dx$ for real fields with
$f\cdot g\in L^1$.  For a $3\times3$ matrix $M$, $|M|$ is the operator norm
and $|M|_F=(\sum_{i,j}M_{ij}^2)^{1/2}$ the Frobenius norm; by the
Cauchy--Schwarz inequality $|Ma|^2=\sum_i(\sum_jM_{ij}a_j)^2\le|M|_F^2|a|^2$,
so
\begin{equation}\label{eq:qe-frobenius}
 |M|\le|M|_F .
\end{equation}
For a matrix field, $\norm{M}_\infty=\sup_x|M(x)|$.  For a
$C^1$ field $v:\R^3\to\R^3$, $Dv$ is the Jacobian matrix
$(Dv)_{ji}=\partial_iv_j$, so that for vectors $a$,
\begin{equation}\label{eq:qe-jacobian}
 (Dv\,a)_j=a_i\partial_iv_j=\bigl((a\cdot\nabla)v\bigr)_j,
 \qquad
 (Dv^{\mathsf T}a)_i=(\partial_iv_j)a_j ,
\end{equation}
with summation over repeated indices; $\nabla v$ denotes the same matrix.
$C_c(\R^3)$, $C^1_c(\R^3)$, $C_c^\infty(\R^3)$ are the continuous, $C^1$,
smooth functions with compact support, and $B_r$ is the open ball of radius
$r$ about the origin.  For $u\in L^3$ we write $q=q(u)$, $w=w(u)=u+q$,
$A=A(u)=|w|w$ as in Lemma~\ref{lem:quotient-minimizer}(b), and along the
solution $q(t)=q(u(t))$, $w(t)=w(u(t))$, $A(t)=A(u(t))$.  The constant
$C_{\mathbb P}=\norm{\mathbb P}_{L^3\to L^3}$ is that of
Lemma~\ref{lem:leray}(b).

\begin{lemma}[Bounded uniformly continuous representatives]
\label{lem:qe-embedding}
Let $f\in H^2(\R^3)$.  Then $f$ has a representative that is bounded and
uniformly continuous on $\R^3$, with
\begin{equation}\label{eq:qe-embedding}
 \norm f_\infty\le\pi\norm f_{H^2},
 \qquad
 \norm f_3\le\norm f_2^{2/3}\norm f_\infty^{1/3}\le\pi^{1/3}\norm f_{H^2}.
\end{equation}
Consequently, if $f\in H^{k+2}(\R^3)$ and $|\alpha|\le k$, then the
element $\partial^\alpha f$ of $L^2$ with Fourier transform
$(2\pi i\xi)^\alpha\hat f$ has a bounded uniformly continuous
representative with
$\norm{\partial^\alpha f}_\infty\le\pi(2\pi)^{|\alpha|}\norm f_{H^{k+2}}$.
\end{lemma}

\begin{proof}
By \eqref{eq:qe-sobolev-norm}, $(1+|\xi|^2)\hat f\in L^2$.  By the
Cauchy--Schwarz inequality,
\[
 \int_{\R^3}|\hat f(\xi)|\,d\xi
 \le\Bigl(\int_{\R^3}(1+|\xi|^2)^{-2}d\xi\Bigr)^{1/2}
 \Bigl(\int_{\R^3}(1+|\xi|^2)^{2}|\hat f(\xi)|^2d\xi\Bigr)^{1/2}
 =\pi\norm f_{H^2},
\]
because, with the substitution $r=\tan\vartheta$,
\[
 \int_{\R^3}(1+|\xi|^2)^{-2}d\xi
 =4\pi\int_0^\infty\frac{r^2}{(1+r^2)^{2}}dr
 =4\pi\int_0^{\pi/2}\sin^2\vartheta\,d\vartheta=\pi^2 .
\]
Put $g(x)=\int_{\R^3}e^{2\pi ix\cdot\xi}\hat f(\xi)\,d\xi$.  Then
$|g(x)|\le\norm{\hat f}_1\le\pi\norm f_{H^2}$ for every $x$, and for
$h\in\R^3$,
$|g(x+h)-g(x)|\le\int|e^{2\pi ih\cdot\xi}-1|\,|\hat f(\xi)|\,d\xi$, a bound
independent of $x$ which tends to $0$ as $h\to0$ by dominated convergence
(dominant $2|\hat f|\in L^1$).  Thus $g$ is bounded and uniformly
continuous.  Since $\hat f\in L^1\cap L^2$, the Fourier transform of $f$ in
the $L^2$ sense coincides almost everywhere with the absolutely convergent
integral defining $\hat f$, and the $L^2$ inverse transform
$\mathcal F^{-1}$ extends $h\mapsto h^\vee$,
$h^\vee(x)=\int e^{2\pi ix\cdot\xi}h(\xi)\,d\xi$, from $L^1\cap L^2$ to
$L^2$ with $\mathcal F^{-1}\mathcal Ff=f$ almost everywhere; both facts are
part of Definition~\ref{def:lp}, and their source is
\cite[\S2.2.4, pp.~113--114]{Grafakos2014}.  Applying this with
$h=\hat f\in L^1\cap L^2$ gives $g=(\hat f)^\vee=\mathcal F^{-1}\mathcal Ff=f$
almost everywhere; hence $g$ is a representative of $f$.  The second
inequality in \eqref{eq:qe-embedding} is
$\int|f|^3\le\norm f_\infty\int|f|^2$ together with
$\norm f_2\le\norm f_{H^2}$.  For the last claim apply the first part to
$\partial^\alpha f$: since $|\xi|^{|\alpha|}\le(1+|\xi|^2)^{k/2}$ for
$|\alpha|\le k$,
$|(2\pi i\xi)^\alpha\hat f|\le(2\pi)^{|\alpha|}(1+|\xi|^2)^{k/2}|\hat f|$,
so $\norm{\partial^\alpha f}_{H^2}\le(2\pi)^{|\alpha|}\norm f_{H^{k+2}}$
by \eqref{eq:qe-sobolev-norm}.
\end{proof}

By (R1) and Lemma~\ref{lem:qe-embedding}, for every $t\in[0,T]$ the fields
$u(t)$, $\nabla u(t)$, $\nabla^2u(t)$, $\Delta u(t)$, $u_t(t)$, $p(t)$,
$\nabla p(t)$ are bounded and uniformly continuous (a continuous function
that agrees almost everywhere with a continuous function agrees with it
everywhere), and each component of $\nabla^2u(t)$ is bounded by
$4\pi^3\norm{u(t)}_{H^4}$, which is bounded on $[0,T]$ because
$u\in C([0,T];H^4)$.  Moreover $(u\cdot\nabla)u=Du\,u$ is bounded and
uniformly continuous with
$\norm{(u\cdot\nabla)u}_3\le\norm u_\infty\norm{\nabla u}_3$, and
$t\mapsto(u(t)\cdot\nabla)u(t)$ belongs to $C([0,T];L^3)$ by (R3), since
$\norm{Du\,u-Dv\,v}_3\le\norm{Du-Dv}_3\norm u_\infty+\norm{Dv}_\infty\norm{u-v}_3$.
Finally $u(t)$ is solenoidal in the sense of Definition~\ref{def:quotient}:
for $\phi\in C_c^\infty$, integration by parts over a ball containing
$\operatorname{supp}\phi$ gives
$\int u(t)\cdot\nabla\phi\,dx=-\int(\operatorname{div}u(t))\phi\,dx=0$ by
(R2).

\begin{lemma}[Averaging in $L^3$]\label{lem:qe-average}
Let $s\ne0$, let $J$ be the closed interval with endpoints $0$ and $s$, and
let $F:(J\setminus\{0\})\times\R^3\to\R^3$ be continuous and bounded.  Then
$x\mapsto\int_0^sF(\sigma,x)\,d\sigma$ is continuous and bounded, and
\[
 \Bigl\|\int_0^sF(\sigma,\cdot)\,d\sigma\Bigr\|_3
 \le|s|\sup_{\sigma\in J\setminus\{0\}}\norm{F(\sigma,\cdot)}_3 .
\]
\end{lemma}

\begin{proof}
Continuity and boundedness of the integral follow from dominated
convergence with the constant dominant $\sup|F|$.  By H\"older's inequality
on $J$ with exponents $3$ and $3/2$,
$|\int_0^sF(\sigma,x)d\sigma|^3\le|s|^2\int_J|F(\sigma,x)|^3d\sigma$ for
every $x$.  Integrating in $x$ and applying Tonelli's theorem to the
nonnegative Borel function $|F|^3$ on $J\times\R^3$,
\[
 \int_{\R^3}\Bigl|\int_0^sF(\sigma,x)d\sigma\Bigr|^3dx
 \le|s|^2\int_J\norm{F(\sigma,\cdot)}_3^3\,d\sigma
 \le|s|^3\sup_{\sigma}\norm{F(\sigma,\cdot)}_3^3 .
\]
\end{proof}

\begin{lemma}[Gronwall]\label{lem:qe-gronwall}
Let $a,M\ge0$, $S>0$, and let $y:[0,S]\to[0,\infty)$ be continuous with
$y(t)\le a+M\int_0^ty(\sigma)\,d\sigma$ for all $t\in[0,S]$.  Then
$y(t)\le a\,e^{Mt}$ on $[0,S]$.  The same conclusion holds on $[-S,0]$ with
$|t|$ in place of $t$ if $y(t)\le a+M\bigl|\int_0^ty\bigr|$ there.
\end{lemma}

\begin{proof}
If $M=0$ there is nothing to prove.  Let $M>0$ and $Y(t)=\int_0^ty$, a $C^1$
function with $Y'=y\le a+MY$.  Then
$\frac d{dt}\bigl(e^{-Mt}Y(t)\bigr)=e^{-Mt}(Y'-MY)\le a\,e^{-Mt}$, and
integrating from $0$ to $t$ gives $e^{-Mt}Y(t)\le a(1-e^{-Mt})/M$, that is
$MY(t)\le a(e^{Mt}-1)$.  Hence $y(t)\le a+MY(t)\le a\,e^{Mt}$.  The
negative-time statement follows by applying this to $\tilde y(t)=y(-t)$ on
$[0,S]$, for which $|\int_0^{-t}y|=\int_0^t\tilde y$.
\end{proof}

\begin{lemma}[Gradients of $C^1_c$ functions lie in $\mathcal G_3$]
\label{lem:qe-mollify}
If $g\in C^1_c(\R^3)$ then $\nabla g\in\mathcal G_3$.
\end{lemma}

\begin{proof}
Fix $\rho\in C_c^\infty(\R^3)$ with $\rho\ge0$, $\int\rho=1$,
$\operatorname{supp}\rho\subset B_1$, and put
$\rho_\varepsilon=\varepsilon^{-3}\rho(\cdot/\varepsilon)$ for
$0<\varepsilon\le1$.  Let $g_\varepsilon(x)=\int\rho_\varepsilon(x-y)g(y)dy$.
Differentiation under the integral sign (the $y$-integral runs over the
compact set $\operatorname{supp}g$ and all derivatives of $\rho_\varepsilon$
are bounded) shows $g_\varepsilon\in C^\infty$, and
$\operatorname{supp}g_\varepsilon\subset\operatorname{supp}g+\overline{B_1}=:K$.
Writing $g_\varepsilon(x)=\int\rho_\varepsilon(y)g(x-y)dy$ and
differentiating under the integral sign (the $y$-integral runs over
$\overline{B_\varepsilon}$, and $\nabla g$ is bounded and continuous) gives
$\nabla g_\varepsilon(x)=\int\rho_\varepsilon(y)\nabla g(x-y)dy$.  Hence, with
$\omega(\varepsilon)=\sup_{|y|\le\varepsilon}\sup_x|\nabla g(x-y)-\nabla g(x)|$,
\[
 |\nabla g_\varepsilon(x)-\nabla g(x)|
 =\Bigl|\int\rho_\varepsilon(y)\bigl(\nabla g(x-y)-\nabla g(x)\bigr)dy\Bigr|
 \le\omega(\varepsilon),
\]
and the left side vanishes for $x\notin K$.  Therefore
$\norm{\nabla g_\varepsilon-\nabla g}_3\le\omega(\varepsilon)|K|^{1/3}\to0$
as $\varepsilon\to0$, because $\nabla g$ is uniformly continuous.  Since
$g_\varepsilon\in C_c^\infty$, $\nabla g$ is an $L^3$ limit of elements of
$\{\nabla\phi:\phi\in C_c^\infty\}$, i.e.\ $\nabla g\in\mathcal G_3$.
\end{proof}

\begin{lemma}[Pressure gradients are annihilated]\label{lem:quotient-pressure}
For every $t\in[0,T]$: $p(t)\in L^3$, $\nabla p(t)\in L^3\cap\mathcal G_3$,
and
\[
 D\mathcal Q(u(t))[\nabla p(t)]=\langle A(t),\nabla p(t)\rangle=0 .
\]
\end{lemma}

\begin{proof}
Fix $t$ and write $p=p(t)$.  By (R3), $p,\nabla p\in L^3$, and by (R2),
$p\in C^\infty(\R^3)$.  Choose $\chi\in C_c^\infty(\R^3)$ with
$0\le\chi\le1$, $\chi=1$ on $B_1$, $\chi=0$ outside $B_2$, and put
$\chi_R=\chi(\cdot/R)$ for $R\ge1$.  Then $\chi_Rp\in C^1_c(\R^3)$ and
$\nabla(\chi_Rp)-\nabla p=(\chi_R-1)\nabla p+p\,\nabla\chi_R$, so that
\begin{equation}\label{eq:qe-cutoff-error}
 \norm{\nabla(\chi_Rp)-\nabla p}_3
 \le\Bigl(\int_{|x|\ge R}|\nabla p|^3dx\Bigr)^{1/3}
 +\frac{\norm{\nabla\chi}_\infty}{R}\norm p_3 ,
\end{equation}
where we used $0\le1-\chi_R\le\mathbf 1_{\{|x|\ge R\}}$ and
$|\nabla\chi_R|\le R^{-1}\norm{\nabla\chi}_\infty$.  Both terms on the
right of \eqref{eq:qe-cutoff-error} tend to $0$ as $R\to\infty$: the first
by dominated convergence, since $|\nabla p|^3\in L^1$; the second because
$\norm p_3<\infty$.  By Lemma~\ref{lem:qe-mollify},
$\nabla(\chi_Rp)\in\mathcal G_3$ for every $R$, and $\mathcal G_3$ is closed
in $L^3$; hence $\nabla p\in\mathcal G_3$.  The last claim is the
stationarity condition Lemma~\ref{lem:quotient-minimizer}(c) applied with
$g=\nabla p$, together with the derivative formula of
Proposition~\ref{prop:quotient-derivative}.
\end{proof}

\begin{remark}[Pressure normalisation]\label{rem:qe-pressure-normalisation}
The pressure in (R2) is the normalised pressure
$p=R_iR_j(u_iu_j)=-\Delta^{-1}\partial_i\partial_j(u_iu_j)$ of
Proposition~\ref{prop:localtheory}; with the conventions of
Definition~\ref{def:lp} both expressions are the $L^2$ multiplier with
symbol $-\xi_i\xi_j/|\xi|^2$ applied to $u_iu_j$, so they coincide, as
recorded there.  This is the only pressure used in this section.
Lemma~\ref{lem:quotient-pressure} uses nothing about $p$ beyond $p\in C^1$
with $p,\nabla p\in L^3$; adding a function of time to $p$ would not change
$\nabla p$.
\end{remark}

\begin{lemma}[Chain rule along the trajectory]\label{lem:quotient-chainrule}
The function $t\mapsto\mathcal Q(u(t))$ belongs to $C^1([0,T])$, and for
every $t\in[0,T]$ (one-sided at the endpoints)
\begin{equation}\label{eq:qe-chainrule}
 \frac d{dt}\mathcal Q(u(t))
 =\langle A(t),u_t(t)\rangle
 =\nu\langle A(t),\Delta u(t)\rangle
 -\langle A(t),(u(t)\cdot\nabla)u(t)\rangle .
\end{equation}
\end{lemma}

\begin{proof}
\emph{Step 1: $u\in C^1([0,T];L^3)$.}  By (R1), $u\in C^1([0,T];H^2)$:
for every $t$, $\delta_h:=h^{-1}(u(t+h)-u(t))-u_t(t)\to0$ in $H^2$ as
$h\to0$ (with $t+h\in[0,T]$), and $u_t\in C([0,T];H^2)$.  By
\eqref{eq:qe-embedding}, $\norm f_3\le\pi^{1/3}\norm f_{H^2}$, so the same
convergence and continuity hold in $L^3$.  In particular
$\norm{u(t+h)-u(t)}_3\le|h|\bigl(\norm{u_t(t)}_3+\norm{\delta_h}_3\bigr)\le K|h|$
for $|h|\le h_0$, with $K=\norm{u_t(t)}_3+1$.

\emph{Step 2: derivative.}  Fix $t$ and put $\delta=u(t+h)-u(t)\in L^3$
and $w=w(t)$.  By Proposition~\ref{prop:quotient-derivative},
$\mathcal Q(u(t)+\delta)-\mathcal Q(u(t))=\langle A(t),\delta\rangle+r(\delta)$
with, by \eqref{eq:cp-derivative-remainder},
$|r(\delta)|\le6(\norm w_3+\norm\delta_3)^{3/2}\norm\delta_3^{3/2}$.  Hence,
for $0<|h|\le h_0$,
\[
 \frac{\mathcal Q(u(t+h))-\mathcal Q(u(t))}h
 =\Bigl\langle A(t),\frac{\delta}h\Bigr\rangle+\frac{r(\delta)}h,
 \qquad
 \Bigl|\frac{r(\delta)}h\Bigr|
 \le6\bigl(\norm w_3+K|h|\bigr)^{3/2}K^{3/2}|h|^{1/2}\longrightarrow0 .
\]
Since $\delta/h\to u_t(t)$ in $L^3$ and $A(t)\in L^{3/2}$, H\"older's
inequality gives $\langle A(t),\delta/h\rangle\to\langle A(t),u_t(t)\rangle$.
This proves the first equality in \eqref{eq:qe-chainrule}.

\emph{Step 3: continuity.}  By (R1) and \eqref{eq:qe-embedding},
$u\in C([0,T];L^3)$, so $t\mapsto A(t)$ is continuous into $L^{3/2}$ by
Lemma~\ref{lem:quotient-stability}, estimate \eqref{eq:cp-continuity}, and
$u_t\in C([0,T];L^3)$ by Step~1.  For $s,t\in[0,T]$,
$|\langle A(t),u_t(t)\rangle-\langle A(s),u_t(s)\rangle|
\le\norm{A(t)-A(s)}_{3/2}\norm{u_t(t)}_3+\norm{A(s)}_{3/2}\norm{u_t(t)-u_t(s)}_3$,
so the derivative is continuous and $\mathcal Q\circ u\in C^1([0,T])$.

\emph{Step 4: the equation.}  By (R2), $u_t=\nu\Delta u-(u\cdot\nabla)u-\nabla p$
pointwise, and each of the three terms belongs to $L^3$ (by (R3) and the
bound $\norm{(u\cdot\nabla)u}_3\le\norm u_\infty\norm{\nabla u}_3$).
Since $A(t)\in L^{3/2}$, the pairing is linear in the $L^3$ argument, and
$\langle A(t),\nabla p(t)\rangle=0$ by Lemma~\ref{lem:quotient-pressure}.
This is the second equality in \eqref{eq:qe-chainrule}.
\end{proof}

\subsection{The heat direction}
\label{subsec:qe-heat}

Recall from Definition~\ref{def:quotient} that $G_rf=k_r*f$ with
$k_r(x)=(4\pi r)^{-3/2}e^{-|x|^2/4r}$, $k_r\ge0$, $\int k_r=1$, and that
$\norm{G_rf}_3\le\norm f_3$ (Lemma~\ref{lem:quotient-heat}).  We also use
the same inequality for the truncated kernels
$k_r\mathbf 1_{\{|y|>\delta\}}$: for $k\in L^1$ and $f\in L^3$,
$\norm{k*f}_3\le\norm k_1\norm f_3$ (Minkowski's inequality
\cite[Thm.~1.2.10]{Grafakos2014}).  Put
\begin{equation}\label{eq:qe-eta}
 \eta(\rho)=\int_{|z|>\rho}k_1(z)\,dz,
 \qquad
 \int_{|y|>\delta}k_r(y)\,dy=\eta(\delta/\sqrt r),
\end{equation}
the second identity by the substitution $y=\sqrt r\,z$, under which
$k_r(y)\,dy=k_1(z)\,dz$; $\eta(\rho)\to0$ as $\rho\to\infty$ by dominated
convergence.

\begin{lemma}[Strong continuity of the heat semigroup]
\label{lem:qe-heat-continuity}\leavevmode
\begin{enumerate}
\item[(a)] If $f:\R^3\to\R^3$ is bounded and uniformly continuous, then
 $\sup_x|G_rf(x)-f(x)|\to0$ as $r\downarrow0$; moreover
 $(r,x)\mapsto G_rf(x)$ is continuous on $(0,\infty)\times\R^3$ and bounded
 by $\norm f_\infty$.
\item[(b)] If $f\in L^3(\R^3;\R^3)$, then $\norm{G_rf-f}_3\to0$ as
 $r\downarrow0$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) Let $\omega_f(\delta)=\sup_{|y|\le\delta}\sup_x|f(x-y)-f(x)|$, which
tends to $0$ as $\delta\to0$.  Since $\int k_r=1$,
\[
 |G_rf(x)-f(x)|
 =\Bigl|\int k_r(y)\bigl(f(x-y)-f(x)\bigr)dy\Bigr|
 \le\omega_f(\delta)+2\norm f_\infty\,\eta(\delta/\sqrt r)
\]
by \eqref{eq:qe-eta}.  Letting first $r\downarrow0$ and then
$\delta\downarrow0$ gives the uniform convergence.  For the joint
continuity fix $0<a<b$ and $R>0$; for $r\in[a,b]$ and $|x|\le R$,
$|k_r(x-y)f(y)|\le(4\pi a)^{-3/2}e^{-(|y|-R)_+^2/4b}\norm f_\infty$, an
integrable function of $y$, while $(r,x)\mapsto k_r(x-y)f(y)$ is
continuous for each $y$; dominated convergence gives continuity of
$G_rf(x)=\int k_r(x-y)f(y)dy$ on $[a,b]\times\overline{B_R}$.  The bound
$|G_rf|\le\norm f_\infty$ is $\int k_r=1$.

(b) Let $\varepsilon>0$ and choose $g\in C_c(\R^3;\R^3)$ with
$\norm{f-g}_3<\varepsilon$ (density of $C_c$ in $L^3$
\cite[Thm.~3.14]{Rudin1987}).  By the contraction property,
\[
 \norm{G_rf-f}_3
 \le\norm{G_r(f-g)}_3+\norm{G_rg-g}_3+\norm{g-f}_3
 \le2\varepsilon+\norm{G_rg-g}_3 .
\]
For $\delta>0$ split
$G_rg(x)-g(x)=\int_{|y|\le\delta}k_r(y)(g(x-y)-g(x))dy
+\int_{|y|>\delta}k_r(y)(g(x-y)-g(x))dy=:I_1(x)+I_2(x)$.
The first integrand vanishes unless $x\in K_\delta:=\operatorname{supp}g+\overline{B_\delta}$,
and $|I_1|\le\omega_g(\delta)$, so
$\norm{I_1}_3\le\omega_g(\delta)|K_\delta|^{1/3}$.  For the second,
$|I_2|\le(k_r\mathbf 1_{\{|y|>\delta\}})*|g|+\eta(\delta/\sqrt r)|g|$, so by
Minkowski's inequality and \eqref{eq:qe-eta},
$\norm{I_2}_3\le2\eta(\delta/\sqrt r)\norm g_3$.  Hence
$\limsup_{r\downarrow0}\norm{G_rg-g}_3\le\omega_g(\delta)|K_\delta|^{1/3}$
for every $\delta\in(0,1]$, and letting $\delta\downarrow0$ (with
$|K_\delta|\le|K_1|$) gives $\norm{G_rg-g}_3\to0$.  Thus
$\limsup_{r\downarrow0}\norm{G_rf-f}_3\le2\varepsilon$ for every
$\varepsilon>0$.
\end{proof}

\begin{lemma}[Heat generator in $L^3$]\label{lem:heat-generator}
Let $f\in C^2(\R^3;\R^3)$ with $f$, $\nabla f$, $\nabla^2f$ bounded, and
$\Delta f$ bounded, uniformly continuous, and in $L^3$.  Then for every
$s>0$ and every $x\in\R^3$,
\begin{equation}\label{eq:qe-heat-integral}
 G_sf(x)-f(x)=\int_0^s(G_r\Delta f)(x)\,dr ,
\end{equation}
where the integrand is continuous and bounded on $(0,s]\times\R^3$.
Consequently
\begin{equation}\label{eq:qe-generator}
 \norm{G_sf-f}_3\le s\norm{\Delta f}_3,
 \qquad
 \Bigl\|\frac{G_sf-f}s-\Delta f\Bigr\|_3
 \le\sup_{0<r\le s}\norm{G_r\Delta f-\Delta f}_3\longrightarrow0
 \quad(s\downarrow0).
\end{equation}
In particular \eqref{eq:qe-heat-integral}--\eqref{eq:qe-generator} hold for
$f=u(t)$, every $t\in[0,T]$.
\end{lemma}

\begin{proof}
\emph{Step 1: the kernel solves the heat equation.}  For $r>0$ and
$z\in\R^3$, direct differentiation of $k_r(z)=(4\pi r)^{-3/2}e^{-|z|^2/4r}$
gives
\[
 \partial_rk_r(z)=k_r(z)\Bigl(-\frac3{2r}+\frac{|z|^2}{4r^2}\Bigr),
 \qquad
 \partial_j k_r(z)=-\frac{z_j}{2r}k_r(z),
 \qquad
 \Delta k_r(z)=k_r(z)\Bigl(\frac{|z|^2}{4r^2}-\frac3{2r}\Bigr),
\]
so $\partial_rk_r=\Delta k_r$.  For $0<a\le r\le b$,
\begin{equation}\label{eq:qe-kernel-dominant}
 |\partial_rk_r(z)|\le D_{a,b}(z):=(4\pi a)^{-3/2}
 \Bigl(\frac3{2a}+\frac{|z|^2}{4a^2}\Bigr)e^{-|z|^2/4b},
 \qquad D_{a,b}\in L^1(\R^3),
\end{equation}
and likewise $|\nabla k_r|,|\nabla^2k_r|\le D'_{a,b}$ with
$D'_{a,b}\in L^1$ of the same Gaussian form.

\emph{Step 2: $(\Delta k_r)*f=k_r*\Delta f$.}  Fix $r>0$, $x\in\R^3$ and
$j\in\{1,2,3\}$.  For fixed values of the two coordinates $y_l$, $l\ne j$,
the one-dimensional function $y_j\mapsto k_r(x-y)$ is smooth with
$\partial_{y_j}[k_r(x-y)]=-(\partial_jk_r)(x-y)$ and
$\partial_{y_j}^2[k_r(x-y)]=(\partial_j^2k_r)(x-y)$, and it decays with all
its derivatives like a Gaussian as $|y_j|\to\infty$, while $f$ and
$\partial_jf$ are bounded.  Two integrations by parts on $\R$ (the boundary
terms $k_r(x-y)\partial_jf(y)$ and $(\partial_jk_r)(x-y)f(y)$ vanish at
$y_j=\pm\infty$) give
$\int_\R(\partial_j^2k_r)(x-y)f(y)\,dy_j=\int_\R k_r(x-y)\partial_j^2f(y)\,dy_j$.
Both integrands are absolutely integrable over $\R^3$ (Gaussian times
bounded), so Fubini's theorem lets us integrate over the remaining two
coordinates and sum over $j$:
$\int(\Delta k_r)(x-y)f(y)dy=\int k_r(x-y)\Delta f(y)dy=(G_r\Delta f)(x)$.

\emph{Step 3: differentiation in $r$.}  Fix $x$.  For $r\in[a,b]\subset(0,\infty)$,
$G_rf(x)=\int k_r(x-y)f(y)dy$, the integrand is $C^1$ in $r$ with
$|\partial_rk_r(x-y)f(y)|\le D_{a,b}(x-y)\norm f_\infty$, an integrable
function of $y$ by \eqref{eq:qe-kernel-dominant}.  Differentiation under
the integral sign and Steps~1--2 give that $r\mapsto G_rf(x)$ is $C^1$ on
$(0,\infty)$ with
$\frac d{dr}G_rf(x)=\int(\Delta k_r)(x-y)f(y)dy=(G_r\Delta f)(x)$.
By the fundamental theorem of calculus, for $0<a<s$,
$G_sf(x)-G_af(x)=\int_a^s(G_r\Delta f)(x)dr$.

\emph{Step 4: $a\downarrow0$.}  By Lemma~\ref{lem:qe-heat-continuity}(a)
applied to the bounded uniformly continuous $f$, $G_af(x)\to f(x)$; and
since $|G_r\Delta f(x)|\le\norm{\Delta f}_\infty$, the integral over $[a,s]$
converges to the integral over $(0,s]$.  This is
\eqref{eq:qe-heat-integral}.  The integrand $(r,x)\mapsto G_r\Delta f(x)$
is continuous and bounded on $(0,s]\times\R^3$ by
Lemma~\ref{lem:qe-heat-continuity}(a) applied to $\Delta f$.

\emph{Step 5: the $L^3$ limits.}  By \eqref{eq:qe-heat-integral},
$\frac{G_sf-f}s-\Delta f=\frac1s\int_0^s\bigl(G_r\Delta f-\Delta f\bigr)dr$
pointwise, and $F(r,x)=G_r\Delta f(x)-\Delta f(x)$ is continuous and bounded
on $(0,s]\times\R^3$.  Lemma~\ref{lem:qe-average} gives the second
inequality in \eqref{eq:qe-generator}, and the right side tends to $0$ by
Lemma~\ref{lem:qe-heat-continuity}(b) applied to $\Delta f\in L^3$.  The
first inequality is Lemma~\ref{lem:qe-average} applied to
$F(r,x)=G_r\Delta f(x)$ together with $\norm{G_r\Delta f}_3\le\norm{\Delta f}_3$.

\emph{The case $f=u(t)$.}  By (R2), $u(t)\in C^\infty$; by (R1) and
Lemma~\ref{lem:qe-embedding}, $u(t)$, $\nabla u(t)$, $\nabla^2u(t)$ are
bounded and $\Delta u(t)$ is bounded and uniformly continuous; by (R3),
$\Delta u(t)\in L^3$.
\end{proof}

\begin{definition}[Quotient dissipation]\label{def:qe-dissipation}
For $t\in[0,T]$ put
\[
 D_{\mathcal Q}(u(t)):=-\langle A(t),\Delta u(t)\rangle
 =-\int_{\R^3}|w(t)|\,w(t)\cdot\Delta u(t)\,dx .
\]
The integral converges absolutely, since $A(t)\in L^{3/2}$
(Lemma~\ref{lem:quotient-minimizer}(b)) and $\Delta u(t)\in L^3$ (R3).
\end{definition}

\begin{lemma}[Nonnegative quotient dissipation]\label{lem:quotient-heatsign}
For every $t\in[0,T]$, $D_{\mathcal Q}(u(t))\ge0$, and
$t\mapsto D_{\mathcal Q}(u(t))$ is continuous on $[0,T]$.
\end{lemma}

\begin{proof}
Fix $t$, write $u=u(t)$, $A=A(t)$, $w=w(t)$, and put $h_s=G_su-u\in L^3$
for $s>0$.  By Lemma~\ref{lem:quotient-heat}, $\mathcal Q(G_su)\le\mathcal Q(u)$.
By Proposition~\ref{prop:quotient-derivative} and
\eqref{eq:cp-derivative-remainder},
$\mathcal Q(u+h_s)-\mathcal Q(u)=\langle A,h_s\rangle+r(h_s)$ with
$|r(h_s)|\le6(\norm w_3+\norm{h_s}_3)^{3/2}\norm{h_s}_3^{3/2}$, and
$\norm{h_s}_3\le s\norm{\Delta u}_3$ by Lemma~\ref{lem:heat-generator},
inequality \eqref{eq:qe-generator}.  Hence
\[
 0\ge\frac{\mathcal Q(G_su)-\mathcal Q(u)}s
 =\Bigl\langle A,\frac{h_s}s\Bigr\rangle+\frac{r(h_s)}s,
 \qquad
 \Bigl|\frac{r(h_s)}s\Bigr|
 \le6\bigl(\norm w_3+s\norm{\Delta u}_3\bigr)^{3/2}\norm{\Delta u}_3^{3/2}s^{1/2}\to0 .
\]
By \eqref{eq:qe-generator}, $h_s/s\to\Delta u$ in $L^3$, so
$\langle A,h_s/s\rangle\to\langle A,\Delta u\rangle$ by H\"older's
inequality.  Therefore $\langle A,\Delta u\rangle\le0$, i.e.\
$D_{\mathcal Q}(u(t))\ge0$.  Continuity in $t$ follows from
$A\in C([0,T];L^{3/2})$ (Step~3 of Lemma~\ref{lem:quotient-chainrule}) and
$\Delta u\in C([0,T];L^3)$ (R3), by the same H\"older estimate.
\end{proof}

\begin{remark}[Scope of the dissipation sign]\label{rem:qe-heatsign-scope}
Its sign follows by differentiating the heat contraction at zero;
$\Delta u\in L^3$ justifies this generator limit.  No quantitative
comparison with the original cubic dissipation is claimed.  In particular,
no lower bound for $D_{\mathcal Q}$ in terms of $D_3$ of
Proposition~\ref{prop:pressure}, or in terms of any norm of $u$, is
asserted.
\end{remark}

\subsection{Transport by inner variation and the evolution identity}
\label{subsec:qe-transport}

One can rewrite transport without differentiating the $L^3$ minimizer.
The device is the flow of the frozen velocity field; we prove the needed
facts about it in full.

\begin{lemma}[Jacobi's formula]\label{lem:qe-jacobi}
Let $M:I\to\R^{3\times3}$ be differentiable on an interval $I$.  Then
$\det M$ is differentiable on $I$ and
$(\det M)'=\operatorname{tr}\bigl(\operatorname{adj}(M)\,M'\bigr)$, where
$\operatorname{adj}(M)$ is the adjugate matrix, characterised by
$M\operatorname{adj}(M)=\operatorname{adj}(M)M=(\det M)I$.  In particular,
if $M'=BM$ on $I$ for a matrix function $B$, then
$(\det M)'=(\operatorname{tr}B)\det M$.
\end{lemma}

\begin{proof}
By the Leibniz formula $\det M=\sum_\sigma\operatorname{sgn}\sigma\prod_{l=1}^3M_{\sigma(l)l}$
(sum over permutations of $\{1,2,3\}$), and the product rule,
\[
 (\det M)'=\sum_{i=1}^3\sum_\sigma\operatorname{sgn}\sigma\;M'_{\sigma(i)i}\prod_{l\ne i}M_{\sigma(l)l}
 =\sum_{i,k=1}^3M'_{ki}\,C_{ki},
 \qquad
 C_{ki}:=\sum_{\sigma:\sigma(i)=k}\operatorname{sgn}\sigma\prod_{l\ne i}M_{\sigma(l)l}.
\]
$C_{ki}$ is the determinant of the matrix obtained from $M$ by replacing
its $i$-th column with the unit vector $e_k$ (in the Leibniz formula for
that matrix only the permutations with $\sigma(i)=k$ contribute), i.e.\ the
$(k,i)$ cofactor of $M$, and $\operatorname{adj}(M)_{ik}=C_{ki}$ is the
definition of the adjugate, for which the cofactor expansion of the
determinant along a column gives $M\operatorname{adj}(M)=\operatorname{adj}(M)M=(\det M)I$.  Hence
$(\det M)'=\sum_{i,k}\operatorname{adj}(M)_{ik}M'_{ki}=\operatorname{tr}(\operatorname{adj}(M)M')$.
If $M'=BM$ then, using $\operatorname{tr}(XY)=\operatorname{tr}(YX)$,
$\operatorname{tr}(\operatorname{adj}(M)BM)=\operatorname{tr}(BM\operatorname{adj}(M))
=\operatorname{tr}\bigl(B\,(\det M)I\bigr)=(\operatorname{tr}B)\det M$.
\end{proof}

\begin{lemma}[Flow of a bounded divergence-free field]\label{lem:flow}
Let $b\in C^1(\R^3;\R^3)$ with $\norm b_\infty<\infty$,
$\Lambda:=\sup_y|Db(y)|<\infty$, $Db$ uniformly continuous with modulus
$\omega(\rho)=\sup_{|y-y'|\le\rho}|Db(y)-Db(y')|$ (a nondecreasing
function of $\rho$ with $\omega(\rho)\to0$ as $\rho\to0$), and
$\operatorname{div}b=\operatorname{tr}Db=0$.  Then:
\begin{enumerate}
\item[(a)] (\emph{Global flow.})  For every $y\in\R^3$ there is a unique
 $C^1$ curve $s\mapsto\Phi_s(y)$ on $\R$ with $\partial_s\Phi_s(y)=b(\Phi_s(y))$
 and $\Phi_0(y)=y$.  For all $s,r\in\R$ and $y,y'\in\R^3$,
 \[
  \Phi_{s+r}=\Phi_s\circ\Phi_r,\qquad
  |\Phi_s(y)-y|\le|s|\norm b_\infty,\qquad
  |\Phi_s(y)-\Phi_s(y')|\le e^{\Lambda|s|}|y-y'| ,
 \]
 and $(s,y)\mapsto\Phi_s(y)$ is continuous on $\R\times\R^3$.
\item[(b)] (\emph{Differentiability.})  For each $s$, $\Phi_s\in C^1(\R^3;\R^3)$,
 and $M_s(y):=D\Phi_s(y)$ is the unique solution of the linear equation
 $\partial_sM_s(y)=Db(\Phi_s(y))M_s(y)$, $M_0(y)=I$.  The map
 $(s,y)\mapsto D\Phi_s(y)$ is continuous, and $|D\Phi_s(y)|\le e^{\Lambda|s|}$.
\item[(c)] (\emph{Diffeomorphism, volume preservation.})  $\Phi_s$ is a
 $C^1$ diffeomorphism of $\R^3$ with inverse $\Phi_{-s}$, and
 $D\Phi_{-s}(\Phi_s(y))=D\Phi_s(y)^{-1}$.  For all $s$ and $y$,
 $\det D\Phi_s(y)=1$.
\item[(d)] (\emph{Expansions.})  Uniformly in $y$,
 \begin{align}
  |D\Phi_s(y)-I|&\le\Lambda|s|e^{\Lambda|s|},
  \label{eq:qe-flow-first}\\
  |D\Phi_s(y)-I-s\,Db(y)|&\le|s|e^{\Lambda|s|}\bigl(\omega(|s|\norm b_\infty)+\Lambda^2|s|\bigr)
  =:|s|\,\beta(s),
  \label{eq:qe-flow-second}
 \end{align}
 with $\beta(s)\to0$ as $s\to0$.  Let $s_0=1/(4\Lambda)$ ($s_0=\infty$ if
 $\Lambda=0$).  For $|s|\le s_0$ the matrix
 $E_s(y):=D\Phi_s(y)^{-\mathsf T}-I$ satisfies
 \begin{equation}\label{eq:qe-flow-inverse}
  |E_s(y)|\le2\Lambda|s|e^{\Lambda|s|},
  \qquad
  |E_s(y)+s\,Db(y)^{\mathsf T}|\le|s|\beta(s)+2\Lambda^2s^2e^{2\Lambda|s|} .
 \end{equation}
 In particular $\norm{E_s}_\infty\to0$ and
 $\norm{s^{-1}E_s+Db^{\mathsf T}}_\infty\to0$ as $s\to0$.
\end{enumerate}
\end{lemma}

\begin{proof}
\emph{Preliminaries.}  For $z,z'\in\R^3$,
$b(z)-b(z')=\int_0^1Db(z'+\vartheta(z-z'))(z-z')\,d\vartheta$, so
$|b(z)-b(z')|\le\Lambda|z-z'|$ and
\begin{equation}\label{eq:qe-taylor-b}
 |b(z)-b(z')-Db(z')(z-z')|
 =\Bigl|\int_0^1\bigl[Db(z'+\vartheta(z-z'))-Db(z')\bigr](z-z')\,d\vartheta\Bigr|
 \le\omega(|z-z'|)\,|z-z'| .
\end{equation}
If $\Lambda=0$ then $Db\equiv0$, $b$ is a constant vector $b_0$,
$\Phi_s(y)=y+sb_0$, $D\Phi_s=I$, and every claim is immediate; we assume
$\Lambda>0$ below.

(a) Fix $S>0$ and $y\in\R^3$.  Let $X=C([-S,S];\R^3)$ with the norm
$\norm x_*=\sup_{|s|\le S}e^{-2\Lambda|s|}|x(s)|$, which is equivalent to
the supremum norm; $X$ is complete.  Define
$(\mathcal Kx)(s)=y+\int_0^sb(x(\sigma))\,d\sigma$; $\mathcal Kx\in X$ since
$b\circ x$ is continuous.  For $x,x'\in X$ and $0\le s\le S$,
\[
 |\mathcal Kx(s)-\mathcal Kx'(s)|
 \le\Lambda\int_0^s|x(\sigma)-x'(\sigma)|\,d\sigma
 \le\Lambda\norm{x-x'}_*\int_0^se^{2\Lambda\sigma}d\sigma
 \le\tfrac12e^{2\Lambda s}\norm{x-x'}_* ,
\]
and symmetrically for $-S\le s\le0$; hence
$\norm{\mathcal Kx-\mathcal Kx'}_*\le\frac12\norm{x-x'}_*$.  By the Banach
fixed point theorem $\mathcal K$ has a unique fixed point $x_y\in X$.  By
the fundamental theorem of calculus $x_y$ is $C^1$ with $x_y'=b(x_y)$,
$x_y(0)=y$; conversely every $C^1$ solution on $[-S,S]$ is a fixed point of
$\mathcal K$, so $x_y$ is the unique solution on $[-S,S]$.  Solutions on
$[-S,S]$ and $[-S',S']$ agree on the smaller interval by this uniqueness,
so they define a unique global solution $\Phi_s(y)$, $s\in\R$.  The group
property: for fixed $r$, both $s\mapsto\Phi_{s+r}(y)$ and
$s\mapsto\Phi_s(\Phi_r(y))$ solve $x'=b(x)$ with $x(0)=\Phi_r(y)$, hence
coincide.  The bound $|\Phi_s(y)-y|\le|\int_0^s|b(\Phi_\sigma(y))|d\sigma|\le|s|\norm b_\infty$
is immediate.  For the Lipschitz bound put $d(s)=|\Phi_s(y)-\Phi_s(y')|$;
then $d(s)\le|y-y'|+\Lambda|\int_0^sd(\sigma)d\sigma|$, and
Lemma~\ref{lem:qe-gronwall} gives $d(s)\le e^{\Lambda|s|}|y-y'|$.  Joint
continuity: $|\Phi_s(y)-\Phi_{s'}(y')|\le e^{\Lambda|s|}|y-y'|+|s-s'|\norm b_\infty$.

(b) \emph{The variational equation.}  Fix $y$ and put
$B(s)=Db(\Phi_s(y))$, continuous in $s$ with $|B(s)|\le\Lambda$.  The map
\[
 (\mathcal LM)(s)=I+\int_0^sB(\sigma)M(\sigma)\,d\sigma
\]
on $C([-S,S];\R^{3\times3})$ with the norm
$\norm M_*=\sup_{|s|\le S}e^{-2\Lambda|s|}|M(s)|$ satisfies the same contraction estimate as $\mathcal K$ (replace
$|b(x)-b(x')|\le\Lambda|x-x'|$ by $|B(\sigma)(M-M')|\le\Lambda|M-M'|$), so
there is a unique global solution $M_s(y)$ of $M'=B(s)M$, $M_0=I$.  From
$|M_s|\le1+\Lambda|\int_0^s|M_\sigma|d\sigma|$ and
Lemma~\ref{lem:qe-gronwall}, $|M_s(y)|\le e^{\Lambda|s|}$.

\emph{Continuity of $M$ in $(s,y)$.}  Fix $s\ne0$ and $y,y'$, and put
$Z(\sigma)=M_\sigma(y)-M_\sigma(y')$ for $\sigma$ between $0$ and $s$.
Then $Z(0)=0$ and
$Z'=Db(\Phi_\sigma(y))Z+\bigl[Db(\Phi_\sigma(y))-Db(\Phi_\sigma(y'))\bigr]M_\sigma(y')$,
so by (a), and because $\omega$ is nondecreasing,
\[
 |Z(\sigma)|\le\Lambda\Bigl|\int_0^\sigma|Z|\Bigr|
 +|s|\,e^{\Lambda|s|}\,\omega\bigl(e^{\Lambda|s|}|y-y'|\bigr)
 \qquad(\sigma\text{ between }0\text{ and }s).
\]
For this fixed $s$ the second term is a constant $a$, and
Lemma~\ref{lem:qe-gronwall}, applied on the interval with endpoints $0$ and
$s$, gives
$|Z(s)|\le|s|e^{2\Lambda|s|}\omega\bigl(e^{\Lambda|s|}|y-y'|\bigr)$, which
tends to $0$ as $y'\to y$ uniformly for $|s|\le S$.  Together with
$|M_s(y)-M_{s'}(y)|\le\Lambda e^{\Lambda S}|s-s'|$ this gives joint
continuity.

\emph{$M_s(y)$ is the derivative of $\Phi_s$ at $y$.}  Fix $s\ne0$, $y$ and
$h\in\R^3$, and put $z(\sigma)=\Phi_\sigma(y+h)-\Phi_\sigma(y)-M_\sigma(y)h$
for $\sigma$ between $0$ and $s$.  Then $z(0)=0$ and, with
$\zeta(\sigma)=\Phi_\sigma(y+h)-\Phi_\sigma(y)$,
\[
 z'(\sigma)
 =\bigl[b(\Phi_\sigma(y+h))-b(\Phi_\sigma(y))-Db(\Phi_\sigma(y))\zeta(\sigma)\bigr]
 +Db(\Phi_\sigma(y))\,z(\sigma).
\]
By \eqref{eq:qe-taylor-b}, (a), and the monotonicity of $\omega$, the
bracket is bounded by
$\omega(|\zeta(\sigma)|)|\zeta(\sigma)|\le\omega(e^{\Lambda|s|}|h|)e^{\Lambda|s|}|h|$
for all $\sigma$ between $0$ and $s$.  Hence
$|z(\sigma)|\le|s|e^{\Lambda|s|}\omega(e^{\Lambda|s|}|h|)|h|+\Lambda|\int_0^\sigma|z||$
on that interval, with a constant first term, and
Lemma~\ref{lem:qe-gronwall} on the interval with endpoints $0$ and $s$
gives
\[
 |\Phi_s(y+h)-\Phi_s(y)-M_s(y)h|
 \le|s|e^{2\Lambda|s|}\,\omega\bigl(e^{\Lambda|s|}|h|\bigr)\,|h|=o(|h|)
 \qquad(h\to0),
\]
uniformly in $y$.  Thus $\Phi_s$ is differentiable at every $y$ with
$D\Phi_s(y)=M_s(y)$, and $D\Phi_s$ is continuous in $y$, so $\Phi_s\in C^1$
(for $s=0$, $\Phi_0=\mathrm{id}$ and $M_0=I$).

(c) By the group property, $\Phi_{-s}\circ\Phi_s=\Phi_0=\mathrm{id}$ and
$\Phi_s\circ\Phi_{-s}=\mathrm{id}$, so $\Phi_s$ is a bijection with inverse
$\Phi_{-s}$; both are $C^1$ by (b), and the chain rule applied to
$\Phi_{-s}\circ\Phi_s=\mathrm{id}$ gives $D\Phi_{-s}(\Phi_s(y))D\Phi_s(y)=I$.
For the volume claim apply Lemma~\ref{lem:qe-jacobi} to $s\mapsto M_s(y)$,
which satisfies $M'=B(s)M$ with $B(s)=Db(\Phi_s(y))$:
\[
 \frac d{ds}\det M_s(y)=\operatorname{tr}\bigl(Db(\Phi_s(y))\bigr)\det M_s(y)
 =(\operatorname{div}b)(\Phi_s(y))\det M_s(y)=0 ,
\]
and $\det M_0(y)=\det I=1$; hence $\det D\Phi_s(y)=\det M_s(y)=1$ for all
$s$.  (This is Liouville's formula for the divergence-free field $b$.)

(d) From $M_s-I=\int_0^sDb(\Phi_\sigma(y))M_\sigma d\sigma$ and (b),
$|M_s-I|\le\Lambda|s|e^{\Lambda|s|}$, which is \eqref{eq:qe-flow-first}.
Next,
\[
 M_s-I-s\,Db(y)
 =\int_0^s\bigl[Db(\Phi_\sigma(y))-Db(y)\bigr]M_\sigma\,d\sigma
 +Db(y)\int_0^s\bigl(M_\sigma-I\bigr)d\sigma .
\]
Since $|\Phi_\sigma(y)-y|\le|\sigma|\norm b_\infty\le|s|\norm b_\infty$, the
first integrand is bounded by $\omega(|s|\norm b_\infty)e^{\Lambda|s|}$, and
the second by $\Lambda\cdot\Lambda|s|e^{\Lambda|s|}$ by
\eqref{eq:qe-flow-first}; integrating over an interval of length $|s|$
gives \eqref{eq:qe-flow-second}.  For the inverse, let $N=M_s-I$.  If
$|s|\le s_0=1/(4\Lambda)$ then $|N|\le\frac14e^{1/4}<\frac12$, so
$(I+N)^{-1}=\sum_{n\ge0}(-N)^n$ converges and
\[
 |(I+N)^{-1}-I|\le\frac{|N|}{1-|N|}\le2|N|,
 \qquad
 |(I+N)^{-1}-I+N|=\Bigl|\sum_{n\ge2}(-N)^n\Bigr|\le\frac{|N|^2}{1-|N|}\le2|N|^2 .
\]
Since $M_s^{-1}=(I+N)^{-1}$, the first bound with \eqref{eq:qe-flow-first}
gives $|M_s^{-1}-I|\le2\Lambda|s|e^{\Lambda|s|}$, and
$M_s^{-1}-I+s\,Db(y)=\bigl[(I+N)^{-1}-I+N\bigr]-\bigl[N-s\,Db(y)\bigr]$ gives
$|M_s^{-1}-I+s\,Db(y)|\le2\Lambda^2s^2e^{2\Lambda|s|}+|s|\beta(s)$ by
\eqref{eq:qe-flow-second}.  Transposing (the operator norm is invariant
under transposition) yields \eqref{eq:qe-flow-inverse}.  Finally
$\beta(s)\to0$ because $\omega(\rho)\to0$ as $\rho\to0$.
\end{proof}

\begin{remark}[Inputs of the flow lemma]\label{rem:qe-flow-inputs}
Lemma~\ref{lem:flow} is proved from the Banach fixed point theorem,
Lemma~\ref{lem:qe-gronwall} and Lemma~\ref{lem:qe-jacobi} only.  Only
boundedness and uniform continuity of $Db$ enter; boundedness of $D^2b$,
available for $b=u(t)$ by Lemma~\ref{lem:qe-embedding}, would improve
$|s|\beta(s)$ to $O(s^2)$ but is not needed.
\end{remark}

\begin{lemma}[Pullback by a volume-preserving diffeomorphism]
\label{lem:qe-pullback}
Let $\Phi:\R^3\to\R^3$ be a $C^1$ diffeomorphism with
$\Lambda_\Phi:=\sup_x|D\Phi(x)|<\infty$ and $\det D\Phi\equiv1$.
\begin{enumerate}
\item[(a)] For every nonnegative measurable $f$ on $\R^3$,
 $\int f\circ\Phi\,dx=\int f\,dx$; $\Phi^{-1}$ maps Lebesgue null sets to
 null sets, so $f\mapsto f\circ\Phi$ is a well-defined linear isometry of
 $L^r(\R^3;\R^3)$ for every $1\le r<\infty$.  The map
 $T_\Phi f:=D\Phi^{\mathsf T}(f\circ\Phi)$ satisfies
 $\norm{T_\Phi f}_3\le\Lambda_\Phi\norm f_3$.
\item[(b)] $T_\Phi\nabla\phi=\nabla(\phi\circ\Phi)$ for $\phi\in C^1(\R^3)$,
 and $T_\Phi\mathcal G_3\subset\mathcal G_3$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) The change of variables formula \cite[Thm.~7.26]{Rudin1987}, applied
with $X=V=\R^3$ and $T=\Phi$ (continuous, one-to-one, differentiable at
every point, so that its hypotheses (i)--(iii) hold with
$T(V\setminus X)=\emptyset$), reads
\[
 \int_{\Phi(\R^3)}f\,dx=\int_{\R^3}|\det D\Phi(y)|\,f(\Phi(y))\,dy
 \qquad\text{for every Lebesgue measurable }f:\R^3\to[0,\infty];
\]
here $\Phi(\R^3)=\R^3$ and $|\det D\Phi|=1$.  Applying it to the indicator
of a Borel null set $N$ gives $|\Phi^{-1}(N)|=\int\mathbf 1_N\circ\Phi=|N|=0$,
so $f\circ\Phi$ depends only on the equivalence class of $f$ (a Lebesgue
measurable $f$ agrees with a Borel function off a null set).  Applying the
formula to $|f|^r$ gives the isometry, and
$|T_\Phi f(x)|^3\le\Lambda_\Phi^3|f(\Phi(x))|^3$ integrates to the last
claim.

(b) The chain rule gives
$\partial_i(\phi\circ\Phi)(x)=(\partial_j\phi)(\Phi(x))\,\partial_i\Phi_j(x)
=\bigl(D\Phi(x)^{\mathsf T}\nabla\phi(\Phi(x))\bigr)_i$ by
\eqref{eq:qe-jacobian}, i.e.\ $\nabla(\phi\circ\Phi)=T_\Phi\nabla\phi$.  If
$\phi\in C_c^\infty$, then $\phi\circ\Phi\in C^1$ and its support
$\Phi^{-1}(\operatorname{supp}\phi)$ is compact, being the image of a
compact set under the continuous map $\Phi^{-1}$; so
$T_\Phi\nabla\phi\in\mathcal G_3$ by Lemma~\ref{lem:qe-mollify}.  For
general $g\in\mathcal G_3$ choose $\phi_n\in C_c^\infty$ with
$\nabla\phi_n\to g$ in $L^3$; then $T_\Phi\nabla\phi_n\to T_\Phi g$ in
$L^3$ by (a), and $\mathcal G_3$ is closed.
\end{proof}

\begin{lemma}[Transport identity]\label{lem:quotient-transport}
For every $t\in[0,T]$, with $u=u(t)$, $q=q(t)$, $A=A(t)$,
\begin{equation}\label{eq:qe-transport}
 \int_{\R^3}A\cdot\bigl((u\cdot\nabla)u\bigr)dx
 =\int_{\R^3}q\cdot\bigl((A\cdot\nabla)u\bigr)dx ,
\end{equation}
that is, in components,
\begin{equation}\label{eq:qe-contraction}
 \int_{\R^3}A_j\,u_i\,\partial_iu_j\,dx
 =\int_{\R^3}q_j\,A_i\,\partial_iu_j\,dx
 =\langle A,\,Du^{\mathsf T}q\rangle .
\end{equation}
Both integrals converge absolutely:
\[
 |\langle A,(u\cdot\nabla)u\rangle|\le\norm A_{3/2}\norm{(u\cdot\nabla)u}_3,
 \qquad
 |\langle A,Du^{\mathsf T}q\rangle|\le\norm A_{3/2}\norm{Du}_\infty\norm q_3 .
\]
\end{lemma}

\begin{proof}
Fix $t$.  \emph{Step 1: the flow.}  By (R1)--(R3) and
Lemma~\ref{lem:qe-embedding}, $b:=u(t)$ is $C^\infty$ with $u$, $Du$,
$D^2u$ bounded; hence $Du$ is Lipschitz with constant
$\norm{D^2u}_\infty$, so uniformly continuous with
$\omega(\rho)\le\norm{D^2u}_\infty\rho$, and $\operatorname{div}u=0$.
Lemma~\ref{lem:flow} applies; let $\Phi_s$ be the flow, $\Lambda=\norm{Du}_\infty$,
and $s_0$ as there.  For $0<|s|\le s_0$ define
\[
 u_s:=u\circ\Phi_{-s},
 \qquad
 q_s:=T_{\Phi_{-s}}q=D\Phi_{-s}^{\mathsf T}\,(q\circ\Phi_{-s}),
 \qquad
 E_s:=D\Phi_s^{-\mathsf T}-I .
\]
By Lemma~\ref{lem:flow}(b),(c), $\Phi_{-s}$ is a $C^1$ diffeomorphism with
$|D\Phi_{-s}|\le e^{\Lambda|s|}$ and $\det D\Phi_{-s}\equiv1$, so
Lemma~\ref{lem:qe-pullback} gives $u_s\in L^3$ and $q_s\in\mathcal G_3$.

\emph{Step 2: the envelope inequality.}  Since $q_s\in\mathcal G_3$, the
field $u_s+q_s$ is admissible in the definition of $\mathcal Q(u_s)$:
$\mathcal Q(u_s)\le F(u_s+q_s)$.  By Lemma~\ref{lem:qe-pullback}(a) applied
to $\Phi=\Phi_s$ (unit Jacobian),
$F(u_s+q_s)=\frac13\int|u_s+q_s|^3(\Phi_s(y))\,dy$.  At $x=\Phi_s(y)$ we
have $\Phi_{-s}(x)=y$ and, by Lemma~\ref{lem:flow}(c),
$D\Phi_{-s}(x)=D\Phi_s(y)^{-1}$, so
$u_s(x)+q_s(x)=u(y)+D\Phi_s(y)^{-\mathsf T}q(y)=w(y)+E_s(y)q(y)$, using
$w=u+q$.  Therefore
\begin{equation}\label{eq:qe-envelope}
 \mathcal Q(u_s)\le\mathcal R(s):=F(w+E_sq)
 =\frac13\int_{\R^3}\bigl|w+(D\Phi_s^{-\mathsf T}-I)q\bigr|^3dy,
 \qquad\mathcal R(0)=F(w)=\mathcal Q(u).
\end{equation}

\emph{Step 3: expansion of the right side.}  Put $h_s=E_sq\in L^3$; by
\eqref{eq:qe-flow-inverse},
$\norm{h_s}_3\le\norm{E_s}_\infty\norm q_3\le2\Lambda e^{\Lambda|s|}|s|\norm q_3=O(|s|)$.
By Lemma~\ref{lem:cubic-frechet}, inequality \eqref{eq:cp-F-taylor}, with
$v=w$ and $j(w)=|w|w=A$,
$|\mathcal R(s)-\mathcal Q(u)-\langle A,h_s\rangle|\le(\norm w_3+\norm{h_s}_3)\norm{h_s}_3^2=O(s^2)$.
Moreover
$\langle A,h_s\rangle=-s\langle A,Du^{\mathsf T}q\rangle+\langle A,(E_s+s\,Du^{\mathsf T})q\rangle$
with, by H\"older's inequality and \eqref{eq:qe-flow-inverse},
$|\langle A,(E_s+s\,Du^{\mathsf T})q\rangle|
\le\norm A_{3/2}\norm q_3\norm{E_s+s\,Du^{\mathsf T}}_\infty=o(|s|)$.
Hence
\begin{equation}\label{eq:qe-right-expansion}
 \mathcal R(s)=\mathcal Q(u)-s\,\langle A,Du^{\mathsf T}q\rangle+o(|s|),
 \qquad
 \langle A,Du^{\mathsf T}q\rangle=\int A_i(\partial_iu_j)q_j\,dx
 =\int q\cdot\bigl((A\cdot\nabla)u\bigr)dx ,
\end{equation}
where the index contraction is \eqref{eq:qe-jacobian}:
$(Du^{\mathsf T}q)_i=(\partial_iu_j)q_j$ and $((A\cdot\nabla)u)_j=A_i\partial_iu_j$.

\emph{Step 4: expansion of the left side.}  Put $g=(u\cdot\nabla)u=Du\,u$,
which is bounded, uniformly continuous, and in $L^3$.  For each $x$, the
curve $\sigma\mapsto\Phi_{-\sigma}(x)$ is $C^1$ with derivative
$-b(\Phi_{-\sigma}(x))$, so by the chain rule
$\frac d{d\sigma}u(\Phi_{-\sigma}(x))=-Du(\Phi_{-\sigma}(x))\,u(\Phi_{-\sigma}(x))=-g(\Phi_{-\sigma}(x))$,
and
\[
 u_s(x)-u(x)=-\int_0^sg(\Phi_{-\sigma}(x))\,d\sigma,
 \qquad
 \frac{u_s-u}s+g=-\frac1s\int_0^s\bigl(g\circ\Phi_{-\sigma}-g\bigr)d\sigma .
\]
The function $(\sigma,x)\mapsto g(\Phi_{-\sigma}(x))-g(x)$ is continuous
and bounded (Lemma~\ref{lem:flow}(a)), so Lemma~\ref{lem:qe-average}
gives
\begin{equation}\label{eq:qe-left-bounds}
 \norm{u_s-u}_3\le|s|\norm g_3,
 \qquad
 \Bigl\|\frac{u_s-u}s+g\Bigr\|_3\le\sup_{|\sigma|\le|s|}\norm{g\circ\Phi_{-\sigma}-g}_3 ,
\end{equation}
using $\norm{g\circ\Phi_{-\sigma}}_3=\norm g_3$ (Lemma~\ref{lem:qe-pullback}(a)).
We claim that $\norm{g\circ\Phi_{-\sigma}-g}_3\to0$ as $\sigma\to0$; this
holds for every $g\in L^3$.  Given $\varepsilon>0$ choose
$g_\varepsilon\in C_c(\R^3;\R^3)$ with $\norm{g-g_\varepsilon}_3<\varepsilon$
\cite[Thm.~3.14]{Rudin1987}.  By the isometry,
$\norm{g\circ\Phi_{-\sigma}-g}_3\le2\varepsilon+\norm{g_\varepsilon\circ\Phi_{-\sigma}-g_\varepsilon}_3$.
Since $|\Phi_{-\sigma}(x)-x|\le|\sigma|\norm u_\infty$, the function
$g_\varepsilon\circ\Phi_{-\sigma}-g_\varepsilon$ is bounded by
$\omega_{g_\varepsilon}(|\sigma|\norm u_\infty)$ and vanishes outside the
compact set $K=\operatorname{supp}g_\varepsilon+\overline{B_{s_0\norm u_\infty}}$
for $|\sigma|\le s_0$, so
$\norm{g_\varepsilon\circ\Phi_{-\sigma}-g_\varepsilon}_3
\le\omega_{g_\varepsilon}(|\sigma|\norm u_\infty)|K|^{1/3}\to0$.  Hence
$\limsup_{\sigma\to0}\norm{g\circ\Phi_{-\sigma}-g}_3\le2\varepsilon$ for
every $\varepsilon$, proving the claim, and \eqref{eq:qe-left-bounds}
gives $(u_s-u)/s\to-g$ in $L^3$.  Now apply
Proposition~\ref{prop:quotient-derivative} at $u$ with increment
$\delta_s=u_s-u$: $\mathcal Q(u_s)-\mathcal Q(u)=\langle A,\delta_s\rangle+r(\delta_s)$
with, by \eqref{eq:cp-derivative-remainder} and \eqref{eq:qe-left-bounds},
\[
 |r(\delta_s)|\le6(\norm w_3+\norm{\delta_s}_3)^{3/2}\norm{\delta_s}_3^{3/2}
 \le6\bigl(\norm w_3+|s|\norm g_3\bigr)^{3/2}\bigl(|s|\norm g_3\bigr)^{3/2}=o(|s|),
\]
and $\langle A,\delta_s\rangle=-s\langle A,g\rangle+\langle A,\delta_s+sg\rangle$
with $|\langle A,\delta_s+sg\rangle|\le\norm A_{3/2}|s|\sup_{|\sigma|\le|s|}\norm{g\circ\Phi_{-\sigma}-g}_3=o(|s|)$.
Thus
\begin{equation}\label{eq:qe-left-expansion}
 \mathcal Q(u_s)=\mathcal Q(u)-s\,\langle A,g\rangle+o(|s|).
\end{equation}

\emph{Step 5: comparison.}  Insert \eqref{eq:qe-right-expansion} and
\eqref{eq:qe-left-expansion} into \eqref{eq:qe-envelope}:
\[
 -s\,\langle A,g\rangle+o(|s|)\le-s\,\langle A,Du^{\mathsf T}q\rangle+o(|s|)
 \qquad(0<|s|\le s_0).
\]
Dividing by $s>0$ and letting $s\downarrow0$ gives
$\langle A,g\rangle\ge\langle A,Du^{\mathsf T}q\rangle$; dividing by $s<0$
(which reverses the inequality) and letting $s\uparrow0$ gives
$\langle A,g\rangle\le\langle A,Du^{\mathsf T}q\rangle$.  Hence
$\langle A,(u\cdot\nabla)u\rangle=\langle A,Du^{\mathsf T}q\rangle$, which is
\eqref{eq:qe-transport}--\eqref{eq:qe-contraction} by
\eqref{eq:qe-right-expansion}.  The absolute convergence statements are
H\"older's inequality.
\end{proof}

\begin{remark}[No derivative of the minimizer]\label{rem:qe-transport-scope}
No derivative of $q$ or $w$ appears in the proof: the competitor $q_s$ is
the pullback of the fixed $L^3$ field $q$, and the two-sided comparison at
$s=0$ replaces the differentiation of the minimizer.  No smoothness of the
minimizer is used or asserted.
\end{remark}

\begin{proposition}[Evolution of the quotient]\label{prop:quotient-evolution}
With the notation and package (R) of Section~\ref{subsec:qe-trajectories},
$t\mapsto\mathcal Q(u(t))$ belongs to $C^1([0,T])$; the functions
$t\mapsto D_{\mathcal Q}(u(t))$ and
$t\mapsto\int q(t)\cdot\bigl((A(t)\cdot\nabla)u(t)\bigr)dx$ are continuous
on $[0,T]$; and for every $t\in[0,T]$
\begin{equation}\label{eq:quotient-evolution}
 \frac d{dt}\mathcal Q(u(t))+\nu D_{\mathcal Q}(u(t))
 =-\int_{\R^3}q(t)\cdot\bigl((A(t)\cdot\nabla)u(t)\bigr)dx,
 \qquad D_{\mathcal Q}(u(t))\ge0 .
\end{equation}
\end{proposition}

\begin{proof}
By Lemma~\ref{lem:quotient-chainrule}, $\mathcal Q\circ u\in C^1([0,T])$
and
$\frac d{dt}\mathcal Q(u(t))=\nu\langle A,\Delta u\rangle-\langle A,(u\cdot\nabla)u\rangle$;
the pressure term has already been cancelled there by
Lemma~\ref{lem:quotient-pressure}.  By Definition~\ref{def:qe-dissipation},
$\nu\langle A,\Delta u\rangle=-\nu D_{\mathcal Q}(u(t))$, with
$D_{\mathcal Q}(u(t))\ge0$ and continuous by
Lemma~\ref{lem:quotient-heatsign}.  By Lemma~\ref{lem:quotient-transport},
$\langle A,(u\cdot\nabla)u\rangle=\int q\cdot((A\cdot\nabla)u)$.  Combining
gives \eqref{eq:quotient-evolution}.  For the continuity of the right
side: $q(t)=w(t)-u(t)$ is continuous into $L^3$ by
Lemma~\ref{lem:quotient-stability}, estimate \eqref{eq:cp-continuity},
and $u\in C([0,T];L^3)$; $A\in C([0,T];L^{3/2})$ by the same estimate;
$Du\in C([0,T];L^\infty)$ by (R3); and for $q,q'\in L^3$,
$A,A'\in L^{3/2}$, $v,v'$ with bounded gradients,
\[
\begin{aligned}
 \Bigl|\int q\cdot((A\cdot\nabla)v)-\int q'\cdot((A'\cdot\nabla)v')\Bigr|
 &\le\norm{q-q'}_3\norm A_{3/2}\norm{Dv}_\infty
 +\norm{q'}_3\norm{A-A'}_{3/2}\norm{Dv}_\infty\\
 &\quad+\norm{q'}_3\norm{A'}_{3/2}\norm{Dv-Dv'}_\infty ,
\end{aligned}
\]
by H\"older's inequality with exponents $3$, $3/2$, $\infty$ and the
pointwise bound $|q\cdot((A\cdot\nabla)v)|=|q\cdot(Dv\,A)|\le|q|\,|Dv|\,|A|$
from \eqref{eq:qe-jacobian}.
\end{proof}

\begin{remark}[Content of the evolution identity]\label{rem:qe-evolution-scope}
Identity \eqref{eq:quotient-evolution} contains no pressure term and no
derivative of the minimizer.  It is exact on every compact classical
interval.  It supplies neither a sign nor a bound for its right side.
\end{remark}

\subsection{Low strain, the missing high-strain estimate, and its consequence}
\label{subsec:qe-highstrain}

Let $S_L$, $L\in\mathbb Z$, be the low-pass projection of
Definition~\ref{def:lp}, i.e.\ Tao's $P_{\le2^L}$ with symbol
$\varphi(\xi/2^L)$, so that $S_Lf=\kappa_L*f$ with
$\kappa_L=2^{3L}\kappa(2^L\,\cdot)$ and $\hat\kappa=\varphi$; the symbol
$\psi=\varphi-\varphi(2\,\cdot)$ and the homogeneous blocks $\Delta_j$ of
Definition~\ref{def:lp} are not used here, and
Lemma~\ref{lem:lp-coincide} reconciles $S_L$ with $\sum_{j\le L}\Delta_j$
on $L^2$.  Since $\kappa_L\in\mathcal S(\R^3)$, $S_L$ acts componentwise
on vector fields and $\partial_kS_Lf=(\partial_k\kappa_L)*f$
(Lemma~\ref{lem:lowpass-kernel}).  We use the Bernstein estimate of
Lemma~\ref{lem:bernstein}: for $f\in L^2(\R^3;\R^3)$, $S_Lf$ has a
$C^\infty$ representative and
\begin{equation}\label{eq:qe-bernstein}
 \sup_{x\in\R^3}\bigl|\nabla S_Lf(x)\bigr|_F\le C_B\,2^{5L/2}\norm f_2 ,
 \qquad C_B=2\pi\norm{\,|\xi|\varphi\,}_2\le16\pi\sqrt{2\pi/5},
\end{equation}
and $t\mapsto\nabla S_Lu(t)\in C([0,T];L^\infty)$ whenever
$u\in C([0,T];L^2)$.

\begin{lemma}[Low-strain Gronwall coefficient]\label{lem:quotient-lowstrain}
Let $L\in\mathbb Z$ and $[0,T]\subset[0,T_*)$.  For $t\in[0,T]$ put
$v(t)=S_Lu(t)$ and
\[
 K_{\rm low}(t)=-\int_{\R^3}q(t)\cdot\bigl((A(t)\cdot\nabla)v(t)\bigr)dx,
 \qquad
 K_L(t)=-\int_{\R^3}q(t)\cdot\bigl((A(t)\cdot\nabla)(u(t)-v(t))\bigr)dx .
\]
Then $K_{\rm low}$ and $K_L$ are continuous on $[0,T]$,
\eqref{eq:quotient-evolution} reads
\begin{equation}\label{eq:qe-split}
 \frac d{dt}\mathcal Q(u(t))+\nu D_{\mathcal Q}(u(t))=K_L(t)+K_{\rm low}(t),
\end{equation}
and
\begin{equation}\label{eq:qe-lowstrain}
 |K_{\rm low}(t)|\le M_L\,\mathcal Q(u(t)),
 \qquad
 M_L:=3\,(1+C_{\mathbb P})\,C_B\,2^{5L/2}\norm{u_0}_2 .
\end{equation}
\end{lemma}

\begin{proof}
Fix $t$ and write $u=u(t)$, $v=S_Lu$, $q=q(t)$, $A=A(t)$, $w=w(t)$.  By
(R1), $u\in L^2$, so by \eqref{eq:qe-bernstein} $Dv$ is continuous and
bounded, $D(u-v)$ is bounded as well, and both integrals converge
absolutely; the splitting $Du=Dv+D(u-v)$ is exact, which gives
\eqref{eq:qe-split} from \eqref{eq:quotient-evolution}.  Pointwise, by
\eqref{eq:qe-jacobian} and \eqref{eq:qe-frobenius},
$|q\cdot((A\cdot\nabla)v)|=|q\cdot(Dv\,A)|\le|q|\,|Dv|_F\,|A|$, and by
\eqref{eq:qe-bernstein} and Proposition~\ref{prop:energy},
\[
 \sup_x|Dv(x)|_F\le C_B2^{5L/2}\norm{u(t)}_2\le C_B2^{5L/2}\norm{u_0}_2 .
\]
H\"older's inequality with exponents $\infty$, $3$, $3/2$, then
Lemma~\ref{lem:quotient-coercive} ($\norm q_3\le(1+C_{\mathbb P})\norm w_3$,
applicable because $u(t)\in L^3$ is solenoidal, as shown after
Lemma~\ref{lem:qe-embedding}) and
Lemma~\ref{lem:quotient-minimizer}(b) ($\norm A_{3/2}=\norm w_3^2$,
$\norm w_3^3=3\mathcal Q(u)$), give
\[
 |K_{\rm low}(t)|
 \le\sup_x|Dv|_F\;\norm q_3\norm A_{3/2}
 \le C_B2^{5L/2}\norm{u_0}_2\,(1+C_{\mathbb P})\norm w_3\cdot\norm w_3^2
 =M_L\,\mathcal Q(u(t)) .
\]
Continuity of $K_{\rm low}$ follows from the three-term estimate in the
proof of Proposition~\ref{prop:quotient-evolution}, with $Dv$ in place of
$Du$, since $t\mapsto Dv(t)=\nabla S_Lu(t)$ belongs to $C([0,T];L^\infty)$
by Lemma~\ref{lem:bernstein} and $u\in C([0,T];L^2)$ (R1).  Then $K_L$ is
continuous as the difference of the continuous right side of
\eqref{eq:quotient-evolution} and $K_{\rm low}$.
\end{proof}

The remaining term $K_L$ is the only part of the transport work not
controlled by an input-dependent coefficient.  A sufficient
\emph{unproved} producer is the following.

\begin{hypothesis}[Signed high-strain absorption]\label{hyp:highstrain}
For an integer $L$ and $t\in[0,T_*)$ let, as in
Lemma~\ref{lem:quotient-lowstrain},
\[
 K_L(t)=-\int_{\R^3}q(t)\cdot\bigl((A(t)\cdot\nabla)(u(t)-S_Lu(t))\bigr)dx ,
\]
where $q(t)$, $A(t)$ are the minimizer data of
Lemma~\ref{lem:quotient-minimizer}(b) at $u(t)$ and $S_L$ is the low-pass
projection of Definition~\ref{def:lp}; let $D_{\mathcal Q}$ be as in
Definition~\ref{def:qe-dissipation}.  There exists a fixed
$\theta\in[0,1]$ such that, for every $\nu>0$, divergence-free Schwartz
datum $u_0$, and $0<H<\infty$, there exist an integer $L=L(\nu,u_0,H)$ and
a finite nonnegative $A_{\rm input}=A_{\rm input}(\nu,u_0,H,L)$ such that
\begin{equation}\label{eq:quotient-gap}
 \int_0^\tau K_L(t)\,dt
 \le\theta\nu\int_0^\tau D_{\mathcal Q}(u(t))\,dt+A_{\rm input}
\end{equation}
for every $0<\tau<\min\{H,T_*\}$.  The same $L$ and $A_{\rm input}$ must
work for the entire interval, and $A_{\rm input}$ depends only on the
initial datum, viscosity, horizon, and input-selected cutoff.
\end{hypothesis}

As with Hypothesis~\ref{hyp:highpressure}, the existential assertion is
nontrivial: the left side could be unbounded as $\tau\uparrow T_*$.  A proof
must produce $A_{\rm input}$ without assuming the continuation bound it is
meant to imply; a remainder defined through the unknown supremum is
circular.  Because $\theta=1$ is permitted, the value of $\theta$ plays no
role below; $\theta<1$ would additionally retain
$(1-\theta)\nu\int_0^\tau D_{\mathcal Q}$.

\begin{proposition}[Conditional critical bound from high-strain absorption]
\label{prop:quotient-conditional}
Hypothesis~\ref{hyp:highstrain} implies Hypothesis~\ref{hyp:critical}, with
\begin{equation}\label{eq:qe-M}
 M(\nu,u_0,H)
 =C_{\mathbb P}\bigl(\norm{u_0}_3^3+3A_{\rm input}\bigr)^{1/3}
 \exp\Bigl(\tfrac13M_LH\Bigr),
\end{equation}
where $L$ and $A_{\rm input}$ are those provided by
Hypothesis~\ref{hyp:highstrain} and $M_L$ is the constant of
\eqref{eq:qe-lowstrain}.  Consequently, by Theorem~\ref{thm:conditional},
Hypothesis~\ref{hyp:highstrain} implies Theorem~\ref{def:target}.
\end{proposition}

\begin{proof}
Fix $\nu$, $u_0$, $H$, and let $\theta$, $L$, $A_{\rm input}$ be given by
Hypothesis~\ref{hyp:highstrain}.  Let $0<\tau_1<\min\{H,T_*\}$; then
$[0,\tau_1]$ is a compact subinterval of $[0,T_*)$, and
Proposition~\ref{prop:quotient-evolution} and
Lemma~\ref{lem:quotient-lowstrain} apply on it.  Put $y(t)=\mathcal Q(u(t))$,
which is nonnegative and belongs to $C^1([0,\tau_1])$; in particular $y$ is
absolutely continuous and the fundamental theorem of calculus applies.
Integrating \eqref{eq:qe-split} over $[0,\tau]$ for $0<\tau\le\tau_1$, all
integrands being continuous,
\[
 y(\tau)+\nu\int_0^\tau D_{\mathcal Q}(u(t))\,dt
 =y(0)+\int_0^\tau K_L(t)\,dt+\int_0^\tau K_{\rm low}(t)\,dt .
\]
By \eqref{eq:quotient-gap} and \eqref{eq:qe-lowstrain},
\[
 y(\tau)+(1-\theta)\nu\int_0^\tau D_{\mathcal Q}(u(t))\,dt
 \le y(0)+A_{\rm input}+M_L\int_0^\tau y(t)\,dt .
\]
Since $\theta\le1$ and $D_{\mathcal Q}\ge0$
(Lemma~\ref{lem:quotient-heatsign}), the second term on the left is
nonnegative and may be dropped; the resulting inequality also holds at
$\tau=0$.  Lemma~\ref{lem:qe-gronwall} with $a=y(0)+A_{\rm input}$ and
$M=M_L$ gives
$y(\tau)\le\bigl(y(0)+A_{\rm input}\bigr)e^{M_L\tau}\le\bigl(y(0)+A_{\rm input}\bigr)e^{M_LH}$
for all $\tau\in[0,\tau_1]$.  Since $\tau_1<\min\{H,T_*\}$ was arbitrary,
the bound holds on $[0,\min\{H,T_*\})$.  By
Lemma~\ref{lem:quotient-coercive}, estimate \eqref{eq:cp-coercive},
$y(0)\le\frac13\norm{u_0}_3^3$ and
$\norm{u(\tau)}_3^3\le3C_{\mathbb P}^3y(\tau)$ ($u(\tau)\in L^3$ is
solenoidal), so
\[
 \sup_{0\le\tau<\min\{H,T_*\}}\norm{u(\tau)}_3^3
 \le C_{\mathbb P}^3\bigl(\norm{u_0}_3^3+3A_{\rm input}\bigr)e^{M_LH},
\]
which is \eqref{eq:missing} with $M$ as in \eqref{eq:qe-M}.  The last
sentence is Theorem~\ref{thm:conditional}.
\end{proof}

\begin{remark}[Scope of the high-strain hypothesis]\label{rem:highstrain-scope}
Integration of \eqref{eq:quotient-evolution} and Gronwall would then bound
$\mathcal Q$, hence $L^3$, through the putative endpoint; this is exactly
Proposition~\ref{prop:quotient-conditional}.  At the quantifiers of
Hypothesis~\ref{hyp:highstrain}, the hypothesis is equivalent to global
continuation of the selected classical branch, as for
Hypothesis~\ref{hyp:highpressure}.  The forward direction is
Proposition~\ref{prop:quotient-conditional} together with
Theorem~\ref{thm:continuation}.  Conversely, if $T_*=\infty$ for the given
datum, take $L=0$ and $\theta=0$: $K_0$ is continuous on the compact
classical interval $[0,H]$ by Lemma~\ref{lem:quotient-lowstrain}, so
$A_{\rm input}=\int_0^H|K_0(t)|dt$ is finite and \eqref{eq:quotient-gap}
holds.  This converse assumes global continuation and supplies no method
for proving it.  Neither \eqref{eq:quotient-gap} nor a quantitative
dissipation mechanism for it has been proved.  Bounding $K_L$ by
$\norm{\nabla(u-S_Lu)}_\infty\mathcal Q(u)$ merely renames the missing
high-frequency control.  This is an alternative to the pressure route; no
novelty or Millennium solution is asserted.
\end{remark}
```

---

## 3. External facts used

Legend as in `cp01-literature-statements.md` §0: [DI] directly inspected
(primary text opened and the statement read, in this session or in the
cited CP01/CP02 record); [MO] metadata or secondary record only. Mathlib
references are to the local checkout
`../stafford38/.lake/packages/mathlib` at `0df444a` (grep and
statement read; not built; every line reference re-opened by the audit).
Textbook page images were read in this session from the PDF mirrors named
in the audit (`math.stonybrook.edu/~bishop/classes/math638.F20/` for
Grafakos; `59clc.wordpress.com` for Rudin, page offset 15).

| # | Fact (exact form used) | Where used | Source | Status |
| --- | --- | --- | --- | --- |
| E1 | Hölder's inequality on `\R^3` and on an interval: `\int|fg|\le\|f\|_r\|g\|_{r'}`, `1/r+1/r'=1` (exponents `3,3/2`; `\infty,3,3/2`) | throughout | Mathlib `MeasureTheory.integral_mul_le_Lp_mul_Lq_of_nonneg`, `Mathlib/MeasureTheory/Integral/Bochner/Basic.lean:1191`; cp01-literature-statements §6 S10 | [DI] |
| E2 | Tonelli's theorem for nonnegative Borel functions on `J\times\R^3` | `lem:qe-average` | Mathlib `MeasureTheory.lintegral_prod`, `Mathlib/MeasureTheory/Measure/Prod.lean:1006` | [DI] |
| E3 | Dominated convergence theorem | `lem:qe-embedding`, `lem:qe-average`, `lem:qe-heat-continuity`, `lem:quotient-pressure` | Mathlib `MeasureTheory.tendsto_integral_of_dominated_convergence`, `Mathlib/MeasureTheory/Integral/DominatedConvergence.lean:57` | [DI] |
| E4 | Fundamental theorem of calculus for `C^1` functions on an interval | `lem:qe-gronwall`, `lem:heat-generator` Step 3, `lem:flow`, `prop:quotient-conditional` | Mathlib `intervalIntegral.integral_eq_sub_of_hasDerivAt`, `Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean:1148` | [DI] |
| E5 | Differentiation under the integral sign with an integrable dominant for the derivative | `lem:qe-mollify`, `lem:heat-generator` Step 3 | Mathlib `hasDerivAt_integral_of_dominated_loc_of_deriv_le`, `Mathlib/Analysis/Calculus/ParametricIntegral.lean:288` | [DI] |
| E6 | Banach fixed point theorem in a complete metric space; completeness of `C([-S,S];\R^n)` with the sup norm (equivalent to `\|\cdot\|_*`) | `lem:flow` (a),(b) | Mathlib `ContractingWith.exists_fixedPoint`, `Mathlib/Topology/MetricSpace/Contracting.lean:95`; `BoundedContinuousFunction.instCompleteSpace`, `Mathlib/Topology/ContinuousMap/Bounded/Basic.lean:296` | [DI] |
| E7 | Change of variables: for `X\subset V\subset\R^k`, `V` open, `T:V\to\R^k` continuous, `X` Lebesgue measurable, `T` one-to-one on `X` and differentiable at every point of `X`, `m(T(V\setminus X))=0`: `\int_{T(X)}f\,dm=\int_X(f\circ T)|J_T|\,dm` for every measurable `f:\R^k\to[0,\infty]` (used with `X=V=\R^3`, `T=\Phi`) | `lem:qe-pullback` (a) | Rudin, *Real and Complex Analysis*, 3rd ed., McGraw-Hill 1987, Thm. 7.26, pp. 153–154 (statement read as page image this session; hypotheses (i)–(iii) exactly as listed); Mathlib `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul`, `Mathlib/MeasureTheory/Function/Jacobian.lean:1213` | [DI] (both) |
| E8 | Density of `C_c(X)` in `L^p(\mu)`, `1\le p<\infty`, for `X` locally compact Hausdorff and `\mu` as in Rudin Thm. 2.14 (Lebesgue measure on `\R^k` is the example named there) | `lem:qe-heat-continuity` (b), `lem:quotient-transport` Step 4 | Rudin RCA Thm. 3.14, p. 69 ("For `1\le p<\infty`, `C_c(X)` is dense in `L^p(\mu)`"; read as page image this session); Mathlib `MeasureTheory.MemLp.exists_hasCompactSupport_eLpNorm_sub_le`, `Mathlib/MeasureTheory/Function/ContinuousMapDense.lean:135` | [DI] (both) |
| E9 | Minkowski's inequality for convolution: for `1\le p\le\infty`, `f\in L^p(G)`, `g\in L^1(G)`: `g*f` exists a.e. and `\|g*f\|_{L^p}\le\|g\|_{L^1}\|f\|_{L^p}` (used with `G=\R^3`, `p=3`, `g=k_r` and `g=k_r\mathbf 1_{\{|y|>\delta\}}`) | `lem:qe-heat-continuity`, `lem:heat-generator` | Grafakos, *Classical Fourier Analysis*, 3rd ed., GTM 249, Thm. 1.2.10, p. 21 (read as page image this session; also confirmed by the audit); Tao 2013, APDE 6, p. 39, eq. (18) with `p=q` (cp01-literature-statements §1.4) | [DI] |
| E10 | `L^2` Fourier theory: for `f\in L^1\cap L^2` the `L^2` transform `\mathcal F(f)` coincides a.e. with the integral `\hat f`; `\mathcal F` is an isometry of `L^2`; the isometry `\mathcal F'` extending `f\mapsto f^\vee` from `L^1\cap L^2` equals `\mathcal F^{-1}`; `f=\mathcal F^{-1}\mathcal F(f)=\mathcal F\mathcal F^{-1}(f)` a.e. on `L^2` | `lem:qe-embedding` (via `def:lp`) | Grafakos op. cit. **§2.2.4, pp. 113–114** (unnumbered development; Exercise 2.2.6 for pointwise `L^1` inversion). Read as page images this session: p. 114 "for `f` in `L^1(\R^n)\cap L^2(\R^n)` the expressions `\hat f` and `\mathcal F(f)` coincide pointwise a.e."; "`\mathcal F'` coincides with the inverse operator `\mathcal F^{-1}` of `\mathcal F:L^2\to L^2`, and Fourier inversion `f=\mathcal F^{-1}\circ\mathcal F(f)=\mathcal F\circ\mathcal F^{-1}(f)` a.e. holds on `L^2`". **Theorem 2.2.14 (p. 112) is stated for `f,g,h\in\mathcal S(\R^n)` and is not cited in this lane.** Mathlib `MeasureTheory.Lp.fourierTransformₗᵢ` / `fourierInv`, `Mathlib/Analysis/Fourier/LpSpace.lean:50,132` | [DI] (both) |
| E11 | Leibniz formula for `\det`; adjugate identity `M\operatorname{adj}(M)=\operatorname{adj}(M)M=(\det M)I`; `\operatorname{tr}(XY)=\operatorname{tr}(YX)` | `lem:qe-jacobi` | Mathlib `Matrix.det_apply`, `Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean:63`; `Matrix.mul_adjugate`, `Mathlib/LinearAlgebra/Matrix/Adjugate.lean:264` (the adjugate identity is also proved in the text via cofactor expansion) | [DI] |
| E12 | Littlewood–Paley projection `P_{\le N}` with smooth bump `\varphi` (`=1` on `|\xi|\le1`, supported in `|\xi|\le2`), `N=2^L`; `S_L=P_{\le2^L}` (D1) | §"Low strain" | Tao 2013, p. 40, eq. (26) (verbatim in cp01-literature-statements §1.4); project text `def:lp`, `eq:lp-symbol` | [DI] via the CP01 record; project definition |
| E13 | Bernstein estimate `\sup_x|\nabla S_Lf(x)|_F\le C_B2^{5L/2}\|f\|_2` for scalar or vector `f\in L^2`, `C_B=2\pi\||\xi|\varphi\|_2\le16\pi\sqrt{2\pi/5}`, `C^\infty` representative, `t\mapsto\nabla S_Lu(t)\in C([0,T];L^\infty)` for `u\in C([0,T];L^2)` | `lem:quotient-lowstrain` | project-owned: `cp02-lowpressure.md` `lem:bernstein` (statement read at source; label and form confirmed by the audit) | project lemma |
| E14 | Package R: `u,p\in C^j([0,T];H^k)` for all `j,k`, classical smooth solution, normalised pressure, memberships (R3); classical = weak derivatives for the smooth `u(t)`, `p(t)` | (R1)-(R3) | project-owned: local-theory lane, `prop:localtheory` (D2) | project proposition |
| E15 | Pressure normalisation `R_iR_j(u_iu_j)=-\Delta^{-1}\partial_i\partial_j(u_iu_j)` (same symbol `-\xi_i\xi_j/|\xi|^2`) | `rem:qe-pressure-normalisation` | project text `def:lp` (proved there); cp01-literature-statements §7.3 (Tao (9) [DI], Grafakos Prop. 5.1.14 [DI]) | project definition; [DI] via the CP01 record |
| E16 | Functional-lane results: `def:quotient`, `lem:cubic-frechet` (`eq:cp-F-taylor`), `lem:quotient-minimizer` (b),(c), `lem:quotient-stability` (`eq:cp-continuity`), `lem:leray`(b) (`C_{\mathbb P}`), `lem:quotient-coercive` (`eq:cp-coercive`), `lem:quotient-heat`, `prop:quotient-derivative` (`eq:cp-derivative-remainder`) | throughout | project-owned (`cp02-quotient-functional.md`; every label and sub-item letter checked at source in this session) | project lemmas |
| E17 | `prop:energy`: `\|u(t)\|_2\le\|u_0\|_2` | `lem:quotient-lowstrain` | manuscript, energy lane | project proposition |
| E18 | Low-pass kernel: `\kappa=\varphi^\vee\in\mathcal S`, `\hat\kappa=\varphi`, `S_Jf=\kappa_J*f` a.e. for `f\in L^2`, `\partial^\alpha(\kappa_J*f)=(\partial^\alpha\kappa_J)*f`; `S_J=\sum_{j\le J}\Delta_j` on `L^2` | §"Low strain" (orientation only) | project-owned: `cp02-lowpressure.md` `lem:lowpass-kernel`, `lem:lp-coincide` | project lemmas |
| E19 | Elementary calculus: `\int_0^\infty r^2(1+r^2)^{-2}dr=\pi/4`; derivatives of the Gaussian kernel; Neumann series for `(I+N)^{-1}`, `|N|<1`; mean value inequality along a segment; `\int k_r=1` and the scaling `k_r(\sqrt r z)r^{3/2}=k_1(z)`; `|Ma|\le|M|_F|a|` by Cauchy–Schwarz | `lem:qe-embedding`, `lem:heat-generator`, `lem:flow`, notation | computed inline | proved in text |

Dropped in this version: Teschl 2012 (was corroboration only, never used).

Bibliography entries needed in `references.bib` (the integrator adds them;
`Grafakos2014` is already required by the functional and low-pressure
lanes):

```bibtex
@book{Rudin1987,
  author    = {Walter Rudin},
  title     = {Real and Complex Analysis},
  edition   = {3},
  publisher = {McGraw-Hill},
  year      = {1987}
}
@book{Grafakos2014,
  author    = {Loukas Grafakos},
  title     = {Classical {Fourier} Analysis},
  edition   = {3},
  series    = {Graduate Texts in Mathematics},
  volume    = {249},
  publisher = {Springer},
  year      = {2014},
  doi       = {10.1007/978-1-4939-1194-3}
}
```

The Grafakos citations surviving in this lane are exactly
`\cite[Thm.~1.2.10]{Grafakos2014}` and
`\cite[\S2.2.4, pp.~113--114]{Grafakos2014}`; the Rudin citations are
`\cite[Thm.~3.14]{Rudin1987}` (twice) and `\cite[Thm.~7.26]{Rudin1987}`.

---

## 4. Obligations not discharged (exact statements)

Nothing in Q-8 .. Q-18 is left unproved in the text. The remaining items
are integration seams (1-2) and the section's standing non-claims (3-4).

1. **Sobolev norm convention across lanes.** The block fixes
   `\|f\|_{H^m}=\|(1+|\xi|^2)^{m/2}\hat f\|_2` (display
   `eq:qe-sobolev-norm`) and reads (R1) with it, including the
   identification of the classical derivatives of the smooth `u(t)`,
   `p(t)` with the elements `\partial^\alpha u(t)\in H^k` (an integration
   by parts against test functions for smooth functions; the local-theory
   lane owns it as part of `prop:localtheory`). If the local-theory lane
   fixes a different but equivalent norm, only the constant `\pi` in
   `eq:qe-embedding` (and hence `4\pi^3` in the paragraph after it)
   changes; no statement of this lane depends on the value of that
   constant.
2. **`def:lp` must be integrated before `sec:quotient`** (or at least
   before `lem:qe-embedding`), since REPAIR 1 cites it for the `L^2`
   Fourier facts; if it is dropped or renamed, the sentence in
   `lem:qe-embedding` must cite `\cite[\S2.2.4, pp.~113--114]{Grafakos2014}`
   alone (the source is already [DI] here).
3. **`eq:quotient-gap` (Hypothesis `hyp:highstrain`)** is not proved. No
   sign, bound, or dissipation mechanism for `K_L` is asserted. (Non-claim
   retained verbatim.)
4. **No quantitative comparison of `D_{\mathcal Q}` with `D_3`** is claimed,
   and no coercive lower bound for `D_{\mathcal Q}`. (Non-claim retained
   verbatim.)

The version-1 open items (Bernstein label placeholder; [MO] Fourier
inversion citation; form of (R3)) are closed: the label `lem:bernstein`
exists with the vector-valued Frobenius statement and the continuity clause;
E10 is now sourced to Grafakos §2.2.4 and [DI]; (R3) is D2 verbatim.

---

## 5. Frontier record

**MODE / RESULT.** INTEGRATE (paper proof), lane CP02-7, repair round 1
after the audit `cp02-review-quotient-evolution.md` (verdict REPAIR, no
invalid mathematical step). All five surgical repairs and all thirteen
minor editorial items of the audit are applied; Rudin Thms. 3.14 and 7.26
and Grafakos Thm. 1.2.10 and §2.2.4 were opened in this session, so every
textbook fact in the block is now [DI]. Complete proofs of Q-8 .. Q-18 at
the D5 standard: pressure gradient in `L^3\cap\mathcal G_3` with displayed
cutoff errors; `C^1` chain rule along the `C^1([0,T];L^3)` trajectory with
exact pressure cancellation; heat generator limit in `L^3` from the integral
representation and strong continuity (proved from density of `C_c` and the
`L^3` contraction); sign `D_{\mathcal Q}\ge0`; flow lemma proved from the
Banach fixed point theorem, Gronwall, and Jacobi's formula (Jacobi and
Liouville proved), with uniform expansions of `D\Phi_s` and
`D\Phi_s^{-\mathsf T}` under bounded uniformly continuous `Du` only;
pullback lemma; envelope inequality by change of variables; `L^3`
continuity along the flow and the transport limit; two-sided expansion and
the contraction identity; `eq:quotient-evolution`; low-strain bound
`|K_{\rm low}|\le M_L\mathcal Q(u)` with
`M_L=3(1+C_{\mathbb P})C_B2^{5L/2}\|u_0\|_2`; `hyp:highstrain` (self-contained)
with `eq:quotient-gap`; conditional Gronwall proposition with explicit
`M(\nu,u_0,H)=C_{\mathbb P}(\|u_0\|_3^3+3A_{\rm input})^{1/3}e^{M_LH/3}`.

**CLAIM AND SCOPE.** For the original unforced equation on `\R^3`, arbitrary
`\nu>0`, divergence-free Schwartz data, and the maximal classical branch of
`prop:localtheory` (package R), on every compact `[0,T]\subset[0,T_*)`:
`t\mapsto\mathcal Q(u(t))` is `C^1` and satisfies the pressure-free identity
`eq:quotient-evolution` with `D_{\mathcal Q}\ge0`; the low-strain part of
its right side is bounded by `M_L\mathcal Q(u)`; and
`hyp:highstrain\Rightarrow hyp:critical\Rightarrow` (by `thm:conditional`)
`def:target`. No decay of `u(t)` in `x` beyond `H^k` membership is used.

**EVIDENCE.** Every step is written in the block of §2; the mathematics is
unchanged from version 1, which the audit reconstructed bridge by bridge
(all constants recomputed) and tested against `prop:pressure` in the
degenerate case `q=0` without refutation. The cross-references into the
functional lane were re-read at source in this session
(`lem:quotient-minimizer`(a)-(d) at `cp02-quotient-functional.md:344`,
`lem:quotient-stability`/`eq:cp-continuity` at 803-816, `lem:leray`(b) at
501, `eq:cp-derivative-remainder` at 871), as were `def:lp`,
`eq:lp-symbol`, `lem:lp-coincide`, `lem:lowpass-kernel`, `lem:bernstein` in
`cp02-lowpressure.md`. External facts are listed in §3 with sources:
Mathlib statements read in the local checkout (E1-E8, E10-E11), Grafakos
pp. 21, 112-114 and Rudin pp. 69, 153-154 read as page images (E7-E10).
The LaTeX block compiles against a stub of the other lanes' labels.

**FIRST GAP.** Unchanged: Hypothesis `hyp:highstrain`
(`eq:quotient-gap`), a signed, input-only, finite-horizon bound for
`\int_0^\tau K_L` uniform up to `\min\{H,T_*\}`. Within this lane's
deliverable the only open seams are the two integration items of §4 (Sobolev
norm convention shared with `prop:localtheory`; placement of `def:lp`).

**SURVIVING CONDITIONAL SUFFIX.** `prop:quotient-conditional`: any proof
of `hyp:highstrain` yields `hyp:critical` with the explicit constant
`C_{\mathbb P}(\|u_0\|_3^3+3A_{\rm input})^{1/3}e^{M_LH/3}`, and then
`thm:conditional` yields the target. Independently of any hypothesis,
`eq:quotient-evolution` with `D_{\mathcal Q}\ge0` and the low-strain bound
hold unconditionally on compact classical intervals.

**NON-CLAIMS.** No proof of `eq:quotient-gap`; no sign or bound for `K_L`;
no smoothness of `w` or `q`; no quantitative comparison with the original
cubic dissipation (`D_3`) and no coercive lower bound for `D_{\mathcal Q}`;
no HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3 result; no
continuation bound; no regularity theorem; no novelty claim for the quotient
construction; no Millennium solution. The Mathlib statements were read but
not built; `prop:localtheory` (package R) is an assumed lane interface, not
proved here.

**NEXT DISTINCT ACTION.** Round-2 audit of this repaired file (checking
REPAIRS 1-5 and M1-M13 against the audit's §5 and §9, and the new `[DI]`
page references), then controller integration: splice the functional lane's
first half, this lane's second half, and the low-pressure lane's `def:lp` /
`lem:bernstein` into `sec:quotient` and `prop:lowpressure`, add the two
`\newtheorem` lines, drop the `\theta\le1` annotation from the manuscript's
`eq:quotient-gap` display, re-run the structural verifier on the D4 label
list, and audit the integrated section for cross-lane notation collisions
(`S_J`/`S_L`; `q` as minimizer versus `q` as the `\nu`-normalised pressure
in `eq:nu-normalization`).
