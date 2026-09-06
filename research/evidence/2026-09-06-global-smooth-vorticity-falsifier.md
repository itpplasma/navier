# Global-smooth upgrade of the maximum-vorticity falsifier

Date: 2026-09-06.
Frozen research input: `itpplasma/navier` at
`6595e4f7e7227abf04de7efadbb83c83055bbfd6`.
Status: author derivation; independent mathematical audit pending.
Terminal theorem: **not proved**. Terminal obstruction: **unchanged**.
No novelty or priority claim. No graph node is promoted.

This note strengthens one scope point of
`research/evidence/2026-09-06-pointwise-vorticity-helicity-exclusions.md`.
Its Theorem A already constructs actual unforced Navier--Stokes branches with
identical energy, enstrophy and maximum vorticity but arbitrarily large
initial growth of the maximum vorticity. The construction there is stated
only on the local classical branch.

The same construction can be parameterized so that **every one of those
branches is globally smooth**. Thus the instantaneous maximum-vorticity
closure fails already inside a uniformly compactly supported family of
global smooth solutions. This does not prove NS-R3 and does not make the
remaining terminal obstruction smaller. It strengthens the architectural
falsification: the failure is not a pathology confined to hypothetical
near-singular trajectories.

## 1. Strengthened theorem

**Proposition GS.** Fix `nu > 0`. There exist positive constants
`E_*`, `Y_*`, `gamma`, one compact set `K`, and smooth compactly supported
solenoidal data `u_(0,N)`, `N >= 1`, such that

\[
 \|u_{0,N}\|_2^2=E_*,\qquad
 \|\nabla u_{0,N}\|_2^2=Y_*,\qquad
 \|\omega_{0,N}\|_\infty=1,
\]

all data are supported in `K`, and near the origin

\[
 \omega_{0,N}=e_3,
\]

while the original unforced Navier--Stokes solution of viscosity `nu` from
each datum is global and smooth and satisfies

\[
 \liminf_{t\downarrow0}
 \frac{\|\omega_N(t)\|_\infty-1}{t}\ge \gamma N.
\]

In particular the local spatial vorticity jet at the exhibited global
maximum remains exactly the same as in Theorem A: all positive-order spatial
derivatives of `omega` vanish there, while the initial stretching rate tends
to infinity with `N`.

## 2. Only one parameter of Theorem A must change

Use Sections 2.1--2.3 of
`2026-09-06-pointwise-vorticity-helicity-exclusions.md` unchanged. Thus the
central field `C_N` has maximum vorticity exactly one, equals a rigid rotation
plus the sum of `N` nested irrotational strains near the origin, and has
energy and enstrophy bounds

\[
 E(C_N)\le C_E r_0^5,\qquad
 Y(C_N)\le C_Y r_0^3,
\]

with constants independent of `N` and `r_0`. At the origin the actual
vorticity equation gives

\[
 \partial_t\omega_N(0,0)=\gamma N e_3.
\]

In the reservoir construction of Section 2.4, replace the fixed amplitude
`delta=1/8` by an arbitrary

\[
 0<\delta<1/8.
\]

Keep the two fixed reservoir length scales `L_1=1`, `L_2=2`. Their exact
energy and enstrophy are then

\[
 E_j=2\delta^2 L_j^5 E(V),\qquad
 Y_j=2\delta^2 L_j^3 Y(V).
\]

The two-by-two matrix with columns `(E_j,Y_j)` remains invertible for every
`delta>0`, because `Y_j/E_j=L_j^{-2}Y(V)/E(V)` differs between the two
length scales. Put as before

\[
 E_*=E_1+E_2,\qquad Y_*=Y_1+Y_2.
\]

Hence

\[
 E_*Y_* = C_R\delta^4                                      \tag{1}
\]

for one fixed constant `C_R>0` depending only on the reservoir profile and
the two fixed scales.

