# Actual-pulse adjoint: entry seeds, mean stress, and gluing impulses

Date: 2026-09-10. Repository input:
`itpplasma/navier@f49078bf4af66bd58c04373ae47af928e32cad5e`.

**Author derivations; independent mathematical audit pending.** The results
below concern the primary pulse system actually used in the source, its
covariance, and a precisely specified attempt to glue the resulting fields.
They do not construct an unforced NS solution. The adjoint of the complete
physical NS evolution through the entire history has **not** been computed.
No canonical claim, formal status, or terminal result is promoted.

## 0. The attempt and its outcome

The preceding note constructed a generic adjoint test but did not evaluate
it on a source pulse. This note performs that evaluation, retaining the
actual two-component principal matrix rather than substituting an arbitrary
scalar flat-source counterexample. It then tests the attempted removal of
the cutoff against the mean stress and physical time gluing.

There are four results:

* The startup cutoff term has exactly unit response in a normalized peak
  observation, although its unweighted size is exponentially small.
* The desired pulse nevertheless has an exponentially cheap **local entry
  seed**. Replacing the cutoff by that seed preserves the peak; the two
  covariance weights can be retuned by an exponentially small relative
  amount to restore the same leading mean stress.
* Retaining the original zero extension after that replacement creates
  nonzero time-impulse forces at every nonzero entry/exit trace. This is an
  exact distributional obstruction for the full NS equation, not just for
  the principal amplitude equation.
* Cutting off the local adjoint to give it an artificial zero initial trace
  produces an order-one adjoint-defect pairing. It cannot be used to claim
  that the source is unreachable from initial data.

The source-specific local calculation is therefore favorable to replacing
startup by a seed, but it does not prepare those seeds from ONE common
Schwartz datum. No lower bound for the pairing of the **total final force**
with a **complete physical adjoint** is inferred from a single cutoff term.

The original correction target remains

    L_U w = -P F - P div(w tensor w),
    u = U+w,  u(0) in S_sigma(R3),

with a preserved singular observation. Here U,F are the complete forced
velocity and force, not just a primary wave and its cutoff residual.

## 1. Source input and an explicit envelope

Inspected source: OpenAI, *Finite Time Blowup for Navier--Stokes*, September
8, 2026, equations (6.11)--(6.16), (7.12), (7.17)--(7.21), (7.27), (7.38),
(7.40), and (9.2), and Lemma 7.4 / Proposition 7.5. These are used at their
stated scopes, not as an unforced theorem. On a fixed label and regular slow
patch, let L=L_s and let h(v) be its real primary m=1 amplitude in the
moving frame, 0<=v<=L. Write its exact principal matrix as M(v). Thus

    h'=M h,     h(0)=P(0)e_+,
    M=diag(lambda,-lambda)+E-d I,
    ||V(v,s)|| <= C P(v)/P(s),       0<=s<=v<=L,
    c P(v) <= ||h(v)|| <= C P(v).                       (1.1)

V is the fundamental matrix; E and d are retained, not set to their
reference values. The last lower bound follows also from the nonzero radial
component in Lemma 7.4. The frame and its left inverse are uniformly bounded
on the specified patch. Fixed-order coefficient derivatives have the
source's polynomial factors in L. Constants can depend on the fixed source
profiles and derivative order.

Put u=u_*>0, lambda_0>0 and y(v)=u/2+uv/L. The reference rate is

    a(v)=lambda_0/sqrt(1+y(v)^2)
               -lambda_0(1+y(v)^2)/(1+u^2)^(3/2),
    P(v)=exp(integral_(L/2)^v a(s) ds).                  (1.2)

The following closed form is obtained by integrating (1.2), not by
approximating M. Define

    J_u(y)=asinh(y)-(y+y^3/3)/(1+u^2)^(3/2).

Then

    log P(v)=(lambda_0 L/u)[J_u(y(v))-J_u(u)],
    P(0)=exp(-gamma_- L),    P(L)=exp(-gamma_+ L),
    gamma_-=(lambda_0/u)[J_u(u)-J_u(u/2)]>0,
    gamma_+=(lambda_0/u)[J_u(u)-J_u(3u/2)]>0.             (1.3)

