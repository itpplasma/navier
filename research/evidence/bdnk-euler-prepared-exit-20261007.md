# Euler-prepared kinetic-cone exit across conformal BDNK frames

2026-10-07. Base: `itpplasma/navier@a08f84bcb7d4e3b968659948d2db4e86ba3a7a73`.
Status: **AUTHOR PROOF; independent reconstruction pending**.
This strengthens the kinetic-exit construction, not the PDE blow-up claim.

## 1. What is improved

The preceding kinetic-exit example used an adjustable initial rest heat flux.
Here BOTH the frame energy correction A and heat flux Q vanish on the entire
initial slice. The complete primitive Cauchy data and initial physical stress
are the same across frames at fixed shear viscosity. Thermal curvature, not
an imposed heat-flux gradient, drives the pressure out of the kinetic cone.
All four unforced conservation equations are retained.

**Theorem.** Fix eta0>0 and any conformal causal BDNK frame in the stated local
well-posedness sector. The analytic Euler-prepared family below contains data
whose initial stress is realizable by a smooth positive massless distribution,
with nonnegative initial canonical entropy production, but whose smooth local
BDNK evolution develops negative directional pressure. This holds for frame A,
frame B, and the other positive causal coefficient choices. For any FIXED
finite collection of frames, one sufficiently small delta works simultaneously.
No uniform exit time over unbounded frame-parameter sets is asserted.

At the pressure-exit event the solution still has positive temperature,
bounded velocity and derivatives, satisfies the dominant energy condition,
and has positive canonical entropy production at the event point. Those
properties alone therefore do not preserve positive classical particle
realizability. The shear correction is already order one initially; these
are NOT near-equilibrium stress data.

The model, notation and primary tensor sources are precisely those in
`bdnk-transfer-20261007.md` and `bdnk-kinetic-exit-20261007.md`:
Pandya--Pretorius, https://arxiv.org/html/2104.00804v2 , (13)--(16), (54)--(56);
Clarisse et al., https://arxiv.org/html/2510.16603v1 , (10)--(23).
The construction below is our own argument, not a theorem attributed to them.

## 2. Common Euler-prepared Cauchy data

Use a flat 3-torus, with dependence initially on x=x1. Fix K>=4 and define

    0<delta<=1/6, a=(1-3delta)/(4eta0), k=K/eta0, b=1/(12K^2),
    r=(a/k)sin(kx), ell=log Theta=b[cos(kx)-1],
    g=cosh r, p=sinh r, d=r_x, h=ell_x, D0=3+2p^2,
    ell_t=(-d-2gp h)/D0,
    r_t=(-2gp d-3h)/D0.                                         (1)

Set u=(g,p,0,0); specify u_t=r_t(p,g,0,0), Theta_t=Theta ell_t. The x1
period is 2pi/k. These are analytic, positive-temperature, normalized data.
The derivative data are EXACTLY the relativistic ideal Euler time derivatives:

    3D ell+theta=0, Du+Delta grad ell=0.

Consequently A0=Q0=0 for every chi0,lambda0; no frame parameter enters (1).
The expansion and complete rest-frame stress are

    theta0=3(gd-ph)/(3+2p^2),
    Erest=Theta^4, P_L=Theta^3(Theta-4eta0 theta0)/3,
    P_T=Theta^3(Theta+2eta0 theta0)/3,
    T_rest=diag(Erest,P_L,P_T,P_T).                              (2)

The shear is not set to zero: its longitudinal eigenvalue is 2theta0/3 and
its two transverse eigenvalues are -theta0/3. Thus the initial BDNK tensor
is identical across frames with the same eta0, including its dissipative part.

## 3. Positivity on the full initial torus

One has |r|<=1/(4K)<=1/16, Theta>=exp(-2b)>=1-2b, and
h=-bk sin(kx), so -ph>=0. Writing C=cos(kx), the bounds 0<3g/(3+2p^2)<=1
and |p|<=2(a/k)|sin(kx)| give

    theta0>=-a.

If C>=0, theta0<=a[C+2b(1-C^2)]<=a[1-(1-4b)(1-C)]. It follows that

    Theta-4eta0 theta0
      >=3delta+[(1-3delta)(1-4b)-b](1-C)
      >=3delta+(31/64)(1-C)>0.                                 (3)

