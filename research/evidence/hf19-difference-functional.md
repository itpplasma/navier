# HF19-D: the difference functional \(\Delta=X/3-\mathcal Q\), its exact evolution, and the sign structure of \(D_3(u)-D_3(w)\)

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
\(\|A-j(u)\|_{3/2}\le(\|w\|_3+\|u\|_3)\|q\|_3\). The sign question is settled
negatively in both directions by two rigorous heat-flow arguments that never
differentiate the minimizer: (i) for every smooth solenoidal \(u\notin\mathcal M\),
\(\int_0^\infty\big(D_3(G_su)-D_3(w(G_su))\big)\,ds=\Delta(u)>0\), so
\(D_3(w)\ge D_3(u)\) fails on a set of positive measure along every such heat
trajectory; (ii) \(D_3(w)\le D_3(u)\) on the class would force \(\mathcal M\) to be
invariant under the heat semigroup, and it is not: for the "elliptic swirl"
\(u_0=f(x_3)\,\varphi(d)\,\nabla^\perp d\) (\(d\) the distance to a non-circular
convex curve) one computes in closed form
\(\partial_s\big|_{s=0}\,\operatorname{div}(|G_su_0|G_su_0)=-4\kappa\kappa_s\varphi^3/(1+\kappa d)^4\ne0\).
Hence \(D_3(u)-D_3(w)\) has no sign, and \(P_3-K\) has none either. Every
\(\Delta\)-weighted bound of \(P_3-K\) or \(D_3(u)-D_3(w)\) that is
dissipation-controlled would integrate to a bound of \(\Delta\) by
\(\int(D_3(u)+D_3(w))\,dt\), the very quantity the gap is about; the difference
functional therefore supplies no coercive mechanism and no new producer.
HIGH-STRAIN and HIGH-PRESSURE remain open; NS-R3 remains open.

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
of \(\mathcal M\), which contains every axisymmetric swirl and every shear
flow). This already excludes \(\Delta\) as a stand-alone Lyapunov functional.

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
This is the pointwise form of `prop:pressure`(ii), which the manuscript states
in integrated form; the \(H^m\) regularity of (R1) makes it pointwise. \(\square\)

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

