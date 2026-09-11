# Full nonlinear correction cancels the mean-assisted zero-entry startup

Date: 2026-09-11. Repository input:
`itpplasma/navier@81b618a9dcdfe5da9f3fe0b2beae33c3ee988575`.

**Status: exact scoped obstruction.** The conditional linear module in
`2026-09-11-source-mean-assisted-startup.md` does not survive restoration of
the full quadratic correction equation when the total non-axisymmetric wave
has been canceled exactly. An axisymmetric mean perturbation acts on the
**total** wave, not on the prescribed source wave separately, so it cannot
create a nonzero angular harmonic from zero.

The bilinear algebra is frozen by
`research/check_source_mean_assisted_cancellation.py`.

This retires only the zero-wave-entry, axisymmetric-mean regeneration shortcut.
It does not exclude amplification of a nonzero tiny wave seed, non-axisymmetric
parent generation, radial-exterior import, or a complete source-specific
adjoint obstruction.

## 1. Complete correction equation

Write the prescribed forced source as

    U=B+Y,                                                 (1.1)

where `B` is the axisymmetric/mean part and `Y` denotes one selected nonzero
angular harmonic. Split the correction as

    w=b+W+... ,                                            (1.2)

with `b` axisymmetric and `W` in the same angular harmonic as `Y`.

The exact correction equation is

    L_U w + P div(w tensor w) = -P F.                     (1.3)

Let `N(a,c)=P[(a.grad)c]` denote the projected bilinear convection form. The
terms coupling the mean correction `b` to the selected source/correction wave
are

    N(b,Y)+N(Y,b)                                         (1.4)

from the linearization `L_U w`, together with

    N(b,W)+N(W,b)                                         (1.5)

from `P div(w tensor w)`.

Their exact sum is

    N(b,Y+W)+N(Y+W,b).                                    (1.6)

Thus the mean correction sees only the total wave

    Q=Y+W.                                                 (1.7)

No sign, asymptotic expansion, or smallness assumption is used.

## 2. The apparent scalar control disappears at zero total wave

The preceding conditional linear calculation considered

    (partial_v-M)W=-psi' h+c psi h                        (2.1)

and used the last term to rebuild a pulse starting with zero wave correction.
But the term `c psi h` is the principal representation of (1.4) alone. If the
zero-seed correction has canceled the source wave, `W=-Y`, then (1.5) supplies
its exact opposite and

    N(b,Y+W)+N(Y+W,b)=0.                                  (2.2)

Equivalently, after writing the physical equation for the total field `U+w`,
an axisymmetric mean background preserves every angular Fourier sector. The
zero state in a nonzero sector is invariant by uniqueness.

Therefore a bounded axisymmetric mean correction cannot make a nonzero pulse
appear from an exactly zero total harmonic. The conditional identity in the
preceding packet remains algebraically correct for a **linearized controlled
problem**, but it is not a physical full-NS startup mechanism.

## 3. What remains possible

Three genuinely different mechanisms survive this obstruction:

1. **nonzero tiny seed plus amplification.** If `Q` is not identically zero,
   mean strain may amplify it; the global problem becomes how to deliver a
   seed small enough to survive the prehistory yet large enough for the
   available finite amplification;
2. **non-axisymmetric generation.** Other wave harmonics can create the parent
   sector through quadratic convolution, so zero is no longer invariant for
   that sector; or
3. **radial-exterior import.** A nonzero high-angular packet may avoid the
   trapped preparation cost in the exterior and enter the source window late.

The full physical adjoint remains the alternative exclusion route.

## 4. Recomputed frontier

The high-angular parent-supply problem is not removed by an `m=0` control.
After the finite-L local causal module, the first terminal dependency is again:

> deliver a **nonzero** parent-sector trace to each source pulse from one global
> Schwartz correction, by radial exterior transport or genuinely
> non-axisymmetric nonlinear/parametric generation, or prove with the complete
> physical adjoint that every such bounded correction class fails.

Another axisymmetric zero-seed modulation does not change that dependency and
should not be retried.

No global correction, singularity preservation or `NS-R3` result is claimed.
Independent mathematical audit and novelty assessment remain pending.
