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

### 1.1 The classical Hilbert-space theory (not the programme's case, but the
### frame everything else is stated against)

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
  space", Pacific J. Math. 170 (1995) 567–592.**  **[DI]** (MSP open PDF read
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

### 1.2 Convex sensitivity theory — the general machinery the candidate's proof
### instantiates

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
  (1988) 75–108; "Proto-differentiability of set-valued mappings and its
  applications in optimization", Ann. Inst. H. Poincaré Anal. Non Linéaire 6
  (1989) 449–482 **[MO]**.  The controlling general fact, confirmed in several
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

### 1.3 The directly-on-topic recent line: metric projections in uniformly
### convex, uniformly smooth Banach spaces

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
  spaces", arXiv:2311.00942 (2 Nov 2023)** **[AB]** — the reference already
  carried by the candidate as `\cite{Li}`.  \(L^p(S;X)\) with \(X\) uniformly
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
- **B. O. Björnestål, "Local Lipschitz continuity of the metric projection
  operator", Banach Center Publ. 4 (1979) 43–53** **[MO]**; generalized and
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
  (1974) 229–251** **[AB]**.  For \(p=3\) this gives exactly: \(\|\cdot\|_3^3\)
  is twice continuously differentiable on \(L^3\), with Lipschitz second
  derivative — which is Lemma 3.2 and equation (2.19) `eq:Qprime` of the
  candidate.

---

## 2. Area 2 — nonlinear Hodge and \(p\)-Laplacian perturbation theory

*(filled in from the dedicated searches; see §2.1–§2.3.)*

---

## 3. Area 3 — the degenerate weighted space

*(see §3.1–§3.3.)*

---

## 4. Area 4 — the cubic case \(p=3\) in three dimensions

*(see §4.)*

---
