# Helical discovery period: actual pair production invisible to signed budgets

Date: 2026-09-07. Frozen repository base for provenance:
`ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.
Author derivations with an audit-requested solenoidal-packet repair.
Exact review inputs and current verdict are recorded in
2026-09-07-helical-production-audit.md.
No terminal NS theorem, singular solution, or canonical promotion.

## 1. Object and proposed consumer

For the original unforced equation on R3, fixed nu>0, put

    Lambda=|D|, C=Lambda^(-1) curl,
    P_+=(I+C)/2, P_-=(I-C)/2, u_+=P_+u, u_-=P_-u,
    E_+=(1/2)||Lambda^(1/2)u_+||_2^2,
    E_-=(1/2)||Lambda^(1/2)u_-||_2^2,
    S=E_++E_-=(1/2)||u||_(dot H^(1/2))^2.                (1.1)

The definitions concern solenoidal fields; the single Fourier point zero
does not affect the L2 multipliers. Helicity is

    H=integral u.curl u=2(E_+-E_-).

Both H and S are invariant under the NS rescaling of snapshots. The
proposed gain was an additional restriction on the creation of equal
positive/negative helicity, obtained from signed helicity transfer and
dissipation. An input-only bound on S over every finite horizon would give
the required L-infinity_t L3 input by homogeneous Sobolev embedding, then
continue the original smooth branch with its normalized pressure, trace,
and energy identity. No such bound is obtained below.

The decisive tests are actual full-Leray interactions and actual local NS
branches. No chiral sector is assumed invariant and no generic cascade
model is identified with NS.

## 2. Exact pair-production identity

Let B(u,u)=P[(u.grad)u] and set

    D_+=||Lambda^(3/2)u_+||_2^2,
    D_-=||Lambda^(3/2)u_-||_2^2,
    T_+=-<Lambda u_+,P_+ B(u,u)>,
    T_-=-<Lambda u_-,P_- B(u,u)>.

On every compact classical interval,

    E_+'=-nu D_+ + T_+,
    E_-'=-nu D_- + T_-.

The identity (u.grad)u=omega cross u+grad(|u|^2/2) gives
<curl u,B(u,u)>=0. Therefore

    T_+-T_-=-<curl u,B(u,u)>=0.

Writing T=T_+=T_- gives the exact balances

    S'=-nu(D_++D_-)+2T,
    H'=-2nu(D_+-D_-).                                    (2.1)

This is not an estimate of T. The nonlinear source is precisely common
pair production; it drops out of the signed balance before any inequality
is applied.

## 3. Actual branches with every radial signed-helicity budget zero

Let R=diag(1,1,-1) and act on polar velocity fields by

    (mathcal R u)(x)=R u(Rx).

Curl changes orientation:

    curl(mathcal R u)=-mathcal R(curl u).

Radial Fourier multipliers commute with mathcal R, so P_+ mathcal R=
mathcal R P_-. If u=mathcal R u, then E_+=E_- and D_+=D_-.
More generally, for every real radial multiplier m(Lambda) for which the
pairing is finite,

    <u,m(Lambda) curl u>=0.                               (3.1)

This includes bandwise signed helicity and signed helicity dissipation.
It is not merely cancellation of the total helicity across distant scales.

The original NS equation is invariant under this reflection, including
the reflected scalar pressure. Uniqueness of its local smooth branch
therefore preserves u=mathcal R u throughout that branch's smooth lifespan.
Thus (3.1) is an exact trajectory statement, not just a snapshot statement.

Nevertheless T can be strictly positive on a time interval, as follows.

### 3.1 Explicit full-equation triad calibration

Temporarily use normalized average on the 2pi-periodic three-torus and
define

    psi=A cos x+B cos(2y)+C0 cos(x+2y),
    U=(partial_y psi,-partial_x psi,0).

All nonlinear pairings below use the full convection and full Leray
projection. Only the three input carriers contribute to pairing with
Lambda U, so the calculation does not assume an invariant three-mode ODE.
The scalar vorticity is

    omega=A cos x+4B cos(2y)+5C0 cos(x+2y).

Projecting the instantaneous vorticity derivative -U.grad omega onto these
three carriers gives

    dot A=-B C0,
    dot B=A C0,
    dot C0=-(3/5) A B.                                   (3.2)

Other generated modes remain in the full derivative and are orthogonal
only to the pairing being evaluated. Since

    S(U)=(1/4)[A^2+8B^2+5 sqrt(5) C0^2],

the exact nonlinear critical production is

    Ncrit(U):=-<Lambda U,B(U,U)>
             =(7-3 sqrt(5)) A B C0/2.                    (3.3)

It is positive for A,B,C0>0, since 49>45. For comparison, the energy and
enstrophy derivatives from these same pairings vanish, with coefficients
-1+4-3=0 and -1+16-15=0 respectively. Those cancellations do not force
(3.3) to vanish.

### 3.2 Compact whole-space datum

Choose nonnegative nonzero theta in C_c^infinity(R3), even in z, and put

    theta_L(x)=theta(x/L),
    u_L=curl[theta_L(0,0,psi)].                            (3.4)

These are real compact smooth solenoidal data, with third component zero
and first two components even in z; hence mathcal R u_L=u_L. Product
estimates give

    u_L=theta_L U+O(L^(-1)) pointwise on its support,
    ||(u_L.grad)u_L-theta_L^2(U.grad)U||_2=O(L^(1/2)).

For each nonzero carrier k of U, Plancherel after rescaling the envelope
gives

    ||Lambda(theta_L exp(i k.x))
          -|k| theta_L exp(i k.x)||_2=o(L^(3/2)).

Dominated convergence is justified by the rapidly decreasing Fourier
transform of theta and the bound |k+zeta/L|<=|k|+|zeta|. The curl-cutoff
error has H1 norm O(L^(1/2)), hence the same harmless order after Lambda.
Because Lambda u_L is solenoidal, the Leray projection in Ncrit can be
removed from this pairing. Consequently

    L^(-3) Ncrit(u_L)
      -> (integral_R3 theta^3) (7-3 sqrt(5)) A B C0/2>0.   (3.5)

Fix any sufficiently large finite L. This is a legitimate compact datum
with strictly positive Ncrit, exact reflection symmetry, and no periodic
or infinite-volume trajectory assumption.

### 3.3 Strict growth of both chiral energies despite zero signed budgets

Fix the requested viscosity nu. For the datum u0=M u_L,

    Ncrit(u0)=M^3 Ncrit(u_L),
    D_+(u0)+D_-(u0)=M^2 ||Lambda^(3/2)u_L||_2^2.

Choose a finite M large enough that Ncrit(u0) exceeds the displayed
viscous term. Then S'(0)>0. Reflection gives E_+=E_-=S/2 throughout the
actual local solution, so both E_+'(0)>0 and E_-'(0)>0. By smoothness
these inequalities persist on some positive interval [0,tau]. On this
same interval EVERY signed radial helicity quantity in (3.1), including
H and D_+-D_-, is identically zero.

This proves the following scoped counterexample for every fixed nu>0:

    A compact smooth solenoidal NS datum can have an actual interval
    of simultaneous positive/negative chiral-energy growth while all
    radial signed-helicity histories and their signed dissipative
    budgets vanish identically.

Thus a proposed bound of cumulative positive pair production solely by
signed-helicity variation/dissipation, with a right side vanishing when
those signed data and histories vanish, is false. This includes shellwise
radial signed budgets. It does NOT exclude an estimate with a separate,
nonzero full-input cost, nor does it imply unbounded S on this branch.

## 4. Pure positive helicity also seeds the missing chirality

A separate initial-data test rules out closing the argument by assuming
that no minority helicity can be generated without pre-existing minority.
This is a full Leray numerator calculation, followed by a Schwartz packet
construction and an actual short-time expansion.

Use parent wavevectors a=(1,0,0), b=(0,2,0) and complex polarizations

    U=(0,1,i),       V=(i,0,1).

They obey

    a.U=b.V=0,
    i a cross U=|a| U,
    i b cross V=|b| V.

Thus both parents have positive helicity. At k=a+b=(1,2,0), the sum of
the two ordered convection coefficients, after Leray projection, is

    F=i P_k[(U.b)V+(V.a)U]=(-6/5,3/5,i).

The sign of the NS vector field is -F; its squared projection is unchanged.
Directly,

    |F|^2=14/5,
    <F,i k cross F>=6,
    |P_-(k)F|^2=(7-3 sqrt(5))/5>0.                       (4.1)

The bracket is the Hermitian pairing. Unequal parent lengths matter here;
equal-length pure Beltrami combinations can have vanishing Leray
nonlinearity. No claim that all parent choices force this daughter is made.

For actual R3 data the projection must first enforce solenoidality away
from the carrier centers. For xi!=0 define

    Q_+(xi)=(P(xi)+i xi cross/|xi|)/2=P_+(xi)P(xi).

Choose a real nonzero nonnegative even bump phi_delta in C_c^infinity, supported
in a sufficiently small radius-delta ball, and put

    u0_hat(xi)=Q_+(xi)[U phi_delta(xi-a)+V phi_delta(xi-b)
                +conjugate(U) phi_delta(xi+a)
                +conjugate(V) phi_delta(xi+b)].

The supports avoid zero; Q_+(-xi)=conjugate(Q_+(xi)) gives reality, and
xi.Q_+(xi)=0 gives exact solenoidality. Smooth compact Fourier support
gives Schwartz data, with P_-u0=0. Applying (I+C)/2 directly to arbitrary
constant-polarization bumps would not ensure solenoidality and is not used.
Near k only the two positive parent packets contribute to the named
daughter. At k their convolution divided by the positive integral
of phi_delta squared tends to F as delta tends to zero. Continuity of the
Leray and chiral symbols there, together with (4.1), proves that for finite
sufficiently narrow packets

    P_- B(u0,u0) != 0.                                   (4.2)

This uses no plane wave as the actual initial datum.

On the actual local smooth NS branch, the linear heat term preserves
chirality, so

    partial_t u_-(0)=-P_-B(u0,u0).

Taylor expansion in dot H^(1/2) gives

    E_-(t)=(t^2/2)||Lambda^(1/2)P_-B(u0,u0)||_2^2+o(t^2), (4.3)

with a strictly positive coefficient, for every fixed nu>0. Minority
energy is created even from exact pure-positive initial data. In
particular a homogeneous Gronwall closure

    E_-' <= a(t) E_-,      integral_0^tau |a(t)|dt<infinity,

would falsely preserve E_-=0. An additive creation term remains necessary.
Formula (4.3) does not rule out controlling that additive term by a genuine
new full-input estimate.

## 5. Checks, first gap, and exact conclusion

A bounded independent numerical calculation evaluated the full real-space
convection pairing of the trigonometric field on a 32 by 32 Fourier grid,
including all generated frequencies. For A=B=C0=1 it gave

    Ncrit=0.14589803375031513,
    (7-3 sqrt(5))/2=0.1458980337503153.

A separate vector-cross-product calculation gave the squared negative
daughter norm 0.058359213500126184, agreeing with (4.1). These are small
arithmetic checks of the written derivations, not independent mathematical
review or proof of a universal PDE statement. No external source or
priority claim is needed for the derivations in this note.

DECISIVE SCOPED RESULTS: the reflection-symmetric compact-data construction
in Section 3 and pure-chirality birth construction in Section 4. They test
actual local NS, arbitrary fixed viscosity, full Leray interactions, and
admissible whole-space data. Section 3 supplies an interval statement,
rather than inferring a sustained cascade from one instantaneous daughter.

FIRST GAP: a signed-helicity argument still needs a bound for the common
production T that remains nontrivial on reflection-symmetric trajectories
with every radial signed budget zero. A minority-helicity argument must
also pay for the strictly positive birth term (4.3). Neither the energy
identity nor signed helicity transfers supplies that bound here.

SURVIVING CONDITIONAL SUFFIX: an input-only finite-horizon bound for S
would imply L-infinity_t L3 and the original continuation target. No such
bound, and no rigorous singular solution, has been obtained.

NON-CLAIMS: these counterexamples do not exclude every use of helical
geometry, angularly resolved unsigned information, an additive full-input
cost, or additional dynamical constraints beyond the identities tested.
They do not establish a global chiral norm amplification rate or a
three-dimensional blow-up cascade.
