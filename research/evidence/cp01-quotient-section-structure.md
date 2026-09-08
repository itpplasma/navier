# CP01: the cubic gradient quotient as a proposition sequence

MODE / RESULT: **INTEGRATE (design).**  This note rewrites manuscript
section `sec:quotient` as a self-contained sequence of definitions, lemmas
and propositions with complete proofs, importing the audited HF17 arguments
and the reviewer's direct derivative proof, and isolating every external
fact with a primary source.  The terminal claim NS-R3 remains OPEN.
HIGH-PRESSURE and HIGH-STRAIN remain open.  Nothing here proves
`eq:quotient-gap`.

Status date: 2026-09-05.  Frozen inputs (SHA-256):

| File | SHA-256 |
| --- | --- |
| `research/evidence/hf17-quotient-functional.md` | `a57fd95e847bfda0a597c75322cafad42827c559f33420b369f2a5897f8c0ce7` |
| `research/evidence/hf17-quotient-evolution.md` | `84f2dcbf7801c911eea2535b870a358b99cb2b5af06da97a7ec8689d4b09b670` |
| `research/evidence/hf17-review-quotient-functional.md` | `46e3f65b4e05d823ebcf29f7b5db3df36a9baac97cdfcf7b9ddabc07fe2c4e0f` |
| `research/evidence/hf17-review-quotient-evolution.md` | `4cbad789b68fc1779bbf6c54ae0a67b05d1f9ae907b470284bd3fbeeaee17b37` |
| `research/evidence/hf16-taylor-commutator.md` | `842545da7844d62aa847aeb7ad63303c5abcf3be05798d5e07b36b3452c25683` |
| `research/evidence/hf16-review-taylor-commutator.md` | `32c65d379fa72dc8944519136c67eaf4349d6999e7f522f2c9aa6e4b3da98a0a` |
| `navier-paper/main.tex` (commit `1ad73c2`) | `2b2c072f0e461c5abb94d11430bdc2f4940dc4c3e2a93c999071e07a22c40012` |

Research repository HEAD at writing: `fd1c20e4ec32d7932bb318836d02b10a073e3500`.

## 1. Design decisions

1. **Elementary route through the pointwise cubic.**  All convexity input is
   replaced by four pointwise inequalities for \(f(z)=|z|^3/3\) on
   \(\mathbb R^3\) (Lemma `lem:cubic-pointwise`): a Taylor remainder, a
   midpoint-convexity gain \(\ge|a-b|^3/24\), the monotonicity
   \((j(a)-j(b))\cdot(a-b)\ge|a-b|^3/4\) for \(j(z)=|z|z\), and the Lipschitz
   bound \(|j(a)-j(b)|\le2(|a|+|b|)|a-b|\).  Existence of the minimizer then
   follows from completeness of \(L^3\) (minimizing sequences are Cauchy),
   uniqueness from the midpoint gain, and the Fréchet derivative from the
   manuscript's monotonicity argument with the explicit remainder
   \(10(\|w\|_3+\|h\|_3)^{5/3}\|h\|_3^{4/3}\).  Reflexivity, weak lower
   semicontinuity, uniform convexity of \(L^3\), the Radon–Riesz property and
   the abstract uniform-smoothness sentence of HF17 §5 are all unnecessary.
   The reviewer's "direct derivative proof" is retained in its competitor
   structure; its Radon–Riesz step is replaced by the quantitative
   monotonicity step, which is both more elementary and Lean-friendlier.
2. **Solenoidal class for coercivity.**  Coercivity is stated for
   \(u\in L^2\cap L^3\) with distributional divergence zero, where
   \(\mathbb Pu=u\) is a two-line Plancherel fact.  This covers every
   Navier–Stokes velocity used in the section.  The general \(L^3\)
   Helmholtz decomposition (Galdi Thm. III.1.2, Fujiwara–Morimoto 1977) is
   mentioned in a remark and is not a dependency.
3. **Pressure gradient without \(L^3\) Riesz theory.**  On the standing
   class, \(u_iu_j\in H^2\), so \(p=R_iR_j(u_iu_j)\in H^2\subset W^{1,3}\)
   by \(L^2\) Fourier multipliers only.  \(L^3\)-boundedness of Riesz
   transforms (Grafakos Cor. 5.2.8) is used once: for \(\|\mathbb P\|_{3\to3}\)
   in the coercivity lemma.
4. **Gradient-closure lemma.**  One lemma (`lem:gradient-closure`) shows
   \(\nabla\psi\in\mathcal G_3\) for every \(\psi\in L^3\) with weak gradient
   in \(L^3\), and that pullback by a volume-preserving \(C^1\)
   diffeomorphism with bounded differential preserves \(\mathcal G_3\).  It
   serves the heat lemma, the pressure lemma and the inner variation.
5. **Regularity class.**  A named standing assumption
   (`prem:classical-interval`): \(u\in C([0,T];H^m)\cap C^1([0,T];H^{m-2})\),
   \(m\ge4\), divergence-free, \(p=R_iR_j(u_iu_j)\), equation holding in
   \(H^{m-2}\) at each time.  A remark records why Tao Theorem 5.4 solutions
   satisfy it (directly inspected, see §3) and which persistence step is the
   manuscript's existing premise `premise:local`.
