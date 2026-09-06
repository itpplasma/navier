# HF19-D: the difference functional \(\Delta=X/3-\mathcal Q\), its exact evolution, and the sign structure of \(D_3(u)-D_3(w)\)

Status: **audited, REPAIR applied by the controller**, 2026-09-06. The
independent audit `hf19-review-difference-functional.md` returns **REPAIR**:
§§1–3 and §4.1 were reconstructed independently and are correct as stated
(including a from-scratch re-derivation of the Fermi-chart identity (3.3),
which agrees exactly), and the first bad bridge is in the *negative* section
§4.2, which discharges nothing: its selection of (4.3) as "the strongest
candidate" was unjustified, and its "no scaling family violates (4.3)" was
unsupported for the second half of (4.3) and is, on the scaling heuristic,
refuted there on the HF18-B witness family. The controller has applied the
audit's repairs: the unsupported claims are **removed** (not patched); the
audit's replacement Lemma R1 (sharp two-sided defect control) is inserted with
its proof and consequences; the corrected candidate (4.3\('\)) replaces (4.3)
as the recorded open side-question; the \(|D_3(u)-D_3(w)|\) half is recorded as
closed-negative pending one bounded cell computation; the retirement wording is
demoted from a non-existence claim to a survey result; and the editorial and
scope items of the audit's cosmetic list are applied. Everything downstream of
the bad bridge is unchanged, in particular the exact evolution (Theorem 2.2)
and the heat-flow identity (Theorem 3.2). The FIRST GAP is untouched.

Lane HF19-D, MODE: DISCOVER, 2026-09-05. Inputs: PLAN.md ("Frontier packet",
"Beyond the checkpoint", "HF16–HF17", "HF18"); manuscript `sec:quotient`
(labels `lem:cubic-pointwise`, `lem:cubic-frechet`, `lem:quotient-minimizer`,
`lem:quotient-coercive`, `lem:quotient-heat`, `lem:quotient-stability`,
`prop:quotient-derivative`, `lem:quotient-pressure`, `lem:quotient-chainrule`,
`lem:heat-generator`, `lem:quotient-heatsign`, `lem:quotient-transport`,
`prop:quotient-evolution`, `lem:quotient-lowstrain`, `hyp:highstrain`) and
`def:D3P3`, `prop:pressure`; audited notes `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, `hf18-hodge-regularity.md` (+ review),
`hf18-divergence-speed-link.md` (+ two reviews). Source tags: [DI] directly
inspected, [MO] metadata only or standard textbook fact, never load-bearing.

**MODE / RESULT: DISCOVER, with two exact obstructions.** The difference
\(\Delta:=\tfrac13\|u\|_3^3-\mathcal Q(u)\ge0\) of the two audited cubic
functionals has the exact evolution
\(\Delta'=\langle j(u)-A,\,u_t\rangle\), i.e.
\(\Delta'+\nu\,(D_3(u)-D_3(w))=P_3-K\), and every term is the pairing of one
object, the *Hodge defect* \(A-j(u)=|w|w-|u|u\), with one piece of the
equation: \(D_3(u)-D_3(w)=\langle A-j(u),\Delta u\rangle\),
\(P_3=\langle A-j(u),\nabla p\rangle\), \(K=-\langle A-j(u),(u\cdot\nabla)u\rangle\),
\(P_3-K=\langle A-j(u),\mathbb P[(u\cdot\nabla)u]\rangle\). The defect is
controlled two-sidedly by \(\Delta\):
\(\tfrac16\|q\|_3^3\le\Delta\le(\|w\|_3+\|u\|_3)\|q\|_3^2\) and
\(\|A-j(u)\|_{3/2}\le(\|w\|_3+\|u\|_3)\|q\|_3\), and sharply, for solenoidal
\(u\), by \(\Delta\ge\tfrac14\int|w||q|^2\) and
\(\|A-j(u)\|_{3/2}\le C_1\Delta^{1/2}\mathcal Q^{1/6}\) (Lemma R1, supplied by
the audit). The sign question is settled negatively in both directions by two
rigorous heat-flow arguments that never differentiate the minimizer: (i) for
every solenoidal \(u\in H^m(\mathbb R^3)\), \(m\ge4\), with \(u\notin\mathcal M\),
\(\int_0^\infty\big(D_3(G_su)-D_3(w(G_su))\big)\,ds=\Delta(u)>0\), so
\(D_3(w)\ge D_3(u)\) fails on a set of positive measure along every such heat
trajectory; (ii) \(D_3(w)\le D_3(u)\) on the class would force \(\mathcal M\) to be
invariant under the heat semigroup, and it is not: for the "elliptic swirl"
\(u_0=f(x_3)\,\varphi(d)\,\nabla^\perp d\) (\(d\) the distance to a non-circular
convex curve) one computes in closed form
\(\partial_s\big|_{s=0}\,\operatorname{div}(|G_su_0|G_su_0)=-4\kappa\kappa_s\varphi^3/(1+\kappa d)^4\ne0\).
Hence \(D_3(u)-D_3(w)\) has no sign, and \(P_3-K\) has none either. Among the
\(\Delta\)-weighted bounds surveyed here — the exact monomial lattice
\(\Delta^\alpha\mathcal Q^\beta D\) with \(\alpha+\beta=\tfrac13\), and more
generally any bound that controls \(\Delta'\) by the dissipation — every member
Grönwalls into a bound of \(\Delta\) by \(\int(D_3(u)+D_3(w))\,dt\), the very
quantity the gap is about; the difference functional therefore supplies no
coercive mechanism, and **no producer was found among the bounds surveyed**.
No claim is made that none exists. HIGH-STRAIN and HIGH-PRESSURE remain open;
NS-R3 remains open.

## 0. Setting, notation, audited inputs

Throughout, \((u,p)\) is the classical branch on a compact interval
\([0,T]\subset[0,T_*)\) with package (R1)–(R3) of the manuscript
(\(u\in C^1([0,T];H^k)\) for every \(k\), \(p=R_iR_j(u_iu_j)\), the equation
holds pointwise, \(u,\nabla u,\Delta u,u_t,p,\nabla p\in C([0,T];L^r)\) for
\(2\le r\le\infty\)). For a field \(z\) put \(j(z)=|z|z\),
\(F(z)=\tfrac13\|z\|_3^3\). Manuscript objects: \(\mathcal G_3\), \(\mathcal Q\),
the minimizer \(q=q(u)\in\mathcal G_3\), \(w=u+q\), \(A=j(w)\),
\(\mathbb P\) with \(C_{\mathbb P}=\|\mathbb P\|_{L^3\to L^3}\), \(G_s=e^{s\Delta}\).
Pressure-route objects (`def:D3P3`): \(X=\|u\|_3^3\),
\[
 D_3(u)=\int\big(|u||\nabla u|^2+|u||\nabla|u||^2\big)dx,\qquad
 P_3=\int p\,u\cdot\nabla|u|\,dx ,
\]
the integrands being \(0\) on \(\{u=0\}\). Quotient-route objects
(HF17, HF18-A): \(D_{\mathcal Q}(u):=-\langle A,\Delta u\rangle\ge0\),
\(K:=\mathcal Q'+\nu D_{\mathcal Q}(u)=-\langle A,(u\cdot\nabla)u\rangle\)
(manuscript `lem:quotient-chainrule`, `prop:quotient-evolution`), and the
audited identification \(D_{\mathcal Q}(u)=D_3(w)\) (HF18-A Theorem 2, PASS),
where \(D_3(w)=\int(|\nabla V|^2-\tfrac19|\nabla|V||^2)\), \(V=|w|^{1/2}w\in H^1\).
Below, "\(D_3(w)\)" always means \(D_{\mathcal Q}(u)=-\langle A,\Delta u\rangle\);
nothing here depends on the approximate-gradient reading. Finally
\[
 \mathcal M:=\{v\in L^3:\ \operatorname{div}(|v|v)=0\ \text{in }\mathcal D'\},
\]
and (HF18-B Prop. 1.4, audited; manuscript `lem:quotient-minimizer`) a
solenoidal \(v\in L^3\) lies in \(\mathcal M\) iff \(q(v)=0\) iff \(w(v)=v\).
For smooth solenoidal \(v\), \(\operatorname{div}(|v|v)=v\cdot\nabla|v|\) (a.e.,
with the a.e. gradient of the Lipschitz function \(|v|\)), so
\(v\in\mathcal M\iff v\cdot\nabla|v|\equiv0\).

Scaling bookkeeping (HF18-B §0): under amplitude \(a\) and dilation
\(\lambda\), \(\mathcal Q,\ F(u),\ \Delta,\ \|q\|_3^3\sim(a^3,\lambda^0)\);
\(D_3(u),D_3(w)\sim(a^3,\lambda^2)\); \(P_3,K,\Delta',\nu D_3\sim(a^4,\lambda^2)\)
with \(\nu\sim(a,\lambda^0)\); \(\|A-j(u)\|_{3/2}\sim(a^2,\lambda^0)\);
\(\|\nabla p\|_3,\|(u\cdot\nabla)u\|_3,\|\mathbb P(u\cdot\nabla)u\|_3\sim(a^2,\lambda^2)\);
\(\|\Delta u\|_3\sim(a,\lambda^2)\). Every displayed inequality below was
checked against this table.

## 1. The difference functional and the Hodge defect

**Definition.** \(\Delta(u):=F(u)-\mathcal Q(u)=\tfrac13\|u\|_3^3-\tfrac13\|w\|_3^3\)
for \(u\in L^3\), and for solenoidal \(u\) the *ratio*
\(\rho(u):=\mathcal Q(u)/F(u)=1-\Delta(u)/F(u)\in[C_{\mathbb P}^{-3},1]\)
(`lem:quotient-coercive`), dimensionless and invariant under both scalings.

**Lemma 1.1 (cubic lower Taylor bound).** For \(a,h\in\mathbb R^3\),
\[
 f(a+h)-f(a)-j(a)\cdot h\ \ge\ \tfrac16|h|^3,\qquad f(z)=\tfrac13|z|^3 .
\]
*Proof.* \(f(a+h)-f(a)-j(a)\cdot h=\int_0^1\big(j(a+\theta h)-j(a)\big)\cdot h\,d\theta\)
(\(f\in C^1\), `lem:cubic-pointwise`). By `eq:cp-monotone` of
`lem:cubic-pointwise` applied to the pair \(a+\theta h,\ a\):
\((j(a+\theta h)-j(a))\cdot(\theta h)\ge\tfrac12|\theta h|^3\), i.e.
\((j(a+\theta h)-j(a))\cdot h\ge\tfrac12\theta^2|h|^3\) for \(\theta>0\);
integrate. \(\square\)

**Proposition 1.2 (two-sided control of \(\Delta\); the defect).** For every
\(u\in L^3\), with \(q=q(u)\), \(w=w(u)\):
\[
 \tfrac16\|q\|_3^3\ \le\ \Delta(u)\ \le\ -\langle j(u),q\rangle-\tfrac16\|q\|_3^3
 \ \le\ (\|w\|_3+\|u\|_3)\,\|q\|_3^2 ,                                    \tag{1.1}
\]
\[
 \|A-j(u)\|_{3/2}\ \le\ (\|w\|_3+\|u\|_3)\,\|q\|_3\ \le\ (\|w\|_3+\|u\|_3)\,(6\Delta)^{1/3}. \tag{1.2}
\]
In particular \(\Delta(u)=0\iff q(u)=0\iff u\in\mathcal M\) (for solenoidal \(u\)),
and for solenoidal \(u\), using \(\|u\|_3\le C_{\mathbb P}\|w\|_3\) and
\(\|w\|_3=(3\mathcal Q)^{1/3}\),
\(\|A-j(u)\|_{3/2}\le(1+C_{\mathbb P})\,(3\mathcal Q)^{1/3}(6\Delta)^{1/3}\).

*Proof.* Lemma 1.1 with \(a=w\), \(h=-q\), integrated: \(F(u)-F(w)+\langle A,q\rangle\ge\tfrac16\|q\|_3^3\), and
\(\langle A,q\rangle=0\) (`lem:quotient-minimizer`(c)); this is the first
inequality. Lemma 1.1 with \(a=u\), \(h=q\): \(F(w)-F(u)-\langle j(u),q\rangle\ge\tfrac16\|q\|_3^3\),
which is the second. Then \(-\langle j(u),q\rangle=\langle A-j(u),q\rangle\le\|A-j(u)\|_{3/2}\|q\|_3\)
and `eq:cp-F-lipschitz` of `lem:cubic-frechet` gives (1.2) and the last
inequality of (1.1). All pairings are \(L^{3/2}\times L^3\). \(\square\)

Scaling: every term of (1.1) is \((a^3,\lambda^0)\), of (1.2) \((a^2,\lambda^0)\).
Remark: (1.1) says \(\Delta\) is a *coercive distance to \(\mathcal M\)* in the
gradient part, comparable to \(\|q\|_3^3\) from below and to
\(\|w\|_3\|q\|_3^2\) from above; it is not coercive on \(u\) (it vanishes on all
of \(\mathcal M\), which contains every *decaying* axisymmetric swirl and every
*decaying* shear flow — representatives must lie in \(L^3\), since
\(\mathcal M\subset L^3\)). This already excludes \(\Delta\) as a stand-alone
Lyapunov functional.

**Lemma R1 (sharp two-sided control of the Hodge defect by \(\Delta\);
supplied by the audit `hf19-review-difference-functional.md`).**
Let \(u\in L^3(\mathbb R^3;\mathbb R^3)\), \(q=q(u)\), \(w=w(u)=u+q\), \(A=j(w)\).
Then
\[
 \Delta(u)\ \ge\ \tfrac14\int_{\mathbb R^3}|w|\,|q|^2\,dx,                  \tag{R1a}
\]
and if in addition \(u\) is solenoidal,
\[
 \|A-j(u)\|_{3/2}\ \le\ C_1\,\Delta(u)^{1/2}\,\mathcal Q(u)^{1/6},\qquad
 C_1=\bigl(14\,(3+C_{\mathbb P})\bigr)^{1/2}3^{1/6}.                        \tag{R1b}
\]

*Proof of (R1a).* By `lem:quotient-minimizer`(c), \(\langle A,q\rangle=0\), so
\[
 \Delta(u)=F(u)-F(w)=\int\bigl(f(w-q)-f(w)+j(w)\cdot q\bigr)dx
 =\int\!\!\int_0^1\bigl(j(w-\theta q)-j(w)\bigr)\cdot(-q)\,d\theta\,dx,
\]
using \(f\in C^1\) with \(\nabla f=j\) (`lem:cubic-pointwise`). Apply the
*identity* half of `eq:cp-monotone` to the pair \(a=w-\theta q\), \(b=w\), so
\(a-b=-\theta q\):
\[
 \bigl(j(w-\theta q)-j(w)\bigr)\cdot(-\theta q)
 =\bigl(|w-\theta q|+|w|\bigr)\Bigl(\tfrac12\bigl(|w-\theta q|-|w|\bigr)^2
 +\tfrac12\theta^2|q|^2\Bigr)\ \ge\ \tfrac12|w|\,\theta^2|q|^2 ,
\]
both discarded terms being nonnegative. Dividing by \(\theta>0\) and
integrating \(\int_0^1\tfrac12\theta\,d\theta=\tfrac14\) gives a nonnegative
integrand \(\ge\tfrac14|w||q|^2\) pointwise; Tonelli permits the exchange. \(\square\)

*Proof of (R1b).* By `eq:cp-lipschitz`,
\(|A-j(u)|=|j(w)-j(w-q)|\le(|w|+|w-q|)|q|\le(2|w|+|q|)|q|\). Write
\[
 \bigl((2|w|+|q|)|q|\bigr)^{3/2}
 =\bigl[(2|w|+|q|)|q|^2\bigr]^{3/4}\,(2|w|+|q|)^{3/4}
\]
and apply Hölder with exponents \(\tfrac43\) and \(4\):
\[
 \int|A-j(u)|^{3/2}\le\Bigl(\int(2|w|+|q|)|q|^2\Bigr)^{3/4}
 \Bigl(\int(2|w|+|q|)^3\Bigr)^{1/4}.
\]
For the first factor, (R1a) and the first inequality of (1.1) give
\(\int(2|w|+|q|)|q|^2=2\int|w||q|^2+\int|q|^3\le8\Delta+6\Delta=14\Delta\).
For the second, Minkowski and \(\|q\|_3\le(1+C_{\mathbb P})\|w\|_3\)
(`lem:quotient-coercive`, solenoidal \(u\)) give
\(\int(2|w|+|q|)^3\le(3+C_{\mathbb P})^3\|w\|_3^3=(3+C_{\mathbb P})^3\,3\mathcal Q\).
Hence
\(\|A-j(u)\|_{3/2}^{3/2}\le(14\Delta)^{3/4}(3+C_{\mathbb P})^{3/4}(3\mathcal Q)^{1/4}\),
i.e. \(\|A-j(u)\|_{3/2}\le(14(3+C_{\mathbb P}))^{1/2}\Delta^{1/2}(3\mathcal Q)^{1/6}\). \(\square\)

Scaling: \(\Delta^{1/2}\mathcal Q^{1/6}\sim(a^{3/2},\lambda^0)(a^{1/2},\lambda^0)=(a^2,\lambda^0)\),
the weight of \(\|A-j(u)\|_{3/2}\) — the same as (1.2), as it must be.
Comparison: (R1b) improves the right-hand side of (1.2) by the factor
\((\Delta/\mathcal Q)^{1/6}\le(C_{\mathbb P}^3-1)^{1/6}\), so it never exceeds
(1.2) by more than a fixed factor and is strictly sharper in the
near-\(\mathcal M\) regime, where it is order-correct. The audit records that
the §5.1 numerics already exhibit this: there \(\tfrac16\|q\|_3^3=0.0068\)
against \(\Delta=0.79\), two orders of magnitude of slack in the cube-root
bound, whereas \(\tfrac14\int|w||q|^2\) is of the right order. (No new number
was computed for this note; the observation is the auditor's, from the same
frozen table.)

## 2. Exact evolution of \(\Delta\) and of \(\rho\)

**Lemma 2.1 (pointwise cubic balance on the classical branch).** On \([0,T]\),
\(t\mapsto X(t)\) is \(C^1\) and
\[
 \tfrac13X'+\nu D_3(u)=P_3,\qquad
 D_3(u)=-\langle j(u),\Delta u\rangle,\qquad
 P_3=-\langle j(u),\nabla p\rangle,\qquad \langle j(u),(u\cdot\nabla)u\rangle=0. \tag{2.1}
\]
*Proof.* \(F\) is Fréchet differentiable on \(L^3\) with \(DF(v)[h]=\langle j(v),h\rangle\)
(`lem:cubic-frechet`, `eq:cp-F-taylor`) and \(u\in C^1([0,T];L^3)\)
(Step 1 of `lem:quotient-chainrule`), so \(\tfrac13X'=\langle j(u),u_t\rangle\)
with \(u_t=\nu\Delta u-(u\cdot\nabla)u-\nabla p\), each term in \(L^3\).
\(j(u)\in C^1\) with \(\nabla j(u)=Dj(u)\nabla u\), \(|Dj(u)|\le2|u|\), so
\(j(u)\in W^{1,3/2}\) and the cutoff argument of HF18-A Theorem 2 Step 3 gives
\(-\langle j(u),\Delta u\rangle=\int\nabla j(u):\nabla u=\int(|u||\nabla u|^2+u_j\partial_i|u|\,\partial_iu_j)
=\int(|u||\nabla u|^2+|u||\nabla|u||^2)=D_3(u)\), using \(u_j\partial_iu_j=|u|\partial_i|u|\)
a.e. Next \(j(u)\cdot(u\cdot\nabla)u=u\cdot\nabla(|u|^3/3)\) with \(|u|^3\in W^{1,1}\),
so the pairing vanishes by HF18-A (0.3). Finally
\(-\langle j(u),\nabla p\rangle=\int p\operatorname{div}j(u)=\int p\,u\cdot\nabla|u|=P_3\)
(same cutoff, \(p\in L^3\), \(\operatorname{div}j(u)=|u|\operatorname{div}u+u\cdot\nabla|u|\)).
Continuity of \(t\mapsto D_3(t),P_3(t)\) follows, since
\(-\langle j(u),\Delta u\rangle\) and \(-\langle j(u),\nabla p\rangle\) are
continuous in \(t\) by (R3) and `eq:cp-F-lipschitz`. \(\square\)

**Remark 2.1\('\) (this is not an application of `prop:pressure`; audit
integration item).** Lemma 2.1 does not import `prop:pressure`(ii): it
*re-derives* the cubic balance in pointwise \(C^1\) form from
`lem:cubic-frechet`, \(u\in C^1([0,T];L^3)\), and the three fixed-time
identifications above. It is therefore a **strict upgrade** of
`prop:pressure`(ii), which the manuscript states as an integrated identity on
\([s,t]\) with \(D_3,P_3\) merely measurable and bounded (`prop:pressure`(i)):
Lemma 2.1 yields \(X\in C^1([0,T])\) with \(t\mapsto D_3(t),P_3(t)\) *continuous*.
§2 below therefore carries **no dependency** on `prop:pressure`. The audit
records this upgrade as a manuscript-grade by-product that should be recorded
in the manuscript rather than left in an evidence note; that integration is a
separate action and is not performed here.

**Theorem 2.2 (evolution of the difference).** On \([0,T]\), \(\Delta\circ u\in C^1\) and
\[
 \boxed{\ \Delta'=\langle j(u)-A,\ u_t\rangle=-\langle A-j(u),\ u_t\rangle,\ }  \tag{2.2}
\]
\[
 \boxed{\ \Delta'+\nu\big(D_3(u)-D_3(w)\big)=P_3-K,\ }                          \tag{2.3}
\]
where, with the Hodge defect \(A-j(u)=|w|w-|u|u\in L^{3/2}\),
\[
 D_3(u)-D_3(w)=\langle A-j(u),\Delta u\rangle,\qquad
 P_3=\langle A-j(u),\nabla p\rangle,\qquad
 K=-\langle A-j(u),(u\cdot\nabla)u\rangle,                                 \tag{2.4}
\]
\[
 P_3-K=\langle A-j(u),\ (u\cdot\nabla)u+\nabla p\rangle=\langle A-j(u),\ \mathbb P[(u\cdot\nabla)u]\rangle,
 \qquad
 P_3+K=\langle A-j(u),\ \nabla p-(u\cdot\nabla)u\rangle.                    \tag{2.5}
\]
All pairings converge absolutely (\(A-j(u)\in L^{3/2}\); \(u_t,\Delta u,\nabla p,(u\cdot\nabla)u\in L^3\)).
On \(\mathcal M\) (i.e. at any time with \(q(t)=0\)) every quantity in
(2.2)–(2.5) vanishes: \(\Delta=0\), \(\Delta'=0\), \(D_3(u)=D_3(w)\), \(P_3=K=0\).

*Proof.* \(\mathcal Q\circ u\in C^1\) with \(\mathcal Q'=\langle A,u_t\rangle\)
(`lem:quotient-chainrule`), and \(\tfrac13X'=\langle j(u),u_t\rangle\) (Lemma 2.1);
subtract: (2.2). Insert the equation: \(\Delta'=\nu\langle j(u)-A,\Delta u\rangle-\langle j(u)-A,(u\cdot\nabla)u\rangle-\langle j(u)-A,\nabla p\rangle\).
Now \(-\langle j(u),\Delta u\rangle=D_3(u)\) and \(-\langle A,\Delta u\rangle=D_{\mathcal Q}=D_3(w)\),
so the first term is \(-\nu(D_3(u)-D_3(w))\) and the first identity of (2.4)
holds. \(\langle A,\nabla p\rangle=0\) (`lem:quotient-pressure`) gives
\(P_3=-\langle j(u),\nabla p\rangle=\langle A-j(u),\nabla p\rangle\).
\(\langle j(u),(u\cdot\nabla)u\rangle=0\) gives \(K=-\langle A,(u\cdot\nabla)u\rangle=-\langle A-j(u),(u\cdot\nabla)u\rangle\).
Adding, \(\Delta'=-\nu(D_3(u)-D_3(w))+P_3-K\), i.e. (2.3); (2.5) follows, with
\((u\cdot\nabla)u+\nabla p=\mathbb P[(u\cdot\nabla)u]\) since \(-\nabla p=(I-\mathbb P)[(u\cdot\nabla)u]\)
in the manuscript's normalisation (HF18-B §0, verified there by FFT).
The vanishing on \(\mathcal M\) is \(A=j(u)\) when \(q=0\). \(\square\)

**Corollary 2.3 (ratio).** With \(\rho=\mathcal Q/F(u)\),
\[
 \rho'+\frac{\nu}{F(u)}\big(D_3(w)-\rho\,D_3(u)\big)=\frac{K-\rho P_3}{F(u)},
 \qquad
 (\log\rho)'=\frac{K-\nu D_3(w)}{\mathcal Q}-\frac{P_3-\nu D_3(u)}{F(u)} .    \tag{2.6}
\]
Both brackets vanish on \(\mathcal M\) (\(\rho=1\)). Proof: quotient rule from
\(\mathcal Q'+\nu D_3(w)=K\) and Lemma 2.1; \(F(u)>0\) unless \(u=0\).

Remarks. (i) (2.2) is the cleanest statement: the defect functional moves by
the pairing of the Hodge defect with the velocity increment; the two audited
balances are its decomposition along \(\nu\Delta u\) and
\(-\mathbb P[(u\cdot\nabla)u]\). (ii) Since \(F(u)=\mathcal Q+\Delta\) with
both terms \(\ge0\) and \(\mathcal Q\ge F(u)/C_{\mathbb P}^3\), a bound on any two
of \(F(u),\mathcal Q,\Delta\) bounds the third, and a bound on either of
\(F(u),\mathcal Q\) bounds the other; the difference route cannot be easier
than either audited route. (iii) The pressure work is a pairing with the
defect: \(P_3=\langle A-j(u),\nabla p\rangle\); so is its high-frequency part
\(Q_J=\langle A-j(u),\nabla p_{>J}\rangle\) (`def` of \(Q_J\) in the manuscript,
same argument), which exhibits HIGH-PRESSURE as "defect against high pressure
gradient". This is an equivalent identity and, by the packet rule, discharges
nothing.

## 3. Sign structure of \(D_3(u)-D_3(w)\): two heat-flow theorems

The natural guess "\(w\) is a 3-harmonic projection, so \(D_3(w)\le D_3(u)\)"
and its opposite are both false on the class of smooth solenoidal fields. Both
proofs use the heat semigroup and never differentiate the minimizer.

**Lemma 3.1 (heat flow of \(\Delta\)).** Let \(u\in H^m(\mathbb R^3)\), \(m\ge4\), be
solenoidal, and \(v_s:=G_su\). Then \(s\mapsto\Delta(v_s)\) belongs to
\(C^1([0,\infty))\) (one-sided at \(0\)) with
\[
 \frac{d}{ds}\Delta(v_s)=\langle j(v_s)-A(v_s),\Delta v_s\rangle=D_3(w(v_s))-D_3(v_s), \tag{3.1}
\]
and \(\Delta(v_s)\to0\) as \(s\to\infty\).

*Proof.* \(v_s\) is solenoidal and in \(H^m\) for every \(s\ge0\). By
`lem:heat-generator`, \((G_hv_s-v_s)/h\to\Delta v_s\) in \(L^3\) as \(h\downarrow0\);
for \(h\uparrow0\) and \(s>0\) write \((v_{s+h}-v_s)/h=G_{s+h}\big[(G_{|h|}u-u)/|h|\big]\),
\(G_{s+h}\) applied to a family converging to \(\Delta u\) in \(L^3\), and use the
\(L^3\) contraction with strong continuity (`lem:qe-heat-continuity`(b)) to
get the limit \(G_s\Delta u=\Delta v_s\).
So \(s\mapsto v_s\) is \(C^1\) into \(L^3\) with derivative \(\Delta v_s\). The
Fréchet derivatives of \(F\) and \(\mathcal Q\) (`lem:cubic-frechet`,
`prop:quotient-derivative`) give (3.1) by the chain rule; continuity of the
derivative in \(s\) follows from \(v\mapsto A(v)\) continuous \(L^3\to L^{3/2}\)
(`lem:quotient-stability`), \(v\mapsto j(v)\) likewise, and \(s\mapsto\Delta v_s\)
continuous into \(L^3\). The identifications \(-\langle j(v),\Delta v\rangle=D_3(v)\)
(Lemma 2.1, applied at the fixed field \(v=v_s\)) and
\(-\langle A(v),\Delta v\rangle=D_{\mathcal Q}(v)=D_3(w(v))\) (HF18-A Theorem 2 at
\(v\in H^m\) solenoidal) give the second form. Decay:
\(0\le\Delta(v_s)\le F(v_s)=\tfrac13\|v_s\|_3^3\) and
\(\|v_s\|_3\le\|v_s\|_2^{2/3}\|v_s\|_\infty^{1/3}\le\|u\|_2^{2/3}(\|k_s\|_2\|u\|_2)^{1/3}
=(8\pi s)^{-1/4}\|u\|_2\to0\), with \(\|k_s\|_2=(8\pi s)^{-3/4}\). \(\square\)

**Theorem 3.2 (heat-flow identity; the "\(\ge\)" direction fails).** For every
solenoidal \(u\in H^m\), \(m\ge4\),
\[
 \boxed{\ \int_0^\infty\Big(D_3(G_su)-D_3\big(w(G_su)\big)\Big)ds=\Delta(u)\ \ge\ \tfrac16\|q(u)\|_3^3,\ } \tag{3.2}
\]
as an improper Riemann integral of a continuous function (absolute convergence
is not claimed and not needed). Consequently, if \(u\notin\mathcal M\), then
\(D_3(w(G_su))<D_3(G_su)\) on a set of \(s\) of positive measure: the inequality
\(D_3(w(v))\ge D_3(v)\) fails on the class of Schwartz solenoidal fields. An
explicit \(u\notin\mathcal M\): \(u=\operatorname{curl}(x_1e^{-|x|^2}e_3)=e^{-|x|^2}(-2x_1x_2,\,2x_1^2-1,\,0)\),
for which \(u\cdot\nabla|u|^2=4e^{-3}\ne0\) at \((0,1,0)\).

*Proof.* Integrate (3.1) over \([0,S]\) and let \(S\to\infty\) using
\(\Delta(v_S)\to0\); then (1.1). The explicit field is Schwartz and
solenoidal; \(|u|^2=e^{-2|x|^2}(4x_1^2x_2^2+(1-2x_1^2)^2)\), and at \(x_1=0\),
\(\partial_2|u|^2=-4x_2e^{-2(x_2^2+x_3^2)}\), \(u_2=-e^{-|x|^2}\), so
\(u\cdot\nabla|u|^2=4e^{-3}\) at \((0,1,0)\); hence \(\operatorname{div}(|u|u)\not\equiv0\)
and \(u\notin\mathcal M\). \(\square\)

Scaling of (3.2): \(D_3\,ds\sim(a^3,\lambda^2)(a^0,\lambda^{-2})=(a^3,\lambda^0)=\Delta\). ✓

Reading: along every heat trajectory the solenoidal field dissipates, in
total, exactly \(\Delta(u)\) more than its representative does. This is a
rigorous integrated inequality of the kind sought, but along the *heat* flow,
not the Navier–Stokes flow; the transport term is exactly what it lacks.

**Proposition 3.3 (the "\(\le\)" direction would make \(\mathcal M\) heat-invariant).**
If \(D_3(w(v))\le D_3(v)\) for every Schwartz solenoidal \(v\), then
\(G_su_0\in\mathcal M\) for every \(u_0\in\mathcal M\cap\mathcal S\) solenoidal and
every \(s>0\). *Proof.* By (3.1), \(s\mapsto\Delta(G_su_0)\) is nonincreasing,
\(\Delta(u_0)=0\), \(\Delta\ge0\); hence \(\Delta(G_su_0)=0\), i.e. \(G_su_0\in\mathcal M\)
by Proposition 1.2. \(\square\)

**Proposition 3.4 (the elliptic swirl leaves \(\mathcal M\)).** Let \(\Gamma\subset\mathbb R^2\)
be a smooth closed strictly convex curve with arc-length parametrisation
\(\gamma\), unit tangent \(T=\gamma'\), outward unit normal \(N\), curvature
\(\kappa>0\) (\(N'=\kappa T\), \(T'=-\kappa N\)), and let \(d(x)\) be the distance
to \(\Gamma\) on the exterior. Let \(\varphi\in C_c^\infty((0,\infty))\),
\(\Psi'=\varphi\) with \(\Psi=0\) near \(+\infty\), \(\psi:=\Psi(d)\) on the exterior
and \(\psi:=\Psi(0)\) on the closed interior, \(a:=\nabla^\perp\psi=\varphi(d)\,T\),
\(f\in C_c^\infty(\mathbb R)\) with \(f\equiv1\) on \([-1,1]\), and
\[
 u_0(x):=f(x_3)\,a(x_1,x_2)\in C_c^\infty(\mathbb R^3;\mathbb R^3).
\]
Then \(u_0\) is solenoidal, \(u_0\in\mathcal M\), and, writing \(v_s=G_su_0\),
\(h(s,x):=\big(v_s\cdot\nabla|v_s|^2\big)(x)\),
\[
 \boxed{\ \partial_sh(0,x)=R(u_0)(x):=\Delta u_0\cdot\nabla|u_0|^2+2u_0\cdot\nabla(u_0\cdot\Delta u_0)
 =-\,\frac{4\,\kappa(t)\,\kappa_s(t)\,\varphi(d)^3}{(1+\kappa(t)d)^4}\ }      \tag{3.3}
\]
at every \(x=(\gamma(t)+dN(t),x_3)\) with \(|x_3|<1\), where \(\kappa_s=d\kappa/dt\)
is the arc-length derivative. Hence, if \(\Gamma\) is not a circle, then for
every point with \(\kappa_s(t)\varphi(d)\ne0\) one has \(h(s,x)\ne0\) for all
small \(s>0\), so \(G_su_0\notin\mathcal M\) for all small \(s>0\).

*Proof.* (a) *Chart.* \(\Phi(t,d)=\gamma(t)+dN(t)\) maps \(S^1\times(0,\infty)\)
bijectively onto the exterior: every exterior point has a unique nearest
point on the compact convex set bounded by \(\Gamma\) (standard [MO]), the
nearest point \(\gamma(t)\) satisfies \(x-\gamma(t)\parallel N(t)\) pointing
outward, and \(d=|x-\gamma(t)|\). \(\partial_t\Phi=(1+\kappa d)T=:JT\),
\(\partial_d\Phi=N\), \(J>0\); so \(\Phi\) is a \(C^\infty\) diffeomorphism, \(d\in C^\infty\)
on the exterior, \(\nabla d=N\), and \(\nabla^\perp d=T\). \(\psi\) is
constant on \(\{d\le\inf\operatorname{supp}\varphi\}\cup\text{interior}\) and vanishes
for \(d\ge\sup\operatorname{supp}\varphi\), hence \(\psi\in C^\infty\) and
\(a=\nabla^\perp\psi=\varphi(d)\nabla^\perp d=\varphi(d)T\in C_c^\infty\).
(b) *Membership.* \(\operatorname{div}a=0\) (a \(\nabla^\perp\)), \(|a|=|\varphi(d)|\),
\(a\cdot\nabla|a|^2=\varphi\,T\cdot\nabla(\varphi^2)=2\varphi^2\varphi'\,T\cdot N=0\).
So \(\operatorname{div}u_0=f\operatorname{div}a=0\) and
\(\operatorname{div}(|u_0|u_0)=u_0\cdot\nabla|u_0|=f^3\,a\cdot\nabla|a|=0\) a.e.,
hence in \(\mathcal D'\) (\(|u_0|u_0\in C^1\)); \(u_0\in\mathcal M\).
(c) *Differentiation in \(s\).* For Schwartz \(u_0\), \(v_s=u_0+\int_0^sG_r\Delta u_0\,dr\)
pointwise with \(G_r\Delta u_0\to\Delta u_0\) uniformly (`lem:heat-generator`,
`lem:qe-heat-continuity`(a)), and the same for \(\nabla v_s\) (apply to
\(\partial_iu_0\); \(G_r\) commutes with \(\partial_i\)). Hence \(v_s(x),\nabla v_s(x)\)
are differentiable in \(s\) at \(s=0\) with derivatives \(\Delta u_0(x)\),
\(\nabla\Delta u_0(x)\), and \(\partial_sh(0,x)=\Delta u_0\cdot\nabla|u_0|^2+u_0\cdot\nabla(2u_0\cdot\Delta u_0)=R(u_0)(x)\).
(d) *Locality.* For \(|x_3|<1\), \(u_0=a\) on a neighbourhood, so
\(\Delta u_0=\Delta_2a\), and \(R(u_0)=R_{2}(a)\), the planar expression.
(e) *Planar computation.* In the chart, a scalar \(F(t,d)\) has
\(\nabla F=(\partial_tF/J)\,T+(\partial_dF)\,N\). Writing the Cartesian
components \(a=\varphi(d)(\cos\theta(t),\sin\theta(t))\) with \(\theta'=\kappa\),
applying this gradient twice to each component (a symbolic computation,
scratch `fermi_R.py`, sympy 1.14, exact), one finds
\(\operatorname{div}a=0\), \(|a|^2=\varphi^2\),
\[
 a\cdot\Delta a=\varphi\Big(\varphi''+\frac{\kappa\varphi'}{J}-\frac{\kappa^2\varphi}{J^2}\Big),\qquad
 (\Delta a)\cdot N=-\frac{\varphi\,\kappa_s}{J^3},\qquad
 R_2(a)=-\frac{4\kappa\kappa_s\varphi^3}{J^4}.
\]
Independent hand derivation: \(\Delta a=-\operatorname{curl}\operatorname{curl}a\)
(as \(\operatorname{div}a=0\)); the scalar curl is \(\omega=\mp(\varphi'+\kappa\varphi/J)\)
and \(\Delta a=\mp\big((\partial_t\omega/J)N-(\partial_d\omega)T\big)\), which gives
the two displayed components (the overall orientation sign cancels in
\(a\cdot\Delta a\) and enters \((\Delta a)\cdot N\) consistently); then
\(\nabla|a|^2=2\varphi\varphi'N\), \(\Delta a\cdot\nabla|a|^2=-2\varphi^2\varphi'\kappa_s/J^3\),
and, since \(a\cdot\nabla=(\varphi/J)\partial_t\) and \(\varphi\) does not depend on \(t\),
\(2a\cdot\nabla(a\cdot\Delta a)=\tfrac{2\varphi^2}{J}\big(\varphi'\partial_t(\kappa/J)-\varphi\partial_t(\kappa^2/J^2)\big)
=2\varphi^2\varphi'\kappa_s/J^3-4\varphi^3\kappa\kappa_s/J^4\), using
\(\partial_t(\kappa/J)=\kappa_s/J^2\) (because \(J-\kappa d=1\)) and
\(\partial_t(\kappa^2/J^2)=2\kappa\kappa_s/J^3\). The \(\varphi'\)-terms cancel and
(3.3) follows. Consistency: for a circle \(\kappa_s=0\) and \(R_2=0\), as it must
(azimuthal fields are heat-invariant); and \(a\cdot\Delta a\) reduces to
\(\varphi(\varphi''+\varphi'/r-\varphi/r^2)\) with \(r=r_0+d\). \(\square\)

The audit re-derived (3.3) twice and independently — by hand in the orthogonal
Fermi frame, and symbolically from scratch in its own script — and confirms it
exactly. A numerical corroboration is recorded in §5.2 (agreement to
\(2\times10^{-4}\) at a test point after Richardson extrapolation in \(s\)).

**Corollary 3.5 (the "\(\le\)" direction fails; both signs along one trajectory).**
Let \(u_0\) be the elliptic swirl of Proposition 3.4 with \(\Gamma\) an ellipse
(or any non-circular smooth strictly convex curve) and \(\varphi\not\equiv0\).
Then there are \(0<s'<s''<\infty\) with
\[
 D_3\big(w(G_{s'}u_0)\big)>D_3(G_{s'}u_0)\qquad\text{and}\qquad
 D_3\big(w(G_{s''}u_0)\big)<D_3(G_{s''}u_0).
\]
Hence neither \(D_3(w)\le D_3(u)\) nor \(D_3(w)\ge D_3(u)\) holds on the class of
Schwartz solenoidal fields (equivalently, of initial data of classical
solutions), and \(D_3(u)-D_3(w)\) takes both signs along a single heat
trajectory.

*Proof.* By Proposition 3.4, \(G_su_0\notin\mathcal M\) for small \(s>0\), so
\(\Delta(G_su_0)>0=\Delta(u_0)\) (Proposition 1.2); by Lemma 3.1 and the mean
value theorem some \(s'\in(0,s)\) has \(\tfrac{d}{ds}\Delta(G_{s'}u_0)>0\), which is
the first inequality by (3.1). Since \(\Delta(G_su_0)\to0\) as \(s\to\infty\)
(Lemma 3.1), some \(s''>s\) has a negative derivative, the second. \(\square\)

Remarks. (i) *The \(L^2\) analogy is empty, not opposite.* For the quadratic
functional the minimiser over gradients of a solenoidal field is the field
itself (\(L^2\)-orthogonality), so \(\Delta_2\equiv0\); the true \(L^2\) fact
\(\|\nabla\mathbb Pz\|_2\le\|\nabla z\|_2\) for arbitrary \(z\) is a statement
about the projection of *non-minimising* representatives and has no
counterpart here. (ii) *Formal linearisation.* Near \(u_0\in\mathcal M\), with
\(u_\varepsilon=u_0+\varepsilon h\), a formal expansion gives
\(D_3(u_\varepsilon)-D_3(w_\varepsilon)=\varepsilon\langle Dj(u_0)q_1,\Delta u_0\rangle+o(\varepsilon)\)
and \(P_3-K=\varepsilon\langle Dj(u_0)q_1,\mathbb P(u_0\cdot\nabla)u_0\rangle+o(\varepsilon)\),
odd in \(h\); this is only heuristic (the minimiser is known to be
\(\tfrac12\)-Hölder in \(L^3\), `lem:quotient-stability`, not differentiable),
it is used nowhere, and Theorems 3.2/3.4 replace it. (iii) The bulk-field
numerics of §5.1 all give \(D_3(w)<D_3(u)\) by a few per cent, the same
direction that (3.2) forces *in the aggregate along a heat trajectory*, while
the \(>\) sign appears on the near-\(\mathcal M\) family of §5.2 (ratio
\(\sim10^{-5}\)). This is a loose analogy only: the §5.1 fields do not sit on a
heat trajectory, so (3.2) implies nothing about them, and nothing is claimed
about the sign on any class beyond Corollary 3.5.

## 4. Sign and control of \(P_3-K\)

**Proposition 4.1 (no sign; defect-weighted size bounds).** (a) \(u\mapsto-u\)
preserves the class and maps \((A,j(u),(u\cdot\nabla)u,\nabla p)\mapsto(-A,-j(u),(u\cdot\nabla)u,\nabla p)\),
hence \(P_3\mapsto-P_3\), \(K\mapsto-K\), \(P_3-K\mapsto-(P_3-K)\); so \(P_3-K\)
has no sign on the class unless it vanishes identically, and it does not
(§5.1 exhibits both signs; no analytic witness is needed for the negative
statement, since the sign flip alone shows that a one-sided bound
\(P_3-K\le\theta\nu D_3+\dots\) is equivalent to the two-sided one).
(b) For solenoidal \(u\in H^m\), by (1.2),
\[
 |P_3|\le C_\Delta\,\|\nabla p\|_3,\quad |K|\le C_\Delta\,\|(u\cdot\nabla)u\|_3,\quad
 |P_3-K|\le C_\Delta\,\|\mathbb P[(u\cdot\nabla)u]\|_3,\quad
 |D_3(u)-D_3(w)|\le C_\Delta\,\|\Delta u\|_3,                                \tag{4.1}
\]
\(C_\Delta:=(1+C_{\mathbb P})(3\mathcal Q)^{1/3}(6\Delta)^{1/3}\sim(a^2,\lambda^0)\).
By Lemma R1(b) the same four bounds hold with the sharper constant
\[
 C_\Delta'\ :=\ C_1\,\Delta^{1/2}\mathcal Q^{1/6}\ \sim\ (a^2,\lambda^0),
 \qquad C_\Delta'\ \le\ C\,(\Delta/\mathcal Q)^{1/6}\,C_\Delta ,             \tag{4.1$'$}
\]
i.e. (4.1) improves by the factor \((\Delta/\mathcal Q)^{1/6}\), which is the
order-correct power in the near-\(\mathcal M\) regime.
Each right factor is supercritical (\((a^2,\lambda^2)\), resp. \((a,\lambda^2)\))
and is not controlled by \(\mathcal Q\), \(\Delta\), \(D_3\) and the inputs:
(4.1)/(4.1\('\)) are exact but not a closing mechanism — a conclusion the
sharpening does not change, now with the correct power of \(\Delta\).
(c) The dissipation-controlled bounds are the audited
\(|K|\le C_*\mathcal Q^{1/3}D_3(w)\) (HF18-A (4.2)) and its pressure twin
\[
 |P_3|\ \le\ C_{**}\,\|u\|_3\,D_3(u),\qquad C_{**}=\tfrac{3}{2\sqrt2}\,S\,C_{CZ},   \tag{4.2}
\]
proof: \(|P_3|\le\int|p||u|^{1/2}\cdot|u|^{1/2}|\nabla|u||\le(\int p^2|u|)^{1/2}D_3(u)^{1/2}\);
\(\int p^2|u|\le\|p\|_3^2\|u\|_3\le C_{CZ}^2\|u\|_6^4\|u\|_3\le C_{CZ}^2\|u\|_3^2\|u\|_9^3\)
(interpolation \(\tfrac16=\tfrac14\cdot\tfrac13+\tfrac34\cdot\tfrac19\));
\(\|u\|_9^3=\|V_u\|_6^2\le S^2\|\nabla V_u\|_2^2\le\tfrac98S^2D_3(u)\), \(V_u=|u|^{1/2}u\),
by the pointwise algebra HF18-A (1.12) applied to the \(C^1\) field \(u\).
Scaling \((a^4,\lambda^2)\) on both sides ✓. (4.2) is classical in substance
(Kato's small-\(L^3\) mechanism [MO], manuscript `rem:quotient-related`) and
closes only under \(\|u\|_3\lesssim\nu\); it is recorded here because it makes
the pressure route and the quotient route exactly parallel: each is the unique
scaling-consistent size bound of its nonlinear term by its own dissipation.
(The audit verified (4.2) in full, constant included, and independently
re-derived the pointwise algebra it uses.)

**Proposition 4.2 (the scaling lattice of \(\Delta\)-weighted candidates).**
Among monomials \(\Delta^\alpha\mathcal Q^\beta D\) with \(D\) of weight
\((a^3,\lambda^2)\), the weight \((a^4,\lambda^2)\) of \(P_3-K\) forces
\(\alpha+\beta=\tfrac13\), and for \(\alpha>\alpha'\) in that family the ratio of
the two right-hand sides is \((\Delta/\mathcal Q)^{\alpha-\alpha'}\). *Proof:*
\(\Delta,\mathcal Q\sim(a^3,\lambda^0)\), \(D\sim(a^3,\lambda^2)\), so
\(3(\alpha+\beta)+3=4\); the ratio is immediate. \(\square\)

The statuses below are **not** part of the proposition; each is labelled.

(i) *The family is not totally ordered; no member is "the strongest".* By the
ratio above, larger \(\alpha\) is the stronger statement in the near-\(\mathcal M\)
regime \(\Delta/\mathcal Q\to0\) — the only regime in which such a bound has
content — and smaller \(\alpha\) is the stronger statement at the opposite end
\(\Delta/\mathcal Q\to C_{\mathbb P}^3-1\). Nothing in the scaling lattice selects
\((\alpha,\beta)=(\tfrac13,0)\). **An earlier version of this note asserted that
\(\Delta^{1/3}(D_3(u)+D_3(w))\) is "the strongest candidate" and that "no
scaling family violates" the resulting pair (4.3); the audit found both claims
unsupported, and they are withdrawn.** The selection of \((\tfrac13,0)\) was an
artefact of the lossy cube-root in (1.2), not of the structure.

(ii) *The member the defect bound actually delivers, and the recorded open
side-question.* By Lemma R1(b) and (2.5), the exponent pair the structure
supplies is \((\alpha,\beta)=(\tfrac12,-\tfrac16)\):
\[
 |P_3-K|\ \le\ C\,\Delta^{1/2}\mathcal Q^{-1/6}\big(D_3(u)+D_3(w)\big) .   \tag{4.3$'$}
\]
*Status: OPEN, not proved, unrefuted by every family tried here.* It survives
the two probes of the earlier version — near-\(\mathcal M\): \(|P_3-K|\sim\varepsilon\)
against \(\Delta^{1/2}\sim\varepsilon\), i.e. order-matched, hence consistent but
not a margin; high-frequency \(u_0+\varepsilon h_k\):
\(\varepsilon+\varepsilon^2k\) against \(\varepsilon(1+\varepsilon^2k^2)\), which
holds for all \(k\) by AM–GM — and it survives the HF18-B §2.3 witness family of
(iii) below (\(\delta^{3/2}\) against \(\delta^{1/2}\)). No claim is made about
families not tried. (4.3\('\)) replaces the earlier (4.3)-first as the recorded
open side-question; the earlier (4.3)-first is likewise OPEN and is superseded,
not refuted.

(iii) *The \(|D_3(u)-D_3(w)|\) analogue: closed-negative, pending one bounded
computation.* The earlier version also asserted
\(|D_3(u)-D_3(w)|\le C(\Delta/\mathcal Q)^{1/3}(D_3(u)+D_3(w))\) as untouched by
any scaling family. It was never probed, and the audit's scaling computation on
the HF18-B §2.3 witness family refutes it. Take \(w_\delta=w_0+w_1\) of
`hf18-divergence-speed-link.md` §2.3 Prop. 2.2: \(w_0=|A_0|^{-1/2}A_0\) the
azimuthal bulk (\(w_0\in\mathcal M\), \(q_0=0\), \(\mathbb Pw_0=w_0\)) and
\(w_1=|A_1|^{-1/2}A_1=\delta\,G(kx)\chi((x-x_0)/R)\) the oscillatory piece on a
disjoint ball, with \(R^3=\delta^{-2}\), \(k=\delta^{-1/2}\), and put
\(u_\delta:=\mathbb Pw_\delta\); HF18-B (1.6) gives \(w(u_\delta)=w_\delta\) and
\(q(u_\delta)=(I-\mathbb P)w_1\). Then \(\mathcal Q(u_\delta)\asymp1\),
\(\Delta(u_\delta)\asymp\delta\) (by (R1a) and (1.1)), and
\(D_3(u_\delta),D_3(w_\delta)\asymp1\), so the right side
\((\Delta/\mathcal Q)^{1/3}(D_3(u)+D_3(w))\sim\delta^{1/3}\to0\), while the left
side tends to \(\langle\mathbb PG\rangle_{D_3}-\langle G\rangle_{D_3}\), a
difference of two cell functionals of the fixed profile \(G\) and its cell Leray
projection, which is nonzero unless \(G\) is exceptional (\(w_1\) is not
solenoidal, and \((I-\mathbb P)w_1\) has amplitude comparable to \(w_1\), so
\(\mathbb PG\ne G\) at leading order). The same family kills every version of
this second inequality carrying a positive power of \(\Delta\), including the
\((\Delta/\mathcal Q)^{1/2}\) member.
*Status: CLOSED-NEGATIVE (refutation candidate), not OPEN.* This is a scaling
computation on an audited family, **not a completed proof**: it assumes the two
cell functionals differ, which is generic and consistent with §5.1's twelve
fields (\(D_3(w)/D_3(u)\in[0.978,0.994]\), bounded away from \(1\)), but was not
evaluated. **Reopening condition (the decisive bounded test):** evaluate, on one
periodic cell of the HF18-B oscillatory profile
\(F=((2+\cos y_1)\cos y_2,\ \sin y_1\sin y_2,\ 0)\), \(G=|F|^{-1/2}F\), the two
cell integrals \(\mathcal D[G]=\int_{\rm cell}|G|(|\nabla G|^2+|\nabla|G||^2)\)
and \(\mathcal D[\mathbb PG]\) with \(\mathbb P\) the cell Leray projection. If
\(\mathcal D[\mathbb PG]\ne\mathcal D[G]\), the inequality is FALSE and closes
negatively; only if \(\mathcal D\) were \(\mathbb P\)-invariant for every
admissible profile does it return to OPEN.
*Why the first inequality is untouched by this family:* on the oscillation
region \(|A-j(u)|\sim|w||q|\sim\delta^2\) and \(|(u\cdot\nabla)u|\sim\delta^2k\),
so \(|P_3-K|\lesssim\delta^4kR^3=\delta^{3/2}\), against \(\delta^{1/3}\) (old
form) resp. \(\delta^{1/2}\) (4.3\('\)); the bulk contributes nothing.

(iv) *Why (4.3\('\)) is not proved.* A dissipation-controlled bound must move one
derivative onto the defect: \(P_3-K=-\langle\partial_i(A-j(u)),\mathbb P(u_iu)\rangle\)
(HF18-A (F5) and its \(j(u)\) analogue), and then
\(|P_3-K|\le\|\nabla(A-j(u))\|_{3/2}\,C\|u\|_6^2\le C\|u\|_3(D_3(u)+D_3(w))\), which
loses the \(\Delta\)-factor entirely: no pointwise bound
\(|\nabla(A-j(u))|\lesssim|q|(\dots)\) is available without a bound on \(\nabla q\),
i.e. without (H1)-type regularity of the minimiser (HF18-A NON-CLAIMS). Keeping
the defect underived, as in (4.1)/(4.1\('\)), puts the derivative on \(u\), which
is supercritical. Neither of these two routes yields (4.3\('\)); nothing is
claimed about routes not examined.

(v) *Why it could not close even if true.* Suppose, counterfactually for the
second half — §4.2(iii) records it as closed-negative — that both (4.3\('\))
and its \(|D_3(u)-D_3(w)|\) analogue held. Inserting them into (2.3):
\(|\Delta'|\le C(\nu+\mathcal Q^{1/3})\mathcal Q^{-1/6}\Delta^{1/2}(D_3(u)+D_3(w))\),
hence \((\Delta^{1/2})'\le\tfrac12C(\nu+\mathcal Q^{1/3})\mathcal Q^{-1/6}(D_3(u)+D_3(w))\).
The \(\nu\)-part of the coefficient carries \(\nu\mathcal Q^{-1/6}\), which is
**not** bounded a priori (no lower bound on \(\mathcal Q\) is available) and must
be carried through Grönwall rather than discarded; the \(\nu\)-free part alone
integrates to
\[
 \Delta(\tau)^{1/2}\le\Delta(0)^{1/2}+C\int_0^\tau\big(D_3(u)+D_3(w)\big)dt
 \qquad\text{(the \(\nu\)-free part only),}
\]
a bound of \(\Delta\) by the spacetime dissipation, which is exactly the
quantity HIGH-STRAIN/HIGH-PRESSURE must control (\(\nu\int D_3\ge c\int\|u\|_9^3\)
is the \(L^3_tL^9_x\) Serrin class, HF18-A §4 item 3). The same conclusion holds
for any member of the lattice of Proposition 4.2, and more generally for any
bound that controls \(\Delta'\) by the dissipation, since such a bound Grönwalls
into a bound of \(\Delta\) by \(\int(D_3(u)+D_3(w))\,dt\). So a \(\Delta\)-weighted
refinement, true or not, changes nothing at the quantifiers of the gap; this
is the packet's forbidden inference "another equivalent identity alone
discharges the gap", displayed concretely. This item is unaffected by the
withdrawal of (i) and by the outcome of (iii).

Remark (constant speed on a set). If \(|w|\) is constant on an open set \(U\),
then HF18-B Prop. 1.1 gives \(\sigma=0\), hence \(\operatorname{div}w=0\) and
\(q=\nabla\phi\) with \(\phi\) harmonic on \(U\); the local contribution of \(U\)
to \(D_3(u)-D_3(w)=\langle A-j(u),\Delta u\rangle\) has no sign either (the
defect \(A-j(u)\) is not aligned with \(\Delta u\)). No use was found.

## 5. Bounded numerical evidence (periodic proxy for the static problem; never for the evolution)

### 5.1 Three-dimensional torus, explicit minimisers with \(q\ne0\)

On \([0,2\pi)^3\) with \(N^3\) spectral collocation, take a smooth solenoidal
\(A\) with \(|A|\ge c_0>0\) (either \(A=(a(y,z),b(x,z),c(x,y))\) or
\(A=\operatorname{curl}\Psi+\text{const}\), random low modes), \(w=|A|^{-1/2}A\)
(smooth, in \(\mathcal M\) exactly, HF18-B Prop. 1.4 on the torus),
\(u=\mathbb Pw\), \(q=w-u\), \(p=R_iR_j(u_iu_j)\). Scratch `torus_probe.py`.
Twelve resolved cases (\(\min|A|\ge0.79\), \(\max|\operatorname{div}u|\le10^{-5}\)
except two \(\operatorname{curl}\)-cases at \(5\times10^{-5}\) and \(6\times10^{-4}\)), \(N=48\) and \(64\),
\(\|q\|_3/\|w\|_3\in[0.031,0.060]\):

| identity / inequality | outcome |
|---|---|
| \(D_3(w)=\int\nabla A:\nabla u=-\langle A,\Delta u\rangle=\int(|w||\nabla w|^2+|w||\nabla|w||^2)\) | agree to \(10^{-6}\) rel. |
| \(D_3(u)=\int\nabla j(u):\nabla u=-\langle j(u),\Delta u\rangle=\) weighted form | agree to \(10^{-6}\) rel. |
| \(P_3=\int p\,u\cdot\nabla|u|=-\langle j(u),\nabla p\rangle=\langle A-j(u),\nabla p\rangle\) | agree to 6 digits |
| \(K=-\int q\cdot((u\cdot\nabla)A)=-\langle A,(u\cdot\nabla)u\rangle=-\langle A-j(u),(u\cdot\nabla)u\rangle\) | agree to 6 digits |
| \(P_3-K=\langle A-j(u),\mathbb P[(u\cdot\nabla)u]\rangle\) | agree to 6 digits |
| \(\tfrac16\|q\|_3^3\le\Delta\le(\|w\|_3+\|u\|_3)\|q\|_3^2\) (1.1) | holds, e.g. \(0.0068\le0.79\le1.36\) |
| \(\|A-j(u)\|_{3/2}\le(\|w\|_3+\|u\|_3)\|q\|_3\) | holds, e.g. \(5.00\le7.70\) |
| sign of \(D_3(u)-D_3(w)\) | \(>0\) in all 12; \(D_3(w)/D_3(u)\in[0.978,0.994]\) |
| sign of \(P_3-K\) | \(+\) in 5 cases (\(+0.0065\) to \(+0.106\)), \(-\) in 7 (\(-0.025\) to \(-0.62\)) |
| \(|P_3-K|/(\mathcal Q^{1/3}D_3(w))\), \(|P_3-K|/(\Delta^{1/3}(D_3(u)+D_3(w)))\) | \(\le10^{-4}\) (smooth low-mode fields; not a saturation test) |

Two recording corrections from the audit. (a) The upper bound printed in the
sixth row was evaluated as \((\|w\|_3+\|q\|_3)\|q\|_3^2\), not as the
\((\|w\|_3+\|u\|_3)\|q\|_3^2\) of (1.1); since \(\|q\|_3\ll\|u\|_3\) here, the
evaluated quantity is the *smaller* one, so the displayed check holds a fortiori
for (1.1) as stated. No number is restated. (b) The last row probes the
monomial \((\alpha,\beta)=(\tfrac13,0)\) that §4.2(i) withdraws; it is retained
as raw data only. The corresponding ratio for (4.3\('\)) was not computed and no
value for it is asserted.

Declared range: finite resolution, periodic proxy, twelve fields; supports
the identities of §2 and the "both signs" statement for \(P_3-K\); proves
nothing about the gap.

### 5.2 Two-dimensional elliptic swirl under heat flow (corroboration of (3.3) and of Corollary 3.5)

Ellipse with semi-axes \(1.5,\,0.9\) in \([0,2\pi)^2\), \(N=512\), \(d\) by nearest
point plus Newton (projection residual \(4\times10^{-15}\)), \(\varphi\) a
Gevrey bump on \(d\in(0.3,1.2)\), \(a=\nabla^\perp\Psi(d)\) (\(=-\varphi T\) in the
orientation of Proposition 3.4, so the cubic \(R\) flips sign). Scratch
`ellipse2d.py`, `ellipse2d_R.py`. Results:

- membership: \(\max|a\cdot\nabla|a|^2|/\max(|a||\nabla|a|^2|)=1.1\times10^{-4}\);
- (3.3): Richardson limit of \(h(s,x_0)/s\) (\(s=10^{-4},2\times10^{-4}\)) is
  \(-0.037086\) against the formula \(+4\kappa\kappa_s\varphi^3/(1+\kappa d)^4=-0.037079\)
  at the test point (\(2\times10^{-4}\) relative); direct evaluation of \(R\) on
  \(G_{10^{-4}}a\) agrees with the formula to \(2.2\%\) in \(L^2\) over the bulk of
  the support (fourth derivatives of the bump at this resolution);
- \(\Delta(G_su_0)\) with the minimiser computed by preconditioned L-BFGS
  (Euler–Lagrange residual \(3\times10^{-5}\)): \(\Delta=9\times10^{-14}\) at \(s=0\),
  then \(1.27\times10^{-8},\ 8.40\times10^{-8},\ 3.10\times10^{-7}\) at
  \(s=3\times10^{-3},10^{-2},3\times10^{-2}\); \(\tfrac16\|q\|_3^3\le\Delta\) holds;
- \(D_3(w(v_s))-D_3(v_s)=+7.3\times10^{-6},\ +1.15\times10^{-5},\ +1.10\times10^{-5}\)
  at the same \(s\) (noise level \(3\times10^{-8}\) at \(s=0\)); the finite-difference
  slopes of \(\Delta(G_su_0)\), \(1.0\times10^{-5}\) and \(1.1\times10^{-5}\), match
  these values, an independent check of (3.1);
- so on this family \(D_3(w)>D_3(v)\), the opposite sign to every bulk field of
  §5.1, as Corollary 3.5 predicts.

Declared range: finite resolution, planar periodic proxy, one curve; the
theorem is Proposition 3.4/Corollary 3.5, the computation only corroborates it.
The audit did not re-run these numerics; they are bounded evidence, never proof.

## 6. Self-check against the packet falsifiers

- *Norm to be controlled:* the only conclusions asserted are identities
  ((2.1)–(2.6), (3.1)–(3.3)), the two-sided bounds (1.1)–(1.2) and (R1a)–(R1b),
  the size bounds (4.1)/(4.1\('\))–(4.2) with their uncontrolled factors
  displayed, the scaling lattice of Proposition 4.2, and two refutations;
  \(\sup_t\|u\|_3\), \(\|\nabla u\|_\infty\), \(\|u\|_9\) are used nowhere to prove
  anything.
- *Scaling:* every displayed inequality was checked in §0 units. The lattice
  \(\alpha+\beta=\tfrac13\) is a one-parameter family that is **not** totally
  ordered, so no member is "the unique scaling-consistent candidate"; the
  earlier claim to that effect is withdrawn (§4.2(i)). The member the defect
  bound delivers is (4.3\('\)), left OPEN; the \(|D_3(u)-D_3(w)|\) analogue is
  closed-negative pending one bounded cell computation (§4.2(iii)).
- *Hidden smallness:* (4.2) closes only for \(\|u\|_3\lesssim\nu\), stated. The
  \(\nu\mathcal Q^{-1/6}\) coefficient in §4.2(v) is unbounded a priori and is
  displayed as frozen rather than absorbed.
- *Differentiating the merely-\(L^3\) minimiser:* never; §3 uses only the
  Fréchet derivative of \(\mathcal Q\) along \(C^1\) curves in \(L^3\) and the
  audited HF18-A identification \(D_{\mathcal Q}=D_3(w)\); the linearisation of
  Remark 3(ii) is labelled heuristic and is not used.
- *Instantaneous promoted to time-integrated:* (3.2) is integrated along the
  heat flow, not the Navier–Stokes flow, and says so; (2.3) is instantaneous.
- *Unsupported negative claims:* the earlier "no scaling family violates (4.3)"
  quantified over families never probed and is withdrawn, not patched; nothing
  in this note now asserts non-existence over an unexamined class.
- *Forced/periodic/hyperdissipative variants:* none in any theorem; the
  periodic box appears only in the bounded numerics for the static problem.
- *p-Laplace theorems outside hypotheses:* none used.
- *Forbidden inferences:* no size bound in \(\mathcal Q,D_3\) is claimed to close;
  energy is not claimed to control anything critical; §4.2(v) shows explicitly
  that the equivalent \(\Delta\)-identity discharges nothing.

## 7. Frontier record

**MODE / RESULT:** DISCOVER. Exact evolution of the difference functional
\(\Delta=X/3-\mathcal Q\) (Theorem 2.2) with every term a pairing of the Hodge
defect \(A-j(u)\); two-sided control of \(\Delta\) by \(\|q\|_3\) (Prop. 1.2)
and the sharp defect control of Lemma R1; the sign question for
\(D_3(u)-D_3(w)\) settled negatively in both directions by the heat-flow
identity (3.2) and by the non-invariance of \(\mathcal M\) under the heat
semigroup, proved through the closed-form first-order defect (3.3) of the
elliptic swirl; \(P_3-K\) has no sign; \(\Delta\)-weighted control is exhibited
as either supercritical (4.1)/(4.1\('\)) or, in the monomial lattice, OPEN and
non-closing (4.3\('\)) with the \(|D_3(u)-D_3(w)|\) half closed-negative.
Two exact obstructions; **no producer found among the bounds surveyed** (a
survey result, not a non-existence theorem).

**AUDIT STATUS:** REPAIR (`hf19-review-difference-functional.md`, 2026-09-06),
repairs applied by the controller on 2026-09-06. First bad bridge: the
withdrawn selection of (4.3) as "the strongest candidate" and the withdrawn
"no scaling family violates (4.3)" in §4.2 — a negative section that
discharges nothing, so nothing downstream depended on it. The audit
reconstructed §§1–3 and §4.1 independently, re-derived (3.3) twice from
scratch (by hand and symbolically) in exact agreement, verified (4.2) with its
constant and the pointwise algebra behind it, and supplied Lemma R1.

**CLAIM AND SCOPE:** Lemma 1.1, Prop. 1.2 and (R1a) for every \(u\in L^3\),
(R1b) for solenoidal \(u\in L^3\) (solenoidality is used wherever \(\mathbb P\)
appears); Lemma 2.1, Remark 2.1\('\), Theorem 2.2, Cor. 2.3 on every compact
classical interval of the manuscript's branch; Lemma 3.1, Theorem 3.2,
Prop. 3.3, Cor. 3.5 for solenoidal \(u\in H^m\), \(m\ge4\) (Schwartz where
stated); Prop. 3.4 for the explicit family; Prop. 4.1(b),(c) and §4.2(iv),(v)
at every fixed time; Proposition 4.2 (the lattice constraint and the ratio) is
proved; §4.2(i) is a withdrawal, §4.2(ii) is OPEN, §4.2(iii) is
closed-negative pending one bounded cell computation and is explicitly not
proof-grade. HF18-A Theorem 2 (\(D_{\mathcal Q}=D_3(w)\)) is the one audited
input beyond the manuscript.

**EVIDENCE:** pointwise cubic inequalities of `lem:cubic-pointwise`
integrated (including the identity half of `eq:cp-monotone`, which carries
(R1a)); the Euler–Lagrange orthogonality \(\langle A,q\rangle=0\); the
Fréchet chain rule of `lem:quotient-chainrule` applied to \(F\) and along the
heat semigroup (`lem:heat-generator`); \(L^3\) decay of the heat kernel;
the Fermi-chart computation (3.3), done symbolically (sympy, exact), by hand
via \(\Delta a=-\operatorname{curl}\operatorname{curl}a\), corroborated
numerically to \(2\times10^{-4}\), and re-derived independently twice by the
audit; twelve resolved 3D torus minimisers and one 2D heat-flow experiment,
declared as bounded evidence and not re-run by the audit.

**FIRST GAP:** unchanged. The implication "\(\Delta'+\nu(D_3(u)-D_3(w))=P_3-K\)
admits an input-only spacetime bound \(\int_0^\tau(P_3-K)\,dt\le\theta\nu\int_0^\tau(D_3(u)+D_3(w))dt+M\int_0^\tau\Delta\,dt+A_{\rm input}\)"
is unsupported; and it would not suffice, because \(\Delta\) is not coercive
on \(u\): a bound on \(\Delta\) must be paired with a bound on \(\mathcal Q\) or
\(X\), which is the original gap. The first unsupported step in the \(\Delta\)
route is therefore the same critical absorption as in HF17/HF18, in the
coordinates (2.5); neither route examined in §4.2(iv) yields a
dissipation-controlled bound carrying a positive power of \(\Delta\), and any
such bound would integrate to the missing \(\int D_3\,dt\) anyway (§4.2(v)).

**SURVIVING CONDITIONAL SUFFIX:** the HF17/HF18 suffix, unchanged: an
input-only spacetime bound for \(K\) (or for \(P_3\), or for \(P_3-K\) together
with one for \(K\)) gives \(\mathcal Q\), hence \(\|u\|_3\) and \(L^3_tL^9_x\), hence
continuation by ESS. New, unconditional: Theorem 2.2 and Cor. 2.3; Lemma R1;
Prop. 4.1(a),(b),(c); and, off the Navier–Stokes flow, Lemma 3.1, the
heat-flow identity (3.2) \(\int_0^\infty(D_3(G_su)-D_3(w(G_su)))ds=\Delta(u)\),
Props. 3.3–3.4 and Cor. 3.5. Manuscript-grade by-product recorded for
integration elsewhere: Lemma 2.1's upgrade of `prop:pressure`(ii) to
\(X\in C^1([0,T])\) with \(D_3,P_3\) continuous.

**NON-CLAIMS:** no sign, bound or absorption for \(K\), \(P_3\), \(P_3-K\) or
\(D_3(u)-D_3(w)\) beyond (4.1)/(4.1\('\))–(4.2), Lemma R1 and the audited (4.2)
of HF18-A; no proof of (4.3\('\)) or of the withdrawn (4.3)-first; **no
proof-grade refutation** of the \(|D_3(u)-D_3(w)|\) inequality — §4.2(iii) is a
scaling computation on an audited family, contingent on two cell functionals of
\(G\) and \(\mathbb PG\) differing, i.e. a refutation candidate with a decisive
bounded test; no claim that (4.3\('\)) is optimal in the lattice; no claim that
no \(\Delta\)-weighted producer exists — §4.2 is a survey of the candidates
examined, not a non-existence theorem; no regularity of \(w\) or \(q\) ((H1)
remains a hypothesis); no invariance or non-invariance of \(\mathcal M\) under
the Navier–Stokes flow (only under the heat semigroup); no differentiability of
the minimiser map; no continuation criterion, no HIGH-STRAIN or HIGH-PRESSURE
theorem, no NS-R3 result; no novelty claim for the defect decomposition
(2.4)–(2.5) or for Lemma R1. The numerics are bounded evidence at finite
resolution on periodic proxies of the static problem, never proof.

**NEXT DISTINCT ACTION:** The difference route is retired as a producer, on
the two exact facts that \(\Delta\) vanishes on \(\mathcal M\ne\{0\}\) — so no
bound on \(\Delta\) alone bounds any norm of \(u\) — and that \(\Delta\) is
redundant given \(\mathcal Q\) (Remark 2(ii)); **no producer was found among
the bounds surveyed**, which is a survey result, not a non-existence theorem.
Three distinct actions remain from this wave. (1) FALSIFY on the
Navier–Stokes side what §3 did on the heat side: compute, for the elliptic
swirl \(u_0\), the Euler contribution
\(-\mathbb P(u_0\cdot\nabla)u_0\cdot\nabla|u_0|^2-2u_0\cdot\nabla(u_0\cdot\mathbb P(u_0\cdot\nabla)u_0)\)
to \(\partial_t\operatorname{div}(|u|u)\) at \(t=0\); if it is nonzero and not
proportional to (3.3), then \(\mathcal M\) is not Navier–Stokes invariant for
any \(\nu\), and the sign of \(P_3-K\) at \(t=0^+\) on this family is computable
in closed form, giving the first analytic family on which \(K\ne0\) with
\(\|q\|_3/\|w\|_3\) controlled; that family must then be run against
(4.3\('\)) before any promotion. (2) Settle §4.2(iii) with the one bounded cell
computation \(\mathcal D[\mathbb PG]\) versus \(\mathcal D[G]\) specified there,
which either closes the \(|D_3(u)-D_3(w)|\) side-question negatively or returns
it to OPEN. (3) Record the Lemma 2.1 upgrade of `prop:pressure`(ii) in the
manuscript; it is a manuscript-grade improvement obtained from the
manuscript's own package.

## 8. Sources and scratch

Manuscript `main.tex` at the working-tree revision of 2026-09-05, section
`sec:quotient` and `def:D3P3`, `prop:pressure` [DI]. `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, `hf18-hodge-regularity.md`,
`hf18-review-hodge-regularity.md`, `hf18-divergence-speed-link.md`,
`hf18-review-divergence-speed-link.md`, `hf18-review-divergence-speed-link-r2.md`
[DI, all in full]. The audit of this note, `hf19-review-difference-functional.md`
(REPAIR, 2026-09-06), read in full [DI]; it freezes this note at sha256
`c88f90b9843a06dffbccbc47690c200175e5466857f4688070c0c8be09dca5d5` (629 lines),
repository `1014e7e3c33af4a341a5f46156a22b808170257b`, manuscript `39ccb66`,
and supplies Lemma R1 and the replacement text used in §4.2. Standard facts used
without citation: uniqueness of the nearest point on a compact convex set;
Sobolev on \(\mathbb R^3\); \(L^p\)-boundedness of \(R_iR_j\); Gaussian kernel
norms. Kato, Math. Z. 187 (1984) [MO], for the classical status of (4.2).
Scratch scripts (session scratchpad, not part of the repository):
`fermi_R.py` (sympy derivation of (3.3)), `torus_probe.py` (§5.1),
`ellipse2d.py`, `ellipse2d_R.py` (§5.2).
