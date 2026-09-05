# Navier–Stokes foundations and the Clay target

This dossier is for a reader checking the exact mathematical target before using any regularity argument. It records the official Clay formulation and the classical results that sit immediately below it. The status date is 2026-09-05. Nothing here claims a solution of the Millennium problem.

## The equation and the two Clay alternatives

The official statement uses the incompressible Navier–Stokes system on ℝ^n, with (n=3) for the prize problem,

\[
 \partial_t u_i+\sum_j u_j\partial_{x_j}u_i
 = \nu\Delta u_i-\partial_{x_i}p+f_i,
 \qquad \operatorname{div}u=0,
 \qquad u(x,0)=u_0(x),
\]

where ν>0 is fixed, (u) is velocity, (p) pressure, and (f) an imposed force. The official source is Charles Fefferman's chapter in the Clay Mathematics Institute volume, [*Existence and Smoothness of the Navier–Stokes Equation* (PDF)](https://www.claymath.org/library/monographs/MPPc.pdf), pp. 57–68. The displayed equations and hypotheses are on PDF pages 63–64 (printed pages 57–59).

For the whole-space alternative, Fefferman assumes (u_0) is smooth and divergence free and, for every multi-index α and every (K>0),

\[
 |\partial_x^\alpha u_0(x)|\le C_{\alpha K}(1+|x|)^{-K} \quad (x\in\mathbb R^3).
\]

The force hypothesis is quantified more strongly: for every α, every integer (m\ge0), and every (K>0),

\[
 |\partial_x^\alpha\partial_t^m f(x,t)|
 \le C_{\alpha m K}(1+|x|+t)^{-K}
 \quad ((x,t)\in\mathbb R^3\times[0,\infty)).
\]

Thus “rapid decay” means a separate constant (C_{\alpha m K}) for each derivative order and each requested power (K); it is not one fixed decay exponent. A physically reasonable solution is required to have (p,u\in C^\infty(\mathbb R^3\times[0,\infty))) and bounded kinetic energy ∫|u(x,t)|²dx<C for every (t\ge0). In the positive prize alternatives (A) and (B), the force is set identically to zero; the breakdown alternatives (C) and (D) allow an admissible force satisfying the stated decay or periodicity hypotheses.

The periodic alternative is stated on the flat three-torus (\mathbb R^3/\mathbb Z^3), often abbreviated (T^3). Fefferman first imposes periodicity under each unit translation and assumes (u_0) is smooth and divergence free. Divergence free on (T^3) does not imply zero spatial mean; a constant mean can optionally be removed by a Galilean change of frame, but mean zero is not an official Clay hypothesis. The force, when allowed in the setup, obeys

\[
 |\partial_x^\alpha\partial_t^m f(x,t)|
 \le C_{\alpha m K}(1+|t|)^{-K}
 \quad \text{for every }\alpha,m,K,
\]

and is periodic in space. Alternative (B), the positive periodic statement, takes (f\equiv0) and asks for smooth periodic (p,u) for all (t\ge0). The wording in the PDF labels this domain “(\mathbb R^3/\mathbb Z^3)”; “(T^3)” is notation, not a change of problem.

The requested positive alternatives are therefore:

* **R3 (Clay A):** every admissible smooth divergence-free datum on (\mathbb R^3), with (f=0), has a smooth solution for all (t\ge0) satisfying the bounded-energy condition.
* **T3 (Clay B):** every smooth divergence-free periodic datum on (T^3=\mathbb R^3/\mathbb Z^3), with (f=0), has a smooth periodic solution for all (t\ge0).

The negative alternatives (Clay C and D) ask for one admissible datum and force for which no globally smooth physically reasonable solution exists. The official statement explicitly accepts a proof of any one of the four alternatives, so R3/T3 and their breakdown counterparts are logically separate routes. The source’s equations, quantifiers, and alternatives were inspected directly in the PDF. The Clay landing page and bibliographic records are metadata; they should not be treated as substitutes for those pages.

## Leray–Hopf global weak existence

