# Full-state return blocks: a dissipative price without spatial compactness

Date: 2026-09-08. Frozen input main:
`9c69d7637dce58b1b0c251bcadd8ee1bc9919c74`.
Status: AUTHOR PROOF using the inspected Chae--Wolf Euler theorem;
independent mathematical audit PENDING. No canonical graph promotion.
Original unforced R3 NS, ordinary positive viscosity, canonical pressure,
and the entire inherited state throughout. No NS-R3 resolution is claimed.

## 0. Exact consumer and improvement over the current frontier

The positive terminal producer is still the every-upper-time, M-uniform
bound, for one fixed finite q>3,

    integral_0^t Pi_q,M <= nu integral_0^t D_q,M+C(d,nu,H,N0,q).

Together with the exact RF identity, initial Schwartz shells,
RF-LQ-SYNTHESIS, RF-LOCAL-ID, Lorentz Fatou, RF-LQ-CONTINUATION, LOCAL
and ENERGY, it would imply NS-R3 with normalized pressure. This note does
NOT supply that producer or extract the required events from arbitrary
hypothetical blowup.

The actual consumer here is a general cascade-construction exclusion:

    long efficient full-state return + bounded endpoint normalized energy
      + bounded normalized Lipschitz tubes and turnover clocks
        -> a definite normalized ORDINARY VISCOUS expenditure (Theorem 2);
    additionally bounded normalized enstrophy tubes at high amplitude
        -> no such long return block (Corollary 3).

Unlike the predecessor full-state-vorticity-return theorem, these statements
need NO spatial compactness, no small-power vorticity integrability, no
uniform compression constant, and no uniform high Sobolev norm. They allow
noncompact and tail-accreting states. Only the first and last normalized
L2 norms must be bounded; intermediate normalized L2 norms may be arbitrarily
large. Scales, gains, translations, phases, and polarization can vary.
There is no upper bound on the scale or amplitude ratios.

The no-energy-atom rigidity is published prior art [CW], not a new theorem
claimed here. The finite positive-viscosity cost and its full-state return
adapter below are the contributions relative to the frozen repository.
No exhaustive priority search or independent mathematical audit is claimed.

## 1. A uniform vanishing-viscosity endpoint lemma

Use squared kinetic energy E(v)=||v||2^2, without a factor 1/2. Pressures
are always the canonical double-Riesz pressures p=R_i R_j(v_i v_j).

**Lemma 1.** Fix finite Ebar,A and m>0. There exist r_*>0 and eps_*>0,
depending only on Ebar,A,m, such that the following is impossible for a
smooth original NS solution v on [-1,0] with viscosity eta>0:

    sup_[-1,0] E(v) <= Ebar,
    sup_(-1,0) (-s)||grad v(s)||infinity <= A,
    eta <= eps_*,
    D:=2 eta integral_-1^0 ||grad v||2^2 <= eps_*,
    integral_B(x,r_*) |v(0)|^2 >= m for some x in R3.       (1.1)

Smoothness and finite Sobolev norms are required for each solution, not
uniform high-derivative bounds for the family. The statement is qualitative:
no computable value for either threshold is supplied.

**Proof.** If the conclusion fails, choose solutions v_j with eta_j,D_j
both tending to zero and final balls with radii tending to zero carrying
mass at least m. Translate each entire solution so its final ball is centered
at zero. Translation changes neither equation, energy, nor pressure relation.

The elementary finite-energy Lipschitz interpolation inequality in dimension
three gives

    ||v_j(s)||infinity <= C Ebar^(1/5)
                                ||grad v_j(s)||infinity^(3/5)
                      <= C(Ebar,A)(-s)^(-3/5).            (1.2)

For example, at a point where the speed is near its supremum U, a ball of
radius proportional to U/||grad v||infinity has speed at least U/2. Its
energy bounds U^5/||grad v||infinity^3. This proves (1.2), including the
zero-gradient case by finite energy. In particular the right side is
integrable in time. The actual Riesz pressure satisfies

    ||p_j(s)||2 <= C ||v_j(s)||infinity ||v_j(s)||2.        (1.3)

On each compact time interval strictly below zero, local H1 bounds follow
from the gradient bound, and the equation bounds the time derivative in
H^(-2): v_j tensor v_j is bounded in L2, the Leray projector is bounded
on L2, and eta_j Delta v_j is bounded in H^(-2). Apply a fixed compact
spatial cutoff. Rellich compactness and the time equicontinuity (interpolate
H^(-2) with the local H1 bound) give a subsequence converging in C_t L2_loc.
A diagonal covers every compact spatial set and every compact time interval
below zero. The limit v has global L2 norm at most sqrt(Ebar), is divergence
free, and retains the global Lipschitz bound at each such time. The velocity
bound (1.2) also passes to the limit.

