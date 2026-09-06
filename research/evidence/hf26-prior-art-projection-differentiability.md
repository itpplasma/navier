# HF26: prior art for the weighted linearization of the cubic gradient quotient

Status: bounded prior-art audit, 2026-09-06 (Europe/Vienna).
Scope: Section 3 (`sec:linear`) of
`research/evidence/hf26-temporal-continuation.tex` — Theorem 3.4 (weighted
directional response), Theorem 3.5 (Hadamard derivative of the dual field),
Corollary 3.6 (second variation), Remark 3.7 (non-claims).

MODE: SOURCE AUDIT.  No mathematical claim of the programme is proved,
strengthened or weakened here.  **No novelty is claimed anywhere in this
note.**  An "unlocated" verdict is a statement about the reach of this bounded
search, *not* evidence of priority.  Finding that a statement is standard is a
successful outcome of this lane and is reported plainly.

Tags: **[DI]** = statement read directly in the cited source in this lane
(including through a text-extraction proxy of the primary PDF, said explicitly);
**[AB]** = official abstract or indexed abstract read, body not read;
**[MO]** = bibliographic identity only, content not read.

Companion notes, not repeated here: `cp01-prior-art-quotient.md` (the
functional, the nonlinear Hodge mechanism, Kato, Bojarski–Iwaniec),
`cp02-prior-art-related-work.md` (pressure route).  This note is confined to
*differentiability of the projection* and to *linearization in a degenerate
weighted space*.

Local-first check: `~/Zotero/zotero.sqlite` was queried read-only (8884 items,
8084 with field data) for `metric projection`, `directional differentiab*`,
`Hadamard`, `Gateaux`, `Fréchet`, `sensitivity analysis`, `nonlinear Hodge`,
`p-harmonic`, `p-Laplac*`, `quasiregular`, `Muckenhoupt`, `weighted Sobolev`,
`best approximation`, `duality map`, `Bochner space`, `Chebyshev set`, and the
author names below.  **No relevant item exists in the library**; every hit was
plasma physics or surrogate-model uncertainty quantification.  The library is
not a source for this topic and all references below are web-located.

---

## 0. The exact statement being compared

Fix the objects of `sec:foundations`:
\(\mathcal G_3=\overline{\{\nabla\phi:\phi\in C_c^\infty\}}^{L^3}\subset
L^3(\mathbb R^3;\mathbb R^3)\) is a **closed linear subspace**;
\(F(v)=\tfrac13\|v\|_3^3\); \(j(z)=|z|z\); \(w(v)\) minimizes \(F\) on the
coset \(v+\mathcal G_3\); \(q=w-v\); \(A=j(w)\);
\(\mathcal Q(v)=F(w(v))\).

Two reformulations that fix which literature is relevant, and that the
candidate document does not make explicit:

- **(P1)** \(w(v)=v-P_{\mathcal G_3}(v)\) where \(P_{\mathcal G_3}\) is the
  **metric projection** (nearest-point map) of \(L^3\) onto the closed subspace
  \(\mathcal G_3\), and \(-q=P_{\mathcal G_3}(v)\).  Hence
  \(\mathcal Q(v)=\tfrac13\operatorname{dist}_{L^3}(v,\mathcal G_3)^3
  =\tfrac13\|v+\mathcal G_3\|^3_{L^3/\mathcal G_3}\).
  Theorem 3.4 is therefore a statement about the **directional
  differentiability of the metric projection of \(L^3\) onto a closed
  subspace**, and Corollary 3.6 is the second-order expansion of the cube of a
  distance function to a closed subspace.
- **(P2)** The stationarity condition \eqref{eq:stationarity},
  \(\langle j(w),g\rangle=0\;\forall g\in\mathcal G_3\), is the classical
  characterization of best \(L^p\) approximation from a subspace: the duality
  map of the residual annihilates the subspace.  \(\operatorname{div}(|w|w)=0\)
  is that condition written as a PDE.

The statements audited:

- **T3.4 (weighted directional response).**  For every \(v,h\in L^3\), with
  \(U=w(v)\), \(\rho=|U|\), \(M_U=\mathrm Dj(U)=\rho I+U\otimes U/\rho\) (and
  \(0\) on \(\{U=0\}\)), \(\mathcal H_U\) the Hilbert space with
  \(\langle a,b\rangle_U=\int a\cdot M_Ub\) (equivalent to \(L^2(\rho\,dx)\),
  values on \(\{U=0\}\) discarded), \(\mathcal E_U\) the \(\mathcal
  H_U\)-closure of the image of \(\mathcal G_3\), and \(\mathsf L_U=I-\mathsf
  P_{\mathcal E_U}\):
  \[
   \varepsilon^{-1}\bigl(w(v+\varepsilon h)-w(v)\bigr)\to\mathsf L_Uh
   \quad\text{strongly in }\mathcal H_U,\qquad \varepsilon\to0,\ \varepsilon\ne0 .
  \]
  Explicitly **not** claimed: convergence in \(L^3\); \(\mathsf L_Uh\in L^3\);
  that elements of \(\mathcal E_U\) are unweighted gradients.
- **T3.5 (Hadamard derivative of the dual field).**  \(A:L^3\to L^{3/2}\) is
  Hadamard differentiable at every \(v\), with
  \(\mathcal B_vh=M_U\mathsf L_Uh\), \(\|\mathcal B_vh\|_{3/2}\le
  2\|U\|_3\|h\|_3\), and \(\langle\mathcal B_vh,k\rangle=\langle\mathsf
  L_Uh,\mathsf L_Uk\rangle_U\).
- **C3.6.** \(\mathcal Q(v+\varepsilon h)=\mathcal Q(v)+\varepsilon\langle
  A(v),h\rangle+\tfrac12\varepsilon^2\|\mathsf L_Uh\|_U^2+o(\varepsilon^2)\),
  plus the time-derivative corollaries.
- **R3.7 (non-claims).**  No \(L^3\) derivative of \(w\); no two-point \(L^3\)
  Lipschitz estimate for \(q\); no operator-norm continuity of \(v\mapsto
  \mathcal B_v\); hence no \(C^2\) Fréchet claim.

Supporting inequalities used, both **already standard** (see §3.1):
\((j(a)-j(b))\cdot(a-b)=\tfrac{|a|+|b|}2(|a-b|^2+(|a|-|b|)^2)\)
(`eq:mono`), and \(\|\mathrm Dj(a)-\mathrm Dj(b)\|_{\rm op}\le4|a-b|\)
(Lemma 3.2).

---

## 1. Area 1 — differentiability of metric projections in \(L^p\), \(p\ne2\)

### 1.1 The classical Hilbert-space theory (the frame everything else is stated against)

