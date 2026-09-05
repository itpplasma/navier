# Frozen audit of the pressure-critical route

VERDICT: **FAIL WITH SCOPE**

REVIEWED SCOPE: The immutable manuscript at paper commit `d3b60b7`, checked
against evidence commit `f092178`. The audit covers the signed \(L^3\)
pressure balance, regularization and cutoff limits, pressure-absorption
quantifiers, endpoint continuation, viscosity normalization, pressure
smoothness at \(t=0\), and fidelity to Clay alternative A. The paper is
coherent as a conditional argument. It is not a proof of alternative A.

FIRST BAD BRIDGE: The first new implication required for an unconditional
result is Hypothesis 4.2:

\[
 \int_0^\tau P_3(t)\,dt
 \leq \theta\nu\int_0^\tau D_3(t)\,dt
 +\nu^3F\!\left(\nu^{-1}\|u_0\|_3\right).              \tag{PA}
\]

It is asserted for every admissible datum and every \(0<\tau<T_*\), with one
universal \(\theta<1\) and finite \(F\). The manuscript correctly labels (PA)
as unproved and supplies no argument for it. Energy, enstrophy,
Calderón--Zygmund estimates, and compactness do not establish its signed,
trajectory-independent remainder. Thus no full Navier--Stokes proof is
present. This is an open lemma, not a small omitted estimate.

EVIDENCE:

1. **The pressure balance has the correct sign and coefficients.** For
   \(r=|u|\), testing against \(ru\) gives

   \[
    \int u_t\cdot ru=\frac13\frac d{dt}\int r^3,\qquad
    \int (u\cdot\nabla)u\cdot ru
      =\frac13\int u\cdot\nabla r^3=0,
   \]

   \[
    \int \nabla p\cdot ru=-\int p\,u\cdot\nabla r,
   \]

   and

   \[
    -\int\Delta u\cdot ru
      =\int \left(r|\nabla u|^2+r|\nabla r|^2\right).
   \]

   Hence
   \[
    \frac13\frac d{dt}\|u\|_3^3+\nu D_3=P_3,\qquad
    P_3=\int p\,u\cdot\nabla|u|,
   \]
   exactly as stated.

2. **The zero set can be handled rigorously, although the manuscript
   compresses the domination argument.** Let
   \(r_\varepsilon=(|u|^2+\varepsilon)^{1/2}\) and test against
   \(r_\varepsilon u\). The time primitive must be
   \[
    H_\varepsilon(u)=\frac13
      \left((|u|^2+\varepsilon)^{3/2}-\varepsilon^{3/2}\right).
   \]
   Subtracting the constant is necessary on \(\mathbb R^3\). The diffusion
   term is
   \[
    \int\left(r_\varepsilon|\nabla u|^2
      +\frac{|u|^2}{r_\varepsilon}|\nabla|u||^2\right),
   \]
   and
   \[
    \operatorname{div}(r_\varepsilon u)
      =\frac{|u|}{r_\varepsilon}\,u\cdot\nabla|u|.
   \]
   The bounds \(|u|^2/r_\varepsilon\le |u|\),
   \(|u|/r_\varepsilon\le1\), and
   \(|\nabla|u||\le|\nabla u|\) give dominated convergence. A Sobolev
   representative has \(\nabla|u|=0\) almost everywhere on the zero set, so
   defining the limiting second integrand as zero there is consistent.

3. **The cutoff terms are integrable without assuming persistent Schwartz
   decay.** On a compact interval inside \([0,T_*)\), strong Sobolev bounds
   give \(u\in L^2\cap L^6\), hence \(u\in L^3\cap L^4\), and
   \(\nabla u\in L^2\). Since \(p=R_iR_j(u_i u_j)\), Calderón--Zygmund gives
   \(p\in L^2\cap L^3\). Therefore
   \[
    p|u|^2,\quad |u|^2|\nabla u|,\quad |u|^4,\quad
    p|u||\nabla u|\in L^1.
   \]
   These dominate the cutoff errors and the main pressure-work term. Errors
   containing \(\nabla\chi_R\) vanish by tail integrability and their
   \(R^{-1}\) factor. The manuscript's cutoff claim is valid, but a final
   proof should display these estimates.

