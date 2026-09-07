# Tao packet obstruction: audit, repair, and exact structural scope

Date: 2026-09-08. Frozen research input:
`0b087fe886d829ecca8a5591232030fcd6df45b0`.

Status: fresh-context audit of the preceding averaging argument: REPAIR
REQUIRED. The proofs below are new author derivations relative to the stated
published inputs; their independent mathematical audit is PENDING. No
canonical node is promoted. NS-R3 is not proved. No novelty claim is made.

## 1. The precise defects in the preceding argument

The old file is preserved byte-for-byte at
`research/history/averaging-obstruction-before-audit-2026-09-08.md`, original
Git blob `501e99d2a7b070252ff791f0651563a42be8e326`.

1. The reviewed finite-q synthesis gives L^{3,q}, not L3. For q>3 the
   latter does not follow, even with a simultaneous L2 bound and smooth
   solenoidal fields. Thus steps 2 and 4 of the old proof are invalid.
   Applying the original-NS continuation theorem to the averaged equation
   would not repair them.
2. The final averaging definition includes independent dilations as well
   as rotations and multipliers. Exact original Fourier-triad geometry is
   not preserved. Fixed compact dilation ranges permit modified estimates,
   not the asserted verbatim transfer of every support identity.
3. A signed inequality's form does not make its proof averaging-invariant.
   The old blanket retirement of every signed-phase or smooth-block method
   was not established. One must examine its actual assumptions. Section 7
   gives an explicit original-NS identity that fails for the counterexample.
4. Tao's checkpoint proposition is stated under a hypothetical global
   solution. Using its checkpoints on the actual maximal branch requires
   a lifespan adapter. Section 4 supplies that adapter instead of silently
   changing the published quantifiers.

The valid conclusion of the averaging argument can nevertheless be proved,
and strengthened, without any Lorentz continuation theorem or interpretation
of a prose statement about Type II blowup.

## 2. Statement of the repaired obstruction

There exist a fixed real symmetric energy-cancelling averaged Euler operator
C, a real divergence-free Schwartz datum d, and a finite H>0 such that, for
EVERY N0>0, the global projected solutions at unit viscosity

    d_t v_N = Delta v_N + P_N C(v_N,v_N),   v_N(0)=P_N d,

with N_j=2^j N0 satisfy

    sup_(0<=t<=H) sup_(j>=0)
        N_j^(1/2)||v_(N_(j+1))(t)-v_(N_j)(t)||2 = infinity.   (T-INF)

Consequently RF-q fails for every fixed finite q>3, as do RF-CUBE and
RF-SUM, for this averaged equation and its own projected family. Here P_N
is the orthogonal Fourier ball projection on R3. The same C,d,H work for
all N0 and q. The viscosity is one; this suffices to refute an assertion
universal over positive viscosities for the averaged class.

This is NOT a counterexample to original NS, and it does not introduce
q=infinity as a continuation criterion for original NS.

## 3. Projected construction and identification with dilations included

Write T_i=M_i Rot_(R_i) Dil_(lambda_i), with
Dil_lambda f(x)=lambda^(3/2) f(lambda x). The averaging has trilinear form

    <C(f,g),h> = E <B(T_1 f,T_2 g),T_3 h>.

For the chosen C it is symmetric in f,g and <C(f,f),f>=0. The lambda_i
lie in one compact subset of (0,infinity); the multiplier norm products
have finite moments. These are the published averaging hypotheses, not
an assumption that transformations preserve every original triad.

Sobolev embedding and the product rule give, on R3,

    ||C(f,g)||2 <= A_C ||f||H1 ||g||H3,                     (3.1)
    ||C(f,g)||H^(s-1)
        <= A_(C,s)(||f||Hs ||g||H3+||g||Hs ||f||H3), s>=3. (3.2)

For (3.1), bound f.grad g by ||f||2||grad g||infinity and
g.grad f by ||g||infinity||grad f||2 before averaging. Each T_i and its
adjoint is bounded on the required Sobolev spaces; the compact dilation
range and integrable multiplier norm products control their costs.
Symmetry of C permits the displayed ordering of f,g. The usual integer
Sobolev product estimate proves (3.2) by the same argument. Only integer
s=3,4,10 is needed below. All operator constants depend on this fixed C.

At fixed N, (3.1) makes Delta v+P_N C(v,v) a locally Lipschitz vector
field on the real solenoidal bandlimited L2 Hilbert space. Its solutions
obey

    (1/2)d_t||v_N||2^2 + ||grad v_N||2^2 = 0.

