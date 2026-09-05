# CP02-4: low-frequency pressure bound, Bernstein instance, existential equivalence

MODE: PROOF-WRITING (CP02 lane 4). Date: 2026-09-05. Standard: complete
paper proof, every step written, every external fact with a primary source
and a [DI]/[MO] label. Nothing here proves or approaches HIGH-PRESSURE,
HIGH-STRAIN, CRITICAL, ABSORPTION, or NS-R3.

Inputs read in full: `/home/ert/proj/navier-paper/main.tex` (562 lines),
`research/evidence/cp01-manuscript-obligations.md`,
`research/evidence/cp01-literature-statements.md`. Consulted for label
consistency: `cp01-quotient-section-structure.md` (its `lem:lowpass`,
`lem:quotient-lowstrain`), `cp01-lean-statement-design.md` (`LowPassProfile`,
T7, T19), `cp01-critic.md` (K8, U15), `review-frequency.md`.

Controller decisions D1–D5 are followed as written. The regularity package R
of D2 is assumed under the name `Proposition prop:localtheory`; the
continuation theorem is used in its D3 form; `prop:pressure` is used in its
integrated P-3 form with the P-0 integrands; the normalised pressure
`p = R_iR_j(u_iu_j)` is Tao's, by `cp01-literature-statements` §7.3.

---

## 1. Obligations discharged

