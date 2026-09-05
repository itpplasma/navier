# HF18-B: the divergence–speed link of the minimizing representative

Lane HF18-B, mode DISCOVER with self-check, 2026-09-05.
Inputs: PLAN.md (frontier packet, HF16–HF17), `hf17-quotient-functional.md`,
`hf17-quotient-evolution.md`, both HF17 reviews (PASS), and `sec:quotient`
of `../navier-paper/main.tex`.  Base commit `fd1c20e`.

**MODE / RESULT: DISCOVER.**  The pointwise identity
\(\operatorname{div}w=-\hat w\cdot\nabla|w|\) is made rigorous on
\(\{w\ne0\}\) under an explicit Sobolev hypothesis, and the merely-\(L^3\)
statement is shown to carry no pointwise content.  The minimizer class is
characterised linearly as \(\{|A|^{-1/2}A:\ A\in L^{3/2},\ \operatorname{div}A=0\}\).
Two exact identities that need no regularity of \(w\) are new to the
programme: the transport flux is a pure strain form,
\(\mathfrak T=-\int|w|\,w\cdot S(u)\,w\), and \(\int A\cdot((q\cdot\nabla)u)=0\).
The high-strain term is rewritten as a pairing of \(\operatorname{div}w\)
with a pressure-type potential.  The only scaling-admissible inequality of
the requested type, \(\int|q|^2|w|^3\le C\mathcal Q^{2/3}D_3(w)\), is proved
(Hölder–Sobolev, no divergence structure used).  The unweighted speed-gradient
norm \(\|\hat w\cdot\nabla|w|\|_{3/2}\) is proved *not* to be a function of
\((D_3,\mathcal Q,E)\) on the minimizer class (explicit family, numerically
checked).  No control of the high-strain term follows; the first uncontrolled
term is displayed with its scaling.  Every rewriting here is an equivalent
identity and, per PLAN, discharges nothing.

## 0. Setting and notation

