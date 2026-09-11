# Reality sideband defeats the proved small-time sequential two-shear purifier

Date: 2026-09-11. Repository input:
`itpplasma/navier@cdb20518ede358e15d2ab69fa0759323c342d4e5`.

**Status: exact scoped obstruction to the previously proved small-duration
two-shear consumer.** The repository's sequential two-rank-one theorem remains
correct for the carrier set it tested. Once the reality-generated Raman
sideband from the new bidirectional lattice is added, however, its exact first
variation has the wrong sign. Therefore that theorem cannot be used unchanged
to repair the reality wall.

The exact sign is frozen by
`research/check_real_raman_sequential_small_time_wall.py`.

## 1. The new carrier

The reality-complete single-axis Raman lattice contains the depth-two path

    h0 -> h0+l5 -> h0+l5-l4,                              (1.1)

where

    l5=(0,1,-7),
    l4=(0,-1,-7).                                         (1.2)

Thus the net transverse offset is `(0,2,0)`, giving

    k_c=(z-2,1,-1).                                       (1.3)

The active one-axis Raman polarization is `P_(k_c)e1`; use the
denominator-free representative

    v_c=(2,-(z-2),z-2).                                   (1.4)

## 2. The old common filter amplifies it

For the repository inheritance matrix `H` and strength `M=2048`, the normalized
Kelvin rate is

    R_H(k,v)=-2048 (v^T H v)/|v|^2-|k|^2.                (2.1)

At (1.3)--(1.4), exact simplification gives

    (v_c^T H v_c)/|v_c|^2
      =-(127 z^2-1202 z+1612)
         /[200(z^2-4z+6)],                                (2.2)

and

    R_H(k_c,v_c)
      =-(25 z^4-200 z^3-31812 z^2+306512 z-411772)
         /[25(z^2-4z+6)].                                 (2.3)

Exact root counting proves that the numerator and denominator in (2.3) have no
zero on the clean interval

    12847/10000 <= z <= 803/625,                          (2.4)

and their signs give

    R_H(k_c,v_c)>0                                        (2.5)

throughout that interval. At the actual clean root the value is approximately
`+1128.4`.

So the old common filter strongly **grows**, rather than damps, this one
reality-generated clutter mode.

## 3. Consequence for the exact two-shear theorem

The earlier sequential theorem applies the two rank-one gradients whose
symmetric first variation sums to `H`. It proves for every fixed input carrier

    d/dtau log E_seq(tau;k,v)|_(tau=0)=2 R_H(k,v).        (3.1)

Combining (2.5) with (3.1) yields

    E_seq(tau;k_c,v_c)>1                                  (3.2)

for every sufficiently small positive `tau`.

Hence the small-duration two-shear purifier cannot simultaneously retain its
old target signs and suppress the reality-complete Raman clutter. This is an
exact consequence of the already-proved first-variation identity, not a
numerical finite-time inference.

## 4. Frozen multistage schedules do not help

There is also a general algebraic negative control. If carrier geometry is
frozen and strains `S_j` act for durations `t_j`, linearity of the quadratic
form gives

    sum_j t_j[-q_(S_j)(v)-|k|^2]
      =-q_(sum_j t_j S_j)(v)-(sum_j t_j)|k|^2.            (4.1)

Thus any number of commuting/frozen-carrier stages is equivalent to one
duration-weighted average strain. The exact Farkas obstruction therefore
applies unchanged.

A sequential repair can only evade the wall through a genuinely noncommuting
effect: finite wavevector/polarization transport, Raman mixing, spatial staging,
or a changed consumer in which all six conflicting signs are not demanded in
the same state history.

A finite-duration numerical scan of the repository's two fixed rank-one pulses
was used only as a discriminator and found no positive sign window after adding
the new sideband; this is heuristic evidence and is **not** promoted as an
impossibility theorem.

## 5. Diversification decision

The route has now returned seriously to the same sign obstruction twice:

1. every simultaneous trace-free common strain is excluded by the exact Farkas
   certificate;
2. the existing sequential small-time consumer inherits the same bad first
   variation, while frozen multistage alternation reduces to the same average.

According to the repository diversification rule, further optimization of the
same common/two-shear filter is not the next task.

The next attack should change the consumer or representation. A promising
alternative is to exploit the exact `L2`-skew reality-paired Raman transport as
a conservative mixer and seek **hypocoercive spectral export**: move unwanted
slow components to larger wave number where viscosity removes them, while a
protected target subspace remains dark or only weakly coupled. This replaces
simultaneous sign separation by transport-plus-dissipation and is not covered by
the Farkas wall.

No PLAN/canonical proof-graph promotion, recursive turnover, finite-time
singularity, or `NS-R3` conclusion is claimed here.
