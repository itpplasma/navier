# CP02-6: the cubic gradient quotient, first half (Q-0 to Q-7), complete proofs

MODE / RESULT: **INTEGRATE (paper text).**  This note delivers the first
half of the rewritten manuscript section `sec:quotient`: definition of the
gradient space and of the quotient functional, existence and uniqueness of
the minimizing representative, the Euler-Lagrange condition, the Leray
projection on `L^3` with a complete proof that it fixes every
distributionally solenoidal `L^3` field, coercivity, amplitude homogeneity
and critical scaling invariance, heat monotonicity, and the Frechet
derivative with an explicit `O(‖h‖_3^{3/2})` remainder.  Every proof is
written out.  Nothing here proves `eq:quotient-gap`; HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL and NS-R3 remain open and are not asserted.

Date: 2026-09-05.  Lane CP02-6.  Inputs read in full: `navier-paper/main.tex`
(HEAD `1ad73c2`), `research/evidence/cp01-manuscript-obligations.md`,
`research/evidence/cp01-literature-statements.md`,
`research/evidence/cp01-quotient-section-structure.md` (base text, §4),
`research/evidence/hf17-quotient-functional.md`,
`research/evidence/hf17-review-quotient-functional.md`.  Controller
decisions D1-D5 are followed; the conventions of D1 (Fourier transform
`f̂(ξ)=∫e^{-2πi x·ξ}f`, Riesz symbol `-iξ_j/|ξ|`, real `L^3(R^3;R^3)`) are
restated at the top of the section text.

## 1. Obligations discharged

| ID | Obligation (cp01-manuscript-obligations.md §1.14) | Where | Status |
| --- | --- | --- | --- |
| Q-0 | Definition of `G_3` and `Q`; `G_3` closed linear subspace; real `L^3(R^3;R^3)` | `def:quotient` | proved |
| Q-1 | Existence of a minimizer by reflexivity of `L^3`, weak sequential compactness, Mazur, weak lower semicontinuity, boundedness of minimizing sequences | `lem:quotient-minimizer`(a) with (F1), (F2) | proved; sources verified [DI] |
| Q-2 | Uniqueness by strict convexity of `z ↦ |z|^3` on `R^3` (two-line pointwise proof; Clarkson not used) | `lem:cubic-pointwise` (eq:cp-strict), `lem:quotient-minimizer`(b) | proved |
| Q-3 | Euler-Lagrange condition by differentiation under the integral with the displayed dominant `(|w|+|g|)^2|g| ∈ L^1` | `lem:quotient-minimizer`(c) | proved |
| Q-4 | Leray projection: `L^2` definition, `L^3` boundedness imported (Tao p. 38 [DI]; Stein [MO]), `P∇φ=0`, `Pq=0` on `G_3`, `Pu=u` for every solenoidal `u ∈ L^3` (duality plus cutoff, every step written), coercivity (8) with `‖q‖_3 ≤ (1+C_P)‖w‖_3` | `lem:leray`, `lem:quotient-coercive` | proved modulo the one import (F5) |
| Q-5 | Amplitude homogeneity `Q(au)=|a|^3Q(u)`, scaling invariance `Q(S_λu)=Q(u)` with the change of variables, translation invariance | `lem:quotient-scaling` | proved |
| Q-6 | Heat semigroup as Gaussian convolution; `L^3` contraction with constant 1 (proved from Holder/Tonelli, Young cited); `G_s∇φ=∇G_sφ`; `G_sφ` Schwartz; `∇ψ ∈ G_3` for Schwartz `ψ` by cutoff; extension to the closure; `Q(G_su) ≤ F(G_sw) ≤ Q(u)` | `lem:gradient-closure`, `lem:quotient-heat` | proved |
| Q-7 | Frechet derivative: pointwise uniform monotonicity with the explicit constant `1/2` (identity displayed), Lipschitz bound with constant 1, cancellation, quotient contraction, strong convergence `w' → w` with `‖w'-w‖_3 ≤ 2(‖w‖_3+‖h‖_3)^{1/2}‖h‖_3^{1/2}`, pointwise Taylor bound, remainder `≤ 6(‖w‖_3+‖h‖_3)^{3/2}‖h‖_3^{3/2}` | `lem:cubic-pointwise`, `lem:cubic-frechet`, `lem:quotient-stability`, `prop:quotient-derivative` | proved |

Scope statement (requested by the lane brief): every result of this half
holds for **every** `u ∈ L^3(R^3;R^3)` except the lower coercivity bound,
the identities `Pw=u`, `q=(I-P)w`, and the bound `‖q‖_3 ≤ (1+C_P)‖w‖_3`,
which hold exactly when `u` is solenoidal (`lem:leray`(d),
`lem:quotient-coercive`).  This is also recorded as `rem:quotient-scope`
in the text.

Preamble additions required in `main.tex` (the current preamble defines
`theorem`, `proposition`, `hypothesis`, `remark` only):

```latex
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
```

No new macros are used (`\mathcal Q`, `\mathcal G_3`, `\mathbb P` are written
out; `\norm` and `\R` already exist).  Bibliography entries to add to
`references.bib`:

```bibtex
@book{Brezis2011,
  author    = {Ha{\"i}m Brezis},
  title     = {Functional Analysis, {S}obolev Spaces and Partial Differential Equations},
  series    = {Universitext},
  publisher = {Springer},
  address   = {New York},
  year      = {2011},
  doi       = {10.1007/978-0-387-70914-7}
}
@book{Stein1970,
  author    = {Elias M. Stein},
  title     = {Singular Integrals and Differentiability Properties of Functions},
  series    = {Princeton Mathematical Series},
  volume    = {30},
  publisher = {Princeton University Press},
  year      = {1970}
}
@book{Grafakos2014,
  author    = {Loukas Grafakos},
  title     = {Classical {F}ourier Analysis},
  edition   = {3},
  series    = {Graduate Texts in Mathematics},
  volume    = {249},
  publisher = {Springer},
  year      = {2014},
  doi       = {10.1007/978-1-4939-1194-3}
}
```

## 2. Replacement text: first half of `sec:quotient`

The block below replaces the current `sec:quotient` from `\section` up to
(not including) the paragraph beginning "On compact classical intervals".
The second half (Q-8 to Q-18: classical trajectory class, pressure
annihilation, heat generator, inner variation, evolution identity,
low-strain bound, `hyp:highstrain`, conditional consequence) is delivered
by lane CP02-7 and starts with `\subsection{The classical trajectory
class}`; it may use every label defined here.  `eq:quotient-evolution` and
`eq:quotient-gap` are defined in that half.