6. **Flow lemma.**  The ODE facts are isolated in `lem:flow` with the
   quantitative expansions \(|D\Phi_s-I-s\,Du|\le C_us^2\) and
   \(|D\Phi_s^{-\mathsf T}-I+s\,Du^{\mathsf T}|\le C_u's^2\) derived inline
   from the variational equation; only existence, \(C^1\) dependence on the
   initial point and the Liouville formula are imported.
7. **Conditional consequence.**  `hyp:highstrain` is stated with the same
   quantifier order as `hyp:highpressure`; `prop:quotient-conditional` proves
   `hyp:highstrain` \(\Rightarrow\) `hyp:critical` with an explicit
   \(M(\nu,u_0,H)\), hence (by `thm:conditional`) the target.  A remark
   proves that, at these quantifiers, `hyp:highstrain` is equivalent to
   global continuation of the selected branch, mirroring the manuscript's
   discussion of `hyp:highpressure`.  All non-claims are preserved.

## 2. Dependency graph of the proposed section

```text
def:quotient
  lem:cubic-pointwise ──> lem:cubic-frechet ──> lem:quotient-minimizer
  lem:gradient-closure
  lem:leray ─────────────────────────────────> lem:quotient-coercive
  lem:quotient-scaling
  lem:gradient-closure + F4(heat kernel) ─────> lem:quotient-heat
  lem:cubic-frechet + lem:quotient-minimizer ──> prop:quotient-derivative
  lem:sobolev-classical (embedding/multiplication, inline)
  prem:classical-interval (standing class; Tao 5.4 remark)
  lem:sobolev-classical + lem:gradient-closure ──> lem:quotient-pressure
  lem:quotient-heat + prop:quotient-derivative + lem:heat-generator ──> lem:quotient-heatsign
  lem:flow + lem:gradient-closure + prop:quotient-derivative ──> lem:quotient-transport
  all of the above ──> prop:quotient-evolution
  lem:lowpass (Bernstein, inline) + lem:quotient-coercive + prop:energy ──> lem:quotient-lowstrain
  hyp:highstrain (UNPROVED)
  prop:quotient-evolution + lem:quotient-lowstrain + hyp:highstrain ──> prop:quotient-conditional ──> hyp:critical ──> thm:conditional
```

## 3. External facts and sources

Labels: **DI** = directly inspected in this session (page/line seen);
**REC** = recalled from memory, theorem number not re-inspected here; a
Phase-I source record must re-inspect before citing as an axiom.

| Tag | Fact used | Source | Status |
| --- | --- | --- | --- |
| F1a | Riesz transform \(R_j\) is the Fourier multiplier \(-i\xi_j/\lvert\xi\rvert\) on \(\mathcal S(\mathbb R^n)\) (convention \(\hat f(\xi)=\int e^{-2\pi ix\cdot\xi}f\)). | Grafakos, *Classical Fourier Analysis*, 3rd ed., GTM 249, Def. 5.1.13 and Prop. 5.1.14, p. 325. | DI (PDF mirror at math.stonybrook.edu/~bishop/classes/math638.F20/, text pages 341–346) |
| F1b | \(R_j\) bounded on \(L^p(\mathbb R^n)\), \(1<p<\infty\). | Grafakos, op. cit., Cor. 5.2.8, p. 340 (via Thm. 5.2.7, method of rotations). | DI |
| F1c | \(\partial_j\partial_k\varphi=-R_jR_k\Delta\varphi\) for \(\varphi\in\mathcal S\). | Grafakos, op. cit., Prop. 5.1.17, p. 328. | DI (used only for the remark identifying \(R_iR_j(u_iu_j)\) with Tao's normalised pressure) |
| F2 | Minkowski's inequality \(\|g*f\|_p\le\|g\|_1\|f\|_p\); Young's inequality. | Grafakos, op. cit., Thm. 1.2.10 and Thm. 1.2.12. | DI |
| F3 | Approximate identity: \(\|k_\varepsilon*f-f\|_p\to0\) for \(f\in L^p\), \(1\le p<\infty\). | Grafakos, op. cit., Def. 1.2.15, Thm. 1.2.19(1). | DI |
| F4 | Sobolev inequality \(\|f\|_{L^6(\mathbb R^3)}\le C_S\|\nabla f\|_{L^2}\) for \(f\in H^1\). | Lieb–Loss, *Analysis*, 2nd ed., Thm. 8.3 (sharp constant not needed). | REC |
| F5 | Fourier inversion of an \(L^1\) function is continuous and vanishes at infinity (Riemann–Lebesgue); Plancherel. | Grafakos, op. cit., §2.2.2–2.2.4 (Prop. 2.2.17, Thm. 2.2.14 in the 3rd ed. numbering); Mathlib `Mathlib/Analysis/Fourier/RiemannLebesgueLemma.lean`, `Mathlib/Analysis/Fourier/LpSpace.lean` (Plancherel, `fourierTransformₗᵢ`). | REC for Grafakos numbers; Mathlib file names DI |
| F6a | Global flow of a bounded globally Lipschitz \(C^1\) field: existence, uniqueness, group property. | Picard–Lindelöf plus a priori bound; Hartman, *ODE* (SIAM Classics 2002), Ch. II Thm. 1.1 and Ch. II Thm. 3.1 (extension). Mathlib `Mathlib/Analysis/ODE/PicardLindelof.lean` (`IsPicardLindelof`, local existence), `Mathlib/Analysis/ODE/Gronwall.lean` (uniqueness). | REC (Hartman numbers); Mathlib files DI |
| F6b | \(C^1\) dependence on the initial point and the variational equation \(\partial_sD\Phi_s=Db(\Phi_s)D\Phi_s\) for a \(C^1\) field. | Hartman, op. cit., Ch. V Thm. 3.1 (Peano's theorem on differentiability with respect to initial conditions). | REC; **mathlib-absent** (no differentiability of flows w.r.t. initial data found in v4.33.1 checkout) |
| F6c | Liouville formula: \(\partial_s\det D\Phi_s=(\operatorname{div}b)(\Phi_s)\det D\Phi_s\). | Hartman, op. cit., Ch. IV Thm. 1.2 (Liouville's formula for linear systems), applied to the variational equation. | REC; mathlib-absent |
| F7 | Change of variables under a \(C^1\) diffeomorphism with unit Jacobian. | Standard; Mathlib `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul` (`Mathlib/MeasureTheory/Function/Jacobian.lean`). | REC for Mathlib name |
| F8 | Tao, *Localisation and compactness properties of the Navier–Stokes global regularity problem*, arXiv:1108.1165v4 (APDE 6 (2013) 25–107), Thm. 5.4: (ii) local existence with \(\|u\|_{X^k([0,T]\times\mathbb R^3)}\lesssim_{k,\|u_0\|_{H^k},\|f\|_{L^1_tH^k_x}}1\) for each \(k\ge1\) when \((\|u_0\|_{H^1}+\|f\|_{L^1_tH^1_x})^4T\le c\); (iv) for Schwartz data, \(u,p\) smooth with \(\partial_t^ju,\partial_t^jp\in L^\infty_tH^k_x([0,T]\times\mathbb R^3)\) for all \(j,k\ge0\); the proof of (iv) states "it would have sufficed to have \(u_0\in H^k_x\) and \(f\in C^j_tH^k_x\) for all \(j,k\ge0\)". Pressure normalisation (9): \(p=-\Delta^{-1}\partial_i\partial_j(u_iu_j)+\Delta^{-1}\nabla\cdot f\); the \(\mathbb R^3\) \(H^1\) mild solution uses \(p\) given by (9) (p. 6). Viscosity normalised to \(\nu=1\) (footnote 3, p. 4). | arXiv PDF pp. 3–6, 33–35. | DI |
| F9 | Gronwall (integral form) for continuous nonnegative functions. | Elementary; Mathlib `Mathlib/Analysis/ODE/Gronwall.lean` (`le_gronwallBound_of_liminf_deriv_right_le`, `norm_le_gronwallBound_of_norm_deriv_right_le`). | DI for Mathlib names |
| F10 | Completeness of \(L^p\), Hölder, Fubini, dominated convergence, weak derivatives commute with mollification. | Standard; Mathlib `MeasureTheory.Lp.instCompleteSpace` (`Mathlib/MeasureTheory/Function/LpSpace/Complete.lean`), `eLpNorm_smul_le_mul_eLpNorm` (Hölder in \(L^p\), `LpSeminorm/CompareExp.lean`). | DI for Mathlib names |

Facts named in the task but **not needed** in this design: uniform
convexity of \(L^3\) (replaced by `lem:cubic-pointwise`; alternative source
Brezis, *Functional Analysis*, Thm. 4.10 and Prop. 3.32, REC);
Bernstein's inequality in general form (the needed low-pass bound is proved
inline by Cauchy–Schwarz; general reference Bahouri–Chemin–Danchin, Lemma
2.1, REC); Sobolev multiplication algebra (replaced by the inline
\(L^\infty\cdot L^2\) and \(L^4\cdot L^4\) bounds); the HF16 Taylor
commutator (not used by the quotient route; it belongs to the pressure
route).

Mathlib v4.33.1 checkout (`../stafford38/.lake/packages/mathlib`,
commit `0df444a3`) findings relevant to Phase II: Sobolev spaces exist as
Bessel-potential spaces on tempered distributions
(`Mathlib/Analysis/Distribution/Sobolev.lean`, `MemSobolev`,
`MemSobolev.fourier_memL1` for \(2s>\dim\), `MemSobolev.laplacian`); Fourier
multipliers on Schwartz and tempered distributions
(`Mathlib/Analysis/Distribution/FourierMultiplier.lean`); a
Gagliardo–Nirenberg–Sobolev inequality for compactly supported \(C^1\)
functions (`Mathlib/Analysis/FunctionalSpaces/SobolevInequality.lean`,
`eLpNorm_le_eLpNorm_fderiv_of_eq`); Gaussian integrals and Fourier transform
(`Mathlib/Analysis/SpecialFunctions/Gaussian/`).  Absent: \(L^p\)
boundedness of Riesz transforms/Calderón–Zygmund theory, \(L^p\) uniform
convexity of `Lp` (no `UniformConvexSpace` instance for `Lp` found),
differentiable dependence of ODE flows on initial data, Liouville's formula.

## 4. Full LaTeX text of the rewritten section

Preamble additions required in `main.tex` (the current preamble defines
`theorem`, `proposition`, `hypothesis`, `remark` only):

```latex
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newcommand{\Q}{\mathcal Q}
\newcommand{\G}{\mathcal G_3}
\newcommand{\PP}{\mathbb P}
\DeclareMathOperator{\dv}{div}
```

Bibliography additions (`references.bib`):

```bibtex
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
@book{LiebLoss2001,
  author    = {Elliott H. Lieb and Michael Loss},
  title     = {Analysis},
  edition   = {2},
  series    = {Graduate Studies in Mathematics},
  volume    = {14},
  publisher = {American Mathematical Society},
  year      = {2001}
}
@book{Hartman2002,
  author    = {Philip Hartman},
  title     = {Ordinary Differential Equations},
  edition   = {2},
  series    = {Classics in Applied Mathematics},
  volume    = {38},
  publisher = {SIAM},
  year      = {2002}
}
```

The section text follows.  It replaces the current `sec:quotient` in full.

```latex
\section{The cubic gradient quotient}\label{sec:quotient}

This section records a second route to the critical bound of
Hypothesis~\ref{hyp:critical}.  It replaces the explicit pressure work of
Proposition~\ref{prop:pressure} by a functional whose derivative annihilates
every gradient.  Everything up to and including
Lemma~\ref{lem:quotient-lowstrain} is proved here.  The remaining
high-strain estimate, Hypothesis~\ref{hyp:highstrain}, is not proved; it is
an alternative producer of Hypothesis~\ref{hyp:critical}, not an additional
requirement.  No regularity theorem is asserted.

Throughout, $\norm{\cdot}_r$ is the norm of $L^r(\R^3)$ or
$L^r(\R^3;\R^3)$, $\langle f,g\rangle=\int_{\R^3}f\cdot g\,dx$ for real
fields, $\hat f(\xi)=\int e^{-2\pi ix\cdot\xi}f(x)\,dx$, and $H^s=H^s(\R^3)$
with $\norm{f}_{H^s}^2=\int(1+|\xi|^2)^s|\hat f|^2d\xi$.  All functions are
real-valued; $C$ denotes an absolute constant whose value may change.

\subsection{Definition and pointwise inequalities}

\begin{definition}[Gradient space, cubic quotient, auxiliary operators]
\label{def:quotient}\leavevmode
\begin{enumerate}
\item[(a)] $\G$ is the closure in $L^3(\R^3;\R^3)$ of the set
 $\{\nabla\phi:\phi\in C_c^\infty(\R^3)\}$; it is a closed linear
 subspace.
\item[(b)] For $v\in L^3(\R^3;\R^3)$ put $F(v)=\frac13\int_{\R^3}|v|^3dx$ and
 $j(v)=|v|v$.  For $u\in L^3(\R^3;\R^3)$ define
 \[
  \Q(u)=\inf_{q\in\G}F(u+q).
 \]
\item[(c)] A field $u\in L^2(\R^3;\R^3)$ is \emph{solenoidal} if
 $\int u\cdot\nabla\phi\,dx=0$ for every $\phi\in C_c^\infty(\R^3)$.
\item[(d)] For $\lambda>0$, $(\mathcal S_\lambda u)(x)=\lambda u(\lambda x)$.
\item[(e)] For $t>0$, $G_tf=k_t*f$ with
 $k_t(x)=(4\pi t)^{-3/2}e^{-|x|^2/4t}$, so $k_t\ge0$, $\int k_t=1$,
 $\hat k_t(\xi)=e^{-4\pi^2t|\xi|^2}$.
\item[(f)] Fix once and for all a real radial $\psi\in\mathcal S(\R^3)$ with
 $\hat\psi\in C_c^\infty$, $\hat\psi=1$ on $\{|\xi|\le1\}$ and
 $\operatorname{supp}\hat\psi\subset\{|\xi|\le2\}$.  For $L\in\mathbb Z$ put
 $\psi_L(x)=2^{3L}\psi(2^Lx)$ and $S_Lf=\psi_L*f$.
\item[(g)] The Riesz transforms $R_j$ are the bounded extensions to
 $L^r(\R^3)$, $1<r<\infty$, of the Fourier multiplier with symbol
 $-i\xi_j/|\xi|$ on $\mathcal S$ \cite[Def.~5.1.13, Prop.~5.1.14,
 Cor.~5.2.8]{Grafakos2014}.  The Leray projection is
 $(\PP f)_i=f_i+R_iR_jf_j$ (summation over $j$), and
 $C_{\PP}=\norm{\PP}_{L^3\to L^3}<\infty$.
\end{enumerate}
\end{definition}

\begin{lemma}[Pointwise cubic inequalities]\label{lem:cubic-pointwise}
Let $f(z)=\frac13|z|^3$ and $j(z)=|z|z$ on $\R^3$.  Then $f\in C^2(\R^3)$,
$\nabla f=j$, $D^2f(z)=|z|I+z\otimes z/|z|$ for $z\neq0$, $D^2f(0)=0$, and
for all $a,b,h\in\R^3$:
\begin{align}
 &\bigl|f(a+h)-f(a)-j(a)\cdot h\bigr|\le(|a|+|h|)|h|^2,
 \label{eq:cp-taylor}\\
 &f(a)+f(b)-2f\!\left(\tfrac{a+b}2\right)\ge\tfrac1{24}|a-b|^3,
 \label{eq:cp-midpoint}\\
 &\bigl(j(a)-j(b)\bigr)\cdot(a-b)\ge\tfrac14|a-b|^3,
 \label{eq:cp-monotone}\\
 &|j(a)-j(b)|\le2(|a|+|b|)\,|a-b|.
 \label{eq:cp-lipschitz}
\end{align}
\end{lemma}

\begin{proof}
For $z\neq0$ direct differentiation gives $\nabla f(z)=|z|z$ and
$D^2f(z)=|z|I+z\otimes z/|z|$, so $|D^2f(z)h|\le2|z||h|$ and
$D^2f(z)(h,h)=|z||h|^2+(z\cdot h)^2/|z|\ge|z||h|^2$.  Since
$|f(z)|\le|z|^3/3$ and $|j(z)|=|z|^2$, $f$ is differentiable at $0$ with
$\nabla f(0)=0=j(0)$, and $j$ is differentiable at $0$ with derivative $0$
because $|j(h)|=|h|^2$; the formula $|D^2f(z)|\le2|z|$ shows $D^2f$ is
continuous at $0$.  Hence $f\in C^2$.

\eqref{eq:cp-taylor}: Taylor's formula with integral remainder gives
$f(a+h)-f(a)-j(a)\cdot h=\int_0^1(1-\theta)D^2f(a+\theta h)(h,h)\,d\theta$,
and $|D^2f(a+\theta h)(h,h)|\le2(|a|+|h|)|h|^2$, while
$\int_0^1 2(1-\theta)d\theta=1$.

\eqref{eq:cp-midpoint}: put $m=(a+b)/2$, $d=(a-b)/2$, and
$g(\theta)=f(m+\theta d)+f(m-\theta d)$.  Then $g(0)=2f(m)$, $g'(0)=0$, and
$g''(\theta)=D^2f(m+\theta d)(d,d)+D^2f(m-\theta d)(d,d)
\ge(|m+\theta d|+|m-\theta d|)|d|^2\ge2\theta|d|^3$
by the triangle inequality.  Therefore
$g(1)-g(0)=\int_0^1(1-\theta)g''(\theta)d\theta
\ge2|d|^3\int_0^1\theta(1-\theta)d\theta=|d|^3/3=|a-b|^3/24$.

\eqref{eq:cp-monotone}: with $z_\theta=b+\theta(a-b)$,
$(j(a)-j(b))\cdot(a-b)=\int_0^1D^2f(z_\theta)(a-b,a-b)\,d\theta
\ge|a-b|^2\int_0^1|z_\theta|d\theta$.  Let $\theta_0\in\R$ minimize
$\theta\mapsto|z_\theta|$ over $\R$ (if $a=b$ there is nothing to prove).
Then $z_{\theta_0}\perp(a-b)$, so
$|z_\theta|^2=|z_{\theta_0}|^2+(\theta-\theta_0)^2|a-b|^2$ and
$|z_\theta|\ge|\theta-\theta_0||a-b|$.  Since
$\int_0^1|\theta-\theta_0|d\theta\ge\frac14$ for every real $\theta_0$,
the claim follows.

\eqref{eq:cp-lipschitz}: $j(a)-j(b)=\int_0^1D^2f(z_\theta)(a-b)\,d\theta$
and $|D^2f(z_\theta)(a-b)|\le2|z_\theta||a-b|\le2(|a|+|b|)|a-b|$.
\end{proof}

\begin{lemma}[The cubic norm is Fr\'echet differentiable]
\label{lem:cubic-frechet}
For $v,h\in L^3(\R^3;\R^3)$, $j(v)\in L^{3/2}$ with
$\norm{j(v)}_{3/2}=\norm v_3^2$, and
\begin{equation}\label{eq:cp-F-taylor}
 \bigl|F(v+h)-F(v)-\langle j(v),h\rangle\bigr|
 \le(\norm v_3+\norm h_3)\norm h_3^2 .
\end{equation}
Moreover $\norm{j(v)-j(v')}_{3/2}\le2(\norm v_3+\norm{v'}_3)\norm{v-v'}_3$.
\end{lemma}

\begin{proof}
$\int|j(v)|^{3/2}=\int|v|^3$ gives the first claim.  Integrate
\eqref{eq:cp-taylor} pointwise and apply H\"older with exponents $3$ and
$3/2$ to $\int(|v|+|h|)|h|^2$.  For the last claim integrate
\eqref{eq:cp-lipschitz} raised to the power $3/2$ and use H\"older with
exponents $2$ and $2$ on $\int(|v|+|v'|)^{3/2}|v-v'|^{3/2}$.
\end{proof}

\subsection{The minimizing representative}

\begin{lemma}[Existence, uniqueness, Euler--Lagrange condition]
\label{lem:quotient-minimizer}
Let $u\in L^3(\R^3;\R^3)$.
\begin{enumerate}
\item[(a)] There is a unique $q(u)\in\G$ with $F(u+q(u))=\Q(u)$.  Write
 $w(u)=u+q(u)$ and $A(u)=j(w(u))=|w|w\in L^{3/2}$.  Then
 $\Q(u)=\frac13\norm{w}_3^3$ and $\norm{A}_{3/2}=\norm w_3^2$.
\item[(b)] $\langle A(u),g\rangle=0$ for every $g\in\G$; equivalently
 $\dv A(u)=0$ in the sense of distributions.
\item[(c)] $\Q(u+g)=\Q(u)$ and $w(u+g)=w(u)$ for every $g\in\G$.
\item[(d)] For $h\in L^3$, with $w=w(u)$ and $w_h=w(u+h)$,
 \begin{equation}\label{eq:cp-lip}
  \bigl|\norm{w_h}_3-\norm{w}_3\bigr|\le\norm h_3,
  \qquad
  \norm{w_h-w}_3^3\le8(\norm w_3+\norm h_3)^2\norm h_3 .
 \end{equation}
 In particular $u\mapsto w(u)$ is continuous $L^3\to L^3$, $u\mapsto A(u)$
 is continuous $L^3\to L^{3/2}$, and $\Q$ is continuous on $L^3$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) The infimum $I=\Q(u)$ satisfies $0\le I\le F(u)<\infty$.  Let
$q_n\in\G$ with $F(u+q_n)\to I$ and put $w_n=u+q_n$.  For $n,m$, the field
$\frac12(w_n+w_m)=u+\frac12(q_n+q_m)$ is admissible, so
$F(\frac12(w_n+w_m))\ge I$.  Integrating \eqref{eq:cp-midpoint} gives
\[
 \tfrac1{24}\norm{w_n-w_m}_3^3
 \le F(w_n)+F(w_m)-2F\bigl(\tfrac12(w_n+w_m)\bigr)
 \le F(w_n)+F(w_m)-2I\longrightarrow0 .
\]
Thus $(w_n)$ is Cauchy in $L^3$; let $w_n\to w$.  Then $q_n=w_n-u\to
q:=w-u$, and $q\in\G$ because $\G$ is closed.  Continuity of $F$ on $L^3$
gives $F(w)=I$.  If $w'=u+q'$ is another minimizer, the same inequality
with $w_n=w$, $w_m=w'$ yields $\frac1{24}\norm{w-w'}_3^3\le0$.  The norm
identities are immediate.

(b) For $g\in\G$ and $s\in\R$, $w+sg=u+(q+sg)$ is admissible, so
$\varphi(s)=F(w+sg)\ge F(w)=\varphi(0)$.  By \eqref{eq:cp-F-taylor},
$\varphi(s)=\varphi(0)+s\langle A,g\rangle+O(s^2)$, so
$\varphi'(0)=\langle A,g\rangle$ exists and must vanish at the minimum.
Taking $g=\nabla\phi$, $\phi\in C_c^\infty$, gives the distributional
statement.

(c) $\{u+g+q':q'\in\G\}=\{u+q:q\in\G\}$ since $\G$ is a linear space.

(d) $w+h=(u+h)+q(u)$ is admissible for $u+h$, so
$\norm{w_h}_3\le\norm{w+h}_3\le\norm w_3+\norm h_3$; symmetrically
$w_h-h=u+q(u+h)$ is admissible for $u$, so $\norm w_3\le\norm{w_h}_3+\norm
h_3$.  Next, $w_h-w=h+(q(u+h)-q(u))$ and $q(u+h)-q(u)\in\G$, so (b) for
both minimizers gives
$\langle A(u+h),w_h-w\rangle=\langle A(u+h),h\rangle$ and
$\langle A(u),w_h-w\rangle=\langle A(u),h\rangle$.  Integrating
\eqref{eq:cp-monotone},
\[
\begin{aligned}
 \tfrac14\norm{w_h-w}_3^3
 &\le\langle A(u+h)-A(u),w_h-w\rangle
 =\langle A(u+h)-A(u),h\rangle\\
 &\le\bigl(\norm{w_h}_3^2+\norm w_3^2\bigr)\norm h_3
 \le2(\norm w_3+\norm h_3)^2\norm h_3 .
\end{aligned}
\]
Continuity of $A$ follows from Lemma~\ref{lem:cubic-frechet}, and
$|\Q(u+h)-\Q(u)|=\frac13|\norm{w_h}_3^3-\norm w_3^3|$ is controlled by the
first inequality in \eqref{eq:cp-lip}.
\end{proof}

\subsection{Coercivity, scaling, and heat monotonicity}

\begin{lemma}[Gradient closure and pullback]\label{lem:gradient-closure}\leavevmode
\begin{enumerate}
\item[(a)] If $\psi\in L^3(\R^3)$ has distributional gradient
 $\nabla\psi\in L^3(\R^3;\R^3)$, then $\nabla\psi\in\G$.  In
 particular $\nabla\psi\in\G$ whenever $\psi\in C_c^1(\R^3)$.
\item[(b)] Let $\Phi:\R^3\to\R^3$ be a $C^1$ diffeomorphism with
 $\sup_x|D\Phi(x)|=:\Lambda_\Phi<\infty$ and $\det D\Phi\equiv1$.  Then
 $T_\Phi f=D\Phi^{\mathsf T}(f\circ\Phi)$ satisfies
 $\norm{T_\Phi f}_3\le\Lambda_\Phi\norm f_3$ and $T_\Phi\G\subset\G$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) Let $\chi\in C_c^\infty$ with $0\le\chi\le1$, $\chi=1$ on $\{|x|\le1\}$,
$\chi=0$ on $\{|x|\ge2\}$, and $\chi_R=\chi(\cdot/R)$.  Then
$\psi_R=\chi_R\psi\in L^3$ has compact support and weak gradient
$\chi_R\nabla\psi+\psi\nabla\chi_R\in L^3$, with
\[
 \norm{\nabla\psi_R-\nabla\psi}_3
 \le\norm{(1-\chi_R)\nabla\psi}_3+R^{-1}\norm{\nabla\chi}_\infty\norm\psi_3
 \longrightarrow0\qquad(R\to\infty)
\]
by dominated convergence.  Let $\rho_\varepsilon$ be a standard mollifier.
Then $\rho_\varepsilon*\psi_R\in C_c^\infty$ and
$\nabla(\rho_\varepsilon*\psi_R)=\rho_\varepsilon*\nabla\psi_R\to
\nabla\psi_R$ in $L^3$ as $\varepsilon\to0$
\cite[Thm.~1.2.19]{Grafakos2014}.  A diagonal choice shows that
$\nabla\psi$ is an $L^3$ limit of gradients of $C_c^\infty$ functions.

(b) Change of variables with unit Jacobian gives
$\int|f\circ\Phi|^3=\int|f|^3$, hence the norm bound.  For
$\phi\in C_c^\infty$, $\phi\circ\Phi\in C^1_c$ (its support is
$\Phi^{-1}(\operatorname{supp}\phi)$, compact because $\Phi$ is a
homeomorphism) and the chain rule gives
$\nabla(\phi\circ\Phi)=D\Phi^{\mathsf T}(\nabla\phi\circ\Phi)=T_\Phi\nabla\phi$,
which lies in $\G$ by (a).  For general $q\in\G$ choose
$\nabla\phi_n\to q$ in $L^3$; then $T_\Phi\nabla\phi_n\to T_\Phi q$ in
$L^3$ by boundedness, and $\G$ is closed.
\end{proof}

\begin{lemma}[Leray projection on $L^3$]\label{lem:leray}\leavevmode
\begin{enumerate}
\item[(a)] $\PP$ is bounded on $L^3(\R^3;\R^3)$ and on $L^2(\R^3;\R^3)$; on
 $L^2\cap L^3$ the two extensions agree, and on $L^2$,
 $\widehat{(\PP f)}_i=\hat f_i-\xi_i\xi_j|\xi|^{-2}\hat f_j$.
\item[(b)] $\PP q=0$ for every $q\in\G$.
\item[(c)] If $u\in L^2\cap L^3$ is solenoidal, then $\PP u=u$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) Boundedness on $L^3$ is \cite[Cor.~5.2.8]{Grafakos2014}; on $L^2$ the
symbol $-i\xi_j/|\xi|$ is bounded.  Both extensions are continuous
extensions from $\mathcal S$, which is dense in $L^2\cap L^3$ for the sum
norm, so they agree there.  The symbol of $R_iR_j$ is
$(-i\xi_i/|\xi|)(-i\xi_j/|\xi|)=-\xi_i\xi_j/|\xi|^2$.

(b) For $\phi\in C_c^\infty$, $\widehat{\partial_j\phi}=2\pi i\xi_j\hat\phi$,
so
$\widehat{(\PP\nabla\phi)}_i
=2\pi i\xi_i\hat\phi-\xi_i\xi_j|\xi|^{-2}\,2\pi i\xi_j\hat\phi=0$.
Thus $\PP\nabla\phi=0$; (b) follows by density and $L^3$-boundedness.

(c) Solenoidality extends to Schwartz test functions: for $\phi\in\mathcal
S$, $\chi_R\phi\in C_c^\infty$ and $\nabla(\chi_R\phi)\to\nabla\phi$ in
$L^2$, so $\langle u,\nabla\phi\rangle=0$.  By Plancherel,
$0=\langle u,\nabla\phi\rangle=\int\hat u_j(\xi)\overline{2\pi i\xi_j\hat\phi(\xi)}\,d\xi$.
Since $\{\hat\phi:\phi\in\mathcal S\}=\mathcal S$ contains $C_c^\infty(\R^3_\xi)$
and $\xi\cdot\hat u\in L^2_{\rm loc}$, we get $\xi\cdot\hat u(\xi)=0$ for
a.e.\ $\xi$.  Then $\widehat{(\PP u)}_i=\hat u_i-\xi_i(\xi\cdot\hat
u)|\xi|^{-2}=\hat u_i$, so $\PP u=u$ in $L^2$, hence in $L^3$ by (a).
\end{proof}

\begin{lemma}[Coercivity on solenoidal fields]\label{lem:quotient-coercive}
Let $u\in L^2\cap L^3$ be solenoidal, $w=w(u)$, $q=q(u)$.  Then
$u=\PP w$, $q=(I-\PP)w$, and
\begin{equation}\label{eq:cp-coercive}
 \frac{\norm u_3^3}{3C_{\PP}^3}\le\Q(u)\le\frac13\norm u_3^3,
 \qquad
 \norm q_3\le(1+C_{\PP})\norm w_3 .
\end{equation}
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:leray}, $\PP w=\PP u+\PP q=u$.  Hence
$\norm u_3\le C_{\PP}\norm w_3$ and $\norm q_3=\norm{w-\PP w}_3\le(1+C_{\PP})\norm w_3$.
The upper bound is the admissible choice $q=0$, and
$\Q(u)=\frac13\norm w_3^3$.
\end{proof}

\begin{remark}
Lemma~\ref{lem:quotient-coercive} is stated for $L^2\cap L^3$ because that
is the class of every velocity used below.  The $L^3$ Helmholtz
decomposition extends (c) of Lemma~\ref{lem:leray} to all distributionally
solenoidal $L^3$ fields; it is not needed here.
\end{remark}

\begin{lemma}[Homogeneity and critical scaling]\label{lem:quotient-scaling}
For $u\in L^3$, $a\in\R$ and $\lambda>0$,
$\Q(au)=|a|^3\Q(u)$ and $\Q(\mathcal S_\lambda u)=\Q(u)$.
\end{lemma}

\begin{proof}
The first identity uses that $\G$ is a linear space and $F(av)=|a|^3F(v)$.
For the second, $\mathcal S_\lambda$ is a linear isometry of $L^3$ (change
of variables $y=\lambda x$), and
$\mathcal S_\lambda\nabla\phi=\nabla[\phi(\lambda\,\cdot)]$ with
$\phi(\lambda\,\cdot)\in C_c^\infty$; since $\mathcal S_{1/\lambda}$ is the
inverse, $\mathcal S_\lambda$ maps $\G$ bijectively onto $\G$.  Hence
$\Q(\mathcal S_\lambda u)=\inf_{q\in\G}F(\mathcal S_\lambda(u+q))
=\inf_{q\in\G}F(u+q)=\Q(u)$.
\end{proof}

\begin{lemma}[Heat monotonicity]\label{lem:quotient-heat}
For $t>0$: $\norm{G_tf}_3\le\norm f_3$, $G_t\G\subset\G$, and
\begin{equation}\label{eq:cp-heat}
 \Q(G_tu)\le F(G_tw(u))\le\Q(u)\qquad(u\in L^3).
\end{equation}
\end{lemma}

\begin{proof}
The contraction is Minkowski's inequality \cite[Thm.~1.2.10]{Grafakos2014}
with $\norm{k_t}_1=1$.  For $\phi\in C_c^\infty$, differentiation under the
integral gives $G_t\nabla\phi=\nabla(G_t\phi)$, where $G_t\phi\in C^\infty$,
$G_t\phi\in L^3$ and $\nabla G_t\phi=G_t\nabla\phi\in L^3$ by Minkowski.
Lemma~\ref{lem:gradient-closure}(a) gives $G_t\nabla\phi\in\G$.  For
$q\in\G$ pick $\nabla\phi_n\to q$ in $L^3$; then $G_t\nabla\phi_n\to G_tq$
and $\G$ is closed.  Finally $G_tw=G_tu+G_tq(u)$ with $G_tq(u)\in\G$ is
admissible for $G_tu$, so $\Q(G_tu)\le F(G_tw)\le F(w)=\Q(u)$.
\end{proof}

\subsection{The derivative}

\begin{proposition}[Fr\'echet derivative of $\Q$]
\label{prop:quotient-derivative}
$\Q$ is Fr\'echet differentiable on $L^3(\R^3;\R^3)$ with
\begin{equation}\label{eq:cp-derivative}
 D\Q(u)[h]=\langle A(u),h\rangle=\int_{\R^3}|w(u)|w(u)\cdot h\,dx,
\end{equation}
and, with $w=w(u)$,
\begin{equation}\label{eq:cp-derivative-remainder}
 \bigl|\Q(u+h)-\Q(u)-\langle A(u),h\rangle\bigr|
 \le10\,(\norm w_3+\norm h_3)^{5/3}\norm h_3^{4/3}.
\end{equation}
In particular $D\Q(u)[g]=0$ for every $g\in\G$.
\end{proposition}

\begin{proof}
Write $w_h=w(u+h)$, $A=A(u)$, $A_h=A(u+h)$.  Upper bound: $w+h$ is
admissible for $u+h$, so by \eqref{eq:cp-F-taylor}
\[
 \Q(u+h)\le F(w+h)\le\Q(u)+\langle A,h\rangle+(\norm w_3+\norm h_3)\norm h_3^2 .
\]
Lower bound: $w_h-h$ is admissible for $u$, so
$\Q(u)\le F(w_h-h)\le F(w_h)-\langle A_h,h\rangle+(\norm{w_h}_3+\norm
h_3)\norm h_3^2$, that is,
\[
 \Q(u+h)\ge\Q(u)+\langle A,h\rangle+\langle A_h-A,h\rangle
 -(\norm w_3+2\norm h_3)\norm h_3^2 .
\]
By Lemma~\ref{lem:cubic-frechet} and \eqref{eq:cp-lip},
\[
\begin{aligned}
 |\langle A_h-A,h\rangle|
 &\le2(\norm{w_h}_3+\norm w_3)\norm{w_h-w}_3\norm h_3\\
 &\le2(2\norm w_3+\norm h_3)\cdot2(\norm w_3+\norm h_3)^{2/3}\norm h_3^{1/3}\cdot\norm h_3
 \le8(\norm w_3+\norm h_3)^{5/3}\norm h_3^{4/3}.
\end{aligned}
\]
Since $(\norm w_3+2\norm h_3)\norm h_3^2\le2(\norm w_3+\norm h_3)^{5/3}\norm
h_3^{4/3}$, both bounds give \eqref{eq:cp-derivative-remainder}, which is
$o(\norm h_3)$.  The linear map $h\mapsto\langle A,h\rangle$ is bounded on
$L^3$ because $A\in L^{3/2}$.  The last claim is
Lemma~\ref{lem:quotient-minimizer}(b).
\end{proof}

\begin{remark}
No smoothness of $w(u)$ is used or asserted anywhere in this section.  The
representative is an $L^3$ object satisfying the nonlinear divergence
condition $\dv(|w|w)=0$; no derivative of $w$ or $q$ is ever taken.
\end{remark}

\subsection{The classical trajectory class}

\begin{lemma}[Embedding and multiplication facts]\label{lem:sobolev-classical}\leavevmode
\begin{enumerate}
\item[(a)] If $s>k+\frac32$ and $|\alpha|\le k$, then for $f\in H^s(\R^3)$
 the derivative $\partial^\alpha f$ has a representative that is continuous,
 vanishes at infinity, and satisfies
 $\norm{\partial^\alpha f}_\infty\le C_{s,k}\norm f_{H^s}$.
\item[(b)] $\norm f_6\le C_S\norm{\nabla f}_2$ and
 $\norm f_3\le\norm f_2^{1/2}\norm f_6^{1/2}\le C\norm f_{H^1}$ for
 $f\in H^1(\R^3)$.
\item[(c)] Let $m\ge4$ and $u\in H^m(\R^3;\R^3)$.  Then $u\in C^2$ with
 $u,\nabla u,\nabla^2u$ bounded and uniformly continuous;
 $u,\ \nabla u,\ \Delta u,\ (u\cdot\nabla)u\in L^3$; and $u_iu_j\in H^2$
 with $\norm{u_iu_j}_{H^2}\le C\norm u_{H^m}^2$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) $\widehat{\partial^\alpha f}=(2\pi i\xi)^\alpha\hat f$ and, by
Cauchy--Schwarz,
$\int|\xi|^{|\alpha|}|\hat f|d\xi
\le\bigl(\int(1+|\xi|^2)^{|\alpha|-s}d\xi\bigr)^{1/2}\norm f_{H^s}$,
where the first factor is finite because $2(s-|\alpha|)>3$.  Fourier
inversion of an $L^1$ function is continuous and vanishes at infinity
(Riemann--Lebesgue) and agrees a.e.\ with $\partial^\alpha f$.  A continuous
function vanishing at infinity is uniformly continuous.

(b) The first inequality is Sobolev's inequality
\cite[Thm.~8.3]{LiebLoss2001}; the second is H\"older interpolation.

(c) Apply (a) with $s=m\ge4$, $k=2$.  $\nabla u\in H^{m-1}\subset H^1\subset
L^3$, $\Delta u\in H^{m-2}\subset H^1\subset L^3$, and
$\norm{(u\cdot\nabla)u}_3\le\norm u_\infty\norm{\nabla u}_3$.  For $u_iu_j$:
$\norm{u_iu_j}_2\le\norm u_\infty\norm u_2$;
$\partial_k(u_iu_j)=(\partial_ku_i)u_j+u_i\partial_ku_j$ is bounded in $L^2$
by $2\norm u_\infty\norm{\nabla u}_2$; and
$\partial_k\partial_l(u_iu_j)$ is a sum of terms $u\,\partial^2u$, bounded in
$L^2$ by $\norm u_\infty\norm{\nabla^2u}_2$, and $\partial u\,\partial u$,
bounded in $L^2$ by $\norm{\nabla u}_4^2\le\norm{\nabla u}_2\norm{\nabla u}_6
\le C\norm{\nabla u}_{H^1}^2$ using (b).
\end{proof}

\begin{definition}[Compact classical interval]\label{prem:classical-interval}
Let $T>0$ and $m\ge4$ be an integer.  A pair $(u,p)$ is a
\emph{classical solution of \eqref{eq:NS} on the compact interval $[0,T]$ in
$H^m$} if
\begin{enumerate}
\item[(i)] $u\in C([0,T];H^m(\R^3;\R^3))\cap C^1([0,T];H^{m-2}(\R^3;\R^3))$;
\item[(ii)] $u(t)$ is solenoidal for every $t\in[0,T]$;
\item[(iii)] $p(t)=R_iR_j\bigl(u_i(t)u_j(t)\bigr)$, the $L^2$ Fourier
 multiplier with symbol $-\xi_i\xi_j|\xi|^{-2}$ applied to $u_iu_j\in H^2$;
\item[(iv)] for every $t\in[0,T]$,
 $\partial_tu(t)=\nu\Delta u(t)-(u(t)\cdot\nabla)u(t)-\nabla p(t)$ as
 elements of $L^3(\R^3;\R^3)$.
\end{enumerate}
\end{definition}

\begin{remark}[The maximal classical solution belongs to this class]
\label{rem:tao-class}
Let $u_0\in\mathcal S(\R^3)^3$ be divergence-free and let $u$ be the maximal
classical solution of \eqref{eq:NS} on $[0,T_*)$ selected on
page~\pageref{premise:local}.  After the normalization
\eqref{eq:nu-normalization} to unit viscosity, Tao's Theorem~5.4
\cite{Tao2013} applies with forcing $f=0$: part (ii) gives, on
$[0,T_1]\times\R^3$ with $T_1\norm{u_0}_{H^1}^4\le c$, an $H^1$ mild
solution with $\norm u_{X^k([0,T_1]\times\R^3)}<\infty$ for every $k\ge1$,
where $X^k=L^\infty_tH^k_x\cap L^2_tH^{k+1}_x$; part (iv) gives, for
Schwartz data, that $u$ and $p$ are smooth with
$\partial_t^ju,\partial_t^jp\in L^\infty_tH^k_x([0,T_1]\times\R^3)$ for all
$j,k\ge0$.  The pressure of an $H^1$ mild solution is Tao's normalised
pressure $p=-\Delta^{-1}\partial_i\partial_j(u_iu_j)$, equation (9) of
\cite{Tao2013}, whose symbol $-\xi_i\xi_j|\xi|^{-2}$ is that of
$R_iR_j$, so (iii) holds.  Since $\partial_tu\in L^\infty_tH^k_x$ and
$\partial_t^2u\in L^\infty_tH^k_x$ for every $k$, the fundamental theorem
of calculus in $H^k$ gives $u\in C^1([0,T_1];H^k)$ for every $k$, which is
(i) for every $m$; (iv) holds pointwise for a smooth solution and the three
terms lie in $L^3$ by Lemma~\ref{lem:sobolev-classical}(c) and
Lemma~\ref{lem:quotient-pressure} below.  The maximal branch is obtained by
iterating part (ii) from $u(T_1)\in\bigcap_kH^k$; Tao's proof of (iv)
records that $u_0\in H^k_x$ for all $k$ suffices for the same conclusions.
Any compact $[0,T]\subset[0,T_*)$ is covered by finitely many such steps,
and the classes in (i) concatenate.  Identification of this branch and of
$T_*$ is the persistence-and-uniqueness premise already used on
page~\pageref{premise:local} and in Theorem~\ref{thm:continuation}; no
new premise is introduced.  Undoing \eqref{eq:nu-normalization} preserves
(i)--(iv).
\end{remark}

\begin{lemma}[Pressure gradients are annihilated]\label{lem:quotient-pressure}
Let $u\in H^m(\R^3;\R^3)$, $m\ge4$, and $p=R_iR_j(u_iu_j)$.  Then
$p\in H^2$, $p\in L^3$, $\nabla p\in L^3\cap\G$, and
$D\Q(u)[\nabla p]=\langle A(u),\nabla p\rangle=0$.
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:sobolev-classical}(c), $u_iu_j\in H^2$.  The multiplier
$-\xi_i\xi_j|\xi|^{-2}$ is bounded and commutes with $(1+|\xi|^2)$, so
$p\in H^2$ with $\norm p_{H^2}\le\sum_{i,j}\norm{u_iu_j}_{H^2}$.  Then
$p\in H^1\subset L^3$ and $\nabla p\in H^1\subset L^3$ by
Lemma~\ref{lem:sobolev-classical}(b); the distributional gradient of
$p\in H^2$ is its weak gradient.  Lemma~\ref{lem:gradient-closure}(a) gives
$\nabla p\in\G$, and Proposition~\ref{prop:quotient-derivative} gives the
last claim.
\end{proof}

\begin{lemma}[Heat generator in $L^3$]\label{lem:heat-generator}
If $u\in H^m(\R^3;\R^3)$, $m\ge4$, then
$t^{-1}(G_tu-u)\to\Delta u$ in $L^3$ as $t\downarrow0$.
\end{lemma}

\begin{proof}
$\Delta u\in H^{m-2}\subset L^2\cap L^3$.  The family $(k_s)_{s>0}$ is an
approximate identity, so $s\mapsto G_s\Delta u$ is continuous
$[0,\infty)\to L^3$ and $[0,\infty)\to L^2$ \cite[Thm.~1.2.19]{Grafakos2014}
together with the contraction property.  Hence the Riemann integral
$\int_0^tG_s\Delta u\,ds$ exists in $L^3$ and in $L^2$, and the two limits
coincide a.e.  Its $L^2$ value is computed in Fourier variables:
$\widehat{G_s\Delta u}=-4\pi^2|\xi|^2e^{-4\pi^2s|\xi|^2}\hat u$, and
pointwise in $\xi$
\[
 \int_0^t\widehat{G_s\Delta u}\,ds
 =\bigl(e^{-4\pi^2t|\xi|^2}-1\bigr)\hat u
 =\widehat{G_tu-u},
\]
so $\int_0^tG_s\Delta u\,ds=G_tu-u$ in $L^2$; the interchange of the
$s$-integral with the Fourier transform of the $L^2$-valued Riemann
integral is justified by dominated convergence, since
$|\xi|^2|\hat u|\in L^2$.  Therefore
\[
 \Bigl\|\frac{G_tu-u}t-\Delta u\Bigr\|_3
 =\Bigl\|\frac1t\int_0^t\bigl(G_s\Delta u-\Delta u\bigr)ds\Bigr\|_3
 \le\sup_{0\le s\le t}\norm{G_s\Delta u-\Delta u}_3\longrightarrow0 .
\]
\end{proof}

\begin{lemma}[Nonpositive heat direction]\label{lem:quotient-heatsign}
For $u\in H^m(\R^3;\R^3)$, $m\ge4$, define
$D_{\Q}(u)=-\langle A(u),\Delta u\rangle=-\int|w|w\cdot\Delta u\,dx$.  Then
$D_{\Q}(u)\ge0$.
\end{lemma}

\begin{proof}
Put $h_t=G_tu-u$, so $\norm{h_t}_3=O(t)$ by Lemma~\ref{lem:heat-generator}.
By Proposition~\ref{prop:quotient-derivative} and Lemma~\ref{lem:quotient-heat},
\[
 0\ge\frac{\Q(G_tu)-\Q(u)}t
 =\Bigl\langle A(u),\frac{h_t}t\Bigr\rangle+O(t^{1/3})
 \longrightarrow\langle A(u),\Delta u\rangle .
\]
\end{proof}

\begin{remark}
Lemma~\ref{lem:quotient-heatsign} is a sign, not a quantitative
dissipation estimate.  No comparison of $D_{\Q}$ with the cubic dissipation
$D_3$ of Proposition~\ref{prop:pressure} is claimed.
\end{remark}

\subsection{The transport identity by inner variation}

\begin{lemma}[Flow of the frozen velocity]\label{lem:flow}
Let $b\in C^2(\R^3;\R^3)$ with $\norm b_\infty,\ \Lambda=\norm{Db}_\infty,\
\norm{D^2b}_\infty<\infty$ and $\dv b=0$.  There is a unique
$\Phi:\R\times\R^3\to\R^3$, $(s,y)\mapsto\Phi_s(y)$, with
$\partial_s\Phi_s(y)=b(\Phi_s(y))$ and $\Phi_0=\mathrm{id}$, and:
\begin{enumerate}
\item[(a)] $\Phi_{s+r}=\Phi_s\circ\Phi_r$; each $\Phi_s$ is a $C^1$
 diffeomorphism of $\R^3$ with inverse $\Phi_{-s}$;
 $|\Phi_s(y)-y|\le|s|\norm b_\infty$.
\item[(b)] $D\Phi_s(y)$ is continuous in $(s,y)$ and satisfies
 $\partial_sD\Phi_s(y)=Db(\Phi_s(y))D\Phi_s(y)$, $D\Phi_0=I$;
 $\det D\Phi_s\equiv1$.
\item[(c)] $|D\Phi_s(y)|\le e^{\Lambda|s|}$ and, for $|s|\le1$,
 $|D\Phi_s(y)-I-s\,Db(y)|\le C_bs^2$ with
 $C_b=\tfrac12e^{\Lambda}(\norm{D^2b}_\infty\norm b_\infty+\Lambda^2)$,
 uniformly in $y$.
\item[(d)] There is $s_0=s_0(\Lambda)>0$ such that for $|s|\le s_0$,
 $|D\Phi_s(y)^{-\mathsf T}-I+s\,Db(y)^{\mathsf T}|\le C_b's^2$ uniformly in
 $y$, with $C_b'=C_b+2\Lambda^2e^{2\Lambda}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Existence, uniqueness and the group property for all $s\in\R$ follow from
the Picard--Lindel\"of theorem for the globally Lipschitz field $b$
together with the a priori bound $|\Phi_s(y)|\le|y|+|s|\norm b_\infty$,
which excludes finite-time escape \cite[Ch.~II, Thms.~1.1 and
3.1]{Hartman2002}.  Differentiability with respect to $y$, continuity of
$D\Phi$, and the variational equation are
\cite[Ch.~V, Thm.~3.1]{Hartman2002}.  Since $\Phi_{-s}\circ\Phi_s=\mathrm{id}$,
each $\Phi_s$ is a $C^1$ diffeomorphism.  Liouville's formula
\cite[Ch.~IV, Thm.~1.2]{Hartman2002} applied to the linear variational
equation gives
$\det D\Phi_s(y)=\exp\int_0^s\operatorname{tr}Db(\Phi_\sigma(y))\,d\sigma
=\exp\int_0^s(\dv b)(\Phi_\sigma(y))\,d\sigma=1$.

(c) From (b), $D\Phi_s-I=\int_0^sDb(\Phi_\sigma)D\Phi_\sigma\,d\sigma$, so
$|D\Phi_s|\le1+\Lambda\bigl|\int_0^s|D\Phi_\sigma|d\sigma\bigr|$ and
Gronwall gives $|D\Phi_s|\le e^{\Lambda|s|}$; consequently
$|D\Phi_s-I|\le|s|\Lambda e^{\Lambda|s|}$.  Next,
\[
 D\Phi_s-I-s\,Db(y)
 =\int_0^s\bigl[Db(\Phi_\sigma(y))-Db(y)\bigr]D\Phi_\sigma\,d\sigma
 +\int_0^sDb(y)\bigl[D\Phi_\sigma-I\bigr]d\sigma .
\]
The first integrand is bounded by
$\norm{D^2b}_\infty|\Phi_\sigma(y)-y|e^{\Lambda|\sigma|}\le
\norm{D^2b}_\infty\norm b_\infty|\sigma|e^{\Lambda}$ and the second by
$\Lambda^2|\sigma|e^{\Lambda}$ for $|\sigma|\le1$; integrating gives the
bound with $C_b$.

(d) Let $N_s=D\Phi_s(y)-I$, so $|N_s|\le|s|\Lambda e^{\Lambda|s|}\le\frac12$
for $|s|\le s_0$.  Then $D\Phi_s^{-1}=(I+N_s)^{-1}=I-N_s+N_s^2(I+N_s)^{-1}$
and $|D\Phi_s^{-1}-I+N_s|\le2|N_s|^2\le2\Lambda^2e^{2\Lambda}s^2$.  Combine
with $|N_s-s\,Db(y)|\le C_bs^2$ from (c) and transpose.
\end{proof}

\begin{lemma}[Transport rewrite]\label{lem:quotient-transport}
Let $u\in H^m(\R^3;\R^3)$, $m\ge4$, be solenoidal, with $w=w(u)$, $q=q(u)$,
$A=A(u)$.  Then
\begin{equation}\label{eq:cp-transport}
 \int_{\R^3}A\cdot\bigl((u\cdot\nabla)u\bigr)dx
 =\int_{\R^3}q\cdot\bigl((A\cdot\nabla)u\bigr)dx,
 \qquad\text{i.e.}\quad
 \int A_ju_i\partial_iu_j\,dx=\int q_jA_i\partial_iu_j\,dx .
\end{equation}
Both integrals are finite: $A\in L^{3/2}$, $(u\cdot\nabla)u\in L^3$,
$q\in L^3$, and $|(A\cdot\nabla)u|\le|A|\norm{\nabla u}_\infty$.
\end{lemma}

\begin{proof}
By Lemma~\ref{lem:sobolev-classical}(c), $b=u$ satisfies the hypotheses of
Lemma~\ref{lem:flow}; let $\Phi_s$ be its flow, and for $|s|\le s_0$ put
\[
 u_s=u\circ\Phi_{-s},\qquad
 q_s=D\Phi_{-s}^{\mathsf T}(q\circ\Phi_{-s})=T_{\Phi_{-s}}q .
\]
By Lemma~\ref{lem:gradient-closure}(b), $q_s\in\G$, so $u_s+q_s$ is
admissible for $\Q(u_s)$.  Change variables $x=\Phi_s(y)$ (unit Jacobian).
The chain rule for $\Phi_{-s}\circ\Phi_s=\mathrm{id}$ gives
$D\Phi_{-s}(\Phi_s(y))=D\Phi_s(y)^{-1}$, hence
$u_s(\Phi_s(y))+q_s(\Phi_s(y))=u(y)+D\Phi_s(y)^{-\mathsf T}q(y)
=w(y)+E_s(y)q(y)$ with $E_s=D\Phi_s^{-\mathsf T}-I$, and
\begin{equation}\label{eq:cp-envelope}
 \Q(u_s)\le\mathcal R(s):=F(w+E_sq),
 \qquad\mathcal R(0)=\Q(u).
\end{equation}

\emph{Right side.}  By Lemma~\ref{lem:flow}(d), $\norm{E_s}_\infty\le C|s|$
and $\norm{E_s+s\,Du^{\mathsf T}}_\infty\le C_u's^2$.  By
\eqref{eq:cp-F-taylor} with $v=w$, $h=E_sq$,
\[
 \mathcal R(s)=\Q(u)+\langle A,E_sq\rangle+O(s^2)
 =\Q(u)-s\langle A,Du^{\mathsf T}q\rangle+O(s^2),
\]
since $|\langle A,(E_s+s\,Du^{\mathsf T})q\rangle|
\le\norm A_{3/2}C_u's^2\norm q_3$.  Here
$(Du^{\mathsf T}q)_i=(\partial_iu_j)q_j$, so
\[
 \langle A,Du^{\mathsf T}q\rangle=\int A_i(\partial_iu_j)q_j\,dx
 =\int q\cdot((A\cdot\nabla)u)\,dx .
\]

\emph{Left side.}  Put $g=(u\cdot\nabla)u\in L^3$.  For each $x$,
$\sigma\mapsto u(\Phi_{-\sigma}(x))$ is $C^1$ with derivative
$-g(\Phi_{-\sigma}(x))$, so
$u_s-u=-\int_0^sg\circ\Phi_{-\sigma}\,d\sigma$ and, by Minkowski's
integral inequality and volume preservation,
\[
 \norm{u_s-u}_3\le|s|\norm g_3,
 \qquad
 \Bigl\|\frac{u_s-u}s+g\Bigr\|_3
 \le\sup_{|\sigma|\le|s|}\norm{g\circ\Phi_{-\sigma}-g}_3 .
\]
The right side tends to $0$: given $\varepsilon>0$ choose
$g_\varepsilon\in C_c(\R^3;\R^3)$ with $\norm{g-g_\varepsilon}_3<\varepsilon$;
then $\norm{g\circ\Phi_{-\sigma}-g}_3\le2\varepsilon+\norm{g_\varepsilon\circ\Phi_{-\sigma}-g_\varepsilon}_3$,
and the last term tends to $0$ as $\sigma\to0$ by uniform continuity of
$g_\varepsilon$, the bound $|\Phi_{-\sigma}(x)-x|\le|\sigma|\norm u_\infty$,
and dominated convergence on a fixed bounded set.  By
\eqref{eq:cp-derivative-remainder} with $h=u_s-u$,
\[
 \Q(u_s)=\Q(u)+\langle A,u_s-u\rangle+O(|s|^{4/3})
 =\Q(u)-s\langle A,g\rangle+o(s).
\]

\emph{Comparison.}  Insert both expansions into \eqref{eq:cp-envelope}:
$-s\langle A,g\rangle+o(s)\le-s\langle A,Du^{\mathsf T}q\rangle+O(s^2)$.
Dividing by $s>0$ and letting $s\downarrow0$ gives
$\langle A,g\rangle\ge\langle A,Du^{\mathsf T}q\rangle$; dividing by $s<0$
and letting $s\uparrow0$ gives the reverse inequality.  This is
\eqref{eq:cp-transport}.
\end{proof}

\subsection{The pressure-free evolution identity}

\begin{proposition}[Evolution of the quotient]\label{prop:quotient-evolution}
Let $(u,p)$ be a classical solution on $[0,T]$ in $H^m$, $m\ge4$
(Definition~\ref{prem:classical-interval}).  Write $w(t)=w(u(t))$,
$q(t)=q(u(t))$, $A(t)=|w(t)|w(t)$.  Then $t\mapsto\Q(u(t))$ belongs to
$C^1([0,T])$, the functions $t\mapsto D_{\Q}(u(t))$ and
$t\mapsto\int q(t)\cdot((A(t)\cdot\nabla)u(t))\,dx$ are continuous on
$[0,T]$, and for every $t\in[0,T]$
\begin{equation}\label{eq:quotient-evolution}
 \frac{d}{dt}\Q(u(t))+\nu D_{\Q}(u(t))
 =-\int_{\R^3}q(t)\cdot\bigl((A(t)\cdot\nabla)u(t)\bigr)dx,
 \qquad D_{\Q}(u(t))\ge0 .
\end{equation}
\end{proposition}

\begin{proof}
Since $H^{m-2}\hookrightarrow L^3$ continuously
(Lemma~\ref{lem:sobolev-classical}(b)), $u\in C^1([0,T];L^3)$ with
derivative $\partial_tu\in C([0,T];L^3)$.  Proposition~\ref{prop:quotient-derivative}
and the chain rule for a Fr\'echet differentiable map composed with a
$C^1$ curve give that $\Q\circ u$ is differentiable on $[0,T]$ with
\[
 \frac d{dt}\Q(u(t))=\langle A(t),\partial_tu(t)\rangle .
\]
By Lemma~\ref{lem:quotient-minimizer}(d), $t\mapsto A(t)$ is continuous into
$L^{3/2}$, so the right side is continuous and $\Q\circ u\in C^1$.  Insert
(iv) of Definition~\ref{prem:classical-interval}:
\[
 \langle A,\partial_tu\rangle
 =\nu\langle A,\Delta u\rangle-\langle A,(u\cdot\nabla)u\rangle-\langle A,\nabla p\rangle .
\]
The pressure term vanishes by Lemma~\ref{lem:quotient-pressure}; the
transport term is rewritten by Lemma~\ref{lem:quotient-transport} (each
$u(t)$ is solenoidal and in $H^m$); the heat term is $-\nu D_{\Q}(u(t))$
with $D_{\Q}\ge0$ by Lemma~\ref{lem:quotient-heatsign}.  Continuity of
$D_{\Q}(u(t))$ follows from $\Delta u\in C([0,T];H^{m-2})\subset
C([0,T];L^3)$ and continuity of $A$; continuity of the transport term
follows from $q=w-u\in C([0,T];L^3)$, $A\in C([0,T];L^{3/2})$, and
$\nabla u\in C([0,T];H^{m-1})\subset C([0,T];L^\infty)$ by
Lemma~\ref{lem:sobolev-classical}(a), together with the trilinear bound
$|\int q\cdot((A\cdot\nabla)v)|\le\norm q_3\norm A_{3/2}\norm{\nabla v}_\infty$.
\end{proof}

\begin{remark}
Identity \eqref{eq:quotient-evolution} contains no pressure term and no
derivative of the minimizer.  It is exact on every compact classical
interval.  It supplies neither a sign nor a bound for its right side.
\end{remark}

\subsection{Low strain, the missing high-strain estimate, and its consequence}

\begin{lemma}[Low-pass gradient bound]\label{lem:lowpass}
For $f\in L^2(\R^3)$ and $L\in\mathbb Z$, $S_Lf\in C^\infty$ and
$\norm{\nabla S_Lf}_\infty\le\norm{\nabla\psi}_2\,2^{5L/2}\norm f_2$.
If $f\in H^m$ then $S_Lf\in H^m$ with $\norm{S_Lf}_{H^m}\le\norm\psi_1\norm f_{H^m}$,
and $S_L$ commutes with derivatives and preserves solenoidality.
\end{lemma}

\begin{proof}
$\nabla S_Lf=(\nabla\psi_L)*f$ with $\nabla\psi_L=2^{4L}(\nabla\psi)(2^L\cdot)$,
and by Cauchy--Schwarz
$|(\nabla\psi_L*f)(x)|\le\norm{\nabla\psi_L}_2\norm f_2
=2^{4L}2^{-3L/2}\norm{\nabla\psi}_2\norm f_2$.  The remaining claims are
Minkowski's inequality, $\widehat{S_Lf}=\hat\psi(2^{-L}\xi)\hat f$, and the
fact that convolution commutes with distributional derivatives.
\end{proof}

\begin{lemma}[Low-strain Gronwall coefficient]\label{lem:quotient-lowstrain}
Let $u$ be the maximal classical solution from a divergence-free
$u_0\in\mathcal S(\R^3)^3$, let $L\in\mathbb Z$, and for $t<T_*$ put
$v=S_Lu(t)$,
\[
 K_{\rm low}(t)=-\int q(t)\cdot\bigl((A(t)\cdot\nabla)v\bigr)dx,
 \qquad
 K_L(t)=-\int q(t)\cdot\bigl((A(t)\cdot\nabla)(u(t)-v)\bigr)dx .
\]
Then $K_{\rm low}$ and $K_L$ are continuous on $[0,T]$ for every
$T<T_*$, \eqref{eq:quotient-evolution} reads
$\frac d{dt}\Q(u)+\nu D_{\Q}(u)=K_L+K_{\rm low}$, and
\begin{equation}\label{eq:cp-lowstrain}
 |K_{\rm low}(t)|\le M_L\,\Q(u(t)),
 \qquad
 M_L=3(1+C_{\PP})\norm{\nabla\psi}_2\,2^{5L/2}\norm{u_0}_2 .
\end{equation}
\end{lemma}

\begin{proof}
On each compact $[0,T]\subset[0,T_*)$, $u$ is a classical solution in
$H^m$ for every $m$ by Remark~\ref{rem:tao-class}, so
Proposition~\ref{prop:quotient-evolution} applies and the splitting
$\nabla u=\nabla v+\nabla(u-v)$ is exact.  By H\"older,
Lemma~\ref{lem:quotient-coercive}, and Lemma~\ref{lem:lowpass},
\[
\begin{aligned}
 |K_{\rm low}(t)|
 &\le\norm{\nabla v}_\infty\norm{q}_3\norm{A}_{3/2}
 \le\norm{\nabla\psi}_2\,2^{5L/2}\norm{u(t)}_2\,(1+C_{\PP})\norm w_3\cdot\norm w_3^2\\
 &=3(1+C_{\PP})\norm{\nabla\psi}_2\,2^{5L/2}\norm{u(t)}_2\,\Q(u(t)),
\end{aligned}
\]
and $\norm{u(t)}_2\le\norm{u_0}_2$ by Proposition~\ref{prop:energy}.
Continuity of $K_{\rm low}$ follows as in the proof of
Proposition~\ref{prop:quotient-evolution}, using
$\nabla S_Lu\in C([0,T];L^\infty)$ from Lemma~\ref{lem:lowpass} and
$u\in C([0,T];L^2)$; then $K_L$ is continuous as a difference.
\end{proof}

\begin{hypothesis}[Signed high-strain absorption]\label{hyp:highstrain}
For every $\nu>0$, divergence-free $u_0\in\mathcal S(\R^3)^3$, and
$0<H<\infty$, there exist $\theta\in[0,1]$, an integer
$L=L(\nu,u_0,H)$, and a finite $A_{\rm input}=A_{\rm input}(\nu,u_0,H,L)\ge0$
such that
\begin{equation}\label{eq:quotient-gap}
 \int_0^\tau K_L(t)\,dt
 \le\theta\nu\int_0^\tau D_{\Q}(u(t))\,dt+A_{\rm input}
\end{equation}
for every $0<\tau<\min\{H,T_*\}$, with the same $L$ and $A_{\rm input}$
for the entire interval.
\end{hypothesis}

As with Hypothesis~\ref{hyp:highpressure}, the existential assertion is
nontrivial: the left side could be unbounded as $\tau\uparrow T_*$.  A proof
must produce $A_{\rm input}$ without assuming the continuation bound it is
meant to imply; a remainder defined through the unknown supremum is
circular.  Because $\theta=1$ is permitted, the value of $\theta$ plays no
role below; $\theta<1$ would additionally retain
$(1-\theta)\nu\int_0^\tau D_{\Q}$.

\begin{proposition}[Conditional critical bound from high-strain absorption]
\label{prop:quotient-conditional}
Hypothesis~\ref{hyp:highstrain} implies Hypothesis~\ref{hyp:critical}, with
\begin{equation}\label{eq:cp-M}
 M(\nu,u_0,H)
 =C_{\PP}\bigl(\norm{u_0}_3^3+3A_{\rm input}\bigr)^{1/3}
 \exp\Bigl(\tfrac13M_LH\Bigr),
 \qquad M_L=3(1+C_{\PP})\norm{\nabla\psi}_2\,2^{5L/2}\norm{u_0}_2 ,
\end{equation}
where $L$ and $A_{\rm input}$ are those provided by
Hypothesis~\ref{hyp:highstrain}.  Consequently, by
Theorem~\ref{thm:conditional}, Hypothesis~\ref{hyp:highstrain} implies
Theorem~\ref{def:target}.
\end{proposition}

\begin{proof}
Fix $\nu$, $u_0$, $H$, and let $\theta$, $L$, $A_{\rm input}$ be given by
Hypothesis~\ref{hyp:highstrain}.  Let $0<\tau_1<\min\{H,T_*\}$; then
$[0,\tau_1]$ is a compact classical interval.  Put $y(t)=\Q(u(t))$, a
continuous nonnegative function on $[0,\tau_1]$ by
Proposition~\ref{prop:quotient-evolution}.  Integrating
\eqref{eq:quotient-evolution} in the form of
Lemma~\ref{lem:quotient-lowstrain} over $[0,\tau]$, $0<\tau\le\tau_1$, and
using \eqref{eq:quotient-gap}, \eqref{eq:cp-lowstrain}, $\theta\le1$ and
$D_{\Q}\ge0$,
\[
 y(\tau)+(1-\theta)\nu\int_0^\tau D_{\Q}(u(t))\,dt
 \le y(0)+A_{\rm input}+M_L\int_0^\tau y(t)\,dt .
\]
Gronwall's inequality for the continuous function $y$ gives
$y(\tau)\le\bigl(y(0)+A_{\rm input}\bigr)e^{M_L\tau}
\le\bigl(y(0)+A_{\rm input}\bigr)e^{M_LH}$ for all $\tau\in[0,\tau_1]$; the
case $\tau=0$ is trivial.  Since $\tau_1<\min\{H,T_*\}$ was arbitrary, the
bound holds on $[0,\min\{H,T_*\})$.  By Lemma~\ref{lem:quotient-coercive},
$y(0)\le\frac13\norm{u_0}_3^3$ and
$\norm{u(\tau)}_3^3\le3C_{\PP}^3y(\tau)$, so
\[
 \sup_{0\le\tau<\min\{H,T_*\}}\norm{u(\tau)}_3^3
 \le C_{\PP}^3\bigl(\norm{u_0}_3^3+3A_{\rm input}\bigr)e^{M_LH},
\]
which is \eqref{eq:missing} with $M$ as in \eqref{eq:cp-M}.  The last
sentence is Theorem~\ref{thm:conditional}.
\end{proof}

\begin{remark}[Scope of the high-strain hypothesis]\label{rem:highstrain-scope}
At the quantifiers of Hypothesis~\ref{hyp:highstrain}, the hypothesis is
equivalent to global continuation of the selected classical branch, exactly
as for Hypothesis~\ref{hyp:highpressure}.  The forward direction is
Proposition~\ref{prop:quotient-conditional} together with
Theorem~\ref{thm:continuation}.  Conversely, if $T_*=\infty$ for the given
datum, take $L=0$ and $\theta=0$: $K_0$ is continuous on the compact
classical interval $[0,H]$ by Lemma~\ref{lem:quotient-lowstrain}, so
$A_{\rm input}=\int_0^H|K_0(t)|dt$ is finite and \eqref{eq:quotient-gap}
holds.  This converse assumes global continuation and supplies no method
for proving it.  Neither \eqref{eq:quotient-gap} nor any quantitative
dissipation mechanism for $D_{\Q}$ is proved here; bounding $K_L$ by
$\norm{\nabla(u-S_Lu)}_\infty\Q(u)$ merely renames the missing
high-frequency control.  The quotient route is an alternative to the
pressure route of Section~4; the same critical bound is the missing input
in both, and no novelty or Millennium solution is asserted.
\end{remark}
```

Required edits elsewhere in `main.tex` (not made here): the Proof boundary
section should add one sentence naming Hypothesis~`hyp:highstrain` as the
alternative unproved producer and Proposition~`prop:quotient-conditional`
as its proved consequence; `\cite{Grafakos2014,LiebLoss2001,Hartman2002}`
need the bibliography entries above.

## 5. Verification notes on the proofs

- **Build check.**  The block of §4 was spliced into a scratch copy of
  `main.tex` (preamble additions and bibliography entries included, section
  `sec:quotient` replaced) and compiled with `latexmk -pdf`: 16 pages, no
  undefined references, no LaTeX warnings, no overfull boxes; pages 8, 9 and
  12 were rendered and inspected.  The paper repository was not modified.

- **Signs and indices.**  \((Du^{\mathsf T}q)_i=(\partial_iu_j)q_j\), so
  \(\langle A,Du^{\mathsf T}q\rangle=\int A_i(\partial_iu_j)q_j
  =\int q\cdot((A\cdot\nabla)u)\); \(((u\cdot\nabla)u)_j=u_i\partial_iu_j\).
  The comparison in `lem:quotient-transport` gives
  \(\langle A,(u\cdot\nabla)u\rangle=\langle A,Du^{\mathsf T}q\rangle\), which
  is HF17 evolution (9) and review item 6 with identical signs.
  Substituting into \(\frac d{dt}\Q=\nu\langle A,\Delta u\rangle
  -\langle A,(u\cdot\nabla)u\rangle\) gives the manuscript's
  `eq:quotient-evolution` with \(D_{\Q}=-\langle A,\Delta u\rangle\).
- **Constants.**  \(\|q\|_3\le(1+C_{\PP})\|w\|_3\) (not \(C_{\PP}\|w\|_3\));
  \(\|A\|_{3/2}=\|w\|_3^2\); \(\|w\|_3^3=3\Q\).  Hence
  \(|K_{\rm low}|\le3(1+C_{\PP})\|\nabla\psi\|_2 2^{5L/2}\|u_0\|_2\,\Q\),
  matching \(C2^{5L/2}\|u_0\|_2\Q\) in the manuscript and
  \(C2^{5L/2}E_0^{1/2}\Q\) in HF17 (14) with \(E_0=\|u_0\|_2^2\).
- **Remainder exponents.**  `prop:quotient-derivative` gives an
  \(O(\|h\|^{4/3})\) remainder; `lem:quotient-transport` needs only
  \(o(|s|)\) on the left and uses \(O(s^2)\) on the right.  The expansion
  of \(F\) at \(w\) in the right side of the envelope uses
  \(\|E_sq\|_3\le\|E_s\|_\infty\|q\|_3=O(|s|)\).
- **Flow regularity.**  \(m\ge4\) gives \(u\in C^2_b\) (Lemma
  `lem:sobolev-classical`(a) with \(s=4>2+3/2\)), which is what `lem:flow`
  needs for the \(s^2\) expansions.  \(m=3\) would give only uniformly
  continuous \(Du\) and \(o(|s|)\) expansions, which would also suffice for
  the comparison argument, but the standing assumption keeps \(m\ge4\) as
  in HF17.
- **Heat generator.**  The \(L^3\) generator limit is proved for
  \(u\in H^m\) via Fourier in \(L^2\) plus strong continuity in \(L^3\);
  it does not rely on the general domain theory of the \(L^3\) heat
  semigroup.
- **Gronwall use.**  Gronwall is applied to the continuous function
  \(\Q(u(t))\) on a compact classical interval, after integration; no
  regularizer, no uniform-in-\(\eta\) coercivity, and none of the HF16
  functional-value-limit machinery is needed.  The HF16 review's
  qualification concerns the pressure route only.

## 6. Obligations

| ID | Statement | Status | Severity | Note |
| --- | --- | --- | --- | --- |
| O1 | Maximal classical branch: iteration of Tao 5.4(ii) from \(u(T_1)\in\bigcap_kH^k\), finiteness of steps on compact subintervals, identification with the branch of `premise:local`, and its maximal time \(T_*\). | literature (Tao 5.4 DI; iteration/identification asserted by the manuscript's existing `premise:local`) | major | Not new to this section; must be a labelled axiom in Phase I. Tao's remark "it would have sufficed to have \(u_0\in H^k_x\)" is DI (p. 34). |
| O2 | Riesz transforms bounded on \(L^3(\mathbb R^3)\) (needed only for \(C_{\PP}<\infty\)). | literature (Grafakos Cor. 5.2.8, DI); mathlib-absent | major for Phase II | Phase I axiom with verified source record. |
| O3 | \(C^1\) dependence of ODE flows on the initial point, variational equation, Liouville formula. | literature (Hartman V.3.1, IV.1.2, REC); mathlib-absent | major for Phase II | Theorem numbers to be re-inspected. Everything else in `lem:flow` is proved inline. |
| O4 | Sobolev inequality \(H^1(\mathbb R^3)\subset L^6\). | literature (Lieb–Loss Thm 8.3, REC); Mathlib has a compact-support GNS inequality (`eLpNorm_le_eLpNorm_fderiv_of_eq`), density extension needed | minor | Could be replaced by \(H^1\subset L^3\) via Fourier? No: \(H^1\not\subset L^\infty\); \(L^3\) membership of \(H^1\) needs Sobolev or Hausdorff–Young interpolation. Keep import. |
| O5 | Approximate identity convergence in \(L^p\), Minkowski/Young, Plancherel, Riemann–Lebesgue, change of variables under unit-Jacobian diffeomorphism. | literature (Grafakos 1.2.10, 1.2.12, 1.2.19 DI; Riemann–Lebesgue and Plancherel in Mathlib) | minor | mathlib-available for most. |
| O6 | Pressure of the Tao mild solution equals \(R_iR_j(u_iu_j)\) (symbol identity between Tao's (9) and Grafakos' Riesz symbol). | proved (symbol computation; Tao (9) DI p. 5, Grafakos Prop. 5.1.14 DI) | minor | Sign convention checked: both symbols are \(-\xi_i\xi_j/\lvert\xi\rvert^2\). |
| O7 | Every proof in §4 not listed above. | proved | — | Written in full; independent audit still required before integration into `main.tex`. |
| O8 | Hypothesis `hyp:highstrain` (`eq:quotient-gap`). | missing (UNPROVED) | blocking for NS-R3 | Not claimed. Equivalent to global continuation at its quantifiers (Remark `rem:highstrain-scope`). |
| O9 | Quantitative comparison of \(D_{\Q}\) with \(D_3\) or any coercive lower bound for \(D_{\Q}\). | missing | not required by CP1 | Explicitly a non-claim. |

## 7. Frontier record

**CLAIM AND SCOPE.**  The rewritten section proves, for the original
unforced equation on \(\mathbb R^3\) with divergence-free Schwartz data and
the maximal classical branch: existence/uniqueness/Euler–Lagrange for the
\(L^3\) gradient-quotient minimizer; coercivity on solenoidal
\(L^2\cap L^3\) fields with constant \(C_{\PP}\); amplitude and critical
scaling invariance; heat monotonicity; Fréchet differentiability with an
explicit \(O(\|h\|^{4/3})\) remainder; annihilation of the Riesz pressure
gradient on \(H^m\), \(m\ge4\); nonpositivity of the heat direction; the
transport identity by inner variation; the pressure-free \(C^1\) evolution
identity `eq:quotient-evolution` on every compact classical interval; the
low-strain bound with explicit constant; and the conditional implication
`hyp:highstrain` \(\Rightarrow\) `hyp:critical` with explicit
\(M(\nu,u_0,H)\).

**EVIDENCE.**  Full proofs in §4; imports isolated in §3 with DI/REC labels;
Tao Theorem 5.4 and pressure normalisation directly inspected
(arXiv:1108.1165v4 pp. 3–6, 33–35); Grafakos numbering directly inspected.

**FIRST GAP.**  `hyp:highstrain`: a signed, input-only, finite-horizon bound
for \(\int_0^\tau K_L\) uniform up to \(\min\{H,T_*\}\).  Unchanged from
HF17.

**SURVIVING CONDITIONAL SUFFIX.**  `prop:quotient-conditional`: any proof of
`hyp:highstrain` yields `hyp:critical` with the explicit constant
\(C_{\PP}(\|u_0\|_3^3+3A_{\rm input})^{1/3}e^{M_LH/3}\), and then
`thm:conditional` yields the target.

**NON-CLAIMS.**  No proof of `eq:quotient-gap`; no sign or bound for
\(K_L\); no smoothness of \(w\) or \(q\); no quantitative dissipation for
\(D_{\Q}\); no comparison with \(D_3\); no HIGH-PRESSURE theorem; no
continuation bound; no regularity result; no novelty claim for the quotient
construction; the terminal claim NS-R3 is not claimed.

**NEXT DISTINCT ACTION.**  Independent proof audit of §4 (especially
`lem:quotient-transport` and `lem:heat-generator`), then controller
integration into `main.tex` with the preamble and bibliography additions,
then Phase-I source records for O1–O4.
