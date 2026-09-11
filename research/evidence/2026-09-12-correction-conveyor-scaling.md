# Correction-driven radial entry has an energy-compatible scaling window, but a nondegenerate conveyor is already critical

Date: 2026-09-12. Repository input before integration: current `main`.

**Status: exact source-scale reduction and conditional critical-norm theorem;
independent mathematical audit and novelty assessment pending.** This packet
does not construct a correction-driven conveyor. It tests whether the ordinary
energy and dissipation budgets already exclude the radial-entry alternative
left open by the angular preparation, heat-import, exterior-characteristic and
far-pressure estimates.

## 1. Prediction before the test

Prediction: the speed required to move a packet an order-one fraction of the
source radius during one pulse activation window is much larger than the
prescribed source radial speed, but it can still occupy a shrinking volume with
vanishing energy and viscous action. Hence energy scaling alone will not close
UE1. However, if that speed is realized by the **total unforced velocity** on a
nondegenerate material parcel, its local `L3` norm already diverges and the
conveyor is terminal-strength rather than a harmless auxiliary mechanism.

All statements below use the inspected source scales already frozen in
`2026-09-11-angular-heat-import.md`:

    Q=2^(-ell),       0<h<1/100,
    L comparable to ell^2,
    r comparable to Q^(1/2),
    n comparable to Q^(-h/2),
    tau comparable to Q^(1+h) L.                         (1.1)

Here `tau` is the physical duration of one fast pulse window and `n` is the
nondegenerate angular index. Fixed positive comparison constants do not affect
the exponent conclusions.

## 2. Macroscopic radial crossing

To cross distance comparable to `r` in time `tau`, the required radial speed is

    V_mac comparable to r/tau
          comparable to Q^(-1/2-h) / L.                  (2.1)

This is larger than the source-sized radial speed `Q^(-1/2)` by the factor
`Q^(-h)/L -> infinity`; hence it is genuinely correction-driven and is not the
passive mechanism already excluded by the exterior characteristic theorem.

Take only the scaling cost of a divergence-free velocity cell with amplitude
`V_mac`, diameter comparable to `r`, and volume comparable to `r^3`. Then

    kinetic energy   ~ V_mac^2 r^3
                     ~ Q^(1/2-2h) / L^2 -> 0,            (2.2)

and a turnover lasting `tau`, with gradients on scale `r`, has viscous action

    nu integral ||grad u||_2^2 dt
       ~ nu V_mac^2 r tau
       ~ nu Q^(1/2-h) / L -> 0.                           (2.3)

Both exponents are positive for `0<h<1/100`. The local Reynolds number instead
obeys

    V_mac r / nu ~ Q^(-h)/(nu L) -> infinity.             (2.4)

Thus neither finite energy nor the global energy-dissipation identity forbids
this shrinking fast cell on dimensional grounds.

The angular viscous action seen by a passenger harmonic of index `n` at radius
`r` during the same window is

    nu n^2 tau/r^2 comparable to nu L.                    (2.5)

Therefore the bare angular-diffusion exponent is of `exp(-C L)` type, the same
quasi-Gaussian scale class as the local source entry seed `exp(-gamma L)`.
Equation (2.5) is a viscous-action comparison, not a propagator theorem: the
complete advection/stretching/pressure evolution remains uncontrolled.

## 3. A nondegenerate macroscopic conveyor is already terminal-strength

Assume now an exact classical unforced solution has times `t_j` approaching a
finite endpoint and source scales `Q_j -> 0`, and that on measurable sets
`E_j` of volume at least `c r_j^3` the **total velocity** satisfies

    |u(t_j,x)| >= c V_mac,j.                              (3.1)

Then

    ||u(t_j)||_3 >= c V_mac,j r_j
                  >= c Q_j^(-h)/L_j -> infinity.          (3.2)

Hence the repository's existing `L3` continuation suffix already makes such a
nondegenerate macroscopic conveyor a terminal negative consumer. No additional
source pulse amplification is needed to make its critical norm singular.

This is conditional: the scaling argument does not create the sets `E_j`, and
a correction component may cancel against the prescribed source in the total
field. The hypothesis is deliberately on the total unforced velocity.

## 4. The pressure-forced thin collar is cheaper and is the sharper survivor

The far-pressure theorem leaves a necessary relative collar thickness of order
`L/n` (up to fixed constants and lower-order logarithms). Put

    delta = r L/n
          comparable to Q^(1/2+h/2) L.                   (4.1)

Crossing only this collar during one pulse window requires

    V_col = delta/tau
          comparable to Q^(-1/2-h/2).                    (4.2)

Consider a nondegenerate collar parcel with two tangential dimensions
comparable to `r` and radial thickness `delta`, hence volume comparable to
`r^2 delta`. Its scaling costs are

    energy ~ V_col^2 r^2 delta
           ~ Q^(1/2-h/2) L -> 0,                         (4.3)

and, even charging the sharper gradient scale `delta`,

    nu V_col^2 (r^2 delta/delta^2) tau
       ~ nu Q^(1/2-h/2) -> 0.                            (4.4)

Again the energy law does not forbid the cell. But if the total velocity has
size `V_col` on a fixed fraction of this collar volume, then

    ||u||_3
      >= c V_col (r^2 delta)^(1/3)
      comparable to Q^(-h/3) L^(1/3) -> infinity.         (4.5)

Thus a nondegenerate material conveyor even across only the pressure-allowed
thin collar is itself critical-norm divergent.

The important escape is **sparsity/non-material forcing**. The near-collar
quadratic stress could in principle occupy a smaller set, or pressure/nonlocal
coupling could generate the parent without the total velocity satisfying the
nondegeneracy hypotheses of (3.1) or (4.5). The present calculation does not
bound such a stress and does not replace the complete physical adjoint.

## 5. Recomputed frontier

The passive source exterior, pure early heat import, and direct far-pressure
input are already quantitatively blocked. This packet adds two facts:

1. an actively correction-driven radial entry is **not** excluded by energy or
   dissipation scaling; and
2. any such entry realized as a nondegenerate material conveyor at the source
   scales is already strong enough to diverge `L3`.

Therefore the genuinely smaller UE1 object is now a sparse thin-collar stress,
nonlocal pressure/velocity response, or in-core non-axisymmetric generation
that supplies the four parent traces without first producing the nondegenerate
critical conveyor above. The alternative negative route is a complete physical
adjoint controlling those sparse/nonlocal mechanisms and the full-history gain.

No common Schwartz trace, full nonlinear de-forcing solution, singularity
preservation, or `NS-R3` theorem is claimed. The canonical proof graph and
formal status are unchanged.

## 6. Exact checker

`research/check_correction_conveyor_scaling.py` verifies all `Q` and `L`
exponents above in exact rational arithmetic, including positivity over the
repository range `0<h<1/100` and the critical-norm divergence exponents. It is
a scaling regression, not a PDE existence proof.
