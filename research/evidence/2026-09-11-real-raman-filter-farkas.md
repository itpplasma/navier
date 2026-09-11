# Farkas obstruction to one common reality-complete Raman filter

Date: 2026-09-11. Repository input:
`itpplasma/navier@36c5a9f83da1e95c028f32cfe2593bf93fb990da`.

**Status: exact algebraic obstruction for the current common-affine-filter
consumer.** Once Fourier reality is included, the single-axis Beltrami Raman
background generates a bidirectional slow lattice. One depth-two sideband of
the actual `h0` target is enough to make the original common-strain consumer
infeasible: at the clean algebraic return root there is no real symmetric
trace-free strain, at any strength, which simultaneously grows the required
`h_-` selected carrier and damps `p1`, `g2`, `g3`, the first inherited-ladder
carrier, and that reality-generated sideband, with viscosity retained.

The exact Farkas certificate is frozen by
`research/check_real_raman_filter_farkas.py`.

This does not refute state-triggered Raman purification or the common-Beltrami
high background. It refutes the attempted repair in which one keeps the same
single common affine/Kelvin filter objective and asks it to damp the complete
reality-generated slow clutter.

## 1. Six load-bearing rate requirements

Absorb the strain strength into a trace-free symmetric matrix `S`. For a
transverse carrier `(k,v)` define

    q_S(v)=v^T S v/|v|^2,
    R_S(k,v)=-q_S(v)-|k|^2.                               (1.1)

The clean construction requires the selected `h_-` target to grow:

    R_S(h_-,v_-) >= 0.                                    (1.2)

The common inheritance consumer also requires suppression of old material. It
is enough for the obstruction to retain only

    R_S(p1)<=0,
    R_S(g2)<=0,
    R_S(g3)<=0,
    R_S(r1,e3)<=0.                                        (1.3)

The reality-complete single-axis Raman lattice contributes one additional
necessary damping condition. The two shifts

    l5=(0,1,-7),
    -l4=(0,1,7)                                           (1.4)

sum to `(0,2,0)`, so from

    h0=(z-2,-1,-1)                                        (1.5)

one reaches at depth two

    k_c=(z-2,1,-1).                                       (1.6)

Every translated active single-axis Raman polarization is `P_k e1`; a
denominator-free representative at (1.6) is

    v_c=(2,-(z-2),z-2).                                   (1.7)

A common filter that suppresses its own reality-generated clutter would need

    R_S(k_c,v_c)<=0.                                      (1.8)

These six non-strict requirements are already inconsistent. Therefore adding
strict margins, the other old carriers, or more of the bidirectional lattice
cannot repair them.

## 2. Exact algebraic Farkas certificate

Write a trace-free symmetric `S` in the five coordinates

    (S11,S22,S12,S13,S23),    S33=-S11-S22.               (2.1)

Each condition (1.2)--(1.3),(1.8) is a linear inequality

    a_j(z).s <= b_j(z),       j=1,...,6.                  (2.2)

All coefficients are rational functions of the clean parameter `z`. Work
exactly in the number field represented by

    Q[z]/(Q_clean),                                           (2.3)

where

    Q_clean=z^10-z^9+4z^8+2z^6-2z^5-8z^3-32z^2+40z-16.  (2.4)

The checker forms the `5 x 6` normal matrix exactly, takes its cofactor null
vector `mu`, and reduces every arithmetic operation modulo `Q_clean`. It proves

    sum_j mu_j a_j = 0                                    (2.5)

exactly in the quotient field.

For every one of the six multipliers, exact root counting on

    12847/10000 <= z <= 803/625                           (2.6)

shows

    mu_j(z)>0.                                             (2.7)

The same exact root-count/sign test gives

    F(z):=sum_j mu_j b_j <0                               (2.8)

throughout the interval containing the unique positive clean root `z_*`.

At `z_*`, multiplying (2.2) by the positive `mu_j` and summing would therefore
give

    0 <= F(z_*) <0,                                       (2.9)

which is impossible.

This is a genuine Farkas certificate, not a floating linear-program result.
The numerical LP was used only to discover the six-constraint core; the
committed checker reconstructs and proves the certificate from exact algebra.

## 3. Consequence

The failure is not specific to the previously selected rational matrix

    H=[[71/100,-1,147/200], ...].                          (3.1)

Nor can it be repaired by increasing its strength or choosing a different
trace-free matrix. Requirement (2.9) excludes **every** common symmetric
trace-free affine strain compatible with these six rate signs.

Thus the following repair is closed:

    reality-complete Raman clutter
      -> choose a better one-shot common affine filter
      -> grow all required clean targets while damping old carriers and clutter.
                                                                    (3.2)

The repository must change mechanism rather than optimize another `H`.

## 4. Recomputed frontier

The reality-generated Raman translation operator itself still has additional
structure and must not be conflated with this affine-filter obstruction. For
`Q=e1` and `l.Q=0`, the `+l` and `-l` edge coefficients are paired by reality.
On the active scalar subspace they are skew-adjoint in the physical `L2`
weight. In particular the same-module `+l,-l` return is negative semidefinite,
not an autonomous growth mechanism. This should be frozen as a separate exact
checkpoint.

After that identity, viable escapes must change at least one load-bearing part
of the common-filter consumer. The main candidates are:

1. use the reality-paired Raman operator itself as a conservative transport and
   replace one-shot sign damping by a time-dependent/noncommuting filter;
2. redesign the clean consumer so only a lower-dimensional target combination
   must be amplified at a given filtering substep;
3. use spatial staging or sequential filters rather than one simultaneous
   trace-free strain; or
4. abandon the purifier route and return to a genuinely distinct terminal
   mechanism if these alternatives reproduce the same incompatibility.

The next exact discriminator should first freeze the skew-adjoint reality-paired
Raman identity, then test the cheapest sequential/two-stage strain schedule
against the six Farkas constraints. A sequential schedule changes the product
of propagators and is not covered by the static certificate.

No PLAN/canonical proof-graph promotion, recursive turnover, finite-time
singularity, or `NS-R3` conclusion is claimed here.
