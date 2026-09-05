# HF05 radial dynamics: does angular dissipation suppress pressure work?

Status: DISCOVER/REPAIR calculation for smooth unforced Navier--Stokes on
\(\mathbb R^3\).  It tests one concrete producer for pressure absorption:
whether the equation dynamically forces radial cubic dissipation to be small
relative to angular cubic dissipation during concentration.  The derived
evolution contains uncontrolled signed angular-transfer and pressure-Hessian
terms, so no such producer is proved.

## 1. Radial/angular splitting and the direct pressure estimate

Away from \(u=0\), write

\[
 r=|u|,qquad n={u\over r}.
\]

Since \(n\cdot\partial_jn=0\),

\[
 |\nabla u|^2=|\nabla r|^2+r^2|\nabla n|^2.            \tag{1}
\]

Define, initially by regularization at the zero set,

\[
 A=\int r|\nabla r|^2,qquad
 B=\int r^3|\nabla n|^2.                              \tag{2}
\]

Then the cubic dissipation in the exact \(L^3\) balance is

\[
 \boxed{D_3=2A+B.}                                    \tag{3}
\]

The pressure work sees only the radial derivative.  Calderon--Zygmund,
Hölder, interpolation, and Sobolev applied to \(r^{3/2}\) give

\[
\begin{aligned}
 |P_3|
 &\leq\|p\|_{9/4}\|r\nabla r\|_{9/5}\\
 &\leq C\|u\|_{9/2}^2
       \|r^{1/2}\|_{18}\|r^{1/2}\nabla r\|_2\\
 &\leq C\|u\|_3\|r\|_9^{3/2}A^{1/2}\\
 &\leq \boxed{C\|u\|_3A}.                           \tag{4}
\end{aligned}
\]

The exponents are exact:
\(4/9+5/9=1\),
\(1/(9/5)=1/18+1/2\), and

\[
 \|u\|_{9/2}^2\leq\|u\|_3\|u\|_9,qquad
 \|r\|_9^{3/2}=\|r^{3/2}\|_6
 \leq C\|\nabla(r^{3/2})\|_2=C{3\over2}A^{1/2}.       \tag{5}
\]

Thus angular dominance would give genuine absorption.  For example, at a
time when

\[
 {C\|u(t)\|_3A(t)\over 2A(t)+B(t)}\leq\theta\nu,
 \qquad \theta<1,                                    \tag{6}
\]

equations (3)--(4) imply \(|P_3|\leq\theta\nu D_3\).
Condition (6) is not taken as progress: the question is whether the dynamics
produce it for arbitrary data.

## 2. Zero-set regularization and the speed equation

Set

\[
 r_\varepsilon=(|u|^2+\varepsilon^2)^{1/2},qquad
 h_\varepsilon={u\over r_\varepsilon}.                \tag{7}
\]

Dotting Navier--Stokes with \(u/r_\varepsilon\), and using

\[
 \Delta r_\varepsilon
 ={|\nabla u|^2+u\cdot\Delta u\over r_\varepsilon}
 -{|u\cdot\nabla u|^2\over r_\varepsilon^3},         \tag{8}
\]

gives the exact regularized scalar equation

\[
 \partial_t r_\varepsilon+u\cdot\nabla r_\varepsilon
 +h_\varepsilon\cdot\nabla p
 =\nu\Delta r_\varepsilon-\nu Z_\varepsilon,          \tag{9}
\]

where

\[
 Z_\varepsilon
 ={r_\varepsilon^2|\nabla u|^2-|u\cdot\nabla u|^2
   \over r_\varepsilon^3}\geq0.                       \tag{10}
\]

The contraction in \(|u\cdot\nabla u|^2\) denotes the sum
\(\sum_j|u\cdot\partial_ju|^2\).  Positivity in (10) is Cauchy--Schwarz.
At points where \(r>0\),

\[
 Z_\varepsilon\longrightarrow r|\nabla n|^2.          \tag{11}
\]

At zeros, (10) retains the nonnegative defect needed to justify limiting
inequalities; it must not simply be deleted by defining an arbitrary direction.

## 3. Exact evolution of radial cubic dissipation

Put

\[
 \rho_\varepsilon=r_\varepsilon^{3/2},qquad
 A_\varepsilon={4\over9}\|\nabla\rho_\varepsilon\|_2^2
 =\int r_\varepsilon|\nabla r_\varepsilon|^2.         \tag{12}
\]

The chain rule transforms (9) into

\[
 \partial_t\rho_\varepsilon+u\cdot\nabla\rho_\varepsilon
 =\nu\Delta\rho_\varepsilon
   -\Phi_\varepsilon-\Psi_\varepsilon-\Pi_\varepsilon,             \tag{13}
\]

with

\[
 \Phi_\varepsilon={3\nu\over4}r_\varepsilon^{-1/2}
                         |\nabla r_\varepsilon|^2,
\quad
 \Psi_\varepsilon={3\nu\over2}r_\varepsilon^{1/2}Z_\varepsilon,
\quad
 \Pi_\varepsilon={3\over2}r_\varepsilon^{1/2}
                         h_\varepsilon\cdot\nabla p.  \tag{14}
\]

