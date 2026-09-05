# HF01: a heat normal form for high-frequency pressure work

Status: discovery/falsification evidence for the unforced equation on
\(\mathbb R^3\).  This note constructs an explicit modified functional and
derives its exact evolution.  Its boundary value is controlled by energy, but
two resulting remainders are not.  No high-pressure estimate or global
regularity theorem is claimed.

## 1. Setup and target

Fix \(\nu>0\), a real-even homogeneous Littlewood--Paley partition, and an
integer \(J\).  Write \(Q_J=P_{>J}=I-S_J\), let \(\mathbb P\) be the Leray
projector, and put

\[
 N(u)=(u\cdot\nabla)u,\qquad w(u)=|u|u,qquad
 \mathcal H_J(u)=-\langle \mathbb P Q_Jw(u),N(u)\rangle.              \tag{1}
\]

All pairings are real \(L^2\) pairings.  For a strong Sobolev solution they
are justified on compact classical intervals.  Self-adjointness and
commutation of the real-even Fourier multipliers show that \(\mathcal H_J(u)\)
is exactly the signed high-output pressure work \(H_J\) in `frequency.md`:

\[
 \mathcal H_J(u)=\int_{\mathbb R^3}p_{>J},
                 u\cdot\nabla|u|\,dx.                              \tag{2}
\]

The desired producer would bound \(\int_0^\tau\mathcal H_J(u(t))dt\) by a
strict fraction of \(\nu\int_0^\tau D_3dt\) plus an input-only remainder.

## 2. An explicit dissipative normal form

Let \(G_s=e^{\nu s\Delta}\) and choose the parabolic cutoff time

\[
 a_J=\nu^{-1}2^{-2J}.                                             \tag{3}
\]

Define the quartic, non-polynomial functional

\[
 \boxed{\displaystyle
 \mathcal B_J(u)=-\int_{a_J}^{\infty}\mathcal H_J(G_su)\,ds.}       \tag{4}
\]

It is quartic under positive amplitude scaling because both \(w\) and \(N\)
are quadratic in magnitude.  The word “normal form” refers to inversion of the linear heat
generator along its semigroup, rather than to an oscillatory integration by
parts.

The integral converges and, crucially, its value is controlled by kinetic
energy.  The absolute pressure estimate from `frequency.md` gives

\[
 |\mathcal H_J(v)|\leq C\|v\|_6^3\|\nabla v\|_2.                    \tag{5}
\]

The heat estimates from \(L^2(\mathbb R^3)\) are

\[
 \|G_su\|_6\leq C(\nu s)^{-1/2}\|u\|_2,
 \qquad
 \|\nabla G_su\|_2\leq C(\nu s)^{-1/2}\|u\|_2.                    \tag{6}
\]

Consequently

\[
 |\mathcal H_J(G_su)|\leq C(\nu s)^{-2}\|u\|_2^4,
\]

and hence

\[
 \boxed{\displaystyle
 |\mathcal B_J(u)|
 \leq C\nu^{-1}2^{2J}\|u\|_2^4.}                                  \tag{7}
\]

For a Navier--Stokes trajectory, the energy identity makes (7) uniform in
time with \(\|u(t)\|_2\leq\|u_0\|_2\).  Thus
\(|\mathcal B_J(u(\tau))-\mathcal B_J(u(0))|\) is an admissible
input-only finite-horizon remainder (indeed independent of the horizon).

The lower limit in (4) is essential.  Estimate (5)--(6) behaves like
\(s^{-2}\), which is not integrable at zero.  Integrating from zero would
formally give the exact inverse of the heat derivative but would not give an
energy-controlled boundary functional.

## 3. Exact evolution identity

The map \(w(z)=|z|z\) is continuously differentiable, including at \(z=0\),
with

\[
 Dw(z)[h]=|z|h+\mathbf 1_{z\ne0}{z\cdot h\over|z|}z,
 \qquad |Dw(z)[h]|\leq2|z||h|.                                  \tag{8}
\]

For smooth fields, differentiation of (1) gives the explicit first variation

\[
 D\mathcal H_J(v)[h]
 =-\langle\mathbb P Q_JDw(v)[h],N(v)\rangle
  -\langle\mathbb P Q_Jw(v),(h\cdot\nabla)v+(v\cdot\nabla)h\rangle. \tag{9}
\]

Equations (5)--(6), followed if necessary by starting with Schwartz fields,
justify differentiating (4); extension to the strong solution follows by
the same approximation used for the critical balance.  Since
\(G_s\nu\Delta u=\partial_sG_su\),

\[
 \begin{aligned}
 D\mathcal B_J(u)[\nu\Delta u]
 &=-\int_{a_J}^{\infty}{d\over ds}\mathcal H_J(G_su)\,ds\\
 &=\mathcal H_J(G_{a_J}u),                                      \tag{10}
 \end{aligned}
\]

