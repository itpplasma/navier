# Whole-space cubic refinement and separated-scale feedback

Date: 2026-09-07. Base: `ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.
Status: integrated author proof; independent component and final integration
audits passed in their recorded scopes. No NS-R3 proof, new singularity restriction, or novelty claim.
The new owner instruction permits model-agnostic parallel mechanisms;
only the controller integrates authoritative research state.

## 1. Exact frontier and the weaker sufficient output

Fix a real solenoidal Schwartz datum d on R3, viscosity nu>0, base frequency
N0>0, and any finite H>0. Write N_j=2^j N0. Let P_N be the sharp orthogonal
Fourier ball projection, P the Leray projection, and u_j=u_(N_j) the exact
whole-space projected flows constructed in Section 2, with u_N(0)=P_N d.
The coarsest approximation u_0 is distinct from the datum d.

For e_j=u_(j+1)-u_j put a_j(t)=N_j^(1/2)||e_j(t)||2. A sufficient output is

    sup_(0<=t<=H) sup_(M>=1) sum_(j=0)^(M-1) a_j(t)^3
        <= K(d,nu,H,N0)^3 < infinity.                         (RF-CUBE)

It suffices to fix N0 once, for example N0=1. The constant may depend on the
full datum, viscosity and horizon. No energy-only or polynomial dependence
is required. RF-CUBE is UNPROVED for arbitrary data.

This replaces the stronger sum_j sup_t a_j(t)<infinity as the active
sufficient refinement interface. It also avoids sum_j sup_t a_j(t)^3:
levels need not peak simultaneously. The spatial synthesis below proves

    sup_M ||u_M||_(L-infinity(0,H;L3))
      <= B^(1/3) N0^(1/2)||d||2 + C_syn K,                    (1)

where, in this note's Fourier convention fhat(xi)=integral exp(-2pi i x.xi)
f(x) dx,

    B=(4pi/3)^(1/2),
    C_syn=(48B)^(1/3) sqrt(2)/(1-2^(-1/2)).

The construction and the direct identification in Section 4 make (1) a
complete conditional consumer into canonical LOCAL/CONTINUATION/ENERGY.
No expanding box, fixed-box gap, kinetic reconstruction or new weak-solution
uniqueness theorem is needed for this route. This removes extra analytic
obligations in the selected architecture; it does not produce its critical
bound or prove a strict reduction of the terminal singularity class.

## 2. One faithful family directly on R3

Define the closed Hilbert space

    X_N={v in L2(R3;R3): P_N v=v, div v=0}.

It is infinite dimensional: choose arbitrarily many symmetric disjoint
Fourier subsets inside the ball, away from zero, with nonzero solenoidal
polarizations. Reality is preserved by the symmetric real Fourier symbols.
The inclusion X_N -> X_(2N) is the reconstruction, with no mesh transfer.
The value of the Leray symbol at xi=0 is immaterial on L2.

For Fourier support in the radius-N ball, inversion and Cauchy--Schwarz give

    ||f||infinity <= B N^(3/2)||f||2,
    ||f||3 <= B^(1/3) N^(1/2)||f||2.                          (2)

P_N and P are contractions on L2 and every Hs, commute with derivatives,
and P_N converges strongly to the identity on Hs. No L3-to-L3 boundedness
of the sharp ball projection is asserted or used.

For a,b in X_N, set B_N(a,b)=P_N P((a.grad)b). Since div a=0,
(a.grad)b=div(b tensor a), where divergence contracts the second tensor
index. Consequently

    ||B_N(a,b)||2 <= 2pi B N^(5/2)||a||2||b||2,
    ||Delta a||2 <= 4pi^2 N^2||a||2.                          (3)

The evolution

    u_N,t = nu Delta u_N-B_N(u_N,u_N),   u_N(0)=P_N d         (4)

is therefore a locally Lipschitz polynomial ODE on X_N. For completeness,
the integral map z -> a+integral_0^t[nu Delta z-B_N(z,z)] is a contraction
on an appropriate closed C_t X_N ball for a time depending only on its
radius, N and nu, by (3). This gives local existence and uniqueness.

Each element of X_N belongs to every Hm and has bounded derivatives. Pair
(4) with u_N, use self-adjointness to remove projections, and integrate
by parts. The convection boundary error with a radius-R cutoff is at most
C R^(-1)||u_N||infinity||u_N||2^2 and vanishes. Thus, for all s<=t,

    ||u_N(t)||2^2+2nu integral_s^t||grad u_N||2^2
      =||u_N(s)||2^2 <= ||d||2^2.                             (5)

The local contraction time on a ball of radius 2||d||2 is independent of
the starting time; restart gives a global solution. The zero datum gives
the zero solution. Smoothness of the polynomial vector field gives smooth
time dependence into X_N, and its continuous embeddings into every Hm
supply joint smoothness through t=0. There is no positive lower bound on
nonzero frequencies in X_N, hence no Poincare gap is used. This construction
in fact needs only real solenoidal L2 data; the terminal datum remains
Schwartz for the canonical LOCAL interface.

The neighboring error lies in X_(2N), so (2) gives the uniform common-space
inverse inequality with radius 2N. Subtracting the exact projected equations,
with v=u_N, U=u_(2N), w=U-v and B_f=B_(2N), gives

    w_t-nu Delta w+B_f(v,w)+B_f(w,v)+B_f(w,w)=F,
    F=-(I-P_N)B_f(v,v),
    w(0)=(P_(2N)-P_N)d.                                     (6)

In particular the initial error need not vanish, and w includes a resolved
correction. No slaving representation is a prerequisite of this family.

## 3. Cubic synthesis with overlapping refinement increments

The spatial lemma requires no PDE or solenoidality. For lambda_k=2^k N0,
k in Z, let Delta_k project orthogonally in L2 onto
{lambda_k/2<|xi|<=lambda_k}. For f in L2 put g_k=Delta_k f and
b_k=lambda_k^(1/2)||g_k||2. Then

    ||f||3^3 <= 48B sum_(k in Z) b_k^3.                       (7)

Proof first for finitely many shells: inversion gives
||g_k||infinity<=B lambda_k b_k. Set

    A_J=B sum_(k<=J)lambda_k b_k,
    T_J=sum_(k>J)lambda_k^(-1)b_k^2.

The low sum has supremum norm at most A_J and the high sum has squared L2
norm T_J. Thus measure{|f|>alpha}<=4alpha^(-2)T_J for alpha>=2A_J>0
(and also for alpha>0 when A_J=0). Partition the layer-cake integral over
[2A_J,2A_(J+1)); repeated endpoints give empty intervals. The distribution
vanishes above A_infinity. Hence

    ||f||3^3 <=24 sum_J(A_(J+1)-A_J)T_J
      =24B sum_k b_k^2 sum_(l<=k)2^(l-k)b_l
      <=48B ||b||_(ell3)^3.

The last step is Holder with exponents 3/2,3 and convolution with the ell1
kernel (1,1/2,...), of norm 2. For general f truncate both shell extremes,
use L2 convergence and an almost-everywhere subsequence, then Fatou.
The zero frequency has no L2 mass. All estimates hold for Euclidean vector
norms and include arbitrarily low frequencies.

Now let finitely many f_j have support in {|xi|<=N_(j+1)}, and set
c_j=N_j^(1/2)||f_j||2. They need not be orthogonal or annular. Since
Delta_k f_j=0 for k>j+1, L2 contraction and the triangle inequality give

    lambda_k^(1/2)||Delta_k sum_j f_j||2
      <=sum_(j>=k-1)2^((k-j)/2)c_j.

Extend c by zero outside its indices. The convolution kernel has ell1
norm sqrt(2)/(1-2^(-1/2)). Combining with (7) yields

    ||sum_j f_j||3 <= C_syn (sum_j c_j^3)^(1/3).               (8)

Apply (8) to e_0,...,e_(M-1) and (2),(5) to the coarse term. This proves
(1), including every resolved correction. The actual paths are continuous
into L2 and L3; partial cubic sums are continuous, so an essential-time
version of RF-CUBE is equivalent to the displayed all-time version.

For a generic time-dependent family, explicitly assume 0<H<infinity,
strongly measurable L2 paths, almost-everywhere stated increment supports,
coarse support in the radius-N0 ball, a bounded coarse L-infinity L2 norm and the essential-time certificate. Norm control
alone does not imply measurable paths. Fixed-band inversion maps L2
continuously to L3, hence these hypotheses give strongly measurable L3
paths. Countably many support and finite-sum conditions share one null set.
The L3 tail is bounded by

    C_syn [sum_(j>=L)a_j(t)^3]^(1/3),

which tends to zero almost everywhere and is at most C_syn K. Therefore
u_M converges in L^q(0,H;L3) for every finite q>=1, by dominated convergence.
Uniform L3 convergence in time is not asserted. Independently, Holder gives

    ||u_M(t)-u_L(t)||2
      <=N0^(-1/2)2^(-L/2)(1-2^(-3/4))^(-2/3)K,  M>L.         (9)

Thus actual continuous paths converge in C([0,H];L2). This also controls
their global L2 tails: the limiting continuous path has compact image, and
uniform convergence transfers spatial tail control to the sequence.

The exponent 3 is optimal for a universal amplitude-only version of (8).
Take a nonzero real solenoidal Schwartz phi supported in the Fourier
annulus {1/2<|xi|<1} and f_j(x)=N_j phi(N_j(x-x_j)). Then c_j=||phi||2 and
||f_j||3=||phi||3. For each finite number m choose the translations so the
cubed L3 norm of the sum approaches m||phi||3^3. This follows by approximating
the finitely many fields in L3 by compactly supported fields and translating
those supports apart. An ellp right side for p>3 would require
m^(1/3)<=C m^(1/p), impossible. This sharpness says nothing about whether
actual NS increments form such families.

Likewise, levels active on disjoint positive-measure time intervals show
why RF-CUBE does not imply uniform-in-time L3 tail convergence. The stronger
sum_j [N_j^(1/2)||e_j||_(L-infinity L2)]^3<infinity would imply that
convergence, but is not needed by the next section.

## 4. Direct local identification and the complete conditional consumer

Fix T<Tstar for the classical branch u supplied by canonical LOCAL. Put
v_N=P_N u, z_N=u_N-v_N and

    R_N=P_N P[(u.grad)u-(v_N.grad)v_N].

Then z_N(0)=0 and the same projected subtraction/testing as in (6) gives

    (1/2)d||z_N||2^2/dt+nu||grad z_N||2^2
      =<R_N,z_N>-integral (z_N.grad)v_N.z_N.                  (10)

Fourier Cauchy--Schwarz gives
||v_N||infinity+||grad v_N||infinity<=C||u||H3 uniformly in N.
For r_N=u-v_N, expand the quadratic difference as
(r_N.grad)u+(v_N.grad)r_N. The H2-to-L-infinity bound then gives

    ||R_N||2 <= C||u||H3||r_N||H2 <= C_T/N,
    ||grad v_N||infinity <= C_T,                              (11)

for N>=1 and t<=T. The constants use only the finite compact-classical
H3 bound here and may deteriorate as T approaches Tstar. The spectral
H2 tail estimate in (11) follows directly by comparing H2 and H3 weights
on |xi|>N. It asserts no Lp ball multiplier theorem.

Apply norm Gronwall to (10), regularizing the norm by
(||z_N||2^2+eta^2)^(1/2) before sending eta to zero. This yields

    sup_(t<=T)||z_N(t)||2
      <=exp(C_T T) integral_0^T||R_N||2 <= C'_T/N.

Together with the spectral tail of u on this interval,
this proves u_N->u in C([0,T];L2). These local comparison constants are
identification constants only; they are not offered as an endpoint bound.

If RF-CUBE holds with an input-only K for every finite H, (1) gives the
SAME critical constant M_H on every compact T<min(H,Tstar). At almost every
fixed t the L2 convergence plus a spatial almost-everywhere subsequence and
Fatou gives ||u(t)||3<=M_H. LOCAL's C_t H1 regularity makes this pointwise
in time. Increase T to min(H,Tstar) without changing M_H. If Tstar were
finite, choose H>Tstar; canonical CONTINUATION contradicts this bound.
LOCAL then supplies normalized smooth pressure and velocity through t=0
on every finite horizon, and ENERGY supplies the global energy clause.

No limit of approximate pressures or weak-solution identification is a
premise of this shorter consumer. The identified branch is already the
original unforced equation. If a separate weak-limit theorem is claimed,
its pressure and energy passages still require their own proof; they are
unnecessary additional dependencies here. NS-R3 remains open because the
hypothesis RF-CUBE has not been produced.

## 5. The exact nonlinear production that remains

For finite M define W_M(t)=sum_(j<M)a_j(t)^3. Pair (6) with e_j and multiply
by N_j^(3/2)||e_j||2. Since the cubed Hilbert norm is C1 also at zero,

    (1/3)W_M'(t)+nu D_M(t)=Pi_M(t),
    D_M=sum_(j<M)N_j^(3/2)||e_j||2||grad e_j||2^2,
    Pi_M=sum_(j<M)N_j^(3/2)||e_j||2
             [<F_j,e_j>-b(e_j,u_j,e_j)],                     (12)
    b(a,b,c)=integral (a.grad)b.c.

The initial W_M(0) is uniformly finite for Schwartz d: the initial errors
are Fourier shells, so a_j(0)<=C N_j^(-1/2)||grad d||2 and the cubed sum
is geometric. A sufficient NEW estimate would be, uniformly in M and for
EVERY upper time 0<=t<=H,

    integral_0^t Pi_M <= theta nu integral_0^t D_M+C(d,nu,H),
    0<=theta<1.                                              (13)

Control only at H is not enough. Neither (13) nor another producer of
RF-CUBE is proved. Indeed set q_j=(P_(j+1)-P_j)u_(j+1),
r_j=P_j u_(j+1)-u_j. Then e_j=q_j+r_j, but the bracket in (12) is

    <F_j,q_j>-b(r_j,u_j,r_j)-b(r_j,u_j,q_j)
                -b(q_j,u_j,r_j)-b(q_j,u_j,q_j).               (14)

The outside factor remains sqrt(||q_j||2^2+||r_j||2^2). Orthogonality does
not delete the four strain terms. The previous universal polynomial
source-linear obstructions do not refute this actual cubic output.

A second exact accounting exposes why separate energy budgets do not close
it. Write d_j=(P_(j+1)-P_j)d and

    C_j(t)=<u_j(t),e_j(t)>+2nu integral_0^t<grad u_j,grad e_j>.

Subtracting individual energy equalities gives

    ||e_j(t)||2^2+2nu integral_0^t||grad e_j||2^2
      =||d_j||2^2-2C_j(t).                                  (15)

Weighted summation of (15) retains the cross correlations C_j. Individual
energy saturation gives only

    sum_(j<M)N_j[||e_j(t)||2^2+2nu integral_0^t||grad e_j||2^2]
       <=4||d||2^2 sum_(j<M)N_j.

This growing upper estimate is not a proof that every sharper estimate
must grow. It locates the unresolved resolved-history correlation.

## 6. A proved bound for actual separated-scale feedback

Let U be any fine projected flow from the same datum, with cutoff at least
N. Put p=P_N U and q=(I-P_N)U. Its actual resolved stress is

    G=-P_N P div(p tensor q+q tensor p+q tensor q).

For 0<K<=N/2, low output forces the other parent high:

    P_K div(p tensor q)=P_K div(p_hi tensor q),
    p_hi=(P_N-P_(N-K))U,

and similarly for reversed tensor order. Indeed |eta|>N and
|xi+eta|<=K imply |xi|>N-K>=N/2. Fourier inversion bounds an integrable
tensor's transform by its L1 norm, so

    ||P_K P div S||2 <= C K^(5/2)||S||1.

Spatial Holder, time Cauchy--Schwarz, the high supports, and (5) give

    integral_0^H||P_K G||2
      <= C K^(5/2) integral_0^H
                   (2||p_hi||2||q||2+||q||2^2)
      <= C K^(5/2)N^(-2)||d||2^2/nu.                         (16)

The constant is absolute, independent of fine cutoff and H. This bounds
the actual forcing into a separated low band, not its nonlinear response.
At K=N/2 the displayed upper bound costs N^(1/2), before resolved feedback
and the critical error weight. The missing gain is in signed near-diagonal
transfer and its correlated response. Deterioration of (16) is not a no-go
for sharper estimates there.

## 7. Source, audit and outcome boundaries

The construction, synthesis, local comparison and (16) are proved above
using elementary Fourier/Hilbert-space arguments. The only imported PDE
consumers are the canonical LOCAL, CONTINUATION and ENERGY interfaces; this
wave does not recertify their literature proofs.

Primary-source comparison: A. Seeger and W. Trebels, *Embeddings for spaces
of Lorentz-Sobolev type*, arXiv:1801.10570v2 (2018), published in Math. Ann.
373 (2019), 1017--1056, https://arxiv.org/html/1801.10570v2 . Inspected
Theorem 1.1(iii), equations (1)--(3), and Remark 1.3. On R3 the choices
s0=1/2,s1=0,p0=r0=2,p1=r1=3,q0=3,q1=2 give the inhomogeneous spatial
embedding B_(2,3)^(1/2) into L3. This is prior art for the embedding, not
an NS or kinetic estimate. The proof above independently handles sharp
shells, ball-supported increments, and the scaled coarse frequency.

Component reviews used fresh contexts and immutable file hashes. They
checked the construction, synthesis/time quantifiers, direct identification,
and separated-scale feedback separately. The synthesis review required an
explicit measurability assumption for the generic family theorem; Section 3
contains it. Actual smooth ODE paths already satisfy it. Audit records are
in `2026-09-07-cubic-refinement-audit.md`; no author rechecking is labelled
independent. No formal proof or numerical PDE certificate is claimed.

Outcome: a direct whole-space approximation family and a weaker sufficient
critical interface, plus a separated-scale transfer bound. These are
component/adapter results. There is no new strict singularity restriction,
no input-only critical producer, and no terminal regularity theorem.
The active next analytic task is the signed simultaneous-time cubic
production (12)--(14), with single-flow band flux as a distinct alternative.
