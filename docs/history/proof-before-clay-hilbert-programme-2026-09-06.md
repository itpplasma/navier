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
|(grad u)^T u|^2/|u|), and P3 = integral p u dot (grad u)^T u/|u|, with
integrands zero where u vanishes; off the zero set these are the classical
|u||grad|u||^2 and p u dot grad|u|. With pressure
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

The continuation theorem is proved as follows. The local theory package
(Tao Theorem 5.4, Corollaries 5.8 and 4.3, and a manuscript-owned gluing
lemma) gives the maximal classical branch with all Sobolev norms continuous
in time on compact intervals and enstrophy blow-up at a finite maximal time.
Its unit-viscosity rescaling is a Leray–Hopf weak solution in the exact
sense of Escauriaza–Seregin–Šverák on every finite space-time cylinder. If
the L3 norm stayed bounded up to a finite maximal time, their Theorem 1.3
would place the solution in L5 of space-time, and a manuscript-owned
Serrin-type Gronwall estimate would keep the enstrophy bounded, contradicting
the blow-up alternative. Hence a finite maximal time forces an unbounded L3
norm. Taking any finite H>Tstar in the universally quantified finite-horizon
estimate gives the contradiction, and the package plus the energy identity
yield the conditional Clay conclusion. No uniqueness theorem for L3 mild
solutions is imported; Gallagher–Koch–Planchon Theorem 4 is corroboration.
The periodic alternative is not a consequence of this whole-space argument.

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

Both Lean phases were authorized on 2026-09-05 for checkpoint CP1, in the
order paper proof, Phase I, Phase II (see `PLAN.md`). The private repository
`itpplasma/navier-formal` holds the Palomar-shaped development; at this
writing it contains supporting lemmas with standard axioms only (the scalar
obstruction, dilation scaling, the interpolation-mismatch witness, and the
regularisation calculus of the pressure balance). Phase I proves every
project-owned paper step down to exact verified literature results (Tao
Theorem 5.4 and Corollary 5.8, Escauriaza–Seregin–Šverák Theorem 1.3); it
cannot declare pressure absorption a published theorem, and a formal
conditional implication remains conditional. Phase II discharges the
imported results from Mathlib.


## Reviewed quotient alternative (HF17 checkpoint)

The cubic distance Q(u)=inf_{q in G3} ||u+q||_3^3/3, where G3 is the
closed L3 gradient space, is comparable to the critical norm on solenoidal
fields. Its derivative annihilates pressure gradients and heat is
nonincreasing. With w=u+q and A=|w|w, the evolution is
Q'+nu D_Q=-integral q dot ((A dot grad)u), where D_Q=-DQ(u)[Delta u]>=0.
The low strain is bounded by an input coefficient times Q. The audited HF18
note identifies D_Q with the coercive weighted cubic dissipation of the
representative, D_Q = integral (|grad V|^2 - |grad |V||^2/9) with
V = |w|^{1/2} w in H1, and bounds the transport term by C Q^{1/3} D_Q, which
closes only under critical smallness. The remaining high-strain spacetime
estimate is unproved. See the HF17 functional and
evolution notes and their independent reviews. This is an alternative
producer, not a proof of HIGH-PRESSURE or a new dependency of the Clay claim.


## Dissipation-clock continuation component (2026-09-06; review pending)


The main manuscript now includes `sections/dissipation_clock.tex`, with full
derivations of the direct estimates

```text
||u||_9^3 <= (9 S^2/8) D3,
Y'+nu Z <= (4 S^3/(3 nu^2)) D3 Y,
Y(t)+nu integral_0^t Z <= Y0 exp(4 S^3 B(t)/(3 nu^2)),
B(t)=integral_0^t D3.
```

