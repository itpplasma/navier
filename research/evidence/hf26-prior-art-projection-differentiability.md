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
**[MO]** = bibliographic identity only, content not read;
**[SEC]** = statement taken from a directly inspected *citing* source, not the
primary;
**[DL]** = obtained by a delegated search lane inside this note and
re-verified against Crossref/zbMATH/arXiv for bibliographic identity.  The
delegated lane reported that its page-summarising tool **fabricates
bibliographies**, so every [DL] item below carries a verified identifier and no
[DL] item is used for a mathematical conclusion beyond what its quoted text
says.

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
  Problems*, Springer Series in Operations Research, Springer, New York, 2000**,
  DOI 10.1007/978-1-4612-1394-9, ISBN 978-1-4612-1394-9.  **[MO]** (contents and topic list verified: Legendre forms, second-order
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
  space).  Extended to reflexive Banach spaces by **Chi Ngoc Do, "Generalized
  second-order derivatives of convex functions in reflexive Banach spaces",
  Trans. Amer. Math. Soc. 334 (1992) 281–301**, DOI
  10.1090/S0002-9947-1992-1088019-1 **[MO]**, and by **J. L. Ndoutoume and
  M. Théra, "Generalised second-order derivatives of convex functions in
  reflexive Banach spaces", Bull. Austral. Math. Soc. 51 (1995) 55–72**, DOI
  10.1017/S0004972700013897 **[MO]**.  \(L^3\) is reflexive, so this is the
  branch of the general theory that formally covers the present setting.
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

  One further signal, recorded without interpretation: the **arXiv v1** abstract
  announces the \(p\)-\(q\) result ("proves that \(P_C\) is directionally
  differentiable on all of \(X\) for such spaces"), whereas the **published
  JOTA abstract quoted above does not mention it at all**.  Only v1 exists on
  arXiv (28 Mar 2023); the published version was not readable here.  Whether
  Theorem 7.2 survived refereeing is therefore **undetermined**.
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
  Math. J. 15 (1968) 225–248**, DOI 10.1307/mmj/1028999976 (Zbl 0177.16201).
  **[SEC/DL]** — the primary text is blocked on Project Euclid and was not read.
  **This is the single most consequential item in this note.**  Kroó and Pinkus
  (below) state, verbatim:

  > "The Gateaux derivative of the metric projection \(P_Mf\) with respect to
  > \(f\) (not \(M\)) was studied in \(L_p\), \(p>2\), see, e.g., Holmes
  > and Kripke [7]."

  Other citing sources report from it: Lipschitz continuity of \(P_M\) on
  finite-dimensional \(\ell_p^n\) for all \(1<p<\infty\); **local**
  Lipschitz continuity for finite-dimensional subspaces of \(L^p\), \(p>2\);
  and a counterexample of a **one-dimensional** subspace of \(\ell_p\),
  \(p>2\), whose projection is not Lipschitz.  Consequence for this audit: the
  question "is the \(L^p\) metric projection differentiable **in the datum**?"
  was posed and studied in 1968, and the programme may not present it as new.
- **R. Fletcher, J. A. Grant and M. D. Hebden, "The continuity and
  differentiability of the parameters of best linear \(L_p\) approximations",
  J. Approx. Theory 10 (1974) 69–73**, DOI 10.1016/0021-9045(74)90097-5.
  **[MO/DL]** — identity verified, text not obtained (Elsevier 403).  The title
  alone is decisive prior art for the topic of this note.  Companion: **same
  authors, "The calculation of linear best \(L_p\) approximations", Comput. J.
  14 (1971) 276–279**, DOI 10.1093/comjnl/14.3.276 **[AB/DL]**, which derives a
  **second-order convergent** (Newton-type) scheme for best \(L^p\)
  approximation — the linearization was in numerical use by 1971.
- **Two negative results bearing directly on the candidate's scope discipline.**
  - **P. A. Borodin, Yu. Yu. Druzhinin and K. V. Chesnokova, "Finite-dimensional
    subspaces of \(L_p\) with Lipschitz metric projection", Math. Notes 102
    (2017) 465–474**, DOI 10.1134/S0001434617090188 (Mat. Zametki 102 (2017)
    514–525, DOI 10.4213/mzm11479).  **[AB/DL]** (full zbMATH review read): for
    \(p\in(1,\infty)\setminus\{2\}\), \(P_Y\) is Lipschitz **iff**
    \(\operatorname{supp}(Y)\) is a finite union of atoms.  Lebesgue measure
    on \(\mathbb R^3\) is nonatomic, so **no nontrivial finite-dimensional
    subspace of \(L^3(\mathbb R^3)\) has a globally Lipschitz metric
    projection.**  Global Lipschitz continuity is weaker than a bounded Fréchet
    derivative, so this is *external* evidence that the candidate is right to
    refuse an unweighted \(L^3\) derivative of \(w\) and a two-point \(L^3\)
    Lipschitz estimate for \(q\).
  - **V. I. Berdyshev, "On differentiability of the operator of best
    approximation", Colloq. Math. Soc. János Bolyai 35 (1983) 237–248**
    (Zbl 0548.41017).  **[AB/DL]** (full zbMATH review read): there is a smooth,
    bounded, uniformly convex \(M\subset\ell_2^{(2)}\) and a **dense** set on
    which \(P\) has **no directional derivative in any direction**.
- **H. Berens, M. Finzel, W. Li and Y. Xu, J. Math. Anal. Appl. 213 (1997)
  183–201**, DOI 10.1006/jmaa.1997.5521 **[AB/DL]**: a Lipschitz constant for
  \(P_M\) on \((\mathbb R^n,|\cdot|_p)\) **independent of \(p\)**, via
  Hoffman error bounds.
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
- **A. Kroó and A. Pinkus, "On stability of the metric projection operator",
  SIAM J. Math. Anal. 45 (2013) 639–661**, DOI 10.1137/120873534 **[AB]**
  (zbMATH reviewer summary read, Zbl 6189157): for \(L^p(K,\mu)\) with
  \(p>2\) and nonatomic \(\mu\), and \(r\)-dimensional subspaces with the
  \(Z_\mu\) property, \(\|P_Mf-P_Nf\|_p\le c_{M,f}\,d(M,N)\).  This is
  Lipschitz dependence on the **subspace**, not on the point, and the subspaces
  are finite-dimensional; it is the current state of the \(L^p\)-subspace
  projection stability line and does not give T3.4.
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
  functions on certain Banach spaces", Bull. Amer. Math. Soc. 71 (1965)
  393–395**, DOI 10.1090/S0002-9904-1965-11310-6, and **"Smooth functions on
  Banach manifolds", J. Math. Mech. 15 (1966) 877–898**, DOI
  10.1512/iumj.1966.15.15058 **[MO]**; **I. E. Leonard and K. Sundaresan, "Geometry of
  Lebesgue–Bochner function spaces — smoothness", Trans. Amer. Math. Soc. 198
  (1974) 229–251**, DOI 10.1090/S0002-9947-1974-0367652-5 **[AB]**.  For \(p=3\) this gives exactly: \(\|\cdot\|_3^3\)
  is twice continuously differentiable on \(L^3\), with Lipschitz second
  derivative — which is Lemma 3.2 and equation (2.19) `eq:Qprime` of the
  candidate.

### 1.5 Why leaving the ambient space is forced by a theorem, not by technique

The candidate's decision to take the derivative of \(A\) into \(L^{3/2}\)
rather than \(L^3\) — and its refusal to differentiate \(w\) in \(L^3\) —
is not merely convenient; it is compelled by a classical degeneration theorem
for superposition (Nemytskii) operators:

- **J. Appell and P. P. Zabrejko, "On the degeneration of the class of
  differentiable superposition operators in function spaces", Analysis 7 (1987)
  305–312**, DOI 10.1524/anly.1987.7.34.305.  **[AB/DL]** (full zbMATH review
  read by the delegated lane): for ideal spaces \(X,Y\) with suitable
  fundamental-function relations — the review names "particularly \(L_p\) and
  \(L_q\) spaces when \(p\le q\)" — if the superposition operator is
  differentiable at even **one** point, then \(f(s,u)\) is **affine** in
  \(u\).  Consequence for the present objects: \(j:L^3\to L^3\) is provably
  nowhere differentiable, while \(j:L^3\to L^{3/2}\) escapes the theorem
  because \(3/2<3\).  See also **J. Appell and P. P. Zabrejko, *Nonlinear
  Superposition Operators*, Cambridge Tracts in Math. 95, CUP, 1990**, DOI
  10.1017/CBO9780511897450 **[AB/DL]**, and **H. Goldberg, W. Kampowsky and
  F. Tröltzsch, "On Nemytskij operators in \(L_p\)-spaces of abstract
  functions", Math. Nachr. 155 (1992) 127–140**, DOI 10.1002/mana.19921550110
  **[MO/DL]**.

This is a genuine and *citable* structural reason for the candidate's target
space, and it is prior art: the programme must not present "we take the
derivative into \(L^{3/2}\)" as a design insight of its own.

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
  was located in this line.**  Two sharpenings from the delegated lane:
  (i) the Crossref reference list of the 1979 *Applications* paper contains ten
  items (Bers, Conner, Duff–Spencer, Friedrichs, Ladyzhenskaya–Ural'tseva,
  Morrey, Serrin, Shiffman 1952, and their own 1970/1978 papers) — **classical
  a-priori-estimate and direct-method machinery, with no perturbation-theory
  reference at all** **[DI/DL]**; (ii) the existence proof runs through
  "a delicate limiting argument introduced by Shiffman in the planar case"
  (**M. Shiffman, "On the existence of subsonic flows of a compressible fluid",
  J. Rational Mech. Anal. 1 (1952) 605–652**, DOI 10.1512/iumj.1952.1.51020
  **[MO/DL]**), i.e. a variational argument that never requires invertibility of
  a linearization.
- **The programme's density is excluded from that school by hypothesis.**
  **[DI/DL]** — read in **T. H. Otway, "Maps and fields with compressible
  density", arXiv:math-ph/0302064**: the standing assumptions of nonlinear Hodge
  theory are \(0<\frac{d}{dQ}[Q\rho^2(Q)]/\rho(Q)<\infty\) on
  \([0,Q_{\rm crit})\) **together with non-cavitation**
  \(0<\kappa_0\le\rho(Q)\le\rho(0)<\infty\); Otway notes explicitly that
  for the \(L^p\)-critical density "the density … tends to zero (cavitates) as
  ellipticity degenerates; this behavior is atypical of the mass density of
  fluids, for which the sonic value lies at the supremum of the range of
  subsonic speeds."  The programme's \(\rho(Q)=Q^{1/2}\) (\(p=3\), i.e.
  \(\rho=|w|\)) degenerates at \(w=0\) — the **opposite end** from the
  classical sonic degeneracy.  This is the precise, citable reason the Sibner
  school does not cover the programme's equation, and it strengthens (rather
  than weakens) what `cp01` already recorded.
