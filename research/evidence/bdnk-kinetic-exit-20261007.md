# Smooth loss of positive-particle stress realizability in conformal BDNK

2026-10-07. Base: `itpplasma/navier@00bf4614cb2e2412c376787e7461ed936afca32f`.
Status: **AUTHOR PROOF; independent mathematical reconstruction pending**.
No novelty priority, PDE blow-up, or hydrodynamic-limit theorem is claimed.

BEFORE: the virial result gave breakdown OR negative energy, without selecting
an alternative. AFTER: a separate explicit family, initially realizable by
smooth nonnegative particle distributions, leaves the kinetic stress cone
while its full BDNK solution remains smooth. This applies to frame A AND the
luminal frame B. It does not select the alternative for the virial hot cores.

## 1. Model, theorem, and local-existence input

Use the SAME full neutral conformal BDNK tensor of `bdnk-transfer-20261007.md`,
with epsilon=Theta^4 and eta,chi,lambda proportional to Theta^3. Fix positive
transport constants in a conformal causal frame with a noncharacteristic
constant-time slice and local smooth well-posedness. In particular both
frame A and frame B qualify. No source is present. Space is a flat 3-torus.

**Theorem.** There are analytic, timelike, positive-temperature BDNK Cauchy
data with strictly positive-particle-realizable full initial stress and nonnegative
initial canonical entropy production such that
the classical solution develops T11<0 at a positive time, while temperature,
velocity and all derivatives remain finite. The initial stress has a smooth,
nonnegative massless distribution realization with bounded momentum support.
Thus the cone of stresses realizable by positive classical particles is NOT
invariant under this conformal BDNK evolution, including in a luminal frame.

This is stronger than an example already outside the kinetic cone initially.
It is different from violation of the weak/dominant relativistic energy
condition: negative directional pressure can coexist with those conditions.
The data have order-one shear anisotropy and are NOT small-inverse-Reynolds
preparations. Making velocity small does not remove that qualification.

Sources used at their stated scope:
- Pandya--Pretorius, https://arxiv.org/html/2104.00804v2 , constitutive laws
  (13)--(16), speeds (54)--(56), and discussion of energy-condition violations.
- Clarisse et al., https://arxiv.org/html/2510.16603v1 , equations (10)--(23):
  full conformal stress, derivative Cauchy variables and invertible time block.
These sources do not supply the new initial family or its pressure-exit proof.

For existence it suffices to use classical Cauchy--Kowalevski for the analytic
initial family below. The two nontrivial conservation equations can be solved
for the second time derivatives of log Theta and rapidity. Their time block
is nonsingular: in a rest frame its characteristic determinant is (2) of the
virial packet, and a timelike covector cannot be characteristic in a causal
frame. Lorentz covariance transports this fact to the initial moving state.
The other two conservation equations vanish identically for the plane ansatz.
This is a consistent reduction of ALL four equations, not a transverse-shear
truncation. Periodicity and compactness give a common analytic time interval.
Treating the parameter delta as an additional nondifferentiated analytic
parameter gives joint local dependence, including at delta=0. This supplies
the uniform time-jet control used below. Alternatively the standard local
Sobolev theory and its smooth dependence give the same result. No formal
replay of either general existence theorem was performed here.

## 2. Explicit complete Cauchy data

Set Theta(0,x)=1. All constants in this section are their values at Theta=1.
For 0<delta<=1/6 define

    a=(1-3 delta)/(4 eta), k=4/eta,
    B=lambda/[3 eta(lambda+4 eta)],
    r(x)=(a/k)sin(kx), q(x)=(B/k)sin(kx)cos(kx), d(x)=a cos(kx),
    g=cosh r, p=sinh r, f(r)=3g/(3+2p^2),
    theta0=f(r)[d+p q/lambda],
    r_t(0,x)=f(r)[q/lambda-(2/3)p d],
    (log Theta)_t(0,x)=-theta0/(3g).                              (1)

Here x=x1, u=(g,p,0,0) and n=(p,g,0,0). Choose the x1 period 2pi/k;
other periods are arbitrary positive numbers. These are analytic periodic
functions and all derivative Cauchy data are explicitly specified. They stay
uniformly smooth as delta decreases to zero. In particular |r|<=1/16.

Substitute (1) in the full constitutive law, including the material time
terms. Exactly, A0=0, Q0=q n, and the expansion equals theta0. In the comoving
orthonormal basis (u,n,e2,e3), the complete stress is

    [[1, q, 0, 0],
     [q, P_L, 0, 0],
     [0, 0, P_T, 0],
     [0, 0, 0, P_T]],
    P_L=(1-4eta theta0)/3, P_T=(1+2eta theta0)/3.                 (2)

