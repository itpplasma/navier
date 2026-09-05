# CP02-2: continuation section (obligations C-0, C-2, C-3)

MODE: PROOF WRITING, **repair round 2** (math-frontier discipline; complete
paper-proof standard of CP1). Date: 2026-09-05. Owner: lane CP02-2. File
written: this one only. Repository HEAD at writing time:
`f20e6bf579f74c3fef4e365fa5267929667f1228`.

This version replaces round 1 in full. It answers the independent audit
`research/evidence/cp02-review-continuation.md` (verdict REPAIR): the single
bad bridge (the Sobolev inequality imported for the class $D^1(\R^3)$ and
applied to $H^1(\R^3)$ through an inclusion that is itself the Sobolev
embedding) is repaired by restricting the imported fact to compactly
supported functions and proving the extension to $\bigcap_kH^k(\R^3)$ as a
lemma (`lem:sobolev-h1`, truncation plus Fatou). Every one of the audit's
twenty editorial items is resolved or, where it concerns another lane's
text, recorded with the exact action for the integrator (Section 5 below
lists each item against the change). No statement was weakened and no
hypothesis was added.

Inputs read in full: `/home/ert/proj/navier-paper/main.tex` (562 lines),
`research/evidence/cp01-manuscript-obligations.md`,
`research/evidence/cp01-literature-statements.md`,
`research/evidence/cp02-review-continuation.md`; read for interface purposes
only: the local-theory lane's `cp02-local-theory.md` (statement of
`prop:localtheory` (i)–(vi), `cor:Lq`, `lem:nu-scaling`, `lem:sup-esssup`,
`lem:global-smooth`, `rem:continuation-shape`, label inventory) and the
energy lane's `cp02-energy-enstrophy.md` (`def:sobolev-constant`,
`lem:sobolev`, label inventory).

Primary sources inspected by this lane (cumulative):

* Escauriaza–Seregin–Šverák, Russian Math. Surveys 58:2 (2003), **pp. 211–214**
  read as page images (rounds 1 and 2) from the mathnet.ru English
  translation PDF (`getFT.phtml?jrnid=rm&paperid=609&what=fullteng`, Referer
  `https://www.mathnet.ru/eng/rm609`): space definitions, (1.3)–(1.7) with
  the domain $\overline{Q_T}$, mixed norm, Theorem 1.2, the prose before
  Theorem 1.3, Theorem 1.3. The audit re-read the same pages and confirmed
  every transcription.
* Lieb–Loss, *Analysis*, 2nd ed., **pp. 64–70** read as page images (round 1:
  Theorem 2.16, Lemma 2.19); **table of contents pp. ix–xv** read as page
  images (this round, from a hosted 9-page front-matter sample): confirms
  "1.7 Fatou's lemma … 18", "2.16 Approximation by $C^\infty$-functions … 64",
  "2.19 Approximation by $C_c^\infty$-functions … 69", "8.2 Definition of
  $D^1(\R^n)$ and $D^{1/2}(\R^n)$ … 201", "8.3 Sobolev's inequality for
  gradients … 202". The text of Theorem 8.3 remains unread (AMS endmatter PDF
  returned HTTP 403; the hosted copy is front matter only).
* Rudin, *Real and Complex Analysis*, 3rd ed., **pp. 80–82** (round 1, OCR
  text; Theorems 4.11 and 4.12), confirmed by the audit from page images.