Projection orthogonality and the cancellation of C prove the identity.
The L2 bound prevents escape from every bounded ball of that Hilbert
space; continuation of the ODE gives a global solution. The space is
not finite dimensional. Sharp Fourier ball boundedness on L3 is unused.

Let u be the maximal classical solution of u_t=Delta u+C(u,u), with
initial datum d, and fix tau<Tstar. Put v=P_N u, r=u-v, z=v_N-v. Then

    z_t=Delta z+P_N[C(z,z)+2C(z,v)+C(v,v)-C(u,u)],  z(0)=0.

The cubic energy term <C(z,z),z> vanishes. The cross term does not vanish:
(3.1) bounds it by A_C ||v||H3 ||z||H1 ||z||2, so Young's inequality
absorbs its gradient contribution and leaves a finite coefficient times
||z||2^2. With M_tau=sup_(t<=tau)||u(t)||H3,

    ||C(v,v)-C(u,u)||2 <= 2 A_C M_tau ||r||H1.

Fourier truncation gives sup_(t<=tau)||r||H1 -> 0. Testing the equation
with z and applying Gronwall therefore proves

    v_N -> u in C([0,tau];L2).                             (3.3)

For N>=1, the H3 bound even gives an O(N^(-2)) forcing bound in this
argument. Neither that rate nor its possibly divergent endpoint constant
is used as a critical estimate. The proof uses no exact support relation
for C's input frequencies.

A bounded H4 norm also prevents finite-time termination of this classical
branch. Indeed, (3.2) and the heat estimate H3 -> H4 with integrable
(t-s)^(-1/2) singularity give a local H4 contraction with lifespan bounded
below on H4 balls. Persistence of H10 follows, for example, by H10 energy
testing using (3.2), absorbing H11 against diffusion, and Gronwall with
coefficient bounded by a constant times 1+||u||H4^2. Starting sufficiently
near a proposed endpoint with a uniform H4 bound extends the same branch
past that endpoint. No critical-space continuation assertion is involved.

## 4. Localising the published cascade checkpoints

The selected C is Tao's local cascade operator represented as an averaged
Euler operator. Put lambda=1+epsilon_0>1. Its real, solenoidal, L2-normalised
Schwartz packets have the form

    psi_(i,n)(x)=lambda^(3n/2) psi_i(lambda^n x),
    X_(i,n)(t)=<u(t),psi_(i,n)>.

Their Fourier supports are disjoint packet sets in annuli
[a lambda^n,b lambda^n], with fixed 0<a<b<infinity. Let E_n be half the
squared L2 norm in the four packet regions at scale n. The solution has
no Fourier component outside their union: both heat propagation and the
cascade preserve that union. Initially d=psi_(1,n0).

The finite-step cascade estimates in the cited source yield checkpoint
amplitudes and times satisfying

    e_n0=1,  t_n0=0,
    lambda^(-1/100)e_(n-1) <= e_n <= lambda^(1/100)e_(n-1),
    0<t_n-t_(n-1) <=100 lambda^(-5(n-1)/2)/e_(n-1),
    X_(1,n)(t_n)=e_n.                                     (4.1)

We must justify their use before Tstar, rather than invoke the global
hypothesis of Proposition 6.3. Here is the additional argument.

Induct on the number of completed checkpoints, retaining ALL checkpoint
hypotheses of that proposition, not just (4.1). The initial checkpoint
lies in the local lifespan. Suppose t_N<Tstar has been reached. Run the
published finite-step bootstrap on the rescaled time interval starting
at t_N, but include termination of the classical lifespan as an additional
possible exit. All preceding identities and finite-time estimates apply
on compact intervals before this exit.

During that bootstrap the high-mode energy condition (6.94) gives, in
unscaled variables and for this FIXED N, a bound of the form

    E_(N+1+m)(t) <= C_N lambda^(-10m),  m>=1,               (4.2)

where C_N is finite and independent of t in the bootstrap interval. It
may depend on N and the preceding amplitude. Low modes are controlled
by total energy. Hence disjoint Fourier support gives

    ||u(t)||H4^2
      <= C sum_k (1+lambda^(8k)) E_k(t)
      <= C'_N + C''_N sum_(m>=1) lambda^(-2m) < infinity.  (4.3)