- **S. Fitzpatrick and R. R. Phelps, "Differentiability of the metric
  projection in Hilbert space", Trans. Amer. Math. Soc. 270 (1982) 483–501**,
  DOI 10.1090/S0002-9947-1982-0645326-5.  **[DI]** (open AMS PDF read through a
  text proxy).  Gâteaux/Fréchet differentiability of \(P_K\) onto a closed
  convex \(K\subset H\) is tied to the smoothness of \(\partial K\): if
  \(\partial K\) is \(C^k\), \(k\ge2\), then \(P\) is \(C^{k-1}\) on
  \(H\setminus K\) with \(P'(x)\) invertible on the relevant hyperplane
  (attributed there to Holmes), and conversely.  \(dP(x)\) and \(P'(x)\) are
  symmetric, positive, norm \(\le1\).  **Hilbert spaces only**; the only
  function-space example is \(L^2[0,1]\).  No \(L^p\), \(p\ne2\); no weighted
  space.
- **D. Noll, "Directional differentiability of the metric projection in Hilbert
  space", Pacific J. Math. 170 (1995) 567–592**, DOI 10.2140/pjm.1995.170.567.
  **[DI]** (MSP open PDF read
  through a text proxy).  *This is the closest methodological ancestor of the
  candidate's proof.*  Thm 3.3: \(P_C\) is directionally Gâteaux differentiable
  at \(x\notin C\) **iff** the support function \(\sigma_C\) is **twice Mosco
  differentiable** at \(x\) with respect to \(y\in\partial\sigma_C(x)\);
  Thm 5.1: directional Fréchet differentiability corresponds to second-order
  Attouch–Wets differentiability.  Hilbert only.
- **A. Shapiro, "Existence and differentiability of metric projections in
  Hilbert spaces", SIAM J. Optim. 4 (1994) 130–141**, DOI 10.1137/0804006.
  **[MO]**.
- **A. Shapiro, "Directionally nondifferentiable metric projection", J. Optim.
  Theory Appl. 81 (1994) 203–204**, DOI 10.1007/BF02190320.  **[MO]** — the
  standard counterexample: a nonempty closed convex set in the Euclidean plane
  whose metric projection has no directional derivative.  Sharpened to a set
  with \(C^{1,1}\) boundary by **S. S. Akmal, N. M. Nam and J. J. P. Veerman,
  "On a convex set with nondifferentiable metric projection", Optim. Lett. 9
  (2015) 1039–1052**, DOI 10.1007/s11590-015-0847-x, arXiv:1412.0058 **[AB]**.
  Consequence for this audit: **no theorem can assert directional
  differentiability of the metric projection onto an arbitrary closed convex set
  in a Hilbert (hence in a general \(L^p\)) space.**  Positive results need
  structure — and a *subspace* is exactly such structure.
- **A. Shapiro, "Differentiability properties of metric projections onto convex
  sets", J. Optim. Theory Appl. 169 (2016) 953–964**, DOI
  10.1007/s10957-016-0871-8; preprint at optimization-online 4119 (2014).
  **[DI]** (preprint read through a text proxy).  Thm 3.1: if \(S\) is
  **second-order regular** at \(P_S(\bar x)\) then \(P_S\) is directionally
  differentiable at \(\bar x\).  Finite-dimensional Euclidean spaces only; no
  \(L^p\), \(p\ne2\), no weighted space.  Earlier: **A. Shapiro, "Sensitivity
  analysis of nonlinear programs and differentiability properties of metric
  projections", SIAM J. Control Optim. 26 (1988) 628–645**, DOI
  10.1137/0326037 **[MO]**; **"On differentiability of metric projections in
  \(\mathbb R^n\). I. Boundary case", Proc. Amer. Math. Soc. 99 (1987)
  123–128**, DOI 10.1090/S0002-9939-1987-0866441-7 **[MO]**; **"Directional
  differentiability of metric projections onto moving sets at boundary points",
  J. Math. Anal. Appl. 131 (1988) 392–403**, DOI 10.1016/0022-247X(88)90213-2
  **[MO]**.
- **F. Mignot, "Contrôle dans les inéquations variationelles elliptiques",
  J. Funct. Anal. 22 (1976) 130–185**, DOI 10.1016/0022-1236(76)90017-3
  **[MO]**, and **A. Haraux, "How to differentiate the projection on a convex
  set in Hilbert space. Some applications to variational inequalities",
  J. Math. Soc. Japan 29 (1977) 615–631**, DOI 10.2969/jmsj/02940615 **[MO]**:
  conical differentiability of \(P_K\) for **polyhedric** closed convex sets in
  Hilbert space.  This is the origin of the whole "directional derivative of a
  projection = projection onto a critical cone" template.

### 1.2 Convex sensitivity theory: the general machinery the proof instantiates

- **J. F. Bonnans and A. Shapiro, *Perturbation Analysis of Optimization
  Problems*, Springer Series in Operations Research, Springer, New York, 2000.**
  **[MO]** (contents and topic list verified: Legendre forms, second-order
  conditions, directional regularity, differentiability of the optimal value
  \(v(u)\) and of the solution set \(S(u)\)).  This is the standard reference
  for "difference quotients of minimizers of a parametrized convex problem
  converge to the solution of the linearized problem".
- **J. F. Bonnans, R. Cominetti and A. Shapiro, "Sensitivity analysis of
  optimization problems under second order regular constraints", Math. Oper.
  Res. 23 (1998) 806–831**, DOI 10.1287/moor.23.4.806 **[MO]**.
- **R. T. Rockafellar**, the epi-derivative programme: "First- and second-order
  epi-differentiability in nonlinear programming", Trans. Amer. Math. Soc. 307
  (1988) 75–108, DOI 10.1090/S0002-9947-1988-0936806-9; "Proto-differentiability
  of set-valued mappings and its applications in optimization", Ann. Inst.
  H. Poincaré Anal. Non Linéaire 6 (1989) 449–482, DOI
  10.1016/S0294-1449(17)30034-3; "Second-order optimality conditions in
  nonlinear programming obtained by way of epi-derivatives", Math. Oper. Res. 14
  (1989) 462–484, DOI 10.1287/moor.14.3.462.  All **[MO]**.  The controlling general fact, confirmed in several
  secondary sources **[AB]**: a convex function is **twice epi-differentiable in
  the Mosco sense iff its subdifferential is proto-differentiable**, the proof
  going through **Attouch's theorem** (Mosco epi-convergence of convex functions
  \(\Leftrightarrow\) graph convergence of subgradients, on a reflexive Banach
  space).  Extended to reflexive Banach spaces by **C. N. Do, "Generalized
  second-order derivatives of convex functions in reflexive Banach spaces",
  Trans. Amer. Math. Soc. 334 (1992) 281–301** **[MO]**.
- **Integral functionals specifically:** **A. B. Levy, "Second-order
  epi-derivatives of integral functionals", Set-Valued Anal. 1 (1993)
  379–392**, DOI 10.1007/BF01027827 **[MO]**; **P. D. Loewen and H. Zheng,
  "Epi-derivatives of integral functionals with applications", Trans. Amer.
  Math. Soc. 347 (1995) 443–459**, DOI 10.2307/2154896 **[MO]**.  \(F(v)=\int
  f(v)\), \(f(z)=\tfrac13|z|^3\), is exactly an integral functional of this
  type.

Comparison: the *shape* of the candidate's proof — bound the difference
quotients in a space adapted to the base point, extract a weak limit, identify
it by passing the (linearized) stationarity condition to the limit, then upgrade
to strong convergence by a monotonicity/coercivity argument — is the standard
proof template of convex sensitivity analysis and of second-order
epi-differentiability.  Nothing in that template is new, and Noll's Hilbert
theorem is the same statement in the Hilbert case.

### 1.3 The on-topic recent line: metric projections in uniformly convex, uniformly smooth Banach spaces

- **Jinlu Li, "Directional differentiability of the metric projection operator
  in uniformly convex and uniformly smooth Banach spaces", J. Optim. Theory
  Appl. 200 (2024), no. 3, 923–950**, DOI 10.1007/s10957-023-02329-7;
  preprint arXiv:2303.16265.  **[DI]** for the arXiv text (read through a text
  proxy), **[AB]** for the published abstract.  Published abstract, verbatim:
  > "Let X be a real uniformly convex and uniformly smooth Banach space and C a
  > nonempty closed and convex subset of X.  Let \(P_C: X\to C\) denote the
  > (standard) metric projection operator.  In this paper, we define the Gâteaux
  > directional differentiability of \(P_C\).  We investigate some properties of
  > the Gâteaux directional differentiability of \(P_C\).  In particular, if C
  > is a closed ball or a closed and convex cone (including proper closed
  > subspaces), then, we give the exact representations of the directional
  > derivatives of \(P_C\)."

  From the arXiv text: Definition 4.1 defines directional differentiability as
  the existence of \(\lim_{t\downarrow0}[P_C(x+tv)-P_C(x)]/t\) **as a point of
  \(X\)**, i.e. a **norm** limit, one-sided (\(t\downarrow0\)); Lemma 4.6 gives
  only positive homogeneity, so the derivative is not asserted linear.
  §5 treats closed balls, §6 "subspaces and cones", §7 introduces "\(p\)-\(q\)
  uniformly convex and uniformly smooth" spaces, §8 applies to Hilbert spaces.
  The §6 subspace statement extracted (Theorem 6.1) is confined to base points
  **inside** the subspace: for \(C\) a proper closed subspace, \(P_C\) is
  directionally differentiable at every \(y\in C\) along \(v\in
  C^{\perp}\setminus\{\theta\}\), with derivative \(\theta\).  Proposition 6.4
  computes the derivative for the **positive cone in \((\mathbb R^3,\|\cdot\|_3)\)**.
  Theorem 7.2 is the general claim: "Let X be a \(p\)-\(q\) uniformly convex and
  uniformly smooth Banach space and C a nonempty closed and convex subset of X.
  Then \(P_C\) is directionally differentiable on X."
- **Jinlu Li, "Directional differentiability of the metric projection in Bochner
  spaces", Applicable Nonlinear Analysis 1 (2024) 79–109**, DOI
  10.69829/apna-024-0101-ta05; preprint arXiv:2311.00942 (2 Nov 2023).
  **[AB]** — the reference already carried by the candidate as `\cite{Li}`,
  which cites it **as an unpublished 2023 preprint**; it is in fact published
  and must be cited as such.  \(L^p(S;X)\) with \(X\) uniformly
  convex and uniformly smooth; the three projections treated are onto the
  **support subspace** \(L^p(A;X)\), the ball \(B_A(c;r)\) and the cylinder
  \(C_A(c;r)\).  The candidate's characterization of this as not directly
  applicable is **correct and should be kept**: \(L^p(A;X)\) is a
  restriction-type subspace on which the metric projection is the *linear* map
  \(f\mapsto f\mathbf 1_A\); \(\mathcal G_3\) is nothing like it.
- Same author, adjacent: **"Mordukhovich derivatives of the metric projection
  operator in uniformly convex and uniformly smooth Banach spaces", Set-Valued
  Var. Anal. 32 (2024)**, DOI 10.1007/s11228-024-00734-2, arXiv:2401.11321
  **[AB]** (balls, cylinders, positive cones); **"Fréchet differentiability of
  the metric projection operator in Banach spaces", arXiv:2401.01480** **[AB]**
  (balls, cylinders, positive cones); **"Gâteaux directional differentiability
  of the generalized metric projection in Banach spaces", Acta Math. Sci. (2025)**,
  DOI 10.1007/s10473-025-0419-9 **[MO]**; **arXiv:2310.16254**, **arXiv:2311.01561**
  **[MO]**.  All concern balls, cylinders, cones, or support subspaces — none
  concerns a subspace like \(\mathcal G_3\), and none introduces a weighted
  space.

**A consistency caveat that this lane could not resolve.**  As extracted,
Li's Definition 7.1 requires exponents with \(1<p<q\) satisfying
\(\delta(\varepsilon)\ge a\varepsilon^p\) on \((0,2]\) and \(\rho(t)\le bt^q\)
for \(t>0\).  For every Banach space one has \(\delta\le\delta_{\rm Hilbert}
\sim\varepsilon^2/8\) and \(\rho\ge\rho_{\rm Hilbert}\sim t^2/2\), which forces
\(p\ge2\ge q\); with the extracted ordering \(p<q\) the class would be empty and
Theorem 7.2 vacuous.  With the ordering \(1<q\le2\le p\) — the usual
"\(p\)-uniformly convex and \(q\)-uniformly smooth" convention, under which
\(L^3\) is \(3\)-uniformly convex and \(2\)-uniformly smooth — the class
contains \(L^3(\mathbb R^3;\mathbb R^3)\), Theorem 7.2 would apply to
\(C=\mathcal G_3\), and it would give **norm** convergence of the difference
quotients in \(L^3\), i.e. strictly more than T3.4 asserts.  It would then also
apply to Hilbert space if \(p=q=2\) were admitted, which Shapiro's 1994
counterexample forbids.  **Which reading is correct was not determined**: the
published JOTA version was paywalled, the arXiv PDF is only readable here
through a text-extraction proxy, and no review (MathSciNet/zbMATH) was
reachable.  This is recorded as an open item, not as a defect finding, and not
as licence to ignore the paper.

### 1.4 The older \(L^p\)/\(\ell^p\) best-approximation literature

- **R. B. Holmes and B. R. Kripke, "Smoothness of approximation", Michigan
  Math. J. 15 (1968) 225–248**, DOI 10.1307/mmj/1028999976.  **[AB]** (content
  via secondary sources): on \(\mathbb R^n\) with the \(\ell_p\) norm,
  \(1<p<\infty\), the metric projection onto a linear subspace is **Lipschitz
  continuous**, with a \(p\)-dependent constant.  This is the earliest located
  reference for regularity of the \(L^p\) subspace projection.
- **B. Björnestål, "Local Lipschitz continuity of the metric projection
  operator", Banach Center Publ. 4 (1979), no. 1, 43–53**, ISSN 0137-6934
  (identity verified on the EuDML record, `eudml.org/doc/208992`; MSC 46B20,
  41A50, 41A65) **[MO]**; generalized and
  improved in **"Continuity of metric projections in uniformly convex and
  uniformly smooth Banach spaces", J. Approx. Theory 39 (1983)** (ScienceDirect
  pii 0021904583900746; the record returned HTTP 403 and pages/authors were not
  verified) **[MO]**.  The general modulus in \(L^p\), \(2\le p<\infty\)
  (\(2\)-uniformly smooth, \(p\)-uniformly convex), is Hölder, not Lipschitz,
  and Hölder is stated in the secondary literature as **optimal up to
  constants** for \(L^p\) **[AB]**.