where the term at \(s=\infty\) vanishes by (5)--(6).  The projected
Navier--Stokes equation is

\[
 u_t=\nu\Delta u-\mathbb PN(u).                                  \tag{11}
\]

Therefore

\[
 {d\over dt}\mathcal B_J(u(t))
 =\mathcal H_J(G_{a_J}u)-D\mathcal B_J(u)[\mathbb PN(u)].         \tag{12}
\]

Rearranging gives the promised exact normal-form identity

\[
 \boxed{\displaystyle
 \mathcal H_J(u)
 ={d\over dt}\mathcal B_J(u)+\mathcal R_J^{\rm heat}(u)
                         +\mathcal R_J^{\rm tr}(u),}              \tag{NF}
\]

with

\[
 \mathcal R_J^{\rm heat}(u)
 :=\mathcal H_J(u)-\mathcal H_J(G_{a_J}u),                         \tag{13}
\]

\[
 \mathcal R_J^{\rm tr}(u)
 :=D\mathcal B_J(u)[\mathbb PN(u)]
 =-\int_{a_J}^{\infty}
 D\mathcal H_J(G_su)[G_s\mathbb PN(u)],ds.                       \tag{14}
\]

After time integration, (7) controls the boundary contribution in (NF).
Thus HF01 reduces the original high-pressure problem to the signed sum of
the short-heat defect (13) and the transport correction (14).  This is an
exact identity, not a proposed telescoping analogy.

## 4. Fourier denominator and absence of a heat resonance

For a polynomial quartic surrogate of (1), applying (4) to Fourier modes
\(\xi_1+\xi_2+\xi_3+\xi_4=0\) inserts the dissipative denominator

\[
 {e^{-\nu a_J\Omega}\over\nu\Omega},
 \qquad \Omega=|\xi_1|^2+|\xi_2|^2+|\xi_3|^2+|\xi_4|^2.            \tag{15}
\]

The high-output projector means that one quadratic output, say
\(\xi_1+\xi_2\), has size \(\gtrsim2^J\).  Hence

\[
 \Omega\geq|\xi_1|^2+|\xi_2|^2
 \geq\tfrac12|\xi_1+\xi_2|^2\gtrsim2^{2J}.                       \tag{16}
\]

There is therefore no nonzero-frequency heat resonance in the quartic
interaction and the inverse denominator gains two derivatives at the active
output scale.  Formula (4) is the physical-space version that remains
meaningful for the non-polynomial map \(|u|u\).

This does not remove the transport interaction.  Differentiating a quartic
functional along the quadratic vector field \(-\mathbb PN(u)\) creates the
quintic term (14).  A second normal-form step would create degree six, and so
on.  Without smallness or another summable parameter, no convergence of that
iteration follows for arbitrary large data.

## 5. Bounds attempted for the two remainders

### 5.1 The heat defect retains the unresolved active scales

By the fundamental theorem of calculus along the heat flow,

\[
 \mathcal R_J^{\rm heat}(u)
 =-\int_0^{a_J}D\mathcal H_J(G_su)[\nu\Delta G_su],ds.            \tag{17}
\]

This is exact but does not help at energy level: the singularity at \(s=0\)
is precisely the part excluded from the boundary functional.  Equivalently,
\(I-G_{a_J}\) has no small operator norm on an energy-class field whose
frequency is at or above \(2^J\).

For a concentrated snapshot \(u_N(x)=N\phi(Nx)\), take fixed \(J\) and
\(N/2^J\to\infty\).  Then

\[
 G_{a_J}u_N(x)
 =N\left(e^{(N^2/2^{2J})\Delta}\phi\right)(Nx),                   \tag{18}
\]

where viscosity cancels because \(\nu a_J=2^{-2J}\).  The heat-smoothed
profile tends to zero in every positive Sobolev norm (with polynomial decay
at low frequency), whereas

\[
 \mathcal H_J(u_N)=N^2P_3[\phi]+O_{\phi,J}(N^{-1})                 \tag{19}
\]

conditionally on \(P_3[\phi]\ne0\), as in `frequency.md`.  Hence
\(\mathcal R_J^{\rm heat}(u_N)\) retains the full \(N^2\) critical size in
that conditional test.  No such nonzero profile is constructed here, so
(19) is a mechanism test rather than a counterexample.  More generally,
the operator fact \(\|(I-G_{a_J})Q_J\|_{L^2\to L^2}=1\) already rules out
uniform smallness from frequency separation alone.

### 5.2 The transport correction is not energy-controlled

Substitution of (9) into (14) makes the obstruction explicit.  With
\(v_s=G_su\) and \(h_s=G_s\mathbb PN(u)\),

\[
 \begin{aligned}
 \mathcal R_J^{\rm tr}(u)=\int_{a_J}^{\infty}
 &\langle\mathbb P Q_JDw(v_s)[h_s],N(v_s)\rangle\\
 &+\langle\mathbb P Q_Jw(v_s),
        (h_s\cdot\nabla)v_s+(v_s\cdot\nabla)h_s\rangle\,ds.       \tag{20}
 \end{aligned}
\]