Thus termination of the classical lifespan cannot be the new exit, by
Section 3. This also handles a lifespan endpoint coinciding with a
bootstrap boundary: after extension, compact-time H10 bounds make only
finitely many high-mode conditions relevant to a first exit, exactly as
in the published finite-step argument. There is no escape to infinitely
many bootstrap conditions before the extension is available.

The remaining exits and checkpoint construction are the published
finite-step estimates (Sections 6.5--6.7); their hypotheses have not
changed. They therefore supply t_(N+1)<Tstar and all the inductive
checkpoint conditions. This proves the localised induction. Notice that
(4.3) is not uniform in N, and cannot be used to continue through the
accumulation of infinitely many checkpoints.

It follows from (4.1) that

    e_n >= lambda^(-(n-n0)/100),
    lambda^(n/2)e_n >= lambda^(n0/100)lambda^(49n/100),     (4.4)
    sup_n t_n <= H0:=100 lambda^(-5n0/2)
                            /(1-lambda^(-249/100))<infinity.

Let Tinf=sup_n t_n. The localised construction gives Tinf<=Tstar. If
Tinf<Tstar, a compact-time H10 bound would instead give
|X_(1,n)(t_n)|<=C lambda^(-10n), contradicting (4.4). Consequently
Tinf=Tstar<=H0. Choose H=H0+1 in Section 2.

Source use is limited and explicit: the published cascade estimates are
inputs; the extra lifespan-exit argument (4.2)--(4.3) is the new adapter.
The adapter and its composition require independent review before this
result is promoted beyond author-proof status.

## 5. A direct packet detector for refinement

This elementary lemma is independent of the equation. Suppose f_j is
supported in the Fourier ball N_j=2^j N0 and f_j -> f in L2. Set

    A=sup_(j>=0) N_j^(1/2)||f_(j+1)-f_j||2.

Let psi_n be L2-normalised and Fourier supported where |xi|>=a lambda^n.
For all sufficiently large n, the coarse term f_0 pairs to zero. Let J
be the first j>=0 for which N_(j+1)>=a lambda^n. All increments before J
pair to zero. Telescoping, L2 convergence, and Cauchy--Schwarz give

    |<f,psi_n>| <= A sum_(j>=J)N_j^(-1/2)
                 = A N_J^(-1/2)/(1-2^(-1/2)).

Since N_J>=a lambda^n/2,

    lambda^(n/2)|<f,psi_n>|
       <= [sqrt(2/a)/(1-2^(-1/2))] A.                     (5.1)

If A is infinite the inequality is interpreted as a trivial upper bound;
the finite-A proof above is the only case needed. No assumption that an
increment is confined to an annulus is made: resolved corrections remain.

Apply (5.1) at each t_n<Tstar to f_j=v_(N_j)(t_n), f=u(t_n). Convergence
is (3.3), which needs only this compact classical time. Equations (4.4)
and (5.1) force the supremum of the weighted increments over t and j to
be infinite. This proves (T-INF). For finite q, each a_j(t)^q is bounded
by sup_M sum_(j<M)a_j(t)^q, so the asserted RF-q failure follows.

In particular, the argument does not use Phuc, ESS, Fatou in a critical
space, or a claim that finite-q synthesis lands in L3.

## 6. What actually diverges, and a smooth solenoidal embedding falsifier

For completeness, the same packet amplitudes imply divergence of weak L3
along the checkpoint times. Rearrangement gives

    |<u,psi>| <= ||u||_(3,infinity) ||psi||_(3/2,1),
    ||psi_(1,n)||_(3/2,1)=lambda^(-n/2)||psi_1||_(3/2,1).

Indeed, bound u*(s) by ||u||_(3,infinity)s^(-1/3) in the rearrangement
integral. Thus (4.4) gives an explicit diverging lower bound for the weak
L3 norm. This is a property of the particular constructed solution, not
an averaged-equation continuation theorem.

The earlier L^{3,q} -> L3 error cannot be repaired just by adding energy
or pointwise smoothness. Fix q>3 and 1/q<alpha<1/3. For small r=|x| put

    w(x)=(-x_2,x_1,0) r^(-2) [log(1/r)]^(-alpha).

Multiply by a fixed smooth radial outer cutoff supported in r<exp(-2),
equal to one for r<=exp(-3), and an inner cutoff vanishing for r<=exp(-m), equal to one for
r>=exp(-(m-1)). The resulting w_m are real solenoidal C_c^infinity fields:
the radial gradient is orthogonal to (-x_2,x_1,0). Their L2 norms and
L^{3,q} norms are uniformly bounded. To see the latter, dominate |w_m|
by r^(-1)[log(1/r)]^(-alpha); its rearrangement near zero is comparable
to s^(-1/3)[log(1/s)]^(-alpha), integrable in L^{3,q} because alpha q>1.
But angular integration on any cone away from the x_3 axis gives

    ||w_m||3^3 >= c integral_3^(m-1) t^(-3alpha) dt -> infinity.

