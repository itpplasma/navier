# A logarithmic-loss mixed-trace inverse for the complete principal harmonic family

Date: 2026-09-08. Integration input:
`694be9648450dbb1528232e08d20ec07ace302d0`.
Status: AUTHOR PROOF; independent mathematical audit PENDING.
This is a PRINCIPAL AMPLITUDE theorem, not the original-NS PDE inverse.

## 0. Precise consumer and relation to the concurrent obstruction

The zero-data principal inverse has a superalgebraic loss on raw flat seed
errors. The concurrent `2026-09-08-autonomous-pulse-obstruction.md` already
proved that fact and its finite-gauge extension. The support/pulse audit
reproduces it to explain the trace problem; it is NOT counted twice here.
Its Proposition 6 also gives the exact small repair (1-psi)h when the initial
trace is free. This note goes further: arbitrary small raw principal sources
have a bounded mixed-trace inverse, uniformly over ALL nonzero harmonics,
with O(sqrt(L)) loss. Since L is comparable to ell^2, that is O(log(1/Q)).

One trace is fixed at the turning point of each unstable low harmonic;
strongly damped harmonics use their left initial trace. The problem is NOT
the causal zero-data problem, nor a quotient by finitely many global gauges.
Across infinitely many pulse labels it prescribes infinitely many traces.
It therefore does not contradict either concurrent obstruction.

Consumer: this repairs the principal linear component of UE1 without deleting
its pulse. The first unproved step is to realize these traces simultaneously
by one original whole-space Cauchy solution, including all transverse and
mean equations. Neither this theorem nor flatness supplies that realization.

## 1. A scalar turning-point inverse

Let a be real C1 on [0,L], L>=1, and assume a'<=-kappa/L with kappa>0.
Choose v_* as the unique zero of a when it lies in [0,L]; choose v_*=0 if
a(0)<=0, or v_*=L if a(L)>=0. Then the problem

    z'-a z=f,  z(v_*)=0

has a unique solution, and its inverse T_a satisfies

    ||T_a f||_infinity <= sqrt(pi L/(2 kappa)) ||f||_infinity.     (1.1)

Proof. The exact solution is the oriented integral

    (T_a f)(v)=integral_(v_*)^v exp(integral_s^v a(r)dr) f(s)ds.  (1.2)

For v>=v_* and v_*<=s<=v, monotonicity and a(v_*)<=0 imply

    integral_s^v a <= -kappa[(v-v_*)^2-(s-v_*)^2]/(2L)
                    <= -kappa(v-s)^2/(2L).                      (1.3)

For v<=v_* the same estimate, with s>=v, follows using a(v_*)>=0 and
reversing the integral. At a clamped endpoint only the relevant one-sided
argument is used. The integral of exp[-kappa r^2/(2L)] on [0,infinity) is
sqrt(pi L/(2 kappa)). This proves (1.1); uniqueness is scalar ODE uniqueness
with data at v_*. For b<=-beta<0, the ordinary left-data inverse T_b obeys

    ||T_b f||_infinity <= beta^(-1)||f||_infinity.                (1.4)

The sqrt(L) order is optimal in this class. For a(v)=-(v-L/2)/L, f=1,
and L>=4, evaluation of (1.2) at v=L/2+sqrt(L) gives

    |z(v)| >= exp(-1/2) sqrt(L).

This follows by bounding the integrand from below by exp(-1/2) on the
interval of integration of length sqrt(L). Thus the logarithmic loss is not
an artifact of applying an exponentially large causal estimate.

## 2. Coupled two-component system

Consider, in the maximum-component norm,

    z'=[diag(a,b)+E]z+f,
    a'<=-kappa/L, b<=-beta,
    ||E||_(infinity,induced)<=C_E/L.                             (2.1)

Impose z_+(v_*)=0 and z_-(0)=0, with v_* chosen from a above. Put

    H_L=max(sqrt(pi L/(2 kappa)),1/beta).

If C_E H_L/L<=1/2, there is a unique solution with these two traces and

    ||z||_infinity <= 2 H_L ||f||_infinity.                       (2.2)

Proof. With T=diag(T_a,T_b), the boundary-value problem is exactly
z=T f+T E z on C([0,L];C^2). The norm of T E is at most C_E H_L/L<=1/2.
The convergent Neumann series gives existence, uniqueness and (2.2).
The solution is C1 and solves the original coupled equation. QED.

