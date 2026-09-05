# Whole-space proof dossier

The mathematical target is Clay alternative A for the original unforced
three-dimensional equation on R3. The manuscript is a conditional argument.
It does not prove the arbitrary-data estimate needed to settle the problem.

## Classical identities

For a maximal smooth solution with viscosity nu and Schwartz divergence-free
datum, let E be squared L2 velocity and Y squared L2 gradient. On compact
classical intervals, integration by parts gives

```text
E(t) + 2 nu integral_0^t Y(s) ds = E(0).
Y'(t) <= C nu^(-3) Y(t)^3.
integral_0^T ||u(t)||_3^4 dt <= C E(0)^2 / nu.
```

The manuscript proves these estimates. Neither the time integral nor the
cubic differential inequality supplies an arbitrary-data continuation bound.
The function y(t) = [2C(T-t)]^(-1/2) has finite time integral, obeys y'=Cy^3,
and diverges at T. This is an obstruction to that scalar inference, not a
Navier–Stokes singular solution.

## Pressure route

Define X3 = integral |u|^3, D3 = integral (|u||grad u|^2 +
|u||grad |u||^2), and P3 = integral p u dot grad |u|. With pressure
p = sum R_i R_j(u_i u_j), testing against |u|u gives

```text
(1/3) X3' + nu D3 = P3.
```

The first proposed new producer is signed pressure absorption: for each
finite horizon H and admissible datum, bound accumulated P3 by theta nu times
accumulated D3 plus a finite a priori A(nu,u0,H), uniformly in all
tau < min(H,Tstar), with theta < 1. The bound must be obtained without the
unknown trajectory norm it is supposed to control. Integrating the identity
then bounds X3 and weighted dissipation on the same interval.

The frequency reduction now narrows that producer further. Fix a real-even
smooth low-pass cutoff S_J. Its composition with the pressure Riesz multiplier
has a frequency L1 norm bounded by C 2^(3J), so its spatial kernel is bounded.
The resulting estimate is

```text
|integral_0^tau (S_J p) u dot grad |u| dt|
    <= C 2^(3J) ||u0||_2^4 sqrt(H/(2 nu)).
```

This follows from energy and Cauchy–Schwarz and is uniform for
tau < min(H,Tstar). Thus only the signed high-output pressure contribution
needs a new absorption estimate. The cutoff J must be finite and chosen from
input data; convergence of high tails at each fixed regular time does not
give uniform control through a putative singular endpoint.

The endpoint theorem of Escauriaza–Seregin–Šverák, in the maximal L3 solution
form of Gallagher–Koch–Planchon Theorem 4, rules out a finite Tstar when the
L3 norm is uniformly bounded. Taking any finite H>Tstar in the universally quantified
finite-horizon estimate gives the contradiction. Local uniqueness,
persistence of regularity, and the energy identity yield the conditional
Clay conclusion. The periodic alternative is not a consequence of this
whole-space argument.

## Other analytic routes

| Route | Established evidence | Missing input |
| --- | --- | --- |
| Stretching absorption | Cubic bound and a valid scale-invariant small-data bootstrap | Large-data depletion with integrable coefficient through the putative endpoint |
| Ancient solutions | Exact rescaling and conditional normalized ancient-limit construction | Bounds or rigidity for the actual extracted class; energy rescaling alone supplies neither |
| Critical pressure | Exact cubic balance and absorption consumer | Signed integrated pressure estimate for arbitrary data |
| Frequency splitting | Explicit energy bound for low-output pressure work | Signed high-output absorption uniform through the endpoint |

Detailed calculations are in `research/evidence/`. These are different
questions, not additional prerequisites that must all be solved. The
dependency graph records only the selected pressure route and diagnostic
claims. Review records identify immutable inputs and their exact scope.

## Formalization boundary

No Lean implementation is present. Phase I would prove every project-owned
paper step down to exact verified literature results; it cannot declare
pressure absorption a published theorem. A formal conditional implication
would remain conditional. Phase II would discharge the imported results
from Mathlib. The user has reserved the Phase I kickoff.


## Reviewed quotient alternative (HF17 checkpoint)

The cubic distance Q(u)=inf_{q in G3} ||u+q||_3^3/3, where G3 is the
closed L3 gradient space, is comparable to the critical norm on solenoidal
fields. Its derivative annihilates pressure gradients and heat is
nonincreasing. With w=u+q and A=|w|w, the evolution is
Q'+nu D_Q=-integral q dot ((A dot grad)u), where D_Q=-DQ(u)[Delta u]>=0.
The low strain is bounded by an input coefficient times Q. The remaining
high-strain spacetime estimate is unproved. See the HF17 functional and
evolution notes and their independent reviews. This is an alternative
producer, not a proof of HIGH-PRESSURE or a new dependency of the Clay claim.
