# Actual NS normal transients: contraction fails, a bounded moving metric repairs the test

Date: 2026-09-07. Input checkpoint:
`1e4e28b7fac18311763dc1ddb7be8ad818888844`.
Status: complete author derivations, independent audit pending; no novelty claim.
NS-R3 remains unproved. This tests the central normal-stability hypothesis
needed to extend the preceding causal-refinement theorem. It is neither an
NS-R3 counterexample nor a new general regularity criterion.

## 1. Why this is the next test rather than another unrelated no-go

The preceding wave repaired static C2 slaving by an exact causal expansion,
using a contractive skew-advection sector. Its attempted extension stopped at
the term B(error,coarse), which is not skew. The present question is whether
that term actually destroys contractivity on genuine NS trajectories, or
whether the apparent obstacle is only an absolute-value estimate.

We prove an actual noncontractive high-mode linearized evolution about an
unforced smooth NS shear. The perturbation is the derivative of a family of
exact GLOBAL periodic NS solutions. Thus no arbitrary strain matrix or forced
response is substituted. We then explicitly repair the test with a bounded
nonautonomous propagator estimate and a uniformly equivalent moving metric.
The repair does not assume an unknown fundamental matrix is bounded.

Only the assertion of universal contraction in the UNCORRECTED mass norm is
retired. Normal stability with bounded transient amplification, corrected
metrics and genuinely nonlinear signed feedback estimates remain open routes.

## 2. Exact NS family and its normal variation

Use T3 with period 2pi, fixed viscosity nu>0 and integers K>=1, L>K.
Set lambda=nu K^2, gamma=nu L^2, beta=lambda+gamma, and fix real amplitude A0.
The base velocity and pressure are

    v(x,t)=(A0 exp(-lambda t) sin(Kx2),0,0),    p=0.            (2.1)

This is an exact unforced NS solution. For a parameter delta, let

    u_delta(x,t)=(f_delta(x2,x3,t),
                  delta exp(-gamma t)cos(Lx3),0),
    f_delta(x2,x3,0)=A0 sin(Kx2),                            (2.2)

where

    partial_t f_delta+delta exp(-gamma t)cos(Lx3)partial_2 f_delta
      =nu(partial_2^2+partial_3^2)f_delta.                    (2.3)

Direct substitution shows that all components solve NS with p=0. These fields
are solenoidal and the nonlinear pressure source is zero; the convective
term is itself solenoidal. The scalar equation has a bounded skew perturbation
of heat on the invariant transverse-frequency space k2=+/-K, whose operator
norm is at most K. The Volterra proof in the preceding evidence, with x2 and
x3 exchanged and coefficient decay gamma, constructs a global smooth solution
for every finite delta. It also gives differentiability in delta by an
absolutely convergent series. This is an explicit actual family, not a
linearity assumption about the full equation.

Its derivative z=partial_delta u_delta|_(delta=0) is

    z_2(x,t)=exp(-gamma t)cos(Lx3),   z_3=0,
    z_1(x,t)=-A0 K t exp(-beta t)cos(Kx2)cos(Lx3).             (2.4)

Indeed the z1 forcing is -A0 K exp[-(lambda+gamma)t]
cos(Kx2)cos(Lx3), whose output heat rate is beta=lambda+gamma.
The exact integral is resonant and gives the t factor in (2.4).
This verifies all components of the linearized NS equation, including the
zero pressure variation. It is not a freely forced Stokes counterexample.

The same formulas hold for the linearization of the exact Galerkin equation
whenever the fine cutoff N>=sqrt(K^2+L^2). The base lies in E_K; z initially
has frequency L>K, and both modes in (2.4) remain strictly above K. Thus this
is an actual invariant NORMAL subspace at the linearized level, not a
low-frequency perturbation relabelled as unresolved.

## 3. A rigorous high-mode amplification at critical amplitude

Let q=(0,cos(Lx3),0) and r=(cos(Kx2)cos(Lx3),0,0). These fields are orthogonal
in L2, and ||r||2^2=||q||2^2/2. Formula (2.4) gives exactly

    ||z(t)||2^2/||z(0)||2^2
      = exp(-2gamma t)+(A0 K t)^2 exp(-2beta t)/2.             (3.1)