```latex
\section{A quotient functional and its remaining strain estimate}
\label{sec:quotient}

A separate route avoids the explicit pressure work of Section~4.  It rests
on a functional on $L^3(\R^3;\R^3)$ whose derivative annihilates every
gradient.  This section records an independently audited analytic
mechanism, not a regularity theorem.  Its first part,
Definition~\ref{def:quotient} through
Proposition~\ref{prop:quotient-derivative}, concerns the functional alone:
it uses no property of Navier--Stokes solutions, and every statement says
whether it holds for all of $L^3$ or requires a divergence-free field
(Remark~\ref{rem:quotient-scope}).  No estimate for the remaining strain
term is proved anywhere in this section.

\subsection{Conventions and imported facts}
\label{subsec:quotient-conventions}

All functions and fields in this section are real-valued unless a complex
Fourier transform is displayed.  For $z\in\R^3$, $|z|$ is the Euclidean
norm.  $L^r$ stands for $L^r(\R^3)$ or $L^r(\R^3;\R^3)$ with
$\norm f_r=(\int_{\R^3}|f|^r\,dx)^{1/r}$, and
$\langle f,g\rangle=\int_{\R^3}f\cdot g\,dx$ whenever $f\cdot g\in L^1$; by
H\"older's inequality this is the case for $f\in L^{3/2}$, $g\in L^3$,
with $|\langle f,g\rangle|\le\norm f_{3/2}\norm g_3$.  Fix
$\chi\in C_c^\infty(\R^3)$ with $0\le\chi\le1$, $\chi=1$ on
$\{|x|\le1\}$, $\chi=0$ on $\{|x|\ge2\}$, and set $\chi_R(x)=\chi(x/R)$
for $R\ge1$, so that $\norm{\nabla\chi_R}_\infty=R^{-1}\norm{\nabla\chi}_\infty$
and $\norm{\nabla\chi_R}_6=R^{-1/2}\norm{\nabla\chi}_6$.  Fix a mollifier
$\rho\in C_c^\infty(\R^3)$ with $\rho\ge0$, $\int\rho=1$,
$\operatorname{supp}\rho\subset\{|x|\le1\}$, and set
$\rho_\varepsilon(x)=\varepsilon^{-3}\rho(x/\varepsilon)$.  A field
$u\in L^1_{\rm loc}(\R^3;\R^3)$ is \emph{solenoidal} if
$\int_{\R^3}u\cdot\nabla\phi\,dx=0$ for every $\phi\in C_c^\infty(\R^3)$,
that is, if $\operatorname{div}u=0$ in the sense of distributions.  The
Fourier transform is $\hat f(\xi)=\int_{\R^3}e^{-2\pi ix\cdot\xi}f(x)\,dx$
for $f\in L^1(\R^3;\mathbb C)$, taken componentwise for fields; this is
the convention of \cite{Tao2013}, under which the Riesz transforms of
Section~4 have symbols $-i\xi_j/|\xi|$.  $\mathcal S(\R^3)$ is the
Schwartz space.

The following facts are imported; each is stated in the form in which it
is used, with the source in which it was checked.
\begin{itemize}
\item[(F1)] \emph{Reflexivity and weak sequential compactness.}  For a
 $\sigma$-finite measure space and $1<p<\infty$, $L^p$ is reflexive
 \cite[Thm.~4.10]{Brezis2011}; every bounded sequence in a reflexive
 Banach space has a weakly convergent subsequence
 \cite[Thm.~3.18]{Brezis2011}.
\item[(F2)] \emph{Weak closedness and lower semicontinuity.}  In a Banach
 space a convex set is weakly closed if and only if it is norm closed
 \cite[Thm.~3.7]{Brezis2011}; if $x_n\rightharpoonup x$ weakly then
 $\norm x\le\liminf_n\norm{x_n}$ \cite[Prop.~3.5(iii)]{Brezis2011}.
\item[(F3)] \emph{Convolution.}  For $k\in L^1(\R^3)$ and
 $g\in L^p(\R^3)$, $1\le p\le\infty$, the integral
 $(k*g)(x)=\int_{\R^3}k(x-y)g(y)\,dy$ converges absolutely for a.e.\ $x$
 and $\norm{k*g}_p\le\norm k_1\norm g_p$ \cite[Thm.~4.15]{Brezis2011}.
 For $k\in C_c^\infty(\R^3)$ and $g\in L^1_{\rm loc}(\R^3)$, $k*g\in
 C^\infty(\R^3)$ with $\partial^\alpha(k*g)=(\partial^\alpha k)*g$
 \cite[Prop.~4.20]{Brezis2011}, and $k*g$ has compact support if $g$ does
 \cite[Prop.~4.18]{Brezis2011}.  For $g\in L^p(\R^3)$, $1\le p<\infty$,
 $\rho_\varepsilon*g\to g$ in $L^p$ as $\varepsilon\downarrow0$
 \cite[Thm.~4.22]{Brezis2011}, and $C_c(\R^3)$ is dense in $L^p(\R^3)$
 \cite[Thm.~4.12]{Brezis2011}.
\item[(F4)] \emph{Plancherel.}  The map $f\mapsto\hat f$ on
 $L^1\cap L^2(\R^3;\mathbb C)$ extends uniquely to a unitary operator
 $\mathcal F$ of $L^2(\R^3;\mathbb C)$, whose inverse extends
 $g\mapsto\check g$, $\check g(x)=\int_{\R^3}e^{2\pi ix\cdot\xi}g(\xi)\,d\xi$,
 from $L^1\cap L^2$; and $\int f\,\overline g\,dx=\int\mathcal Ff\,
 \overline{\mathcal Fg}\,d\xi$ for $f,g\in L^2$
 \cite[\S2.2.4]{Grafakos2014}.  For fields, $\mathcal F$ acts
 componentwise.
\item[(F5)] \emph{Leray projection on $L^p$.}  Let $\mathbb P$ be the
 operator on $L^2(\R^3;\R^3)$ of Lemma~\ref{lem:leray}(a) below, the
 orthogonal projection onto the solenoidal subspace.  For every
 $1<p<\infty$ there is $C_p<\infty$ such that
 $\norm{\mathbb Pf}_p\le C_p\norm f_p$ for all
 $f\in L^2\cap L^p(\R^3;\R^3)$.  This is stated on page~38 of
 \cite{Tao2013}: ``If $u$ is square-integrable, then $\mathbb Pu$ is the
 orthogonal projection of $u$ onto the space of square-integrable
 divergence-free vector fields; from Calder\'on--Zygmund theory we know
 that the projection $\mathbb P$ is bounded on $L^p_x(\R^3)$ for every
 $1<p<\infty$.''  The underlying theorem is the $L^p$ boundedness of the
 Riesz transforms \cite[Ch.~II, \S2; Ch.~III, \S1]{Stein1970}, since
 $(\mathbb Pf)_i=f_i+R_iR_jf_j$ (summation over $j$) has the symbol
 $\delta_{ij}-\xi_i\xi_j|\xi|^{-2}$ of Lemma~\ref{lem:leray}(a).  Only
 $p=3$ and $p=3/2$ are used.
\end{itemize}

\subsection{Definition and pointwise inequalities}

\begin{definition}[Gradient space, cubic quotient, auxiliary operators]
\label{def:quotient}\leavevmode
\begin{enumerate}
\item[(a)] $\mathcal G_3$ is the closure in $L^3(\R^3;\R^3)$ of the set
 $\{\nabla\phi:\phi\in C_c^\infty(\R^3)\}$.  This set is a linear
 subspace, and the closure of a linear subspace of a normed space is a
 linear subspace (limits of sums and multiples are sums and multiples of
 limits); hence $\mathcal G_3$ is a closed linear subspace of
 $L^3(\R^3;\R^3)$.
\item[(b)] For $v\in L^3(\R^3;\R^3)$ put
 $F(v)=\frac13\int_{\R^3}|v|^3\,dx=\frac13\norm v_3^3$ and $j(v)=|v|v$.
 For $u\in L^3(\R^3;\R^3)$ define
 \[
  \mathcal Q(u)=\inf_{q\in\mathcal G_3}F(u+q)
  =\inf_{q\in\mathcal G_3}\frac13\norm{u+q}_3^3 .
 \]
\item[(c)] For $\lambda>0$ and $a\in\R^3$, $(\mathcal S_\lambda u)(x)=\lambda u(\lambda x)$
 and $(\tau_au)(x)=u(x-a)$.
\item[(d)] For $s>0$ let $k_s(x)=(4\pi s)^{-3/2}e^{-|x|^2/4s}$ and
 $G_sf=k_s*f$; this is the heat semigroup $e^{s\Delta}$ in the explicit
 form of \cite[p.~39]{Tao2013}.  One has $k_s\in\mathcal S(\R^3)$,
 $k_s>0$, and $\int_{\R^3}k_s\,dx=1$ because
 $\int_{\R}e^{-t^2/4s}\,dt=(4\pi s)^{1/2}$.
\end{enumerate}
\end{definition}

\begin{lemma}[Pointwise cubic inequalities]\label{lem:cubic-pointwise}
Let $f(z)=\frac13|z|^3$ and $j(z)=|z|z$ for $z\in\R^3$.  Then
$f\in C^1(\R^3)$ with $\nabla f=j$, and for all $a,b,h\in\R^3$:
\begin{align}
 |j(a)-j(b)|&\le(|a|+|b|)\,|a-b|,
 \label{eq:cp-lipschitz}\\
 \bigl|f(a+h)-f(a)-j(a)\cdot h\bigr|&\le(|a|+|h|)\,|h|^2,
 \label{eq:cp-taylor}\\
 \bigl(j(a)-j(b)\bigr)\cdot(a-b)
 &=(|a|+|b|)\Bigl(\tfrac12(|a|-|b|)^2+\tfrac12|a-b|^2\Bigr)
 \ \ge\ \tfrac12|a-b|^3,
 \label{eq:cp-monotone}\\
 f\!\left(\tfrac{a+b}2\right)&\le\tfrac12\bigl(f(a)+f(b)\bigr),
 \quad\text{with equality only if }a=b.
 \label{eq:cp-strict}
\end{align}
\end{lemma}

\begin{proof}
Since $f(z)=\frac13(|z|^2)^{3/2}$ and $t\mapsto t^{3/2}$ is $C^1$ on
$[0,\infty)$ with derivative $\frac32t^{1/2}$, the chain rule gives
$f\in C^1(\R^3)$ and $\nabla f(z)=\frac13\cdot\frac32|z|\cdot2z=|z|z=j(z)$.

\eqref{eq:cp-lipschitz}: $j(a)-j(b)=|a|(a-b)+(|a|-|b|)b$ and
$\bigl||a|-|b|\bigr|\le|a-b|$.

\eqref{eq:cp-taylor}: $g(\theta)=f(a+\theta h)$ is $C^1$ on $[0,1]$ with
$g'(\theta)=j(a+\theta h)\cdot h$, so
\[
 f(a+h)-f(a)-j(a)\cdot h=\int_0^1\bigl(j(a+\theta h)-j(a)\bigr)\cdot h\,d\theta .
\]
By \eqref{eq:cp-lipschitz},
$|(j(a+\theta h)-j(a))\cdot h|\le(|a+\theta h|+|a|)\,\theta|h|\,|h|
\le(2|a|+|h|)\,\theta|h|^2$, and $\int_0^1\theta\,d\theta=\frac12$.

\eqref{eq:cp-monotone}: expanding,
$(|a|a-|b|b)\cdot(a-b)=|a|^3+|b|^3-(|a|+|b|)\,a\cdot b$.  Insert
$|a|^3+|b|^3=(|a|+|b|)(|a|^2-|a||b|+|b|^2)$ and
$a\cdot b=\frac12(|a|^2+|b|^2-|a-b|^2)$:
\[
 (|a|a-|b|b)\cdot(a-b)
 =(|a|+|b|)\Bigl(\tfrac12|a|^2+\tfrac12|b|^2-|a||b|+\tfrac12|a-b|^2\Bigr),
\]
which is the stated identity.  The inequality follows from
$|a|+|b|\ge|a-b|$.

\eqref{eq:cp-strict}: for $s,t\ge0$,
$\frac12(s^3+t^3)-\bigl(\frac{s+t}2\bigr)^3=\frac38(s+t)(s-t)^2\ge0$.
With $s=|a|$, $t=|b|$ and $|a+b|\le|a|+|b|$,
\[
 \Bigl|\frac{a+b}2\Bigr|^3\le\Bigl(\frac{|a|+|b|}2\Bigr)^3
 \le\frac12\bigl(|a|^3+|b|^3\bigr).
\]
Suppose equality holds throughout and $a\ne b$.  Equality in the second
inequality forces $(|a|+|b|)(|a|-|b|)^2=0$; since $a\ne b$ excludes
$a=b=0$, this gives $|a|=|b|=:r>0$.  Equality in the first gives
$|a+b|=2r$, so $4r^2=|a+b|^2=2r^2+2a\cdot b$, that is, $a\cdot b=r^2=|a||b|$,
and the equality case of the Cauchy--Schwarz inequality with $|a|=|b|$
gives $a=b$, a contradiction.
\end{proof}

\begin{lemma}[The cubic functional on $L^3$]\label{lem:cubic-frechet}
Let $v,v',h\in L^3(\R^3;\R^3)$.  Then $j(v)\in L^{3/2}(\R^3;\R^3)$ with
$\norm{j(v)}_{3/2}=\norm v_3^2$, and
\begin{gather}
 \bigl|F(v+h)-F(v)-\langle j(v),h\rangle\bigr|
 \le(\norm v_3+\norm h_3)\norm h_3^2,
 \label{eq:cp-F-taylor}\\
 \norm{j(v)-j(v')}_{3/2}\le(\norm v_3+\norm{v'}_3)\norm{v-v'}_3,
 \label{eq:cp-F-lipschitz}\\
 \langle j(v)-j(v'),v-v'\rangle\ge\tfrac12\norm{v-v'}_3^3 .
 \label{eq:cp-F-monotone}
\end{gather}
In particular $F$ is continuous on $L^3$, and $h\mapsto\langle j(v),h\rangle$
is a bounded linear functional on $L^3$ of norm at most $\norm v_3^2$.
\end{lemma}

\begin{proof}
$\int|j(v)|^{3/2}=\int|v|^3$ gives the first claim.  For
\eqref{eq:cp-F-taylor}, apply \eqref{eq:cp-taylor} pointwise with
$a=v(x)$, $h=h(x)$, integrate, and use H\"older's inequality with exponents
$3$ and $3/2$:
$\int(|v|+|h|)|h|^2\le\norm{|v|+|h|}_3\,\norm{|h|^2}_{3/2}
\le(\norm v_3+\norm h_3)\norm h_3^2$.  For \eqref{eq:cp-F-lipschitz},
raise \eqref{eq:cp-lipschitz} to the power $3/2$, integrate, and apply the
Cauchy--Schwarz inequality:
\[
 \int|j(v)-j(v')|^{3/2}
 \le\int(|v|+|v'|)^{3/2}|v-v'|^{3/2}
 \le\Bigl(\int(|v|+|v'|)^3\Bigr)^{1/2}\Bigl(\int|v-v'|^3\Bigr)^{1/2},
\]
so $\norm{j(v)-j(v')}_{3/2}\le\norm{|v|+|v'|}_3\norm{v-v'}_3
\le(\norm v_3+\norm{v'}_3)\norm{v-v'}_3$.  \eqref{eq:cp-F-monotone} is
\eqref{eq:cp-monotone} integrated; the left side is finite because
$j(v)-j(v')\in L^{3/2}$ and $v-v'\in L^3$.  Continuity of $F$:
$|F(v+h)-F(v)|\le\norm v_3^2\norm h_3+(\norm v_3+\norm h_3)\norm h_3^2$ by
\eqref{eq:cp-F-taylor} and H\"older.
\end{proof}

\begin{lemma}[Two density facts]\label{lem:density}\leavevmode
\begin{enumerate}
\item[(a)] If $f\in L^1_{\rm loc}(\R^3;\mathbb C)$ and
 $\int_{\R^3}f\eta\,dx=0$ for every real-valued $\eta\in C_c^\infty(\R^3)$,
 then $f=0$ a.e.  The same holds componentwise for fields.
\item[(b)] For $u\in L^3(\R^3;\R^3)$ put
 $u_n=u\,\mathbf 1_{\{|x|\le n\}}\mathbf 1_{\{|u|\le n\}}$.  Then
 $u_n\in L^2\cap L^3\cap L^\infty$, $|u_n|\le|u|$, and $u_n\to u$ in
 $L^3$.  In particular $L^2\cap L^3$ is dense in $L^3$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) Taking real and imaginary parts, assume $f$ real.  For fixed $x$ and
$\varepsilon\in(0,1)$, $\eta=\rho_\varepsilon(x-\cdot)$ is an admissible
test function, so $(\rho_\varepsilon*f)(x)=0$ for every $x$.  Fix $r>0$
and put $f_r=f\,\mathbf 1_{\{|y|\le r+1\}}\in L^1(\R^3)$.  For
$|x|\le r$ the integrand $\rho_\varepsilon(x-y)f(y)$ vanishes unless
$|y|\le r+1$, so $(\rho_\varepsilon*f_r)(x)=(\rho_\varepsilon*f)(x)=0$.
By (F3), $\rho_\varepsilon*f_r\to f_r$ in $L^1(\R^3)$, hence $f=f_r=0$
a.e.\ on $\{|x|\le r\}$; $r$ is arbitrary.

(b) $u_n$ is bounded by $n$ and supported in $\{|x|\le n\}$, so
$u_n\in L^2\cap L^\infty$; $|u_n|\le|u|$ gives $u_n\in L^3$; and
$u_n(x)\to u(x)$ for a.e.\ $x$ (for every $x$ at which $u(x)$ is finite),
so $\norm{u_n-u}_3\to0$ by dominated convergence with dominant $(2|u|)^3$.
\end{proof}

\subsection{The minimizing representative}

\begin{lemma}[Existence, uniqueness, and Euler--Lagrange condition]
\label{lem:quotient-minimizer}
Let $u\in L^3(\R^3;\R^3)$.
\begin{enumerate}
\item[(a)] There is $q\in\mathcal G_3$ with $F(u+q)=\mathcal Q(u)$.
\item[(b)] This $q$ is unique.  Write $q(u)$ for it, $w(u)=u+q(u)$ and
 $A(u)=j(w(u))=|w(u)|w(u)$.  Then $A(u)\in L^{3/2}$,
 $\mathcal Q(u)=\frac13\norm{w(u)}_3^3$ and $\norm{A(u)}_{3/2}=\norm{w(u)}_3^2$.
\item[(c)] $\langle A(u),g\rangle=0$ for every $g\in\mathcal G_3$.  In
 particular $\int_{\R^3}|w|w\cdot\nabla\phi\,dx=0$ for every
 $\phi\in C_c^\infty(\R^3)$, that is, $\operatorname{div}(|w|w)=0$ in the
 sense of distributions, where $w=w(u)$.
\item[(d)] For every $g\in\mathcal G_3$: $\mathcal Q(u+g)=\mathcal Q(u)$,
 $w(u+g)=w(u)$, and $q(u+g)=q(u)-g$.
\end{enumerate}
All four statements hold for every $u\in L^3(\R^3;\R^3)$.
\end{lemma}

\begin{proof}
(a) Put $I=\mathcal Q(u)$.  Since $q=0$ is admissible and $F\ge0$,
$0\le I\le F(u)<\infty$.  Choose $q_n\in\mathcal G_3$ with
$F(u+q_n)\to I$ and, discarding finitely many terms,
$F(u+q_n)\le F(u)+1$ for all $n$.  Then
\[
 \norm{q_n}_3\le\norm{u+q_n}_3+\norm u_3
 \le\bigl(3F(u)+3\bigr)^{1/3}+\norm u_3=:M
 \qquad\text{for all }n .
\]
Let $X$ be the space $L^3$ of the product of Lebesgue measure on $\R^3$
with counting measure on $\{1,2,3\}$, a $\sigma$-finite measure space;
as a set $X=L^3(\R^3;\R^3)$, with norm
$\norm v_X=(\sum_{i=1}^3\int|v_i|^3)^{1/3}$.  The norms are equivalent:
$\norm v_X^3\le3\norm v_3^3$ because $|v_i|\le|v|$, and
$\norm v_3^3\le\int(|v_1|+|v_2|+|v_3|)^3\le9\norm v_X^3$ because
$(\frac{a_1+a_2+a_3}3)^3\le\frac13(a_1^3+a_2^3+a_3^3)$ for $a_i\ge0$ by
convexity of $t\mapsto t^3$ on $[0,\infty)$.  Hence
$(L^3(\R^3;\R^3),\norm\cdot_3)$ and $X$ have the same bounded sets, the
same continuous linear functionals, and therefore the same weakly
convergent sequences.  By (F1), $X$ is reflexive and the bounded sequence
$(q_n)$ has a subsequence $(q_{n_k})$ converging weakly to some
$q\in L^3(\R^3;\R^3)$.  $\mathcal G_3$ is convex (a linear subspace) and
norm closed, hence weakly closed by (F2), so $q\in\mathcal G_3$.  For
every continuous linear functional $\ell$,
$\ell(u+q_{n_k})=\ell(u)+\ell(q_{n_k})\to\ell(u)+\ell(q)=\ell(u+q)$, so
$u+q_{n_k}\rightharpoonup u+q$ weakly, and by (F2)
$\norm{u+q}_3\le\liminf_k\norm{u+q_{n_k}}_3$.  Since $t\mapsto t^3/3$ is
increasing and continuous on $[0,\infty)$,
$F(u+q)\le\liminf_kF(u+q_{n_k})=I$.  As $q\in\mathcal G_3$, also
$F(u+q)\ge I$.  Thus $F(u+q)=I$.

(b) Let $q,q'\in\mathcal G_3$ both attain the infimum and put $w=u+q$,
$w'=u+q'$.  Then $\frac12(w+w')=u+\frac12(q+q')$ is admissible, so
$F(\frac12(w+w'))\ge I$.  By \eqref{eq:cp-strict} applied pointwise,
$f(\frac12(w+w'))\le\frac12(f(w)+f(w'))$ everywhere, with strict
inequality on the set $\{w\ne w'\}$.  If that set had positive measure,
integration would give $F(\frac12(w+w'))<\frac12(F(w)+F(w'))=I$, a
contradiction.  Hence $w=w'$ a.e., that is, $q=q'$.  The remaining claims
are Lemma~\ref{lem:cubic-frechet} with $v=w(u)$ and the definition of
$\mathcal Q$.

(c) Let $g\in\mathcal G_3$, $w=w(u)$, $q=q(u)$, and put
$\varphi(s)=F(w+sg)$ for $s\in\R$.  Since $q+sg\in\mathcal G_3$, the field
$w+sg=u+(q+sg)$ is admissible, so $\varphi(s)\ge\varphi(0)$ for all $s$.
For a.e.\ $x$ the function $s\mapsto f(w(x)+sg(x))$ is $C^1$ with
derivative $j(w(x)+sg(x))\cdot g(x)$, and for $|s|\le1$
\[
 \bigl|j(w+sg)\cdot g\bigr|\le|w+sg|^2|g|\le(|w|+|g|)^2|g|,
 \qquad
 \int_{\R^3}(|w|+|g|)^2|g|\,dx\le\norm{|w|+|g|}_3^2\norm g_3<\infty
\]
by H\"older's inequality with exponents $3/2$ and $3$.  For
$0<|s|\le1$ the difference quotient
$s^{-1}\bigl(f(w+sg)-f(w)\bigr)$ is, by the mean value theorem, bounded
pointwise by the integrable function $(|w|+|g|)^2|g|$ and converges
pointwise to $j(w)\cdot g$ as $s\to0$.  Dominated convergence gives
$\varphi'(0)=\int j(w)\cdot g\,dx=\langle A(u),g\rangle$.  Since
$\varphi$ has a minimum at $s=0$, the one-sided limits of
$s^{-1}(\varphi(s)-\varphi(0))$ are $\ge0$ for $s\downarrow0$ and
$\le0$ for $s\uparrow0$; both equal $\varphi'(0)$, so
$\langle A(u),g\rangle=0$.  Taking $g=\nabla\phi$ with
$\phi\in C_c^\infty$ gives the distributional statement.

(d) Since $\mathcal G_3$ is a linear space,
$\{u+g+q':q'\in\mathcal G_3\}=\{u+q:q\in\mathcal G_3\}$; the two
minimization problems have the same admissible set and the same
functional, so the same value and, by (b), the same minimizer
$w(u+g)=w(u)$, whence $q(u+g)=w(u)-(u+g)=q(u)-g$.
\end{proof}

\begin{remark}
Reflexivity of $L^3$ is used only in Lemma~\ref{lem:quotient-minimizer}(a).
Uniqueness uses only the pointwise strict convexity \eqref{eq:cp-strict};
no uniform convexity of $L^3$ and no Clarkson inequality is used anywhere
in this section.  No regularity of $w(u)$ beyond membership in $L^3$ is
asserted; the representative satisfies only the nonlinear divergence
condition of (c).
\end{remark}

\subsection{Gradients, the Leray projection, and coercivity}

\begin{lemma}[Gradient closure]\label{lem:gradient-closure}
Let $\psi\in L^3(\R^3)$ have a distributional gradient
$\nabla\psi\in L^3(\R^3;\R^3)$.  Then $\nabla\psi\in\mathcal G_3$.  In
particular $\nabla\psi\in\mathcal G_3$ for every $\psi\in\mathcal S(\R^3)$
and every $\psi\in C^1(\R^3)$ with $\psi,\nabla\psi\in L^3$.
\end{lemma}

\begin{proof}
\emph{Cutoff.}  Put $\psi_R=\chi_R\psi$.  For $\eta\in C_c^\infty$,
$\int\psi_R\,\partial_i\eta=\int\psi\,\partial_i(\chi_R\eta)
-\int\psi\eta\,\partial_i\chi_R
=-\int(\chi_R\partial_i\psi+\psi\,\partial_i\chi_R)\eta$,
so $\psi_R\in L^3$ has compact support and distributional gradient
$\nabla\psi_R=\chi_R\nabla\psi+\psi\nabla\chi_R\in L^3$, and
\[
 \norm{\nabla\psi_R-\nabla\psi}_3
 \le\norm{(1-\chi_R)\nabla\psi}_3+R^{-1}\norm{\nabla\chi}_\infty\norm\psi_3
 \longrightarrow0\qquad(R\to\infty)
\]
by dominated convergence in the first term.

\emph{Mollification.}  By (F3), $\rho_\varepsilon*\psi_R\in C_c^\infty(\R^3)$
and $\partial_i(\rho_\varepsilon*\psi_R)=(\partial_i\rho_\varepsilon)*\psi_R$.
For fixed $x$, $y\mapsto\rho_\varepsilon(x-y)$ is in $C_c^\infty$, so by
the definition of the distributional gradient
\[
 (\partial_i\rho_\varepsilon)*\psi_R(x)
 =\int(\partial_i\rho_\varepsilon)(x-y)\psi_R(y)\,dy
 =-\int\partial_{y_i}\bigl[\rho_\varepsilon(x-y)\bigr]\psi_R(y)\,dy
 =\int\rho_\varepsilon(x-y)\,\partial_i\psi_R(y)\,dy ,
\]
that is, $\nabla(\rho_\varepsilon*\psi_R)=\rho_\varepsilon*\nabla\psi_R$,
which tends to $\nabla\psi_R$ in $L^3$ as $\varepsilon\downarrow0$ by (F3).
Given $\delta>0$ choose $R$ with $\norm{\nabla\psi_R-\nabla\psi}_3<\delta$
and then $\varepsilon$ with
$\norm{\rho_\varepsilon*\nabla\psi_R-\nabla\psi_R}_3<\delta$; the
gradient of the $C_c^\infty$ function $\rho_\varepsilon*\psi_R$ is then
within $2\delta$ of $\nabla\psi$ in $L^3$.  Hence
$\nabla\psi\in\mathcal G_3$.  For $\psi\in\mathcal S$ or
$\psi\in C^1$ with $\psi,\nabla\psi\in L^3$, the classical gradient is the
distributional one (integration by parts against $\eta\in C_c^\infty$).
\end{proof}

\begin{lemma}[Leray projection]\label{lem:leray}\leavevmode
\begin{enumerate}
\item[(a)] For $\xi\ne0$ let $\Pi(\xi)=I-\xi\otimes\xi/|\xi|^2$, a real
 symmetric $3\times3$ matrix with $\Pi(\xi)^2=\Pi(\xi)$ and
 $\Pi(\xi)\xi=0$.  For $f\in L^2(\R^3;\R^3)$ define
 $\mathbb Pf=\mathcal F^{-1}\bigl(\Pi\,\mathcal Ff\bigr)$.  Then
 $\mathbb P$ is linear, $\norm{\mathbb Pf}_2\le\norm f_2$,
 $\mathbb P^2=\mathbb P$, $\langle\mathbb Pf,g\rangle=\langle f,\mathbb Pg\rangle$
 for $f,g\in L^2$, $\mathbb Pf$ is real-valued, and
 $\{f\in L^2:\mathbb Pf=f\}$ is exactly the set of solenoidal fields in
 $L^2(\R^3;\R^3)$.  Thus $\mathbb P$ is the orthogonal projection of
 $L^2(\R^3;\R^3)$ onto its solenoidal subspace, and $\mathbb Pu=u$ for
 every solenoidal $u\in L^2$.
\item[(b)] $\mathbb P$ extends uniquely from $L^2\cap L^3$ to a bounded
 linear operator on $L^3(\R^3;\R^3)$, again denoted $\mathbb P$, with
 $C_{\mathbb P}:=\norm{\mathbb P}_{L^3\to L^3}\le C_3<\infty$; on $L^3$
 one has $\mathbb P^2=\mathbb P$, and $\mathbb P$ maps real fields to
 real fields.  Moreover $\norm{\mathbb P\psi}_{3/2}\le C_{3/2}\norm\psi_{3/2}$
 for $\psi\in C_c^\infty(\R^3;\R^3)$.
\item[(c)] $\mathbb P\nabla\phi=0$ for every $\phi\in C_c^\infty(\R^3)$,
 and consequently $\mathbb Pq=0$ for every $q\in\mathcal G_3$.
\item[(d)] If $u\in L^3(\R^3;\R^3)$ is solenoidal, then $\mathbb Pu=u$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) $\Pi(\xi)^2=I-2\xi\otimes\xi/|\xi|^2+\xi(\xi\cdot\xi)\xi/|\xi|^4=\Pi(\xi)$
and $\Pi(\xi)\xi=\xi-\xi(\xi\cdot\xi)/|\xi|^2=0$.  A real symmetric
idempotent matrix is an orthogonal projection, so $|\Pi(\xi)z|\le|z|$ for
$z\in\mathbb C^3$; hence $\Pi\,\mathcal Ff\in L^2$ with
$\norm{\Pi\mathcal Ff}_2\le\norm{\mathcal Ff}_2$, and by (F4)
$\mathbb Pf$ is well defined with $\norm{\mathbb Pf}_2\le\norm f_2$.
$\mathbb P^2=\mathbb P$ follows from $\Pi^2=\Pi$.  For $f,g\in L^2$ real,
(F4) and the symmetry of the real matrix $\Pi$ give
\[
 \langle\mathbb Pf,g\rangle
 =\int\Pi\mathcal Ff\cdot\overline{\mathcal Fg}\,d\xi
 =\int\mathcal Ff\cdot\overline{\Pi\mathcal Fg}\,d\xi
 =\langle f,\mathbb Pg\rangle .
\]
Realness: for real $f\in L^1\cap L^2$ the definition gives
$\hat f(-\xi)=\overline{\hat f(\xi)}$; the set of $g\in L^2(\R^3;\mathbb C^3)$
with $g(-\xi)=\overline{g(\xi)}$ a.e.\ is closed and $\mathcal F$ is
continuous, so $\mathcal Ff$ has this symmetry for every real
$f\in L^2$.  Since $\Pi(-\xi)=\Pi(\xi)$ is real, $\Pi\mathcal Ff$ has the
same symmetry.  For $g\in L^1\cap L^2$ with $g(-\xi)=\overline{g(\xi)}$,
$\overline{\check g(x)}=\int e^{-2\pi ix\cdot\xi}\overline{g(\xi)}\,d\xi
=\int e^{-2\pi ix\cdot\xi}g(-\xi)\,d\xi=\check g(x)$, so $\check g$ is
real; for general such $g\in L^2$ apply this to
$g\,\mathbf 1_{\{|\xi|\le n\}}$, which has the same symmetry, and pass to
the $L^2$ limit.  Hence $\mathbb Pf$ is real.

Range: $\mathbb Pf=f$ iff $\Pi\mathcal Ff=\mathcal Ff$ a.e.\ iff
$\xi\,(\xi\cdot\mathcal Ff)/|\xi|^2=0$ a.e.\ iff $\xi\cdot\mathcal Ff(\xi)=0$
for a.e.\ $\xi$.  We show that $f\in L^2$ is solenoidal iff
$\xi\cdot\mathcal Ff=0$ a.e.  For $\phi\in\mathcal S(\R^3)$ (real),
integration by parts in the Fourier integral gives
$\mathcal F(\partial_j\phi)=2\pi i\xi_j\mathcal F\phi$, so by (F4)
\begin{equation}\label{eq:cp-sol-fourier}
 \langle f,\nabla\phi\rangle
 =\int\mathcal Ff\cdot\overline{2\pi i\xi\,\mathcal F\phi}\,d\xi
 =-2\pi i\int(\xi\cdot\mathcal Ff)\,\overline{\mathcal F\phi}\,d\xi .
\end{equation}
If $\xi\cdot\mathcal Ff=0$ a.e., the right side vanishes for every
$\phi\in C_c^\infty$, so $f$ is solenoidal.  Conversely let $f$ be
solenoidal.  First, $\langle f,\nabla\phi\rangle=0$ for every real
$\phi\in\mathcal S$: indeed $\chi_R\phi\in C_c^\infty$ and
$\nabla(\chi_R\phi)-\nabla\phi=(\chi_R-1)\nabla\phi+\phi\nabla\chi_R\to0$
in $L^2$ as $R\to\infty$ (dominated convergence, and
$\norm{\phi\nabla\chi_R}_2\le R^{-1}\norm{\nabla\chi}_\infty\norm\phi_2$).
Next, let $\eta\in C_c^\infty(\R^3;\mathbb C)$ and $\phi=\check\eta$.
Differentiating under the integral sign and integrating by parts in $\xi$,
\[
 x^\beta\partial^\alpha\phi(x)
 =\Bigl(-\frac1{2\pi i}\Bigr)^{|\beta|}
 \int e^{2\pi ix\cdot\xi}\,\partial_\xi^\beta\bigl[(2\pi i\xi)^\alpha\eta(\xi)\bigr]\,d\xi
\]
is bounded for all multi-indices $\alpha,\beta$, so
$\phi\in\mathcal S(\R^3;\mathbb C)$, and $\mathcal F\phi=\eta$ by (F4).
Write $\phi=\phi_1+i\phi_2$ with $\phi_1,\phi_2$ real Schwartz functions;
then $\eta=\mathcal F\phi_1+i\mathcal F\phi_2$ and by
\eqref{eq:cp-sol-fourier} applied to $\phi_1$ and $\phi_2$,
\[
 \int(\xi\cdot\mathcal Ff)\,\overline\eta\,d\xi
 =\int(\xi\cdot\mathcal Ff)\,\overline{\mathcal F\phi_1}\,d\xi
 -i\int(\xi\cdot\mathcal Ff)\,\overline{\mathcal F\phi_2}\,d\xi
 =-\frac1{2\pi i}\bigl(\langle f,\nabla\phi_1\rangle-i\langle f,\nabla\phi_2\rangle\bigr)=0 .
\]
Since $\xi\cdot\mathcal Ff\in L^2_{\rm loc}\subset L^1_{\rm loc}$ and
$\eta$ ranges over all of $C_c^\infty$ (in particular over all real
$\eta$), Lemma~\ref{lem:density}(a) gives $\xi\cdot\mathcal Ff=0$ a.e.
So the fixed space of $\mathbb P$ is the solenoidal subspace, which is
therefore closed, and a self-adjoint idempotent with a given range is the
orthogonal projection onto it.

(b) By (F5) with $p=3$, $\norm{\mathbb Pf}_3\le C_3\norm f_3$ for
$f\in L^2\cap L^3$.  For $u\in L^3$ choose $u_n\in L^2\cap L^3$ with
$u_n\to u$ in $L^3$ (Lemma~\ref{lem:density}(b)); then $(\mathbb Pu_n)$
is Cauchy in $L^3$, its limit does not depend on the chosen sequence
(interlace two sequences), and setting $\mathbb Pu$ equal to this limit
defines a linear operator with $\norm{\mathbb Pu}_3\le C_3\norm u_3$
which agrees with (a) on $L^2\cap L^3$ (constant sequences).  Real fields
go to real fields (a.e.\ limits of real fields).  For
$u_n\in L^2\cap L^3$ one has $\mathbb Pu_n\in L^2\cap L^3$ and
$\mathbb P(\mathbb Pu_n)=\mathbb Pu_n$ by (a); letting $n\to\infty$ and
using continuity on $L^3$ gives $\mathbb P^2u=\mathbb Pu$.  The last
claim is (F5) with $p=3/2$, since $C_c^\infty\subset L^2\cap L^{3/2}$.

(c) For $\phi\in C_c^\infty$, $\mathcal F(\nabla\phi)=2\pi i\xi\,\hat\phi$,
so $\mathcal F(\mathbb P\nabla\phi)=2\pi i\,\Pi(\xi)\xi\,\hat\phi=0$ and
$\mathbb P\nabla\phi=0$.  For $q\in\mathcal G_3$ choose
$\phi_n\in C_c^\infty$ with $\nabla\phi_n\to q$ in $L^3$; since
$\nabla\phi_n\in L^2\cap L^3$, continuity of $\mathbb P$ on $L^3$ gives
$\mathbb Pq=\lim\mathbb P\nabla\phi_n=0$.

(d) Let $u\in L^3$ be solenoidal and fix $\psi\in C_c^\infty(\R^3;\R^3)$.

\emph{Step 1 (duality).}  Let $u_n\in L^2\cap L^3$ with $u_n\to u$ in
$L^3$.  By (a), $\langle\mathbb Pu_n,\psi\rangle=\langle u_n,\mathbb P\psi\rangle$.
As $n\to\infty$ the left side tends to $\langle\mathbb Pu,\psi\rangle$
because $\mathbb Pu_n\to\mathbb Pu$ in $L^3$ and $\psi\in L^{3/2}$, and
the right side tends to $\langle u,\mathbb P\psi\rangle$ because
$\mathbb P\psi\in L^{3/2}$ by (b).  Hence
\begin{equation}\label{eq:cp-duality}
 \langle\mathbb Pu-u,\psi\rangle=-\langle u,\psi-\mathbb P\psi\rangle .
\end{equation}

\emph{Step 2 ($\psi-\mathbb P\psi$ is a gradient).}  Put
$\hat\psi=\mathcal F\psi$.  For every multi-index $\alpha$,
$(2\pi i\xi)^\alpha\hat\psi=\mathcal F(\partial^\alpha\psi)$ is bounded by
$\norm{\partial^\alpha\psi}_1$, so $|\hat\psi(\xi)|\le C_N(1+|\xi|)^{-N}$
for every $N$.  Define, for $\xi\ne0$,
\[
 g(\xi)=\frac{\xi\cdot\hat\psi(\xi)}{2\pi i\,|\xi|^2},
 \qquad |g(\xi)|\le\frac{|\hat\psi(\xi)|}{2\pi|\xi|} .
\]
Since $|\xi|^{-1}$ and $|\xi|^{-2}$ are integrable on $\{|\xi|\le1\}\subset\R^3$
and $\hat\psi$ decays rapidly, $g\in L^1\cap L^2$ and
$|\xi|^kg\in L^1\cap L^2$ for every $k\ge0$.  Put $\Phi=\check g$.
Differentiation under the integral sign, with dominant
$|2\pi\xi|^{|\alpha|}|g|\in L^1$, shows $\Phi\in C^\infty(\R^3)$ with
$\partial^\alpha\Phi=\bigl((2\pi i\xi)^\alpha g\bigr)^\vee$ bounded.
$\Phi$ is real: $\hat\psi(-\xi)=\overline{\hat\psi(\xi)}$ because $\psi$
is real, and $\overline{(2\pi i)^{-1}}=-(2\pi i)^{-1}$, so
$g(-\xi)=\overline{g(\xi)}$, and as in the proof of (a) this gives
$\overline{\Phi}=\Phi$.  By (F4), $\Phi\in L^2$ with $\mathcal F\Phi=g$
and $\partial_i\Phi\in L^2$ with
$\mathcal F(\partial_i\Phi)=2\pi i\xi_ig=\xi_i(\xi\cdot\hat\psi)/|\xi|^2$.
On the other hand,
$\mathcal F(\psi-\mathbb P\psi)=(I-\Pi)\hat\psi=\xi(\xi\cdot\hat\psi)/|\xi|^2$.
Since $\mathcal F$ is injective on $L^2$,
\begin{equation}\label{eq:cp-gradient-rep}
 \psi-\mathbb P\psi=\nabla\Phi\quad\text{a.e.},
 \qquad \Phi\in C^\infty(\R^3)\cap L^2(\R^3)\ \text{real},
 \qquad \nabla\Phi\in L^{3/2}(\R^3;\R^3),
\end{equation}
where the last membership is (b).

\emph{Step 3 (cutoff).}  Since $\chi_R\Phi\in C_c^\infty(\R^3)$ and $u$ is
solenoidal, $\langle u,\nabla(\chi_R\Phi)\rangle=0$ for every $R\ge1$.
Now $\nabla(\chi_R\Phi)-\nabla\Phi=(\chi_R-1)\nabla\Phi+\Phi\nabla\chi_R$,
and
\begin{align*}
 \norm{(\chi_R-1)\nabla\Phi}_{3/2}&\longrightarrow0
 \quad\text{(dominated convergence, since }\nabla\Phi\in L^{3/2}),\\
 \norm{\Phi\nabla\chi_R}_{3/2}&\le\norm{\nabla\chi_R}_6\norm\Phi_2
 =R^{-1/2}\norm{\nabla\chi}_6\norm\Phi_2\longrightarrow0
 \quad\text{(H\"older, }\tfrac23=\tfrac16+\tfrac12).
\end{align*}
Since
$u\in L^3$, $\langle u,\nabla\Phi\rangle=\lim_{R\to\infty}\langle u,\nabla(\chi_R\Phi)\rangle=0$.

\emph{Step 4.}  By \eqref{eq:cp-duality} and \eqref{eq:cp-gradient-rep},
$\langle\mathbb Pu-u,\psi\rangle=-\langle u,\nabla\Phi\rangle=0$ for
every $\psi\in C_c^\infty(\R^3;\R^3)$.  Since $\mathbb Pu-u\in L^3\subset L^1_{\rm loc}$,
Lemma~\ref{lem:density}(a) gives $\mathbb Pu=u$ a.e.
\end{proof}

\begin{remark}
The displayed formula ``$\mathbb Pu:=\Delta^{-1}(\nabla\times\nabla\times u)$''
on page~38 of \cite{Tao2013} differs by a sign from the operator defined
in Lemma~\ref{lem:leray}(a) when $\Delta^{-1}$ is the multiplier
$-(4\pi^2|\xi|^2)^{-1}$ of his equation~(14), because
$\nabla\times\nabla\times u=\nabla(\nabla\cdot u)-\Delta u$; the operator
meant there is pinned by the accompanying sentence quoted in (F5), and the
$L^p$ bound is insensitive to the sign.  Only that sentence is imported.
\end{remark}

\begin{lemma}[Coercivity on solenoidal fields]\label{lem:quotient-coercive}
For every $u\in L^3(\R^3;\R^3)$, $\mathcal Q(u)\le F(u)=\frac13\norm u_3^3$.
If $u\in L^3(\R^3;\R^3)$ is solenoidal, then with $w=w(u)$ and
$q=q(u)$ one has $\mathbb Pw=u$, $q=w-\mathbb Pw$, and
\begin{equation}\label{eq:cp-coercive}
 \frac{\norm u_3^3}{3C_{\mathbb P}^3}\le\mathcal Q(u)\le\frac13\norm u_3^3,
 \qquad
 \norm q_3\le(1+C_{\mathbb P})\norm w_3
 =(1+C_{\mathbb P})\bigl(3\mathcal Q(u)\bigr)^{1/3} .
\end{equation}
\end{lemma}

\begin{proof}
The upper bound is the admissible choice $q=0$.  Let $u$ be solenoidal.
By Lemma~\ref{lem:leray}(d) and (c), $\mathbb Pw=\mathbb Pu+\mathbb Pq=u$,
hence $q=w-u=w-\mathbb Pw$ and
$\norm u_3=\norm{\mathbb Pw}_3\le C_{\mathbb P}\norm w_3$, that is,
$\norm u_3^3\le C_{\mathbb P}^3\norm w_3^3=3C_{\mathbb P}^3\mathcal Q(u)$.
Finally $\norm q_3\le\norm w_3+\norm{\mathbb Pw}_3\le(1+C_{\mathbb P})\norm w_3$.
\end{proof}

\subsection{Homogeneity, scaling, and heat monotonicity}

\begin{lemma}[Homogeneity, critical scaling, translations]
\label{lem:quotient-scaling}
For every $u\in L^3(\R^3;\R^3)$, $\alpha\in\R$, $\lambda>0$ and $a\in\R^3$,
\[
 \mathcal Q(\alpha u)=|\alpha|^3\mathcal Q(u),\qquad
 \mathcal Q(\mathcal S_\lambda u)=\mathcal Q(u),\qquad
 \mathcal Q(\tau_au)=\mathcal Q(u),
\]
and $w(\alpha u)=\alpha w(u)$, $w(\mathcal S_\lambda u)=\mathcal S_\lambda w(u)$,
$w(\tau_au)=\tau_aw(u)$.
\end{lemma}

\begin{proof}
For $\alpha=0$ both sides vanish since $q=0$ gives $F(0)=0\le\mathcal Q(0)$.
For $\alpha\ne0$, $q\mapsto\alpha q$ is a bijection of $\mathcal G_3$ and
$F(\alpha v)=|\alpha|^3F(v)$, so
$\mathcal Q(\alpha u)=\inf_{q}F(\alpha(u+q))=|\alpha|^3\mathcal Q(u)$;
the infimum is attained at $\alpha q(u)$, so $w(\alpha u)=\alpha w(u)$ by
uniqueness.  For the scaling, the change of variables $y=\lambda x$ gives
$\norm{\mathcal S_\lambda v}_3^3=\int\lambda^3|v(\lambda x)|^3dx=\norm v_3^3$,
so $\mathcal S_\lambda$ is a linear isometry of $L^3$ with inverse
$\mathcal S_{1/\lambda}$.  For $\phi\in C_c^\infty$,
$\mathcal S_\lambda\nabla\phi=\lambda(\nabla\phi)(\lambda\,\cdot)
=\nabla[\phi(\lambda\,\cdot)]$ with $\phi(\lambda\,\cdot)\in C_c^\infty$;
thus $\mathcal S_\lambda$ maps the generating set of $\mathcal G_3$ into
itself, and being an isometry it maps $\mathcal G_3$ into $\mathcal G_3$
(if $\nabla\phi_n\to q$ then $\mathcal S_\lambda\nabla\phi_n\to\mathcal S_\lambda q$,
and $\mathcal G_3$ is closed).  Applying this to $\mathcal S_{1/\lambda}$
shows $\mathcal S_\lambda\mathcal G_3=\mathcal G_3$.  Hence
\[
 \mathcal Q(\mathcal S_\lambda u)
 =\inf_{q\in\mathcal G_3}F(\mathcal S_\lambda u+q)
 =\inf_{q'\in\mathcal G_3}F(\mathcal S_\lambda(u+q'))
 =\inf_{q'\in\mathcal G_3}F(u+q')=\mathcal Q(u),
\]
attained at $q=\mathcal S_\lambda q(u)$, so
$w(\mathcal S_\lambda u)=\mathcal S_\lambda w(u)$.  Translations are
handled identically: $\tau_a$ is an isometry of $L^3$,
$\tau_a\nabla\phi=\nabla(\tau_a\phi)$, and $\tau_{-a}$ is the inverse.
\end{proof}

\begin{lemma}[Heat monotonicity]\label{lem:quotient-heat}
Let $s>0$.
\begin{enumerate}
\item[(a)] For $f\in L^3$ the integral defining $G_sf(x)$ converges
 absolutely for a.e.\ $x$, and $\norm{G_sf}_3\le\norm f_3$.
\item[(b)] For $\phi\in C_c^\infty(\R^3)$, $G_s\phi\in\mathcal S(\R^3)$ and
 $\nabla(G_s\phi)=G_s\nabla\phi$.
\item[(c)] $G_s\mathcal G_3\subset\mathcal G_3$.
\item[(d)] For every $u\in L^3(\R^3;\R^3)$, with $w=w(u)$,
 \begin{equation}\label{eq:cp-heat}
  \mathcal Q(G_su)\le F(G_sw)\le F(w)=\mathcal Q(u).
 \end{equation}
\end{enumerate}
\end{lemma}

\begin{proof}
(a) This is the case $p=3$, $\norm{k_s}_1=1$, of Young's inequality (F3),
recorded on page~39 of \cite{Tao2013}; the constant $1$ is the point, so
we include the two-line proof.  By H\"older's inequality with exponents
$3/2$ and $3$ applied to $k_s^{2/3}\cdot k_s^{1/3}|f(x-\cdot)|$,
\[
 \int k_s(y)|f(x-y)|\,dy
 \le\Bigl(\int k_s\Bigr)^{2/3}\Bigl(\int k_s(y)|f(x-y)|^3dy\Bigr)^{1/3}
 =\bigl(k_s*|f|^3\bigr)(x)^{1/3}.
\]
By Tonelli's theorem $\int\!\!\int k_s(y)|f(x-y)|^3\,dy\,dx=\norm f_3^3<\infty$,
so $k_s*|f|^3<\infty$ a.e., the defining integral converges absolutely
a.e., and $\norm{G_sf}_3^3\le\int k_s*|f|^3\,dx=\norm f_3^3$.

(b) By (F3) with $k=\phi\in C_c^\infty$ and $g=k_s\in L^1_{\rm loc}$,
$G_s\phi=\phi*k_s\in C^\infty$ and
$\partial^\alpha(G_s\phi)=(\partial^\alpha\phi)*k_s=G_s\partial^\alpha\phi$.
Let $\operatorname{supp}\phi\subset\{|y|\le R_0\}$.  For $|x|\ge2R_0$
and $|y|\le R_0$ one has $|x-y|\ge|x|-R_0\ge|x|/2$, so
\[
 |\partial^\alpha(G_s\phi)(x)|
 \le\int_{|y|\le R_0}k_s(x-y)|\partial^\alpha\phi(y)|\,dy
 \le(4\pi s)^{-3/2}e^{-|x|^2/16s}\norm{\partial^\alpha\phi}_1 ,
\]
which decays faster than any power of $|x|$; together with boundedness on
$\{|x|\le2R_0\}$ this shows $x^\beta\partial^\alpha(G_s\phi)$ is bounded
for all $\alpha,\beta$, that is, $G_s\phi\in\mathcal S$.

(c) Let $q\in\mathcal G_3$ and $\phi_n\in C_c^\infty$ with
$\nabla\phi_n\to q$ in $L^3$.  By (b), $G_s\nabla\phi_n=\nabla(G_s\phi_n)$
with $G_s\phi_n\in\mathcal S$, so $G_s\nabla\phi_n\in\mathcal G_3$ by
Lemma~\ref{lem:gradient-closure}.  By (a),
$\norm{G_s\nabla\phi_n-G_sq}_3\le\norm{\nabla\phi_n-q}_3\to0$, and
$\mathcal G_3$ is closed; hence $G_sq\in\mathcal G_3$.

(d) $G_sw=G_su+G_sq(u)$ with $G_sq(u)\in\mathcal G_3$ by (c), so $G_sw$
is admissible for $\mathcal Q(G_su)$ and $\mathcal Q(G_su)\le F(G_sw)$.
By (a), $F(G_sw)=\frac13\norm{G_sw}_3^3\le\frac13\norm w_3^3=F(w)=\mathcal Q(u)$.
\end{proof}

\begin{remark}
Lemma~\ref{lem:quotient-heat} holds for every $u\in L^3$ and every
$s>0$; it uses neither the semigroup property nor strong continuity of
$G_s$, and it does not differentiate or regularize the minimizer $w$.
Iterating it, $s\mapsto\mathcal Q(G_su)$ is nonincreasing, since
$G_{s+t}u=G_t(G_su)$ by the semigroup property of the Gaussian kernel.
\end{remark}

\subsection{The derivative}

\begin{lemma}[Stability of the minimizer]\label{lem:quotient-stability}
Let $u,h\in L^3(\R^3;\R^3)$, $w=w(u)$, $w'=w(u+h)$, $A=A(u)$, $A'=A(u+h)$.
Then
\begin{gather}
 \bigl|\norm{w'}_3-\norm w_3\bigr|\le\norm h_3,
 \label{eq:cp-contraction}\\
 \tfrac12\norm{w'-w}_3^3\le\langle A'-A,\,h\rangle,
 \qquad
 \norm{w'-w}_3\le2\,(\norm w_3+\norm h_3)^{1/2}\norm h_3^{1/2},
 \label{eq:cp-strong}\\
 \norm{A'-A}_{3/2}\le4\,(\norm w_3+\norm h_3)^{3/2}\norm h_3^{1/2},
 \qquad
 |\mathcal Q(u+h)-\mathcal Q(u)|\le(\norm w_3+\norm h_3)^2\norm h_3 .
 \label{eq:cp-continuity}
\end{gather}
In particular $u\mapsto w(u)$ is continuous $L^3\to L^3$,
$u\mapsto A(u)$ is continuous $L^3\to L^{3/2}$, and $\mathcal Q$ is
continuous on $L^3$.  All of this holds for every $u\in L^3$.
\end{lemma}

\begin{proof}
\emph{Quotient contraction.}  $w+h=(u+h)+q(u)$ is admissible for $u+h$,
so $\norm{w'}_3\le\norm{w+h}_3\le\norm w_3+\norm h_3$; symmetrically
$w'-h=u+q(u+h)$ is admissible for $u$, so
$\norm w_3\le\norm{w'}_3+\norm h_3$.  This is \eqref{eq:cp-contraction}.

\emph{Cancellation.}  $w'-w=h+\bigl(q(u+h)-q(u)\bigr)$ with
$q(u+h)-q(u)\in\mathcal G_3$, so Lemma~\ref{lem:quotient-minimizer}(c)
for the two minimizers gives $\langle A',w'-w\rangle=\langle A',h\rangle$
and $\langle A,w'-w\rangle=\langle A,h\rangle$, hence
$\langle A'-A,w'-w\rangle=\langle A'-A,h\rangle$.

\emph{Strong convergence.}  By \eqref{eq:cp-F-monotone} with $v=w'$,
$v'=w$, and the cancellation,
$\frac12\norm{w'-w}_3^3\le\langle A'-A,w'-w\rangle=\langle A'-A,h\rangle$,
the first part of \eqref{eq:cp-strong}.  By H\"older and
\eqref{eq:cp-F-lipschitz},
\[
 \langle A'-A,h\rangle\le\norm{A'-A}_{3/2}\norm h_3
 \le(\norm w_3+\norm{w'}_3)\norm{w'-w}_3\norm h_3 .
\]
If $w'\ne w$, dividing by $\norm{w'-w}_3$ and using
\eqref{eq:cp-contraction} gives
$\norm{w'-w}_3^2\le2(\norm w_3+\norm{w'}_3)\norm h_3
\le2(2\norm w_3+\norm h_3)\norm h_3\le4(\norm w_3+\norm h_3)\norm h_3$,
which is the second part of \eqref{eq:cp-strong}; if $w'=w$ it is
trivial.

\emph{Continuity.}  By \eqref{eq:cp-F-lipschitz}, \eqref{eq:cp-contraction}
and \eqref{eq:cp-strong},
$\norm{A'-A}_{3/2}\le(2\norm w_3+\norm h_3)\cdot2(\norm w_3+\norm h_3)^{1/2}\norm h_3^{1/2}
\le4(\norm w_3+\norm h_3)^{3/2}\norm h_3^{1/2}$.  Finally, with
$\alpha=\norm{w'}_3$ and $\beta=\norm w_3$, both at most
$\norm w_3+\norm h_3$ and $|\alpha-\beta|\le\norm h_3$,
$|\mathcal Q(u+h)-\mathcal Q(u)|=\frac13|\alpha^3-\beta^3|
=\frac13|\alpha-\beta|(\alpha^2+\alpha\beta+\beta^2)
\le(\norm w_3+\norm h_3)^2\norm h_3$.
\end{proof}

\begin{proposition}[Fr\'echet derivative of $\mathcal Q$]
\label{prop:quotient-derivative}
$\mathcal Q$ is Fr\'echet differentiable at every $u\in L^3(\R^3;\R^3)$,
with
\begin{equation}\label{eq:cp-derivative}
 D\mathcal Q(u)[h]=\langle A(u),h\rangle=\int_{\R^3}|w(u)|\,w(u)\cdot h\,dx
 \qquad(h\in L^3),
\end{equation}
and, with $w=w(u)$,
\begin{equation}\label{eq:cp-derivative-remainder}
 \bigl|\mathcal Q(u+h)-\mathcal Q(u)-\langle A(u),h\rangle\bigr|
 \le6\,(\norm w_3+\norm h_3)^{3/2}\norm h_3^{3/2}
 \qquad(h\in L^3).
\end{equation}
In particular $D\mathcal Q(u)[g]=0$ for every $g\in\mathcal G_3$, and
$\norm{D\mathcal Q(u)}_{(L^3)^*}\le\norm w_3^2=(3\mathcal Q(u))^{2/3}$.
\end{proposition}

\begin{proof}
Write $w'=w(u+h)$, $A=A(u)$, $A'=A(u+h)$.  The functional
$h\mapsto\langle A,h\rangle$ is linear and bounded on $L^3$ with norm at
most $\norm A_{3/2}=\norm w_3^2$ (Lemma~\ref{lem:cubic-frechet}), so
\eqref{eq:cp-derivative-remainder} implies Fr\'echet differentiability
with derivative \eqref{eq:cp-derivative}, the remainder being
$o(\norm h_3)$.

\emph{Upper bound.}  $w+h$ is admissible for $u+h$, so by
\eqref{eq:cp-F-taylor} with $v=w$,
\[
 \mathcal Q(u+h)\le F(w+h)
 \le\mathcal Q(u)+\langle A,h\rangle+(\norm w_3+\norm h_3)\norm h_3^2 .
\]

\emph{Lower bound.}  $w'-h$ is admissible for $u$, so by
\eqref{eq:cp-F-taylor} with $v=w'$ and increment $-h$,
\[
 \mathcal Q(u)\le F(w'-h)
 \le F(w')-\langle A',h\rangle+(\norm{w'}_3+\norm h_3)\norm h_3^2 ,
\]
and $F(w')=\mathcal Q(u+h)$, $\norm{w'}_3\le\norm w_3+\norm h_3$ by
\eqref{eq:cp-contraction}.  Hence
\[
 \mathcal Q(u+h)\ge\mathcal Q(u)+\langle A,h\rangle+\langle A'-A,h\rangle
 -(\norm w_3+2\norm h_3)\norm h_3^2 .
\]

\emph{Remainder.}  By H\"older and \eqref{eq:cp-continuity},
$|\langle A'-A,h\rangle|\le\norm{A'-A}_{3/2}\norm h_3
\le4(\norm w_3+\norm h_3)^{3/2}\norm h_3^{3/2}$.  Combining the two
bounds,
\begin{align*}
 \bigl|\mathcal Q(u+h)-\mathcal Q(u)-\langle A,h\rangle\bigr|
 &\le4(\norm w_3+\norm h_3)^{3/2}\norm h_3^{3/2}
 +2(\norm w_3+\norm h_3)\norm h_3^2\\
 &\le6(\norm w_3+\norm h_3)^{3/2}\norm h_3^{3/2},
\end{align*}
using $\norm h_3^{1/2}\le(\norm w_3+\norm h_3)^{1/2}$ in the last term.
The final claims are Lemma~\ref{lem:quotient-minimizer}(c) and
Lemma~\ref{lem:cubic-frechet}.
\end{proof}

\begin{remark}[Scope of the results of this part]\label{rem:quotient-scope}
Definition~\ref{def:quotient}, Lemmas~\ref{lem:quotient-minimizer},
\ref{lem:quotient-scaling}, \ref{lem:quotient-heat},
\ref{lem:quotient-stability} and
Proposition~\ref{prop:quotient-derivative} hold for every
$u\in L^3(\R^3;\R^3)$, solenoidal or not, and so does the upper bound
$\mathcal Q(u)\le\frac13\norm u_3^3$.  The identities $\mathbb Pw(u)=u$,
$q(u)=w(u)-\mathbb Pw(u)$, the lower bound
$\norm u_3^3\le3C_{\mathbb P}^3\mathcal Q(u)$ and the bound
$\norm{q(u)}_3\le(1+C_{\mathbb P})\norm{w(u)}_3$ of
Lemma~\ref{lem:quotient-coercive} require $u$ to be solenoidal, and are
then valid for every solenoidal $u\in L^3$ by Lemma~\ref{lem:leray}(d);
in particular for every Navier--Stokes velocity $u(t)$ of
Proposition~\ref{prop:localtheory}, which lies in $L^2\cap L^3$ and is
solenoidal.  No smoothness of $w(u)$ or $q(u)$ is used or asserted
anywhere in this section.  The results of this part are properties of a
functional on $L^3$; they contain no estimate for Navier--Stokes
solutions, and no HIGH-PRESSURE, HIGH-STRAIN, critical, or regularity
result is asserted.
\end{remark}
```

