# HF19-B: second-order behaviour of the transport term on the nonlinear-Hodge class

Lane HF19-B, MODE: FALSIFY, 2026-09-05. Inputs [DI]: PLAN.md ("Frontier packet",
"Beyond the checkpoint", "HF16–HF17", "HF18"); manuscript `sec:quotient` of
`../navier-paper/main.tex` (labels `lem:quotient-minimizer`, `lem:quotient-coercive`,
`lem:quotient-stability`, `prop:quotient-derivative`, `lem:quotient-chainrule`,
`lem:quotient-heatsign`, `lem:quotient-transport`, `prop:quotient-evolution`,
`lem:quotient-lowstrain`, `hyp:highstrain`, `prop:quotient-conditional`);
`hf17-quotient-functional.md`, `hf17-quotient-evolution.md`, `hf18-hodge-regularity.md`
with `hf18-review-hodge-regularity.md` (PASS), `hf18-divergence-speed-link.md` with its two
reviews (REPAIR, then PASS with S1–S4 applied). Source tags: [DI] directly inspected in this
programme; [MO] metadata only or from memory, never load-bearing.

**MODE / RESULT: FALSIFY, target "a monotone/Lyapunov mechanism for \(\mathcal Q\)"; outcome:
the second-order expansion on \(\mathcal M\) does NOT produce the sought failure — on every
tested member of the explicit swirl class the transport term leaves \(\mathcal M\) with the
favourable sign, \(dK/dt(0)<0\).** What is proved: an exact first-order expansion of \(K\) at
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
datum with \(K\ne0\), and the family \(u_0-\varepsilon h\) (\(h\) a compactly supported
solenoidal approximation of \(m\)) supplies Clay data with \(K=\varepsilon|K'(0)|+o(\varepsilon)>0\);
(ii) along the actual trajectory from a tested \(u_0\in\mathcal M\),
\(\mathcal Q'(t)=-\nu D_3(w(t))-t|K'(0)|+O(t^{3/2})\): no failure of monotonicity is produced
near \(\mathcal M\) by second-order dynamics. Nothing here touches the first gap.

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
\(dK/dt\sim(a^5,\lambda^4)\sim D_3^2\mathcal Q^{-1/3}\), and \(\nu D_3\cdot(\nu D_3/\mathcal Q)\sim(a^4\nu^2,\lambda^4)\).
The dimensionless ratio of the transport-driven second-order rate to the viscous one is
therefore \((dK/dt)/(\nu^2D_3^2/\mathcal Q)\sim\mathcal Q^{2/3}/\nu^2\sim\mathrm{Re}^2\).

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

### Step 2 (the linearised equation, tested inside \(\Omega'\))

\(D\tilde A(z)=|z|I+z\otimes\hat z\) is positively 1-homogeneous and smooth on the sphere, hence globally Lipschitz;
so \(|\tilde A(z')-\tilde A(z)-D\tilde A(z)(z'-z)|\le C_L|z'-z|^2\). For \(\eta\in C_c^\infty(\Omega')\), \(c:=\min_{\operatorname{supp}\eta}\rho>0\), and
\(0=\langle A_\varepsilon-A_0,\nabla\eta\rangle=\varepsilon\langle M\omega_\varepsilon,\nabla\eta\rangle+\langle R_\varepsilon,\nabla\eta\rangle\) with
\(|\langle R_\varepsilon,\nabla\eta\rangle|\le C_L\|\nabla\eta\|_\infty\int_{\{\rho\ge c\}}|w_\varepsilon-u_0|^2\le8C_LC_1^2\|\nabla\eta\|_\infty\varepsilon^2/c\).
Hence \(\langle M\omega_\varepsilon,\nabla\eta\rangle=O(\varepsilon)\to0\).

### Step 3 (weak limit)

By Step 1 a subsequence \(\omega_{\varepsilon_j}\rightharpoonup\omega\) in \(L^2(\rho)\). Since
\((I+\hat u_0\otimes\hat u_0)\nabla\eta\in L^2(\rho)\), Step 2 gives
\[
 \int_{\Omega'}\rho\,(I+\hat u_0\otimes\hat u_0)\,\omega\cdot\nabla\eta\,dx=0\qquad(\eta\in C_c^\infty(\Omega')).    \tag{1.4}
