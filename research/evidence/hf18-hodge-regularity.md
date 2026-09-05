# HF18-A: Euler–Lagrange structure of the quotient minimizer, weighted dissipation identity, and the transport term

Status: bounded analytic mechanism with self-check, 2026-09-05. Independent audit `hf18-review-hodge-regularity.md`: PASS; the controller applied its wording corrections S1–S3 (the (N2) summary now uses the theorem-grade \(V\) form, the Section 4 sentence on absorption is restricted to what (4.2) proves, and inequality (VI) is labelled) on 2026-09-05. Lane HF18-A of
the Track B frontier packet (PLAN.md "Frontier packet", "HF16–HF17"; inputs
`hf17-quotient-functional.md`, `hf17-quotient-evolution.md` and their two PASS
reviews; manuscript `sec:quotient`).

MODE: DISCOVER, then self-check against the packet falsifiers.

Summary. The minimizer of the cubic quotient solves a 3-Laplace-type equation
whose ellipticity degenerates on the x-dependent set \(\{u+\nabla\phi=0\}\);
none of the cited \(C^{1,\alpha}\) theorems applies as stated, and no such
regularity is claimed. What does survive the shift is the Bojarski–Iwaniec
difference-quotient mechanism, and because the Euler–Lagrange condition holds
against the whole closed gradient space, it can be run globally on
\(\mathbb R^3\) with no cutoff. This proves \(V:=|w|^{1/2}w\in H^1(\mathbb R^3)\),
\(A=|w|w\in W^{1,3/2}(\mathbb R^3)\), the exact identity
\(D_{\mathcal Q}(u)=D_3(w)\) (the heat generator of HF17 is the full weighted
cubic dissipation of the representative), rigorous derivative-free forms of the
transport term, and the scaling-sharp bound \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\).
The bound closes exactly when \(\|w\|_3<\nu/C_*'\) and not otherwise; this is the
critical-norm smallness obstruction, not a new one. HIGH-STRAIN remains open.

## 0. Standing hypotheses, notation, imported facts

Freeze a time on a compact classical interval. Throughout,
\[
 u\in H^m(\mathbb R^3;\mathbb R^3),\quad m\ge4,\qquad \nabla\cdot u=0.  \tag{0.1}
\]
Consequently \(u\in W^{2,3}\cap W^{1,\infty}\), \(u\in L^p\) for \(2\le p\le\infty\),
\(\nabla u\in L^2\cap L^\infty\), \(\Delta u\in L^3\), and \(u\otimes u\in W^{1,3}\).
No preserved rapid decay of \(u\) is used anywhere below; only (0.1).

Notation:
\[
 \tilde A(z)=|z|z,\qquad V(z)=|z|^{1/2}z,\qquad
 \Phi(V)=|V|^{1/3}V,\qquad \Psi(V)=|V|^{-1/3}V\quad(V\ne0),\ \Psi(0)=0.
\]
Thus \(\tilde A=\Phi\circ V\), \(\mathrm{id}=\Psi\circ V\), \(|V(z)|=|z|^{3/2}\),
\(|\Phi(V)|=|V|^{4/3}\). We write \(w=u+q\), \(A=\tilde A(w)\), and, abusing
notation, \(V=V(w)=|w|^{1/2}w\). Difference quotients in direction \(e_k\):
\(\tau_hf(x)=f(x+he_k)\), \(D_hf=(\tau_hf-f)/h\). Summation by parts is exact
for \(f\in L^{3/2}\), \(g\in L^3\):
\[
 \int f\cdot D_{-h}g\,dx=-\int D_hf\cdot g\,dx.                     \tag{0.2}
\]

Imported from HF17 (both audited PASS):

- (E1) \(q\in\mathcal G_3\) is the unique minimizer, \(w\in L^3\), \(A\in L^{3/2}\),
  \(\|A\|_{3/2}=\|w\|_3^2\), \(\|w\|_3^3=3\mathcal Q(u)\).
- (E2) Euler–Lagrange: \(\int A\cdot g=0\) for every \(g\in\mathcal G_3\).
  \(\mathcal G_3\) is translation invariant, so \(D_hg\in\mathcal G_3\) and
  \(D_{-h}D_hg\in\mathcal G_3\) for \(g\in\mathcal G_3\).
- (E3) \(u=\mathbb Pw\), \(q=(I-\mathbb P)w\), with \(C_p:=\|\mathbb P\|_{L^p\to L^p}<\infty\)
  for \(1<p<\infty\); the operators on different \(L^p\) agree on intersections.
- (E4) \(D\mathcal Q(u)[h]=\int A\cdot h\); on the classical interval
  \(\mathcal Q\) is \(C^1\) in time with
  \(\mathcal Q'+\nu D_{\mathcal Q}(u)=-\int q\cdot((A\cdot\nabla)u)\),
  \(D_{\mathcal Q}(u):=-\int A\cdot\Delta u\ge0\).
- (E5) \(\nabla p\in\mathcal G_3\) and, by the same cutoff-and-mollify argument,
  \(\nabla f\in\mathcal G_3\) for every \(f\in W^{1,3}(\mathbb R^3)\); in
  particular \(\nabla(|u|^2/2)\in\mathcal G_3\).

Also used: \(L^{3/2}\) fields \(F\) with \(\nabla\cdot F=0\) in \(\mathcal D'\)
annihilate \(\mathcal G_3\) (the annihilator of the generating set passes to the
\(L^3\)-closure); and, for \(f\in W^{1,1}(\mathbb R^3)\) and \(u\) as in (0.1),
\[
 \int u\cdot\nabla f\,dx=0                                          \tag{0.3}
\]
(density of \(C_c^\infty\) in \(W^{1,1}(\mathbb R^3)\), \(u\in L^\infty\),
\(\nabla\cdot u=0\)).

## 1. The Euler–Lagrange equation and its structure function (Goal 1)

### 1.1 The equation

Every \(q\in\mathcal G_3\) is curl-free in \(\mathcal D'\), hence \(q=\nabla\phi\)
for some \(\phi\in W^{1,3}_{\rm loc}(\mathbb R^3)\) (de Rham; \(\phi\) is
determined up to a constant and lies in BMO). Nothing below uses \(\phi\)
itself; the test class is all of \(\mathcal G_3\). Taking \(g=\nabla\psi\),
\(\psi\in C_c^\infty\), in (E2):
\[
 \int_{\mathbb R^3}a(x,\nabla\phi)\cdot\nabla\psi\,dx=0,\qquad
 a(x,\xi):=|u(x)+\xi|\,(u(x)+\xi)=\tilde A(u(x)+\xi).               \tag{1.1}
\]
So \(\phi\) is a weak solution of \(\operatorname{div}a(x,\nabla\phi)=0\) on
\(\mathbb R^3\), with \(\nabla\phi\in L^3(\mathbb R^3)\) globally, and (E2) says
the weak formulation extends from \(\nabla C_c^\infty\) to its \(L^3\)-closure.

### 1.2 Structure conditions, verified

Write \(z=u(x)+\xi\), \(z'=u(x)+\eta\). All constants are uniform in \(x\).

- Growth: \(|a(x,\xi)|=|z|^2\le2\|u\|_\infty^2+2|\xi|^2\).
- Coercivity: \(a(x,\xi)\cdot\xi=|z|^2z\cdot(z-u)\ge|z|^3-|z|^2|u|
  \ge\tfrac23|z|^3-\tfrac13|u|^3\ge\tfrac16|\xi|^3-\|u\|_\infty^3\).
- Monotonicity (Lindqvist §10 (I) with \(p=3\), directly inspected):
  \[
   (a(x,\xi)-a(x,\eta))\cdot(\xi-\eta)=(\tilde A(z)-\tilde A(z'))\cdot(z-z')
   \ge\tfrac12(|z|+|z'|)|z-z'|^2\ge\tfrac12|\xi-\eta|^3 .            \tag{1.2}
  \]
  Strict monotonicity, uniformly in \(x\); existence and uniqueness are consistent
  with (E1).
- Ellipticity: for \(z\ne0\), \(D_\xi a(x,\xi)=|z|I+z\otimes z/|z|\), eigenvalues
  \(|z|,|z|,2|z|\):
  \[
   |u(x)+\xi|\,|\eta|^2\le D_\xi a(x,\xi)\eta\cdot\eta\le2|u(x)+\xi|\,|\eta|^2. \tag{1.3}
  \]
  The degeneracy set is \(\{\xi=-u(x)\}\), i.e. \(\{w=0\}\), not \(\{\xi=0\}\).
- \(x\)-dependence: \(D_xa(x,\xi)=D\tilde A(z)\,Du(x)\), so
  \(|D_xa(x,\xi)|\le2|z||\nabla u(x)|\le2\|\nabla u\|_\infty(\|u\|_\infty+|\xi|)\).

### 1.3 Exact obstruction to importing the \(C^{1,\alpha}\) theorems

The interior \(C^{1,\alpha}\) theory for \(\operatorname{div}a(x,u,\nabla u)=B\)
with \(p\)-growth (Uraltseva 1968; Uhlenbeck 1977; Evans 1982; DiBenedetto
1983; Lewis 1983; Tolksdorf 1984; Lieberman 1988 — attribution directly
inspected in Lindqvist, *Notes on the p-Laplace equation*, p. 28; the primary
papers were not inspectable through the available fetch channel and are cited
metadata-only) assumes an ellipticity lower bound of the form
\[
 D_\xi a(x,\cdot,\xi)\eta\cdot\eta\ \ge\ \gamma\,(\kappa+|\xi|)^{p-2}|\eta|^2
 \qquad\hbox{for all }\xi,\ \kappa\ge0,                              \tag{1.4}
\]
which degenerates only at \(\xi=0\). For (1.1) with \(p=3\), at any \(x\) with
\(u(x)\ne0\) and \(\xi=-u(x)\), the left side of (1.4) is \(0\) by (1.3) while the
right side is \(\gamma(\kappa+|u(x)|)|\eta|^2>0\). Hence (1.4) fails for every
\(\gamma>0\), \(\kappa\ge0\). The failure is not repairable by a change of the
dependent variable: \(\xi\mapsto\xi+u(x)\) restores isotropy but destroys the
gradient structure, because \(u\) is divergence-free, not curl-free. In the
shifted variable the problem is the first-order system
\[
 \operatorname{div}(|w|w)=0,\qquad \operatorname{curl}w=\operatorname{curl}u\ (\hbox{smooth, nonzero}), \tag{1.5}
\]
a nonlinear Hodge system with inhomogeneous curl. Uhlenbeck's theorem
(metadata-only) covers the closed case \(\operatorname{curl}w=0\). No theorem
directly applicable to (1.5) was found. Consequently:

**Non-claims for Goal 1.** \(\phi\in C^{1,\alpha}_{\rm loc}\), \(w\in C^0\),
\(w\in L^\infty_{\rm loc}\), \(w\in W^{1,1}_{\rm loc}\), \(\phi\in W^{2,2}_{\rm loc}\)
are not established here. (For the unshifted \(p\)-Laplacian in \(\mathbb R^n\),
\(W^{2,2}_{\rm loc}\) holds for \(1<p<3+2/(n-2)\) — Manfredi–Weitsman, Comm. PDE 13
(1988) 651–668, metadata-only, statement confirmed in the directly inspected
citing paper Yu, EJDE 2022/27, p. 2 — which for \(n=3\), \(p=3\) is inside the
range; the extension to the shifted equation (1.1) is plausible but unproved.)

What does survive is the difference-quotient mechanism of Bojarski–Iwaniec
(Lindqvist Theorem 4.1, directly inspected), because the shift \(u\) enters
only through \(D_hu\), which is smooth. Section 1.5 executes it globally.

### 1.4 Lemma V (pointwise inequalities for \(p=3\))

For all \(z,z'\in\mathbb R^3\):
\[
 \tfrac89\,|V(z)-V(z')|^2\ \le\ (\tilde A(z)-\tilde A(z'))\cdot(z-z')\ \le\ 4\,|V(z)-V(z')|^2, \tag{1.6}
\]
\[
 (|z|+|z'|)\,|z-z'|^2\ \le\ 8\,|V(z)-V(z')|^2,                        \tag{1.7}
\]
\[
 |\tilde A(z)-\tilde A(z')|\ \le\ 2\sqrt2\,(|z|+|z'|)^{1/2}\,|V(z)-V(z')|.  \tag{1.8}
\]

Proof. Put \(\rho=|z|\ge\rho'=|z'|\) (by symmetry) and \(s=z\cdot z'\in[-\rho\rho',\rho\rho']\).
Then
\(M:=(\tilde A(z)-\tilde A(z'))\cdot(z-z')=\rho^3+\rho'^3-(\rho+\rho')s\),
\(N:=|V(z)-V(z')|^2=\rho^3+\rho'^3-2\sqrt{\rho\rho'}\,s\),
\(P:=(\rho+\rho')|z-z'|^2=(\rho+\rho')(\rho^2+\rho'^2-2s)\) are affine in \(s\),
so each linear inequality among them holds on the whole segment once it holds
at both endpoints. At \(s=-\rho\rho'\): \(M-N=(\sqrt\rho-\sqrt{\rho'})^2\rho\rho'\ge0\);
\(M=(\rho+\rho')(\rho^2+\rho'^2)\le4\rho^3\le4N\) since \(N\ge\rho^3\); and
\(P=(\rho+\rho')^3\le8\rho^3\le8N\). At \(s=\rho\rho'\): with \(t=\rho'/\rho\), \(a=\sqrt t\in[0,1]\),
\(M=(\rho-\rho')^2(\rho+\rho')\), \(N=(\rho^{3/2}-\rho'^{3/2})^2\), and
\(N/M=(1+a+a^2)^2/((1+a)^2(1+a^2))\); the inequality \(N\le\frac98M\) is
\(1+2a-6a^2+2a^3+a^4\ge0\), i.e. \(y^2+2y-8=(y+4)(y-2)\ge0\) with \(y=a+1/a\ge2\);
and \(M\le N\), \(P\le N\) follow from \((1+a+a^2)^2\ge(1+a)^2(1+a^2)\).
This gives (1.6) and (1.7). For (1.8), Lindqvist §10, inequality (VI) (directly inspected) gives
\(|\,|b|^{p-2}b-|a|^{p-2}a\,|\le(p-1)(|a|^{(p-2)/2}+|b|^{(p-2)/2})\,|\,|b|^{(p-2)/2}b-|a|^{(p-2)/2}a\,|\)
for \(p\ge2\); with \(p=3\) and \(|a|^{1/2}+|b|^{1/2}\le\sqrt2(|a|+|b|)^{1/2}\) this is (1.8).
Cross-checks: Lindqvist (V) gives the weaker \(N\le\frac94M\); Lindqvist (I) gives
\(M\ge\frac12 P\). A 400 000-sample random test (scratchpad `check.py`) found
\(\min M/N=0.88889\) (the constant \(8/9\) is attained on collinear pairs),
\(\max M/N\approx1.05\), \(\max P/N=2.0\), and \(\max|\tilde A(z)-\tilde A(z')|^2/((|z|+|z'|)N)=1.0\);
all displayed constants are valid and, except \(8/9\), not sharp. \(\square\)

### 1.5 Theorem 1 (global weighted \(H^1\) regularity of the representative)

Under (0.1): \(V=|w|^{1/2}w\in H^1(\mathbb R^3)\), with
\[
 \|V\|_2^2=\|w\|_3^3=3\mathcal Q(u),\qquad
 \|\partial_kV\|_2\le\tfrac92\,\|w\|_3^{1/2}\|\partial_ku\|_3\quad(k=1,2,3). \tag{1.9}
\]

Proof. Fix \(k\) and \(h\ne0\). By (E2) with \(g=D_{-h}D_hq\in\mathcal G_3\) and (0.2),
\[
 0=\int A\cdot D_{-h}D_hq=-\int D_hA\cdot D_hq
 \quad\Longrightarrow\quad
 \int D_hA\cdot D_hw\,dx=\int D_hA\cdot D_hu\,dx .                   \tag{1.10}
\]
This identity is exact and global; it uses only \(A\in L^{3/2}\), \(q\in L^3\).
Since \(D_hA\cdot D_hw=h^{-2}(\tilde A(\tau_hw)-\tilde A(w))\cdot(\tau_hw-w)\), (1.6) gives
\(\int D_hA\cdot D_hw\ge\frac89\|D_hV\|_2^2\). By (1.8),
\(|D_hA|\le2\sqrt2(|\tau_hw|+|w|)^{1/2}|D_hV|\), so by Cauchy–Schwarz and Hölder
(exponents \(3\) and \(3/2\)),
\[
 \Big|\int D_hA\cdot D_hu\Big|
 \le2\sqrt2\,\|D_hV\|_2\Big(\int(|\tau_hw|+|w|)|D_hu|^2\Big)^{1/2}
 \le2\sqrt2\,\|D_hV\|_2\big(2\|w\|_3\|D_hu\|_3^2\big)^{1/2}
 \le4\|w\|_3^{1/2}\|\partial_ku\|_3\,\|D_hV\|_2 ,
\]
using \(\|D_hu\|_3\le\|\partial_ku\|_3\) for \(u\in W^{1,3}\). Combining,
\(\|D_hV\|_2\le\frac98\cdot4\,\|w\|_3^{1/2}\|\partial_ku\|_3\), uniformly in \(h\).
Since \(V\in L^2\) (as \(|V|^2=|w|^3\)), the uniform bound on difference quotients
gives \(\partial_kV\in L^2\) with the same bound (weak compactness in \(L^2\)). \(\square\)

### 1.6 Corollary 1 (consequences)

Under (0.1):

(a) \(w\in L^3\cap L^9(\mathbb R^3)\), \(\|w\|_9^{3/2}=\|V\|_6\le S\|\nabla V\|_2\)
(Sobolev in \(\mathbb R^3\)); hence \(u=\mathbb Pw\in L^9\) with \(\|u\|_9\le C_9\|w\|_9\), and
\(q=w-u\in L^3\cap L^9\).

(b) \(w\in B^{2/3}_{3,\infty}(\mathbb R^3)\): \(\|\tau_hw-w\|_3\le C|h|^{2/3}\|\nabla V\|_2^{2/3}\),
because \(\Psi\) is homogeneous of degree \(2/3\) and Lipschitz on the sphere,
hence globally \(2/3\)-Hölder, so \(|\tau_hw-w|^3\le C|\tau_hV-V|^2\).
Thus \(\phi\in W^{1,3}_{\rm loc}\) with \(\nabla\phi\in B^{2/3}_{3,\infty}\).

(c) Chain rule: \(\Phi\in C^1(\mathbb R^3;\mathbb R^3)\) with \(\Phi(0)=0\), \(D\Phi(0)=0\),
\(D\Phi(V)=|V|^{1/3}(I+\tfrac13\hat V\otimes\hat V)\), \(|D\Phi(V)|\le\frac43|V|^{1/3}\).
Then \(A=\Phi(V)\in W^{1,1}_{\rm loc}\) with \(\nabla A=D\Phi(V)\nabla V\) a.e.
Proof: mollify, \(V_\varepsilon\to V\) in \(H^1_{\rm loc}\) and a.e.; classically
\(\nabla\Phi(V_\varepsilon)=D\Phi(V_\varepsilon)\nabla V_\varepsilon\);
\(|D\Phi(V_\varepsilon)|\le\frac43|V_\varepsilon|^{1/3}\) with \(V_\varepsilon\to V\) in
\(L^6_{\rm loc}\) gives \(D\Phi(V_\varepsilon)\to D\Phi(V)\) in \(L^{18}_{\rm loc}\) (a.e.
convergence plus uniform integrability), so \(D\Phi(V_\varepsilon)\nabla V_\varepsilon\to D\Phi(V)\nabla V\)
in \(L^{9/5}_{\rm loc}\), while \(\Phi(V_\varepsilon)\to\Phi(V)\) in \(L^{3/2}_{\rm loc}\) by
\(|\Phi(a)-\Phi(b)|\le\frac43(|a|+|b|)^{1/3}|a-b|\); closedness of the weak
gradient concludes.

(d) \(A\in W^{1,3/2}(\mathbb R^3)\):
\[
 |\nabla A|\le\tfrac43|V|^{1/3}|\nabla V|=\tfrac43|w|^{1/2}|\nabla V|,\qquad
 \|\nabla A\|_{3/2}\le\tfrac43\|w\|_3^{1/2}\|\nabla V\|_2,             \tag{1.11}
\]
by Hölder with \(\||w|^{1/2}\|_6=\|w\|_3^{1/2}\). Also \(\nabla A\in L^{9/5}\) using
\(w\in L^9\). Since \(\nabla\cdot A=0\) in \(\mathcal D'\) and \(\nabla\cdot A\in L^{3/2}\),
\(\nabla\cdot A=0\) a.e.

(e) On \(\{V\ne0\}\) the field \(w=\Psi(V)\) has the approximate gradient
\(\nabla w=D\Psi(V)\nabla V\), \(D\Psi(V)=|V|^{-1/3}(I-\tfrac13\hat V\otimes\hat V)\),
so \(|\nabla w|\le|w|^{-1/2}|\nabla V|\) there. Whether this approximate gradient
is a distributional gradient, i.e. whether \(w\in W^{1,1}_{\rm loc}\), is not
established: \(|w|^{-1}\) need not be locally integrable. This is the only
hypothesis missing in Section 3.2.

(f) Pointwise algebra (verified symbolically by the random test): on \(\{V\ne0\}\),
\[
 \partial_kA\cdot\partial_kw=|\partial_kV|^2-\tfrac19(\partial_k|V|)^2
 =|w||\partial_kw|^2+|w|(\partial_k|w|)^2,\qquad
 w\cdot\partial_kA=\tfrac43V\cdot\partial_kV=\tfrac23\partial_k|V|^2,           \tag{1.12}
\]
using \((I+\frac13P)(I-\frac13P)=I-\frac19P\) for the projection \(P=\hat V\otimes\hat V\),
and \(|\nabla V|^2=|w||\nabla w|^2+\frac54|w||\nabla|w||^2\).

## 2. The weighted dissipation identity (Goal 2)

Define, with \(V\in H^1(\mathbb R^3)\) from Theorem 1,
\[
 D_3(w):=\int_{\mathbb R^3}\Big(|\nabla V|^2-\tfrac19|\nabla|V||^2\Big)dx,
 \qquad \tfrac89\|\nabla V\|_2^2\le D_3(w)\le\|\nabla V\|_2^2 .        \tag{2.1}
\]
By (1.12), \(D_3(w)=\int(|w||\nabla w|^2+|w||\nabla|w||^2)\) with the integrand
understood through the approximate gradient of \(w\) on \(\{V\ne0\}\) and \(0\)
on \(\{V=0\}\) (where \(\nabla V=0\) a.e.); this is the quantity named \(D_3\)
in the lane statement.

### Theorem 2

Under (0.1),
\[
 \boxed{\;D_{\mathcal Q}(u)=-\int A\cdot\Delta u\,dx=\int\nabla A:\nabla u\,dx=D_3(w).\;} \tag{2.2}
\]
In particular \(D_{\mathcal Q}(u)\ge\frac89\|\nabla V\|_2^2\ge\frac{8}{9S^2}\|w\|_9^3\ge\frac{8}{9S^2C_9^3}\|u\|_9^3\),
so \(D_{\mathcal Q}(u)>0\) unless \(u=0\); and
\[
 D_{\mathcal Q}(u)\le2\,\|w\|_3\,\|\nabla u\|_3^2=2\,(3\mathcal Q(u))^{1/3}\|\nabla u\|_3^2. \tag{2.3}
\]

Proof. Step 1 (no boundary terms). Fix \(k\). Since \(u\in W^{2,3}\),
\(D_{-h}D_hu\to\partial_k^2u\) in \(L^3\); as \(A\in L^{3/2}\),
\[
 -\int A\cdot\partial_k^2u=-\lim_{h\to0}\int A\cdot D_{-h}D_hu
 =\lim_{h\to0}\int D_hA\cdot D_hu
 =\lim_{h\to0}\int D_hA\cdot D_hw ,
\]
by (0.2) and (1.10). Every equality is exact on \(\mathbb R^3\); no cutoff, no
decay of \(w\) beyond \(w\in L^3\), and no derivative of \(q\) is used. Summing over
\(k\) gives \(D_{\mathcal Q}(u)=\lim_h\sum_k\int D_hA\cdot D_hw\).

Step 2 (identification of the limit). Let \(f_h:=D_hA\cdot D_hw\ge0\). By (1.6),
\(f_h\le4|D_hV|^2\), and \(|D_hV|^2\to|\partial_kV|^2\) in \(L^1\) because
\(D_hV\to\partial_kV\) in \(L^2\) (Theorem 1). Along a sequence \(h_j\to0\),
\(D_{h_j}V\to\partial_kV\) and \(\tau_{h_j}V\to V\) a.e. At a.e. \(x\) with
\(V(x)\ne0\), \(\Phi\) and \(\Psi\) are \(C^1\) near \(V(x)\), so
\(D_{h_j}A(x)\to D\Phi(V(x))\partial_kV(x)\) and \(D_{h_j}w(x)\to D\Psi(V(x))\partial_kV(x)\),
whence \(f_{h_j}(x)\to|\partial_kV(x)|^2-\frac19(\partial_k|V|(x))^2\) by (1.12).
At a.e. \(x\) with \(V(x)=0\), \(\partial_kV(x)=0\), so \(f_{h_j}(x)\le4|D_{h_j}V(x)|^2\to0\).
The generalized dominated convergence theorem (Vitali) yields
\(\int f_{h_j}\to\int(|\partial_kV|^2-\frac19(\partial_k|V|)^2)\). Since the full
limit exists by Step 1, it equals this value; summing over \(k\) gives
\(D_{\mathcal Q}(u)=D_3(w)\).

Step 3 (the middle expression in (2.2)). \(A\in W^{1,3/2}(\mathbb R^3)\) by
Corollary 1(d) and \(\nabla u\in W^{1,3}(\mathbb R^3)\); density of \(C_c^\infty\) in
\(W^{1,3/2}(\mathbb R^3)\) and continuity of both sides in \(A\) give
\(-\int A\cdot\Delta u=\int\nabla A:\nabla u\). (Explicit cutoff version: with
\(\eta_R(x)=\eta(x/R)\), \(\int\eta_RA\cdot\Delta u=-\int\eta_R\nabla A:\nabla u-\int(A\otimes\nabla\eta_R):\nabla u\);
the last term is at most \(R^{-1}\|\nabla\eta\|_\infty\|A\|_{3/2}\|\nabla u\|_{L^3(R\le|x|\le2R)}\to0\),
and the others converge by dominated convergence.)

Step 4 (2.3). By Step 3, (1.11) and (2.1):
\(D_3\le\|\nabla A\|_{3/2}\|\nabla u\|_3\le\frac43\|w\|_3^{1/2}\|\nabla V\|_2\|\nabla u\|_3
\le\frac43(\frac98)^{1/2}\|w\|_3^{1/2}D_3^{1/2}\|\nabla u\|_3\), and
\((\frac43)^2\frac98=2\). The lower bounds use (2.1), Sobolev, and Corollary 1(a). \(\square\)

Remarks. (i) The HF17 generator inequality \(D_{\mathcal Q}\ge0\) is now the
coercive weighted dissipation (2.2); the term "\(\int\nabla A:\nabla q\)" that a
formal computation would have to kill never appears, because (1.10) removes
the \(q\)-difference-quotient before any limit is taken. (ii) Every boundary
term at infinity is controlled; nothing is conditional. (iii) (2.3) is not an
input bound: \(\|\nabla u\|_3\) is not energy-controlled and scales like
\(\lambda\).

## 3. Forms of the transport term (Goal 3)

Let \(T:=-\int A\cdot((u\cdot\nabla)u)\,dx\) (the HF17 transport flux) and
\(K:=\mathcal Q'+\nu D_{\mathcal Q}(u)\).

### 3.1 Proposition 3 (rigorous, derivative-free in \(q\) and \(w\))

Under (0.1), all the following integrals converge absolutely and
\[
 K=T=-\int q\cdot((A\cdot\nabla)u)              \tag{F1}
\]
\[
 \phantom{K}=\int A\cdot(u\times\omega)=\int u\cdot(\omega\times A),\qquad \omega=\operatorname{curl}u=\operatorname{curl}w, \tag{F2}
\]
\[
 \phantom{K}=\int(u\otimes u):\nabla A=\int u\cdot((u\cdot\nabla)A)      \tag{F5}
\]
\[
 \phantom{K}=-\int q\cdot((u\cdot\nabla)A)                                \tag{F6}
\]
\[
 \phantom{K}=-\tfrac12\int q\cdot\operatorname{div}(u\otimes A+A\otimes u)
 =-\int q\cdot(I-\mathbb P)\big[(u\cdot\nabla)A\big].                      \tag{F7}
\]

Proof. (F1) is (E4) (HF17 inner variation). (F2): \((u\cdot\nabla)u=\nabla(|u|^2/2)+\omega\times u\)
pointwise for the smooth \(u\); \(\int A\cdot\nabla(|u|^2/2)=0\) by (E2) and (E5);
\(A\cdot(\omega\times u)=-u\cdot(\omega\times A)\); \(\operatorname{curl}q=0\) in \(\mathcal D'\).
(F5): \((u\cdot\nabla)u_j=\partial_i(u_iu_j)\) since \(\nabla\cdot u=0\), and
\(\int A_j\partial_i(u_iu_j)=-\int(\partial_iA_j)u_iu_j\) by density of \(C_c^\infty\) in
\(W^{1,3/2}(\mathbb R^3)\), \(A\in W^{1,3/2}\), \(u\otimes u\in W^{1,3}\). (F6): write
\(u=w-q\) in (F5); by (1.12), \(w\cdot((u\cdot\nabla)A)=\frac23u\cdot\nabla|V|^2\) a.e.,
with \(|V|^2\in W^{1,1}(\mathbb R^3)\) (\(|V|^2=|w|^3\in L^1\), \(\nabla|V|^2=2(\nabla V)^{\!\top}V\in L^1\)),
so \(\int w\cdot((u\cdot\nabla)A)=0\) by (0.3); the remaining pairing converges since
\(q\in L^3\), \(u\in L^\infty\), \(\nabla A\in L^{3/2}\). (F7): average (F1) and (F6);
\(u_i\partial_iA_j+A_i\partial_iu_j=\partial_i(u_iA_j+A_iu_j)\) a.e. because \(\nabla\cdot u=0\)
and \(\nabla\cdot A=0\) a.e. (Corollary 1(d)); the last form uses that
\(\mathbb P[(u\cdot\nabla)A]\in L^{3/2}\) is divergence-free and therefore
annihilates \(q\in\mathcal G_3\). Consistency: (F1) and (F6) differ by
\(\int q\cdot\operatorname{curl}(A\times u)\), which vanishes for the same reason. \(\square\)

The forms (F2), (F5), (F6), (F7) are new relative to HF17; (F6) is the one
used in Section 4. (F7) exhibits \(K\) as the work of the mixed
pressure \(\Pi_{u,A}\), \(\nabla\Pi_{u,A}=(I-\mathbb P)[(u\cdot\nabla)A]\), against \(q\)
(equivalently against \(w\), since \(\int u\cdot\nabla\Pi_{u,A}=0\)). By the packet
rule, this equivalent identity does not by itself discharge the gap.

### 3.2 Proposition 3' (the lane's forms, conditional)

Hypothesis (H1): \(w\in W^{1,1}_{\rm loc}(\mathbb R^3)\) (equivalently
\(q\in W^{1,1}_{\rm loc}\), equivalently \(\phi\in W^{2,1}_{\rm loc}\)).

Under (0.1) and (H1):
\[
 K=-\int q\cdot((A\cdot\nabla)w)\,dx=\int u\cdot((A\cdot\nabla)w)\,dx,       \tag{F3–F4}
\]
with both integrands in \(L^1(\mathbb R^3)\).

Proof. Under (H1) the weak gradient of \(w\) coincides with the approximate
gradient of Corollary 1(e) on \(\{V\ne0\}\) and vanishes a.e. on \(\{w=0\}\); hence
\(|A||\nabla w|\le|w|^{3/2}|\nabla V|=|V||\nabla V|\) with \(|V|\in L^2\cap L^6\), so
\((A\cdot\nabla)w\in L^{3/2}\cap L^1\), and \(|q||A||\nabla w|\le|q||V||\nabla V|\in L^1\)
(exponents \(3,6,2\)). Also \(\nabla q=\nabla w-\nabla u\in L^1_{\rm loc}\) is a.e. symmetric
(it is the Hessian of \(\phi\in W^{2,1}_{\rm loc}\)).
Step A: \(\int q\cdot((A\cdot\nabla)q)=0\). Put \(f=|q|^2\); \(q\in L^9_{\rm loc}\cap W^{1,1}_{\rm loc}\)
with \(|q||\nabla q|\le|q||\nabla u|+|q||w|^{-1/2}|\nabla V|\), and the second term is in
\(L^1\) after multiplication by \(|A|=|w|^2\); so \(fA\in W^{1,1}_{\rm loc}\) with
\(\operatorname{div}(fA)=2q\cdot((A\cdot\nabla)q)\) a.e. (product rule, \(\nabla\cdot A=0\) a.e.,
\(f\nabla A\in L^{9/8}\) by \(f\in L^{9/2}\), \(\nabla A\in L^{3/2}\)). Then
\(\int\eta_R\operatorname{div}(fA)=-\int fA\cdot\nabla\eta_R\), bounded by
\(R^{-1}\|\nabla\eta\|_\infty\int_{R\le|x|\le2R}|q|^2|w|^2\to0\) (\(|q|^2\in L^{3/2}\), \(|w|^2\in L^3\)),
while the left side converges to \(2\int q\cdot((A\cdot\nabla)q)\) by dominated
convergence. Step B: \(-\int q\cdot((A\cdot\nabla)u)=-\int q\cdot((A\cdot\nabla)w)+\int q\cdot((A\cdot\nabla)q)\),
giving the first form. Step C: \(\int u\cdot((A\cdot\nabla)u)=\int A\cdot\nabla(|u|^2/2)=0\)
by (E2), (E5); so \(\int u\cdot((A\cdot\nabla)w)=\int u_jA_i\partial_iq_j=\int u_jA_i\partial_jq_i
=\int A\cdot((u\cdot\nabla)q)=-\int q\cdot((u\cdot\nabla)A)\), the last by the same cutoff
argument applied to \(\operatorname{div}((A\cdot q)u)=u\cdot\nabla(A\cdot q)\) with
\(|A||q|\in L^1\); this is (F6). \(\square\)

Exact status of Goal 3: the identities requested in the lane are true under
(H1) and false to assert without it, because no step of Sections 1–2 shows
that \(|w|^{-1/2}|\nabla V|\) is locally integrable. Section 4 does not need
them.

## 4. Evolution and the sharpest scaling-consistent estimate (Goal 4)

### Theorem 4

On every compact classical interval, with \(V=|w|^{1/2}w\),
\[
 \boxed{\;\mathcal Q'(u)+\nu D_3(w)=K,\qquad K=-\int q\cdot((u\cdot\nabla)A)\,dx,\;}   \tag{4.1}
\]
and
\[
 \boxed{\;|K|\ \le\ \tfrac43\,C_9\,S\,(1+C_3)\ \|w\|_3\,\|\nabla V\|_2^2
 \ \le\ C_*\,\mathcal Q(u)^{1/3}\,D_3(w),\qquad
 C_*:=\tfrac32\,3^{1/3}\,(1+C_3)\,C_9\,S .\;}                                  \tag{4.2}
\]

Proof. (4.1) is (E4) with Theorem 2 and (F6). For (4.2), by (1.11) and Hölder
with exponents \(3,6,2\):
\[
 |K|\le\tfrac43\int|q|\,|u|\,|w|^{1/2}|\nabla V|
 \le\tfrac43\|q\|_3\,\big\||u||w|^{1/2}\big\|_6\,\|\nabla V\|_2 .
\]
Now \(\||u||w|^{1/2}\|_6^6=\int|u|^6|w|^3\le\|u\|_9^6\|w\|_9^3\), so
\(\||u||w|^{1/2}\|_6\le\|u\|_9\|w\|_9^{1/2}\le C_9\|w\|_9^{3/2}=C_9\|V\|_6\le C_9S\|\nabla V\|_2\)
(Corollary 1(a)). Finally \(\|q\|_3\le(1+C_3)\|w\|_3=(1+C_3)(3\mathcal Q)^{1/3}\) and
\(\|\nabla V\|_2^2\le\frac98D_3\). \(\square\)

### Corollary 4 (Lyapunov property for small critical size)

If at some time \(t_0\) of the classical interval
\[
 \mathcal Q(u(t_0))^{1/3}<\nu/C_*\qquad(\hbox{implied by }\|u(t_0)\|_3<3^{1/3}\nu/C_*), \tag{4.3}
\]
then \(\mathcal Q(u(t))\) is nonincreasing for \(t\ge t_0\) on the whole classical
interval, and \(\sup_{t\ge t_0}\|u(t)\|_3\le C_3\,(3\mathcal Q(u(t_0)))^{1/3}\).

Proof. By (4.1)–(4.2), \(\mathcal Q'\le-(\nu-C_*\mathcal Q^{1/3})D_3\le0\) wherever
\(\mathcal Q^{1/3}\le\nu/C_*\). Let \(t_*=\inf\{t\ge t_0:\mathcal Q(t)>\mathcal Q(t_0)\}\) and
suppose it is finite. Continuity gives \(\mathcal Q(t_*)=\mathcal Q(t_0)\), so
\(\mathcal Q^{1/3}<\nu/C_*\) on \([t_*,t_*+\delta]\), where \(\mathcal Q'\le0\); the mean value
theorem gives \(\mathcal Q\le\mathcal Q(t_0)\) there, contradicting the definition of
\(t_*\). The \(L^3\) bound is (E1), (E3). \(\square\)

With the project's imported endpoint continuation criterion (ESS; PLAN.md
node ESS), Corollary 4 yields global regularity for data satisfying (4.3).
This is a known result (Kato, Math. Z. 187 (1984) 471–480, metadata-only)
obtained here with a stronger tool; the corollary claims no new regularity.
Its value is as a consistency check: the quotient mechanism closes with the
correct dimensionless threshold \(\|u_0\|_3/\nu\), and (4.2) is a pure size
bound with no cancellation used.

### Why (4.2) does not close for arbitrary data, and what is supercritical

1. Scaling. Under \(\mathcal S_\lambda\): \(\mathcal Q\to\mathcal Q\), \(D_3\to\lambda^2D_3\),
   \(K\to\lambda^2K\). Under \(u\to au\): \(\mathcal Q\to a^3\mathcal Q\), \(D_3\to a^3D_3\),
   \(K\to a^4K\). The only monomial \(\mathcal Q^\alpha D_3^\beta\) consistent with both is
   \(\alpha=1/3\), \(\beta=1\). Hence (4.2) is the unique scaling-consistent size
   bound of \(K\) by \(\mathcal Q\) and \(D_3\), and any absorption
   \(|K|\le\theta\nu D_3+A\) with \(\theta<1\) is not obtainable from (4.2) alone unless \(C_*\|w\|_3\le\theta\nu\), i.e.
   smallness of the critical norm \(\|w\|_3\sim\|u\|_3\). That smallness is
   exactly the hidden-smallness falsifier; for arbitrary data it is unavailable.
2. Alternative Hölder splits produce Gronwall coefficients instead:
   \(|K|\le\frac43(1+C_3)\|u\|_\infty\|w\|_3^{3/2}\|\nabla V\|_2\le\frac{\nu}2D_3+C\nu^{-1}\|u\|_\infty^2\mathcal Q\),
   or, using \(\nabla A\in L^{9/5}\), \(|K|\le C\mathcal Q^{1/3}\|u\|_9D_3^{2/3}\le\frac\nu2D_3+C\nu^{-2}\|u\|_9^3\mathcal Q\).
   The coefficients \(\int\|u\|_\infty^2dt\) and \(\int\|u\|_9^3dt\) are Serrin-critical
   (\(2/s+3/r=1\)); a bound on either is a regularity criterion. This is the
   same critical-versus-supercritical mismatch recorded in `prop:scaling`: the
   inputs control \(\|u\|_2\) and \(\int\|\nabla u\|_2^2\) (supercritical), while
   every coefficient that closes (4.1) is critical.
3. The dissipation side is itself critical: by Theorem 2,
   \(\nu\int_0^\tau D_3\,dt\ge\frac{8\nu}{9S^2C_9^3}\int_0^\tau\|u\|_9^3dt\), so any
   input-only bound \(\int_0^\tau K\le\theta\nu\int_0^\tau D_3+A_{\rm input}\) would bound
   \(u\) in \(L^3_tL^9_x\), a Ladyzhenskaya–Prodi–Serrin class. This makes explicit
   the packet's statement that the gap implies continuation (via \(L^3_tL^9_x\) and ESS); the converse is the packet's statement, not proved here.

### Strictly new structural facts (claims with scope)

Scope: every fixed time of a classical solution with \(u\in H^m\), \(m\ge4\),
divergence-free, on \(\mathbb R^3\); no smallness, no decay beyond (0.1).

- (N1) \(V=|w|^{1/2}w\in H^1(\mathbb R^3)\) with (1.9); \(A=|w|w\in W^{1,3/2}(\mathbb R^3)\)
  with (1.11); \(w\in L^3\cap L^9\cap B^{2/3}_{3,\infty}\). Proof global, cutoff-free,
  via (1.10).
- (N2) \(D_{\mathcal Q}(u)=\int(|\nabla V|^2-\tfrac19|\nabla|V||^2)\) with \(V=|w|^{1/2}w\in H^1\) (equal to \(D_3(w)=\int(|w||\nabla w|^2+|w||\nabla|w||^2)\) in the approximate-gradient sense of Section 2; \(w\in W^{1,1}_{loc}\) is not proved): the viscous
  term of the quotient evolution is the full weighted cubic dissipation of the
  representative \(w\), coercive: \(D_{\mathcal Q}(u)\ge\frac89\|\nabla V\|_2^2\ge c\|u\|_9^3\).
- (N3) Derivative-free transport forms (F2), (F5), (F6), (F7); in particular
  \(K=-\int q\cdot((u\cdot\nabla)A)\), dual to HF17's \(-\int q\cdot((A\cdot\nabla)u)\).
- (N4) \(|K|\le C_*\mathcal Q^{1/3}D_3(w)\), the unique scaling-consistent size bound,
  with explicit \(C_*\); \(\mathcal Q\) is a Lyapunov functional under (4.3).

## 5. Self-check against the packet falsifiers

- Differentiating the merely-\(L^3\) minimizer: never done. Derivatives appear
  only for \(V\) (Theorem 1), \(A=\Phi(V)\) (Corollary 1(c)), \(|V|^2\), and the smooth \(u\);
  the limit in Theorem 2 is identified through \(V\) with Vitali. Forms needing
  \(\nabla w\) or \(\nabla q\) are isolated in Proposition 3' under the explicit (H1).
- Using the controlled norm: (4.2) uses \(\|w\|_3\), which is the controlled
  quantity, and (2.3) uses \(\|\nabla u\|_3\); both are stated as non-input bounds.
  No \(\|\nabla u\|_\infty\), \(\|u\|_\infty\), or \(\sup_t\|u\|_3\) enters any claimed
  conclusion except in the explicitly labelled non-closing alternatives.
- Scaling: checked in Section 4 for every displayed estimate.
- Hidden smallness: the only smallness is (4.3), displayed as the hypothesis
  of Corollary 4 and identified as the obstruction.
- Periodic or forced variant: none; unforced \(\mathbb R^3\) throughout.
- \(p\)-Laplace theorems outside their hypotheses: none applied. Section 1.3
  records exactly why (1.4) fails; the Bojarski–Iwaniec mechanism is re-executed
  from scratch rather than cited.
- Forbidden inferences: energy is never claimed to control anything critical;
  no Hölder regularity is claimed, hence none is upgraded; Theorem 4 is an
  instantaneous identity plus a size bound, and no time-integrated absorption
  is asserted; (F7) is labelled an equivalent identity that does not discharge
  the gap.

## 6. Frontier record

MODE / RESULT: DISCOVER, then self-check. Goal 1: exact PDE and structure
verified; \(C^{1,\alpha}\) import obstructed exactly; global \(H^1\) of
\(|w|^{1/2}w\) proved directly. Goal 2: \(D_{\mathcal Q}=D_3(w)\) proved globally with
no boundary term. Goal 3: derivative-free forms proved; the lane's two
\(\nabla w\)-forms proved conditionally on \(w\in W^{1,1}_{\rm loc}\). Goal 4:
evolution (4.1) and the unique scaling-consistent bound (4.2); closure only
under critical smallness.

CLAIM AND SCOPE: (N1)–(N4) for every fixed time of a classical
\(H^m\)-solution, \(m\ge4\), on \(\mathbb R^3\); Corollary 4 for trajectories
satisfying (4.3) at one time; Proposition 3' under (H1).

EVIDENCE: exact global identity (1.10) from the Euler–Lagrange condition on
the closed gradient space; Lemma V (proved, numerically cross-checked,
consistent with Lindqvist §10 (I), (V), directly inspected); Bojarski–Iwaniec
mechanism (Lindqvist Theorem 4.1, directly inspected) re-executed globally;
chain rule by mollification; Vitali; Leray boundedness on \(L^3\), \(L^9\);
Sobolev in \(\mathbb R^3\).

FIRST GAP: unchanged. Prove
\(\int_0^\tau K\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+A_{\rm input}\) uniformly for
\(\tau<\min(H,T_*)\) with \(\theta\le1\) and \(A_{\rm input}\) depending only on
\(u_0,\nu,H\). By (4.2) this holds with \(A_{\rm input}=0\) whenever
\(C_*\sup_t\mathcal Q^{1/3}\le\theta\nu\); for arbitrary data the first
unsupported implication is the passage from the supercritical inputs
\(\|u_0\|_2\), \(\nu\int\|\nabla u\|_2^2\) to the critical coefficient
\(C_*\|w\|_3\), or to any Serrin-critical coefficient. Section 4 shows that no
size estimate can supply it; a cancellation in \(K=-\int q\cdot((u\cdot\nabla)A)\)
would be required.

SURVIVING CONDITIONAL SUFFIX: with the gap estimate, (4.1) integrates to
\(\mathcal Q(\tau)+(1-\theta)\nu\int_0^\tau D_3\le\mathcal Q(0)+A_{\rm input}\), giving
\(\sup_t\|u\|_3\) and \(u\in L^3_tL^9_x\) up to \(\min(H,T_*)\), hence
continuation by the imported ESS node; unchanged from HF17 except that the
dissipation is now explicit and coercive.

NON-CLAIMS: no \(C^{1,\alpha}\), continuity, local boundedness, or
\(W^{1,1}_{\rm loc}\) regularity of \(w\) or \(\nabla\phi\); no \(W^{2,2}_{\rm loc}\) of
\(\phi\); no validity of (F3)–(F4) without (H1); no time-integrated absorption of
\(K\); no input-only bound for \(K\); no new regularity theorem (Corollary 4
reproduces a classical small-data result); no HIGH-STRAIN or HIGH-PRESSURE
theorem; no continuation theorem for arbitrary data; no Millennium claim; no
novelty claim for the nonlinear Hodge decomposition itself. Tolksdorf,
DiBenedetto, Lieberman, Uraltseva, Uhlenbeck, Manfredi–Weitsman and Kato are
cited metadata-only and no statement of theirs is load-bearing.

NEXT DISTINCT ACTION: FALSIFY the possibility of a cancellation in
\(K=-\int q\cdot((u\cdot\nabla)A)=-\int q\cdot\nabla\Pi_{u,A}\): construct, for fixed
smooth divergence-free \(u\), the minimizer \(w\) numerically (3-Laplace-type
Euler–Lagrange, e.g. on a large periodic box as a proxy for the variational
problem only, never for the evolution) and test whether \(K/(\mathcal Q^{1/3}D_3)\)
can approach \(C_*\) with a sign that defeats absorption; if the ratio is
bounded away from \(C_*\) on a structured family, target a sharper constant or a
sign for the symmetrized form (F7). Independently, attempt (H1) via a
Manfredi–Weitsman-type argument for the shifted equation, which would
promote Proposition 3' and give \(\nabla w\) as a genuine object.

## 7. Sources

Directly inspected:
- P. Lindqvist, *Notes on the p-Laplace equation* (Jyväskylä lecture notes,
  2005 lectures; PDF from the author's NTNU page), §4 Theorem 4.1
  (Bojarski–Iwaniec: \(|\nabla u|^{(p-2)/2}\nabla u\in W^{1,2}_{\rm loc}\) for \(p\ge2\), proof by
  difference quotients), p. 28 attribution of \(C^{1,\alpha}\) to Uraltseva 1968
  with references [E], [Uh], [Le2], [Db], [To]; §10 inequalities (I), (IV), (V)
  and the bound \(|\,|b|^{p-2}b-|a|^{p-2}a|\le(p-1)(|a|^{(p-2)/2}+|b|^{(p-2)/2})|\,|b|^{(p-2)/2}b-|a|^{(p-2)/2}a|\).
- C. Yu, EJDE 2022, No. 27, pp. 1–15, p. 2 and reference list: statement that
  Euclidean \(p\)-harmonic functions are \(W^{2,2}_{\rm loc}\) for \(1<p<3+2/(n-2)\)
  (Manfredi–Weitsman [12]), and the reference entries for Tolksdorf [16],
  Uhlenbeck [17], Ural'ceva [18], Evans [7], Lewis [9].

Metadata-only (fetch blocked; not load-bearing):
- P. Tolksdorf, J. Differential Equations 51 (1984) 126–150.
- E. DiBenedetto, Nonlinear Anal. 7 (1983) 827–850.
- G. Lieberman, Nonlinear Anal. 12 (1988) 1203–1219.
- N. N. Ural'ceva, Zap. Nauchn. Sem. LOMI 7 (1968) 184–222.
- K. Uhlenbeck, Acta Math. 138 (1977) 219–240.
- J. Manfredi, A. Weitsman, Comm. PDE 13 (1988) 651–668.
- T. Kato, Math. Z. 187 (1984) 471–480.

Bounded numerical evidence: scratchpad `check.py` (400 000 random pairs with
collinear and near-coincident subfamilies; five random gradient matrices for
(1.12)); declared range: finite sampling, supports but does not prove Lemma V.