Compile check: the block was spliced into a scratch copy of `main.tex`
(preamble additions above, the bibliography entries above, the rest of the
old `sec:quotient` retained after the block so that the labels
`eq:quotient-evolution` and `eq:quotient-gap` still exist, and a stub
`\phantomsection\label{prop:localtheory}` for the local-theory lane's
label) and compiled with `latexmk -pdf` (17 pages): no LaTeX errors, no undefined
or multiply defined references, no overfull boxes; page 10 was rendered and
inspected.  The paper repository was not modified.

## 3. External facts used

| Tag | Exact statement as used | Primary source and location | Status |
| --- | --- | --- | --- |
| F1 | (i) For a $\sigma$-finite measure space $(\Omega,\mathcal M,\mu)$ and $1<p<\infty$, "$L^p$ is reflexive for any $p$, $1<p<\infty$" (standing assumption (iii) of Ch. 4, p. 89: $\Omega$ $\sigma$-finite). (ii) "Assume that $E$ is a reflexive Banach space and let $(x_n)$ be a bounded sequence in $E$. Then there exists a subsequence $(x_{n_k})$ that converges in the weak topology $\sigma(E,E')$." | Brezis, *Functional Analysis, Sobolev Spaces and PDE*, Universitext, Springer 2011: Thm. 4.10, p. 95; Thm. 3.18, p. 69; Ch. 4 opening, p. 89 | [DI] (text read in the Toronto mirror PDF of the book, 614 pp., outline and pages 57-62, 67-72, 89-91, 95-97, 104-109 extracted) |
| F2 | (i) "Let $C$ be a convex subset of $E$. Then $C$ is closed in the weak topology $\sigma(E,E')$ if and only if it is closed in the strong topology." (ii) "If $x_n\rightharpoonup x$ weakly in $\sigma(E,E')$, then $(\|x_n\|)$ is bounded and $\|x\|\le\liminf\|x_n\|$." | Brezis, Thm. 3.7, p. 60; Prop. 3.5(iii), p. 58 | [DI] |
| F3 | (i) Young: $f\in L^1(\mathbb R^N)$, $g\in L^p(\mathbb R^N)$, $1\le p\le\infty$ ⟹ $y\mapsto f(x-y)g(y)$ integrable for a.e. $x$, $f*g\in L^p$, $\|f*g\|_p\le\|f\|_1\|g\|_p$. (ii) $f\in C_c^k(\mathbb R^N)$, $g\in L^1_{\rm loc}$ ⟹ $f*g\in C^k$, $D^\alpha(f*g)=(D^\alpha f)*g$. (iii) $\operatorname{supp}(f*g)\subset\operatorname{supp}f+\operatorname{supp}g$. (iv) $f\in L^p$, $1\le p<\infty$ ⟹ $\rho_n*f\to f$ in $L^p$. (v) $C_c(\mathbb R^N)$ dense in $L^p(\mathbb R^N)$, $1\le p<\infty$. | Brezis, Thm. 4.15 (p. 104), Prop. 4.20 (p. 107), Prop. 4.18 (p. 106), Thm. 4.22 (p. 109), Thm. 4.12 (p. 97) | [DI] |
| F4 | Plancherel: $\mathcal F$ extends from $L^1\cap L^2$ to a unitary operator on $L^2(\mathbb R^3;\mathbb C)$ with inverse extending $g\mapsto\check g$; $\int f\bar g=\int\mathcal Ff\,\overline{\mathcal Fg}$. | Grafakos, *Classical Fourier Analysis*, 3rd ed., GTM 249, Springer 2014, §2.2.4 (Plancherel and the $L^2$ extension); theorem numbers not verified in this pass | [MO] (section-level; the book text could not be fetched) |
| F5 | "If $u$ is square-integrable, then $Pu$ is the orthogonal projection of $u$ onto the space of square-integrable divergence-free vector fields; from Calderón-Zygmund theory we know that the projection $P$ is bounded on $L^p_x(\mathbb R^3)$ for every $1<p<\infty$, and from Fourier analysis we see that $P$ is also $H^s_x(\mathbb R^3)$ for every $s\in\mathbb R$. Note that if $u$ is square-integrable and divergence-free, then $Pu=u$." Used for $p=3$ and $p=3/2$ in the form $\|Pf\|_p\le C_p\|f\|_p$ for $f\in L^2\cap L^p$. Also: heat kernel $e^{t\Delta}f(x)=(4\pi t)^{-3/2}\int e^{-|x-y|^2/4t}f(y)dy$ for $f\in L^p$, and "From Young's inequality we thus record the dispersive inequality" (18); $\Delta^{-1}$ = multiplier $-1/(4\pi^2|\xi|^2)$, eq. (14). | Tao, *Localisation and compactness properties of the Navier-Stokes global regularity problem*, Anal. PDE 6 (2013) 25-107, p. 38 (Leray projection), p. 39 (heat semigroup, Young); arXiv:1108.1165 PDF pp. 17-18 | [DI] (arXiv PDF fetched and text-extracted this session; the printed formula $Pu:=\Delta^{-1}(\nabla\times\nabla\times u)$ is off by a sign relative to (14), recorded in a manuscript remark; the operator is pinned by the quoted sentence) |
| F5' | Underlying theorem for F5: Riesz transforms $R_j$ (symbol $-i\xi_j/\lvert\xi\rvert$) are bounded on $L^p(\mathbb R^n)$, $1<p<\infty$. | Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton 1970, Ch. II §2 (pp. 28-34), Ch. III §1 (pp. 54-60); pagination from cp01-literature-statements §6 (S1) | [MO] |

