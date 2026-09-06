# HF19-B: second-order behaviour of the transport term on the nonlinear-Hodge class

**AUDIT STATUS (2026-09-06).** Independently audited by
`research/evidence/hf19-review-second-order-falsifier.md` (full reconstruction from the first
nontrivial implication; frozen candidate sha256
`6114fd73322cfc6789c9c46a54810bf5ff39c1eedcdbdd39f53e97757f06c408`). **Verdict: REPAIR** — two
load-bearing gaps, both in the identification of the weak limit of the difference quotients
(former Steps 3 and 4), plus five presentational slips; no claim refuted. The controller applied
the audit's prescribed repairs to this note on 2026-09-06: the audit's **R1** replaces Step 3 and
deletes the hypothesis (H\(_\Omega\)) everywhere (it is a theorem, not a hypothesis, and needs no
connectivity or symmetry); **R2** replaces Step 4 and adds the explicit shell hypothesis (W) to
Lemma 1's scope line; **R3** replaces the derivation of (2.5) with a form that never differentiates
\(|u|\) pointwise; **R4** replaces §5.1's numerics-dependent family by an unconditional one; and
D3–D6, D8 are corrected (scaling exponent in §0; the citation of Lemma 1 inside Lemma 1.4; the
pointwise differentiation of \(|u|\); the three shell magnitudes of §4, whose numbers are withdrawn
as not reproducible; and the headline, which understated the outcome). Two statements are thereby
upgraded from conditional to unconditional. Numerics remain bounded evidence, never proof, and the
first gap is unchanged.

Lane HF19-B, MODE: FALSIFY, 2026-09-05; repaired 2026-09-06. Inputs [DI]: PLAN.md
("Frontier packet", "Beyond the checkpoint", "HF16–HF17", "HF18"); manuscript `sec:quotient` of
`../navier-paper/main.tex` (labels `lem:quotient-minimizer`, `lem:quotient-coercive`,
`lem:quotient-stability`, `prop:quotient-derivative`, `lem:quotient-chainrule`,
`lem:quotient-heatsign`, `lem:quotient-transport`, `prop:quotient-evolution`,
`lem:quotient-lowstrain`, `hyp:highstrain`, `prop:quotient-conditional`);
`hf17-quotient-functional.md`, `hf17-quotient-evolution.md`, `hf18-hodge-regularity.md`
with `hf18-review-hodge-regularity.md` (PASS), `hf18-divergence-speed-link.md` with its two
reviews (REPAIR, then PASS with S1–S4 applied); `hf19-review-second-order-falsifier.md` (REPAIR,
repairs applied here). Source tags: [DI] directly inspected in this programme; [MO] metadata only
or from memory, never load-bearing.