This estimate applies to arbitrary unweighted continuous f, not only sources
already divided by a Gaussian envelope. Fixed-order v derivatives can be
estimated by differentiating the equation when the corresponding coefficient
and source derivatives are bounded. No transverse/slow-parameter derivative
estimate or compatibility across changing trace surfaces is asserted here.

## 3. Application to the inspected phase, including arbitrarily high harmonics

Use the actual two-dimensional principal frame of [OA, (7.17)], with a fixed
regular slow label and fixed sign, on [0,L]. The reference coefficients are

    y(v)=u_*/2+u_* v/L,  u_*>0,
    lambda(v)=lambda_0/sqrt(1+y(v)^2),
    d_ref(v)=lambda_0(1+y(v)^2)/(1+u_*^2)^(3/2).                  (3.1)

The sign of the source's phase variable does not affect these coefficients.
Assume the displayed positive lambda_0 and u_* stay in fixed compact subsets
of (0,infinity), and the inspected frame error bounds hold:

    z_m'=[diag(lambda,-lambda)+E-m^2 d I] z_m+g_m,
    ||E||<=C/L,  |d-d_ref|<=C/L.                                (3.2)

Constants may depend on those compact sets and frame bounds, not m,L,Q.
This is exactly the principal equation; slow transport, residual viscosity,
mean modes and other PDE correction terms are NOT dropped from the original
problem by asserting (3.2).

### Theorem 3: harmonic-uniform mixed-trace right inverse

There are fixed L_0, m_0 and C_* such that for all L>=L_0, every nonzero
integer m and every continuous g_m, (3.2) has a unique solution with the
following homogeneous trace constraints:

* for 1<=|m|<m_0, z_(m,+)(v_m)=0 and z_(m,-)(0)=0, where v_m is the zero
  of a_m=lambda-m^2 d_ref, clamped to an endpoint as in Section 1;
* for |m|>=m_0, z_m(0)=0.

The resulting linear operator J_L satisfies

    ||(J_L g)_m||_infinity <= C_* sqrt(L) ||g_m||_infinity,        (3.3)

and, for |m|>=m_0, the stronger bound

    ||(J_L g)_m||_infinity <= C_* m^(-2)||g_m||_infinity.          (3.4)

In particular, for ANY nonnegative fixed harmonic weights w_m,

    sum_(m!=0) w_m ||(J_L g)_m||_infinity
         <= C_* sqrt(L) sum_(m!=0) w_m ||g_m||_infinity.          (3.5)

No finite-harmonic cutoff is needed. With L comparable to ell^2 and Q=2^-ell,
the loss in (3.3) is O(ell). A family flat to all algebraic orders in Q in
these specified norms remains flat after this inverse.

Proof. Uniform constants d_0,kappa_0>0 exist with d_ref>=d_0 and

    a_m'=-lambda_0 u_* y/[L(1+y^2)^(3/2)]
         -2 m^2 lambda_0 u_* y/[L(1+u_*^2)^(3/2)]
         <= -kappa_0 m^2/L,
    -lambda-m^2 d_ref <= -m^2 d_0.                              (3.6)

For any fixed finite range 1<=|m|<m_0, absorb -m^2(d-d_ref)I into E.
Its norm is at most C(1+m_0^2)/L. Section 2 applies uniformly in that finite
range once L>=L_0, giving (3.3). For m=1, the reference root is exactly L/2.

It is important NOT to apply that perturbative argument uniformly to m^2/L
for unbounded m. Instead enlarge L_0 so d>=d_0/2 and ||E||_(Euclidean)<=1.
Let lambda_max bound lambda. Choose m_0 so m_0^2 d_0>=4(lambda_max+1).
For |m|>=m_0 the exact Hermitian part in (3.2) is bounded above by

    lambda_max+1-m^2 d_0/2 <= -m^2 d_0/4.                        (3.7)

The full forward matrix propagator consequently has norm at most
exp[-m^2 d_0(v-s)/4] for v>=s. Its zero-initial-value integral has norm at
most 4/(m^2 d_0), proving (3.4) without losing m^2 in an error estimate.
Increasing constants for equivalent component norms gives (3.3) for all m.
Summing the nonnegative inequalities proves (3.5), including countable
families by absolute convergence. Reality follows by pairing m and -m when
the inputs are conjugate and the real frame coefficients are shared. QED.