A numerical corroboration of (3.3) is recorded in §5.2 (agreement to
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
and Theorems 3.2/3.4 replace it. (iii) The formal expansion also shows why
the bulk-field numerics of §5.1 all give \(D_3(w)<D_3(u)\) by a few per cent:
that is the sign that (3.2) forces on average, and the \(>\) sign is confined
to a transient near \(\mathcal M\) (§5.2, ratio \(\sim10^{-5}\)).

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
Each right factor is supercritical (\((a^2,\lambda^2)\), resp. \((a,\lambda^2)\))
and is not controlled by \(\mathcal Q\), \(\Delta\), \(D_3\) and the inputs:
(4.1) is exact but not a closing mechanism.
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

**Proposition 4.2 (what \(\Delta\)-control could and could not do).** By scaling,
the only monomials \(\Delta^\alpha\mathcal Q^\beta D\) with the weight
\((a^4,\lambda^2)\) of \(P_3-K\) have \(\alpha+\beta=\tfrac13\); the strongest
candidate is
\[
 |P_3-K|\ \le\ C\,\Delta^{1/3}\big(D_3(u)+D_3(w)\big),\qquad
 |D_3(u)-D_3(w)|\ \le\ C\,(\Delta/\mathcal Q)^{1/3}\big(D_3(u)+D_3(w)\big).       \tag{4.3}
\]
(i) *Status: OPEN, not refuted.* The near-\(\mathcal M\) heuristic gives
\(|P_3-K|\sim\varepsilon\) against \(\Delta^{1/3}\sim\varepsilon^{2/3}\), and high-frequency
perturbations \(u_0+\varepsilon h_k\) give \(|P_3-K|\lesssim\varepsilon+\varepsilon^2k\) against
\(\varepsilon^{2/3}(1+\varepsilon^2k^2)\); no scaling family violates (4.3), and the
probe of §5.1 has ratios \(\le10^{-4}\).
(ii) *Why it is not proved.* A dissipation-controlled bound must move one
derivative onto the defect: \(P_3-K=-\langle\partial_i(A-j(u)),\mathbb P(u_iu)\rangle\)
(HF18-A (F5) and its \(j(u)\) analogue), and then
\(|P_3-K|\le\|\nabla(A-j(u))\|_{3/2}\,C\|u\|_6^2\le C\|u\|_3(D_3(u)+D_3(w))\), which
loses the factor \(\Delta^{1/3}\): no pointwise bound
\(|\nabla(A-j(u))|\lesssim|q|(\dots)\) is available without a bound on \(\nabla q\),
i.e. without (H1)-type regularity of the minimiser (HF18-A NON-CLAIMS). Keeping
the defect underived, as in (4.1), puts the derivative on \(u\), which is
supercritical. Neither route yields (4.3).
(iii) *Why it could not close even if true.* Inserting (4.3) into (2.3):
\(|\Delta'|\le C\big(\nu(\Delta/\mathcal Q)^{1/3}+\Delta^{1/3}\big)(D_3(u)+D_3(w))\), hence
\((\Delta^{2/3})'\le\tfrac23C\,(1+\nu\mathcal Q^{-1/3})(D_3(u)+D_3(w))\). The \(\nu\)-term
carries \(\mathcal Q^{-1/3}\), large only where \(\mathcal Q\) is small (the harmless
regime), and the \(\nu\)-free part integrates only to
\[
 \Delta(\tau)^{2/3}\le\Delta(0)^{2/3}+C\int_0^\tau\big(D_3(u)+D_3(w)\big)dt ,
\]
a bound of \(\Delta\) by the spacetime dissipation, which is exactly the
quantity HIGH-STRAIN/HIGH-PRESSURE must control (\(\nu\int D_3\ge c\int\|u\|_9^3\)
is the \(L^3_tL^9_x\) Serrin class, HF18-A §4 item 3). So a \(\Delta\)-weighted
refinement, true or not, changes nothing at the quantifiers of the gap; this
is the packet's forbidden inference "another equivalent identity alone
discharges the gap", displayed concretely.

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
| \(\tfrac16\|q\|_3^3\le\Delta\le(\|w\|_3+\|q\|_3)\|q\|_3^2\) | holds, e.g. \(0.0068\le0.79\le1.36\) |
| \(\|A-j(u)\|_{3/2}\le(\|w\|_3+\|u\|_3)\|q\|_3\) | holds, e.g. \(5.00\le7.70\) |
| sign of \(D_3(u)-D_3(w)\) | \(>0\) in all 12; \(D_3(w)/D_3(u)\in[0.978,0.994]\) |
| sign of \(P_3-K\) | \(+\) in 5 cases (\(+0.0065\) to \(+0.106\)), \(-\) in 7 (\(-0.025\) to \(-0.62\)) |
| \(|P_3-K|/(\mathcal Q^{1/3}D_3(w))\), \(|P_3-K|/(\Delta^{1/3}(D_3(u)+D_3(w)))\) | \(\le10^{-4}\) (smooth low-mode fields; not a saturation test) |

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

## 6. Self-check against the packet falsifiers

- *Norm to be controlled:* the only conclusions asserted are identities
  ((2.1)–(2.6), (3.1)–(3.3)), the two-sided bounds (1.1)–(1.2), the size
  bounds (4.1)–(4.2) with their uncontrolled factors displayed, and two
  refutations; \(\sup_t\|u\|_3\), \(\|\nabla u\|_\infty\), \(\|u\|_9\) are used
  nowhere to prove anything.
- *Scaling:* every displayed inequality was checked in §0 units; (4.3) is
  stated as the unique scaling-consistent candidate and left OPEN.
- *Hidden smallness:* (4.2) closes only for \(\|u\|_3\lesssim\nu\), stated.
- *Differentiating the merely-\(L^3\) minimiser:* never; §3 uses only the
  Fréchet derivative of \(\mathcal Q\) along \(C^1\) curves in \(L^3\) and the
  audited HF18-A identification \(D_{\mathcal Q}=D_3(w)\); the linearisation of
  Remark 3(ii) is labelled heuristic and is not used.
- *Instantaneous promoted to time-integrated:* (3.2) is integrated along the
  heat flow, not the Navier–Stokes flow, and says so; (2.3) is instantaneous.
- *Forced/periodic/hyperdissipative variants:* none in any theorem; the
  periodic box appears only in the bounded numerics for the static problem.
- *p-Laplace theorems outside hypotheses:* none used.
- *Forbidden inferences:* no size bound in \(\mathcal Q,D_3\) is claimed to close;
  energy is not claimed to control anything critical; Proposition 4.2(iii)
  shows explicitly that the equivalent \(\Delta\)-identity discharges nothing.

## 7. Frontier record

**MODE / RESULT:** DISCOVER. Exact evolution of the difference functional
\(\Delta=X/3-\mathcal Q\) (Theorem 2.2) with every term a pairing of the Hodge
defect \(A-j(u)\); two-sided control of \(\Delta\) by \(\|q\|_3\) (Prop. 1.2);
the sign question for \(D_3(u)-D_3(w)\) settled negatively in both directions
by the heat-flow identity (3.2) and by the non-invariance of \(\mathcal M\)
under the heat semigroup, proved through the closed-form first-order defect
(3.3) of the elliptic swirl; \(P_3-K\) has no sign; \(\Delta\)-weighted control
is exhibited as either supercritical (4.1) or OPEN and non-closing (4.3).
Two exact obstructions, no new producer.

**CLAIM AND SCOPE:** Lemma 1.1, Prop. 1.2 for every \(u\in L^3\)
(solenoidal where \(\mathbb P\) is used); Lemma 2.1, Theorem 2.2, Cor. 2.3 on
every compact classical interval of the manuscript's branch; Lemma 3.1,
Theorem 3.2, Prop. 3.3, Cor. 3.5 for solenoidal \(u\in H^m\), \(m\ge4\)
(Schwartz where stated); Prop. 3.4 for the explicit family; Prop. 4.1(b),(c)
and Prop. 4.2(ii),(iii) at every fixed time; Prop. 4.2(i) is OPEN.
HF18-A Theorem 2 (\(D_{\mathcal Q}=D_3(w)\)) is the one audited input beyond
the manuscript.

**EVIDENCE:** pointwise cubic inequalities of `lem:cubic-pointwise`
integrated; the Euler–Lagrange orthogonality \(\langle A,q\rangle=0\); the
Fréchet chain rule of `lem:quotient-chainrule` applied to \(F\) and along the
heat semigroup (`lem:heat-generator`); \(L^3\) decay of the heat kernel;
the Fermi-chart computation (3.3), done symbolically (sympy, exact), by hand
via \(\Delta a=-\operatorname{curl}\operatorname{curl}a\), and corroborated
numerically to \(2\times10^{-4}\); twelve resolved 3D torus minimisers and one
2D heat-flow experiment, declared as bounded evidence.

**FIRST GAP:** unchanged. The implication "\(\Delta'+\nu(D_3(u)-D_3(w))=P_3-K\)
admits an input-only spacetime bound \(\int_0^\tau(P_3-K)\,dt\le\theta\nu\int_0^\tau(D_3(u)+D_3(w))dt+M\int_0^\tau\Delta\,dt+A_{\rm input}\)"
is unsupported; and it would not suffice, because \(\Delta\) is not coercive
on \(u\): a bound on \(\Delta\) must be paired with a bound on \(\mathcal Q\) or
\(X\), which is the original gap. The first unsupported step in the \(\Delta\)
route is therefore the same critical absorption as in HF17/HF18, in the
coordinates (2.5); no dissipation-controlled bound with a \(\Delta^{1/3}\)
factor is available (Prop. 4.2(ii)), and one would integrate to the missing
\(\int D_3\,dt\) anyway (Prop. 4.2(iii)).

**SURVIVING CONDITIONAL SUFFIX:** the HF17/HF18 suffix, unchanged: an
input-only spacetime bound for \(K\) (or for \(P_3\), or for \(P_3-K\) together
with one for \(K\)) gives \(\mathcal Q\), hence \(\|u\|_3\) and \(L^3_tL^9_x\), hence
continuation by ESS. New, unconditional, but off the Navier–Stokes flow: the
heat-flow identity (3.2), \(\int_0^\infty(D_3(G_su)-D_3(w(G_su)))ds=\Delta(u)\).

**NON-CLAIMS:** no sign, bound or absorption for \(K\), \(P_3\), \(P_3-K\) or
\(D_3(u)-D_3(w)\) beyond (4.1)–(4.2) and the audited (4.2) of HF18-A; no
proof or refutation of (4.3); no regularity of \(w\) or \(q\) ((H1) remains a
hypothesis); no invariance or non-invariance of \(\mathcal M\) under the
Navier–Stokes flow (only under the heat semigroup); no differentiability of
the minimiser map; no continuation criterion, no HIGH-STRAIN or HIGH-PRESSURE
theorem, no NS-R3 result; no novelty claim for the defect decomposition
(2.4)–(2.5). The numerics are bounded evidence at finite resolution on
periodic proxies of the static problem.

**NEXT DISTINCT ACTION:** The difference route is retired as a producer
(exact obstruction: \(\Delta\) is not coercive on \(u\), and its balance has the
same critical absorption as the two audited ones). Two distinct actions
remain from this wave. (1) FALSIFY on the Navier–Stokes side what §3 did on
the heat side: compute, for the elliptic swirl \(u_0\), the Euler contribution
\(-\mathbb P(u_0\cdot\nabla)u_0\cdot\nabla|u_0|^2-2u_0\cdot\nabla(u_0\cdot\mathbb P(u_0\cdot\nabla)u_0)\)
to \(\partial_t\operatorname{div}(|u|u)\) at \(t=0\); if it is nonzero and not
proportional to (3.3), then \(\mathcal M\) is not Navier–Stokes invariant for
any \(\nu\), and the sign of \(P_3-K\) at \(t=0^+\) on this family is computable
in closed form, giving the first analytic family on which \(K\ne0\) with
\(\|q\|_3/\|w\|_3\) controlled. (2) Test (4.3) for falsification on the
HF18-B witness family driven toward \(\|q\|_3/\|w\|_3\to\sup\) (HF18-A audit
R9), since a scaling-consistent refutation of (4.3) would show that even the
defect-weighted refinement of the size bound is false, closing that
side-question.

## 8. Sources and scratch

Manuscript `main.tex` at the working-tree revision of 2026-09-05, section
`sec:quotient` and `def:D3P3`, `prop:pressure` [DI]. `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, `hf18-hodge-regularity.md`,
`hf18-review-hodge-regularity.md`, `hf18-divergence-speed-link.md`,
`hf18-review-divergence-speed-link.md`, `hf18-review-divergence-speed-link-r2.md`
[DI, all in full]. Standard facts used without citation: uniqueness of the
nearest point on a compact convex set; Sobolev on \(\mathbb R^3\);
\(L^p\)-boundedness of \(R_iR_j\); Gaussian kernel norms. Kato, Math. Z. 187
(1984) [MO], for the classical status of (4.2). Scratch scripts (session
scratchpad, not part of the repository): `fermi_R.py` (sympy derivation of
(3.3)), `torus_probe.py` (§5.1), `ellipse2d.py`, `ellipse2d_R.py` (§5.2).
