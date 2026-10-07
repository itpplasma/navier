# Strict-front conformal BDNK: finite-time breakdown or negative energy

2026-10-07. Base: `itpplasma/navier@0dd54e036d14c30ed6ad5a77ef8e229eaf717fe1`.
Status: **AUTHOR PROOF; fresh independent reconstruction pending**.
This is an unforced full-3+1-dimensional companion theorem, not NS-R3 and not
an unconditional BDNK shock theorem. The solution need not remain symmetric.

BEFORE: only a specified accelerating similarity class had been excluded.
AFTER: explicit smooth, Euler-prepared data cannot have a smooth BDNK continuation
through a finite deadline while retaining even laboratory energy positivity.
If the PDE continues smoothly, a quantitative amount of negative total energy
density is forced. This proves failure of global physical admissibility, not
which branch (PDE breakdown versus energy-condition failure) actually occurs.

## 1. Fixed model and external inputs

Use the complete conformal tensor and conventions of
`bdnk-transfer-20261007.md`: signature (-,+,+,+), epsilon=Theta^4,
eta=eta0 Theta^3, chi=chi0 Theta^3, lambda=lambda0 Theta^3, eta0>0,
A=chi(3D log Theta+theta), Q=lambda(Du+Delta grad log Theta),
T=(epsilon+A)(uu+Delta/3)+uQ+Qu-2eta sigma, and partial_mu T^{mu nu}=0.
Choose frame A: chi0=25eta0/2, lambda0=25eta0/3.

No gravitational dynamics, prescribed force, collision operator, or pressure
projection is added. On R3 the data are compact perturbations of a positive
constant rest state, so total energy is infinite but relative energy is finite.
A separate large-flat-torus corollary below has finite total energy.

Primary sources read this round:
- Pandya--Pretorius, https://arxiv.org/html/2104.00804v2 : equations (13)--(16),
  (54)--(56), and the energy-condition discussion. These supply the exact frame,
  tensor and characteristic speeds; not our dynamical conclusion.
- Clarisse et al., https://arxiv.org/html/2510.16603v1 : equations (10)--(23),
  the constrained first-order reduction and invertibility of the time matrix.
- Disconzi--Hoang--Radosz, https://arxiv.org/html/2008.03841v3 : introduction's
  virial-method discussion and the proof of Theorem 7's background-speed support
  property. This credits the Sideris/Guo--Tahvildar-Zadeh tradition. Their MIS
  constitutive theorem is not silently applied to BDNK.

Local smooth Cauchy existence/uniqueness in the positive-temperature timelike
BDNK sector is an external input, as recorded in these primary sources. The
support adapter needed here is proved at the classical-solution level below.
No Lean/comparator replay or independent acceptance of a new theorem is claimed.

## 2. Actual propagation speeds, not the physical velocity bound

At a constant rest state, rotate the spatial covector onto x1. Linearizing the
FULL four-tensor and retaining second derivatives gives, for longitudinal
variables (delta log Theta, delta u1), the characteristic matrix

    [[3 chi c^2+lambda, -(chi+lambda)c],
     [-(chi+lambda)c, lambda c^2+(chi-4eta)/3]].                    (1)

Each transverse mode has factor lambda c^2-eta. Consequently the full
characteristic polynomial is that transverse factor squared times

    3 chi lambda z^2-2 chi(2eta+lambda)z+lambda(chi-4eta)/3,
    z=c^2.                                                        (2)

In frame A, the two longitudinal squared speeds are

    z_+/-=(31 +/- 2 sqrt(134))/75,

and the transverse squared speed is 3/25. Thus c_max=sqrt(z_+)<9/10<1.
These ratios are independent of temperature and eta0. They agree with the
primary source's longitudinal speeds; the transverse factors were checked
from the full tensor. Constrained reduction adds no faster physical mode.

**Background-front lemma.** A classical BDNK solution whose complete Cauchy
jet equals the constant rest state outside B_R remains that state outside
B_(R+c t), on its classical interval, for any fixed c_max<c<1.

