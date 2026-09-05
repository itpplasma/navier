# Critical regularity criteria for three-dimensional Navier–Stokes

This note is for a reader checking whether a conditional regularity theorem can settle the Clay problem. The equation is
\[
 \partial_tu+u\cdot\nabla u+\nabla p=\nu\Delta u,\qquad \nabla\cdot u=0,
\]
with \(\nu>0\). On \(\mathbb R^3\), the Navier–Stokes scaling is
\(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\). Thus \(L^p_tL^q_x\) is critical when \(2/p+3/q=1\), and \(\dot B^{3/q-1}_{q,r}\) is critical in space.

## Prodi–Serrin range

Serrin’s interior theorem gives the standard criterion: a Leray–Hopf (or suitable weak, in the local formulation) solution is regular on an interior cylinder whenever
\[
 u\in L^p(0,T;L^q(\Omega)),\qquad \frac2p+\frac3q\le1,
\]
with \(q\in(3,\infty]\), \(p\in[2,\infty]\), and the displayed relation (the case \(q=\infty\) is therefore allowed, with \(p=2\) on the critical line). The endpoint \(p=\infty,q=3\) is excluded here and is supplied by the separate theorem below. In the Cauchy problem on \(\mathbb R^3\), if a Leray–Hopf solution has this membership up to every finite \(T\), it is strong and unique on that interval; for smooth data it therefore continues smoothly. The original source is Serrin, “On the interior regularity of weak solutions of the Navier–Stokes equations,” *Arch. Rational Mech. Anal.* 9 (1962), 187–195, [DOI and publisher record](https://doi.org/10.1007/BF00253344). The source concerns interior regularity, so boundary regularity requires the corresponding boundary hypotheses; \(\Omega\) may be a domain and the local conclusion is away from its parabolic boundary.

The strict condition \(2/p+3/q<1\) is subcritical and is easier to propagate. The equality line with \(q>3\) is critical and is included in the Prodi–Serrin theorem. The point \((p,q)=(\infty,3)\) is the unresolved endpoint in the elementary energy argument and needs Escauriaza–Seregin–Šverák. These criteria fail to settle arbitrary three-dimensional data because they assume precisely the spacetime integrability whose finiteness is unknown; Leray–Hopf theory supplies only \(L^\infty_tL^2_x\cap L^2_t\dot H^1_x\), which is supercritical relative to the scaling.

## The Escauriaza–Seregin–Šverák endpoint

For the whole-space Cauchy problem in three dimensions, Escauriaza, Seregin and Šverák proved the endpoint statement
\[
 u\in L^\infty(0,T;L^3(\mathbb R^3))
 \quad\Longrightarrow\quad
 \text{no singularity occurs before }T
\]
for a suitable weak solution (with the usual local energy inequality and finite-energy framework). Equivalently, a solution that first becomes singular at a finite time must have unbounded critical \(L^3_x\) norm as that time is approached. The proof uses backward uniqueness and unique continuation for the vorticity. The primary paper is Escauriaza, Seregin and Šverák, “\(L_{3,\infty}\)-solutions of the Navier–Stokes equations and backward uniqueness,” *Russian Math. Surveys* 58 (2003), 211–250, [DOI record](https://doi.org/10.1070/RM2003v058n02ABEH000609). A full theorem-text source is Gallagher–Koch–Planchon, [arXiv:1012.0145](https://arxiv.org/html/1012.0145), Theorem 4 (§3.1): for every \(u_0\in L^3(\mathbb R^3)\), if \(T^*(u_0)\) is the maximal strong-solution time and \(\sup_{0\le t<T^*}\|NS(u_0)(t)\|_{L^3}<\infty\), then \(T^*=\infty\) (the displayed theorem and equivalence with \(L_{3,\infty}\) are at lines 449–455). Its contrapositive is the requested finite-time formulation: if \(T^*<\infty\), then \(\sup_{t<T^*}\|u(t)\|_{L^3}=\infty\). This applies to a maximal smooth Schwartz-data solution because Schwartz data lie in \(L^3\); an \(H^m\) solution needs additional \(L^3\) membership (or an embedding assumption), since bare \(H^m(\mathbb R^3)\) does not uniformly imply \(L^3\) at every low regularity.

The endpoint is conditional because it assumes a uniform-in-time bound in the scale-invariant norm. It does not establish such a bound for arbitrary Leray–Hopf solutions, nor does it rule out finite-time growth of \(\|u(t)\|_{L^3}\). It is a continuation criterion, not global regularity from arbitrary finite-energy data.

## BKM-type vorticity continuation for Navier–Stokes

The name Beale–Kato–Majda properly refers to the 1984 Euler theorem: for a smooth Euler solution, finite-time breakdown requires divergence of \(\int_0^T\|\omega(t)\|_{L^\infty}\,dt\), where \(\omega=\nabla\times u\). The original paper is Beale, Kato and Majda, “Remarks on the breakdown of smooth solutions for the 3-D Euler equations,” *Comm. Math. Phys.* 94 (1984), 61–66, [bibliographic record](https://doi.org/10.1007/BF01212349).

For Navier–Stokes, the standard viscous continuation theorem has the same necessary condition: let \(u\) be a classical solution on \([0,T)\times\mathbb R^3\) (or on the periodic torus), with divergence-free initial data in \(H^m\), \(m>5/2\), and let \(T<\infty\) be its maximal classical time. Then
\[
 \int_0^T\|\omega(t)\|_{L^\infty}\,dt<\infty
 \quad\Longrightarrow\quad
 u\text{ extends as a classical solution past }T.
\]
Hence a finite-time breakdown forces the integral to be infinite. A primary Navier–Stokes source in this BMO/vorticity continuation line is Kozono and Taniuchi, “Bilinear estimates in BMO and the Navier–Stokes equations,” *Math. Z.* 235 (2000), 173–194, [DOI and abstract](https://doi.org/10.1007/s002090000130); its abstract explicitly states that velocity and vorticity BMO norms control blow-up of smooth Cauchy solutions in \(\mathbb R^n\), \(n\ge3\). The exact \(L^\infty_x\)-vorticity continuation implication also follows from the classical higher Sobolev energy estimate and the logarithmic control of \(\|\nabla u\|_\infty\).

This criterion does not prove global regularity: it converts the unknown question into control of a stronger, pointwise vorticity integral. It is also a whole-space/periodic classical-solution statement; bounded domains need boundary-compatible versions, and one cannot apply it directly to an arbitrary weak solution before knowing that the solution is strong.

## Critical spaces and small data

Kato proved local well-posedness and the small-data global theory in the critical Lebesgue framework: for divergence-free \(u_0\in L^3(\mathbb R^3)\) with sufficiently small norm, the mild solution is global and regular for positive times. The general-dimensional source is Kato, “Strong \(L^p\)-solutions of the Navier–Stokes equation in \(\mathbb R^m\), with applications to weak solutions,” *Math. Z.* 187 (1984), 471–480, [EuDML record](https://eudml.org/doc/173504) and [DOI metadata](https://doi.org/10.1007/BF01174182).

The directly inspected formulation in Gallagher–Koch–Planchon’s preliminaries uses \(\dot B^{s_p}_{p,q}(\mathbb R^3)\), \(s_p=-1+3/p\), with \(3<p\le q<\infty\): it defines the maximal strong solution in this class and states that sufficiently small data give \(T^*=\infty\). It adds that \(q=\infty\) can be included under a smallness condition, while local solutions are not generally available there; this is a precise setup statement, not a license to assert a theorem for every Besov index. See [their full theorem source, §1, lines 116–129](https://arxiv.org/html/1012.0145). Koch and Tataru reached the endpoint scale \(BMO^{-1}(\mathbb R^3)\): there is an \(\varepsilon>0\) such that \(\|u_0\|_{BMO^{-1}}<\varepsilon\) implies a global solution regular for \(t>0\). The primary paper is Koch and Tataru, “Well-posedness for the Navier–Stokes equations,” *Adv. Math.* 157 (2001), 22–35, [author-hosted bibliographic page](https://math.berkeley.edu/~tataru/research.html); the regularity consequence is recorded in Germain–Pavlović–Staffilani, [arXiv:math/0609781](https://arxiv.org/abs/math/0609781).

Smallness is the decisive restriction. Criticality alone gives no global theorem for large data; \(BMO^{-1}\) is a rough initial-data space and the construction does not supply a bound for arbitrary data. Some critical Besov endpoints are in fact ill-posed, so “critical” is not synonymous with a usable global theory.

## Quantitative bounds from critical control

Tao quantified the ESS mechanism for smooth solutions on \(\mathbb R^3\times[0,T)\) that are uniformly bounded in critical \(L^3_x\): replacing compactness and qualitative backward uniqueness by quantitative estimates gives higher-derivative bounds with triple-exponential dependence on the critical bound. If a finite blow-up time \(T_*\) exists, then along an infinite sequence \(t\uparrow T_*\),
\[
 \|u(t)\|_{L^3_x}\gtrsim
 \bigl(\log\log\log(1/(T_*-t))\bigr)^c
\]
for an absolute \(c>0\). See Tao, “Quantitative bounds for critically bounded solutions to the Navier–Stokes equations,” [arXiv:1908.04958](https://arxiv.org/abs/1908.04958), revised 2020; the abstract gives both the domain, norm, and triple-logarithmic conclusion.

Subsequent quantitative work includes Barker–Prange, “Quantitative regularity for the Navier–Stokes equations via spatial concentration,” *Comm. Math. Phys.* 385 (2021), 717–792, [open-access article](https://link.springer.com/article/10.1007/s00220-021-04122-x), which treats finite-energy solutions on \(\mathbb R^3\) under Type-I weak-\(L^3\) control and quantifies concentration and singular-point information. Palasek, [arXiv:2101.08586](https://arxiv.org/abs/2101.08586), obtains improved double-exponential estimates for axisymmetric or cylindrical weighted critical norms. Lei–Ren, “Quantitative partial regularity of the Navier–Stokes equations and applications,” *Adv. Math.* 445 (2024), 109654, [DOI](https://doi.org/10.1016/j.aim.2024.109654), gives logarithmic improvements to Caffarelli–Kohn–Nirenberg partial regularity and applications mainly in the axisymmetric/small-swirl setting.

The newest directly relevant source found by the requested cutoff is Hu, Nguyen, Nguyen and Zhang, “Quantitative bounds for bounded solutions to the Navier–Stokes equations in endpoint critical Besov spaces,” [arXiv:2411.06483](https://arxiv.org/abs/2411.06483), version 4 revised 20 August 2026. For classical \(u\) on \([0,T]\times\mathbb R^3\), \(3<p<\infty\), it assumes simultaneous uniform bounds
\[
 u\in L^\infty_t\dot B^{-1+3/p}_{p,\infty},
 \qquad |D|^{-1+3/p}u\in L^\infty_tL^p_x,
\]
and obtains explicit derivative bounds and a mixed blow-up criterion, with quadruple-exponential dependence on the Besov norm and double-exponential dependence on the fractional \(L^p\) quantity (the arXiv abstract is the inspected source for these hypotheses and conclusions). This is an arXiv preprint, even though its 2026 revision is newer than the 2024 version.

These quantitative results sharpen conditional information but leave the central gap intact. They require a uniform critical bound, a Type-I bound, symmetry, spatial concentration hypotheses, or two simultaneous critical controls. None establishes a priori control of those quantities for every large, arbitrary, smooth divergence-free datum, and none proves global regularity for the full three-dimensional Cauchy problem.

## Source status

“Inspected” here means the linked primary paper, publisher record, or arXiv abstract was opened and its domain, hypotheses, and stated conclusion were checked. The Serrin and Kato links are bibliographic/full-text records rather than theorem-text extraction; the ESS theorem is corroborated by the later primary-author arXiv paper and its explicit attribution. Search-result snippets and secondary explanatory pages were used only to locate sources and are not treated as evidence for a stronger claim. The literature and status above are checked through 5 September 2026.