Indeed J_u' is positive below u and negative above u. Its unique maximum
on [u/2,3u/2] is u. This proves both strict signs. The exact amplitude h is
comparable to P, not asserted to equal P times a constant vector.

Let psi be the source's smooth pulse cutoff: it equals one for
|v-L/2|<=L/5 and is supported where |v-L/2|<L/3. The bounds on a' give

    exp[-C(v-L/2)^2/L] <= P(v) <= exp[-c(v-L/2)^2/L].      (1.4)

Consequently the primary cutoff residual

    r(v)=(partial_v-M)(psi h)=psi' h                      (1.5)

has every fixed-order coefficient derivative bounded by a polynomial in L
times exp(-c_1 L). In physical normalization there are additional fixed
powers of Q, but L is comparable to ell^2 and Q=2^(-ell); these tails remain
flat at every fixed physical derivative order. This statement is about the
identified primary cutoff contribution, not a signed decomposition of the
entire final forcing into contributions of known nonzero sign.

## 2. Exact evaluation of the principal adjoint test

Set v_*=L/2 and choose

    q=h(v_*)/||h(v_*)||^2,
    z(v)=V(v_*,v)^T q.                                  (2.1)

For v>v_* the expression uses the inverse fundamental matrix; it is a
finite-interval ODE solution, not a backward heat initial-value problem.
The vector z solves -z'-M^T z=0 and

    z(v).h(v)=1.                                        (2.2)

This follows by differentiating the pairing and evaluating at v_*.

### Proposition 1: tiny cutoff force, unit startup response

For the actual primary cutoff residual (1.5),

    integral_0^v_* z.r dv=1,
    integral_v_*^L z.r dv=-1,
    integral_0^L z.r dv=0.                              (2.3)

Proof: z.r=psi' by (2.2). Integrate the changes of psi. No diagonalization,
sign approximation, scalar replacement, or numerical estimate is used.

The zero integral over the entire pulse is cancellation between startup
and shutdown, not absence of a force effect at the peak. Conversely the
unit startup response is not an obstruction to initial-data preparation:
the relevant initial adjoint is large. From (1.1), (2.1), and (2.2),

    c/P(0) <= ||z(0)|| <= C/P(0).                        (2.4)

The lower bound uses z(0).h(0)=1; the upper bound uses the stated forward
fundamental-matrix estimate and ||q||=O(1).

### Proposition 2: the desired source pulse has a cheap local seed

The minimum Euclidean norm of a seed b satisfying the single observation

    q.V(v_*,0)b=1

is 1/||z(0)||, hence comparable to P(0). The seed producing the entire
vector h(v_*) is uniquely h(0)=P(0)e_+ and has norm P(0).

Proof: the observation is the nonzero linear functional z(0).b. Its
minimum-norm preimage of 1 is z(0)/||z(0)||^2. For the entire vector target,
invertibility of V(v_*,0) gives uniqueness. Both conclusions survive the
bounded change of frame with comparable constants.

This is the opposite of the preceding arbitrary small-transmission
countermodel: the source deliberately chooses an amplifying channel, and
the required local seed lies in that channel.

The correction equation for deleting only the primary cutoff source is

    (partial_v-M)w=-r.

With w(0)=0 its unique solution is w=-psi h, which removes the pulse.
With w(0)=h(0), however, its solution is

    w=(1-psi)h,       psi h+w=h.                         (2.5)

It is zero on the peak plateau and exponentially small elsewhere on this
closed rectangle, at every fixed coefficient derivative order. In the
physical primary wave the slow amplitude, transverse cutoff and physical
powers multiply (2.5); they do not change this conclusion on the stated
patch. These are data at the label's entry face, NOT data at a single
physical initial time for the entire construction.

## 3. The actual two-pulse mean covariance survives local replacement

Return to the physical three-component amplitude t_sigma=B h_sigma,
sigma=+,-, with its radial component x_sigma. The source's two covariance
columns, before the exact-curl remainder, are of the form

    H_sigma=c_geom c_i integral_0^L
                       psi^2 x_sigma t_(sigma,tan) dv.  (3.1)

The common positive geometric factor includes the transverse cutoff
integral and angular average. Define tilde H by omitting psi^2 in this
integral but still integrating only over the same rectangle. These are
well-defined covariance integrals even before temporal gluing is solved.