This is LOCAL convergence; global tightness of kinetic energy is not assumed.
Nevertheless the limiting equation has the actual canonical pressure. On
a fixed spatial ball, split the double-Riesz pressure into stresses within
a larger ball and stresses outside it. Products converge strongly in L2
on the larger ball, since velocities converge locally in L2 and are uniformly
bounded. The far kernel has size C|z|^(-3), so its contribution on the
smaller fixed ball is at most C Ebar R^(-3) when the separation is R.
Its gradient is bounded by C Ebar R^(-4). Taking j to infinity, then R to
infinity, identifies the limit pressure with R_i R_j(v_i v_j). In particular
no pressure or hidden harmonic forcing is discarded with escaping energy.
The viscosity term vanishes distributionally. Thus v solves ORIGINAL Euler
and belongs to

    L-infinity_t L2_sigma intersect L-infinity_loc,t W1,infinity,
    sup_(-1,0) (-s)||grad v(s)||infinity <= A.              (1.4)

One may restrict to [-1/2,0) and rescale time if an initial-endpoint
representative is needed; this does not affect the endpoint argument.

It remains essential to pass the FINAL energy, not just the equation.
For every compact smooth real test phi, the full NS local energy identity is

    partial_s |v_j|^2 + div[(|v_j|^2+2p_j)v_j]
         = eta_j Delta |v_j|^2 - 2 eta_j |grad v_j|^2.     (1.5)

Equations (1.2)--(1.3) imply, for -1<s<0,

    |integral (|v_j(0)|^2-|v_j(s)|^2) phi|
      <= C(Ebar,A)||grad phi||infinity (-s)^(2/5)
         +eta_j Ebar ||Delta phi||infinity (-s)
         +||phi||infinity D_j.                            (1.6)

Indeed the absolute spatial energy flux is bounded by
C Ebar ||v_j(s)||infinity. The last term in (1.6) is the ENTIRE viscous
energy loss; it has not been set to zero before the limit.

Take a weak-* subsequential limit sigma of |v_j(0)|^2 dx as finite
measures. Pass j to infinity at a fixed s<0 in (1.6), using local strong
convergence, then take s up to zero. This identifies sigma with the final
energy trace of v. The inspected Chae--Wolf Corollary 1.2 [CW] says precisely
that a whole-space Euler solution in (1.4) has an energy trace without atoms.
It permits any finite A; no smallness or vorticity-tail assumption is added.

On the other hand, a nonnegative cutoff equal to one on B(0,r) and supported
in B(0,2r) has sigma integral at least m for every r>0: all sufficiently
late j have their mass-m final ball inside B(0,r). Sending r to zero gives
sigma({0})>=m. This contradiction proves the uniform thresholds. QED.

## 2. The complete return state and the finite-block cost

Use exactly the predecessor's multiplier Q_K: psi supported in (2/3,5/3),
0<=psi<=1 and equal to one on [3/4,3/2], in angular frequency. Write G for
the actual convolution kernel of Q_1, so Q_1 V=G*V. The entire normalized
state and viscosity are

    V(y)=u(t,x+y/K)/(a K),
    a=K^(1/2)||Q_K u(t)||2,
    mu=nu/a,
    ||Q_1 V||2=1.                                        (2.1)

The full W flow from V has viscosity mu. At time theta the exact return is

    g=sqrt(lambda)||Q_lambda W(theta)||2,
    Vplus(z)=(g lambda)^(-1) O^T W(theta,c+Oz/lambda),
    muplus=mu/g,  aplus=g a,  Kplus=lambda K.               (2.2)

Here O is any rotation and c any translation. No output projection, mode
deletions, resets, or independent pressure choices are permitted. We use
(2.2) only when the actual smooth flow and the nonzero selected annulus
exist. It is still a partial augmented map, not a global event selector.

Fix constants

    M0>=1, L>0, 0<theta0<=Theta,
    lambda0>1, g0>1, gamma_*>0.                           (2.3)

Consider N consecutive applications of (2.2), with

    theta0 <= theta_n <= Theta,
    lambda_n >= lambda0,  g_n >= g0,
    sup_(0<=tau<=theta_n)||grad W_n(tau)||infinity <= L,   (2.4)
    ||V_0||2, ||V_N||2 <= M0,
    gamma_1(V_N) >= gamma_*.

There is NO upper normalized L2 hypothesis at intermediate returns and
NO spatial localization or compactness hypothesis anywhere. All the tube
bounds are for the full W_n, including inherited exterior and slow fields.
Only the FINAL endpoint must be efficient. The intermediate forward gains
and the genuine nonlinear clocks still concern the actual trajectory.

