# Perturbative co-located mixed-packet discrimination by one finite-energy strain

Date: 2026-09-11. This packet combines the exact common second-target strain
with the finite-energy localized-strain amplifier.

**Status: author proof using standard short-time smooth dependence of classical
Navier--Stokes; independent audit and novelty undetermined.** The theorem is
perturbative in the target-packet amplitude relative to the strain background.
It does not yet realize the large-amplitude recursive gate or remove the strain
background after purification.

## 1. Six packet directions at one spatial site

Use the common rational strain

    S = [[ 9/8,   1/36,   1/4 ],
         [ 1/36, -1/5,    1/14],
         [ 1/4,   1/14, -37/40]],                         (1.1)

and the three clean second-target wavevectors `k_j`, intended transverse unit
polarizations `e_j`, and rejected transverse unit polarizations

    f_j=(k_j/|k_j|) cross e_j.                            (1.2)

The exact common-strain packet proves, at the positive clean root, strict
margins

    -10 e_j.S.e_j-|k_j|^2 > 0,                            (1.3)

    -10 f_j.S.f_j-|k_j|^2 < 0                             (1.4)

for every `j=1,2,3`.

Choose one large radial spatial envelope `chi_L(x)=chi(x/L)`.  As in the
localized-strain amplifier, construct exact compact solenoidal packets
`w_(j,e),w_(j,f)` whose leading parts on the common envelope are

    chi_L cos(k_j.x) e_j,
    chi_L cos(k_j.x) f_j,                                 (1.5)

with relative cutoff errors tending to zero as `L -> infinity`.

Because the six carriers/polarizations are distinct, normalized cross inner
products between different carrier families tend to zero by the
Riemann--Lebesgue lemma.  The same holds for gradient inner products and for
`S`-weighted inner products.  Therefore their finite Gram matrices converge to
the diagonal plane-wave Gram matrices encoded by (1.3)--(1.4).

Let

    E_L=span{w_(1,e),w_(2,e),w_(3,e)},
    F_L=span{w_(1,f),w_(2,f),w_(3,f)}.                    (1.6)

For all sufficiently large fixed `L`, there is a number `gamma>0` such that
for the quadratic form

    q(w)=-10 <w,S w> - ||grad w||_2^2,                    (1.7)

one has the **uniform subspace inequalities**

    q(e) >= gamma ||e||_2^2        for all e in E_L,      (1.8)

    q(f) <= -gamma ||f||_2^2       for all f in F_L.      (1.9)

Moreover `E_L` and `F_L` are transverse; for large `L` they are arbitrarily
close to orthogonal in `L2`.

## 2. Compact strain background

Choose `R>2L` and a cutoff equal to one on a ball containing all six packet
supports.  Set

    B_0=10 curl[-chi_R(x) x cross (Sx)/3].                (2.1)

Then `B_0` is real, compactly supported, smooth and solenoidal, and

    grad B_0=10 S                                         (2.2)

on the complete packet region.

Let `B(t)` be the classical viscosity-one unforced NS solution from `B_0`.
Let `L(t,0)` denote the linearized solution operator about `B(t)`.
For a linearized perturbation `w`, the exact energy identity at time zero is

    (1/2) d/dt ||w||_2^2 |_(t=0) = q(w).                  (2.3)

Because `E_L` and `F_L` are finite dimensional, all Sobolev norms on each are
equivalent.  The classical linearized flow is `C^1` in time in the required
Sobolev spaces.  Hence the Taylor remainder in (2.3) is uniform on the unit
spheres of these two subspaces.

It follows from (1.8)--(1.9) that there is `delta>0` and numbers

    a>1,       0<b<1                                      (2.4)

such that

    ||L(delta,0)e||_2 >= a ||e||_2       for e in E_L,    (2.5)

    ||L(delta,0)f||_2 <= b ||f||_2       for f in F_L.    (2.6)

The output spaces

    E_delta=L(delta,0)E_L,
    F_delta=L(delta,0)F_L                                 (2.7)

remain transverse for sufficiently small `delta`, because the linearized
operator is close to the identity on the fixed finite-dimensional space.

Thus the **linearized mixed-packet discriminator** is already a genuine
finite-time statement.  If an input is decomposed as `e+f` with
`e in E_L`, `f in F_L`, its output decomposes uniquely as

    L(delta,0)e + L(delta,0)f in E_delta + F_delta,       (2.8)