4. **Pressure normalization is correct.** Divergence gives
   \(-\Delta p=\partial_i\partial_j(u_i u_j)\). With
   \(\widehat{R_i f}=-i\xi_i|\xi|^{-1}\widehat f\), this is
   \(p=R_iR_j(u_i u_j)\), up to a spatial constant depending on time. Such a
   constant does not change \(P_3\), since
   \(\int\operatorname{div}(|u|u)=0\).

5. **(PA) implies the critical bound.** Integration gives
   \[
    \|u(\tau)\|_3^3
    +3(1-\theta)\nu\int_0^\tau D_3
    \le \|u_0\|_3^3+3\nu^3F(\nu^{-1}\|u_0\|_3).
   \]
   Taking the supremum over \(\tau<T_*\) proves Hypothesis 5.2 with the
   manuscript's \(\Phi_\nu\). There is no circular dependence on the unknown
   critical supremum in (PA).

6. **The quantifiers in (PA) are sufficient but unnecessarily restrictive.**
   The terminal argument does not need a universal global remainder depending
   only on \(\|u_0\|_3\). A minimal finite-horizon replacement is:
   \[
   \begin{split}
    &\text{for every }\nu>0,\ u_0\in\mathcal S_\sigma(\mathbb R^3),
      \text{ and }H<\infty,\\
    &\text{there is an explicitly prescribed }A(\nu,u_0,H)<\infty
      \text{ and }\theta(\nu,u_0,H)\le1\text{ such that}\\
    &\quad \int_0^\tau P_3\le
      \theta(\nu,u_0,H)\nu\int_0^\tau D_3+A(\nu,u_0,H)\\
    &\hspace{28mm}\text{for every }0<\tau<\min\{T_*,H\}.
                                                               \tag{PA-H}
   \end{split}
   \]
   Here \(A\) must be computed from \(\nu,H\) and explicitly named initial-data
   norms or seminorms; it may not be defined through the solution trajectory,
   \(T_*\), or the unknown critical supremum. Without that requirement, mere
   existential dependence on \(u_0\) would be vacuous because the trajectory
   is itself determined by \(u_0\). If \(T_*<\infty\), choose \(H>T_*\). Then
   \(\sup_{t<T_*}\|u(t)\|_3^3\le\|u_0\|_3^3+3A(\nu,u_0,H)\), enough for
   continuation. Strict \(\theta<1\) is needed only for positive
   \(D_3\)-control; \(\theta\le1\) suffices for critical control. Thus (PA-H)
   repairs the formulation of the minimum open obligation, but does not prove
   it. The global \(L^3\)-only (PA) remains a legitimate stronger programme.