### Principal pressure and constraints

Let t_m=B z_m, using the uniformly invertible moving basis of n_Phi^perp,
and g_m=-B^left proj_(n_Phi^perp) f_m as in [OA]. Then n_Phi.t_m=0.
The missing normal equation is solved algebraically by

    pi_m= -(n_Phi.K t_m - n_Phi'.t_m + n_Phi.f_m)
                       /(i k m |n_Phi|^2).                     (3.8)

Indeed differentiating n_Phi.t_m=0, and inserting (3.8), gives precisely

    t_m'+K t_m+m^2 d t_m+i k m n_Phi pi_m=-f_m.                   (3.9)

Thus the theorem is a complete PRINCIPAL velocity/pressure inverse, not only
one scalar component. With the fixed frame bounds its pressure norm obeys
C/(k|m|) times the sum of the velocity and source norms. This principal
pressure is not yet the canonical whole-space pressure of a completed flow.

## 4. The seed repair, and the point where completion still fails

For the homogeneous primary pulse h of [OA, Lemma 7.4], its stable-frame
initial coordinate is zero. For its cutoff a=psi h, the correction
w=(1-psi)h has w_+(L/2)=0 and w_-(0)=0 and solves the negative cutoff residual.
Uniqueness above therefore selects exactly the flat tail-filling correction,
not the large pulse-deleting zero-data correction. The covariance in the
middle is preserved. This is a positive principal exactification result.

The mixed traces are noncausal constraints used to SELECT initial data.
They are mathematically legitimate boundary data for each finite principal
interval, but they are not independent controls available to an unforced
Navier--Stokes evolution. Across infinitely many labels they form a coupled
trace-realization problem. Filling tails also destroys the source's exact
support separation, introducing the very cross-label terms that were absent
from its residual split. Those terms cannot be assumed flat at all future
intersections just because the individual endpoint tails are small.

These interval solutions need not match across source rectangles or descend
to the source's common auxiliary torus after their cutoffs are removed.
Single-valuedness and trace compatibility must be proved, not inherited from
the cutoff construction.

A precise warning is supplied by the following elementary cyclic version.
For a fixed coefficient matrix C continued around a closed interval of length
P, let Phi(P,0) be its monodromy. If a is a periodic cutoff pulse and
r=(partial_v-C)a, any PERIODIC correction of -r has

    a+w=Phi(v,0)c,  [Phi(P,0)-I]c=0.                            (4.1)

If one is not an eigenvalue of the monodromy, the only corrected periodic
field is zero. Proof: a+w solves the homogeneous equation and periodicity
is exactly (4.1). This is a condition on a specified cyclic principal
extension, NOT an assertion that the source's coupled physical continuation
has such a monodromy or lacks its unit eigenspace. It records explicitly
why separate mixed boundary inverses do not prove gluing.

No bound has been proved for the full L_U inverse including slow derivatives,
all mean and exterior coupling, localization, or a common Schwartz trace.
The angular-preparation theorem further excludes a naive confined homogeneous
realization of these prescribed high-frequency traces from one earlier datum.
It requires radial prehistory/overlap, nonlinear supply, or changed geometry.

Accordingly the completed chain here is ONLY

    principal phase bounds -> mixed-trace inverse for all nonzero harmonics
      -> flat principal residual can be corrected without deleting its pulse.

The missing chain remains

    ONE coupled whole-space Cauchy trace realizing those constraints
      + full nonlinear correction with retained overlap/analytic leakage
      -> original unforced singular solution -> endpoint verification.

Neither an original-NS singularity nor an arbitrary-data continuation producer
has been obtained. Independent audit is pending; no canonical status changes.

[OA] OpenAI, *Finite Time Blowup for Navier--Stokes*, owner's 165-page PDF:
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Directly inspected here: printed pp.74--80, equations (7.2), (7.10)--(7.18),
and Lemma 7.4; relevant pages visually checked. No full proof audit is claimed.

The final integration also preserves the concurrent formal-core update
`dd074604f04ebd705583df8dba1d9d3e53df0793`; no formal file or status is promoted.
