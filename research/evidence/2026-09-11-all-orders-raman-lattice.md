# All-orders effective Raman lattice is inheritance-safe

Date: 2026-09-11. Repository input:
`itpplasma/navier@c4ec09948dea4e3ebb110ad040e208569e786af4`.

**Status: exact author theorem for every order of the leading high-frequency
effective Raman slow operator.** A five-module state-triggered purifier basis
exists for which the entire repeated low-frequency translation lattice of all
explicitly tracked pre-filter carriers and the complete inherited ladder is
strictly damped by the same common inheritance filter, except for the five
intended first outputs of the actual middle second target. No repeated
translated state collides with a clean-target or intended-purifier window.

The theorem is frozen by
`research/check_all_orders_raman_lattice.py`. The checker uses exact integer
arithmetic, exact polynomial arithmetic on the rational clean-root isolating
interval, Sturm/root-gcd statements for the trigger span, and an analytic
coercive cutoff. It does **not** use a finite-depth floating-point surrogate.

This closes the repeated-effective-Raman-clutter blocker left by
`2026-09-11-damping-compatible-raman-basis.md`. It does not yet prove that the
high-frequency Navier--Stokes system converges to this effective slow Raman
operator at the required order-one coupling, nor finite-energy localization of
the complete five-module history.

## 1. The all-orders-safe five-module basis

Use the actual ancestry-contaminated middle second target

    h=(z-2,-1,-1),                                        (1.1)

at the unique positive clean return root

    1.2847<z_*<1.2848.                                    (1.2)

For a low shift `l` and high direction `Q`, the silent high-pair construction
is the one from the state-triggered Raman packet:

    q=l/2+NQ,
    r=l/2-NQ,                                              (1.3)

with `l.Q=0` and transverse polarizations

    beta=l-|l|^2/(2N|Q|^2)Q+Q cross l,
    epsilon=l+|l|^2/(2N|Q|^2)Q-Q cross l.                (1.4)

The direct high-high source is exactly longitudinal and is killed by Leray.
The selected two-step slow output instead requires a slow trigger and has the
leading effective direction

    D_(l,Q)(k)
      =P_(k+l)[
          (l.(k+l))l
          -((Q cross l).(k+l))(Q cross l)].               (1.5)

The new basis is

    l_1=(-3,-3, 1),    Q_1=(1,-2,-3),
    l_2=(-3,-2, 2),    Q_2=(0, 1, 1),
    l_3=(-3,-2, 2),    Q_3=(2,-3, 0),
    l_4=(-2,-3, 2),    Q_4=(0, 2, 3),
    l_5=(-2,-3, 2),    Q_5=(1,-2,-2).                    (1.6)

Thus there are five different effective polarizations but only three distinct
frequency shifts,

    A=(-3,-3,1),
    B=(-3,-2,2),
    C=(-2,-3,2).                                          (1.7)

Every shift has strictly negative first component.

## 2. The five triggered strains still span the exact filter

Let `a_full(z)` be the complete leading middle-target coefficient from the
second-generation ancestry wall, with its common Fourier phase removed. For
module `j`, put

    kappa_j=h+l_j                                         (2.1)

and use the target-triggered leading direction (1.5), including its nonzero
scalar factor `a_full.Q_j`. The symmetric gradient tensor

    T_j=sym(D_j(h) tensor kappa_j)                         (2.2)

is trace free.

After clearing only manifestly nonzero common denominators, the determinant of
the five coordinates

    (T_11,T_22,T_12,T_13,T_23)                            (2.3)

is a degree-71 polynomial in `z`. Its gcd with the clean return polynomial is
exactly `1`. Therefore the five tensors form a basis of `Sym_0(3)` at every
clean return root and in particular at `z_*`.

Hence their amplitudes/phases can synthesize the exact stronger inheritance
filter

    H = [[ 71/100,   -1,       147/200],
         [ -1,      -143/200,   7/25  ],
         [147/200,    7/25,     1/200 ]]                  (2.4)

while the high pairs themselves remain Leray-silent at their own direct low
difference frequencies.

## 3. Repeated Raman translations collapse to a pointed three-generator semigroup

A second effective Raman interaction translates the preceding slow output by
another member of `(A,B,C)`, and so on. Independently of order, every frequency
reachable after the first translation has the form

    k+n_A A+n_B B+n_C C,

    n_A,n_B,n_C in N.                                    (3.1)

The actual interaction graph is smaller because a step disappears whenever
the incoming polarization is orthogonal to the next `Q_j`. For the theorem we
ignore that selection rule completely and test the **larger** semigroup (3.1).
Thus the certificate is conservative with respect to all exact zero couplings.

Since

    A_x=B_x=-3,
    C_x=-2,                                                (3.2)

every translation moves strictly toward negative `k_x`. There are no return
cycles or recurrent frequency classes.

## 4. A universal viscous cutoff makes the all-orders problem finite

The exact Frobenius norm is

    ||H||_F^2=21263/5000
             <(33/16)^2.                                  (4.1)

Therefore

    ||H||_op < 33/16.                                     (4.2)

For any transverse polarization `d`, the normalized Kelvin rate at the fixed
repository strength `M=2048` obeys

    R(k,d)
      =-2048 (d.H.d)/|d|^2-|k|^2
      <4224-|k|^2.                                        (4.3)

Hence every polarization at every frequency with

    |k|^2>=4224                                           (4.4)

is automatically damped.

Among the finite tracked seed families, the largest possible initial
`x`-component on the whole clean-root interval is

    1+z < 1428/625.                                       (4.5)

After 34 Raman translations, (3.2) gives

    k_x <= 1428/625-68=-41072/625,                        (4.6)

