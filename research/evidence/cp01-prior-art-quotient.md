# CP01: prior art for the cubic gradient-quotient functional

Status: bounded prior-art audit, 2026-09-05.  Scope: the objects of
`hf17-quotient-functional.md`, `hf18-hodge-regularity.md`,
`hf18-divergence-speed-link.md` and manuscript `sec:quotient`
(`../navier-paper/main.tex`, from `\label{sec:quotient}`).

MODE: SOURCE AUDIT.  No mathematical claim of the programme is proved,
strengthened or weakened here.  **No novelty is claimed anywhere in this
note**, and an "unlocated" verdict below is a statement about the reach of this
bounded search, *not* evidence of novelty.

Tags: **[DI]** = statement read directly in the cited source in this lane;
**[MO]** = metadata only (bibliographic identity verified, content not read, or
content verified only through a directly inspected citing source — said
explicitly where that is the case).

## 0. The programme's objects, as fixed for comparison

- (Q) \(\mathcal Q(u)=\inf_{q\in\mathcal G_3}\tfrac13\|u+q\|_3^3\),
  \(\mathcal G_3=\overline{\nabla C_c^\infty}^{L^3}(\mathbb R^3;\mathbb R^3)\),
  \(u\) solenoidal.
- (W) unique minimizer \(w=u+q\); Euler–Lagrange \(\int|w|w\cdot g=0\) for all
  \(g\in\mathcal G_3\), i.e. \(\operatorname{div}(|w|w)=0\), with
  \(\operatorname{curl}w=\operatorname{curl}u\neq0\) prescribed.
- (C) coercivity \(\|u\|_3^3/(3\|\mathbb P\|_{3\to3}^3)\le\mathcal Q\le\|u\|_3^3/3\).
- (S) cubic homogeneity and invariance under \(u\mapsto\lambda u(\lambda\cdot)\).
- (H) heat monotonicity \(\mathcal Q(e^{t\Delta}u)\le\mathcal Q(u)\).
- (D) Fréchet derivative \(D\mathcal Q(u)[h]=\int|w|w\cdot h\); exact
  annihilation of \(\mathcal G_3\), hence of \(\nabla p\).
- (E) \(D_{\mathcal Q}(u)=-\int|w|w\cdot\Delta u=D_3(w)
  =\int(|\nabla V|^2-\tfrac19|\nabla|V||^2)\), \(V=|w|^{1/2}w\), and
  \(D_{\mathcal Q}\ge c\|u\|_9^3\).
- (R) \(V\in H^1(\mathbb R^3)\), \(A=|w|w\in W^{1,3/2}(\mathbb R^3)\), by a
  global Bojarski–Iwaniec difference-quotient argument against all of
  \(\mathcal G_3\).
- (L) \(\mathcal Q\) is a Lyapunov functional under critical smallness
  \(\|w\|_3<\nu/C_*'\); the arbitrary-data absorption
  (`eq:quotient-gap`, HIGH-STRAIN) is open.

## 1. Hits

### 1.1 Sibner–Sibner 1970 — the same variational mechanism, closed datum, bounded density

**L. M. Sibner and R. J. Sibner, "A non-linear Hodge–de Rham theorem",
Acta Math. 125 (1970) 57–73** (Project Euclid, `euclid.acta/1485889662`;
full text read). **[DI]**

What it defines and proves (pages as printed):

- p. 58: \(E_p\) is the \(L^2\)-closure of exact forms \(d\xi\) with compact
  carrier, \(E_p^*\) the closure of coexact forms; \(E_p^{*\perp}\) is the
  closure of closed forms.
- p. 59, admissibility: \(\rho(x,a)\in C^{1+\alpha}\) with
  \(k^{-1}\le\rho\le k\) and \(\frac{d}{da}(a\rho^2(x,a))>0\) on
  \(0\le a<a_\rho\); "regular" adds \(a_\rho=\infty\) and
  \(k_1^{-1}<\frac{d}{da}(a\rho^2)<k_1\).
- p. 59–60, NON-REGULAR / REGULAR THEOREM: for \(M\) compact and \(\gamma\in
  E_1^{*\perp}\) there is a unique \(\omega_t\in\Omega^1\) with
  (i) \(d\omega_t=0\), (ii) \(\delta(\rho\,\omega_t)=0\) with
  \(\rho=\rho(x,Q^1(\omega_t))\), (iii) \(\omega_t-t\gamma\in E_1\) (and exact
  if \(\gamma\in\Omega^1\)), (iv) \(\omega_t\) \(\rho\)-subsonic.  In the
  regular case \(t_\rho=\infty\) and \(M\) need not be compact.
- p. 63 (§3.2), plain-language form: *"Let \(M\) be a Riemannian manifold (not
  necessarily compact) and \(\rho\) regular.  Given a closed 1-form \(\gamma\)
  there exists a \(\rho\)-harmonic \(\omega\in\Omega^1\) such that
  \(\omega-\gamma\) is exact."*