### Proposition 3: exponentially small change, exact local stress repair

On a fixed regular slow patch where the source target T is strictly inside
the two-column positive cone,

    ||tilde H-H|| <= C exp(-c_2 L),
    ||H^(-1)|| <= C sqrt(L),
    rho:=||H^(-1)(tilde H-H)|| <= C sqrt(L) exp(-c_2 L).   (3.2)

For sufficiently large L, the squared weights

    y=H^(-1)T,        tilde y=tilde H^(-1)T

are both strictly positive and

    ||tilde y-y|| <= rho/(1-rho) ||y||.                  (3.3)

The corresponding square-root amplitudes change by an exponentially small
relative amount. Thus the local leading mean stress can be preserved
EXACTLY after the local seed replacement, by retuning two positive weights.

Proof. The difference in each column is (3.1) with psi^2 replaced by
1-psi^2. It is supported in |v-L/2|>=L/5. The amplitude bound (1.4) gives
|x_sigma t_(sigma,tan)|<=C P^2 there. Integration over length L costs L,
and c_i is comparable to 1/L, proving the first estimate.

For the inverse bound, the source's scalar column strengths are comparable
to c_i sqrt(L), hence L^(-1/2). After dividing by those strengths, their
limiting directions are

    c_0 sqrt(1+u^2) N - sigma u K,

with an O(L^(-1/2)) error. Since c_0 is nonzero, u>0 and N,K are orthonormal,
the two limiting directions are independent with a fixed margin. The
inverse bound follows. This uses the same fixed profile/phase margin as the
source; it is not an assertion for arbitrary nearly parallel columns.

Now tilde H=H[I+H^(-1)(tilde H-H)]. The Neumann inverse gives (3.3).
Strict interiority supplies min(y_+,y_-)>=theta||y|| for some theta>0
on the chosen patch. Taking rho/(1-rho)<theta preserves positivity.
For each positive coordinate, the identity

    sqrt(tilde y_j)-sqrt(y_j)
       =(tilde y_j-y_j)/(sqrt(tilde y_j)+sqrt(y_j))

gives the relative amplitude estimate. Fixed-order parameter estimates
follow by differentiating these finite matrix identities and the tail
integrals; fixed powers of L do not destroy their exponential factor. QED.

**Scope:** this repairs the local leading covariance, not the entire
pressure/mean evolution or its exact-curl remainder. In particular it does
not make the uncut fields descend smoothly through the rectangle faces.
Existing higher-order mean corrections would need recomputation. Nothing
here licenses dropping their residuals or their pressure interactions.

## 4. Attempted physical gluing: a nonzero impulse remains

The source's physical evaluation has a particularly useful property:
on a fixed lifted label,

    grad_x v=0,        partial_t v=Q^(-1-h).              (4.1)

Thus its local entry and exit faces are physical time faces. The slow
variables of the amplitude still change with physical time. The coefficient
ODE at fixed slow variables is not the entire physical evolution.

Consider the explicit attempted conversion: replace psi t_sigma by
 t_sigma on 0<v<L, retaining the slow/transverse cutoffs, but continue to
extend that rectangle's contribution by zero outside it. Form the velocity
by the same spatial curl. Denote this uncut, locally smooth velocity by W
inside the rectangle. Since v has no spatial derivatives, its zero-extended
version is locally

    W_box(t,x)=1_(t_a<t<t_b) W(t,x).                     (4.2)

This formula applies near a temporal face away from transverse boundaries;
there are no spatial derivatives of the time indicator. The source's
smooth transverse cutoffs can be retained.

### Proposition 4: zero-extending an uncut seed is still forced

Suppose the complete remaining velocity is continuous through these faces,
and W has a nonzero solenoidal L2 trace J_a=W(t_a) or J_b=W(t_b). The
solenoidal NS residual of the piecewise field has the singular temporal
part

    J_a delta_(t=t_a) - J_b delta_(t=t_b).               (4.3)

It cannot be canceled by the ordinary viscosity, convection, or pressure
of the piecewise-smooth fields. It is not zero forcing and not smooth
forcing, even when J_a and J_b are exponentially small in the band scale.

