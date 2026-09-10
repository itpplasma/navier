# Adjoint initialization and a source-sensitive de-forcing test

Date: 2026-09-10. Research input: `itpplasma/navier@bc70da065f00e69799128bad9949baaeeda3a2c6`.

**Status: author proofs below, independent mathematical audit pending.** No
novelty claim, terminal promotion, Lean certification, or unforced blow-up is
claimed. The finite-horizon result changes the auxiliary initialization law;
it does not prove that the previous law has no exceptional parameters.

## 0. The actual task and the first uncontrolled quantity

Let U be the prescribed forced velocity, with viscosity nu>0, and let P be
the whole-space Leray projection. To produce an unforced velocity V=U+w,
one must solve, exactly,

    L_U w = -P F - P div(w tensor w),
    L_U w = w_t - nu Delta w + P[(U.grad)w + (w.grad)U].       (0.1)

F is the given physical force. All fields are on R3; all exterior modes,
pressure interactions, viscosity, and quadratic terms are retained.
The initial state of V is allowed to change. No nonzero unforced evolution
can retain the source construction's zero initial state.

The consumer is: a quantitative full-PDE inverse on a concentrating history
-> a convergent solution of (0.1) -> ONE Schwartz initial velocity -> a
correction small enough in a stated observation to preserve blow-up.
None of those last three implications follows from finite-interval linear
solvability. The first unbounded quantity for the construction remains the
response of its actual full propagator to its actual forcing near T=1,
including whether the needed pulse observations lie in a bounded-cost
initial-data range.

The current manuscript proves a full finite-interval inverse for generic
positive penalties, but not common traces or endpoint control [R1]. The
source leaves flat residuals rather than setting them identically to zero
[OA, Proposition 9.3 and (9.20)]. Its pulse cutoff estimates are of Gaussian
size in a logarithmic scale, not zero [OA, section 7.4, (7.40)]. Our earlier
connected-pulse example already shows why raw flatness need not survive an
inverse [R2]. We therefore do not repeat the argument 'flat means removable'.

This packet makes two changes: an all-positive-penalty auxiliary
initialization with a uniform operator-perturbation estimate, and an adjoint
test that retains the precise nonlinear term capable of overcoming failed
linear preparation. The latter has NOT yet been evaluated on the source's
actual propagators.

## 1. Whole-space operators and a different initialization law

Fix a finite T>0, nu>0, a real solenoidal
U in C^infinity([0,T];H^m(R3)) for every nonnegative integer m, and a real
chi in C_c^infinity(R3). Write H=L2_sigma(R3;R3), X=L2(R3;R3).
Let E(t,s):H->H be the complete forward evolution of L_U. Let T(t,s)
be Piola transport, solving

    (partial_t + U.grad)b = (grad U)b.

It is not unitary in general. Set

    C = (-Delta)^(-1/2) chi curl : H -> X,
    A = C* C = curl chi (-Delta)^(-1) chi curl : H -> H.

The adjoints are Hilbert-space adjoints. In particular they are not obtained
by replacing viscous evolution by backward heat as an initial-value problem.
C and C* preserve every nonnegative integer Sobolev class. C* has
solenoidal output supported in supp chi. These facts, including the
low-frequency bounds in three dimensions, are proved in [R1].
For a smooth all-Sobolev solenoidal source g define

    V_g(t) = integral_0^t E(t,r) g(r) dr,
    H_T = integral_0^T T(0,s) E(s,0) ds,
    S_T = H_T C* : X -> H,
    b_T = integral_0^T T(0,s) V_g(s) ds.                    (1.1)

Consider this CHANGED auxiliary initial law:

    L_U v = g,
    (partial_t + U.grad)eta - (grad U)eta = v,
    v(0) = lambda A H_T* eta(0),      eta(T)=0.             (1.2)

Lambda is any nonnegative real number. The law depends on the prescribed
history up to T. This is a choice of initial data, not an additional body
force; it need not be causally implementable without knowing that history.
It is not the Euler variational boundary law, and is not claimed to be.

### Theorem 1: existence for every nonnegative penalty

For each prescribed finite history above, (1.2) has a unique smooth
all-Sobolev solution, with v(0) compactly supported in supp chi. Put

    R_T = (I + lambda S_T S_T*)^(-1).

Then the exact formulas are

    eta(0) = -R_T b_T,
    a_T = -lambda S_T* R_T b_T,
    v(0) = C* a_T,
    v(t) = E(t,0) C* a_T + V_g(t).                         (1.3)