- **M. Finzel and W. Li, "Hoffman's error bounds and uniform Lipschitz
  continuity of best \(\ell_p\)-approximations", J. Math. Anal. Appl. 220
  (1998)** (ScienceDirect pii S0022247X97955219) **[AB]**: uniform-in-\(p\)
  Lipschitz continuity of best \(\ell_p\)-approximation from **polyhedral** sets
  in \(\mathbb R^n\).
- The linearization weight itself is folklore in numerical approximation:
  the Gauss–Newton/IRLS linearization of \(\min\|r(x)\|_p^p\) is the weighted
  least-squares problem with diagonal weight \(|r|^{p-2}\)
  (Lawson 1961; **J. R. Rice and K. H. Usow, "The Lawson algorithm and
  extensions", Math. Comp. 22 (1968) 118–127**; **M. R. Osborne, *Finite
  Algorithms in Optimization and Data Analysis*, Wiley, 1985**, whose
  convergence proof for IRLS covers \(1<p<3\)) **[AB]**.  This is an
  algorithmic, not a differentiability, statement, but it means the *shape* of
  \(M_U\) as "the linearization weight of an \(L^p\) best-approximation problem"
  is entirely standard and cannot be presented as a discovery.
- Smoothness of the ambient functional is classical: the best order of
  differentiability of the \(L^p\) norm (and of \(\|\cdot\|_p^p\)) is
  \(\lceil\cdot\rceil\)-sharp — **R. Bonic and J. Frampton, "Differentiable
  functions on certain Banach spaces" / "Smooth functions on Banach manifolds",
  1965/1966** **[MO]**; **I. E. Leonard and K. Sundaresan, "Geometry of
  Lebesgue–Bochner function spaces — smoothness", Trans. Amer. Math. Soc. 198
  (1974) 229–251**, DOI 10.1090/S0002-9947-1974-0367652-5 **[AB]**.  For \(p=3\) this gives exactly: \(\|\cdot\|_3^3\)
  is twice continuously differentiable on \(L^3\), with Lipschitz second
  derivative — which is Lemma 3.2 and equation (2.19) `eq:Qprime` of the
  candidate.