Pairing (13) with \(-\Delta\rho_\varepsilon\) and integrating the transport
term by parts gives

\[
\boxed{
 {9\over8}{dA_\varepsilon\over dt}
 +\nu\|\Delta\rho_\varepsilon\|_2^2
 =-\int\partial_i u_j\,partial_i\rho_\varepsilon
                         \partial_j\rho_\varepsilon
  +\int(\Phi_\varepsilon+\Psi_\varepsilon+
                         \Pi_\varepsilon)\Delta\rho_\varepsilon.} \tag{15}
\]

All terms in (15) are exact for \(\varepsilon>0\), after ordinary spatial
cutoffs.  This is the requested evolution law for radial cubic dissipation.

The angular-transfer term is not damping.  Formally on \(r>0\), integrate it
by parts and use (11):

\[
\begin{aligned}
 \int\Psi\Delta\rho
 &=-{3\nu\over2}\int\nabla(r^{3/2}|\nabla n|^2)
                              \cdot\nabla(r^{3/2})\\
 &=-{27\nu\over8}\int r|\nabla r|^2|\nabla n|^2
   -{9\nu\over4}\int r^2\nabla(|\nabla n|^2)\cdot\nabla r.     \tag{16}
\end{aligned}
\]

The first term is favorable.  The second is a signed transfer involving
second derivatives of direction.  The quantity
\(B=\int r^3|\nabla n|^2\) controls neither
\(r^2\nabla|\nabla n|^2\) nor its pairing with \(\nabla r\).  Taking absolute
values in (15) instead gives

\[
 \left|\int\Psi_\varepsilon\Delta\rho_\varepsilon\right|
 \leq {\nu\over4}\|\Delta\rho_\varepsilon\|_2^2
      +C\nu\|r_\varepsilon^{1/2}Z_\varepsilon\|_2^2,  \tag{17}
\]

whose new norm tends formally to
\(\int r^3|\nabla n|^4\), again strictly beyond \(B\).

The radial chain-rule term is also signed at the \(H^1\) level:

\[
 \int\Phi_\varepsilon\Delta\rho_\varepsilon
 =-{3\nu\over4}\int
 \nabla(r_\varepsilon^{-1/2}|\nabla r_\varepsilon|^2)
 \cdot\nabla\rho_\varepsilon.                         \tag{18}
\]

It contains the radial Hessian and is not controlled by \(A_\varepsilon\)
alone.

## 4. Pressure-Hessian and direction transfer

Define

\[
 b_\varepsilon=r_\varepsilon^{1/2}h_\varepsilon
 ={u\over r_\varepsilon^{1/2}}.                       \tag{19}
\]

The pressure term in (15) has the exact integrated form

\[
\begin{aligned}
 \int\Pi_\varepsilon\Delta\rho_\varepsilon
 =-{3\over2}\int
 &\left[(\partial_i b_{\varepsilon,k})(\partial_kp)
       +b_{\varepsilon,k}\partial_i\partial_kp\right]
       \partial_i\rho_\varepsilon.                   \tag{20}
\end{aligned}
\]

Thus radial dynamics couples to both variation of direction/amplitude through
\(\nabla b_\varepsilon\) and the full pressure Hessian.  Calderon--Zygmund
expresses \(\nabla^2p\) through two derivatives of \(u\otimes u\); no
energy-level estimate follows.  Avoiding integration by parts only replaces
(20) by

\[
 \left|\int\Pi_\varepsilon\Delta\rho_\varepsilon\right|
 \leq {\nu\over4}\|\Delta\rho_\varepsilon\|_2^2
 +C\nu^{-1}\|r_\varepsilon^{1/2}
                    h_\varepsilon\cdot\nabla p\|_2^2, \tag{21}
\]

which introduces a weighted pressure-gradient norm not controlled by energy,
\(A\), or \(B\).

Finally, the strain term in (15) satisfies only

\[
 \left|\int\partial_i u_j\partial_i\rho_\varepsilon
                              \partial_j\rho_\varepsilon\right|
 \leq\|\nabla u\|_\infty\|\nabla\rho_\varepsilon\|_2^2,           \tag{22}
\]

which invokes a standard higher continuation norm.  Equations (16), (20),
and (22) are the first terms preventing a closed evolution inequality for
\(A/(2A+B)\).

## 5. A simpler speed-gradient audit reaches the same obstruction

For orientation, let \(K_\varepsilon=\|\nabla r_\varepsilon\|_2^2\).
Pairing (9) with \(-\Delta r_\varepsilon\) gives

\[
\begin{aligned}
 {1\over2}{dK_\varepsilon\over dt}
 +\nu\|\Delta r_\varepsilon\|_2^2
 &=-\int\partial_i u_j\partial_i r_\varepsilon
                         \partial_j r_\varepsilon
   +\nu\int Z_\varepsilon\Delta r_\varepsilon\\
 &\quad-\int\left[(\partial_i h_{\varepsilon,k})(\partial_kp)
       +h_{\varepsilon,k}\partial_i\partial_kp\right]
       \partial_i r_\varepsilon.                     \tag{23}
\end{aligned}
\]

