# State-triggered Raman synthesis of the common inheritance filter

Date: 2026-09-11. Repository input:
`itpplasma/navier@286ce4495d94913615844e00c22322734f8bdc2e`.

**Status: exact high-frequency Fourier-symbol theorem for the actual
ancestry-contaminated middle second target.** Five explicit preloaded
near-opposite high-pair modules have exactly zero direct low quadratic output,
yet their two-step action on the newborn target spans the full five-dimensional
space of trace-free symmetric strains. Hence their target-triggered outputs can
synthesize the repository's exact common inheritance filter `H`.

This is a genuine timing-mechanism change. The purifier modes are no longer
created by an independent preloaded high-high source that must be delayed by a
viscous clock. Their selected low output requires a slow input at the clean
target frequency. The theorem is not yet a time-integrated Navier--Stokes stage:
the effective transfer loses one power of the high/low scale ratio, and the same
high modules translate every other slow carrier to off-target low frequencies.
Those are now the live PDE/scaling questions.

The exact algebra is frozen by
`research/check_state_triggered_raman_span.py`.

## 1. The actual trigger, not the ideal selected polarization

Use the nominal middle second target

    h_lattice=(-2,-1,-1).                                 (1.1)

At the clean projective-return parameter `z`, its physical wavevector is

    h=(z-2,-1,-1).                                        (1.2)

Let `a_full(z)` be the complete leading `t^3` coefficient at this target,
including the pure selected child-child tree and all old-parent/second-jet
trees frozen in
`research/check_clean_gate_second_generation_wall.py`. Remove only its common
`-i` Fourier phase. Then

    h.a_full=0                                             (1.3)

exactly. No projection onto the intended component is made in this note: the
trigger is the actual ancestry-contaminated coefficient.

The clean return root remains isolated by

    1.2847 < z_* < 1.2848.                                (1.4)

## 2. One exactly silent high pair

Choose two fixed nonzero low vectors `l,Q` with

    l.Q=0.                                                 (2.1)

Put

    m=Q cross l.                                          (2.2)

For a large scalar `N`, define equal-length near-opposite high wavevectors

    q=l/2+N Q,
    r=l/2-N Q,                                             (2.3)

so

    q+r=l,
    |q|=|r|.                                               (2.4)

Choose high polarizations

    beta_N
      = l - |l|^2/(2N|Q|^2) Q + m,

    epsilon_N
      = l + |l|^2/(2N|Q|^2) Q - m.                       (2.5)

They are exactly transverse:

    q.beta_N=0,
    r.epsilon_N=0.                                        (2.6)

For the Leray interaction

    C(p,a;q,b)
      =P_(p+q)[(a.q)b+(b.p)a],                            (2.7)

the direct high-high output is at frequency `l`. Its unprojected vector is

    (beta_N.r) epsilon_N + (epsilon_N.q) beta_N
      = |l|^2 (epsilon_N+beta_N)
      = 2 |l|^2 l.                                        (2.8)

This is exactly longitudinal. Therefore

    C(q,beta_N;r,epsilon_N)=0                             (2.9)

for every `N`, not merely asymptotically.

Thus this preloaded pair cannot create its own selected low velocity mode. Its
quadratic low difference-frequency output is pure pressure.

## 3. A newborn slow target unlocks a two-step low transfer

Let

    p=h+q,
    kappa=h+l.                                             (3.1)

Once the target coefficient `(h,a_full)` is present, consider

    c_N=C(h,a_full;q,beta_N),                              (3.2)

followed by

    d_N=C(p,c_N;r,epsilon_N).                              (3.3)

The final wavevector is exactly

    p+r=h+q+r=kappa.                                      (3.4)

Although the direct high pair is Leray-silent, this target-assisted chain is
generically nonzero. It has one high/low cancellation rather than two generic
powers of `N`. Writing

    beta_0=l+m,
    epsilon_0=l-m,                                        (3.5)

one obtains the exact high-frequency limit

    N^(-1)d_N -> d_infty,                                 (3.6)

where

    d_infty
      =(a_full.Q)
        P_kappa[
          (beta_0.kappa) epsilon_0
          +(epsilon_0.kappa) beta_0]

      =2(a_full.Q)
        P_kappa[
          (l.kappa)l-(m.kappa)m].                         (3.7)

In particular

    kappa.d_infty=0.                                      (3.8)

The selected slow output is therefore divergence free and is **linear in the
actual newborn target coefficient**. At the selected frequency `kappa`, no
other slow input `k!=h` can substitute for the trigger through this same
frequency translation: it would land at `k+l`, not `h+l`.

## 4. Five explicit modules span every trace-free symmetric strain

Use the following five integer pairs `(l,Q)`:

    l_1=( 1, 0,-1),   Q_1=(1,-1, 1),
    l_2=( 1,-1, 0),   Q_2=(1, 1,-1),
    l_3=( 0, 1,-1),   Q_3=(1,-1,-1),
    l_4=( 1, 1, 0),   Q_4=(1,-1, 1),
    l_5=( 0, 1, 1),   Q_5=(1,-1, 1).                     (4.1)

