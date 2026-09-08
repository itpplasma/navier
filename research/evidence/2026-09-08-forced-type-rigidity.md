# Forced-type rigidity: no unforced whole-space flow in the [OA] candidate class

Date: 2026-09-08. Frozen repository input:
`373bd3e0504df775434ad579607ded9481af624f`.
Status: AUTHOR PROOFS; independent mathematical audit PENDING for every
component, including the one new component of Section 2. No terminal,
canonical proof-graph, refinement-graph, manuscript, or formal promotion.
No claim of literature priority. This is PLAN item UEF's positive use of the
already-recorded obstructions, consolidated into one theorem, plus one new
quantitative component and an explicit statement of the surviving class.

## 0. Consumer, scope, and what is deliberately NOT claimed

Consumer: PLAN Section 4, gate UEF ("prove the strongest precise obstruction
to THAT proposed unforced conversion"), feeding the UE0/UE1 allocation in
PLAN Section 1a and Section 7. Nothing here supplies the input-only RF-q
producer of PLAN Section 1, extracts a hypothetical blowup, or certifies a
regenerative turnover. The reviewed positive consumer chain is untouched.

Not claimed, explicitly:

* No refutation of [OA] Theorem 1.1. Every theorem below is about the
  ORIGINAL UNFORCED equation of PLAN Section 1 with the canonical pressure.
  [OA]'s fields solve a FORCED equation with `f` in `C_c^infty(R3 x (0,inf))`
  and are outside the hypothesis class of every statement here.
* No arbitrary-data regularity. Theorem A excludes a class of hypothetical
  unforced flows; it says nothing about the flow from a generic Schwartz
  datum, and it does not close any of UE2, UE3, UE4.
* No independent audit. All proofs below are author proofs written in this
  run. The cited component theorems (Sections 1.4, 1.6) are themselves at
  AUTHOR-PROOF status with audits pending; assembling them does not raise
  their status, and Theorem A inherits the weakest link.
* No line-by-line validation of [OA]'s 165-page forced construction. Only the
  quoted statements were inspected (Section 4).

## 1. Forced-type rigidity

### 1.1 Standing solution class U(nu, t0, T)

Fix nu>0 and t0<T<=infinity. `U(nu,t0,T)` is the set of pairs (u,p) with:

* (S1) u real, divergence-free, smooth on R3 x [t0,T), and
       (u,p) solves the UNFORCED equation
       `dt u - nu Delta u + (u.grad)u + grad p = 0`, `div u = 0`,
       with the canonical whole-space pressure
       `p = sum_{i,j} R_i R_j (u_i u_j)` (PLAN Section 1);
* (S2) finite energy: `sup_{t0<=t<=T'} ||u(t)||_2 < infinity` for each T'<T;
* (S3) u in `C([t0,T']; H^s(R3))` for every s and every T'<T.

(S3) is a hypothesis, not a consequence of (S1)-(S2). It is automatic when
u(t,.) is smooth with a FIXED compact spatial support for all t, which is
exactly the situation of branch (C1) below; it is the regularity used by
Lemma 1 of `2026-09-08-unforced-support-and-pulse-audit.md`.

### 1.2 The hypothesis class C

(u,p) in `U(nu,t0,T)` belongs to C if at least one of the following holds.

**(C1) Fixed compact support at an interior time.** There are a compact
K in R3 and a time t in (t0,T) with `supp u(t,.) subset K`.
(The pressure support plays no role in the proof; it is recorded because
[OA]'s statement and Lean structure both assert it, Section 1.5.)

**(C2) Exact label separation with an absent late label.** There is a
decomposition, valid on some [s,t_*] with t0<=s<t_*<T,

    u = B + sum_gamma W_gamma,   M B = B,  M W_gamma = 0,
    div B = div W_gamma = 0,                                         (1.1)

where M is the normalized angular average about the z-axis of the unitary
rotation action `T_alpha v(x) = R_alpha v(R_alpha^{-1} x)`; the labels have
pairwise disjoint closed spacetime supports (smooth extension by zero, as in
`2026-09-08-autonomous-pulse-obstruction.md` Theorem 1); the sum is locally
finite in `C_t H^m ∩ C^1_t H^{m-2}`, m>=4; and some label gamma0 satisfies
`W_gamma0(s) = 0` while `W_gamma0(t_1) != 0` for some t_1 in (s,t_*].

**(C3) An exact [OA]-type patch.** There are a nonempty open set
Omega in R3 and a time t in (t0,T) with one of:
(a) `u(t,.) = 0` on Omega;
(b) `dz u(t,.) = 0` on Omega;
(c) `u(t,.)` is axisymmetric on Omega while `u(t,.)` is not globally
    axisymmetric.

### 1.3 Theorem A (forced-type rigidity)

**Theorem A.** Let nu>0 and (u,p) in `U(nu,t0,T)`.

(A1) If (C1) holds at time t, then `u(t,.) = 0`, hence `u = 0` and `p = 0`
     on R3 x [t,T). In particular no (u,p) in `U(nu,t0,T)` with
     `limsup_{t->T} ||u(t)||_infinity = infinity` satisfies (C1) at any
     interior time; and if (C1) holds for every t in (t0,T) then u vanishes
     identically on R3 x (t0,T).

(A2) If (C2) holds, then `W_gamma0 = 0` on all of [s,t_*], contradicting
     `W_gamma0(t_1) != 0`. Hence no (u,p) in `U(nu,t0,T)` admits a
     separated-label decomposition (1.1) in which some label is absent at an
     earlier time and present at a later time. Equivalently: separated labels
     cannot be born inside the unforced flow, however large the axisymmetric
     background B is and however its own dynamics evolve.

(A3) Under (C3)(a) or (C3)(b), `u(t,.) = 0`, hence `u = 0` on R3 x [t,T).
     Under (C3)(c) the hypothesis is self-contradictory: local axisymmetry on
     a nonempty open set forces global axisymmetry at that time.

Consequently the class C contains NO nonzero unforced whole-space solution
with a finite-time velocity blowup at T, and (C3)(c) is empty.

### 1.4 Proof of Theorem A, by cited component with hypotheses re-verified

Write [SUP] for `research/evidence/2026-09-08-unforced-support-and-pulse-audit.md`
and [AUT] for `research/evidence/2026-09-08-autonomous-pulse-obstruction.md`.

*Analyticity input.* [SUP] Section 1, Lemma 1: for a real divergence-free
classical finite-energy whole-space NS solution on (a,b) with fixed nu>0,
canonical unforced pressure, and `u in C_t H^s` on compact subintervals for
every s, `u(t,.)` is real analytic on all of R3 for every a<t<b. Hypotheses
checked: (S1) supplies the equation, viscosity, pressure representative and
divergence-freeness; (S2) supplies finite energy; (S3) supplies exactly the
`C_t H^s` premise the lemma names. The proof there restarts the mild equation
at a regular time c<t inside the SAME classical interval, which exists here
because (t0,T) is open and (S3) holds up to any T'<T.

*(A1).* Apply [SUP] Theorem 2(a): if u vanishes on a nonempty spatial open
set at a positive time of an unforced classical interval, then u is
identically zero at that time. Under (C1), `u(t,.)` vanishes on the nonempty
open set `R3 \ K`. Hence `u(t,.) = 0`. Forward uniqueness then gives u=0 on
[t,T): by the same `H^s` mild local well-posedness used in Lemma 1, whose
existence time is bounded below on bounded subsets of `H^s`, the set
`{t' in [t,T) : u(t',.) = 0}` is nonempty, open (a zero datum at t' forces u=0
on a short interval to the right of t', and u is continuous into `H^s`) and
closed in [t,T), hence equal to [t,T). The canonical pressure
`R_iR_j(u_iu_j)` then vanishes too. The blowup statement is
immediate. If (C1) holds at every interior time, apply this at each t.
No backward statement is asserted on [t0,t]: that would need a backward
uniqueness theorem, which is NOT invoked here.

*(A3).* (C3)(a) is [SUP] Theorem 2(a) verbatim. (C3)(b) is [SUP] Theorem
2(b): analyticity of each component of `dz u` plus the identity theorem on
connected R3 gives `dz u = 0` globally, and a z-independent `L^2(R3)` field
is zero by Fubini. (C3)(c) is [SUP] Theorem 2(c): the rotation generator
`D_rot u = (Jx.grad)u - Ju`, `Jx = (-x2,x1,0)`, has analytic components,
vanishes on Omega, hence vanishes everywhere; integrating along rotations
gives `u(R_theta x) = R_theta u(x)` for all theta. Then forward uniqueness
as in (A1) for the (a),(b) cases.

*(A2).* Apply [AUT] Theorem 1. Its hypotheses: classical finite-energy
solution of the possibly forced equation on [s,t_*] with nu>0 (supplied by
(S1) with f=0); decomposition (1.1) with M B=B, M W_gamma=0 and all fields
divergence-free (supplied by (C2)); regularity `C_t H^m ∩ C^1_t H^{m-2}`,
m>=4, with `f in C_t L^2` and the pressure gradient in the corresponding
class (supplied by (S1)+(S3)+(C2), with f=0); pairwise disjoint closed
spacetime supports including derivative supports, with smooth extension by
zero (supplied by (C2)). Its conclusion is the exact label identity

    (1/2) dt ||W_gamma||_2^2 + nu ||grad W_gamma||_2^2
       = - integral W_gamma . S(B) W_gamma + <P f, W_gamma>,          (1.2)

with `S(B) = (grad B + (grad B)^T)/2`. With f=0 and
`b(t) = ||S(B(t))||_{L^infinity, operator}` integrable on the compact
classical interval [s,t_*], (1.2) gives `E_gamma' <= 2 b E_gamma` and
`E_gamma0(s)=0`, hence `E_gamma0 = 0` on [s,t_*]. Note what (1.2) does NOT
require: no bound on b uniform up to T, no smallness, no fixed background,
no leading-order ansatz, and no locality of the pressure — the canonical
whole-space pressure drops out only through `div W_gamma = 0`.
QED (Theorem A).

Theorem A is an assembly; the only new mathematics in this note is Section 2.

### 1.5 Verification that [OA]'s asserted fields satisfy the branches

The point of this subsection is that C is not an artificial class: branch
(C1) is verbatim [OA]'s own candidate class, and branch (C3) is verbatim its
own exterior/core structure. [OA] = OpenAI, *Finite Time Blowup for
Navier-Stokes*, 165 pp., the owner-supplied PDF (Section 4 below).

**(C1) is [OA]'s candidate class.** [OA, Theorem 1.1, p.1] asserts, for every
nu>0, a force `f in C_c^infty(R3 x (0,infinity); R3)`, a compact `K subset R3`
and smooth u,p on `R3 x [0,1)` solving (1.1) of [OA] with `u(.,0)=0`,
"such that supp u(.,t) ∪ supp p(.,t) ⊂ K for every 0 <= t < 1",
`sup_{0<=t<1} ||u(t)||_{L^2(R3)} < infinity`, and
`limsup_{t↑1} ||u(t)||_{L^infinity(R3)} = infinity`. The support clause is
quoted verbatim from printed p.1.

The same class is the Lean predicate `CandidateProperties` of
`openai/NavierStokesAndEuler@8937a8f4`, audited in
`/home/ert/proj/navier-formal/docs/external-openai-audit.md` Sections 1.2 and
3.1. Its fields, at `NavierStokes/R3/ProblemStatement.lean:90-111`, are
`velocity_smooth`, `pressure_smooth`, `support_compact : IsCompact K`,
`velocity_support : ∀ t ∈ Ico 0 1, tsupport (fun x => u (t,x)) ⊆ K`,
`pressure_support : ∀ t ∈ Ico 0 1, tsupport (fun x => p (t,x)) ⊆ K`,
`force_smooth`, `force_support : CompactPositiveTimeSupport f`,
`zero_initial_velocity`, `divergence_free`,
`navier_stokes : ∀ t ∈ Ioo 0 1, ... residual ν u p t x = f (t,x)`,
`energy_bounded : UniformFiniteEnergy (Ico 0 1) u`, and
`speed_unbounded : SpeedUnboundedAtOne u`. The three clauses that matter for
(C1) are `velocity_support`, `divergence_free`, and `velocity_smooth`.

Hypothesis check for Theorem A(A1) on that field, IF its force were removed
on a terminal slab: (S1) would hold on (t_*,1) with `f=0` and the canonical
pressure reconstructed (PLAN Section 3: the trial pressure may be changed;
only the solenoidal residual `P f` matters); (S2) holds by
`energy_bounded`; (S3) holds because a smooth field with a FIXED compact
spatial support for all t<1 is in `C_t H^s` for every s on compact
subintervals of [0,1). (C1) holds at every t in (t_*,1) by
`velocity_support`. Theorem A(A1) then forces u=0 on that slab, contradicting
`speed_unbounded`. This is exactly [SUP] Corollary 3 and is recorded here as
the first branch of the consolidated theorem. It uses only [OA]'s STATED
support/regularity/blowup properties, not the correctness of its
construction, and it does not say `P f` is nonzero at every individual time.

**(C3)(b),(c) are [OA]'s stated exterior/core structure.** [OA, Theorem 3.1,
printed p.15, display (3.5)] states: "For X >= X_ext the residual is
identically zero, and

    A = 0,  B = K(r,tau),  p = - int_r^infty K(rho,tau)^2 / rho drho,
    K(r,tau) = r^{-1-2h} H_ext(tau / r^2)",

with `-dtau K = dr^2 K + r^{-1} dr K - r^{-2} K` and, by [OA, Theorem 3.1(i),
p.14], `u = curl A + B e_theta`. Hence on the open set
`{X > X_ext} ∩ Omega_*` (nonempty and open, Omega_* = {(x,t): tau>0, q<q_*})
the velocity is exactly `K(r,tau) e_theta`: axisymmetric and independent of
z, so `dz u = 0` there. [OA, Section 2.3, p.5] states the same in words:
"Beyond the annulus, the flow is purely azimuthal and independent of height
... We choose this outer flow to satisfy the radial heat equation for the
azimuthal velocity exactly, and call it the heat exterior. Its momentum
residual vanishes." Meanwhile [OA, Section 2.2, p.5] places the oscillatory
pulses in the annulus at the core edge, with "cylindrical velocity components
[having] zero angular average" - i.e. the field is NOT globally axisymmetric.
So the pair (exact heat exterior, nonaxisymmetric annulus) instantiates both
(C3)(b) and (C3)(c).

Theorem A(A3) therefore excludes any attempted unforced conversion that
PRESERVES those exact patches: an unforced whole-space solution cannot have a
z-independent open patch at all, and cannot have an exactly axisymmetric open
core together with a nonaxisymmetric annulus. It does not contradict [OA],
whose global field is forced; on the exterior patch [OA]'s own residual is
zero, but its residual is nonzero elsewhere, so the field is not a global
unforced solution and Theorem A does not apply to it.

**(C2) is [OA]'s label structure.** Recorded in [AUT] Section 2 from
[OA, Lemma 6.1 and (6.13), printed p.66] (different labels and their
derivatives have zero products, uniformly in theta, also after physical
evaluation of the auxiliary torus), [OA, Lemma 7.7] (velocities are actual
curls with smooth zero extension and nonzero angular harmonics),
[OA, Proposition 9.3, pp.104-105] (nonzero harmonics retain label, support
and envelope; angular means aggregate but stay axisymmetric),
[OA, Proposition 9.9] (cutoffs depend on q and preserve the support
structure), and [OA, (3.2)] giving `q - z^2 q^{2h} = T - t`, hence
`q >= T - t`. Consequently, for a band with support in `{q <= C 2^{-ell}}`,
at any fixed s<T all sufficiently large ell have `W_ell(s)=0`; Theorem A(A2)
then excludes retaining any such band as nonzero later. This is [AUT]
Corollary 1.2, recorded here as branch (C2).

Scope boundary, stated once: [OA]'s pulses are seeded by an explicit external
force - "An exponentially small external force seeds each pulse; the
background shear supplies its subsequent growth" [OA, Section 2.2, p.5] - so
(C2) is a statement about an attempted CONVERSION, never an objection to the
forced construction.

### 1.6 Audit status of each component of Theorem A

| Branch | Component used | File / statement | Status |
|---|---|---|---|
| A1, A3 | spatial analyticity | [SUP] Lemma 1 | AUTHOR PROOF; audit PENDING; classical prior art in substance (Giga, PRIMS 19 (1983) 887-910 cited there for context) |
| A1, A3 | patch rigidity | [SUP] Theorem 2(a),(b),(c) | AUTHOR PROOF; audit PENDING |
| A1 | terminal slab | [SUP] Corollary 3 | AUTHOR PROOF; audit PENDING |
| A2 | label energy identity | [AUT] Theorem 1, (1.2) | AUTHOR PROOF; audit PENDING |
| A2 | late-band vanishing | [AUT] Corollary 1.2 | AUTHOR PROOF; audit PENDING |
| 1.5 | [OA] statements | Theorem 1.1 p.1; Theorem 3.1 and (3.5) pp.14-15; Sections 2.2-2.3 p.5; Lemma 6.1/(6.13) p.66; Props 9.3, 9.9 | statement inspected 2026-09-08; NO proof audit |
| 1.5 | Lean `CandidateProperties` | `NavierStokes/R3/ProblemStatement.lean:90-111` | read directly; statement-faithfulness discussion in `navier-formal/docs/external-openai-audit.md` Sections 1.2, 3.1 |

## 2. New component: quantified no-start under controlled overlap

Theorem A(A2) is an all-or-nothing statement: EXACT separation plus a zero
late label gives an identically zero label. The obvious escape, named in
[AUT] Section 4 and PLAN Section 1a, is to allow overlap. This section
converts the qualitative no-start into a quantitative one with an explicit
cross-coupling parameter that vanishes exactly in the separated case, and
then states precisely where the resulting lower bound becomes useless.

Throughout, all norms and pairings are over the whole of R3.

### 2.1 Setting and the cross-coupling parameter

Fix nu>0 and a compact classical interval [s,t_1] inside an interval on which
u solves the possibly forced equation
`dt u - nu Delta u + (u.grad)u + grad p = f`, `div u = 0`,
with `u in C_t H^m ∩ C^1_t H^{m-2}`, m>=4, `f in C_t L^2`, and the pressure
gradient in the corresponding class. Suppose a decomposition (1.1) holds,
with M B = B, M W_gamma = 0 and all fields divergence-free, and with the sum
locally finite in those spaces and smoothly extended by zero from closed
spacetime supports. NO support disjointness is assumed.

Fix one label gamma and write

    W = W_gamma,   V = sum_{beta != gamma} W_beta,   u = B + W + V,
    A(t) = ||W(t)||_2,
    Omega(t) = supp W(t,.),   Sigma(t) = supp V(t,.),
    O(t) = Omega(t) ∩ Sigma(t)   (the OVERLAP set).                  (2.1)

Define the **other-label residual**

    g = dt V - nu Delta V + (B.grad)V + (V.grad)B + (V.grad)V,        (2.2)

i.e. the residual of V under the B-linearized operator plus its own
self-advection. Every term of (2.2) contains V or a derivative of V, so
`supp g(t,.) subset Sigma(t)`. Define the **cross-coupling parameter** and
the **overlap strain**

    kappa(t) = || g(t,.) ||_{L^2(O(t))},                             (2.3)
    sigma(t) = || S(V(t,.)) ||_{L^infinity(Omega(t)), operator},      (2.4)

with `S(V) = (grad V + (grad V)^T)/2`, and the background strain and force
terms

    b(t) = ||S(B(t,.))||_{L^infinity, operator},
    phi(t) = min( ||P f(t)||_2 , ||f(t)||_{L^2(Omega(t))} ).          (2.5)

Under exact separation, `O(t)` is empty and `S(V)` vanishes on `Omega(t)`, so
`kappa = sigma = 0` identically: the parameters degenerate correctly.

Finally assume a **spectral gap hypothesis**: a measurable `Lambda(t) >= 0`
with

    (H-Lambda)   ||grad W(t)||_2^2 >= Lambda(t) ||W(t)||_2^2 .        (2.6)

Three sufficient conditions, all exact:

* (L1) *Faber-Krahn.* If `|Omega(t)| < infinity`, then (2.6) holds with
  `Lambda = pi^2 (4 pi/3)^{2/3} |Omega(t)|^{-2/3}`, the Dirichlet ground-state
  eigenvalue of the ball of the same volume, applied componentwise via
  Polya-Szego rearrangement (classical; Lieb-Loss, *Analysis*, Thm. 7.17).
* (L2) *Angular.* If `W(t)` lies in the rotation modes `|n| >= N >= 2` in the
  sense of `2026-09-08-angular-preparation-obstruction.md` (1.1), and
  `Omega(t) subset {r <= R}`, then (2.6) holds with `Lambda = (N-1)^2/R^2`,
  by (1.3) of that note summed over modes (the weight `r^{-2}` is rotation
  invariant, so the modes stay orthogonal in it). The shift by one is
  essential and is the vector, not scalar, constant.
* (L3) *Fourier.* If the spatial Fourier transform of `W(t)` is supported in
  `{|xi| >= k}`, then (2.6) holds with `Lambda = k^2`.

We write `lambda(t) = nu Lambda(t)` and

    m(t) = b(t) + sigma(t) - lambda(t)                                (2.7)

for the **net rate**. All constants below are exactly the ones displayed; no
unnamed constant enters.

### 2.2 Lemma B (exact overlap label identity)

**Lemma B.** Under the hypotheses of Section 2.1, for a.e. t in [s,t_1],

    (1/2) d/dt A^2 + nu ||grad W||_2^2
      = - integral W . S(B) W - integral W . S(V) W
        - <g, W> + <P f, W>.                                          (2.8)

**Proof.** Pair the full equation with W and use `u = B + W + V`.

*Pressure.* `<grad p, W> = -<p, div W> = 0`, by `div W = 0` and decay in the
stated class; the actual nonlocal canonical pressure is used, not a local
substitute.

*Force.* `<f, W> = <P f, W>` since `div W = 0`.

*Background terms.* M is the average of the unitary rotation action, hence a
self-adjoint orthogonal `L^2` projection commuting with `dt`, `Delta` and the
Leray projector, and preserving divergence-freeness. `dt B` and `Delta B` are
axisymmetric, and `(B.grad)B` is axisymmetric because rotations commute with
Euclidean convection and `T_alpha B = B`. For any axisymmetric G,
`<G,W> = <M G, W> = <G, M W> = 0`. So all three background terms drop. This
needs NO support hypothesis.

*Nine convection terms.* Expanding `(u.grad)u`:
`<(B.grad)B, W> = 0` (above);
`<(B.grad)W, W> = 0` and `<(V.grad)W, W> = 0` by `div B = div V = 0` and
integration by parts of `div(a |W|^2/2)`;
`<(W.grad)W, W> = 0` likewise;
`<(W.grad)B, W> = integral W_i W_j dj B_i = integral W . S(B) W`, since the
symmetric tensor `W_i W_j` annihilates the antisymmetric part;
`<(W.grad)V, W> = integral W . S(V) W` by the same identity;
`<(B.grad)V, W>`, `<(V.grad)B, W>`, `<(V.grad)V, W>` are three of the five
terms of `g`.

*Time and viscous terms.* `<dt W, W> = (1/2) d/dt A^2`;
`-nu <Delta W, W> = nu ||grad W||_2^2`; `<dt V, W>` and `-nu <Delta V, W>`
are the remaining two terms of `g`. The second uses `V in H^2`, supplied by
m>=4, so that no `grad V . grad W` term with an uncontrolled `grad W` factor
is produced.

Collecting gives (2.8). QED.

Setting V=0 and f=0 in (2.8) returns exactly (1.2), i.e. [AUT] Theorem 1.

### 2.3 Theorem C (Gronwall bound with overlap)

**Theorem C.** Under the hypotheses of Section 2.1 and (2.6), for
`s <= t <= t_1`,

    A(t) <= exp( int_s^t m ) A(s)
            + int_s^t exp( int_a^t m ) [ kappa(a) + phi(a) ] da,      (2.9)

with m as in (2.7). In particular, for an unforced flow (f=0, so phi=0) with
`A(s)=0`,

    A(t) <= int_s^t exp( int_a^t m(r) dr ) kappa(a) da.               (2.10)

Every quantity in (2.9)-(2.10) is one of `b, sigma, lambda, kappa, phi`
defined in (2.3)-(2.5); there is no additional constant, and no dependence on
the number of labels, the size of B, the harmonic content of any label, or
the proximity of t to a singular endpoint. `int|m|` is finite on [s,t_1] by
the assumed regularity.

**Proof.** By Lemma B, (2.6) and Cauchy-Schwarz on `<g,W>` restricted to
`Omega(t)` (legitimate because `supp W(t,.) = Omega(t)`, so only
`g` on `O(t) = Omega ∩ Sigma` is seen) and on `<P f, W>`,

    (1/2) (A^2)' <= m A^2 + (kappa + phi) A.                          (2.11)

Regularize: `A_eps = (A^2 + eps^2)^{1/2}`, eps>0. Then
`A_eps' = (A^2)'/(2 A_eps)` and `A^2/A_eps = A_eps - eps^2/A_eps`, so from
(2.11), using `A <= A_eps` and `A_eps >= eps`,

    A_eps' <= m A_eps + (kappa + phi) + |m| eps.

Gronwall's inequality for this linear differential inequality gives

    A_eps(t) <= exp(int_s^t m) A_eps(s)
                + int_s^t exp(int_a^t m) [kappa + phi + |m| eps](a) da,

and letting eps -> 0 (dominated convergence, `int_s^{t_1}|m| < infinity`)
gives (2.9). QED.

**Corollary C1 (net-damped windows: an absolute integrated overlap cost).**
Suppose `lambda(t) >= b(t) + sigma(t)` for all t in [s,t_1], i.e. `m <= 0`.
If `A(s) = 0` and `A(t_1) = a_1 > 0`, then

    int_s^{t_1} [ kappa(a) + phi(a) ] da >= a_1 .                     (2.12)

For an unforced flow this reads `int_s^{t_1} kappa >= a_1`: the
time-integrated cross-coupling into the label, measured in `L^2` on the
overlap set only, is at least the amplitude to be produced. Proof: in (2.9)
the weights are <= 1. QED.

**Corollary C2 ([OA]-type rates: a pointwise lower bound).**
Write `tau = T - t`, `q = T - t_1`, and suppose on [s,t_1]

    b(t) + sigma(t) <= C_B tau^{-1-h},                                (2.13)
    lambda(t) >= beta q^{-h} tau^{-1},                                (2.14)

for constants `C_B >= 0`, `beta > 0`, `0 < h < 1`. (Realization: (2.13) is
hypothesis (2.1) of the angular-preparation note; (2.14) is (L2) with
`(N-1)^2 >= c_- q^{-h}` and `Omega(t) subset {r <= R sqrt(tau)}`, giving
`beta = nu c_- / R^2`.) Put `mu = (beta - C_B) q^{-h}`. If `beta > C_B` and
`mu > 1`, then for `A(s)=0`, `A(t_1) = a_1 > 0` and f=0,

    sup_{[s,t_1]} kappa >= a_1 (mu - 1) / q
                        = a_1 [ (beta - C_B) q^{-h} - 1 ] / q .       (2.15)

**Proof.** For `tau >= q`, `tau^{-h} <= q^{-h}`, so
`m <= tau^{-1}(C_B tau^{-h} - beta q^{-h}) <= -mu/tau`. Substituting
`t = T - tau` in the weight, `int_a^{t_1} m <= -mu log(tau_a/q)` where
`tau_a = T-a`, so `exp(int_a^{t_1} m) <= (q/tau_a)^mu`. Hence by (2.10),

    a_1 <= (sup kappa) int_q^{T-s} (q/tau)^mu dtau
        <= (sup kappa) q^mu int_q^infinity tau^{-mu} dtau
         = (sup kappa) q / (mu - 1),

using `mu > 1`. QED.

Corollaries C1 and C2 are complementary to Theorem 4 of the
angular-preparation note. That theorem lower-bounds the NORMALIZED work
`W_n^+ = int Re<G_n,v_n>/E_n`, which can be large while the absolute
interaction is exponentially small; (2.12) and (2.15) lower-bound the
ABSOLUTE `L^2` size of the seeding term on the overlap set. Neither implies
the other, and neither is an energy budget: `kappa` is not bounded by total
kinetic energy in any direction that would make these summable.

### 2.4 Where this proof stops: the net-growth barrier

The useful content of Theorem C is confined to windows with `m <= 0`. Where
`m > 0` the weight `exp(int_a^{t} m)` is large and (2.10) permits an
exponentially small `kappa` to produce an order-one label. This is not a
defect of the derivation; it is the full-PDE image of the exact amplitude
statements already recorded.

Concretely, in [OA]'s parameters the pulse dynamics are DESIGNED to sit in
the net-growth regime first: [OA, Section 2.2, p.6] states "We choose the
initial wavelength so that amplification dominates at first, but damping
overtakes it later." The homogeneous principal pulse of [SUP] Theorem 4 /
[AUT] Theorem 2 satisfies `|h_Q(v)| <= C exp(-c(v-L/2)^2/L)` with
`L ≍ S = ell^2`, `Q = 2^{-ell}`; its accumulated growth exponent over the
first half of the interval is therefore `Gamma ≍ c L/4 ≍ c ell^2/4`. Plugging
`Gamma` into (2.10) gives only

    sup kappa >= a_1 exp(-Gamma) / (t_1 - s)  ≍  a_1 exp(-c ell^2/4)/(t_1-s),

and `exp(-c ell^2/4) Q^{-N} -> 0` for every fixed N (the flatness computation
of [SUP] (2.3)). So:

**the cross-coupling required to give birth to a late [OA]-type label through
overlap is superalgebraically small in `Q`, and NO energy-type argument of
the shape (2.8) can exclude it.**

This is a sharp negative finding for the programme, not a gap to be repaired
by a better constant. It says the autonomous-overlap route survives Theorem
A, and that any future exclusion of it must control the SIGN or the
realizability of an exponentially small overlap term, not its size. It also
says the converse: the (C2) branch of Theorem A is exactly at the boundary of
what an `L^2` label identity can give, since removing the exact-zero
hypothesis costs all quantitative strength in the growth phase.

Two further honest limitations of Section 2:

* Corollary C2's hypothesis `beta > C_B` is a CONSTANT competition
  `nu c_-/R^2 > C_B` between viscous angular damping and mean strain at the
  same power `tau^{-1-h}`. Whether [OA]'s actual labels satisfy it is NOT
  determined here: it depends on unpublished constants, and it additionally
  requires nondegenerate pitch so that the azimuthal wavenumber `n = k p`
  is genuinely large (angular-preparation note Section 4; [OA] asserts only
  `n != 0` in general). Without `beta > C_B` the bound degrades to the
  crude `sup kappa >= a_1 exp(-int m^+)/(t_1-s)`.
* Lemma B and Theorem C require `V` to be a genuine part of the SAME
  solution, in the same regularity class, with the axisymmetric-mean
  splitting (1.1). They do not apply to a decomposition into pieces that are
  separately evolved or to an averaged operator.

### 2.5 Routes not taken, and the exact reason

The two alternative new components offered by the task were examined and
rejected before Section 2 was written; recording why is part of the result.

*Route (a): a quantitative version of (C1) (tail lower bound).* One would
want: if `||u(t)||_{L^2(|x|>R)} <= eps(t)` with eps small, the unforced
equation forces a lower bound on the tail. The natural attempt is Duhamel,
`u(t) = e^{nu(t-t0)Delta}u(t0) - int_{t0}^t e^{nu(t-a)Delta} P div(u⊗u)(a) da`,
and comparison of the two far fields. It fails at the first step, for a
reason that is structural rather than technical: the heat term's tail at
`|x| = R` decays like `exp(-R^2/(4 nu (t-t0)))`, whereas `e^{nu s Delta} P div` has an Oseen-type
kernel whose far field decays only polynomially in R: the Leray projector's
kernel is homogeneous of degree -3, so `P div` contributes order `|x|^{-4}`,
and for `|x| >> sqrt(nu s)` the heat factor does not improve this. Hence for large R the NONLINEAR/pressure
tail dominates the linear one at every fixed time, and no lower bound on the
total tail follows from a lower bound on the heat tail. A quantitative (C1)
therefore needs sign or cancellation information about the far-field Riesz
tail of `u ⊗ u`, which we do not have. We state this as the stopping point
and assert no partial result; in particular we do NOT claim any quantitative
strengthening of [SUP] Theorem 2(a).

*Route (b): a lower bound on `||P f||` from the leading self-similar profile
alone.* [OA]'s own core scales are explicit - `ell_r ≍ tau^{1/2}`,
`ell_z ≍ tau^{1/2-h}`, `0<h<1/100`, `ell_r/ell_z ≍ tau^h`, core volume
`≍ tau^{3/2-h}`, `|u_theta^{(0)}|,|u_z^{(0)}| ≍ tau^{-1/2-h}`,
`|u_r^{(0)}| = O(tau^{-1/2})`, core kinetic energy `≍ tau^{1/2-3h}`
[OA, Section 2.1, printed p.4], with `E_core ≍ tau^{1/2-3h}`,
`D_core ≍ tau^{-1/2-3h}` [OA, p.16] - and [OA, Section 2.2, p.5] states
directly that "The external force needed to sustain the background becomes
unbounded as t ↑ 1". A projected-residual lower bound for the background
ALONE is therefore already asserted by the source in words. Turning it into
our own theorem requires the actual profile equations of [OA, Proposition 5.5,
(5.41)], which were not inspected in this run; producing a number from the
scales alone would be dimensional analysis, not a proof. Not attempted.

## 3. What Theorem A and Theorem C do and do not imply

**Do not imply: arbitrary-data regularity.** Theorem A excludes a class of
hypothetical unforced solutions defined by support/patch/label properties.
The unknown critical quantity of PLAN Section 1 is untouched, no input-only
producer is supplied, and `RF-q`, `RF-LQ-CONTINUATION`, `hyp:critical`,
`hyp:absorption`, `hyp:highpressure` gain nothing. Theorem A gives no
information about the flow from a generic nonzero Schwartz datum.

**Do not imply: any refutation of [OA].** [OA]'s asserted fields solve the
FORCED equation. They fail (S1). The forced-insensitivity test of
`research/evidence/2026-09-08-forced-insensitivity-falsifier.md` Section 1
applies in the safe direction: Theorem A's proof uses `f = 0` in two
irreducible places - the vanishing of `P f` in the label identity (1.2), and
the identification of the field as a global unforced classical solution
needed for the analyticity Lemma 1 - so Theorem A is NOT forced-insensitive
and is not at risk from [OA] Theorem 1.1 being correct. Symmetrically, this
means Theorem A gives no information about the forced case.

**Do not imply: an unforced counterexample is impossible.** Theorem A is a
statement about three specific architectures. It is not a no-blowup theorem,
and PLAN's `unforced_counterexample: not-constructed` and
`terminal_status: not-proved` are unchanged.

**Do imply: the following UE1 initializations are excluded**, each in its
exact stated scope, with AUTHOR-PROOF status and audits pending:

* U-1: keep [OA]'s localized velocity and reinterpret its force as pressure
  on a terminal slab. Excluded by Theorem A(A1) ([SUP] Corollary 3).
* U-2: any conversion whose velocity has fixed compact spatial support at one
  interior time. Excluded by Theorem A(A1).
* U-3: any conversion preserving the exact heat-exterior patch (z-independent
  open set) or an exactly axisymmetric open core coexisting with a
  nonaxisymmetric annulus. Excluded by Theorem A(A3).
* U-4: exact label separation with zero late-label initial data and a nonzero
  late label. Excluded by Theorem A(A2).
* U-5: cancelling the principal seed residual `psi' h_Q` with the SAME
  zero-initial-value causal inverse while keeping the pulse. Excluded by
  [SUP] Corollary 5 / [AUT] Theorem 2 (amplitude equation only).
* U-6: homogeneous preloading of the high-angular, substantially
  column-trapped family from one finite-energy datum. Excluded by
  `2026-09-08-angular-preparation-obstruction.md` Corollary 2.
* U-7: repairing U-6 solely by lowering the carrier in an otherwise fixed
  bounded phase geometry while preserving a two-sided Gaussian pulse.
  Excluded by that note's Lemma 6 and identity (4.4).
* U-8 (NEW, this note): a decomposition (1.1) with overlap in which the
  entire preparation window of a late label is NET DAMPED
  (`lambda >= b + sigma`) and the integrated cross-coupling satisfies
  `int kappa < a_1`. Excluded by Corollary C1. Under the [OA]-type rates
  (2.13)-(2.14) with `beta > C_B`, additionally excluded whenever
  `sup kappa < a_1[(beta - C_B)q^{-h} - 1]/q` (Corollary C2).

**The exact remaining admissible class.** After Theorem A and Theorem C, an
unforced conversion must satisfy ALL of the following simultaneously; nothing
below is excluded by any result in this repository:

1. *Everywhere-nonzero analytic leakage.* At every interior time, `u(t,.)` is
   real analytic and vanishes on no nonempty open set, has no z-independent
   open patch, and has no exactly axisymmetric open patch unless it is
   globally axisymmetric. The exterior and core patches of the [OA] design
   must be perturbed by a nonzero, possibly superalgebraically small, leak.
   No lower bound on that leak is proved (Section 2.5, route (a)).
2. *Overlapping, not separated, labels.* Either no decomposition (1.1) with
   disjoint supports exists, or every late label is already nonzero at t0
   (continuous preload). In the overlapping case the cross-coupling `kappa`
   of (2.3) must be nonzero on a set of positive measure and must satisfy
   Corollary C1/C2 on every net-damped window. During net-growth windows
   `kappa` may be superalgebraically small in `Q` (Section 2.4) - this is the
   open door.
3. *Either radial escape or large normalized nonlinear supply.* By
   `2026-09-08-angular-preparation-obstruction.md` Corollary 3 and Theorem 4,
   a high-angular family with the stated frequency/size class must either
   spend almost all of its logarithmic preparation time outside the shrinking
   column, or receive normalized nonlinear work at least
   `c_* q^{-h} log(tau0/q)`.
4. *One Cauchy datum realizing all traces simultaneously.* Free-trace filling
   repairs each principal pulse on its own interval with a flat correction
   ([SUP] Proposition 6, (2.4)-(2.7)), and
   `2026-09-08-mixed-trace-principal-inverse.md` gives a logarithmic-loss
   principal inverse after changing the trace constraints. Their simultaneous
   realization by ONE whole-space Schwartz datum, with the inherited exterior
   and full nonlinear feedback, remains unproved and is the first missing
   theorem.
5. *And then UE2, UE3, UE4 unchanged:* exact zero solenoidal residual on
   [t0,T) x R3, one nonzero Schwartz datum with canonical pressure, and a
   preserved singularity with finite maximal lifespan. None of these arrows
   is filled here.

In one sentence: what survives is a continuously preloaded, overlapping,
everywhere-leaking autonomous cascade whose new labels are seeded by an
exponentially small but nonzero cross-coupling during their net-growth
windows - and the reason it survives is exactly the exponential weight in
(2.10), which no `L^2` identity of the form (2.8) can improve.

## 4. Sources, verification scope, and the checker

[OA] OpenAI, *Finite Time Blowup for Navier-Stokes*, 165 pp., the
owner-supplied PDF accessed 2026-09-08 at
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Directly inspected in THIS run, as text through the PDF tool: printed pages
1-6 (Theorem 1.1 and its support clause; historical context; Sections 2.1-2.3
core scales, pulses, heat exterior; Section 3 residual definition and the
viscosity rescaling `u_nu(x,t) = sqrt(nu) u(x/sqrt(nu), t)`) and printed pages
14-16 (Theorem 3.1(i)-(iv), (3.4), (3.5), Figure 6, Section 3.5 localization
and completion, the core energy/dissipation scales, and the Lemma 10.5
uniqueness step). Statements from pp.63-67, 73-87, 101-116 are carried over
from [AUT] and [SUP] and were NOT re-inspected here. This is not a proof
audit of [OA] and no third-party PDF is stored in this repository.

[OA-LEAN] `openai/NavierStokesAndEuler`, commit
`8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`, Apache-2.0. Read directly:
`NavierStokes/R3/ProblemStatement.lean` lines 60-175 (`CandidateProperties`,
`GlobalFiniteEnergySolution`, `candidateStatement`, `coreBreakdownStatement`,
`breakdownStatement`). Prior statement-faithfulness analysis:
`/home/ert/proj/navier-formal/docs/external-openai-audit.md` Sections 1.1,
1.2, 3.1, including the finding recorded there that `breakdownStatement` and
`coreBreakdownStatement` are never proved in that repository and that the
exported Comparator theorems are the weaker existential form. Nothing here
imports or promotes any Lean statement.

Repository inputs, all AUTHOR-PROOF with independent audit PENDING:
`research/evidence/2026-09-08-unforced-support-and-pulse-audit.md`,
`research/evidence/2026-09-08-autonomous-pulse-obstruction.md`,
`research/evidence/2026-09-08-angular-preparation-obstruction.md`,
`research/evidence/2026-09-08-forced-insensitivity-falsifier.md`,
`research/evidence/2026-09-08-mixed-trace-principal-inverse.md`,
PLAN Sections 1, 1a, 2, 3, 4 (UE0-UEF), 5, 8.1.

The accompanying checker `research/check_forced_type_rigidity.py` verifies,
by exact symbolic and rational algebra only: the full nine-term convection
expansion and the exact divergence-form identity underlying Lemma B; the
degeneration `g = 0` when V = 0; the strain identity
`W_i W_j dj V_i = W . S(V) W`; the pressure pairing identity; the exact
angular derivative formula and the eigenvalues `(n-1)^2`, `(n+1)^2`, `n^2`
behind (L2); the Faber-Krahn constant `pi^2 (4 pi/3)^{2/3}` in (L1); the
regularization identity `A^2/A_eps = A_eps - eps^2/A_eps` used in Theorem C;
the weight comparison `m <= -mu/tau` and the exact integral
`int_q^infinity (q/tau)^mu dtau = q/(mu-1)` used in Corollary C2; and the
superalgebraic-flatness comparison `exp(-c ell^2/4) Q^{-N} -> 0` used in
Section 2.4. It prints PASS/FAIL counts. It certifies NO continuum argument,
no function-space hypothesis, no property of [OA]'s construction, and no
independent review.