Proof. Distributional time differentiation of (4.2) gives the ordinary
interior derivative and exactly (4.3). Spatial differentiation, including
the complete viscous Laplacian, does not differentiate this time indicator.
The quadratic velocity product is piecewise locally integrable in time;
it has no temporal delta. Apply the whole-space Leray projector: each trace
is solenoidal, so P J=J, whereas every pressure gradient is annihilated.
Even adding a pressure with a temporal impulse can cancel only a gradient,
not a nonzero solenoidal trace. QED.

At a source entry face the principal trace is nonzero by h(0)=P(0)e_+.
Where the physical slow and transverse cutoffs are nonzero on an interior
patch, the exact-curl correction is lower by the source's positive power
of epsilon, up to polynomial factors in L. Consequently it cannot cancel
the leading nonzero trace for sufficiently small band scale on that patch.
The same reasoning applies to an exit trace. This application is stated
for crossings with nonzero physical traces; no assertion that every label
face intersects every slow box is needed.

The separated enlarged rectangles prevent cancellation by another label
at the same point in this unchanged gluing architecture. Smooth mean
corrections cannot cancel a velocity jump. Retuning covariance weights as
in Section 3 also leaves the trace nonzero. Thus that explicit way of
assembling the local replacements fails the full equation.

Replacing the hard boundary by another smooth cutoff merely relocates a
term of the form cutoff' times the homogeneous amplitude. Equation (2.3)
then records its startup response again. To remove the force rather than
relocate it, the nonzero traces must be matched to an actual continuously
evolving exterior/prehistory, not to zero.

For clarity, inside an open smooth time window the complete residual
identity, with B any smooth solenoidal background, is

    N(B+W)-N(B+psi W)
      =(1-psi)L_B W+(1-psi^2)P div(W tensor W)-psi_t W,   (4.4)
    N(V)=V_t-nu Delta V+P div(V tensor V).

The two terms preceding -psi_t W remain. Deleting the startup cutoff alone
never established N(B+W)=0. The source's later residual corrections and
whole-space localization are not silently omitted from the target.

## 5. A localized adjoint produces its own order-one error

The full-PDE adjoint identity of the preceding note needs an additional
term when a proposed test Z is only an approximate adjoint. Write

    R_Z=L_U* Z
       =-Z_t-nu Delta Z-P[(U.grad)Z]+P[(grad U)^T Z]

between its observation jumps. For w(0)=C* a and those same jumps, the
exact finite-interval identity is

    sum_j q_j <w(t_j),phi_j>
      =<a,C Z(0)>-integral <F,Z>
        +integral integral (w tensor w):grad Z
        -integral <w,R_Z>.                              (5.1)

It follows directly by integration by parts, retaining the jumps, pressure
projection, viscosity and the entire quadratic product.

There is an exact warning already for the source's principal matrices.
Take the z from Section 2 on [0,v_*] and set Z=psi z, so Z(0)=0. Then

    (-partial_v-M^T)Z=-psi' z.

Use the small pulse-preserving correction w=(1-psi)h from (2.5). The two
pairings are EXACTLY

    integral_0^v_* r.Z dv=integral psi psi' dv=1/2,
    integral_0^v_* w.((-partial_v-M^T)Z) dv
                =-integral (1-psi)psi' dv=-1/2.          (5.2)

There is no nonlinear term in this principal calculation. Its initial
pairing is zero because Z(0)=0, and its terminal correction observation is
zero because w(v_*)=0. The two half-unit terms in (5.1) cancel precisely.

Thus an apparent obstruction obtained by cutting off the adjoint, setting
its initial trace to zero, and discarding R_Z is false even for the actual
source pulse. The correction w is flat in the unweighted coefficient norm,
but the adjoint grows like the reciprocal envelope in the same tail region.
Their defect pairing is not small. The analogous cutoff error has to be
retained in any physical lift before invoking (5.1).

## 6. Exact point where this attempt stops

Local source-specific startup removal and leading covariance repair work.
The explicit zero-extension gluing fails by (4.3). The attempted localized
adjoint shortcut fails by (5.2). Neither failure implies that a genuinely
coupled, smoothly prepared unforced cascade is impossible.