Reset units at the first endpoint so a_0=K_0=1 and reconstruct the single
original solution u with viscosity mu_0. Set

    a_n=product_(j<n) g_j,   K_n=product_(j<n) lambda_j,
    D_n=a_n K_n^2,  t_(n+1)-t_n=theta_n/D_n,
    T=t_N,  E_n=||u(t_n)||2^2,
    Dblock=2 mu_0 integral_0^T ||grad u||2^2=E_0-E_N.       (2.5)

D_n is a frequency/amplitude clock, distinct from Dblock and the RF D_q,M.

**Theorem 2 (positive full-block viscous expenditure).** There exist
N_* in N and mu_*,delta_*>0, depending only on (2.3) and psi, such that
any block satisfying (2.4), with N>=N_* and 0<mu_0<=mu_*, obeys

    Dblock > delta_*.                                    (2.6)

Thus a long high-amplitude return in this class cannot be essentially
energy-conservative. This is a complete-interval statement, not a Taylor
coefficient or a boundary tangency condition. It does not assert that such
blocks exist, or that the cost is paid by a particular exterior component.

**Proof.** Let

    r=g0 lambda0^2>1,
    Tbar=Theta/(1-r^(-1)),
    A=L Tbar.

Since D_(n+1)>=r D_n, geometric summation gives

    theta0<=T<=Tbar,
    T-t <= Tbar/D_n for t_n<=t<=t_(n+1),
    (T-t)||grad u(t)||infinity <= A.                      (2.7)

The physical gradient in that interval is bounded by L D_n. Translations
and rotations do not change this bound. By the full energy identity,
E(t)<=E_0<=M0^2. Hence the entire finite block has a derived Euler-Type-I
gradient bound relative to its endpoint. No Type I hypothesis about an
arbitrary NS singularity is being assumed or extracted.

Next the efficiency gives a localized piece of kinetic energy without
assuming localization of the rest. Put v=Q_1 V_N. Then ||v||2=1, and

    gamma_1(V_N)<=||v||infinity||grad v||2
                   <=(5/3)||v||infinity.                 (2.8)

Choose y with |v(y)|>=b:=3gamma_*/10. Choose R so

    M0 ||1_(|z|>R)G||2 <= b/2.

The convolution and Cauchy--Schwarz, retaining both parts of V_N, give

    integral_B(y,R)|V_N|^2 >= m0:=b^2/(4||G||2^2)>0.       (2.9)

If Dblock<=1/2, then E_N>=1/2 since E_0>=||Q_1 V_0||2^2=1.
The exact physical energy scaling is

    E_N=(a_N^2/K_N)||V_N||2^2.

Consequently a final PHYSICAL ball of radius R/K_N carries energy at least
m0/(2M0^2). Its center can be arbitrary; no translation bound is needed.

Apply Lemma 1 with

    Ebar=Tbar^2 M0^2,
    m=theta0^2 m0/(2M0^2),  A as in (2.7).

Indeed the whole solution

    v(s,x)=T u(T(s+1),x),  -1<=s<=0,                     (2.10)

has viscosity eta=T mu_0, pressure T^2 p(T(s+1),x), squared energy at most
Ebar, the same Type-I gradient constant A, and total dissipation T^2 Dblock.
Its final small ball has mass at least m. This time-amplitude change is an
exact NS change of variables, not a same-viscosity spatial dilation.

Let r_*,eps_* be supplied by Lemma 1. Choose N_* so R/lambda0^N_*<=r_*,
choose mu_*<=eps_*/(2Tbar), and put

    delta_* = min(1/4, eps_*/(2Tbar^2)).                  (2.11)

A block with Dblock<=delta_* would satisfy every forbidden condition in
(1.1). This proves (2.6). QED.

## 3. Bounded full enstrophy excludes long returns, even in noncompact classes

**Corollary 3.** Add just the full normalized enstrophy bound

    sup_(n,tau)||grad W_n(tau)||2 <= M1<infinity.           (3.1)

Then there are N_* and mu_**>0 depending only on the displayed constants
and psi such that NO block as above has N>=N_* and mu_0<=mu_**.
No high Sobolev, small-power vorticity, or spatial compactness bound is needed.

Proof. On interval n, exact change of variables gives

    2 mu_0 integral_(t_n)^(t_(n+1)) ||grad u||2^2
       =2 mu_0 (a_n/K_n) integral_0^theta_n ||grad W_n||2^2. (3.2)

Normalization gives ||V_n||2>=1 at EVERY endpoint, whether its full energy
is bounded or not. Thus a_n^2/K_n<=E_n<=M0^2 and a_n>=g0^n. Therefore

    Dblock <= C_D mu_0,
    C_D=2 Theta M1^2 M0^2/(1-g0^(-1)).                    (3.3)