- §4 (pp. 65–68) is the variational construction: \(F(x,v)=\int_0^Q\mu\,d\xi\)
  convex (Thm 4.1), \(I(v)=\int F-2(v,*\gamma)\) has a minimizer by weak lower
  semicontinuity on a weakly closed affine class (Lemma 4.2), the Euler
  equation is the membership statement \(\mu v_0-*\gamma\in E^*_{n-1}\), and
  the minimizer is unique by strict convexity (Lemma 4.3, Thm 4.2).
  Thm 4.3: the extremal is \(C^{1,\alpha}_{\rm loc}\) (and \(C^\infty\) for
  \(\mu\in C^\infty\)) — *for regular \(\mu\) only*.

Comparison. This is the same variational mechanism as (Q)–(W): minimize a
convex integrand of the pointwise norm over a coset of (co)exact forms in a
reflexive space; existence by weak lower semicontinuity, uniqueness by strict
convexity, and an Euler–Lagrange condition asserting that the *nonlinear*
expression \(\rho(|\omega|^2)\omega\) is (co)closed.  Two independent
differences, both of which matter:

1. **Closed datum.**  Sibner–Sibner prescribe a closed \(\gamma\), so their
   minimizer satisfies \(d\omega=0\) — curl-free.  The programme's datum is
   \(u\) with \(\operatorname{curl}u\ne0\), so \(w\) is *not* closed and
   \(\operatorname{curl}w=\operatorname{curl}u\) is prescribed and nonzero.
   This is the exact obstruction already recorded in `hf18-hodge-regularity.md`
   §1.3 ("nonlinear Hodge system with inhomogeneous curl") and in the Stern
   scope note of `hf18-divergence-speed-link.md` §1.4.
2. **Bounded density.**  \(k^{-1}\le\rho\le k\) excludes
   \(\rho(Q)=Q^{1/2}\), i.e. \(p=3\), which is unbounded above and degenerate
   at \(Q=0\).  Their smoothness theorem (Thm 4.3) therefore does not transfer,
   consistently with the non-claims of HF18-A.

Verdict: **same mechanism, strictly more restrictive hypotheses in both
directions**; the earliest verified source for "unique minimizer over a coset
of exact forms whose nonlinear expression is coclosed".

### 1.2 Nonlinear Hodge theory with \(p\)-growth, closed forms

- **T. Iwaniec, C. Scott, B. Stroffolini, "Nonlinear Hodge theory on manifolds
  with boundary", Ann. Mat. Pura Appl. (4) 177 (1999) 37–115**
  (DOI 10.1007/BF02505905). **[MO]** — abstract/description only: Sobolev
  spaces of differential forms on manifolds with boundary, "Hodge systems"
  (first-order quasilinear elliptic, extensions of Cauchy–Riemann), Dirichlet
  and Neumann problems, \(L^p\) estimates, compactness and removability of
  singularities.
- **C. Scott, "\(L^p\) theory of differential forms on manifolds", Trans. Amer.
  Math. Soc. 347 (1995) 2075–2096.** **[MO]** — cited in the literature for the
  \(L^p\) Hodge decomposition of forms on closed manifolds.
