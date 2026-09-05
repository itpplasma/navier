# HF07: a dyadic square-function cubic energy

Status: failed mechanism candidate, repaired after `hf07-review-square.md`.
The original candidate is preserved at commit `f0196f75b2c8dd92e2ea32199baf608753e23aa5`.
The finite-band identity survives. The original promotion of the L2 strain
oracle to the nonlinear cubic remainder is invalid; the complete second
variation and its scope repair are in `hf08-square-second-variation.md`.
No universal high-frequency estimate is proved.

## 1. Tight dyadic frame and regularized energy

Let \(\Delta_j=m_j(D)\) be real, self-adjoint, smooth homogeneous annular
multipliers chosen as a tight frame,
\[
 \sum_{j\in\mathbb Z}m_j(\xi)^2=1\qquad(\xi\ne0).
                                                               \tag{1}
\]
Write \(u_j=\Delta_j u\). For a finite interval
\(I=[-M,N]\cap\mathbb Z\), set
\[
 S_I^2=\sum_{j\in I}|u_j|^2,
 \quad s_{I,\epsilon}=(\epsilon^2+S_I^2)^{1/2},
 \quad
 \mathcal F_{I,\epsilon}(u)
 ={1\over3}\int_{\mathbb R^3}(s_{I,\epsilon}^3-\epsilon^3)\,dx. \tag{2}
\]
The subtraction is necessary on \(\mathbb R^3\): without it the
\(\epsilon\)-regularized functional is infinite. The Littlewood--Paley
square-function theorem gives, after \(I\uparrow\mathbb Z\) and
\(\epsilon\downarrow0\),
\[
 \mathcal F(u):={1\over3}\int
 \left(\sum_j|u_j|^2\right)^{3/2}dx
 \simeq \|u\|_3^3.                                  \tag{3}
\]
This is equivalence of energies only, not a new estimate.

## 2. Exact finite-band evolution

For the finite-band identity, take a smooth divergence-free solution with
sufficient decay/integrability to justify these finite sums and integrations
by parts; this is a regular-time identity, not a decay persistence theorem. Applying \(\Delta_j\) to
\[
 u_t+u\cdot\nabla u+\nabla p=\nu\Delta u,
 \qquad \nabla\cdot u=0,
\]
and differentiating (2) gives
\[
 {d\over dt}\mathcal F_{I,\epsilon}
 +\nu\mathcal D_{I,\epsilon}
 =\mathcal R_{I,\epsilon},                           \tag{4}
\]
where the diffusion is exactly
\[
 \mathcal D_{I,\epsilon}
 =\int s_{I,\epsilon}\sum_{j\in I}|\nabla u_j|^2dx
  +\int s_{I,\epsilon}|\nabla s_{I,\epsilon}|^2dx\ge0,             \tag{5}
\]
and, with \(p_j=\Delta_jp\) and
\(C_j=[\Delta_j,u\cdot\nabla]u\),
\[
 \boxed{\quad
 \mathcal R_{I,\epsilon}
 =-\sum_{j\in I}\int s_{I,\epsilon}u_j\cdot C_j\,dx
   +\sum_{j\in I}\int p_j\,u_j\cdot\nabla s_{I,\epsilon}\,dx.
 \quad}                                               \tag{6}
\]
Indeed,
\[
 \Delta_j(u\cdot\nabla u)=u\cdot\nabla u_j+C_j,
\]
and the common transport cancels without an estimate:
\[
 \sum_{j\in I}\int s_{I,\epsilon}u_j\cdot
                    (u\cdot\nabla u_j)
 ={1\over3}\int u\cdot\nabla(s_{I,\epsilon}^3)=0.  \tag{7}
\]
The pressure term in (6) follows from \(\nabla\cdot u_j=0\). Formula (5)
uses
\(\sum_j u_j\cdot\partial_\alpha u_j
=s_{I,\epsilon}\partial_\alpha s_{I,\epsilon}\).

Formula (6) includes every interaction with shells outside \(I\), because
the advecting and differentiated fields inside \(C_j\) are the full \(u\).
If one Bony-decomposes \(C_j\), the terms containing an input index below
\(-M-O(1)\) or above \(N+O(1)\) are precisely the lower and upper band
boundary terms; they have not been discarded in (6). In Fourier variables
the commutator is exactly
\[
 \widehat C_j(\xi)
 =\int i(\xi-\eta)\cdot\widehat u(\eta)
   [m_j(\xi)-m_j(\xi-\eta)]
   \widehat u(\xi-\eta)\,d\eta,                      \tag{8}
\]
while
\[
 \widehat{\nabla p_j}(\xi)
 =-m_j(\xi)(I-\mathbb P(\xi))
       \widehat{u\cdot\nabla u}(\xi).               \tag{9}
\]
Thus (8)--(9), together with (6), are the exact transfer and pressure
symbols; no termwise absolute-pressure estimate has yet been made.

## 3. The attempted pressure/transfer grouping

For a low mode \(U\) and a high solenoidal mode \(q\) near shell \(j\), the
combined high-output transport and pressure are, to first order in \(q\),
\[
 L_Uq=\mathbb P\bigl(U\cdot\nabla q+q\cdot\nabla U\bigr).       \tag{10}
\]
This is the correct grouping: (9) supplies exactly the longitudinal part
removed by \(\mathbb P\), while (8) removes the large constant-transport
piece from the differentiated square energy. If \(U\) is constant, (10) is
skew under spatial integration and contributes zero, agreeing with (7).

The unweighted toy pairing satisfies
\[
 \int q\cdot L_Uq=\int q_aq_b\partial_b U_a.
\]
It has an indefinite strain form. This is not the complete second variation
of the cubic square energy: high-high feedback into the background, variation
of its weight, and weighted Leray terms must also be retained. The prior
claim that these terms do not negate the strain was unsupported. The exact
constant-weight example in `hf08-controller-constant-weight.md` has nonzero
toy strain but zero complete second variation.

## 4. Remaining producer

A low-high absolute paraproduct bound or an unnamed Carleson estimate cannot
supply the missing arbitrary-data producer. One must first derive the full
remainder, with all multipliers and regularizations declared, and then prove
its signed spacetime absorption with an input-only finite remainder uniform
through the maximal endpoint. Equivalence of square energy to L3 does not
prove this absorption. A nonzero instantaneous coefficient also does not
refute a spacetime estimate.

## 5. Removing the regularizations

For fixed finite \(I\), as \(\epsilon\downarrow0\), (2) converges to
\(\frac13\int S_I^3\). In (5), define the second integrand to be zero on
\(\{S_I=0\}\). The pointwise inequality
\[
 s_{I,\epsilon}|\nabla s_{I,\epsilon}|^2
 ={1\over s_{I,\epsilon}}
   \sum_\alpha\left|\sum_j u_j\cdot\partial_\alpha u_j\right|^2
 \le s_{I,\epsilon}\sum_j|\nabla u_j|^2              \tag{16}
\]
gives dominated convergence for smooth rapidly decreasing fields.
All terms in (6) converge by the same finite-sum smooth bounds.

The all-band differentiated limit requires a separate argument with summable
bounds for the aggregate remainder and diffusion. The earlier appeal to
"standard homogeneous low-frequency estimates" did not supply that argument.
In particular, no persistence of Schwartz spatial decay for the actual
Navier--Stokes trajectory is assumed. Even a limit justified on every compact
regular interval would not supply endpoint-uniform a priori control.