Every dot product `l_j.Q_j` is zero. For each module set

    kappa_j=h+l_j                                         (4.2)

and compute `d_(j,infty)` from (3.7). The associated symmetric gradient tensor
is

    T_j=sym(d_(j,infty) tensor kappa_j).                  (4.3)

Because `d_j.kappa_j=0`, every `T_j` is trace free.

Encode a trace-free symmetric `3 x 3` matrix by the five coordinates

    (T_11,T_22,T_12,T_13,T_23).                           (4.4)

After clearing only manifestly nonzero rational denominators from
`a_full(z)` and the individual Leray projections, let `M(z)` be the `5 x 5`
matrix whose columns are the five tensors (4.3). The checker obtains an exact
polynomial determinant of degree `71`. Sturm root counting gives

    det M(z) != 0

for every

    1.2847 <= z <= 1.2848.                                (4.5)

Hence, at the unique clean root `z_*`, the five target-triggered effective
strains form a basis of

    Sym_0(3),                                              (4.6)

the complete five-dimensional space of real symmetric trace-free matrices.

In particular the stronger common inheritance filter

    H = [[ 71/100,   -1,       147/200],
         [ -1,      -143/200,   7/25  ],
         [147/200,    7/25,     1/200 ]]                  (4.7)

has a unique linear combination

    H=sum_(j=1)^5 alpha_j T_j.                             (4.8)

The scalar coefficients can be implemented by the phases and amplitudes of the
five high modules. This is an exact span statement, not a numerical rank test.

## 5. Why this evades the activation-time wall algebraically

The perturbative long-tail switch failed because an independent low purifier
was forced to choose between

    accurate high-frequency construction

and

    remaining dormant until the clean target was born.    (5.1)

Here the selected purifier frequency `kappa_j` has no direct quadratic source
from its own high pair by (2.9). Its leading designed source contains the
actual target coefficient `a_full` by (3.2)--(3.7). Therefore the desired low
filter component is absent from this module before the corresponding target
frequency exists.

This does not mean the high modules are dynamically invisible before target
birth. They can interact with other slow carriers and create **different** low
translations. The point is narrower and exact: the timing of the selected
purifier output is now tied to the state rather than to waiting for a
preloaded high-high low tail to turn on.

## 6. Scale ledger: one Raman loss

The high-frequency limit (3.6) shows one power of scale-separation loss. Let

    R=N/b >>1                                             (6.1)

be the high/clean wave-number ratio, and let one high-parent velocity amplitude
have dimensionless velocity/frequency ratio

    rho=P/(nu N).                                         (6.2)

Over one fast viscous interval `O((nu N^2)^-1)`, the two-step slow translation
has the schematic relative size

    output/trigger = O(rho^2/R).                          (6.3)

This is the same one-power fast/slow cancellation exposed by the repository's
Leray-return and lifted-Galilean packets. Consequently an order-one triggered
filter requires

    rho^2 comparable to R.                                (6.4)

Unlike the independent strong purifier, this need not force high-parent
velocities to match the clean-stage velocity. At clean Reynolds number

    Re=A/(nu b),                                          (6.5)

target birth occurs on the advective clock `(A b)^-1`. To keep the high pair
alive through that clock it is enough to take

    R^2 <= C Re.                                          (6.6)

For example `R=Re^theta`, `0<theta<1/2`, and

    rho=R^(1/2)                                           (6.7)

give an order-one Raman coefficient while

    P/A = R^(3/2)/Re ->0                                  (6.8)

for every such `theta`. Thus there is no immediate amplitude or energy
contradiction analogous to the two preceding purifier walls.

The price is that the high-pair ratio `rho` is not uniformly bounded. A new
all-orders estimate is required; the old bounded-lifted-data theorem cannot be
quoted unchanged.

## 7. Recomputed frontier: off-target Raman clutter

A module with low shift `l_j` acts at leading two-step order on **every** slow
carrier `(k,a)`, sending it to `k+l_j`. The desired purifier frequency
`h+l_j` is target-specific, but the original parents, first-generation modes,
other second targets and the inherited ladder can generate additional low
sidebands of comparable Raman strength.

This is now the first discriminating obstruction. The next calculation must:

1. enumerate `k+l_j` for every explicitly tracked pre-target carrier and all
   five shifts;
2. identify exact frequency collisions with the five purifier outputs and with
   the next clean-gate input windows;
3. compute the effective polarizations using the analogue of (3.7);
4. test their instantaneous rates under the synthesized `H` and viscosity;
5. then address the infinite inherited ladder and cross-module high-frequency
   interactions.

If the off-target low translations collide with required windows or contain an
undamped recurrent family, this state-triggered route fails cleanly. If they
are spectrally disjoint and damped, the next task is an all-orders lifted-phase
realization with `rho^2/R=O(1)`.

No PLAN, canonical proof graph, manuscript, formal proof, regenerative turnover,
finite-time singularity, or `NS-R3` result is claimed here.
