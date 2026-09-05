# Enstrophy, vortex stretching, and the energy-level obstruction

This note is written for a mathematical referee checking exactly what the
classical enstrophy method proves for the unforced incompressible
Navier--Stokes equation on \(\mathbb R^3\).  Let

\[
 \partial_tu+(u\mathbin\cdot\nabla)u+\nabla p=\nu\Delta u,
 \qquad \nabla\mathbin\cdot u=0,
 \qquad \nu>0,
\]

and let \(u\) be the strong Sobolev solution arising from smooth
divergence-free Schwartz data. On each compact interval before its maximal
time, use sufficiently high Sobolev bounds and positive-time smoothing.
Insert spatial cutoffs \(\chi(x/R)\) in the pairings below; Hölder and Sobolev
estimates make the errors containing \(R^{-1}\) or \(R^{-2}\) vanish as
\(R\to\infty\). Regularize nonlinear tests when needed, then take their
limit. No persistence of Schwartz spatial decay is assumed. Set

\[
 E(t)=\|u(t)\|_{L^2}^2,\qquad
 \omega=\nabla\times u,\qquad
 Y(t)=\|\omega(t)\|_{L^2}^2,
 \qquad X(t)=\|\nabla\omega(t)\|_{L^2}^2.
\]

All unlabelled norms below are over \(\mathbb R^3\).  Constants denoted by
\(C\) are universal and may change from line to line.  Their values depend
only on the stated Sobolev, Gagliardo--Nirenberg, and Calderón--Zygmund
inequalities, never on the solution, time, or viscosity.

## Exact energy and enstrophy identities

Taking the \(L^2\) inner product of the velocity equation with \(u\) gives

\[
 \frac12E'(t)+\nu\|\nabla u(t)\|_2^2=0.
\]

Indeed, incompressibility and decay give

\[
 \int_{\mathbb R^3}(u\mathbin\cdot\nabla)u\mathbin\cdot u\,dx
 =\frac12\int_{\mathbb R^3}u\mathbin\cdot\nabla|u|^2\,dx=0,
 \qquad
 \int_{\mathbb R^3}\nabla p\mathbin\cdot u\,dx=0.
\]

The Fourier identity

\[
 \|\nabla u\|_2^2=\|\nabla\times u\|_2^2+
 \|\nabla\mathbin\cdot u\|_2^2
\]

therefore yields the exact energy law

