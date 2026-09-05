# HF08 variable-weight diagnostic: an exact nonzero second variation

Status: bounded periodic mechanism test at frozen base
`f0196f75b2c8dd92e2ea32199baf608753e23aa5`.  This note evaluates the full
coefficient from `hf08-square-second-variation.md`, including the Leray
projection and the finite-band multipliers.  It gives an exact signed example,
but no whole-space transfer, high-frequency estimate, or continuation result.

## 1. Frame and plateau hypotheses

Work on the flat torus \(\mathbb T^3=(\mathbb R/2\pi\mathbb Z)^3\), with
normalized spatial integral \(\langle h\rangle=(2\pi)^{-3}\int h\).  Fix a
smooth real radial tight Littlewood--Paley frame

\[
 \Delta_j=m_j(D),\qquad m_j(\xi)=m_0(2^{-j}|\xi|),\qquad
 \sum_{j\in\mathbb Z}m_j(\xi)^2=1\quad(\xi\ne0).
 \tag{1}
\]

The frame is chosen with a nonempty plateau: for some \(\delta>0\),

\[
 m_j(\xi)=1\quad\hbox{when}\quad
 2^j\le |\xi|\le (1+\delta)2^j.                       \tag{2}
\]

This is an admissible, explicitly used choice rather than a generic property
of every dyadic partition.  For example, on the logarithmic radial variable
one may choose a smooth bump equal to one on \([0,\log_2(1+\delta)]\), supported
in an interval of length less than two, arrange that its squared integer
translates sum to one on one period, and extend by integer translation.  The
flatness at the plateau endpoints makes the resulting radial multipliers
smooth away from the origin.  Taking \(\delta<1\) gives annular supports.

Let \(K=2^J\), where \(J\) is large enough that

\[
 \sqrt{K^2+4}\le(1+\delta)K.                          \tag{3}
\]

Use the finite band \(W=(\Delta_0,\Delta_J)\).  Thus (2)--(3) make
\(\Delta_0\) exactly the identity on frequencies of length one and
\(\Delta_J\) exactly the identity on all frequencies

\[
 (\pm K,0,r),\qquad r\in\{-1,0,1,2\}.                \tag{4}
\]

The values in (2)--(4), not an asymptotic replacement of the multipliers, are
what remove the multiplier defects in the calculation below.  Other frame
values and all band edges are irrelevant because their shell components are
paired with zero in the exact finite-band formula.

## 2. Explicit fields and theorem

Fix \(A>0\) and \(\epsilon>0\).  Set

\[
 U=(A\cos z,0,0),                                     \tag{5}
\]
and introduce the two-mode stream function and divergence-free perturbation

\[
 \psi=\cos(Kx+z)+\sin(Kx),\qquad
 v=(\partial_z\psi,0,-\partial_x\psi).                \tag{6}
\]

Then \(WU=(U,0)\), \(Wv=(0,v)\), and hence
\(WU\mathbin\cdot Wv=0\) pointwise.  Moreover

\[
 s=s_U=(\epsilon^2+A^2\cos^2z)^{1/2},qquad V(U)=0.  \tag{7}
\]

**Proposition.**  For (1)--(7), the complete coefficient \(\mathcal C_2(U,v)\)
defined by formula (11) of the frozen HF08 note is

\[
 \boxed{
 \mathcal C_2(U,v)=
 -{A^3K(K^4-K^2+4)\over
        8(K^2+1)(K^2+4)}
   \left\langle{\sin^2(2z)\over
    (\epsilon^2+A^2\cos^2z)^{1/2}}\right\rangle_z .}
                                                               \tag{8}
\]

Here \(\langle\cdot\rangle_z=(2\pi)^{-1}\int_0^{2\pi}\cdot\,dz\).
In particular (8) is strictly negative.  Replacing \(+\sin(Kx)\) in (6) by
\(-\sin(Kx)\) reverses the sign of \(\mathcal C_2\).  Thus the full
variable-weight second variation is nonzero and indefinite on this explicit
scale-separated family.

## 3. Exact evaluation with the Leray term

The plateau identities imply that the first two lines of the exact
finite-band coefficient are literally

\[
 \langle sU,V(v)\rangle+\langle sv,V_{\rm lin}(U,v)\rangle,    \tag{9}
\]