If C<0, theta0<=2ab, hence Theta-4eta0 theta0>=1-4b>=47/48.
Also Theta+2eta0 theta0>=1-2b-1/2>=47/96. Both pressures in (2) are
therefore positive everywhere and P_L+2P_T=Theta^4.

The positive smooth kinetic realization in section 4 of the preceding packet
applies with energy normalization Theta^4, mean m=0 and z=P_L/Theta^4 in (0,1).
Use equal positive circle weights, an inverse-adjusted spherical heat-kernel
smoothing, a smooth compact radial distribution, and the specified local boost.
Thus f0>=0 is smooth with bounded momentum support and exactly the FULL initial
BDNK stress. No signed-particle or indefinite initial moment is introduced.

The canonical entropy identity gives on this initial slice

    partial_mu S^mu=(4eta/3Theta)theta0^2>=0,                    (4)

because A0=Q0=0. This is exact for the chosen PDE and canonical current.

## 4. The decisive full-PDE time jet

At the reflection center x=0:

    Theta=1, r=r_t=h=0, theta0=a, ell_t=-a/3,
    ell_xx=-bk^2=-1/(12eta0^2),
    theta_t=r_xt=-2a^2/3-ell_xx,
    eta_t=-eta0 a.

Stress conservation, not an independent scalar model, supplies
(Erest)_t=-partial_x T01=-4a/3+4eta0 a^2/3. Differentiating the full
longitudinal rest pressure P_L=(epsilon+A)/3-4eta theta/3 then gives

    partial_t P_L(0,0)
       =-4a/9+(8/3)eta0 a^2+(4eta0/3)ell_xx
       =[-1-12delta+27delta^2]/(18eta0)
       <=-1/(18eta0),
    P_L(0,0)=delta.                                            (5)

Again A_t is not discarded just because A0=0. Its contribution is contained
in (Erest)_t, as forced by the energy equation. The other nontrivial momentum
equation determines the remaining time derivatives in the actual local solution.

For clarity, the normal-time principal determinant of the coupled (ell,r)
equations, divided by the positive common temperature factor, is

    Dtime=3chi0 lambda0 gamma^4
          -2chi0(2eta0+lambda0)gamma^2 p^2
          +lambda0(chi0-4eta0)p^4/3
         =3chi0 lambda0 (gamma^2-z_+ p^2)(gamma^2-z_- p^2)>0.     (6)

Here z_+,z_- are the rest squared characteristic speeds. Causality gives
0<=z_+,z_-<=1 and gamma^2-p^2=1. For frame A the determinant is
25eta0^2(56gamma^4+152gamma^2+17)/18; for frame B it is
75eta0^2(24gamma^2+1)/28. These are strictly positive even in the luminal case.

The analytic equations can therefore be solved for ell_tt,r_tt.
Cauchy--Kowalevski, with delta as a nondifferentiated analytic parameter, gives
a common positive local interval and continuous pressure time jets for delta
near zero. Compactness supplies periodic patching. The transverse conservation
equations vanish identically under this longitudinal plane symmetry; their
constitutive stresses were included in deriving (2) and (5).
After shrinking the common interval, P_L,t(t,0)<=-1/(36eta0). For sufficiently
small delta, t_delta=72eta0 delta lies in that interval and

    T11_BDNK(t_delta,0)=P_L(t_delta,0)<=-delta<0.                 (7)

No norm diverges here. Standard local hyperbolic continuous dependence extends
the strict outcome, for each fixed delta, to a neighborhood of compatible
smooth three-dimensional Cauchy data. The analytic plane solution alone already
establishes the stated existential theorem in the full 3+1 equations.

## 5. Physical diagnostics at the exit event

As delta tends to zero, the event time tends to zero, Erest tends to 1,
P_L tends to 0, P_T tends to 1/2, and Q(t,0)=0 by reflection symmetry.
Thus for all sufficiently small delta, Erest>|P_L| and Erest>|P_T| at the
event. The dominant (hence weak) energy condition holds there. Likewise the
canonical entropy production tends to 1/(12eta0)>0 and remains positive.
Yet (7) forbids any representation T^{mu nu}=integral p^mu p^nu f d^3p/p^0
with f>=0. The kinetic obstruction is stronger than these familiar diagnostics.

For the positive f0 realizing (2), massless free transport gives the global
smooth solution f(t,x,p)=f0(x-t p/|p|,p) and nonnegative T11 forever. It has
exactly the same initial stress, so its directional stress differs from BDNK
by at least delta at (7). This is a stress-level comparison, not a derivation
of finite-viscosity BDNK from collisionless transport. Momentum-space derivatives
of the realizing f0 need not be bounded uniformly as delta tends to zero.

