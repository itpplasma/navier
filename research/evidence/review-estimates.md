# Frozen independent audit of estimates and compactness

**VERDICT: REPAIR.**  The mathematical estimates and conditional compactness
claims in the reviewed scope are correct.  One sentence in the enstrophy
evidence implicitly treats rapid spatial decay as available throughout the
maximal classical evolution from Schwartz data.  That persistence is neither
proved nor needed.  The exact repair is to formulate the integrations for the
strong Sobolev solution and justify them by spatial cutoffs and regularization,
as the manuscript itself already does.

## Reviewed scope and frozen inputs

The review used these immutable inputs:

* paper repository `/home/ert/proj/navier-paper`, exact commit `d3b60b7`,
  file `main.tex`;
* evidence repository `/home/ert/proj/navier`, exact commit `f092178`, files
  `research/evidence/enstrophy.md` and
  `research/evidence/compactness.md`.

The authored pressure-balance and pressure-absorption route was excluded from
this audit.  In `main.tex`, the reviewed mathematical scope is the energy
identity, scaling and interpolation calculation, enstrophy inequality, scalar
ODE obstruction, and the qualitative compactness section.  In the evidence,
the small-data enstrophy argument and the complete compactness note were
reviewed.

## First bad bridge

The first unsupported phrasing occurs in the opening of `enstrophy.md`:

> suppose initially that \(u\) is a smooth solution whose spatial derivatives
> decay sufficiently rapidly ... This is the relevant calculation on the
> maximal classical interval arising from ... Schwartz data.

Schwartz initial data do not by that sentence alone establish persistence of
rapid decay for every derivative throughout the maximal interval.  Pressure
is nonlocal, so this should not be left implicit.  No displayed estimate needs
that claim.

## Replacement argument

Fix \(0<T<T_*\).  The local strong solution from Schwartz data has, for a
sufficiently large integer \(m\), uniform Sobolev regularity on \([0,T]\),
and parabolic smoothing supplies the additional derivatives used at positive
times.  Insert a cutoff \(\chi_R(x)=\chi(x/R)\) in each energy or enstrophy
pairing.  The principal terms converge by the available \(L^2\)-Sobolev
bounds; cutoff-error terms contain a factor \(R^{-1}\) or \(R^{-2}\) and
vanish by Hölder, Sobolev, and absolute continuity of the relevant integrals.
At zeros of quantities used in nonlinear test functions, regularize first and
then pass to the limit.  Therefore all identities hold on \([0,T]\), and
since \(T<T_*\) was arbitrary, on the maximal interval.  Replace the quoted
opening by this Sobolev-cutoff formulation.  This repairs the only issue
without strengthening the data or changing any conclusion.

## Reconstructed estimate checks

For the energy identity, pairing with \(u\) gives

\[
 \frac12\frac d{dt}\|u\|_2^2+\nu\|\nabla u\|_2^2=0.
\]

The convection term is \(\frac12\int u\cdot\nabla|u|^2=0\), and the pressure
term is \(-\int p\,\operatorname{div}u=0\).  The manuscript's signs and the
factor \(2\nu\) in the integrated form are correct.

Under \(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\),
\(\|u_\lambda\|_q=\lambda^{1-3/q}\|u\|_q\).  In particular, \(L^3_x\) is
critical and squared energy scales as \(\lambda^{-1}\).  Interpolation gives

\[
 \|u\|_3^4\leq C\|u\|_2^2\|\nabla u\|_2^2,
\]

so energy yields \(L^4_tL^3_x\), whose Serrin scaling index is
\(2/4+3/3=3/2>1\).  The manuscript correctly calls it supercritical and
correctly refuses to infer a time supremum.

Pairing with \(-\Delta u\), including the sign from moving the nonlinear
term, yields

\[
 \frac12Y'+\nu\|\Delta u\|_2^2
 =\int (u\cdot\nabla)u\cdot\Delta u,
 \qquad Y=\|\nabla u\|_2^2.
\]

The chain

\[
 \|u\|_6\|\nabla u\|_3\|\Delta u\|_2
 \leq C Y^{3/4}\|\Delta u\|_2^{3/2}
 \leq \frac\nu2\|\Delta u\|_2^2+C\nu^{-3}Y^3
\]

uses the correct Gagliardo--Nirenberg exponents and Young conjugates
\(4/3,4\).  The vorticity derivation in the evidence gives the same powers:
with \(X=\|\nabla\omega\|_2^2\), the stretching term is bounded by
\(CY^{3/4}X^{3/4}\).  Plancherel justifies
\(\|D^2u\|_2=\|\Delta u\|_2=\|\nabla\omega\|_2\) for divergence-free fields
with the full-Hessian norm convention used there.