- **Where linearization-in-the-datum *is* classical: transonic gas dynamics —
  and it is known to be ill-posed at the degeneracy.**  The linearized
  potential-flow operator with matrix \(\rho I+2\rho'(Q)\,w\otimes w\) and
  its degeneration at the sonic set is classical, and
  **C. S. Morawetz, "On the non-existence of continuous transonic flows past
  profiles I, II, III", Comm. Pure Appl. Math. 9 (1956) 45–68 (DOI
  10.1002/cpa.3160090104); 10 (1957) 107–131 (DOI 10.1002/cpa.3160100105);
  11 (1958) 129–144 (DOI 10.1002/cpa.3160110107)** **[SEC/DL]** proves that the
  perturbation problem attached to a smooth transonic flow **is not correctly
  posed**: shock-free transonic flows are unstable under arbitrarily small
  perturbations of the profile.  Survey used: **G.-Q. G. Chen, "Morawetz's
  contributions to the mathematical theory of transonic flows, shock waves, and
  partial differential equations of mixed type", Bull. Amer. Math. Soc. (2024)**,
  DOI 10.1090/bull/1816, arXiv:2310.07097 **[DI/DL]**; the survey does *not* put
  the linearized transonic operator in a weighted energy space.  Background:
  Bers, Comm. Pure Appl. Math. 7 (1954) 441–504, DOI 10.1002/cpa.3160070303;
  Finn–Gilbarg, Acta Math. 98 (1957) 265–296, DOI 10.1007/BF02404476; and, for
  the modern weighted treatment of elliptic degeneracy at a sonic boundary,
  **G.-Q. Chen and M. Feldman, *The Mathematics of Shock Reflection-Diffraction
  and von Neumann's Conjectures*, Ann. of Math. Studies 197, Princeton, 2018**,
  DOI 10.1515/9781400885435 **[MO/DL]**.  This is genuine cognate prior art for
  the *degeneracy* half of the question, with the caveat that the degeneracy
  sits at the opposite end of the range.
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
  abs:"directional differentiability"` returns **zero**.  A zbMATH Open API
  search for `nonlinear Hodge linearized` returns nothing in this subject at
  all; the delegated lane reports that the arXiv abstract index contains only
  **eight** papers using the phrase "nonlinear Hodge" at all.  These are bounded
  index searches, not proof of absence.  The delegated lane additionally checked
  and found no linearization-in-the-datum content in: L. M. Sibner, Manuscripta
  Math. 43 (1983) 45–72 (DOI 10.1007/BF01169096); P. Smith, Indiana Univ. Math.
  J. 31 (1982) 553–577 (DOI 10.1512/iumj.1982.31.31042); Otway, J. Geom. Phys.
  27 (1998) 65–78 (DOI 10.1016/S0393-0440(97)00066-1), J. Math. Phys. 41 (2000)
  5745–5766 (DOI 10.1063/1.533436), Ann. Mat. Pura Appl. 181 (2002) 437–452
  (DOI 10.1007/s10231-002-0049-x), and both of his books (*The Dirichlet Problem
  for Elliptic-Hyperbolic Equations of Keldysh Type*, LNM 2043, Springer 2012,
  DOI 10.1007/978-3-642-24415-5 — whose weighted spaces are for **linear**
  equations whose degeneracy is a prescribed function of position, not generated
  by the unknown; and *Elliptic–Hyperbolic Partial Differential Equations*,
  SpringerBriefs, 2015, DOI 10.1007/978-3-319-19761-6); Iwaniec–Scott–
  Stroffolini, Ann. Mat. Pura Appl. 177 (1999) 37–115; Iwaniec–Martin, *Geometric
  Function Theory and Non-linear Analysis*, OUP 2001, DOI
  10.1093/oso/9780198509295.001.0001; Hamburger, J. Reine Angew. Math. 431
  (1992) 7–64, Adv. Math. 190 (2005) 360–424 and its general-growth sequel; Stern
  arXiv:2403.19481 (published in Contemp. Math. 816, AMS, 2025, 151–170); and
  Beck–Stroffolini, Calc. Var. PDE 46 (2012) 769–808.  All **[MO/DL]** or
  **[AB/DL]**.
- **Citation correction for `cp01`.**  `cp01-prior-art-quotient.md` §1.2 lists
  the general-growth nonlinear Hodge heat-flow sequel as "J. Differential
  Equations 421 (2025) 264–290".  Crossref gives **C. Hamburger, "The heat flow
  in nonlinear Hodge theory under general growth", J. Differential Equations 416
  (2025) 531–575, DOI 10.1016/j.jde.2024.09.043** **[MO/DL]**.  The `cp01`
  volume/pages appear to have come from an indexed summary and should be
  corrected there; its authorship question is also answered (Hamburger).  Its
  36-item reference list contains nothing on linearization or differentiability
  in the datum.
- **One structurally identical statement exists, but discrete and
  degeneracy-free**: **S. Pardo-Guerra, A. Thapa, J. Washburn, "The cactus
  criterion: when nonlinear Hodge theory reduces to linear on graphs",
  arXiv:2604.17775 (2026)** **[DI/DL]**, an unrefereed preprint.  On a finite
  graph they build a nonlinear coclosed selector \(\Pi_{cc}\) and prove
  (Thm III.7) that its differential is a **weighted Hodge projector**,
  \(D\Pi_{cc}(\omega)[\xi]=\xi-d\,L_w^{-1}\delta_w\xi\) with
  \(\delta_w\xi=\delta(w\odot\xi)\), \(w_e=\cosh(\Pi_{cc}(\omega)_e)\).
  That is the same *shape* as T3.4 — but the degeneracy is absent by
  construction (\(\psi''=\cosh\ge1\)), the proof is the finite-dimensional
  implicit function theorem, and the authors cite no continuum prior art.  Treat
  as a same-shape statement in a setting where the whole difficulty is removed.

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

**"Linearized \(p\)-Laplacian" is an established name for exactly the
programme's \(M_U\).**  The delegated lane established this with primary
sources:

- **B. Sciunzi, "A weak maximum principle for the linearized operator of
  \(m\)-Laplace equations with applications to a nondegeneracy result", Adv.
  Differential Equations 10 (2005), no. 2**, DOI 10.57262/ade/1355867889
  **[MO/DL]**; **D. Castorina, P. Esposito and B. Sciunzi, "Spectral theory for
  linearized \(p\)-Laplace equations", Nonlinear Anal. 74 (2011) 3606–3613**,
  DOI 10.1016/j.na.2011.03.009 **[MO/DL]** — the canonical reference;
  **S. Cingolani, M. Degiovanni and B. Sciunzi, "Weighted Sobolev spaces and
  Morse estimates for quasilinear elliptic equations", J. Funct. Anal. 286
  (2024), no. 8, 110346**, DOI 10.1016/j.jfa.2024.110346 **[MO/DL]** — the title
  alone records that the degenerate weighted Sobolev space is the working
  setting for the second variation.
- **The operator written out with the programme's exact two-sided bound.**
  **J. Lewis**, chapter in **J. Lewis, P. Lindqvist, J. J. Manfredi and
  S. Salsa, *Regularity Estimates for Nonlinear Elliptic and Parabolic
  Problems*, Lecture Notes in Math. 2045 (CIME Foundation Subseries), Springer,
  2012**, DOI 10.1007/978-3-642-27145-8.  **[DI/DL]** (2009 preprint read in
  full).  Equations (1.6)–(1.10):
  \(L\zeta=\partial_i[b_{ij}\zeta_{x_j}]=0\),
  \(b_{ij}=|\nabla u|^{p-4}[(p-2)u_{x_i}u_{x_j}+\delta_{ij}|\nabla u|^2]\),
  with
  \(\min\{p-1,1\}|\nabla u|^{p-2}|\xi|^2\le b_{ik}\xi_i\xi_k\le
  \max\{1,p-1\}|\nabla u|^{p-2}|\xi|^2\),
  and the verbatim remark "Observe from (1.10) that \(L\) can be degenerate
  elliptic if \(\nabla u=0\)."  This is the programme's \(M_U\), its
  eigenvalue bounds, and its degeneracy, in print and named.
- **Yitian Zhang, "The complete spectrum of the linearized \(p\)-Laplacian at a
  Sobolev extremal", arXiv:2608.27276 (27 Aug 2026)** **[AB]** (official
  abstract read here; text read by the delegated lane **[DI/DL]**).  Verbatim:
  "…the linearized \(p\)-Laplacian at \(v\), **defined by its closed quadratic
  form in \(L^2(\mathbb R^n,v^{p^*-2}\,dx)\)**".  The form is
  \(a_v[\varphi,\psi]=\int A_v\nabla\varphi\cdot\nabla\psi\) with
  \(A_v=|\nabla v|^{p-2}(I+(p-2)\nu\otimes\nu)\); the radial and tangential
  eigenvalues \((p-1)|\nabla v|^{p-2}\) and \(|\nabla v|^{p-2}\) "both vanish
  where \(v'=0\)", and the degeneracy is handled **by form closure rather than
  by a differential expression** — precisely the candidate's device.
- **The strongest existing use of a space of this type**: **A. Figalli and
  Y. R.-Y. Zhang, "Sharp gradient stability for the Sobolev inequality", Duke
  Math. J. 171 (2022), no. 12**, DOI 10.1215/00127094-2022-0051,
  arXiv:2003.04037.  **[DI/DL]** — they work in
  \(\dot W^{1,2}(\mathbb R^n;|Dv|^{p-2})\), the closure of \(C^1_{c,0}\)
  under \((\int|D\varphi|^2|Dv|^{p-2})^{1/2}\), and prove a **compact
  embedding** into \(L^2(\mathbb R^n;v^{p^*-2})\) (Prop. 3.2) and a **spectral
  gap** for the second-variation form (Prop. 3.6).  Predecessor: **A. Figalli
  and R. Neumayer, J. Eur. Math. Soc. 21 (2019) 319–354**, DOI 10.4171/JEMS/837
  **[MO/DL]**.
- **H. Varpanen, "On a linearized \(p\)-Laplace equation with rapidly
  oscillating coefficients", arXiv:1506.04586 (2015)** **[DI/DL]** — solves a
  singular Neumann problem for the linearized \(p\)-Laplace equation in an
  explicitly degenerate power-weighted space.

Together with §3 below this settles the status of the *construction* \(\mathcal
H_U\): it is the routine, **named** energy space of a linearized degenerate
elliptic operator, not a new object.  Two scale caveats from the delegated lane:
the exact phrase "linearized \(p\)-Laplacian" occurs in only about four arXiv
titles/abstracts (many authors simply write "the linearized operator" or display
the matrix), and the delegated lane found **no** source using that phrase for the
*normalized/game-theoretic* \(p\)-Laplacian \(\Delta_p^N\), so the two names
are not in fact conflated in print.

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
- A reviewed *negative* statement of the same species: **O. P. Kupenko and
  R. Manzo, "On optimality conditions for optimal control problem in
  coefficients for \(\Delta_p\)-Laplacian", Bound. Value Probl. 2014, Paper
  No. 72**, DOI 10.1186/1687-2770-2014-72 (Zbl 6370892) **[AB]** — the zbMATH
  review states that "the mapping \(u\to y(u)\) is **not
  Fréchet-differentiable** on the class of admissible controls", which forces
  quasi-adjoint states instead of classical optimality conditions.  Control is
  in the coefficients there, not the datum, so this is an analogue and not a
  counterpart; but it shows that failure of differentiability for
  \(p\)-Laplacian solution maps is a recognized, published phenomenon and not
  something the programme discovered.

- **Two further published statements that the ambient-space derivative does not
  exist**, both **[AB/DL]**: **A. Hirn and W. Wollner, "An optimal control
  problem for equations with \(p\)-structure and its finite element
  discretization", in *Optimization and Control for Partial Differential
  Equations*, De Gruyter, 2022, 137–166**, DOI 10.1515/9783110695984-007 —
  verbatim from the abstract: *"As the nonlinear operator related to the
  \(p\)-Laplace equation mapping the space \(W_0^{1,p}(\Omega)\) to its dual
  \((W_0^{1,p}(\Omega))^*\) is **not Gâteaux differentiable**, first-order
  optimality conditions cannot be formulated in a standard way."*  And
  **M. Salo and X. Zhong, "An inverse problem for the \(p\)-Laplacian: boundary
  determination", SIAM J. Math. Anal. 44 (2012) 2474–2495**, DOI
  10.1137/110838224, whose abstract says *"The proofs work with the nonlinear
  equation directly instead of being based on linearization"* and whose
  Appendix A shows the Gâteaux derivatives of the \(p\)-DtN map "do not even
  exist if \(1<p<2\)".
- **The closest published statement of the candidate's programme — as an open
  problem.**  **A. Hannukainen, N. Hyvönen and L. Mustonen, "An inverse boundary
  value problem for the \(p\)-Laplacian: a linearization approach", Inverse
  Problems 35 (2019), no. 3, 034001**, DOI 10.1088/1361-6420/aaf2df,
  arXiv:1803.10591.  **[DI/DL]**  The published abstract ends: the forward
  operator "is Fréchet differentiable, **excluding the degenerate case that
  corresponds to the classical (weighted) \(p\)-Laplace equation**."  Remark
  3.5, verbatim: *"If \(\tau=0\), \(p\ne2\) and \(u_\sigma\) has critical
  points in \(\bar\Omega\), then the coefficient matrix … is either unbounded
  (\(1<p<2\)) or without a positive definite lower bound (\(2<p<\infty\)).
  There exists theory for the unique solvability of such degenerate elliptic
  equations, but those results would typically require \(|\nabla u_\sigma|^{p-2}\)
  to lie in a suitable Muckenhoupt class … **The unique solvability … for
  \(\tau=0\) in an appropriate weighted Sobolev space does not seem to
  straightforwardly follow … without further assumptions on the behavior of
  \(|\nabla u_\sigma|\) close to the critical points.**"*  The delegated lane
  checked all ten papers citing it: **none carries out the extension.**  This is
  the single best external reference point for what the candidate's Section 3
  is attempting.
- **Recovery under a nondegeneracy hypothesis, with the programme's matrix
  written out.**  **C. I. Cârstea and A. Feizmohammadi, "Two uniqueness results
  in the inverse boundary value problem for the weighted \(p\)-Laplace
  equation", Forum Math. Sigma (2025)**, DOI 10.1017/fms.2025.10095,
  arXiv:2405.04123, §2 and Prop. 3 **[DI/DL]**: linearizing
  \(\nabla\cdot(\gamma|\nabla u|^{p-2}\nabla u)=0\) at \(u_0\) gives
  \(\nabla\cdot(A\nabla\dot u)=0\) with
  \(A_{jk}=\gamma|\nabla u_0|^{p-2}[\delta_{jk}+(p-2)\partial_ju_0\,\partial_ku_0/
  |\nabla u_0|^2]\) — exactly \(M_U\) — together with the verbatim caveat "we
  can only perform the linearization if \(u_0\) does not have any critical points
  in \(\Omega\)".

**Verdict for Area 2.**  The *mechanism* (linearize the nonlinear Hodge /
\(p\)-Laplacian equation, land in a degenerate weighted energy space) is
standard and named; a *theorem* that the nonlinear Hodge projection is
differentiable in the datum was **not located** in the nonlinear Hodge
literature at all, and the delegated lane established the precise reason that
literature does not reach here (cavitation).  On the \(p\)-Laplacian side the
pattern is sharper than "not located": differentiability in the ambient space is
**published as false or unavailable** (Hirn–Wollner; Salo–Zhong; and
structurally, Appell–Zabrejko, §1.5), it is recovered only after regularization
or under \(|\nabla u|>0\), and the degenerate case is named as **open** by
Hannukainen–Hyvönen–Mustonen.  Nothing found contradicts the candidate; the
literature instead marks its target as the recognized hard case.

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

- **"quasi-norm"** — **J. W. Barrett and W. B. Liu, "Quasi-norm error bounds
  for the finite element approximation of a non-Newtonian flow", Numer. Math. 68
  (1994) 437–456**, DOI 10.1007/s002110050071 **[MO/DL]**, and **W. B. Liu and
  J. W. Barrett, "Quasi-norm error bounds for the finite element approximation of
  some degenerate quasilinear elliptic equations and variational inequalities",
  RAIRO Modél. Math. Anal. Numér. 28 (1994) 725–744**, DOI
  10.1051/m2an/1994280607251 **[MO/DL]**.  **Attribution correction:** the
  earlier **Math. Comp. 61 (1993) 523–537** paper, DOI
  10.1090/S0025-5718-1993-1192966-4, proves \(W^{1,q}\) error bounds and does
  **not** yet introduce the quasi-norm; the name dates from the two 1994 papers.
  The term is a *fixed attributed phrase*: "the quasi-norm of Barrett and Liu"
  occurs verbatim from **L. Diening and C. Kreuzer, SIAM J. Numer. Anal. 46
  (2008) 614–638**, DOI 10.1137/070681508 onward, and the attribution is explicit
  in reviewed sources, e.g. **B. Andreianov, F. Boyer and F. Hubert, IMA J.
  Numer. Anal. 26 (2006) 472–502**, DOI 10.1093/imanum/dri047 (Zbl 5043011)
  **[AB]**.  Later development: Liu–Yan, SIAM J. Numer. Anal. 39 (2001) 100–127,
  DOI 10.1137/S0036142999351613 and 40 (2002) 1870–1895, DOI
  10.1137/S0036142901393589; Ebmeyer–Liu, Numer. Math. 100 (2005) 233–258, DOI
  10.1007/s00211-005-0594-5; Belenki–Berselli–Diening–Růžička, SIAM J. Numer.
  Anal. 50 (2012) 373–397, DOI 10.1137/100804360.  All **[MO/DL]**.
- **"shifted \(N\)-function"** \(\varphi_a(t)=\int_0^t\varphi'(a+s)\frac
  {s}{a+s}\,ds\) — canonically **L. Diening and F. Ettwein, "Fractional
  estimates for non-differentiable elliptic systems with general growth", Forum
  Math. 20 (2008) 523–556**, DOI 10.1515/forum.2008.027 **[MO]**; the earliest
  located occurrence of the phrase is **M. Růžička and L. Diening,
  "Non-Newtonian fluids and function spaces", in *NAFSA 8 — Nonlinear Analysis,
  Function Spaces and Applications*, Institute of Mathematics AS CR, Praha, 2007,
  95–143** **[AB/DL]**, self-described as "a detailed and self-contained
  exposition of shifted \(N\)-functions".  See also Diening–Růžička, Numer.
  Math. 107 (2007) 107–129, DOI 10.1007/s00211-007-0079-9 **[MO/DL]**.  That the term is established is confirmed by an independent
  reviewed source: the zbMATH review of **L. Diening and C. Kreuzer, "Linear
  convergence of an adaptive finite element method for the \(\varphi\)-Laplacian
  equation", SIAM J. Numer. Anal. 46 (2008) 614–638**, DOI 10.1137/070681508
  (Zbl 5549695) speaks of "so-called shifted \(N\)-functions which provide to
  handle with more complex problem than \(p\)-Laplacian" **[AB]**.
- **"natural distance"** — the settled name for the whole equivalence class.
  **A. Kaltenbach, "Error analysis for a Crouzeix–Raviart approximation of the
  \(p\)-Dirichlet problem", J. Numer. Math. 32 (2024) 111–138**, DOI
  10.1515/jnma-2022-0106, arXiv:2210.12116.  **[DI/DL]** Remark 2.6, verbatim:
  "\((\mathcal A(\nabla u)-\mathcal A(\nabla v),\nabla u-\nabla v)_\Omega
  \sim\|F(\nabla u)-F(\nabla v)\|^2_{L^2}\sim
  \rho_{\varphi_{|\nabla u|},\Omega}(\nabla u-\nabla v)$ … **We refer to all
  three equivalent quantities as the natural distance.**"  Its Proposition 2.4
  and Remark 2.1 give the candidate's chain in exactly the candidate's form,
  including \(\varphi_a(t)\sim(\delta+a+t)^{p-2}t^2\).  Corroborating:
  **J. Storn, arXiv:2507.12742** **[DI/DL]**, Prop. 6 and Remark 7;
  **L. C. Berselli and A. Kaltenbach, IMA J. Numer. Anal. 45 (2025) 3026–3076**,
  DOI 10.1093/imanum/drae082 **[DI/DL]**, Remark 2.22 and Prop. 2.14;
  **K.-N. Le and J. Wichmann, Stochastic Process. Appl. 177 (2024) 104443**, DOI
  10.1016/j.spa.2024.104443 **[AB/DL]**, which uses "the natural distance" twice
  in its abstract with no definition — settled vocabulary.
- **the \(V\)- / \(F\)-function substitution** \(V(z)=|z|^{(p-2)/2}z\),
  \(F(z)=(\delta+|z|)^{(p-2)/2}z\) — already recorded in
  `cp01-prior-art-quotient.md` §1.7 (Bojarski–Iwaniec 1983 via Lindqvist Thm 4.1
  **[DI]**; Uhlenbeck 1977).  The programme uses exactly this as
  \(V=|w|^{1/2}w\).  Note **[DL]**: "\(V\)-function" as a *name* is marginal
  in the literature; the substitution is universally attributed to Uhlenbeck.
- **a fourth name, not anticipated:** the same object is the (symmetric)
  **Bregman divergence** of the \(\varphi\)-Dirichlet integrand,
  \(\mathcal D_\varphi(a,b)=\varphi(a)-\varphi(b)-\mathcal A(b)\cdot(a-b)\)
  — stated explicitly in **P. A. Gazca-Orozco, "Bregman divergences and error
  control via convex duality", arXiv:2606.05088 (2026)** **[DI/DL]**, §2.3, which
  also says verbatim that this quantity "is what is usually known as a
  *quasi-norm* or *natural distance*".  This matters for the candidate:
  \(B(a,d)\) of `eq:Bbelow`/`eq:Babove` **is** the Bregman divergence of
  \(\tfrac13|z|^3\), and that identification is standard.

So: the *weight*, the *quadratic form*, the *change of variable* and the
*Bregman-divergence reading* in the candidate's \(\mathcal H_U\) and its
Taylor remainders are all standard \(p\)-Laplacian machinery, named since 1994
(quasi-norm), 2007 (shifted \(N\)-function) and roughly 2012 (natural
distance).  Classical ancestry, all **[MO/DL]** except as noted: Uhlenbeck, Acta
Math. 138 (1977) 219–240, DOI 10.1007/BF02392316; **J. Simon, "Régularité de la
solution d'une équation non linéaire dans \(\mathbb R^N\)", Lecture Notes in
Math. 665, Springer, 1978, 205–227**, DOI 10.1007/BFb0061807; Bojarski–Iwaniec,
Ann. Acad. Sci. Fenn. 8 (1983) 257–324, DOI 10.5186/aasfm.1983.0806;
Giaquinta–Modica, Manuscripta Math. 57 (1986) 55–99, DOI 10.1007/BF01172492;
**E. Acerbi and N. Fusco, J. Math. Anal. Appl. 140 (1989) 115–135**, DOI
10.1016/0022-247X(89)90098-X.

### 3.2 Shifted weight versus frozen weight: the point on which the candidate is careful, and which is elementary

For \(p\ge2\) the **shifted** quantity does control the ambient norm, pointwise:
\(|a|+|b|\ge|a-b|\) gives \((|a|+|b|)^{p-2}|a-b|^2\ge|a-b|^p\).  The candidate's
\(\mathcal H_U\) uses instead the **frozen** weight \(\rho=|U|\) at the base
point, and then no such inequality is available: \(|U|\) does not dominate
\(|z_\varepsilon-z_m|\), and the form vanishes identically on \(\{U=0\}\).  The
only available comparison runs the other way, by Hölder:
\(\int\rho|a|^2\le\|\rho\|_3\|a\|_3^2\), which is the candidate's
\eqref{eq:L3embed}.  This is elementary and already recorded internally in
`hf22-projection-regularity.md` (the weighted-to-unweighted conversion failure
and the exponent \(1/2\)).

**It is also said explicitly in print, and the sentence should be quoted rather
than re-derived.**

- **A. Figalli and Y. R.-Y. Zhang, "Sharp gradient stability for the Sobolev
  inequality", Duke Math. J. 171 (2022), no. 12**, DOI
  10.1215/00127094-2022-0051, §1.3.  **[DI/DL]** Verbatim: *"for \(p>2\) the
  \(L^p\) norm of \(D\varphi\) may **not** be controllable by its weighted
  \(L^2\) norm"*, and *"when \(p<2\), the \(\dot W^{1,p}\) norm is weaker
  than any weighted \(\dot W^{1,2}\) norm, so we cannot expand the deficit at
  order 2."*  Their weight is exactly \(|Dv|^{p-2}\) with \(v\) a **frozen**
  base point (the Aubin–Talenti bubble).  **This is the candidate's Remark 3.7
  obstruction, stated in the literature four years earlier, for the same weight
  and the same reason.**
- The positive half is equally in print: **S. Conti, M. Focardi and F. Iurlano,
  Commun. Contemp. Math. 21 (2019), no. 6, 1950026**, DOI
  10.1142/S0219199719500263, eq. (2.16) **[DI/DL]**:
  \(t^p/p\le\phi_a(t)\le(\mu+(a+t)^2)^{p/2-1}t^2/2\) for \(p\in[2,\infty)\),
  which with their (2.24) gives \(|a-b|^p\le C|V(a)-V(b)|^2\).
- **The decisive structural point, and it is not a technicality.**  The standard
  quasi-norm is **two-argument by construction**: Storn's Remark 7
  (arXiv:2507.12742) **[DI/DL]** identifies the Barrett–Liu quasi-norm as
  \((|Q|+|P-Q|)^{p-2}|P-Q|^2\), and Lewis–Nyström's linearization uses the
  *secant* coefficient \(\int_0^1\mathrm Dj(\nabla u_\tau)\,d\tau\) with
  \(\lambda\approx(|\nabla\hat u|+|\nabla\hat v|)^{p-2}\) (JEMS 20 (2018),
  eq. (4.13)) **[DI/DL]**.  **A frozen base-point weight \(|U|^{p-2}\) is the
  degenerate special case that the standard objects were designed to avoid.**
- **The literature's uniform response to the frozen weight is avoidance, not
  resolution** — a pattern worth recording because the candidate does *not*
  avoid it:
  - truncate/relax the weight: **L. Diening, M. Fornasier, R. Tomasi and
    M. Wank, "A relaxed Kačanov iteration for the \(p\)-Poisson problem",
    Numer. Math. 145 (2020) 1–34**, DOI 10.1007/s00211-020-01107-1 **[AB/DL]**;
    **A. Kh. Balci, L. Diening and J. Storn, "Relaxed Kačanov scheme for the
    \(p\)-Laplacian with large exponent", SIAM J. Numer. Anal. 61 (2023)
    2775–2794**, DOI 10.1137/22M1528550 **[DI/DL]**, which says verbatim that the
    approach "degenerates at points where \(|\sigma|=0\) and
    \(|\sigma|=\infty\)" and truncates the weight as
    \((\varepsilon_-\vee|\sigma|\wedge\varepsilon_+)^{2-q}\);
  - restrict the operator to \(\{\nabla u\ne0\}\): **A. Naber and
    D. Valtorta, Math. Z. 277 (2014) 867–891**, DOI 10.1007/s00209-014-1282-x,
    Definition 3.1 **[DI/DL]** — the linearized operator "is defined pointwise
    only where the gradient of \(u\) is non zero … and it is easily proved that
    at these points it is strictly elliptic";
  - concede the difficulty outright: **J. Lewis and K. Nyström, Ann. of Math.
    (2) 172 (2010) 1907–1948**, DOI 10.4007/annals.2010.172.1907, p. 1946
    **[DI/DL]** — the PDE "degenerates at points where \(\nabla u=0\), and
    therefore at such points it is not clear how to prove even basic interior
    estimates for solutions";
  - or get it wrong: **H. Varpanen, Illinois J. Math. 59 (2015), no. 2**, DOI
    10.1215/ijm/1462450711, §1.4 headed **"Statement of error"** **[DI/DL]** — a
    previously published claim that solutions of the linearized \(p\)-Laplace
    equation are \(C^0(\bar D)\cap W^{1,\infty}(D)\) is **withdrawn**, because
    the argument "claimed uniform ellipticity in dyadic annuli near the origin,
    but in fact the gradients of the test functions in Caccioppoli-type
    inequalities do not stay bounded".  A documented failure caused precisely by
    the frozen-weight degeneracy.
- **The candidate's own device is also in print.**  **Y. Zhang,
  arXiv:2608.27276 (2026)**, §1 **[DI/DL]**, verbatim: *"In the present
  whole-space problem, the formal differential expression
  \(-\operatorname{div}(A_v\nabla\cdot)\) does not by itself specify a
  self-adjoint operator.  We therefore define \(L_v\) through the closure of its
  quadratic form; this construction determines both the operator domain and the
  endpoint conditions inherited from the original energy space."*  That is
  exactly the candidate's move of defining \(\mathcal H_U\) and
  \(\mathcal E_U\) by completion rather than by a differential expression, and
  the programme may not present it as its own idea.

Two delegated cross-cutting findings, recorded because they bound the whole
area: **no located source claims that the frozen-weight form controls \(L^p\)**,
and **no located source claims to have overcome the obstruction across
\(\{U=0\}\) in general** — consistent across numerical analysis,
boundary-behaviour/potential theory, and Sobolev-stability.

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
- Independent confirmation that the term is standard, from zbMATH reviewer texts
  **[AB]**: **K. Malanowski, "Sufficient optimality conditions for optimal
  control subject to state constraints", SIAM J. Control Optim. 35 (1997)
  205–227**, DOI 10.1137/S0363012994267637 (Zbl 1000472) — reviewed as "the
  two-norm discrepancy approach, where the problem is defined and differentiable
  in a strong norm … but the coercivity condition is satisfied only in a weaker
  norm"; **K. Malanowski, "Regularity of solutions in stability analysis of
  optimization and optimal control problems", Control Cybernet. 23 (1994)
  61–86** (Zbl 597932) — the norm discrepancy is "intrinsicly connected with
  nonlinear optimal control problems"; **F. Tröltzsch, Optimization 22 (1991)**
  (Zbl 4205241); **H. Maurer, Math. Program. Stud. 14 (1981) 163–177**, DOI
  10.1007/BFb0120927; **L. M. Betz, SIAM J. Control Optim. 57 (2019) 4033–4062**,
  DOI 10.1137/19M1239106 ("the second-order conditions require the typical
  two-norm discrepancy").
- The abstract counterpart is the failure of the **Legendre form** condition of
  Bonnans–Shapiro: their sensitivity theorems require the second-order term to
  be a Legendre form on the ambient space (weak lower semicontinuity plus
  "weak convergence with convergence of the form implies strong convergence").
  \(\|\cdot\|_U^2\) *is* a Legendre form on \(\mathcal H_U\) — it is the square
  of that Hilbert norm — but not on \(L^3\).  **[AB]** for the definition, as
  quoted in several primary sources located.
- The degenerate weighted \(L^2\) space itself sits in the classical
  Muckenhoupt/degenerate-elliptic framework: **B. Muckenhoupt, Trans. Amer.
  Math. Soc. 165 (1972) 207–226**, DOI 10.1090/S0002-9947-1972-0293384-6;
  **E. B. Fabes, C. E. Kenig and R. P. Serapioni, "The local regularity of
  solutions of degenerate elliptic equations", Comm. Partial Differential
  Equations 7 (1982) 77–116**, DOI 10.1080/03605308208820218 **[MO]**, which for
  \(w\in A_2\) builds \(H^{1,2}(\Omega,w)\) with uniqueness of the weak
  gradient, weighted Sobolev–Poincaré, local boundedness, Hölder continuity and
  a scale-invariant Harnack inequality; **E. Fabes, D. Jerison and C. Kenig,
  "The Wiener test for degenerate elliptic equations", Ann. Inst. Fourier
  (Grenoble) 32 (1982) 151–182**, DOI 10.5802/aif.883 **[DI/DL]** (open at
  Numdam); nonlinear counterpart **J. Heinonen, T. Kilpeläinen and O. Martio,
  *Nonlinear Potential Theory of Degenerate Elliptic Equations*, Oxford, 1993
  (Dover 2006/2018)** **[AB/DL]**, whose Theorem 15.21 states that \(A_p\)
  weights are \(p\)-admissible; and **B. O. Turesson, *Nonlinear Potential
  Theory and Weighted Sobolev Spaces*, Lecture Notes in Math. 1736, Springer,
  2000**, DOI 10.1007/BFb0103908 **[AB/DL]**.
- **The programme's exact space is attributed in print.**  The completion of
  \(C_c^1\) under \((\int|\nabla U|^{p-2}|\nabla\varphi|^2)^{1/2}\) with
  inner product \(\int|\nabla U|^{p-2}\langle\nabla\varphi,\nabla\psi\rangle\)
  — i.e. \(\langle a,b\rangle_U\) — is credited to **L. Damascelli and
  B. Sciunzi, J. Differential Equations 206 (2004) 483–515**, DOI
  10.1016/j.jde.2004.05.012, and **Calc. Var. PDE 25 (2006) 139–159**, DOI
  10.1007/s00526-005-0337-6, in later work (**A. Pistoia and G. Vaira, Proc.
  Roy. Soc. Edinburgh Sect. A 151 (2021) 151–168**, DOI 10.1017/prm.2020.7,
  arXiv:1903.11011, §2, verbatim: "A similar first order Sobolev space with
  weight was introduced by Damascelli and Sciunzi [9] to study a linearized
  operator on a bounded domain") **[DI/DL]**.  Also named and constructed as
  \(\tilde W^{1,2}(O)\) with \(\|v\|^2=\int v^2\lambda+\int|\nabla
  v|^2\lambda\), \(\lambda=|\nabla u|^{p-2}\), and its \(C_0^\infty\)
  closure, in **J. Lewis and K. Nyström, "Quasi-linear PDEs and low-dimensional
  sets", J. Eur. Math. Soc. 20 (2018) 1689–1746**, DOI 10.4171/JEMS/797, eq.
  (4.5), which then says "For the proof of the following lemma we refer to
  [FKS]" **[DI/DL]**.
- **The \(A_2\) question for \(|\nabla u|^{p-2}\) is answered in the boundary
  setting, and answered both ways.**  **J. Lewis and K. Nyström, Ann. Sci. Éc.
  Norm. Supér. (4) 40 (2007) 765–813**, DOI 10.1016/j.ansens.2007.09.001, p. 769
  **[DI/DL]**, verbatim: for \(p\) near 2, \(|\nabla\hat u|^{p-2}\) "extends
  to an \(A_2\) weight on \(\mathbb R^n\)"; but "**In the general case,
  \(1<p<\infty\), \(p\ne2\), we must work harder, as simple examples show
  that \(h=|\nabla\hat u|^{p-2}(\cdot,\tau)\) need not be an \(A_2\)
  weight.**"  Positively, in Reifenberg-flat domains with small constant it does
  extend to an \(A_2\) weight (**Lewis–Nyström, Adv. Calc. Var. 1 (2008)
  133–170**, DOI 10.1515/ACV.2008.005, Lemma 3.30, restated as Lemma 4.7 of
  **Lewis–Nyström–Vogel, J. Eur. Math. Soc. 15 (2013) 2197–2256**, DOI
  10.4171/JEMS/420) **[DI/DL]** — but the mechanism is the fundamental
  inequality \(|\nabla u|\approx u/d(\cdot,\partial\Omega)\), which **excludes
  critical points by hypothesis**.  The candidate assumes **no** weighted
  Calderón–Zygmund or \(A_2\) property (`sec:foundations` says so explicitly),
  so this is context, not an import; and see §7 for what remains open.

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

- One genuine \(p=3\) boundary in the located literature: **Osborne's
  convergence analysis of IRLS covers exactly \(1<p<3\)** (**M. R. Osborne,
  *Finite Algorithms in Optimization and Data Analysis*, Wiley, 1985**
  **[SEC/DL]**, as reported in J. Sigl, Comput. Optim. Appl. 64 (2016) 755–792,
  DOI 10.1007/s10589-016-9829-x, arXiv:1504.06815, which also writes the weight
  verbatim as \(w_i=|r_i|^{p-2}\) from the identity
  \(\|r\|_p^p=\|r\|^2_{\ell_2(w)}\)).  The programme's exponent sits **at
  that boundary**.  Nothing follows from this for the programme's theorem, but
  it is the only place located where \(p=3\) is a genuine endpoint rather than
  an arbitrary value.

**Verdict for Area 4.**  The cubic case carries no special standing in this
literature; \(p=3\) is convenient (it makes \(f(z)=\tfrac13|z|^3\) exactly
\(C^2\) with Lipschitz second derivative, by the classical smoothness
classification of \(L^p\) norms — Bonic–Frampton; Leonard–Sundaresan) but is not
a distinguished object anywhere located.

---

## 5. Verdicts

### (a) Is directional differentiability of \(L^p\) metric projections onto subspaces already known, and under what hypotheses?

**Yes in substance, and the programme must not claim the general statement.**

0. **The question was posed and studied in 1968.**  Kroó–Pinkus (SIAM J. Math.
   Anal. 45 (2013) 639–661) write verbatim: "The Gateaux derivative of the metric
   projection \(P_Mf\) with respect to \(f\) (not \(M\)) was studied in
   \(L_p\), \(p>2\), see, e.g., Holmes and Kripke [7]" — i.e. **Holmes–Kripke,
   Michigan Math. J. 15 (1968) 225–248**.  Six years later,
   **Fletcher–Grant–Hebden, J. Approx. Theory 10 (1974) 69–73**, is titled *"The
   continuity and differentiability of the parameters of best linear \(L_p\)
   approximations"*.  Neither text could be read in this lane, but the
   attribution and the title are enough: **the differentiability of the \(L^p\)
   metric projection in the datum is a fifty-year-old subject.**

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

7. **Two independent results push against any naive stronger statement.**
   Borodin–Druzhinin–Chesnokova (2017): over a nonatomic measure, no nontrivial
   finite-dimensional subspace of \(L^p\), \(p\ne2\), has a globally Lipschitz
   metric projection.  Berdyshev (1983): a dense set of points where the
   best-approximation operator has no directional derivative in any direction.
   These support the candidate's non-claims and make Li's Theorem 7.2 (§1.3) all
   the more in need of checking.

**No source was located that states T3.4** — a general infinite-dimensional
closed subspace of \(L^p(\mathbb R^n)\), \(p\ne2\), a general base point, strong
two-sided convergence in the *degenerate weighted completion* \(\mathcal H_U\),
with the explicit warning that \(\mathcal E_U\) need not consist of unweighted
gradients.  That is an absence of located prior art, not priority — and it is a
*weaker* absence than it looked before this lane read Holmes–Kripke's citation
context, since the 1968 and 1974 primary texts were not obtained.

### (b) Is the degenerate-weighted-space phenomenon already named?

**Yes — unambiguously, and one source states the exact obstruction verbatim.**
The single most important sentence located in this whole lane is
**Figalli–Zhang, Duke Math. J. 171 (2022), §1.3**: *"for \(p>2\) the \(L^p\)
norm of \(D\varphi\) may not be controllable by its weighted \(L^2\) norm"* —
same weight \(|Dv|^{p-2}\), same frozen base point, same conclusion as the
candidate's Remark 3.7, four years earlier.  Beyond that, four established names
apply to parts of the phenomenon:

- **two-norm discrepancy** — differentiability/coercivity split between a
  stronger and a weaker norm; Ioffe, SIAM J. Control Optim. 17 (1979) 266–288;
  standard modern statement Casas–Tröltzsch, Jahresber. DMV 117 (2014/15) 3–44
  **[DI]**.
- **quasi-norm** (Barrett–Liu **1994**, not 1993), **natural distance**
  (settled since roughly 2012, defined verbatim in Kaltenbach 2024 Rem. 2.6),
  **shifted \(N\)-function** (Růžička–Diening 2007; Diening–Ettwein 2008), and
  the **\(V\)/\(F\) substitution** (Uhlenbeck 1977; Bojarski–Iwaniec 1983) —
  four names for one object, which is also the **Bregman divergence** of the
  \(p\)-Dirichlet integrand (Gazca-Orozco 2026).
- **the linearized \(p\)-Laplacian and its degenerate weighted energy space** —
  named at title level since Sciunzi 2005 and Castorina–Esposito–Sciunzi 2011;
  Naber–Valtorta (Math. Z. 2014, §3) call the operator "quite common in recent
  literature"; the energy space is constructed and named repeatedly
  (Lewis–Nyström JEMS 2018 eq. (4.5) citing Fabes–Kenig–Serapioni;
  Damascelli–Sciunzi 2004/2006, to whom the *exact* form \(\langle
  a,b\rangle_U\) is credited in print; Pistoia–Vaira 2021; Figalli–Neumayer 2019
  and Figalli–Zhang 2022, with a proved compact embedding and spectral gap;
  Varpanen 2015, with a proved density theorem for it; Y. Zhang 2026, defining
  it by form closure exactly as the candidate does).
- **degenerate elliptic / Muckenhoupt framework** — Muckenhoupt 1972;
  Fabes–Kenig–Serapioni 1982; Fabes–Jerison–Kenig 1982; Heinonen–Kilpeläinen–
  Martio 1993; Turesson 2000.

What is **not** named, so far as located, is the *specific* configuration —
frozen base-point weight, **gradient coset / metric-projection** setting, whole
space \(\mathbb R^3\), \(p=3\).  That is a gap in the located literature, not a
naming gap in the subject.  And a delegated cross-cutting finding sharpens it:
the standard objects are **two-argument (shifted) by construction** — Barrett–Liu's
quasi-norm is \((|Q|+|P-Q|)^{p-2}|P-Q|^2\), and Lewis–Nyström linearize with the
*secant* coefficient \(\int_0^1\mathrm Dj(\nabla u_\tau)d\tau\) — so the frozen
weight is the degenerate special case that everyone else regularizes,
truncates, or excludes by hypothesis.  The candidate does none of those, which
is its real distinguishing feature; but "nobody else kept the degenerate case"
is not the same as "nobody else could have".

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
   an \(L^3\) derivative.  Contextually this is the sharpest item: every
   located community meeting the same frozen-weight degeneracy **avoids** it
   (relax/truncate the weight, regularize the equation, or assume
   \(\nabla u\ne0\)), and no located source claims to have overcome it in
   general.  Keeping the degenerate case is what the candidate does that they do
   not; that is a difference in scope, not by itself a theorem nobody could
   prove.
3. **Hadamard** (not merely Gâteaux) differentiability of \(A:L^3\to L^{3/2}\)
   with derivative \(M_U\mathsf L_U\), obtained by combining the weighted limit
   with the unweighted two-point dual estimate \eqref{eq:Alip}.  Li's framework
   is one-sided Gâteaux; Noll's is Hilbert; nothing located produces a *dual*
   Hadamard derivative into a different \(L^r\).
4. The bilinear identity \(\langle\mathcal B_vh,k\rangle=\langle\mathsf
   L_Uh,\mathsf L_Uk\rangle_U\) and the resulting exact second variation
   \eqref{eq:Qsecond} for \(\tfrac13\operatorname{dist}_{L^3}(\cdot,\mathcal
   G_3)^3\).  The *existence* of a second-order expansion of this kind is what
   second-order epi-differentiability delivers in general, and a spectral-gap
   analysis of the same kind of degenerate second-variation form is already in
   print (Figalli–Neumayer 2019; Figalli–Zhang 2022); the *closed formula* for
   the distance-cubed to a gradient subspace was not located.

**Removed from this list by the delegated searches.**  The device of defining
the linearized operator **by closure of its quadratic form** rather than by a
differential expression, which the candidate uses for \(\mathcal H_U\) and
\(\mathcal E_U\), is *not* distinctive: Y. Zhang (arXiv:2608.27276, §1) states
it verbatim as the required construction in the whole-space \(p\)-Laplacian
setting.  Likewise the choice of an unweighted \(L^{3/2}\) target for the dual
derivative is *forced* by the Appell–Zabrejko degeneration theorem (§1.5), not a
design insight.

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
10. **Not**: "the degenerate weighted space is defined by form closure because
    the differential expression is not self-adjoint — a device we introduce."
    Y. Zhang (arXiv:2608.27276, §1) states exactly that, verbatim, for the
    whole-space linearized \(p\)-Laplacian.
11. **Not**: "we take the dual derivative into \(L^{3/2}\) rather than \(L^3\)
    as a matter of convenience or of our own design."  Appell–Zabrejko
    (Analysis 7 (1987) 305–312) makes leaving the ambient space **mandatory**: a
    superposition operator differentiable at even one point between comparable
    ideal spaces is affine.
12. **Not**: "the frozen base-point weight is the natural object of the
    \(p\)-Laplacian literature."  It is not — the standard quasi-norm and the
    standard linearization coefficient are both **shifted / two-argument**
    (Storn, Remark 7; Lewis–Nyström JEMS 2018, eq. (4.13)).  The programme's
    frozen weight is the degenerate special case, and saying so is part of an
    honest related-work paragraph.
13. **Not**: "the obstruction that the weighted derivative gives no unweighted
    control is our observation."  Figalli–Zhang (Duke 2022, §1.3) state it
    verbatim for the same weight.
14. **Not**: attributing the nonlinear Hodge non-coverage to a vague
    'different hypotheses'.  The precise, citable reason is **cavitation**: the
    standing non-cavitation hypothesis \(0<\kappa_0\le\rho\le\rho(0)<\infty\)
    of that school excludes \(\rho(Q)=Q^{1/2}\), whose degeneracy sits at the
    **opposite end** of the range from the classical sonic degeneracy (Otway,
    arXiv:math-ph/0302064).
15. **Not**, in any form: a priority or novelty claim for Theorem 3.5.  The
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
> by Li [JOTA 200 (2024) 923–950; Appl. Nonlinear Anal. 1 (2024) 79–109].  The
> Gâteaux derivative of the \(L^p\) metric projection with respect to the datum
> was already studied for \(p>2\) by Holmes and Kripke [1968], and the
> continuity and differentiability of the parameters of best linear \(L^p\)
> approximations by Fletcher, Grant and Hebden [1974]; the modulus of continuity
> of \(L^p\)-subspace projections is due to Björnestål [1979].  Over a nonatomic
> measure no nontrivial finite-dimensional subspace of \(L^p\), \(p\ne2\), has a
> globally Lipschitz metric projection [Borodin–Druzhinin–Chesnokova 2017], and
> a superposition operator differentiable at one point between comparable ideal
> spaces is affine [Appell–Zabrejko 1987]; both explain why no unweighted
> derivative is available and why the dual derivative must land in a smaller
> \(L^r\).  The weight \(\mathrm Dj(U)=|U|I+U\otimes U/|U|\) is the standard
> linearization weight of an \(L^p\) best-approximation problem and the
> "quasi-norm" / "natural distance" / shifted \(N\)-function of the
> \(p\)-Laplacian literature [Barrett–Liu 1994; Diening–Ettwein 2008;
> Kaltenbach 2024]; the corresponding degenerate weighted energy space is the
> standard setting for the linearized \(p\)-Laplacian [Damascelli–Sciunzi
> 2004/2006; Lewis–Nyström 2018; Figalli–Zhang 2022], and defining it by closure
> of the quadratic form is the standard construction [Zhang 2026].  That the
> weighted control gives no unweighted control is stated in exactly this setting
> by Figalli and Zhang [2022], and the general phenomenon of a functional twice
> differentiable in one norm being coercive only in a weaker one is the two-norm
> discrepancy [Ioffe 1979; Casas–Tröltzsch 2015].  We claim no novelty for any of
> these.  We located no statement of the present theorem — strong two-sided
> convergence of the difference quotients in the degenerate weighted completion
> at an arbitrary base point of \(L^3\), for the gradient coset, with the
> weighted gradient closure not identified with unweighted gradients — but that
> is a statement about the reach of a bounded search and not a claim of
> priority.

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
   text-extraction proxy, and no MathSciNet/zbMATH review was reachable.
   The zbMATH record exists (**Zbl 7814937**, MSC 47A58, 47J30, 49J40) but its
   review text is withheld ("contents unavailable due to conflicting licenses").
   A second unresolved sub-item: the published JOTA abstract does not mention
   the \(p\)-\(q\) theorem at all, although the arXiv v1 abstract does, so
   Theorem 7.2 may not be in the printed paper.  **This must be resolved from
   the printed JOTA article before any statement about the novelty of T3.4 is
   made anywhere.**  Resolving it either way is consequential:
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
4. Whether **Casas–Fernández, J. Differential Equations 104 (1993) 20–47**,
   DOI 10.1006/jdeq.1993.1062, genuinely excludes degeneracy.  Neither this lane
   nor the delegated lane could read it (the publisher suppresses the abstract;
   ScienceDirect returns 403), so the "excludes degeneracy" reading rests on
   secondary description only.  The related Casas–Tröltzsch line (SIAM J. Control
   Optim. 48 (2009) 688–718, DOI 10.1137/080720048) was checked and is **not**
   applicable: its nonlinearity is in the state, not in the gradient, so the
   \(p\)-Laplacian is outside that class.
5. Whether \(|w|\) is an \(A_2\) weight for \(w\) in the nonlinear Hodge class
   \(\mathcal M\).  Not asserted by the candidate; see item 7 for the state of
   the analogous \(p\)-harmonic question, which is the nearest available proxy.
6. **Two 20th-century primary texts that decide how much of T3.4 is old were
   not obtained**, and they now rank with item 1:
   - **Holmes–Kripke, Michigan Math. J. 15 (1968) 225–248** — the source Kroó
     and Pinkus cite for "the Gateaux derivative of the metric projection
     \(P_Mf\) with respect to \(f\) … in \(L_p\), \(p>2\)".  Project Euclid
     blocked every route.  **What exactly is proved there, and under what
     hypotheses on the subspace, is the single largest remaining unknown in this
     note.**
   - **Fletcher–Grant–Hebden, J. Approx. Theory 10 (1974) 69–73** — five pages
     whose title is this note's question.  Elsevier returned 403.
   Two zbMATH queries (`differentiability best approximation operator L_p`;
   `best L_p approximation operator Gateaux derivative subspace`) returned
   nothing further, and MathSciNet was unreachable, so the rest of that period
   (Wolfe; Marano–Quesada; Huotari) is under-covered.
7. **The interior \(A_2\) question.**  No published statement, positive or
   negative, was located on whether \(|\nabla u|^{p-2}\) is a Muckenhoupt
   \(A_2\) weight **in the interior** for a general \(p\)-harmonic \(u\) with
   critical points — including in the plane, where critical points are isolated.
   Full-text searches for `"is an A_2 weight" AND "p-harmonic"` and
   `"extends to an A_2 weight"` returned nothing.  The two places an explicit
   open-problem list plausibly sits could not be reached: **J. Lewis, LNM 2045
   (2012), pp. 1–72** (its zbMATH review notes "A list of open problems is also
   given") and Lewis's BIRS 10w5066 slides.  Not load-bearing for the candidate,
   which assumes no \(A_2\) property, but load-bearing for anyone who later
   wants weighted Calderón–Zygmund tools here.
8. **How large \(\{w=0\}\) can be is not known in the relevant generality.**
   For \(p\)-harmonic functions in \(n\ge3\), **no bound of any kind on the
   critical set is known** — verbatim from **V. Agostiniani, C. Mantegazza,
   L. Mazzieri and F. Oronzio, arXiv:2205.11642v3, §1.3** **[DI/DL]**: "unlike
   for harmonic functions — no a priori bound is available for the Hausdorff
   dimension of the critical set of a \(p\)-harmonic function, when \(n\ge3\)
   … albeit it is a common belief that critical values of \(p\)-harmonic
   functions should not have positive measure, this possibility is not excluded
   by any result in the literature, so far."  The programme's \(w\) is not
   \(p\)-harmonic, so this does not transfer; it is recorded because it shows
   that the degeneracy the candidate carries is not one the field knows how to
   dismiss.

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
zbMATH Open API records and reviewer texts for Kroó–Pinkus (Zbl 6189157),
Diening–Kreuzer (Zbl 5549695), Kupenko–Manzo (Zbl 6370892), Malanowski
(Zbl 1000472, Zbl 597932), Betz (Zbl 7141507), and the withheld review of Li
(Zbl 7814937) [AB]; two zbMATH queries on the differentiability of the best
\(L^p\) approximation operator returned nothing [DI, negative];
Crossref/Semantic Scholar records for all bibliographic identities marked [MO].
Zotero: searched, no relevant holdings.  Two delegated search lanes inside this
note contributed the [DL] items; both re-verified every citation against
Crossref/zbMATH/arXiv/OpenAlex after reporting that the page-summarising tool
fabricates bibliographies, and both deleted the PDFs the fetch tool auto-cached.
No third-party PDF was retained anywhere in this lane; the fetch tool's automatic
PDF cache was cleared after each read.

Reliability note carried forward: no [DL] item is used here for a mathematical
conclusion beyond what its quoted text says, and every [DL] item carries a
verified identifier.  The delegated lanes also flagged that they could not read
Sibner–Sibner 1970, Uhlenbeck 1977, Iwaniec 1992, Iwaniec–Sbordone 1994,
Iwaniec–Martin 2001, Casas–Fernández 1993, Holmes–Kripke 1968,
Fletcher–Grant–Hebden 1974, Fabes–Kenig–Serapioni 1982,
Heinonen–Kilpeläinen–Martio, or Turesson; statements about those are [SEC], [AB]
or [MO] and are labelled as such.

NON-CLAIMS: no novelty for any programme object; no priority; no assertion that
any unlocated item is new; no judgement on the correctness of any cited paper,
including Li's; no mathematical consequence of any cited theorem is imported
into the programme by this note.

NEXT DISTINCT ACTION: obtain three primary texts, in this order — (1) the
printed **J. Optim. Theory Appl. 200 (2024) 923–950**, to read Definition 7.1
and Theorem 7.2 and settle §7.1; (2) **Holmes–Kripke, Michigan Math. J. 15
(1968) 225–248**, to find out exactly what was proved in 1968 about the Gâteaux
derivative of the \(L^p\) metric projection in the datum; (3)
**Fletcher–Grant–Hebden, J. Approx. Theory 10 (1974) 69–73**, five pages whose
title is this note's question.  Together these decide how much of Theorem 3.4 is
genuinely uncovered.  Until that is done,
`hf26-temporal-continuation.tex` §10.2 should be amended to cite the **published
JOTA paper** alongside arXiv:2311.00942, and to say that the comparison is
**pending**, not merely "would be required".


---

## 9. CONTROLLER RESOLUTION of item 7.1 (2026-09-06)

The lane recorded the applicability of Li's Theorem 7.2 as **undetermined**,
because the exponent ordering in Definition 7.1 could not be verified from the
openly available text, and flagged obtaining the printed JOTA article as the
next distinct action. That was recorded in `PLAN.md` as a blocking external
dependency.

**It is no longer blocking.** The lane's obstacle was tooling, not access: it
read the preprint through a text-extraction proxy, which is exactly the wrong
instrument for a mathematical definition. Re-read through a PDF reader, the
arXiv preprint `arXiv:2303.16265` yields Definition 7.1 and the proof of
Theorem 7.2 verbatim. The third-party file was read and then deleted; nothing
is retained.

**Definition 7.1, verbatim in substance.** `X` is *p-q uniformly convex and
uniformly smooth* if there are `a, b >= 1` and `1 < p < q` with

    (c)  delta(eps) >= a eps^p   for eps in (0,2],
    (d)  rho(t)     <= b t^q     for t > 0,

where `delta` is the modulus of convexity and `rho` the modulus of smoothness.
The proof of Theorem 7.2 uses the ordering essentially: its convergence factor
is `t^(q/p - 1)`, and the proof's closing step is the observation
`q/p - 1 > 0`.

**Finding 1 — Theorem 7.2 does not apply to our space, for a reason independent
of any convention.** `L^3(R^3)` has modulus of convexity of power type
`max(3,2) = 3` and modulus of smoothness of power type `min(3,2) = 2`, so in
Li's notation `p = 3` and `q = 2`. The hypothesis `p < q` fails, and the proof's
convergence factor becomes `t^(2/3 - 1) = t^(-1/3)`, which **diverges** as
`t` decreases to zero rather than vanishing. So the theorem's mechanism does not
merely fail to be verifiable for `L^3`; it runs backwards there.

**Finding 2 — as stated in the preprint the hypothesis class is empty, so the
theorem is vacuous.** By Nordlander's theorem every Banach space satisfies
`delta_X <= delta_Hilbert ~ eps^2/8` and `rho_X >= rho_Hilbert ~ t^2/2`.
Condition (c) with `a >= 1` therefore forces `p > 2`, and condition (d) forces
`q <= 2`. Hence `p > 2 >= q` for every Banach space, contradicting the required
`p < q`. Verified numerically against the Hilbert moduli. Relatedly, the
preprint attributes (c) and (d) to the Pisier renorming theorem, which gives the
**opposite** ordering, convexity of power type at least two and smoothness of
power type at most two.

**Verdict.** Li's Theorem 7.2 **does not subsume** the candidate's weighted
linearization, and could not subsume anything as the hypothesis is stated. The
programme still may not claim novelty for the linearization — every other ground
in section 6 stands untouched, and those grounds are what matter — but this
particular paper is not the reason.

**Scope of this resolution.** This reads the March 2023 arXiv preprint, not the
published J. Optim. Theory Appl. 200 (2024) 923-950, which may have been
corrected in review. Finding 1 is independent of that: it depends only on the
power types of `L^3` and on the direction of the proof's convergence factor, so
a corrected ordering in the published version would still leave `L^3` outside
the theorem's reach unless the proof were changed as well. Finding 2 is a claim
about the preprint only. This is a controller derivation and has not been
independently audited.
