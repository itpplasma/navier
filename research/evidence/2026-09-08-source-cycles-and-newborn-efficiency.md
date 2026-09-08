# Original-NS source cycles, full time trees, and newborn efficiency

Date: 2026-09-08. Status: AUTHOR derivation plus exact finite arithmetic; independent mathematical audit PENDING. NS-R3 remains open. No canonical graph promotion.

## Terminal gate

For one fixed finite q>3 the missing terminal producer remains

    integral_0^t Pi_q,M <= nu integral_0^t D_q,M + C(d,nu,H,N0,q)

for every upper time t<=H uniformly in M. Together with the exact RF identity, Schwartz initial shells, RF-LQ-SYNTHESIS, RF-LOCAL-ID, Lorentz Fatou, RF-LQ-CONTINUATION, LOCAL and ENERGY, this would prove original unforced R3 NS with normalized pressure. Nothing here proves this estimate or a replacement continuation producer.

## 1. Exact full-source scale cycle

Let N(v)=-P[(v.grad)v], with the exact Leray projection, and consider the real planar periodic field

    U(x,y,z)=(sin(x+y), sin(2x)-sin(x+y), 0).

In the odd Fourier convention Uhat(k)=i b_k, put p=(2,0,0), q=(1,1,0),

    b_p=(0,-1/2,0),  b_q=(-1/2,1/2,0),  b_-k=-b_k.

The complete original quadratic source has positive representatives

    g_(p+q)=(-1/20,3/20,0),
    g_(p-q)=(-1/4,-1/4,0),

and their negatives. Applying the complete original source again gives only

    C(g,g)_(2p)=(0,-1/10,0),
    C(g,g)_(2q)=(-1/10,1/10,0),

and their negatives. Hence exactly

    N(N(U))=(1/5) U(2x,2y,2z).

No carrier is deleted between applications. The difference channel is essential: its squared coefficient norm is five times the sum daughter's, and deleting it makes the second source vanish. Thus mandatory side/difference state can be a resource rather than merely a loss.

The exact checker searches a broad rational planar two-carrier family and confirms that source copying is not algebraically forbidden by the original Leray convolution. This kills a possible universal no-go based solely on source-map algebra.

## 2. R3 Schwartz realization with inherited source error

Use a horizontal streamfunction Psi for U and a real even slowly varying envelope h_L. Define

    F_L=curl[h_L Psi e_3].

Then F_L is exactly real, solenoidal and Schwartz, and F_L=h_L U+O(L^-1). For finite carrier polynomials, smoothness of the Leray symbol away from nonzero output carriers gives

    N(F_L)=h_L^2 N(U)+r_L,
    ||r_L||_2=o(L^(3/2)).

The whole inherited error is retained in the second source application. Fixed-carrier bilinear estimates give

    N(N(F_L))=h_L^4 N(N(U))+o(L^(3/2)).

Choosing a Gaussian-type envelope with h(x)^4=h(2x), and then approximating its Fourier transform by real even C_c^infinity functions if compact Fourier support is desired, yields

    ||N(N(F_L))-(1/5)F_L(2 .)||_2 / ||F_L(2 .)||_2 -> 0.

By amplitude homogeneity, for every beta>0 and epsilon>0 there is a nonzero real solenoidal Schwartz F such that

    ||N(N(F))-beta F(2 .)||_2 <= epsilon ||F(2 .)||_2.

For beta>2 the ideal map beta F(2.) amplifies homogeneous critical velocity norms such as L3. This is an algebraic source-cycle statement, not a trajectory statement.

These profiles can also be placed in the published Chemin-Gallagher slowly-varying global-smooth class by taking the vertical dependence sufficiently slow after fixing the horizontal profile and amplitude. That global theorem is prior art, not a new NS theorem. Consequently even an apparently critical-amplifying full-source cycle can occur arbitrarily accurately in data known by prior theory to generate a global smooth original-NS solution.

## 3. Full temporal tree separates source recurrence from NS recurrence

For the actual quadratic time evolution, write the top-amplitude inviscid jet

    b(t)=b0+t b1+t^2 b2+t^3 b3+O(t^4).

Then

    b1=C(b0,b0),
    b2=(C(b0,b1)+C(b1,b0))/2,
    b3=(C(b1,b1)+C(b0,b2)+C(b2,b0))/3.