Proof: first use causal domain of dependence to confine any perturbation to
B_(R+t). The principal coefficients depend smoothly on (Theta,u), not on their
derivatives. At the constant rest state their dual propagation cone lies
strictly inside the cone of speed c, by (1)--(2). This persists in a neighborhood
of that state. Suppose the sharper support property holds to some time t0.
Continuity of a classical solution gives a uniform spacetime collar of the
compact moving boundary where the state is sufficiently close to equilibrium.
In this collar the boundary r=R+ct is strictly outgoing for every physical
characteristic. Local uniqueness/domain of dependence for the hyperbolic system
therefore preserves the zero perturbation on its exterior for a further time.
The exterior away from the collar also remains zero by local uniqueness;
causal confinement makes the relevant region compact. The property is closed
under increasing classical times and holds initially by the same collar
argument. The open/closed continuation proves it on every compact classical
interval. The derivative constraints in a first-order reduction are initially
satisfied and propagate; no arbitrary extra characteristic field is inserted.

The lemma does NOT say interior velocities or characteristic speeds are bounded
by c. They can be larger. A smooth disturbance front in the equilibrium exterior
cannot outrun the exterior cone; overtaking the front is precisely a possible
loss-of-smoothness mechanism. Merely citing the light-speed bound would NOT
suffice for the result below. This collar/domain-of-dependence adapter is a
specific load-bearing item for independent review.

## 3. Exact virial theorem for any trace-free conserved stress

Let bar_e>0 and bar_T=diag(bar_e,bar_e/3,bar_e/3,bar_e/3). Suppose a symmetric
C1 stress is conserved, trace-free, and equals bar_T outside B_(R+ct), c<1.
Set e=T00-bar_e, m_i=T0i, and define the finite integrals

    E=integral e, F=integral x dot m, I=integral |x|^2 e.

Integration by parts on the compact perturbation gives EXACTLY

    E'=0, I'=2F, F'=integral sum_i(Tii-bar_e/3)=E,
    I(t)=I(0)+2F(0)t+E t^2.                                     (3)

The derivative stresses are not estimated or discarded: trace-freeness cancels
them in F'. This is a standard virial mechanism with its exact BDNK adapter.

Put L=R+ct. If T00>=0, then

    I(t) <= L^2 E+(8 pi/15) bar_e L^5.                            (4)

Indeed I=integral r^2 T00-bar_e integral r^2, and r^2<=L^2 on the support ball;
its volume is 4pi L^3/3 and its second moment is 4pi L^5/5.
More generally, with N_-(t)=integral_(B_L) max(-T00,0),

    N_-(t) >= [I(0)+2F(0)t+E(t^2-L^2)
                    -(8pi/15)bar_e L^5]/L^2.                    (5)

This follows by retaining the positive weight L^2-r^2 in the exact difference
L^2 E+(8pi/15)bar_e L^5-I=integral_(B_L)(L^2-r^2)T00.
Only a positive right-hand side of (5) asserts anything.

Thus a positive value of the numerator gives an unconditional disjunction:
there is no classical admissible continuation to that time, OR the total
laboratory energy density is negative somewhere, with the bound (5).
Neither an energy condition nor its propagation is assumed in deriving (5).

## 4. Explicit initial data that produce the contradiction

Choose any C-infinity radial F with 1<=F<=32, F=32 on B_(1/2), and F=1
outside B_1. For arbitrary R>0 and bar_Theta>0 prescribe

    Theta(0,x)=bar_Theta F(x/R), u(0,x)=(1,0,0,0),
    partial_t log Theta(0,x)=0,
    partial_t u^i(0,x)=-partial_i log Theta(0,x),
    partial_t u^0(0,x)=0.                                       (6)

These are legitimate compatible derivative Cauchy data for this second-order
system. They are precisely the instantaneous ideal-Euler derivatives at rest.
On this entire initial slice A=0, Q=0, sigma=0, so the FULL BDNK stress is
ideal, positive and satisfies the usual classical energy conditions. In
particular F(0)=0, I(0)>=0 and, writing bar_e=bar_Theta^4,

    E >= (pi/6) bar_e R^3 (32^4-1).                              (7)