At t_*=1/beta,

    ||z(t_*)||2/||z(0)||2 >= |A0|K/(sqrt(2)*e*beta).           (3.2)

Take L=2K and |A0|=32 nu K. Then beta=5nu K^2 and the squared lower bound
is 32^2/(50e^2)>32^2/450>1, using e<3. There is no numerical sign uncertainty.
This holds for every K, with a fixed dimensionless critical amplitude
alpha=|A0|/(nu K)=32 and fixed positive viscosity. Fine cutoff N=3K suffices.

**Theorem 4 (failure of uncorrected normal contraction).** The actual NS
linearized high-mode propagator cannot, for all smooth coarse states and
arbitrary amplitudes, satisfy ||z(t)||2<=exp(-c nu L^2 t)||z(0)||2 with
c>=0 and prefactor one. It fails even on the explicit global periodic family
(2.2) and on faithful finite Galerkin truncations. Frozen diffusion eigenvalues
are negative throughout this example, which does not prevent transient growth.

For a fixed time t_* as above, differentiability of u_delta shows

    ||u_delta(t_*)-v(t_*)||2/||u_delta(0)-v(0)||2 >1

for every sufficiently small nonzero delta. Hence the phenomenon is present
on nearby actual nonlinear trajectories as well. Their nonlinear difference
need not remain purely high frequency, and no such claim is made.

This theorem does not refute a bound with an input-dependent finite prefactor,
a moving norm, or a signed spacetime estimate. Nor does it establish a blow-up,
a Lyapunov instability as t->infinity, or a whole-space Schwartz example.
It tests a universal contraction premise used by the proposed discretization
route in a class to which that premise would have applied.

## 4. Exact repair: a bounded propagator without a small-amplitude assumption

More generally linearize about (2.1) on the solenoidal subspace of fields
independent of x1 and with |k3|>=L. A Galerkin cutoff may be included.
The variation equations are triangular:

    dot z_2=nu Delta z_2,    dot z_3=nu Delta z_3,
    dot z_1=nu Delta z_1
              -A0 K exp(-lambda t)P_N[cos(Kx2) z_2].          (4.1)

The forcing is solenoidal (it has only an x1 component independent of x1),
so the canonical linearized pressure vanishes. P_N is orthogonal and
preserves |k3|>=L. The heat semigroup on this space has norm <=exp(-gamma t),
and multiplication by cos(Kx2), with compression, has norm <=1.

**Theorem 5 (cutoff-uniform transient bound).** For any 0<=s<=t, the exact
normal propagator of (4.1) satisfies

    ||z(t)||2 <= exp[-gamma(t-s)]
       [1+alpha(exp(-lambda s)-exp(-lambda t))] ||z(s)||2,
    alpha=|A0|/(nu K).                                     (4.2)

In particular the prefactor is at most 1+alpha, independent of N and of the
horizon. No smallness of alpha is required.

**Proof.** z2,z3 have the heat evolution. Duhamel for z1 has just one feed-
forward coupling, since z1 has no feedback into z2,z3. Its source norm is
bounded by |A0|K exp(-lambda r)exp[-gamma(r-s)]||z2(s)||2.
The last heat factor exp[-gamma(t-r)] makes the product exp[-gamma(t-s)].
Integrating the coefficient from s to t gives

    (|A0|K/lambda)[exp(-lambda s)-exp(-lambda t)]
      =alpha[exp(-lambda s)-exp(-lambda t)].

The norm of the diagonal heat evolution of the WHOLE initial vector is at
most exp[-gamma(t-s)]||z(s)||2. Add the forcing norm and use
||z2(s)||2<=||z(s)||2. This proves (4.2). QED.

This estimate is a real repair of the failed test, not an assumption that a
nonnormal propagator behaves like its eigenvalues. The one-way structure is
essential. A general linearized NS solution has no such triangular split.

## 5. A uniformly equivalent metric for the exact two-mode subsystem

Normalize q,r separately to unit L2 norm, and write z=x*r_hat+y*q_hat.
Let kappa=A0 K/sqrt(2). On this invariant span the exact equations are

    dot x=-beta x-kappa exp(-lambda t)y,
    dot y=-gamma y.                                         (5.1)

