# Independent audit of the HF01 source table

Status: primary-source audit performed 5 September 2026. This note checks
the six rows of `hf01-source-table.md`; it does not edit that table and does
not promote any claim. The conclusion that none of the sources proves
HIGH-PRESSURE survives, but three rows require material correction.

## 1. Tran and Yu (2016): pass with metadata and hypothesis repairs

The cited PDF is by **Chuong V. Tran and Xinwei Yu**, not Tran alone. In
Section 2 they set \(r\geq3\) and \(q=(r+6)/3\), hence \(3\leq q\leq r\).
Their Lemma 2 assumes that a pressure moderator \(P\), as defined in Lemma 1,
satisfies
\[
 \|p+P\|_{L^2}\leq c'_2\|u\|_{L^4}^2.                 \tag{9}
\]
It chooses \(c_1>0\), depending on \(c'_2\), \(\|u_0\|_2\), and the Sobolev
constant, sets
\(\Omega(t)=\{x:|u(x,t)|>c_1\|u(t)\|_{L^r}\}\), and proves
\[
 \int_{\mathbb R^3\setminus\Omega}
 |p+P|\,|u|^{q-2}\widehat u\cdot\nabla|u|\,dx
 \leq \frac12
 \bigl\||u|^{(q-2)/2}\nabla|u|\bigr\|_2^2.
\]
The left side is a signed integral whose pressure factor has been replaced
by \(|p+P|\); it is not the absolute value of the whole integral. The ambient
equation is the unit-viscosity, unforced Cauchy problem on \(\mathbb R^3\),
with smooth divergence-free, sufficiently decaying initial data and a
classical solution on its interval of existence. The table should name both
authors and record \(r,q\), the dependence of \(c_1\), and the moderator
assumption. Its comparison with HF is otherwise sound: the lemma controls
only the low-velocity region and assumes a trajectory-dependent pressure
moderator estimate. Primary source: [Tran--Yu PDF, Lemma 2, pp. 2--3](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/12230/Tran_2016_Regularity_AML_AAM.pdf?isAllowed=true&sequence=1).

## 2. Beirão da Veiga and Yang (2020): pass with exact data hypotheses

Theorem 5.2 is accurately numbered. It takes
\(\Omega=\mathbb R^3\) or \(\mathbb T^3\), a weak solution of the unforced
unit-viscosity system, and divergence-free
\(v_0\in L^2(\Omega)\cap L^4(\Omega)\). For \(0\leq\theta\leq1\), finite
\(p,q\), and
\[
 \frac{\pi}{(e^{-|x|^2}+|v|)^\theta}
 \in L^p(0,T;L^{q,\infty}(\Omega)),
 \qquad \frac2p+\frac3q=2-\theta,
\]
it concludes regularity on \((0,T]\times\Omega\). On the torus, Remark 5.1
states equivalence with denominator \((1+|v|)^\theta\). The row should add
\(v_0\in L^2\cap L^4\), finite \(p,q\), and normalized viscosity. Its
assessment relative to HF is correct. Primary source:
[Theorem 5.2 and Remark 5.1](https://arxiv.org/html/2007.02089#S5.Thmtheorem2).

## 3. Ji--Wang--Wei (2019): fail in theorem attribution, repairable

The row states the two correct pressure exponents but assigns the
pressure-gradient alternative to Theorem 1.2. Both alternatives are in
**Theorem 1.1**. For a weak solution on \(\mathbb R^3\) with divergence-free
\(u_0\in L^2\cap L^4\), Theorem 1.1 gives regularity on \((0,T]\) if either
\[
 \|\Pi\|_{L^{p,\infty}_tL^{q,\infty}_x}\leq\varepsilon_1,
 \quad \frac2p+\frac3q=2,\quad \frac32<q<\infty,
\]
or
\[
 \|\nabla\Pi\|_{L^{p,\infty}_tL^{q,\infty}_x}\leq\varepsilon_1,
 \quad \frac2p+\frac3q=3,\quad 1<q<\infty.
\]
By contrast, **Theorem 1.2 is a velocity-gradient criterion**: it assumes
\(u_0\in L^2\cap W^{1,2}\) and small
\(\nabla u\in L^{p,\infty}_tL^{q,\infty}_x\) on the line
\(2/p+3/q=2\), \(3/2<q<\infty\). Replace “Theorem 1.2 gives the
gradient-pressure analogue” by “Theorem 1.1(2) gives the gradient-pressure
analogue”; use Theorem 1.2 only for a gradient-of-velocity row. The conclusion
that these assumed small critical Lorentz norms do not yield HF remains
valid. Primary source:
[Theorems 1.1--1.2](https://arxiv.org/html/1909.09960#S1.Thmtheorem1).

## 4. Gallagher--Koch--Planchon (2012): failed extraction and wrong source

The claimed “GKP Lemma 6.1” does not exist in arXiv:1012.0145v3. That paper
has Sections 1--4 and Appendix A; its HTML contents confirm there is no
Section 6, and a search finds neither “Lemma 6.1” nor the displayed \(L^4\)
formula.

The inequality is instead **Lemma 6.1 of Beirão da Veiga--Yang,
arXiv:2007.02089**. For a regular solution \((v,\pi)\) on
\(\Omega\times[0,T]\), it states
\[
 \frac14\frac d{dt}\int_\Omega|v|^4
 +\frac12\int_\Omega|\nabla v|^2|v|^2
 +\frac12\int_\Omega|\nabla|v|^2|^2
 \leq\int_\Omega|\pi|^2|v|^2.                         \tag{6.1}
\]
Thus the formula survives, but the source attribution, link, and year in row
4 must be replaced. It may be folded into row 2 or retained as a separate
result from the same paper. Primary sources:
[GKP contents](https://arxiv.org/html/1012.0145) and
[Beirão da Veiga--Yang, Lemma 6.1](https://arxiv.org/html/2007.02089#S6.Thmlemma1).

## 5. He--Wang--Zhou (2017): pass with notation clarification

Theorem 1.1 is correctly quoted. A suitable weak solution in
\(Q(1)=B(1)\times(-1,0)\) satisfies \(u\in L^\infty(Q(1/2))\) if
\[
 \|u\|_{L^{p,q}(Q(1))}+\|\Pi\|_{L^1(Q(1))}<\varepsilon,
 \qquad 1\leq \frac2q+\frac3p<2,\quad 1\leq p,q\leq\infty.
\]
The paper defines \(L^{p,q}(Q(r))=L^q_tL^p_x\); the table should state this
ordering because conventions vary. “Bounded in \(Q(1/2)\)” is the exact
conclusion. The source develops a local pressure decomposition in Lemma 2.1,
but that decomposition is not part of the theorem's hypotheses. The table's
conclusion concerning HF is correct. Primary source:
[Theorem 1.1](https://arxiv.org/html/1709.01382#S1.Thmtheorem1).

## 6. Tran--Yu--Dritschel (2021): theorem exists, criterion incomplete

The bibliographic attribution and Theorem 3.1 are correct. The theorem takes
a three-dimensional Leray--Hopf solution of the unit-viscosity initial-value
problem on \(\mathbb R^3\), assumed smooth on \((0,T)\), and gives continuation
through \(T\) under any of three criteria. Criterion (a), equation (3.16), is
not merely time-integrability of \(\Gamma_s/R_0^2\). For some \(s>3\) it
requires
\[
 \int_0^T
 \left(\frac{\Gamma_s}{R_0^2}\right)^{s/(s-3)}
 \|u\|_{L^s}^{2s/(s-3)}dt<\infty.                    \tag{3.16}
\]
Equations (3.14)--(3.15) define
\[
 R_0=\frac{\||u|^{(q-2)/2}\nabla|u|\|_{L^2}}
 {\||u|^{(q-2)/2}\nabla|u|\|_{L^2(\Omega_0)}}\geq1,
 \qquad
 \Gamma_q=
 \frac{\int_{\Omega_0}p^2|u|^{q-2}dx}{\|u\|_{L^{q+2}}^{q+2}}.
\]
Equations (3.21)--(3.23) are a different family, specialized to the \(L^3\)
evolution and \(s\in(3/2,9/4]\). They use a different correlation
\(\Gamma'_s\), the pressure norm \(\|p\|_{L^s(\Omega_0)}\), \(R_0\), and an
explicit denominator \(\|u\|_3^3\). Equation (3.22) is a differential
Gronwall/Osgood-type inequality; equation (3.23), not Theorem 3.1(a), records
the corresponding integral criterion. The table should print the full
integrand in (3.16) and separate the later \(L^3\) criterion.

This source is the closest of the six to the manuscript's signed pressure
mechanism because equation (3.14) begins from pressure work on a reduced
high-velocity set and retains a negative weighted-dissipation term. It still
does not address a Fourier high-output tail, and every continuation criterion
assumes time integrability involving velocity/pressure correlation and
solution norms. The paper states that the pressure-work integrand is not sign
definite and that quantitative knowledge of its correlation coefficients is
lacking. Primary source:
[Theorem 3.1 and equations (3.14)--(3.23)](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/velocitypressure-correlation-in-navierstokes-flows-and-the-problem-of-global-regularity/CE28509C5B6844BC5F27F3EF52075E47).

## Required repairs to the source table

1. Change row 1 to Tran--Yu, and add \(r\geq3\), \(q=(r+6)/3\), the
   dependence of \(c_1\), and the signed-integral qualification.
2. Add \(v_0\in L^2\cap L^4\), finite \(p,q\), and unit viscosity to row 2;
   describe the torus denominator as \(1+|v|\).
3. Attribute both pressure alternatives to Ji--Wang--Wei Theorem 1.1 and
   identify Theorem 1.2 as the \(\nabla u\) criterion.
4. Replace the nonexistent GKP Lemma 6.1 by Beirão da Veiga--Yang Lemma 6.1,
   or merge it into row 2.
5. State the \(L^{p,q}=L^q_tL^p_x\) convention and exact \(L^\infty\)
   conclusion in row 5.
6. Restore the missing factor \(\|u\|_{L^s}^{2s/(s-3)}\) and exponent
   \(s/(s-3)\) in row 6, and keep equations (3.21)--(3.23) distinct from
   Theorem 3.1(a).

After these repairs, all six entries remain useful negative evidence. None
supplies a trajectory-independent estimate for the signed Fourier tail, an
input-only remainder, or the coefficient required by HIGH-PRESSURE.
