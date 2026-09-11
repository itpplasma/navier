# Factor-two relay has two quadratic and two quartic parent channels

Date: 2026-09-12. Repository input: `itpplasma/navier@43499559d73dac6dca62529881dd558aeb503f7f`.

**Status: exact source-reference algebra / author proof with exact checker; independent mathematical audit and novelty assessment pending.** This refines the phase-graded factor-two route. It does not construct a finite-duration stage map, a common Schwartz trace, a nonlinear de-forcing solution, or an unforced singularity.

## 1. Prediction and discriminator

Prediction before testing: because the desired doubled-parent grade is `2m`, all four doubled parents might first occur at quartic amplitude degree, in which case every complete first-relay coefficient would acquire the same cubic factor under uniform frequency rescaling.

The exact discriminator is cheaper and sharper than recomputing the full `t^3` jet: inspect the complete quadratic coefficient at each doubled positive parent frequency, then use the exact homogeneity of the incompressible bilinear symbol under uniform frequency scaling.

Use the caged parent tilts

    s_1= 1/2,    s_2=-2/5,    s_3=1/5,    s_4=-1/10,

with wavevectors `p_j=(s_j,0,1)` and growing polarizations

    a_+(s)=(1,-sqrt(1+s^2),-s).

The dual pair-product tuning is the one already frozen in
`2026-09-11-source-factor-two-relay.md`.

## 2. Exact quadratic split

For the unordered Leray coefficient

    C(p,a;q,b)=P_(p+q)[(a.q)b+(b.p)a],

consider all positive-parent decompositions of each doubled target.

For `2p_1` and `2p_2`, the only quadratic decompositions are the self-pairs

    p_1+p_1=2p_1,    p_2+p_2=2p_2.

Since every parent polarization is transverse to its own wavevector,

    C(p,a;p,a)=0.

Therefore the complete quadratic growing coordinate vanishes identically at these two targets. Their first known nonzero terms remain the already-frozen quartic/time-order-three coefficients of the complete `t^3` relay theorem.

For the other two targets the lattice admits cross-pair decompositions:

    2p_3 = p_1+p_4 = p_3+p_3 = p_4+p_1,
    2p_4 = p_2+p_3 = p_3+p_2 = p_4+p_4.

After the same dual pair-product tuning, the complete quadratic growing coordinates are strictly nonzero. Exact rational radical enclosures from `research/check_relay_scale_homogeneity.py` give

    Pi_+^(2p_3) U_1 in
      [-25078897431/208520000000000,
       -5015778201/41704000000000],

    Pi_+^(2p_4) U_1 in
      [-34933887/40501000000000,
       -43666749/50626250000000].

Both intervals are strictly negative. Thus the first factor-two relay is intrinsically **mixed order**:

    hard channels 2p_1,2p_2: quartic amplitude degree,
    easy channels 2p_3,2p_4: quadratic amplitude degree.

This falsifies the symmetric-four-channel quartic prediction.

## 3. Exact frequency-scale homogeneity

Uniformly scale all wavevectors by `alpha>0`, leaving tilt and polarization unchanged. Since the Leray projector is homogeneous of degree zero,

    P_(alpha k)=P_k,

and each dot product with a wavevector contributes one factor of `alpha`. Hence

    C(alpha p,a; alpha q,b)=alpha C(p,a;q,b).              (3.1)

The easy quadratic channels therefore scale exactly as `alpha`.

For either hard target, grade `2m` permits only even amplitude degree. Degree two is exactly the self-pair and vanishes identically for every transverse polarization at that wavevector. The already-proved first nonzero hard contribution is degree four and time order three. Every such degree-four tree contains exactly three quadratic vertices. Equation (3.1) therefore gives the exact scale law

    hard coefficient(alpha)=alpha^3 hard coefficient(1).  (3.2)

At factor-two stage normalization `alpha=1/2`, the local source-reference births retain the nonzero factors

    hard channels: 1/8,
    easy channels: 1/2.                                   (3.3)

No sign crossing or disappearance occurs merely from frequency renormalization.

## 4. Consequence for the terminal frontier

The reference passive-carry theorem shows that simply birthing a doubled mode early and waiting until it becomes next-stage unstable loses by `exp(-c Q^{-h})`. The present theorem shows that **local late regeneration itself does not disappear under stage rescaling**. In fact two channels are lower nonlinear order than previously assumed.

Therefore the surviving constructive mechanism is more specific:

1. use continuous/late nonlinear feeding near each stage, not passive interstage storage;
2. control the asymmetric mixed-order returned state, with two easy `O(epsilon^2)` channels and two hard `O(epsilon^4)` channels;
3. retain the grade-`m` cubic pollutant and the expanding inherited unstable family; and
4. obtain finite-duration stage amplification strong enough that the hard channels are restored to the four-parent input class before the next relay.

The first uncontrolled quantity is now the **hard/easy amplitude balance of a finite-duration stage map**, not the existence of a nonzero local frequency path. A proof must quantify depletion, viscosity, source growth, every returned sideband, physical localization, and the one-trace interstage history. Conversely, an obstruction should show that the hard channels necessarily fall below the required next-stage seed scale relative to the easy channels or force a terminal-strength critical norm.

## 5. Scope and exact check

`research/check_relay_scale_homogeneity.py` verifies the complete quadratic decomposition list, exact vanishing of the two self-pair hard channels, strict rational enclosures for the two easy growing coordinates, bilinear frequency homogeneity, phase-grade parity through degree four, and the factor-two scale factors `1/8` and `1/2`.

The previously frozen complete `t^3` relay theorem supplies the nonzero hard quartic coefficients; this packet does not recompute them. No continuum finite-duration stage map, physical source propagator, common trace, singularity preservation, or `NS-R3` result is claimed.
