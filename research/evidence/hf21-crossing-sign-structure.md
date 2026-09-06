# HF21-B: distance to the nonlinear-Hodge class, and the sign structure of the time-integrated transport term

**AUDIT STATUS (2026-09-06).** This note has been independently audited:
`hf21-review-crossing-sign-structure.md`, **VERDICT: REPAIR**. The controller
applied every repair the review prescribes, on 2026-09-06. Three defects were
found; all three are repaired here.

- **B1 (first bad bridge), §3.2.** The first-order expansion of
  \(K(U+\varepsilon h)\) at \(\mathcal M\) omitted a term of the same order as
  the one it kept, and the boxed conditional it supported was **logically
  inverted** — a bound with exponent above one would *force* the nonlinear
  projection to be non-Lipschitz, not require it to be Lipschitz — which
  contradicted this note's own record item (iv). The expansion and the box are
  deleted and replaced by the review's Lemmas R1 and R2, reproduced verbatim.
  Under the audited Hölder-\(\frac12\) rate alone the family refutes only
  exponents \(\alpha>2\), leaving \(\alpha\in(1,2]\) open.
- **B2, Theorem 4.5 item 3, second display.** The claimed good-set bound does
  not follow from its proof and is not derivable from the ingredients. It is
  replaced by the review's Lemma R3, reproduced verbatim, and the residual
  impossibility is recorded as obstruction O3.
- **B3, the former Proposition 4.3.** Correct but **not new**: it is
  `prop:scaling`(iii) \eqref{eq:L4L3} of the manuscript plus one time-Hölder
  step. The novelty claim is withdrawn, the manuscript proposition is cited in
  its place, and the review's Lemma R4 is reproduced verbatim.

One result is **strengthened** by the review and is recorded in the stronger
form: Theorem 4.5 item 1 now carries the \(\tau\)-uniform crossing-measure
bound R4.4, \(|\mathcal B_\tau|\le24C_S^2C_\sharp^4E_0^2\nu^{-5}\), in place of
the \(\tau^{1/4}\)-growing bound of the pre-audit version. The corrections O1a
(constant power \(3\to1\)) and O1b (restored \(\mathcal Q^{(1-\alpha)/3}\)
factor; "strictly stronger" downgraded to "at least as strong") are applied to
obstruction O1, Corollary 4.2 is presented as a dictionary with an explicit
constant rather than as a new implication, and HF18-B is removed from the
premise list everywhere except the two places the review certifies it is
genuinely used (the scope sentence of §3.3 and §4.6).

Nothing is promoted and no statement is strengthened beyond what the review
licenses. No HIGH-PRESSURE, HIGH-STRAIN, CRITICAL or NS-R3 result is asserted;
the first gap is unchanged and is **not** closed; every non-claim of the
pre-audit note is preserved. The review's own numerical checks (Bregman
constants, the O2 arithmetic) are bounded evidence, never proof, and none of
them is load-bearing; this note itself still uses no numerics.

---

Lane HF21-B, MODE: DISCOVER, 2026-09-06. Owned file; nothing else in the
repository is edited, and nothing is committed.

Inputs [DI]: `PLAN.md` ("Frontier packet", "Beyond the checkpoint",
"HF16–HF17", "HF18", "HF19", "HF20", "HF21", "Ordered next actions");
`../navier-paper/main.tex` `sec:quotient` in full (labels `def:quotient`,
`lem:cubic-pointwise`, `lem:cubic-frechet`, `lem:density`,
`lem:quotient-minimizer`, `lem:gradient-closure`, `lem:leray`,
`lem:quotient-coercive`, `lem:quotient-scaling`, `lem:quotient-stability`,
`prop:quotient-derivative`, `lem:quotient-pressure`, `lem:quotient-chainrule`,
`def:qe-dissipation`, `lem:quotient-heatsign`, `lem:quotient-transport`,
`prop:quotient-evolution`, `lem:quotient-lowstrain`, `hyp:highstrain`,
`prop:quotient-conditional`, `rem:highstrain-scope`, `rem:no-monotone`) and,
outside that section, `prop:energy`, `def:D3P3`, `prop:pressure`,
`prop:scaling` with \eqref{eq:L4L3} and `rem:mismatch`, `hyp:highpressure`,
`hyp:absorption`, `lem:absorption-split`, `cor:absorption-consequence`,
`prop:lowpressure`, `thm:continuation`, `hyp:critical`, `thm:conditional`;
`hf18-hodge-regularity.md` with `hf18-review-hodge-regularity.md` (PASS);
and the audit of this note, `hf21-review-crossing-sign-structure.md` (REPAIR,
repairs applied).

**Premise discipline after the audit.** The audited HF18-A note is the only
repository evidence used as a premise for the displayed results of §§1, 2, 3,
4.1–4.5. Two dependency corrections prescribed by the audit are applied here.

- **HF18-B** (`hf18-divergence-speed-link.md` with
  `hf18-review-divergence-speed-link.md` (REPAIR) and
  `hf18-review-divergence-speed-link-r2.md` (PASS, S1–S4 applied)) is **not**
  a premise of any displayed result of §§1, 2, 3, 4.1–4.5. It is used in
  exactly two places and is cited only there: the scope sentence of §3.3 (its
  Proposition 1.4, that \(\mathcal M\) is the range of \(A\mapsto|A|^{-1/2}A\)
  over solenoidal \(A\in L^{3/2}\)) and §4.6 (its (3.2), Remark 1.3,
  Proposition 3.1, and \(\int|w|\sigma^2\le\frac12D_3(w)\)). Listing it among
  the note's premises overstated the dependency surface of the surviving
  results.
- **HF17** (`hf17-quotient-functional.md`, `hf17-quotient-evolution.md`) is
  read as background but is **not** a separate premise: everything this note
  uses from it is available through the manuscript labels
  `prop:quotient-evolution`, `lem:quotient-transport`, `def:qe-dissipation`.