Everything else in the block (pointwise inequalities, Hölder, Tonelli,
dominated convergence, the Gaussian integral, product rule for weak
derivatives, the fundamental lemma of the calculus of variations, the
Schwartz property of $\check\eta$ and of $G_s\phi$, the truncation density)
is proved in the text or is a named elementary fact used with its argument.

## 4. Obligations not discharged

- **Q-4 import.** The $L^p$ boundedness of the Leray projection (F5) is
  imported, not proved. Its primary Calderón-Zygmund source (Stein) is
  [MO]; the directly inspected source is Tao p. 38, which itself cites
  "Calderón-Zygmund theory" without a reference. A Lean formalization
  must treat F5 as an axiom (mathlib-absent per cp01-mathlib-coverage).
- **F4 numbering.** Plancherel is cited at section level in Grafakos
  [MO]; the exact theorem number was not verified because no accessible
  copy was found. Any standard reference will do; the statement used is
  exact.
- **Not in this lane's scope (CP02-7):** Q-8 to Q-18, in particular the
  pullback statement `lem:gradient-closure`(b) of the CP01 draft (needed
  by the inner-variation lemma), the classical-trajectory class, the
  pressure lemma, the heat generator, the evolution identity, the
  low-strain bound, `hyp:highstrain`, and `prop:quotient-conditional`.
  The second half may cite the labels here; the draft's
  `lem:gradient-closure`(a) is delivered here as the whole of
  `lem:gradient-closure`, so the pullback part must be stated there as a
  separate lemma or the integrator must merge it as part (b).