**MODE / RESULT: FALSIFY, target "a monotone/Lyapunov mechanism for \(\mathcal Q\)"; outcome: the
target IS refuted — unconditionally, by oddness (0.5) together with an explicit smooth compactly
supported solenoidal datum with \(K\ne0\) (§5.1, Proposition 5.1). What survived is only the
sharper sub-question this lane put to the target: whether the second-order dynamics *through*
\(\mathcal M\) produce the failure. They do not on the tested class — on every tested member of the
explicit swirl class the transport term leaves \(\mathcal M\) with the favourable sign,
\(dK/dt(0)<0\).** What is proved: an exact first-order expansion of \(K\) at
any \(u_0\in\mathcal M\) that never differentiates the minimizer (weighted a-priori estimate
plus a uniquely solvable degenerate-elliptic linearised nonlinear-Hodge problem); on the
axisymmetric swirl class the derivative is explicit,
\[
 \frac{d}{dt}K(u(t))\Big|_{t=0}
 =\big\langle(\Pi-\Pi_\rho)f,\,f\big\rangle_\rho
 =P_3'(0)-\|q_1\|_{L^2(\rho)}^2\ \le\ P_3'(0),\qquad
 P_3'(0)=\int p_0\,m\cdot\nabla|u_0|\,dx ,
\]
with \(\rho=|u_0|\), \(f=(s^2/r)e_r\) the centrifugal field, \(\Pi\) the Leray gradient
projection, \(\Pi_\rho\) its \(\rho\)-weighted analogue on \(\{u_0\ne0\}\), \(m=f-\nabla p_0\)
the meridional Euler tendency, \(q_1\) the first-order gradient part of the minimizer, and
\(P_3\) the pressure work of the pressure route. Both \(dK/dt(0)\) and \(P_3'(0)\) are
independent of \(\nu\). The sign of \(dK/dt(0)\) is therefore decided by the explicit
minimizer-free functional \(P_3'(0)\) whenever the latter is \(\le0\); bounded numerics on
twenty-one smooth profiles, a thin-ring ODE reduction with a closed form for constant speed,
and an independent 3D nonlinear minimisation all give \(P_3'(0)<0\) and \(dK/dt(0)<0\).
Two consequences are rigorous: (i) \(K\) is odd, \(K(-u)=-K(u)\), while \(\mathcal Q,D_3\)
are even, so non-monotonicity of \(\mathcal Q\) at large amplitude is immediate from any
datum with \(K\ne0\), and Proposition 5.1 exhibits such a datum unconditionally, giving Clay data
with \(K=\varepsilon\|U\|_3^3+o(\varepsilon)>0\);
(ii) along the actual trajectory from a tested \(u_0\in\mathcal M\),
\(\mathcal Q'(t)=-\nu D_3(w(t))-t|K'(0)|+O(t^{3/2})\): no failure of monotonicity is produced
near \(\mathcal M\) by second-order dynamics on that class. Nothing here touches the first gap.

## 0. Standing facts, notation, and the characterisation of \(\mathcal M\)

Throughout \(u_0\) is a divergence-free field in \(H^m(\mathbb R^3)\), \(m\ge4\), so that
\(u_0\in W^{1,\infty}\cap L^3\), and \(\rho:=|u_0|\), \(\hat u_0:=u_0/\rho\) on
\(\Omega':=\{u_0\ne0\}\) (open, since \(u_0\) is continuous). Imported and audited [DI]:

- (E1)–(E5) of HF18-A §0 and (A1)–(A5) of HF18-B §0: the minimizer \(q(u)\in\mathcal G_3\),
  \(w=u+q\), \(A=|w|w\in L^{3/2}\), \(\int A\cdot g=0\) for \(g\in\mathcal G_3\),
  \(q(u+g)=q(u)-g\), \(w(u+g)=w(u)\) (`lem:quotient-minimizer`(d)), \(\|q\|_3\le(1+C_3)\|w\|_3\),
  \(V=|w|^{1/2}w\in H^1\), \(D_{\mathcal Q}(u)=D_3(w)\), and on a compact classical interval
  \(\mathcal Q'+\nu D_3(w)=K\), with the derivative-free forms
  \[
   K=-\int q\cdot((A\cdot\nabla)u)=-\int A\cdot((u\cdot\nabla)u)=-\int q\cdot((u\cdot\nabla)A)
   =-\int|w|\,w\cdot S(u)\,w .                                                     \tag{0.1}
  \]
- Stability (`lem:quotient-stability`): with \(w'=w(u+h)\), \(A'=A(u+h)\),
  \(\tfrac12\|w'-w\|_3^3\le\langle A'-A,h\rangle\), \(\|w'-w\|_3\le2(\|w\|_3+\|h\|_3)^{1/2}\|h\|_3^{1/2}\),
  \(\|A'-A\|_{3/2}\le4(\|w\|_3+\|h\|_3)^{3/2}\|h\|_3^{1/2}\), \(\big|\|w'\|_3-\|w\|_3\big|\le\|h\|_3\).
- Lemma V of HF18-A §1.4: for \(z,z'\in\mathbb R^3\), with \(\tilde A(z)=|z|z\), \(V(z)=|z|^{1/2}z\),
  \[
   \tfrac89|V(z)-V(z')|^2\le(\tilde A(z)-\tilde A(z'))\cdot(z-z'),\quad
   (|z|+|z'|)|z-z'|^2\le8|V(z)-V(z')|^2,\quad
   |\tilde A(z)-\tilde A(z')|\le2\sqrt2(|z|+|z'|)^{1/2}|V(z)-V(z')| .                 \tag{0.2}
  \]
  All three were independently re-verified by the audit (a \(4\times10^5\)-sample search over
  \(\mathbb R^3\times\mathbb R^3\) gives sharp ratios \(0.888889=8/9\) for the first — sharp — and
  valid but not sharp constants in the other two).
- Pressure route (PLAN "ALSO ESTABLISHED"; recomputed here): with \(X=\|u\|_3^3\),
  \[
   \tfrac13X'+\nu D_3(u)=P_3:=\int p\,u\cdot\nabla|u|\,dx ,                          \tag{0.3}
  \]
  because \(\int|u|u\cdot(u\cdot\nabla)u=\int u\cdot\nabla(|u|^3/3)=0\) and
  \(-\int|u|u\cdot\nabla p=\int p\operatorname{div}(|u|u)=\int p\,u\cdot\nabla|u|\).
- Riesz/pressure convention of the manuscript (`rem:qe-pressure-normalisation`):
  \(p=R_iR_j(u_iu_j)\), \(\Delta p=-\partial_i\partial_j(u_iu_j)=-\operatorname{div}((u\cdot\nabla)u)\),
  \((I-\mathbb P)[(u\cdot\nabla)u]=-\nabla p\).

**Characterisation of \(\mathcal M\).** For \(u\in W^{1,\infty}\) solenoidal,
\(\operatorname{div}(|u|u)=|u|\operatorname{div}u+u\cdot\nabla|u|=u\cdot\nabla|u|\) a.e.
(\(|u|\) is Lipschitz). Hence
\[
 \mathcal M=\{u:\operatorname{div}(|u|u)=0\}=\{u:\ u\cdot\nabla|u|=0\ \text{a.e.}\},          \tag{0.4}
\]
the speed is constant along streamlines. On \(\mathcal M\): \(q=0\), \(w=u\), \(A=|u|u\),
\(\mathcal Q=X/3\), \(D_3(w)=D_3(u)\), \(K=0\) (HF18-A audit R9), and by (0.4) also \(P_3=0\).
So at an instant \(t_0\) with \(u(t_0)\in\mathcal M\) the two routes coincide exactly:
\(\mathcal Q'(t_0)=X'(t_0)/3=-\nu D_3(u(t_0))<0\) unless \(u=0\). The question of this lane is
the next order.

**Oddness.** \(q(-u)=-q(u)\), \(A(-u)=-A(u)\) (uniqueness and homogeneity,
`lem:quotient-scaling`), hence from (0.1)
\[
 K(-u)=-K(u),\qquad \mathcal Q(-u)=\mathcal Q(u),\qquad D_3(w(-u))=D_3(w(u)),\qquad P_3(-u)=-P_3(u). \tag{0.5}
\]
Also \(\mathcal M=-\mathcal M\).

**Scalings** (HF18-B §0, [DI]): under amplitude \(a\) and dilation \(\lambda\),
\(\mathcal Q\sim(a^3,1)\), \(D_3\sim(a^3,\lambda^2)\), \(K\sim(a^4,\lambda^2)\); a time
derivative adds \((a,\lambda^2)\) (advective time \(\sim a^{-1}\lambda^{-2}\)), so
\(dK/dt\sim(a^5,\lambda^4)\sim D_3^2\mathcal Q^{-1/3}\), and
\(\nu D_3\cdot(\nu D_3/\mathcal Q)=\nu^2D_3^2/\mathcal Q\sim(a^3\nu^2,\lambda^4)\)
(corrected per audit D3: \(\nu^2a^6\lambda^4/a^3=a^3\nu^2\lambda^4\)).
The dimensionless ratio of the transport-driven second-order rate to the viscous one is
therefore \((dK/dt)/(\nu^2D_3^2/\mathcal Q)\sim a^2/\nu^2\sim\mathcal Q^{2/3}/\nu^2\sim\mathrm{Re}^2\).

## 1. First-order expansion of \(K\) at a point of \(\mathcal M\) (no derivative of the minimizer)

Fix \(u_0\in\mathcal M\cap H^m\), \(m\ge4\), and \(h\in H^m\) (so \(h\in L^3\), \(\nabla h\in L^\infty\)).
Put \(u_\varepsilon=u_0+\varepsilon h\), \(w_\varepsilon=w(u_\varepsilon)\), \(q_\varepsilon=q(u_\varepsilon)\),
\(A_\varepsilon=A(u_\varepsilon)\), \(V_\varepsilon=|w_\varepsilon|^{1/2}w_\varepsilon\); \(w_0=u_0\), \(q_0=0\),
\(A_0=\rho u_0\), \(V_0=\rho^{1/2}u_0\). Write
\[
 M(x):=D\tilde A(u_0(x))=\rho\,(I+\hat u_0\otimes\hat u_0)\ \text{on }\Omega',\qquad M:=0\ \text{off }\Omega',
 \qquad \rho|\zeta|^2\le M\zeta\cdot\zeta\le2\rho|\zeta|^2 ,                                   \tag{1.1}
\]
\(L^2(\rho):=L^2(\Omega';\rho\,dx)\) with \(\langle a,b\rangle_\rho=\int_{\Omega'}\rho\,a\cdot b\), and
\[
 g:=(A_0\cdot\nabla)u_0=\rho\,(u_0\cdot\nabla)u_0,\qquad g/\rho=(u_0\cdot\nabla)u_0\in L^\infty ,\qquad g\in L^2(\rho^{-1}) . \tag{1.2}
\]

### Step 1 (weighted a-priori bound; unconditional)

By the Euler–Lagrange condition both \(A_\varepsilon\) and \(A_0\) annihilate \(q_\varepsilon\in\mathcal G_3\), so
\(\langle A_\varepsilon-A_0,\,w_\varepsilon-u_0\rangle=\langle A_\varepsilon-A_0,\,\varepsilon h+q_\varepsilon\rangle=\varepsilon\langle A_\varepsilon-A_0,h\rangle\).
By (0.2) (first and third inequalities), Cauchy–Schwarz and Hölder (\(\int|w||h|^2\le\|w\|_3\|h\|_3^2\)),
\[
 \tfrac89\|V_\varepsilon-V_0\|_2^2\le\varepsilon\,2\sqrt2\,\|V_\varepsilon-V_0\|_2\,(\|w_\varepsilon\|_3+\|u_0\|_3)^{1/2}\|h\|_3 ,
\]
hence, with \(\|w_\varepsilon\|_3\le\|u_0\|_3+\varepsilon\|h\|_3\),
\[
 \|V_\varepsilon-V_0\|_2\le\tfrac94\sqrt2\,(2\|u_0\|_3+\varepsilon\|h\|_3)^{1/2}\|h\|_3\;\varepsilon=:C_1\varepsilon, \qquad
 \int(|w_\varepsilon|+\rho)\,|w_\varepsilon-u_0|^2\,dx\le8C_1^2\varepsilon^2                                  \tag{1.3}
\]
by the second inequality of (0.2). Consequences: \(\omega_\varepsilon:=(w_\varepsilon-u_0)/\varepsilon\) is bounded in
\(L^2(\rho)\); on \(\{\rho\ge c\}\), \(\int_{\{\rho\ge c\}}|w_\varepsilon-u_0|^2\le8C_1^2\varepsilon^2/c\);
and off \(\Omega'\), \(\int_{\Omega'^c}|w_\varepsilon|^3\le8C_1^2\varepsilon^2\), i.e. \(\|q_\varepsilon\|_{L^3(\Omega'^c)}=O(\varepsilon^{2/3})\)
(only this weaker rate is used; the exterior is a nonlinear 3-Laplace problem at leading order, see Remark 1.3).
The audit records that this step is valid at *any* base point, not only on \(\mathcal M\), since \(A(v)\) and
\(A(v+z)\) both annihilate \(\mathcal G_3\) and \(q(v+z)-q(v)\in\mathcal G_3\); Lemma 1.4 uses it at \(\bar u\).

### Step 2 (the linearised equation, tested inside \(\Omega'\))

\(D\tilde A(z)=|z|I+z\otimes\hat z\) is positively 1-homogeneous and smooth on the sphere, hence globally Lipschitz;
so \(|\tilde A(z')-\tilde A(z)-D\tilde A(z)(z'-z)|\le C_L|z'-z|^2\). For \(\eta\in C_c^\infty(\Omega')\), \(c:=\min_{\operatorname{supp}\eta}\rho>0\), and
\(0=\langle A_\varepsilon-A_0,\nabla\eta\rangle=\varepsilon\langle M\omega_\varepsilon,\nabla\eta\rangle+\langle R_\varepsilon,\nabla\eta\rangle\) with
\(|\langle R_\varepsilon,\nabla\eta\rangle|\le C_L\|\nabla\eta\|_\infty\int_{\{\rho\ge c\}}|w_\varepsilon-u_0|^2\le8C_LC_1^2\|\nabla\eta\|_\infty\varepsilon^2/c\).
Hence \(\langle M\omega_\varepsilon,\nabla\eta\rangle=O(\varepsilon)\to0\).

### Step 3 (the weak limit is a gradient — unconditionally)

*(This step replaces the former hypothesis (H\(_\Omega\)) and its axisymmetric verification, which the
audit's first bad bridge showed to be incomplete: excluding the generator \(d\theta\) of \(H^1_{\rm dR}\)
does not exclude the meridional harmonic form \(d\vartheta=e_\vartheta/\varrho\), which is axisymmetric,
meridional, curl-free, not a single-valued gradient, and admissible in \(L^2(\rho)\) whenever the speed has
an interior zero in the meridional cross-section — as it does for every shell profile of §4. The audit
supplies the following replacement, which needs no connectivity, symmetry or regularity hypothesis, so
(H\(_\Omega\)) is deleted from this note entirely.)*

By Step 1 a subsequence \(\omega_{\varepsilon_j}\rightharpoonup\omega\) in \(L^2(\rho)\). Since
\((I+\hat u_0\otimes\hat u_0)\nabla\eta\in L^2(\rho)\), Step 2 gives
\[
 \int_{\Omega'}\rho\,(I+\hat u_0\otimes\hat u_0)\,\omega\cdot\nabla\eta\,dx=0\qquad(\eta\in C_c^\infty(\Omega')).    \tag{1.4}
\]
Moreover \(\omega-h=\lim q_{\varepsilon_j}/\varepsilon_j\) weakly in \(L^2_{\rm loc}(\Omega')\) (on compacts \(\rho\ge c\)).

**Lemma 1.2 (audit R1).** Let \(\Omega'\subset\mathbb R^3\) be open, \(\varepsilon_j\to0\),
\(q_j\in\mathcal G_3\), and suppose \(q_j/\varepsilon_j\rightharpoonup v\) weakly in \(L^2_{\rm loc}(\Omega')\).
Then \(v=\nabla\phi\) for some \(\phi\in W^{1,2}_{\rm loc}(\Omega')\). No connectivity, symmetry or
regularity hypothesis on \(\Omega'\) is used.

*Proof.* (i) Each \(q_j\) is an \(L^3\) limit of gradients of \(C_c^\infty\) functions, hence
\(\operatorname{curl}q_j=0\) in \(\mathcal D'(\mathbb R^3)\), hence \(\operatorname{curl}v=0\) in \(\mathcal D'(\Omega')\).
(ii) Let \(J\in C_c^\infty(\Omega';\mathbb R^3)\) with \(\operatorname{div}J=0\). For \(\phi\in C_c^\infty(\mathbb R^3)\),
\(\int\nabla\phi\cdot J=-\int\phi\operatorname{div}J=0\); since \(J\in L^{3/2}\) this passes to the \(L^3\) limit, so
\(\int q_j\cdot J=0\) for every \(j\). As \(\operatorname{supp}J\) is a compact subset of \(\Omega'\),
\(J\in L^2(\operatorname{supp}J)\) and weak \(L^2_{\rm loc}\) convergence gives
\[
 \int_{\Omega'}v\cdot J=\lim_j\varepsilon_j^{-1}\int q_j\cdot J=0\qquad
 \text{for every solenoidal }J\in C_c^\infty(\Omega';\mathbb R^3).                                  \tag{R1.1}
\]
(iii) Fix a connected open \(\omega\) with compact closure in \(\Omega'\), and let \(v_\delta=v*\eta_\delta\) for
\(\delta<\operatorname{dist}(\omega,\partial\Omega')\). Then \(v_\delta\) is smooth and curl-free on \(\omega\), and for
solenoidal \(J\in C_c^\infty(\omega)\) the field \(J*\check\eta_\delta\) is again solenoidal, smooth and compactly
supported in \(\Omega'\), so \(\int v_\delta\cdot J=0\) by (R1.1). In the language of forms, \(v_\delta\) is a smooth
closed 1-form on \(\omega\) annihilating every compactly supported closed 2-form; by the de Rham isomorphism
\(H^1_{\rm dR}(\omega)\cong(H^2_c(\omega))^*\) (compactly supported solenoidal vector fields are exactly the
compactly supported closed 2-forms), \([v_\delta]=0\), i.e. \(v_\delta=\nabla\phi_\delta\) on \(\omega\).
Normalising \(\phi_\delta\) to have zero mean on a fixed ball and using \(v_\delta\to v\) in \(L^2(\omega)\)
together with the Poincaré inequality, \(\phi_\delta\to\phi\) in \(L^2(\omega)\) with \(\nabla\phi=v\).
Exhausting \(\Omega'\) by such \(\omega\) and matching on overlaps (the potentials differ by constants on
connected overlaps) gives \(\phi\in W^{1,2}_{\rm loc}(\Omega')\). \(\square\)

Applied to \(q_{\varepsilon_j}\), Lemma 1.2 gives \(\omega-h=\nabla\phi_1\) with
\(\phi_1\in W^{1,2}_{\rm loc}(\Omega')\), for every open \(\Omega'\) — including the shell profiles of §4,
whose harmonic mode \(d\vartheta\) is excluded here by the vanishing of its periods, not by symmetry.
No novelty is claimed: the vanishing of periods under weak limits of exact forms is standard de Rham duality.

### Step 4 (uniqueness in the weighted class; "\(H=W\)" for the degenerate weight, under (W))

*(This step replaces the former coarea/log-cutoff argument, which the audit's second bad bridge showed to
need an unstated upper Minkowski bound \(|\{d<t\}|\le Ct\), and whose parenthetical for unbounded \(\Omega'\)
was wrong as written. The replacement builds the cutoff from the weight itself, needs no geometry of
\(\partial\Omega'\) and no Lipschitz-distance bound, and carries one explicit hypothesis.)*

**Hypothesis (W).** For every \(R>0\),
\[
 \int_{\{\delta^2<\rho<\delta\}\cap B_R}\frac{|\nabla\rho|^2}{\rho}\,dx=o\big(\log^2(1/\delta)\big)\qquad(\delta\to0). \tag{W}
\]

**Lemma 1.3 (audit R2).** Let \(u_0\in\mathcal M\cap H^m\), \(m\ge4\), \(\rho=|u_0|\), \(\Omega'=\{\rho>0\}\),
\(M=\rho(I+\hat u_0\otimes\hat u_0)\), and assume (W). Let \(\phi\in L^2_{\rm loc}(\Omega')\) with
\(\nabla\phi\in L^2(\rho)\) and \(\int_{\Omega'}M\nabla\phi\cdot\nabla\eta=0\) for all \(\eta\in C_c^\infty(\Omega')\).
Then \(\nabla\phi=0\).

*Proof.* Put \(\zeta_\delta=\min\{1,(\log(\rho/\delta^2))_+/\log(1/\delta)\}\) — built from \(\rho\), not from the
distance to \(\partial\Omega'\). Then \(\zeta_\delta=0\) on \(\{\rho\le\delta^2\}\), \(=1\) on \(\{\rho\ge\delta\}\),
it is Lipschitz on \(\Omega'\), and on the shell \(|\nabla\zeta_\delta|=|\nabla\rho|/(\rho\log(1/\delta))\), so
\[
 \int\rho|\nabla\zeta_\delta|^2=\log(1/\delta)^{-2}\int_{\rm shell}\frac{|\nabla\rho|^2}{\rho} .          \tag{R2.2}
\]
Let \(\chi_R=1\) on \(B_R\), \(0\) off \(B_{2R}\), \(|\nabla\chi_R|\le2/R\), and \(\phi_N=\max(-N,\min(\phi,N))\).
The function \(\eta=\zeta_\delta\chi_R\phi_N\) is Lipschitz with support in the compact set
\(\{\rho\ge\delta^2\}\cap\overline{B_{2R}}\subset\Omega'\), hence admissible by mollification. Expanding \(\nabla\eta\),
\[
 \int\chi_R\zeta_\delta M\nabla\phi_N\cdot\nabla\phi_N
 =-\int\phi_N\chi_R M\nabla\phi\cdot\nabla\zeta_\delta-\int\phi_N\zeta_\delta M\nabla\phi\cdot\nabla\chi_R .
\]
The left side is nonnegative and increases to \(\int\chi_RM\nabla\phi_N\cdot\nabla\phi_N\) as \(\delta\to0\)
(dominated convergence, dominant \(2\rho|\nabla\phi|^2\in L^1\)). By \(M\le2\rho\), \(|\phi_N|\le N\),
Cauchy–Schwarz and (R2.2), the first right-hand term is at most
\(2N\big(\int_{\{\rho<\delta\}}\rho|\nabla\phi|^2\big)^{1/2}\big(o(\log^2(1/\delta))\big)^{1/2}/\log(1/\delta)\to0\)
as \(\delta\to0\) at fixed \(R\), the first factor tending to \(0\) by dominated convergence. The second
right-hand term is at most
\[
 \frac{4N}{R}\Big(\int_{|x|>R}\rho|\nabla\phi|^2\Big)^{1/2}\Big(\int_{B_{2R}}\rho\Big)^{1/2}
 \le\frac{4N}{R}\,o_R(1)\,\big(\|\rho\|_3(CR^3)^{2/3}\big)^{1/2}=CN\,o_R(1),
\]
uniformly in \(\delta\): the factor that vanishes is the tail \(\int_{|x|>R}\rho|\nabla\phi|^2\), not
\(R^{-2}\int\rho\), which is merely bounded. Letting \(\delta\to0\) at fixed \(R\) and then \(R\to\infty\) gives
\(\int M\nabla\phi_N\cdot\nabla\phi_N=0\), so \(\nabla\phi_N=0\) for every \(N\), so \(\nabla\phi=0\). \(\square\)

The same argument shows that (1.4) then holds for every test gradient \(\nabla\eta\in L^2(\rho)\) (replace \(\eta\)
by \(\zeta_\delta\chi_R\eta_N\) and pass to the limit).

**Where (W) holds.** (W) is implied by the content bound \(|\{0<\rho<t\}\cap B_R|\le C_Rt\) (then the shell
integral is \(O(\log(1/\delta))\)); it holds whenever \(\rho\) vanishes to finite order \(k\ge1\) on a rectifiable
set (\(|\nabla\rho|^2/\rho\sim d^{k-2}\), locally integrable for \(k\ge1\)) and whenever it vanishes to infinite
order (\(\rho\sim e^{-c/d}\) gives \(|\nabla\rho|^2/\rho\sim\rho/d^4\to0\), bounded). Every profile of §§2–4 —
\(B(x)=(1-x^2)^4_+\), the exponential bumps, the shells, and the \(b(t)=e^{-1/(1-t^2)}\) swirl of §5.1 —
satisfies (W). (W) is not known to hold for every \(u_0\in\mathcal M\cap H^m\), so it is carried explicitly in
the scope line of Lemma 1; no claim is made without it.

### Lemma 1 (first-order expansion of \(K\) on \(\mathcal M\))

Let \(u_0\in\mathcal M\cap H^m\), \(m\ge4\), satisfy (W), and let \(h\in H^m\). Then the following hold, for
every open \(\Omega'\) (no simple connectivity, no symmetry, no hypothesis (H\(_\Omega\))).

(a) *The linearised nonlinear-Hodge problem* — find \(\nabla\phi_1\in L^2(\rho)\), \(\phi_1\in L^2_{\rm loc}(\Omega')\), with
\[
 \operatorname{div}\big(M\,(h+\nabla\phi_1)\big)=0\ \text{in }\mathcal D'(\Omega'),\qquad
 M=\rho(I+\hat u_0\otimes\hat u_0),                                                                   \tag{1.5}
\]
has exactly one solution (up to constants). It is the \(M\)-orthogonal projection: \(-\nabla\phi_1\) minimises
\(\int_{\Omega'}M(h+\nabla\phi)\cdot(h+\nabla\phi)\) over the \(L^2(\rho)\)-closure of \(\nabla C_c^\infty(\Omega')\)
(Riesz), and Lemma 1.3 identifies it with any solution in the larger class. This is the linearisation of
\(\operatorname{div}(|w|w)=0\) at \(w=u_0\): \(w_1=h+\nabla\phi_1\), \(\operatorname{div}(D\tilde A(u_0)w_1)=0\).

(b) *Convergence.* \(\omega_\varepsilon=(w_\varepsilon-u_0)/\varepsilon\rightharpoonup h+\nabla\phi_1\) in \(L^2(\rho)\) along the full
family \(\varepsilon\to0\), and \(q_\varepsilon/\varepsilon\rightharpoonup\nabla\phi_1\) in \(L^2(\rho)\).

(c) *Expansion.*
\[
 K(u_0+\varepsilon h)=\varepsilon\,DK(u_0)[h]+o(\varepsilon),\qquad
 DK(u_0)[h]:=-\langle\nabla\phi_1,g\rangle=-\int_{\Omega'}\rho\,\nabla\phi_1\cdot\big((u_0\cdot\nabla)u_0\big)\,dx .   \tag{1.6}
\]
The map \(h\mapsto DK(u_0)[h]\) is linear and \(|DK(u_0)[h]|\le\sqrt2\,\|h\|_{L^2(\rho)}\|(u_0\cdot\nabla)u_0\|_{L^2(\rho)}
\le C(u_0)\|h\|_3\).

Here \(K\) is the functional \(K=-\int q\cdot((A\cdot\nabla)u)\) of (0.1); it coincides with the transport term of
the quotient evolution on solenoidal directions, which is the only case used below (Remark 1.5).

*Proof.* (a), (b) are Steps 1–4 (with Lemma 1.2 for the gradient structure and Lemma 1.3 for uniqueness).
For (c), by (0.1), \(K(u_\varepsilon)=-\langle q_\varepsilon,G_\varepsilon\rangle\) with
\(G_\varepsilon:=(A_\varepsilon\cdot\nabla)u_\varepsilon\), and \(q_\varepsilon=(w_\varepsilon-u_0)-\varepsilon h\), so
\[
 K(u_\varepsilon)=-\langle w_\varepsilon-u_0,\,g\rangle-\langle w_\varepsilon-u_0,\,G_\varepsilon-g\rangle+\varepsilon\langle h,g\rangle+\varepsilon\langle h,G_\varepsilon-g\rangle .
\]
Now \(G_\varepsilon-g=((A_\varepsilon-A_0)\cdot\nabla)u_\varepsilon+\varepsilon(A_0\cdot\nabla)h\) and, by
\(|\tilde A(z)-\tilde A(z')|\le(|z|+|z'|)|z-z'|\) (`lem:cubic-pointwise`) and (1.3),
\(\int|w_\varepsilon-u_0||A_\varepsilon-A_0||\nabla u_\varepsilon|\le\|\nabla u_\varepsilon\|_\infty\int(|w_\varepsilon|+\rho)|w_\varepsilon-u_0|^2=O(\varepsilon^2)\)
and \(\varepsilon\int|w_\varepsilon-u_0|\rho^2|\nabla h|\le\varepsilon\|\nabla h\|_\infty\|w_\varepsilon-u_0\|_{L^2(\rho)}\|\rho\|_3^{3/2}=O(\varepsilon^2)\);
also \(|\langle h,G_\varepsilon-g\rangle|\le\|h\|_3\|G_\varepsilon-g\|_{3/2}=O(\varepsilon)\) by the stability lemma
(indeed \(\|A_\varepsilon-A_0\|_{3/2}=O(\varepsilon)\) follows from (1.3) by Hölder with exponents \(4/3,4\)). Finally
\(\langle w_\varepsilon-u_0,g\rangle=\varepsilon\langle\omega_\varepsilon,(u_0\cdot\nabla)u_0\rangle_\rho\to\varepsilon\langle h+\nabla\phi_1,g\rangle\)
by (b) and (1.2), the single limit being taken against the *fixed* element
\((u_0\cdot\nabla)u_0\in L^2(\rho)\). Collecting, \(K(u_\varepsilon)=-\varepsilon\langle\nabla\phi_1,g\rangle+o(\varepsilon)\). The bound on
\(DK\) uses \(\|\nabla\phi_1\|_{L^2(\rho)}\le\sqrt2\|h\|_{L^2(\rho)}\) (projection in the \(M\)-inner product, (1.1))
and \(\|h\|_{L^2(\rho)}^2\le\|\rho\|_3\|h\|_3^2\). \(\square\)

**Remark 1.2 (what is and is not differentiated).** No derivative of \(w\) or \(q\) is taken; only the
\(L^2(\rho)\)-boundedness of the difference quotient \((w_\varepsilon-u_0)/\varepsilon\) from the monotonicity structure
(0.2), and the fact that \(g\) carries the factor \(\rho\). The expansion is one-sided in nothing: the pairing
\(\langle q_\varepsilon,g\rangle\) is first-order exact. The lemma is the Gateaux derivative of \(K\) at \(u_0\in\mathcal M\)
in the direction \(h\); it says nothing about \(u_0\notin\mathcal M\).

**Remark 1.3 (the degenerate exterior).** Off \(\Omega'\), \(u_\varepsilon=\varepsilon h\) and the Euler–Lagrange equation
is \(\operatorname{div}(|\varepsilon h+\nabla\phi_\varepsilon|(\varepsilon h+\nabla\phi_\varepsilon))=0\), homogeneous of degree
two: the first-order problem there is the *nonlinear* exterior 3-Laplace problem
\(\operatorname{div}(|h+\nabla\tilde\phi|(h+\nabla\tilde\phi))=0\) with matching to the interior data across the
boundary layer \(\{\rho\lesssim\varepsilon\}\), where the linearisation (1.5) is invalid (the linear \(q_1\) grows to
\(O(1)\) relative to \(\rho\) there: \(\max|q_1|/\max\rho\approx2.6\) on the blob of §4). None of this enters (1.6),
because \(g=0\) off \(\Omega'\) and \(g=O(\rho)\) near \(\partial\Omega'\); the lemma quantifies exactly this.

**Remark 1.5 (independent route to (1.6), and the solenoidality caveat; from the audit).** Expanding the
*other* derivative-free form \(K=-\langle A,(u\cdot\nabla)u\rangle\) for solenoidal \(h\) gives
\(DK[h]=-\langle A_0,N_1\rangle-\lim\varepsilon^{-1}\langle A_\varepsilon-A_0,N_0\rangle\) with
\(N_1=(h\cdot\nabla)u_0+(u_0\cdot\nabla)h\), \(N_0=(u_0\cdot\nabla)u_0\); here
\(\langle A_0,(h\cdot\nabla)u_0\rangle=\int h\cdot\nabla(\rho^3/3)=0\) (needs \(\operatorname{div}h=0\)),
\(\langle A_0,(u_0\cdot\nabla)h\rangle=-\langle h,g\rangle\) (needs \(u_0\in\mathcal M\), \(\operatorname{div}u_0=0\)), and
\(\varepsilon^{-1}\langle A_\varepsilon-A_0,N_0\rangle\to\langle h+\nabla\phi_1,g\rangle\) because
\(\hat u_0\cdot N_0=\rho^{-1}u_0\cdot\nabla(\rho^2/2)=0\) on \(\mathcal M\) kills the rank-one part. The two
\(\langle h,g\rangle\) cancel and \(DK[h]=-\langle\nabla\phi_1,g\rangle\), which is (1.6): an independent
derivation of the same coefficient. It needs \(\operatorname{div}h=0\), which Lemma 1 does not assume; for
non-solenoidal \(h\) the three forms of (0.1) have different first-order parts (differing by
\(\int(\rho^3/3)\operatorname{div}h\)), so (1.6) is the expansion of the form \(K=-\int q\cdot((A\cdot\nabla)u)\)
and coincides with the transport term only on solenoidal directions. Every application below uses solenoidal \(h\).

### Lemma 1.4 (along the Navier–Stokes trajectory)

Let \((u,p)\) be the classical solution with datum \(u_0\in\mathcal M\cap\mathcal S\), \(u_1:=u_t(0)=\nu\Delta u_0-(u_0\cdot\nabla)u_0-\nabla p_0\).
Then
\[
 K(u(t))=t\,DK(u_0)[u_1]+o(t)\qquad(t\downarrow0),\qquad\text{i.e.}\qquad \frac{dK}{dt}(0)=DK(u_0)[u_1] .   \tag{1.7}
\]
*Proof.* \(u\in C^2([0,T];H^k)\) for all \(k\) (package (R1) applied to \(u_t\)), so \(u(t)=u_0+tu_1+r(t)\) with
\(\|r(t)\|_3+\|\nabla r(t)\|_\infty\le Ct^2\). With \(\bar u=u_0+tu_1\), \(u=\bar u+r\),
\(K(u)-K(\bar u)=-\langle w(u)-w(\bar u),G_u\rangle+\langle r,G_u\rangle-\langle q(\bar u),G_u-G_{\bar u}\rangle\).
First term: \(|G_u|\le\|\nabla u\|_\infty|w(u)|^2\) and, by Step 1 at base point \(\bar u\) with perturbation \(r\),
\(\int|w(u)||w(u)-w(\bar u)|^2\le8C_1^2\|r\|_3^2\); Cauchy–Schwarz with \(\int|w(u)|^3\) gives \(O(\|r\|_3)=O(t^2)\).
Second: \(O(\|r\|_3)\). Third: \(\|q(\bar u)\|_3=O(t^{1/2})\) (stability lemma, \(q(u_0)=0\)) and
\(\|G_u-G_{\bar u}\|_{3/2}\le\|A(u)-A(\bar u)\|_{3/2}\|\nabla u\|_\infty+\|A(\bar u)\|_{3/2}\|\nabla r\|_\infty=O(t)\).
So \(K(u(t))=K(u_0+tu_1)+O(t^{3/2})\), and Lemma 1(c) applies with \(h=u_1\). *(Citation corrected per audit D4:
\(u_1=\nu\Delta u_0+m\in H^{m-2}\), and Lemma 1 needs \(\nabla h\in L^\infty\), i.e. \(m\ge5\); the Schwartz
hypothesis \(u_0\in\mathcal M\cap\mathcal S\) actually assumed here supplies this. Also \(u_0\in\mathcal S\)
satisfies (W) on every profile used.)* \(\square\)

Since \(\mathcal Q'=K-\nu D_3(w)\) and \(t\mapsto D_3(w(t))=D_{\mathcal Q}(u(t))\) is continuous
(`lem:quotient-heatsign`),
\[
 \mathcal Q'(t)=t\,\frac{dK}{dt}(0)-\nu D_3(w(t))+o(t),\qquad D_3(w(t))\to D_3(u_0) .                         \tag{1.8}
\]
No claim about \(\mathcal Q''(0)\) is made (it would need the derivative of \(D_3(w(t))\), which the weighted bound
(1.3) does not control near \(\partial\Omega'\)). Lemma 1 is a Gateaux derivative in data space; Lemma 1.4 converts
it to the actual flow in the single direction \(u_1=u_t(0)\), at the cost of \(O(t^{3/2})\). The two are not
interchanged anywhere in this note.

## 2. The swirl class: explicit derivative, \(\nu\)-independence, and the pressure-route link

Let \(u_0=s(r,z)\,e_\theta\) with \(s\) smooth, compactly supported in \(\{r>0\}\) (or Schwartz with the obvious
changes). Then \(\operatorname{div}(|s|s\,e_\theta)=r^{-1}\partial_\theta(|s|s)=0\), so \(u_0\in\mathcal M\) (HF18-A audit
R5(i)), \(\rho=|s|\), \(\hat u_0=\pm e_\theta\), \(\Omega'=\{s\ne0\}\), and
\[
 (u_0\cdot\nabla)u_0=-\frac{s^2}{r}e_r=:-f,\qquad g=(A_0\cdot\nabla)u_0=-\rho f=-\frac{|s|s^2}{r}e_r,\qquad
 \Delta u_0=\Big(\Delta s-\frac{s}{r^2}\Big)e_\theta .                                                      \tag{2.1}
\]
Pressure and Euler tendency: \(\Delta p_0=\operatorname{div}f=r^{-1}\partial_r(s^2)\), i.e. \(\nabla p_0=\Pi f:=(I-\mathbb P)f\),
and
\[
 u_1=\nu\Delta u_0+m,\qquad m:=\mathbb Pf=f-\nabla p_0\quad(\text{meridional, axisymmetric, solenoidal}),        \tag{2.2}
\]
\(m\) is the secondary (meridional) circulation driven by the unbalanced centrifugal force; \(m\) and \(p_0\) are smooth,
\(m=O(|x|^{-4})\), \(p_0=O(|x|^{-3})\) (quadrupole: monopole and dipole moments of \(\operatorname{div}f\) vanish;
independently re-verified by the audit).

### Theorem 2

Let \(u_0=s\,e_\theta\) as above (so that (W) holds — it does for every profile used here), \(\rho=|s|\),
\(f=(s^2/r)e_r\), \(\langle\cdot,\cdot\rangle_\rho\) the weighted pairing on
\(\Omega'\), \(\Pi_\rho f:=-\nabla\psi\) the \(\rho\)-weighted gradient part of \(f\) on \(\Omega'\), i.e. the unique
\(\nabla\psi\in L^2(\rho)\) with
\[
 \operatorname{div}\big(\rho\,(f+\nabla\psi)\big)=0\ \text{in }\mathcal D'(\Omega')                        \tag{2.3}
\]
(Lemma 1(a) with the scalar weight, since \(M\) acts as \(\rho I\) on meridional fields). Then:

(i) The first-order gradient part of the minimizer along \(u_1\) is \(q_1=\nabla\phi_1=\nabla\psi+\nabla p_0=(\Pi-\Pi_\rho)f\)
on \(\Omega'\); the viscous direction contributes nothing, \(Dq(u_0)[\nu\Delta u_0]=0\).

(ii)
\[
 \boxed{\ \frac{dK}{dt}(0)=DK(u_0)[u_1]=DK(u_0)[m]=\langle q_1,f\rangle_\rho=\big\langle(\Pi-\Pi_\rho)f,\,f\big\rangle_\rho
 =\langle\nabla p_0,f\rangle_\rho-\|\nabla\psi\|_{L^2(\rho)}^2 ,\ }                                          \tag{2.4}
\]
independent of \(\nu\), and a functional of the speed field \(\rho\) alone (through \(f=\rho^2e_r/r\)).

(iii) Pressure route: \(P_3(u(t))=\int p\,u\cdot\nabla|u|\) satisfies \(P_3(0)=0\) and
\[
 \boxed{\ P_3'(0)=\int p_0\,m\cdot\nabla\rho\,dx=-\langle m,\nabla p_0\rangle_\rho ,\ }                    \tag{2.5}
\]
also \(\nu\)-independent; and the exact link
\[
 \boxed{\ \frac{dK}{dt}(0)=P_3'(0)-\|q_1\|_{L^2(\rho)}^2\ \le\ P_3'(0),\qquad
 -\langle m,f\rangle_\rho\le\frac{dK}{dt}(0)\le-\langle m,\nabla p_0\rangle_\rho .\ }                        \tag{2.6}
\]
Equality on the right holds iff \(\Pi_\rho f=\Pi f\), i.e. iff \(m\cdot\nabla\rho=0\).

*Proof.* (i) The linearised problem (1.5) is linear in \(h=u_1=\nu\Delta u_0+m\), and Lemma 1 applies with no
hypothesis on \(\Omega'\) (Step 3) and with (W) (Step 4). For \(h=\nu\Delta u_0\) (azimuthal, \(\theta\)-independent),
\(Mh=2\rho\nu(\Delta u_0)_\theta e_\theta\)
and \(\int Mh\cdot\nabla\eta=\int2\rho\nu(\Delta u_0)_\theta\,r^{-1}\partial_\theta\eta=0\) for every \(\eta\), so
\(\nabla\phi_1=0\) by uniqueness (Lemma 1.3). For \(h=m\) (meridional) and axisymmetric \(\phi_1\),
\(M(m+\nabla\phi_1)=\rho(m+\nabla\phi_1)\),
and (1.5) reads \(\operatorname{div}(\rho(m+\nabla\phi_1))=0\); with \(m=f-\nabla p_0\) and \(\psi:=\phi_1-p_0\) this is (2.3).
Lemma 1.3 gives \(\nabla\phi_1=\nabla\psi+\nabla p_0\).
(ii) By (1.6) and (2.1), \(DK(u_0)[u_1]=-\langle\nabla\phi_1,g\rangle=\langle\nabla\phi_1,f\rangle_\rho\). Testing (2.3)
with \(\psi\) (admissible by the end of Step 4, since \(\nabla\psi=\nabla\phi_1-\nabla p_0\in L^2(\rho)\)) gives
\(\langle\nabla\psi,f\rangle_\rho=-\|\nabla\psi\|_\rho^2\), whence (2.4). Lemma 1.4 gives \(dK/dt(0)=DK(u_0)[u_1]\).
(iii) *(Derivation replaced per audit R3: \(|u|\) is nowhere differentiated pointwise. The former argument
differentiated \(|u|\) through \(\partial_t|u|=\hat u\cdot u_t\), which is meaningless on the interior of
\(\{u_0=0\}\), non-empty here; the value is unchanged.)* Since \(\operatorname{div}(|u|u)=u\cdot\nabla|u|\) for
solenoidal \(u\in W^{1,\infty}\), with \(j(z):=|z|z\),
\[
 P_3(t)=\int p\,(u\cdot\nabla|u|)=\int p\,\operatorname{div}(j(u))=-\int j(u)\cdot\nabla p .
\]
\(t\mapsto u(t)\) is \(C^1\) into \(L^3\) and \(t\mapsto\nabla p(t)\) is \(C^1\) into \(L^3\) by package (R1); \(j\) is
\(C^1\) from \(L^3\) to \(L^{3/2}\) with \(Dj(u_0)=M\). Hence \(P_3\) is \(C^1\) near \(0\) and
\[
 P_3'(0)=-\int M u_1\cdot\nabla p_0-\int j(u_0)\cdot\nabla\dot p_0
 =-\big\langle(I+\hat u_0\otimes\hat u_0)u_1,\nabla p_0\big\rangle_\rho ,
\]
the second term vanishing because \(u_0\in\mathcal M\) means \(j(u_0)=A_0\) annihilates \(\mathcal G_3\) and
\(\nabla\dot p_0\in\mathcal G_3\). For the swirl, \(\hat u_0=\pm e_\theta\) is orthogonal to the meridional
\(\nabla p_0\), so the rank-one part drops and the azimuthal \(\nu\Delta u_0\) drops with it; with \(u_1=\nu\Delta u_0+m\),
\[
 P_3'(0)=-\langle m,\nabla p_0\rangle_\rho=\int p_0\,m\cdot\nabla\rho ,
\]
which is (2.5), \(\nu\)-independent (the last equality by \(\operatorname{div}m=0\), \(\rho p_0m\in W^{1,1}\)).
For (2.6) put \(a=\Pi_\rho f=-\nabla\psi\), \(b=\Pi f=\nabla p_0\), both gradients in \(L^2(\rho)\); \(\langle f-a,\nabla\eta\rangle_\rho=0\)
for gradients. Then \(dK/dt(0)=\langle b-a,a\rangle_\rho\), \(-\langle m,\nabla p_0\rangle_\rho=\langle b,b-f\rangle_\rho=\langle b,b-a\rangle_\rho\),
and their difference is \(-\|a-b\|_\rho^2=-\|q_1\|_\rho^2\). The lower bound: \(\|a\|_\rho^2=\langle a,f\rangle_\rho\le\|f\|_\rho\|a\|_\rho\)
gives \(\|a\|_\rho^2\le\|f\|_\rho^2\), so \(\langle b-a,a\rangle_\rho=\langle b,f\rangle_\rho-\|a\|_\rho^2\ge\langle b-f,f\rangle_\rho=-\langle m,f\rangle_\rho\).
\(\square\)

**Remark 2.1 (interpretation of (2.6)).** \(\mathcal Q\le X/3\) with equality on \(\mathcal M\), and at an
\(\mathcal M\)-instant \(\mathcal Q'=X'/3\). Formally \(\mathcal Q(t)=X(t)/3-\tfrac{t^2}2\|q_1\|_M^2+o(t^2)\), consistent
with \(K'-P_3'=-\|q_1\|_\rho^2\): the quotient functional gains over the cubic norm, at second order, exactly the
weighted energy of the gradient part it removes. The gain has the favourable sign but is of the transport
(not viscous) scale.

**Remark 2.2 (the general class).** For a general \(u_0\in\mathcal M\) satisfying (W) the same steps give
\(DK(u_0)[u_1]=DK_E+\nu DK_V\) with \(DK_E=-\langle\nabla\phi_1^E,g\rangle\), \(DK_V=-\langle\nabla\phi_1^V,g\rangle\), where
\(\phi_1^{E},\phi_1^{V}\) solve (1.5) with \(h=\mathbb P(-(u_0\cdot\nabla)u_0)\) and \(h=\Delta u_0\); the viscous part
vanishes exactly when \(\operatorname{div}(M\Delta u_0)=0\), which is the swirl case. Testing (1.5) with \(\phi_1\) gives in
general \(DK(u_0)[h]=-\langle M\nabla\phi_1,\nabla\phi_1\rangle-\langle(\hat u_0\cdot h)(\hat u_0\cdot\nabla\phi_1)\rangle_\rho
-\nu\langle\Delta u_0,\nabla\phi_1\rangle_\rho+\langle\nabla p_0,\nabla\phi_1\rangle_\rho\) for \(h=u_1\): a negative-definite
part plus three cross terms; no sign in general.

## 3. Explicit class: the thin-ring reduction and the constant-speed closed form

Let \(s=S_0\,R(\varrho/a)\) with \(\varrho=\sqrt{(r-r_0)^2+z^2}\), \(R\) supported in \([0,1]\), \(a\ll r_0\). To leading
order in \(a/r_0\) the meridional cross-section is a disk, \(f=S_0^2R^2e_x/r_0\) with \(x=r-r_0\), and both potentials
separate: \(p_0=P(\varrho)\cos\vartheta\), \(\psi=\Psi(\varrho)\cos\vartheta\) (in units \(S_0=a=r_0=1\)), with
\[
 P(\varrho)=\frac1\varrho\int_0^\varrho tR(t)^2dt,\qquad
 (\varrho R\Psi')'-\frac{R\Psi}{\varrho}=-\varrho\,(R^3)'\ \text{on }(0,1),\ \ \text{regular at }0,\ \text{natural at }1,      \tag{3.1}
\]
(the first is the closed-form solution of \(P''+P'/\varrho-P/\varrho^2=(R^2)'\), obtained from the homogeneous
solutions \(\varrho,\varrho^{-1}\); the second is (2.3) with the weight \(R\)), and
\[
 \frac{dK}{dt}(0)=\frac{2\pi a^2S_0^5}{r_0}\,I[R]+O\Big(\frac{a^3S_0^5}{r_0^2}\Big),\qquad
 I[R]:=\pi\int_0^1R^3\big[(\varrho P)'+(\varrho\Psi)'\big]d\varrho ,                                           \tag{3.2}
\]
\(P_3'(0)\) and the bounds with the corresponding angular averages. For the **constant-speed tube** \(R\equiv1\) on the
disk — the lane's nondegenerate class, with a jump at the boundary, hence *outside* the hypotheses of Lemma 1 and
presented as the explicit solution of the limiting weighted problem only — everything is closed-form: \(f\) is
constant on the disk, so \(\Pi_\rho f=f\) (\(\Psi=-\varrho\), \(\psi=-x\)), the unweighted projection is the 2D
depolarising field \(\nabla p_0=f/2\) (\(P=\varrho/2\)), hence
\[
 q_1=\nabla p_0-\Pi_\rho f=-\tfrac12f,\qquad
 I[1]=-\frac\pi2,\qquad
 \frac{dK}{dt}(0)=-\frac{\pi^2a^2S_0^5}{r_0},\qquad P_3'(0)=-\frac{\pi^2a^2S_0^5}{2r_0},\qquad
 \|q_1\|_\rho^2=\frac{\pi^2a^2S_0^5}{2r_0} .                                                                    \tag{3.3}
\]
The first-order gradient correction is half the centrifugal field, inward; \(dK/dt(0)<0\) with the lower bound of (2.6)
attained. The audit verified (3.3) twice independently — once from (3.1) with the natural condition
\(R(1)^3+R(1)\Psi'(1)=0\), and once from the exterior identity of §4 with \(p_0^{\rm ext}=\cos\vartheta/(2\varrho)\),
\(\int_{\rm ext}|\nabla p_0|^2dA=\pi/4\) — and confirms the depolarisation factor \(\tfrac12\) (the circular-cylinder
value, not the spherical \(\tfrac13\)). For smooth radial profiles the ODE (3.1) is solved numerically in §4 and
agrees with the 2D solver as \(a\to0\).

## 4. Bounded numerical nominations (not proof)

All computations: scratchpad `swirl2d.py` (2D axisymmetric, cell-centred conservative finite differences, \(p_0\) on a
box \([0,R]\times[-Z,Z]\) with \(p_0=0\) at the far boundary — quadrupole decay makes the box error \(O((\ell/R)^3)\);
the weighted problem (2.3) on the active cells with face weights \(r\rho\) evaluated from the analytic profile, so
no flux crosses \(\{\rho=0\}\); the discrete identity \(\langle\nabla\psi,f\rangle_\rho+\|\nabla\psi\|_\rho^2=0\) holds to
\(10^{-16}\), and \(dK/dt(0)=P_3'(0)-\|q_1\|_\rho^2\) to \(10^{-15}\)), `thinring.py` (ODE reduction (3.1)),
`check3d.py` (3D periodic box, full nonlinear minimisation of \(\tfrac13\int|u_0+\varepsilon m+\nabla\phi|^3\) by
L-BFGS, \(K\) from three of the forms (0.1), compared with the 3D linear weighted solve on the same grid; periodic
proxy for the variational problem only, never for the evolution). Profiles \(s=S_0B((r-r_0)/a)B(z/b)\times(\text{factor})\),
\(B(x)=(1-x^2)^4_+\) unless stated, \(S_0=r_0=1\).

Convergence of the blob (\(a=b=\tfrac12\)): \(dK/dt(0)=-0.078258\) (\(h=0.04\)), \(-0.078247\) (\(h=0.02\)),
\(-0.078246\) (\(h=0.02\), box doubled); bounds \([-0.1143,-0.0445]\); \(\mathcal Q=0.1290\), \(D_3=19.11\),
\(\|u_0\|_2^2=0.564\), \(\|q_1\|_\rho^2=0.0338\).

| profile | \(dK/dt(0)\) | \(P_3'(0)\) (upper bd) | lower bd | \(\mathcal Q\) | \(D_3\) | \(\frac{dK/dt(0)\,\mathcal Q^{1/3}}{D_3^{2}}\) |
|---|---|---|---|---|---|---|
| blob \(a=b=.5\) | \(-0.0783\) | \(-0.0445\) | \(-0.114\) | 0.129 | 19.0 | \(-1.1\times10^{-4}\) |
| blob, \(B=\exp\)-bump | \(-0.275\) | \(-0.154\) | \(-0.358\) | 0.383 | 28.7 | \(-2.4\times10^{-4}\) |
| thin ring \(a=b=.15\) | \(-0.00743\) | \(-0.00401\) | \(-0.0106\) | 0.0116 | 17.1 | \(-5.8\times10^{-6}\) |
| thin \(a=.1\), \(b=.5\) | \(-0.00677\) | \(-0.00555\) | \(-0.00792\) | 0.0257 | 41.4 | \(-1.2\times10^{-6}\) |
| tall \(a=.5\), \(b=2\) | \(-0.119\) | \(-0.0980\) | \(-0.148\) | 0.516 | 41.1 | \(-5.7\times10^{-5}\) |
| very tall \(a=.3\), \(b=4\) | \(-0.0437\) | \(-0.0397\) | \(-0.0474\) | 0.619 | 125 | \(-2.4\times10^{-6}\) |
| flat \(a=.5\), \(b=.1\) | \(-0.0288\) | \(-0.00576\) | \(-0.0353\) | 0.0257 | 41.4 | \(-5.0\times10^{-6}\) |
| near axis \(r_0=.6\), \(a=.55\) | \(-0.139\) | \(-0.0811\) | \(-0.209\) | 0.0851 | 12.0 | \(-4.3\times10^{-4}\) |
| far \(r_0=3\) | \(-0.0274\) | \(-0.0149\) | \(-0.0394\) | 0.387 | 55.9 | \(-6.4\times10^{-6}\) |
| two lobes \(z_1=.8\) / \(.55\) | \(-0.153\) / \(-0.147\) | \(-0.0886\) / \(-0.0880\) | \(-0.225\) / \(-0.219\) | 0.258 | 38.0 | \(-6.7\times10^{-5}\) |
| counter-rotating lobes | same as two lobes (functional of \(\rho\) only) | | | | | |
| tilted \(c=\pm.8\) | \(-0.0852\) / \(-0.0921\) | \(-0.0490\) / \(-0.0533\) | \(-0.124\) / \(-0.134\) | 0.144 / 0.132 | 22.1 / 20.2 | \(-1\times10^{-4}\) |
| saddle (speed larger at the ends) \(c=3\) / \(10\) | \(-0.111\) / \(-0.494\) | \(-0.0681\) / \(-0.300\) | \(-0.150\) / \(-0.648\) | 0.188 / 0.500 | 23.2 / 74.1 | \(-1\times10^{-4}\) |
| shell (speed larger near the support boundary) \(c=3\) / \(10\) / \(10\), \(a=.2\) | \(-0.137\) / \(-0.652\) / \(-0.180\) | \(-0.0704\) / \(-0.320\) / \(-0.121\) | \(-0.200\) / \(-0.929\) / \(-0.238\) | 0.188 / 0.500 / 0.200 | 23.2 / 74.1 / 96.5 | \(-1\times10^{-4}\) |

Thin-ring ODE (3.1), unit-maximum-normalised \(I[R]\) (\(n=8000\), converged to 5 digits; the weighted energy identity
holds to \(10^{-9}\)): uniform \(-1.5705\) (exact \(-\pi/2=-1.5708\)); \((1-\varrho^2)^4\): \(-0.05259\)
(2D solver on radial rings \(a=0.3,0.15,0.075\): \(dK/dt(0)/(2\pi a^2)=-0.05138,-0.05223,-0.05250\), converging
to the ODE value); \((1-\varrho^2)^2\): \(-0.1047\); \(1-\varrho^2\): \(-0.2054\); \(\sqrt{1-\varrho^2}\): \(-0.3835\);
cores \((1-\varrho^2)^{8,20}\): \(-0.0263,-0.0105\); two-shell: \(-299\) (with \(P_3'\)-bound \(-163\)).
The audit's independent linear finite-element solve of the same weak form (4000 elements, 8-point Gauss, natural
condition at \(\varrho=1\)) reproduces every one of these entries to four digits under unit-maximum normalisation,
and finds \(P_3'(0)/I\in[0.50,0.55]\) (consistent with, and sharper than, the \(0.4\)–\(0.8\) reported below).

**Withdrawn (audit D6): the three shell magnitudes.** The entry previously read "shells
\(\varrho^{2,4,8}(1-\varrho^2)^2\): \(-0.0273,-0.0045,-0.0042\)". These three numbers are **not reproducible as
published**: the audit's solver gives raw \(-2.66\times10^{-5},-3.22\times10^{-7},-1.30\times10^{-9}\); unit-maximum
normalisation \(-0.373,-0.337,-0.256\); fixed-\(\mathcal Q\) normalisation \(-1.99,-2.03,-2.29\); and no inferable
convention reproduces the published triple, although every other entry of the same list reproduces to four digits.
The three magnitudes are therefore withdrawn and are not used anywhere. Only the **sign** survives — negative under
every convention tried, in the audit's computation as in this note's — and no conclusion of this note moves, since
none rests on their size.

3D nonlinear check: see §4.1 (appended when the run completes).

**Mechanism (reading of the sign).** Where the speed is largest the centrifugal field \(f\propto\rho^2\) dominates its own
Leray gradient part \(\nabla p_0\) (a nonlocal average of \(f\)), so \(m=f-\nabla p_0\) is aligned with \(\nabla p_0\)
there: the secondary circulation flows *up* the pressure gradient exactly where the weight \(\rho\) is large, giving
\(\langle m,\nabla p_0\rangle_\rho>0\), i.e. \(P_3'(0)<0\); the negative contributions of \(m\cdot\nabla p_0\) live where
\(\rho\) is small (low-pressure return flow at the ends of the vortex, \(\rho=0\) on the axis). The correction
\(-\|q_1\|_\rho^2\) only lowers \(dK/dt(0)\) further. For \(\rho\equiv\rho_0\) on its support one has exactly
\(\langle m,\nabla p_0\rangle_\rho=\rho_0\int_{\Omega'^c}|\nabla p_0|^2>0\) (since \(\int_{\mathbb R^3}m\cdot\nabla p_0=0\) and
\(m=-\nabla p_0\) off the support; this identity was independently re-verified by the audit), which explains the
robustness for profiles close to constant speed; no proof for general \(\rho\) is claimed (§6).

## 5. Consequences for the target ("monotone/Lyapunov mechanism for \(\mathcal Q\)")

**5.1 (rigorous, unconditional) The target is refuted: Clay data with \(K>0\).**
By (0.5), for any solenoidal \(u\) with \(K(u)\ne0\), one of \(\pm u\) has \(K>0\), and then
\(\mathcal Q'(0)=a^4K(u)-a^3\nu D_3(w(u))>0\) for the datum \(au\), \(a>\nu D_3/K\). So *any* nonzero value of \(K\) refutes
monotonicity of \(\mathcal Q\) for large data at time zero; this is what "sharp by scaling" in the packet already
encodes, and it is not a new obstruction to the first gap. What this lane adds is that such a datum is now
exhibited **without numerical input**, from Lemma 1 itself.

**Proposition 5.1 (audit R4).** There exist \(U,h\in C_c^\infty(\mathbb R^3;\mathbb R^3)\) with
\(\operatorname{div}U=\operatorname{div}h=0\), \(U\in\mathcal M\), \(U\ne0\), such that
\[
 K(U+\varepsilon h)=-\varepsilon\|U\|_3^3+o(\varepsilon),\qquad\varepsilon\to0 .                                \tag{5.1}
\]
In particular \(K(U-\varepsilon h)>0\) for all small \(\varepsilon>0\): smooth compactly supported solenoidal fields
with \(K\ne0\) exist, and this subsection holds with no numerical input.

*Proof.* Take the explicit pair of the HF20 candidate (§3 there), whose stated properties are verified directly
here and which is used only as a displayed pair of fields, not as an imported theorem: with \(b(t)=e^{-1/(1-t^2)}\),
\(s(r,z)=b(4r-6)b(2z)\), put \(U=s\,e_\theta\) (support in \(5/4\le r\le7/4\), \(|z|\le1/2\), so \(U\) is smooth,
compactly supported away from the axis, and \(U\in\mathcal M\) by (0.4)); with \(\chi=1\) on \(B_3\), \(\chi=0\) off
\(B_4\), \(a=(yz,-xz,0)\), \(\Phi=(x^2+y^2)/2-z^2\), put \(h=\operatorname{curl}(\chi a)\). Then \(h\) is smooth,
compactly supported and solenoidal, and on a neighbourhood of \(\operatorname{supp}U\) one has
\(h=\nabla\Phi=(x,y,-2z)\). \(U\) satisfies (W) (infinite-order vanishing), so Lemma 1 applies, with Lemma 1.2 and
Lemma 1.3 in place of the former Steps 3–4. Since \(h=\nabla\Phi\) on \(\Omega'=\{U\ne0\}\) with \(\Phi\) smooth and
bounded there, \(\nabla\phi_1:=-h|_{\Omega'}\) lies in \(L^2(\rho)\), has a potential in \(L^2_{\rm loc}(\Omega')\),
and solves \(\operatorname{div}(M(h+\nabla\phi_1))=0\); by Lemma 1.3 it is *the* solution. Hence, by (1.6),
\[
 DK(U)[h]=-\langle\nabla\phi_1,g\rangle=\langle h,g\rangle=\int\rho\,h\cdot\big((U\cdot\nabla)U\big)
 =\int\rho\,(x,y,-2z)\cdot\Big(-\frac{\rho^2}{r}e_r\Big)=-\int\frac{\rho^3}{r}\,r=-\|U\|_3^3 ,
\]
using \((x,y,-2z)\cdot e_r=(x^2+y^2)/r=r\) on \(\operatorname{supp}U\). Lemma 1(c) then gives (5.1). \(\square\)

*(Bounded evidence, not part of the above.)* For the swirl profiles of §4 with \(dK/dt(0)=DK(u_0)[m]<0\)
(numerically established, every tested profile), a second family of such data is
\(u_0-\varepsilon h_R\) with \(h_R:=\operatorname{curl}(\chi_R\Psi_mr^{-1}e_\theta)\), \(\Psi_m\) the Stokes stream
function of \(m\) and \(\chi_R\) a cutoff; \(h_R\) is smooth, compactly supported, solenoidal, axisymmetric
meridional, and \(h_R\to m\) in \(L^3\) (\(m=O(|x|^{-4})\)), so by Lemma 1(c) and the \(L^3\)-continuity of
\(DK(u_0)[\cdot]\),
\[
 K(u_0-\varepsilon h_R)=\varepsilon\,|DK(u_0)[m]|\,(1+o_R(1))+o(\varepsilon) .                                 \tag{5.1'}
\]
Its positivity depends on the numerical value \(DK(u_0)[m]\ne0\) and is therefore evidence, not proof; the
unconditional statement of this subsection is Proposition 5.1. For the blob, \(|DK(u_0)[m]|=0.078\), so
\(\mathcal Q'(0)>0\) for \(a(u_0-\varepsilon h_R)\) once \(a\gtrsim\nu D_3/(0.078\,\varepsilon)\approx2.4\times10^3\nu/\varepsilon\).

**5.2 (rigorous given the tested sign) Along the trajectory from \(\mathcal M\).** By (1.8) and Theorem 2, for every tested \(u_0\),
\[
 \mathcal Q'(t)=-\nu D_3(w(t))-t\,\big|DK(u_0)[m]\big|+o(t),\qquad D_3(w(t))\to D_3(u_0),
\]
so \(\mathcal Q\) is strictly decreasing on an initial interval with a *negative* second-order correction, for every
\(\nu>0\); the flow leaves \(\mathcal M\) on the side where the transport term is a sink (the identity is exact; the
sign of \(DK(u_0)[m]\) on the tested profiles is numerical). Reversing the Euler direction
(\(u_0-\varepsilon h_R\), (5.1')) shows that trajectories reaching \(\mathcal M\) do so from the \(K>0\) side and exit on the
\(K<0\) side, to first order. Had \(DK(u_0)[m]\) been positive, (1.8) with the scaling of §0 would have given
\(\mathcal Q'\) crossing zero at \(t_*\approx\nu D_3(u_0)/DK(u_0)[m]\), an \(O(\mathrm{Re}^{-1})\) fraction of the turnover
time, inside the range of validity of the expansion for large Re (uniformity in \(\nu\) of the remainders would then
have to be imported from the uniform-in-\(\nu\) local theory [MO]); this is the quantification the lane asked for,
and it is not realised on the tested class.

**5.3 Size.** In all examples \(|dK/dt(0)|\,\mathcal Q^{1/3}/D_3^2\sim10^{-4}\)–\(10^{-6}\), far below the scaling-allowed
\(O(1)\); this mirrors the HF18-A audit's \(|K|/(\mathcal Q^{1/3}D_3)\approx2.5\times10^{-4}\) for a generic field and the
fact that \(D_3\) is dominated by gradient energy. It is a property of these examples, not a bound.

**5.4 What this does not do.** The first gap of the packet is a time-integrated, input-only bound for
\(\int_0^\tau K\,dt\) along arbitrary trajectories. Everything above is instantaneous and local to \(\mathcal M\); an
identity for \(dK/dt\) at one instant, however favourable its sign, is exactly the "instantaneous fact promoted to a
time-integrated one" the packet forbids, and the gap is untouched. In particular the sign \(dK/dt(0)<0\) on
\(\mathcal M\) does not bound \(K\) away from \(\mathcal M\), where by (5.1) it is positive at first order on one side.

**5.5 Relation to HF20 (consistency, not an audit).** Proposition 5.1 evaluates this note's data-space functional
\(DK(U)[\cdot]\) at the direction displayed in the HF20 candidate and obtains \(-\|U\|_3^3\), the same first-order
coefficient HF20 obtains by a competitor-gradient argument that never linearises — two different derivative-free
forms of \(K\) of (0.1), with the minimizer handled in two different ways. The two notes are consistent on the
data-space / flow distinction as well: Lemma 1 is a Gateaux derivative in data space, Lemma 1.4 evaluates it at the
one distinguished direction \(u_1=u_t(0)\) and pays \(O(t^{3/2})\), whereas HF20 evaluates a harmonic-gradient
direction and rescales the perturbed datum before invoking the flow. There is no contradiction with Theorem 2's
negative \(\langle(\Pi-\Pi_\rho)f,f\rangle_\rho\): \(DK(u_0)[\cdot]\) is a linear functional, negative on \(m\) and on
\(h\), positive on \(-m\) and \(-h\). Nothing of HF20 is imported or audited here beyond the two displayed fields,
whose stated properties are verified in the proof.

## 6. Frontier record

**MODE / RESULT:** FALSIFY. The target mechanism ("monotone functional of \(\mathcal Q\) alone") is **refuted**,
unconditionally: by oddness (0.5) together with Proposition 5.1, which supplies a smooth compactly supported
solenoidal datum with \(K\ne0\) and hence \(\mathcal Q'(0)>0\) at large amplitude. The lane's sharper question —
whether the *dynamics through \(\mathcal M\)* produce the failure at second order — is
answered negatively on the whole tested swirl class: \(dK/dt(0)<0\), with the explicit formula (2.4), the
\(\nu\)-independence, and the exact link (2.6) to the pressure route. That negative answer is what "the intended
refutation did not occur" refers to; the target itself does not survive. The lane's Goal B (\(dK/dt(0)\le0\) on
\(\mathcal M\)) is reduced to the sign of the minimizer-free functional \(P_3'(0)=\int p_0\,m\cdot\nabla|u_0|\), nominated
negative on the swirl class (21 profiles, ODE reduction, closed form (3.3)); not proved.

**AUDIT:** `hf19-review-second-order-falsifier.md`, verdict REPAIR; repairs R1–R4 and D3–D6, D8 applied here on
2026-09-06. Two statements upgraded from conditional to unconditional (Lemma 1's gradient structure, §5.1). No claim
refuted. No node of the graph is promoted; `hyp:highstrain` and `hyp:highpressure` are untouched.

**CLAIM AND SCOPE:** Lemma 1 (Steps 1–4, Lemma 1.2, Lemma 1.3, (1.5)–(1.6)) for every \(u_0\in\mathcal M\cap H^m\),
\(m\ge4\), **satisfying (W)**, every open \(\Omega'\) (no simple connectivity, no symmetry, no hypothesis
(H\(_\Omega\)) — that hypothesis is deleted, being a theorem: Lemma 1.2), and every \(h\in H^m\), for the functional
\(K=-\int q\cdot((A\cdot\nabla)u)\) of (0.1), which coincides with the transport term on solenoidal directions
(Remark 1.5); Lemma 1.4 and (1.8) for classical trajectories from Schwartz data in \(\mathcal M\) (Lemma 1 cited
there at \(m\ge5\) or Schwartz, per D4); Theorem 2 (i)(ii)(iii), (2.4)–(2.6) and Remark 2.1 for smooth compactly
supported (or Schwartz) swirl fields, including the exact link \(dK/dt(0)=P_3'(0)-\|q_1\|_\rho^2\), the two-sided
bound, and the \(\nu\)-independence of both \(dK/dt(0)\) and \(P_3'(0)\); (3.3) for the constant-speed thin tube as
the explicit solution of the limiting weighted problem only (still outside Lemma 1's hypotheses), together with the
exterior identity \(\langle m,\nabla p_0\rangle_\rho=\rho_0\int_{\Omega'^c}|\nabla p_0|^2>0\) for constant speed;
(0.4), (0.5) and §5.1 Proposition 5.1 rigorous as stated. §5.2 is rigorous as an identity; its sign input on the
tested class is numerical.

**EVIDENCE:** monotonicity/Lipschitz inequalities (0.2) and the stability lemma [DI, audited, and re-verified
numerically by the audit] for the weighted a-priori bound (1.3), which replaces differentiation of the minimizer;
the Euler–Lagrange condition against the whole closed gradient space for Step 2; weak compactness in \(L^2(\rho)\)
and de Rham duality (vanishing periods of weak limits of exact forms) for Step 3 — the distance function \(d\) and
the bound \(\rho\le\operatorname{Lip}(u_0)d\) are no longer used anywhere; the weight-built logarithmic cutoff with
hypothesis (W) for Step 4; the manuscript's package (R) for Lemma 1.4; elementary Hilbert-space algebra for (2.6);
the depolarisation factor \(\tfrac12\) of the disk for (3.3), verified twice. Numerics: 2D solver with two grid
sizes and two box sizes (agreement \(2\times10^{-4}\)), discrete identities to roundoff; ODE reduction converging to
the 2D solver as \(a\to0\) (\(0.2\%\)) and reproducing \(-\pi/2\) for the uniform tube; independent re-solve of the
whole ODE column by the audit, agreeing to four digits except for the three withdrawn shell magnitudes (§4); a
direct maximisation of \(I[R]\) over \(R=z^2\ge0\) by the audit (401 nodes, L-BFGS-B, six starts) which found no
positive value. All of this is bounded evidence at finite resolution, never proof. Sources: Lindqvist [DI, via
HF18-A and its audit] for (0.2); Kato's uniform-in-\(\nu\) local theory [MO], used only in the non-load-bearing
remark of §5.2 (confirmed non-load-bearing by the audit).

**FIRST GAP:** unchanged — the input-only spacetime bound
\(\int_0^\tau K\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+M\int_0^\tau\mathcal Q\,dt+A_{\rm input}\), uniformly for
\(\tau<\min(H,T_*)\), \(\theta\le1\). The present note supplies no input on it: its first unsupported implication
would be "\(dK/dt<0\) on \(\mathcal M\) (instantaneous, local) ⟹ any control of \(\int K\) away from \(\mathcal M\)", which is
false as stated by (5.1). Within the lane, the open implication is
"\(P_3'(0)=\int p_0\,m\cdot\nabla|u_0|\le0\) for every \(u_0\in\mathcal M\)" (would give Goal B via (2.6) on the swirl class);
supported by every example and by the constant-speed identity, not proved.

**SURVIVING CONDITIONAL SUFFIX:** if \(P_3'(0)\le0\) on the swirl class, then \(dK/dt(0)\le P_3'(0)\le0\) there (Theorem 2),
i.e. \(\mathcal M\)-instants of swirl trajectories are strict local maxima of \(K\) along the flow at second order,
and \(\mathcal Q'(t)\le-\nu D_3(w(t))+o(t)\). Nothing further follows for the gap.

**NON-CLAIMS:** no bound, sign, or time-integrated absorption for \(K\) off \(\mathcal M\); no monotonicity or Lyapunov
property of \(\mathcal Q\) for any class of data (at large amplitude it is false at time zero by §5.1); no statement
about \(\mathcal Q''(0)\) (the derivative of \(D_3(w(t))\) is not controlled); no differentiability of \(u\mapsto q(u)\) in
\(L^3\) (only the weak \(L^2(\rho)\)-convergence of difference quotients on \(\{u_0\ne0\}\)); no rate for
\(q_\varepsilon\) off \(\{u_0\ne0\}\) beyond \(O(\varepsilon^{2/3})\) in \(L^3\); no claim for \(u_0\) violating (W)
(the hypothesis is explicit in Lemma 1 and is not known to hold for every \(u_0\in\mathcal M\cap H^m\)); no
general-\(\mathcal M\) sign (Remark 2.2 has indefinite cross terms); no proof of \(P_3'(0)\le0\); no first-order
expansion of the other forms of (0.1) for non-solenoidal directions (Remark 1.5); no magnitude for the three shell
entries withdrawn in §4, only their sign; no HIGH-STRAIN, HIGH-PRESSURE, continuation or regularity result; no
novelty claim for the linearisation of a nonlinear Hodge problem, for Lemma 1.2 (standard de Rham duality) or for
Lemma 1.3 (a standard degenerate-weight "\(H=W\)" argument with an explicit sufficient condition). Numerics are
bounded evidence at finite resolution; the periodic box is a proxy for the variational problem only. NS-R3 remains
OPEN. *(Superseded non-claim, recorded for the history: the earlier item "no treatment of non-simply-connected
supports without symmetry (harmonic component)" is void — Lemma 1.2 covers that case unconditionally, which is why
the hypothesis it hedged has been deleted rather than weakened.)*

**REOPENING CONDITIONS (from the audit):** (1) a \(u_0\in\mathcal M\cap H^m\) for which (W) fails and for which the
homogeneous weighted problem \(\operatorname{div}(M\nabla\phi)=0\), \(\nabla\phi\in L^2(\rho)\), has a nonzero solution
(a Lavrentiev gap for this weight) — this would restrict Lemma 1 further, without affecting any profile used here;
(2) a solenoidal \(h\in H^m\) and \(u_0\in\mathcal M\) for which two forms of (0.1) have different first-order parts,
which would break Remark 1.5 and hence (1.6); (3) a thin-ring profile \(R\ge0\) with \(I[R]>0\), or a smooth swirl
\(u_0\in\mathcal M\) with \(P_3'(0)>0\) — this would not invalidate Lemma 1, Lemma 1.4 or Theorem 2, since (2.6) is
sign-free, but it would retire Goal B and change the next action; (4) a refutation of the coefficient
\(\|U\|_3^3\) for the displayed \(U,h\), which would force re-examination of Lemma 1 through Proposition 5.1;
(5) any later use of \(dK/dt(0)<0\) as an input to a bound on \(\int_0^\tau K\,dt\) — not available at any scope
(§5.4).

**NEXT DISTINCT ACTION:** prove or refute \(\int p_0\,m\cdot\nabla|u_0|\le0\) on the swirl class (equivalently
\(\int\rho|\nabla p_0|^2\le\int\rho^3\partial_rp_0/r\) with \(\Delta p_0=r^{-1}\partial_r\rho^2\)), a minimizer-free
weighted-potential inequality; the constant-speed identity and the two-parameter scaling of §0 are the first tools
(a scaling-consistent counterexample would need the low-speed return flow to dominate the weighted pressure work).
Equivalent forms worth carrying, from the audit: with \(a=\Pi_\rho f\), \(b=\Pi f\) the nomination is
\(\langle b,b-a\rangle_\rho\le0\), and \(dK/dt(0)=-\langle m,f\rangle_\rho+\min_{\nabla}\|f-\nabla\|_\rho^2\), which
makes the lower bound of (2.6) the statement \(\min\ge0\) and the upper bound the choice \(\nabla=\nabla p_0\).
Independently, and more relevant to the gap: since \(K\) is odd and first-order in the distance to \(\mathcal M\),
seek the *time-integrated* sign structure — whether \(\int_0^\tau K\,dt\) along trajectories that cross \(\mathcal M\)
is controlled by the crossing values — as a test of the "cancellation, not size" strategy recorded in HF18.
