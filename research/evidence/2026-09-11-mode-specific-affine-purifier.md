# Exact finite-time mode-specific affine polarization purifier

Date: 2026-09-11. Repository input before this additive note:
`itpplasma/navier@a4817da4224c6ea9ea96c615593d20bbd37118b9`.

**Status: author proof for an exact affine/infinite-energy mechanism; independent
mathematical audit and novelty undetermined.** This does not construct a
finite-energy localized purifier, a multi-mode turnover, a one-datum cascade,
or an unforced singularity. No PLAN/manuscript/canonical/formal status is
promoted.

The closed-strain-loop packet proves that a *common* affine deformation which
returns all carrier geometry cannot erase the clean-gate parents while
preserving both signed `1--3` children. This note removes the common-loop
requirement and proves an exact finite-time mechanism for one carrier at a
time. The carrier itself does not move.

## 1. Coordinate-free purifier

Let `k` and `a` be nonzero real vectors with

    k.a=0.

Put

    e=a/|a|,
    f=(k cross a)/(|k||a|),
    n=k/|k|.

Then `(e,f,n)` is an orthonormal frame. Define

    S_(k,a) = - e tensor e + f tensor f.                 (1.1)

The matrix is real, symmetric and trace free, and

    S k=0,       S e=-e,       S f=f,
    S^2=I-n tensor n=P_k.                                (1.2)

For any constants `sigma>0` and `nu>0`, the affine field

    U(x)=sigma S x                                      (1.3)

is an exact steady unforced incompressible Navier--Stokes solution on `R3`:
`div U=0`, `Delta U=0`, and

    (U.grad)U=sigma^2 S^2 x
              =grad [sigma^2 x.S^2.x/2].                (1.4)

Thus the pressure is the negative of the quadratic potential in (1.4).
The field has infinite kinetic energy; (1.3) is a mechanism reference, not an
admissible Clay datum.

## 2. Exact full-NS one-frequency dynamics

Fix a physical wavevector `K=b k`, `b>0`. Since `S^T K=0`, the affine flow does
not deform the Fourier phase. For arbitrary complex scalars `A_0,B_0`, set

    v(t,x)=Re[(A(t)e+B(t)f) exp(i K.x)].                 (2.1)

Because every Fourier coefficient in (2.1) is transverse to `K`, its
self-convection vanishes exactly: every ordered interaction of `+/-K` has a
factor `(coefficient).K=0`. Consequently `U+v` is an exact solution of the
full, not merely linearized, equation provided

    A'=( sigma-nu|K|^2) A,
    B'=(-sigma-nu|K|^2) B.                              (2.2)

Hence

    A(t)=A_0 exp[(sigma-nu|K|^2)t],
    B(t)=B_0 exp[(-sigma-nu|K|^2)t],                    (2.3)

and the unwanted-to-desired coefficient ratio satisfies the exact identity

    |B(t)/A(t)|=|B_0/A_0| exp(-2 sigma t).               (2.4)

If

    sigma>nu|K|^2,                                      (2.5)

the desired polarization grows while its transverse orthogonal complement
decays. Unlike the previous common affine filter, there is no wavevector drift
to undo because `K(t)=K` identically.

This does not contradict the closed-loop wall. That wall concerns one common
closed deformation applied simultaneously to the signed children and parents.
The present purifier is tailored to one pair `(k,a)` and need not preserve any
other carrier.

## 3. Application to the clean circuit's premature doubled `k2` mode

For the contamination-free family,

    k2=(0,1,0),       a2=(1,0,z),                         (3.1)

and choose the transverse orthogonal vector

    w2=(-z,0,1).                                         (3.2)

Formula (1.1) becomes

    S2=1/(1+z^2) [[z^2-1, 0, -2z],
                  [0,     0,   0 ],
                  [-2z,   0, 1-z^2]].                    (3.3)

It obeys exactly

    S2 k2=0,       S2 a2=-a2,       S2 w2=w2.            (3.4)

The full-time-tree analysis of the clean gate found premature/polluting
components on doubled target frequencies before the desired three-gate return
is complete. At the `2k2` frequency, the vertical direction splits as

    e3 = [z/(1+z^2)] a2 + [1/(1+z^2)] w2.                (3.5)

Thus the pollution is not intrinsically locked to the wrong polarization: it
already has a nonzero desired component, and (3.3) separates the two
components exactly.

For the physical wavevector

    K=2 b k2,                                             (3.6)

choose

    sigma=5 nu b^2.                                      (3.7)

Then (2.2) gives the exact rates

    desired:    +nu b^2,
    orthogonal: -9 nu b^2,                               (3.8)