| Id | Obligation (from `cp01-manuscript-obligations.md`) | Where |
| --- | --- | --- |
| F-1 (convention) | Littlewood–Paley convention fixed as a labelled definition: real, even, `0 ≤ φ ≤ 1`, `φ = 1` on `|ξ| ≤ 1`, `supp φ ⊂ {|ξ| ≤ 2}`; `S_J = P_{≤2^J}` (Tao's inhomogeneous projection); `ψ(ξ) = φ(ξ) − φ(2ξ)`; proof that on `L²` the inhomogeneous `S_J` and the homogeneous `Σ_{j≤J}Δ_j` coincide (partial sums converge in `L²`; symbols agree off `{0}`) | `def:lp`, `lem:lp-coincide` |
| F-1 (kernel) | `m_J^{ij} ∈ L¹∩L²`, `‖m_J^{ij}‖₁ ≤ 2^{3J}‖φ‖₁ ≤ (4π/3)2^{3(J+1)} = (32π/3)2^{3J}`; `K_J := (m_J)^∨` bounded, continuous, real, `‖K_J‖_∞ ≤ ‖m_J‖₁` **with constant exactly 1** under the `e^{−2πix·ξ}` convention (verified: `|∫e^{2πix·ξ}m(ξ)dξ| ≤ ∫|m|`, no `(2π)^{−3}`) | `lem:riesz-kernel` |
| F-1 (convolution representation) | `S_JR_iR_jf = K_J∗f` a.e. for `f ∈ L¹∩L²`, proved from the `L¹` convolution theorem plus Plancherel by truncating the `L²` kernel (`K_J ∉ L¹` in general; no `L¹` kernel bound is claimed or used) | `lem:fourier-tools`(iv), `lem:riesz-kernel`(c) |
| F-1 (measurability of `L_J`) | `t ↦ L_J(t)` is continuous on `[0,T_*)` | `prop:lowpressure`(ii) |
| F-1 (constant) | `prop:lowpressure` with the explicit constant `C = 32π/3` (sharper: `‖φ‖₁`), independent of `ν, u_0, J, H, τ` | `prop:lowpressure` |
| P-0 (shared) | `L_J`, `Q_J`, `P_3` written through `Γ(u) = u_iu_j∂_ju_i/|u|` (`:= 0` where `u = 0`), with the pointwise bound `|Γ(u)| ≤ |u||∇u|` proved, and `P_3 = L_J + Q_J` with absolutely convergent integrals | `def:pressure-work`, `lem:gamma` |
| Q-17 (Bernstein input) | `‖∇S_Lf‖_∞ ≤ C_B 2^{5L/2}‖f‖₂` for `f ∈ L²`, `C_B = ‖∇κ‖₂ = 2π‖ |ξ|φ ‖₂ ≤ 16π(2π/5)^{1/2}`; Lipschitz form giving `∇S_Lu ∈ C([0,T];L^∞)`; `∇S_L f = S_L∇f` on `H¹` | `lem:bernstein` |
| (prose after `hyp:absorption`) | `prop:lowpressure` + `hyp:highpressure` ⟹ `hyp:absorption` with `A = A_low + A_high`, `J = J(ν,u_0,H)` | `lem:absorption-split` |
| X-1 | Existential equivalence as `Proposition prop:existential-equivalence` with both directions proved; converse via `‖p_{>0}‖₃ ≤ (1+‖κ‖₁)‖p‖₃`, `p ∈ C([0,H];L³)` from R, `S_0` bounded on `L³` by Minkowski with the Schwartz kernel `κ` (proved), Hölder `1/3+1/6+1/2 = 1`, continuity of `Q_0`, `A_high := ∫_0^H|Q_0|`; scoping sentences retained verbatim | `prop:existential-equivalence`, `rem:existential-scope` |

New theorem environments used: `definition` and `lemma` (the integrator must
add `\newtheorem{lemma}[theorem]{Lemma}` and
`\newtheorem{definition}[theorem]{Definition}` to `main.tex`). New labels:
`def:lp`, `lem:lp-coincide`, `lem:fourier-tools`, `lem:lowpass-kernel`,
`lem:riesz-kernel`, `def:pressure-work`, `lem:gamma`, `lem:bernstein`,
`lem:absorption-split`, `prop:existential-equivalence`,
`rem:lowpressure-constant`, `rem:existential-scope`, `eq:lp-symbol`,
`eq:riesz-symbol`, `eq:gamma`. Retained labels: `prop:lowpressure`,
`eq:lowpressure`, `hyp:highpressure`, `hyp:absorption` (unchanged; their
position is marked by a comment).

Notation note for the integrator. D1 assigns `ψ` to the annular symbol
`φ(ξ) − φ(2ξ)`; the quotient lane's `lem:lowpass` uses `ψ` for the kernel of
`S_L`. Here the kernel is `κ := φ^∨`, so the quotient lane's `‖∇ψ‖₂` is this
lane's `‖∇κ‖₂ = C_B`; `lem:bernstein` below can replace `lem:lowpass` verbatim
(it proves the same bound and the `C([0,T];L^∞)` continuity that
`lem:quotient-lowstrain` uses). One of the two letters must be renamed at
integration.

---

## 2. Replacement text

Placement: replaces, in §4 of `main.tex`, everything from "Fix a smooth
homogeneous Littlewood--Paley partition" through the end of the proof of
`prop:lowpressure`; keeps `hyp:highpressure` and `hyp:absorption` unchanged
at the marked position; replaces the paragraph "At these existential
quantifiers, …" and the sentence "Proposition~\ref{prop:lowpressure} and
Hypothesis~\ref{hyp:highpressure} imply Hypothesis~\ref{hyp:absorption}, with
$A=A_{\rm low}+A_{\rm high}$." The remaining sentences of that paragraph
("The high-frequency hypothesis is the refined first new gap; …") and the
display `eq:pressure-consequence` are not touched.

```latex
%% ---- CP02-4: Littlewood--Paley convention, kernel bounds, low-frequency
%% ---- pressure work, Bernstein instance, existential equivalence.
%% Requires in the preamble:
%%   \newtheorem{lemma}[theorem]{Lemma}
%%   \newtheorem{definition}[theorem]{Definition}

\begin{definition}[Fourier, Riesz, and Littlewood--Paley conventions]
\label{def:lp}
For $f\in L^1(\R^3)$ put $\hat f(\xi)=\int_{\R^3}e^{-2\pi ix\cdot\xi}f(x)\,dx$
and $f^\vee(x)=\hat f(-x)$.  The map $f\mapsto\hat f$ is an $L^2$ isometry
on $L^1\cap L^2$ and extends uniquely to a unitary operator
$\mathcal F$ on $L^2(\R^3)$ with inverse $\mathcal F^{-1}$ extending
$f\mapsto f^\vee$ (Plancherel); we keep writing $\hat f=\mathcal Ff$ for
$f\in L^2$.  For a bounded measurable $m:\R^3\to\mathbb C$ the
\emph{multiplier} $T_m f:=\mathcal F^{-1}(m\hat f)$ is bounded on $L^2$ with
$\norm{T_mf}_2\le\norm m_\infty\norm f_2$, and $T_mT_{m'}=T_{mm'}$.
Operators on scalar functions act componentwise on vector fields.

The Riesz transforms are $R_j:=T_{r_j}$ with $r_j(\xi)=-i\xi_j/|\xi|$ for
$\xi\ne0$ ($r_j(0):=0$), so that
\begin{equation}\label{eq:riesz-symbol}
 R_iR_j=T_{m^{ij}},\qquad m^{ij}(\xi)=-\frac{\xi_i\xi_j}{|\xi|^2}\quad(\xi\ne0),
 \qquad m^{ij}(0):=0 .
\end{equation}
Since $\widehat{\partial_jf}=2\pi i\xi_j\hat f$ and $\Delta^{-1}$ is the
multiplier $-(4\pi^2|\xi|^2)^{-1}$, the operator $-\Delta^{-1}\partial_i\partial_j$
has the same symbol $m^{ij}$; hence $p=R_iR_j(u_iu_j)$ (summed over $i,j$) is
exactly the normalised pressure $p=-\Delta^{-1}\partial_i\partial_j(u_iu_j)$ of
Tao \cite[eq.~(9)]{Tao2013}.

Fix once and for all a real-valued, even
$\varphi\in C_c^\infty(\R^3)$ with $0\le\varphi\le1$, $\varphi(\xi)=1$ for
$|\xi|\le1$, and $\varphi(\xi)=0$ for $|\xi|\ge2$.  For $J\in\mathbb Z$ set
\begin{equation}\label{eq:lp-symbol}
 S_J:=T_{\varphi(2^{-J}\cdot)},\qquad
 \psi(\xi):=\varphi(\xi)-\varphi(2\xi),\qquad
 \Delta_j:=T_{\psi(2^{-j}\cdot)}\quad(j\in\mathbb Z),
\end{equation}
so that $S_J$ is Tao's projection $P_{\le 2^J}$
\cite[p.~40]{Tao2013}.  For $p\in L^2$ write
$p_{\le J}:=S_Jp$ and $p_{>J}:=p-p_{\le J}$.  We put
$C_\varphi:=\norm\varphi_{L^1(\R^3)}$; since $0\le\varphi\le\mathbf 1_{\{|\xi|\le2\}}$,
\[
 C_\varphi\le|B(0,2)|=\tfrac{4\pi}3\cdot 8=\tfrac{32\pi}3 .
\]
\end{definition}

\begin{lemma}[Homogeneous and inhomogeneous low-pass agree on $L^2$]
\label{lem:lp-coincide}
For every $f\in L^2(\R^3)$ and $J\in\mathbb Z$,
\[
 \sum_{j=-N}^{J}\Delta_jf\;\longrightarrow\;S_Jf
 \quad\text{in }L^2(\R^3)\text{ as }N\to\infty .
\]
Hence $S_J=\sum_{j\le J}\Delta_j$ on $L^2$, the series converging in $L^2$,
and no polynomial ambiguity arises.
\end{lemma}

\begin{proof}
For $\xi\in\R^3$ and $N\ge0$ the sum telescopes:
\[
 \sum_{j=-N}^{J}\psi(2^{-j}\xi)
 =\sum_{j=-N}^{J}\bigl(\varphi(2^{-j}\xi)-\varphi(2^{-(j-1)}\xi)\bigr)
 =\varphi(2^{-J}\xi)-\varphi(2^{N+1}\xi).
\]
Thus $\sum_{j=-N}^J\Delta_jf=S_Jf-T_{\varphi(2^{N+1}\cdot)}f$, and by
Plancherel
\[
 \Bigl\|S_Jf-\sum_{j=-N}^{J}\Delta_jf\Bigr\|_2^2
 =\int_{\R^3}\varphi(2^{N+1}\xi)^2|\hat f(\xi)|^2\,d\xi .
\]
For every $\xi\ne0$ one has $\varphi(2^{N+1}\xi)=0$ as soon as
$2^{N+1}|\xi|\ge2$, so the integrand tends to $0$ for every $\xi\ne0$; it is
dominated by $|\hat f|^2\in L^1$.  Dominated convergence gives the claim.
(At $\xi=0$ the symbols differ, $\psi(0)=0$ while $\varphi(0)=1$; a single
point is a null set, so the two $L^2$ multipliers coincide.)
\end{proof}

\begin{lemma}[Convolution and Fourier tools]\label{lem:fourier-tools}
Let $n=3$.
\begin{itemize}
\item[(i)] (Minkowski) If $g\in L^1$ and $f\in L^q$, $1\le q\le\infty$, then
$g*f(x)=\int g(x-y)f(y)\,dy$ converges absolutely for a.e.\ $x$ and
$\norm{g*f}_q\le\norm g_1\norm f_q$.  Convolution is commutative on $\R^3$.
\item[(ii)] (Endpoint) If $g\in L^r$ and $f\in L^{r'}$, $1\le r\le\infty$,
$1/r+1/r'=1$, then $g*f(x)$ converges absolutely for \emph{every} $x$ and
$|g*f(x)|\le\norm g_r\norm f_{r'}$.  If moreover $g$ is bounded and
continuous and $f\in L^1$, then $g*f$ is bounded and continuous.
\item[(iii)] If $m\in L^1\cap L^2$, then $m^\vee(x)=\int e^{2\pi ix\cdot\xi}m(\xi)\,d\xi$
is continuous with $\norm{m^\vee}_\infty\le\norm m_1$, it coincides a.e.\ with
$\mathcal F^{-1}m$, $\norm{m^\vee}_2=\norm m_2$, and $\widehat{m^\vee}=m$ a.e.
If $m$ is real and even, $m^\vee$ is real and even.
\item[(iv)] (Convolution theorem, $L^2*L^1$) If $g\in L^2$ and $f\in L^1$,
then $g*f\in L^2$ and $\mathcal F(g*f)=\hat g\,\hat f$ a.e.
\end{itemize}
\end{lemma}

\begin{proof}
(i) is Minkowski's inequality \cite[Thm.~1.2.10]{Grafakos2014};
commutativity is the change of variables $y\mapsto x-y$.

(ii) H\"older's inequality applied to $y\mapsto g(x-y)$ and $f$ gives
absolute convergence and the bound for every $x$.  If $g$ is bounded and
continuous and $x_k\to x$, then $g(x_k-y)f(y)\to g(x-y)f(y)$ for every $y$
with $|g(x_k-y)f(y)|\le\norm g_\infty|f(y)|\in L^1$, so $g*f(x_k)\to g*f(x)$
by dominated convergence.

(iii) The integral converges absolutely, $|m^\vee(x)|\le\norm m_1$, and
continuity follows by dominated convergence as in (ii).  The
$L^2$ operator $\mathcal F^{-1}$ is the unique bounded extension of
$m\mapsto m^\vee$ from $L^1\cap L^2$ \cite[pp.~113--114]{Grafakos2014}, so
$\mathcal F^{-1}m=m^\vee$ a.e., and Plancherel gives
$\norm{m^\vee}_2=\norm m_2$ and $\widehat{m^\vee}=\mathcal F\mathcal F^{-1}m=m$ a.e.
If $m$ is real and even, then
$\overline{m^\vee(x)}=\int e^{-2\pi ix\cdot\xi}m(\xi)\,d\xi
=\int e^{2\pi ix\cdot\eta}m(-\eta)\,d\eta=m^\vee(x)$, and
$m^\vee(-x)=m^\vee(x)$ by the same substitution.

(iv) By (i) (with the roles of $g$ and $f$ exchanged, using commutativity),
$g*f\in L^2$ with $\norm{g*f}_2\le\norm g_2\norm f_1$.  Put
$g_k:=g\mathbf 1_{B(0,k)}\in L^1\cap L^2$.  For integrable functions the
Fourier transform of a convolution is the product of the transforms
\cite[Prop.~2.2.11(12) and p.~113]{Grafakos2014}, so
$\widehat{g_k*f}=\hat g_k\hat f$; here $g_k*f\in L^1\cap L^2$ by (i), and on
$L^1\cap L^2$ the $L^1$ transform and $\mathcal F$ agree
\cite[p.~113]{Grafakos2014}.  Now $\norm{g_k-g}_2\to0$ by dominated
convergence, hence $\norm{(g_k-g)*f}_2\le\norm{g_k-g}_2\norm f_1\to0$ by (i),
and $\norm{\hat g_k\hat f-\hat g\hat f}_2\le\norm{\hat f}_\infty\norm{g_k-g}_2\to0$
by Plancherel and $\norm{\hat f}_\infty\le\norm f_1$
\cite[Prop.~2.2.11(1)]{Grafakos2014}.  Since $\mathcal F$ is an isometry of
$L^2$, $\mathcal F(g*f)=\lim_k\mathcal F(g_k*f)=\lim_k\hat g_k\hat f=\hat g\hat f$
in $L^2$, hence a.e.
\end{proof}

\begin{lemma}[Kernel of the low-pass projection]\label{lem:lowpass-kernel}
Let $\kappa:=\varphi^\vee$ and $\kappa_J(x):=2^{3J}\kappa(2^Jx)$.  Then:
\begin{itemize}
\item[(a)] $\kappa\in\mathcal S(\R^3)$ is real and even, $\hat\kappa=\varphi$,
$\hat\kappa_J(\xi)=\varphi(2^{-J}\xi)$, and $\norm{\kappa_J}_1=\norm\kappa_1$.
\item[(b)] For $f\in L^2$, $S_Jf=\kappa_J*f$ a.e.; consequently, for
$f\in L^2\cap L^q$, $1\le q\le\infty$, $\norm{S_Jf}_q\le\norm\kappa_1\norm f_q$.
\item[(c)] For $f\in L^2$, $\kappa_J*f$ is $C^\infty$ and
$\partial^\alpha(\kappa_J*f)=(\partial^\alpha\kappa_J)*f$ for every
multi-index $\alpha$, each of these being a bounded continuous function.
\item[(d)] For $f\in H^1$ and $k\in\{1,2,3\}$, $\partial_kS_Jf=S_J\partial_kf$.
\end{itemize}
\end{lemma}

\begin{proof}
(a) $\varphi\in C_c^\infty\subset\mathcal S$, and the Fourier transform is a
bijection of $\mathcal S$ onto itself \cite[Cor.~2.2.15]{Grafakos2014};
since $\varphi^\vee=\hat\varphi(-\cdot)$ and reflection preserves $\mathcal S$,
$\kappa\in\mathcal S$.  Realness and evenness are
Lemma~\ref{lem:fourier-tools}(iii).  Fourier inversion on $\mathcal S$
\cite[Thm.~2.2.14(2)]{Grafakos2014} gives $\hat\kappa=(\varphi^\vee)^\wedge=\varphi$.
The substitution $x=2^{-J}y$ gives
$\hat\kappa_J(\xi)=\int e^{-2\pi i2^{-J}y\cdot\xi}\kappa(y)\,dy=\varphi(2^{-J}\xi)$
and $\norm{\kappa_J}_1=\norm\kappa_1$.

(b) Apply Lemma~\ref{lem:fourier-tools}(iv) with $g=f\in L^2$ and the
integrable function $\kappa_J$: $\mathcal F(\kappa_J*f)=\hat\kappa_J\hat f
=\varphi(2^{-J}\cdot)\hat f=\widehat{S_Jf}$, so $\kappa_J*f=S_Jf$ a.e.  The
$L^q$ bound is Lemma~\ref{lem:fourier-tools}(i).

(c) Let $h\in\mathcal S$ and $f\in L^2$.  For fixed $x$ and $0<|s|\le1$,
\[
 \frac{(h*f)(x+se_k)-(h*f)(x)}{s}
 =\int\frac{h(x+se_k-y)-h(x-y)}{s}f(y)\,dy .
\]
The difference quotient tends to $\partial_kh(x-y)$ for every $y$, and by
the mean value theorem it is bounded by
$\sup_{|\sigma|\le1}|\partial_kh(x-y+\sigma e_k)|\le C_h(1+|x-y|)^{-4}$,
because $|\partial_kh(w)|\le C_h'(1+|w|)^{-4}$ and $1+|z|\le2(1+|w|)$ for
$|z-w|\le1$.  The majorant $(1+|x-y|)^{-4}|f(y)|$ is integrable in $y$ by
Cauchy--Schwarz, so dominated convergence gives
$\partial_k(h*f)(x)=(\partial_kh*f)(x)$; boundedness and continuity of
$(\partial_kh)*f$ follow from Lemma~\ref{lem:fourier-tools}(ii) with
$r=2$ (continuity by the same dominated-convergence argument, the
majorant now being $(1+|x_0-y|)^{-4}|f(y)|$ for $|x-x_0|\le1$).  Induction
on $|\alpha|$ with $h=\partial^\alpha\kappa_J\in\mathcal S$ completes (c).

(d) For $f\in H^1$, $\widehat{\partial_kf}=2\pi i\xi_k\hat f$ in $L^2$, so
$\widehat{\partial_kS_Jf}=2\pi i\xi_k\varphi(2^{-J}\xi)\hat f
=\varphi(2^{-J}\xi)\widehat{\partial_kf}=\widehat{S_J\partial_kf}$.
\end{proof}

\begin{lemma}[Kernel of $S_JR_iR_j$]\label{lem:riesz-kernel}
For $i,j\in\{1,2,3\}$ and $J\in\mathbb Z$ let
\[
 m^{ij}_J(\xi):=\varphi(2^{-J}\xi)\,m^{ij}(\xi)
 =-\varphi(2^{-J}\xi)\frac{\xi_i\xi_j}{|\xi|^2}\quad(\xi\ne0),
 \qquad m^{ij}_J(0):=0,
\]
and $K^{ij}_J:=(m^{ij}_J)^\vee$.  Then:
\begin{itemize}
\item[(a)] $m^{ij}_J$ is bounded, measurable, real, and even, with
$|m^{ij}_J(\xi)|\le\varphi(2^{-J}\xi)\le\mathbf 1_{\{|\xi|\le2^{J+1}\}}$; hence
$m^{ij}_J\in L^1\cap L^2$ and
\[
 \norm{m^{ij}_J}_1\le\int_{\R^3}\varphi(2^{-J}\xi)\,d\xi
 =2^{3J}C_\varphi\le\tfrac{32\pi}{3}\,2^{3J}
 =\tfrac{4\pi}{3}\,2^{3(J+1)} .
\]
\item[(b)] $K^{ij}_J$ is a real, even, bounded, continuous function with
$\norm{K^{ij}_J}_\infty\le\norm{m^{ij}_J}_1\le\frac{32\pi}{3}2^{3J}$; moreover
$K^{ij}_J\in L^2$ and $\widehat{K^{ij}_J}=m^{ij}_J$ a.e.  No $L^1$ bound on
$K^{ij}_J$ is claimed: $m^{ij}_J$ is discontinuous at $\xi=0$, and none is
needed.
\item[(c)] For $f\in L^1\cap L^2$, $S_JR_iR_jf=K^{ij}_J*f$ a.e., and
$K^{ij}_J*f$ is bounded and continuous with
$\norm{K^{ij}_J*f}_\infty\le\norm{m^{ij}_J}_1\norm f_1$.
\item[(d)] (Bilinear form) For all $z,c,d\in\R^3$,
\[
 \Bigl|\sum_{i,j=1}^3K^{ij}_J(z)\,c_id_j\Bigr|\le 2^{3J}C_\varphi\,|c|\,|d| .
\]
\end{itemize}
\end{lemma}

\begin{proof}
(a) Measurability and boundedness are clear; $|\xi_i\xi_j|\le|\xi|^2$ gives
$|m^{ij}_J|\le\varphi(2^{-J}\cdot)$, which is supported in
$\{|\xi|\le2^{J+1}\}$ and bounded by $1$.  $\varphi$ is real and even and
$\xi\mapsto\xi_i\xi_j/|\xi|^2$ is real and even, so $m^{ij}_J$ is.  The
substitution $\eta=2^{-J}\xi$ gives $\int\varphi(2^{-J}\xi)\,d\xi=2^{3J}\norm\varphi_1$,
and $C_\varphi\le32\pi/3$ was noted in Definition~\ref{def:lp}.

(b) is Lemma~\ref{lem:fourier-tools}(iii).  Note that with the convention of
Definition~\ref{def:lp} the inverse transform carries no normalising factor,
so $|K^{ij}_J(x)|=|\int e^{2\pi ix\cdot\xi}m^{ij}_J(\xi)\,d\xi|\le\norm{m^{ij}_J}_1$
with constant exactly $1$.

(c) By Definition~\ref{def:lp}, $S_JR_iR_jf=T_{\varphi(2^{-J}\cdot)}T_{m^{ij}}f
=T_{m^{ij}_J}f=\mathcal F^{-1}(m^{ij}_J\hat f)$.  By
Lemma~\ref{lem:fourier-tools}(iv) with $g=K^{ij}_J\in L^2$,
$\mathcal F(K^{ij}_J*f)=\widehat{K^{ij}_J}\hat f=m^{ij}_J\hat f$, so
$K^{ij}_J*f=\mathcal F^{-1}(m^{ij}_J\hat f)=S_JR_iR_jf$ a.e.  Boundedness,
continuity, and the bound are Lemma~\ref{lem:fourier-tools}(ii) with $r=\infty$.

(d) The sum is a finite sum of absolutely convergent integrals, so
\[
 \sum_{i,j}K^{ij}_J(z)c_id_j
 =-\int_{\R^3}e^{2\pi iz\cdot\xi}\varphi(2^{-J}\xi)\frac{(c\cdot\xi)(d\cdot\xi)}{|\xi|^2}\,d\xi ,
\]
and $|(c\cdot\xi)(d\cdot\xi)|\le|c||d||\xi|^2$ by Cauchy--Schwarz, so the
modulus is at most $|c||d|\int\varphi(2^{-J}\xi)\,d\xi=2^{3J}C_\varphi|c||d|$.
\end{proof}

\begin{definition}[Pressure-work integrand and its frequency split]
\label{def:pressure-work}
For a $C^1$ vector field $v:\R^3\to\R^3$ define pointwise
\begin{equation}\label{eq:gamma}
 \Gamma(v)(x):=
 \begin{cases}
  \dfrac{\sum_{i,j=1}^3v_i(x)v_j(x)\,\partial_jv_i(x)}{|v(x)|}, & v(x)\ne0,\\[1.2ex]
  0, & v(x)=0 ,
 \end{cases}
\end{equation}
which on $\{v\ne0\}$ equals $v\cdot\nabla|v|$ and is the integrand of
Proposition~\ref{prop:pressure}.  With $g(a):=a\otimes a/|a|$ for $a\ne0$,
$g(0):=0$, one has $\Gamma(v)=g(v):\nabla v=\sum_{i,j}g_{ij}(v)\,\partial_jv_i$.
For the solution of Proposition~\ref{prop:localtheory} and $0\le t<T_*$ put
\[
 P_3(t)=\int_{\R^3}p\,\Gamma(u)\,dx,\qquad
 L_J(t)=\int_{\R^3}p_{\le J}\,\Gamma(u)\,dx,\qquad
 Q_J(t)=\int_{\R^3}p_{>J}\,\Gamma(u)\,dx ,
\]
all evaluated at time $t$.  Norms of matrices are Frobenius norms, so
$|a\otimes a|=|a|^2$ and $\norm{u\otimes u}_1=\norm u_2^2$.
\end{definition}

\begin{lemma}[Pointwise and time-continuity facts]\label{lem:gamma}
\begin{itemize}
\item[(a)] $|g(a)|=|a|$ and $|g(a)-g(b)|\le3|a-b|$ for all $a,b\in\R^3$.
\item[(b)] $|\Gamma(v)|\le|v|\,|\nabla v|$ pointwise, where
$|\nabla v|^2=\sum_{i,j}(\partial_jv_i)^2$.
\item[(c)] Let $T<T_*$.  For $t\in[0,T]$, $\Gamma(u(t))$ is a continuous function
of $x$ with $\norm{\Gamma(u(t))}_1\le\norm{u(t)}_2\norm{\nabla u(t)}_2$ and
$\norm{\Gamma(u(t))}_{3/2}\le\norm{u(t)}_6\norm{\nabla u(t)}_2$; the maps
$t\mapsto\Gamma(u(t))$ belong to $C([0,T];L^1)$ and to $C([0,T];L^{3/2})$.
\item[(d)] For $0\le t<T_*$ and $J\in\mathbb Z$ the integrals defining
$P_3(t)$, $L_J(t)$, $Q_J(t)$ converge absolutely and $P_3=L_J+Q_J$.
\end{itemize}
\end{lemma}

\begin{proof}
(a) $|g(a)|=|a\otimes a|/|a|=|a|^2/|a|=|a|$.  On $\R^3\setminus\{0\}$ the map
$g$ is $C^1$ with
\[
 Dg(a)[h]=\frac{h\otimes a+a\otimes h}{|a|}-\frac{(a\cdot h)\,a\otimes a}{|a|^3},
 \qquad |Dg(a)[h]|\le\frac{2|h||a|}{|a|}+\frac{|a||h||a|^2}{|a|^3}=3|h| .
\]
If the segment $[a,b]$ does not contain $0$, the mean value inequality
along the segment gives $|g(a)-g(b)|\le3|a-b|$.  If $0\in[a,b]$, then
$|a-b|=|a|+|b|$ and $|g(a)-g(b)|\le|g(a)|+|g(b)|=|a|+|b|=|a-b|$.

(b) On $\{v\ne0\}$, write $\Gamma(v)=|v|^{-1}\sum_jv_j\bigl(\sum_iv_i\partial_jv_i\bigr)$.
Cauchy--Schwarz in $i$ gives $|\sum_iv_i\partial_jv_i|\le|v||\partial_jv|$
with $|\partial_jv|^2=\sum_i(\partial_jv_i)^2$, and then Cauchy--Schwarz in
$j$ gives $|\sum_jv_j(\cdots)|\le|v|\cdot|v|\bigl(\sum_j|\partial_jv|^2\bigr)^{1/2}
=|v|^2|\nabla v|$.  Divide by $|v|$.  On $\{v=0\}$ both sides vanish.

(c) By Proposition~\ref{prop:localtheory}, $u(t)\in C^1$ with
$u\in C([0,T];L^2\cap L^6)$ and $\nabla u\in C([0,T];L^2)$.  Since
$g$ is continuous and $\Gamma(u)=g(u):\nabla u$, $\Gamma(u(t))$ is continuous
in $x$.  The two norm bounds follow from (b) and H\"older
($1=\tfrac12+\tfrac12$, respectively $\tfrac23=\tfrac16+\tfrac12$).  For
$s,t\in[0,T]$, using $|A:B|\le|A||B|$ and (a),
\[
 \bigl|\Gamma(u(t))-\Gamma(u(s))\bigr|
 \le\bigl|g(u(t))-g(u(s))\bigr|\,|\nabla u(t)|+|g(u(s))|\,|\nabla u(t)-\nabla u(s)|
 \le3|u(t)-u(s)||\nabla u(t)|+|u(s)||\nabla u(t)-\nabla u(s)| ,
\]
so by H\"older
$\norm{\Gamma(u(t))-\Gamma(u(s))}_1\le3\norm{u(t)-u(s)}_2\norm{\nabla u(t)}_2
+\norm{u(s)}_2\norm{\nabla u(t)-\nabla u(s)}_2$ and
$\norm{\Gamma(u(t))-\Gamma(u(s))}_{3/2}\le3\norm{u(t)-u(s)}_6\norm{\nabla u(t)}_2
+\norm{u(s)}_6\norm{\nabla u(t)-\nabla u(s)}_2$; both tend to $0$ as $s\to t$.

(d) By Proposition~\ref{prop:localtheory}, $p(t)\in L^2\cap L^\infty$, and by
Lemma~\ref{lem:lowpass-kernel}(b) $p_{\le J}(t)\in L^\infty$ with
$\norm{p_{\le J}}_\infty\le\norm\kappa_1\norm p_\infty$; hence
$p_{>J}(t)\in L^\infty$ as well.  Each of $\int|p||\Gamma(u)|$,
$\int|p_{\le J}||\Gamma(u)|$, $\int|p_{>J}||\Gamma(u)|$ is at most the
$L^\infty$ norm of the pressure factor times $\norm{\Gamma(u(t))}_1<\infty$ by
(c).  Linearity of the integral and $p=p_{\le J}+p_{>J}$ give $P_3=L_J+Q_J$.
\end{proof}

\begin{proposition}[Low-frequency pressure work]\label{prop:lowpressure}
Let $C:=32\pi/3$.  For every integer $J$ and every $0\le t<T_*$:
\begin{itemize}
\item[(i)] $p_{\le J}(t)$ coincides a.e.\ with a real, bounded, continuous
function, and
\[
 \norm{p_{\le J}(t)}_\infty
 \le C_\varphi2^{3J}\norm{u(t)\otimes u(t)}_1
 =C_\varphi2^{3J}\norm{u(t)}_2^2
 \le C2^{3J}\norm{u_0}_2^2 .
\]
\item[(ii)] $|L_J(t)|\le C2^{3J}\norm{u_0}_2^3\norm{\nabla u(t)}_2$, and
$t\mapsto L_J(t)$ is continuous on $[0,T_*)$.
\item[(iii)] For every $H<\infty$ and $0<\tau<\min\{H,T_*\}$,
\begin{equation}\label{eq:lowpressure}
 \left|\int_0^\tau L_J(t)\,dt\right|
 \leq C2^{3J}\norm{u_0}_2^4\left(\frac{H}{2\nu}\right)^{1/2}
 =:A_{\rm low}(\nu,u_0,H,J).
\end{equation}
\end{itemize}
\end{proposition}

\begin{proof}
Fix $t<T_*$ and write $u=u(t)$, $p=p(t)$.  By
Proposition~\ref{prop:localtheory}, $u\in L^2\cap L^\infty$, so
$f_{ij}:=u_iu_j\in L^1\cap L^2$ (indeed $\norm{f_{ij}}_1\le\norm u_2^2$ by
Cauchy--Schwarz and $\norm{f_{ij}}_2\le\norm u_\infty\norm u_2$), and
$p=\sum_{i,j}R_iR_jf_{ij}$ in $L^2$ (Definition~\ref{def:lp}; this is the
normalised pressure of Proposition~\ref{prop:pressure}).

(i) By linearity of $S_J$ and Lemma~\ref{lem:riesz-kernel}(c),
\[
 p_{\le J}=S_Jp=\sum_{i,j}S_JR_iR_jf_{ij}=\sum_{i,j}K^{ij}_J*f_{ij}
 \quad\text{a.e.},
\]
and the right side is a finite sum of real, bounded, continuous functions
(Lemma~\ref{lem:riesz-kernel}(b),(c)).  For every $x$, interchanging the
finite sum with the absolutely convergent integrals and applying
Lemma~\ref{lem:riesz-kernel}(d) with $c=d=u(y)$,
\[
 \Bigl|\sum_{i,j}K^{ij}_J*f_{ij}(x)\Bigr|
 =\Bigl|\int_{\R^3}\sum_{i,j}K^{ij}_J(x-y)\,u_i(y)u_j(y)\,dy\Bigr|
 \le2^{3J}C_\varphi\int_{\R^3}|u(y)|^2\,dy
 =C_\varphi2^{3J}\norm{u\otimes u}_1 .
\]
Finally $\norm{u(t)}_2\le\norm{u_0}_2$ by Proposition~\ref{prop:energy} and
$C_\varphi\le C$.

(ii) By Lemma~\ref{lem:gamma}(b),(c) and (i),
\[
 |L_J(t)|\le\norm{p_{\le J}(t)}_\infty\int_{\R^3}|u||\nabla u|\,dx
 \le\norm{p_{\le J}(t)}_\infty\norm{u(t)}_2\norm{\nabla u(t)}_2
 \le C2^{3J}\norm{u_0}_2^3\norm{\nabla u(t)}_2 .
\]
For continuity fix $T<T_*$ and $s,t\in[0,T]$.  Since
$u_i(t)u_j(t)-u_i(s)u_j(s)=(u_i(t)-u_i(s))u_j(t)+u_i(s)(u_j(t)-u_j(s))$, the
bilinear bound of Lemma~\ref{lem:riesz-kernel}(d) gives, for every $x$,
\[
 |p_{\le J}(t)(x)-p_{\le J}(s)(x)|
 \le2^{3J}C_\varphi\int_{\R^3}|u(t)-u(s)|\bigl(|u(t)|+|u(s)|\bigr)\,dy
 \le2^{3J}C_\varphi\norm{u(t)-u(s)}_2\bigl(\norm{u(t)}_2+\norm{u(s)}_2\bigr),
\]
so $p_{\le J}\in C([0,T];L^\infty)$ because $u\in C([0,T];L^2)$.  Together
with $\Gamma(u)\in C([0,T];L^1)$ (Lemma~\ref{lem:gamma}(c)),
\[
 |L_J(t)-L_J(s)|
 \le\norm{p_{\le J}(t)-p_{\le J}(s)}_\infty\norm{\Gamma(u(t))}_1
 +\norm{p_{\le J}(s)}_\infty\norm{\Gamma(u(t))-\Gamma(u(s))}_1\to0
 \quad(s\to t).
\]

(iii) By (ii), $L_J$ is continuous, hence measurable, on $[0,\tau]$, and
\[
 \left|\int_0^\tau L_J\,dt\right|
 \le C2^{3J}\norm{u_0}_2^3\int_0^\tau\norm{\nabla u(t)}_2\,dt
 \le C2^{3J}\norm{u_0}_2^3\,\tau^{1/2}\Bigl(\int_0^\tau\norm{\nabla u(t)}_2^2\,dt\Bigr)^{1/2}
\]
by the Cauchy--Schwarz inequality on $[0,\tau]$.  Proposition~\ref{prop:energy}
gives $\int_0^\tau\norm{\nabla u}_2^2\,dt\le\norm{u_0}_2^2/(2\nu)$, and
$\tau\le H$; hence the right side is at most
$C2^{3J}\norm{u_0}_2^4(H/(2\nu))^{1/2}$.
\end{proof}

\begin{remark}[On the constant]\label{rem:lowpressure-constant}
The constant in \eqref{eq:lowpressure} is $C_\varphi=\norm\varphi_1\le32\pi/3$,
the $L^1$ norm of the cutoff profile; it depends on nothing else.  Under the
Fourier convention of Definition~\ref{def:lp} the inverse transform of an
$L^1$ symbol is bounded by the $L^1$ norm of the symbol with constant $1$,
so no further normalising factor enters.  The estimate is a band-limited
kernel bound; it neither asserts nor uses that the kernel of
$S_JR_iR_j$, or of an untruncated Riesz transform, is integrable.
\end{remark}

\begin{lemma}[Bernstein instance for the low-pass gradient]\label{lem:bernstein}
Let $C_B:=\norm{\nabla\kappa}_2=2\pi\norm{\,|\xi|\varphi\,}_{L^2}
\le2\pi\bigl(\tfrac{128\pi}{5}\bigr)^{1/2}=16\pi\sqrt{2\pi/5}$.
For every $L\in\mathbb Z$ and every $f\in L^2(\R^3)$ (scalar or vector-valued),
$S_Lf$ has a $C^\infty$ representative and
\[
 \norm{\nabla S_Lf}_\infty\le C_B\,2^{5L/2}\norm f_2 .
\]
Consequently $\norm{\nabla S_Lf-\nabla S_Lg}_\infty\le C_B2^{5L/2}\norm{f-g}_2$,
so $t\mapsto\nabla S_Lu(t)$ belongs to $C([0,T];L^\infty)$ whenever
$u\in C([0,T];L^2)$; and for $f\in H^1$, $\nabla S_Lf=S_L\nabla f$.
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:lowpass-kernel}(b),(c), $S_Lf=\kappa_L*f$ a.e., $\kappa_L*f$
is $C^\infty$, and $\partial_k(\kappa_L*f)=(\partial_k\kappa_L)*f$.  By
Lemma~\ref{lem:fourier-tools}(ii) with $r=2$, for every $x$ and each
component $f_m$ of $f$,
$|\partial_k(\kappa_L*f_m)(x)|\le\norm{\partial_k\kappa_L}_2\norm{f_m}_2$, hence
\[
 |\nabla S_Lf(x)|^2=\sum_{k,m}|\partial_k(\kappa_L*f_m)(x)|^2
 \le\sum_{k,m}\norm{\partial_k\kappa_L}_2^2\norm{f_m}_2^2
 =\norm{\nabla\kappa_L}_2^2\norm f_2^2 .
\]
Now $\partial_k\kappa_L(x)=2^{3L}2^L(\partial_k\kappa)(2^Lx)$, so the
substitution $y=2^Lx$ gives
$\norm{\nabla\kappa_L}_2^2=2^{8L}2^{-3L}\norm{\nabla\kappa}_2^2=2^{5L}\norm{\nabla\kappa}_2^2$.
By Plancherel and $\widehat{\partial_k\kappa}(\xi)=2\pi i\xi_k\hat\kappa(\xi)
=2\pi i\xi_k\varphi(\xi)$ \cite[Prop.~2.2.11(9)]{Grafakos2014},
\[
 \norm{\nabla\kappa}_2^2=\sum_k\norm{2\pi\xi_k\varphi}_2^2
 =4\pi^2\int_{\R^3}|\xi|^2\varphi(\xi)^2\,d\xi
 \le4\pi^2\int_{|\xi|\le2}|\xi|^2\,d\xi
 =4\pi^2\cdot4\pi\int_0^2r^4\,dr=4\pi^2\cdot\frac{128\pi}{5},
\]
using $0\le\varphi\le\mathbf 1_{\{|\xi|\le2\}}$.  This proves the bound with
$C_B=\norm{\nabla\kappa}_2\le2\pi(128\pi/5)^{1/2}$.  The Lipschitz form is
the bound applied to $f-g$, and the continuity statement follows.  The
commutation $\nabla S_Lf=S_L\nabla f$ on $H^1$ is
Lemma~\ref{lem:lowpass-kernel}(d).
\end{proof}

%% ---- hyp:highpressure and hyp:absorption are UNCHANGED and stand here,
%% ---- followed by the unchanged paragraph "These existential assertions are
%% ---- nontrivial: ...".  The paragraph "At these existential quantifiers, ..."
%% ---- and the sentence "Proposition lowpressure and Hypothesis highpressure
%% ---- imply Hypothesis absorption, with A = A_low + A_high." are replaced by:

\begin{lemma}[Absorption from the frequency split]\label{lem:absorption-split}
Suppose Hypothesis~\ref{hyp:highpressure} holds with $\theta\in[0,1)$, and
for given $\nu$, $u_0$, $H$ let $J=J(\nu,u_0,H)$ and
$A_{\rm high}=A_{\rm high}(\nu,u_0,H,J)$ be the witnesses it provides.  Then
Hypothesis~\ref{hyp:absorption} holds for these $\nu$, $u_0$, $H$ with the
same $\theta$ and
\[
 A(\nu,u_0,H):=A_{\rm low}(\nu,u_0,H,J)+A_{\rm high}(\nu,u_0,H,J),
\]
where $A_{\rm low}$ is the explicit quantity of \eqref{eq:lowpressure}.
\end{lemma}

\begin{proof}
Let $0<\tau<\min\{H,T_*\}$.  By Proposition~\ref{prop:pressure} (integrated
form) $P_3$ is integrable on $[0,\tau]$; $L_J$ is continuous on $[0,\tau]$ by
Proposition~\ref{prop:lowpressure}(ii); and $Q_J=P_3-L_J$ by
Lemma~\ref{lem:gamma}(d).  Hence
\[
 \int_0^\tau P_3\,dt=\int_0^\tau L_J\,dt+\int_0^\tau Q_J\,dt
 \le A_{\rm low}+\theta\nu\int_0^\tau D_3\,dt+A_{\rm high}
\]
by \eqref{eq:lowpressure} and \eqref{eq:highpressure}, which is
\eqref{eq:absorption} with the stated $A$; the same $A$ serves for every
$\tau$ because $A_{\rm low}$ and $A_{\rm high}$ do not depend on $\tau$.
\end{proof}

\begin{proposition}[Existential equivalence of the signed tail hypothesis]
\label{prop:existential-equivalence}
The following are equivalent.
\begin{itemize}
\item[(A)] Hypothesis~\ref{hyp:highpressure}.
\item[(B)] For every $\nu>0$ and every divergence-free $u_0\in\mathcal S(\R^3)^3$,
the maximal classical solution of Proposition~\ref{prop:localtheory} is
global: $T_*=\infty$.
\end{itemize}
\end{proposition}

\begin{proof}
(A)$\Rightarrow$(B).  Assume (A) with its $\theta\in[0,1)$.  Fix $\nu$ and
$u_0$ and suppose, for contradiction, that $T_*<\infty$.  Put $H:=T_*+1$,
so that $\min\{H,T_*\}=T_*$, and let $J$, $A_{\rm high}$ be the witnesses of
(A) for $(\nu,u_0,H)$.  By Lemma~\ref{lem:absorption-split},
\eqref{eq:absorption} holds for every $0<\tau<T_*$ with
$A=A_{\rm low}+A_{\rm high}<\infty$.  Write $X(t)=\norm{u(t)}_3^3$.  By
Proposition~\ref{prop:pressure} in integrated form,
\[
 \tfrac13X(\tau)+\nu\int_0^\tau D_3\,dt=\tfrac13X(0)+\int_0^\tau P_3\,dt
 \le\tfrac13\norm{u_0}_3^3+\theta\nu\int_0^\tau D_3\,dt+A
 \qquad(0<\tau<T_*).
\]
Since $D_3\ge0$ and $\theta<1$, the dissipation terms combine to
$(1-\theta)\nu\int_0^\tau D_3\ge0$ on the left, and therefore
$X(\tau)\le\norm{u_0}_3^3+3A$ for every $0<\tau<T_*$; that is,
\[
 \sup_{0<\tau<T_*}\norm{u(\tau)}_3\le\bigl(\norm{u_0}_3^3+3A\bigr)^{1/3}<\infty .
\]
Theorem~\ref{thm:continuation} states that $T_*<\infty$ forces
$\sup_{t<T_*}\norm{u(t)}_3=\infty$.  This contradiction shows $T_*=\infty$.
As $\nu$ and $u_0$ were arbitrary, (B) holds.

(B)$\Rightarrow$(A).  We show (A) with $\theta:=0$.  Fix $\nu$, $u_0$, and
$0<H<\infty$.  By (B), $T_*=\infty$, so $\min\{H,T_*\}=H$ and
Proposition~\ref{prop:localtheory} applies on the compact interval $[0,H]$:
$u\in C([0,H];L^2\cap L^6)$, $\nabla u\in C([0,H];L^2)$, and
$p\in C([0,H];L^2\cap L^3)$.  Choose $J:=0$.

\emph{Step 1: bound on $p_{>0}$ in $L^3$.}  For $t\in[0,H]$,
$p(t)\in L^2\cap L^3$, so by Lemma~\ref{lem:lowpass-kernel}(b) (with $q=3$)
$\norm{S_0p(t)}_3\le\norm\kappa_1\norm{p(t)}_3$, and therefore
\[
 \norm{p_{>0}(t)}_3=\norm{p(t)-S_0p(t)}_3\le(1+\norm\kappa_1)\norm{p(t)}_3 .
\]
By the same bound applied to $p(t)-p(s)$, $p_{>0}\in C([0,H];L^3)$.

\emph{Step 2: bound on $Q_0$.}  By Lemma~\ref{lem:gamma}(b) and H\"older's
inequality with $\tfrac13+\tfrac16+\tfrac12=1$,
\[
 |Q_0(t)|\le\int_{\R^3}|p_{>0}||u||\nabla u|\,dx
 \le\norm{p_{>0}(t)}_3\norm{u(t)}_6\norm{\nabla u(t)}_2
 \le(1+\norm\kappa_1)\norm{p(t)}_3\norm{u(t)}_6\norm{\nabla u(t)}_2 .
\]
The three norms on the right are continuous functions of $t\in[0,H]$,
hence bounded; call their maxima $M_p$, $M_6$, $M_\nabla$.

\emph{Step 3: continuity of $Q_0$.}  For $s,t\in[0,H]$,
\[
 |Q_0(t)-Q_0(s)|
 \le\norm{p_{>0}(t)-p_{>0}(s)}_3\norm{\Gamma(u(t))}_{3/2}
 +\norm{p_{>0}(s)}_3\norm{\Gamma(u(t))-\Gamma(u(s))}_{3/2}\to0
 \quad(s\to t)
\]
by Step~1 and Lemma~\ref{lem:gamma}(c).  Thus $Q_0$ is continuous on
$[0,H]$, and
\[
 A_{\rm high}(\nu,u_0,H,0):=\int_0^H|Q_0(t)|\,dt
 \le H(1+\norm\kappa_1)M_pM_6M_\nabla<\infty .
\]

\emph{Step 4: the inequality.}  For every $0<\tau<H=\min\{H,T_*\}$,
\[
 \int_0^\tau Q_0(t)\,dt\le\int_0^\tau|Q_0(t)|\,dt\le A_{\rm high}
 =\theta\nu\int_0^\tau D_3(t)\,dt+A_{\rm high}\qquad(\theta=0),
\]
which is \eqref{eq:highpressure} with $J=0$ and the same $A_{\rm high}$ for
the entire interval.  The quantity $A_{\rm high}$ depends only on
$(\nu,u_0,H)$, because the branch $(u,p)$ is uniquely determined by
$(\nu,u_0)$ (Proposition~\ref{prop:localtheory}).  Hence (A) holds with
$\theta=0$.
\end{proof}

\begin{remark}[Scope of the equivalence]\label{rem:existential-scope}
Uniqueness makes this an input-dependent witness.  This reverse argument
assumes global continuation and supplies no method for proving it.  Strict
absorption retains weighted dissipation in the forward argument, but does
not strengthen the existential assertion beyond global strong continuation.
No converse from an arbitrary smooth finite-energy solution class to the
selected strong branch is asserted here.  The converse above uses only the
regularity package of Proposition~\ref{prop:localtheory}
($p\in C([0,H];L^3)$); with the Calder\'on--Zygmund bound
$\norm p_3\le C\norm{u}_6^2$ one would recover the form
$|Q_0|\le C\norm u_6^3\norm{\nabla u}_2$, but that bound is not needed and
is not used.  Proposition~\ref{prop:lowpressure} and
Hypothesis~\ref{hyp:highpressure} imply Hypothesis~\ref{hyp:absorption}
with $A=A_{\rm low}+A_{\rm high}$ (Lemma~\ref{lem:absorption-split}), the
$J$ in $A_{\rm low}$ being the $J(\nu,u_0,H)$ supplied by
Hypothesis~\ref{hyp:highpressure}.
\end{remark}
```

Bibliography entry to add to `references.bib` (the manuscript currently has
no harmonic-analysis textbook):

```bibtex
@book{Grafakos2014,
  author    = {Loukas Grafakos},
  title     = {Classical {F}ourier Analysis},
  edition   = {Third},
  series    = {Graduate Texts in Mathematics},
  volume    = {249},
  publisher = {Springer},
  address   = {New York},
  year      = {2014},
  doi       = {10.1007/978-1-4939-1194-3},
  isbn      = {978-1-4939-1193-6}
}
```

---

## 3. External facts used

Page numbers for Grafakos are the printed page numbers of the third edition
(Springer GTM 249, 2014; ISBN 978-1-4939-1193-6, DOI
10.1007/978-1-4939-1194-3), read on 2026-09-05 from the mirror
`https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf`
through `helpy_pdf` text extraction (title page, pp. 21–25, 108–116,
325–329).

| # | Fact, in the form used | Source, exact location | Status | Used in |
| --- | --- | --- | --- | --- |
| E1 | Definition of the Fourier transform `f̂(ξ) = ∫ f(x)e^{−2πix·ξ}dx` on `𝒮(ℝⁿ)` | Grafakos, Def. 2.2.8, p. 108 | [DI] | `def:lp` |
| E2 | For `f, g ∈ 𝒮`: (1) `‖f̂‖_∞ ≤ ‖f‖₁`; (8) `(δ^t f)^ = t^{−n}δ^{t^{−1}}f̂`; (9) `(∂^α f)^(ξ) = (2πiξ)^α f̂(ξ)`; (12) `(f∗g)^ = f̂ ĝ`; and the statement on p. 113 that properties (1)–(8), (12), (13) hold for `f, g ∈ L¹` | Grafakos, Prop. 2.2.11, pp. 109–110; extension to `L¹`, p. 113 | [DI] | `lem:fourier-tools`(iv), `lem:lowpass-kernel`(a), `lem:bernstein` |
| E3 | Fourier inversion `(f̂)^∨ = f = (f^∨)^` and Plancherel `‖f‖₂ = ‖f̂‖₂ = ‖f^∨‖₂` on `𝒮` | Grafakos, Thm. 2.2.14 (2),(4), p. 112 | [DI] | `lem:lowpass-kernel`(a) |
| E4 | The Fourier transform is a homeomorphism of `𝒮(ℝⁿ)` onto itself | Grafakos, Cor. 2.2.15, p. 113 | [DI] | `lem:lowpass-kernel`(a) (`κ ∈ 𝒮`) |
| E5 | `L²` theory: the Fourier transform is an `L²` isometry on `L¹∩L²`, extends uniquely to an isometry `𝓕` of `L²`; `𝓕′` extends `f ↦ f^∨` from `L¹∩L²`; `𝓕′ = 𝓕^{−1}`; inversion holds a.e. on `L²` | Grafakos, §2.2.4, pp. 113–114 | [DI] | `def:lp`, `lem:fourier-tools`(iii),(iv) |
| E6 | Minkowski's inequality: `g ∈ L¹`, `f ∈ L^p`, `1 ≤ p ≤ ∞` ⟹ `g∗f` exists a.e. and `‖g∗f‖_p ≤ ‖g‖₁‖f‖_p` | Grafakos, Thm. 1.2.10, p. 21 | [DI] | `lem:fourier-tools`(i) |
| E7 | Young's inequality `‖f∗g‖_q ≤ ‖g‖_r‖f‖_p`, `1/q + 1 = 1/p + 1/r` (general form; only the `r = 1` case E6 and the Hölder endpoint are used) | Grafakos, Thm. 1.2.12, p. 22 | [DI] | corroboration only |
| E8 | Riesz transform `R_j` is the multiplier `−iξ_j/|ξ|` on `𝒮` (with kernel `c_n p.v. x_j/|x|^{n+1}`) | Grafakos, Def. 5.1.13 and Prop. 5.1.14, p. 325 | [DI] | `def:lp` (the D1 convention agrees with the textbook definition; the kernel form is not used) |
| E9 | `∂_j∂_k φ = −R_jR_k Δφ` on `𝒮` | Grafakos, Prop. 5.1.17, p. 328 | [DI] | corroboration of the symbol identity in `def:lp` (proved there directly from E2(9)) |
| E10 | Tao's Littlewood–Paley projections `P_{≤N}` with symbol `φ(ξ/N)`, `φ = 1` on `|ξ| ≤ 1`, supported in `|ξ| ≤ 2`, and the Bernstein estimates (26), in particular `‖∇^k P_N f‖_p ∼ N^k‖P_N f‖_p`, `‖P_{≤N}f‖_q ≲ N^{3/p−3/q}‖P_{≤N}f‖_p` | Tao, APDE 6 (2013), p. 40, eq. (26); transcribed verbatim in `cp01-literature-statements.md` §1.4 | [DI] (via the CP01 record) | `def:lp` (`S_J = P_{≤2^J}`); `lem:bernstein` is the instance `k = 1, p = 2, q = ∞` proved here directly with an explicit constant |
| E11 | Tao's normalised pressure `p = −Δ^{−1}∂_i∂_j(u_iu_j)`, `Δ^{−1}` the multiplier `−(4π²|ξ|²)^{−1}`, and the identity with `R_iR_j(u_iu_j)` under D1 | Tao, APDE 6 (2013), eq. (9) and (14); `cp01-literature-statements.md` §1.1, §7.3 | [DI] (via the CP01 record) | `def:lp` |
| E12 | Hölder's and Cauchy–Schwarz inequalities; Fubini–Tonelli; dominated convergence; the mean value inequality for `C¹` maps along a segment | standard; e.g. Folland, *Real Analysis*, 2nd ed. (Wiley 1999), Thm. 6.2 (Hölder), Thm. 2.37 (Fubini–Tonelli), Thm. 2.24 (DCT); mean value inequality: any calculus text | [MO] | throughout |
| E13 | `|B(0,r)| = (4π/3)r³`; `∫_{|ξ|≤2}|ξ|²dξ = 4π∫_0^2 r⁴dr = 128π/5` | computation | — | `def:lp`, `lem:bernstein` |
| E14 | Calderón–Zygmund `L³` bound for `R_iR_j` (`‖p‖₃ ≤ C‖u‖₆²`) | Grafakos, Cor. 5.2.8 (per quotient lane, not re-inspected here); Stein 1970 Ch. II §2, Ch. III §1 | [MO] | **not used**; mentioned in `rem:existential-scope` only |

Assumed (not external): Proposition `prop:localtheory` (package R of D2,
including uniqueness of the branch); Theorem `thm:continuation` in the D3
form `T_* < ∞ ⟹ sup_{t<T_*}‖u(t)‖₃ = ∞`; Proposition `prop:pressure` in the
integrated P-3 form `X(τ)/3 + ν∫_0^τ D_3 = X(0)/3 + ∫_0^τ P_3` with
`D_3 ≥ 0`, `P_3` integrable on `[0,τ]`, and the P-0 integrand
`Γ(u)` of `def:pressure-work`; Proposition `prop:energy`.

---

## 4. Obligations not discharged

None of F-1, X-1, or the Q-17 Bernstein input is left open. Items outside
this lane that the text above depends on, stated exactly:

1. `prop:pressure` in integrated form with `P_3 = ∫ p Γ(u)` (P-0, P-3) and
   `P_3` integrable on compact subintervals of `[0,T_*)` — used in
   `lem:absorption-split` and in (A)⟹(B). Owner: pressure lane. If the
   pressure lane defines `P_3` through `(u⊗u):∇u/|u|`, it coincides with
   `Γ(u)` here (`Σ u_iu_j∂_ju_i` under either index convention).
2. `thm:continuation` in the D3 form. Owner: continuation lane.
3. `prop:localtheory` with the memberships listed in D2, in particular
   `u ∈ C([0,T];L²∩L⁶∩L^∞)`, `∇u ∈ C([0,T];L²)`, `p ∈ C([0,T];L²∩L³∩L^∞)`,
   and uniqueness of the branch. Owner: local-theory lane.
4. The general Bernstein inequality (Tao (26)) is **not** proved; only the
   instance `‖∇S_Lf‖_∞ ≤ C_B2^{5L/2}‖f‖₂` is, which is all Q-17 uses.
5. Notation clash `ψ` (D1 annular symbol) versus `ψ` (quotient lane kernel):
   integrator's choice; see §1.

---

## 5. Frontier record

**MODE / RESULT.** PROOF-WRITING; all three assigned obligations discharged
at the CP02 standard. Result: `prop:lowpressure` is proved in full with
`C = 32π/3` (sharper `‖φ‖₁`) and the kernel path
`‖K_J‖_∞ ≤ ‖m_J‖₁ ≤ 2^{3J}‖φ‖₁` with Fourier constant exactly 1;
the Bernstein instance is proved with `C_B = 2π‖|ξ|φ‖₂ ≤ 16π(2π/5)^{1/2}`;
the existential equivalence is a labelled proposition with both directions
written.

**CLAIM AND SCOPE.** On the unforced equation on `ℝ³` with arbitrary `ν > 0`
and divergence-free Schwartz data, in the classical branch of
`prop:localtheory` (assumed): (1) with the D1 convention, the inhomogeneous
`S_J = P_{≤2^J}` and the homogeneous `Σ_{j≤J}Δ_j` coincide on `L²`; (2)
`‖p_{≤J}(t)‖_∞ ≤ (32π/3)2^{3J}‖u_0‖₂²`, `|L_J(t)| ≤ (32π/3)2^{3J}‖u_0‖₂³‖∇u(t)‖₂`,
`L_J` continuous, and `|∫_0^τ L_J| ≤ (32π/3)2^{3J}‖u_0‖₂⁴(H/2ν)^{1/2}`;
(3) `‖∇S_Lf‖_∞ ≤ C_B2^{5L/2}‖f‖₂` for `f ∈ L²`; (4) `hyp:highpressure` ⟺
every branch is global, given `prop:pressure` (P-3), `thm:continuation`
(D3), and R. No estimate here bears on the size of `Q_J` for any `J`
without assuming global continuation.

**EVIDENCE.** Every displayed identity and constant was rederived in this
lane: the telescoping of `ψ(2^{−j}·)`; the `L²∗L¹` convolution theorem by
kernel truncation; realness and evenness of `κ` and `K_J`; the bilinear
symbol bound giving `‖p_{≤J}‖_∞ ≤ ‖φ‖₁2^{3J}‖u‖₂²` without a factor 3; the
Lipschitz constant 3 of `a ↦ a⊗a/|a|` (two-case argument); the pointwise
bound `|Γ(v)| ≤ |v||∇v|` by two Cauchy–Schwarz steps; the `L¹` and `L^{3/2}`
time-continuity of `Γ(u)`; the Cauchy–Schwarz-in-time step with `τ ≤ H`;
`‖∇κ_L‖₂ = 2^{5L/2}‖∇κ‖₂` and `∫_{|ξ|≤2}|ξ|² = 128π/5`; the quantifier
bookkeeping of both directions of the equivalence (`θ = 0`, `J = 0`,
`A_high = ∫_0^H|Q_0|`, `min{H,T_*} = H`). Textbook facts are pinned to
Grafakos 3rd ed. by page (E1–E9, all [DI] today) and to Tao 2013 p. 40 /
eq. (9) via the CP01 record (E10–E11).

**FIRST GAP.** Within this lane, none. For the chain the lane feeds, the
first gap is unchanged: `hyp:highpressure` (HIGH-PRESSURE) is not proved,
and `prop:existential-equivalence` shows that proving it is exactly as hard
as global continuation of every branch. The lane's text depends on three
results owned elsewhere (integrated `prop:pressure`, D3-form
`thm:continuation`, `prop:localtheory`); if any of these is not delivered,
`lem:absorption-split` and `prop:existential-equivalence` (both directions)
are the affected items, while `def:lp`–`lem:bernstein` and
`prop:lowpressure` depend only on R and `prop:energy`.

**SURVIVING CONDITIONAL SUFFIX.** Given `prop:pressure` (P-3), the chain
`hyp:highpressure ⟹ (lem:absorption-split) hyp:absorption ⟹
sup_{t<min(H,T_*)}‖u(t)‖₃³ ≤ ‖u_0‖₃³ + 3(A_low + A_high)` is valid with the
explicit `A_low` of `eq:lowpressure`; `sec:quotient`'s low-strain
coefficient `M = 3(1+C_ℙ)C_B2^{5L/2}‖u_0‖₂` is valid with the `C_B` above.

**NON-CLAIMS.** No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL, ABSORPTION, or
NS-R3 result is asserted. No bound on `Q_J`, `A_high`, or `θ` is claimed
without the hypothesis of global continuation. The general Bernstein
inequality, Calderón–Zygmund theory, and the `L¹` integrability of any
Riesz-type kernel are neither claimed nor used. Stein 1970 and Grafakos
Cor. 5.2.8 were not inspected in this lane ([MO], unused).

**NEXT DISTINCT ACTION.** Integrator: add `\newtheorem{lemma}` and
`\newtheorem{definition}`, the `Grafakos2014` bib entry, resolve the `ψ`
notation clash with the quotient lane, replace the quotient lane's
`lem:lowpass` by `lem:bernstein` (or cite it), and confirm that the
pressure lane's `P_3` integrand equals `Γ(u)` of `def:pressure-work`. Then
an adversarial review lane (`cp02-review-lowpressure.md`) should check
`lem:fourier-tools`(iv) and `lem:riesz-kernel`(c),(d) line by line, since
these carry the entire kernel argument.
