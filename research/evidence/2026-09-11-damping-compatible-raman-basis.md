# A damping-compatible state-triggered Raman basis

Date: 2026-09-11. Repository input:
`itpplasma/navier@292ad7721e92847293185f5842fea8675665c44c`.

**Status: exact leading effective-symbol theorem.** The first-order off-target
clutter obstruction from the initial state-triggered Raman basis can be removed
algebraically. There are five explicit Raman modules which simultaneously:

* have exactly Leray-zero direct high-high difference-frequency output;
* span the full trace-free symmetric strain space when triggered by the actual
  contaminated middle second target;
* have no translated-frequency collision with any of the five desired purifier
  outputs or the three clean second-target windows;
* send every explicitly tracked original parent, first-generation carrier and
  other second target either to zero or to a mode strictly damped by the same
  `M=2048` inheritance filter; and
* send the complete inherited ladder `r_n=(-n,-1,0)`, `n>=1`, only to modes
  strictly damped by that filter.

The exact certificate is
`research/check_damping_compatible_raman_basis.py`.

This closes the **single-Raman-step finite-carrier clutter** problem. It does
not yet close repeated Raman translations, simultaneous high-module
interactions, or the time-integrated original-NS realization.

## 1. Frozen five-module geometry

Use the actual middle target

    h=(z-2,-1,-1)                                        (1.1)

and its complete ancestry-contaminated leading coefficient `a_full(z)` from the
second-generation wall, with only the common Fourier phase removed.

For a low shift `l` and a high direction `Q` with `l.Q=0`, use the equal-length
near-opposite construction from the preceding packet. The improved basis is

    l_1=(-3, 0, 0),      Q_1=(0, 3,-1),
    l_2=(-2,-2, 1),      Q_2=(2,-2, 0),
    l_3=(-2, 2, 0),      Q_3=(2, 2,-1),
    l_4=( 0,-3, 0),      Q_4=(2, 0,-2),
    l_5=(-1,-2,-2),      Q_5=(0, 2,-2).                  (1.2)

Every `l_j.Q_j` is exactly zero. Put

    m_j=Q_j cross l_j,                                    (1.3)

    q_j=l_j/2+N Q_j,
    r_j=l_j/2-N Q_j,                                      (1.4)

and

    beta_j
      =l_j-|l_j|^2/(2N|Q_j|^2) Q_j+m_j,

    epsilon_j
      =l_j+|l_j|^2/(2N|Q_j|^2) Q_j-m_j.                  (1.5)

Then

    q_j.beta_j=r_j.epsilon_j=0                            (1.6)

and the complete unprojected direct quadratic source at `l_j` is

    (beta_j.r_j)epsilon_j+(epsilon_j.q_j)beta_j
      =2 |l_j|^2 l_j.                                    (1.7)

Therefore its Leray projection is exactly zero for every `N`.

## 2. Effective target-triggered strain basis

Let

    kappa_j=h+l_j.                                        (2.1)

For a generic slow input `(k,a)`, the leading high-frequency two-step Raman
translation through module `j` has output frequency `k+l_j`; up to its scalar
input factor `a.Q_j`, its transverse direction is

    D_j(k)
      =P_(k+l_j)[
          (l_j.(k+l_j))l_j
          -(m_j.(k+l_j))m_j].                            (2.2)

For the actual trigger `(h,a_full)`, the effective strain tensor is

    T_j
      =sym(D_j(h) tensor kappa_j)                         (2.3)

up to a nonzero scalar factor `2(a_full.Q_j)`.

After clearing only common trigger and Leray denominators, the five coordinate
columns `(T_11,T_22,T_12,T_13,T_23)` have a degree-70 determinant. Its exact
gcd with the clean return polynomial

    Q_clean(z)
      =z^10-z^9+4z^8+2z^6-2z^5
       -8z^3-32z^2+40z-16                               (2.4)

is `1`. Hence the determinant is nonzero at every clean return root, in
particular at the unique positive root in

    1.2847<z_*<1.2848.                                   (2.5)

The five triggered tensors therefore form a basis of `Sym_0(3)` at the actual
clean root and synthesize the exact inheritance filter

    H = [[ 71/100,   -1,       147/200],
         [ -1,      -143/200,   7/25  ],
         [147/200,    7/25,     1/200 ]].                 (2.6)

This is an algebraic basis certificate, not a numerical condition-number
claim.

## 3. No first-order collision with required windows