Still [MO]: Stein–Weiss Ch. I theorem numbers (E8), Lieb–Loss Theorem 8.3
text and constant (E10), Folland theorem numbers (E12), Nirenberg 1959
p. 125 (E10′, cited through the energy lane's `def:sobolev-constant`).
Galdi Ch. III remains behind a login wall and remains uncited.

Controller decisions (D1)–(D5) are followed. Proposition `prop:localtheory`
with package (R) of (D2) is **assumed**, as is Proposition `prop:energy`.
Nothing in this file bears on HIGH-PRESSURE, HIGH-STRAIN, CRITICAL,
ABSORPTION, or NS-R3.

---

## 1. Obligations discharged

| id | obligation (cp01-manuscript-obligations §4) | how it is discharged below |
|---|---|---|
| **C-0** | restate `thm:continuation` as "$T_*<\infty\Rightarrow\sup_{t<T_*}\|u(t)\|_3=\infty$"; replace ess sup by sup with justification | Theorem `thm:continuation` is stated in exactly that form, contrapositive displayed as `eq:endpoint`; sup = ess sup = sup over $[0,T_*)$ proved from $u\in C([0,T];L^3)$ (R1), consistent with the local-theory lane's `lem:sup-esssup` |
| **C-2** | the identification "classical branch = maximal $L^3$ solution" and the case $T^*(v_0)>\nu T_*$ | **Replaced** by (D3): the $\nu$-normalised branch is a Leray–Hopf weak solution in the exact printed ESS sense on every $Q_T$, $T\le S_*$ (Lemma `lem:leray-hopf`; density Lemma `lem:solenoidal-density` proved in full; endpoint $s=S_*$ by a weak limit), ESS Theorem 1.3 is quoted verbatim and applied (Lemma `lem:l3-to-l5`), and the manuscript-owned Serrin-type enstrophy bound (Lemma `lem:serrin-enstrophy`, explicit constant path, $\nu^{-4}$) closes through the $H^1$ alternative (R4). No uniqueness theorem for $L^3$ mild solutions is imported; the case $T^*(v_0)>\nu T_*$ does not arise (Remark `rem:gkp`) |
| **C-3** (assembly) | `thm:conditional`: smoothness on $\R^3\times[0,\infty)$ through the local-theory lemma; normalised pressure smooth; all Fefferman clauses | The proof of Theorem `thm:conditional` checks Fefferman's (1), (2), (3), (4), (6), (7) one by one, with (5) vacuous under alternative (A); smoothness cites the local-theory lane's Lemma `lem:global-smooth` (its C-3 lemma); the datum-class equivalence (4) $\iff$ Schwartz is written out |
| **S-1** ($H^1$-extension half) | the Sobolev inequality is needed on $H^1$, i.e. a density extension of the $C^1_c$ inequality | Lemma `lem:sobolev-h1` proves $\|f\|_6\le C_S\|\nabla f\|_2$ for every real $f\in\bigcap_kH^k(\R^3)$ from the compactly supported case (F3), by truncation with the cutoff of Lemma `lem:solenoidal-density` and Fatou; this is the class actually used. The source half of S-1 (pinning the $C^1_c$ statement and constant) is shared with the energy lane's `def:sobolev-constant` and remains [MO] here (Section 4) |
| §8 item 3 (literature) | cite ESS p. 213 for the meaning of $L_{3,\infty}$ | Remark `rem:ess-norm`, with the verbatim norm definition |
| $\nu$-normalisation | verified formula, now a lemma | Lemma `lem:nu-normalisation`: equation, pressure, time regularity, $H^1$ alternative, energy identity, and the $\nu^{-4}$ identity for $\int\|v\|_5^5$ transported; items (i)–(iv) coincide with the local-theory lane's `lem:nu-scaling`(a)–(d) and `prop:localtheory`(vi) and cite them |
| N-1 (partial) | enstrophy identity from exact memberships; $\|\nabla^2u\|_2=\|\Delta u\|_2$ | Steps 1–2 of the proof of Lemma `lem:serrin-enstrophy` (label `eq:serrin-enstrophy-identity`, renamed to avoid the energy lane's `eq:enstrophy-identity`) |

### Interface for the integrator

**Preamble.** The block uses a `lemma` environment: add
`\newtheorem{lemma}[theorem]{Lemma}` (the local-theory lane requires the same
line plus `corollary` and `definition`; one copy suffices). No other
environment or macro is needed beyond `\R`, `\norm` and the `amsmath`,
`amssymb`, `amsthm` already loaded.

**Labels retained (D4 and existing):** `thm:continuation`,
`thm:conditional`, `hyp:critical`, `eq:nu-normalization`, `eq:endpoint`,
`eq:missing`. **New labels owned by this lane:** `sec:continuation`,
`lem:nu-normalisation`, `eq:ess-13`–`eq:ess-17`, `lem:hardy`,
`lem:solenoidal-density`, `lem:leray-hopf`, `thm:ess`, `rem:ess-norm`,
`eq:ess-norm`, `lem:l3-to-l5`, `lem:sobolev-h1`, `lem:serrin-enstrophy`,
`eq:serrin-enstrophy-identity`, `eq:serrin-bound`, `rem:gkp`. Checked against
the label inventories of `cp02-local-theory.md` and
`cp02-energy-enstrophy.md`: no collision remains (round 1 had
`eq:enstrophy-identity`, which the energy lane also defines; renamed here).

**Cross-references to other lanes** (must resolve after the splice):
`prop:localtheory` with clauses (iii), (iv), (v), (vi) and `cor:Lq`,
`lem:nu-scaling`, `lem:global-smooth`, `lem:sup-esssup` (local-theory lane);
`prop:energy`, `def:sobolev-constant` (energy lane); `def:target`, `eq:NS`,
`hyp:absorption`, `eq:pressure-consequence`, `prop:lowpressure`,
`hyp:highpressure` (existing).

**Alignment of (R1)–(R4) with `prop:localtheory`.** The block abbreviates:
(R1) = Proposition `prop:localtheory`(iii) together with Corollary `cor:Lq`
(the $L^q$-continuity consequences, which (iii) does not itself state);
(R2) = the preamble of `prop:localtheory` ("smooth on $[0,T_*)\times\R^3$")
with clause (iii) (bounded derivatives on $[0,T]\times\R^3$) and clause (iv)
(equation pointwise, $\nabla\cdot u=0$, $p=R_iR_j(u_iu_j)$); (R3) = clause
(iv) ($u(0,x)=u_0(x)$); (R4) = clause (v) (which gives the stronger
$\lim_{t\uparrow T_*}\|u(t)\|_{H^1}=+\infty$). The block states this
abbreviation in its first paragraph.

**Overlaps to deduplicate (integrator's choice, both resolutions are
consistent).** (a) Lemma `lem:nu-normalisation`(i)–(iv) restates
`lem:nu-scaling`(a)–(d) and `prop:localtheory`(vi) for the branch; its proof
cites them and keeps a one-display chain-rule check. Items (v)–(vi) (energy
identity and the $\nu^{-4}$ identity) are new and are the ones used. (b)
`eq:nu-normalization` (this block, retained from `main.tex`, argument order
$(x,s)$) and `eq:nu-map` (local-theory lane, argument order $(s,x)$) name the
same substitution; the block says so. (c) Lemma `lem:sobolev-h1` proves the
scalar Sobolev inequality on $\bigcap_kH^k$; the energy lane's `lem:sobolev`
proves it on all of $H^1(\R^3)^m$ with the factor $\sqrt m$. The block uses
only the scalar statement on $\bigcap_kH^k$ (componentwise), with the same
constant $C_S$ of `def:sobolev-constant`, so the integrator may either keep
`lem:sobolev-h1` (self-contained) or replace its single use by
`lem:sobolev` with $m=1$; $C_*$ is unchanged either way.

**Items outside this lane's file, flagged for the owners.** (i)
`main.tex` lines 51–52 (inside `premise:local`: "Persistence of higher
Sobolev regularity and uniqueness identify this branch with the maximal mild
solutions used in the continuation theorem below") is false as a description
of the (D3) proof; the local-theory lane's §2.1 replacement paragraph
already deletes it — the integrator must use that paragraph. (ii) The
"Proof boundary" section of `main.tex` should, after integration, add the
sentence: "The continuation step is manuscript-owned except for the single
imported theorem of Escauriaza, Seregin, and Šverák
(Theorem~\ref{thm:ess}): the Leray--Hopf membership of the normalised branch
(Lemma~\ref{lem:leray-hopf}) and the Serrin-type enstrophy bound
(Lemma~\ref{lem:serrin-enstrophy}) are proved here." (iii) **Correction to
the CP01 record** (owner: literature lane): `cp01-literature-statements.md`
§3.1 writes the ESS Leray–Hopf domain as "$v:Q_T\to\R^3$"; the printed text
(p. 212) is $v\colon\overline{Q_T}\to\R^3$, which together with "for all
$t_0\in[0,T]$" in (1.6) is what forces the endpoint construction in
Lemma `lem:leray-hopf` Step 1. (iv) Noticed while checking label
inventories, not this lane's: both `cp02-local-theory.md` and
`cp02-energy-enstrophy.md` define `\label{lem:duality}`.

The block replaces the whole of the manuscript's Section 5 ("Endpoint
continuation and the missing estimate"), from `\section{Endpoint continuation
...}` to the end of the proof of `thm:conditional`. `hyp:critical` and the
two paragraphs following it are reproduced verbatim (marked `% RETAINED
VERBATIM`) so that the block is a drop-in replacement; they are not edited.

---

## 2. Replacement text

```latex
% ---------------------------------------------------------------------------
% CP02-2 replacement for Section 5 (repair round 2).  Requires in the preamble:
%   \newtheorem{lemma}[theorem]{Lemma}
% Assumes Proposition~\ref{prop:localtheory} with Corollary~\ref{cor:Lq},
% Lemma~\ref{lem:nu-scaling}, Lemma~\ref{lem:global-smooth} (local-theory
% section), Proposition~\ref{prop:energy} and Definition~\ref{def:sobolev-constant}
% (energy section).
% ---------------------------------------------------------------------------
\section{Endpoint continuation and the missing estimate}
\label{sec:continuation}

Throughout this section $u$ is the maximal classical solution on $[0,T_*)$
selected by Proposition~\ref{prop:localtheory}, with the normalised pressure
$p=R_iR_j(u_iu_j)$.  We abbreviate the clauses of that proposition that are
used here as follows; in each case $0<T<T_*$ is arbitrary.
\begin{itemize}
\item[(R1)] (Proposition~\ref{prop:localtheory}(iii) and
 Corollary~\ref{cor:Lq}) $u,p\in C^j([0,T];H^k(\R^3))$ for all integers
 $j,k\geq0$, and $u$, $\nabla u$, $p$, $\nabla p$, $\Delta u$, $\partial_tu$
 belong to $C([0,T];L^q(\R^3))$ for every $2\leq q\leq\infty$;
\item[(R2)] (the preamble of Proposition~\ref{prop:localtheory} with clauses
 (iii) and (iv)) $u,p\in C^\infty([0,T]\times\R^3)$ with all derivatives
 bounded on $[0,T]\times\R^3$, $\nabla\cdot u=0$, \eqref{eq:NS} holds
 pointwise on $[0,T]\times\R^3$, and $p(t)=R_iR_j(u_iu_j)(t)$ for every $t$;
\item[(R3)] (clause (iv)) $u(0)=u_0$;
\item[(R4)] (clause (v)) if $T_*<\infty$, then $\norm{u(t)}_{H^1}\to\infty$
 as $t\uparrow T_*$.
\end{itemize}
The global form of (R2) when $T_*=\infty$ is Lemma~\ref{lem:global-smooth}
of the local-theory section; it is used in Theorem~\ref{thm:conditional}.

\paragraph{Conventions.}
$\hat f(\xi)=\int_{\R^3}e^{-2\pi ix\cdot\xi}f(x)\,dx$, so that
$(\partial_jf)^\wedge=2\pi i\xi_j\hat f$ and
$(\Delta f)^\wedge=-4\pi^2|\xi|^2\hat f$; the Riesz transforms have symbols
$\widehat{R_jf}=-i\xi_j|\xi|^{-1}\hat f$.  Hence $R_iR_j$ has multiplier
$-\xi_i\xi_j|\xi|^{-2}$, which is also the multiplier of
$-\Delta^{-1}\partial_i\partial_j$ ($\Delta^{-1}$ has symbol
$-(4\pi^2|\xi|^2)^{-1}$ and $\partial_i\partial_j$ has symbol
$-4\pi^2\xi_i\xi_j$); thus $p=R_iR_j(u_iu_j)=-\Delta^{-1}\partial_i\partial_j(u_iu_j)$
is Tao's normalised pressure \cite[eq.~(9)]{Tao2013}.
We write $\norm{f}_{H^k}=\norm{(1+|\xi|^2)^{k/2}\hat f}_2$; this norm is
equivalent to $\norm{\langle\nabla\rangle^kf}_2$ used in \cite{Tao2013} and to
$(\sum_{|\alpha|\leq k}\norm{\partial^\alpha f}_2^2)^{1/2}$, with constants
depending only on $k$, so the memberships in (R1) and the divergence
statement (R4) do not depend on the choice.  For $k=1$ and $f\in H^1$,
Plancherel gives the exact identity
$\norm f_{H^1}^2=\norm f_2^2+(2\pi)^{-2}\norm{\nabla f}_2^2$ for this
convention.  $\langle f,g\rangle=\int_{\R^3}f\cdot g\,dx$ for real fields.
For a matrix field, $|\nabla u|^2=\sum_{i,j}|\partial_ju_i|^2$,
$\norm{\nabla u}_q=\norm{\,|\nabla u|\,}_q$, and
$\norm{\nabla^2u}_2^2=\sum_{i,j,k}\norm{\partial_j\partial_ku_i}_2^2$.
The substitution \eqref{eq:nu-normalization} below is the map
\eqref{eq:nu-map} of the local-theory section, written with the arguments
in the order $(x,s)$.

\paragraph{Standard facts used.}
Each is invoked below by its tag.
\begin{itemize}
\item[(F1)] \emph{Fourier package} (Stein--Weiss, \emph{Introduction to Fourier
 Analysis on Euclidean Spaces}, Princeton 1971, Chapter~I, \S\S1--2; the
 convention is that of \cite[eq.~(14)]{Tao2013}).  (a) The Fourier transform is
 a bijection of the Schwartz class $\mathcal S(\R^3)$ onto itself.
 (b) (Plancherel) For $h\in L^1\cap L^2$, $\norm{\hat h}_2=\norm h_2$, and the
 Fourier transform extends uniquely to a unitary operator $\mathcal F$ on
 $L^2(\R^3)$; in particular $\langle f,g\rangle=\int\hat f\,\overline{\hat g}\,d\xi$
 for real $f,g\in L^2$, the right side being real because for real $f,g$ the
 integrand at $-\xi$ is the complex conjugate of the integrand at $\xi$.
 (c) For $h\in L^1\cap L^2$,
 the function $x\mapsto\int e^{2\pi ix\cdot\xi}h(\xi)\,d\xi$ coincides almost
 everywhere with $\mathcal F^{-1}h$.  (d) For $f\in H^1(\R^3)$ the
 distributional derivative satisfies $(\partial_jf)^\wedge=2\pi i\xi_j\hat f$;
 in particular, if $f\in H^1(\R^3)^3$ and $\nabla\cdot f=0$, then
 $\xi\cdot\hat f(\xi)=0$ for a.e.\ $\xi$.
\item[(F2)] $C_c^\infty(\R^3)$ is dense in $L^r(\R^3)$ for $1\leq r<\infty$,
 for complex-valued functions (Lieb--Loss, \emph{Analysis}, 2nd ed., AMS 2001:
 Theorem~2.16, p.~64, gives $j_\varepsilon*f\to f$ in $L^r$ with
 $j_\varepsilon*f\in C^\infty$ for $j\in C_c^\infty$, $\int j=1$; Lemma~2.19,
 p.~69, multiplies these approximants by cutoffs $g_i\in C_c^\infty$ with
 $0\leq g_i\leq1$, $g_i\to1$ pointwise, preserving the $L^r$ convergence).
\item[(F3)] \emph{Sobolev inequality for compactly supported functions.}
 Let $C_S\in(0,\infty)$ be the constant of Definition~\ref{def:sobolev-constant}:
 $\norm g_6\leq C_S\norm{\nabla g}_2$ for every real-valued
 $g\in C_c^1(\R^3)$, in particular for every real $g\in C_c^\infty(\R^3)$.
 Its existence is documented there (Nirenberg, \emph{Ann.\ Scuola Norm.\
 Sup.\ Pisa} 13 (1959), p.~125, inequality (2.2), in the case $n=3$, $j=0$,
 $m=1$, $r=q=2$, $a=1$, $p=6$).  The sharp value is $C_S=S_3^{-1/2}$ with
 $S_3=\tfrac34(2\pi^2)^{2/3}=3(\pi/2)^{4/3}$ (Lieb--Loss, \emph{Analysis},
 2nd ed., Theorem~8.3, ``Sobolev's inequality for gradients'', p.~202, stated
 there for the class $D^1(\R^3)$ of \S8.2, p.~201, which contains
 $C_c^\infty(\R^3)$ because a compactly supported bounded function lies in
 $L^6$ and its gradient in $L^2$); only the existence of $C_S$ is used below,
 not its value.  We do \emph{not} assume $H^1(\R^3)\subset D^1(\R^3)$: the
 extension of the inequality from $C_c^\infty$ to the fields we need is
 Lemma~\ref{lem:sobolev-h1}.
\item[(F4)] \emph{Hilbert space package} (Rudin, \emph{Real and Complex
 Analysis}, 3rd ed., McGraw--Hill 1987, Theorem~4.11, p.~80, and
 Theorem~4.12, p.~81; stated there for complex scalars, but the proofs use
 only the inner-product axioms and the completeness of $H$, and apply verbatim
 to the real Hilbert space $L^2(\R^3;\R^3)$).  If $M$ is a closed subspace of
 $L^2$, every $w\in L^2$ decomposes uniquely as $w=\Pi w+(w-\Pi w)$ with
 $\Pi w\in M$ and $w-\Pi w\perp M$ (Theorem~4.11(a); $\Pi$ is the orthogonal
 projection onto $M$).  Consequently $(M^\perp)^\perp=M$: the inclusion
 $M\subset(M^\perp)^\perp$ is the definition, and if $x\perp M^\perp$ then,
 with $x=\Pi x+(x-\Pi x)$ and $x-\Pi x\in M^\perp$,
 $\norm{x-\Pi x}_2^2=\langle x,x-\Pi x\rangle-\langle\Pi x,x-\Pi x\rangle=0-0$,
 so $x=\Pi x\in M$.  Every bounded linear functional $\ell$ on $L^2$ is of the
 form $\ell(w)=\langle v_*,w\rangle$ for a unique $v_*\in L^2$
 (Theorem~4.12), and $\norm{v_*}_2=\norm\ell$ by Cauchy--Schwarz and
 $\ell(v_*)=\norm{v_*}_2^2$.
\item[(F5)] \emph{Lebesgue package}: Tonelli--Fubini, monotone and dominated
 convergence, Fatou's lemma, differentiation under the integral sign with an
 integrable dominant, and integration in polar coordinates
 $\int_{\R^3}f\,dx=\int_{S^2}\int_0^\infty f(r\omega)r^2\,dr\,d\sigma(\omega)$
 (Folland, \emph{Real Analysis}, 2nd ed., Wiley 1999, Theorems~2.14 (monotone
 convergence), 2.18 (Fatou), 2.24 (dominated convergence), 2.27 (parameter
 integrals), 2.37 (Fubini--Tonelli), 2.49 (polar coordinates); Fatou's lemma
 is also Lieb--Loss, \emph{Analysis}, 2nd ed., Theorem~1.7, p.~18).
\item[(F6)] H\"older's inequality, and Young's inequality
 $ab\leq a^{r}/r+b^{r'}/r'$ for $a,b\geq0$, $1/r+1/r'=1$.
\end{itemize}

\subsection{Viscosity normalisation}

\begin{lemma}[$\nu$-normalisation]\label{lem:nu-normalisation}
Put $S_*=\nu T_*$, $a=\nu^{-1}u_0$, and
\begin{equation}\label{eq:nu-normalization}
 v(x,s)=\nu^{-1}u(x,s/\nu),\qquad
 q(x,s)=\nu^{-2}p(x,s/\nu),\qquad 0\leq s<S_*.
\end{equation}
Then:
\begin{itemize}
\item[(i)] for every $0<S<S_*$, $v,q\in C^\infty([0,S]\times\R^3)$ with all
 derivatives bounded, $\nabla\cdot v=0$, $v(0)=a\in\mathcal S(\R^3)^3$,
 $q(s)=R_iR_j(v_iv_j)(s)$ for every $s$, and
 \[
  \partial_sv+(v\cdot\nabla)v+\nabla q=\Delta v
  \quad\text{pointwise on }[0,S]\times\R^3;
 \]
\item[(ii)] for every $0<S<S_*$ and all $j,k\geq0$,
 $v,q\in C^j([0,S];H^k(\R^3))$, with
 $\partial_s^jv(s)=\nu^{-1-j}(\partial_t^ju)(s/\nu)$; consequently
 $v,\nabla v,q,\nabla q,\Delta v,\partial_sv\in C([0,S];L^r)$ for
 $2\leq r\leq\infty$;
\item[(iii)] $\norm{v(s)}_r=\nu^{-1}\norm{u(s/\nu)}_r$ for $1\leq r\leq\infty$,
 $\norm{\nabla v(s)}_2=\nu^{-1}\norm{\nabla u(s/\nu)}_2$, and
 $\norm{v(s)}_{H^k}=\nu^{-1}\norm{u(s/\nu)}_{H^k}$;
\item[(iv)] if $S_*<\infty$ then $\norm{v(s)}_{H^1}\to\infty$ as $s\uparrow S_*$;
\item[(v)] for $0\leq s<S_*$,
 $\tfrac12\norm{v(s)}_2^2+\int_0^s\norm{\nabla v(\sigma)}_2^2\,d\sigma
 =\tfrac12\norm a_2^2$;
\item[(vi)] $\sup_{0\leq s<S_*}\norm{v(s)}_3=\nu^{-1}\sup_{0\leq t<T_*}\norm{u(t)}_3$
 and $\int_0^{S_*}\norm{v(s)}_5^5\,ds=\nu^{-4}\int_0^{T_*}\norm{u(t)}_5^5\,dt$,
 both identities holding in $[0,\infty]$.
\end{itemize}
Moreover $(v,q)$ is the classical branch of Proposition~\ref{prop:localtheory}
for the datum $a$ and viscosity $1$, with maximal time $S_*$
(Proposition~\ref{prop:localtheory}(vi)); this identification is recorded
for completeness and is not used below.
\end{lemma}

\begin{proof}
Items (i)--(iv) are Lemma~\ref{lem:nu-scaling}(a)--(d) applied to the branch,
with (R1)--(R4) as input; we record the computation.  (i) Fix $S<S_*$; then
$S/\nu<T_*$, and $(x,s)\mapsto(x,s/\nu)$ maps $[0,S]\times\R^3$ into
$[0,S/\nu]\times\R^3$, where $u,p$ are $C^\infty$ with bounded derivatives by
(R2).  Hence $v,q\in C^\infty([0,S]\times\R^3)$ with bounded derivatives.  By
the chain rule,
$\partial_sv(x,s)=\nu^{-2}(\partial_tu)(x,s/\nu)$,
$(v\cdot\nabla)v=\nu^{-2}\big((u\cdot\nabla)u\big)(x,s/\nu)$,
$\nabla q=\nu^{-2}(\nabla p)(x,s/\nu)$, and
$\Delta v=\nu^{-1}(\Delta u)(x,s/\nu)=\nu^{-2}\,(\nu\Delta u)(x,s/\nu)$.
Therefore
$\partial_sv+(v\cdot\nabla)v+\nabla q-\Delta v
=\nu^{-2}\big(\partial_tu+(u\cdot\nabla)u+\nabla p-\nu\Delta u\big)(x,s/\nu)=0$
by (R2), and $\nabla\cdot v=\nu^{-1}(\nabla\cdot u)(x,s/\nu)=0$.
$v(0)=\nu^{-1}u(0)=\nu^{-1}u_0$ by (R3), and $\nu^{-1}u_0$ is Schwartz.
Since $v_iv_j(\cdot,s)=\nu^{-2}(u_iu_j)(\cdot,s/\nu)$ and $R_iR_j$ is linear,
$R_iR_j(v_iv_j)(\cdot,s)=\nu^{-2}p(\cdot,s/\nu)=q(\cdot,s)$ by (R2).

(ii) The map $s\mapsto s/\nu$ is affine, so composing the $C^j([0,S/\nu];H^k)$
curve $u$ (from (R1)) with it gives a $C^j([0,S];H^k)$ curve, with the stated
derivative formula by the chain rule; the same for $p$.  The $L^r$
consequences are those of (R1) transported.

(iii) There is no change of the spatial variable, so every spatial norm of
$v(s)$ is $\nu^{-1}$ times the same norm of $u(s/\nu)$.

(iv) By (iii), $\norm{v(s)}_{H^1}=\nu^{-1}\norm{u(s/\nu)}_{H^1}$, and
$s\uparrow S_*$ if and only if $s/\nu\uparrow T_*$; apply (R4).

(v) Proposition~\ref{prop:energy} with $s=0$ and $t=s/\nu<T_*$ reads
$\tfrac12\norm{u(s/\nu)}_2^2+\nu\int_0^{s/\nu}\norm{\nabla u(\tau)}_2^2\,d\tau
=\tfrac12\norm{u_0}_2^2$.  Substitute $\tau=\sigma/\nu$ and (iii):
$\int_0^{s/\nu}\norm{\nabla u(\tau)}_2^2\,d\tau
=\nu^{-1}\int_0^s\norm{\nabla u(\sigma/\nu)}_2^2\,d\sigma
=\nu\int_0^s\norm{\nabla v(\sigma)}_2^2\,d\sigma$, while
$\norm{u(s/\nu)}_2^2=\nu^2\norm{v(s)}_2^2$ and $\norm{u_0}_2^2=\nu^2\norm a_2^2$.
Dividing by $\nu^2$ gives (v).

(vi) The first identity is (iii) with $r=3$.  For the second,
$\norm{v(s)}_5^5=\nu^{-5}\norm{u(s/\nu)}_5^5$, and the substitution $s=\nu t$
gives $\int_0^{S_*}\norm{v(s)}_5^5\,ds=\nu\int_0^{T_*}\nu^{-5}\norm{u(t)}_5^5\,dt$;
the integrands are continuous on $[0,S]$, resp.\ $[0,T]$, for every $S<S_*$,
$T<T_*$, by (ii) and (R1), hence on $[0,S_*)$, resp.\ $[0,T_*)$, so both
integrals are well defined in $[0,\infty]$ by monotone convergence.

The final assertion is Proposition~\ref{prop:localtheory}(vi).
\end{proof}

\subsection{The Leray--Hopf class of Escauriaza, Seregin, and \v Sver\'ak}

We recall the definitions of \cite[p.~212]{ESS2003} verbatim.  ``We denote by
$\dot C_0^\infty$ the space of all infinitely differentiable solenoidal vector
fields with compact support in $\R^3$; let $\mathring J$ and $\mathring J{}^1_2$
be the closures of $\dot C_0^\infty$ in the spaces $L_2$ and $W^1_2$,
respectively.''  Here $W^1_2=H^1(\R^3)^3$ with the norm
$\norm w_{W^1_2}=(\norm w_2^2+\norm{\nabla w}_2^2)^{1/2}$.
``Let $Q_T=\R^3\times{]0,T[}$.  By a Leray--Hopf weak solution of the Cauchy
problem (1.1), (1.2) in $Q_T$ we mean a vector field
$v\colon\overline{Q_T}\to\R^3$ such that''
\begin{align}
 &v\in L_\infty(0,T;\mathring J)\cap L_2(0,T;\mathring J{}^1_2),
 \label{eq:ess-13}\\
 &\text{the function }t\to\int_{\R^3}v(x,t)\cdot w(x)\,dx\text{ is continuous on }
 [0,T]\text{ for any }w\in L_2,\label{eq:ess-14}\\
 &\int_{Q_T}\big(-v\cdot\partial_tw-v\otimes v:\nabla w+\nabla v:\nabla w\big)
 \,dx\,dt=0\quad\text{for all }w\in\dot C_0^\infty(Q_T),\label{eq:ess-15}\\
 &\frac12\int_{\R^3}|v(x,t_0)|^2\,dx+\int_{\R^3\times]0,t_0[}|\nabla v|^2\,dx\,dt
 \leq\frac12\int_{\R^3}|a(x)|^2\,dx\quad\forall\,t_0\in[0,T],\label{eq:ess-16}\\
 &\norm{v(\cdot,t)-a(\cdot)}_2\to0\quad\text{as }t\to0.\label{eq:ess-17}
\end{align}
Here (1.1), (1.2) of \cite{ESS2003} are
$\partial_tv+\operatorname{div}v\otimes v-\Delta v=-\nabla p$,
$\operatorname{div}v=0$, $v(x,0)=a(x)$ (unit viscosity), and
$v\otimes v:\nabla w=v_iv_j\partial_jw_i$ in \eqref{eq:ess-15}.  The class
$\dot C_0^\infty(Q_T)$ is not defined separately in \cite{ESS2003} (only
$\dot C_0^\infty$ on $\R^3$ is); we read it, as is standard, as the space of
infinitely differentiable vector fields on $Q_T$ with compact support in
$Q_T$ which are solenoidal in $x$ for each $t$.  With this reading the
verification of \eqref{eq:ess-15} in Lemma~\ref{lem:leray-hopf} is the
strongest one possible, since any narrower test class is contained in it.
The numbers (1.3)--(1.7) of \cite{ESS2003} correspond to
\eqref{eq:ess-13}--\eqref{eq:ess-17}.  The existence theorem
\cite[Theorem~1.1]{ESS2003} assumes $a\in\mathring J$ (their (1.8)); the
regularity theorem we import, Theorem~\ref{thm:ess}, does not restate (1.8),
but our datum satisfies it (Lemma~\ref{lem:leray-hopf}), so the hypotheses
under which Theorem~\ref{thm:ess} is applied are at least as strong as those
of the neighbouring theorems in \cite{ESS2003}.

Two preparatory lemmas show that the smooth solenoidal fields we encounter
lie in $\mathring J{}^1_2$ on $\R^3$.

\begin{lemma}[Hardy's inequality along rays]\label{lem:hardy}
Let $A\in C^1(\R^3;\R^m)$ satisfy $\nabla A\in L^2(\R^3)$ and
$A(x)\to0$ as $|x|\to\infty$.  Then $A/|x|\in L^2(\R^3)$ and
$\norm{A/|x|}_2\leq2\norm{\nabla A}_2$.
\end{lemma}

\begin{proof}
For $\omega\in S^2$ and $r>0$ put $g_\omega(r)=|(\omega\cdot\nabla)A(r\omega)|$;
then $g_\omega$ is continuous on $(0,\infty)$, $g_\omega(r)\leq|\nabla A(r\omega)|$,
and $\frac{d}{dr}A(r\omega)=(\omega\cdot\nabla)A(r\omega)$.  By polar
coordinates (F5),
$\int_{S^2}\int_0^\infty r^2|\nabla A(r\omega)|^2\,dr\,d\sigma(\omega)
=\norm{\nabla A}_2^2<\infty$, so for $\sigma$-a.e.\ $\omega$ the number
$M_\omega=(\int_0^\infty r^2g_\omega(r)^2\,dr)^{1/2}$ is finite.  Fix such an
$\omega$.  By Cauchy--Schwarz, for $r>0$,
\[
 F_\omega(r):=\int_r^\infty g_\omega(s)\,ds
 \leq\Big(\int_r^\infty s^{-2}ds\Big)^{1/2}
 \Big(\int_r^\infty s^2g_\omega^2\,ds\Big)^{1/2}
 \leq r^{-1/2}M_\omega<\infty .
\]
For $0<r<R'$ the fundamental theorem of calculus gives
$A(r\omega)=A(R'\omega)-\int_r^{R'}\frac{d}{ds}A(s\omega)\,ds$; letting
$R'\to\infty$ and using $A(R'\omega)\to0$ yields
$|A(r\omega)|\leq F_\omega(r)$.

We now prove the one-dimensional inequality
$\int_0^\infty F_\omega^2\,dr\leq4M_\omega^2$.  Fix $0<\alpha<R$.  On
$[\alpha,R]$ the function $F_\omega$ is $C^1$ with $F_\omega'=-g_\omega$, so
integrating by parts,
\[
 \int_\alpha^RF_\omega^2\,dr
 =\big[rF_\omega^2\big]_\alpha^R+2\int_\alpha^R rF_\omega g_\omega\,dr
 \leq RF_\omega(R)^2+2\Big(\int_\alpha^RF_\omega^2\,dr\Big)^{1/2}M_\omega ,
\]
where the term $-\alpha F_\omega(\alpha)^2\leq0$ was dropped and
Cauchy--Schwarz was applied to $\int rF_\omega g_\omega$.  By the bound on
$F_\omega$, $RF_\omega(R)^2\leq\int_R^\infty s^2g_\omega^2\,ds=:\varepsilon_R$,
and $\varepsilon_R\to0$ as $R\to\infty$.  With
$X=(\int_\alpha^RF_\omega^2)^{1/2}<\infty$ we have
$X^2\leq\varepsilon_R+2M_\omega X$, hence
$X\leq M_\omega+(M_\omega^2+\varepsilon_R)^{1/2}$.  Letting $R\to\infty$
(monotone convergence) gives $(\int_\alpha^\infty F_\omega^2)^{1/2}\leq2M_\omega$,
and letting $\alpha\downarrow0$ gives the claim.  Consequently
$\int_0^\infty|A(r\omega)|^2\,dr\leq4\int_0^\infty r^2|\nabla A(r\omega)|^2\,dr$
for a.e.\ $\omega$, and integrating over $S^2$ (Tonelli, polar coordinates),
\[
 \int_{\R^3}\frac{|A(x)|^2}{|x|^2}\,dx
 =\int_{S^2}\int_0^\infty|A(r\omega)|^2\,dr\,d\sigma(\omega)
 \leq4\norm{\nabla A}_2^2 .\qedhere
\]
\end{proof}

\begin{lemma}[Smooth solenoidal fields lie in $\mathring J{}^1_2$]
\label{lem:solenoidal-density}
Let $v\in H^k(\R^3)^3$ for every $k\geq0$, with $\nabla\cdot v=0$.  Then there
are $v_R\in\dot C_0^\infty$ $(R\geq1)$ with $\norm{v_R-v}_{W^1_2}\to0$ as
$R\to\infty$.  Hence $v\in\mathring J{}^1_2\subset\mathring J$.  In
particular every divergence-free Schwartz field belongs to $\mathring J{}^1_2$.
(The statement is restricted to $\bigcap_kH^k$, which is all that is needed;
the general $H^1$ case is not claimed.)
\end{lemma}

\begin{proof}
\emph{Step 1: a vector potential.}  Define, for $\xi\neq0$,
\[
 \hat A(\xi)=\frac{i\,\xi\times\hat v(\xi)}{2\pi|\xi|^2},
 \qquad\text{so that}\qquad |\hat A(\xi)|\leq\frac{|\hat v(\xi)|}{2\pi|\xi|}.
\]
For $m\geq0$, Cauchy--Schwarz with the weight $(1+|\xi|^2)^{-2}$ and
$\int_{\R^3}(1+|\xi|^2)^{-2}d\xi=4\pi\int_0^\infty r^2(1+r^2)^{-2}dr=\pi^2$
give
\[
 \int_{\R^3}|\xi|^m|\hat v(\xi)|\,d\xi
 \leq\Big(\int(1+|\xi|^2)^{m+2}|\hat v|^2\Big)^{1/2}\pi
 =\pi\norm v_{H^{m+2}}<\infty .
\]
Hence for every multi-index $\alpha$ with $|\alpha|\geq1$,
$|\xi^\alpha\hat A|\leq(2\pi)^{-1}|\xi|^{|\alpha|-1}|\hat v|$ belongs to $L^1$,
and also to $L^2$ because $|\xi|^{|\alpha|-1}|\hat v|\leq(1+|\xi|^2)^{(|\alpha|-1)/2}|\hat v|$;
for $\alpha=0$,
$\norm{\hat A}_1\leq(2\pi)^{-1}\big(\int_{|\xi|<1}|\hat v|\,|\xi|^{-1}d\xi
+\int_{|\xi|\geq1}|\hat v|\,d\xi\big)
\leq(2\pi)^{-1}\big((4\pi)^{1/2}\norm v_2+\pi\norm v_{H^2}\big)$,
using $\int_{|\xi|<1}|\xi|^{-2}d\xi=4\pi$.  Define
\[
 A(x)=\int_{\R^3}e^{2\pi ix\cdot\xi}\hat A(\xi)\,d\xi .
\]
Since $|2\pi\xi|^{|\alpha|}|\hat A|\in L^1$ for every $\alpha$, differentiation
under the integral sign (F5) shows $A\in C^\infty(\R^3;\mathbb C^3)$ with
$\partial^\alpha A(x)=\int e^{2\pi ix\cdot\xi}(2\pi i\xi)^\alpha\hat A(\xi)\,d\xi$,
each derivative bounded by $\norm{(2\pi\xi)^\alpha\hat A}_1$.  Because $v$ is
real, $\hat v(-\xi)=\overline{\hat v(\xi)}$, hence $\hat A(-\xi)=\overline{\hat A(\xi)}$
and $A$ is real-valued.  For $|\alpha|\geq1$ the symbol
$(2\pi i\xi)^\alpha\hat A$ lies in $L^1\cap L^2$, so by (F1)(b),(c)
$\partial^\alpha A\in L^2$ with $\norm{\partial^\alpha A}_2=\norm{(2\pi\xi)^\alpha\hat A}_2$.
In particular, since $|\xi\times\hat v|\leq|\xi||\hat v|$,
\[
 \norm{\nabla A}_2^2=\sum_{j=1}^3\norm{2\pi\xi_j\hat A}_2^2
 \leq\sum_{j=1}^3\int\frac{\xi_j^2}{|\xi|^2}|\hat v|^2\,d\xi
 =\norm{\hat v}_2^2=\norm v_2^2 .
\]
$A$ vanishes at infinity: given $\varepsilon>0$ choose by (F2) a
$g\in C_c^\infty(\R^3;\mathbb C^3)$ with $\norm{\hat A-g}_1\leq\varepsilon$; then
$|A(x)-\check g(x)|\leq\varepsilon$ for all $x$, where
$\check g(x)=\int e^{2\pi ix\cdot\xi}g(\xi)\,d\xi$ is Schwartz by (F1)(a), so
$|\check g(x)|\leq\varepsilon$ for $|x|$ large, and
$\limsup_{|x|\to\infty}|A(x)|\leq2\varepsilon$.

\emph{Step 2: $\operatorname{curl}A=v$.}  By the derivative formula,
$(\operatorname{curl}A)(x)=\int e^{2\pi ix\cdot\xi}\,2\pi i\,\xi\times\hat A(\xi)\,d\xi$.
By (F1)(d), $\xi\cdot\hat v(\xi)=0$ for a.e.\ $\xi$, so
\[
 2\pi i\,\xi\times\hat A
 =-\frac{\xi\times(\xi\times\hat v)}{|\xi|^2}
 =-\frac{\xi(\xi\cdot\hat v)-|\xi|^2\hat v}{|\xi|^2}=\hat v
 \quad\text{a.e.}
\]
Thus $\operatorname{curl}A=\int e^{2\pi ix\cdot\xi}\hat v(\xi)\,d\xi$, and since
$\hat v\in L^1\cap L^2$ (the case $m=0$ above), (F1)(c) gives
$\operatorname{curl}A=v$ almost everywhere.

\emph{Step 3: cutoff.}  Fix $\chi\in C_c^\infty(\R^3)$ with $0\leq\chi\leq1$,
$\chi=1$ on $\{|x|\leq1\}$, $\chi=0$ on $\{|x|\geq2\}$, and put
$\chi_R(x)=\chi(x/R)$, so that $\nabla\chi_R$ and $\nabla^2\chi_R$ are
supported in $\{R\leq|x|\leq2R\}$ with $|\nabla\chi_R|\leq R^{-1}\norm{\nabla\chi}_\infty$
and $|\nabla^2\chi_R|\leq R^{-2}\norm{\nabla^2\chi}_\infty$.  Define
$v_R=\operatorname{curl}(\chi_RA)$.  Then $v_R\in C_c^\infty(\R^3)^3$
(support in $\{|x|\leq2R\}$), $\nabla\cdot v_R=0$ because
$\operatorname{div}\operatorname{curl}=0$, so $v_R\in\dot C_0^\infty$.  By the
product rule and Step~2,
\[
 v_R-v=(\chi_R-1)\,v+\nabla\chi_R\times A\quad\text{a.e.}
\]
By Lemma~\ref{lem:hardy} (applicable by Step~1),
$A/|x|\in L^2$ with $\norm{A/|x|}_2\leq2\norm{\nabla A}_2\leq2\norm v_2$, and on
$\{R\leq|x|\leq2R\}$ we have $|A|\leq2R\,|A|/|x|$; hence
\[
 \norm{A}_{L^2(R\leq|x|\leq2R)}\leq2R\,\norm{A/|x|}_{L^2(|x|\geq R)}
 =:2R\,\eta(R),\qquad \eta(R)\to0\ (R\to\infty),
\]
the last by dominated convergence applied to the tail of the $L^2$ function
$A/|x|$.  Therefore
\[
 \norm{v_R-v}_2\leq\norm{(1-\chi_R)v}_2+R^{-1}\norm{\nabla\chi}_\infty\cdot2R\,\eta(R)
 \longrightarrow0,
\]
the first term by dominated convergence ($|1-\chi_R|\leq1$, $\chi_R\to1$
pointwise).  For the gradient, for each $j$,
\[
 \partial_j(v_R-v)=(\chi_R-1)\partial_jv+(\partial_j\chi_R)\,v
 +(\partial_j\nabla\chi_R)\times A+\nabla\chi_R\times\partial_jA\quad\text{a.e.},
\]
and the four terms are bounded in $L^2$ by, respectively,
$\norm{(1-\chi_R)\partial_jv}_2\to0$ (dominated convergence),
$R^{-1}\norm{\nabla\chi}_\infty\norm v_2$,
$R^{-2}\norm{\nabla^2\chi}_\infty\cdot2R\,\eta(R)\leq4R^{-1}\norm{\nabla^2\chi}_\infty\norm v_2$,
and $R^{-1}\norm{\nabla\chi}_\infty\norm{\nabla A}_2\leq R^{-1}\norm{\nabla\chi}_\infty\norm v_2$.
All tend to zero, so $\norm{v_R-v}_{W^1_2}\to0$.  Since $\dot C_0^\infty\ni v_R$
and convergence in $W^1_2$ implies convergence in $L_2$, $v$ lies in the
$W^1_2$-closure $\mathring J{}^1_2$ and in the $L_2$-closure $\mathring J$.
A divergence-free Schwartz field belongs to every $H^k$, so the last claim
follows.
\end{proof}

\begin{lemma}[The normalised branch is a Leray--Hopf weak solution]
\label{lem:leray-hopf}
Let $v$, $q$, $a$, $S_*$ be as in Lemma~\ref{lem:nu-normalisation}, and let
$0<T\leq S_*$ with $T<\infty$.  If $T=S_*$, extend $v$ to $s=S_*$ by (any
Lebesgue representative of) the weak limit $v(\cdot,S_*):=v_*\in\mathring J$
constructed in Step~1 of the proof.
Then $v\colon\overline{Q_T}\to\R^3$ is a Leray--Hopf weak solution of the
Cauchy problem (1.1), (1.2) of \cite{ESS2003} in $Q_T$ with initial datum
$a\in\mathring J{}^1_2$, that is, \eqref{eq:ess-13}--\eqref{eq:ess-17} hold,
and the bounds are uniform up to $T=S_*$:
\[
 \sup_{0\leq s\leq T}\norm{v(s)}_2\leq\norm a_2,\qquad
 \int_0^T\norm{\nabla v(s)}_2^2\,ds\leq\tfrac12\norm a_2^2 .
\]
\end{lemma}

\begin{proof}
\emph{Step 0: memberships.}  For $0\leq s<S_*$, $v(s)\in H^k$ for all $k$ and
$\nabla\cdot v(s)=0$ (Lemma~\ref{lem:nu-normalisation}(i),(ii)), so
$v(s)\in\mathring J{}^1_2\subset\mathring J$ by
Lemma~\ref{lem:solenoidal-density}; in particular $a=v(0)\in\mathring J{}^1_2$.
By Lemma~\ref{lem:nu-normalisation}(v), $\norm{v(s)}_2\leq\norm a_2$ and
$\int_0^s\norm{\nabla v}_2^2\leq\tfrac12\norm a_2^2$ for all $s<S_*$; by
monotone convergence $\int_0^{S_*}\norm{\nabla v}_2^2\,ds\leq\tfrac12\norm a_2^2$.

\emph{Step 1: the weak limit at $S_*$.}  Suppose $T=S_*<\infty$.  Let $\Pi$ be
the orthogonal projection of $L_2$ onto the closed subspace $\mathring J$
(F4).  For $\varphi\in\dot C_0^\infty$ and $s<S_*$, the function
$s\mapsto\langle v(s),\varphi\rangle$ is $C^1$ on every $[0,S]$, $S<S_*$
(Lemma~\ref{lem:nu-normalisation}(ii) with $j=1$, $k=0$), with derivative
$\langle\partial_sv,\varphi\rangle=\langle\Delta v-(v\cdot\nabla)v-\nabla q,\varphi\rangle$.
Integrating by parts against the compactly supported smooth $\varphi$
($v$, $q$ smooth):
$\langle\Delta v,\varphi\rangle=\langle v,\Delta\varphi\rangle$;
$-\langle(v\cdot\nabla)v,\varphi\rangle=-\int v_j\partial_jv_i\varphi_i
=\int v_iv_j\partial_j\varphi_i$ (using $\nabla\cdot v=0$);
$-\langle\nabla q,\varphi\rangle=\langle q,\nabla\cdot\varphi\rangle=0$.  Hence
\[
 \Big|\frac{d}{ds}\langle v(s),\varphi\rangle\Big|
 \leq\norm{v(s)}_2\norm{\Delta\varphi}_2+\norm{v(s)}_2^2\norm{\nabla\varphi}_\infty
 \leq\norm a_2\norm{\Delta\varphi}_2+\norm a_2^2\norm{\nabla\varphi}_\infty=:L_\varphi ,
\]
so $s\mapsto\langle v(s),\varphi\rangle$ is $L_\varphi$-Lipschitz on $[0,S_*)$
and has a limit as $s\uparrow S_*$.  Now let $w\in L_2$ be arbitrary.  Since
$v(s)\in\mathring J$ and $w-\Pi w\perp\mathring J$,
$\langle v(s),w\rangle=\langle v(s),\Pi w\rangle$.  Given $\varepsilon>0$ choose
$\varphi\in\dot C_0^\infty$ with $\norm{\Pi w-\varphi}_2\leq\varepsilon$
($\dot C_0^\infty$ is dense in $\mathring J$ by definition).  Then for
$s,s'<S_*$,
\[
 |\langle v(s)-v(s'),w\rangle|
 \leq|\langle v(s)-v(s'),\Pi w-\varphi\rangle|+|\langle v(s)-v(s'),\varphi\rangle|
 \leq2\norm a_2\varepsilon+L_\varphi|s-s'| ,
\]
so $\limsup_{s,s'\uparrow S_*}|\langle v(s)-v(s'),w\rangle|\leq2\norm a_2\varepsilon$
for every $\varepsilon$, and $\ell(w):=\lim_{s\uparrow S_*}\langle v(s),w\rangle$
exists.  $\ell$ is linear with $|\ell(w)|\leq\norm a_2\norm w_2$, so by (F4)
there is a unique $v_*\in L_2$ with $\ell(w)=\langle v_*,w\rangle$ for all $w$,
and $\norm{v_*}_2\leq\norm a_2$.  Moreover $v_*\in\mathring J$: for
$w\perp\mathring J$, $\langle v_*,w\rangle=\lim\langle v(s),w\rangle=0$, so
$v_*\in(\mathring J^\perp)^\perp=\mathring J$ (F4).  Finally
$\norm{v_*}_2^2=\lim_{s\uparrow S_*}\langle v(s),v_*\rangle
\leq\liminf_{s\uparrow S_*}\norm{v(s)}_2\norm{v_*}_2$, so
$\norm{v_*}_2\leq\liminf_{s\uparrow S_*}\norm{v(s)}_2$.
Fix any Lebesgue representative of $v_*$ (a function $\R^3\to\R^3$) and set
$v(\cdot,S_*):=v_*$, so that $v$ is literally a function on
$\overline{Q_{S_*}}$; the choice of representative affects none of
\eqref{eq:ess-13}--\eqref{eq:ess-17}, which involve $v(\cdot,S_*)$ only
through integrals.  (If $T<S_*$ nothing is needed: $v$ is defined and
continuous into $W^1_2$ on $[0,T]$.)

\emph{Step 2: \eqref{eq:ess-13}.}  On $[0,T)$ the map $s\mapsto v(s)$ is
continuous into $W^1_2$ (Lemma~\ref{lem:nu-normalisation}(ii)), hence
strongly measurable on $(0,T)$, with values in $\mathring J{}^1_2$ by Step~0.
By Step~0 and Step~1, $\norm{v(s)}_2\leq\norm a_2$ for every $s\in[0,T]$, so
$v\in L_\infty(0,T;\mathring J)$; and
$\int_0^T\norm{v(s)}_{W^1_2}^2\,ds=\int_0^T(\norm{v}_2^2+\norm{\nabla v}_2^2)\,ds
\leq T\norm a_2^2+\tfrac12\norm a_2^2<\infty$, so
$v\in L_2(0,T;\mathring J{}^1_2)$.  The displayed uniform bounds are those of
Step~0 and Step~1.

\emph{Step 3: \eqref{eq:ess-14}.}  Let $w\in L_2$.  For $s,s'\in[0,T)$,
$|\langle v(s)-v(s'),w\rangle|\leq\norm{v(s)-v(s')}_2\norm w_2$, and
$s\mapsto v(s)$ is continuous into $L_2$ on $[0,S]$ for every $S<S_*$; this
gives continuity on $[0,T)$, and on $[0,T]$ if $T<S_*$.  If $T=S_*$,
continuity at $s=S_*$ is the statement $\langle v(s),w\rangle\to\langle v_*,w\rangle$
of Step~1.

\emph{Step 4: \eqref{eq:ess-15}.}  Let $w\in\dot C_0^\infty(Q_T)$.  Its support
lies in $K\times[t_1,t_2]$ for a compact $K\subset\R^3$ and
$0<t_1<t_2<T\leq S_*$.  On $[t_1,t_2]\times\R^3$, $v$ and $q$ are $C^\infty$
and satisfy $\partial_sv+(v\cdot\nabla)v+\nabla q-\Delta v=0$ pointwise
(Lemma~\ref{lem:nu-normalisation}(i)); note $(v\cdot\nabla)v=\operatorname{div}(v\otimes v)$
because $\nabla\cdot v=0$, so this is (1.1) of \cite{ESS2003}.  Multiply by
$w$ and integrate over $\R^3\times[t_1,t_2]$; every integrand is continuous
with compact support, so all integrals are finite and Fubini applies.
Integrating by parts in $s$ (with $w(\cdot,t_1)=w(\cdot,t_2)=0$) and in $x$
(compact support in $x$):
$\int\partial_sv\cdot w=-\int v\cdot\partial_sw$;
$\int(v\cdot\nabla)v\cdot w=\int v_j\partial_jv_i\,w_i=-\int v_iv_j\partial_jw_i$
(using $\partial_jv_j=0$);
$\int\nabla q\cdot w=-\int q\,\nabla\cdot w=0$;
$-\int\Delta v\cdot w=\int\nabla v:\nabla w$.  Adding,
$\int_{Q_T}(-v\cdot\partial_sw-v\otimes v:\nabla w+\nabla v:\nabla w)\,dx\,ds=0$,
which is \eqref{eq:ess-15}.

\emph{Step 5: \eqref{eq:ess-16}.}  For $t_0\in[0,T)$, Tonelli gives
$\int_{\R^3\times]0,t_0[}|\nabla v|^2\,dx\,ds=\int_0^{t_0}\norm{\nabla v(s)}_2^2\,ds$
($|\nabla v|^2$ is continuous on $\R^3\times[0,t_0]$), and
Lemma~\ref{lem:nu-normalisation}(v) gives equality in \eqref{eq:ess-16}.
If $T=S_*$ and $t_0=S_*$: by Step~1 and Lemma~\ref{lem:nu-normalisation}(v),
\[
 \tfrac12\norm{v_*}_2^2\leq\liminf_{s\uparrow S_*}\tfrac12\norm{v(s)}_2^2
 =\tfrac12\norm a_2^2-\lim_{s\uparrow S_*}\int_0^s\norm{\nabla v}_2^2
 =\tfrac12\norm a_2^2-\int_0^{S_*}\norm{\nabla v}_2^2\,ds ,
\]
the limit existing by monotonicity; this is \eqref{eq:ess-16} at $t_0=S_*$.

\emph{Step 6: \eqref{eq:ess-17}.}  $v\in C([0,S];L_2)$ for $S<S_*$ and
$v(0)=a$ (Lemma~\ref{lem:nu-normalisation}(i),(ii)).
\end{proof}

\subsection{The endpoint theorem}

\begin{theorem}[Escauriaza--Seregin--\v Sver\'ak, Theorem~1.3 of \cite{ESS2003};
quoted, not proved here]\label{thm:ess}
\textup{(Verbatim from \cite[p.~214]{ESS2003}; (1.1), (1.2) are as recalled
above and (1.13) is recalled in Remark~\ref{rem:ess-norm}.)}
Suppose that $v$ is a weak Leray--Hopf solution of the Cauchy problem (1.1),
(1.2) in $Q_T$ and $v$ satisfies the additional condition (1.13).  Then
\[
 v\in L_5(Q_T),
\]
and hence it is smooth and unique on $Q_T$.
\end{theorem}

\begin{remark}[The mixed norm]\label{rem:ess-norm}
Condition (1.13) of \cite{ESS2003} is $v\in L_{3,\infty}(Q_T)$, where
(\cite[p.~213]{ESS2003}, verbatim) ``the norm in the mixed Lebesgue space
$L_{s,l}(Q_T)$ is given as follows:
\begin{equation}\label{eq:ess-norm}
 \norm f_{s,l,Q_T}=
 \begin{cases}
  \Big(\int_0^T\norm{f(\cdot,t)}_s^l\,dt\Big)^{1/l}, & l\in[1,+\infty[,\\[4pt]
  \operatorname*{ess\,sup}_{t\in]0,T[}\norm{f(\cdot,t)}_s, & l=+\infty .
 \end{cases}
\end{equation}
If $s=l$, then we briefly write $\norm f_{s,Q_T}$ instead of
$\norm f_{s,s,Q_T}$.''  Thus $L_{3,\infty}(Q_T)=L^\infty_tL^3_x(Q_T)$; the
subscript does not denote the weak Lorentz space $L^{3,\infty}_x$.  We use
only the conclusion $v\in L_5(Q_T)$, i.e.\ $\int_{Q_T}|v|^5\,dx\,dt<\infty$,
not the smoothness or uniqueness clauses.  The backward-uniqueness proof of
Theorem~\ref{thm:ess} is imported rather than reproduced here.  The prose
preceding Theorem~1.3 in \cite[p.~214]{ESS2003} states the classical form
``If $]0,T_*[$ is the maximal interval on which a smooth solution of the
problem (1.1), (1.2) exists and if $T_*<+\infty$, then
$\limsup_{t\uparrow T_*}\int_{\R^3}|v(x,t)|^3\,dx=+\infty$''; since the
solution class of that sentence is not specified there, we import only the
numbered theorem and verify its hypotheses in Lemma~\ref{lem:leray-hopf}.
\end{remark}

\begin{lemma}[$L^3$ control gives $L^5$ integrability]\label{lem:l3-to-l5}
If $T_*<\infty$ and $\sup_{0\leq t<T_*}\norm{u(t)}_3<\infty$, then
\[
 \int_0^{T_*}\norm{u(t)}_5^5\,dt<\infty ,
\]
that is, $u\in L^5(\R^3\times(0,T_*))$.
\end{lemma}

\begin{proof}
Let $v$, $a$, $S_*=\nu T_*<\infty$ be as in Lemma~\ref{lem:nu-normalisation}.
By Lemma~\ref{lem:leray-hopf} with $T=S_*$, $v$ is a Leray--Hopf weak solution
in $Q_{S_*}$ with datum $a\in\mathring J$.  The function $s\mapsto\norm{v(s)}_3$
is continuous on $[0,S]$ for every $S<S_*$ (Lemma~\ref{lem:nu-normalisation}(ii)),
hence continuous on $[0,S_*)$ and measurable on $]0,S_*[$, and by
\eqref{eq:ess-norm} and Lemma~\ref{lem:nu-normalisation}(vi),
\[
 \norm v_{3,\infty,Q_{S_*}}
 =\operatorname*{ess\,sup}_{s\in]0,S_*[}\norm{v(s)}_3
 \leq\sup_{0\leq s<S_*}\norm{v(s)}_3
 =\nu^{-1}\sup_{0\leq t<T_*}\norm{u(t)}_3<\infty ,
\]
which is (1.13).  Theorem~\ref{thm:ess} gives $\int_{Q_{S_*}}|v|^5\,dx\,ds<\infty$.
Since $v$ is continuous on $\R^3\times[0,S_*)$, Tonelli gives
$\int_{Q_{S_*}}|v|^5=\int_0^{S_*}\norm{v(s)}_5^5\,ds$, and
Lemma~\ref{lem:nu-normalisation}(vi) converts this into
$\nu^{-4}\int_0^{T_*}\norm{u(t)}_5^5\,dt<\infty$.  The last assertion is
Tonelli again ($u$ is continuous on $\R^3\times[0,T_*)$).
\end{proof}

\subsection{The Sobolev inequality on smooth square-integrable fields}

\begin{lemma}[Sobolev inequality on $\bigcap_kH^k$]\label{lem:sobolev-h1}
Let $f\in H^k(\R^3)$ for every integer $k\geq0$, with $f$ real-valued.  Then
$f\in L^6(\R^3)$ and
\[
 \norm f_6\leq C_S\norm{\nabla f}_2 ,
\]
with $C_S$ the constant of \textup{(F3)} and $\nabla f$ the distributional
gradient.
\end{lemma}

\begin{proof}
\emph{Step 1: a smooth representative with bounded derivatives.}  For every
$m\geq0$, the computation of Step~1 of the proof of
Lemma~\ref{lem:solenoidal-density}---Cauchy--Schwarz with the weight
$(1+|\xi|^2)^{-2}$, whose integral is $\pi^2$, and
$|\xi|^m\leq(1+|\xi|^2)^{m/2}$---gives
$\int_{\R^3}|\xi|^m|\hat f(\xi)|\,d\xi\leq\pi\norm f_{H^{m+2}}<\infty$.
Hence $(2\pi i\xi)^\alpha\hat f\in L^1$ for every multi-index $\alpha$, and
also $(2\pi i\xi)^\alpha\hat f\in L^2$ since $f\in H^{|\alpha|}$.  By
differentiation under the integral sign \textup{(F5)} the function
$F(x):=\int e^{2\pi ix\cdot\xi}\hat f(\xi)\,d\xi$ is in $C^\infty(\R^3)$ with
$\partial^\alpha F(x)=\int e^{2\pi ix\cdot\xi}(2\pi i\xi)^\alpha\hat f(\xi)\,d\xi$,
every derivative bounded by $\norm{(2\pi\xi)^\alpha\hat f}_1$; $F$ is
real-valued because $\hat f(-\xi)=\overline{\hat f(\xi)}$.  By
\textup{(F1)(c)} (applicable since $\hat f\in L^1\cap L^2$), $F=f$ almost
everywhere, and by \textup{(F1)(c),(d)} applied to $(\partial_jf)^\wedge
=2\pi i\xi_j\hat f\in L^1\cap L^2$, $\partial_jF=\partial_jf$ almost
everywhere, where the right side is the distributional derivative.  In
particular $\norm F_2=\norm f_2$, $\norm{\nabla F}_2=\norm{\nabla f}_2$, and
$\norm F_6=\norm f_6$ in $[0,\infty]$.

\emph{Step 2: truncation.}  Let $\chi_R$ be the cutoff of Step~3 of the proof
of Lemma~\ref{lem:solenoidal-density}: $\chi\in C_c^\infty(\R^3)$,
$0\leq\chi\leq1$, $\chi=1$ on $\{|x|\leq1\}$, $\chi=0$ on $\{|x|\geq2\}$, and
$\chi_R(x)=\chi(x/R)$, so $|\nabla\chi_R|\leq R^{-1}\norm{\nabla\chi}_\infty$.
Then $\chi_RF\in C_c^\infty(\R^3)$ is real-valued, and \textup{(F3)} gives
\[
 \norm{\chi_RF}_6\leq C_S\norm{\nabla(\chi_RF)}_2
 \leq C_S\bigl(\norm{\chi_R\nabla F}_2+\norm{F\nabla\chi_R}_2\bigr)
 \leq C_S\Bigl(\norm{\nabla f}_2
 +\frac{\norm{\nabla\chi}_\infty}{R}\norm f_2\Bigr),
\]
using $0\leq\chi_R\leq1$ and Step~1.

\emph{Step 3: limit.}  $\chi_RF\to F$ pointwise on $\R^3$ as $R\to\infty$
(for each $x$, $\chi_R(x)=1$ once $R\geq|x|$), so Fatou's lemma
\textup{(F5)} applied to $|\chi_RF|^6$ gives
$\norm F_6\leq\liminf_{R\to\infty}\norm{\chi_RF}_6$.  Letting $R\to\infty$ in
the display of Step~2 yields $\norm F_6\leq C_S\norm{\nabla f}_2<\infty$; by
Step~1 this is $\norm f_6\leq C_S\norm{\nabla f}_2$, and in particular
$f\in L^6$.
\end{proof}

\subsection{A Serrin-type enstrophy bound}

\begin{lemma}[Serrin-type enstrophy bound]\label{lem:serrin-enstrophy}
Let $0<T\leq T_*$ and suppose $\int_0^T\norm{u(t)}_5^5\,dt<\infty$.  Then,
with $C_*=\frac{256}{3125}C_S^3$ and $C_S$ the constant of (F3),
\begin{equation}\label{eq:serrin-bound}
 \sup_{0\leq t<T}\norm{\nabla u(t)}_2
 \leq\norm{\nabla u_0}_2\exp\Big(C_*\nu^{-4}\int_0^T\norm{u(t)}_5^5\,dt\Big),
\end{equation}
and consequently $\sup_{0\leq t<T}\norm{u(t)}_{H^1}<\infty$.
\end{lemma}

\begin{proof}
\emph{Step 1: the enstrophy identity.}  Fix $T'<T$ (so $T'<T_*$).  By (R1),
$u\in C^1([0,T'];H^2)$, hence $\nabla u\in C^1([0,T'];L^2)$ with
$\partial_t\nabla u=\nabla\partial_tu$ ($\nabla\colon H^2\to L^2$ is bounded
linear).  For a $C^1$ curve $f$ in $L^2$ the identity
$\norm{f(t+h)}_2^2-\norm{f(t)}_2^2=2\langle f(t),f(t+h)-f(t)\rangle+\norm{f(t+h)-f(t)}_2^2$
shows that $Y(t)=\norm{\nabla u(t)}_2^2$ is $C^1$ on $[0,T']$ with
$Y'=2\langle\nabla u,\nabla\partial_tu\rangle$.  By Plancherel (F1)(b) and
$(\partial_jf)^\wedge=2\pi i\xi_j\hat f$,
\[
 \langle\nabla u,\nabla\partial_tu\rangle
 =\sum_{i,j}\int4\pi^2\xi_j^2\,\hat u_i\,\overline{(\partial_tu)^\wedge_i}\,d\xi
 =-\sum_i\int(-4\pi^2|\xi|^2\hat u_i)\overline{(\partial_tu)^\wedge_i}\,d\xi
 =-\langle\Delta u,\partial_tu\rangle ,
\]
all integrals converging absolutely since $u(t)\in H^2$ and $\partial_tu(t)\in L^2$.
By (R2), $\partial_tu=\nu\Delta u-(u\cdot\nabla)u-\nabla p$ pointwise, hence as
elements of $L^2$ (each term is in $L^2$ by (R1); $|(u\cdot\nabla)u|\leq|u||\nabla u|$
with $u\in L^\infty$, $\nabla u\in L^2$).  Therefore
$\langle\Delta u,\partial_tu\rangle=\nu\norm{\Delta u}_2^2-\langle\Delta u,(u\cdot\nabla)u\rangle
-\langle\Delta u,\nabla p\rangle$, and the last term vanishes: by Plancherel,
\[
 \langle\Delta u,\nabla p\rangle
 =\sum_i\int(-4\pi^2|\xi|^2\hat u_i)\,\overline{2\pi i\xi_i\hat p}\,d\xi
 =\int4\pi^2|\xi|^2\,\overline{\hat p}\,\Big(\sum_i2\pi i\xi_i\hat u_i\Big)d\xi
 =\int4\pi^2|\xi|^2\,\overline{\hat p}\,(\nabla\cdot u)^\wedge\,d\xi=0 ,
\]
absolutely convergent because $u,p\in H^k$ for all $k$, and
$(\nabla\cdot u)^\wedge=0$ by (F1)(d).  Collecting,
\begin{equation}\label{eq:serrin-enstrophy-identity}
 \tfrac12Y'(t)+\nu\norm{\Delta u(t)}_2^2
 =\big\langle(u\cdot\nabla)u,\Delta u\big\rangle(t),\qquad 0\leq t<T .
\end{equation}

\emph{Step 2: the estimate.}  Pointwise $|(u\cdot\nabla)u|\leq|u||\nabla u|$,
so H\"older with $\frac15+\frac3{10}+\frac12=1$ gives
\[
 \big|\langle(u\cdot\nabla)u,\Delta u\rangle\big|
 \leq\norm u_5\norm{\nabla u}_{10/3}\norm{\Delta u}_2 .
\]
Interpolation: for $f=|\nabla u|$ and $\theta=\frac25$, since
$\frac3{10}=\frac\theta2+\frac{1-\theta}6$, H\"older with the conjugate
exponents $\frac{2}{\theta\cdot10/3}=\frac32$ and $\frac{6}{(1-\theta)10/3}=3$
gives
$\int f^{10/3}=\int f^{4/3}f^{2}\leq(\int f^2)^{2/3}(\int f^6)^{1/3}$,
i.e.\ $\norm{\nabla u}_{10/3}\leq\norm{\nabla u}_2^{2/5}\norm{\nabla u}_6^{3/5}$.
Sobolev: each component $g_{ij}=\partial_ju_i$ of $\nabla u(t)$ is
real-valued and lies in $H^k(\R^3)$ for every $k\geq0$ by (R1), so
Lemma~\ref{lem:sobolev-h1} gives $\norm{g_{ij}}_6\leq C_S\norm{\nabla g_{ij}}_2$;
hence
\[
 \norm{\nabla u}_6^2=\Big\|\sum_{i,j}g_{ij}^2\Big\|_3
 \leq\sum_{i,j}\norm{g_{ij}^2}_3=\sum_{i,j}\norm{g_{ij}}_6^2
 \leq C_S^2\sum_{i,j}\norm{\nabla g_{ij}}_2^2=C_S^2\norm{\nabla^2u}_2^2 .
\]
Plancherel: $\norm{\nabla^2u}_2^2=\sum_{i,j,k}\int(2\pi\xi_j)^2(2\pi\xi_k)^2|\hat u_i|^2
=\sum_i\int(4\pi^2|\xi|^2)^2|\hat u_i|^2=\norm{\Delta u}_2^2$.  Altogether
\[
 \big|\langle(u\cdot\nabla)u,\Delta u\rangle\big|
 \leq C_S^{3/5}\,\norm u_5\,Y^{1/5}\,\norm{\Delta u}_2^{8/5}.
\]

\emph{Step 3: absorption.}  Young's inequality (F6) with exponents $\frac54$
and $5$, $ab\leq\frac45a^{5/4}+\frac15b^5$, applied to
$a=(\tfrac{5\nu}4)^{4/5}\norm{\Delta u}_2^{8/5}$ and
$b=(\tfrac{5\nu}4)^{-4/5}C_S^{3/5}\norm u_5Y^{1/5}$, gives
\[
 C_S^{3/5}\norm u_5Y^{1/5}\norm{\Delta u}_2^{8/5}
 \leq\nu\norm{\Delta u}_2^2+\frac15\Big(\frac4{5\nu}\Big)^4C_S^3\norm u_5^5\,Y
 =\nu\norm{\Delta u}_2^2+C_*\nu^{-4}\norm u_5^5\,Y .
\]
Inserting this in \eqref{eq:serrin-enstrophy-identity} and cancelling
$\nu\norm{\Delta u}_2^2$,
\[
 Y'(t)\leq g(t)Y(t),\qquad g(t)=2C_*\nu^{-4}\norm{u(t)}_5^5,\qquad0\leq t<T .
\]

\emph{Step 4: Gronwall.}  $g$ is continuous on $[0,T']$ for every $T'<T$
(R1), hence on $[0,T)$, and $G(t)=\int_0^tg$ satisfies
$G(t)\leq G_T:=2C_*\nu^{-4}\int_0^T\norm u_5^5<\infty$ by hypothesis.  Since
$(Ye^{-G})'=(Y'-gY)e^{-G}\leq0$ on $[0,T')$, $Y(t)\leq Y(0)e^{G(t)}\leq Y(0)e^{G_T}$
for $0\leq t<T'$, and $T'<T$ was arbitrary.  By (R3), $Y(0)=\norm{\nabla u_0}_2^2$;
taking square roots gives \eqref{eq:serrin-bound}.  Finally, with the norm
convention fixed above,
$\norm{u(t)}_{H^1}^2=\norm{u(t)}_2^2+(2\pi)^{-2}\norm{\nabla u(t)}_2^2
\leq\norm{u_0}_2^2+\norm{\nabla u_0}_2^2e^{G_T}$ by
Proposition~\ref{prop:energy} and \eqref{eq:serrin-bound}; for any
equivalent $H^1$ norm the bound changes by a constant factor, and the
conclusion $\sup_{0\leq t<T}\norm{u(t)}_{H^1}<\infty$ is the same.
\end{proof}

\subsection{Endpoint continuation}

\begin{theorem}[Endpoint continuation]\label{thm:continuation}
Let $u$ be the maximal classical solution on $[0,T_*)$ arising from a
divergence-free Schwartz datum $u_0$ and viscosity $\nu>0$
(Proposition~\ref{prop:localtheory}).  If $T_*<\infty$, then
\[
 \sup_{0<t<T_*}\norm{u(t)}_{L^3(\R^3)}=\infty .
\]
Equivalently: if
\begin{equation}\label{eq:endpoint}
 \sup_{0<t<T_*}\norm{u(t)}_{L^3(\R^3)}<\infty ,
\end{equation}
then $T_*=\infty$.  Because $u\in C([0,T];L^3)$ for every $T<T_*$ by (R1),
the supremum in \eqref{eq:endpoint} equals the essential supremum over
$(0,T_*)$, and it equals $\sup_{0\leq t<T_*}$
(cf.\ Lemma~\ref{lem:sup-esssup}).
\end{theorem}

\begin{proof}
Suppose $T_*<\infty$ and, for contradiction, that \eqref{eq:endpoint} holds.
Then $\sup_{0\leq t<T_*}\norm{u(t)}_3<\infty$ as well (the value at $t=0$ is
$\norm{u_0}_3<\infty$).  Lemma~\ref{lem:l3-to-l5} gives
$\int_0^{T_*}\norm{u(t)}_5^5\,dt<\infty$.  Lemma~\ref{lem:serrin-enstrophy}
with $T=T_*$ gives $\sup_{0\leq t<T_*}\norm{u(t)}_{H^1}<\infty$.  This
contradicts (R4).  Hence \eqref{eq:endpoint} fails, i.e.\ the supremum is
infinite.  The equivalence with the contrapositive form and the statements
about the supremum are immediate from continuity of $t\mapsto\norm{u(t)}_3$
on $[0,T_*)$: a continuous function on an interval has essential supremum
equal to its supremum (every value is a limit of values taken outside any
null set), and its supremum over $(0,T_*)$ equals that over $[0,T_*)$.
\end{proof}

% RETAINED VERBATIM from the current manuscript (not edited by lane CP02-2).
\begin{hypothesis}[Finite-horizon critical estimate]\label{hyp:critical}
For every $\nu>0$, divergence-free $u_0\in\mathcal S(\R^3)^3$, and
$0<H<\infty$, there is a finite nonnegative $M(\nu,u_0,H)$ such that
\begin{equation}\label{eq:missing}
 \sup_{0<t<\min\{H,T_*\}}\norm{u(t)}_3\leq M(\nu,u_0,H).
\end{equation}
The same bound must work for the entire interval. Proving that the
left side is finite is the unresolved assertion, not a definition of a
finite bound.
\end{hypothesis}

Hypothesis~\ref{hyp:absorption} implies Hypothesis~\ref{hyp:critical}, with
\[
 M(\nu,u_0,H)=
 \bigl(\norm{u_0}_3^3+3A(\nu,u_0,H)\bigr)^{1/3},
\]
by \eqref{eq:pressure-consequence}.  This implication is elementary; proving
the absorption estimate remains a conceptual open gap, refined here to
Hypothesis~\ref{hyp:highpressure} after the proved low-frequency estimate.

Small initial $L^3$ norm is covered by critical small-data theory
\cite{Kato1984}; the arbitrary-data estimate \eqref{eq:missing} is unknown.
Finite-horizon dependence is enough: if $T_*<\infty$, choose any finite
$H>T_*$ and obtain the terminal bound required by
Theorem~\ref{thm:continuation}.
% END RETAINED VERBATIM.

\begin{theorem}[Conditional Clay alternative A]\label{thm:conditional}
If Hypothesis~\ref{hyp:critical} holds, then
Theorem~\ref{def:target} holds.
\end{theorem}

\begin{proof}
\emph{Step 0: the data class.}  Let $\nu>0$ and let $u_0$ be a Clay datum,
i.e.\ a smooth divergence-free field satisfying Fefferman's decay condition
(4), $|\partial_x^\alpha u_0(x)|\leq C_{\alpha K}(1+|x|)^{-K}$ on $\R^3$ for
all multi-indices $\alpha$ and all $K$ \cite[p.~2]{Fefferman2000}.  This is
exactly $u_0\in\mathcal S(\R^3)^3$, where the Schwartz class is defined by
the finiteness of $\sup_x(1+|x|)^K|\partial^\alpha f(x)|$ for all $\alpha$
and all integers $K\geq0$ (the definition of Schwartz data used in
\cite[Definition~1.1]{Tao2013}).  Indeed, if (4) holds then
$\sup_x(1+|x|)^K|\partial^\alpha u_0(x)|\leq C_{\alpha K}<\infty$ for every
integer $K\geq0$; conversely, if $u_0\in\mathcal S$ then for every $\alpha$
and every real $K\geq0$, with $\lceil K\rceil$ the least integer $\geq K$,
$|\partial^\alpha u_0(x)|\leq(1+|x|)^{-\lceil K\rceil}
\sup_y(1+|y|)^{\lceil K\rceil}|\partial^\alpha u_0(y)|
\leq C_{\alpha K}(1+|x|)^{-K}$ with
$C_{\alpha K}:=\sup_y(1+|y|)^{\lceil K\rceil}|\partial^\alpha u_0(y)|<\infty$,
because $(1+|x|)^{-\lceil K\rceil}\leq(1+|x|)^{-K}$.  Let $u$, $p$ be the
maximal classical solution and its normalised pressure on $[0,T_*)$ from
Proposition~\ref{prop:localtheory}.

\emph{Step 1: $T_*=\infty$.}  Suppose $T_*<\infty$.  Choose $H=T_*+1$, so
$\min\{H,T_*\}=T_*$.  Hypothesis~\ref{hyp:critical} gives
$\sup_{0<t<T_*}\norm{u(t)}_3\leq M(\nu,u_0,H)<\infty$, which is
\eqref{eq:endpoint}; Theorem~\ref{thm:continuation} then yields $T_*=\infty$,
a contradiction.  Hence $T_*=\infty$.

\emph{Step 2: smoothness on $\R^3\times[0,\infty)$ (Fefferman's (6)).}  Since
$T_*=\infty$, Lemma~\ref{lem:global-smooth} of the local-theory section (the
global form of (R2)) gives $u,p\in C^\infty(\R^3\times[0,\infty))$ in the
sense of \cite[(6)]{Fefferman2000}: all partial derivatives
$\partial_t^j\partial_x^\alpha u$, $\partial_t^j\partial_x^\alpha p$ exist,
one-sided in $t$ at $t=0$, and are continuous on $\R^3\times[0,\infty)$.
(Explicitly: for $(x,t)\in\R^3\times[0,\infty)$ pick any $T>t$; since
$T<T_*=\infty$, (R2) gives $u,p\in C^\infty([0,T]\times\R^3)$, and the
derivatives computed on $[0,T]\times\R^3$ and on $[0,T']\times\R^3$, $T<T'$,
are derivatives of one and the same function.)

\emph{Step 3: the equations (1), (2), (3) with $f\equiv0$.}  By (R2),
$\partial_tu+(u\cdot\nabla)u+\nabla p=\nu\Delta u$ and $\nabla\cdot u=0$ hold
pointwise on $[0,T]\times\R^3$ for every $T$, hence on $\R^3\times[0,\infty)$;
by (R3), $u(x,0)=u_0(x)$.  These are Fefferman's (1) (with $f_i\equiv0$), (2),
and (3).  Alternative (A) of \cite{Fefferman2000} fixes $f\equiv0$, so his
condition (5) on the force is vacuous.

\emph{Step 4: bounded energy (Fefferman's (7)).}  For every $t\geq0$ pick
$T>t$; Proposition~\ref{prop:energy} on $[0,T]$ gives
$\int_{\R^3}|u(x,t)|^2\,dx\leq\norm{u_0}_2^2$.  Hence
$\int_{\R^3}|u(x,t)|^2\,dx<C$ for all $t\geq0$ with the single constant
$C=\norm{u_0}_2^2+1$, and $\sup_{t\geq0}\int|u(x,t)|^2dx<\infty$.

\emph{Step 5: the pressure.}  The pressure in Steps 2--3 is
$p=R_iR_j(u_iu_j)$, which by the convention paragraph equals
$-\Delta^{-1}\partial_i\partial_j(u_iu_j)$, Tao's normalised pressure; it is
the pressure of (R2) and is smooth on $\R^3\times[0,\infty)$ by Step~2.
Fefferman's statement requires some smooth $p$; this one qualifies, and no
freedom ``up to a function of time'' remains to be fixed.

Steps 2--5 verify (1), (2), (3), (6), (7) of \cite{Fefferman2000} for the
data class (4) with $f\equiv0$, which is Theorem~\ref{def:target}.
\end{proof}

\begin{remark}[The maximal-$L^3$ route of Gallagher, Koch, and Planchon]
\label{rem:gkp}
Theorem~4 of \cite{GKP2013} (arXiv:1012.0145, \S``Serrin's endpoint
regularity criterion''; \emph{Math.\ Ann.}\ 355 (2013), \S3.1; unit viscosity)
states, verbatim: ``For any $u_0\in L^3(\R^3)$,
$\sup_{t\in[0,T^*(u_0))}\norm{NS(u_0)(t)}_{L^3(\R^3)}<\infty\Longrightarrow T^*(u_0)=+\infty$,''
where $NS(u_0)$ is the strong (Duhamel) solution with datum $u_0$ in the
class $E_{p,q}(T)$ and $T^*(u_0)$ its maximal time; the remark following it
confirms that the left side is $NS(u_0)\in L^\infty((0,T^*);L^3)$,
``or in the notation of [ESS], $NS(u_0)\in L_{3,\infty}(0,T^*)$.''  With
$a=\nu^{-1}u_0$ this corroborates the \emph{statement} of
Theorem~\ref{thm:continuation} for the maximal $L^3$ branch $NS(a)$: the
same kind of $L^3$ bound forces that branch to be global.  We do not use it,
because turning the corroboration into a proof for the classical branch $v$
of Lemma~\ref{lem:nu-normalisation} requires three further statements that
Theorem~4 does not contain: membership of $v$ in $E_{p,q}(T)$ together with
the Leray-projected Duhamel identity; a uniqueness theorem identifying $v$
with $NS(a)$ on every $[0,T]$, $T<S_*$; and, in the case $T^*(a)>S_*$, a
regularity theorem for $NS(a)$ beyond $S_*$ contradicting (R4).  The
uniqueness theorem usually invoked for the second point (Furioli,
Lemari\'e-Rieusset, and Terraneo, \emph{Rev.\ Mat.\ Iberoam.}\ 16 (2000)
605--667) was not inspected in its primary text.  The route through
Lemma~\ref{lem:leray-hopf} avoids all three: its hypotheses are checked line
by line against the printed definition of the Leray--Hopf class, and the
passage from $L^5(Q_{S_*})$ back to the classical branch is the
manuscript-owned Lemma~\ref{lem:serrin-enstrophy}, the case $s=l=5$ of the
Ladyzhenskaya--Prodi--Serrin condition $\frac3s+\frac2l=1$ of
\cite[Theorem~1.2, p.~213]{ESS2003}, proved here directly because an explicit
$H^1$ bound for the classical branch is needed rather than a smoothness
statement for weak solutions.  Theorem~\ref{thm:continuation} concerns only
the branch selected by Proposition~\ref{prop:localtheory}.  No converse from
an arbitrary smooth finite-energy solution class to the selected strong
branch is asserted here.
\end{remark}
```

---

## 3. External facts used

| # | fact, as used | source, exact location | status |
|---|---|---|---|
| E1 | ESS definitions: $\dot C_0^\infty$, $\mathring J$, $\mathring J{}^1_2$, $Q_T$; Leray–Hopf weak solution as a map on $\overline{Q_T}$ via (1.3)–(1.7) (text reproduced verbatim in the block); $\dot C_0^\infty(Q_T)$ is **not** defined there — the block marks its reading as its own | Escauriaza–Seregin–Šverák, Russian Math. Surveys 58:2 (2003), **p. 212** | **[DI]** (page image read in rounds 1–2; independently confirmed verbatim by the audit) |
| E2 | ESS mixed norm $\|f\|_{s,l,Q_T}$, $L_{s,l}(Q_T)$, condition (1.13) $v\in L_{3,\infty}(Q_T)$; Theorem 1.2 (LPS condition $3/s+2/l=1$, $s\in]3,+\infty]$) | same, **p. 213** | **[DI]** |
| E3 | ESS Theorem 1.3 (verbatim) and the prose classical form before it; Theorem 1.1 assumes $a\in\mathring J$ (their (1.8)) | same, **p. 214** (Thm 1.3), **p. 212** (Thm 1.1/(1.8)) | **[DI]** |
| E4 | ESS equation (1.1)–(1.2), unit viscosity | same, **p. 211** | **[DI]** |
| E5 | Tao's normalised pressure $p=-\Delta^{-1}\partial_i\partial_j(u_iu_j)$, Fourier convention, $\Delta^{-1}$ symbol; Tao's definition of Schwartz data by $\sup_x(1+|x|)^k|\nabla^\alpha u_0|<\infty$ | Tao, APDE 6 (2013), eq. (9), eq. (14), Definition 1.1 (cp01-literature-statements §1.1, §1.4, §7.3) | **[DI]** (per cp01 record; identity $R_iR_j=-\Delta^{-1}\partial_i\partial_j$ re-derived in the block) |
| E6 | GKP Theorem 4 (verbatim) and the $L_{3,\infty}$ remark; $NS(u_0)$, $E_{p,q}(T)$, $T^*(u_0)$ | Gallagher–Koch–Planchon, arXiv:1012.0145 §"Serrin's endpoint regularity criterion" = Math. Ann. 355 (2013) §3.1 (cp01-literature-statements §2) | **[DI]** (per cp01 record) — Remark `rem:gkp` only, not load-bearing |
| E7 | Fefferman (A): data condition (4), force (5) and $f\equiv0$, equations (1)–(3), requirements (6), (7) with a single constant | Clay official statement, PDF pp. 1–2 (cp01-literature-statements §5) | **[DI]** (per cp01 record) |
| E8 | (F1) Fourier package: $\mathcal F$ bijective on $\mathcal S$; Plancherel on $L^1\cap L^2$ with unitary extension; $L^1$-inverse integral equals $\mathcal F^{-1}$ a.e. on $L^1\cap L^2$; $(\partial_jf)^\wedge=2\pi i\xi_j\hat f$ on $H^1$ | Stein–Weiss, *Introduction to Fourier Analysis on Euclidean Spaces*, Princeton 1971, Ch. I §§1–2 | **[MO]** (theorem numbers not pinned) |
| E9 | (F2) density of $C_c^\infty$ in $L^r$, $1\le r<\infty$ (complex-valued) | Lieb–Loss, *Analysis*, 2nd ed., AMS GSM 14, 2001: **Theorem 2.16, p. 64** and **Lemma 2.19, p. 69** | **[DI]** (pp. 64–70 read as page images in round 1; TOC entries re-confirmed this round) |
| E10 | (F3) sharp Sobolev constant $C_S=S_3^{-1/2}$, $S_3=\tfrac34(2\pi^2)^{2/3}=3(\pi/2)^{4/3}$, inequality stated for the class $D^1(\R^3)$ | Lieb–Loss, *Analysis*, 2nd ed., **Theorem 8.3, p. 202**, class $D^1$ defined in **§8.2, p. 201** | **[MO]** for the statement text and constant (TOC confirms section titles and pages; AMS endmatter 403; the hosted copy is front matter only). **Not load-bearing after the repair**: only the existence of some $C_S$ valid on $C_c^\infty$ is used, and the block takes $C_S$ to be the constant of the energy lane's `def:sobolev-constant`; the numerical value affects $C_*$ only |
| E10′ | (F3) existence of $C_S$ with $\|g\|_6\le C_S\|\nabla g\|_2$ for real $g\in C^1_c(\R^3)$ | Nirenberg, Ann. Scuola Norm. Sup. Pisa 13 (1959), p. 125, inequality (2.2), case $n=3$, $j=0$, $m=1$, $r=q=2$, $a=1$, $p=6$ — as pinned by the energy lane in `def:sobolev-constant`; also Mathlib `MeasureTheory.eLpNorm_le_eLpNorm_fderiv_of_eq` (cp01-literature-statements S7) | **[MO]** for this lane (cited through the energy lane, whose record claims the page; not re-read here) |
| E11 | (F4) orthogonal projection onto a closed subspace; Riesz representation; $(M^\perp)^\perp=M$ derived in the block from 4.11 | Rudin, *Real and Complex Analysis*, 3rd ed., McGraw–Hill 1987: **Theorem 4.11, p. 80**, **Theorem 4.12, p. 81** | **[DI]** (round 1, OCR text; confirmed verbatim by the audit from page images) |
| E12 | (F5) Tonelli–Fubini, MCT, Fatou, DCT, differentiation under the integral, polar coordinates | Folland, *Real Analysis*, 2nd ed., Wiley 1999, Thms 2.14, 2.18, 2.24, 2.27, 2.37, 2.49; Fatou also Lieb–Loss Theorem 1.7, **p. 18** | **[MO]** for Folland's numbers (secondary corroboration only); Lieb–Loss 1.7/p. 18 confirmed at TOC level this round, text not read |
| E13 | (F6) Hölder; Young $ab\le a^r/r+b^{r'}/r'$ | elementary (cp01-literature-statements S10, S11: Mathlib-present) | [DI] per cp01 record |
| E14 | Existence of a cutoff $\chi\in C_c^\infty$, $\chi=1$ on $B_1$, $\chi=0$ off $B_2$, $0\le\chi\le1$ | standard (mollified indicator of $B_{3/2}$ with a mollifier of radius $1/4$) | — |
| — | Galdi, *An Introduction to the Mathematical Theory of the Navier–Stokes Equations*, 2nd ed. 2011, Ch. III (characterisation of $\mathring J$, $\mathring J{}^1_2$ on $\R^n$) | Springer front matter behind IdP login; theorem number **not verified**; **not cited in the block** — Lemma `lem:solenoidal-density` is proved in full instead | [MO] / unused |

Assumed manuscript results (not external): Proposition `prop:localtheory`
with clauses (iii)–(vi) and Corollary `cor:Lq` (cited as (R1)–(R4)),
Lemma `lem:nu-scaling`, Lemma `lem:global-smooth`, Lemma `lem:sup-esssup`
(local-theory lane); Proposition `prop:energy` and Definition
`def:sobolev-constant` (energy lane); `hyp:critical` (statement only),
`def:target` (statement only).

---

## 4. Obligations not discharged (exactly stated)

1. **C-3, the smoothness lemma itself.** The block *cites*
   Lemma `lem:global-smooth` and clause (R2) of `prop:localtheory`. The
   proof of that clause from Tao 5.4(iv) is owned by the local-theory lane
   and is not written here.
2. **S-1, source half.** The compactly supported Sobolev inequality (F3) is
   taken from the energy lane's `def:sobolev-constant` (Nirenberg 1959
   p. 125, (2.2); Mathlib), which this lane did not re-read; the sharp value
   from Lieb–Loss Theorem 8.3 remains [MO] (statement text and constant not
   read in the primary text; TOC pages confirmed). The $H^1$-extension half
   of S-1 is discharged by `lem:sobolev-h1`. The $\nu$-power in
   `eq:serrin-bound` is independent of the source; $C_*$ changes
   numerically if a non-sharp $C_S$ is fixed.
3. **Galdi citation.** Not verified (login wall); no theorem number is
   asserted. Lemma `lem:solenoidal-density` (proved in full) replaces it and
   is stated only for fields in $\bigcap_kH^k$, which is all the branch
   needs; the general $H^1$ statement is not claimed.
4. **[MO] textbook facts.** E8 (Stein–Weiss Ch. I theorem numbers), E12
   (Folland numbers), E10/E10′ as above. E9 and E11 are [DI].
5. **Nothing about `prop:energy`, `prop:pressure`, `prop:lowpressure`,
   `sec:quotient`, or the existential-equivalence paragraph (X-1)** is
   touched; the retained paragraphs after `hyp:critical` still cite
   `eq:pressure-consequence`, whose integrated form is the pressure lane's
   P-3.

(The round-1 item "uniqueness of the normalised branch as the branch for
$(a,1)$ is not asserted" is dropped: `prop:localtheory`(vi) asserts exactly
that, the block now records it in Lemma `lem:nu-normalisation`, and nothing
in this section uses it.)

---

## 5. Changes against the round-1 audit

| audit item | change in this version |
|---|---|
| §3 / §5 **first bad bridge** | (F3) restated for compactly supported functions only, with $C_S$ identified with the energy lane's `def:sobolev-constant`; the inclusion "$D^1\supset H^1$" is no longer asserted; new Lemma `lem:sobolev-h1` (smooth representative via the $L^1$-Fourier bound, truncation by $\chi_R$, Fatou) placed before the Serrin subsection; Step 2 of `lem:serrin-enstrophy` cites it. Constant path and $\nu^{-4}$ unchanged |
| §7 trim (Theorem 1.1 sentence) | kept, with the reason stated: Theorem 1.3 does not restate (1.8), so the hypotheses under which it is applied are at least as strong as its neighbours' |
| §10.1 CP01 record correction | reported in §1 for the literature lane (not this lane's file) |
| §10.2 $\dot C_0^\infty(Q_T)$ undefined in ESS | the block now says so and marks the reading as its own, noting that the verification is strongest for the widest class |
| §10.3 Lebesgue representative of $v_*$ | added in the statement and Step 1 of `lem:leray-hopf` |
| §10.4 intervals in (vi) | $[0,S]$, $[0,T]$, hence $[0,S_*)$, $[0,T_*)$ |
| §10.5 lemma title | "Smooth solenoidal fields lie in $\mathring J{}^1_2$", restriction stated in the lemma |
| §10.6 `premise:local` sentence | flagged in §1; the local-theory lane's §2.1 paragraph deletes it |
| §10.7 backward-uniqueness sentence | reinstated in `rem:ess-norm` |
| §10.8 Proof boundary | suggested sentence given in §1 for the integrator |
| §10.9 `thm:ess` presentation | `\begin{theorem}[…, Theorem~1.3 of \cite{ESS2003}; quoted, not proved here]` |
| §10.10 redundant $\operatorname{Re}$ | removed; reality of the integral explained once in (F1)(b) |
| §10.11 $H^1$ norm convention | exact identity stated in the conventions paragraph; convention-independence of (R4) and of the conclusion noted in Step 4 |
| §10.12 Fefferman (5) | "alternative (A) fixes $f\equiv0$, so (5) is vacuous" |
| §10.13 Schwartz equivalence | both directions written out (Step 0 of `thm:conditional`), with Tao's definition of Schwartz data as the reference definition |
| §10.14 `rem:gkp` wording | "corroborates the *statement* of Theorem `thm:continuation` for the maximal $L^3$ branch $NS(a)$" |
| §10.15 preamble | unchanged requirement (`lemma` only); noted that the local-theory lane's preamble lines subsume it |
| §10.16 labels | all D4 labels retained; new label `eq:serrin-enstrophy-identity` replaces the colliding `eq:enstrophy-identity` |
| §10.17 (R1)–(R4) alignment | explicit map to `prop:localtheory`(iii),(iv),(v) and `cor:Lq` in the block's first paragraph and in §1 |
| §10.18 open item 4 | dropped from §4; `prop:localtheory`(vi) recorded in `lem:nu-normalisation` |
| §10.19 overlap with `lem:nu-scaling` | (i)–(iv) now cite `lem:nu-scaling`(a)–(d); (v),(vi) remain the new content; integrator note in §1 |
| §10.20 `eq:nu-normalization` vs `eq:nu-map` | both kept; the block states they are the same map (argument order differs); `eq:nu-normalization` is the `main.tex` label |
| additional (not in the audit) | Step 2 of `thm:conditional` cites `lem:global-smooth`; Step 4 of `lem:serrin-enstrophy` and the proof of `lem:l3-to-l5` say "continuous on $[0,T']$ for every $T'<T$, hence on $[0,T)$" instead of the loose "on $[0,T')$"; the enstrophy-identity label renamed; `lem:duality` collision between two other lanes reported |

---

## 6. Frontier record

**MODE / RESULT.** PROOF WRITING, repair round 2; result: complete
replacement text for the continuation section discharging C-0, C-2 (by the
(D3) Leray–Hopf route), the assembly half of C-3, and the $H^1$-extension
half of S-1, with the audit's single bad bridge repaired by a proved lemma
and all twenty editorial items resolved or routed.

**CLAIM AND SCOPE.** For the unforced Navier–Stokes system on $\R^3$ with
arbitrary $\nu>0$ and divergence-free Schwartz data, on the classical branch
of `prop:localtheory` with package (R) and given `prop:energy` and the
existence of a Sobolev constant on $C_c^1(\R^3)$ (`def:sobolev-constant`):
(a) the $\nu$-normalised branch is a Leray–Hopf weak solution in the exact
printed sense of ESS (1.3)–(1.7) on every finite $Q_T$, $T\le S_*$,
including the endpoint $T=S_*$ via a weak limit; (b) $T_*<\infty$ and
$\sup_{t<T_*}\|u(t)\|_3<\infty$ imply $u\in L^5(\R^3\times(0,T_*))$ through
ESS Theorem 1.3; (c) every real $f\in\bigcap_kH^k(\R^3)$ satisfies
$\|f\|_6\le C_S\|\nabla f\|_2$; (d) $\int_0^T\|u\|_5^5<\infty$ implies
$\sup_{t<T}\|\nabla u(t)\|_2\le\|\nabla u_0\|_2
\exp(\tfrac{256}{3125}C_S^3\nu^{-4}\int_0^T\|u\|_5^5)$; (e) hence
`thm:continuation` in the shape "$T_*<\infty\Rightarrow\sup_{t<T_*}\|u\|_3=\infty$",
and `thm:conditional` with all Fefferman clauses checked. Scope is exactly
the Schwartz-data classical branch; no statement about other solution
classes, and no converse from arbitrary smooth finite-energy solutions.

**EVIDENCE.** Direct inspection of ESS pp. 211–214 (page images, two
rounds; independently confirmed by the audit): the Leray–Hopf class on
$\overline{Q_T}$, the sign convention of (1.5), the mixed norm, Theorem 1.3.
Lieb–Loss pp. 64–70 (round 1) and TOC pp. ix–xv (this round); Rudin
pp. 80–82. Independent rederivation (this lane, confirmed number by number
by the audit) of: the $\nu$-normalisation with the transported energy
identity and the $\nu^{-4}$; the Biot–Savart symbol and
$2\pi i\,\xi\times\hat A=\hat v$; the $L^1$ bounds with
$\int(1+|\xi|^2)^{-2}=\pi^2$ and $\int_{|\xi|<1}|\xi|^{-2}=4\pi$;
$\|\nabla A\|_2\le\|v\|_2$; Hardy with constant 2; every cutoff error in
$W^1_2$; the (1.5) test identity term by term; the enstrophy identity with
$\langle\Delta u,\nabla p\rangle=0$; the exponents
$1/5+3/10+1/2=1$, $\theta=2/5$, $\|\nabla^2u\|_2=\|\Delta u\|_2$; Young at
$(5/4,5)$ giving $C_*=\tfrac{256}{3125}C_S^3$; the Gronwall halving. New in
this round: the repair lemma's three steps (the $L^1$-Fourier bound
$\int|\xi|^m|\hat f|\le\pi\|f\|_{H^{m+2}}$ giving a $C^\infty$
representative with $\nabla F=\nabla f$ a.e.; the product-rule bound
$\|\nabla(\chi_RF)\|_2\le\|\nabla f\|_2+R^{-1}\|\nabla\chi\|_\infty\|f\|_2$;
Fatou on $|\chi_RF|^6$), and the two-line Schwartz equivalence via
$(1+|x|)^{-\lceil K\rceil}\le(1+|x|)^{-K}$.

**FIRST GAP (for the CP1 paper-proof goal).** None inside this section's
own argument at the level of mathematics after the repair. The first
*documentation* gap is the [MO] status of the compactly supported Sobolev
inequality's sources (E10′ Nirenberg via the energy lane; E10 Lieb–Loss 8.3
for the sharp value), behind it E8 (Stein–Weiss) and E12 (Folland). The
first *structural* dependency is Lemma `lem:global-smooth` / clause (R2) of
`prop:localtheory` (the local-theory lane's C-3 lemma), cited but not proved
here.

**SURVIVING CONDITIONAL SUFFIX.** Given `prop:localtheory` with (R1)–(R4),
`prop:energy`, and `def:sobolev-constant`: `hyp:critical` $\Rightarrow$
(Thm `thm:continuation`, via Lemmas `lem:nu-normalisation`, `lem:hardy`,
`lem:solenoidal-density`, `lem:leray-hopf`, ESS Theorem 1.3, `lem:l3-to-l5`,
`lem:sobolev-h1`, `lem:serrin-enstrophy`) $T_*=\infty$ $\Rightarrow$
(`lem:global-smooth`, (R3), `prop:energy`) Clay alternative (A) exactly as in
`def:target`. One imported literature theorem (ESS 1.3), its hypothesis class
verified in full against its printed definition; no imported uniqueness
theorem.

**NON-CLAIMS.** No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or
NS-R3 result is asserted or approached; `hyp:critical` remains an unproved
hypothesis and the retained paragraph says so. GKP Theorem 4 is corroboration
only. Galdi's theorem number is not asserted. Lieb–Loss Theorem 8.3,
Nirenberg 1959, Stein–Weiss Ch. I, and Folland 2.14–2.49 were not read in
their primary texts by this lane and are [MO]; Lieb–Loss 2.16/2.19 (and the
TOC) and Rudin 4.11/4.12 were. No converse from arbitrary smooth
finite-energy solutions to the selected branch is asserted.

**NEXT DISTINCT ACTION.** Integrator: add `\newtheorem{lemma}[theorem]{Lemma}`
(shared with the local-theory lane), splice the block in place of Section 5,
resolve the overlaps listed in §1 (`lem:nu-normalisation`/`lem:nu-scaling`,
`lem:sobolev-h1`/`lem:sobolev`, `eq:nu-normalization`/`eq:nu-map`), add the
Proof-boundary sentence, use the local-theory lane's `premise:local`
paragraph, and run the structural verifier. Audit round 2 need only
re-check `lem:sobolev-h1` and the clause alignment. Literature lane: read
Lieb–Loss pp. 201–204 and Nirenberg p. 125 to upgrade E10/E10′ to [DI], and
correct `cp01-literature-statements` §3.1 ($Q_T\to\overline{Q_T}$).
