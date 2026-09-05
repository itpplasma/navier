# HF15: energy-only elimination of low-pressure Euler gradients

Status: bounded analytic producer substep, 2026-09-05.

This note bounds the two terms created when the low-pressure gradient is
removed from the Euler part of the fixed-high-output homogeneous functional.
The bounds are uniform in the coupling parameter \(k>0\). They do not bound
the remaining high-output Euler sum.

## Setup and scalar coefficients

For instantaneous estimates assume a solenoidal field in
\(H^1(\mathbb R^3)\); the time-integrated statements apply on compact
classical Navier--Stokes intervals with the energy identity. This supplies
the gradient norm required by the interpolation estimates below.

Let \(S_J\) be the fixed smooth low-pass from HF14 and write
\[
 p^L=S_Jp,\qquad z=p^H=(I-S_J)p,
 \qquad p=R_iR_j(u_i u_j).                                    \tag{1}
\]
For
\[
 g_k(r,z)=z\left(\sqrt{r^2+kz_-}-\sqrt{kz_-}\right),
\]
define, away from the scalar cusps and by the indicated bounded extensions
on them,
\[
 b_k(r,z)={\partial_rg_k(r,z)\over r},\qquad
 a_k(r,z)=\partial_zg_k(r,z)-{3\over2}\sqrt{z_-}.              \tag{2}
\]
Only the products in the estimates below are needed. Define the vector
\(b_ku\) to be zero at \(u=0\). This is a chosen bounded representative,
not an assertion of a vector derivative at \(u=0,z>0\). The scalar formulas
give, pointwise and uniformly for \(k>0\),
\[
 |b_k(r,z)u|\le|z|.                                          \tag{3}
\]
and
\[
 |a_k(r,z)|\le r+{3\over2}\sqrt{z_-}.                         \tag{4}
\]
Since the high-output multiplier is uniformly bounded on \(L^{3/2}\),
\[
 \boxed{\quad \|a_k(|u|,z)\|_3\le C\|u\|_3,\quad}            \tag{5}
\]
with a constant independent of \(k\) and \(J\).

Let
\[
 E(t)=\|u(t)\|_2^2,\qquad Y(t)=\|\nabla u(t)\|_2^2.           \tag{6}
\]
The two low-gradient forms are
\[
 T_1(t)=\int b_k(|u|,z)u\cdot\nabla p^Ldx,                    \tag{7}
\]
\[
 T_2(t)=2\int a_k(|u|,z)(I-S_J)R_iR_j
                  (u_i\partial_jp^L)dx.                       \tag{8}
\]

## Fixed-cutoff kernel estimates

The kernel of \(\nabla S_JR_iR_j\) scales as
\[
 L_J(x)=2^{4J}L_0(2^Jx).                                      \tag{9}
\]
The extra derivative changes the degree-minus-three Riesz tail into an
\(O(|x|^{-4})\) tail, while the compactly supported frequency multiplier is
integrable and gives local boundedness. Thus \(L_0\in L^q\) for the two
values \(q=2,6\) used below, and convolution with
\(u_i u_j\in L^1\) gives
\[
 \boxed{\quad
 \|\nabla p^L\|_2\le C2^{5J/2}E,
 \qquad
 \|\nabla p^L\|_6\le C2^{7J/2}E.
 \quad}                                                       \tag{10}
\]
No \(L^1\) bound on the undifferentiated low-Riesz kernel and no Schwartz
decay of \(u\) are used.

## Instantaneous bounds

From (3), Cauchy--Schwarz, and (10),
\[
 |T_1|\le\|z\|_2\|\nabla p^L\|_2.                            \tag{11}
\]
The high-output multiplier is bounded on \(L^2\), and the
three-dimensional Gagliardo--Nirenberg inequality gives
\[
 \|z\|_2\le C\|u\otimes u\|_2
 \le C\|u\|_4^2
 \le C E^{1/4}Y^{3/4}.                                       \tag{12}
\]
Therefore
\[
 \boxed{\quad
 |T_1(t)|\le C2^{5J/2}E(t)^{5/4}Y(t)^{3/4}.
 \quad}                                                       \tag{13}
\]