Thus a finite B budget gives continuation without an endpoint theorem. Under
the existing strict signed pressure absorption, the bound is
`B <= (X0+3A)/(3(1-theta)nu)`. The resulting direct exponent is
`4 S^3 (X0+3A)/(9(1-theta)nu^3)`. This alternative suffix does not require
ESS or quotient-minimizer regularity. The separately stated bare-L3 endpoint
theorem retains its original dependency.

A single first-crossing pressure barrier also suffices. More generally,
`integral Q_J <= nu B-Phi(B)+A_high` prevents crossing any finite b with
`Phi(b)>X0/3+A_high+L_J(H)`. A logarithmic Phi is enough despite a vanishing
fractional absorption margin. The source proves the endpoint-uniform
first-crossing argument and a scalar boundary example, with their exact
scope. These sharpenings are author-checked and await independent audit;
the graph lists a separate pending supplement, not a promoted theorem.

The missing arbitrary-data pressure estimate is still missing. Absolute
pressure estimates produce only a B-to-the-three-halves upper bound. No
choice of Phi, existence of a certificate in the already-regular case, or
successful build provides a noncircular producer. See the dated evidence
note for the derivations, failed inference, and review questions.

## Defect interval and quotient clock (2026-09-06; review pending)

The component `sections/defect_extensions.tex` in the manuscript proves:

    d = -(3/4)(n tensor n-I/3):(T d + grad u),
    ||K_n||_(2->2) <= 1/2,
    ||sigma||_r <= A_r ||grad u||_r       (r in a fixed interval around 2),
    Y'+nu Z <= (4 S^3 C9^3/(3 nu^2)) D_Q Y.

The Neumann construction is simultaneous in L2 and Lr, so membership of the
unknown defect in Lr is proved rather than assumed. Neither derivatives of
n nor an all-exponent weighted Calderon-Zygmund theorem are used.

With `Astar=8 S^3 C9^3 Q0/(3 nu^3)` and the already defined
`Lambda_sigma=C_sigma nu^-3 integral ||sigma||_2^4`, the exact suffix is

    integral_0^t Y^2 <= (E0 Y0/(2 nu)) exp(Astar exp(Lambda_sigma(t))),
    integral_0^t ||sigma||_2^4 <= (1/16) integral_0^t Y^2.

Hence the two integral finiteness conditions cannot separate on an actual
selected branch, even at its full lifespan. The old undecided statement is
superseded by this author-checked proof, pending independent audit. The
suffix is nonendpoint and requires no comparison of the two dissipations.

These results still do not supply an arbitrary-data fourth-power bound.
The first is spatial and the second places the unknown fourth-power integral
on its right side. No gap is promoted. The complete proof, precise extra
integrability hypothesis, source attribution and review questions are indexed
in `research/evidence/2026-09-06-defect-extensions.md`.


## Conformal inversion and spatial moments (2026-09-06; review pending)

The main manuscript component `sections/conformal_moment.tex` proves that
conformal inversion of one-forms is an isometry of the cubic gradient
quotient: `w(Ku)=K w(u)`. Applying the accepted div-curl theorem to `P K u`
and then Hardy answers the finite-energy representative and L^(3/2) defect
questions when `|x| grad u in L2`. With `A=|| |x| grad u ||2`, `U=||u||2`,
`F=sqrt(5)(A+2sqrt(3)U)/2` and `c1=1+4sqrt(3)`, the derived bounds are

    ||w||2 <= 2F,              ||q||2 <= 2F+U,
    || |x| grad w ||2 <= c1F,  || |x|sigma ||2 <= c1F/sqrt(3),
    ||sigma||_(3/2) <= 2^(2/3)(4pi/3)^(1/6) (||sigma||2 || |x|sigma ||2)^(1/2).

Inversion is not a solenoidality-preserving or NS-preserving operation.
The projection, cutoff density, weak derivative at the puncture and
noncircular Hardy argument are all explicit in the source.