The complete data equal equilibrium outside B_R. Local BDNK existence therefore
starts an actual classical branch, not just a tensor satisfying a few identities.
Apply the front lemma with c=9/10. At t_d=20R, L=19R, (5)--(7) give

    N_-(20R) >= (164854541 pi/10830) bar_e R^3 >0                 (8)

whenever the classical branch exists through t_d in its positive-temperature,
timelike BDNK state space. The constant is an exact rational calculation.

**Conclusion.** For every eta0>0 in frame A, the data (6) cannot admit a global
classical BDNK evolution that retains T00>=0. By time 20R there must be failure
of classical continuation/admissible state space OR negative laboratory energy.
Equation (8) quantifies the latter alternative. It is NOT a theorem selecting
finite-time gradient blow-up over smooth energy-condition violation.

The strict inequality has a large margin and persists under sufficiently small
smooth perturbations of the complete Cauchy data supported in the same ball,
provided local admissibility remains. Symmetry is not used after constructing
the data. This is a full-3D open-data obstruction, not a planar invariant ansatz.

For any other strictly causal conformal frame, choose c_max<c<1, t_d=2R/(1-c),
and increase the hot-core amplitude until

    E > (8pi/15)bar_e R^3 (1+c)^5/[(1-c)^4(3+c)].                 (9)

Here t_d^2-(R+ct_d)^2=R^2(3+c)/(1-c). The same proof applies.

## 5. Initially controlled gradients and finite-total-energy version

For the fixed smooth profile F, dimensionless initial first gradients obey

    |grad log Theta|/Theta <= C_F/(R bar_Theta),
    |partial_t u|/Theta <= C_F/(R bar_Theta).

All first constitutive corrections actually vanish by (6). Taking R bar_Theta
large compared with the fixed transport constants makes the usual initial
Knudsen-type measures arbitrarily small, without changing the dimensionless
hot-core contrast or contradiction. Large AMPLITUDE is not a large initial
gradient expansion error. The proof does not show when the regime is left.

On a flat torus of side length L_box>38R, the same smooth data, periodically
extended with constant exterior, have finite total energy. Until 20R the
perturbation ball does not meet its periodic copies. The identical compact
perturbation virial calculation applies in one coordinate cell. Hence the
same physical-breakdown disjunction holds with finite total energy. This is
not a claim about asymptotically vacuum R3 data.

## 6. What is and is not settled

This rejects the unrestricted physical claim that a strictly causal conformal
BDNK closure takes every smooth physically prepared datum to a globally smooth,
positive-energy state. It does not establish the exact PDE shock mechanism,
prove failure for frame B, or derive a fluid-to-kinetic limit. The prior
similarity exclusion remains scoped and is not used here.

Frame B has a luminal longitudinal characteristic: (2) has z=1 and z=1/25.
The gap t^2-(R+t)^2 is negative, so this particular obstruction disappears.
This is dependence of the PROVED OBSTRUCTION on the frame, not proof that
frame B is globally regular. A genuinely different argument is required there.

The remaining high-value question is now narrower: can the negative-energy
alternative be ruled out dynamically for a useful BDNK subclass, forcing an
actual PDE singularity, or can one explicitly continue one of these hot cores
smoothly into energy-condition violation? Do not assume the answer. Published
BDNK computations already observe energy-condition violations, so positivity
propagation is a substantive missing theorem, not an innocent physical axiom.

## 7. Verification

`research/check_bdnk_virial.py` passed 31 exact SymPy checks. It constructs the
prepared stress and full rest principal symbol, verifies the frame polynomials,
ball moments, explicit contradiction constants, and a massless kinetic control's
isotropic moments. Python compilation passed. The script does not verify the
nonlinear support lemma or substitute for independent mathematical review.
Full repository checkout download again failed at DNS in the execution container;
no repository-wide tests, Lean, Comparator, manuscript build or CI are claimed.