These are fields from different data, not a common-data NS trajectory
and not a counterexample to an input-dependent original-NS estimate.
They isolate precisely the false functional implication in the old proof.

## 7. An exact structural discriminator: common translation

Let T_a f(x)=f(x-a). The original Euler operator obeys

    B(T_a f,T_a g)=T_a B(f,g).                             (7.1)

Differentiation, pointwise multiplication, and the Leray Fourier multiplier
commute with common translation, which proves (7.1).

The fixed local cascade C used above does NOT obey (7.1). Choose real
solenoidal Schwartz f,g with Fourier supports compact and bounded away
from zero, for which C(f,g) is nonzero. Such a pair exists from a nonzero
cascade coefficient and density; equivalently use a nonzero pump input.
In the defining packet expansion of C, only finitely many scales can
pair with f and g. Translations preserve their Fourier supports, so the
same finite set suffices for all a. Each coefficient contains factors
of the form <T_a f,psi_(i,n)> and <T_a g,psi_(k,l)>, which tend rapidly
to zero as |a| tends to infinity (Schwartz cross-correlations). Therefore

    ||C(T_a f,T_a g)||2 -> 0,
    ||T_a C(f,g)||2 = ||C(f,g)||2 >0.                      (7.2)

This proves the claimed failure within real, finite-energy Schwartz data;
no constant velocity outside the data class is substituted.

An additional exact gate test illustrates the distinction. If a real
field f has Fourier support in the two radius-delta*r balls about +/-k,
|k|=r and delta<1/4, then B(f,f) is supported in balls of radius
2*delta*r about 0 and +/-2k. Its projection to the open annulus
(r/2,3r/2) is zero. A same-annulus pump from this one carrier is therefore
not an exact original-NS interaction. Multiple carriers may evade this
particular test; it is not an exclusion of every possible cascade.

The averaging gate must consequently be a gate on proof assumptions,
not on the name of a lane or the syntax of a signed budget. A new argument
using common transport, exact triad matching, or the original pressure
may fail for this C and is not ruled out just because it uses Fourier
blocks. Passing this discriminator is necessary against this counterexample,
not sufficient for regularity. No input-only critical estimate is produced
by (7.1) or by the one-carrier test.

## 8. Sources, checks, and the still-open terminal edge

Primary source: T. Tao, *Finite time blowup for an averaged three-dimensional
Navier--Stokes equation*, JAMS 29 (2016), 601--674; arXiv:1402.0290v3.
https://arxiv.org/html/1402.0290v3
Source inputs: the averaging definition in Section 1.1, (1.12)--(1.15),
Theorem 3.2, the packet definitions, Lemma 4.1, and the finite-step
cascade estimates. The checkpoint quantifiers, (6.13)--(6.15),
(6.25)--(6.27), and the bootstrap conditions (6.92)--(6.95) were checked
directly, including rendered PDF pages 51--52. The remaining published
finite-step estimates are used as literature inputs, not claimed to have
been independently reproved here. No source PDF is stored in the repo.

Repository comparisons: the cubic-refinement construction, finite-Lorentz
synthesis and continuation files dated 2026-09-07. Their original-NS
conditional conclusions are not retracted by the failures of the separate
averaging argument.

`research/check_tao_packet.py` checks exact exponents, dyadic threshold
arithmetic, cancellation versus cross terms, Fourier translation phases,
and the one-carrier support separation. It does not certify Tao's proof,
the lifespan adapter, the PDE convergence proof, or original-NS regularity.
The existing closed-feedback oracle was rerun from its verified frozen
blob `ba8c7d8df16d943bb8738bb12c526acbc282b20e`: 652 assertions passed.
This does not enlarge the mathematical scope of either finite regression.

For original NS the required estimate remains an input-only critical
bound on every finite horizon, obtained using an actual structure absent
from the counterexample. The signed comparable-frequency source/response
term is still uncontrolled. Kinetic endpoint control and microscopic
class/domain adapters are separate unproved obligations. Neither (T-INF)
nor a necessary discriminator closes any of those positive terminal gaps.
