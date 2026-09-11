# Reality-complete Raman kick followed by viscous wait is a full-carrier relative purifier

Date: 2026-09-11. Repository input:
`itpplasma/navier@44e4355ec57de70aa4bede6b2f291734ec0e9f22`.

**Status: author theorem for the reality-complete leading Raman slow model, plus
an explicit full-PDE scale-compatibility ledger.** The continuous Raman-plus-
slow-viscosity Schur theorem is not the direct lift of one freely decaying high
Beltrami sphere because its high clock is too short. The correct split is:

    short conservative Raman kick
      -> high Beltrami sphere decays
      -> ordinary viscous wait
      -> next clean nonlinear stage.                       (0.1)

For a sufficiently small fixed kick action and sufficiently large translation
spacing, this map preserves a larger fraction of all three desired selected
second targets than of every tracked rejected/inherited carrier, including the
complete inherited ladder. The effect is fixed and nonzero; the kick action is
not sent to zero in the physical scale limit.

The exact geometry and exponent ledger are frozen by
`research/check_raman_kick_wait.py`. The common-line and reality identities
used below are frozen by the preceding Raman checkers.

This is still an effective slow-model theorem. Deriving the kick from one
finite-energy exact Navier--Stokes Cauchy history, with quantified normal-form
error, remains the first full-PDE blocker.

## 1. Why the continuous Schur lift is not the physical clock

Let `R=Lambda/b` be the high/clean scale ratio and `J` the exported slow
sideband scale. The Beltrami Raman expansion requires

    J/R ->0.                                               (1.1)

A freely heat-decaying common-sphere high background lives on

    t_H=O(R^-2)                                            (1.2)

in clean viscous time units, while an exported sideband at wave number `O(J)`
needs

    t_J=O(J^-2)                                            (1.3)

to experience order-one ordinary viscosity. Therefore

    t_H/t_J=O((J/R)^2)->0.                                 (1.4)

So the high sphere cannot directly sustain the continuous generator
`-D_J+S_J` long enough for the Schur damping in the preceding packet to act.
This does not invalidate that operator theorem; it rules out that particular
one-pulse physical interpretation.

During the high clock the `J`-scale viscosity is asymptotically negligible.
The correct leading action is therefore the **skew Raman transport alone**.
After the high sphere has decayed, the exported slow sidebands remain and may
be removed by an ordinary viscous wait.

## 2. Fixed-strength reality-complete kick

Keep

    Q_A=(-1,-5,-6),
    Q_B=(10,-3,-1),
    ell=Q_A cross Q_B=(-13,-61,53).                       (2.1)

Use reality-paired slow shifts

    +/- J ell,
    +/- 2J ell,                                            (2.2)

with kick coefficients of squared magnitudes

    w_A=30,
    w_B=10.                                                (2.3)

Let `q_i=Q_i/|Q_i|`. The leading Raman operator `S_J` is the same skew
translation operator as in the common-line packet, now without the `J`-growing
strength factor. Thus

    S_J^*=-S_J                                             (2.4)

exactly, and

    exp(theta S_J)                                        (2.5)

is unitary for every real kick action `theta`.

Because `q_i.ell=0`, the scalar factors `q_i.k_n` are constant along each
translated lattice. For each fixed finite Bloch carrier `k`, `S_J` is therefore
bounded on the whole lattice by a constant independent of `J`. This makes the
small-`theta` expansion uniform as `J->infinity`.

## 3. Exact center-loss curvature

Start with one center-supported transverse carrier `a`. Since the Raman shifts
are nonzero,

    P_0 S_J P_0=0.                                        (3.1)

Let

    E_0(theta)=||P_0 exp(theta S_J)a||^2/|a|^2.            (3.2)

Skew-adjointness gives

    E_0(0)=1,
    E_0'(0)=0,
    E_0''(0)=-2 ||S_J a||^2/|a|^2.                       (3.3)

Hence

    E_0(theta)
      =1-A_J(k,a) theta^2+O(theta^3),                     (3.4)

where

    A_J=||S_Ja||^2/|a|^2.                                 (3.5)

The exact checker evaluates the four first sideband norms and proves

    A_J(k,a) -> 8 C(k,a)                                  (3.6)

as `J->infinity`, where

    C(k,a)
      =30 (a.Q_A)^2(k.Q_A)^2/(|a|^2|Q_A|^4)
       +10 (a.Q_B)^2(k.Q_B)^2/(|a|^2|Q_B|^4).             (3.7)

The factor eight is the product of the `-2` Raman coefficient squared and the
two reality-reflected sidebands for each axis.

The previously proved exact inequalities are

    desired selected targets: C<1/4,                     (3.8)

while

    rejected targets, p1--p3, g1--g3, r1,r2,r3: C>1.     (3.9)

Therefore the limiting center-loss curvatures satisfy

    desired:  A<2,
    finite unwanted: A>8.                                 (3.10)

The separation is strict on the entire clean-root interval, so one common
large `J` preserves a fixed margin for all finite carriers in (3.8)--(3.9).

## 4. Viscous wait and the second-order purifier gap

After the Raman kick, let the high Beltrami background decay away and evolve
the slow field by ordinary viscosity for

    tau_w=theta^2/2.                                      (4.1)

For the center component, the energy multiplier is

    exp(-2|k|^2 tau_w)
      =1-|k|^2 theta^2+O(theta^4).                        (4.2)

