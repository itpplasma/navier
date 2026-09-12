# Six growing half-grade ancestors give a rank-four quadratic bridge to the next source-parent quartet

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@b65c240284cef29a0589b02fb30dad130f2c0e33`.

**Status: exact frozen source-reference frequency/polarization theorem with exact radical checker; independent mathematical audit and novelty assessment pending.** This packet is the first positive checkpoint after the route diversified to grade-changing/nonparent late regeneration. It proves a local algebraic bridge conditional on six half-grade ancestors being available near the next source window. It does not supply those ancestors from one global trace and it is not yet a physical finite-duration theorem.

## 1. Prediction before the test

The four-parent factor-two relay looked intrinsically mixed order: two desired doubled parents are born quadratically and two only quartically. The same full dynamics, however, also creates unavoidable cubic extreme sidebands. After factor-two normalization those sidebands are linearly unstable half-grade modes rather than useless pollutants.

Prediction: enlarge the inherited state from the four old parent frequencies to the six half-grade frequencies

    14, -13, 5, -4, 2, -1,

where a key `x` denotes the normalized half-grade vector

    h_x=(x/20,0,1/2).

Then the two extreme modes should repair the hard channels: all four next `z=1` parents should be obtainable by direct quadratic interactions, and the leading map from the six ancestor amplitudes to the four next-parent growing coordinates should have rank four.

## 2. Both cubic extremes are genuinely present

The previously frozen pollution theorem proves that pair `A`, with positive parent keys `5,-4`, creates the cubic extreme `14` with a nonzero growing coordinate and that this frequency is the unique cubic monomial

    14=5+5-(-4).

Recomputing the complete order-two Taylor coefficient also gives the reflected positive-frequency extreme

    -13=-4-4-5,

again with a strictly nonzero growing coordinate. Inside the complete four-parent key set `{5,-4,2,-1}`, the only two-positive/one-reflected representation of `-13` is the monomial

    A_2^2 conjugate(A_1).

Thus the second designated pair cannot cancel either extreme while pair `A` remains active.

The exact checker encloses both complete cubic coefficients away from zero; no selected-tree numerator is used.

## 3. All six ancestors grow at half grade

At the next factor-two normalization a key `x` has

    z=1/2,     s=x/10.

The source-reference positive rate is

    r_+(z,s)=1/sqrt(1+s^2)-(3/5)z^2(1+s^2).

The old four parent keys are already known to lie inside the `z=1/2` unstable interval. For the two extremes,

    r_+(1/2,7/5)=5/sqrt(74)-111/250 >0,

and

    r_+(1/2,-13/10)=10/sqrt(269)-807/2000 >0.

Hence all six bridge coordinates are linearly growing in the frozen reference at the late half-grade stage.

## 4. Four exact quadratic edges

Two half-grade keys `a,b` sum to the next `z=1` parent key `K` precisely when

    a+b=2K.

The six-mode state contains the four interactions

    14 + (-4) = 10  -> K= 5,
   -13 +   5  = -8  -> K=-4,
     5 +  (-1)=  4  -> K= 2,
    -4 +   2  = -2  -> K=-1.

Thus the two extremes feed the formerly hard outer parents, while the old modes feed the two inner parents.

Using the full unordered incompressible Leray symbol

    C(p,a;q,b)=P_(p+q)[(a.q)b+(b.p)a]

with the growing half-grade eigenpolarizations, the next-parent growing coordinates are all strictly nonzero. Exact rational enclosures are

    K= 5:
      [72872052669/125000000000,
       36436026339/62500000000],

    K=-4:
      [-288518836401/580000000000,
       -144259418187/290000000000],

    K= 2:
      [8823194511/260000000000,
       17646389031/520000000000],

    K=-1:
      [-1762717383/101000000000,
       -275424591/15781250000].

These are coefficients before the common Fourier `-i` convention factor. Every interval is separated from zero.

## 5. The leading target map has rank four

Let the six complex positive-frequency ancestor amplitudes be

    x_14, x_-13, x_5, x_-4, x_2, x_-1.

At quadratic order the four selected next-parent growing coordinates have the monomial form

    T_5   =c_5   x_14  x_-4,
    T_-4  =c_-4  x_-13 x_5,
    T_2   =c_2   x_5   x_-1,
    T_-1  =c_-1  x_-4  x_2,

with every `c_K` nonzero by Section 4.

Fix any nonzero `x_5,x_-4`. The Jacobian with respect to

    (x_14,x_-13,x_-1,x_2)

is diagonal up to target ordering, with determinant

    c_5 c_-4 c_2 c_-1 x_-4^2 x_5^2 !=0.

Therefore the leading quadratic map is locally onto the four complex next-parent coordinates. In particular the old two-hard/two-easy order mismatch is **not intrinsic to a grade-changing six-mode state**. It arose from restricting the inherited state to the original four coordinates.

Reality simply fixes the negative-frequency coefficients by conjugation and does not remove these positive-frequency degrees of freedom.

## 6. Meaning for the terminal frontier

This converts an earlier obstruction into a candidate resource: the extreme cubic pollutants can act as bridge coordinates one scale later. Conditional on six comparable half-grade modes being available sufficiently late, there is no local frequency, polarization, or leading-order rank obstruction to generating a balanced next parent quartet quadratically.

The new first dependency is therefore **causal late supply of the six half-grade ancestors**. Passive reuse of the old four is already excluded by the super-amplification theorem. A constructive proof must either regenerate all six near the next window, or prove a finite-duration nonlinear stage which depletes/renormalizes the over-amplified old parents while preserving the two useful extremes. Before attacking global supply, the immediate local question is whether this rank-four leading map persists for a full short-time infinite-lattice evolution, rather than only in the instantaneous quadratic symbol.

No common Schwartz trace, physical whole-space bridge, nonlinear de-forcing solution, singularity preservation, or `NS-R3` conclusion is claimed.

Companion checker: `research/check_half_grade_six_mode_bridge.py`.