On the original Schwartz-data branch the weight is not assumed to persist:
testing with bounded approximations to |x|^2 proves
`M(t)+2nu integral W <= L_H^2` uniformly below min(H,Tstar), where
`M=|| |x|u ||2^2`, `W=|| |x|grad u ||2^2` and L_H is explicit in initial
energy, initial moment, horizon and viscosity. A separate compact-interval
estimate makes W finite at every classical time. This yields input-only
integrals of `||w||2^2`, `|| |x|sigma ||2^2` and `||sigma||_(3/2)^2`.

These full component derivations are independently unaudited. They resolve
the spatial questions for weighted data and for this branch, not for every
bare H1 field. Their defect time-space pair (2,3/2) is supercritical and
does not supply the critical fourth-power time bound. The source gives an
energy-exact, self-similar non-solution curve demonstrating that the new
finiteness statements alone do not imply it. No open producer is promoted.
See `research/evidence/2026-09-06-conformal-moment.md` for the frozen source,
constants, primary-source attribution and independent-review obligations.


## Signed defect and one-sided form clock (2026-09-06; review pending)

The new manuscript section `sections/signed_defect.tex` proves, without
assuming moments or finite L2 energy of the representative,

    integral sigma |w|^3 = 0,
    K = -integral V^T S(u) V = integral V^T B0 V,
    |K| <= (2/3) ||sigma||2 ||w||6^3,
    Q' + (nu/2) D_Q <= a0^3 ||sigma||2^4 Q/(2 nu^3),
    B0=(R_i R_j sigma)+sigma I/3,  a0=9 C_S^2/8.

The cutoff identity, zero-set chain rule and trace-free constants are
written in full. This improves the old coefficient, not its fourth-power
time exponent. The old audited inequality is preserved as such.

A measurable nonnegative rate b_nu is defined by the positive Rayleigh
supremum of B0 minus `(4 nu/9)` times the Dirichlet form. One has

    Q(t)+(nu/2) integral_0^t D_Q <= Q0 exp(3 integral_0^t b_nu),
    integral_0^t ||sigma||2^4
      <= E0 Y0/(32 nu) exp(Astar exp(3 integral_0^t b_nu)),
    Astar=8 C_S^3 C9^3 Q0/(3 nu^3).

The second inequality uses the separately review-pending quotient clock
and the accepted energy identity. An explicit L^(3/2)-small amplitude-tail
certificate bounds b_nu from above. The clocks scale critically; their
local finiteness is not a bound at a putative maximal time.

The missing arbitrary-data producer is still missing. Its sharpened target
is an input-only finite bound on the accumulated signed form rate. The
available `b_nu <= a0^3 ||sigma||2^4/(6 nu^3)` cannot supply it because
the integral on its right is the original unknown. All graph node kinds
remain unchanged. See `research/evidence/2026-09-06-signed-defect.md` for
frozen hashes, primary-source distinctions, the scalar-budget diagnostic,
mechanical-check scope and required independent mathematical audit.


## Speed-shell cancellation and effective defect (2026-09-06; audit pending)

The new source `sections/speed_shell.tex` proves
`integral_{|w|>k} sigma=0` for every k>0, with an L^(3/2) flux cutoff and
no finite-energy assumption on w. Thus sigma annihilates every L2 function
of speed. Projecting the scalar signed-work field chi off the closed speed
subspace gives a measurable factor delta in [0,1] and
`|K| <= (2/3) delta ||sigma||2 ||w||6^3`. Finite speed-shell averages
bound the residual, converging under nested refinement.

Speed-dependent scalar corrections `h(|w|)sigma I` leave the signed work
unchanged. Their countable form-rate infimum beta satisfies
`0<=beta<=b_nu(B0)`. With
`c_nu=min(3 beta, a0^3 delta^4 ||sigma||2^4/(2 nu^3))` and `L_c=integral c_nu`,

    Q(t)+nu/2 integral D <= Q0 exp(L_c(t)),
    integral ||sigma||2^4 <= E0 Y0/(32 nu) exp(Astar exp(L_c(t))).