\(\mathcal G_3\), \(\mathcal Q\), \(w=u+q\), \(A=|w|w\), \(\mathbb P\) as in
HF17.  Established (audited): \(A\in L^{3/2}\), \(\int A\cdot g=0\) for
\(g\in\mathcal G_3\), \(u=\mathbb Pw\), \(q=(I-\mathbb P)w\),
\(\|w\|_3^3=3\mathcal Q\), \(D\mathcal Q(u)[h]=\int A\cdot h\).
Write \(\hat w=w/|w|\) on \(\{w\ne0\}\),
\[
 \sigma:=\hat w\cdot\nabla|w|=\hat w_i\hat w_j\,\partial_iw_j
 \quad\text{on }\{w\ne0\},\qquad \sigma:=0\ \text{on }\{w=0\},
\]
the *radial speed derivative* (derivative of the speed \(|w|\) along the
direction of \(w\)), and
\[
 D_3(w):=\int\big(|w||\nabla w|^2+|w||\nabla|w||^2\big)dx,\qquad
 D_3^{\rm rad}(w):=\int|w||\nabla|w||^2dx=\tfrac49\big\|\nabla|w|^{3/2}\big\|_2^2 .
\]
Scaling bookkeeping used throughout: \((a,\lambda)\) denotes amplitude
\(w\mapsto aw\) and Navier–Stokes dilation \(w\mapsto\lambda w(\lambda\cdot)\):
\(\mathcal Q\sim(a^3,\lambda^0)\), \(D_3\sim(a^3,\lambda^2)\),
\(E=\|u\|_2^2\sim(a^2,\lambda^{-1})\), \(\|q\|_3^3\sim(a^3,\lambda^0)\),
\(\|\sigma\|_{3/2}^{3/2}\sim(a^{3/2},\lambda^0)\),
\(\int|q|^2|w|^3\sim(a^5,\lambda^2)\), \(2^L\sim(1,\lambda)\),
\(\nu\sim(a,\lambda^0)\) (amplitude scaling is a Navier–Stokes symmetry only
together with \(\nu\mapsto a\nu\)), rates \(\mathcal Q',K_L,\nu D_3\sim(a^4,\lambda^2)\).

## 1. The pointwise identity: exact scope

### 1.1 Distributional statement (no hypothesis)

The audited Euler condition is
\(\operatorname{div}(|w|w)=0\) in \(\mathcal D'(\mathbb R^3)\) with
\(|w|w\in L^{3/2}\).  Since \(\operatorname{div}u=0\) in \(\mathcal D'\),
\[
 \operatorname{div}q=\operatorname{div}w\in W^{-1,3}(\mathbb R^3),\qquad
 q=\nabla\Delta^{-1}\operatorname{div}w=R(R\cdot w),                  \tag{1.1}
\]
where \(R_j=\partial_j(-\Delta)^{-1/2}\) are the Riesz transforms, bounded on
\(L^p\), \(1<p<\infty\).  This is the whole content at the \(L^3\) level: a
nonlinear function of \(w\) has zero divergence.  A pointwise identity
involving \(\nabla w\) has no meaning until \(\nabla w\) exists in some sense.
No mollification argument produces one, because
\(\operatorname{div}(|w_\varepsilon|w_\varepsilon)\ne(\operatorname{div}(|w|w))_\varepsilon\).

### 1.2 Sobolev hypothesis and the identity on \(\{w\ne0\}\)

**Hypothesis (H1).** \(w\in W^{1,1}_{\rm loc}(\mathbb R^3;\mathbb R^3)\) and
\(|w||\nabla w|\in L^1_{\rm loc}\).

(H1) is *not* implied by the variational construction; lane HF18-A studies
whether it holds.  Everything in 1.2–1.4 is conditional on it.

**Proposition 1.1.** Under (H1): (i) \(A=|w|w\in W^{1,1}_{\rm loc}\) with
\[
 \partial_iA_j=|w|\,\partial_iw_j+w_j\,\partial_i|w|,\qquad
 \partial_i|w|=\hat w_k\partial_iw_k\ \text{on }\{w\ne0\},\quad
 \nabla|w|=0,\ \nabla w=0\ \text{a.e. on }\{w=0\};                  \tag{1.2}
\]
(ii) \(\operatorname{div}A=|w|\operatorname{div}w+w\cdot\nabla|w|=0\) a.e.;
(iii) for a.e. \(x\in\{w\ne0\}\),
\[
 \boxed{\ \operatorname{div}w=-\hat w\cdot\nabla|w|=-\sigma,\qquad
 \text{equivalently}\quad \operatorname{tr}\big((I+\hat w\otimes\hat w)\nabla w\big)=0\ }
                                                                    \tag{1.3}
\]
and (iv) \(\operatorname{div}w=0\) a.e. on \(\{w=0\}\); hence
\(\operatorname{div}w=-\sigma\) a.e. on \(\mathbb R^3\) with the convention
\(\sigma=0\) on the zero set.

*Proof.* \(F(z)=|z|z\) is \(C^1(\mathbb R^3;\mathbb R^3)\) with
\(DF(z)=|z|I+\hat z\otimes z\) (\(DF(0)=0\)), \(|DF(z)|\le2|z|\).  Truncate
\(F\) to a Lipschitz \(C^1\) map \(F_R\) agreeing with \(F\) on \(|z|\le R\)
with \(|DF_R|\le2|z|\); the chain rule for \(C^1\) maps with bounded derivative
applied to \(W^{1,1}_{\rm loc}\) fields (scalar form: Gilbarg–Trudinger
Lemma 7.5, cited from memory, not re-inspected this wave; vector form by the
same mollification proof) gives \(F_R\circ w\in W^{1,1}_{\rm loc}\),
\(\nabla(F_R\circ w)=DF_R(w)\nabla w\).  Let \(R\to\infty\): \(F_R\circ w\to
F\circ w\) in \(L^1_{\rm loc}\) (\(|w|^2\in L^{3/2}_{\rm loc}\)) and
\(DF_R(w)\nabla w\to DF(w)\nabla w\) in \(L^1_{\rm loc}\) by dominated
convergence with majorant \(2|w||\nabla w|\).  This is (1.2), where
\(\nabla w=0\) a.e. on \(\{w=0\}=\bigcap_j\{w_j=0\}\) because
\(\nabla w_j=0\) a.e. on \(\{w_j=0\}\) for each component (Gilbarg–Trudinger
Lemma 7.7, from memory), and \(|w|\in W^{1,1}_{\rm loc}\) with the stated
gradient because \(z\mapsto|z|\) is Lipschitz.  Taking the trace of (1.2)
gives the a.e. formula for \(\operatorname{div}A\); the distributional
divergence of a \(W^{1,1}_{\rm loc}\) field is its a.e. divergence, so
\(\operatorname{div}A=0\) a.e.  On \(\{w\ne0\}\) divide by \(|w|\); on
\(\{w=0\}\) both sides vanish by \(\nabla w=0\) a.e.  For the trace form,
\(\hat w\cdot\nabla|w|=\hat w_i\hat w_k\partial_iw_k\). \(\square\)

**Remark 1.2 (zero set).** (1.3) carries no information on \(\{w=0\}\); the
constraint there is only the Sobolev fact \(\nabla w=0\) a.e.  On the other
hand, nothing prevents \(\{w=0\}\) from containing hypersurfaces: if
\(A=\operatorname{curl}(\psi e_3)\) with \(\psi=-x_1^3/3\) near \(x_1=0\) then
\(|w|=|A|^{1/2}\sim|x_1|\).  Near a codimension-one zero with
\(|w|\sim\operatorname{dist}^\beta\), \(\int|w||\nabla|w||^2<\infty\) and
\(\int|\sigma|^{3/2}<\infty\) locally have the *same* threshold
\(\beta>1/3\); the failure of control proved in 2.4 below is not a zero-set
effect.

**Remark 1.3 (a family of exact integrals).** Under (H1) and
\(|w|^{\alpha+1}\in L^1\), \(|w|^{\alpha}|\nabla w|\in L^1\), \(\alpha\ne1\):
\(\operatorname{div}(|w|^\alpha w)=(1-\alpha)|w|^\alpha\operatorname{div}w\)
a.e. (from (1.3)), hence
\[
 \int|w|^\alpha\operatorname{div}w\,dx=0 .                          \tag{1.4}
\]
The case \(\alpha=3\) is used in 3.2 (formal cross-check).

### 1.3 The natural finite-dissipation class

**Hypothesis (H1').** \(w\in W^{1,1}_{\rm loc}\), \(w\in L^3\), \(D_3(w)<\infty\).

(H1') implies (H1): \(|w||\nabla w|=|w|^{1/2}\cdot|w|^{1/2}|\nabla w|\in
L^6\cdot L^2\subset L^{3/2}\).  Consequences (each by Hölder or
Gagliardo–Nirenberg on \(g:=|w|^{3/2}\in H^1\), \(\|g\|_2^2=3\mathcal Q\),
\(\|\nabla g\|_2^2=\tfrac94D_3^{\rm rad}\)):
\[
 \|\nabla A\|_{3/2}\le C\,\mathcal Q^{1/6}D_3^{1/2},\qquad
 \int|w|^5\le C\,\mathcal Q^{2/3}D_3^{\rm rad},\qquad
 \|w\|_{9/2}^3\le C\,\mathcal Q^{1/2}(D_3^{\rm rad})^{1/2},\qquad
 \int|w|\sigma^2\le D_3^{\rm rad}.                                  \tag{1.5}
\]
What (H1') does **not** give: any unweighted integrability of \(\sigma\) or
\(\nabla w\).  Only \(|w|^{1/2}\sigma\in L^2\) is available.  This is the
exact point where the divergence–speed link stops being quantitative (2.4).

Formally, under enough regularity, \(D_{\mathcal Q}=-\int A\cdot\Delta u
=D_3(w)\) (write \(u=w-q\), use \(\Delta q=\nabla\operatorname{div}w\) and
\(\operatorname{div}A=0\), then integrate \(-\int|w|w\cdot\Delta w\) by
parts).  This identity is **not** proved here; it belongs to lane HF18-A.
All bounds below are stated with \(D_3(w)\), and their use in the evolution
would additionally require \(D_{\mathcal Q}\ge cD_3(w)\).

### 1.4 The minimizer class is linear in \(A\)

**Proposition 1.4.** Let \(\mathcal M:=\{w\in L^3:\operatorname{div}(|w|w)=0
\text{ in }\mathcal D'\}\).  Then
\[
 \mathcal M=\{\,|A|^{-1/2}A:\ A\in L^{3/2}(\mathbb R^3;\mathbb R^3),\
 \operatorname{div}A=0\text{ in }\mathcal D'\,\},                    \tag{1.6}
\]
and for every \(w\in\mathcal M\), \(w=w(\mathbb Pw)\) is the minimizing
representative of the solenoidal field \(u=\mathbb Pw\), with
\(q=(I-\mathbb P)w\) and \(\mathcal Q(\mathbb Pw)=\tfrac13\|A\|_{3/2}^{3/2}\).
Conversely \(w(u)\in\mathcal M\) for every solenoidal \(u\in L^3\).

*Proof.* \(z\mapsto|z|z\) is a bijection \(L^3\to L^{3/2}\) with inverse
\(a\mapsto|a|^{-1/2}a\) and \(\|w\|_3^3=\|A\|_{3/2}^{3/2}\); this gives (1.6).
For \(w\in\mathcal M\) put \(u=\mathbb Pw\), \(q=(I-\mathbb P)w\).
Claim: \((I-\mathbb P)L^3\subset\mathcal G_3\).  For \(f\in C_c^\infty\),
\((I-\mathbb P)f=\nabla\psi\) with \(\psi=\partial_i(\Gamma*f_i)\),
\(\Gamma=-1/(4\pi|x|)\); \(\psi\) is smooth, \(\psi=O(|x|^{-2})\),
\(\nabla\psi=O(|x|^{-3})\), so \(\psi,\nabla\psi\in L^3\) and the HF17 cutoff
argument gives \(\nabla\psi\in\mathcal G_3\); density of \(C_c^\infty\) in
\(L^3\) and \(L^3\)-boundedness of \(I-\mathbb P\) extend this.  Hence
\(q\in\mathcal G_3\), \(u=w-q\) is solenoidal, and \(\int|w|w\cdot g=0\) for
all \(g\in\mathcal G_3\) (test with compact gradients, extend by density,
\(|w|w\in L^{3/2}\)).  The functional \(q'\mapsto\tfrac13\int|u+q'|^3\) is
convex and Fréchet differentiable on \(\mathcal G_3\) with derivative
\(\int|u+q'|(u+q')\cdot(\,\cdot\,)\); a stationary point of a convex
differentiable functional is a global minimizer, and HF17 gives uniqueness.
The converse is HF17 (5). \(\square\)

**Scope note.** The one-form, closed-form analogue of this statement — the
unique \(L^p\)-norm minimizer \(h\) in a reduced cohomology class satisfies
\(d^*(|h|^{p-2}h)=0\) — is Stern, *\(L_p\)-cohomology and the geometry of
\(p\)-harmonic forms*, arXiv:2403.19481v2, Lemma 2.2 and Theorem 2.9
(*Nonlinear Hodge Theorem*), **directly inspected** (pages 3–4); he
attributes the ideas to Scott 1995 and Iwaniec–Scott–Stroffolini 1999.
Our \(w\) is not closed (\(\operatorname{curl}w=\operatorname{curl}u\ne0\)),
so (1.6) is the vector-field variant; no novelty is claimed for the
mechanism.  The Iwaniec–Martin \(L^p\) Hodge decomposition (Acta Math. 170
(1993)) was reachable only as **metadata** this wave; the linear
\(L^3=\mathbb PL^3\oplus\mathcal G_3\) splitting used above is proved
directly through Riesz transforms and needs no citation.

Practical consequence of (1.6): test fields in the minimizer class are
produced *linearly* by choosing any solenoidal \(A\) (for instance
\(A=\operatorname{curl}\Psi\) with \(\Psi\in C_c^\infty\)), which is how the
counterexample family of 2.4 is built.

### 1.5 The link \(q\leftrightarrow\sigma\)

Under (H1) and \(\sigma\in L^{3/2}\): \(\operatorname{div}w=-\sigma\in
L^{3/2}\) (Prop. 1.1(iv)), and
\[
 q=\nabla\Delta^{-1}\operatorname{div}w=-\nabla(\Gamma*\sigma)
 =\frac{1}{4\pi}\int\frac{x-y}{|x-y|^3}\,\sigma(y)\,dy ,            \tag{1.7}
\]
as \(L^3\) functions: the right side is in \(L^3\) by
Hardy–Littlewood–Sobolev (\(I_1:L^{3/2}(\mathbb R^3)\to L^3\), exponent
\(1/3=2/3-1/3\); Lieb–Loss *Analysis* Thm 4.3 / Stein *Singular Integrals*
Ch. V §1 Thm 1, cited from memory, not re-inspected this wave), is a
gradient, and has divergence \(-\sigma=\operatorname{div}q\); the difference
with \(q\) is a curl-free divergence-free \(L^3\) field, hence zero.  So
\[
 \|q\|_3\le C_{\rm HLS}\,\|\sigma\|_{3/2}\qquad\big[(a,\lambda)\text{-consistent: both sides }(a,\lambda^0)\big].
                                                                    \tag{1.8}
\]
Under (1.6) the same statement reads: \(q\) is the gradient part of
\(|A|^{-1/2}A\), i.e. of the "square root" of a solenoidal field, and is
driven by the transport of the speed along its own direction,
\(|w|\sigma=(w\cdot\nabla)|w|\).

## 2. Quantitative bounds and their scaling

### 2.1 \(\|q\|_3\)

Always: \(\|q\|_3\le\|I-\mathbb P\|_{3\to3}\|w\|_3=C(3\mathcal Q)^{1/3}\).
Hence (1.8) is only informative where \(\|\sigma\|_{3/2}\ll\|w\|_3\)
(nearly speed-transporting \(w\)); as a bound in terms of controlled
quantities it is *weaker* than the trivial one, because
\(\|\sigma\|_{3/2}\) is uncontrolled (2.4).

Exponent analysis for \(\|q\|_3^3\le C D_3^aQ^bE^c\):
\((3,0)=a(3,2)+b(3,0)+c(2,-1)\) forces \(c=2a\), \(7a+3b=3\).  \(a=0\) is
the trivial bound.  For \(a>0\) the energy must enter.  Gagliardo–Nirenberg
on \(g=|w|^{3/2}\) (\(\|g\|_2\le\|g\|_{4/3}^{4/7}\|g\|_6^{3/7}\)) gives the
*true* inequality
\[
 \|w\|_3^3\le C\,\|w\|_2^{12/7}\,(D_3^{\rm rad})^{3/7},              \tag{2.1}
\]
but with \(\|w\|_2\), not \(\|u\|_2\).  Whether \(\|w(u)\|_2\le C\|u\|_2\)
on \(L^2\cap L^3\) (an \(L^2\) bound for the nonlinear projection) is
**open** here; no proof or counterexample was found in the time box.  So no
member of this family with \(a>0\) is available with input-only \(E\).

### 2.2 \(\int|q|^2|w|^3\): the only scaling-admissible exponents

\((5,2)=a(3,2)+b(3,0)+c(2,-1)\) gives \(a=1+c/2\), \(b=\tfrac23-\tfrac76c\),
\(0\le c\le4/7\).  The energy-free member \(c=0\), \(a=1\), \(b=2/3\) is:

**Proposition 2.1.** Under (H1'),
\[
 \boxed{\ \int|q|^2|w|^3dx\ \le\ C\,\|w\|_3^2\,D_3^{\rm rad}(w)
 \ =\ C'\,\mathcal Q^{2/3}\,D_3^{\rm rad}(w).\ }                      \tag{2.2}
\]
*Proof.* \(\int|q|^2|w|^3=\|q\,g\|_2^2\le\|q\|_3^2\|g\|_6^2\le
C\|w\|_3^2\|\nabla g\|_2^2\) by Hölder (\(\tfrac23+\tfrac13=1\)), Sobolev
\(H^1(\mathbb R^3)\subset L^6\), and \(\|q\|_3\le C\|w\|_3\). \(\square\)

Remarks. (a) The divergence structure is not used; (2.2) holds for every
\(w\in L^3\) with \(|w|^{3/2}\in H^1\) and any \(q\) with \(\|q\|_3\le
C\|w\|_3\).  (b) It is sharp on single-scale fields (\(A=\operatorname{curl}\Psi\),
\(|A|\sim\varepsilon^2\) on \(B_R\)): both sides \(\sim\varepsilon^5R^3\).
(c) Members with \(c>0\) would need \(E\) in place of \(\|w\|_2^2\) and are
open for the same reason as 2.1.  (d) This is exactly the second factor in
the Cauchy–Schwarz split of the high-strain term (3.3(c)); its consequence
there is a small-data closure only.

### 2.3 \(\|\sigma\|_{3/2}\): scaling-admissible exponents

\((\tfrac32,0)=a(3,2)+b(3,0)+c(2,-1)\): \(c=2a\), \(7a+3b=\tfrac32\).
All these members, and every other function of \((D_3,\mathcal Q,E)\), are
refuted in 2.4.

### 2.4 Obstruction: \(\|\sigma\|_{3/2}\) is not a function of \((D_3,\mathcal Q,E)\)

**Proposition 2.2.** There is a family \(w_\delta\in\mathcal M\),
\(\delta\downarrow0\), of smooth compactly supported fields (so (H1') holds
and \(u_\delta=\mathbb Pw_\delta\in L^2\cap L^3\)) with
\[
 D_3(w_\delta)\le C,\qquad \tfrac1C\le\mathcal Q(u_\delta)\le C,\qquad
 \|u_\delta\|_2^2\le C,\qquad
 \|\sigma_\delta\|_{3/2}^{3/2}\ \ge\ c\,\delta^{-5/4}\to\infty .
\]
In particular no inequality \(\|\sigma\|_{3/2}\le\Phi(D_3,\mathcal Q,E)\)
holds on \(\mathcal M\), for any function \(\Phi\); in particular none of
the products of 2.3, with either sign of \(b\).

*Construction.* Fix a bulk field \(A_0=\operatorname{curl}(\phi_0e_3)\),
\(\phi_0=(1-|x|^2)^4_+\), so \(|A_0|=8(1-|x|^2)^3_+\rho\) (\(\rho\) the
cylindrical radius): its zero set is a segment and a sphere with finite
vanishing order, so \(w_0=|A_0|^{-1/2}A_0\) has finite
\(D_3,\mathcal Q,\|\sigma\|_{3/2}\), and \(\mathcal Q(\mathbb Pw_0)>0\).
Add, at a centre \(x_0\) with \(B_R(x_0)\cap B_1=\emptyset\), the
oscillatory field
\[
 A_1=\operatorname{curl}\big(\psi\,e_3\big),\quad
 \psi(x)=\delta^2\,(2+\cos kx_1)\,\frac{\sin kx_2}{k}\,\chi\!\Big(\frac{x-x_0}{R}\Big),
\]
so that on \(B_R(x_0)\), away from the cutoff annulus,
\(A_1=\delta^2\big((2+\cos kx_1)\cos kx_2,\ \sin kx_1\sin kx_2,\ 0\big)\),
and \(A=A_0+A_1\), \(w_\delta=|A|^{-1/2}A\in\mathcal M\) by (1.6).
On \(B_R(x_0)\): \(|w|\sim\delta\) (zeros only on lines, codimension two),
\(|\nabla w|\sim\delta k\), \(|\sigma|\sim\delta k\) on a set of proportional
measure (the speed varies along \(\hat w\): the \(x_2\)-dependence of
\(|A_1|\) is seen along \(\hat w\approx\pm e_2\) where \(\cos kx_2\approx0\),
and the \(x_1\)-dependence along \(\hat w\approx\pm e_1\) elsewhere).  The
cutoff annulus contributes \(O((kR)^{-1})\) relative corrections.  Hence, per
unit volume of \(B_R\), \(\int|\sigma|^{3/2}\sim(\delta k)^{3/2}\),
\(\int|w||\nabla w|^2\sim\delta^3k^2\), \(\int|w|^3\sim\delta^3\),
\(\int|w|^2\sim\delta^2\); \(\|u\|_2\le\|w\|_2\) since \(\mathbb P\) is an
\(L^2\)-orthogonal projection, and \(\mathcal Q(\mathbb Pw_\delta)\ge
c\|\mathbb Pw_\delta\|_3^3\) stays bounded below by the bulk part because the
two supports are disjoint and the oscillatory part contributes only
\(O(\delta)\) to \(\|w\|_3^3\).  Choose
\[
 R^3=\delta^{-2},\qquad k=\delta^{-1/2}\quad(\Rightarrow kR=\delta^{-7/6}\to\infty):
\]
\(\int|w||\nabla w|^2\sim\delta^3k^2R^3=1\), \(\int|w|^3\sim\delta\),
\(\int|w|^2\sim1\), \(\int|\sigma|^{3/2}\sim(\delta k)^{3/2}R^3=\delta^{-5/4}\). \(\square\)

**Numerical check** (scratch script, periodic cell of the oscillatory
profile, \(N=384^2\), central differences; per-unit-volume integrals):

| \(\delta\) | \(k\) | \(\int|\sigma|^{3/2}\) | \(D_3\) | \(\int|w|^3\) | rel. err. of \(\operatorname{div}w+\sigma=0\) |
|---|---|---|---|---|---|
| 1 | 1 | 1.890e-1 | 2.186 | 1.848 | 1.3e-3 |
| 1 | 2 | 5.347e-1 | 8.743 | 1.848 | 1.3e-3 |
| 1 | 4 | 1.512 | 34.97 | 1.848 | 1.3e-3 |
| 0.5 | 1 | 6.683e-2 | 2.732e-1 | 2.310e-1 | 1.3e-3 |
| 0.25 | 1 | 2.363e-2 | 3.415e-2 | 2.887e-2 | 1.3e-3 |

Ratios: \(2^{1.5},4^{1.5}\) for the \(\sigma\)-integral in \(k\); \(4,16\)
for \(D_3\); \((1/2)^{1.5},(1/4)^{1.5}\) and \((1/2)^3,(1/4)^3\) in
\(\delta\).  The pointwise identity (1.3) holds to discretisation accuracy
on the family.  This is a bounded computation confirming the asymptotic
orders, not part of the proof.

**Mechanism.** \(|\sigma|^{3/2}=(|w|^{1/2}|\sigma|)^{3/2}|w|^{-3/4}\): the
dissipation weight \(|w|\) is small precisely where the family oscillates.
The loss is at *low amplitude with many oscillations*, not at the zero set
(Remark 1.2) and not at high frequency alone.  Consequently the link (1.7)–(1.8)
is an exact representation of \(q\) but not an estimate in terms of the
dissipation: any use of \(\|\sigma\|_{3/2}\) is a hidden hypothesis.

## 3. The high-strain term through the link

Throughout, \(u\in H^m(\mathbb R^3)\) solenoidal, \(m\ge4\) (frozen time on
the classical interval), \(v=S_Lu\), \(u^{hi}=u-v\in H^m\subset C^2_b\),
\(\operatorname{div}u^{hi}=0\), \(\omega=\operatorname{curl}u\).

### 3.1 Exact rewriting with no regularity of \(w\)

Let \(F:=(A\cdot\nabla)u^{hi}\in L^{3/2}\).  Since \(\operatorname{div}A=0\)
in \(\mathcal D'\) and \(u^{hi}\in C^1_b\), \(F=\partial_i(A_iu^{hi})\) in
\(\mathcal D'\) (test \(\operatorname{div}A=0\) against \(C^1_c\) functions by
mollification).  Define the *pressure-type potential of the pair*
\[
 \Pi_L:=R_iR_j\big(A_iu^{hi}_j\big)\in L^{3/2},\qquad
 \nabla\Pi_L=(I-\mathbb P)F\in L^{3/2},\quad\text{so }\Pi_L\in W^{1,3/2}\subset L^3.
                                                                    \tag{3.1}
\]
(For Navier–Stokes itself \(p=R_iR_j(u_iu_j)\); \(\Pi_L\) is the same
operator applied to \(A\otimes u^{hi}\).)  Because \(q\in\mathcal G_3\) is
annihilated by the solenoidal part \(\mathbb PF\) (test with compact
gradients, extend by density),
\[
 \boxed{\ K_L=-\int q\cdot\nabla\Pi_L\,dx
 =\big\langle \operatorname{div}w,\ \Pi_L\big\rangle_{W^{-1,3}\times W^{1,3/2}} .\ }
                                                                    \tag{3.2}
\]
This is rigorous at the audited \(L^3\) level and displays the link: the
high-strain form is the pairing of the divergence of the representative,
i.e. of the speed-transport source, with a pressure.  Under (H1) and
\(\sigma\in L^{3/2}\),
\[
 K_L=-\int_{\{w\ne0\}}(\hat w\cdot\nabla|w|)\,\Pi_L\,dx .            \tag{3.3}
\]
Using \(\operatorname{div}u^{hi}=0\) once more,
\(\nabla\Pi_L=(I-\mathbb P)\big[(u^{hi}\cdot\nabla)A\big]\) whenever
\(\nabla A\in L^{3/2}\) (true under (H1'), (1.5)).

### 3.2 Two exact identities for the full flux

**Proposition 3.1.** With \(\mathfrak T:=-\int A\cdot((u\cdot\nabla)u)
=\mathcal Q'+\nu D_{\mathcal Q}\) (HF17 (13)):
\[
 \text{(Lamb form)}\qquad
 \mathfrak T=-\int A\cdot(\omega\times u)=\int|w|\,\omega\cdot(q\times u)\,dx,
                                                                    \tag{3.4}
\]
\[
 \text{(orthogonality)}\qquad \int A\cdot\big((q\cdot\nabla)u\big)dx=0,
                                                                    \tag{3.5}
\]
\[
 \boxed{\ \text{(strain form)}\qquad
 \mathfrak T=-\int A\cdot\big((w\cdot\nabla)u\big)dx
 =-\int|w|\;w\cdot S(u)\,w\;dx,\qquad S(u)=\tfrac12(\nabla u+\nabla u^T).\ }
                                                                    \tag{3.6}
\]
No derivative of \(w\) or \(q\) is taken.

*Proof.* (3.4): \((u\cdot\nabla)u=\nabla(|u|^2/2)+\omega\times u\) pointwise;
\(|u|^2\in W^{1,3}\) (\(u\in L^\infty\cap L^6\), \(\nabla u\in L^3\)), so the
HF17 cutoff–mollification argument gives \(\nabla|u|^2\in\mathcal G_3\) and
\(\int A\cdot\nabla|u|^2=0\).  Then \(A\cdot(\omega\times u)=
A\cdot(\omega\times w)-A\cdot(\omega\times q)=-A\cdot(\omega\times q)\)
because \(A\parallel w\); all terms are in \(L^1\)
(\(A\in L^{3/2}\), \(\omega\in L^\infty\), \(q\in L^3\)).  Finally
\(A\cdot(\omega\times q)=|w|\,\omega\cdot(q\times w)=|w|\,\omega\cdot(q\times u)\).
(3.5): the pointwise identity
\((A\times\omega)_j=A_k\partial_ju_k-A_k\partial_ku_j\) gives
\(q\cdot(A\times\omega)=A\cdot((q\cdot\nabla)u)-q\cdot((A\cdot\nabla)u)\), and
\(\int q\cdot(A\times\omega)=\int A\cdot(\omega\times q)=\mathfrak T\) by
(3.4).  The reviewed inner-variation identity HF17 (9) is
\(\mathfrak T=-\int q\cdot((A\cdot\nabla)u)\).  Subtracting gives (3.5).
(3.6): \(-\int A\cdot((u\cdot\nabla)u)=-\int A\cdot((w\cdot\nabla)u)
+\int A\cdot((q\cdot\nabla)u)\) and (3.5); then
\(A\cdot((w\cdot\nabla)u)=|w|w_iw_j\partial_iu_j\), symmetric in \(ij\). \(\square\)

Formal cross-check of (3.5) under (H1') and \(w\in L^5\) (given by (1.5)):
\(\int|w|w_iq_j\partial_ju_i=\int|w|^2q\cdot\nabla|w|-\int A\cdot\nabla(|q|^2/2)
=-\tfrac13\int|w|^3\operatorname{div}w-0=0\) by (1.4) with \(\alpha=3\).
The two routes agree.

**Reading of (3.6).** For the standard cubic energy the analogous term
\(\int|u|u\cdot S(u)u=\int u\cdot\nabla(|u|^3/3)\) vanishes and the whole
nonlinearity sits in the pressure; for the quotient functional the pressure
vanishes and the whole nonlinearity is the strain of \(u\) along the
direction of the non-solenoidal representative, weighted by the cube of its
speed: \(\mathfrak T=-\int|w|^3\,\hat w\cdot S(u)\hat w\).  Under (H1') and
\(u=w-q\), \(\hat w\cdot S(u)\hat w=-\operatorname{div}w-\hat w\cdot\nabla^2\varphi\,\hat w
=-\operatorname{tr}\big((I+\hat w\otimes\hat w)\nabla^2\varphi\big)\) with
\(q=\nabla\varphi\), \(\Delta\varphi=\operatorname{div}w=-\sigma\); together
with (1.4) this gives the third form
\(\mathfrak T=\int|w|^3\,\partial_{\hat w\hat w}\varphi\): the second
derivative of the potential of \(q\) along \(\hat w\), whose source is
\(-\sigma\), again the \(\hat w\hat w\)-component of a gradient.  The
analogy with vortex stretching \(\int|\omega|^2\hat\omega\cdot S\hat\omega\)
is exact in form and opposite in sign.

**Split.** With \(K^S_L:=-\int|w|\,w\cdot S(u^{hi})\,w\),
\[
 K_L-K^S_L=\int q\cdot((A\cdot\nabla)v)-\int A\cdot((w\cdot\nabla)v),\qquad
 |K_L-K^S_L|\le C2^{5L/2}E_0^{1/2}\mathcal Q ,                      \tag{3.7}
\]
so the frozen gap may be posed for \(K^S_L\) with the same quantifiers.
(3.4)–(3.7) are equivalent identities; PLAN's rule that an equivalent identity
alone discharges nothing applies to every one of them.

### 3.3 Attempts to control \(K_L\); the first uncontrolled term

Every attempt below is displayed with the exact point of failure and its
\((a,\lambda)\) scaling.  Target: \(K_L\le\theta\nu D_3+M\mathcal Q+(\text{input})\)
pointwise in time, or its integrated form.

(a) *Unweighted link.* From (3.3), \(|K_L|\le\|\sigma\|_{3/2}\|\Pi_L\|_3\).
The second factor: \(\Pi_L=R_iR_j(A_iu^{hi}_j)\) and, under (H1'),
\(\Delta\Pi_L=-\partial_jA_i\,\partial_iu^{hi}_j\) is a sum of div–curl
products (\(\nabla A_i\) curl-free, \(\partial_iu^{hi}\) divergence-free), so
by the Coifman–Lions–Meyer–Semmes div–curl theorem (J. Math. Pures Appl. 72
(1993), the \(E\cdot B\in\mathcal H^1\) statement; **metadata only** this
wave, the primary text was not reachable) and \(I_2:\mathcal H^1\to L^3\),
\(\|\Pi_L\|_3\le C\|\nabla A\|_{3/2}\|\nabla u^{hi}\|_3\le
C\mathcal Q^{1/6}D_3^{1/2}\|\nabla u^{hi}\|_3\).  Two uncontrolled factors:
\(\|\sigma\|_{3/2}\) (Prop. 2.2, not a function of the controlled
quantities) and \(\|\nabla u^{hi}\|_3\sim(a,\lambda)\) (unweighted gradient;
\(\int|\nabla u|^3\) is not bounded by \(D_3\) for the same weight reason).
Even granting both, the product \(\mathcal Q^{1/6}D_3^{1/2}\|\sigma\|_{3/2}\|\nabla u^{hi}\|_3
\sim(a^4,\lambda^2)\) absorbs into \(\theta\nu D_3\) only if
\(\mathcal Q^{1/3}\|\sigma\|_{3/2}^2\|\nabla u^{hi}\|_3^2\lesssim\nu^2D_3\), a
smallness of \(\|u\|_3/\nu\).

(b) *Weighted link.* \(-\int\sigma\Pi_L=-\int(|w|^{1/2}\sigma)(|w|^{-1/2}\Pi_L)\),
so with (1.5)
\[
 |K_L|\le (D_3^{\rm rad})^{1/2}\Big(\int|w|^{-1}\Pi_L^2dx\Big)^{1/2},\qquad
 \int|w|^{-1}\Pi_L^2\sim(a^5,\lambda^2).                              \tag{3.8}
\]
**First uncontrolled term of the link route:** \(\int|w|^{-1}\Pi_L^2\).  It
is a weighted \(L^2\) norm of a Riesz-transform image with the weight
\(|w|^{-1}\), which is not locally integrable across codimension-one zeros of
\(w\) with \(|w|\sim\operatorname{dist}\) (Remark 1.2) while \(\Pi_L\) is
nonlocal and need not vanish there; so the term can be \(+\infty\) on
\(\mathcal M\).  Where finite, Young gives
\(K_L\le\theta\nu D_3+(4\theta\nu)^{-1}\int|w|^{-1}\Pi_L^2\), and heuristically
\(\Pi_L\sim|w|^2|u^{hi}|\) so the remainder is \(\sim\nu^{-1}\int|w|^3|u^{hi}|^2\);
absorbing that into \(\theta\nu\int|w||\nabla w|^2\) needs
\(|u^{hi}|\lesssim\nu2^L\) pointwise, a supercritical sup bound on the
high frequencies (\(\|u^{hi}\|_\infty\sim(a,\lambda)\)), i.e. a regularity
criterion.  This is the packet's forbidden "bound by the norm to be
controlled".

(c) *Strain form.* \(|K^S_L|\le\int|w|^3|S(u^{hi})|
=\int(|w|^{1/2}|S(u^{hi})|)\,|w|^{5/2}\le\big(\int|w||\nabla u^{hi}|^2\big)^{1/2}
\big(\int|w|^5\big)^{1/2}\), and by (1.5)
\[
 |K^S_L|\le C\,\mathcal Q^{1/3}(D_3^{\rm rad})^{1/2}
 \Big(\int|w||\nabla u^{hi}|^2\Big)^{1/2}\sim(a^4,\lambda^2).           \tag{3.9}
\]
(Equivalently, using (2.2) on the Cauchy–Schwarz split of \(K_L\) itself:
\(|K_L|\le(\int|w||\nabla u^{hi}|^2)^{1/2}(\int|q|^2|w|^3)^{1/2}\), same bound.)
Two obstructions, in order: (i) the weighted Calderón–Zygmund inequality
\(\int|w||\nabla(I-S_L)\mathbb Pw|^2\le C\int|w||\nabla w|^2\) would need
\(|w|\) to be an \(A_2\) weight uniformly, which fails on \(\mathcal M\)
(\(|w|\) may vanish on open sets: choose \(A=0\) on a ball); (ii) even
granting (i), Young leaves \(K^S_L\le\theta\nu D_3+C\theta^{-1}\nu^{-1}\mathcal Q^{2/3}D_3\),
which closes only if \(\mathcal Q^{2/3}\lesssim\theta\nu^2\), i.e.
\(\|u\|_3\lesssim\nu\): hidden smallness (the classical small-\(L^3\) regime).
Both are exact, scaling-consistent obstructions to this split, not to the target.

(d) *Sign.* None of (3.2)–(3.6) has a sign: \(\hat w\cdot S\hat w\) ranges
over \([\lambda_{\min}(S),\lambda_{\max}(S)]\) with \(\operatorname{tr}S=0\),
and \(\Pi_L\) is a Riesz image without pointwise sign.  Averaging over
directions is unavailable because \(\hat w\) is fixed by \(A\).

**Conclusion of §3.** The divergence–speed link converts \(K_L\) into
\(\langle\operatorname{div}w,\Pi_L\rangle\) and \(\mathfrak T\) into a pure
strain form, with every factor identified; after any Hölder/Young split the
first term not controlled by \((D_3,\mathcal Q,\text{input})\) is
\(\int|w|^{-1}\Pi_L^2\) in route (b) and the weighted high-frequency
dissipation \(\int|w||\nabla u^{hi}|^2\) times the small-data factor
\(\mathcal Q^{1/3}/\nu\) in route (c).  These are the same critical
obstruction as HIGH-PRESSURE in a different coordinate system, as the packet
predicts for any equivalent rewriting.

## 4. New structural facts (exact scope)

1. (Prop. 1.1) Under (H1), \(\operatorname{div}w=-\hat w\cdot\nabla|w|\) a.e.
   on \(\{w\ne0\}\), \(\operatorname{div}w=0\) a.e. on \(\{w=0\}\);
   equivalently \(\operatorname{tr}((I+\hat w\otimes\hat w)\nabla w)=0\) a.e.
   Without (H1) only (1.1) holds.
2. (Prop. 1.4) \(\mathcal M=\{|A|^{-1/2}A:\ A\in L^{3/2}\ \text{solenoidal}\}\);
   the minimizing representative of \(u\) is the unique \(w\in\mathcal M\)
   with \(\mathbb Pw=u\); \(\mathcal Q(u)=\tfrac13\|A\|_{3/2}^{3/2}\).
   Known in the closed-form setting (Stern Thm 2.9, inspected); vector variant
   here.  Enables linear construction of test fields.
3. (1.7)–(1.8) \(q=-\nabla\Gamma*\sigma\), \(\|q\|_3\le C\|\sigma\|_{3/2}\),
   under (H1) and \(\sigma\in L^{3/2}\).
4. (Prop. 2.1) \(\int|q|^2|w|^3\le C\mathcal Q^{2/3}D_3^{\rm rad}(w)\) under
   (H1'); exponents forced by scaling; sharp on single-scale fields.
5. (Prop. 2.2) \(\|\sigma\|_{3/2}\) is not bounded by any function of
   \((D_3,\mathcal Q,\|u\|_2^2)\) on \(\mathcal M\); explicit family,
   numerically checked orders.
6. (3.2) \(K_L=\langle\operatorname{div}w,\Pi_L\rangle\),
   \(\Pi_L=R_iR_j(A_iu^{hi}_j)\), rigorous at the \(L^3\) level.
7. (Prop. 3.1) On the classical class, without any regularity of \(w\):
   \(\int A\cdot((q\cdot\nabla)u)=0\) and
   \(\mathcal Q'+\nu D_{\mathcal Q}=-\int|w|\,w\cdot S(u)\,w
   =\int|w|\,\omega\cdot(q\times u)\).  Depends on the reviewed HF17 (9).
8. (3.7) The frozen gap is equivalent, up to the input Gronwall coefficient,
   to the same bound for \(K^S_L=-\int|w|\,w\cdot S(u^{hi})\,w\).

## 5. Frontier record

**MODE / RESULT:** DISCOVER.  Rigorous scope of the divergence–speed identity
fixed; minimizer class linearised in \(A\); transport flux shown to be a pure
weighted strain form; high-strain term rewritten as a divergence–pressure
pairing; one true and one false quantitative inequality established with
scaling; no estimate for the gap.

**CLAIM AND SCOPE:** Items 1–8 of §4 with the hypotheses displayed there:
(H1)/(H1') for pointwise and weighted statements, \(u\in H^m\), \(m\ge4\)
frozen-time solenoidal for §3, HF17 (9) as reviewed input.  \(D_{\mathcal Q}=D_3(w)\)
is *not* claimed.

**EVIDENCE:** Chain rule and Sobolev level-set facts for §1; convexity and
Riesz-transform Helmholtz splitting for Prop. 1.4; HLS for (1.8);
Hölder–Sobolev for (2.2); explicit solenoidal-potential family with parameter
choice \(R^3=\delta^{-2}\), \(k=\delta^{-1/2}\) for Prop. 2.2, orders
confirmed numerically; distributional product rule and \(L^{3/2}\) Helmholtz
splitting for (3.2); vector identities plus the reviewed inner-variation
identity for Prop. 3.1, cross-checked formally through (1.4).
Sources: Stern arXiv:2403.19481 Lemma 2.2, Thm 2.9 (directly inspected);
Iwaniec–Martin Acta 170 (1993) and CLMS J. Math. Pures Appl. 72 (1993)
(metadata only); HLS and Gilbarg–Trudinger Lemmas 7.5, 7.7 (standard, from
memory).  Tolksdorf 1984, DiBenedetto 1983, Lieberman 1988, Uraltseva 1968
were not invoked: the equation \(\operatorname{div}(|u+\nabla\varphi|(u+\nabla\varphi))=0\)
degenerates on the moving set \(\{\nabla\varphi=-u(x)\}\), outside the
standard structure conditions; that question is lane HF18-A's.

**FIRST GAP:** the implication "\(K_L=\langle\operatorname{div}w,\Pi_L\rangle\)
(or \(K^S_L=-\int|w|w\cdot S(u^{hi})w\)) admits a bound
\(\le\theta\nu D_{\mathcal Q}+M\mathcal Q+\text{input}\)".  After the weighted
split the first uncontrolled term is \(\int|w|^{-1}\Pi_L^2\,dx\sim(a^5,\lambda^2)\),
possibly infinite on \(\mathcal M\); after the strain split it is
\(\mathcal Q^{1/3}\nu^{-1}\int|w||\nabla u^{hi}|^2\), controlled only under
\(\|u\|_3\lesssim\nu\) plus a false weighted Calderón–Zygmund inequality.

**SURVIVING CONDITIONAL SUFFIX:** If \(D_{\mathcal Q}\ge cD_3(w)\) (HF18-A)
and any one-sided spacetime bound
\(\int_0^\tau(-\int|w|w\cdot S(u^{hi})w)\,dt\le\theta\nu\int_0^\tau D_3(w)\,dt+A_{\rm input}\)
were proved, then (3.7), HF17 (13)–(14) and Gronwall bound \(\mathcal Q\),
hence \(\|u\|_3\), through the putative endpoint.  Equivalent to the frozen
gap; not proved.

**NON-CLAIMS:** no smoothness or Sobolev regularity of \(w\) (H1, H1' are
hypotheses); no identification \(D_{\mathcal Q}=D_3(w)\); no bound or sign
for \(K_L\), \(K^S_L\), or \(\mathfrak T\); no \(L^2\) bound for the
nonlinear projection \(u\mapsto w(u)\); no applicability of p-Laplace
regularity theorems; no continuation criterion, HIGH-STRAIN or HIGH-PRESSURE
theorem, or regularity result; no novelty for the nonlinear Hodge
construction (Stern/Scott/Iwaniec–Scott–Stroffolini).  The counterexample
family refutes static inequalities on \(\mathcal M\); it says nothing about
which \(w\) occur along Navier–Stokes trajectories.

**NEXT DISTINCT ACTION:** test the strain form (3.6) rather than the
divergence form: decide whether the weighted strain functional
\(w\mapsto\int|w|^3\hat w\cdot S(\mathbb Pw)\hat w\) admits a one-sided
interpolation \(\le\theta\nu D_3(w)+C(\nu,E_0,2^L)\mathcal Q\) on the *linear*
family \(A=\operatorname{curl}\Psi\) (Prop. 1.4), by searching for a
counterexample family with \(\hat w\) aligned with the expanding
eigenvector of \(S(\mathbb Pw)\) at high frequency; a family with
\(-\int|w|^3\hat w\cdot S\hat w\gg\nu D_3\) at bounded \(\mathcal Q\) would
show that the gap cannot be closed by a static inequality and must use the
dynamics.
