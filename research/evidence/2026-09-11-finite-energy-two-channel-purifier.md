# Finite-energy two-channel purifier with asymptotically exact low strain

Date: 2026-09-11. Repository input:
`itpplasma/navier@6bd177ab306073ca68860a5e0ec95333183c8960`.

**Status: author proof of a finite-energy, compact-Schwartz, two-channel
low-band purifier theorem; independent mathematical audit and novelty are
undetermined.** This packet combines the nested one-channel localization,
Wiener shadowing, gradient-preserving rescaling, and two-channel spectral moat.
It produces one actual unforced `R3` Navier--Stokes solution whose **selected
low purifier bands** carry the required symmetric strain `H` with vanishing
error on the complete `O(N^-2)` pulse interval.

It deliberately does **not** claim that the total pointwise velocity gradient
is close to `H`. The high pump bands and high cross-family bands can have large
gradients even when their velocities are small. Their effect on the clean
dyadic gate must be controlled by spectral separation in the next stage-map
argument.

No regenerative turnover, finite-time singularity, arbitrary-data regularity,
or `NS-R3` resolution is claimed.

## 1. Parameters and exact channel inputs

Let `(kappa_i,d_i)`, `i=1,2`, be the two transverse low pairs of the exact
rank-two purifier reduction, so

    2 d_1 tensor kappa_1+2 d_2 tensor kappa_2=G,
    sym G=H.                                               (1.1)

The exact geometry checker proves that both the low directions `kappa_i` and
the high pump directions

    rho_i=(kappa_i cross d_i)/|kappa_i cross d_i|          (1.2)

are pairwise nonparallel.

Choose

    lambda=N^(-alpha),       1/2<alpha<1,                 (1.3)

and rescale

    d_i -> lambda d_i,
    kappa_i -> kappa_i/lambda.                             (1.4)

For each `i`, construct the exact three-layer 2D3C purifier channel with shear
centers `mN rho_i`, `m=1,2,3`. Its high-to-low gaps remain exactly

    D_m=2m^2N^2,                                           (1.5)

its velocity Wiener size is

    O(lambda N),                                           (1.6)

and its intended low gradient is unchanged by (1.4).

## 2. Rotate and nest-localize each channel separately

For each channel choose a rigid orthonormal frame putting it in the normal form

    U_i=(v_i(y,t),0,w_i(x,y,t)).                           (2.1)

Apply the nested localization construction in that frame: an outer
streamfunction cutoff localizes the shear, an inner vector-potential cutoff
localizes the passive scalar, and the outer cutoffs are identically one on a
neighborhood of the complete inner support. Rotate the resulting field back to
physical coordinates. Denote it

    U_(i,N,L).                                             (2.2)

Rigid rotations preserve all `F L1` estimates. Each `U_(i,N,L)` is real,
smooth, compactly supported and exactly divergence free. The two localized
channels may be centered at the same physical point; their supports are allowed
to overlap.

The rescaled channel bounds are, uniformly on `0<=t<=T/N^2`,

    ||U_(i,N,L)||_A <= C lambda N,                         (2.3)

where `A=F L1(R3)`.

To track the localization residual, note the rescaled potential sizes in a
normal frame:

    ||v_i||_A=O(lambda N),
    ||partial_y v_i||_A=O(lambda N^2),
    ||psi_i||_A=O(lambda),                                (2.4)

and, because the low `x` frequency is `O(lambda^-1)`,

    ||q_i||_A=O(lambda^2 N),
    ||partial_x q_i||_A=O(lambda N),
    ||partial_y q_i||_A=O(lambda^2 N^2),
    ||partial_x partial_y q_i||_A=O(lambda N^2).          (2.5)

The exact nested residual formulas contain at least one cutoff derivative. The
largest surviving term is a cutoff derivative times either
`partial_y v_i` or `partial_x partial_y q_i`. Therefore

    ||F_(i,N,L)||_A
      <= C lambda N^2/L,                                  (2.6)