---

## 2. Area 2 — nonlinear Hodge and \(p\)-Laplacian perturbation theory

### 2.1 Nonlinear Hodge theory: no located linearization in the datum

The existence/uniqueness/regularity side is already audited in
`cp01-prior-art-quotient.md` §1 and is not repeated.  What is new here is the
*perturbation* question, and the answer located is thin:

- **L. M. Sibner and R. J. Sibner, "A non-linear Hodge–de Rham theorem", Acta
  Math. 125 (1970) 57–73** **[DI in cp01]**, and **"Nonlinear Hodge theory:
  Applications", Adv. Math. 31 (1979) 1–15**, DOI 10.1016/0001-8708(79)90016-1
  **[MO]** (bibliographic identity verified; indexed content: subsonic
  irrotational flow on Riemannian manifolds, maximum of the speed).  Also
  **"Transonic flow on an axially symmetric torus", J. Math. Anal. Appl. 72
  (1979) 362–382**, DOI 10.1016/0022-247X(79)90295-6 **[MO]**.  The classical
  *degeneracy* studied in this line is the **sonic** degeneracy of
  \(\rho+2Q\rho'(Q)\) at the sonic speed, not the \(p\)-Laplacian degeneracy at
  \(\{\omega=0\}\); the programme's \(M_U\) degenerates at the *zero* of the
  field, which the bounded-density admissibility hypothesis \(k^{-1}\le\rho\le k\)
  of Sibner–Sibner excludes outright.  **No linearization-in-the-datum theorem
  was located in this line.**
- **A. Marini and T. H. Otway, "Duality methods for a class of quasilinear
  systems", Ann. Inst. H. Poincaré Anal. Non Linéaire 31 (2014) 339–…;
  arXiv:1206.0189** **[DI]** (arXiv HTML read).  Treats
  \(\delta(\rho(Q)\omega)=0\), \(d\omega=\Gamma\wedge\omega\) by
  Hodge–Bäcklund duality.  Read directly: the paper **does not linearize**, and
  **does not discuss differentiability of the solution with respect to data**;
  its "weighted" structures are amplitude constraints \(t_1\le|\omega|^2\le t_2\),
  not a degenerate energy space.  Same for **A. Marini and T. H. Otway,
  "Hodge–Frobenius equations and the Hodge–Bäcklund transformation",
  arXiv:0907.2685** **[AB]**.
- **T. H. Otway, "An elliptic inequality for nonlinear Hodge fields",
  arXiv:math-ph/9806007** **[DI in cp01]** — an elliptic differential
  inequality for \(Q\), requiring \(k>0\) (non-degenerate); not a sensitivity
  statement.
- **Negative index evidence.**  An arXiv abstract search for
  `abs:"nonlinear Hodge" AND abs:"linearized"` returns exactly **one** record
  (the Marini–Otway Bäcklund paper above); `abs:"p-Laplacian" AND
  abs:"directional differentiability"` returns **zero**.  This is a bounded
  index search, not proof of absence.

### 2.2 The linearized \(p\)-Laplacian: its degenerate weighted quadratic form is a routine construction

The construction "linearize the \(p\)-Laplacian-type operator at a fixed
solution and read the linearization as a **closed quadratic form on a weighted
\(L^2\) determined by the base solution**" is used in the literature without
comment, i.e. as standard practice.  A clean recent instance read in this lane:

- **Yitian Zhang, "The complete spectrum of the linearized \(p\)-Laplacian at a
  Sobolev extremal", arXiv:2608.27276 (27 Aug 2026)** **[AB]** (official
  abstract read).  Verbatim: "…the linearized \(p\)-Laplacian at \(v\),
  **defined by its closed quadratic form in \(L^2(\mathbb R^n,v^{p^*-2}\,dx)\)**".
  The weighted-\(L^2\) realization of the linearization is introduced as the
  natural formulation of the problem, with no claim of novelty attached to the
  space itself.

Together with §3 below this settles the status of the *construction* \(\mathcal
H_U\): it is the routine energy space of a linearized degenerate elliptic
operator, not a new object.

### 2.3 Control-to-state differentiability for quasilinear/degenerate equations

- **E. Casas and L. A. Fernández, "Distributed control of systems governed by a
  general class of quasilinear elliptic equations", J. Differential Equations
  104 (1993)** and **"Optimal control of quasilinear elliptic equations with non
  differentiable coefficients at the origin" (1991)** **[MO]** (identities from
  secondary sources only; bodies not read).  Indexed secondary statements
  **[AB]**: for \(p\)-Laplacian-type control problems the control-to-state map
  is studied for Gâteaux differentiability, and in degenerate cases it **may
  fail to be directionally differentiable**, forcing weaker notions
  (finite-dimensional directional differentiability).  This is the closest
  located analogue of the candidate's situation — a solution map for a
  \(p\)-Laplacian-type problem whose differentiability is delicate exactly
  because of degeneracy — but no located statement is about a *gradient-coset
  minimization in \(L^p(\mathbb R^n)\)*.