The same angular-transfer, direction-gradient, strain, and pressure-Hessian
terms appear.  Moreover, unweighted \(K\) does not control the weighted
quantity \(A\) without an unavailable pointwise speed bound.  Thus switching
from \(A\) to the simpler speed-gradient energy does not repair (6).

## 6. Signed pressure cancellation test

The exact critical balance reads

\[
 {1\over3}{d\over dt}\|u\|_3^3+\nu(2A+B)=P_3.         \tag{24}
\]

Estimate (4) shows why angular dominance would help, but inserting (15) does
not produce a signed cancellation with \(P_3\).  The pressure in (24) is
linear in \(p\) and first-order in \(r\), whereas differentiating \(A\)
produces the pressure-Hessian expression (20).  Integrating (20) back by parts
returns \(\Pi\Delta\rho\), not \(P_3\); no boundary functional matching the
critical pressure work appears.

A possible exact repair would combine (15) with an evolution law for an
angular functional whose transfer term cancels the second term of (16).
The obvious weighted sum satisfies
\(A+B=\int r|\nabla u|^2\), which is not the classical enstrophy
\(\int|\nabla u|^2\).  No cancellation or reduction to the enstrophy identity
may be asserted without deriving that weighted evolution.  The calculation
above establishes only that the radial identity by itself does not close; it
does not exclude a new coupled radial-angular functional.

## 7. Exact dynamical oracle: angular shear creates radial variation

There is a simple periodic solution that falsifies propagation of the naive
condition \(A=0\).  On \(\mathbb T^3\), take a smooth periodic nonaffine
function \(\varphi(z)\) and

\[
 u_0(z)=(\cos\varphi(z),\sin\varphi(z),0).             \tag{25}
\]

This field is divergence free.  It depends only on \(z\) and has zero third
component, so \((u\cdot\nabla)u=0\).  With constant pressure its exact
Navier--Stokes evolution is componentwise heat flow,

\[
 u(t)=e^{\nu t\partial_z^2}u_0.                       \tag{26}
\]

Initially \(r=|u_0|=1\), hence \(A(0)=0\), while

\[
 \partial_t r\big|_{t=0}
 ={u_0\over|u_0|}\cdot\nu\partial_z^2u_0
 =-\nu(\varphi')^2.                                   \tag{27}
\]

Therefore

\[
 \partial_z r(t)=-2\nu t\varphi'\varphi''+O(t^2)
\]

in every fixed smooth norm, and

\[
 \boxed{A(t)=4\nu^2t^2
 \int_{\mathbb T^3}(\varphi'\varphi'')^2+o(t^2).}     \tag{28}
\]

Choose \(\varphi\) with \(\varphi'\varphi''\not\equiv0\).  Then \(A(t)>0\)
for all sufficiently small positive \(t\), even though the initial velocity
has purely directional variation.  This is an actual Navier--Stokes
trajectory and an independent sign check on the transfer mechanism in
(15)--(16): viscosity can transfer angular variation into speed variation.

The example is periodic and has nondecaying unit speed.  It is not an R3
counterexample and supplies no conclusion about concentration.  Localizing a
high-frequency shear in R3 would introduce boundary and pressure errors that
must be estimated before making an analogous claim.

## 8. Scaling, falsifiers, and result

Under \(u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t)\),

\[
 A_\lambda(t)=\lambda^2A(\lambda^2t),qquad
 B_\lambda(t)=\lambda^2B(\lambda^2t),qquad
 P_{3,\lambda}(t)=\lambda^2P_3(\lambda^2t).            \tag{29}
\]

Thus \(A/(2A+B)\) and \(\|u\|_3\) are invariant.  Condition (6) is
scale-consistent; its absence cannot be repaired by a subcritical scaling
factor.

Amplitude reversal leaves \(r,A,B,D_3\) unchanged but reverses \(P_3\).
Hence radial/angular magnitudes alone cannot determine the sign of pressure
work.  The compactly supported profiles in `hf02-r3-profile.md` realize
nonzero pressure work, so this sign test is not vacuous.  It remains a static
falsifier; it does not disprove a signed time cancellation on trajectories.

**Actual result:** equations (9), (15), (16), and (20) give the regularized
speed and radial-dissipation dynamics, including zero-set, angular-transfer,
and pressure-Hessian terms.  Equation (4) rigorously shows that only radial
cubic dissipation enters the direct absolute pressure bound.

**First failed bridge:** large \(B/A\) at one time does not propagate from
these identities.  Its derivative couples to
\(r^3|\nabla n|^4\), second derivatives of direction, strain in
\(L^\infty\), and weighted pressure-gradient/Hessian norms.  None is bounded
by energy and \(2A+B\).

**Non-claims:** no arbitrary-data angular dominance, pressure absorption,
high-frequency estimate, or global regularity theorem is proved.  The
conditional algebra (6) is not presented as a novel theorem or replacement
for the original target.