- **`prop:localtheory` reference.** `rem:quotient-scope` cites
  Proposition~`prop:localtheory` (regularity package R of D2, local-theory
  lane). If that label differs after integration, one `\ref` changes.
- The hypothesis `eq:quotient-gap` (HIGH-STRAIN) is not proved and is not
  addressed here.

## 5. Frontier record

**MODE / RESULT.** INTEGRATE (paper text). Complete proofs for Q-0 to
Q-7 at the D5 standard, with every import isolated and labelled.

**CLAIM AND SCOPE.** For the functional $\mathcal Q(u)=\inf_{q\in\mathcal
G_3}\frac13\|u+q\|_3^3$ on real $L^3(\mathbb R^3;\mathbb R^3)$: a unique
minimizing representative $w(u)$ exists for every $u\in L^3$; it satisfies
$\operatorname{div}(|w|w)=0$ in distributions; $\mathcal Q$ is invariant
under adding gradients, cubically homogeneous, invariant under the
critical scaling $\lambda u(\lambda\cdot)$ and under translations,
nonincreasing under the heat semigroup, Lipschitz-stable in the sense of
`lem:quotient-stability`, and Fréchet differentiable with derivative
$h\mapsto\int|w|w\cdot h$ and remainder at most
$6(\|w\|_3+\|h\|_3)^{3/2}\|h\|_3^{3/2}$. The Leray projection, extended to
$L^3$ by the imported $L^p$ bound, annihilates $\mathcal G_3$ and fixes
every distributionally solenoidal $L^3$ field (proved by duality, with
the gradient potential $\Phi\in C^\infty\cap L^2$ constructed on the
Fourier side and a cutoff estimated by $\|\nabla\chi_R\|_6\|\Phi\|_2 =
O(R^{-1/2})$); hence $\|u\|_3^3\le3C_{\mathbb P}^3\mathcal Q(u)\le
C_{\mathbb P}^3\|u\|_3^3$ for solenoidal $u$. Constants: monotonicity
constant $1/2$ (exact identity), Lipschitz constant $1$, strong-convergence
bound $\|w'-w\|_3\le2(\|w\|_3+\|h\|_3)^{1/2}\|h\|_3^{1/2}$.