**Verdict for Area 2.**  The *mechanism* (linearize the nonlinear Hodge /
\(p\)-Laplacian equation, land in a degenerate weighted energy space) is
standard; a *theorem* that the nonlinear Hodge projection is differentiable in
the datum was **not located** in the nonlinear Hodge literature at all.  That
absence is a statement about this search.  Nothing found contradicts the
candidate.

---

## 3. Area 3 — the degenerate weighted space: is the phenomenon named?

### 3.1 The weighted quantity itself is standard and named

The candidate's `eq:mono`,
\((j(a)-j(b))\cdot(a-b)=\tfrac{|a|+|b|}2(|a-b|^2+(|a|-|b|)^2)\), is the \(p=3\)
case of the classical monotonicity equivalence
\[
 (|a|^{p-2}a-|b|^{p-2}b)\cdot(a-b)\ \simeq\ (|a|+|b|)^{p-2}|a-b|^2
 \ \simeq\ \bigl|V(a)-V(b)\bigr|^2,\qquad V(z)=|z|^{(p-2)/2}z,
\]
and the middle quantity is a **named object** with at least three established
names:

- **"quasi-norm"** — **J. W. Barrett and W. B. Liu, "Finite element
  approximation of the \(p\)-Laplacian", Math. Comp. 61 (1993) 523–537**,
  DOI 10.1090/S0025-5718-1993-1192966-4 **[MO]**, together with **W. B. Liu and
  J. W. Barrett, "A remark on the regularity of the solutions of the
  \(p\)-Laplacian and its application to their finite element approximation",
  J. Math. Anal. Appl. 178 (1993) 470–487**, DOI 10.1006/jmaa.1993.1319
  **[MO]**.  The term is in routine use in the numerical \(p\)-Laplacian
  literature (verified by arXiv abstract sampling **[AB]**: Lee–Park
  arXiv:2210.09183; Ignat–Zuazua arXiv:2504.09637; Georgoulis–Paraschis
  arXiv:2604.15879).
- **"shifted \(N\)-function"** \(\varphi_a(t)\) — **L. Diening and F. Ettwein,
  "Fractional estimates for non-differentiable elliptic systems with general
  growth", Forum Math. 20 (2008) 523–556**, DOI 10.1515/forum.2008.027
  **[MO]**.
- **the \(V\)-function / \(F\)-function substitution** \(V=|z|^{(p-2)/2}z\) —
  already recorded in `cp01-prior-art-quotient.md` §1.7 (Bojarski–Iwaniec 1983
  via Lindqvist Thm 4.1 **[DI]**; Uhlenbeck 1977).  The programme uses exactly
  this substitution as \(V=|w|^{1/2}w\).

So: the *weight*, the *quadratic form*, and the *change of variable* in the
candidate's \(\mathcal H_U\) are all standard \(p\)-Laplacian machinery.

### 3.2 Shifted weight versus frozen weight: the point on which the candidate is careful, and which is elementary

For \(p\ge2\) the **shifted** quantity does control the ambient norm, pointwise:
\(|a|+|b|\ge|a-b|\) gives \((|a|+|b|)^{p-2}|a-b|^2\ge|a-b|^p\).  The candidate's
\(\mathcal H_U\) uses instead the **frozen** weight \(\rho=|U|\) at the base
point, and then no such inequality is available: \(|U|\) does not dominate
\(|z_\varepsilon-z_m|\), and the form vanishes identically on \(\{U=0\}\).  The
only available comparison runs the other way, by Hölder:
\(\int\rho|a|^2\le\|\rho\|_3\|a\|_3^2\), which is the candidate's
\eqref{eq:L3embed}.  This is elementary and consistent with the candidate's
non-claims; **no source is needed and none was located that presents this
one-sided comparison as a result.**  It is also already recorded internally in
`hf22-projection-regularity.md` (the weighted-to-unweighted conversion failure
and the exponent \(1/2\)).

### 3.3 The named phenomenon: "two-norm discrepancy"

The structural situation — *the functional is twice differentiable in one norm,
but the second-order/coercivity information lives in a strictly weaker norm in
which it is not twice differentiable* — is a **named, classical phenomenon**:

- **E. Casas and F. Tröltzsch, "Second order optimality conditions and their
  role in PDE control", Jahresber. Dtsch. Math.-Ver. 117 (2014/2015) 3–44**,
  DOI 10.1365/s13291-014-0109-3.  **[DI]** (author PDF read through a text
  proxy).  Verbatim: *"This phenomenon is called the **two-norm discrepancy**:
  the functional \(J\) is twice differentiable with respect to one norm, but the
  inequality \(J''(\bar u)v^2\ge\delta\|v\|^2\) holds in a weaker norm in which
  \(J\) is not twice differentiable."*  And: *"the difficulty that the
  coercivity condition … is not true in the spaces where the functional \(J\) is
  twice differentiable."*  Attribution given there: *"To our knowledge, Ioffe
  was the first who proved a result of this type by using two norms in the
  context of optimal control"*, citing **A. D. Ioffe, "Necessary and sufficient
  conditions for a local minimum. 3: Second order conditions and augmented
  duality", SIAM J. Control Optim. 17 (1979) 266–288**, DOI 10.1137/0317021
  **[MO, identity verified]**; further **H. Maurer**, **W. Alt and K. Malanowski
  (1993)**, **J. C. Dunn (1998)** **[MO]**.
- The abstract counterpart is the failure of the **Legendre form** condition of
  Bonnans–Shapiro: their sensitivity theorems require the second-order term to
  be a Legendre form on the ambient space (weak lower semicontinuity plus
  "weak convergence with convergence of the form implies strong convergence").
  \(\|\cdot\|_U^2\) *is* a Legendre form on \(\mathcal H_U\) — it is the square
  of that Hilbert norm — but not on \(L^3\).  **[AB]** for the definition, as
  quoted in several primary sources located.
- The degenerate weighted \(L^2\) space itself sits in the classical
  Muckenhoupt/degenerate-elliptic framework: **E. B. Fabes, C. E. Kenig and
  R. P. Serapioni, "The local regularity of solutions of degenerate elliptic
  equations", Comm. Partial Differential Equations 7 (1982) 77–116**,
  DOI 10.1080/03605308208820218 **[MO]**.  Note that the candidate deliberately
  assumes **no** weighted Calderón–Zygmund or \(A_2\) property (`sec:foundations`
  says so explicitly), so this framework is context, not an import — and whether
  \(|w|\) is an \(A_2\) weight is not asserted anywhere and was not determined
  here.