Define

    h(t)=kappa t exp(-lambda t),
    xi=x+h(t)y,
    E_corr=|xi|^2+|y|^2.                                    (5.2)

A DIRECT differentiation gives

    dot xi=-beta xi,     dot y=-gamma y,
    dE_corr/dt=-2beta|xi|^2-2gamma|y|^2 <=-2gamma E_corr.      (5.3)

The h' term is indispensable: h'=kappa exp(-lambda t)-lambda h cancels
exactly the forcing in (5.1). With H=alpha/(sqrt(2)*e), |h(t)|<=H and the
triangular transformation and its inverse both have norm at most 1+H. Thus

    (1+H)^(-2)(|x|^2+|y|^2) <= E_corr
       <=(1+H)^2(|x|^2+|y|^2).                              (5.4)

This is a concrete bounded moving-metric repair, with constants computed
from the prescribed shear and viscosity. It is NOT a fixed universally
monotone quadratic functional of all velocities, nor a new thermodynamic
entropy. It therefore does not contradict the repository's earlier fixed-
functional no-go results. It also does not justify defining a metric through
an unknown ill-conditioned full-NS fundamental matrix and assuming (5.4).

At critical |A0|=alpha nu K, both the propagator prefactor and the condition
bound are independent of K after viscous time normalization. Normal
contractivity fails in the original norm while quantitatively controlled
normal evolution survives. This is precisely why the plan now permits
bounded transient growth instead of requiring pointwise contraction.

## 6. Audit checks and exact frontier after the repair

The sign in (2.4) is minus: the variation equation has -(z.grad)v. The
pressure projection does not change this forcing. The high-frequency
assertion uses L>K; it is not inferred from the amplitude. The value L=2K
and N=3K keeps every displayed mode, without an aliasing or cutoff limit.
The factor 1/2 in (3.1) comes from the Fourier norms, not a changed amplitude.
All solution claims are forward in time; no ancient boundedness is assumed.
The nonlinear family is global by the same convergent bounded-advection
construction as the previous note, so differentiating it is legitimate.

The exact-rational oracle is extended to check the two variation equations
for integer K,L, the energy-normalization factor, the critical amplification
lower bound and the full time-dependent quadratic matrix identity. A negative
control omits the metric derivative, which the identity detects. This finite
regression is not an independent review or proof of the universal formulas.
No novelty is claimed for nonnormal transient growth or the triangular repair.

The unresolved step is now more precise than "find a slow manifold": prove
an input-controlled normal PROPAGATOR or moving metric for the genuinely
three-dimensional retained-feedback system, AND control how its corrections
and forcing accumulate under critically weighted refinement. The general
error identity remains

    (1/2)d||w||2^2/dt+nu||grad w||2^2
       =<F,w>-integral (w.grad)v . w.

The term on the right is neither refuted nor bounded by Theorems 4--5 in
its general scope. Chaining the test estimates 1+alpha at infinitely many
levels would require a new bound on their accumulation. That bound is NOT
inferred from finite physical energy or from the shear's explicit decay.

A plausible next object is a critical weighted metric with off-diagonal
interscale blocks that incorporates the matched forcing and transient
corrections. Its positivity, equivalence constants, time derivative and
nonlinear remainder must all be proved from inputs. This is an unproved
research obligation, not a claimed universal metric. Failure to construct it
is not proof that all geometric, kinetic, FEEC or slow-manifold routes fail.

MODE / RESULT: test the first strain-containing normal equation; falsify
uncorrected universal contraction and explicitly repair the example with
bounded transient propagation and a moving metric.
CLAIM AND SCOPE: Theorems 4--5 and (5.2)--(5.4), actual periodic NS family
and its faithful Galerkin linearization; not arbitrary full-NS tracking.
FIRST GAP: general critically summable nonlinear feedback and reconstruction.
SURVIVING SUFFIX: the RF-SUM/consistency/whole-space contract still implies
NS-R3 if its unproved input-only estimate is supplied.
NON-CLAIMS: no NS-R3 proof or strict singularity reduction; no automatic
normal hyperbolicity; no FEEC/kinetic/full R3 adapter completed.
NEXT DISTINCT ACTION: the full paired-feedback metric estimate, not another
contractive passive calibration or a frozen-eigenvalue argument.