while the third line is zero by \(V(U)=0\).  No scalar-principal
approximation is being made in (9).

Write the linearized Euler pressure as

\[
 V_{\rm lin}(U,v)=
 -(U\cdot\nabla)v-(v\cdot\nabla)U-\nabla p_{\rm lin}.
\]

Taking divergence, using \(U=(U(z),0,0)\), gives the exact pressure equation

\[
 \Delta p_{\rm lin}=-2U'(z)\partial_xv_z.             \tag{10}
\]

Integration by parts in the two terms of (9) cancels the ordinary strain and
transport contributions.  The nonlinear pressure paired with \(sU\) is zero
because \(\operatorname{div}(sU)=0\).  What remains is

\[
 \mathcal C_2(U,v)
 =\left\langle s'(z)v_z\bigl(Uv_x+p_{\rm lin}\bigr)\right\rangle. \tag{11}
\]

This identity retains the weighted Leray contribution through
\(p_{\rm lin}\); omitting it changes the coefficient below.

Only the Fourier modes \(e^{\pm2iz}\) in the \(x\)-average of the last two
factors can pair with \(s'\).  Direct substitution of (6) into (10), followed
by inversion of \(\Delta\) on each nonzero Fourier mode, yields

\[
 \widehat{\langle v_z(Uv_x+p_{\rm lin})\rangle_x}(2)
 =-{iAK(K^4-K^2+4)\over8(K^2+1)(K^2+4)},              \tag{12}
\]

with the coefficient at \(-2\) its complex conjugate.  More explicitly, the
convective part of (12) is \(-iAK/8\), and the pressure/Leray part is

\[
 {3iAK^3\over4(K^2+1)(K^2+4)}.                       \tag{13}
\]

Thus the pressure correction is included exactly and does not cancel the
convective coefficient.  Finally, if \(\widehat s(2)=\langle s\cos2z\rangle_z\),
integration by parts gives

\[
 \widehat s(2)
 =-{1\over2}\langle s'\sin2z\rangle_z
 ={A^2\over4}\left\langle{\sin^2(2z)\over s}\right\rangle_z>0. \tag{14}
\]

Pairing (12) and its conjugate with
\(\widehat{s'}(\pm2)=\pm2i\widehat s(2)\) proves (8).  Also
\(K^4-K^2+4>0\), so every claimed strict sign follows without a numerical
sign check.

## 4. Scope and frontier consequence

**MODE / RESULT:** FALSIFY/DISCOVER.  There is no further cancellation identity
forcing the full second variation to vanish for a spatially variable square
weight, even after low backreaction, weighted Leray projection, background
weight evolution, and finite-shell multipliers are all retained.  Both signs
occur by an exact phase reversal.

**CLAIM AND SCOPE:** (8) is a theorem for the stated smooth periodic fields,
positive regularization, finite band, and the explicit admissible plateau
conditions (2)--(4).  The carrier-to-background ratio is the arbitrary dyadic
integer \(K\), subject only to (3).

**EVIDENCE:** equations (10)--(14) give a finite Fourier calculation and a
strict analytic sign certificate.  The Leray correction is the rational term
(13).  Multiplier defects vanish exactly on the frequencies used because of
the declared plateaus; they were not estimated away.

**FIRST GAP:** this diagnostic supplies neither an \(\mathbb R^3\) construction
nor a time-integrated inequality on a Navier--Stokes trajectory.  Periodic
plane waves cannot be transferred to \(\mathbb R^3\) by assertion, and a
nonzero instantaneous second variation does not prove or disprove HIGH-PRESSURE.

**SURVIVING CONDITIONAL SUFFIX:** the finite-band square functional remains an
exact energy identity.  Any proposed universal sign mechanism must control,
rather than cancel algebraically, the variable-weight interaction exposed by
(8).

**NON-CLAIMS:** no infinite-band limit, \(\epsilon\downarrow0\) limit,
Littlewood--Paley norm conclusion, pressure absorption, critical bound,
regularity, or Clay conclusion is asserted.

**NEXT DISTINCT ACTION:** an \(\mathbb R^3\) wave-packet calculation would need
quantitative control of localization errors in the Leray operator and every
active dyadic multiplier before this periodic obstruction could bear on the
HF mechanism.
