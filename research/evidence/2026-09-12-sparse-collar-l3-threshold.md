# Sparse collar pressure input has an exact criticality threshold, not automatic `L^3` blowup

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@7734a69523da391800532a4078fb8dcd89141483`.

**Status: analytic scaling theorem built from the existing exact exterior-pressure estimate and Hölder; exact exponent algebra is frozen by a checker. Independent mathematical audit and novelty assessment pending.** The result does not construct a pressure-producing quadratic stress. It closes a tempting negative shortcut: sparsity plus finite energy does not by itself force the thin-collar route to be terminal-strength.

## 1. Prediction before the test

The nondegenerate collar-conveyor estimate gives divergent `L^3`, but the surviving pressure mechanism can use much less kinetic energy because the required parent entry trace is exponentially small in `L`. The question is whether concentrating that energy into a sparse near collar nevertheless forces a critical norm divergence.

Prediction: there is a quantitative sparsity threshold. For a collar thin enough to overcome the angular barrier, the pressure estimate only forces exponentially small kinetic energy. A wide class of exponentially sparse supports still has a pressure/energy/Hölder lower bound on `L^3` which tends to zero rather than infinity.

## 2. Midpoint pressure estimate on a source collar

Use the source scales

    r ~ Q^(1/2),
    N ~ Q^(-h/2),
    L ~ ell^2,       Q=2^(-ell),                         (2.1)

and take an outer radius

    R=r+delta,
    delta/r = kappa L/N,                                 (2.2)

with fixed `kappa>0`. In the exact estimate

    ||Pi_N g||_(L2(C_r))
      <= C0 (r/s)^N (R-s)^(-5/2) ||S||_1,                (2.3)

choose the midpoint `s=r+delta/2`. Then

    (r/s)^N
      = (1+kappa L/(2N))^(-N).                           (2.4)

Since `L/N ->0`, the elementary logarithmic bounds

    x-x^2/2 <= log(1+x) <= x,       x>=0 small,           (2.5)

with `x=kappa L/(2N)` give

    (1/L) log (r/s)^N -> -kappa/2.                        (2.6)

The factor `(R-s)^(-5/2)=(delta/2)^(-5/2)` contributes only `o(L)` to its logarithm: `log r`, `log N` and `log L` are all `O(ell)`, whereas `L~ell^2`. Therefore the operator norm in (2.3) has the exponential scale

    K_L = exp[-(kappa/2)L+o(L)].                          (2.7)

All fixed powers of `Q,N,r,L` are included in the `o(L)` term; none changes the `L`-exponent.

## 3. Minimum energy forced by an entry-scale signal

Suppose the mechanism must directly provide a pressure input of size

    A_L = exp[-C L+o(L)],       C>0.                      (3.1)

For a quadratic stress `S=chi u tensor u`,

    ||S||_1 <= ||u||_2^2=:E_L.                           (3.2)

Equations (2.3) and (2.7) imply the necessary lower bound

    E_L >= exp[-(C-kappa/2)L+o(L)].                       (3.3)

Thus if

    0<kappa<2C,                                           (3.4)

the energy forced by this direct pressure requirement is itself exponentially small. This is exactly the collar regime in which the angular attenuation exponent is weaker than the desired entry exponent.

## 4. Exact sparsity threshold for the forced `L^3` lower bound

The full geometric collar has volume scale

    V_col ~ r^2 delta
          ~ Q^(3/2+h/2) L,                               (4.1)

so `log V_col=o(L)`. Suppose the actual stress-bearing velocity occupies at most the exponentially sparse fraction

    V_L <= exp[-beta L+o(L)] V_col,       beta>=0.        (4.2)

Hölder gives

    ||u||_3 >= ||u||_2 V_L^(-1/6).                        (4.3)

Combining (3.3), (4.1), and (4.2), the lower bound has exponential rate

    (1/L) log ||u||_3
      >= -(C-kappa/2)/2 + beta/6 + o(1).                  (4.4)

Hence the pressure/energy/support-size mechanism forces exponential `L^3` growth only when

    beta > 3(C-kappa/2).                                  (4.5)

At the level of these inequalities, every

    0 <= beta < 3(C-kappa/2)                              (4.6)

is non-obstructive. The interval is nonempty whenever (3.4) holds. In particular, exponentially sparse support is not synonymous with terminal-strength critical norm.

The checker records the exact sample `C=1`, `kappa=1`: the threshold is `beta=3/2`, while `beta=1` gives forced `L^3` exponent `-1/12` and therefore no divergence from this argument.

## 5. Meaning for UE1

This does not prove that such a sparse quadratic stress can actually produce the required parent trace. Equation (2.3) is an upper bound, not an attainability theorem, and the full source-history propagator after the pressure input remains uncontrolled.

What it does prove is that the surviving thin-collar mechanism cannot be excluded by combining only:

1. the current direct-pressure upper bound,
2. finite kinetic energy,
3. collar support size, and
4. the `L^3` continuation criterion.

A negative proof now needs additional structure: an **operator lower bound / non-attainability theorem for divergence-free quadratic stresses**, a stronger angular/localization constraint, or a complete physical adjoint including history gain. A constructive proof would need the complementary explicit stress/propagator mechanism.

No common Schwartz trace, collar parent-supply construction, unforced correction, singularity preservation, or `NS-R3` theorem is claimed.

Companion checker: `research/check_sparse_collar_l3_threshold.py`.
