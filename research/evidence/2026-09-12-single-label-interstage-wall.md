# One fixed source label cannot carry the finite-L cage across a factor-two normalized scale change perturbatively

Date: 2026-09-12. Repository input: `itpplasma/navier@4aeeecccb51266c8e06ae6fd43a8212a0b2215bc`.

**Status: exact source-coordinate/lattice-deformation obstruction to one specific physical adapter. Author proof with exact checker; independent mathematical audit and novelty assessment pending.** This does not prove that no physical interstage adapter exists. It proves that the repository's existing fixed-label, fixed-reference finite-`L` persistence theorem cannot simply be extended across one factor-two normalized scale change. A surviving adapter must recenter/change labels or use a genuinely nonperturbative physical propagator.

## 1. Prediction and exact interface

The reference passive-carry theorem needs the physical similarity scale to contract from `q=Q` to

    q=rho Q,      rho=2^(-2/h),                           (1.1)

before a doubled physical frequency changes from normalized axial scale `z=2` to `z=1`.

The finite-`L` source-cage theorem, however, compares one unrounded source label with the frozen cage through the exact lattice embedding

    T_(tau,eta)(k)
      =(c k_z+(1+tau)d(k), -eta d(k), k_z),
    d(k)=k_x-c k_z,
    tau=v/L.                                               (1.2)

Its perturbative conclusion is explicitly only for a **fixed fast-time window**, where `tau=O(L^-1)`.

Prediction: if one keeps the same lifted label through the entire scale change (1.1), then the actual fast coordinate displacement satisfies `Delta v/L -> infinity`. The exact map (1.2) therefore leaves every small perturbative neighborhood of the frozen cage; the fixed-window theorem cannot serve as the full interstage adapter.

## 2. Exact same-label fast displacement

Use the already inspected source identities. On a fixed lifted label of band scale `Q`,

    partial_t v=Q^(-1-h).                                 (2.1)

On the exact `eta=0` similarity ray,

    1-t=q.                                                (2.2)

Hence the physical duration of the factor-two normalized scale change (1.1) is exactly

    Delta t=(1-rho)Q.                                    (2.3)

If the **same** lifted label is extrapolated across this interval, (2.1) gives

    Delta v=(1-rho)Q^(-h).                               (2.4)

The source pulse length satisfies

    L comparable to ell^2,      Q=2^(-ell).              (2.5)

Therefore

    Delta v/L comparable to 2^(h ell)/ell^2 -> infinity. (2.6)

This is not the reference growth-action integral `3Q^(-h)/h`; it is the actual fixed-label fast-coordinate displacement. Distinguishing those quantities is essential.

For an exact calibration take `h=1/200`, `ell=400k`. Then

    Q^(-h)=4^k,
    L=160000 k^2,
    tau_k=(1-rho)4^k/(160000 k^2),                        (2.7)

and

    tau_(k+1)/tau_k = 4 k^2/(k+1)^2 >=16/9,    k>=2.      (2.8)

Thus `tau_k` grows at least geometrically.

## 3. Exact lattice deformation leaves the frozen cage

For the four caged parent tilts

    s=1/2,-2/5,1/5,-1/10,

with `c=1/20`, one has

    |d(k)|=|s-c| >=3/20.                                  (3.1)

Also `|k|^2=1+s^2<=5/4`. Consequently

    d(k)^2/|k|^2 >=9/500.                                 (3.2)

Equation (1.2) gives

    |T_(tau,eta)k-k|^2/|k|^2
      = [d(k)^2/|k|^2](tau^2+eta^2)
      >= (9/500) tau^2.                                  (3.3)

Combining (2.6) and (3.3), the same-label frequency embedding moves an unbounded relative distance from the frozen cage during the required scale change.

In particular, the fixed-window estimate

    sup_(k!=0) |T k-k|/|k| <= C/L                       (3.4)

cannot be extrapolated to this interval on the same label/reference. The obstruction is already in the exact phase lattice; it does not depend on nonlinear errors, pressure estimates, or numerical evolution.

## 4. What is and is not excluded

This closes only the **direct same-label perturbative adapter**:

    fixed finite-L cage theorem
      -> keep one label/reference across factor-two scale change
      -> reuse local hyperbolicity/graph transform.

That route is invalid because the load-bearing small deformation parameter becomes unbounded.

It does **not** exclude:

1. a sequence of recentered/overlapping source labels whose local reference frames are changed before `|v|/L` becomes large;
2. a genuinely nonperturbative propagator in the moving physical variables;
3. inherited-mode transport that is not described by the one-label principal phase map;
4. sparse thin-collar/nonlocal entry; or
5. a full physical adjoint obstruction.

A successful recentered construction must supply an actual transition map between neighboring labels/windows and prove that the complete returned state, stable counterterms, pressure, localization, and nonlinear convolution are preserved through every transition. Merely restarting the local theorem would reintroduce the forbidden reset/gluing problem.

## 5. Exact check and terminal scope

`research/check_interstage_single_label_wall.py` freezes (2.7)--(2.8), the four-parent lower bound (3.2), and the resulting divergence in (3.3).

No recentered multi-label propagator, common Schwartz trace, nonlinear de-forcing solution, singularity preservation, or `NS-R3` theorem is proved. The reference passive-carry loss remains a reference theorem until a valid recentered/nonperturbative physical adapter or adjoint is supplied.