Combining (3.4) and (4.2), the center energy after kick and wait is

    1-[A_J(k,a)+|k|^2] theta^2+O(theta^3).                (4.3)

For desired selected targets, exact bounds give

    8 C+|k|^2 <6.                                         (4.4)

For every finite unwanted carrier in (3.9),

    8 C+|k|^2 >9.                                         (4.5)

Thus there is a strict second-order separation by more than three units.
Uniform boundedness of `S_J` on the finite carrier set gives one fixed

    theta_*>0                                             (4.6)

and then one sufficiently large `J` such that for every
`0<theta<=theta_*` the complete kick--wait map preserves a strictly larger
energy fraction of each desired selected target than of every finite unwanted
class in (3.9).

Unlike the preceding asymptotic exploratory scaling, `theta` need not tend to
zero with the physical high scale. Choose any one sufficiently small positive
`theta` and keep it fixed. The relative purification per stage is then fixed
and nonzero.

## 5. Exported sidebands vanish during the wait

For every finite carrier in the checked set and every `n!=0`, the common-line
bound gives

    |k+nJ ell|^2>6437 J^2 n^2.                            (5.1)

Consequently every noncenter component left by the kick gains during (4.1) an
energy factor at most

    exp(-6437 J^2 n^2 theta^2).                           (5.2)

For fixed `theta>0`, this tends to zero superalgebraically in every fixed
translated sector as `J->infinity`, and the quadratic lattice growth plus
unitarity controls the full tail. Thus the post-wait field is asymptotically
its center projection; the exported energy has been genuinely dissipated, not
merely hidden in a conservative sideband.

The high sphere itself is already gone much earlier because `R/J->infinity`:
its heat clock is `R^-2`, whereas the wait is fixed positive in clean viscous
units.

## 6. Complete inherited ladder

For the first three inherited carriers `r1,r2,r3`, the exact finite curvature
certificate (3.9) applies.

For

    r_n=(-n,-1,0),   n>=4,                                (6.1)

no kick expansion is needed. Translation by any multiple of `ell` preserves
`r_n cross ell`, and the common-line geometry gives

    min_s |r_n+s ell|^2>n^2/2.                            (6.2)

The Raman kick is unitary, so it cannot increase total energy. During the wait
(4.1), every frequency in the entire translated lattice therefore obeys

    E_after/E_before <= exp(-n^2 theta^2/2).              (6.3)

At `n=4` the second-order coefficient is already eight, and it grows
quadratically thereafter. Desired selected targets have coefficient less than
six by (4.4). After shrinking `theta_*` if needed, every `n>=4` is therefore
uniformly more damped than every desired target. This closes the entire
inherited ladder without an order-of-limits problem between `n` and `J`.

## 7. Compatible full-PDE scaling

The kick construction returns to the standard order-one Raman regime rather
than the `J`-growing continuous-Schur strength. Fix the small positive kick
parameter `theta`. Use a large parameter `sigma` and take

    J=sigma^2,
    R=sigma^6,
    rho=sqrt(theta R)=sqrt(theta) sigma^3,
    Re=sigma^13,
    epsilon=delta/b=sigma^-2.                             (7.1)

Then

    J/R=sigma^-4 ->0,                                     (7.2)

so the growing slow shifts remain asymptotically small compared with the high
Beltrami radius, while

    rho^2/R=theta                                         (7.3)

keeps the integrated Raman kick fixed.

The old clean/high compatibility ledgers improve:

    R^2/Re=sigma^-1 ->0,                                  (7.4)

    P/A=R rho/Re=sqrt(theta) sigma^-4 ->0.                (7.5)

For a thin positive-helicity shell of relative clean width `epsilon`, the raw
shell defect after the worst first-star `sqrt(R)` balancing loss scales as

    (rho epsilon/R) sqrt(R)
      =sqrt(theta) sigma^-2 ->0.                           (7.6)

Also

    t_H/t_J=(J/R)^2=sigma^-8 ->0,                         (7.7)

exactly the kick--wait clock separation used above.

Thus the new purifier is compatible simultaneously with high/slow scale
separation, a fixed nonzero Raman action, small high-parent velocity relative
to the clean stage, the existing thin-shell localization ledger, and a wait
long enough to dissipate the exported slow sidebands.

## 8. Exact common-sphere realization still required

For module `i`, let the slow shift be

    L_i=m_i J ell,      m_A=1, m_B=2.                     (8.1)

To put both modules on one exact Beltrami sphere of radius `Lambda`, choose
unit fast axes `q_i` and radial components

    N_i=sqrt(Lambda^2-|L_i|^2/4).                         (8.2)

Then

    p_i=N_i q_i+L_i/2,
    r_i=-N_i q_i+L_i/2                                    (8.3)

have exactly

    |p_i|=|r_i|=Lambda.                                   (8.4)

Since `J/R->0`, `N_i/Lambda->1`. Positive-helicity polarizations place all
parents and their reality reflections in the same curl eigenspace, so their
complete high--high projected nonlinearity vanishes exactly for arbitrary
module amplitudes.

The next checkpoint must freeze this growing-shift common-sphere geometry and
then prove that the **full high--slow normal form over one high heat pulse**
converges to the unitary kick `exp(theta S_J)` uniformly in the simultaneous
limit (7.1). That is now the first unresolved mathematical term.

No PLAN/canonical proof-graph promotion, recursive turnover, finite-time
singularity, or `NS-R3` conclusion is claimed here.