**Verdict for Area 3.**  Yes — the phenomenon has an established name and an
established literature.  The name is **two-norm discrepancy** (Ioffe 1979;
Casas–Tröltzsch's survey is the standard modern statement), the weighted
quantity is the **quasi-norm / natural distance / shifted \(N\)-function**, and
the degenerate weighted \(L^2\) realization of a linearized \(p\)-Laplacian is
routine.  The programme must not describe any of this as unnamed, unnoticed or
new.

---

## 4. Area 4 — the cubic case \(p=3\) in three dimensions

- No source was located that treats \(p=3\) in \(\mathbb R^3\) as a
  distinguished case of the *projection-differentiability* question.
- The nearest literal appearance of the cubic norm in dimension three in the
  projection literature is **Li, arXiv:2303.16265, Example 6.2 and
  Proposition 6.4**, which compute the metric projection and its directional
  derivative for the **positive cone in \((\mathbb R^3,\|\cdot\|_3)\)** **[DI]** —
  finite-dimensional, and a cone rather than the gradient subspace.  It is
  \(p=3\), \(n=3\), and it is *not* the programme's object.
- In the PDE literature \(p=3\) is unremarkable: it lies inside the
  Manfredi–Weitsman \(W^{2,2}_{\rm loc}\) range \(1<p<3+2/(n-2)\) (already
  recorded in `cp01`), and appears in \(p\)-harmonic regularity papers only as a
  range endpoint (arXiv abstract sampling **[AB]**: Haarala–Sarsa
  arXiv:2204.13550; Miśkiewicz arXiv:1708.00900).
- The genuinely \(p=3\)-specific facts already located by earlier lanes are
  Kato's \(m=p=3\) Lyapunov lemmas (`cp01` §1.6) and the \(q=3\) case of the
  Tran–Yu–Dritschel identity (`cp02` §1.4).  Neither concerns the projection or
  its derivative.

**Verdict for Area 4.**  The cubic case carries no special standing in this
literature; \(p=3\) is convenient (it makes \(f(z)=\tfrac13|z|^3\) exactly
\(C^2\) with Lipschitz second derivative, by the classical smoothness
classification of \(L^p\) norms — Bonic–Frampton; Leonard–Sundaresan) but is not
a distinguished object anywhere located.

---

## 5. Verdicts

### (a) Is directional differentiability of \(L^p\) metric projections onto subspaces already known, and under what hypotheses?

**Partly, and enough that the programme must not claim the general statement.**

1. **Hilbert space (\(p=2\)): completely settled**, and the subspace case is
   trivial there because the projection is linear.  For convex sets the
   definitive characterization is Noll (Pacific J. Math. 170 (1995) 567–592) via
   second-order Mosco differentiability of the support function; the
   Fitzpatrick–Phelps (Trans. AMS 270 (1982) 483–501) boundary-smoothness
   correspondence is the earlier standard.
2. **Directional differentiability of the metric projection is FALSE in
   general** for closed convex sets, already in the Euclidean plane
   (Shapiro, JOTA 81 (1994) 203–204; \(C^{1,1}\) version Akmal–Nam–Veerman,
   Optim. Lett. 9 (2015) 1039–1052).  Positive results therefore always come
   with structure — second-order regularity (Shapiro, JOTA 169 (2016) 953–964),
   polyhedricity (Mignot 1976; Haraux 1977), or, as here, the set being a
   *subspace*, which is flat.
3. **General Banach case: published claim on the nose.**  Li, J. Optim. Theory
   Appl. 200 (2024) 923–950 (DOI 10.1007/s10957-023-02329-7, arXiv:2303.16265)
   defines Gâteaux directional differentiability of \(P_C\) in uniformly convex
   and uniformly smooth Banach spaces — \(L^3(\mathbb R^3;\mathbb R^3)\) is such
   a space — as a **norm** limit of \([P_C(x+tv)-P_C(x)]/t\) as \(t\downarrow0\),
   and Theorem 7.2 asserts directional differentiability **on all of \(X\)** for
   **every** nonempty closed convex \(C\) once \(X\) is "\(p\)-\(q\) uniformly
   convex and uniformly smooth".  If that hypothesis is read as the usual
   power-type moduli (\(L^3\) being \(3\)-uniformly convex, \(2\)-uniformly
   smooth), then Theorem 7.2 **covers \(C=\mathcal G_3\) and gives a strictly
   stronger conclusion than T3.4**, namely convergence in \(L^3\) itself.  This
   lane could not verify the exponent ordering in Definition 7.1 (see §1.3), so
   the applicability is **undetermined** — but the paper is refereed, published,
   on exactly this topic, and must be cited and compared, not passed over with
   the single sentence the candidate currently gives to a different Li preprint.
4. **The regularity of \(P_{\mathcal G_3}\) short of differentiability is
   classical**: Holmes–Kripke (Michigan Math. J. 15 (1968), DOI
   10.1307/mmj/1028999976) for Lipschitz continuity of \(\ell_p\) subspace
   projections in \(\mathbb R^n\); Björnestål 1979 for the local modulus of
   uniform continuity of the metric projection **onto a closed subspace** in
   uniformly convex and uniformly smooth Banach spaces, globalized by Alber
   (funct-an/9312003) **[AB, abstract read]**; and the nonlinearity of
   \(P_{\mathcal G_3}\) is itself the classical characterization of inner-product
   spaces (Németh, arXiv:2511.19382 **[AB]**).
5. **The shape of the derivative is folklore.**  The stationarity condition
   \(\int|w|^{p-2}w\cdot g=0\) is the textbook characterization of best \(L^p\)
   approximation from a subspace, and its linearization is the weighted normal
   equation with weight \(|r|^{p-2}\) — the IRLS/Gauss–Newton weight
   (Lawson 1961; Rice–Usow, Math. Comp. 22 (1968) 118–127; Osborne 1985)
   **[AB]**.  "The derivative of the \(L^p\) projection is a weighted \(L^2\)
   projection with weight \(\mathrm Dj(\text{residual})\)" is not a new idea.
6. **The proof template is standard.**  Bound the difference quotients in a
   base-point-adapted space, take a weak limit, identify it from the linearized
   optimality condition, upgrade to strong convergence by monotonicity: that is
   convex sensitivity analysis (Bonnans–Shapiro 2000) and second-order
   epi-differentiability via Attouch's theorem (Rockafellar 1988, 1989; Do,
   Trans. AMS 334 (1992) 281–301; for integral functionals specifically Levy,
   Set-Valued Anal. 1 (1993) 379–392, and Loewen–Zheng, Trans. AMS 347 (1995)
   443–459).

**No source was located that states T3.4** — a general infinite-dimensional
closed subspace of \(L^p(\mathbb R^n)\), \(p\ne2\), a general base point, strong
two-sided convergence in the *degenerate weighted completion* \(\mathcal H_U\),
with the explicit warning that \(\mathcal E_U\) need not consist of unweighted
gradients.  That is an absence of located prior art, not priority.

### (b) Is the degenerate-weighted-space phenomenon already named?

**Yes.**  Three separate established names apply to parts of it, and together
they cover the phenomenon:

- **two-norm discrepancy** — differentiability/coercivity split between a
  stronger and a weaker norm; Ioffe, SIAM J. Control Optim. 17 (1979) 266–288;
  standard modern statement Casas–Tröltzsch, Jahresber. DMV 117 (2014/15) 3–44
  **[DI]**.