What is still required is a construction of ONE physical initial datum
whose full evolution supplies all the needed nonzero entry traces, allowing
all previously generated modes, pressure, diffusion, and nonlinear transfer.
Alternatively an exact global adjoint could show that those traces require
an excessive initial/nonlinear budget within a stated correction class.
The source's local pulse ODE fixes slow variables and cannot be used as
that full propagator before, between, or outside the rectangles.

In particular none of the following was proved here:

    one Schwartz initial trace for the complete source history;
    a uniform full-PDE inverse preserving the singular core;
    convergent cancellation of the entire nonlinear force;
    a quantitative full-physical-adjoint exclusion;
    an unforced singular solution or arbitrary-data regularity.

The next meaningful task is physical prehistory matching with no pulse
restarts. Another generic inverse or another arbitrary scalar countermodel
would not answer the question exposed by this calculation.

## 7. Validation, implementation and provenance

Companion script: `research/check_source_pulse_adjoint.py`.
Frozen report: `research/evidence/2026-09-10-source-pulse-adjoint-checks.json`.

The script passed **12 exact symbolic assertions and 102 numerical
assertions**, distinguished explicitly. The exact checks cover the envelope
primitive, matrix adjoint and cutoff identities, both impulse signs, the
full nonlinear cutoff difference, and the half-unit defect pairings.

The numerical checks integrate the source-form THREE-component principal
matrix (7.6), retaining its pressure constraint, cylindrical connection
terms, carrier rounding and leading viscosity. Integration is performed
with the forward amplitude divided by P and backward adjoint multiplied by
P, avoiding spurious underflow from the Gaussian factors. The two covariance
columns are computed and retuned. The numerical results are floating-point
calibrations, not interval certificates or proofs of the analytic estimates.

Calibration values F_0=R_0=1, g_0=(-3,2) have positive principal growth.
They are not claimed to be the source's selected profile point. L and k
are varied independently, so the cases are NOT simultaneous realizations
of all dyadic scaling relations of the full construction. The test mean
target is an explicitly chosen interior combination of the two computed
columns, not a newly computed global source background stress.

For example, at u_*=1, L=512 the log10 of the full local entry-seed norm
is approximately -47.85; its normalized startup adjoint response is 1 to
the reported tolerance, and the relative covariance matrix change is about
4.26e-23. These numbers illustrate the proved distinction between a small
seed/force and a unit normalized response; they are not evidence for an NS
blow-up or for common-history preparation.

The preceding `check_adjoint_deforcing.py`, extracted from the uploaded
continuation packet, was rerun and passed its 1049 exact assertions.
Local syntax/whitespace checks were also run. Shell networking failed at
DNS resolution; source inspection used the web PDF reader and GitHub
connector. A full repository checkout was unavailable, so the repository-
wide verifier, all other checkers, manuscript builds and Lean were NOT run.
The new checker is read-only by default and writes JSON only with --output.

No independent audit or exhaustive novelty search was performed. The
identities and numerical code here are newly written, not copied external
code. Existing proofs, live PLAN, manuscripts and formal status are not
replaced. This additive packet is for review and controller integration.

### Source locations inspected in this run

* OpenAI, *Finite Time Blowup for Navier--Stokes* (2026-09-08): physical
  pulse description; (6.11)--(6.16); (7.5)--(7.21); covariance (7.27)--(7.30);
  exact curls and cutoff residual (7.38)--(7.40); Proposition 9.1 and (9.2);
  the flat residual statement (9.20). Relevant equation pages were also
  inspected as rendered screenshots. PDF pagination is cited by equation
  number because the parsed page boundaries can differ from the render.
  https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
* Source announcement, scope only:
  https://openai.com/index/navier-stokes-solution/
* Prior project input, at the SHA above:
  `research/evidence/2026-09-10-adjoint-deforcing.md`;
  `research/evidence/2026-09-08-smooth-pulse-inverse-and-history.md`;
  `research/evidence/2026-09-08-angular-preparation-obstruction.md`;
  `paper/sections/viscous_fredholm.tex` and `PLAN.md`.
  The prior generic adjoint identity, scalar countermodels, and finite-
  horizon inversion are internal work, not independent external literature.