For the second term, Holder, the boundedness of the high-output double
Riesz multiplier on \(L^{3/2}\), (5), and (10) give
\[
 \begin{split}
 |T_2|
 &\le C\|a_k\|_3\|u\nabla p^L\|_{3/2}\\
 &\le C\|u\|_3\|u\|_2\|\nabla p^L\|_6.
 \end{split}                                                  \tag{14}
\]
Using \(\|u\|_3\le C\|u\|_2^{1/2}\|\nabla u\|_2^{1/2}\)
yields
\[
 \boxed{\quad
 |T_2(t)|\le C2^{7J/2}E(t)^{7/4}Y(t)^{1/4}.
 \quad}                                                       \tag{15}
\]
All constants in (13) and (15) are uniform in \(k>0\).

## Time-integrated energy remainders

Let \(u\) be an actual classical unforced Navier--Stokes solution, fix
\(H>0\), and take \(0<\tau<\min(H,T_*)\). Assume enough Sobolev regularity
to justify the displayed pairings; for example
\(u\in C([0,\tau];H^m)\), \(u_t\in C([0,\tau];H^{m-2})\), \(m\ge4\).
The energy identity gives
\[
 E(t)\le E_0:=E(0),\qquad
 \int_0^\tau Y(t)dt\le {E_0\over2\nu}.                       \tag{16}
\]
Holder's inequality in time applied to (13) and (15) now gives, uniformly
for every \(0<\tau\le H\),
\[
 \boxed{\quad
 \int_0^\tau|T_1(t)|dt
 \le C2^{5J/2}E_0^2\nu^{-3/4}H^{1/4},
 \quad}                                                       \tag{17}
\]
and
\[
 \boxed{\quad
 \int_0^\tau|T_2(t)|dt
 \le C2^{7J/2}E_0^2\nu^{-1/4}H^{3/4}.
 \quad}                                                       \tag{18}
\]
The harmless powers of two from (16) are absorbed in \(C\).

## Exact place in the Euler decomposition

If
\[
 V=-u\cdot\nabla u-\nabla p
\]
is split as
\[
 V=W-\nabla p^L,\qquad W=-u\cdot\nabla u-\nabla p^H,           \tag{19}
\]
then the velocity variation contributes \(-T_1\). Since the high pressure
variation is
\[
 (p^H)_V=2(I-S_J)R_iR_j(u_iV_j),                              \tag{20}
\]
substitution of (19) contributes \(-T_2\). These signs are irrelevant to
the absolute estimates (17)--(18), but fix the algebraic bookkeeping.

The field \(W\) is generally not solenoidal:
\[
 \nabla\cdot W=\Delta p^L.
\]
Consequently no Leray orthogonality, projected transport identity, or
divergence-free cancellation may be reused with \(W\). Equations
(17)--(18), together with the already controlled low-output pressure-work
term, eliminate the low-pressure Euler pieces only. They do not estimate the
remaining expression involving \(W\), \(p^H\), and the high-output pressure
variation.

The terms (7)--(8) are rigorously defined under the stated Sobolev
hypotheses, including at the scalar cusp sets by the bounds (3)--(5). Their
identification as pieces of an unregularized Frechet derivative remains
subject to the known zero-set issue. A regularized evolution identity may
use (17)--(18) for the corresponding limiting pieces, but its extra
regularizer terms require separate bookkeeping.

## Frontier record

**MODE / RESULT:** REPAIR. The two low-pressure-gradient Euler terms have
the uniform-in-\(k\), energy-only finite-horizon bounds (17)--(18).

**FIRST GAP:** control the complete remaining high-output Euler and heat
sum. The replacement field \(W\) is not divergence-free.

**SURVIVING CONDITIONAL SUFFIX:** these low-gradient terms may be placed in
the input-only remainder of any rigorously regularized high-output identity
once its limiting decomposition is justified.

**NON-CLAIMS:** no bound on the remaining high-output sum, unregularized
Frechet derivative, pressure absorption, HF estimate, or regularity theorem
is asserted.