The pressure anisotropy is produced by the actual shear tensor. It is not an
independent relaxation variable inserted into BDNK. To see (1), the expansion
is p r_t+g d and the scalar rest-frame heat flux is
lambda[g r_t+p d+p g (log Theta)_t]; solving these together with A0=0 gives
precisely (1). This proves the identities for all rapidities, not just the
rational jets checked by the regression script.

## 3. Initial positivity holds everywhere, not just at the test point

One has 1/2<f(r)<=1, |p|<=|r| cosh(1/16)<2|r|, and

    B/k<1/12<1/8,
    B cosh(1/16)/(lambda k^2)<1/4.                               (3)

The second bound follows already from 2B/(lambda k^2)
=eta/[24(lambda+4eta)]<1/96. Write C=cos(kx). Since p sin(kx)>=0,

    theta0=f(r) C [a+B p sin(kx)/(lambda k)].

The bracket lies between a and (5/4)a. Hence theta0>=-(5/4)a,
P_T>=1/8 and P_L<=3/4. If C>=0 then

    theta0<=a[C+(1-C^2)/4]<=a[1-(1-C)/2],
    P_L>=delta+(2eta a/3)(1-C)>=delta+(1/24)sin^2(kx),
    q^2<sin^2(kx)/64.

Here eta a>=1/8 for delta<=1/6. Therefore
P_L-q^2>=delta+(5/192)sin^2(kx)>0. If C<0, theta0<0, so
P_L>=1/3 and P_L-q^2>61/192. Consequently (2) is positive definite as a
quadratic form on covectors, P_L+2P_T=1, and q^2<P_L<1 everywhere.
At x=0, q=r=0 and P_L=delta.

The preparation also obeys the canonical second law INITIALLY. For this exact
BDNK model define S^mu=[(4/3)Theta^3+A/Theta]u^mu+Q^mu/Theta. Contracting
stress conservation with u gives the exact identity

    partial_mu S^mu=[2eta sigma:sigma-A^2/(3chi)-Q:Q/lambda]/Theta.

Initially A=0, sigma:sigma=2theta0^2/3, Q:Q=q^2. Also
|theta0|>=a|C|/2 and |q|<=|C|/12. The conformal causal family has lambda>=3eta,
so q^2/lambda<=16eta theta0^2/27. Thus

    partial_mu S^mu at t=0 >= (20/27)eta theta0^2 >=0.

The cosine factor in q is important: it makes q vanish wherever theta0 does.
A sine-only q would fail this additional initial physical screen. Entropy
production is not asserted nonnegative at later times.

## 4. A smooth nonnegative kinetic realization of the full initial stress

This step matters: the dominant energy condition alone does not supply a
positive particle distribution. Put z=P_L, m=q. At each spatial point take
unit directions with first component +/-sqrt(z), uniformly distributed in
azimuth on the two corresponding circles. Give them masses

    w_+=(1+m/sqrt(z))/2, w_-=(1-m/sqrt(z))/2.

Both masses are positive. The angular measure has total mass 1, mean
(m,0,0), and second moment diag(z,(1-z)/2,(1-z)/2), exactly (2).

It can be replaced by a SMOOTH strictly positive angular density without
changing these moments. The spherical heat kernel at time s multiplies the
l=1 harmonics by exp(-2s) and l=2 harmonics by exp(-6s). First use circle
moments m_pre=exp(2s)m and z_pre=1/3+exp(6s)(z-1/3), then apply that kernel.
For each fixed delta>0 choose a sufficiently small uniform s>0; compactness
and the strict inequalities above guarantee m_pre^2<z_pre<1 and z_pre>0
at every x. The resulting density is smooth in x and direction and has
exactly the desired moments. Its construction is explicit up to an arbitrarily
small heat time satisfying these displayed inequalities.

Multiply by a smooth nonnegative radial function supported, for example, in
1<|p|<2 and normalized by integral rho^3 phi(rho)dr=1. In the local rest frame
this realizes T^{mu nu}=integral p^mu p^nu f d^3p/p^0 for p^0=|p|.
Boost the distribution by the specified smooth u(x). Invariance of d^3p/p^0
makes its LAB stress exactly the full BDNK initial tensor. The bounded boost
preserves smoothness and a bounded momentum support separated from p=0.
This proves actual particle realizability, not only a matrix inequality.

## 5. Conservation forces the pressure to leave the cone while smooth