This concerns the MATTER stress of a positive classical particle model.
Electromagnetic field stress can have negative directional stresses (magnetic
tension), and interacting/quantum matter is not identified with this kinetic
cone. No claim about the total stress of arbitrary Vlasov--Maxwell plasmas,
all microscopic theories, or generic unphysicality is inferred from T11<0.
The chosen BDNK problem has no electromagnetic field component.

## 6. A model-independent constraint on a proposed repair

The earlier virial mechanism is not peculiar to one BDNK coefficient. Any
symmetric conserved trace-free stress with an equilibrium exterior and a
strictly subluminal smooth disturbance front obeys the same contradiction
for sufficiently energetic hot-core data if its energy stays nonnegative.
A repair retaining all those hypotheses must allow a luminal front, abandon
smooth continuation, or fail positive energy. Frame B passes that necessary
front-speed test but fails the separate kinetic-cone test above.

More generally set D(t)=integral[(T00-sum_i Tii)-(bar_T00-sum_i bar_Tii)].
Without assuming a trace-free stress, compact perturbation conservation gives

    I(t)=I0+2F0 t+E t^2-2 integral_0^t (t-s)D(s)ds.              (8)

With nonnegative T00 and support radius L=R+ct, the same ball calculation
therefore requires

    2 integral_0^t(t-s)D(s)ds
       >=I0+2F0t+E(t^2-L^2)-(8pi/15)bar_e L^5.                 (9)

A nonconformal correction must supply this actual trace budget if it is to
repair that positive-energy/front contradiction. A new model name alone does
not do so. The coefficient of the background allowance uses only bar_T00=bar_e;
D includes the full background trace subtraction.

There is also an observer-uniform sufficient bound for positive energy in
BDNK. In the hydrodynamic rest frame put pi=-2eta sigma and define

    Rcorr=|A|/epsilon+2|Q|/epsilon+||pi||op/epsilon.

For every inertial observer, |T00-T00_ideal|/T00_ideal<=Rcorr. This follows
from T00_ideal=epsilon(4gamma^2-1)/3>=epsilon gamma^2, |Q0|<=gamma|Q|,
and |pi00|<=gamma^2||pi||op. Hence Rcorr<1 implies positive energy for all
observers. The strict-front hot-core theorem forces breakdown OR Rcorr>=1
by its deadline. It cannot remain a uniformly small constitutive correction.

## 7. Current boundary of the result

The result now uses common Euler-prepared data across frames, a positive
kinetic initial realization, and a verified full-PDE local producer of cone
exit. The cost is explicit: eta0 theta is near 1/4, so the stress anisotropy
is order one. Increasing K makes velocity and temperature AMPLITUDES small,
not the complete derivative data or inverse-Reynolds correction.

No argument here proves a global smooth kinetic parent with the SAME finite
viscosity, or determines whether the ideal-prepared virial hot cores form a
PDE singularity or instead leave admissibility smoothly. The model comparison
does not have a proved Newtonian limit: this neutral conformal equation of
state lacks a massive conserved rest density. A classical-backtransfer claim
needs a separate massive/compressible kinetic and constitutive argument.

A homogeneous zero-laboratory-momentum shortcut was also screened: in frames
A/B the temperature ODE has a positive lower barrier when the conserved energy
is positive, so vacuum collapse cannot simply be assumed. No full homogeneous
classification or extra theorem is published from that exploratory calculation.
The first unresolved singularity producer remains the coupled inhomogeneous
large-data dynamics, not local Cauchy existence or initial stress compatibility.

## 8. Verification and correction receipt

`research/check_bdnk_euler_prepared_exit.py` passed 38 exact algebra checks and
Python compilation. Together with the 31-check virial and 48-check first-exit
scripts this round has 117 distinct executed exact checks. All three were
replayed before final integration. No independent review, Lean, Comparator,
repository-wide test, manuscript build, or CI run is claimed.

One explanatory scalar formula in the preceding kinetic-exit report had an
extra gamma: the rest heat scalar is lambda[g r_t+p d+p ell_t], not
lambda[g r_t+p d+p g ell_t]. Its displayed Cauchy data and independent tensor
checker already used the correct formula. The prose and hash receipt are
corrected in this integration; no theorem or check was changed by that fix.