There is no exceptional positive lambda. Moreover

    ||eta(0)||_H <= ||b_T||_H,
    ||a_T||_X <= sqrt(lambda)/2 ||b_T||_H,
    ||v(0)||_H <= ||C*|| sqrt(lambda)/2 ||b_T||_H.          (1.4)

The constants displayed in (1.4) do not depend on U or T. The SIZE of b_T,
and all high-order regularity constants, can depend on them without bound.

Proof. Pulling the terminal displacement back to zero gives exactly

    eta(0) + H_T v(0) + b_T = 0.

The new initial law is v(0)=C* a_T with a_T=lambda S_T* eta(0).
Thus (I+lambda S_T S_T*)eta(0)=-b_T. The bounded operator S_T S_T*
is nonnegative self-adjoint. Its shifted inverse exists on H, with norm
at most one: the quadratic form is at least ||eta||^2, and its range is
closed and dense (the adjoint has zero kernel). This proves the formulas
and uniqueness in L2. Spectral calculus applied to S_T S_T* gives

    ||lambda S_T*(I+lambda S_T S_T*)^(-1)||
      <= sup_{s>=0} lambda s/(1+lambda s^2)
       = sqrt(lambda)/2.

For lambda=0 the formula is read directly as a_T=0.

Here is the regularity step, rather than an assumption of smooth inversion.
For the stated smooth finite history, E(t,s) gains sigma derivatives with
bound C(t-s)^(-sigma/2), for 0<=sigma<=2; transport preserves all H^m.
Consequently H_T gains every sigma<2. These are the forward estimates in
[R1], before multiplication by A. H_T* preserves each H^m. To see the
latter without a false adjoint-transport identification, if Phi_s is the
flow from time zero, then

    T(0,s)* h(x) = P[(D Phi_s(Phi_s^(-1)x))^(-T)
                        h(Phi_s^(-1)x)].                 (1.5)

This follows by changing variables in the L2 pairing and using det D Phi=1.
Composition and multiplication preserve H^m on a fixed finite interval.
E(s,0)* has the usual backward-adjoint parabolic Sobolev estimate, obtained
by reversing time in its terminal problem. Integrating E(s,0)*T(0,s)*
proves the assertion for H_T*.

Therefore G_T=H_T A H_T* gains one derivative from each H^m into H^(m+1).
The equation eta(0)=-b_T-lambda G_T eta(0), starting in L2, bootstraps
all Sobolev orders, since b_T has all of them. Formula (1.3), followed by
the transport equation, gives smooth v and eta. C* gives the fixed compact
support of the initial velocity only. No compact support is imposed at
positive times. QED.

This is the standard positive normal-operator mechanism applied to a new
mixed initialization. Its value here is an exact whole-space, all-penalty
formula, not a claim to have invented least squares or positive resolvents.

## 2. A uniform stability bound for changing horizons

Let S:X->H be any bounded operator and define

    B_lambda(S) = lambda S* (I+lambda S S*)^(-1).

### Theorem 2: operator-Lipschitz trace selection

For lambda>=0 and bounded S_1,S_2 between the same spaces,

    ||B_lambda(S_1)|| <= sqrt(lambda)/2,
    ||B_lambda(S_1)-B_lambda(S_2)||
          <= lambda ||S_1-S_2||.                          (2.1)

Hence, for a_i=-B_lambda(S_i)b_i,

    ||a_1-a_2|| <= sqrt(lambda)/2 ||b_1-b_2||
                    +lambda ||S_1-S_2|| ||b_2||.         (2.2)

Proof. Complexify the Hilbert spaces and introduce the self-adjoint block
operator on X direct-sum H,

    D_S = [0 S*; S 0].

For lambda>0 set c=1/sqrt(lambda). The top-right block of

    lambda D_S (I+lambda D_S^2)^(-1)
       = 1/2 [(D_S-i c I)^(-1)+(D_S+i c I)^(-1)]           (2.3)

is B_lambda(S). The resolvent identity and the self-adjoint resolvent bound
|| (D_S +/- i c I)^(-1)|| <= 1/c give a Lipschitz bound lambda times
||D_(S_1)-D_(S_2)||=||S_1-S_2||. The norm estimate follows as in Theorem 1.
Subtract the two selected controls to obtain (2.2). Lambda=0 is immediate.
QED.