After choosing `delta`, choose `r_0` sufficiently small. Since the inverse
matching matrix has size `O(delta^{-2})` whereas
`E(C_N)=O(r_0^5)` and `Y(C_N)=O(r_0^3)` uniformly in `N`, the coefficients
used to match the two scalar values exactly still obey, uniformly in `N`,

\[
 3/4\le a_N^2,b_N^2\le5/4.
\]

The reservoir vorticity is at most

\[
 \sqrt{5/4}\,\delta<1,
\]

so it does not change the exact global maximum of vorticity. All support and
local-jet properties from Theorem A are unchanged. Thus the resulting family
still has the identical scalar tuple `(E_*,Y_*,1)` and the unbounded initial
maximum-vorticity growth.

The remaining point is to choose `delta` small enough that this common scalar
tuple lies in a standard global small-data region.

## 3. Energy--enstrophy smallness gives global smoothness

On every compact interval of the local classical branch write

\[
 E=\|u\|_2^2,\qquad Y=\|\nabla u\|_2^2,
 \qquad Z=\|\Delta u\|_2^2.
\]

The already-established ENERGY node gives

\[
 E(t)\le E_*.
\]

The standard enstrophy estimate used in the repository gives, for a universal
constant `C_0>0`,

\[
 Y' + \nu Z\le C_0\nu^{-3}Y^3.                              \tag{2}
\]

For completeness, (2) follows from the exact enstrophy identity, Sobolev and
interpolation,

\[
 \left|\int\omega\cdot((\omega\cdot\nabla)u)\right|
 \le C Y^{3/4}Z^{3/4},
\]

followed by Young's inequality.

Fourier Cauchy--Schwarz gives

\[
 Y^2\le EZ\le E_*Z,
\]

hence

\[
 Z\ge \frac{Y^2}{E_*}.                                      \tag{3}
\]

Combining (2)--(3),

\[
 Y'\le -\frac{\nu}{E_*}Y^2+C_0\nu^{-3}Y^3
 =-\frac{\nu}{E_*}Y^2
   \left(1-C_0\frac{E_*Y}{\nu^4}\right).                    \tag{4}
\]

By (1) choose `delta>0` so small that

\[
 C_0\frac{E_*Y_*}{\nu^4}<\frac12.                            \tag{5}
\]

At any time at which `Y=Y_*`, equations (4)--(5) give

\[
 Y'\le -\frac{\nu}{2E_*}Y_*^2<0.
\]

Since `Y(0)=Y_*`, the usual first-crossing argument shows

\[
 Y(t)\le Y_*
\]

throughout the maximal classical interval. Indeed a first upward crossing of
the level `Y_*` would have nonnegative upper right derivative, contradicting
the displayed strict negative bound.

The LOCAL node in the repository states that a finite maximal time forces
enstrophy to diverge. The uniform bound `Y(t)<=Y_*` therefore rules out a
finite maximal time. Every solution in the family is global and smooth.

This global conclusion uses only already-established ENERGY, the standard
repository enstrophy estimate, Fourier Cauchy--Schwarz, and the LOCAL blow-up
alternative. It does not assume the terminal theorem.

## 4. Exact architectural consequence

The scalar-input maximum-vorticity producer remains falsified even after the
test family is restricted to globally smooth solutions. More precisely,
there is no finite function of the instantaneous scalar tuple

\[
 (\nu,E,Y,\Omega)
\]

that bounds `D^+ Omega` at every classical state: Proposition GS supplies the
same tuple `(nu,E_*,Y_*,1)` for every `N` and an initial upper-right growth at
least `gamma N`.

The same local-jet scope from the parent evidence file remains in force. At
the exhibited maximum, every spatial derivative of the vorticity vanishes;
the coherent neighborhood shrinks with `N`. Therefore this does **not**
exclude full-datum estimates, constants depending on high initial norms,
quantitative control of a coherence radius, or genuinely nonlocal spacetime
stretching estimates.

Terminal theorem: **not proved**.
Terminal obstruction: **unchanged**.
Architectural delta: the instantaneous scalar/local-vorticity-jet closure is
now falsified already on globally smooth actual NS trajectories.