where

    F_(i,N,L)=partial_t U_(i,N,L)-nu Delta U_(i,N,L)
       +P div(U_(i,N,L) tensor U_(i,N,L)).                 (2.7)

This is the rescaled version of the one-channel Wiener shadowing estimate.

## 3. The compact two-channel approximate path

Put

    U_(N,L)=U_(1,N,L)+U_(2,N,L).                          (3.1)

It is one compactly supported smooth solenoidal path. Its projected residual is

    F_self+F_cross,                                       (3.2)

where

    F_self=F_(1,N,L)+F_(2,N,L),                           (3.3)

and

    F_cross=P div(U_1 tensor U_2+U_2 tensor U_1).         (3.4)

The self part obeys

    ||F_self||_A <= C lambda N^2/L.                       (3.5)

The cross stress itself obeys

    ||U_1 tensor U_2+U_2 tensor U_1||_A
       <= C lambda^2 N^2.                                 (3.6)

## 4. Actual unforced solution and global correction

Let `u_(N,L)` be the actual solution with the same initial datum,

    u_(N,L)(0)=U_(N,L)(0) in S_sigma(R3;R3),              (4.1)

and write

    u_(N,L)=U_(N,L)+r.                                    (4.2)

Using heat contraction for the vector self residual and the standard Wiener
heat--Leray estimate

    ||e^(nu s Delta)P div G||_A
       <= C(nu s)^(-1/2)||G||_A,                          (4.3)

the two seed contributions on `0<=t<=T/N^2` are

    self localization: O(lambda/L),                       (4.4)

    cross-family:      O(lambda^2 N).                     (4.5)

The linearized mild-map norm around `U_(N,L)` is

    C sqrt(t)||U_(N,L)||_A <= C lambda,                   (4.6)

which tends to zero. A contraction on the full scaled interval therefore gives
an actual classical solution and

    sup_(0<=t<=T/N^2)||r(t)||_A
      <= C_T [lambda/L+lambda^2 N].                       (4.7)

Since `alpha>1/2`, the global velocity correction tends to zero for every
`L>=1` growing or fixed.

## 5. Low purifier bands after localization

Let `K_*` be the four intended centers

    +/-kappa_1/lambda, +/-kappa_2/lambda.                 (5.1)

Choose a smooth Fourier projector `Pi_*` whose four components have radius
`c/lambda`, with `c>0` fixed sufficiently small. Exact nonparallelism of the
low and high channel directions gives a uniform center separation:

* every nontrivial high cross-family center is distance `>=c_1 N` from `K_*`;
* every low--low cross-family center is distance `>=c_2/lambda` from `K_*`;
* every non-target sideband of one channel is distance `>=c_3 N` from its
  target low center,

for all sufficiently large `N`.

A localized plane-wave center is convolved with the Fourier transform of a
smooth cutoff at scale `L`. For every `M` its `A`-mass a distance `delta` away
is bounded by

    C_M (L delta)^(-M)                                    (5.2)

relative to its polynomial amplitude. The same statement holds for the nested
curl terms because each is a finite combination of scaled cutoff derivatives
multiplying the absolutely summable channel ladder.

Consequently direct cross-family leakage into `Pi_*` obeys, for every `M`,

    ||Pi_*[U_1 tensor U_2+U_2 tensor U_1]||_A
      <= C_M lambda^2 N^2 (L/lambda)^(-M).                (5.3)

The exact zero target coefficient of the unlocalized almost-periodic problem is
therefore replaced only by a superalgebraic cutoff tail.

## 6. Target-band correction estimate

On `supp Pi_*`,

    |xi| <= C/lambda.                                     (6.1)

Project the mild equation for `r` onto `Pi_*`.

The direct self-localization forcing contributes target velocity at most

    C lambda/L,                                           (6.2)

hence target gradient at most `C/L`.

By (5.3), the direct localized cross seed contributes target gradient at most

    C_M (L/lambda)^(-M).                                  (6.3)