so over a physical interval `t=tau/(nu b^2)`,

    desired multiplier = exp(tau),
    orthogonal multiplier = exp(-9 tau),
    relative purification = exp(-10 tau).                (3.9)

This is a genuine finite-time separation. It is stronger than an
instantaneous derivative sign and is unaffected by the closed-strain-loop
parallelogram identity because no inverse deformation is required for this
carrier.

## 4. Scale compatibility with a supercritical localized turnover

The purifier requires a strain magnitude of order

    sigma ~ nu/ell^2                                    (4.1)

when `b~ell^(-1)`. A localized turnover cell of velocity amplitude `A` and
size `ell` has its natural advective strain scale

    A/ell = Re * nu/ell^2,
    Re=A ell/nu.                                          (4.2)

Under the supercritical recurrence

    ell_(n+1)=ell_n/s,       A_(n+1)=g A_n,               (4.3)

its Reynolds number changes by

    Re_(n+1)/Re_n=g/s.                                    (4.4)

The turnover condition requires `g>s`; hence the available advective strain
in units of the viscous threshold (4.1) grows geometrically. There is therefore
**no scaling contradiction** between the supercritical turnover window and the
strain size required by the purifier. This is only a dimensional feasibility
statement: the correct signed strain geometry still has to be generated by
the same unforced solution.

The relevant physical purifier clock is parabolic,

    Delta t ~ ell^2/nu.                                  (4.5)

For a geometrically shrinking sequence `ell_n=ell_0 s^(-n)`, the sum of these
clocks is finite. Therefore a future turnover theorem does not need to realize
the purifier on the stricter advective clock `ell/A`; a uniform fixed multiple
of (4.5) is already compatible with finite-time accumulation. Again, this is a
consumer observation, not a construction of the stages.

## 5. Compact localization: exact initial germ, unresolved positive-time error

The infinite-energy defect of (1.3) can be removed at **time zero** without
changing its local velocity germ. For a trace-free linear field `L(x)=Sx`,

    curl[-(x cross L(x))/3]=L(x).                         (5.1)

Choose a smooth compact cutoff `chi` equal to one on an inner ball and set

    V=curl[-chi(x) (x cross Sx)/3].                       (5.2)

Then `V` is real, compactly supported and solenoidal and equals `Sx` on the
inner ball. Scaling

    V_b(x)=nu b V(bx)                                     (5.3)

produces a compact smooth strain packet of radius `O(b^(-1))`, velocity scale
`O(nu b)`, and gradient scale `O(nu b^2)`, exactly the purifier scaling.
Moreover

    ||V_b||_2^2 = nu^2 b^(-1) ||V||_2^2,                 (5.4)

so the **energy cost decreases with frequency**. The critical L3 size is scale
invariant, as expected.

However (5.2) is not an exact affine solution for positive time. Canonical
pressure is nonlocal and heat has infinite propagation. The repository's
remote-pressure theorem shows that the trace-free part of the initial pressure
Hessian at the center can be prescribed exactly without changing the local
velocity germ; this is useful for matching the affine initial acceleration,
but it does not provide a whole parabolic-time history. Spatial analyticity
also prevents a nonzero finite-energy solution from remaining exactly affine on
an open set at positive time.

Thus localization is now the load-bearing gap for this purifier route:

    exact finite-time affine purification
      -> compact exact initial affine germ
      -> ??? uniform positive-time localized shadowing on t~1/(nu b^2).

A proof of that shadowing, or a different finite-energy strain producer, is
needed before this mechanism can be inserted into the clean dyadic turnover.

## 6. Consequence for the current programme

The closed common-strain loop is dead, but affine filtering itself is not. The
strongest surviving architecture is now spatially non-affine/routed:

1. create selected children by an actual localized gate;
2. send different carrier families through different local strain histories;
3. purify their polarizations on the parabolic clock without moving their own
   target wavevectors;
4. recombine only the purified children for the next gate;
5. retain or damp inherited parents and the all-orders ladder in the complete
   flow.

Steps 2--4 are not proved. In particular there is no dispersion in the heat
operator that automatically separates co-located Fourier packets. A genuine
physical-space transport/routing theorem remains necessary.

## 7. Reproducibility

`research/check_mode_purifier.py` freezes the exact matrix (3.3), its spectrum,
the `e3` decomposition (3.5), and the finite-time rates (3.8)--(3.9). The
general theorem in Sections 1--2 is elementary Hilbert-frame algebra plus a
direct substitution into the full NS equation; the checker is a regression
certificate, not a PDE solver.

No full repository checkout, repository-wide verifier, manuscript build, Lean
build, finite-energy purifier, or independent mathematical audit is supplied
by this additive packet. NS-R3 remains unresolved and no unforced singularity
is claimed.
