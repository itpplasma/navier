# Solenoidal adjoint strain cannot give a one-sided nonlinear certificate

Date: 2026-09-12. Repository input before integration: `itpplasma/navier@9c001281e6b30ccde1c90728dc4842a0fd78b1ab`.

**Status: exact structural theorem for the nonlinear adjoint identity. Independent audit pending.** The result does not compute the source's complete physical adjoint and does not exclude nonlinear de-forcing. It rules out one natural way of turning the existing adjoint identity into a terminal obstruction.

The repository's full finite-horizon adjoint identity contains the exact nonlinear term

    integral (w tensor w):S(z),
    S(z)=(grad z+grad z^T)/2,                              (1.1)

where `z` is solenoidal. A tempting negative route is to choose `z` so this term has a fixed sign for every possible correction `w` and therefore cannot cancel the force pairing.

This is impossible. Since `div z=0`,

    tr S(z)=0.                                             (1.2)

At every point, a nonzero real symmetric trace-free `3x3` matrix has at least one positive and one negative eigenvalue. Hence the quadratic form

    w -> w^T S(z) w                                       (1.3)

is indefinite whenever `S(z)` is nonzero. A semidefinite trace-free strain must vanish.

Moreover a nonzero admissible whole-space `L2` solenoidal adjoint cannot have `S(z)=0` everywhere. At each nonzero Fourier frequency `k`, with `k.z_hat=0`,

    S_hat = (i/2)(k tensor z_hat + z_hat tensor k)

and exactly

    2 |S_hat|_F^2 = |k|^2 |z_hat|^2.                     (1.4)

After integration,

    2 ||S(z)||_2^2 = ||grad z||_2^2.                      (1.5)

Thus `S(z)=0` implies `grad z=0`, and an `L2(R3)` constant field is zero.

Therefore **no nonzero solenoidal adjoint can make the nonlinear term in the full de-forcing identity pointwise one-signed for arbitrary corrections**. A complete negative adjoint argument must instead obtain a quantitative magnitude bound, exploit structure of the actual correction, or establish a more delicate signed spacetime cancellation. Merely choosing a favorable adjoint strain sign is unavailable.

This is a structural wall, not a terminal theorem. It leaves the exact source-specific quotient between force pairing, controllable initial trace and nonlinear strain budget open.

Companion checker: `research/check_adjoint_strain_sign_wall.py`.
