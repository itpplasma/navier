# Mean-assisted startup removes the local high-harmonic entry seed

Date: 2026-09-11. Repository input:
`itpplasma/navier@2a9a9822e2b0d67149e591e9aa8c7d97f7564e71`.

**Status: exact conditional local control theorem for the source principal pulse.** A small trace-free mean strain of size `O(L^-1)` on the startup interval can replace the nonzero high-harmonic entry seed: the correction starts with zero wave trace, cancels the startup cutoff residual, and is exactly zero at the pulse peak. The required mean strain can be chosen pointwise to leave the wave normal fixed and to act as a real scalar gain on the instantaneous transverse pulse polarization.

This is a genuine mechanism change from homogeneous high-angular preloading and from the four-parent nonlinear daughter module. It does **not** yet construct the required mean strain from one global Schwartz datum, solve its mean/pressure equation, or close the full nonlinear correction.

The algebra is frozen by `research/check_source_mean_assisted_startup.py`.

## 1. Exact scalar startup identity

On one regular source label write the exact principal growing solution as

    h'=M(v)h,                                               (1.1)

and the actual cutoff primary pulse as

    y=psi(v)h.                                             (1.2)

The startup residual is

    (partial_v-M)y=psi' h.                                 (1.3)

Instead of prescribing the local entry seed `h(0)`, consider a correction `w` with

    w(0)=0,
    (partial_v-M)w=-psi' h+c psi h,                        (1.4)

where `c` is a real scalar supplied by an axisymmetric/mean correction channel.

Since `h` solves (1.1), the exact solution is

    w(v)=s(v)h(v),
    s(v)=-psi(v)+c integral_0^v psi(a) da.                 (1.5)

Let `v_*=L/2` be the source peak. The cutoff satisfies `psi(v_*)=1`. Put

    I_*=integral_0^v_* psi(a) da,
    c=1/I_*.                                               (1.6)

Then

    w(v_*)=0,
    y(v_*)+w(v_*)=h(v_*).                                 (1.7)

Thus the source peak is preserved **with zero high-harmonic correction at the local entry face**.

The source cutoff is one on

    3L/10 <= v <= 7L/10

and supported inside

    L/6 < v < 5L/6.

Hence

    L/5 <= I_* <= L/2,
    2/L <= c <= 5/L.                                      (1.8)

Only an `O(L^-1)` normalized mean control is required.

At the right face `psi(L)=0`, so

    w(L)=c I_L h(L),
    I_L=integral_0^L psi.                                  (1.9)

The ratio `c I_L` is `O(1)`, while the actual source pulse satisfies

    ||h(L)|| comparable to exp(-gamma_+ L).               (1.10)

Therefore the carried exit wave trace remains exponentially small. There is no zero-extension impulse: the correction simply carries this tiny trace forward.

## 2. Real divergence-free strain producing the scalar gain

The control in (1.4) is not an arbitrary scalar body force. It can be realized at the principal geometric-optics level by a trace-free velocity gradient.

At a fixed `(v,x_slow)` let `n` be the unit phase normal and let `e=h/|h|` be the instantaneous real transverse pulse polarization; choose the transverse unit vector `f` so that `(e,f,n)` is orthonormal. Define

    G_c=c(f tensor f-e tensor e).                          (2.1)

Then

    tr G_c=0,
    G_c^T n=0,
    G_c e=-c e.                                           (2.2)

For a mean affine gradient `G`, the pressure-retaining transverse amplitude action is

    A_G a=-G a+2 n (n.Ga)/|n|^2.                          (2.3)

Consequently

    A_(G_c)e=c e.                                         (2.4)

Moreover the phase equation

    n'=-G_c^T n                                           (2.5)

has zero contribution from this control. Thus `G_c` supplies exactly the real scalar term in (1.4) while leaving the phase normal unchanged at leading principal order.

This avoids the defect of using an isotropic transverse compression with a compensating normal eigenvalue, which would change the phase magnitude by order one over the `O(L)` pulse.

## 3. What changes in the prehistory problem

The source-pulse adjoint theorem showed that replacing the startup cutoff by an uncut pulse requires an exponentially small **wave** seed `h(0)`. The whole-prehistory angular theorem then made homogeneous high-angular preparation of that seed expensive unless it uses radial exterior occupation or nonlinear supply.

The present identity supplies a third local realization:

    zero wave entry trace
      + O(L^-1) mean transverse strain during startup
      -> exact preserved wave peak.                       (3.1)

Therefore the local high-angular seed itself is no longer logically indispensable. A successful unforced exactification may instead prepare an axisymmetric/mean correction whose normalized strain on each pulse startup approximates (2.1).

This is potentially important because angular mode zero is not subject to the `(abs(n)-1)^2/r^2` preparation penalty used to exclude trapped high-angular homogeneous seeds.

## 4. What remains load-bearing

The theorem is conditional on the availability of the mean gradient `G_c`. It does not establish that one initial datum produces the required sequence of stage-local gradients. In physical variables the fast pulse coordinate satisfies a stage-dependent scaling, so `c=O(L^-1)` in the principal equation need not correspond to a uniformly small physical gradient. A direct stagewise localized affine preload would again face viscosity and all-order Schwartz summability.

A full constructive use therefore needs one of the following:

1. a single axisymmetric correction mode which the source's contracting background amplifies into the required stagewise transverse strains;
2. causal generation of those mean strains from earlier wave stresses; or
3. a coupled correction solve in which the source's own smooth mean residual creates the required `m=0` component while the wave equation uses (1.4).

The alternative is a complete physical adjoint showing that even this mean-assisted class has divergent common-control cost.

## 5. Recomputed frontier

The first discriminator is no longer whether the four high-angular parents can survive from the global initial time. Before paying that cost, test the cheaper mean-assisted route:

> Can one axisymmetric finite-energy correction, issued from the global Schwartz trace or generated by the source mean residual, supply the `O(L^-1)` **normalized transverse-strain history** (2.1) on the countable pulse windows with summable all-order cost?

If yes, the local wave startup problem can be closed without high-angular preloading. If no, the exact obstruction must include the physical scale conversion and the mean/pressure equation; simply citing the angular preparation theorem would not address this new mechanism.

No common physical trace, full nonlinear de-forcing solution, singularity preservation, or `NS-R3` result is claimed. Independent mathematical audit and novelty assessment remain pending.
