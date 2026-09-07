Controller-retained worker snapshot, 2026-09-07. Original worker file: kinetic-production.md;
SHA256 `55d2f1fe18a57a20999e22bc73dc10a7a2f17dc73bd252f13f3b17f6dac69de9`.
Author derivation with independent mathematical audit PENDING. This
record is evidence for further research, not an established graph theorem.
The original worker text follows unchanged. PLAN alone allocates work.

# Spatial Fisher production, the genuine initial layer, and its surviving cubic source

Worker evidence, 2026-09-07. MODE: DISCOVER/REPAIR.
Frozen input: ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df; clean patch
SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.
Author derivation only; independent audit pending. No authoritative file,
claim status, manuscript, formal source, or repository commit changed.

## Frontier and outcome

For every solenoidal Schwartz U=u0 on R3 and nu>0, retain the positive
hard-sphere preparation F0=M(v-epsilon U), and

    epsilon^2 F_t + epsilon v.grad_x F = Q_nu(F,F).

The desired producer is a finite input-only bound for
X_epsilon=I_x(F)/epsilon^2 on (delta,H), or a weaker estimate with a complete
C1 consumer. Its constant may depend on all of u0,nu,delta,H, but not epsilon
or the observation resolution J. The established truncated-momentum estimate

    ||m_tilde||_3 <= C (H(F|M)/epsilon^2)^(1/4) X_epsilon^(1/4)

followed by the contracted GSR/identification/continuation suffix is retained.

I derived a signed spatial Fisher balance, an exact initial acceleration
on the actual Maxwellian preparation, and an explicit stress relaxation
corrector. The corrector resolves the apparent epsilon^-2 acceleration:
the Fisher change on a collision-time layer is only order epsilon^2. Its
relaxed production contains precisely the indefinite cubic gradient term,
with the correct viscous dissipation. It does not yield the missing
arbitrary-data bound. The precise failed positive bridge is controlling
this signed stress/score covariance over macroscopic time using only the
existing entropy and dissipation budgets. This conclusion is obtained from
the kinetic equation, not transferred from a fluid counterexample.

There is also a narrow, genuine prepared-trajectory exclusion: propagation
with no initial slack whose only additive payment is entropy *spent* fails.
An arbitrary input-only additive production term, a bound starting after an
initial layer, and a mixed kinetic compensator remain open.

## 1. Exact spatial Fisher balance on a stated regular class

Write q=log F, a(v)=grad_x q(v), R=F F_*, R'=F'F_*',
A=a+a_*, A'=a'+a_*'. All collision integrals below include dx dv dv_* dσ,
with the unchanged hard-sphere B_nu; there is no velocity truncation. Define

    I_x(F) = integral F |grad_x log F|^2,
    D(F) = (1/4) integral B_nu (R'-R) log(R'/R).