7. **The endpoint source has the claimed whole-space strong-solution scope.**
   Gallagher--Koch--Planchon, arXiv:1012.0145v3, Theorem 4, states for every
   \(u_0\in L^3(\mathbb R^3)\) that boundedness of the maximal strong solution
   in \(L^\infty([0,T^*);L^3)\) implies \(T^*=\infty\). The source defines
   \(NS(u_0)\) as the local strong/mild solution and records time continuity
   in \(L^3\). It attributes the original endpoint result to
   Escauriaza--Seregin--Šverák and explains that \(L_{3,\infty}\) denotes the
   time-space class used there, not spatial weak \(L^3\). See the primary
   author source, [Theorem 4 and its setup](https://arxiv.org/html/1012.0145#S3.SS1).
   Schwartz data lie in \(L^3\); uniqueness and persistence identify the
   classical branch with this maximal \(L^3\) branch.

8. **The omitted viscosity normalization is exactly repairable.** GKP use
   viscosity one, while the manuscript fixes arbitrary \(\nu>0\). Define
   \[
    v(x,s)=\nu^{-1}u(x,s/\nu),\qquad
    q(x,s)=\nu^{-2}p(x,s/\nu).
   \]
   Then \(v_s+(v\cdot\nabla)v+\nabla q=\Delta v\), its maximal time is
   \(S_*=\nu T_*\), and
   \(\|v(s)\|_3=\nu^{-1}\|u(s/\nu)\|_3\). The GKP hypothesis follows from a
   finite uniform bound for \(u\); \(S_*=\infty\) then gives \(T_*=\infty\).
   This fully repairs the omission. It also explains the factors in (PA):
   unit-viscosity pressure absorption for \(v\) transforms into the displayed
   \(\nu^3F(\nu^{-1}\|u_0\|_3)\) estimate for \(u\).

9. **The terminal contradiction is valid after normalization.** If
   \(T_*<\infty\), Hypothesis 5.2, or (PA-H) with \(H>T_*\), bounds
   \(\sup_{t<T_*}\|u(t)\|_3\). The normalized endpoint theorem forces
   \(T_*=\infty\), a contradiction. The solution is global, and energy gives
   the single uniform kinetic-energy constant required by Clay A.

10. **Smooth pressure at the initial time is supported by a direct primary
    source.** For Schwartz \(u_0\),
    \(\partial_i\partial_j(u_{0i}u_{0j})\) is smooth and rapidly decreasing.
    Newtonian inversion, equivalently the Riesz formula modulo a
    time-dependent constant, gives smooth spatial pressure at \(t=0\).
    Tao's whole-space local well-posedness theorem gives existence and
    uniqueness of an \(H^1\) mild solution and states that Schwartz data make
    both \(u\) and \(p\) smooth, with all time derivatives bounded in every
    spatial Sobolev norm through \(t=0\): [Tao, Theorem 5.4(ii)--(iv)](https://msp.org/apde/2013/6-1/apde-v6-n1-p02-s.pdf#page=29).
    This also avoids a false persistence premise: the same primary paper
    explicitly observes that incompressible evolution need not preserve
    Schwartz decay. The manuscript uses compact-interval Sobolev bounds, not
    persistent rapid decay, in its integrations by parts.

11. **The target matches Clay alternative A.** The equation is unforced on
    \(\mathbb R^3\), \(\nu>0\) is arbitrary, and the datum is smooth,
    divergence free, and rapidly decreasing. The conclusion supplies global
    smooth \(u,p\) and a time-uniform finite kinetic-energy bound. No periodic,
    forced, weak, averaged, or modified equation is substituted.

REPLACEMENT ARGUMENT: Items 2--3 complete the formal pressure balance. Item 8
repairs the unit-viscosity endpoint application. Replacing (PA) by (PA-H)
repairs the overrestrictive statement of the minimum open hypothesis, but
cannot turn it into a theorem because (PA-H) remains unproved.

CONDITIONAL SUFFIX THAT SURVIVES: Assuming (PA) or (PA-H), the exact balance
yields a uniform \(L^3\) bound up to any putative finite maximal time. After
viscosity normalization, GKP Theorem 4 rules out that finite time. Standard
persistence, elliptic pressure recovery, and energy then give the conditional
Clay A conclusion.

UNNECESSARY DEPENDENCIES: Positive dissipation with \(\theta<1\) is not needed
for endpoint continuation; \(\theta\le1\) suffices. The cubic enstrophy
inequality, scalar ODE example, and compactness discussion are not used in
\((\mathrm{PA})\Rightarrow L^\infty_tL^3_x\Rightarrow\) continuation. They
explain failed alternatives but are dispensable from the conditional theorem.

NON-CLAIMS: This audit finds no Navier--Stokes blowup and no global regularity
proof. It does not infer (PA) from pressure balance, absolute-value estimates,
energy, enstrophy, or compactness. It does not treat the periodic alternative
or either breakdown alternative.

REOPENING CONDITION: Reopen the terminal proof only after (PA-H), or another
a priori estimate yielding a finite \(L^3\) supremum up to every putative
finite \(T_*\), is proved for every unforced whole-space Schwartz datum without
dependence on the unknown critical supremum or a higher continuation norm.
That lemma needs an independent audit at frozen revisions. The manuscript
should cite the directly verified whole-space local regularity source when it
states smoothness of pressure through the initial time.
