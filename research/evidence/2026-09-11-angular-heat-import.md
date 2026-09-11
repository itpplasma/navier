# Angular heat-import barrier and the surviving exterior route

Date: 2026-09-11. Repository input for this packet:
`itpplasma/navier@9a8831569317d3d5a6c2e88621bd0fbef31a81d2`.

**Status: author proof; independent mathematical audit and novelty undetermined.**
No unforced singular solution, arbitrary-data regularity theorem, or canonical
claim is promoted. The result excludes a specific surviving shortcut: store
the future high-angular pulse in the existing/passive exterior and rely on
ordinary diffusion, or on source-sized radial motion during the pulse startup
window, to import it into the shrinking annulus. It does not exclude a
redesigned exterior with load-bearing nonlinear transport.

The motivation is the exact alternative proved in
`2026-09-08-angular-preparation-obstruction.md`: a homogeneous high-angular
mode that remains substantially inside the shrinking column for most of its
prehistory is killed by cumulative viscosity. Consequently a plausible escape
was to keep future modes mostly outside and import them shortly before they
are amplified. The source itself has an exact heat exterior, but its velocity
there is purely azimuthal and has no radial advection. The source's physical
description also places the oscillatory pulses at the core/annulus edge and
states that an exponentially small external force seeds each pulse before
background shear amplifies it.

## 1. Exact scalar heat observation bound in one angular harmonic

Let `a=nu t>0`. For a scalar function on R2 in the angular harmonic m>=0,

    f(r,theta)=f_m(r) exp(i m theta),

ordinary heat evolution preserves m. With radial L2 measure `r dr`, its
kernel is

    K_m^a(r,s)=(1/(2a)) exp[-(r^2+s^2)/(4a)]
                         I_m(rs/(2a)),                    (1.1)

where `I_m` is the modified Bessel function. This follows by expanding the
2D Gaussian heat kernel in the angular difference. No asymptotic formula is
used below.

The series

    I_m(z)=sum_(k>=0) (z/2)^(2k+m)/(k!(k+m)!)

and `(k+m)! >= m! k!` give, for z>=0,

    I_m(z) <= (z/2)^m e^z/m!.                            (1.2)

Therefore

    |K_m^a(r,s)| <= (1/(2a)m!) (rs/(4a))^m
                    exp[-(r-s)^2/(4a)].                  (1.3)

### Theorem 1: high angular modes cannot enter a small cylinder cheaply by heat

Let `H_m^a` denote the scalar heat operator (1.1), and restrict its output to
`0<r<R`. For m>=1 and `R^2<=a`,

    ||1_(r<R) H_m^a||_(L2(rdr)->L2(rdr))
       <= R/sqrt(2a(m+1))
          [R^2/(2a)]^(m/2) / sqrt(m!).                   (1.4)

Proof. The operator norm is bounded by its Hilbert--Schmidt norm. Squaring
(1.3) reduces the required double integral to

    P_m integral_0^R r^(2m+1)
        integral_0^infinity s^(2m+1)
          exp[-(r-s)^2/(2a)] ds dr,

    P_m=[4a^2(4a)^(2m)(m!)^2]^-1.                       (1.5)

Put y=s-r and use, for r<=R,

    s^(2m+1) <= 2^(2m)[R^(2m+1)+|y|^(2m+1)].             (1.6)

The two whole-line Gaussian integrals are

    integral_R exp[-y^2/(2a)]dy = sqrt(2 pi a),
    integral_R |y|^(2m+1) exp[-y^2/(2a)]dy
        =2^(m+1) a^(m+1) m!.                             (1.7)

After `integral_0^R r^(2m+1)dr=R^(2m+2)/(2m+2)`, the squared
Hilbert--Schmidt norm is at most A_m+B_m, where

    A_m = sqrt(2pi) R^3/[8a^(3/2)(m+1)]
          [R^4/(4a^2)]^m/(m!)^2,

    B_m = R^2/[4a(m+1)] [R^2/(2a)]^m/m!.                (1.8)

Their ratio is

    A_m/B_m = sqrt(pi/2) (R/sqrt a)
              [R^2/(2a)]^m/m! < 1                      (1.9)