\[
 \boxed{\frac12E'(t)+\nu Y(t)=0},\qquad
 \boxed{E(t)+2\nu\int_0^tY(s)\,ds=E(0)}.                 \tag{1}
\]

Taking curl of the equation gives

\[
 \partial_t\omega+(u\mathbin\cdot\nabla)\omega
 -(\omega\mathbin\cdot\nabla)u=\nu\Delta\omega.
\]

Pairing this equation with \(\omega\), the transport term vanishes by the
same divergence calculation.  Consequently

\[
 \boxed{\frac12Y'(t)+\nu X(t)
 =\int_{\mathbb R^3}\omega_i\,\partial_i u_j\,\omega_j\,dx
 =\int_{\mathbb R^3}(S\omega)\mathbin\cdot\omega\,dx}, \tag{2}
\]

where \(S=(\nabla u+\nabla u^{T})/2\).  The antisymmetric part of
\(\nabla u\) contributes zero to the quadratic form.  Equation (2) isolates
the vortex-stretching term: unlike transport, pressure, and viscosity, it has
no sign.

For later use, testing the velocity equation against \(-\Delta u\) gives the
equivalent identity

\[
 \frac12Y'(t)+\nu\|\Delta u(t)\|_2^2
 =\int_{\mathbb R^3}(u\mathbin\cdot\nabla)u\mathbin\cdot\Delta u\,dx. \tag{3}
\]

There is no mismatch between (2) and (3): for divergence-free decaying
fields, Fourier calculation gives
\(\|\Delta u\|_2=\|\nabla\omega\|_2\), so the dissipation in (3) is \(X\).

## The cubic differential inequality

The strain is an order-zero singular integral of vorticity.  Thus, for
\(1<p<\infty\), the Calderón--Zygmund estimate gives
\(\|S\|_p\le C_p\|\omega\|_p\).  Hölder's inequality at \(p=3\) and the
three-dimensional Gagliardo--Nirenberg inequality then give

\[
 \left|\int(S\omega)\mathbin\cdot\omega\,dx\right|
 \le \|S\|_3\|\omega\|_3^2
 \le C\|\omega\|_3^3
 \le C Y^{3/4}X^{3/4}.                                 \tag{4}
\]

The last step uses
\(\|\omega\|_3\le C\|\omega\|_2^{1/2}
\|\nabla\omega\|_2^{1/2}\).  Young's inequality with conjugate exponents
\(4/3\) and \(4\), with the scaling parameter chosen to absorb half the
viscous term, yields

\[
 C Y^{3/4}X^{3/4}\le \frac\nu2X+C_0\nu^{-3}Y^3.         \tag{5}
\]

Combining (2) and (5), multiplying by two, and enlarging the universal
constant produces

\[
 \boxed{Y'(t)\le C_1\nu^{-3}Y(t)^3}.                    \tag{6}
\]

This derivation is independent of the velocity-form estimate from (3):

\[
 \begin{aligned}
 \left|\int(u\mathbin\cdot\nabla)u\mathbin\cdot\Delta u\,dx\right|
 &\le \|u\|_6\|\nabla u\|_3\|\Delta u\|_2\\
 &\le C\|\nabla u\|_2
       \bigl(\|\nabla u\|_2^{1/2}\|D^2u\|_2^{1/2}\bigr)
       \|\Delta u\|_2\\
 &\le C Y^{3/4}X^{3/4}.
 \end{aligned}                                           \tag{7}
\]

Here \(\|D^2u\|_2=\|\Delta u\|_2=X^{1/2}\) by Plancherel, while
\(\|\nabla u\|_2=Y^{1/2}\).  Thus (7) reproduces (6) without invoking the
strain representation.

Where the denominator is positive, comparison with \(z'=C_1\nu^{-3}z^3\)
gives only

\[
 Y(t)\le
 \frac{Y(0)}{\sqrt{1-2C_1\nu^{-3}Y(0)^2t}}.             \tag{8}
\]

The right side ceases to be informative at a finite time.  An upper
differential inequality whose comparison function blows up neither proves
that \(Y\) blows up nor supplies a bound after that time.  It is a local
a priori estimate.

## Scaling and concentration prevent an energy-only closure

For fixed viscosity the Navier--Stokes scaling is

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
 \qquad p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t).
\]

At corresponding times,

\[
 E_\lambda(t)=\lambda^{-1}E(\lambda^2t),\qquad
 Y_\lambda(t)=\lambda Y(\lambda^2t),\qquad
 X_\lambda(t)=\lambda^3X(\lambda^2t).                  \tag{9}
\]

Thus energy becomes smaller under concentration while enstrophy becomes
larger.  The invariant product \(EY\), rather than \(E\) alone, appears in
the valid small-data repair below.

There is also a direct obstruction at the level of admissible initial data.
Choose any nonzero divergence-free Schwartz field \(\phi\) and set

\[
 u_0^{(N)}(x)=N^{3/2}\phi(Nx),\qquad N\ge1.             \tag{10}
\]

Every member of this family is divergence free and Schwartz, while

\[
 \|u_0^{(N)}\|_2=\|\phi\|_2,
 \qquad \|\nabla u_0^{(N)}\|_2=N\|\nabla\phi\|_2,
 \qquad \|u_0^{(N)}\|_3=N^{1/2}\|\phi\|_3.             \tag{11}
\]

Consequently no function of kinetic energy alone can bound initial
enstrophy or the critical \(L^3\) norm uniformly over the Clay data class.
The integrated information in (1),
\(\int_0^T Y\,dt\le E(0)/(2\nu)\), does not repair (6): a time integral of
\(Y\) does not control the cubic quantity \(Y^3\), and arbitrarily narrow,
high peaks are compatible with a fixed \(L^1_t\) bound.  These facts locate
the failed implication; they do not imply that an actual Navier--Stokes
solution develops such peaks.

## A concrete absorption attempt and its exact hypothesis

One useful elementary absorption form comes from (3).  Sobolev and
Plancherel give

\[
 \begin{aligned}
 \left|\int(u\mathbin\cdot\nabla)u\mathbin\cdot\Delta u\,dx\right|
 &\le \|u\|_3\|\nabla u\|_6\|\Delta u\|_2\\
 &\le C_A\|u\|_3\|\Delta u\|_2^2
 =C_A\|u\|_3X.                                         \tag{12}
 \end{aligned}
\]

Hence

\[
 \frac12Y'+(\nu-C_A\|u\|_3)X\le0.                    \tag{13}
\]

This really depletes or absorbs stretching when
\(C_A\|u(t)\|_3<\nu\).  Energy does not imply that hypothesis: (10)--(11)
keep energy fixed while making \(\|u_0\|_3\) arbitrarily large.  The common
proposal to replace \(\|u\|_3\) in (13) by a quantity depending only on
\(\|u\|_2\) is therefore false on divergence-free Schwartz fields.  The
obstruction arises before any question of singularity formation.

Interpolation does, however, give a rigorous scale-invariant small-data
theorem.  From \(L^2\)--\(L^6\) interpolation and Sobolev,

\[
 \|u\|_3\le \|u\|_2^{1/2}\|u\|_6^{1/2}
 \le C_I E^{1/4}Y^{1/4}.                                \tag{14}
\]

Assume

\[
 C_AC_I\,[E(0)Y(0)]^{1/4}<\nu.                         \tag{15}
\]

On every time interval on which \(Y(t)\le Y(0)\), (1), (14), and (15)
make the coefficient in (13) strictly positive, so \(Y'\le0\).  A standard
continuity argument closes the bootstrap: the inequality holds throughout
the maximal classical interval and

\[
 E(t)\le E(0),\qquad Y(t)\le Y(0),
 \qquad
 \int_0^T X(t)\,dt
 \le \frac{Y(0)}{2\delta}                               \tag{16}
\]

for every \(T\) in that interval, where
\(\delta=\nu-C_AC_I[E(0)Y(0)]^{1/4}>0\).  The bounded
\(H^1\) norm supplies the usual strong-solution continuation bound, so the
classical solution is global.  Condition (15) is dimensionless because
\(EY/\nu^4\) is invariant under (9).  It is a sufficient smallness theorem,
not a route from arbitrary finite energy.

The same calculation identifies a clean conditional consumer for any future
depletion estimate.  If one proves on a maximal classical interval that

\[
 \int(S\omega)\mathbin\cdot\omega\,dx
 \le (\nu-\delta)X+g(t)Y,
 \qquad \delta>0,\quad g\in L^1_{\mathrm{loc}}([0,\infty)), \tag{17}
\]

then (2) and Gronwall imply

\[
 Y(t)\le Y(0)\exp\!\left(2\int_0^t g(s)\,ds\right),
 \qquad
 2\delta\int_0^tX(s)\,ds
 \le Y(0)+2\int_0^tg(s)Y(s)\,ds.                       \tag{18}
\]

Thus (17), established for every finite time from the original arbitrary
Schwartz data, would yield the missing continuation control.  Neither the
energy law nor the estimates above prove (17) with a suitable \(\delta,g\)
for large data.

## Relation to established continuation theory

The global conclusion under (15) uses only the standard local strong solution
and continuation theory for the original equation.  Fujita and Kato's primary
paper is [*On the Navier--Stokes initial value problem. I*, Archive for
Rational Mechanics and Analysis 16 (1964), 269--315](https://doi.org/10.1007/BF00276188).
Kato's primary critical-space paper proves global existence for sufficiently
small \(L^3(\mathbb R^3)\) data:
[*Strong \(L^p\)-solutions of the Navier--Stokes equation in \(\mathbb R^m\),
with applications to weak solutions*, Mathematische Zeitschrift 187 (1984),
471--480](https://doi.org/10.1007/BF01174182).  Estimate (15) is a more
restrictive, elementary sufficient condition that places the initial datum in
that small critical regime through (14), while also propagating enstrophy
directly.

The endpoint theorem of Escauriaza, Seregin, and Šverák states that boundedness
in \(L^\infty_tL^3_x\) prevents breakdown for the whole-space suitable weak
solution in its hypotheses; see
[*\(L_{3,\infty}\)-solutions of Navier--Stokes equations and backward
uniqueness*, Russian Mathematical Surveys 58 (2003), 211--250](https://doi.org/10.1070/RM2003v058n02ABEH000609).
It consumes the critical bound but does not generate it from energy.  Under
(15), equations (14) and (16) already provide such a uniform bound.  For
arbitrary data, (10)--(11) and the unclosed coefficient in (13) remain the
precise obstruction.

## Claim boundary

Equations (1)--(7) prove the exact classical identities and the standard
cubic enstrophy inequality.  Equations (9)--(11) disprove any uniform
energy-only control of initial enstrophy or \(L^3\) over the admissible data
class.  Equations (12)--(16) prove absorption and global continuation under
the explicit scale-invariant smallness condition (15).  Equation (17) is a
conditional interface for a future geometric or analytic depletion theorem.
No step above derives (15) or (17) for arbitrary smooth Schwartz data, and no
step asserts finite-time blowup.