The finite pre-filter slow set is

    p1=(1,0,0),
    p2=(0,1,0),
    p3=(-z,0,1),                                          (3.1)

    g1=(-1,-1,0),
    g2=(1+z,0,-1),
    g3=(1-z,0,1),                                         (3.2)

plus the two non-trigger second targets

    h_+=(-z,1,1),
    h_-=(-z,-1,1).                                       (3.3)

For every module `j` and every `k` in this set, the checker compares

    k+l_j                                                   (3.4)

against all five desired purifier frequencies `h+l_i` and all three clean
second-target windows. In every case at least one coordinate difference is a
polynomial coprime to `Q_clean`; therefore no equality can occur at the clean
algebraic root.

So a first Raman translation of an old finite carrier cannot masquerade as a
desired purifier component or overwrite one of the clean target windows.

## 4. The same H damps every finite translated contaminant

For a nonzero translated direction `D_j(k)`, define the exact normalized rate
at strength `M=2048`

    R_j(k)
      =-2048 [D_j(k)^T H D_j(k)]/|D_j(k)|^2
       -|k+l_j|^2.                                       (4.1)

The checker clears the positive direction norm and obtains one exact polynomial
rate numerator in `z` for each of the `5 x 8` finite translated modes. Every
nonzero numerator has no root in the entire clean-root isolating interval and
is negative at its rational midpoint. Two translations are identically zero
and hence harmless.

Therefore

    R_j(k)<0                                               (4.2)

for every active first-order translated finite contaminant at `z=z_*`.

This is stronger than spectral noncollision: if the common filter has been
formed, all these translated sidebands point into its damped cone rather than
its amplified cone.

## 5. The complete inherited ladder is also safe at one Raman step

The old all-orders ancestry family is

    r_n=(-n,-1,0),       n>=1,                            (5.1)

with fixed polarization `e3`. For each of the five Raman shifts, apply (2.2) to
`r_n`. The exact rate numerator (4.1) becomes a rational polynomial in the
integer `n`, independent of `z`.

After changing sign, each polynomial is positive at `n=1` and has no real root
on `[1,infinity)`, by exact Sturm counting. Hence

    R_j(r_n)<0

for every `j=1,...,5` and every integer `n>=1`.            (5.2)

Thus the state-triggered module does not merely avoid the first few inherited
modes; its **entire previously known infinite ladder** is mapped into the damped
sector at first effective Raman order.

## 6. What this removes

The initial Raman packet left a sharp question: order-one pump strength also
translates every old slow mode, so perhaps any useful target-triggered filter
necessarily creates equally dangerous low clutter.

The present exact basis answers that question negatively. There is enough
geometric freedom in `(l,Q)` to satisfy the strain-span constraints and the
finite/infinite damping constraints simultaneously.

At leading effective order, the route can therefore be organized as

    clean ancestry creates actual h target
      -> five silent high pairs act conditionally on slow modes
      -> h-translations synthesize H
      -> all old first translations land in H-damped directions.             (6.1)

This is the first purifier architecture in the repository that has, at the
same algebraic level, both **state-triggered switch-on** and **inheritance-aware
clutter control**.

## 7. Recomputed frontier: repeated Raman translations

The leading effective Raman coefficient must be order one to create an
advective-strength filter. Hence a first translated contaminant cannot simply
be discarded after one step. While the high pairs remain active, it can be
translated again:

    k -> k+l_i -> k+l_i+l_j -> ...                         (7.1)

The five shifts generate a lattice semigroup. Even though every one-step old
translation is damped by `H`, repeated translations can in principle:

* return to a required window through an integer relation among the `l_j`;
* enter an `H`-amplified polarization cone;
* generate a low-frequency cycle before viscosity/filter damping wins; or
* create a nonnormal effective slow operator whose transient gain invalidates
  carrierwise rate tests.

The next decisive calculation is therefore **not** another isolated module.
It is the finite/high-mode-eliminated slow generator on the Raman lattice,
including the five shift operators, viscosity, and the `H` filter. One should
first search for exact short integer cycles and invariant congruence classes;
then truncate by a coercive large-|k| bound and compute an exact/numerically
certified spectral or energy estimate on the remaining finite lattice.

If this effective operator is dissipative off the five intended `h+l_j`
components, the next blocker becomes lifting the effective Raman dynamics to
one original-NS Cauchy history with `rho^2/R=O(1)`. If it has an unstable
off-target cycle, that cycle is the precise obstruction to record.

No PLAN/canonical proof-graph promotion, recursive turnover, finite-time
singularity, or `NS-R3` conclusion is made here.
