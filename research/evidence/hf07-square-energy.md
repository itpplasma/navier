# HF07: a dyadic square-function cubic energy

Status: mechanism test, 2026-09-05. This note tests a nonscalar frequency
energy for smooth solutions of the unforced Navier--Stokes equation on
\(\mathbb R^3\). It derives an exact regularized finite-band identity and
identifies the first interaction for which the proposed pressure/transfer
cancellation has no sign. It does not prove the universal high-frequency
estimate.

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

Let \(u,p\) be a Schwartz-class smooth solution at the time under
consideration. Applying \(\Delta_j\) to
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
   +\sum_{j\in I}\int p_j,u_j\cdot\nabla s_{I,\epsilon}\,dx.
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

The first nonconstant coefficient does not cancel. In the unweighted
divergence-free \(L^2\) pairing,
\[
 \int q\cdot L_Uq\,dx
 =\int q_aq_b\,\partial_bU_a\,dx,                    \tag{11}
\]
because \(\mathbb Pq=q\) and the transport part integrates to zero. Only
the symmetric strain of \(\nabla U\) occurs, but it is indefinite. The
square-cubic weight adds commutators of \(\mathbb P\) with multiplication by
\(s_{I,\epsilon}\); those are also order \(\nabla U\) in the low--high
regime. They do not negate (11). Equivalently, expanding (8) for
\(|\eta|\ll|\xi|\) replaces the vanished zeroth-order translation by
\[
 \nabla m_j(\xi)\cdot\eta,
\]
and (9) applies the order-zero matrix \(\mathbb P(\xi)\). The resulting
matrix coefficient is linear in \(\widehat{\nabla U}(\eta)\), has a
nonzero symmetric part, and has no factor \(2^{-j}\) after the derivative
on the high mode and the multiplier difference are combined.

This supplies a concrete failure of the hoped-for sign: pressure cancels
the longitudinal acceleration and the commutator cancels constant sweeping,
but neither cancels low-frequency strain. Changing the signs of the
eigenvalues of a trace-free strain matrix changes the sign of (11), so
incompressibility supplies no one-sided bound.

## 4. Exact missing coefficient

The standard paraproduct estimate corresponding to (11) has the form
\[
 |\mathcal R_{I,\epsilon}^{\rm low-high}|
 \lesssim
 \sum_{j\in I}\int
 |\nabla S_{j-4}u|\,s_{I,\epsilon}|u_j|^2dx
 +\text{balanced and band-boundary interactions}.    \tag{12}
\]
The displayed coefficient is critical. An absolute closure uses
\[
 \sum_j\|\nabla S_{j-4}u\|_\infty
       \int s_{I,\epsilon}|u_j|^2dx,                 \tag{13}
\]
or a sharper Carleson version retaining the sum inside space-time. Energy
does not control either coefficient. Nor can viscosity absorb (12) with a
fixed fraction merely by taking \(j\) large: the dimensionless coefficient
\[
 2^{-2j}\|\nabla S_{j-4}u\|_\infty                  \tag{14}
\]
has no energy-level uniform tail modulus, and balanced high--high
interactions require an analogous square/Carleson summability bound.

A sufficient repair would be an input-only space-time estimate for the
positive part of the aggregate strain and balanced-shell form, strong enough
that for some input-selected \(J\)
\[
 \int_0^\tau \mathcal R_{>J,0}(t)\,dt
 \le \theta\nu\int_0^\tau\mathcal D_{>J,0}(t)\,dt+A,
\qquad \theta<1,                                    \tag{15}
\]
uniformly up to the maximal time. Here \(\mathcal R_{>J,0}\) and
\(\mathcal D_{>J,0}\) denote the limits of (6) and (5) over
\(I=[J+1,N]\) as \(N\to\infty\) and \(\epsilon\downarrow0\), whenever
those limits exist. This is a precise new producer, not a
consequence of (3): controlling (12) requires a one-sided strain/Carleson
input beyond kinetic energy. A time derivative normal form for the symmetric
part in (11) would also repair the route, but none is obtained here.

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

For a Schwartz solution at a fixed regular time, the rapid high-frequency
decay and the standard homogeneous low-frequency estimates permit
\(M,N\to\infty\) in (2)--(6). The band-boundary portions already retained in
\(C_j\) tend to zero. This produces the infinite-frame identity at every
strictly regular time. It does not provide estimates uniform as a putative
singular endpoint is approached; precisely that missing uniformity is (15).

## Frontier record

**MODE / RESULT:** DISCOVER/FALSIFY. The dyadic square energy has an exact
positive diffusion and cancels common transport, but the combined pressure
and transfer symbol leaves an indefinite low-frequency strain interaction.

**FIRST GAP:** obtain an input-only one-sided space-time bound for the
aggregate strain/Carleson coefficient in (12), together with the balanced
high--high shell form, or construct a temporal normal form for their symmetric
part. Energy and the tight-frame identity do not supply this bound.

**SURVIVING CONDITIONAL SUFFIX:** estimate (15), plus control of the finite
low-output portion, would give a cubic critical bound equivalent to
\(\|u\|_3^3\) and feed the existing continuation argument.

**NON-CLAIMS:** no new equivalence beyond the classical square-function
theorem is claimed. There is no universal HF estimate, endpoint bound,
blow-up construction, or global regularity theorem here.
