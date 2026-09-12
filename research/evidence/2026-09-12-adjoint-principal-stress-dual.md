# Principal solenoidal source forcing is small in the nonlinear strain-dual norm

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@b4ed946123b030819e7eaee600c8cf66e3804f5c`.

**Status: exact Fourier-symbol theorem for the principal high-frequency force component. Independent audit pending.** This is not a whole-space localized source theorem and does not estimate the source envelope, low-frequency leakage, or complete physical history.

For a nonzero wavevector `k` and a solenoidal force coefficient `f` with

    k.f=0,                                                  (1.1)

define the symmetric tensor symbol

    H(k,f) = [k tensor f + f tensor k]/|k|^2.              (1.2)

Then exactly

    H k = f.                                               (1.3)

Thus, restoring the Fourier phase, the symmetric tensor

    Ghat = -i H                                             (1.4)

satisfies

    i k_j Ghat_ij = f_i.                                   (1.5)

Its Frobenius norm is

    |Ghat|_F^2 = 2 |f|^2/|k|^2.                           (1.6)

For any test coefficient `z`,

    H : sym(k tensor z) = f.z.                             (1.7)

Consequently a pure high-frequency projected force mode is exactly the divergence of a symmetric stress whose norm is smaller than the force amplitude by the factor `sqrt(2)/|k|`, and its pairing with an adjoint is exactly a pairing against symmetric strain.

This matters for the full nonlinear de-forcing identity because the unknown quadratic correction also appears as a symmetric stress `w tensor w` paired with `S(z)`. At the principal-carrier symbol level there is therefore no favorable dual mismatch obtained merely from high frequency: increasing `|k|` makes the force **cheaper**, not more expensive, in the same strain-dual variable used by the nonlinear budget.

The theorem is intentionally scoped. A localized packet has envelope derivatives and a distribution of frequencies; the full source residual has mean/slow pieces, moving geometry, pressure reconstruction, and long history. These terms can invalidate the pure `1/|k|` stress scale and are precisely where a successful complete adjoint obstruction would now have to live.

Combined with the preceding strain-sign wall, two distinct simple adjoint mechanisms have failed: neither a sign choice nor the principal carrier itself produces a terminal nonlinear de-forcing obstruction. Per the diversification rule, further principal-symbol adjoint algebra is not the next attack. The constructive grade-changing/nonparent late-regeneration route is next; the complete adjoint remains available only through genuinely nonprincipal, localized full-history structure.

No common trace, nonlinear correction, singularity preservation, or `NS-R3` result is claimed.

Companion checker: `research/check_adjoint_principal_stress_dual.py`.
