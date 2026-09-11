# Exact 2D3C parent birth still cancels at the leading Raman scale

Date: 2026-09-11. Repository input:
`itpplasma/navier@0a17a98409de057f506fa56973ba04287eec5af7`.

**Status: exact leading-symbol obstruction and diversification checkpoint.** The
first genuinely dynamic repair of the Raman ordering wall uses the repository's
exact 2D3C invariant channel to generate the second near-opposite high parent
from zero. This really removes the initial simultaneous `q/r` symmetry. However,
when every cubic target-response tree is included, the complete `O(N)` slow
coefficient cancels exactly. The mechanism therefore does not restore the
leading state-triggered Raman scale that the preceding one-ordered packets
used.

The exact high-frequency Taylor algebra is frozen by
`research/check_raman_2d3c_parent_birth_wall.py`.

## 1. Exact parent-birth geometry

Let

    q=K e1+N e2,
    s=-2N e2,
    r=q+s=K e1-N e2.                                     (1.1)

Use scalar polarization

    a=e3                                                    (1.2)

for `q` and the 2D3C shear polarization

    b=e1/K                                                  (1.3)

for `s`. The exact 2D3C interaction satisfies

    C(q,a;s,b)=a,                                          (1.4)

so if `q` and `s` are preloaded but `r(0)=0`, then the missing Raman parent has
nonzero first derivative and is genuinely born dynamically. No forcing or
external reset is used in this model subsystem.

## 2. Full leading target Taylor coefficient

Let `(h,A)` be the slow target and write `A_y=A.e2`. The leading target-to-high
first sidebands are

    N^-1 C(h,A;q,a) -> +A_y a,
    N^-1 C(h,A;s,b) -> -2 A_y b.                          (2.1)

At second Taylor order, the target-plus-born-parent sideband receives all three
load-bearing contributions: `q` acting on the target-plus-shear sideband, `s`
acting on the target-plus-`q` sideband, and the newly generated `r` acting on
the target. Their exact leading sum is

    V_2(h+r)/N -> -A_y a.                                 (2.2)

The double-`q` sideband has

    V_2(h+2q)/N ->0.                                      (2.3)

The output of interest is

    kappa=h+q+r=h+2K e1.                                  (2.4)

At cubic order the complete leading coefficient has three possible sources:

    q + V_2(h+r),
    s + V_2(h+2q),
    r + V_1(h+q).                                         (2.5)

The middle term vanishes by (2.3). The other two are individually nonzero when
`A_y h_z!=0`, but the checker proves exactly

    T_q=-2 A_y h_z P_kappa e3,
    T_r=+2 A_y h_z P_kappa e3.                            (2.6)

Hence

    T_q+T_s+T_r=0.                                        (2.7)

This is a complete leading-tree cancellation, not a numerical observation.

## 3. Consequence for Raman

The Raman route has now returned to the same ordering obstruction after a real
mechanism change:

1. simultaneously preloaded near-opposite parents cancel between the two
   second-order time orderings;
2. passive heat/phase/polarization asymmetries cannot select one ordering; and
3. an exact autonomous 2D3C parent-birth channel still cancels after all cubic
   trees are summed.

A lower-order residual may remain, but exploiting it would require a new
strong-amplitude scaling and a new control theorem for the corresponding large
high-background propagator. That is no longer a repair of the existing Raman
shortcut; it recreates the autonomous-preparation hard core in a larger high
subsystem.

Under the repository diversification rule, the state-triggered Raman purifier
is therefore retired as the active terminal route. All exact negative controls
and scoped one-tree algebra are retained, but further Raman parameter searches
are not the next task.

## 4. Recomputed terminal frontier

The terminal mission remains open. Two genuinely different unresolved routes
remain available in the authoritative architecture:

* **positive continuation:** construct the input-only arbitrary-data critical
  producer feeding the reviewed `RF-q -> L^{3,q} -> continuation` consumer;
* **full-PDE exactification:** strengthen the finite viscous mixed-trace inverse
  to one common trace / endpoint-uniform nonlinear correction, without assuming
  a prescribed singular trial history.

The next research-game round should switch to one of these terminal mechanisms,
starting from its first uncontrolled term rather than inventing another
purifier functional. The positive route is the cleaner discriminator because
its consumer is already closed and its missing estimate has a precise universal
quantifier.

No terminal regularity theorem, finite-time singular solution, regenerative
turnover, or `NS-R3` resolution is claimed.