For mu_**<=min(mu_*,delta_*/(2C_D)), (3.3) contradicts Theorem 2. QED.

In particular no infinite exact full-state orbit with the uniform tube
bounds and clocks above can have an infinite subsequence of returns for
which BOTH ||V_n||2<=M0 and gamma_1(V_n)>=gamma_*. Start sufficiently far
along this subsequence so mu_n=nu/a_n<mu_**, then end sufficiently many
turnovers later at another such endpoint. Corollary 3 gives the contradiction.
This also excludes fixed points, periodic returns and noncompact invariant
sets in the stated bounded class. It does not prove existence of any orbit.

Only endpoint gamma was used to separate this theorem from the passive
spectral-mixing example. No inference of regeneration from high frequency
or a large critical Sobolev norm is involved. The hypotheses do not assert
that Q_1 V alone drives the transition; they constrain the actual full flow.

## 4. The cost is not yet the terminal budget

Undoing the first normalization, (2.6) reads

    (K_start/a_start^2) 2 nu integral_block ||grad u||2^2
          > delta_*.                                    (4.1)

For disjoint blocks the actual ENERGY consumer supplies only

    sum_blocks (a_start^2/K_start) Cost_block <= ||d||2^2,
    Cost_block=(K_start/a_start^2)2nu integral_block||grad u||2^2.

The physical weight a_start^2/K_start can tend to zero. There is no lower
input-only bound for it here. Hence infinitely many positive NORMALIZED
costs need not contradict the finite PHYSICAL energy budget. This distinction
prevents an invalid RF-q promotion. Without (3.1), Theorem 2 forces genuine
viscous work, not global regularity.

Nor do finite input energy and efficient critical packets imply ||V||2<=M0:
||V||2^2=K||u||2^2/a_K(u)^2. A concentrating critical core can carry vanishing
kinetic energy while a large, dynamically weak low-frequency exterior makes
this full-state ratio diverge. The predecessor's small-power satellites do
not settle this different dynamical issue. It must be tested on whole finite
flow intervals, not repaired by dropping the bulk in (2.1).

The new dominant nut is the actual critically concentrating return with
inherited exterior in the regime outside this theorem: in particular
vanishing core-energy fraction / unbounded normalized full energy, or
unbounded normalized gradients or failing fixed turnover clocks. Construct
and shadow that full-state recurrence, OR prove a required critical cost,
extract those events from hypothetical blowup, and feed the Section 0
consumer. This note does not claim a reduction of all blowup to one of
these return parametrizations.

## 5. Original-operator discriminator and source boundary

The essential original identities are the local energy/pressure flux (1.5)
and, in the imported Euler rigidity, material vorticity transport. Tao's
averaged operator has the global energy cancellation but is not the original
local cubic transport with pressure R_i R_j(u_i u_j). If C denotes that
averaged quadratic source and N the original one, its local energy equation
has the additional term 2u dot(C(u,u)-N(u)) on the right of (1.5).
Global cancellation only makes this term's spatial integral zero; it does
not remove it from (1.6). Its curl likewise adds a source to the original
material-vorticity equation. Thus the proof cannot be transferred using
energy cancellation and norm estimates alone. No unproved universal
sign of local pressure is used.

[CW] D. Chae and J. Wolf, *Energy Concentrations and Type I Blow-Up for the
3D Euler Equations*, arXiv:1706.02020v2 (21 May 2018),
https://arxiv.org/pdf/1706.02020 . Directly inspected the full statement of
Corollary 1.2 and Theorem 1.1 on printed p.3, including a rendered page;
the proof's material-vorticity endpoint on printed p.27 was also inspected.
We use only the whole-space corollary: finite-energy, locally W1,infinity
Euler flow and finite sup (-t)||grad v||infinity imply an atomless final
energy measure. This is an imported theorem, not independently reproved
or formally verified here. It is not a Navier--Stokes regularity theorem.

[T] T. Tao, *Finite time blowup for an averaged three-dimensional
Navier--Stokes equation*, arXiv:1402.0290v3,
https://arxiv.org/html/1402.0290v3 . Inspected the averaged-operator definition
and energy-cancellation scope. The earlier packet audit's concrete original
convolution/support discriminator is preserved, not reclassified as a
positive producer.

The new exact checker verifies only finite identities: NS scaling, local
energy product rule, turnover clocks, geometric sums, localization constants,
and dissipation transformations. No computational search for a recurrent
state, independent audit, interval PDE validation, or positive regenerative
turnover is claimed. The thresholds N_*,mu_*,delta_* remain qualitative.