Jean Leray's foundational paper is [*Sur le mouvement d'un liquide visqueux emplissant l'espace*, Acta Mathematica 63 (1934), 193–248](https://warwick.ac.uk/fac/sci/maths/people/staff/james_robinson/lf/leray.pdf). A searchable scan/translation is also available as [arXiv:1604.02484](https://arxiv.org/abs/1604.02484). Leray constructs a global-in-time generalized (“turbulent” in his terminology) solution for square-integrable initial velocity with weakly zero divergence, together with an energy-control function. The scanned original states the existence theorem near its later pages: arbitrary (L^2) initial velocity with weak divergence zero gives at least one solution defined for all future times, and the dissipation plus kinetic-energy control is non-increasing except at the exceptional singular times in Leray's formulation.

In modern terminology, a Leray–Hopf weak solution on (\mathbb R^3) or (T^3) has the typical regularity

\[
 u\in L^\infty_{\mathrm{loc}}([0,\infty);L^2_\sigma)
 \cap L^2_{\mathrm{loc}}([0,\infty);H^1_\sigma),
\]

satisfies Navier–Stokes distributionally, attains (u_0) weakly (and strongly in (L^2) at the initial time in the standard energy setting), and obeys the global energy inequality

\[
 \frac12\|u(t)\|_2^2+\nu\int_s^t\|\nabla u(\tau)\|_2^2d\tau
 \le \frac12\|u(s)\|_2^2
 +\int_s^t\langle f,u\rangle d\tau
\]

for almost every (s\ge0) and every later (t), with the unforced version obtained by removing the last term. (L^2_\sigma) denotes the divergence-free (L^2) closure; on (T^3), one may choose either the full periodic space or its mean-zero subspace after a Galilean normalization, but mean zero is not part of the Clay statement. This modern package is the Leray–Hopf class; the original 1934 paper predates this exact terminology and notation. Fefferman's Clay chapter directly confirms the relevant bridge: Leray established weak existence in three dimensions with suitable growth properties, while uniqueness of arbitrary weak solutions was not known (pp. 65–66 of the chapter, PDF lines corresponding to 1788–1841).

Weak existence is global in time but does not provide the smoothness required by R3/T3. The energy inequality controls the critical bookkeeping needed for compactness, while the nonlinear term can still prevent a global (H^1) or (L^\infty) bound. The existence of a global Leray–Hopf solution is consequently far weaker than global smooth existence.

## Local strong existence and continuation