under `R^2<=a`, m>=1. Thus A_m+B_m<=2B_m and (1.4) follows. QED.

The estimate is much stronger than a radial Gaussian off-diagonal bound:
it also records the angular-momentum barrier. It allows the initial datum to
be anywhere in radius; no exterior-support assumption is needed.

## 2. Vector rotation modes and three dimensions

Use the repository's rotation convention

    (T_alpha v)(x)=R_(-alpha)v(R_alpha x).

A vector rotation mode n has cylindrical components proportional to
`exp(i n theta)`. Its Cartesian combinations `v_x +/- i v_y` have scalar
angular harmonics n+1 and n-1, while `v_z` has harmonic n. Ordinary heat
acts componentwise. The axial 1D heat factor has L2 operator norm at most one.
Consequently, for |n|>=2, Theorem 1 gives the same bound up to a fixed
universal vector factor with

    m=|n|-1.                                               (2.1)

In particular, for the cylinder `C_R={x in R3:r<R}`,

    ||1_(C_R) e^(nu t Delta) Pi_n||_(L2->L2)
       <= C R/sqrt(a(m+1))
           [R^2/(2a)]^(m/2)/sqrt(m!),                    (2.2)

whenever `a=nu t` and `R^2<=a`. This is an observation estimate for pure
heat, not for the full linearized Navier--Stokes equation around a sheared
background.

## 3. Source-scale consequence from one fixed earlier Cauchy time

The source pulse scaling recorded and audited in the repository is

    Q=2^(-ell),       epsilon=Q^h,       0<h<1/100,
    L comparable to ell^2,
    k comparable to Q^(-h/2),                            (3.1)

and the pulse annulus has radial scale `R comparable to sqrt Q` on a
nondegenerate label. If the angular pitch p is bounded away from zero, its
actual rotation index satisfies

    m=|n|-1 >= c Q^(-h/2)                                (3.2)

for all sufficiently large ell.

Fix one earlier physical time t0 strictly below the pulse times approaching
1. Then `a_j=nu(t_j-t0)` is bounded below by one positive constant. Applying
(2.2) with `R_j^2<=C Q_j` gives, after harmless fixed constants,

    ||1_(C_Rj) e^(nu(t_j-t0)Delta) Pi_(n_j)||
       <= C Q_j^(m_j/2).                                  (3.3)

The factorial only improves this estimate. Its logarithm obeys

    log RHS <= -c ell_j 2^(h ell_j/2)                    (3.4)

on every nondegenerate-pitch subsequence. Hence, for every fixed C_*,

    Q_j^(m_j/2) = o(exp[-C_* ell_j^2]).                   (3.5)

The local source pulse entry seed found in
`2026-09-10-source-pulse-adjoint.md` has coefficient size comparable to
`P(0)=exp(-gamma L)` with gamma>0 and `L comparable to ell^2`. Fixed powers
of Q and polynomial factors in ell do not alter the comparison (3.5).
Therefore a uniformly bounded L2 initial rotation mode evolved **only by
ordinary heat from one fixed earlier time** reaches the shrinking pulse
cylinder at a scale asymptotically far below the required source-type entry
seed.

This is a pure-diffusion exclusion. Applying it directly to a complete
physical pulse norm requires the usual regular-patch lower normalization
between coefficient and physical field; the source's fixed powers of Q do
not affect the exponent comparison. No statement is made for labels whose
angular pitch degenerates so that (3.2) fails.

## 4. The last-moment source-sized radial-import window is also too thin

There is a second, independent scaling obstruction to simply storing the
seed a macroscopic radial distance outside the annulus and moving it inward
only during pulse activation.

For a fixed lifted pulse label the inspected source coordinates have

    partial_t v = Q^(-1-h),                              (4.1)

and the fast pulse interval has length `L comparable to ell^2`. Its physical
activation duration is therefore

    Delta t_pulse comparable to Q^(1+h) L.               (4.2)

The source core/annulus radial scale is `R comparable to sqrt Q`, while the
source-sized radial velocity satisfies

    |u_r| <= C Q^(-1/2)                                  (4.3)