and the component norm ratio satisfies

    ||L(delta,0)f||_2 / ||L(delta,0)e||_2
       <= (b/a) ||f||_2/||e||_2,                          (2.9)

with `b/a<1`.

## 3. Full nonlinear perturbations

Now solve the original unforced equation from

    U_epsilon(0)=B_0 + epsilon (e+f),                     (3.1)

where `e+f` ranges over a fixed bounded subset of `E_L+F_L`.  For Sobolev
regularity above the classical local threshold, the NS solution map is
Frechet differentiable at `B_0`.  Uniformly on this finite-dimensional bounded
set,

    U_epsilon(delta)-B(delta)
       = epsilon L(delta,0)(e+f) + O(epsilon^2)            (3.2)

in a lower fixed Sobolev norm and hence in `L2`.

Let `P_E,P_F` be bounded projections onto `E_delta,F_delta` for a fixed direct
sum decomposition of their finite-dimensional span, extended by an arbitrary
bounded complement projection.  Applying these projections to (3.2) gives

    P_E[U_epsilon(delta)-B(delta)]
      = epsilon L(delta,0)e + O(epsilon^2),                (3.3)

    P_F[U_epsilon(delta)-B(delta)]
      = epsilon L(delta,0)f + O(epsilon^2).                (3.4)

Therefore on every cone

    ||e||_2 >= kappa ||f||_2,
    ||e||_2+||f||_2 <= C                                  (3.5)

with fixed `kappa>0,C<infinity`, there exists `epsilon_0>0` such that for
`0<epsilon<=epsilon_0` the rejected-to-desired output ratio is strictly smaller
than the corresponding input ratio, up to any prescribed slack above `b/a`.
In particular, the six-mode mixture is **genuinely discriminated inside one
finite-energy, co-located, full nonlinear NS evolution**.

The cone restriction is essential: if the desired component is arbitrarily
smaller than the nonlinear `O(epsilon^2)` remainder, a uniform ratio statement
cannot hold.  The clean second-target calculation supplies nonzero intended
projections with comfortable fixed coefficients, so a fixed cone is the
relevant regime for that application.

## 4. Scaling

As in the localized-strain amplifier, viscosity-one solutions scale to any
fixed physical viscosity `nu>0` and carrier scale `b_scale` by

    V_b(t,x)=nu b_scale V(nu b_scale^2 t,b_scale x).       (4.1)

The discrimination time is

    Delta t = delta/(nu b_scale^2),                       (4.2)

and all component amplification/contraction ratios are unchanged.  The `L2`
energy cost of the compact background still scales like `nu^2/b_scale`.

Hence neither finite energy nor fixed viscosity creates a scale obstruction to
this **single-stage perturbative discriminator**.

## 5. What this removes from the blocker list

The following previously separate concerns are now removed at mechanism level:

* three different affine purifier matrices are not required;
* the three target carrier families need not be spatially separated merely for
  polarization discrimination;
* compact finite-energy strain germs suffice for a short genuine nonlinear
  discrimination interval;
* a finite mixture, not only six separate test solutions, is covered in the
  small-perturbation regime.

The live gap moves to **stage integration**:

1. prove that the actual target packets born from the clean gate enter the
   perturbative cone (3.5) relative to a strain packet generated by the same
   forward solution rather than independently prescribed at the purification
   time;
2. control old parents, ladder modes and strain-background sidebands during
   the interval (4.2);
3. prove that after discrimination the desired three components have the
   phases/envelopes needed for the next nonlinear gate;
4. generate the next-scale strain/background autonomously rather than resetting
   `B_0` at each stage.

These are substantially narrower than the earlier abstract `router` label.

## 6. Audit boundary

The exact carrier margins are independently frozen in
`research/check_common_second_target_strain.py`.  The compact-strain identity,
relative-energy identity and fixed-viscosity scaling are frozen in the
localized-strain amplifier packet.  The only new analytic input here is
standard short-time differentiability/continuous dependence of the classical
NS flow and finite-dimensional compactness.

No claim is made that the actual clean-gate output has yet been inserted into
this discriminator in one autonomous history.  No recursive turnover or
terminal NS-R3 result is claimed.
