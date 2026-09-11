# Birth-then-linear amplification cannot balance the mixed-order four-parent relay

Date: 2026-09-12. Repository input: `itpplasma/navier@ba76db1caa4941e771c46cdbfe3275203abae877`.

**Status: exact scoped algebraic/spectral obstruction; author proof with exact checker, independent mathematical audit and novelty assessment pending.** The theorem closes a specific finite-duration stage architecture: generate the four doubled parents using only the existing four dual-tuned parents, then apply one common interval of linear positive-branch amplification. It does not exclude genuinely nonlinear saturation, additional stable target preloads, extra-mode interference, a larger expanding-state stage map, sparse exterior entry, or the complete physical adjoint.

## 1. Prediction and terminal consumer

The mixed-order relay theorem leaves two hard doubled parents born first at quartic amplitude order and two easy doubled parents born already at quadratic order. A tempting repair is to retune the four parent amplitudes and then let the source instability amplify the weak hard channels until all four become comparable.

Prediction before the exact test: the dual pair-product constraints force a nonzero invariant product of the two easy quadratic outputs, so both cannot be suppressed simultaneously; moreover the easy tilts have strictly larger linear positive-branch growth rates than the hard tilts. If both statements hold, any stage of the form

    four dual-tuned parents -> local birth -> common linear amplification

moves the returned state farther from a balanced four-parent input class.

The intended terminal consumer remains UE1: one global history must regenerate all four growing parent traces at every source scale without resetting inherited modes.

## 2. Dual tuning fixes the product of the easy children

Use the four caged parents

    p_1=( 1/2, 0,1),
    p_2=(-2/5, 0,1),
    p_3=( 1/5, 0,1),
    p_4=(-1/10,0,1),

with growing source polarizations `a_+(s)`. Let their complex amplitudes be `A_1,...,A_4`.

The dual common-daughter tuning fixes the two pair products at the scale of a common small parameter `epsilon`:

    A_1 A_2 = w_A epsilon^2,
    A_3 A_4 = w_B epsilon^2,                              (2.1)

where the previously frozen determinant calculation gives `w_A !=0`, `w_B !=0`.

At the two easy doubled targets, self-pairs vanish by incompressibility and the surviving cross-pair growing coordinates have nonzero universal coefficients `e_3,e_4`:

    E_3 = e_3 A_1 A_4,
    E_4 = e_4 A_2 A_3.                                   (2.2)

The exact checker encloses both `e_3` and `e_4` away from zero. Multiplying (2.2) and using (2.1) gives the identity

    E_3 E_4 = e_3 e_4 w_A w_B epsilon^4 !=0.             (2.3)

Therefore no choice of individual amplitudes preserving the two dual pair products can make both easy quadratic children small beyond their natural product scale. In particular, in any balanced parent class `|A_j| comparable to epsilon`, at least one easy child has magnitude `>=c epsilon^2`, whereas the two hard channels first appear at `O(epsilon^4)`.

This is not a dimension count and does not assume equal parent amplitudes. It is an exact multiplicative constraint.

## 3. Linear growth ordering worsens the imbalance

At normalized parent scale `z=1` the positive source-reference growth rate is

    r_+(s)=1/sqrt(1+s^2)-(3/5)(1+s^2).                   (3.1)

Put `x=1+s^2`. The scalar function

    f(x)=x^(-1/2)-(3/5)x

has

    f'(x)=-(1/2)x^(-3/2)-3/5 <0.                         (3.2)

For the four parent tilts,

    1+s_4^2 < 1+s_3^2 < 1+s_2^2 < 1+s_1^2.              (3.3)

Hence the exact rate ordering is

    r_4 > r_3 > r_2 > r_1.                               (3.4)

The easy channels correspond to `p_3,p_4`; the hard channels to `p_1,p_2`. Thus even the **slowest** easy rate exceeds the **fastest** hard rate:

    min(r_3,r_4) > max(r_1,r_2).                         (3.5)

Suppose after local birth the four channels are allowed to evolve for any common positive time interval under their diagonal positive-branch linear dynamics. Then every easy/hard amplitude ratio grows by an additional positive exponential factor. Linear amplification cannot restore the hard pair to the easy scale; it makes the mismatch strictly worse.

The same conclusion persists under sufficiently small finite-`L` rate perturbations on a fixed fast-time window because the strict ordering margin is positive. No claim is made on a full physical interstage interval.

## 4. Closed architecture and surviving repair

Equations (2.3) and (3.5) close the architecture

    dual-tuned four-parent birth + common linear amplification.

The stage cannot be balanced by redistributing the original four parent amplitudes while preserving the load-bearing dual tuning, and it cannot be balanced by simply waiting for the hard channels to catch up.

A successful stage must therefore add a genuinely nonlinear or higher-dimensional operation, for example:

1. nonlinear saturation/depletion that preferentially limits the easy channels;
2. additional grade-`2m` stable target preloads or extra modes that destructively interfere with the easy quadratic births while preserving the hard channels;
3. a larger expanding-state graph transform whose admissible input class already contains the required counterterms; or
4. abandonment of this cascade route in favor of the full physical interstage adjoint/propagator or sparse exterior-entry mechanisms.

Because the previous checkpoint identified the mixed-order mismatch and this theorem shows the obvious linear-amplification repair fails, another estimate of the same four-channel linear stage is not a distinct mechanism under the repository diversification rule.

## 5. Scope and exact check

`research/check_stage_balance_wall.py` verifies the dual pair-product identity, strict nonzero easy interaction coefficients by exact radical enclosure, the invariant product (2.3), and the exact linear-rate ordering (3.4)--(3.5).

This theorem is source-reference/fixed-window structure. It proves no nonlinear saturation bound, no stable-preload recursion, no global common trace, no physical interstage adapter, no singularity preservation, and no `NS-R3` result.