For the terms involving the already constructed correction `r`, use (4.7):

    lambda^-1 N^-2
      (lambda N)[lambda^2 N+lambda/L]
      <= C[lambda^2+lambda/(NL)]                          (6.4)

for the target velocity. Multiplying by the target frequency `O(lambda^-1)`
gives target-gradient error

    O(lambda)+O((NL)^-1).                                 (6.5)

The `r tensor r` term is smaller. Thus

    sup_t ||grad Pi_* r(t)||_infinity
      <= C_T [lambda+L^-1]
        +C_(T,M)(L/lambda)^(-M).                          (6.6)

## 7. Intended low strain and the slow-heat correction

For the unlocalized exact channel, the individual low-gradient ladder error is
`O(1/N)` after the rescaling. Its low heat factor is

    h_i(t)=exp[-nu |kappa_i|^2 t/lambda^2],               (7.1)

so on the pulse clock

    |1-h_i(t)| <= C_T N^(2alpha-2).                       (7.2)

Localization changes the selected low profile only by the superalgebraic tails
from (5.2). Combining (6.6), the one-channel ladder estimate, and (7.2) gives

    sym grad Pi_* u_(N,L)(t)
      =g_fast(t) H+E_(N,L)(t),                            (7.3)

with

    sup_t |E_(N,L)(t)|
      <= C_T [
          lambda
          +N^(-1)
          +N^(2alpha-2)
          +L^(-1)]
        +C_(T,M)(L/lambda)^(-M).                          (7.4)

Here `g_fast` is the common normalized three-layer fast pulse profile. The
antisymmetric part of the exact rank-two gradient remains present in the low
bands, as required by the construction; (7.3) takes only the symmetric part.

Thus for any

    1/2<alpha<1,
    L=L(N)->infinity,                                     (7.5)

the selected finite-energy low purifier strain converges uniformly to the
intended pulse.

A concrete calibration is

    alpha=3/4,       lambda=N^(-3/4),       L=N.           (7.6)

Then

    global correction = O(N^(-1/2)),                     (7.7)

and the low-strain error is

    O(N^(-1/2))                                           (7.8)

up to arbitrarily high superalgebraic powers.

## 8. The theorem and its exact scope

**Theorem (finite-energy low-band purifier).** Fix `nu>0` and a finite scaled
pulse horizon `T`. For all sufficiently large `N`, choose (7.6). There is a
real compactly supported smooth solenoidal datum in `R3` whose original
unforced Navier--Stokes classical solution exists on `0<=t<=T/N^2` and whose
four selected low purifier bands satisfy

    sym grad Pi_* u(t)=g_fast(t)H+O_T(N^-1/2)             (8.1)

uniformly on that interval.

The datum is Schwartz and has finite kinetic energy for every fixed `N`.
Neither the energy nor higher norms are asserted uniform in `N`; recursive
stage summability is a separate requirement.

Equation (8.1) is a statement about the selected low Fourier bands. It is **not**

    sym grad u(t,x) approximately g_fast(t)H              (8.2)

pointwise for the full field. The high pump modes are load-bearing, and their
high gradients are not small. This distinction is essential for the next
stage.

## 9. New live blocker: clean-gate/purifier composition

The isolated purifier problem has now been reduced to an admissible
finite-energy unforced module at author-proof level. The next theorem must put
this module and the contaminated clean dyadic gate in one Cauchy history and
show, with scale-explicit spectral windows, that

1. the low purifier bands act on the desired/rejected clean components with the
   previously proved sign separation;
2. the high purifier parents and high cross bands send their clean interactions
   outside the retained target windows or with quantitatively small return;
3. the finite purifier pulse leaves a state admissible for the next clean gate;
4. the resulting one-stage map has the required supercritical gain while its
   energy/time costs can be summed under physical rescaling.

The high-band clean interaction is now the first uncontrolled term; another
standalone purifier construction would not advance the terminal problem.

No PLAN, canonical proof graph, manuscript, or formal status is promoted here.
Full repository verification and independent audit are pending. `NS-R3`
remains unresolved.