For one prescribed history U,g on [0,T_*), a fixed chi and a FIXED lambda,
two sufficient conditions for an L2-Cauchy initial trace as T increases to
T_* are

    integral_0^T_* ||T(0,s) E(s,0) C*||_(X->H) ds < infinity,
    integral_0^T_* ||T(0,s) V_g(s)||_H ds < infinity.        (2.4)

Indeed S_T and b_T then converge in operator norm and H respectively, and
(2.2) proves convergence of a_T and v(0). This is stronger than merely
selecting a common admissible penalty, but the two integrals have NOT been
bounded for the source. Uniform all-order Sobolev bounds for the initial
velocities would additionally give a compactly supported smooth limiting
trace; L2 convergence alone does not imply Schwartz regularity.

Even under (2.4), the velocity correction on approaching singular times can
be large. Vanishing of the pulled-back displacement tail also need not imply
vanishing of eta itself when T(t,0) grows. These conclusions are NOT included
in this theorem. For each fixed preterminal interval the linear velocities
converge by (1.3); endpoint bounds and nonlinear closure are separate.

## 3. Why positive inversion can still destroy the intended pulse

Equation (1.3) also gives the unique minimizer, over a in X, of

    ||a||^2 + lambda ||S a+b||^2.                          (3.1)

It regularizes a preparation problem; it does not solve S a=-b exactly.
For the scalar example S=epsilon>0, b=1, its control is

    a_lambda = -lambda epsilon/(1+lambda epsilon^2).

The exact control is -1/epsilon. A small regularized control leaves nearly
the entire endpoint discrepancy when epsilon is small.

A single infinite-dimensional example makes the common-trace gap precise.
On l2 set S e_j=2^(-j)e_j and b_j=2^(-j). Every finite prefix of
S a=-b has a solution. Its minimum initial squared norm is N for N
constraints, so there is no l2 solution of all constraints. This is an
algebraic calibration, NOT an asserted NS propagator.

Flatness is no safeguard: on an abstract sequence with scale Q_j=2^(-j),
take transmission s_j=2^(-j^3) and residual b_j=2^(-j^2). The residual
is smaller than every fixed power of Q_j, but exact cancellation costs
|a_j|=2^(j^3-j^2). The new uniformly bounded displacement inverse therefore
does not establish a small blowup-preserving velocity inverse.

More generally, suppose bounded observation maps M_j:X->Y_j and targets
d_j define nonempty finite-prefix affine sets

    K_N = {a: M_j a=d_j for j<=N}.

Let a_N be the minimum-norm element of K_N. Then a common finite-norm
initial control exists IFF sup_N ||a_N||<infinity. Indeed K_N are nested
closed affine sets; for M>=N,

    ||a_M-a_N||^2 = ||a_M||^2-||a_N||^2.                  (3.2)

The bounded case makes a_N strongly Cauchy, with limit in every K_N.
Conversely a common control bounds every minimum norm. Equation (3.2)
follows because a_N is orthogonal to the direction space of K_N and
a_M-a_N lies in that space. No infinite-dimensional compact embedding is
used. This is a trace-coherence test, not a theorem that the source passes it.

## 4. Exact adjoint test, including the nonlinear way out

The preceding gap should be tested against the ACTUAL force and full
propagator, not arbitrary worst-case sources. Fix finitely many times
0<t_1<...<t_N<T_*, smooth compactly supported solenoidal test fields
phi_j, and real weights q_j. Observations may be scaled to measure a
particular vortex component or wave amplitude. Define the piecewise smooth
backward adjoint history

    z(t) = sum_{j:t<t_j} E(t_j,t)* q_j phi_j.               (4.1)

Between its observation jumps it solves the complete adjoint equation

    -z_t - nu Delta z - P[(U.grad)z] + P[(grad U)^T z]=0.  (4.2)

The projection is retained. At each observation time the backward jump
adds q_j phi_j. Define S(z)=(grad z+grad z^T)/2.

### Proposition 3: necessary full nonlinear de-forcing budget

Let w be a real solution of (0.1), smooth in time with every spatial
Sobolev norm finite on this closed finite interval, with initial correction
w(0)=C* a, ||a||_X<=M, and suppose

    |<w(t_j),phi_j>| <= epsilon_j.

Then

    |integral_0^t_N <F,z> dt|
      <= M ||C z(0)||_X + sum_j |q_j| epsilon_j
         + integral_0^t_N ||S(z(t))||_infinity ||w(t)||_2^2 dt.   (4.3)

The infinity norm here is the pointwise matrix operator norm. Thus a positive
excess over the first two terms is a REQUIRED nonlinear correction budget,
not proof that nonlinear regeneration is impossible.