This is quintic in amplitude.  Energy controls \(u\) in \(L^2\), but at one
time it does not control \(N(u)=\nabla\cdot(u\otimes u)\) in a norm strong
enough to make (20) smaller than \(D_3\).  The elementary estimate

\[
 \|N(u)\|_{H^{-1}}\lesssim\|u\otimes u\|_2=\|u\|_4^2              \tag{21}
\]

already introduces an instantaneous \(L^4\) norm.  Interpolation gives
\(\|u\|_4^2\lesssim\|u\|_2^{1/2}\|\nabla u\|_2^{3/2}\), whose powers exceed
the available pointwise energy control and whose insertion into the
quartic derivative produces still higher products.  The energy identity does
not furnish an \(L^1_t\) bound for (20).

Equation (21) is only diagnostic; it is not asserted to be the optimal
estimate.  Proving a signed cancellation between (13) and (20), or between
(20) and \(\nu D_3\), remains a possible route.  Bounding their absolute
values by the estimates above does not close it.

## 6. Scaling and sign falsifiers

Under the Navier--Stokes scaling

\[
 u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

shift the cutoff simultaneously by \(J\mapsto J+\log_2\lambda\) (first for
dyadic \(\lambda\)).  Then \(a_{J+\log_2\lambda}=\lambda^{-2}a_J\), and direct
changes of variables give

\[
 \mathcal H_{J+\log_2\lambda}(u_\lambda)=
 \lambda^2\mathcal H_J(u),qquad
 \mathcal B_{J+\log_2\lambda}(u_\lambda)=\mathcal B_J(u).         \tag{22}
\]

Thus \(d\mathcal B_J/dt\), both remainders, and \(\nu D_3\) all scale like
\(\lambda^2\).  Bound (7) is also invariant under the paired cutoff shift:
\(2^{2J}\|u\|_2^4\) is unchanged.  The normal form respects critical scaling
but obtains no subcritical gain.

There is no algebraic sign.  Under amplitude reversal \(u\mapsto-u\),

\[
 w(-u)=-w(u),\qquad N(-u)=N(u),qquad
 \mathcal H_J(-u)=-\mathcal H_J(u),                              \tag{23}
\]

while \(D_3[-u]=D_3[u]\).  Therefore any universal one-sided sign rule such
as \(\mathcal H_J\leq0\) would force \(\mathcal H_J\equiv0\).  Reversal alone
does not refute a two-sided relative bound
\(|\mathcal H_J|\leq c\nu D_3\); it only rules out obtaining absorption from
a bare sign.  The note does not
construct a field with nonzero \(\mathcal H_J\), so (23) is a conditional
sign falsifier.  Also, \(-u(t)\) is not generally a Navier--Stokes solution
when \(u(t)\) is; (23) tests an algebraic snapshot argument, not a signed
time-integrated trajectory law.

## 7. Result and first obstruction

**Exact new identity.**  Equations (4), (7), and (NF) give an explicit heat
normal form for the high pressure work.  Its time-boundary contribution is
bounded solely by \(\nu,J\), and initial kinetic energy.

**First failed bridge.**  Starting the heat inverse at the positive parabolic
time \(a_J\) is necessary for an energy-controlled boundary functional, but
leaves the short-time defect (13).  That defect has no small energy-level
factor on frequencies \(\gtrsim2^J\).  Starting at zero removes the defect
but makes the proposed boundary integral divergent under the available
energy estimate.  The nonlinear transport correction (14) is a second,
quintic obstruction with no energy-level time bound.

**Conditional suffix.**  If one proves, for an input-chosen \(J\) and all
\(\tau<\min\{H,T_*\}\),

\[
 \int_0^\tau
  (\mathcal R_J^{\rm heat}(u(t))+\mathcal R_J^{\rm tr}(u(t)))dt
 \leq\theta\nu\int_0^\tau D_3(t)dt+A(\nu,u_0,H,J),                \tag{24}
\]

with \(\theta<1\) and a noncircular input-only finite \(A\), then integration
of (NF) and (7) proves the high-pressure lemma (HF).  The known low-frequency
bound then gives pressure absorption and the conditional ESS continuation
chain.  Equation (24) is unproved.

**Non-claims.**  Heat denominators remove the linear dissipative resonance;
they do not control the active short-time defect or the transport-generated
quintic term.  No small-data assumption is substituted for arbitrary data,
no profile with nonzero pressure work is asserted, and no Clay alternative is
resolved.

**Reopening condition.**  This normal form becomes viable if a new signed
estimate absorbs the combined remainder in (24), or if a different modified
functional includes the interval \([0,a_J]\) while retaining an energy-level
boundary bound.  An absolute estimate that assumes the unknown critical norm
does not reopen the route.