Since M is x-independent, this I_x is exactly the relative spatial Fisher
quantity in the existing consumer. For positive regular F for which these
integrals and the displayed derivatives converge,

    epsilon^2 dI_x/dt = -D_x(F) + C_x(F),                 (1)
    D_x = (1/4) integral B_nu (R+R') |A'-A|^2,
    C_x = -(1/2) integral B_nu (R'-R)
                            (a'.a_*' - a.a_*).

Proof: the variational derivative of I_x is -2 Delta_x q-|grad_x q|^2.
Transport contributes zero by spatial integration by parts. Symmetrize
the collision weak form, using its factor 1/4. The derivative part is
2(R'-R) div_x(A'-A). Integrating it by parts and writing
|a|^2+|a_*|^2=|A|^2-2a.a_* gives (1). Thus the first term has a sign, while
the second is a genuine pair-score covariance creation term.

No collision-invariant mode was damped by assumption. At a local Maxwellian
both R'-R and A'-A vanish, although individual score products need not.
This is the specific reason a homogeneous Fisher argument misses C_x.
The elementary inequality

    (R'-R)^2/(R'+R) <= (1/2)(R'-R) log(R'/R)

only bounds C_x using sqrt(D) times a *fourth-order score moment*. That new
moment is not bounded by entropy. It cannot be omitted from a Young estimate.

For scope: (1) is not asserted by differentiating a GSR renormalized
solution. An adequate regular class is a positive classical local solution
with sufficiently many x derivatives, a Gaussian lower bound, Gaussian
upper bounds on the differentiated perturbation F-M, and spatial polynomial
weights making all terms integrable. One first uses spatial cutoffs and then
exhausts R3. The exact initial jets in Section 2 are Gaussian polynomials
with Schwartz coefficients, so all the displayed initial integrals converge.
Classical finite-epsilon initial segments can be joined to renormalized
continuations; no uniform classical lifespan is needed for that use.

Source inspection for existence: Alexandre--Morimoto--Ukai--Xu--Yang,
*Bounded solutions of the Boltzmann equation in the whole space*,
arXiv:1010.5590v1, Theorem 1.1 and cutoff Remark 1.2, PDF pp. 3--4,
https://arxiv.org/pdf/1010.5590. The theorem supplies local unique nonnegative
solutions with Maxwellian velocity decay and uniformly local H^k regularity,
k>=4; the cutoff remark permits gamma>-3/2, including hard spheres gamma=1.
The smooth shifted Maxwellian satisfies these hypotheses for each fixed
epsilon. This source alone does not state global spatially weighted Fisher
regularity: persistence of the localized perturbation and justification of
the global Fisher Taylor expansion are extra analytic checks identified
below, not silently imported from the abstract.

## 2. An exact initial jet and a scoped additive failure

Put w=v-epsilon U(x), G=grad U with convention G_ij=partial_i U_j,
S=(G+G^T)/2, and B=G^T G. Divergence-free means tr S=0. For symmetric T,
write q_T(w)=w^T T w. Let L_nu be the linearization at M in the convention

    L phi = -M^-1[Q_nu(M,M phi)+Q_nu(M phi,M)].

Its stress Dirichlet form is isotropic:

    <q_S,L q_T>_M = kappa_nu S:T,     tr S=0,             (2)

where kappa_nu>0 is fixed by the calibrated hard-sphere kernel. This is not
the assertion that quadratic polynomials form an invariant eigenspace.
To check (2), use the exact collision Dirichlet form and center/relative
velocities. The center cancels in the collision difference of q_T; angular
integration of the remaining quadratic forms gives S:T and kills tr S.
The constant is positive because a nonzero trace-free quadratic is not a
collision invariant. Gaussian radial integrals are finite for hard spheres.

At time zero Q(F0,F0)=0, and exactly

    F_t(0)/F0 = -v^T G w = -q_S(w)-epsilon U^T G w.

The second term is a collision invariant in w. Galilean covariance gives

    [d/dt Q(F,F)]_0 = F0 L q_S.

Meanwhile the collision-relevant part of the Fisher variational derivative is

    -2 Delta_x log F0-|grad_x log F0|^2
       = -epsilon^2 q_B(w) + (collision invariants).

Therefore the convergent initial-jet calculation gives

    I_x(0)=epsilon^2 ||grad U||_2^2,
    I_x'(0)=0,
    I_x''(0)=-kappa_nu integral S:(G^T G).                 (3)

No fluid equation was used. The scaled acceleration X''(0) is epsilon^-2
times this cubic quantity. The entropy dissipation has the corresponding jet

    D(F(t)) = kappa_nu t^2 integral |S|^2 + o(t^2),        (4)

for fixed epsilon in a class justifying the Taylor expansion. In (4), expand
log(R'/R); its linear coefficient is the collision difference of -q_S.
The linear collision-invariant piece cancels. The Dirichlet form gives (4).
No remainder is claimed uniform in epsilon.

An explicit admissible sign exists. The periodic field

    V(x,y,z)=(sin y,0,sin x+sin(x+y))

is divergence-free and the mean of S:(G^T G) is 1/4. Its periodic vector
potential can be chosen as

    W=(cos(x+y)/2,-cos x-cos(x+y)/2,-cos y).

Let nonnegative nonzero chi be smooth and compactly supported in R3, and set
U_R=-curl(chi(x/R) W(x)). Then U_R is compactly supported and solenoidal.
Its cubic integral equals

    -(R^3/4) integral chi^3 + O(R^2),

so it is negative for large R. The leading term follows by periodic
averaging; every derivative of the cutoff costs R^-1. Thus (3) has positive
sign on genuine admissible input data, without assuming any singularity.

Let E=H(F|M)/epsilon^2. For this datum the jets give

    X(t)-X(0) = a_nu epsilon^-2 t^2 + o(t^2), a_nu>0,
    E(0)-E(t) = b_nu epsilon^-4 t^3 + o(t^3), b_nu>0.

Consequently no finite C, even depending on this entire datum and epsilon,
can give X(t)<=X(0)+C(E(0)-E(t)) for every sufficiently small positive t.
This excludes exactly a no-initial-slack, dissipation-paid propagation law.
It does not exclude X(t)<=C(u0,nu,H), extra input-only slack, or an estimate
only on (delta,H). If only the local existence theorem above is imported,
the global Taylor/no-go statement remains a candidate until the spatially
weighted Fisher differentiability check in Section 5 is completed; the
initial-jet identities themselves are exact convergent calculations.

## 3. Positive repair: resolve the collision-time layer explicitly

The divergent acceleration in (3) is not evidence of divergent total
information on a macroscopic horizon. Set tau=t/epsilon^2 and
f=(F/M-1)/epsilon. The exact equation is

    f_tau + epsilon T f + L f = epsilon Gamma(f,f),
    T=v.grad_x.

Let a=U.v, b_eq=((U.v)^2-|U|^2)/2, and define the explicit microscopic
corrector

    k_tau + L k = -q_S,       k(0)=0,
    k(tau)=-L^-1(1-exp(-tau L))q_S.                       (5)

Here q_S=Ta, and b_eq is the second coefficient of the *prescribed*
Maxwellian. The known identity Gamma(a,a)=L(a^2)/2 gives the cancellation.
The linear collision semigroup acts on the full velocity space. The
stress-tail part of k is not replaced by a finite moment system.

There is an exact, useful remainder equation, not just a Hilbert series.
Write b=b_eq+k and f=a+epsilon b+epsilon^2 r. Then

    r_tau + epsilon T r + L r
      = -T b + 2 Gamma(a,b)
        +epsilon[2 Gamma(a,r)+Gamma(b,b)]
        +2 epsilon^2 Gamma(b,r)+epsilon^3 Gamma(r,r),     (6)

with the exact r(0) obtained by subtracting a+epsilon b_eq from the initial
exponential and dividing by epsilon^2. This is bounded in every fixed
appropriate Gaussian/spatially weighted norm as epsilon tends to zero.
All five collision invariants are retained in r. Its transport symbol is
i epsilon v.k: replacing (6) by a collision-only equation is not uniform
at |k| comparable to epsilon^-1 or above.

Equation (6) identifies a finite-inner-horizon perturbation problem with
input-only source -Tb+2Gamma(a,b). An actual bound on r and its required
weighted derivatives, uniform for 0<=tau<=T_inner with T_inner FIXED,
would justify the next displayed asymptotic. This bounded remainder estimate
is plausible from local cutoff energy estimates but is not supplied here
as a completed theorem. In particular no assertion is made for
T_inner=H/epsilon^2 or for all observation frequencies simultaneously.

Under this explicit remainder bound, the spatial Fisher balance gives

    lim_{epsilon->0} X_epsilon'(epsilon^2 tau)
       = P_tau(U),                                      (7)
    P_tau(U) = <L k,q_B>_(x,v)
                    -2 sum_i <partial_i k,L partial_i k>_(x,v).

Derivation: log(F/M)=epsilon a+epsilon^2(k-|U|^2/2)+O(epsilon^3).
In the Fisher variational derivative the order-epsilon term is a collision
invariant. The microscopic order-epsilon^2 term is
-2 Delta_x k-q_B. Also Q(F,F)=-epsilon^2 M Lk+O(epsilon^3).
Multiply, integrate, and integrate the Delta_x k term by parts to get (7).
This calculation explains why a third-order macroscopic coefficient is not
needed: its potentially lower-order contribution pairs with an exact
collision invariant and vanishes.

For the corrector (5), contraction gives the genuine input-controlled bound

    P_tau(U) <= C integral |grad U|^3                    (8)

uniformly in tau>=0, because Lk=-(1-exp(-tau L))q_S and the second term
of (7) is nonpositive. Thus the resolved initial-layer contribution to X
is O(epsilon^2 T_inner) on fixed collision-time windows if (6) is bounded.
Equation (8) is a rigorous bound for the explicit corrector production;
its transfer to the true solution is gated by the stated remainder check.

## 4. What survives after the initial layer

The stress subspace is orthogonal to ker L. GSR (2.29)--(2.31) supplies
the self-adjoint domain, weighted gap, and five-dimensional nullspace;
(2.52)--(2.53) supplies L^-1 on stress and the viscosity calibration.
These primary statements were read directly at
https://arxiv.org/html/0808.0039v2 on 2026-09-07. They imply
k(tau)->-L^-1 q_S in the needed linearized collision form as tau->infinity.
The constants here depend on the fixed hard-sphere kernel/nu; no spatial
spectral gap on R3 is used.

Gaussian fourth moments and rotational invariance now yield

    lim_{tau->infinity} P_tau(U)
      = -2 integral S:(G^T G)-2 nu ||Delta U||_2^2.       (9)

Indeed <q_S,q_B>=2 S:B, and
<q_S,L^-1 q_S>=2 nu |S|^2 under the GSR viscosity normalization.
For divergence-free U, sum_i ||partial_i S||_2^2=||Delta U||_2^2/2.
This is an exact calculation about the explicit corrector, followed by
an iterated coefficient limit. It is not a uniform approximation on
epsilon^2<<t<=H, and it never inserts an unknown future fluid solution.

The first term of (9) is the indefinite cubic enstrophy production.
Here it has been derived from hard-sphere score/stress relaxation, including
the initial layer, rather than inferred from a fluid no-go. Its absolute
estimate gives at best

    |integral S:(G^T G)|
       <= C ||grad U||_2^(3/2) ||Delta U||_2^(3/2)
       <= (nu/2)||Delta U||_2^2 + C nu^-3||grad U||_2^6.

For the static input U this is a finite input constant. Restarting with an
evolving macro field makes the coefficient a future cubic power of enstrophy;
the known energy budget controls only the first time integral of enstrophy.
Neither (1), (5), nor (6) supplies that missing temporal bound. Replacing
the evolving field by its input value would delete the true nonlinear
macro evolution from the remainder equation.

## 5. Evidence boundary, exact first gaps, next action

Completed algebra: full signed Fisher balance on its specified regular
class; exact prepared initial jets; explicit compact solenoidal sign datum;
exact collision-time corrector and remainder equation; corrector-production
bound and its relaxed cubic/viscous coefficient. The scalar isotropy constants
were checked against the Gaussian norm <q_S^2>=2|S|^2 and the published
viscosity factor 1/10. No finite-Hermite collision eigenspace was assumed.
An independent 24-by-24 periodic quadrature of the full matrix contraction
returned 0.2499999999999998 for the asserted mean 1/4. The scalar identity
used in the Fisher symmetrization passed all 784 integer choices
1<=R,R'<=4 and -3<=A,A'<=3. These bounded checks support the written
algebra; they do not test PDE existence, tail passages, or the terminal bound.

Not completed: a global spatially weighted Fisher differentiability proof
for the selected local solutions, a uniform strong bound for (6) even on
fixed inner windows written to theorem standard, or passage of any Fisher
upper bound to arbitrary GSR weak solutions. The first is needed before
promoting the narrow trajectory no-go; the second before promoting (7)
as an actual-family asymptotic. None of these local technical completions
would control the surviving cubic source on macroscopic times.

The terminal first gap remains an input-only integrated estimate of C_x
after compensation/relaxation, with its actual nonlinear trajectory and all
remainder terms retained. The two-clock monotonicity and linear L2 stress
obstructions were neither reused as global kinetic no-gos nor broadened.

Next distinct positive action: use (1) and (6) to seek a nonlinear stress/score
compensator whose derivative cancels C_x while its equivalence cost and
remainder are controlled from entropy and the true micro/macro evolution.
The target must handle the order-one signed cubic term in (9), not just
remove the initial epsilon^2 layer. If only Gaussian norm estimates on r
are available, state the resulting strain-dependent bound and stop at that
first missing estimate. NS-R3 and C1 are still open; no terminal reduction
or independent mathematical certification is claimed.