whose square already exceeds `4224`. Thus every path from every finite seed is
universally damped from depth 34 onward, without looking at its polarization.

For the inherited ladder

    r_n=(-n,-1,0),       n>=1,                            (4.7)

one translation gives `k_x<=-n-2`. Therefore every `n>=63` is already in the
universal region after its first Raman step.

So the infinite all-orders problem reduces rigorously to:

* finite seed paths through depth 33;
* inherited ladder indices `1<=n<=62` through depth 33.

Because only the three shifts `(A,B,C)` matter for frequency, this is a small
polynomial-size state set rather than an exponential ordered tree.

## 5. Exact damping certificate on every remaining state

Write

    H_200=200 H
      =[[142,-200,147],
        [-200,-143,56],
        [147,56,1]].                                      (5.1)

For a translated input `k` and one next module, let `d` be the denominator-free
Leray output vector

    W=(l.k')l-((Q cross l).k')(Q cross l),
    k'=k+l,

    d=|k'|^2 W-k'(k'.W).                                  (5.2)

Then `d.k'=0`. For `d!=0`, strict damping is equivalent exactly to

    25 |k'|^2 |d|^2
      +256 d^T H_200 d >0.                                (5.3)

There are no floating divisions in this certificate.

The checker exhausts every semigroup count triple before the coercive cutoff.
For the `z`-independent seeds

    p1,p2,g1,

and the ladder `1<=n<=62`, it proves (5.3) by pure integer arithmetic in

    81,406                                                  (5.4)

nontrivial sub-threshold cases.

The remaining six finite seed families have only one algebraic dependence:
their first coordinate is `c+/-z`, while the other two coordinates and every
shift are integral. Consequently (5.3) is an integer polynomial in `z` of
degree at most eight. On the exact rational interval

    12847/10000 <= z <= 12848/10000,                      (5.5)

the checker lower-bounds each polynomial coefficientwise with exact integer
arithmetic. It proves another

    20,747                                                  (5.6)

strictly positive certificates.

In total the finite core consists of exactly

    102,153                                                (5.7)

explicit exact damping certificates. The remaining infinitely many states are
covered by (4.3)--(4.7).

The actual middle target at zero previous translations is excluded from this
damping test: its five first outputs are the **intended** purifier components
which synthesize `H`. Every subsequent translation of those outputs is included
and is damped.

## 6. Required spectral windows are never revisited

The checker separately compares every repeated finite translated state through
the coercive cutoff against

* the three distinct intended purifier frequencies

      h+A, h+B, h+C,                                      (6.1)

  with duplicated modules sharing the corresponding window; and
* the three clean second-target windows

      h_+, h_0, h_-.                                      (6.2)

After excluding the intended first translation of `h_0`, it performs

    385,488                                                (6.3)

exact state/window comparisons. Every possible coordinate equality reduces to
an integer or linear polynomial in `z`; every nontrivial linear polynomial is
coprime to the clean return polynomial. No collision occurs at `z_*`.

For the inherited ladder, every translated frequency has rational/integer first
coordinate, while all required windows have first coordinate with nonzero
`+/-z` coefficient. A collision would force the monic integer clean return
polynomial to have a rational root in `(1.2847,1.2848)`, impossible by the
rational-root theorem.

Thus repeated Raman clutter does not feed back into either the clean target
windows or the three intended purifier windows.

## 7. All-orders effective theorem

**Theorem (inheritance-safe effective Raman purifier).** At the positive clean
return root, the five modules (1.6) have the following exact properties for the
leading high-frequency Raman slow dynamics:

1. every module is directly silent at its own high-high low difference
   frequency;
2. when triggered by the actual contaminated middle target, the five first
   outputs span `Sym_0(3)` and synthesize the exact common inheritance filter
   `H`;
3. every repeated Raman translation of every original parent,
   first-generation carrier, non-trigger second target, and every member of the
   complete inherited ladder is strictly `H`-damped at `M=2048`;
4. every repeated Raman translation of the intended first purifier outputs is
   also strictly damped after that first intended step; and
5. no repeated translated state reaches a clean-target or intended-purifier
   spectral window.

The proof is genuinely all-orders for the effective Raman lattice. No finite
word-depth hypothesis remains.

## 8. Recomputed frontier: full-NS high-mode elimination

The live blocker is no longer frequency-lattice pollution. It is now the
validity of the **effective Raman reduction at order-one cumulative coupling**.
The scaling from the first state-triggered packet is

    R=N/b -> infinity,
    rho=P/(nu N),
    rho^2/R = O(1),                                       (8.1)

with, for example,

    R=Re^theta,       rho=R^(1/2),       0<theta<1/2.     (8.2)

Thus the high-parent velocity/frequency ratio grows, and the repository's old
bounded-lifted-data Galilean theorem cannot simply be cited. The next theorem
must eliminate the high modes while retaining an order-one Raman operator on
the slow sector and prove that all discarded terms vanish. Concretely it must
control:

* repeated interactions involving three or more high parents;
* interactions between different Raman modules at frequencies `O(N)`;
* the exact time dependence and viscous decay of the preloaded high pairs over
  the clean birth/filter interval;
* feedback from the order-one slow Raman state into the high sidebands; and
* finite-energy packet/localization errors.

The natural next discriminator is a fixed-phase high-frequency normal-form or
Schur-complement calculation. If the `rho^2/R=O(1)` scaling leaves a nonvanishing
third-order high-mode feedback term, that term is the next precise obstruction.
If all higher terms gain an extra power of `R^-alpha`, the state-triggered
purifier becomes a genuine finite-energy module candidate.

No PLAN/canonical proof-graph promotion, recursive turnover, finite-time
singularity, or `NS-R3` conclusion is made here.
