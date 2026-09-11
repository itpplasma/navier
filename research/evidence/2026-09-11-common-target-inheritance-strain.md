# One common strain separates clean second targets from all explicit inherited carrier classes

Date: 2026-09-11. This packet strengthens the common second-target discriminator by adding the inherited carrier classes generated before the nominal second gate.

**Status: exact author carrier theorem; independent audit and novelty undetermined.** It is an instantaneous affine/Kelvin separation theorem. It does not produce the strain autonomously at the correct time, preserve exact carrier geometry for a finite pulse, or close the recursive turnover.

## 1. A stronger rational trace-free strain

Let `z_*` denote the unique positive clean-circuit root in

    1.2847 < z_* < 1.2848.

Set

    H = [[ 71/100,   -1,      147/200],
         [ -1,      -143/200,  7/25  ],
         [147/200,   7/25,     1/200 ]].                 (1.1)

Then `H` is real, symmetric and trace free.

For a transverse carrier `(k,a)`, define the normalized strain form

    q_H(a)=a^T H a/|a|^2.                                (1.2)

The three nominal clean second-generation target frequencies are

    h_+=(0,1,1),
    h_0=(-2,-1,-1),
    h_-=(0,-1,1),                                        (1.3)

with their physical wavevectors and intended selected polarizations `v_j` as frozen in the preceding second-target packets. Let

    f_j=k_j cross v_j                                    (1.4)

be the transverse rejected direction.

Exact polynomial sign checks on the entire isolating interval give

    q_H(v_j)<0,       q_H(f_j)>0                          (1.5)

for all three targets.

The same matrix also has the opposite sign on every explicit inherited carrier class encountered before those second targets:

    q_H(a_p)>0                                            (1.6)

for each original parent

    p1: (k1,a1),   p2: (k2,a2),   p3: (k3,a3),            (1.7)

and

    q_H(a_g)>0                                            (1.8)

for each first-generation selected carrier

    g1=-k1-k2,   g2=k1-k3,   g3=k1+k3.                   (1.9)

At `z_*`, representative normalized values are approximately

    second desired:  (-1.0635, -0.2835, -0.00316),
    second rejected: ( 0.5971,  0.3496,  1.2512),
    original parents:( 0.00479, 0.9835, 0.9835),
    first carriers:  ( 0.00500, 0.00378, 0.00350).        (1.10)

The small margins in the last line and on `h_-` are genuine; they explain why a relatively strong strain is required to dominate viscosity uniformly.

## 2. Viscosity-retaining separation at one explicit strength

Use the affine background

    U(x)=M nu b^2 H x,                                   (2.1)

where `b` is the common physical carrier scale. The instantaneous logarithmic amplitude-energy rate, divided by `nu b^2`, is

    R_M(k,a)=-M q_H(a)-|k|^2.                            (2.2)

At the explicit rational strength

    M=2048,                                               (2.3)

exact sign checks on the whole root interval prove

    R_M(k_j,v_j)>0,                                      (2.4)

    R_M(k_j,f_j)<0                                       (2.5)

for all three second targets, while

    R_M(p_i)<0,       R_M(g_i)<0                         (2.6)

for all three original parents and all three first-generation selected carriers.

The weakest desired margin is the `h_-` target; it remains strictly positive at `M=2048`. Numerically at `z_*`, its normalized rate is about `+2.9`, while all six parent/first-generation rates are negative.

## 3. The full inherited-parent ladder is also damped

The all-orders inheritance packet proved that

    r_n=-n k1-k2=(-n,-1,0),       n>=1,                  (3.1)

has polarization `e3`. Since

    e3^T H e3=1/200,                                     (3.2)

its exact normalized rate at `M=2048` is

    R_M(r_n,e3)
      = -2048/200-(n^2+1)
      = -256/25-n^2-1 <0.                                (3.3)

Thus every member of the explicit infinite inherited-parent ladder is damped, including `n=1`.

This is a substantially stronger compatibility statement than the earlier instantaneous filter: after the second-generation desired targets have been created, one common strain can favor all three intended target polarizations while suppressing all explicitly tracked older carrier generations and the complete ladder responsible for the clean-gate Taylor-tree wall.

## 4. What this changes

The inherited-parent obstruction is no longer a sign incompatibility. The live architecture may now be formulated as

    clean first birth
      -> full ancestry creates second-target modes
      -> turn on common inheritance filter H
      -> desired second-target components survive/grow
      -> old parents, first carriers, rejected polarizations and ladder decay
      -> continue from the filtered target triple.        (4.1)

This is important because it avoids both a three-station purifier and a separate filter for the old parents.

However the phrase **turn on** in (4.1) is now the central unresolved operation. If the strong strain (2.1) is present throughout the first and second births, it alters the carrier wavevectors and the nonlinear Taylor tree on the same timescale; the clean circuit calculation cannot simply be superposed on it. Conversely, independently prescribing `H` only after target birth would reset the solution and is forbidden.

A successful unforced construction must therefore generate the strain autonomously near the filtering time, or spatially stage a pre-existing strain region so the target packet enters it only after birth.

## 5. Strength and clock warning

A fixed dimensionless strength `M=2048` proves carrier-sign feasibility, but a recursive supercritical turnover has increasing local Reynolds number

    Re=A ell/nu,                                          (5.1)

with stage ratio `g/s>1`. The natural nonlinear gate clock is

    tau_adv=ell/A,                                        (5.2)

whereas an `M=O(1)` viscous-strength strain acts on

    tau_strain ~ ell^2/(M nu).                            (5.3)

Their ratio is

    tau_strain/tau_adv ~ Re/M.                            (5.4)

Hence a fixed `M` eventually becomes slow compared with the nonlinear gate. Finite summability of the parabolic clocks is not enough for stagewise control.

To filter on the advective clock at large `Re`, the strain strength must scale as

    M_n >= C Re_n,                                        (5.5)

or equivalently

    |grad U| ~ A/ell.                                     (5.6)

This scaling is not energetically absurd: a localized strain cell of radius `ell`, gradient `A/ell`, and velocity scale `A` has kinetic energy of order

    A^2 ell^3,                                            (5.7)

exactly the same scaling as the turnover cell. Under the admissible energy window `g^2<=s^3`, this stage energy does not grow geometrically.

Thus the new filter is compatible with the turnover's energy scaling, but its autonomous generation and finite-time geometry control are load-bearing.

## 6. Reproducibility

`research/check_common_target_inheritance_strain.py` freezes the matrix (1.1), reconstructs all three intended/rejected second-target directions, the original parents and first selected carriers, and verifies all signs in (1.5)--(2.6) by exact rational polynomial root counting on the isolated clean-root interval. It also proves the exact all-`n` ladder rate (3.3).

No finite-time strain switch, dynamically generated strain packet, next clean gate, recursive turnover, or NS-R3 resolution is claimed.
