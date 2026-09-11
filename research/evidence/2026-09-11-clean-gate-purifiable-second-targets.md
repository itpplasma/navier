# All clean second-generation targets retain the intended purifiable component

Date: 2026-09-11. This packet combines the second-generation ancestry wall
with the mode-specific affine purifier.

**Status: exact author algebra; independent audit and novelty undetermined.** It
establishes a necessary compatibility condition for a routed purifier
architecture.  It does not construct the spatial routing or finite-energy
purifier history.

## 1. Question left by the ancestry wall

At the three nominal second-generation frequencies, the leading quartic,
order-`t^3` coefficient of the co-located original NS vector field is not the
pure selected-gate vector.  Write

    V_full = V_sel + V_old,                               (1.1)

where `V_old` contains inherited-parent Taylor trees.  The previous packet
proved nonparallelism at one target, so a naive second gate fails.

The new mode-specific purifier, however, can recover a desired transverse
polarization `a` from an arbitrary coefficient at the **same fixed wavevector**
provided that coefficient has nonzero projection onto `a`: the purifier strain
leaves the wavevector fixed, grows the `a` component and exponentially damps
its unique transverse orthogonal complement.

Thus the exact algebraic question is

    <V_sel,V_full> != 0 ?                                 (1.2)

for every nominal second target at the clean projective-return root.

## 2. Exact positive answer for all three targets

The nominal second-generation lattice frequencies are

    h_+=(0,1,1),
    h_0=(-2,-1,-1),
    h_-=(0,-1,1).                                        (2.1)

For real `z`, all relevant vectors have a common imaginary phase, so the
Hermitian projection condition (1.2) is equivalent, up to a harmless sign, to
nonvanishing of the algebraic dot product used in the symbolic calculation.

After clearing manifestly nonzero denominators and harmless powers of `z`,
the three projection numerators are respectively

    R_+(z)=
      3z^15+8z^14+7z^13+8z^12+25z^11+76z^10+53z^9
      -2z^8+76z^7+162z^6+256z^5-44z^4
      +128z^3+120z^2+48z-176,                             (2.2)

    R_0(z)=
      9z^15-82z^14+351z^13-912z^12+1701z^11-2876z^10
      +5547z^9-11084z^8+19174z^7-27222z^6+32442z^5
      -31712z^4+23456z^3-11360z^2+2744z-80,               (2.3)

    R_-(z)=
      3z^15-8z^14+7z^13-8z^12+25z^11-76z^10+53z^9
      +2z^8+76z^7-162z^6+256z^5+44z^4
      +128z^3-120z^2+48z+176.                             (2.4)

The clean return polynomial is

    Q(z)=z^10-z^9+4z^8+2z^6-2z^5
         -8z^3-32z^2+40z-16.                              (2.5)

Exact arithmetic gives

    gcd(Q,R_+)=gcd(Q,R_0)=gcd(Q,R_-)=1.                   (2.6)

More specifically, the unique positive clean root is isolated by

    1.2847 < z_* < 1.2848,                                (2.7)

and none of `R_+,R_0,R_-` has a zero on this rational interval.  Therefore

    <V_sel(h_j),V_full(h_j)> != 0

for `j=+,0,-` at `z=z_*`.                                 (2.8)

Numerically, if `V_full=c V_sel+V_perp` with
`V_perp` orthogonal to `V_sel`, the projection coefficients at `z_*` are
approximately

    c_+ = 2.076,
    c_0 = 2.854,
    c_- = 1.436.                                          (2.9)

Thus ancestry contamination does not accidentally erase the intended component;
in fact all three intended projections are comfortably nonzero in the present
normalization.

## 3. Consequence: a coherent gate--purify architecture survives algebraically

For each target `(h_j,V_sel(h_j))`, the coordinate-free purifier from
`2026-09-11-mode-specific-affine-purifier.md` supplies a trace-free symmetric
strain

    S_j=-e_j tensor e_j + f_j tensor f_j,                 (3.1)

where `e_j` is the normalized intended polarization and `f_j` its transverse
orthogonal complement.  The strain obeys

    S_j h_j=0,      S_j e_j=-e_j,      S_j f_j=f_j,       (3.2)

so an affine background of sufficient strength leaves `h_j` fixed while
exponentially increasing the desired-to-orthogonal ratio.

Equations (2.8) therefore mean that **every one of the three contaminated
second-generation target modes is individually purifiable**.  The
second-generation ancestry wall kills naive co-located iteration, but it does
not kill a routed architecture of the form

    clean first gate
      -> contaminated target birth
      -> separate target packets
      -> mode-specific purification
      -> recombine purified targets
      -> next gate.                                       (3.3)

This is the first version of the dyadic mechanism in the current programme for
which both of the following are simultaneously true:

* the first quadratic source can be made algebraically clean;
* the leading second-generation ancestry error at the desired frequencies has
  a proven, nonzero recoverable component rather than an orthogonality wall.

## 4. The remaining hard step is now spatial, not carrier algebra

Architecture (3.3) still lacks its load-bearing PDE operation.  The three
purifier strains are mode-specific and generally incompatible at one common
point.  The affine reference fields have infinite energy.  Therefore one must
prove an autonomous finite-energy **router** that, inside one unforced forward
history,

1. separates the newborn target packets into different interaction regions;
2. supplies each region with the appropriate localized strain history for a
   parabolic-scale time;
3. prevents inherited parents and other packets from producing uncontrolled
   interactions during that routing/purification interval;
4. recombines the purified children in the pairing graph required by the next
   gate;
5. repeats after dyadic rescaling without resetting the state.

No heat dispersion provides this automatically.  This router/recombiner is now
a substantially sharper target than another Fourier cancellation search.

## 5. Reproducibility

`research/check_clean_gate_purifiable_second_targets.py` freezes the exact
projection obstruction polynomials (2.2)--(2.4), the root isolation (2.7), and
the coprimality/nonvanishing checks.  The complete second-order ancestry vector
for `h_0` is independently frozen in
`research/check_clean_gate_second_generation_wall.py`.

No finite-energy purifier, routed packet chain, manuscript/formal update, or
terminal NS-R3 claim is made here.