The source cycle uses only C(b1,b1). The other two four-leaf trees have the same amplitude degree and cannot be made perturbative by amplitude scaling.

For the exact cycle above, the complete rational calculation gives

    b3(2p)=(0,-4/65,0),
    b3(2q)=(-1/50,1/50,0),

so the relative copied-carrier gains are 8/65 and 1/25, not a common multiplier. The same complete four-leaf tree creates the exterior carrier

    b3(3p+q)=(-11/52000,77/52000,0) != 0.

These are complete support calculations, not selected trees. At fixed positive viscosity the first four-leaf birth is unchanged: a heat insertion preserves support and consumes temporal order without increasing input degree, so it cannot contribute at the first temporal appearance of a carrier requiring four initial leaves.

Thus N composed with N is not the NS turnover map. A source-cycle fixed point cannot be promoted to a renormalization fixed point without controlling the other same-order interaction trees and the inherited exterior.

An adversarial symbolic search also finds exceptional geometries where the two copied temporal coefficients align again. Therefore the result is deliberately scoped: it rules out the naive source-map iteration and proves an exterior birth in the tested family, but it does not prove universal polarization mismatch or exclude a correlated full-state return at a later time.

## 4. Newborn regeneration efficiency for the six-carrier ring

For the repository's six-carrier ring, exact full-ring arithmetic gives the carrier-level ratio between the newborn daughter's self-source efficiency and the parent's efficiency

    r^2 = 125485383 / 1340266400,
    r approximately 0.305986.

For R3 packets the envelope is inherited. If the parent bump is phi, the first daughter has envelope phi*phi and its self-source has envelope phi^{*4}. The actual ratio is multiplied by

    ||phi^{*4}||_2 ||phi||_2^2 / ||phi*phi||_2^3.

For a Gaussian this factor is 2^(3/4), giving

    0.51460 < rho_G < 0.51461.

The checker certifies these bounds by exact rational fourth-power comparisons. Smooth nonnegative compact bumps approximate the Gaussian ratio, so one can choose a fixed admissible bump with ratio >0.51.

By local well-posedness and continuity of the original R3 solution from the corresponding packet datum, for every fixed positive viscosity there is a positive interval on which

    gamma_(2K0)(u(t)) > 0.51 gamma_(K0)(d) > 0.

All modes, pressure, reverse interactions and packet errors belong to the actual solution. This defeats a universal immediate-halving argument.

It is not a regenerative turnover theorem. At birth,

    a_(2K0)(u(t)) = const * t + O(t^2),

so the daughter's critical amplitude tends to zero. No order-one amplitude transfer, critical-clock interval, second turnover, shadowing theorem, or input-summable cost is obtained.

## 5. Computational scope

`research/check_source_cycles_and_birth.py` performs exact rational arithmetic for the source cycle, complete temporal trees, six-carrier newborn efficiency and a broad integer-carrier search. The recorded run passed 12,357 assertions over 384 carrier geometries.

`research/check_symbolic_cycle_geometry.py` checks the general symbolic geometry, the exterior coefficient and the exceptional alignment branch; the recorded run passed 11 symbolic identities.

`research/discovery_regeneration_turnovers.py` is floating-point periodic Galerkin discovery only. A run at N=18, nu=.01, dt=.00625, T=.5 retained all modes inside the spherical cutoff and found no sampled two-turnover benchmark. This is not a continuum or R3 no-go theorem.

The inherited exact checkers and `python3 research/verify.py --research-only` passed in the full local checkout before the original local commit. These checks certify finite algebra and repository integrity, not the continuum proof or independent mathematical correctness.

## 6. Tao discriminator and handoff

The calculations use the exact original support relation k=p+q and the actual Leray numerator. Tao's averaged cascade can assign a nonzero same-level pump coefficient which need not obey the original self-convolution support restriction. This remains an exact operator discriminator, but it does not itself yield the RF-q upper producer.

The dominant remaining theorem is therefore a return-time theorem for the ENTIRE actual NS state: either construct a scale-repeating concentration-producing cell on shrinking critical clocks while retaining the inherited nonperturbative exterior, pressure, reverse channels and viscosity, with a rigorous shadowing theorem; or prove that every such regenerative event pays an input-summable original-NS-specific cost and connect the event extraction to the every-upper-time RF-q producer.

No NS-R3 proof, blowup construction, turnover-level cost, arbitrary-data RF-q producer, or independent mathematical audit is claimed.