The scalar function \(y(t)=(2C(T-t))^{-1/2}\) satisfies \(y'=Cy^3\), diverges
at \(T\), and has integral \(\sqrt{2T/C}\).  It proves only the stated
logical insufficiency of an \(L^1_t\) bound plus the cubic differential upper
inequality; the manuscript does not present it as a Navier--Stokes model.

## Small-data enstrophy check

The evidence obtains

\[
 \frac12Y'+(\nu-C_A\|u\|_3)X\leq0,
 \qquad \|u\|_3\leq C_I E^{1/4}Y^{1/4}.
\]

If \(C_AC_I[E(0)Y(0)]^{1/4}<\nu\), the bootstrap region \(Y\leq Y(0)\),
together with \(E\leq E(0)\), makes the dissipation coefficient at least
\(\delta=\nu-C_AC_I[E(0)Y(0)]^{1/4}>0\).  Then \(Y'\leq0\) closes the region
by continuity and integration gives

\[
 \int_0^T X\,dt\leq \frac{Y(0)}{2\delta}.
\]

Uniform \(H^1\) control is a sufficient continuation norm for this strong
solution.  The product \(EY/\nu^4\) is scale invariant.  Thus the evidence
proves the stated restrictive small-data result and does not extend it to
arbitrary energy data.

## Compactness check

The rescaling identities in `compactness.md` are correct.  The local kinetic
energy and dissipation each acquire \(r^{-1}\), while the spacetime cubic
velocity and \(3/2\)-pressure terms acquire \(r^{-2}\).  Hence the quantities
\(A,E,C,D\) defined there are invariant.  The global energy inequality gives
upper bounds proportional to \(r^{-1}\), which diverge at small scales and do
not supply the desired compactness.

The alternative amplitude \(r^{3/2}\) preserves global \(L^2\), but after
the stated time-space rescaling its nonlinear coefficient is \(r^{-1/2}\).
It therefore does not produce a sequence solving one fixed Navier--Stokes
equation.

The point-picking construction has the required hypotheses: a bounded-data
whole-space mild solution, finite maximal time, and the standard
\(L^\infty\) continuation criterion, which forces the record amplitudes
\(M_k\to\infty\).  Record-time choice gives \(|v_k|\leq\gamma_k\) for all
rescaled past times, while choosing spatial near-maximizers and
\(\gamma_k\downarrow1\) gives a nonzero normalized limit.  Since
\(M_k^2t_k\to\infty\), the domains exhaust \(( -\infty,0]\).  The conclusion
is exactly a nonzero bounded ancient mild solution.  No global energy, spatial
decay, terminal zero trace, or global suitability is inherited.

At the same scale,

\[
 \int_{B_R}|v_k|^2=M_k\int_{B_{R/M_k}}|u|^2
 \leq M_k\|u_0\|_2^2,
\]

so the upper bound diverges.  The lower concentration estimate of order
\(M_k^{-1}\) tends to zero and is compatible with finite energy.  Constant
nonzero vector fields are valid bounded ancient mild, locally suitable
solutions and correctly falsify any rigidity statement lacking an additional
condition that excludes them.

For the suitable-limit route, the evidence states sufficient hypotheses
rather than claiming they follow from energy.  On each fixed cylinder it
requires uniform local \(L^\infty_tL^2_x\), \(L^2_tH^1_x\),
\(L^3_{t,x}\), and pressure \(L^{3/2}_{t,x}\) bounds, plus the local energy
inequality.  The equation then bounds a negative-Sobolev time derivative;
Aubin--Lions gives strong local \(L^2\), and interpolation with the uniform
energy-class \(L^{10/3}\) bound gives strong local \(L^3\) after taking a
subsequence.  This is enough for the quadratic nonlinearity; weak lower
semicontinuity and pressure convergence give the standard passage of the
local energy inequality.  A separate epsilon-regularity lower bound is
correctly required to prevent a zero limit.  These upper compactness and
lower nontriviality hypotheses are not derived from global energy.

## Conditional suffix that survives

After the wording repair, all reviewed estimates survive.  They establish:

* energy-level control and the supercritical \(L^4_tL^3_x\) consequence;
* the local cubic enstrophy upper inequality and the scalar obstruction;
* global continuation under the explicit scale-invariant smallness condition;
* conditionally, finite-time breakdown implies a nonzero bounded ancient mild
  solution by point-picking;
* conditionally, the stronger scale-invariant local compactness package plus
  epsilon nontriviality produces a nonzero suitable ancient limit.

They do not supply an arbitrary-data critical bound or a general rigidity
theorem for three-dimensional bounded ancient solutions.

## Unnecessary dependencies

The enstrophy and small-data calculations need no Schwartz-persistence claim,
no ESS theorem, and no compactness machinery.  The scalar obstruction needs
no PDE existence theorem.  The point-picking ancient-limit reduction needs
bounded mild-solution continuation and interior compactness, but not global
finite energy.  The suitable-limit route needs the displayed local bounds and
epsilon regularity, but not the point-picking normalization.

## Non-claims and reopening condition

This review does not audit the pressure route, the exact bibliographic text of
ESS/GKP/KNSS/CKN, the manuscript's terminal pressure regularity at \(t=0\), or
the full Clay implication.  It is a mathematical audit of the listed
manuscript-owned calculations and compactness logic, not source verification.

The repair can be promoted once the opening decay sentence in the enstrophy
evidence is replaced by the cutoff/regularization argument above.  A general
compactness closure can be reopened only after an inherited scale-invariant
quantity is proved to provide both the required local upper bounds and a
condition excluding constants (and all other admissible nonzero ancient
limits).