- **quasi-norm / natural distance / shifted \(N\)-function / \(V\)-function** —
  the weight \((|a|+|b|)^{p-2}\), the substitution \(V=|z|^{(p-2)/2}z\), and the
  equivalence with \((j(a)-j(b))\cdot(a-b)\); Barrett–Liu 1993;
  Diening–Ettwein 2008; Bojarski–Iwaniec 1983 / Uhlenbeck 1977.
- **degenerate elliptic / weighted \(L^2\) energy space of a linearized
  \(p\)-Laplacian** — Fabes–Kenig–Serapioni 1982 for the general framework;
  Zhang arXiv:2608.27276 for a current instance where "the linearized
  \(p\)-Laplacian defined by its closed quadratic form in \(L^2(v^{p^*-2}dx)\)"
  is used without comment.

What is **not** named, so far as located, is the *specific* configuration —
frozen base-point weight, gradient subspace, whole space \(\mathbb R^3\),
\(p=3\).  That is a gap in the located literature, not a naming gap in the
subject.

### (c) What in Section 3 appears not covered by located existing work?

Listed with decreasing confidence.  **None of these is a novelty claim.**

1. The identification of the limit as \(\mathsf L_Uh\) where \(\mathcal E_U\) is
   the \(\mathcal H_U\)-closure of the *image* of \(\mathcal G_3\), together
   with the explicit refusal to identify elements of \(\mathcal E_U\) with
   unweighted gradients.  Located sources either work in Hilbert space (where
   the issue is invisible), in finite dimensions (where the closure is the
   subspace), or with restriction-type subspaces (Li's Bochner support
   subspaces) where the projection is linear.
2. Strong, two-sided (\(\varepsilon\to0\) through both signs) convergence in a
   space that may be the **zero** Hilbert space when \(U=0\) a.e., with the
   remainder bookkeeping carried through an \(L^3\) bound that is allowed to
   diverge like \(|\varepsilon|^{-1/3}\).  The divergent-bound bookkeeping is
   the technically distinctive step; it is what makes the argument work without
   an \(L^3\) derivative.
3. **Hadamard** (not merely Gâteaux) differentiability of \(A:L^3\to L^{3/2}\)
   with derivative \(M_U\mathsf L_U\), obtained by combining the weighted limit
   with the unweighted two-point dual estimate \eqref{eq:Alip}.  Li's framework
   is one-sided Gâteaux; Noll's is Hilbert; nothing located produces a *dual*
   Hadamard derivative into a different \(L^r\).
4. The bilinear identity \(\langle\mathcal B_vh,k\rangle=\langle\mathsf
   L_Uh,\mathsf L_Uk\rangle_U\) and the resulting exact second variation
   \eqref{eq:Qsecond} for \(\tfrac13\operatorname{dist}_{L^3}(\cdot,\mathcal
   G_3)^3\).  The *existence* of a second-order expansion of this kind is what
   second-order epi-differentiability delivers in general; the *closed formula*
   in these terms was not located.

Note also a structural point that no located source makes and that the
candidate could legitimately state as a *framing* observation (not a theorem):
in the entire located metric-projection literature the nonlinearity of \(P_C\)
comes from the **curvature of \(C\)** (hence polyhedricity, second-order
regularity, critical cones).  Here \(C=\mathcal G_3\) is **flat**, and the
entire difficulty comes from the **geometry of the \(L^3\) norm** through the
degeneracy of \(\mathrm Dj\).  That is why the set-geometry hypotheses of
Mignot–Haraux–Shapiro–Noll are all vacuously satisfied and none of their
theorems applies.

---

## 6. WHAT THE PROGRAMME MAY NOT CLAIM

Each item would be false, or unoriginal, if asserted.

1. **Not**: "the differentiability of the metric projection in \(L^p\),
   \(p\ne2\), is new / has not been studied."  It is an active, refereed topic:
   Li, JOTA 200 (2024) 923–950 is exactly this subject, and Björnestål (1979),
   Alber (1993), Holmes–Kripke (1968) are the classical regularity line for
   projections onto **subspaces** of \(L^p\).
2. **Not**: "Li's work is only about \(L^p\) Bochner projections onto support
   subspaces, balls and cylinders", and **not**: that it is an unpublished
   preprint.  That description fits arXiv:2311.00942 only, and that paper is
   published — Applicable Nonlinear Analysis 1 (2024) 79–109, DOI
   10.69829/apna-024-0101-ta05 — so the candidate's bibliography entry
   (`\bibitem{Li}` … "arXiv:2311.00942v1 (2023)") is out of date.  The
   candidate's `sec:ledger` sentence is accurate about that preprint but
   **incomplete as a prior-art statement**, because the same author's *published*
   JOTA paper treats general closed convex subsets of uniformly convex and
   uniformly smooth Banach spaces and states an exact-representation result for
   closed convex cones "including proper closed subspaces".  The comparison must
   be made explicitly, including the possibility that Theorem 7.2 there is
   stronger than T3.4.
3. **Not**: "the derivative of the projection is given by a weighted \(L^2\)
   projection — a new structure."  That is the classical linearization of an
   \(L^p\) best-approximation problem, folklore since Lawson/Rice–Usow/Osborne
   and visible in the textbook characterization \(\int|r|^{p-2}r\cdot g=0\).
4. **Not**: "the degenerate weighted space adapted to the base point is a new
   or unnamed device."  It is the standard energy space of a linearized
   \(p\)-Laplacian-type operator, and the weight/quasi-norm has established
   names (quasi-norm, natural distance, shifted \(N\)-function, \(V\)-function).
5. **Not**: "the failure of the weighted derivative to control the ambient
   \(L^3\) norm is a newly observed obstruction."  It is the **two-norm
   discrepancy**, named and studied since Ioffe (1979) and standard in PDE
   optimal control (Casas–Tröltzsch survey).
6. **Not**: "\(\mathcal Q\) is \(C^{1,1}_{\rm loc}\) / \(j\) is Fréchet
   differentiable \(L^3\to L^{3/2}\) — new."  This is the classical smoothness
   classification of \(L^p\) norms (Bonic–Frampton; Leonard–Sundaresan): the
   best order of differentiability of \(\|\cdot\|_p^p\) is exactly what
   \(p=3\) gives.
7. **Not**: "the proof method (weak limit, identification through the
   linearized optimality condition, monotonicity upgrade) is new."  It is the
   standard convex-sensitivity / second-order epi-derivative template
   (Bonnans–Shapiro; Rockafellar; Attouch; Noll's Hilbert theorem is the same
   statement one setting down).
8. **Not**: "nonlinear Hodge theory does not contain perturbation theory, so
   nothing there is relevant."  The correct statement is weaker and must be said
   as such: *no* linearization-in-the-datum theorem for nonlinear Hodge fields
   was located in this bounded search, and the classical degeneracy studied in
   that line (sonic) is a different degeneracy from the one here (vanishing
   field).