Read but **not used as premises**: `hf19-second-order-falsifier.md`,
`hf19-temporal-normal-form.md`, `hf19-difference-functional.md` (all
unaudited), and `hf20-harmonic-strain-test.md` (audited REPAIR; its integrated
content is the manuscript's `rem:no-monotone`). Every statement of theirs that
touches this note is flagged where it occurs and is never a step. Source tags:
[DI] directly inspected in this programme, [MO] metadata only, never
load-bearing.

---

**MODE / RESULT: DISCOVER, audited REPAIR, repairs applied. Result: partly
affirmative, with an exact obstruction, and the gap is not closed.**

Answering the lane question "does the time-integrated transport term have
sign structure that the pointwise term lacks":

*Yes, in exactly two respects, both proved here from audited inputs.*
(i) The time integral of \(K\) carries a **signed boundary term**: with
\(d_2:=F(u)-\mathcal Q(u)\ge0\) (an exact, scale-invariant distance to the
nonlinear-Hodge class \(\mathcal M\)),
\[
 \int_0^\tau K\,dt=\underbrace{d_2(0)-d_2(\tau)}_{\text{boundary},\ \le d_2(0)\le\frac13\|u_0\|_3^3}
 +\ \nu\int_0^\tau\!\big(D_3(w)-D_3(u)\big)dt+\int_0^\tau\! P_3\,dt ,
\]
an exact identity in which two of the four terms have a sign
(\(-d_2(\tau)\le0\) and \(-\nu\int D_3(u)\le0\)) while the pointwise \(K(t)\)
has none. (ii) Along a trajectory, \(\mathcal Q\) can increase **only on a
set of times of input-bounded measure**: \(\mathcal Q'\le0\) whenever
\(C_\sharp\|q\|_3\le\nu\), and, in the \(\tau\)-uniform form supplied by the
audit (R4.4, Theorem 4.5 item 1),
\(\big|\{t<\tau:\ C_\sharp\|q(t)\|_3>\nu\}\big|\le(C_\sharp/\nu)^4\!\int_0^\tau\!d_1^4dt
\le24\,C_S^2\,C_\sharp^4\,E_0^2\,\nu^{-5}\), uniformly in \(\tau<T_*\) and
with no \(\tau^{1/4}\) growth.

*No, in the respect that matters.* The signed part of the identity is
exactly the pressure-route flux: the identity converts the HIGH-STRAIN
spacetime gap into the HIGH-PRESSURE spacetime gap with an explicit
input remainder (§4.2), and supplies no new sign. And the crossing bound
cannot be upgraded: the two facts "\(|K|\le C_\sharp\|q\|_3D_3(w)\)" and
"\(\int_0^\tau\|q\|_3^3dt\le A_1(\text{input})\)" are, as a pair,
*provably insufficient* for the first gap (§4.5, explicit family, which
adapts verbatim to the \(L^4\) form of the distance bound), and the
only Hölder split that uses them needs \(D_3\in L^r_t\), \(r>1\), which
already implies the Ladyzhenskaya–Prodi–Serrin conclusion (§4.4).

Three further items are proved and are new relative to the audited record;
one is a strengthening of an existing audited line rather than a new theorem;
and one item claimed as new in the pre-audit version is **withdrawn**:

- **(R1)** the exact comparison lattice between the four candidate
  distances, including that \(\|\operatorname{div}(|u|u)\|_{3/2}\) is
  **not** scale-invariant while \(\|q\|_3\), \(F-\mathcal Q\) and
  \(\|(I-\mathbb P)(|u|u)\|_{3/2}\) are (§1);
- **(R2)** the unconditional refinement \(|K|\le C_\sharp\|q\|_3D_3(w)\),
  \(C_\sharp=\tfrac32C_9S\), i.e. exponent \(\alpha=1\) in the lane's
  question, together with the consequent **regularity criterion in the
  distance to \(\mathcal M\)** rather than in the critical norm (§3). Per the
  audit this is recorded as a *strengthening of an existing audited line* —
  it is the line of the audited HF18-A Theorem 4 proof immediately before the
  substitution that produces \(C_*\) — and **not** as a new theorem;
- **(R3)** **withdrawn as new.** The input-only spacetime bound
  \(\int_0^\tau\|q\|_3^3dt\lesssim E_0^{3/2}\nu^{-3/4}\tau^{1/4}\) of §4.3 is
  `prop:scaling`(iii) \eqref{eq:L4L3} of the manuscript plus one time-Hölder
  step, with the same \(E_0,\nu,\tau\) weights. The manuscript proposition is
  cited in its place; its \(L^4_tL^3_x\) form is in fact stronger, being
  \(\tau\)-uniform, and it is what yields the \(\tau\)-uniform crossing bound
  R4.4 (§4.3, §4.4);
- **(R4)** the Gronwall term \(M\int_0^\tau\mathcal Q\,dt\) and the
  Littlewood–Paley split in `hyp:highstrain` are **removable**: the frozen gap
  is equivalent, with input-only changes of \(A_{\rm input}\), to the
  \(L\)-free, \(M\)-free statement
  \(\int_0^\tau K\le\theta\nu\int_0^\tau D_3(w)+A\) (§4.3). After the audit
  this costs no new lemma at all: `prop:scaling`(iii) supplies the required
  input bound directly.

**The first gap is not closed and nothing here is promoted.**

---

## 0. Setting and audited inputs

\(u\) is the classical branch of `prop:localtheory` on \([0,T_*)\) from a
divergence-free Schwartz datum \(u_0\), \(\nu>0\), \(E_0:=\|u_0\|_2^2\);
package (R) of `subsec:qe-trajectories` holds on every compact
\([0,T]\subset[0,T_*)\), in particular \(u(t)\in H^m\), \(m\ge4\),
solenoidal. \(\mathcal G_3\), \(\mathcal Q\), \(q=q(u)\), \(w=u+q\),
\(A=|w|w\), \(j(z)=|z|z\), \(F(v)=\frac13\|v\|_3^3\), \(V=|w|^{1/2}w\),
\(\mathbb P\), \(C_3=C_{\mathbb P}\), \(C_{3/2}\), \(C_9\) (Leray on \(L^9\)),
\(S\) (Sobolev \(\|f\|_6\le S\|\nabla f\|_2\)) as in `sec:quotient` and
HF18-A/B. All integrals are over \(\mathbb R^3\) unless a time integral is
displayed.

Audited facts used, with locations:

- (Q1) `lem:quotient-minimizer`: existence, uniqueness, \(\langle A,g\rangle=0\)
  for \(g\in\mathcal G_3\), \(\operatorname{div}A=0\) in \(\mathcal D'\),
  \(q(u+g)=q(u)-g\).
- (Q2) `lem:cubic-pointwise` \eqref{eq:cp-monotone}/\eqref{eq:cp-taylor} and
  `lem:cubic-frechet`: for \(a,b,h\in\mathbb R^3\),
  \((j(a)-j(b))\cdot(a-b)=\frac{|a|+|b|}2\big(|a-b|^2+(|a|-|b|)^2\big)\ge\frac12|a-b|^3\)
  and \(|f(a+h)-f(a)-j(a)\cdot h|\le(|a|+|h|)|h|^2\), \(f=\frac13|\cdot|^3\);
  their \(L^3\) forms.
- (Q3) `lem:quotient-coercive`: \(\mathcal Q(u)\le F(u)\) (hence
  \(\|w\|_3\le\|u\|_3\)), \(\mathbb Pw=u\), \(\|u\|_3^3\le3C_3^3\mathcal Q(u)\),
  \(\|q\|_3\le(1+C_3)\|w\|_3\).
- (Q4) `lem:leray`(b),(c),(d) with `lem:gradient-closure`: \(\mathbb P\)
  bounded on \(L^3\) and \(L^{3/2}\), \(\mathbb Pq=0\) for \(q\in\mathcal G_3\),
  \((I-\mathbb P)\psi\in\mathcal G_3\) for \(\psi\in C_c^\infty\), and the
  duality \(\langle\mathbb Pf,g\rangle=\langle f,\mathbb Pg\rangle\) for
  \(f\in L^{3/2}\), \(g\in L^3\) (Step 1 of `lem:leray`(d), extended from
  \(L^2\) by density and the two-sided boundedness).
- (Q5) `prop:quotient-evolution`: \(t\mapsto\mathcal Q(u(t))\in C^1\) and
  \(\mathcal Q'+\nu D_{\mathcal Q}(u)=K\), \(K=-\int q\cdot((A\cdot\nabla)u)\),
  \(D_{\mathcal Q}\ge0\); `lem:quotient-lowstrain` for the split
  \(K=K_L+K_{\rm low}\), \(|K_{\rm low}|\le M_L\mathcal Q\),
  \(M_L=3(1+C_3)C_B2^{5L/2}\|u_0\|_2\).
- (Q6) HF18-A (audited PASS): (A1)–(A5) as quoted in HF18-B §0. In
  particular \(V\in H^1\), \(\|V\|_2^2=3\mathcal Q\), \(A\in W^{1,3/2}\) with
  \(\nabla A=D\Phi(V)\nabla V\) a.e.,
  \(D\Phi(V)=|V|^{1/3}(I+\frac13\hat V\otimes\hat V)\); \(u,w\in L^9\) with
  \(\|u\|_9\le C_9\|w\|_9\) and \(\|w\|_9^{3/2}=\|V\|_6\le S\|\nabla V\|_2\);
  \(D_{\mathcal Q}(u)=D_3(w)\) with \(\frac89\|\nabla V\|_2^2\le D_3(w)\le\|\nabla V\|_2^2\);
  the derivative-free form \(K=-\int q\cdot((u\cdot\nabla)A)\) (F6); the size
  bound \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\),
  \(C_*=\frac32 3^{1/3}(1+C_3)C_9S\).
- (Q7) HF18-B (audited PASS after S1–S4). **Not a premise of any displayed
  result of §§1, 2, 3, 4.1–4.5**; per the audit's dependency correction it is
  used in exactly two places, the scope sentence of §3.3 and §4.6, and is
  cited only there. The facts used are:
  \(\mathcal M=\{w\in L^3:\operatorname{div}(|w|w)=0\}\)
  is the range of \(A\mapsto|A|^{-1/2}A\) over solenoidal \(A\in L^{3/2}\)
  (Prop. 1.4, §3.3 only); \(K_L=\int q\cdot\nabla\Pi_L=-\langle\operatorname{div}w,\Pi_L\rangle\),
  \(\Pi_L=R_iR_j(A_iu^{hi}_j)\) (3.2, §4.6 only); the strain form
  \(K=-\int|w|\,w\cdot S(u)\,w\) and \(\int A\cdot((q\cdot\nabla)u)=0\)
  (Prop. 3.1, §4.6 only); \(\int|w|\sigma^2\le\frac12D_3(w)\) (§4.6 only); the
  classification of §2.6, in which
  (H1) \(w\in W^{1,1}_{\rm loc}\), (H2) \(\sigma\in L^{3/2}\), the weighted
  Calderón–Zygmund inequality (W) and \(\|w(u)\|_2\le C\|u\|_2\) are OPEN.
- (P1) `prop:energy`: \(\frac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u\|_2^2=\frac12\|u(s)\|_2^2\);
  \(\int_0^{T_*}\|\nabla u\|_2^2dt\le E_0/(2\nu)\).
- (P2) `def:D3P3` and `prop:pressure`(ii): with \(X=\|u\|_3^3\),
  \(D_3(u)=\int\big(|u||\nabla u|^2+|u||\nabla|u||^2\big)\ge0\) (zero integrand
  on \(\{u=0\}\)) and \(P_3=\int p\,u\cdot\nabla|u|\),
  \[
   \tfrac13X(t)-\tfrac13X(s)+\nu\int_s^tD_3(u)\,d\tau=\int_s^tP_3\,d\tau ,
   \qquad 0\le s\le t<T_* ,                                        \tag{0.1}
  \]
  with \(D_3(u),P_3\) measurable and bounded on compact subintervals.
- (P3) `hyp:absorption`: \(\exists\theta\in[0,1)\) such that for every
  \(\nu,u_0,H\) there is finite \(A\) with
  \(\int_0^\tau P_3\le\theta\nu\int_0^\tau D_3(u)+A\) for all
  \(\tau<\min\{H,T_*\}\); `hyp:highpressure` implies it
  (`lem:absorption-split`).

Two notations must not be confused: \(D_3(u)\) is the *manuscript's* cubic
dissipation of `def:D3P3`, evaluated at the solenoidal \(u\); \(D_3(w)\) is
HF18-A's weighted dissipation of the minimizing representative, equal to
\(D_{\mathcal Q}(u)\) by (Q6). They coincide exactly on \(\mathcal M\)
(where \(w=u\)) and are unrelated in general; no inequality between them is
claimed anywhere below.

**Scaling.** \((a,\lambda)\) denotes amplitude \(u\mapsto au\) and dilation
\(u\mapsto\lambda u(\lambda\cdot)\), with \(\|f(\lambda\cdot)\|_p=\lambda^{-3/p}\|f\|_p\)
and, for the evolution, \(\nu\sim(a,\lambda^0)\),
\(dt\sim(a^{-1},\lambda^{-2})\) (HF18-B §0, [DI]).

---

## 1. "Distance to \(\mathcal M\)" made precise, with exact comparisons

### 1.1 The class and the four candidates

\[
 \mathcal M:=\{v\in L^3(\mathbb R^3;\mathbb R^3):\ \operatorname{div}(|v|v)=0\ \text{in }\mathcal D'\},
 \qquad \mathcal M_{\rm sol}:=\mathcal M\cap\{\operatorname{div}v=0\} .
\]
For \(u\) solenoidal in \(L^3\) put
\[
 d_1(u):=\|q(u)\|_3,\qquad
 d_2(u):=F(u)-\mathcal Q(u),\qquad
 d_3(u):=\|\operatorname{div}(|u|u)\|_{3/2},\qquad
 d_4(u):=\|(I-\mathbb P)\,j(u)\|_{3/2}.
\]
\(d_2\) is the quantity called \(-\Delta\) in the unaudited HF19-D; it is
defined and used here from (Q3) alone, and nothing from that note is
imported. \(d_3\) is finite for \(u\in H^m\), \(m\ge4\), since
\(\operatorname{div}(|u|u)=u\cdot\nabla|u|\) a.e. (\(|u|\) Lipschitz,
\(\operatorname{div}u=0\)) and \(|u\cdot\nabla|u||\le|u||\nabla u|\in L^{3/2}\).
\(d_4\) is the *critical* (scale-invariant) form of \(d_3\): for \(u\in H^m\),
\((I-\mathbb P)j(u)=\nabla\Delta^{-1}\operatorname{div}(|u|u)\), so
\(d_4=\|\operatorname{div}(|u|u)\|_{\dot W^{-1,3/2}}\) up to the fixed
Calderón–Zygmund constants.

**Lemma 1.1 (zero sets agree).** For solenoidal \(u\in L^3\) the following
are equivalent: (a) \(u\in\mathcal M\); (b) \(q(u)=0\); (c) \(d_2(u)=0\);
(d) \(d_4(u)=0\); and for \(u\in H^m\) also (e) \(d_3(u)=0\).

*Proof.* (b)\(\Rightarrow\)(a): \(w=u\) and \(\operatorname{div}A=0\) by
(Q1). (a)\(\Rightarrow\)(b): if \(\operatorname{div}j(u)=0\) then
\(\langle j(u),\nabla\phi\rangle=0\) for \(\phi\in C_c^\infty\), hence
\(\langle j(u),g\rangle=0\) for all \(g\in\mathcal G_3\) by density
(\(j(u)\in L^{3/2}\), \(g\in L^3\)); the convex function
\(g\mapsto F(u+g)\) on \(\mathcal G_3\) is Gâteaux differentiable with
derivative \(\langle j(u),\cdot\rangle\) at \(g=0\) (the dominated-convergence
computation in the proof of `lem:quotient-minimizer`(c)), so \(0\) is a
global minimizer and \(q(u)=0\) by uniqueness. (b)\(\Leftrightarrow\)(c) and
(b)\(\Leftrightarrow\)(d) follow from Prop. 1.2 and Prop. 1.3 below.
(a)\(\Leftrightarrow\)(e) is the definition. \(\square\)

Thus \(\mathcal M_{\rm sol}=\{u\ \text{solenoidal}:q(u)=0\}\), on which
\(w=u\), \(A=j(u)\), \(\mathcal Q=F\), \(D_{\mathcal Q}=D_3(w)=D_3(u)\),
\(K=0\) and \(P_3=\int p\operatorname{div}(|u|u)=0\): both audited balances
degenerate to \(\mathcal Q'=\frac13X'=-\nu D_3(u)\) at such an instant.

### 1.2 Comparison of \(d_1\) and \(d_2\)

**Proposition 1.2.** For every solenoidal \(u\in L^3\),
\[
 d_2(u)=\int_{\mathbb R^3}B\big(w,-q\big)\,dx,\qquad
 B(a,d):=\tfrac13|a+d|^3-\tfrac13|a|^3-j(a)\cdot d\ \ge0,
\]
and
\[
 \boxed{\ \max\Big\{\tfrac16\|q\|_3^3,\ \tfrac14\!\int|w||q|^2\Big\}
 \ \le\ d_2(u)\ \le\ (\|w\|_3+\|q\|_3)\,\|q\|_3^2\ \le\ (2+C_3)\,(3\mathcal Q)^{1/3}d_1^2 .\ }
 \tag{1.1}
\]

*Proof.* \(u=w-q\), so
\(F(u)=F(w)+\langle j(w),-q\rangle+\int B(w,-q)\), and
\(\langle j(w),q\rangle=\langle A,q\rangle=0\) by (Q1); hence
\(d_2=F(u)-\mathcal Q(u)=\int B(w,-q)\). For the pointwise bounds write
\(B(a,d)=\int_0^1\big(j(a+\theta d)-j(a)\big)\cdot d\,d\theta\) (the
fundamental theorem of calculus for the \(C^1\) function
\(\theta\mapsto\frac13|a+\theta d|^3\), \(\nabla f=j\) by
`lem:cubic-pointwise`). By the identity in (Q2) with \(b=a\), \(a\to a+\theta d\):
\(\big(j(a+\theta d)-j(a)\big)\cdot(\theta d)
=\frac{|a+\theta d|+|a|}2\big(\theta^2|d|^2+(|a+\theta d|-|a|)^2\big)
\ge\frac12\big(|a+\theta d|+|a|\big)\theta^2|d|^2\), which is
\(\ge\frac12\theta^3|d|^3\) (as \(|a+\theta d|+|a|\ge\theta|d|\)) and also
\(\ge\frac12|a|\theta^2|d|^2\). Dividing by \(\theta\) and integrating
\(\int_0^1\theta^2d\theta=\frac13\), \(\int_0^1\theta\,d\theta=\frac12\) gives
\(B(a,d)\ge\frac16|d|^3\) and \(B(a,d)\ge\frac14|a||d|^2\). The upper bound
is \eqref{eq:cp-taylor} of `lem:cubic-pointwise`. Integrate, use Hölder
\(\int(|w|+|q|)|q|^2\le(\|w\|_3+\|q\|_3)\|q\|_3^2\), then (Q3). \(\square\)

The two lower bounds are not comparable and both are needed: \(d_2\gtrsim d_1^3\)
is the correct behaviour far from \(\mathcal M\), and \(d_2\gtrsim\int|w||q|^2\)
is the correct (quadratic) behaviour near \(\mathcal M\), where the weight
\(|w|\) cannot be replaced by \(\|w\|_3\) — Hölder runs the wrong way, and
that mismatch is exactly the degeneracy of the cubic functional on
\(\{w=0\}\).

### 1.3 Comparison of \(d_1\), \(d_4\), \(d_3\)

**Proposition 1.3.** For every solenoidal \(u\in L^3\),
\[
 \boxed{\ \tfrac12\,d_1^2\ \le\ d_4\ \le\ (1+C_{3/2})\big(\|u\|_3+\|w\|_3\big)\,d_1
 \ \le\ 2(1+C_{3/2})C_3(3\mathcal Q)^{1/3}d_1 .\ }                         \tag{1.2}
\]
Consequently \(d_4=0\iff d_1=0\), and
\(d_1\le 2\,d_4^{1/2}\), \(d_2\ \ge\ \tfrac16\Big(\dfrac{d_4}{2(1+C_{3/2})C_3(3\mathcal Q)^{1/3}}\Big)^{3}\).

*Proof.* Lower bound: by (Q2) in \(L^3\) form
(`lem:cubic-frechet` \eqref{eq:cp-F-monotone}) with \(v=w\), \(v'=u\),
\(\langle j(w)-j(u),q\rangle\ge\frac12\|q\|_3^3\); \(\langle j(w),q\rangle=0\)
by (Q1), so \(-\langle j(u),q\rangle\ge\frac12\|q\|_3^3\). By (Q4),
\(\langle\mathbb Pj(u),q\rangle=\langle j(u),\mathbb Pq\rangle=0\), hence
\(-\langle(I-\mathbb P)j(u),q\rangle\ge\frac12\|q\|_3^3\) and Hölder gives
\(\frac12\|q\|_3^3\le d_4\|q\|_3\). Upper bound: \(A=j(w)\) is solenoidal in
\(L^{3/2}\) (Q1); for solenoidal \(f\in L^{3/2}\) one has
\((I-\mathbb P)f=0\), because for \(\psi\in C_c^\infty\),
\(\langle(I-\mathbb P)f,\psi\rangle=\langle f,(I-\mathbb P)\psi\rangle=0\) by
(Q4) — \((I-\mathbb P)\psi\in\mathcal G_3\) (Step 2 of `lem:leray`(d) with
`lem:gradient-closure`) and \(f\) annihilates \(\mathcal G_3\) by density —
and `lem:density`(a). Hence
\(d_4=\|(I-\mathbb P)(j(u)-j(w))\|_{3/2}\le(1+C_{3/2})\|j(u)-j(w)\|_{3/2}\),
and \(\|j(u)-j(w)\|_{3/2}\le(\|u\|_3+\|w\|_3)\|q\|_3\) by
`lem:cubic-frechet` \eqref{eq:cp-F-lipschitz}. The last displayed
consequences use \(\|u\|_3\le C_3\|w\|_3\), \(\|w\|_3\le\|u\|_3\) (Q3) and
(1.1). \(\square\)

*Two steps of this proof are unstated in the manuscript but repairable; the
audit records them and they are written out here.* (i) `lem:leray`(b) states
\(\|\mathbb P\psi\|_{3/2}\le C_{3/2}\|\psi\|_{3/2}\) for \(\psi\in C_c^\infty\)
only; the extension of \(\mathbb P\) to \(L^{3/2}\) and the duality
\(\langle\mathbb Pf,g\rangle=\langle f,\mathbb Pg\rangle\) for
\(f\in L^{3/2}\), \(g\in L^3\) follow by taking \(f_n\in C_c^\infty\to f\) in
\(L^{3/2}\), \(g_n\in L^2\cap L^3\to g\) in \(L^3\) and passing to the limit
in `lem:leray`(a). (ii) \((I-\mathbb P)\psi=\nabla\Theta\in\mathcal G_3\) for
\(\psi\in C_c^\infty\) needs \(\Theta\in L^3\), which holds because
\(\Theta=\check g\) with \(g\in L^1\cap L^2\) gives
\(\Theta\in L^2\cap L^\infty\), and then `lem:gradient-closure` applies. The
chain \(\|u\|_3+\|w\|_3\le2C_3\|w\|_3\) uses \(C_3=C_{\mathbb P}\ge1\), which
is automatic (\(\mathbb P^2=\mathbb P\), \(\mathbb P\ne0\) on \(L^3\)); were
\(C_{\mathbb P}<1\) the right-hand constant would have to read
\(\max\{1,C_{\mathbb P}\}\).

**Proposition 1.4 (the \(L^{3/2}\) divergence and the cubic dissipation).**
For \(u\in H^m\), \(m\ge4\), solenoidal,
\[
 d_3(u)\ \le\ D_3(u)^{1/2}\,\|u\|_3^{1/2},                                   \tag{1.3}
\]
where \(D_3(u)\) is the manuscript's cubic dissipation of `def:D3P3`.

*Proof.* \(|u\cdot\nabla|u||\le|u||\nabla|u||\) pointwise, with the
convention that the left side is \(0\) on \(\{u=0\}\). Then
\(|u|^{3/2}|\nabla|u||^{3/2}=\big(|u||\nabla|u||^2\big)^{3/4}\,|u|^{3/4}\), and
Hölder with exponents \((4/3,4)\) gives
\(\int|u|^{3/2}|\nabla|u||^{3/2}\le\big(\int|u||\nabla|u||^2\big)^{3/4}\big(\int|u|^3\big)^{1/4}\).
Raise to the power \(2/3\) and use \(\int|u||\nabla|u||^2\le D_3(u)\). \(\square\)

### 1.4 Scaling

Under \((a,\lambda)\), with \(\mathcal Q\sim(a^3,\lambda^0)\),
\(D_3(w),D_3(u)\sim(a^3,\lambda^2)\), \(K,P_3\sim(a^4,\lambda^2)\),
\(E=\|u\|_2^2\sim(a^2,\lambda^{-1})\), \(\nu\sim(a,\lambda^0)\):

| quantity | amplitude | dilation | critical? |
|---|---|---|---|
| \(d_1=\|q\|_3\) | \(a\) | \(\lambda^0\) | yes |
| \(d_2=F-\mathcal Q\) | \(a^3\) | \(\lambda^0\) | yes |
| \(d_4=\|(I-\mathbb P)j(u)\|_{3/2}\) | \(a^2\) | \(\lambda^0\) | yes |
| \(d_3=\|\operatorname{div}(|u|u)\|_{3/2}\) | \(a^2\) | \(\lambda^{1}\) | **no** |
| \(\int|w||q|^2\) | \(a^3\) | \(\lambda^{0}\) | yes |

Every inequality of §§1.2–1.3 is consistent on both parameters (e.g. (1.2):
\(a^2\lambda^0\) throughout; (1.1): \(a^3\lambda^0\) throughout). (1.3) is
consistent as \((a^2,\lambda)=(a^{3/2},\lambda)(a^{1/2},\lambda^0)\).

**Consequence for the rest of the note.** \(d_3\) carries one power of
\(\lambda\) and therefore cannot appear alone in any scaling-consistent
bound for a critical quantity; it must be paired with a factor carrying
\(\lambda^{-1}\) (a length: \(2^{-L}\), \(\nu/\|u\|_\infty\), …). The three
scale-invariant distances \(d_1,d_2,d_4\) are, by (1.1)–(1.2), mutually
equivalent up to powers and factors of \(\mathcal Q^{1/3}\); \(d_1\) is the
one that appears linearly in the transport estimate of §3, so it is the
distance used below.

---

## 2. Exact evolution of the distance along a classical solution

Neither the minimizer nor any of \(q,w,A\) is differentiated anywhere in
this section: the two ingredients are the audited integrated balances (0.1)
and (Q5), both of which were themselves proved without differentiating the
minimizer (`rem:qe-transport-scope`).

**Proposition 2.1 (distance balance).** Let \(0\le s\le t<T_*\). Then
\(t\mapsto d_2(u(t))=F(u(t))-\mathcal Q(u(t))\) is continuous and
absolutely continuous on every compact \([0,T]\subset[0,T_*)\), and
\[
 \boxed{\ d_2(t)-d_2(s)\ =\ \int_s^t\Big[\underbrace{P_3-K}_{\text{fluxes}}\ +\ \nu\big(D_3(w)-D_3(u)\big)\Big]d\tau\ \ge\ -d_2(s),\ }
                                                                     \tag{2.1}
\]
with \(d_2\ge0\) throughout. Equivalently, a.e. in \(t\),
\(d_2'=P_3-K+\nu\big(D_3(w)-D_3(u)\big)\).

*Proof.* Subtract the integrated quotient balance from (0.1). Precisely,
by (Q5) \(\mathcal Q\circ u\in C^1([0,T])\) with
\(\mathcal Q(t)-\mathcal Q(s)+\nu\int_s^tD_{\mathcal Q}=\int_s^tK\), the
integrands being continuous, and \(D_{\mathcal Q}=D_3(w)\) by (Q6). By (P2),
\(F(u(t))-F(u(s))+\nu\int_s^tD_3(u)=\int_s^tP_3\) with \(D_3(u),P_3\)
integrable on \([s,t]\). Subtracting gives (2.1); \(d_2\ge0\) is (Q3), and
absolute continuity follows because both \(F\circ u\) and \(\mathcal Q\circ u\)
are integrals of \(L^1_{\rm loc}\) functions. \(\square\)

**Remark 2.2 (why \(d_2\) and not \(d_1\)).** \(t\mapsto q(t)\) is
continuous into \(L^3\) (`lem:quotient-stability` with \(u\in C([0,T];L^3)\)),
but the audited stability estimate is only Hölder-\(\frac12\):
\(\|w(t')-w(t)\|_3\le2(\|w(t)\|_3+\|u(t')-u(t)\|_3)^{1/2}\|u(t')-u(t)\|_3^{1/2}\),
so all that follows for \(d_1\) is
\(|d_1(t')-d_1(t)|\le\|q(t')-q(t)\|_3\le C|t'-t|^{1/2}\) on compact
subintervals: \(d_1\) is \(\frac12\)-Hölder in time and is *not* known to be
differentiable or absolutely continuous. Any evolution written for \(d_1\)
would have to differentiate the minimizer, which is forbidden. \(d_2\), by
contrast, is a difference of two functionals each of which has an audited
exact balance, so (2.1) is unconditional. Upper and lower Dini derivatives
of \(d_1\) are therefore *not* estimated here; the comparisons (1.1)–(1.2)
transfer information between \(d_1\) and \(d_2\) instead.

**Remark 2.3 (independent derivation, and the overlap with unaudited HF19-D).**
(2.1) can be obtained pointwise in time without subtracting balances, from
the elementary identity
\[
 K=-\langle j(w)-j(u),\,(u\cdot\nabla)u\rangle ,                       \tag{2.2}
\]
valid because \(\langle j(u),(u\cdot\nabla)u\rangle=\int u\cdot\nabla(|u|^3/3)=0\)
for solenoidal \(u\in H^m\); inserting the momentum equation
\((u\cdot\nabla)u=\nu\Delta u-\nabla p-\partial_tu\) and using
\(\langle j(w),\nabla p\rangle=0\) (`lem:quotient-pressure`),
\(\langle j(w),\Delta u\rangle=-D_{\mathcal Q}\) (`def:qe-dissipation`),
\(\langle j(u),\Delta u\rangle=-D_3(u)\), and
\(\langle j(w)-j(u),\partial_tu\rangle=\mathcal Q'-F'\)
(`prop:quotient-derivative` and the Fréchet derivative of \(F\)) reproduces
the a.e. form of (2.1). The route through the integrated balances is the one
used above because it needs no instantaneous identification of
\(\langle j(u),\Delta u\rangle\) with \(D_3(u)\) at velocity zeros. The
unaudited `hf19-difference-functional.md` reports an evolution for the same
difference; nothing from it is used, and the derivation here rests only on
`prop:pressure` and `prop:quotient-evolution`.

---

## 3. The exponent \(\alpha\): how far is \(|K|\lesssim d^\alpha\cdot(\text{companion})\) available?

### 3.1 \(\alpha=1\) is unconditional

**Proposition 3.1.** At every time of the classical interval,
\[
 \boxed{\ |K|\ \le\ \tfrac43\,C_9S\,\|q\|_3\,\|\nabla V\|_2^2
 \ \le\ C_\sharp\,d_1\,D_3(w),\qquad C_\sharp:=\tfrac32\,C_9S .\ }        \tag{3.1}
\]

*Proof.* All inputs are audited (Q6). By (F6),
\(K=-\int q\cdot((u\cdot\nabla)A)\), absolutely convergent. Pointwise
\(|\nabla A|=|D\Phi(V)\nabla V|\le\frac43|V|^{1/3}|\nabla V|=\frac43|w|^{1/2}|\nabla V|\),
since \(D\Phi(V)=|V|^{1/3}(I+\frac13\hat V\otimes\hat V)\) has operator norm
\(\frac43|V|^{1/3}\) and \(|V|^{1/3}=|w|^{1/2}\). Hence
\(|K|\le\frac43\int|q|\,|u|\,|w|^{1/2}|\nabla V|\), and Hölder with
\(\frac13+\frac16+\frac12=1\) gives
\(|K|\le\frac43\|q\|_3\,\big\||u||w|^{1/2}\big\|_6\,\|\nabla V\|_2\). Now
\(\big\||u||w|^{1/2}\big\|_6^6=\int|u|^6|w|^3\le\|u\|_9^6\|w\|_9^3\) (Hölder
with \(\frac32,3\)), so
\(\big\||u||w|^{1/2}\big\|_6\le\|u\|_9\|w\|_9^{1/2}\le C_9\|w\|_9^{3/2}=C_9\|V\|_6\le C_9S\|\nabla V\|_2\).
Finally \(\|\nabla V\|_2^2\le\frac98D_3(w)\). \(\square\)

Two checks. (i) Consistency with the audited size bound: inserting
\(\|q\|_3\le(1+C_3)\|w\|_3=(1+C_3)(3\mathcal Q)^{1/3}\) turns (3.1) into
\(|K|\le C_*\mathcal Q^{1/3}D_3(w)\) with exactly the audited
\(C_*=\frac32 3^{1/3}(1+C_3)C_9S=3^{1/3}(1+C_3)C_\sharp\); (3.1) is the
line of the audited HF18-A Theorem 4 proof immediately *before* that
substitution, and implies the audited bound on substitution. Per the audit it
is recorded as a *strengthening of an existing audited line*, not as a new
theorem. (ii) Scaling: \(d_1D_3\sim(a\cdot a^3,\lambda^0\cdot\lambda^2)=(a^4,\lambda^2)=K\) ✓.

By (1.1)–(1.2), (3.1) can be rewritten in the other distances:
\(|K|\le C_\sharp(6d_2)^{1/3}D_3(w)\) and \(|K|\le2C_\sharp d_4^{1/2}D_3(w)\),
both scaling-consistent (\(d_2^{1/3},d_4^{1/2}\sim(a,\lambda^0)\)).

### 3.2 The full monomial lattice, and what an \(\alpha>1\) bound would require

**Proposition 3.2 (scaling lattice).** Consider candidate bounds
\(|K|\le C\,d_1^\alpha\,\mathcal Q^{b}\,D_3(w)^{c}\,E^{e}\,2^{Ld}\) with
constants independent of \(u\). Two-parameter scaling forces
\[
 \alpha+3b+3c+2e=4\ (\text{amplitude}),\qquad 2c-e+d=2\ (\text{dilation}).
\]
With \(e=d=0\) the admissible set is the segment
\(c=1,\ \alpha+3b=1\); \(\alpha=0,b=\frac13\) is the audited bound and
\(\alpha=1,b=0\) is (3.1). Every \(\alpha>1\) forces \(b<0\), i.e. a
negative power of \(\mathcal Q\).

*Proof.* Substitute the table of §1.4. \(\square\)

So two-parameter scaling does **not** forbid the monomials here (unlike
HF18-A §4 for the pure \((\mathcal Q,D_3)\) family, where it pins the unique
exponent \(\frac13,1\)); it pins the companion to be exactly \(D_3(w)^1\) and
converts the question "best \(\alpha\)" into "how much of
\(\mathcal Q^{1/3}\) can be replaced by \(d_1\)". Proposition 3.1 answers:
all of it, and (3.1) is the endpoint \(b=0\) of the admissible segment.

**What an \(\alpha>1\) bound would require, exactly (repaired: audit defect
B1, the first bad bridge).** The pre-audit version of this paragraph carried
the note's first invalid bridge, and both of its displayed claims are deleted
rather than patched.

1. Its first-order expansion of \(K(u_\varepsilon)\) at
   \(U\in\mathcal M_{\rm sol}\) omitted the term
   \(-\langle A_\varepsilon-j(U),\mathbb P((U\cdot\nabla)U)\rangle\), which
   under the very upgrade it assumed
   (\(\|A_\varepsilon-j(U)\|_{3/2}=O(\varepsilon)\)) is \(O(\varepsilon)\),
   i.e. **exactly the same order as the term it kept**, not
   \(O(\varepsilon^{3/2})\).
2. Its boxed conditional — "an \(\alpha>1\) bound is compatible with the
   audited record only if the nonlinear projection \(u\mapsto q(u)\) is
   Lipschitz in \(L^3\) at points of \(\mathcal M\)" — was **logically
   inverted**. Lipschitz continuity of \(q\) at \(\mathcal M\) is exactly what
   would *refute* \(\alpha>1\); an \(\alpha>1\) bound *forces* the projection
   to be non-Lipschitz. The box contradicted this note's own record item
   (iv), which states the correct direction, so the pre-audit note was
   internally inconsistent.

The expansion and the box are replaced by the audit's Lemmas R1 and R2,
reproduced here verbatim.

**Lemma R1 (exact expansion at \(\mathcal M\)).** Let
\(U\in\mathcal M_{\rm sol}\cap C_c^\infty(\mathbb R^3)^3\) be solenoidal with
\(\operatorname{div}(|U|U)=0\), let \(h\in C_c^\infty(\mathbb R^3)^3\) be
solenoidal, \(u_\varepsilon=U+\varepsilon h\),
\(A_\varepsilon=A(u_\varepsilon)\), \(p_U\) the normalised pressure of \(U\).
Then \(w(U)=U\), \(q(U)=0\), \(A(U)=j(U)\), and for every
\(\varepsilon\in\mathbb R\)
\[
 K(u_\varepsilon)=-\big\langle A_\varepsilon-j(U),\ \mathbb P\big((U\cdot\nabla)U\big)\big\rangle
  -\varepsilon\big\langle j(U),(h\cdot\nabla)U+(U\cdot\nabla)h\big\rangle
\]
\[
  \qquad\qquad-\varepsilon\big\langle A_\varepsilon-j(U),(h\cdot\nabla)U+(U\cdot\nabla)h\big\rangle
  -\varepsilon^2\big\langle A_\varepsilon,(h\cdot\nabla)h\big\rangle .
\]
Moreover
\(\|A_\varepsilon-j(U)\|_{3/2}\le4(\|U\|_3+\varepsilon\|h\|_3)^{3/2}(\varepsilon\|h\|_3)^{1/2}\),
so unconditionally \(K(u_\varepsilon)=O(\varepsilon^{1/2})\), and the
coefficient of \(\varepsilon\) contains the term
\(-\langle\frac{d}{d\varepsilon}A_\varepsilon|_{0},\mathbb P((U\cdot\nabla)U)\rangle\)
whenever \(\varepsilon\mapsto A_\varepsilon\) is differentiable at \(0\) in
\(L^{3/2}\).

*Proof.* \(q(U)=0\) and \(w(U)=U\) by Lemma 1.1, so \(A(U)=j(U)\).
`lem:quotient-transport` gives \(K(v)=-\langle A(v),(v\cdot\nabla)v\rangle\)
for the fields in question. Expand
\((u_\varepsilon\cdot\nabla)u_\varepsilon=(U\cdot\nabla)U+\varepsilon[(h\cdot\nabla)U+(U\cdot\nabla)h]+\varepsilon^2(h\cdot\nabla)h\),
insert, and add and subtract \(j(U)\) in the first slot; the term
\(-\langle j(U),(U\cdot\nabla)U\rangle\) vanishes because
\(\langle j(U),(U\cdot\nabla)U\rangle=\int U\cdot\nabla(|U|^3/3)=0\) for
solenoidal \(U\). In the first bracket replace \((U\cdot\nabla)U\) by
\(\mathbb P((U\cdot\nabla)U)+\nabla p_U\) and drop \(\nabla p_U\), using
\(\langle A_\varepsilon,\nabla p_U\rangle=0\) and
\(\langle j(U),\nabla p_U\rangle=\langle A(U),\nabla p_U\rangle=0\)
(`lem:quotient-minimizer`(c) with \(\nabla p_U\in\mathcal G_3\) by
`lem:gradient-closure`). The norm bound is \eqref{eq:cp-continuity} of
`lem:quotient-stability` with \(h\to\varepsilon h\). \(\square\)

The dropped first term does not vanish identically: it equals
\(-\langle A_\varepsilon-j(U),\mathbb P((U\cdot\nabla)U)\rangle\), whose
first-order coefficient is the first variation of the minimizer paired with
the solenoidal part of the self-transport of \(U\). It *is* higher order in
the family of the manuscript's `rem:no-monotone` — there \(h\) agrees with a
harmonic gradient near \(\operatorname{supp}U\) and the competitor gradient is
supported away from \(U\), which is exactly why that construction can afford
an \(O(\varepsilon^{3/2})\) error — but that is a property of that
construction, not a general fact. In that family the surviving coefficient
reproduces \(K(U+\varepsilon h)\approx-\varepsilon\|U\|_3^3\), so the
pre-audit coefficient was the right one *there only*.

**Lemma R2 (correct direction of the Lipschitz dichotomy).** Let
\((v_\varepsilon)_{0<\varepsilon\le\varepsilon_0}\) be solenoidal fields in
\(L^3\) with (i) \(|K(v_\varepsilon)|\ge c_0\varepsilon\),
(ii) \(\mathcal Q(v_\varepsilon)\ge q_0>0\),
(iii) \(D_3(w(v_\varepsilon))\le\bar D<\infty\), for constants
\(c_0,q_0,\bar D>0\). Then:

1. If \(|K|\le Cd_1^\alpha\mathcal Q^{(1-\alpha)/3}D_3(w)\) holds on this
   family with \(\alpha>1\), then
   \(d_1(v_\varepsilon)\ge\big(c_0q_0^{(\alpha-1)/3}/(C\bar D)\big)^{1/\alpha}\varepsilon^{1/\alpha}\),
   with \(1/\alpha<1\); in particular \(q\) is **not** Lipschitz along the
   family.
2. Conversely, if \(v_\varepsilon=U+\varepsilon h\) and
   \(\|q(U+z)\|_3\le C(U)\|z\|_3\), then no bound with \(\alpha>1\) holds on
   the family, and \(\alpha=1\) is sharp.
3. Under only the audited rate \(d_1(v_\varepsilon)=O(\varepsilon^{1/2})\)
   (\eqref{eq:cp-strong}), the family refutes \(\alpha>2\) and leaves
   \(\alpha\in(1,2]\) undecided.

*Proof.* 1. \(\mathcal Q\ge q_0\) and \(\frac{1-\alpha}3<0\) give
\(\mathcal Q^{(1-\alpha)/3}\le q_0^{(1-\alpha)/3}\); combine with (i), (iii)
and solve for \(d_1^\alpha\). 2. \(d_1(v_\varepsilon)\le C(U)\|h\|_3\varepsilon\),
so \(|K|/d_1^\alpha\ge c_0\varepsilon(C(U)\|h\|_3\varepsilon)^{-\alpha}\to\infty\)
for \(\alpha>1\); \(\alpha=1\) is attained by (3.1). 3.
\(|K|/d_1^\alpha\gtrsim\varepsilon^{1-\alpha/2}\). \(\square\)

The statement that replaces the deleted box is therefore exactly the audit's:

> *Lipschitz continuity of the nonlinear projection at points of
> \(\mathcal M\), together with a nonvanishing first-order coefficient, would
> prove \(\alpha=1\) sharp; conversely any \(\alpha>1\) bound would force the
> projection to be strictly non-Lipschitz there. The audited Hölder-\(\frac12\)
> rate refutes only \(\alpha>2\) on this family.*

So, under the audited record alone, the interval \(\alpha\in(1,2]\) is
**open**: nothing here establishes a member with \(\alpha>1\), and nothing
here refutes one below \(\alpha=2\). The sharpness of \(\alpha=1\) is strictly
conditional on Lipschitz continuity of \(q\) at \(\mathcal M\), as record item
(iv) says.

This paragraph is a scoping paragraph, not a load-bearing lemma: nothing in
§4 uses it, and Proposition 3.2 is unaffected by the repair.

Three notes report on the first-order behaviour of \(K\) at \(\mathcal M\) and
are recorded as motivation only. `hf19-second-order-falsifier.md` (unaudited)
reports an exact first-order expansion with a favourable sign on a swirl
class; `hf19-difference-functional.md` and `hf19-temporal-normal-form.md`
(unaudited) touch the same point; and the audited HF20 repair sits in the
manuscript as `rem:no-monotone`, with the opposite sign and the
\(O(\varepsilon)\) rate obtained from a competitor gradient supported away
from \(U\). **None is used as a step.** Even granted in full, first-order
information about \(K\) alone does not decide sharpness: by R2 that also
requires Lipschitz continuity of \(u\mapsto q(u)\) at \(\mathcal M\), which no
audited statement supplies.

### 3.3 What \(\alpha=1\) buys: a regularity criterion in the distance to \(\mathcal M\)

**Proposition 3.3 (conditional, not a closure).** Let \(u\) be the classical
branch and suppose that for some \(\theta\in[0,1]\)
\[
 C_\sharp\,\|q(u(t))\|_3\ \le\ \theta\nu\qquad\text{for all }t\in[0,T_*).   \tag{3.2}
\]
Then \(\mathcal Q(u(t))\le\mathcal Q(u_0)\) for all \(t\), hence
\(\sup_{t<T_*}\|u(t)\|_3\le C_3\|u_0\|_3\); if \(\theta<1\) also
\((1-\theta)\nu\int_0^{T_*}D_3(w)\,dt\le\mathcal Q(u_0)\), whence
\(u\in L^3_tL^9_x\). With `thm:continuation` (ESS) this gives
\(T_*=\infty\).

*Proof.* By (Q5) and (3.1), \(\mathcal Q'=-\nu D_3(w)+K\le-(\nu-C_\sharp d_1)D_3(w)\le-(1-\theta)\nu D_3(w)\le0\).
Integrate; use (Q3) for the \(L^3\) bound and (Q6)
\(D_3(w)\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\). \(\square\)

Scope, stated bluntly. (3.2) is **not** an input-only hypothesis and
Proposition 3.3 closes nothing; it is the exact analogue of Kato's
small-\(L^3\) theorem with the reference point \(0\) replaced by the class
\(\mathcal M\). Its content relative to the audited Corollary 4 of HF18-A
(which requires \(C_*\mathcal Q^{1/3}\le\nu\), i.e. \(\|u\|_3\lesssim\nu\))
is that the smallness is demanded of the *distance* only: the criterion is
satisfied at every instant at which \(u(t)\in\mathcal M\), no matter how
large \(\|u(t)\|_3\) is, and \(\mathcal M_{\rm sol}\) contains fields of
arbitrarily large critical norm (by (Q7) Prop. 1.4 the class is the image of
*every* solenoidal \(A\in L^{3/2}\) under \(A\mapsto|A|^{-1/2}A\), and it is
invariant under both scalings). So the hypothesis class of Proposition 3.3
strictly contains the critical-smallness class. It remains a hypothesis on
the unknown trajectory, and by the packet's rule it is a hidden-smallness
condition if presented as a mechanism; it is presented here only as the
exact strength of the \(\alpha=1\) bound.

---

## 4. The time-integrated question

### 4.1 The master identity: boundary term plus fluxes

Integrating (2.1) from \(0\) to \(\tau<\min\{H,T_*\}\) and solving for
\(\int K\):

**Theorem 4.1 (exact spacetime identity for the transport term).**
For every \(0<\tau<T_*\),
\[
 \boxed{\ \int_0^\tau K\,dt
 \ =\ \underbrace{d_2(0)-d_2(\tau)}_{\text{boundary}}
 \ +\ \nu\int_0^\tau D_3(w)\,dt
 \ -\ \nu\int_0^\tau D_3(u)\,dt
 \ +\ \int_0^\tau P_3\,dt\ }                                          \tag{4.1}
\]
with \(d_2=F(u)-\mathcal Q(u)\ge0\), \(d_2(0)\le\frac13\|u_0\|_3^3\) an input
quantity, and \(D_3(u)\ge0\). In particular
\[
 \int_0^\tau K\,dt\ \le\ \nu\int_0^\tau D_3(w)\,dt
 \;+\;\Big[\int_0^\tau P_3\,dt-\nu\int_0^\tau D_3(u)\,dt\Big]\;+\;\tfrac13\|u_0\|_3^3 .
                                                                       \tag{4.2}
\]

Every term is displayed, every hypothesis is (Q5), (P2), (Q6), and no
regularity of the minimizer is used. **Two of the four terms on the right of
(4.1) are signed** — \(-d_2(\tau)\le0\) and \(-\nu\int D_3(u)\le0\) — which is
the sign structure the pointwise \(K(t)\) lacks: no sign for \(K(t)\) is
claimed or established anywhere in this note. (That the pointwise integrand
straddles zero — \(\hat w\cdot S(u)\hat w\) with \(\operatorname{tr}S=0\), and
\(\Pi_{u,A}\) a Riesz image — is reported in HF18-B §3.3(d); per the audit's
dependency correction that observation is recorded here as motivation only and
is a premise of nothing below.)

The scaling of (4.1) is \((a^3,\lambda^0)\) term by term
(\(\int K\,dt\sim(a^4\cdot a^{-1},\lambda^2\lambda^{-2})\), \(d_2\sim(a^3,\lambda^0)\),
\(\nu\int D_3dt\sim(a\cdot a^3a^{-1},\lambda^0)\)) ✓.

### 4.2 What (4.1) does and does not deliver

**Corollary 4.2 (dictionary: HIGH-PRESSURE transfers to the quotient gap with
an explicit constant).**
Assume `hyp:absorption` with constant \(\theta'\in[0,1)\) and witness
\(A(\nu,u_0,H)\) (implied by `hyp:highpressure` via `lem:absorption-split`).
Then for every \(0<\tau<\min\{H,T_*\}\),
\[
 \int_0^\tau K\,dt\ \le\ \nu\int_0^\tau D_{\mathcal Q}(u)\,dt
 \;+\;A(\nu,u_0,H)+\tfrac13\|u_0\|_3^3 ,                                \tag{4.3}
\]
i.e. the first gap of this lane's packet holds with \(\theta=1\), \(M=0\)
and \(A_{\rm input}=A+\frac13\|u_0\|_3^3\); and with
\(|K_{\rm low}|\le M_L\mathcal Q\) (Q5) the same holds for \(K_L\) for every
\(L\), i.e. `hyp:highstrain` holds with \(\theta=1\).

*Proof.* Insert
\(\int P_3\le\theta'\nu\int D_3(u)+A\le\nu\int D_3(u)+A\) into (4.2) and use
\(D_{\mathcal Q}=D_3(w)\). For the last claim add
\(M_L\int_0^\tau\mathcal Q\,dt\), which is input-bounded by Lemma 4.3 below,
itself `prop:scaling`(iii) plus time-Hölder. \(\square\)

**Scope, as the audit requires it to be stated: this is a dictionary, not a
new implication.** The *implication* "`hyp:absorption` \(\Rightarrow\)
`hyp:highstrain`" is already available in the manuscript by composition:
`cor:absorption-consequence`(ii) gives `hyp:critical`, `thm:conditional` gives
\(T_*=\infty\), and the converse direction of `rem:highstrain-scope` (take
\(L=0\), \(\theta=0\), \(A_{\rm input}=\int_0^H|K_0|\)) then gives
`hyp:highstrain`. What Corollary 4.2 adds is **only** the direct, explicit and
quantitative transfer \(A_{\rm input}=A+\frac13\|u_0\|_3^3\), which does not
route through the Clay conclusion. The pre-audit abstract wording ("asserts
one open hypothesis implies another") would have misled a reader into thinking
the implication itself is new; it is not, and it is not presented as such
anywhere in this note.

So Corollary 4.2 is a *route-level* fact, not progress: it says the quotient
route is not harder than the pressure route, with an explicit, non-circular
transfer constant \(\frac13\|u_0\|_3^3\), and it identifies exactly which
pieces differ (the two dissipations and the boundary distance). The converse
implication also holds — from the \(\theta=1\) quotient gap one gets
\(\sup\mathcal Q\le\mathcal Q(0)+A_{\rm input}\) by `prop:quotient-conditional`,
hence \(d_2(\tau)\le F(u(\tau))\le C_3^3(\|u_0\|_3^3+3A_{\rm input})\) is
input-bounded, and (4.1) returns
\(\int P_3-\nu\int D_3(u)\le A_{\rm input}+d_2(\tau)\) — but that converse is
uninformative, since both hypotheses are already equivalent to continuation
at their quantifiers (`rem:highstrain-scope`). The content of (4.1) is the
explicit dictionary, not the equivalence.

**The honest reading.** (4.1) *is* an identity of the shape the lane asked
for — \(\int K=\) boundary terms \(+\) something signed \(+\) a remainder —
but the remainder is precisely the pressure-route flux \(\int P_3-\nu\int D_3(u)\),
i.e. HIGH-PRESSURE. The crossing structure of \(\mathcal M\) therefore
supplies the boundary term \(-d_2(\tau)\le0\) and nothing else. The
mixed-pressure form \(K=\int q\cdot\nabla\Pi_{u,A}\) with
\(\operatorname{div}A=0\) was the suggested source of a signed spacetime
identity; §4.6 records what it does give, which is a gauge freedom, not a
sign.

### 4.3 The input-only spacetime bound for the distance: an existing manuscript result

**Novelty correction (audit defect B3).** The pre-audit note displayed the
bound of this subsection as its own result (R3). It is correct but **not
new**: it is `prop:scaling`(iii) \eqref{eq:L4L3} of the manuscript plus one
time-Hölder step, with the same \(E_0,\nu,\tau\) weights. The novelty claim is
withdrawn. The manuscript proposition is cited in its place, and the audit's
Lemma R4 — reproduced verbatim below — supplies both the cubic form used
downstream and a \(\tau\)-uniform quartic form that is strictly better for the
crossing statement of §4.4. The consequences are favourable, not adverse:
Corollary 4.4 below needs **no new lemma at all**, and Theorem 4.5 item 1 is
upgraded to a \(\tau\)-uniform bound.

**Lemma 4.3 (audit R4; `prop:scaling`(iii) and three consequences).** For the
classical branch and every \(\tau<T_*\):

1. \(\displaystyle\int_0^\tau\|u\|_3^4dt\le\frac{3C_S^2\|u_0\|_2^4}{2\nu}=\frac{3C_S^2E_0^2}{2\nu}\)
   — this is `prop:scaling`(iii), \eqref{eq:L4L3}, **already in the
   manuscript**, and it is \(\tau\)-uniform;
2. hence, by time-Hölder \((4,4/3)\),
   \[
    \int_0^\tau\|u\|_3^3dt\le\tau^{1/4}\Big(\tfrac{3C_S^2E_0^2}{2\nu}\Big)^{3/4},
    \qquad
    \int_0^\tau d_1^3\,dt\le8\!\int_0^\tau\|u\|_3^3dt=:A_1(\nu,E_0,\tau) ,
    \tag{4.4}
   \]
   which is the pre-audit (4.4) with the same
   \(E_0^{3/2}\nu^{-3/4}\tau^{1/4}\) weights;
3. \[
    \int_0^\tau d_1^4dt\le16\!\int_0^\tau\|u\|_3^4dt\le\frac{24C_S^2E_0^2}{\nu}=:A_1^{(4)}(\nu,E_0) ,
    \tag{4.4b}
   \]
   \(\tau\)-uniform;
4. **\(\tau\)-uniform crossing bound.**
   \(\displaystyle|\mathcal B_\tau|\le(C_\sharp/\nu)^4\!\int_0^\tau d_1^4dt\le24\,C_S^2\,C_\sharp^4\,E_0^2\,\nu^{-5}\),
   uniformly in \(\tau<T_*\) — in particular the total measure of the set of
   times at which \(\mathcal Q\) can increase is finite up to the putative
   blow-up time, with no \(\tau^{1/4}\) growth. (\(\mathcal B_\tau\) is
   defined in Theorem 4.5; this item is restated there as item 1.)

*Proof.* 1 is `prop:scaling`(iii). 2 is Hölder in time. 3 uses
\(d_1\le2\|u\|_3\) (Q3) and \(16\cdot\frac32=24\). 4 is Chebyshev at exponent
\(4\): \(|\mathcal B_\tau|(\nu/C_\sharp)^4\le\int_{\mathcal B_\tau}d_1^4\le\int_0^\tau d_1^4\).
\(\square\)

Here \(C_S\) is the manuscript's Sobolev constant (`def:sobolev-constant`);
the note's §0 constant \(S\) is the same Sobolev constant in its vector-field
normalisation, and nothing below uses either value. Consequently
\(\int_0^\tau\mathcal Q\,dt\le\frac13\int_0^\tau\|u\|_3^3dt\) and
\(\int_0^\tau d_2\,dt\) are input-bounded as well (\(\mathcal Q\le F\),
\(d_2\le F\)).

Scaling check of item 4: \(|\mathcal B_\tau|\sim dt\sim(a^{-1},\lambda^{-2})\)
and \(E_0^2\nu^{-5}\sim(a^{4-5},\lambda^{-2})=(a^{-1},\lambda^{-2})\) ✓.
Scaling check of item 2: \(\int\|u\|_3^3dt\sim(a^2,\lambda^{-2})\) and
\(E_0^{3/2}\nu^{-3/4}\tau^{1/4}\sim(a^{3-3/4-1/4},\lambda^{-3/2-1/2})=(a^2,\lambda^{-2})\) ✓.
The bounds are energy-only and finite for every datum and horizon, and they
are *supercritical*: the pair \((r,q)=(4,3)\) has \(2/4+3/3=\frac32>1\) and the
pair \((3,3)\) has \(\frac23+1=\frac53>1\), so neither controls
\(\sup_t\|u\|_3\) — this is exactly `rem:mismatch` of the manuscript, and it
is why no forbidden inference is made here.

**Corollary 4.4 (the Gronwall term and the frequency split in the frozen gap
are removable).** Let \(M\ge0\), \(L\in\mathbb Z\), \(H<\infty\). Then for
\(\tau<\min\{H,T_*\}\),
\[
 M\!\int_0^\tau\!\mathcal Q\,dt\le\tfrac{M}{3}H^{1/4}\Big(\tfrac{3C_S^2E_0^2}{2\nu}\Big)^{3/4},
 \qquad
 \Big|\int_0^\tau\! K_{\rm low}\,dt\Big|\le\tfrac{M_L}{3}H^{1/4}\Big(\tfrac{3C_S^2E_0^2}{2\nu}\Big)^{3/4},
\]
both input-only. Hence the packet's first gap
"\(\int_0^\tau K\le\theta\nu\int_0^\tau D_3(w)+M\int_0^\tau\mathcal Q+A_{\rm input}\)"
is equivalent, with an input-only change of \(A_{\rm input}\), to the
\(M\)-free statement; and `hyp:highstrain` (stated for \(K_L\) with a
datum-selected \(L\)) is equivalent, with an input-only change of
\(A_{\rm input}\), to the same statement for the full \(K\) with no
Littlewood–Paley split at all.

*Proof.* Lemma 4.3 item 2 with \(\tau\le H\) and \(\mathcal Q\le F\); for the
second display, \(|K_{\rm low}|\le M_L\mathcal Q\) (Q5),
\(M_L=3(1+C_3)C_B2^{5L/2}\|u_0\|_2\), which is input-only in
\((\nu,u_0,H,L)\) — exactly the dependence `hyp:highstrain` permits. Both
directions of both equivalences follow by adding or subtracting these input
quantities, and the fixed universal \(\theta\) is preserved in both
directions. \(\square\)

This is a simplification of the frozen gap's *statement*, not of its
content: it says the low-frequency work of the quotient route is free
(unlike the pressure route, where `prop:lowpressure` is a genuine lemma),
and it removes the datum-dependent cutoff \(L\) from `hyp:highstrain`. After
the audit it costs nothing at all: `prop:scaling`(iii) already sits in the
manuscript and supplies the required input bound directly, so no new lemma is
needed. It is offered to the controller as an integration candidate; the
audit of this note confirms it and records the corresponding manuscript
remark as its own recommendation. Nothing here is promoted, and this note
touches no file but itself.

### 4.4 The crossing statement: \(\mathcal Q\) can grow only on a small set of times

**Theorem 4.5 (crossing/measure bound; item 1 upgraded and item 3 repaired by
the audit).** Let \(u\) be the classical branch,
\(C_\sharp=\frac32C_9S\) as in (3.1), and for \(\tau<T_*\) put
\[
 \mathcal B_\tau:=\{t\in(0,\tau):\ C_\sharp\,\|q(u(t))\|_3>\nu\},\qquad
 \mathcal G_\tau:=(0,\tau)\setminus\mathcal B_\tau .
\]
Then:
1. \(\mathcal B_\tau\) is open in \((0,\tau)\) (\(t\mapsto\|q(t)\|_3\) is
   continuous, Remark 2.2) and, in the \(\tau\)-uniform form supplied by the
   audit (Lemma 4.3 item 4 = R4.4),
   \[
    \boxed{\ |\mathcal B_\tau|\ \le\ \Big(\frac{C_\sharp}{\nu}\Big)^{4}\!\!\int_0^\tau\! d_1^4\,dt
    \ \le\ 24\,C_S^2\,C_\sharp^4\,E_0^2\,\nu^{-5}\qquad\text{uniformly in }\tau<T_* ,\ }        \tag{4.5}
   \]
   an input-only bound with no growth in \(\tau\);
2. \(\mathcal Q'(t)\le-\big(\nu-C_\sharp d_1(t)\big)D_3(w(t))\le0\) for every
   \(t\in\mathcal G_\tau\): the quotient is nonincreasing off \(\mathcal B_\tau\);
3. \(\displaystyle\mathcal Q(\tau)\le\mathcal Q(0)+C_\sharp\int_{\mathcal B_\tau}d_1\,D_3(w)\,dt\);
   for the good set, see Lemma R3 immediately below.

*Proof.* 1 is Chebyshev at exponent \(4\) together with Lemma 4.3 items 3–4.
2 is (Q5) with (3.1). 3: integrate \(\mathcal Q'+\nu D_3(w)=K\le C_\sharp d_1D_3(w)\)
over \((0,\tau)\), drop the nonpositive contribution of \(\mathcal G_\tau\) on
the right, and use \(D_3(w)\ge0\). \(\square\)

**What changed, and why (audit defects B2 and B3).** The pre-audit item 1 read
\(|\mathcal B_\tau|\le(C_\sharp/\nu)^3\int_0^\tau d_1^3dt\le
8\cdot2^{-3/4}S^{3/2}C_\sharp^3E_0^{3/2}\nu^{-15/4}\tau^{1/4}\). That bound is
correct but is **superseded**: it grows like \(\tau^{1/4}\), whereas (4.5) is
uniform in \(\tau\) and is therefore the only form that survives the limit
\(\tau\uparrow T_*\). (4.5) is the crossing statement of record. The pre-audit
item 3 carried a second display,
\(\nu\int_{\mathcal G_\tau}D_3(w)\,dt\le\mathcal Q(0)+C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)\,dt\),
which **does not follow from its proof and is not derivable from the
ingredients**: on the good set the deficit \(\nu D_3(w)-K\) may be arbitrarily
small relative to \(\nu D_3(w)\). It is deleted and replaced by the audit's
Lemma R3, reproduced verbatim.

**Lemma R3 (repairs the good-set display).** With the notation of Theorem 4.5,
for \(\tau<T_*\):

1. \(\nu\int_{\mathcal B_\tau}D_3(w)\,dt\le\mathcal Q(0)+C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)\,dt\)
   (this is what the pre-audit proof yields; it is vacuous, since
   \(C_\sharp d_1>\nu\) on \(\mathcal B_\tau\));
2. \(\int_{\mathcal G_\tau}\big(\nu D_3(w)-K\big)dt\le\mathcal Q(0)+C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)\,dt\)
   — a bound on the good-set *deficit*, not on \(\int_{\mathcal G_\tau}D_3(w)\);
3. for fixed \(\delta\in(0,1]\), with
   \(\mathcal G^\delta_\tau:=\{t<\tau:C_\sharp d_1(t)\le(1-\delta)\nu\}\),
   \[
    \delta\nu\int_{\mathcal G^\delta_\tau}D_3(w)\,dt\le\mathcal Q(0)+C_\sharp\int_{(\mathcal G^\delta_\tau)^c}d_1D_3(w)\,dt ,
   \]
   with \(|(\mathcal G^\delta_\tau)^c|\le(1-\delta)^{-3}(C_\sharp/\nu)^3\int_0^\tau d_1^3dt\).

*Proof.* \(\mathcal Q(0)-\mathcal Q(\tau)=\int_0^\tau(\nu D_3(w)-K)\).
1. Bound \(\int_{\mathcal G_\tau}K\le\nu\int_{\mathcal G_\tau}D_3(w)\) (valid
since \(C_\sharp d_1\le\nu\) there) and
\(\int_{\mathcal B_\tau}K\le C_\sharp\int_{\mathcal B_\tau}d_1D_3(w)\), then
cancel \(\nu\int_{\mathcal G_\tau}D_3(w)\) and use \(\mathcal Q(\tau)\ge0\).
2. Split the identity and use \(\nu D_3(w)-K\ge-(C_\sharp d_1-\nu)D_3(w)\) on
\(\mathcal B_\tau\) and \(\mathcal Q(\tau)\ge0\).
3. On \(\mathcal G^\delta_\tau\), \(K\le C_\sharp d_1D_3(w)\le(1-\delta)\nu D_3(w)\),
so \(\nu D_3(w)-K\ge\delta\nu D_3(w)\); insert into 2 with
\(\mathcal G^\delta_\tau\) in place of \(\mathcal G_\tau\); the measure bound
is Chebyshev. \(\square\)

**Obstruction O3 (no input bound on the good set).** No bound of the form
\(\nu\int_{\mathcal G_\tau}D_3(w)\,dt\le\text{input}\) is available, and this
is not a defect of technique: the good set only guarantees
\(K\le\nu D_3(w)\), and a trajectory saturating (3.1) on \(\mathcal G_\tau\)
has \(\nu D_3(w)-K\approx0\) there while \(\int_{\mathcal G_\tau}D_3(w)\) is
unconstrained. This is a second obstruction of the same type as O2, localised
on the *good* set rather than the bad one. Item 3 of Lemma R3 is the only
good-set statement that survives, and whether any input-only bound for
\(\int_{\mathcal G^\delta_\tau}D_3(w)\,dt\) exists for some fixed
\(\delta\in(0,1]\) is **open**.

Item 1 is a genuine crossing-type statement of the kind the lane asked for:
*the set of times at which the quotient can increase at all has measure
bounded by input data, uniformly up to the putative blow-up time.* Its
weaknesses remain explicit: the bound is not small for large data, it is a
statement about a *measure* only, and — decisively — it says nothing about how
much \(D_3(w)\) sits on \(\mathcal B_\tau\).

**Obstruction O1 (the Hölder split is circular; corrected per audit items O1a
and O1b).** Suppose one tries to close item 3 using only (4.4) and (3.1), i.e.
to bound \(\int_{\mathcal B_\tau}d_1D_3(w)\) by Hölder in time against
\(\int d_1^3\le A_1\). For any \(\alpha\in(0,3)\) and the corresponding
member \(|K|\le C\,d_1^\alpha\mathcal Q^{(1-\alpha)/3}D_3(w)\) of the lattice
of Proposition 3.2, Hölder gives
\[
 \int_0^\tau d_1^\alpha\,\mathcal Q^{(1-\alpha)/3}D_3(w)\,dt\ \le\
 \Big(\sup_{t<\tau}\mathcal Q\Big)^{(1-\alpha)/3}
 \Big(\int_0^\tau d_1^3dt\Big)^{\alpha/3}
 \Big(\int_0^\tau D_3(w)^{r}dt\Big)^{1/r},\qquad r=\frac{3}{3-\alpha}>1 ,
\]
where the factor \(\mathcal Q^{(1-\alpha)/3}\) — **silently dropped in the
pre-audit version of this display (audit item O1b)** — carries a *positive*
power for \(\alpha\in(0,1)\). So the split additionally requires
\(\sup_{t<\tau}\mathcal Q\), which is the conclusion itself; restoring the
factor makes O1 *stronger*, not weaker. Independently, the split requires an a
priori bound on \(\int_0^\tau D_3(w)^rdt\) for some \(r>1\). But by (Q6)
\(D_3(w)\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\), so by Hölder in time on the finite
interval,
\[
 \int_0^\tau\|u\|_9^3dt\ \le\ \tau^{1-1/r}\Big(\int_0^\tau\|u\|_9^{3r}dt\Big)^{1/r}
 \ \le\ \tau^{1-1/r}\,\Big(\tfrac{9S^2C_9^3}{8}\Big)^{1}\Big(\int_0^\tau D_3(w)^rdt\Big)^{1/r},
\]
where the exponent on the constant is \(1\), not the \(3\) displayed in the
pre-audit version (**audit item O1a**): from
\(\|u\|_9^{3r}\le(\frac{9S^2C_9^3}{8})^rD_3(w)^r\) the \(1/r\)-th root removes
the exponent. Either way any such bound puts \(u\) in \(L^3_tL^9_x\), which is
the Ladyzhenskaya–Prodi–Serrin class \(2/s+3/r=1\) and already implies the
continuation that the gap is meant to produce (it is exactly the conclusion
extracted in HF18-A §4 item 3 and in `prop:quotient-conditional`). **The route
closes only through a hypothesis at least as strong as its conclusion: it is
circular, for every \(\alpha\in(0,3)\).** \(\square\)

Three scope statements, all from the audit. (a) "At least as strong", not
"strictly stronger" as the pre-audit version had it: what is proved is that
the hypothesis *implies* the conclusion, not that the implication is strict.
(b) The lattice members with \(\alpha\in(1,3)\) invoked here are **not**
established anywhere — by Proposition 3.2 they require \(b<0\) — so O1 covers
them only hypothetically. This does not weaken O1's use, which is to rule out
a proof strategy, not to assert those members exist. (c) The circularity is
not an artefact of the cubic distance bound: with the \(\tau\)-uniform quartic
bound (4.4b) the same split runs at \(r=4/(4-\alpha)\) — \(r=4/3\) for
\(\alpha=1\) — and reaches the same LPS conclusion.

### 4.5 Obstruction O2: the two available facts are provably insufficient

The pair of facts established above,
\[
 \text{(F-a)}\quad |K(t)|\le c(t)\,D_3(w(t))\ \ \text{with}\ \ c=C_\sharp d_1,
 \qquad
 \text{(F-b)}\quad \int_0^\tau c^3\,dt\le C_\sharp^3A_1<\infty ,
\]
does not imply the first gap, and this is not a failure of technique: the
implication is false at the level of the two functions \(c\ge0\), \(D\ge0\).

**Proposition 4.6 (explicit family).** Let \(\tau,\nu,\theta,A_1,A>0\).
There exist \(c\in L^3(0,\tau)\) and \(D\in L^1(0,\tau)\), both nonnegative,
with \(\int_0^\tau c^3dt\le A_1\), such that
\(\int_0^\tau cD\,dt>\theta\nu\int_0^\tau D\,dt+A\).

*Proof.* Fix \(R:=\max\{2\theta\nu,\ (A_1/\tau)^{1/3}\}\), so that
\(R>\theta\nu\) and \(R^{-3}A_1\le\tau\); let \(\mathcal E\subset(0,\tau)\)
have measure \(|\mathcal E|=A_1R^{-3}\) and put \(c=R\mathbf 1_{\mathcal E}\),
\(D=N\mathbf 1_{\mathcal E}\) with \(N>0\) free (the symbol \(S\) is reserved
for the Sobolev constant). Then \(\int c^3=A_1\),
\(\int cD=NRA_1R^{-3}=NA_1R^{-2}\), \(\theta\nu\int D=\theta\nu NA_1R^{-3}\),
and
\(\int cD-\theta\nu\int D=NA_1R^{-3}(R-\theta\nu)\to\infty\) as \(N\to\infty\).
Choose \(N\) so that the left side exceeds \(A\). \(\square\)

Computed instance: \(\tau=\nu=\theta=1\), \(A_1=8\), \(R=2\), \(|\mathcal E|=1\),
\(c\equiv2\), \(D\equiv N\): \(\int cD=2N\), \(\int D=N\), difference
\(N\to\infty\).

**O2 also survives the strengthened (F-b).** After Lemma 4.3 the distance
obeys the \(\tau\)-uniform \(\int_0^\tau c^4dt\le C_\sharp^4A_1^{(4)}\) as
well. The construction adapts verbatim: with
\(R=\max\{2\theta\nu,(A_1/\tau)^{1/4}\}\) and \(|\mathcal E|=A_1R^{-4}\) one
gets \(\int c^4=A_1\) and the same divergence. So upgrading the distance bound
from \(L^3_t\) to \(L^4_t\) does not repair the implication; the missing
ingredient is a coupling, not a better integrability exponent for \(c\).

**Scope of O2.** This does *not* say the first gap is false; it says that
any proof of it must use information beyond (F-a)+(F-b) — some coupling
between where the trajectory is far from \(\mathcal M\) and where the
dissipation lives. The exact missing statement, in the sharpest form the
present note can pose it, is:
\[
 \boxed{\ \text{(G)}\qquad \int_0^\tau\|q(u(t))\|_3\,D_3(w(t))\,dt\ \le\ A_{\rm input}(\nu,u_0,H)
 \qquad\text{uniformly for }\tau<\min\{H,T_*\}.\ }
\]
By (3.1), (G) implies the first gap with \(\theta=0\); by Corollary 4.4 no
\(M\int\mathcal Q\) term and no cutoff \(L\) are needed. (G) has exactly the
scaling of \(\mathcal Q\), \((a^3,\lambda^0)\), so it is scaling-consistent
with an input-only right side (e.g. any product
\(E_0^{x}\nu^{y}H^{z}2^{Lv}\) with \(2x+y-z=3\), \(-x-2z+v=0\)). It is a
joint spacetime statement about the pair (distance, dissipation) and is
**not** implied by (4.4), by (4.4b), by Theorem 4.5, or by any member of the
lattice of Proposition 3.2, per O2.

### 4.6 What the mixed-pressure form contributes: a gauge, not a sign

The lane asked specifically whether
\(K=\int q\cdot\nabla\Pi_{u,A}\) with \(\operatorname{div}A=0\) yields a
signed spacetime identity. Three observations, the first unconditional:

1. **No new spacetime structure at the \(L^3\) level.** \(\Pi_{u,A}\) is
   quadratic in \((u,A)\) and \(q\) is the gradient part of \(w\); the
   pairing is \(-\langle\operatorname{div}w,\Pi_{u,A}\rangle\) ((Q7) (3.2)),
   which is a fixed-time identity with no time derivative in it. Time
   integration of an identity that contains no boundary term produces no
   boundary term; the only source of a boundary term available in the
   audited record is a functional whose derivative reproduces \(K\), and
   §2 shows the unique such functional built from the audited balances is
   \(d_2\), giving exactly (4.1). This is consistent with the route-level
   report of the unaudited `hf19-temporal-normal-form.md` (that the content
   of any temporal normal form sits wholly in its corrector); here the
   corrector is \(d_2\) and its content is displayed.
2. **A gauge freedom (conditional on (H1),(H2)).** By (Q7) Remark 1.3, the
   exact integrals \(\int|w|^\alpha\sigma\,dx=0\) hold **unconditionally** for
   every \(\alpha\in[2,5]\). Hence, whenever the pairing form
   \(K_L=\int\sigma\Pi_L\) is available — i.e. under (H1) and (H2), both
   OPEN — one may subtract any \(c|w|^\alpha\):
   \[
    K_L=\int\sigma\big(\Pi_L-c|w|^\alpha\big)\,dx,\qquad
    |K_L|\le\Big(\tfrac12D_3(w)\Big)^{1/2}
    \inf_{c\in\mathbb R,\ 2\le\alpha\le5}\Big(\int|w|^{-1}\big(\Pi_L-c|w|^\alpha\big)^2dx\Big)^{1/2}.
   \]
   This strictly improves HF18-B (3.8), whose right factor is the
   \(c=0\) case, and it removes the local obstruction of that estimate at
   codimension-one zeros of \(w\) whenever \(\Pi_L\) is comparable to
   \(c|w|^\alpha\) there (each subtracted profile has
   \(\int|w|^{-1}|w|^{2\alpha}<\infty\) for \(\alpha\ge2\) by \(w\in L^3\cap L^9\)).
   It does not make the right factor finite in general, and it supplies no
   sign; the finiteness of \(\int|w|^{-1}\Pi_L^2\) remains OPEN as recorded.
3. **No sign is created by \(\operatorname{div}A=0\).** \(\operatorname{div}A=0\)
   was already used twice in the audited record — to produce the mixed
   pressure (F7) and to give \(\int A\cdot((q\cdot\nabla)u)=0\) (Q7) — and
   both uses are sign-free identities. The single sign that the audited
   structure does provide, \(\int|w|\sigma^2\le\frac12D_3(w)\), is a
   *magnitude* statement about \(\sigma\) and is already used above.

---

## 5. Self-check against the packet's falsifiers

| Falsifier | Where it could have entered | Disposition |
|---|---|---|
| A bound that uses the norm it must control | (3.1) contains \(\|q\|_3\le2\|u\|_3\); (3.2) | (3.1) is an *estimate*, not a closure; Prop. 3.3 is labelled a conditional criterion whose hypothesis is not input-only, and it is not used in §4 |
| Scaling-inconsistent absorption | (1.1)–(1.3), (3.1), (4.1)–(4.5), (G) | every display carries its \((a,\lambda)\) weights; §1.4 table; the only non-critical distance, \(d_3\), is flagged and never used in a bound for \(K\); the audit recomputed all of them |
| Hidden smallness | Prop. 3.3 | stated as a hypothesis on the unknown trajectory, with the explicit comparison to Kato/HF18-A Corollary 4 |
| Differentiating the merely-\(L^3\) minimizer | §2, §4.1 | \(d_2\) is evolved by subtracting two audited *integrated* balances; Remark 2.2 records that \(d_1\) is only \(\frac12\)-Hölder in \(t\) and is never differentiated |
| Instantaneous fact promoted to a time-integrated one | (3.1) \(\to\) Theorem 4.5 | only through integration of the audited \(C^1\) identity (Q5); the promotion to absorption is explicitly refuted by O1, O2 and O3 |
| \(p\)-Laplace / nonlinear-Hodge theorem outside its hypotheses | §1.1 | \(\mathcal M\) is used only through (Q1) and, in §3.3's scope sentence alone, (Q7) Prop. 1.4; no regularity theorem for \(p\)-harmonic objects is invoked, and (H1), (H2), (W) remain OPEN and are used only in §4.6 where marked |
| Forced/periodic/hyperdissipative/Euler substitute | throughout | all statements concern the unforced classical branch on \(\mathbb R^3\) of `prop:localtheory`; \(\nu>0\) fixed and arbitrary |
| Forbidden: size bounds in \(\mathcal Q,D_3\) | §3.2 | the lattice is displayed and the audited \(\alpha=0\) endpoint is recovered as a special case; no monomial is claimed to close, no member with \(\alpha>1\) is claimed to exist, and after the audit \(\alpha\in(1,2]\) is recorded as open |
| Forbidden: energy control implies critical control | (4.4), (4.4b) | both are `prop:scaling`(iii) \eqref{eq:L4L3} plus time-Hölder; the pairs \((4,3)\) and \((3,3)\) are supercritical (`rem:mismatch`), so no \(\sup_t\|u\|_3\) is claimed or implied |
| Forbidden: another equivalent identity discharges the gap | (4.1) | stated as a dictionary; §4.2 records that its remainder *is* HIGH-PRESSURE, and that the implication itself is already available in the manuscript by composition |
| A displayed claim that does not follow from its proof | pre-audit §3.2 box; pre-audit Theorem 4.5 item 3, second display | both found by the audit, both **deleted** rather than patched, and replaced by the audit's Lemmas R1, R2 (§3.2) and R3 (§4.4) |
| An existing result of the record re-derived and claimed as new | pre-audit Proposition 4.3 | novelty claim **withdrawn**; `prop:scaling`(iii) \eqref{eq:L4L3} is cited in its place (§4.3), and Proposition 3.1 is recorded as a strengthening of an audited HF18-A line rather than as a new theorem |

## 6. Frontier record

**AUDIT:** `hf21-review-crossing-sign-structure.md`, **VERDICT REPAIR**,
repairs applied by the controller on 2026-09-06. First bad bridge: §3.2, the
first-order expansion at \(\mathcal M\) (an \(O(\varepsilon)\) term omitted)
and its boxed conditional (logically inverted) — both deleted and replaced by
R1 and R2. Second defect: Theorem 4.5 item 3's good-set display — deleted and
replaced by R3, with the residual impossibility recorded as O3. Third defect:
the former Proposition 4.3 — correct but not new, novelty withdrawn,
`prop:scaling`(iii) \eqref{eq:L4L3} cited in its place with R4. One result
strengthened: Theorem 4.5 item 1 is now \(\tau\)-uniform. Corrections O1a,
O1b applied; Corollary 4.2 restated as a dictionary; HF18-B removed from the
premise list except §3.3's scope sentence and §4.6.

**MODE / RESULT:** DISCOVER, audited REPAIR with repairs applied. Result: the
time-integrated transport term has exactly one signed structure that the
pointwise term lacks — the boundary term \(-d_2(\tau)\le0\) of the exact
identity (4.1), together with \(-\nu\int D_3(u)\le0\) — and this converts the
gap into the pressure-route gap and no further. A crossing-type theorem is
proved (Theorem 4.5: \(\mathcal Q\) grows only on a set of times whose measure
is bounded by input data, and after the audit that bound is *uniform in*
\(\tau\)), and three obstructions are proved to its upgrade: O1 (circularity
of the Hölder split, for every \(\alpha\in(0,3)\)), O2 (an explicit family
showing (F-a)+(F-b) insufficient, in both its \(L^3\) and \(L^4\) forms), and
O3 (no input-only bound on \(\int_{\mathcal G_\tau}D_3(w)\)). Two new
unconditional inequalities are proved — (1.1)–(1.3) (distance comparisons) and
(3.1) (\(\alpha=1\), itself a strengthening of an audited HF18-A line rather
than a new theorem) — together with Corollary 4.4, which removes the Gronwall
term and the frequency cutoff from the frozen gap statement at no cost beyond
`prop:scaling`(iii). The input-only \(L^3_t\) distance bound of §4.3 is **not
new** and is no longer claimed as such.

**CLAIM AND SCOPE:** For the classical branch of an arbitrary
divergence-free Schwartz datum on \(\mathbb R^3\) with arbitrary \(\nu>0\),
on every \([0,\tau]\subset[0,T_*)\): Lemma 1.1, Propositions 1.2, 1.3, 1.4
(comparisons of \(d_1,d_2,d_3,d_4\) and their scalings), Proposition 2.1
(exact distance balance), Proposition 3.1 (\(|K|\le C_\sharp\|q\|_3D_3(w)\),
\(C_\sharp=\frac32C_9S\)), Proposition 3.2 (monomial lattice), Lemmas R1 and
R2 (§3.2: the exact expansion at \(\mathcal M\), and the Lipschitz dichotomy
in its correct direction), Proposition 3.3 (conditional criterion; hypothesis
not input-only), Theorem 4.1 (identity (4.1)), Corollary 4.2 (dictionary:
`hyp:absorption` transfers to the quotient gap with \(\theta=1\) and explicit
constant \(\frac13\|u_0\|_3^3\); the implication itself is not new),
Lemma 4.3 (= `prop:scaling`(iii) and R4) and Corollary 4.4 (removability of
\(M\int\mathcal Q\) and of the Littlewood–Paley split from `hyp:highstrain`),
Theorem 4.5 with the \(\tau\)-uniform crossing bound (4.5) and Lemma R3,
Obstructions O1, O2 (with Proposition 4.6) and O3. Everything rests on
`prop:pressure`, `prop:energy`, `prop:scaling`, `prop:quotient-evolution`,
`lem:quotient-minimizer`, `lem:quotient-coercive`, `lem:quotient-stability`,
`lem:quotient-transport`, `lem:leray`, `lem:gradient-closure`,
`lem:cubic-pointwise`, `lem:cubic-frechet` [all DI, manuscript] and audited
HF18-A (A1)–(A6) [DI]. HF18-B is used **only** in §3.3's scope sentence
(Prop. 1.4) and in §4.6; §4.6 item 2 is additionally conditional on the OPEN
(H1) and (H2).

**EVIDENCE:** Bregman-divergence integration of the audited pointwise cubic
identity for Proposition 1.2; the audited \(L^3\) monotonicity plus the
Leray duality \(\langle\mathbb Pf,g\rangle=\langle f,\mathbb Pg\rangle\) and
\((I-\mathbb P)f=0\) for solenoidal \(f\in L^{3/2}\) for Proposition 1.3;
Hölder \((4/3,4)\) on the audited cubic dissipation for Proposition 1.4;
subtraction of the two audited integrated balances for Proposition 2.1,
cross-checked by the independent route of Remark 2.3 through the identity
\(K=-\langle j(w)-j(u),(u\cdot\nabla)u\rangle\); the audited chain rule
\(\nabla A=D\Phi(V)\nabla V\), Hölder \((3,6,2)\), Leray on \(L^9\) and
Sobolev for Proposition 3.1, whose constant reproduces the audited \(C_*\)
after one substitution; two-parameter scaling for Proposition 3.2;
`lem:quotient-transport` with \eqref{eq:cp-continuity} for Lemma R1 and pure
algebra for Lemma R2; the manuscript's \eqref{eq:L4L3} plus time-Hölder
\((4,4/3)\) for Lemma 4.3; Chebyshev at exponent \(4\) for Theorem 4.5 item 1
and at exponent \(3\) for Lemma R3 item 3;
\(D_3(w)\ge c\|u\|_9^3\) plus Hölder in time for O1; an explicit
two-parameter step family for O2 (computed instance displayed); the
saturation observation for O3. No numerics were used anywhere in this note.
The audit's own two random-sampling computations (Bregman constants, O2
arithmetic) are bounded evidence, never proof, and neither is load-bearing
here.

**FIRST GAP:** unchanged and not closed:
\(\int_0^\tau K\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+M\int_0^\tau\mathcal Q\,dt+A_{\rm input}\),
uniformly for \(\tau<\min\{H,T_*\}\), \(\theta\le1\). This note sharpens its
*shape*: by Corollary 4.4 the \(M\)-term and the cutoff \(L\) are removable,
so the gap is exactly (G) of §4.5 with \(\theta=0\), i.e. an input-only bound
for \(\int_0^\tau\|q\|_3D_3(w)\,dt\); and by Corollary 4.2 it follows from
`hyp:absorption` with the explicit remainder \(A+\frac13\|u_0\|_3^3\), an
implication already available in the manuscript by composition and new here
only in its explicit constant. The first unsupported implication if one tried
to close it here is exactly "(F-a)+(F-b) \(\Rightarrow\) absorption", refuted
by Proposition 4.6 in both the \(L^3\) and the \(L^4\) form of (F-b).

**SURVIVING CONDITIONAL SUFFIX:** (i) If \(C_\sharp\sup_{t<T_*}\|q(u(t))\|_3\le\nu\)
then \(\sup_t\|u\|_3\le C_3\|u_0\|_3\) and \(T_*=\infty\) (Proposition 3.3);
the hypothesis is on the unknown trajectory. (ii) If `hyp:absorption` holds
with any \(\theta'\in[0,1)\), then the quotient gap holds with \(\theta=1\),
\(M=0\), \(A_{\rm input}=A+\frac13\|u_0\|_3^3\) (Corollary 4.2), hence
`hyp:critical` and the Clay conclusion by `prop:quotient-conditional` and
`thm:conditional`. (iii) If (G) holds, the gap holds with \(\theta=0\).
(iv) If the nonlinear projection is \(L^3\)-Lipschitz at points of
\(\mathcal M\), then — with a nonvanishing first-order coefficient —
\(\alpha=1\) in (3.1) is sharp and no member of the lattice of
Proposition 3.2 with \(\alpha>1\) exists (Lemma R2, the direction now stated
consistently in §3.2 and here). None of (i)–(iv) is proved.

**NON-CLAIMS:** no proof or disproof of the first gap, of `hyp:highstrain`,
`hyp:highpressure`, `hyp:absorption`, `hyp:critical`, or of NS-R3; no
regularity theorem, and Proposition 3.3 is a conditional criterion with a
non-input hypothesis; no sign for \(K(t)\), \(P_3(t)\),
\(D_3(w)-D_3(u)\) or any of their time integrals; no claim that
\(D_{\mathcal Q}(u)\le D_3(u)\) or the reverse (both remain undecided here);
no bound on \(\sup_t\|u\|_3\), \(\int D_3(w)\,dt\), \(\int D_3(w)^r dt\)
(\(r>1\)), \(\int_{\mathcal G_\tau}D_3(w)\,dt\), or \(\int\|q\|_3D_3(w)\,dt\);
no progress on (H1), (H2), (W), or on \(\|w(u)\|_2\le C\|u\|_2\); no
differentiation of the minimizer anywhere, and no assertion that \(d_1\) is
differentiable in time; no use of the three unaudited HF19 notes or of the
HF20 candidate as premises. Further non-claims recorded by the audit and kept
here: the \(\tau\)-uniform (4.5) is a strengthening of a *measure* bound only
and implies nothing about where the dissipation sits; no member of the lattice
with \(\alpha>1\) is claimed to exist and none with \(\alpha\in(1,2]\) is
refuted; whether \(q\) is \(L^3\)-Lipschitz at \(\mathcal M\), and whether the
first-order coefficient of \(K\) there vanishes in general, are undecided; no
novelty is claimed for the nonlinear-Hodge construction, for the input-only
\(L^3_t\)/\(L^4_t\) distance bound (`prop:scaling`(iii)), or for the
implication `hyp:absorption` \(\Rightarrow\) `hyp:highstrain`; the
simplification of `hyp:highstrain` in Corollary 4.4 is an integration
*candidate* and is not promoted. Proposition 4.6 refutes an implication
between two displayed facts, not the gap.

**NEXT DISTINCT ACTION:** attack (G) directly, since Corollary 4.4 shows it
is the whole of the frozen gap: prove or refute an input-only bound for
\(\int_0^\tau\|q(t)\|_3\,D_3(w(t))\,dt\). The sub-questions this note
isolates, in the order the audit recommends: (a) is
\(D_{\mathcal Q}(u)=D_3(w)\le D_3(u)\)? — a fixed-time, minimizer-free,
scaling-consistent question (\((a^3,\lambda^2)\) on both sides) whose
affirmative answer would delete the term \(\nu\int(D_3(w)-D_3(u))\) from (4.1)
and give \(\int K\le\int P_3+\frac13\|u_0\|_3^3\), i.e. the quotient gap with
\(\theta=0\) from the pressure flux alone; (b) is the nonlinear projection
\(L^3\)-Lipschitz at points of \(\mathcal M\), \(\|q(U+z)\|_3\le C(U)\|z\|_3\)?
— which decides the sharpness of \(\alpha=1\) **in the R2 direction**, i.e.
Lipschitz *refutes* \(\alpha>1\), and would settle \(\alpha\in(1,2]\);
(c) is any input-only bound for \(\int_{\mathcal G^\delta_\tau}D_3(w)\,dt\)
available for some fixed \(\delta\in(0,1]\)? — O3, the only good-set statement
left open by R3. Corollary 4.4 and Corollary 4.2 are integration candidates
for the controller, not promotions.

## 7. Sources

All manuscript labels are from `../navier-paper/main.tex` at the current
head, directly inspected this wave [DI]: `sec:quotient` in full,
`prop:energy`, `def:D3P3`, `prop:pressure`, `prop:scaling` with
\eqref{eq:L4L3}, `rem:mismatch`, `def:sobolev-constant`, `hyp:highpressure`,
`hyp:absorption`, `lem:absorption-split`, `cor:absorption-consequence`,
`prop:lowpressure`, `thm:continuation`, `hyp:critical`, `thm:conditional`,
`rem:no-monotone`. Repository evidence used as premises [DI]:
`hf18-hodge-regularity.md` with `hf18-review-hodge-regularity.md` (PASS); and
the audit of this note, `hf21-review-crossing-sign-structure.md` (REPAIR),
whose replacement lemmas R1–R4 are reproduced above and whose corrections are
applied throughout. Repository evidence read but used in exactly two places,
§3.3's scope sentence and §4.6, and nowhere else [DI]:
`hf18-divergence-speed-link.md` with `hf18-review-divergence-speed-link.md`
and `-r2.md` (PASS after S1–S4). Read as background but not a separate
premise, its content being available through the manuscript labels [DI]:
`hf17-quotient-functional.md`, `hf17-quotient-evolution.md`; also `PLAN.md`.
Read but not used as premises, and marked as such at every occurrence [DI]:
`hf19-second-order-falsifier.md`, `hf19-temporal-normal-form.md`,
`hf19-difference-functional.md` (unaudited), `hf20-harmonic-strain-test.md`
(audited REPAIR; its integrated content is the manuscript's
`rem:no-monotone`). External facts used are only those already imported by the
manuscript (Brezis; Grafakos; Stein; Tao 2013; ESS), through the labels above;
no new external source is cited and none is [MO] load-bearing.