**EVIDENCE.** Every displayed inequality was rederived in this lane
(identity for $(j(a)-j(b))\cdot(a-b)$ checked on $a=1,b=-1$ and
$a=1,b=0$; the strict-convexity gap $\frac38(s+t)(s-t)^2$ expanded;
exponent bookkeeping of the remainder checked); Brezis theorem numbers and
the Chapter 4 $\sigma$-finiteness assumption read in the primary text;
Tao pp. 38-39 read in the arXiv PDF; scratch compile of the LaTeX block
passed. The HF17 note and its review were compared: the argument
structure (competitors $w+h$ and $w'-h$, cancellation, monotonicity) is
the reviewer's direct proof, with the reviewer's Radon-Riesz / uniform
convexity step replaced by the quantitative monotonicity step.

**FIRST GAP.** For this lane's deliverable: none within Q-0 to Q-7. The
single import without a directly inspected proof is F5 ($L^p$ boundedness
of the Leray projection; Stein [MO]). For the section as a whole the first
gap is unchanged: `eq:quotient-gap` (HIGH-STRAIN) is unproved.

**SURVIVING CONDITIONAL SUFFIX.** With this half in place, the second
half (CP02-7) can take `prop:quotient-derivative`,
`lem:quotient-minimizer`(c), `lem:quotient-heat`, `lem:quotient-coercive`
and `lem:quotient-stability` as proved inputs for the evolution identity
and the conditional implication `hyp:highstrain` ⟹ `hyp:critical`.

**NON-CLAIMS.** No estimate for any Navier-Stokes solution is made here;
no bound on the transport or strain term; no sign or quantitative
dissipation for $D_{\mathcal Q}$; no smoothness of $w$ or $q$; no
HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION or NS-R3 result; no
novelty claim for the construction; no Lean statement is claimed
type-checked.

**NEXT DISTINCT ACTION.** Independent proof audit of `lem:leray`(d)
(Steps 2-3) and of `prop:quotient-derivative`; then integration with the
CP02-7 half (merge `lem:gradient-closure` with its pullback part, confirm
the `prop:localtheory` label), the preamble and bibliography additions,
and a full-manuscript compile.