9. **Not**: "the \(p=3\), \(n=3\) case is untreated."  \((\mathbb R^3,
   \|\cdot\|_3)\) appears explicitly in the projection literature (Li,
   Example 6.2/Prop. 6.4) — for a different set, but the case is not untouched.
10. **Not**, in any form: a priority or novelty claim for Theorem 3.5.  The
    candidate's own `sec:ledger` sentence ("a full comparison … would be
    required before claiming novelty") remains the correct posture; this note
    supplies part of that comparison and does **not** clear the way for a
    novelty claim.

A truthful related-work sentence, offered for reuse:

> The map \(u\mapsto w(u)\) is the residual of the metric projection of
> \(L^3(\mathbb R^3;\mathbb R^3)\) onto the closed subspace of gradients, and
> \(\mathcal Q\) is one third of the cube of the induced quotient norm.
> Differentiability of metric projections is a classical subject: it is
> characterized in Hilbert space [Fitzpatrick–Phelps 1982; Noll 1995], it fails
> for general closed convex sets even in the plane [Shapiro 1994], it holds
> under second-order regularity [Shapiro 2016] or polyhedricity [Mignot 1976;
> Haraux 1977], and directional differentiability in uniformly convex and
> uniformly smooth Banach spaces — a class containing \(L^3\) — has been studied
> by Li [JOTA 200 (2024) 923–950; arXiv:2311.00942].  The regularity of
> \(L^p\)-subspace projections short of differentiability goes back to
> Holmes–Kripke [1968] and Björnestål [1979].  The weight
> \(\mathrm Dj(U)=|U|I+U\otimes U/|U|\) is the standard linearization weight of
> an \(L^p\) best-approximation problem and the standard "quasi-norm"/shifted
> \(N\)-function of the \(p\)-Laplacian literature [Barrett–Liu 1993;
> Diening–Ettwein 2008], and the fact that a functional twice differentiable in
> one norm can be coercive only in a weaker one is the two-norm discrepancy
> [Ioffe 1979; Casas–Tröltzsch 2015].  We claim no novelty for any of these.
> We located no statement of the present theorem — strong two-sided convergence
> of the difference quotients in the degenerate weighted completion at an
> arbitrary base point of \(L^3\), with the weighted gradient closure not
> identified with unweighted gradients — but that is a statement about the reach
> of a bounded search and not a claim of priority.

---

## 7. OPEN / COULD NOT DETERMINE

1. **The decisive open item.**  Whether Li's Theorem 7.2 (arXiv:2303.16265; the
   published JOTA 200 (2024) 923–950) applies to \(X=L^3(\mathbb R^3;\mathbb
   R^3)\), \(C=\mathcal G_3\).  As extracted, Definition 7.1 asks for
   \(1<p<q\) with \(\delta(\varepsilon)\ge a\varepsilon^p\) and
   \(\rho(t)\le bt^q\); since always \(\delta\lesssim\varepsilon^2\) and
   \(\rho\gtrsim t^2\), that ordering would make the class empty and the theorem
   vacuous, whereas the ordering \(1<q\le2\le p\) would include \(L^3\) and give
   a **stronger** conclusion than T3.4 (norm convergence in \(L^3\)).  The
   published text is paywalled, the arXiv PDF was readable here only through a
   text-extraction proxy, and no MathSciNet/zbMATH review was reachable.  **This
   must be resolved from the printed JOTA article before any statement about the
   novelty of T3.4 is made anywhere.**  Resolving it either way is consequential:
   if the theorem applies as stated, T3.4 is subsumed and the programme's
   weighted formulation is a *weaker* result about the same map.
2. Whether Li's §6 contains, beyond the extracted Theorem 6.1 (base point inside
   the subspace, direction in \(C^\perp\), derivative \(\theta\)), any statement
   about a subspace at a *general* base point.  Extraction was partial.
3. The bodies of Björnestål (Banach Center Publ. 4 (1979) 43–53) and of the
   J. Approx. Theory 39 (1983) sequel (ScienceDirect returned HTTP 403); the
   sharp modulus of continuity of \(P_{\mathcal G_3}\) in \(L^3\) is therefore
   quoted only from secondary sources.  If that modulus is Hölder-\(1/2\) and
   optimal, it would be direct external evidence that an unweighted \(L^3\)
   derivative cannot exist in general — which would *support* the candidate's
   scope discipline and would also bear on item 1.
4. Whether Casas–Fernández or the later quasilinear optimal-control literature
   contains an explicit theorem that the control-to-state map of a
   \(p\)-Laplacian-type problem is directionally differentiable **only** in a
   degenerate weighted space.  Only secondary/indexed statements were read.
5. Whether \(|w|\) is an \(A_2\) weight for \(w\) in the nonlinear Hodge class
   \(\mathcal M\).  Not asserted by the candidate, not investigated here, and
   relevant only if someone later wants weighted Calderón–Zygmund tools.
6. MathSciNet and zbMATH full records were unreachable without authentication in
   this lane; the WebSearch budget was exhausted before the older
   (1970s–1980s) \(L^p\) best-approximation-operator differentiability
   literature (Wolfe; Kroó; Marano–Quesada; Huotari) could be searched
   systematically.  That is the most likely place for an older statement of the
   \(L^p\)-subspace derivative formula, and it has **not** been checked.

---

## 8. Frontier record

CLAIM AND SCOPE: bibliographic only.  Section 3 of
`hf26-temporal-continuation.tex` is compared with located prior art; no
mathematical statement of the programme is added, removed, strengthened or
weakened.  The independent correctness review of that section is
`hf26-review-weighted-linearization.md` (PASS WITH SCOPE) and is not revisited.

EVIDENCE: Fitzpatrick–Phelps 1982 [DI]; Noll 1995 [DI]; Shapiro 2014 preprint of
JOTA 2016 [DI]; Li arXiv:2303.16265 [DI, via text-extraction proxy]; Li JOTA 200
(2024) abstract [AB]; Casas–Tröltzsch survey [DI]; Marini–Otway arXiv:1206.0189
[DI]; Zhang arXiv:2608.27276 [AB]; Laforest arXiv:1808.05976 [AB]; Alber
funct-an/9312003 [AB]; Németh arXiv:2511.19382 [AB]; Muga–van der Zee
arXiv:1511.04400v3 [DI, negative]; arXiv API abstract searches [DI, negative];
Crossref/Semantic Scholar records for all bibliographic identities marked [MO].
Zotero: searched, no relevant holdings.

NON-CLAIMS: no novelty for any programme object; no priority; no assertion that
any unlocated item is new; no judgement on the correctness of any cited paper,
including Li's; no mathematical consequence of any cited theorem is imported
into the programme by this note.

NEXT DISTINCT ACTION: obtain the printed **J. Optim. Theory Appl. 200 (2024)
923–950** (institutional access or interlibrary), read Definition 7.1 and
Theorem 7.2 in the published text, and settle item 7.1.  Until that is done,
`hf26-temporal-continuation.tex` §10.2 should be amended to cite the **published
JOTA paper** alongside arXiv:2311.00942, and to say that the comparison is
**pending**, not merely "would be required".