Reflection symmetry gives r(t,0)=0 while the analytic solution exists, so
T11(t,0) is the longitudinal rest pressure there. Let Erest=epsilon+A.
The initial data give, at the origin,

    theta=a, (log Theta)_t=-a/3, eta_t=-eta a,
    theta_t=r_xt=B/lambda-2a^2/3.

The last equality comes by differentiating the prescribed r_t in (1).
The energy equation gives

    (Erest)_t=(T00)_t=-partial_x T01
                    =-4a/3+4eta a^2/3-B.

In particular the scalar energy correction's derivative is NOT assumed zero
just because A0=0. Retaining it and differentiating (2) yields exactly

    partial_t P_L(0,0)
      =-4a/9+(8/3)eta a^2-B(lambda+4eta)/(3lambda)
      =[-1-12delta+27delta^2]/(18eta)
      <=-1/(18eta).                                             (4)

The limiting delta=0 Cauchy data have positive Theta and timelike u; only the
kinetic-cone margin degenerates. The PDE time block stays noncharacteristic.
Uniform local existence and continuous time jets therefore supply t0>0,
independent of sufficiently small delta, on which
partial_t P_L(t,0)<=-1/(36eta). Choose delta>0 so small that

    t_delta=72eta delta<t0.

Then P_L(t_delta,0)<=-delta<0. All primitive variables and all derivatives
remain bounded on this common classical interval. T00 remains positive near
this event (it starts at 1, uniformly). Thus this is a smooth exit from the
kinetic stress cone, not a claimed gradient singularity or WEC violation.
For each fixed small delta the strict initial cone margins and later negative
T11 survive sufficiently small compatible smooth three-dimensional perturbations
by local hyperbolic continuous dependence. No symmetry-restricted equation is
substituted for the full BDNK system in that robustness statement.

## 6. Exact kinetic control and what the comparison means

For the smooth positive f0 just constructed, neutral collisionless massless
transport on the same torus has the explicit solution

    f(t,x,p)=f0(x-t p/|p|,p).

It is globally smooth, nonnegative and retains bounded momentum support.
Its stress is conserved and trace-free, and T11_kinetic>=0 at all times.
The two evolutions have the SAME full T^{mu nu} at t=0, but at the event

    |T11_BDNK-T11_kinetic|>=delta.

This is a genuine stress-level model-separation example. It does NOT identify
collisionless transport as the kinetic derivation of finite-viscosity BDNK,
match all higher moments or primitive time derivatives, prove a collisional
hydrodynamic limit, or import the OpenAI charged Vlasov--Maxwell theorem.
Any positive classical kinetic model that exists through this time has the
same directional-pressure obstruction to agreeing with this BDNK stress.

## 7. What this changes and what is still open

For this conformal first-gradient class, changing to a luminal frame does not
make kinetic realizability invariant. The universal coefficient bounds (3)
apply to all positive eta,lambda; chi drops out of the constructed initial
identity. The local existence/noncharacteristic hypothesis is retained, so no
conclusion is asserted for ill-posed or degenerate transport parameters.

This completes a scoped negative answer to a PHYSICAL closure question. It
does not decide arbitrary-data BDNK PDE regularity or the virial hot-core
alternative. In particular these data have eta*theta near 1/4 and an order-one
inverse-Reynolds correction. They are not small-gradient equilibrium data.
The earlier virial theorem does start with ideal stress and arbitrarily small
initial gradient measures, but has a disjunctive conclusion; do not combine
the two different initial families into a fictitious stronger theorem.

A preliminary DEC-only energy-exit probe was rejected as a kinetic test: a
stress with isotropic pressure e/3 and |q|/e=5/8 satisfies DEC but has
(e/3)-q^2/e=-(11/192)e<0. The present construction repairs exactly that missing
positive-distribution premise. Its checker retains this hostile control.

Next hard producer: actual singularity or controlled continuation for the
Euler-prepared hot cores, and a closure modification or kinetic limit whose
positive-stress invariant survives its nonrelativistic limit. No general
claim that all viscosity models fail is warranted by this BDNK counterexample.

## 8. Verification

`python3 research/check_bdnk_kinetic_exit.py` passed 48 exact SymPy checks,
including independent four-tensor construction on rational normalized jets,
the differentiated Cauchy jet, origin pressure derivative, both frames and
universal coefficient margins, spatial positivity, initial entropy bounds and positive moment weights.
Python compilation passed. These checks support the written general argument;
they do not prove local existence, the spherical-kernel realization or their
application, and do not replace a fresh independent reviewer. No Lean,
Comparator, repository-wide tests, simulation, or CI run is claimed.