Proof. Integration by parts on the subintervals, including every jump,
gives the exact identity

    sum_j q_j <w(t_j),phi_j>
      = <a,C z(0)> - integral <F,z>
          + integral integral_R3 (w tensor w):grad z dx dt.       (4.4)

The last sign follows from -P div(w tensor w) in (0.1). The force may be
paired without P because z is solenoidal. Symmetry of w tensor w permits
replacement of grad z by S(z). Apply Cauchy-Schwarz to the initial term
and the stated observation bounds to obtain (4.3). The whole-space
integration is justified by smooth Sobolev regularity and spatial cutoffs
followed by a limit. QED.

At the LINEAR level the last term is absent. A backward adjoint history
with a tiny initial controllable component C z(0), but a large pairing
with the actual force, rules out a bounded initial replacement satisfying
those observations. This is the continuous full-PDE version of a small
singular-value test. In the nonlinear equation, (4.3) quantifies precisely
the additional transfer that must overcome it.

To exclude a perturbative correction obeying ||w||_(L-infinity_t L2_x)<=delta,
it would suffice to exhibit this z with

    |integral <F,z>| > M||C z(0)|| + sum |q_j|epsilon_j
                         +delta^2 integral ||S(z)||_infinity.    (4.5)

No such z for the actual OpenAI flow has been established in this packet.
An exclusion under this bound would concern that perturbative correction
class, not every possible unforced singularity. Failure to de-force this
profile cannot be promoted to global regularity.

## 5. What the attempt did and did not achieve

The exceptional-penalty issue can be removed by changing the auxiliary
initialization, while keeping the complete viscous PDE and a localized
smooth initial velocity. The new selector also has a uniform operator-
perturbation bound, so there is a precise sufficient trace-convergence test.
This is a finite-interval repair, not a terminal advance.

The forcing was NOT eliminated. Positivity of the initial compatibility
operator does not control the preservation of the collapsing core. The
exact bottleneck is now testable in the source's own observable directions:
initial transmission, force projection onto backward adjoint channels, and
the nonlinear budget in (4.3). Neither signs nor all-orders flatness settle
those quantities.

A next source-specific calculation should use (4.1) for actual coupled
mean/wave observations and retain its radial exterior and pressure. It must
produce either a bounded-cost, all-order common trace with a nonlinear
contraction, or a quantitative violation such as (4.5). Another generic
positive inverse is not a substitute for that calculation.

## 6. Validation and provenance

The companion `check_adjoint_deforcing.py` passes **1049 exact assertions**:
rectangular rational matrix mixed conditions, contraction and control bounds,
operator/data perturbation bounds, self-adjoint block resolvent identities,
a matrix resonance calibration, divergent minimum-prefix costs, flat-source
controls, and signs in a nonlinear ODE adjoint identity. The PDE statements
are supported by the paper proofs above, not by the matrix tests.

No NS numerical orbit, independently verified PDE theorem, full source-proof
audit, Lean build, singular-endpoint inverse estimate, nonlinear contraction,
or unforced counterexample was produced. The whole repository checkout was
not available in this environment: GitHub was read through the connector,
but shell networking was unavailable. The repository-wide research verifier,
all prior checkers, and the manuscript build were NOT run. Only this additive
packet's exact checker and local whitespace/syntax checks were run.

No existing evidence, manuscript, live plan or canonical proof/formal status
is replaced or promoted. Independent review and controller integration are
still needed. All arguments and checking code in this packet are newly
written; no third-party source code has been copied.

### Sources inspected

[R1] `paper/sections/viscous_fredholm.tex` and
`research/evidence/2026-09-09-viscous-fredholm-inverse.md`, at the research
input SHA above. Prior author proof, audit pending. Supplies the localized
operator and finite-history parabolic estimates used here.

[R2] `research/evidence/2026-09-08-smooth-pulse-inverse-and-history.md`,
and `research/evidence/2026-09-08-angular-preparation-obstruction.md`, at the
same SHA. Prior author proofs with explicitly restricted scopes.

[OA] OpenAI, *Finite Time Blowup for Navier--Stokes*, released 2026-09-08.
Theorem 1.1, physical pulse description, section 7 cutoff estimates,
Proposition 9.3, and equation (9.20) inspected for this attempt.
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Announcement: https://openai.com/index/navier-stokes-solution/
No source theorem is silently strengthened to its unforced analogue.
