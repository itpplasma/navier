# The forced source's Type-II exponents obstruct a direct finite-time unforced blow-up limit

Date: 2026-09-11. Repository input:
`itpplasma/navier@74de5ae071418d9d80d964a9eeadf9c310c25638`.

**Status: exact scaling obstruction for the simplest forced-to-unforced blow-up extraction.** Because the external force is smooth, any sufficiently small isotropic Navier--Stokes rescaling makes the rescaled force small. But the particular anisotropic source core is supercritical relative to isotropic NS scaling: no isotropic scale simultaneously keeps a finite nonzero remaining blow-up time and a bounded velocity normalization. Its scale-invariant `L^3` core size also diverges.

This does not exclude more elaborate extraction/localization arguments. It prevents treating the source's smooth force as if its vanishing under blow-up scaling directly produced the required finite-energy/finite-critical-norm unforced singular Cauchy solution.

The exponent ledger is frozen by `research/check_source_unforced_scaling_wall.py`.

## 1. Source exponents

Write `tau=1-t`. The source's central core has the scales

    |U| ~ tau^(-1/2-h),
    ell_r ~ tau^(1/2),
    ell_z ~ tau^(1/2-h),       h>0.                       (1.1)

Thus its volume is of order

    tau^(3/2-h),                                           (1.2)

its kinetic energy scale is

    E_core ~ tau^(1/2-3h),                                (1.3)

and its critical cubic mass is

    ||U||_(L3(core))^3 ~ tau^(-4h).                       (1.4)

The last quantity diverges even though the unscaled kinetic energy tends to zero.

## 2. General isotropic NS scaling

Take an isotropic NS scale

    r=tau^alpha,
    U_r(x,s)=r U(x0+r x,t+r^2 s).                         (2.1)

The rescaled remaining time to the forced singular endpoint is

    tau/r^2 = tau^(1-2 alpha),                            (2.2)

while the rescaled characteristic velocity is

    r |U| ~ tau^(alpha-1/2-h).                            (2.3)

To keep a finite nonzero remaining endpoint time one must take

    alpha=1/2.                                             (2.4)

Then

    r|U| ~ tau^(-h) -> infinity.                          (2.5)

Conversely, bounded velocity requires

    alpha >= 1/2+h.                                       (2.6)

For the velocity-normalizing choice `alpha=1/2+h`,

    tau/r^2=tau^(-2h) -> infinity.                        (2.7)

So the singular endpoint recedes to infinite rescaled time.

There is no exponent `alpha` satisfying both requirements because `h>0`.

## 3. Energy and critical norm do not repair the compactness

Under NS scaling, squared `L2` norm scales by `r^-1`. Hence the endpoint-time scale `r=tau^(1/2)` gives

    r^-1 E_core ~ tau^(-3h) -> infinity,                  (3.1)

while the velocity-normalizing scale `r=tau^(1/2+h)` gives

    r^-1 E_core ~ tau^(-4h) -> infinity.                  (3.2)

The `L3` norm is scale invariant and (1.4) already shows its divergence.
Thus neither natural isotropic normalization supplies a bounded finite-energy or finite-critical-norm family from the source core.

The smooth force does rescale with the factor `r^3` and is therefore harmless in a local blow-up limit when its derivatives stay bounded. The obstruction here is not the force term; it is the source velocity's Type-II/anisotropic scaling.

## 4. Relation to the older ancient-limit programme

The repository already proved a general two-time-marked ancient extraction for a hypothetical unforced singular solution and recorded why its normalized rotational energy cost is summable. The present result is different and source-specific: it asks whether the **known forced singular source** can be turned into the desired unforced singular solution simply by zooming in until the smooth force disappears.

The answer for the direct isotropic extraction is no. Endpoint-normalized rescalings do not have bounded velocity, while velocity-normalized rescalings have no finite singular endpoint.

## 5. Recomputed frontier

The full-PDE exactification route therefore still requires a nonzero global initial correction. After the local finite-`L` four-parent module and the failure of the axisymmetric zero-seed shortcut, the remaining constructive mechanisms are:

1. radial-exterior import of a nonzero parent-sector trace; or
2. genuinely non-axisymmetric nonlinear regeneration of the parent sector from earlier correction modes.

The complete physical adjoint remains the alternative route for quantitatively excluding both mechanisms in a bounded correction class.

No unforced counterexample, regularity theorem, or `NS-R3` conclusion is claimed. Independent audit remains pending.