- **M. Stern, "\(L^p\)-cohomology and the geometry of \(p\)-harmonic forms",
  arXiv:2403.19481v2, Lemma 2.2 and Thm 2.9 (Nonlinear Hodge Theorem).**
  **[DI]** — already inspected in `hf18-divergence-speed-link.md` §1.4; the
  \(L^p\)-minimizer in a reduced cohomology class satisfies
  \(d^*(|h|^{p-2}h)=0\), for *closed* \(h\).
- **C. Hamburger, "The heat flow in nonlinear Hodge theory", Adv. Math. 190
  (2005) 360–424.** **[MO]** — publisher page blocked (HTTP 403); from the
  indexed abstract: for \(\rho\)-harmonic forms on a compact oriented
  Riemannian manifold, defined as stationary points on cohomology classes of
  the functional with \(e'(Q)=\rho(Q)/2\), a technical assumption on
  \(2Q\rho'(Q)/\rho(Q)\) gives a unique global solution of the nonlinear heat
  flow which converges to the \(\rho\)-harmonic form in the cohomology class of
  the initial datum.
- **C. Hamburger, "The heat flow in nonlinear Hodge theory under general
  growth", J. Differential Equations 416 (2025) 531–575** (DOI
  10.1016/j.jde.2024.09.043). **[MO]** **Corrected 2026-09-06.** This entry
  previously gave volume 421, pages 264–290 and DOI 10.1016/j.jde.2024.10.024,
  and left the authorship unverified; the HF26 prior-art lane resolved both
  against Crossref (`hf26-prior-art-projection-differentiability.md`). The
  earlier reference was recorded from an index without verification. — indexed abstract:
  a nonlinear Hodge theorem proved by the heat-flow method for densities
  \(\rho\) of *unrestricted polynomial growth*; every cohomology class has a
  unique \(\rho\)-harmonic representative.  Authorship not verified in this
  lane (the 2005 companion is by C. Hamburger).

Comparison.  This line removes the bounded-density restriction of §1.1 and
therefore covers \(p=3\) — but only for **closed** forms in a cohomology class.
It is the closed-form analogue of (Q)–(W), i.e. exactly the case the programme
cannot use, and the programme already records this (Stern scope note).  The
Hamburger papers are the closest published relatives of (H): a heat flow that
decreases a nonlinear Hodge energy and converges to the minimizing
representative.  They are *not* the programme's (H), which is the linear
Euclidean semigroup applied to the datum \(u\), with monotonicity obtained from
\(L^3\) contraction plus invariance \(e^{t\Delta}\mathcal G_3\subset\mathcal G_3\)
and no flow of \(w\) at all.  Same family, different theorem.

### 1.3 Otway — irrotationality weakened, but no variational theorem and no \(p\)-growth

**T. H. Otway, "An elliptic inequality for nonlinear Hodge fields",
arXiv:math-ph/9806007v2.** **[DI]** (HTML read in this lane; the same source
is [DI] via the HF18-A audit).

Studies \(\delta(\rho(Q)\omega)=0\) together with \(d\omega=u\wedge\omega\)
(equation (2)), explicitly replacing \(d\omega=0\); notes that (2) only
guarantees a closed ideal rather than a prescribed cohomology class.
Hypothesis (3): \(K^{-1}(Q+k)^q\le\rho(Q)+2Q\rho'(Q)\le K(Q+k)^q\).
Theorem 1 is an elliptic differential inequality
\(L_\omega(Q)+C(Q+k)^q(|\nabla u|+|u|^2)Q\ge0\), with \(L_\omega\) uniformly
elliptic when \(k>0\).  No existence/uniqueness for a coset minimization is
claimed, and the fetched reading reports the \(p\)-harmonic density
\(\rho=|\omega|^{p-2}\) as not admitted in the stated framework.

Comparison.  This is the only located work that weakens the closedness
condition, which is precisely the programme's difficulty — but the weakening is
multiplicative (\(d\omega=u\wedge\omega\)), not the programme's additive
prescribed curl, the estimate needs \(k>0\) (non-degenerate), and the
conclusion is an inequality for \(Q\), not \(V\in H^1\).  It does not give (R),
and `hf18-divergence-speed-link.md` already lists it correctly as a target for
hypothesis (H1) rather than as a source.

### 1.4 Iwaniec / Iwaniec–Sbordone "nonlinear Hodge decomposition" — a different object

Verified statement, read in **M. Miśkiewicz, B. Petraszczuk, P. Strzelecki,
"Regularity for solutions of H-systems and \(n\)-harmonic maps with \(n/2\)
square integrable derivatives", arXiv:2206.13833, §2.1** **[DI]**:

> Theorem 2.1 (Hodge decomposition and stability estimates).  Let
> \(w:\mathbb R^n\to\mathbb R^m\) be of class \(W^{1,p}\) for some \(p>1\).  Let
> \(\varepsilon\in(-1,p-1)\).  Then \(G:=|\nabla w|^\varepsilon\nabla w\) can be
> written as \(G=\nabla\alpha+\beta\), with
> \(\nabla\alpha,\beta\in L^{p/(1+\varepsilon)}\) and \(\operatorname{div}\beta=0\)
> in the sense of distributions, and
> \(\|\nabla\alpha\|+\|\beta\|\le C(n,m,p)\|\nabla u\|_{L^p}^{1+\varepsilon}\);
> moreover \(\|\beta\|_{L^{p/(1+\varepsilon)}}\le
> C(n,m,p)|\varepsilon|\,\|\nabla w\|_{L^p}^{1+\varepsilon}\).

Attribution in that source: the stability estimate is Iwaniec, and the simpler
general commutator form is Iwaniec–Sbordone (their Theorem 2.2:
\(\|TS_\varepsilon(f)-S_\varepsilon(Tf)\|_{L^{r/(1+\varepsilon)}}\le
C_r|\varepsilon|\|f\|_{L^r}\)).  Reference entries, verbatim from the same
paper's list:

- [9] **T. Iwaniec, "\(p\)-harmonic tensors and quasiregular mappings",
  Ann. of Math. (2) 136 (1992), no. 3, 589–624**, Thm 8.1 (original proof of
  the stability estimate).  **[MO]**
- [10] **T. Iwaniec and C. Sbordone, "Weak minima of variational integrals",
  J. Reine Angew. Math. 454 (1994), 143–161.**  **[MO]** (identity
  independently confirmed on the De Gruyter and EuDML records).

Comparison.  Despite the shared name, this is **not** the programme's object.
Iwaniec–Sbordone split the nonlinear expression \(|\nabla w|^\varepsilon\nabla
w\) of an *arbitrary* \(w\) into a gradient plus a divergence-free field and
estimate the size of the divergence-free part.  The programme instead *chooses*
the representative \(w\) inside a coset so that its nonlinear expression
\(|w|w\) is exactly divergence-free — i.e. the analogue of the "\(\nabla\alpha\)
part" vanishes identically, by construction, not by smallness of a parameter.
Exponents do line up (\(\varepsilon=1\), \(p=3\), \(p/(1+\varepsilon)=3/2\),
matching \(A\in L^{3/2}\)), so the two objects are cousins in the same
technical family; neither implies the other.  **T. Iwaniec, G. Martin**'s
\(L^p\) Hodge decomposition is [MO] and, as `hf18-divergence-speed-link.md`
§1.4 already records, not needed: the linear splitting
\(L^3=\mathbb PL^3\oplus\mathcal G_3\) is available from Riesz transforms.

### 1.5 The linear splitting behind (C)

**D. Fujiwara and H. Morimoto, "An \(L_r\)-theorem of the Helmholtz
decomposition of vector fields", J. Fac. Sci. Univ. Tokyo Sect. IA Math. 24
(1977) 685–700.** **[MO]** (bibliographic identity only).  Standard earliest
citation for the topological direct sum of \(L^r\) vector fields into
solenoidal and gradient parts, \(1<r<\infty\); on \(\mathbb R^n\) it is
Calderón–Zygmund boundedness of the Riesz transforms.

Comparison.  (C) is exactly this splitting plus the admissible competitor
\(q=0\): the quotient norm on \(L^3/\mathcal G_3\) is equivalent to
\(\|\mathbb Pu\|_3\).  Known, classical, and the programme uses it as such.
Dually, \(\mathcal G_3^\perp=\{F\in L^{3/2}:\operatorname{div}F=0\}\), so
\(\mathcal Q(u)=\sup\{\langle u,F\rangle-\tfrac23\|F\|_{3/2}^{3/2}:
\operatorname{div}F=0\}\) is a Fenchel dual pair in the textbook sense
(Ekeland–Temam); the programme's identification of \(j(w)=|w|w\) as the norming
functional of \(\pi u\) is this duality, not a new fact.

### 1.6 Kato 1990 — the critical-smallness Lyapunov property and the \(L^p\) heat generator

**T. Kato, "Liapunov functions and monotonicity in the Navier–Stokes
equation", in: Functional-Analytic Methods for Partial Differential Equations
(Tokyo, 1989), Lecture Notes in Math. 1450, Springer, Berlin, 1990, 53–63.**
**[MO], content verified through a directly inspected citing source.**

The citing source is **U. Manna and S. S. Sritharan, "Lyapunov functionals and
local dissipativity for the vorticity equation in \(L^p\) and Besov spaces",
Differential Integral Equations 20 (2007) 481–498; arXiv:0802.2898**
**[DI]** (pp. 1–3 read).  Quoting it:

> "This idea was generalized by Tosio Kato [13] to prove that for every
> solution of Navier–Stokes equation in \(\mathbb R^m\) (\(m\ge3\)), there exist
> a large number of Lyapunov functions, which decrease monotonically in time if
> the solution have small \(L^m(\mathbb R^m)\)-norm.  More specifically Kato
> proved that the local Lyapunov property in \(L^p\)-norm for \(1<p<\infty\)
> and in \(W^{s,p}\)-norm for \(s>0\), \(2\le p<\infty\). … Moreover Kato also
> proved the local dissipativity of the sum of the linear and nonlinear
> operators of the Navier–Stokes equation in \(L^p\)-norm for \(2\le p<\infty\)."

and, reproduced there as Kato's own lemmas (p. 3):

> Lemma 2.5.  Let \(2\le p<\infty\) and \(\phi\in W^{1,p}\).  Define
> \(Q_p(\phi)=\int_{\nabla\phi\ne0}|\phi|^{p-2}|\nabla\phi|^2dx\ge0\).  Then
> \(CQ_p(\phi)\le-\langle|\phi|^{p-2}\phi,\Delta\phi\rangle<\infty\).
>
> Lemma 2.6.  Let \(2\le p<\infty\) and \(\phi\in W^{1,p}\).  Then
> \(\|\phi\|_{mp/(m-2)}\le CQ_p(\phi)^{1/p}\).

Comparison, and this is the sharpest hit in the note:

- Kato's Lemma 2.5 with \(p=3\) is the *unshifted* form of (E): the \(L^p\)
  heat generator is bounded below by the weighted dissipation
  \(\int|\phi|\,|\nabla\phi|^2\).  The programme's \(D_{\mathcal Q}=D_3(w)\) is
  the same statement with \(u\) tested against the minimizer's nonlinear
  expression \(|w|w\) instead of \(|u|u\) — an *equality* rather than a
  one-sided bound, and for the shifted field.
- Kato's Lemma 2.6 with \(m=3\), \(p=3\) reads \(\|\phi\|_9\le
  CQ_3(\phi)^{1/3}\), i.e. \(Q_3\ge c\|\phi\|_9^3\).  This is exactly the
  coercivity asserted in (E) as \(D_{\mathcal Q}\ge c\|u\|_9^3\), for the
  unshifted field.
- Kato's Lyapunov theorem is exactly (L): \(L^p\) norms of a Navier–Stokes
  solution decrease while the critical \(L^m\) norm is small.  HF18-A's
  Corollary 4 states it recovers Kato's small-\(L^3\) theorem with ESS, which
  is the correct reading; the located earliest source for the *Lyapunov*
  formulation is Kato 1990 rather than Kato, Math. Z. 187 (1984) 471–480
  (global small-\(L^3\) existence), which the repo currently cites [MO].

Corroborating later work in the same line, all **[MO]** with content read only
through Manna–Sritharan §1: **M. Cannone and F. Planchon, "Fonctions de
Lyapunov pour les équations de Navier–Stokes", Séminaire É.D.P. 1999–2000,
Exposé no. XI, 7 pp.** (Numdam `SEDP_1999-2000____A11_0`; bibliographic
identity confirmed [DI] from the Numdam PDF front matter, whose body text is
not extractable from the scan) — Besov Lyapunov functions under small
\(\dot B^{-1,\infty}_\infty\); **P. G. Lemarié-Rieusset**'s extension to
\(\dot B^{s,q}_p\cap BMO^{-1}\) Koch–Tataru solutions; and Manna–Sritharan's
own \(L^p\) and Besov Lyapunov functionals for the vorticity equation under
small \(L^m\) velocity.

Note the duality map used there (Remark 2.2, **[DI]**):
\(G(x)=x|x|^{p-2}/\|x\|_p^{p-2}\).  This is (D) up to normalization; the
Fréchet differentiability of \(\|\cdot\|^p\) on \(L^p\) and on quotients of
uniformly smooth spaces is textbook Banach-space geometry.

### 1.7 Bojarski–Iwaniec, and the \(V=|z|^{(p-2)/2}z\) substitution

**B. Bojarski and T. Iwaniec, "Analytical foundations of the theory of
quasiconformal mappings in \(\mathbb R^n\)", Ann. Acad. Sci. Fenn. Ser. A I
Math. 8 (1983) 257–324.** **[MO]** — the open PDF at
`acadsci.fi/mathematica/Vol08/vol08pp257-324.pdf` is a scan with no text layer,
so no statement was read in this lane.  Content is [DI] in the programme
already through **P. Lindqvist, *Notes on the p-Laplace equation*, Theorem 4.1**
(`hf18-hodge-regularity.md` §7): for \(p\ge2\), \(p\)-harmonic \(u\) satisfies
\(|\nabla u|^{(p-2)/2}\nabla u\in W^{1,2}_{\rm loc}\), by difference quotients.

Comparison.  (R) is this mechanism, but (i) executed against the whole closed
gradient space rather than on a ball with a cutoff, hence global on
\(\mathbb R^3\), and (ii) applied to the *shifted* equation
\(\operatorname{div}\tilde A(u+\nabla\phi)=0\), where the shift enters only
through \(D_hu\).  The substitution \(V=|z|^{(p-2)/2}z\) itself is generic in
both the \(p\)-Laplace literature (Lindqvist §10; Barrett–Liu quasi-norms;
Diening-style shifted \(N\)-functions) and in \(L^p\) Navier–Stokes energy
estimates, where \(|u|^{p/2}\in H^1\) falls out of the \(L^p\) identity — see
Kato's \(Q_p\) above and, in the repo already, **Beirão da Veiga–Yang (2020)
Lemma 6.1** [DI, `hf01-source-table.md`], the \(p=4\) weighted identity
\(\tfrac14\frac{d}{dt}\int|v|^4+\tfrac12\int|\nabla v|^2|v|^2
+\tfrac12\int|\nabla|v|^2|^2\le\int|\pi|^2|v|^2\).

### 1.8 Negative / non-hits worth recording

- **H. Taha and K. Anand, "Variational projection of Navier–Stokes: fluid
  mechanics as a quadratic programming problem", arXiv:2511.03896v1
  (5 Nov 2025).** **[DI]** — the Principle of Minimum Pressure Gradient
  minimizes an \(L^2\) functional of \(u_t\) over solenoidal \(u_t\).  Strictly
  \(L^2\)/Hilbert: no \(L^q\) minimization over gradients and no
  \(\operatorname{div}(|w|^{q-2}w)=0\).  Not prior art for (Q).
- **K. Uhlenbeck, "Regularity for a class of non-linear elliptic systems",
  Acta Math. 138 (1977) 219–240** **[MO]**; \(C^{1,\alpha}\) theory for
  \(p\)-growth systems.  Covers the closed case; the failure of its ellipticity
  hypothesis for the shifted equation is already proved in
  `hf18-hodge-regularity.md` §1.3 and is not disturbed by anything found here.
- **J. Manfredi and A. Weitsman, Comm. PDE 13 (1988) 651–668** **[MO]**
  (\(W^{2,2}_{\rm loc}\) for \(1<p<3+2/(n-2)\)) — unshifted only, as the repo
  already states.
- No source was located that states, for a *non-closed* datum in
  \(\mathbb R^n\), the existence/uniqueness of the \(L^p\)-minimizer over a
  coset of gradients together with regularity of \(|w|^{(p-2)/2}w\); nor any
  use of a gradient-quotient norm as a Navier–Stokes Lyapunov candidate.
  Searched: arXiv full text, Google/Bing web search, Project Euclid, Numdam,
  EuDML, De Gruyter and Springer landing pages, and citing-paper reference
  lists.  MathSciNet and zbMATH full records were not reachable without
  authentication in this lane; ScienceDirect abstracts returned HTTP 403 and
  were read only through search-engine indexing.  This is a bounded search.

## 2. Verdict by component

| Programme object | Status | Earliest verified reference |
|---|---|---|
| (Q)(W) coset minimization, unique minimizer, nonlinear coclosedness | **known mechanism**, under strictly stronger hypotheses (closed datum, bounded density) | Sibner–Sibner, Acta Math. 125 (1970) 57–73, §1.3/§3.2/§4 **[DI]** |
| (Q)(W) with \(p\)-growth, closed forms | **known** | Scott 1995 / Iwaniec–Scott–Stroffolini 1999 **[MO]**; Stern arXiv:2403.19481 Thm 2.9 **[DI]**; Hamburger, JDE 416 (2025) 531–575 for unrestricted polynomial growth **[MO]** |
| (Q)(W) with **prescribed nonzero curl** at \(p=3\) | **unlocated** (not a novelty claim) | — |
| (C) coercivity / quotient norm equivalent to \(\|u\|_3\) | **known** | Fujiwara–Morimoto 1977 **[MO]**; Riesz transforms, classical |
| (S) scaling invariance | **known/routine** | criticality of \(L^3\), Kato 1984 **[MO]** |
| (H) heat monotonicity of the quotient value | **unlocated as stated**; nearest known relatives are the \(L^p\) heat generator sign and nonlinear Hodge heat flows | Kato 1990 Lemma (via Manna–Sritharan **[DI]**); Hamburger, Adv. Math. 190 (2005) 360–424 **[MO]** |
| (D) derivative \(=\int|w|w\cdot h\), gradients annihilated, pressure cancelled | **known mechanism** (duality map of \(L^p\), uniform smoothness, \(\mathcal G_3^\perp\) solenoidal) | Manna–Sritharan Remark 2.2 **[DI]**; textbook Banach-space geometry |
| (E) \(D_{\mathcal Q}\ge c\|\cdot\|_9^3\) | **known for the unshifted field**, \(m=p=3\) special case | Kato 1990 Lemma 2.6 (via Manna–Sritharan **[DI]**) |
| (E) exact identity \(D_{\mathcal Q}(u)=D_3(w)\) for the minimizer | **unlocated** | — |
| (R) \(V=|w|^{1/2}w\in H^1\), \(A\in W^{1,3/2}\), global, shifted | **mechanism known** (difference quotients); shifted + global version **unlocated** | Bojarski–Iwaniec 1983 **[MO]** via Lindqvist Thm 4.1 **[DI]** |
| (L) Lyapunov under critical smallness | **known**, and the programme says so | Kato 1990 **[MO]** via Manna–Sritharan **[DI]**; Cannone–Planchon 1999–2000, Lemarié-Rieusset **[MO]** |
| arbitrary-data absorption (`eq:quotient-gap`, HIGH-STRAIN, HIGH-PRESSURE) | **open**; nothing found | — |

Two corrections to the repo's citation practice follow from this audit, neither
mathematical: the Lyapunov statement recovered by HF18-A Corollary 4 should be
attributed to **Kato 1990** (Liapunov functions), not only to Kato, Math. Z.
187 (1984); and the coercivity \(D_3\gtrsim\|\cdot\|_9^3\) plus the sign of the
\(L^p\) heat generator have a named earliest source (**Kato 1990, Lemmas as
reproduced in Manna–Sritharan 2007**) that the notes currently derive from
scratch without citation.

## 3. Sentence for a truthful related-work paragraph

> The functional used here is the \(p=3\) case, with a prescribed nonzero curl,
> of the variational mechanism of nonlinear Hodge theory: minimizing a convex
> function of the pointwise norm over a coset of exact forms yields a unique
> representative whose nonlinear expression is coclosed, as Sibner and Sibner
> proved for closed data and densities bounded above and below [Sibner–Sibner
> 1970], and as later work extended to \(p\)-growth densities on cohomology
> classes [Scott 1995; Iwaniec–Scott–Stroffolini 1999; Hamburger 2005 and
> its general-growth sequel; Stern 2024]; the coercivity of the quotient norm
> is the classical \(L^r\) Helmholtz decomposition [Fujiwara–Morimoto 1977],
> the weighted cubic dissipation and its \(L^9\) coercivity are the \(m=p=3\)
> case of Kato's \(L^p\) monotonicity lemmas, and the resulting smallness
> criterion reproduces Kato's theorem that \(L^p\) norms of a Navier–Stokes
> solution decrease while its critical \(L^m\) norm is small [Kato 1990]; we
> claim no novelty for any of these, and we located no prior treatment of the
> non-closed \(p=3\) minimizer, of the identity between its heat generator and
> the weighted cubic dissipation, or of any use of a gradient-quotient norm as
> a Navier–Stokes Lyapunov candidate beyond the critical-smallness regime — an
> absence of located prior art, not a claim of priority.

## 4. Frontier record

CLAIM AND SCOPE: bibliographic only.  The programme's objects (Q)–(L) are
compared to located prior art; no mathematical statement is added or removed.

EVIDENCE: Sibner–Sibner 1970 full text [DI]; Otway math-ph/9806007 [DI];
Miśkiewicz–Petraszczuk–Strzelecki arXiv:2206.13833 §2.1 and reference list
[DI]; Manna–Sritharan arXiv:0802.2898 pp. 1–3 [DI]; Taha–Anand
arXiv:2511.03896 [DI]; Numdam front matter for Cannone–Planchon [DI];
remaining entries [MO] as tagged.

FIRST GAP (for this lane): MathSciNet/zbMATH full-record search and the two
ScienceDirect papers (Hamburger 2005; Hamburger, JDE 416 (2025)) were not reachable
without authentication.  Their bodies could confirm or refute whether the
general-growth nonlinear Hodge theorem admits a prescribed-nonzero-\(d\omega\)
version, which is the one bibliographic question that would materially affect
HF18-A §1.3 and the (H1) programme of `hf18-divergence-speed-link.md`.

NON-CLAIMS: no novelty for any programme object; no priority; no assertion that
any unlocated item is new; no mathematical consequence of any cited theorem is
imported into the programme by this note.

NEXT DISTINCT ACTION: obtain the two Hamburger-line papers (institutional
access or interlibrary) and read their growth hypotheses and the closedness
requirement; if a general-growth *inhomogeneous-curl* nonlinear Hodge theorem
exists, cite it in HF18-A §1.3 and retire the corresponding NEXT DISTINCT
ACTION there.