For smooth enough three-dimensional data, local strong (and hence classical for positive time) existence follows from the Fujita–Kato theory. The primary bibliographic record is [Fujita and Kato, *On the Navier–Stokes initial value problem. I*, Archive for Rational Mechanics and Analysis 16 (1964), 269–315, DOI 10.1007/BF00276188](https://doi.org/10.1007/BF00276188). The record identifies the result as unique local-in-time three-dimensional solutions and global unique solutions in two dimensions; it is metadata and abstract information, not a direct inspection of every theorem hypothesis.

A conservative integer-order formulation, pending direct inspection of an R3 theorem statement, is: if (u_0\in H^m_\sigma(\mathbb R^3)) with integer (m\ge3), then there is (T=T(\|u_0\|_{H^m})>0) and a unique strong solution on ([0,T)), in a class such as

\[
 u\in C([0,T);H^m)\cap C((0,T);H^{m+2})\cap C^1((0,T);H^m),
\]

For Schwartz data, the local solution is smooth. If (T_*<\infty) is its maximal strong lifespan, continuation fails only when the controlling strong norm becomes unbounded; in particular, a uniform bound in a continuation class extends the solution. A directly inspected author-source formulation is Tao's [254A Notes 1, Theorem 37](https://terrytao.wordpress.com/2018/09/16/254a-notes-1-local-well-posedness-of-the-navier-stokes-equations/), which states local existence and uniqueness for divergence-free H^s data on the torus when s>d/2, with an explicit time lower bound. The same notes state that the R^d analogue follows by repeating the proof, but leave that analogue as an exercise (lines 1057–1062), so they do not close the requested directly inspected R3 premise. The notes also derive smooth pressure and time regularity for classical solutions (lines 1048–1052), in the periodic setting. The exact Fujita–Kato R3 theorem statement and its t=0 pressure formulation therefore remain pending direct inspection.

## Weak–strong uniqueness and Serrin criteria

The regularity/uniqueness mechanism is the Prodi–Serrin criterion. The primary bibliographic records are [Prodi, *Un teorema di unicità per le equazioni di Navier–Stokes* (1959), DOI 10.1007/BF02410664](https://doi.org/10.1007/BF02410664) and [Serrin, *On the interior regularity of weak solutions of the Navier–Stokes equations* (1962), DOI 10.1007/BF00253344](https://doi.org/10.1007/BF00253344). The linked records expose publication data and abstracts; they are metadata sources for this dossier. The theorem below is the standard whole-space/periodic formulation synthesized from these results and the usual energy-difference argument.

Let (u) be a Leray–Hopf solution and let (v) be a strong solution with the same initial data. If, on every finite interval (or on the interval under consideration),

\[
 v\in L^q(0,T;L^p),\qquad \frac{2}{q}+\frac{3}{p}\le1,
 \qquad 3<p\le\infty,
\]

then (u=v) almost everywhere on ([0,T]). The endpoint (p=3,q=\infty) requires care and is generally stated separately; the safe classical criterion uses (p>3), (2/q+3/p\le1), or suitable endpoint refinements. The same Serrin integrability condition on a Leray–Hopf solution implies regularity on the interval. In the proof, the difference (w=u-v) satisfies an energy inequality whose convection term is controlled by the Serrin norm of (v), after which Gronwall gives (w=0).

This result explains the phrase “weak–strong uniqueness”: it does not prove uniqueness among two arbitrary Leray–Hopf solutions. It says that once one solution lies in a regularity class, every energy-class weak solution sharing its data coincides with it for as long as that regular solution exists. Global R3/T3 would require a priori control that keeps a strong solution in such a class for every finite time.

## Caffarelli–Kohn–Nirenberg partial regularity

The primary paper is [Caffarelli, Kohn, and Nirenberg, *Partial regularity of suitable weak solutions of the Navier–Stokes equations*, Communications on Pure and Applied Mathematics 35 (1982), 771–831, DOI 10.1002/CPA.3160350604](https://doi.org/10.1002/CPA.3160350604). The publisher page supplies bibliographic metadata. The Clay chapter reproduces the result in a directly inspected, deliberately rough form: for a suitable weak solution satisfying growth conditions, if (E) is its spacetime singular set, then the parabolic (1)-dimensional Hausdorff measure (P^1(E)=0); it also records existence of a weak solution with those growth conditions for admissible data and force (PDF pp. 66–67).

“Suitable” adds the local energy inequality to the distributional equations and energy-class bounds. CKN then proves that the solution is regular outside a relatively small closed singular set. In the parabolic metric, the singular set has parabolic Hausdorff dimension at most one, in the precise measure formulation (P^1(E)=0). This permits singular points but rules out a spacetime singular set containing a curve of the form (x=\phi(t)) in the sense stated by Fefferman. It is a local partial-regularity theorem, not global smoothness, uniqueness of all weak solutions, or a proof of either Clay alternative.

## Source discipline

The Clay PDF is the authoritative inspected source for the official alternatives, the decay quantifiers, the bounded-energy requirement, and the rough CKN summary. Leray's scan is the inspected primary source for the historical global weak-existence construction. Fujita–Kato, Prodi, Serrin, and CKN links above are primary publication records/DOI destinations; where the full article text was not inspected through the web result, claims are restricted to theorem formulations standardly associated with the cited work and are explicitly identified as such. Search-result snippets, citation counts, and publisher metadata establish identity and provenance only; they do not independently verify a theorem's hypotheses. The open Clay target remains the global smooth R3/T3 assertion (or a permitted breakdown construction) under the exact hypotheses above.
