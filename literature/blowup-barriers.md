# Blowup routes and barriers for 3D Navier–Stokes

Scope: the incompressible equations with viscosity normalized to one,
\[
 \partial_tu+u\!\cdot\!\nabla u+\nabla p=\Delta u,\qquad \nabla\!\cdot u=0,
\]
usually on \(\mathbb R^3\).  The statements below concern particular classes of
solutions or particular blowup geometries.  They do not settle the Clay problem
for arbitrary smooth finite-energy data.  Sources and status are checked as of
2026-09-05.

## 1. The scaling gap in the energy route

The Navier–Stokes scaling is
\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),\qquad
 p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t).
\]
Thus \(\|u_\lambda(t)\|_{L^q}=\lambda^{1-3/q}\|u(\lambda^2t)\|_{L^q}\); \(L^3_x\) is
critical, while the kinetic energy \(\|u\|_2^2\) scales as \(\lambda^{-1}\) and is
supercritical.  Under concentration to smaller scales (\(\lambda\to\infty\)),
the rescaled kinetic energy can therefore tend to zero while a critical norm
such as \(\|u\|_{L^3(\mathbb R^3)}\) remains unchanged.
The Leray–Hopf inequality gives only
\[
 u\in L^\infty_tL^2_x\cap L^2_t\dot H^1_x,
\]
which is exactly the energy-level a priori control and does not bound a
scale-critical quantity such as \(L^\infty_tL^3_x\), nor the higher norms needed
to continue a classical solution.  This is a structural obstruction to closing
the energy estimate, not evidence that blowup occurs.