on the corresponding `q comparable to Q` regime. During one complete pulse
window, such radial advection can move material by at most

    Delta r_adv <= C Q^(-1/2) Q^(1+h)L
                 = C sqrt(Q) Q^h L.                      (4.4)

Relative to the annulus radius,

    Delta r_adv/R <= C Q^h L -> 0.                       (4.5)

Pure radial diffusion during the same window reaches only

    Delta r_diff comparable to sqrt(nu Delta t_pulse)
       <= C sqrt(Q) Q^(h/2) sqrt(L),                     (4.6)

so

    Delta r_diff/R <= C Q^(h/2) sqrt(L) -> 0.            (4.7)

Thus neither the source-sized radial flow nor ordinary diffusion can fetch a
future pulse from a fixed positive fraction of the annulus radius during its
startup window. A late-import seed must already occupy a vanishingly thin
radial collar before activation. But storing the high-angular mode near that
shrinking radius for a long prehistory is exactly the branch excluded, under
its stated occupation hypotheses, by the earlier angular-preparation theorem.

The estimates (4.4)--(4.7) use only source scaling and do not say that every
redesigned unforced background must have source-sized radial velocity.
A new construction could use a different exterior flow or nonlinear transfer.
Such a change is load-bearing: it is no longer a passive conversion of the
existing heat exterior.

## 5. What is now excluded and what remains genuinely open

Combining this packet with the independently audited scopes already in the
repository gives a useful trichotomy for a nondegenerate high-angular pulse:

1. **Long trapped preload near the shrinking column:** cumulative angular
   viscosity wins by an additional logarithmic preparation factor.
2. **Pure heat storage/import from one fixed earlier time:** Theorem 1 gives
   the super-flat angular observation bound (3.3)--(3.5), too small to supply
   the source-type local seed.
3. **Fetch from a macroscopic radial distance only during the pulse window:**
   source-sized advection and diffusion reach only a vanishing fraction of
   the required distance by (4.5),(4.7).

This rules out the simplest "put all future pulses in the existing exterior
at t=0" repair. It does **not** rule out:

* nondegenerate nonlinear angular generation close to the activation time;
* a redesigned exterior with substantial radial transport;
* spatially remote packets transported by a genuinely different full flow;
* small-pitch labels outside (3.2);
* a full coupled common-trace inverse whose analytic leakage never has the
  passive-heat form used here.

The previous source-regeneration packets already exhibit nonzero nonlinear
birth channels, but have not closed a supercritical localized turnover. The
new `2026-09-11-supercritical-turnover-contract.md` records exactly what such
a turnover must accomplish. The remaining negative route is therefore no
longer "remove a flat seed somehow"; it needs a **load-bearing autonomous
transport/generation mechanism** absent from the source's passive exterior.

## 6. Validation and source provenance

`research/check_angular_heat_import.py` was executed before upload and passed
**132 exact assertions**. It verifies the Hilbert--Schmidt algebra in (1.8),
the ratio (1.9), twenty Gaussian moments, the vector angular-frequency shifts,
and an exact rational source-scale subsequence showing the eventual dominance
of the heat-import exponent over `ell^2` together with decay of the relative
advection/diffusion reaches. The checker is algebraic calibration, not a
continuum certificate; the proof of Theorem 1 is the argument above.

The source scaling used here was already recorded in
`2026-09-08-unforced-support-and-pulse-audit.md`,
`2026-09-08-angular-preparation-obstruction.md`, and
`2026-09-10-source-pulse-adjoint.md`. For this run the public source PDF was
also re-opened and its physical-description pages 3--6 were visually
inspected: the core radial/axial scales, velocity scaling, annular pulse
location, statement that an exponentially small external force seeds each
pulse, and the purely azimuthal heat exterior agree with the repository's
source ledger. No complete source-proof audit was performed.

No full repository checkout was available for this additive packet, so the
repository-wide verifier, all historical checkers, manuscript build and Lean
were not rerun. No PLAN, manuscript or proof-graph status is promoted.