\]
Moreover \(\omega-h=\lim q_{\varepsilon_j}/\varepsilon_j\) weakly in \(L^2_{\rm loc}(\Omega')\) (on compacts \(\rho\ge c\)), so
\(\operatorname{curl}(\omega-h)=0\) in \(\mathcal D'(\Omega')\).

**Hypothesis (H\(_\Omega\)).** Every curl-free field in \(L^2_{\rm loc}(\Omega')\) arising as such a limit is a gradient
\(\nabla\phi\), \(\phi\in L^2_{\rm loc}(\Omega')\). This holds if \(\Omega'\) is simply connected, and it holds in the
axisymmetric class: if \(u_0\) and \(h\) are axisymmetric then so is \(u_\varepsilon\), the minimizer \(q_\varepsilon\)
is axisymmetric by uniqueness and rotation invariance of \(\mathcal G_3\) and of \(F\), and its potential
\(\phi_\varepsilon\) (a genuine function on \(\mathbb R^3\), since \(q_\varepsilon\) is an \(L^3\)-limit of gradients of
\(C_c^\infty\) functions) satisfies \(\phi_\varepsilon\circ R_\alpha=\phi_\varepsilon+c(\alpha)\) with \(c\) additive and
\(2\pi\)-periodic, hence \(c\equiv0\); so \(q_\varepsilon\) is meridional, and the weak limit of \(q_\varepsilon/\varepsilon\) is a
meridional axisymmetric curl-free field on the solid torus \(\Omega'\), which is the gradient of a single-valued
axisymmetric function (the harmonic 1-form \(d\theta\) has an \(e_\theta\) component). In general (non-simply-connected
\(\Omega'\), no symmetry) the limit may contain a harmonic component fixed by the exterior problem; this case is
not needed here and is left open.

### Step 4 (uniqueness in the weighted class; "\(H=W\)" for the degenerate weight)

Let \(\nabla\phi\in L^2(\rho)\) satisfy \(\int_{\Omega'}M\nabla\phi\cdot\nabla\eta=0\) for all \(\eta\in C_c^\infty(\Omega')\).
Then \(\nabla\phi=0\). *Proof.* \(u_0=0\) on \(\partial\Omega'\) and \(u_0\) is Lipschitz, so
\(\rho(x)\le\|\nabla u_0\|_\infty\,d(x)\), \(d=\operatorname{dist}(\cdot,\partial\Omega')\), and \(\rho\) is bounded. Let
\(\phi_N=\max(-N,\min(\phi,N))\) and \(\zeta_\delta=\min\{1,\log(d/\delta^2)/\log(1/\delta)\}_+\) (so \(\zeta_\delta=0\) on
\(\{d\le\delta^2\}\), \(=1\) on \(\{d\ge\delta\}\), \(|\nabla\zeta_\delta|\le1/(d\log(1/\delta))\)), times a cutoff at
\(|x|=R\) if \(\Omega'\) is unbounded. Testing with \(\eta=\zeta_\delta\phi_N\) (admissible by mollification):
\(\int\zeta_\delta M\nabla\phi\cdot\nabla\phi_N=-\int\phi_N M\nabla\phi\cdot\nabla\zeta_\delta\). The left side tends to
\(\int M\nabla\phi_N\cdot\nabla\phi_N\ge\int\rho|\nabla\phi_N|^2\); the right side is bounded by
\(2N\big(\int_{\{d<\delta\}}\rho|\nabla\phi|^2\big)^{1/2}\big(\int_{\{\delta^2<d<\delta\}}\rho|\nabla\zeta_\delta|^2\big)^{1/2}\), and
\(\int_{\{\delta^2<d<\delta\}}\rho|\nabla\zeta_\delta|^2\le\|\nabla u_0\|_\infty\log(1/\delta)^{-2}\int_{\{\delta^2<d<\delta\}}d^{-1}dx
\le C\log(1/\delta)^{-1}\to0\) (coarea over the Lipschitz level sets of \(d\) on a bounded region), while the first factor
tends to \(0\) as well. Hence \(\nabla\phi_N=0\) for every \(N\), so \(\nabla\phi=0\). (If \(\Omega'\) is unbounded the
radial cutoff contributes \(N^2R^{-2}\int_{R<|x|<2R}\rho\to0\) since \(\rho\in L^1\) is not needed: \(\rho\in L^3\) and
\(|\{R<|x|<2R\}|^{2/3}R^{-2}\to0\).) \(\square\)

The same argument shows that (1.4) then holds for every test gradient \(\nabla\eta\in L^2(\rho)\) (replace \(\eta\) by
\(\zeta_\delta\eta_N\) and pass to the limit).

### Lemma 1 (first-order expansion of \(K\) on \(\mathcal M\))

Under (H\(_\Omega\)) the following hold.

(a) *The linearised nonlinear-Hodge problem* — find \(\nabla\phi_1\in L^2(\rho)\), \(\phi_1\in L^2_{\rm loc}(\Omega')\), with
\[
 \operatorname{div}\big(M\,(h+\nabla\phi_1)\big)=0\ \text{in }\mathcal D'(\Omega'),\qquad
 M=\rho(I+\hat u_0\otimes\hat u_0),                                                                   \tag{1.5}
\]
has exactly one solution (up to constants). It is the \(M\)-orthogonal projection: \(-\nabla\phi_1\) minimises
\(\int_{\Omega'}M(h+\nabla\phi)\cdot(h+\nabla\phi)\) over the \(L^2(\rho)\)-closure of \(\nabla C_c^\infty(\Omega')\)
(Riesz), and Step 4 identifies it with any solution in the larger class. This is the linearisation of
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

*Proof.* (a), (b) are Steps 1–4. For (c), by (0.1), \(K(u_\varepsilon)=-\langle q_\varepsilon,G_\varepsilon\rangle\) with
\(G_\varepsilon:=(A_\varepsilon\cdot\nabla)u_\varepsilon\), and \(q_\varepsilon=(w_\varepsilon-u_0)-\varepsilon h\), so
\[
 K(u_\varepsilon)=-\langle w_\varepsilon-u_0,\,g\rangle-\langle w_\varepsilon-u_0,\,G_\varepsilon-g\rangle+\varepsilon\langle h,g\rangle+\varepsilon\langle h,G_\varepsilon-g\rangle .
\]
Now \(G_\varepsilon-g=((A_\varepsilon-A_0)\cdot\nabla)u_\varepsilon+\varepsilon(A_0\cdot\nabla)h\) and, by
\(|\tilde A(z)-\tilde A(z')|\le(|z|+|z'|)|z-z'|\) (`lem:cubic-pointwise`) and (1.3),
\(\int|w_\varepsilon-u_0||A_\varepsilon-A_0||\nabla u_\varepsilon|\le\|\nabla u_\varepsilon\|_\infty\int(|w_\varepsilon|+\rho)|w_\varepsilon-u_0|^2=O(\varepsilon^2)\)
and \(\varepsilon\int|w_\varepsilon-u_0|\rho^2|\nabla h|\le\varepsilon\|\nabla h\|_\infty\|w_\varepsilon-u_0\|_{L^2(\rho)}\|\rho\|_3^{3/2}=O(\varepsilon^2)\);
also \(|\langle h,G_\varepsilon-g\rangle|\le\|h\|_3\|G_\varepsilon-g\|_{3/2}=O(\varepsilon)\) by the stability lemma. Finally
\(\langle w_\varepsilon-u_0,g\rangle=\varepsilon\langle\omega_\varepsilon,(u_0\cdot\nabla)u_0\rangle_\rho\to\varepsilon\langle h+\nabla\phi_1,g\rangle\)
by (b) and (1.2). Collecting, \(K(u_\varepsilon)=-\varepsilon\langle\nabla\phi_1,g\rangle+o(\varepsilon)\). The bound on
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
So \(K(u(t))=K(u_0+tu_1)+O(t^{3/2})\), and Lemma 1(c) with \(h=u_1\in H^m\) finishes. \(\square\)

Since \(\mathcal Q'=K-\nu D_3(w)\) and \(t\mapsto D_3(w(t))=D_{\mathcal Q}(u(t))\) is continuous
(`lem:quotient-heatsign`),
\[
 \mathcal Q'(t)=t\,\frac{dK}{dt}(0)-\nu D_3(w(t))+o(t),\qquad D_3(w(t))\to D_3(u_0) .                         \tag{1.8}
\]
No claim about \(\mathcal Q''(0)\) is made (it would need the derivative of \(D_3(w(t))\), which the weighted bound
(1.3) does not control near \(\partial\Omega'\)).

## 2. The swirl class: explicit derivative, \(\nu\)-independence, and the pressure-route link

Let \(u_0=s(r,z)\,e_\theta\) with \(s\) smooth, compactly supported in \(\{r>0\}\) (or Schwartz with the obvious
changes). Then \(\operatorname{div}(|s|s\,e_\theta)=r^{-1}\partial_\theta(|s|s)=0\), so \(u_0\in\mathcal M\) (HF18-A audit
R5(i)), \(\rho=|s|\), \(\hat u_0=\pm e_\theta\), \(\Omega'=\{s\ne0\}\) a solid torus, and
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
\(m=O(|x|^{-4})\), \(p_0=O(|x|^{-3})\) (quadrupole: monopole and dipole moments of \(\operatorname{div}f\) vanish).

### Theorem 2

Let \(u_0=s\,e_\theta\) as above, \(\rho=|s|\), \(f=(s^2/r)e_r\), \(\langle\cdot,\cdot\rangle_\rho\) the weighted pairing on
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

*Proof.* (i) \(h=u_1=\nu\Delta u_0+m\) is axisymmetric, so (H\(_\Omega\)) holds (Step 3). The linearised problem
(1.5) is linear in \(h\). For \(h=\nu\Delta u_0\) (azimuthal, \(\theta\)-independent), \(M h=2\rho\nu(\Delta u_0)_\theta e_\theta\)
and \(\int Mh\cdot\nabla\eta=\int2\rho\nu(\Delta u_0)_\theta\,r^{-1}\partial_\theta\eta=0\) for every \(\eta\), so
\(\nabla\phi_1=0\) by uniqueness. For \(h=m\) (meridional) and axisymmetric \(\phi_1\), \(M(m+\nabla\phi_1)=\rho(m+\nabla\phi_1)\),
and (1.5) reads \(\operatorname{div}(\rho(m+\nabla\phi_1))=0\); with \(m=f-\nabla p_0\) and \(\psi:=\phi_1-p_0\) this is (2.3).
Uniqueness (Step 4) gives \(\nabla\phi_1=\nabla\psi+\nabla p_0\).
(ii) By (1.6) and (2.1), \(DK(u_0)[u_1]=-\langle\nabla\phi_1,g\rangle=\langle\nabla\phi_1,f\rangle_\rho\). Testing (2.3)
with \(\psi\) (admissible by the end of Step 4, since \(\nabla\psi=\nabla\phi_1-\nabla p_0\in L^2(\rho)\)) gives
\(\langle\nabla\psi,f\rangle_\rho=-\|\nabla\psi\|_\rho^2\), whence (2.4). Lemma 1.4 gives \(dK/dt(0)=DK(u_0)[u_1]\).
(iii) \(P_3(t)=\int p(t)\,u(t)\cdot\nabla|u(t)|\) with \(u,p\in C^1([0,T];H^k)\); \(\partial_t|u|=\hat u\cdot u_t\) where \(u\ne0\)
and \(u\cdot\nabla|u|\) is \(C^1\) in time as an \(L^{3/2}\)-valued map. At \(t=0\), \(u_0\cdot\nabla\rho=0\), so
\(P_3'(0)=\int p_0\big[u_1\cdot\nabla\rho+u_0\cdot\nabla(\hat u_0\cdot u_1)\big]\). For swirl, \(e_\theta\cdot\nabla\rho=0\)
kills the viscous part, and \(u_0\cdot\nabla(\hat u_0\cdot u_1)=(s/r)\partial_\theta(\pm\nu(\Delta u_0)_\theta)=0\). Hence
\(P_3'(0)=\int p_0\,m\cdot\nabla\rho=-\int\rho\,m\cdot\nabla p_0\) (\(\operatorname{div}m=0\), \(\rho p_0m\in W^{1,1}\)).
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

**Remark 2.2 (the general class).** For a general \(u_0\in\mathcal M\) satisfying (H\(_\Omega\)) the same steps give
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
attained. For smooth radial profiles the ODE (3.1) is solved numerically in §4 and agrees with the 2D solver as
\(a\to0\).

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

Thin-ring ODE (3.1), unit-normalised \(I[R]\) (\(n=8000\), converged to 5 digits; the weighted energy identity
holds to \(10^{-9}\)): uniform \(-1.5705\) (exact \(-\pi/2=-1.5708\)); \((1-\varrho^2)^4\): \(-0.05259\)
(2D solver on radial rings \(a=0.3,0.15,0.075\): \(dK/dt(0)/(2\pi a^2)=-0.05138,-0.05223,-0.05250\), converging
to the ODE value); \((1-\varrho^2)^2\): \(-0.1047\); \(1-\varrho^2\): \(-0.2054\); \(\sqrt{1-\varrho^2}\): \(-0.3835\);
shells \(\varrho^{2,4,8}(1-\varrho^2)^2\): \(-0.0273,-0.0045,-0.0042\); cores \((1-\varrho^2)^{8,20}\): \(-0.0263,-0.0105\);
two-shell: \(-299\) (with \(P_3'\)-bound \(-163\)). In every case the upper bound \(P_3'(0)=-\langle m,\nabla p_0\rangle_\rho\)
is itself negative, typically about \(0.4\)–\(0.8\) of \(dK/dt(0)\).

3D nonlinear check: see §4.1 (appended when the run completes).

**Mechanism (reading of the sign).** Where the speed is largest the centrifugal field \(f\propto\rho^2\) dominates its own
Leray gradient part \(\nabla p_0\) (a nonlocal average of \(f\)), so \(m=f-\nabla p_0\) is aligned with \(\nabla p_0\)
there: the secondary circulation flows *up* the pressure gradient exactly where the weight \(\rho\) is large, giving
\(\langle m,\nabla p_0\rangle_\rho>0\), i.e. \(P_3'(0)<0\); the negative contributions of \(m\cdot\nabla p_0\) live where
\(\rho\) is small (low-pressure return flow at the ends of the vortex, \(\rho=0\) on the axis). The correction
\(-\|q_1\|_\rho^2\) only lowers \(dK/dt(0)\) further. For \(\rho\equiv\rho_0\) on its support one has exactly
\(\langle m,\nabla p_0\rangle_\rho=\rho_0\int_{\Omega'^c}|\nabla p_0|^2>0\) (since \(\int_{\mathbb R^3}m\cdot\nabla p_0=0\) and
\(m=-\nabla p_0\) off the support), which explains the robustness for profiles close to constant speed; no proof for
general \(\rho\) is claimed (§6).

## 5. Consequences for the target ("monotone/Lyapunov mechanism for \(\mathcal Q\)")

**5.1 (rigorous) Non-monotonicity at large amplitude is trivial; data with \(K>0\) near \(\mathcal M\).**
By (0.5), for any solenoidal \(u\) with \(K(u)\ne0\), one of \(\pm u\) has \(K>0\), and then
\(\mathcal Q'(0)=a^4K(u)-a^3\nu D_3(w(u))>0\) for the datum \(au\), \(a>\nu D_3/K\). So *any* nonzero value of \(K\) refutes
monotonicity of \(\mathcal Q\) for large data at time zero; this is what "sharp by scaling" in the packet already
encodes, and it is not a new obstruction to the first gap. What the present lane adds is a rigorous family:
for \(u_0=s\,e_\theta\) with \(dK/dt(0)=DK(u_0)[m]<0\) (every tested profile), let
\(h_R:=\operatorname{curl}(\chi_R\Psi_m r^{-1}e_\theta)\) with \(\Psi_m\) the Stokes stream function of \(m\) and \(\chi_R\) a
cutoff; \(h_R\) is smooth, compactly supported, solenoidal, axisymmetric meridional, and \(h_R\to m\) in \(L^3\)
(\(m=O(|x|^{-4})\)). By Lemma 1(c) and the continuity of \(DK(u_0)[\cdot]\) in \(L^3\),
\[
 K(u_0-\varepsilon h_R)=\varepsilon\,|DK(u_0)[m]|\,(1+o_R(1))+o(\varepsilon)>0 ,                                 \tag{5.1}
\]
a Clay (smooth, compactly supported, divergence-free) datum with positive transport term of first order in the
distance to \(\mathcal M\). For the blob, \(|DK(u_0)[m]|=0.078\), so \(\mathcal Q'(0)>0\) for \(a(u_0-\varepsilon h_R)\) once
\(a\gtrsim\nu D_3/(0.078\,\varepsilon)\approx2.4\times10^3\nu/\varepsilon\).

**5.2 (rigorous) Along the trajectory from \(\mathcal M\).** By (1.8) and Theorem 2, for every tested \(u_0\),
\[
 \mathcal Q'(t)=-\nu D_3(w(t))-t\,\big|DK(u_0)[m]\big|+o(t),\qquad D_3(w(t))\to D_3(u_0),
\]
so \(\mathcal Q\) is strictly decreasing on an initial interval with a *negative* second-order correction, for every
\(\nu>0\); the flow leaves \(\mathcal M\) on the side where the transport term is a sink. Reversing the Euler direction
(\(u_0-\varepsilon h_R\), (5.1)) shows that trajectories reaching \(\mathcal M\) do so from the \(K>0\) side and exit on the
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

## 6. Frontier record

**MODE / RESULT:** FALSIFY. The target mechanism ("monotone functional of \(\mathcal Q\) alone") is refuted at large
amplitude trivially by oddness (0.5) plus any datum with \(K\ne0\), of which (5.1) gives an explicit rigorous family;
the lane's sharper question — whether the *dynamics through \(\mathcal M\)* produce the failure at second order — is
answered negatively on the whole tested swirl class: \(dK/dt(0)<0\), with the explicit formula (2.4), the
\(\nu\)-independence, and the exact link (2.6) to the pressure route. The lane's Goal B (\(dK/dt(0)\le0\) on
\(\mathcal M\)) is reduced to the sign of the minimizer-free functional \(P_3'(0)=\int p_0\,m\cdot\nabla|u_0|\), nominated
negative on the swirl class (21 profiles, ODE reduction, closed form (3.3)); not proved.

**CLAIM AND SCOPE:** Lemma 1 (Steps 1–4, (1.5)–(1.6)) for every \(u_0\in\mathcal M\cap H^m\), \(m\ge4\), and
\(h\in H^m\) under (H\(_\Omega\)) (simply connected support, or the axisymmetric class); Lemma 1.4 for classical
trajectories from Schwartz data in \(\mathcal M\); Theorem 2 (2.4)–(2.6) and Remark 2.1 for smooth compactly
supported (or Schwartz) swirl fields; (3.3) for the constant-speed thin tube as the explicit solution of the
limiting weighted problem; (0.4), (0.5), (5.1), (5.2) rigorous as stated.

**EVIDENCE:** monotonicity/Lipschitz inequalities (0.2) and the stability lemma [DI, audited] for the weighted
a-priori bound (1.3), which replaces differentiation of the minimizer; the Euler–Lagrange condition against the
whole closed gradient space for Step 2; weak compactness in \(L^2(\rho)\), the logarithmic cutoff for the degenerate
weight (\(\rho\le\operatorname{Lip}(u_0)\,d\)) for Step 4; the manuscript's package (R) for Lemma 1.4; elementary Hilbert-space
algebra for (2.6); the depolarisation factor \(\tfrac12\) of the disk for (3.3). Numerics: 2D solver with two grid
sizes and two box sizes (agreement \(2\times10^{-4}\)), discrete identities to roundoff; ODE reduction converging to the
2D solver as \(a\to0\) (\(0.2\%\)) and reproducing \(-\pi/2\) for the uniform tube; 3D nonlinear check (§4.1).
Sources: Lindqvist [DI, via HF18-A and its audit] for (0.2); Kato's uniform-in-\(\nu\) local theory [MO], used only in
the non-load-bearing remark of §5.2.

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
property of \(\mathcal Q\) for any class of data (at large amplitude it is false at time zero by 5.1); no statement
about \(\mathcal Q''(0)\) (the derivative of \(D_3(w(t))\) is not controlled); no differentiability of \(u\mapsto q(u)\) in
\(L^3\) (only the weak \(L^2(\rho)\)-convergence of difference quotients on \(\{u_0\ne0\}\)); no rate for
\(q_\varepsilon\) off \(\{u_0\ne0\}\) beyond \(O(\varepsilon^{2/3})\) in \(L^3\); no treatment of non-simply-connected supports
without symmetry (harmonic component); no general-\(\mathcal M\) sign (Remark 2.2 has indefinite cross terms); no
proof of \(P_3'(0)\le0\); no HIGH-STRAIN, HIGH-PRESSURE, continuation or regularity result; no novelty claim for the
linearisation of a nonlinear Hodge problem. Numerics are bounded evidence at finite resolution; the periodic box is a
proxy for the variational problem only. NS-R3 remains OPEN.

**NEXT DISTINCT ACTION:** prove or refute \(\int p_0\,m\cdot\nabla|u_0|\le0\) on the swirl class (equivalently
\(\int\rho|\nabla p_0|^2\le\int\rho^3\partial_rp_0/r\) with \(\Delta p_0=r^{-1}\partial_r\rho^2\)), a minimizer-free
weighted-potential inequality; the constant-speed identity and the two-parameter scaling of §0 are the first tools
(a scaling-consistent counterexample would need the low-speed return flow to dominate the weighted pressure work).
Independently, and more relevant to the gap: since \(K\) is odd and first-order in the distance to \(\mathcal M\),
seek the *time-integrated* sign structure — whether \(\int_0^\tau K\,dt\) along trajectories that cross \(\mathcal M\)
is controlled by the crossing values — as a test of the "cancellation, not size" strategy recorded in HF18.