The scale-critical regularity theorem of Escauriaza–Seregin–Šverák (ESS) says
that a suitable weak Cauchy solution on \(\mathbb R^3\times(0,T)\) with
\(\sup_{0<t<T}\|u(t)\|_{L^3(\mathbb R^3)}<\infty\) is smooth up to \(T\).  Their
argument uses local energy estimates, epsilon regularity, and backward
uniqueness for a parabolic equation; it does not produce the required uniform
critical bound from the energy inequality.  The original paper is
[ESS, *L_{3,∞}-solutions ... and backward uniqueness*, Russian Math. Surveys
58 (2003), 211–250](https://www.mathnet.ru/eng/rm609), DOI
[10.1070/RM2003v058n02ABEH000609](https://doi.org/10.1070/RM2003v058n02ABEH000609).

## 2. Tao's averaged-equation blowup: a warning about what energy permits

Tao considers on \(\mathbb R^3\) an equation
\(\partial_tu=\Delta u+\widetilde B(u,u)\), where \(\widetilde B\) is an
average of the Navier–Stokes bilinear operator over rotations, order-zero
Fourier multipliers (and, in the final version, dilations).  It preserves
divergence-free fields and the cancellation
\(\langle\widetilde B(u,u),u\rangle=0\), hence the usual energy identity.
Analysis of a related ODE gives a smooth finite-time blowup solution of this
averaged equation.  See [Tao, *Finite time blowup for an averaged
three-dimensional Navier-Stokes equation*, JAMS 29 (2016)](https://arxiv.org/abs/1402.0290)
and the [journal version](https://www.ams.org/jams/2016-29-03/S0894-0347-2015-00838-4/).

The result isolates the insufficiency of cancellation, energy, and broad
harmonic-analysis estimates: those features are shared by the averaged model.
It is not a blowup construction for the true Navier–Stokes operator.  The
averaging changes the triadic interaction geometry, so transferring its ODE
mechanism to \(B(u,u)\) remains an additional, unproved step.

## 3. Self-similar and discretely self-similar routes

The Leray backward self-similar ansatz near \((x_0,T)\) is
\[
 u(x,t)=(T-t)^{-1/2}U\!\left((x-x_0)/(T-t)^{1/2}\right).
\]
It reduces the PDE to a stationary profile equation.  Nečas–Růžička–Šverák
proved that the only profile in \(L^3(\mathbb R^3)\) is zero; Tsai extended
nonexistence to broader assumptions.  See [Nečas, Růžička and Šverák, *On
Leray's self-similar solutions of the Navier–Stokes equations*, Acta Math. 176
(1996), 283–294](https://doi.org/10.1007/BF02551584).  Tsai proved
nonexistence of nontrivial profiles under additional decay or
local-energy assumptions; Tsai's formulation, for example, rules out profiles
in \(L^q(\mathbb R^3)\) for \(q>3\) and profiles satisfying the relevant bounded
local-energy condition.  See [Tsai, *On Leray's self-similar solutions ...
satisfying local energy estimates*, Arch. Rational Mech. Anal. 143 (1998),
29–51](https://doi.org/10.1007/s002050050091).

These theorems exclude an exactly self-similar profile in their stated class;
they do not exclude type-II, oscillatory, multi-scale, or non-self-similar
singularity formation.  For a local asymptotic version, [Chae and Wolf,
*Removing discretely self-similar singularities ...*](https://arxiv.org/abs/1610.09464)
show that a discretely self-similar possible singularity has only one singular
point, and remove it when the scaling parameter \(\lambda\) is sufficiently
near 1.  The conclusion is correspondingly restricted to the DSS hypotheses
and near-one scale ratio.

## 4. Blowup limits, ancient solutions, and concentration compactness

Parabolic rescaling about a hypothetical singular point can yield a bounded
ancient solution on \(\mathbb R^3\times(-\infty,0]\), provided one has the
local bounds and compactness needed for a suitable/mild limit.  A Liouville
theorem saying that every such limit is zero (or regular) would be a powerful
rigidity result.  The difficulty is that compactness is not automatic at the
critical scale: translations, dilations, and profiles can escape; local weak
convergence can lose concentration; and pressure and suitability must be passed
to the limit.  Even a nonzero ancient limit is a conditional consequence of a
carefully normalized blowup sequence, not a classification of all possible
singularities.

The critical-element route makes this precise.  Gallagher–Koch–Planchon prove
that strong solutions bounded in \(L^\infty_tL^3_x(\mathbb R^3)\) do not become
singular, and construct a profile decomposition in critical Besov spaces.  In
their conditional minimization statement, if singularity-producing data exist
in the relevant critical class, their method gives a minimal-norm critical
element; the bounded-\(L^3\) case is then ruled out by the regularity theorem.
What remains for arbitrary finite-energy data is obtaining any uniform bound in
a critical space to which that framework applies.  See [Gallagher, Koch and Planchon,
*A profile decomposition approach ...*](https://arxiv.org/abs/1012.0145),
Math. Ann. 355 (2013), 1527–1559.  Thus the result is a conditional critical
space reduction, not global regularity from the energy class: the missing input
is uniform critical control for arbitrary finite-energy evolutions.

## 5. Vorticity-direction (geometric depletion) criteria

Writing \(\omega=\nabla\times u\), the vorticity equation contains the stretching
term \((\omega\cdot\nabla)u=S\omega\).  Alignment of nearby vorticity
directions reduces the singular kernel in the Biot–Savart representation.
Constantin–Fefferman prove the following representative whole-space criterion:
for a weak solution on \(\mathbb R^3\times(0,T)\) with divergence-free
\(u_0\in H^1(\mathbb R^3)\), if, for almost every \(t\),
\[
 \sin\theta(x,y,t)\le c|x-y|\quad\text{for a.e. }x,y,
\]
where \(\theta\) is the angle between the two nonzero vorticity directions,
then the solution is strong on \([0,T]\), hence regular.  A later theorem in
the same line replaces the Lipschitz modulus by a \(1/2\)-Hölder modulus (with
the stated time-space integrability of the coefficient).  See [Constantin and
Fefferman, *Direction of vorticity and the problem of global regularity*,
Indiana Univ. Math. J. 42 (1993), 775–789](https://web.math.princeton.edu/~const/niD.pdf),
which records the hypotheses and theorem, and the [journal listing](https://iumj.org/article/3627/).

This is a strong conditional regularity mechanism, not a proof that arbitrary
solutions have coherent vorticity.  It also depends on the domain and boundary
conditions; extensions may require slip/free-boundary assumptions, and the
standard no-slip boundary problem is materially different.  Consequently it
cannot be promoted to a full Clay solution without deriving the geometric
modulus from the energy-level hypotheses.

## Scope of the barriers

Together, the results constrain several attractive blowup pictures: energy
alone leaves a supercritical gap; energy-preserving averaged dynamics can still
blow up; exact or mildly discrete self-similarity is heavily restricted; and
critical compactness and vorticity geometry give conditional reduction or
regularity theorems.  None supplies a priori control or a rigidity theorem for
all smooth finite-energy 3D Navier–Stokes evolutions on the Clay domains.
