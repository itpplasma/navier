# The exact source exterior carries passive packets away from the active similarity annulus

Date: 2026-09-11. Repository input:
`itpplasma/navier@8340037220a5e6c21b275aa2eff4c8c7710e12cd`.

**Status: exact source-specific kinematic obstruction.** The whole-prehistory angular theorem leaves radial-exterior occupation as one way a high angular mode might avoid the trapped `n^2/r^2` viscous preparation cost. For the actual forced source background, however, the exact exterior characteristics do not carry such a packet back into the active similarity annulus. In the region where the source velocity profile has already vanished in its radial/axial components, the similarity radius `X` is strictly increasing along material trajectories.

The algebra is frozen by
`research/check_source_exterior_characteristic_wall.py`.

This excludes **passive transport by the prescribed source base flow** as the missing exterior-return mechanism. It does not exclude transport created by the correction itself, diffusion/nonlocal pressure coupling, or genuinely nonlinear generation of the parent harmonic.

## 1. Exact material identity for the similarity radius

Use the source similarity variables

    tau=1-t=q(1-eta^2),    z=q^D eta,
    D=1/2-h,    A=1/2+h,    L=1-2h eta^2,
    X=r^2/(2q),       A+D=1.                              (1.1)

Equivalently, q is the positive preterminal solution of
`q-z^2 q^(2h)=1-t`, not `1-t/L`. Here L is the geometric Jacobian factor,
not the length of a fast-time pulse. For `0<h<1/2` and `abs(eta)<1`, L is
positive. This definition was corrected on 2026-09-11; the material identity
and exterior conclusion below are unchanged. The checker now derives the
coordinate derivatives from this implicit definition rather than assuming them.

The source coordinate identities give

    X_t=X/(qL),
    X_r=r/q,
    X_z=-2 eta X/(q^D L).                                (1.2)

For the prescribed base velocity write

    u_r=V_0/r,
    u_z=q^(-A)U.                                          (1.3)

The source's radial reconstruction has

    V_0 = X/L [2 eta U-2D eta A_X(U)-d partial_eta A_X(U)], (1.4)

where `A_X` is the source radial averaging operator. Therefore

    D_t X
      =X_t+u_r X_r+u_z X_z
      =X/(qL)+V_0/q-2 eta X U/(qL)

      =X/(qL) [1-2D eta A_X(U)-d partial_eta A_X(U)].      (1.5)

This is exactly the source quantity customarily denoted by the bracket `W` in the similarity-coordinate transport formulas.

## 2. Exact exterior sign

The source support theorem gives an exterior threshold `X_v` beyond which

    U=V_0=0,                                               (2.1)

and a larger threshold `X_b` beyond which the remaining exterior equation is the pure radial heat equation for the swirl. In the region (2.1), `A_X(U)` and its eta derivative also vanish. Thus (1.5) becomes

    D_t X = X/(qL) >0                                     (2.2)

for `X>0` and preterminal `q>0`.

Equivalently, the physical radial and axial base velocities vanish in that exterior, so a base characteristic stays at fixed physical `(r,z)` while the contracting similarity coordinate `X=r^2/(2q)` increases as `q` decreases.

Hence a packet which avoids the core preparation loss by occupying the true source exterior is not passively carried inward into the active similarity annulus by the prescribed source history. It moves in the opposite direction in similarity coordinates.

## 3. Consequence for the angular-preparation alternative

The whole-space angular preparation theorem proved the exhaustive alternative for a high angular mode of the unforced correction: if it is not supplied nonlinearly and is not superalgebraically damped while trapped, it must spend almost all logarithmic preparation time in the radial exterior.

The present source-specific calculation shows that **base-flow exterior occupation alone does not complete that mechanism**. Returning such a nonzero packet to the pulse region requires an effect absent from the passive source characteristics, for example

* correction-driven radial/axial advection;
* diffusion combined with sufficiently large exterior amplitude;
* nonlocal pressure/velocity coupling; or
* fresh non-axisymmetric nonlinear generation nearer the pulse time.

All of these are part of the correction's genuinely nonlinear/global dynamics. The passive-exterior branch has therefore merged back into the nonlinear parent-supply problem.

## 4. Scope

This note does not prove that no unforced correction can ever enter from large radius. It proves only that the **known forced source background** supplies no inward characteristic conveyor in its exact exterior. A successful exterior construction would have to quantify the correction's own transport or diffusion and its all-order Schwartz/energy cost.

No common initial trace, nonlinear de-forcing contraction, singularity preservation, or `NS-R3` conclusion is claimed. Independent mathematical audit and novelty assessment remain pending.

Source provenance: OpenAI, *Finite Time Blowup for Navier--Stokes* (2026), similarity-coordinate identities and the exact exterior/support theorem inspected at the public source; the repository's prior source audits retain version/provenance qualifications.