The last implication retains the pending quotient-clock dependency.
The bound on L_c from arbitrary initial data is NOT proved; delta<=1 only
returns the old unknown fourth-power integral. No temporal derivative of
the moving speed projection is assumed. Full proofs, cutoff and
measurability details, and the stopping point are in the source.
These are author-checked components, not an independent audit or promotion
of any open claim. The paper target `make check-shell` is a finite algebra/source regression.

Evidence: `research/evidence/2026-09-06-speed-shell.md`.


## Natural-variable time regularity and regularized shell dynamics

The pending component `sections/shell_dynamics.tex` proves

    ||V1-V0||2^2 <= (9/8) integral (|w0|+|w1|)|f1-f0+g|^2

for every admissible gradient g. Thus on compact classical intervals
V=|w|^(1/2)w is W^(1,infinity) into L2, and choosing the time-integrated
pressure gradient gives

    ||V_t||2^2 <= (9/4) integral |w| |nu Delta u-(u dot grad)u|^2.

For finite smooth features phij=gj(|w|), Gram matrix G, moment vector b,
and eta>0, the residual
`R=||chi||2^2-b^T(G+eta I)^(-1)b` is absolutely continuous and retains
`|K|<=||sigma||2 sqrt(R)`. With `a=(G+eta I)^(-1)b` and
`r=chi-sum aj phij`, its exact evolution is

    R'=2<r,chi_t>-2<r,sum aj phij,t>.

The source supplies the dual-space justifications and a full bound for
this derivative. It unblocks a finite regularized temporal calculation,
not differentiation of the sharp moving projection. Refining features and
letting eta decrease gives the exact shell residual at each fixed time,
but the derivative estimates are not uniform in that limit or at Tstar.
The missing arbitrary-data estimate on L_c or integral ||sigma||2^4 is
therefore unchanged. See `research/evidence/2026-09-06-shell-dynamics.md`.
These are author-checked derivations awaiting independent audit; no existing
graph node or formal claim is promoted.

## Strong material response (2026-09-06; audit pending)

The new source `sections/material_response.tex` in `navier-paper`, frozen at
`2959003806907fa4742518bff741f24c592921e6`, proves a strong moving-metric
response for the cubic gradient minimizer. A cubic little-o remainder, not
just the earlier big-O estimate, justifies the natural-variable derivative
in L2 including velocity zeros. No unweighted L3 derivative of w is assumed.

Pullback by the actual volume-preserving flow gives, with N=DJ(w),
P the fixed weighted gradient projection, L=I-P and S the velocity strain,

    U=(partial_t+u dot grad)V-Omega V
      =N[L(nu Delta u-Sw)+P(I-n tensor n/2)Sw].

The two weighted responses are orthogonal and their squared action obeys
`action <= ||U||2^2 <= 9 action/8`. Its explicit upper bound is
`(9/2)nu^2 integral rho|Delta u|^2 +(81/16) integral rho^3 ||S||op^2`.
This removes pressure, bulk transport and rigid rotation from the driver,
not strain or diffusion. The material finite-ridge residual equation keeps
the complete Riesz/rotation commutator and its correct dual-space pairing.
The accepted quotient balance is recovered exactly as a consistency check.

The endpoint bound is still unproved. Weighted acceleration, strain action,
the full commutator and uniform refinement losses are not controlled by
the available energy/moment budgets. Differentiating dissipation did not
establish the signed estimate needed to pay for this action. No heat
convexity or differentiation of a moving weighted projection is assumed.
See `research/evidence/2026-09-06-material-response.md` for the complete
source trail, attempted closure, author checks and independent-audit list.
This and predecessor supplements remain independently unaudited. No main
graph node or formal status is promoted; NS-R3, HIGH-PRESSURE, HIGH-STRAIN
and DEFECT-L4 remain open.
