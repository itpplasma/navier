# Exact NS circuit tests: delayed leakage and an unavoidable six-carrier ring

Date: 2026-09-08. Input main: `18b3dad2696e8f7ed94bce8fd448851581c0aa5b`.
Status: author derivations; independent mathematical audit PENDING.
These are scoped mechanism obstructions, not a regularity proof, singular
solution, or claim of priority. The original equation is never modified.

## 0. The terminal gate and what this work actually establishes

For the actual whole-space projected family, an input-only bound on RF-q
for one fixed finite q>3 gives the original NS-R3 theorem by the reviewed
Lorentz synthesis, compact-classical identification and continuation suffix.
Alternatively an input-only critical bound on the classical branch suffices.
The missing signed source/response bound is NOT proved here.

We test two proposed steps in a circuit/no-circuit proof: compulsory immediate
leakage of a fixed fraction of a critically large birth, and replacement of a
six-carrier NS cell by its intended six daughters. The first is false even
for real Schwartz data and actual neighboring projected flows (Section 2).
The second discards a rigorously computed, stronger source (Sections 3--5).
That extra source initially INCREASES, not decreases, the critical quadratic
norm (Section 6). None of these facts supplies a sign for its later response.

Thus no positive terminal chain starts with the present results alone.
They eliminate specified steps, not the RF-q strategy or every NS cascade.

## 1. Convention and the two-carrier calculation, including back reaction

Use exp(i k.x), and write Q(u)=-P[(u.grad)u]. For two different carriers
p,q, with complex coefficients a,b perpendicular to their carriers, define

    C+(p,q;a,b)=P_(p+q)[(q.a)b+(p.b)a],
    C-(p,q;a,b)=P_(p-q)[-(q.a)conj(b)+(p.conj(b))a].       (1)

The corresponding NS coefficients are -i C+ and -i C-. Negative modes
are conjugates. All dot products inside (1) are bilinear; norms are Hermitian.

Take p=(1,0,0), q=(0,1,0), a=(0,1,1), b=(-1,0,-1), with negative
coefficients fixed by reality. Direct substitution gives

    C+=(0,0,-2),                 C-=0.                   (2)

Every self-pair and opposite pair is zero by solenoidality. Consequently
the ENTIRE nonlinear derivative of this four-mode datum is supported at
+/-(p+q), with c=Q_(p+q)=2i(0,0,1). There is no hidden difference daughter.

Let R=Q_bilin(u,Q(u))+Q_bilin(Q(u),u), where
Q_bilin(v,w)=-P[(v.grad)w]. Its complete nonzero positive representatives
(and their conjugate negative modes) are

    R_p=(0,0,-2),       R_q=(0,0,2),
    R_(2p+q)=(0,0,2),   R_(p+2q)=(0,0,-2).              (3)

For viscosity nu the complete second derivative is
nu^2 u - 4nu Q(u) + R. Here the parents have squared length one and
the first daughters squared length two. In particular (3) includes the
resolved back reaction, and all genuinely new second-order daughters.

For the full periodic local NS solution the newly generated side-mode
energy divided by first-daughter energy tends to zero quadratically:

    E_side(t)/E_first(t) = t^2/2 + O(t^3).                (4)

Indeed E_first=t^2|c|^2+O(t^3) and
E_side=(t^4/4)(|a.q|^2+|b.p|^2)|c|^2+O(t^5), using
half the sum over positive and negative modes as energy. The old modes in
(3) are not counted as new side modes; Section 2 counts their nonlinear
response as well. This is not an invariant two/three-mode ODE.

There is a useful general calibration. In the plane of p,q write
p=P e1, q=Q(cos(theta)e1+sin(theta)e2),
a=a_t e2+a_z e3, b=b_t(-sin(theta)e1+cos(theta)e2)+b_z e3.
For nonparallel parents of unequal lengths, C-=0 implies C+=0.
For equal lengths and a_t b_t nonzero, C-=0 is equivalent to

    b_z/b_t=-conj(a_z/a_t),
    C+=-2P sin(theta) a_t b_t Re(a_z/a_t) e3.             (5)

To check necessity, the in-plane coefficient of C- is a nonzero geometric
factor times (Q^2-P^2)a_t conj(b_t); its normal coefficient is
-sin(theta)[Q a_t conj(b_z)+P conj(b_t)a_z]. If a tangential
coefficient vanishes, the normal equation either kills the other one or
makes one parent zero, so no unequal-length exception is lost.
Formula (5) also proves |C+| <= P |sin(theta)| |a||b|; equality is possible.
Pairwise zero-interaction classification is prior art [KY]; (2)--(5) are
included as an independently calculated calibration, not a novelty claim.

## 2. An actual Schwartz-data falsifier, also in the refinement family

**Theorem 2.1.** Fix nu>0, L>0 and eta>0. Fix N=6/5. There are a real
solenoidal Schwartz datum d with Fourier support below N and a time t>0
such that the actual whole-space neighboring flows e=u_(2N)-u_N obey

    N^(1/2)||J e(t)||2 >= L,
    ||(I-J)e(t)||2 <= eta ||J e(t)||2,                    (6)

where J projects onto small disjoint balls around +/-(1,1,0), strictly
above N. The same assertion holds, after possibly changing d,t, with e
replaced by u(t)-exp(nu t Delta)d on the original, unprojected NS branch.
The time is inside its classical lifespan. Thus all non-forward nonlinear
response, INCLUDING resolved response, can be relatively arbitrarily small
at a critically large birth. The input changes with L and eta.

**Proof.** Fix a nonzero nonnegative real even phi in C_c^infinity(B1), and
phi_delta(xi)=delta^(-3/2)phi(xi/delta). For the four carriers in (2) put

    f_delta_hat(xi)=P_xi sum_(k in S) a_k phi_delta(xi-k). (7)

For small delta the support avoids zero, so (7) is smooth compactly
supported, real by conjugation, and exactly solenoidal. Its inverse Fourier
transform is Schwartz. Use the unitary exp(-i x.xi) transform; its fixed
convolution normalization factor is denoted kappa_F below.

For any nonzero sum carrier h, rescale xi=h+delta z. Taylor expansion of
the smooth Leray symbols in the finite convolution gives

    Q(f_delta)_hat(h+delta z)
      = kappa_F Q_h(u) (phi*phi)(z) + O(delta),           (8)

uniformly on a fixed compact z set. Each ordered pair is included. Hence
its L2 error is O(delta^(5/2)), whereas a nonzero leading output has norm
of order delta^(3/2). At output zero use the exact divergence form:
the symbol is bounded by |xi| times the convolution of absolute values,
so the entire zero packet also has L2 norm O(delta^(5/2)). Self-pair
packets and the cancelled difference packets have the same small order.
There is no source outside the finite union of these output balls.

Choose J to contain the two radius-2delta output balls at +/-(p+q).
All input packets lie below N, and all initial source packets below 2N.
With F_delta=-(I-P_N)P[(f_delta.grad)f_delta], (2),(8) give

    ||J F_delta||2 >= c delta^(3/2)>0,
    ||(I-J)F_delta||2 <= C delta ||J F_delta||2.          (9)

The identical estimates hold for Q(f_delta) without the coarse projection.
All constants here are for this fixed carrier set and fixed bump.

For d=A f_delta, A>=1, introduce s=A t and viscosity mu=nu/A.
The exact projected solutions scale as u_K(t)=A v_K(s), where v_K has
input P_K f_delta and viscosity mu. The fixed-band polynomial vector
fields and their first two derivatives are bounded uniformly for
mu in [0,nu] on an input-energy ball. Their local Taylor estimate is
therefore uniform in A:

    v_(2N)(s)-v_N(s)=s F_delta+O_delta,nu(s^2) in L2.    (10)

For the original equation the same local estimate holds for
v(s)-exp(mu s Delta)f_delta with F_delta replaced by Q(f_delta).
For clarity this needs no a priori endpoint norm: the elementary integer
H^m energy inequality d_s||v||H^m <= C_m||v||H^m^2, m>=8,
obtained by the product rule, transport cancellation and Sobolev embedding,
gives an input-only common small interval for all 0<mu<=nu. The negative
viscous term is discarded. LOCAL's continuation alternative supplies the
whole interval, and the equation twice differentiated into L2 supplies
a uniform Taylor remainder using these higher input Sobolev norms.
The heat Taylor remainder is uniform for the same reason.

First fix delta making the ratio in (9) smaller than eta/4. Choose a
positive s sufficiently small to make the remainder in (10), after
projection, smaller than eta/4 times s||J F_delta||2 and smaller than
s||J F_delta||2/2. Finally choose

    A >= max(1, 2L/[N^(1/2)s||J F_delta||2]),  t=s/A.

The bounds are uniform in this final choice. They prove (6), and prove
the unprojected assertion identically. Shrinking s further handles large
eta by first replacing it with min(eta,1). This proves the theorem.

This rules out a universal, amplitude-independent compulsory fraction of
non-forward response at every critically large birth, even counting the
resolved correction. It does NOT rule out leakage after an order-one
fraction of parent energy has transferred, after a full turnover, over
many cells, or with an additive cost depending on the full input. In this
construction the transferred fraction of parent energy tends to zero.
There is no one-fixed-datum cascade or blowup in this argument.

## 3. Polarization compatibility on a genuine three-dimensional carrier ring

Fix r,z>0, n=e3, theta_i=2pi i/m and m>=3. Set

    k_i=r e_r(theta_i)+z n, R^2=r^2+z^2,
    M_i=z e_r(theta_i)-r n, T_i=e_theta(theta_i),
    a_i=A_i M_i+C_i T_i !=0, a_(-k_i)=conj(a_i).         (11)

These are three-dimensional carrier configurations. Suppose each pair's
difference interaction vanishes INDIVIDUALLY. This is an explicit clean-cell
assumption; cancellation among different pairs at an identical difference
frequency is not classified by the following theorem.

**Theorem 3.1.** Either every A_i=0, or every A_i is nonzero and

    C_i/A_i=i gamma  for one common real gamma.          (12)

With (12), a non-antipodal pair with angular half-separation h in (0,pi/2)
has sum coefficient

    C+_ij = A_i A_j [-4rz(R^2-gamma^2) sin^2(h)cos(h)
                    /(z^2+r^2 cos^2(h))]
                 [z e_r(theta_mid)-r cos(h)n].          (13)

Every antipodal sum is zero. Self-pairs and zero outputs are zero.
When gamma=+/-R every interaction vanishes (the Beltrami cases).
Otherwise every non-antipodal sum is nonzero and meridionally polarized.
The pure-azimuthal alternative has the same ratios of sum magnitudes,
as follows by taking the gamma limit of (13) with A_i scaled by 1/gamma.

**Proof.** Rotate a pair so its angles are -h,+h. Substitution into (1)
gives for the difference coefficient

    (A_i conj(C_j)+C_i conj(A_j))
          [-2rz sin(h)e_r(theta_mid)+r^2 sin(2h)n].     (14)

The bracket is nonzero for distinct carriers. If any A_i is zero, (14)
forces all others zero. Otherwise let x_i=C_i/A_i. The equations are
x_i+conj(x_j)=0 for i!=j. Using any three indices shows all x_i are equal
and purely imaginary, proving (12). In the same rotated coordinates
k_i+k_j=(2r cos h,0,2z); subtracting its longitudinal component from the
raw convolution gives (13). At h=pi/2 the entire raw sum is longitudinal
and projects to zero. This calculation includes the complex conjugations
in reality, not a real-polarization surrogate.

## 4. Exact all-scale lower bound on the omitted six-carrier forcing

Take m=6 in (11), with equal |a_i| and the hypotheses of Theorem 3.1,
excluding the all-zero-nonlinearity cases. Call adjacent sums the intended
ring T and step-two sums the omitted ring S. There are six distinct sums
in each ring. Their transverse radii are sqrt(3)r and r, respectively,
and their common axial coordinate is 2z. All remaining pair sums and
differences are zero. Negative output rings are supplied by reality.

No sum in T or S can be represented by another unordered pair: a nonzero
midpoint of a chord of a circle determines the chord. Thus arbitrary
phases of the nonzero A_i cannot cancel any named output.

**Theorem 4.1.** For the FULL Leray nonlinearity at this snapshot,

    ||Q_S||2^2 / ||Q_T||2^2
       = 3 (z^2+3r^2/4)/(z^2+r^2/4) > 3.               (15)

Here these are Fourier coefficient sums (or normalized torus L2 norms
when the carriers belong to a lattice). Equal parent magnitudes make
all products |A_i A_j| equal; (13) at h=pi/6 and pi/3 proves (15).
The ratio is independent of the common helical mixture gamma and of
individual phases. In particular eliminating S by that polarization
parameter eliminates T as well.

More generally for m>=5 the step-two ring is at least as strong in L2
as the adjacent ring. With h=pi/m, the ratio of individual magnitudes is

    4 cos(h)cos(2h)
       sqrt[(z^2+r^2 cos^2(h))/(z^2+r^2 cos^2(2h))] >=1. (16)

The first factor is >=1 because h<=pi/5 and
4 cos(pi/5)cos(2pi/5)=1; the second factor is >=1. Each named ring has m
unique outputs. Other rings are retained by the full equation, not deleted.
For m=3 all unordered pairs are adjacent; for m=4 the remaining opposite
pairs vanish. These special counts do not imply invariant trajectories.

### 4.1 Exact comparison with Miller's actual carrier geometry

Miller [M, Section 1.1] uses, with sigma=(1,1,1), permutations of

    k^m=4^m sigma+3^m(1,0,-1),
    h^m=2*4^m sigma+3^m(1,1,-2),
    j^m=2*4^m sigma+3^m(2,-1,-1).

Each level is a regular hexagon about the sigma axis. The intended
adjacent replacement has z_(n+1)=2z_n and r_(n+1)=sqrt(3)r_n,
with a rotation by pi/6. Therefore

    z_n^2=3*4^n, r_n^2=2*3^n,
    rho_n^2=||Q_S||2^2/||Q_T||2^2
       =3[3*4^n+(3/2)*3^n]/[3*4^n+(1/2)*3^n].          (17)

It decreases from 27/7 to 3. Formula (17) is a full-NS calculation,
not an estimate for Miller's restricted equation.

For a rational exact calibration at level zero set
u_k=-i P_k sigma at every permutation k of (2,1,0), and impose reality.
The only positive nonlinear outputs are the permutations of

    T: (3,3,0), (4,1,1);            S: (3,2,1).

Their squared coefficient sums are respectively 216/25 and 5832/175,
with ratio 27/7. The actual restricted model projects S away. Our claim is
not that Miller overlooked these modes: his Appendix D explicitly says
its Fourier space is not invariant under the full equation. The new
calculation here quantifies the omitted source and its polarization rigidity.
Miller's model also has a global-regularity theorem covering ordinary
viscosity; its hypodissipative blowup must not be called original NS blowup.

## 5. Packet localization does not erase the fixed-ring obstruction

For any one fixed nondegenerate ring in Section 4, replace every carrier
by the same bump construction (7), retaining its phase and exact Leray
projection. Apply (8) at every sum center. The finite outputs are separated,
so after orthogonal projection to their radius-2delta neighborhoods,

    ||J_S Q(f_delta)||2^2/||J_T Q(f_delta)||2^2 -> rho^2>3. (18)

This is a theorem about actual real solenoidal Schwartz data, and follows
from an L2 asymptotic with a nonzero denominator, not numerical convergence.
All other output packets remain present. For each fixed ring, sufficiently
small finite delta gives, for example, a ratio bigger than 5/2.
No uniform packet width over infinitely many levels is asserted by (18).
Different envelopes, broad packets, time-dependent preparation and joint
feedback from already occupied daughter rings are not excluded.

## 6. The omitted modes initially add to critical growth

Let a be any finite real solenoidal snapshot supported on one sphere
|k|=R, and suppose Q(a) has no component on that sphere. Let

    S(u)=(1/2) sum_k |k||u_k|^2.

For the full inviscid vector field, writing R_a=DQ(a)Q(a), energy
cancellation differentiated in direction Q(a) gives

    <a,R_a>=-||Q(a)||2^2.

Since |D|a=Ra, the exact nonlinear part of the second derivative is

    S''(0)_nonlinear
       =sum_k (|k|-R)|Q_k(a)|^2.                         (19)

This includes the parents' entire back reaction. At positive viscosity
one obtains exactly the same coefficient for
S(u(t))-S(exp(nu t Delta)a), whose leading term is t^2/2 times (19).
Terms linear in Q pair to zero with a; the pure heat terms cancel.

For the six-carrier ring every nonzero output in T and S lies above R:
its squared length is 4z^2+3r^2 or 4z^2+r^2. Consequently both summands
are positive. In the level-zero rational calibration, (19) is

    2[(sqrt(18)-sqrt(5))*216/25
         +(sqrt(14)-sqrt(5))*5832/175] >0.               (20)

Thus the omitted ring is not a negative signed critical contribution at
birth. Helicity still cancels: the full identities are
<u,Q(u)>=0 and <curl u,Q(u)>=0, by integration by parts and
(u.grad)u=omega cross u+grad(|u|^2/2). No energy/helicity constraint
was relaxed to obtain (19).

This strict sign also has a Schwartz version. In (7),
||(|D|-R)f_delta||2=O(delta), ||Q(f_delta)||2=O(delta^(3/2)),
and ||DQ(f_delta)Q(f_delta)||2=O(delta^3); the last bound follows from
Young's inequality and the L1 Fourier size O(delta^(3/2)) of f_delta.
Energy cancellation is exact before estimating. Subtracting the parent
weight R in (19) therefore leaves an O(delta^4) error, while the strictly
positive leading expression has size delta^3. Thus for sufficiently
small fixed delta the nonlinear critical curvature is strictly positive.
Source supports are disjoint from input supports, so the initial nonlinear
critical derivative is exactly zero. Multiplying the datum by A and using
the input-only small-time estimates of Section 2, with mu=nu/A, shows that
for every fixed nu>0 these data have an actual interval of increasing S
when A is large enough. All modes and the original Riesz pressure are kept.
This is a short-time assertion for varying inputs, not a divergent S bound.

## 7. Three-carrier replication and what was rejected

An independent exact calibration uses k_i=e_i and a_i=(1,1,1)-e_i, with
reality. Its whole first nonlinear derivative is

    Q_(e_i+e_j)=-2i e_l,  {i,j,l}={1,2,3}.

At the next derivative the complete inviscid support is:
old parents +/-e_i; +/- (2e_i+e_j), i!=j; and
+/-(e_i-e_j-e_l). Coefficients are respectively
-2a_i, -2e_l, and the permutations of (-4/3,-2/3,-2/3).
For the last family the representative (1,-1,-1) has coefficient
(-4/3,-2/3,-2/3). The output at (1,1,1) is zero. There are 24
nonzero second-derivative modes, not a closed three-mode circuit.

Retaining only complementary sums gives the carrier recurrence

    k_(n,i)=((2^n-(-1)^n)/3)(1,1,1)+(-1)^n e_i.           (21)

Axial components double and transverse separations stay fixed. For a
regular m-gon adjacent-only recurrence the transverse factor instead is
2 cos(pi/m), while the axial factor is two. This is an exact convolution
constraint; it does not license ignoring cross-generation daughters.
The generated modes just listed rule out exact closure of the three-carrier
trajectory under (21). No global theorem is inferred from angular collapse.

## 8. Checks, Tao discrimination, and the surviving mathematical task

The exact regression `research/check_exact_ns_circuits.py` enumerates EVERY
ordered Fourier pair, checks reality and solenoidality, first and second
mode supports, energy/helicity cancellation, the rational six-carrier ratio,
and the symbolic pair identities. Its test count is arithmetic coverage,
not a PDE proof or an independent audit. No external reviewer or agent
was available for this derivation. Packet and lifespan arguments above
remain author proofs requiring independent review.

Tao discrimination is precise: (1), (13)--(18), and (21) use the unaveraged
constraint k=p+q and the actual P_k numerator, not only cancellation and
Sobolev bounds. Tao's fixed packet pump and rotor coefficients are assigned
in a local cascade operator; they need not satisfy these identities or
produce the ring S. There is an explicit test on his specific operator:
Section 4 places each real psi_i in Fourier balls B_i union -B_i in
1<|xi|<1+epsilon0/2. For epsilon0<1 the self-sum support of
psi_(1,n) lies near zero or twice its carrier, disjoint from psi_(2,n).
Therefore

    <Q_NS(psi_(1,n)),psi_(2,n)>=0,
    <C_Tao(psi_(1,n),psi_(1,n)),psi_(2,n)>
                  =epsilon*(1+epsilon0)^(5n/2) !=0.

The second equality is his actual coefficient (1,1,2,0,0,0) in
Section 6 Table 1, also equation (6.4); the first is the convolution
support calculation just given. Thus an exact step used here fails for
the specific blowup operator, not merely for a hypothetical average.
Common-translation covariance is another valid gate, but was not substituted
for these computations. Passing the gate has supplied mechanism obstructions,
NOT a critical upper bound.

The next concrete circuit question is the signed response of the joint
T/S cell with all cross-generation modes. Norm leakage alone cannot answer
it: (19) shows the initial critical sign is unfavorable. No reduction of
arbitrary blowup to these symmetric cells has been proved. The exact first
TERMINAL gap therefore remains the input-only, every-upper-time bound for
integral Pi_q,M - nu integral D_q,M, uniformly M. Claiming that solving a
single-cell problem already closes that gap would add an unproved
universality assumption. No such implication is claimed here.

## Source ledger

[T] T. Tao, *Finite time blowup for an averaged three-dimensional
Navier-Stokes equation*, arXiv:1402.0290v3,
https://arxiv.org/html/1402.0290v3 . Averaging definition including dilations,
local cascade coefficients, and Section 5 pump/amplifier/rotor inspected.
No averaged-equation continuation theorem is applied to NS or conversely.

[KY] N. Kishimoto and T. Yoneda, *Characterization of three-dimensional
Euler flows supported on finitely many Fourier modes*, arXiv:2110.08039v1,
https://arxiv.org/html/2110.08039v1 . Definition 1.1, Proposition 2.2 and
Theorem 5.1 inspected. Finite exact Fourier support over a time interval
is a much stronger assumption than finitely supported initial data. Their
finite-support theorem is prior art, not a new result of this run.

[M] E. Miller, *Finite-time blowup for the Fourier-restricted Euler and
hypodissipative Navier-Stokes model equations*, arXiv:2307.03434v5,
https://arxiv.org/html/2307.03434v5 . Section 1.1 carrier/polarization
construction, Theorem 1.9 and Appendix D inspected. The restricted equation
is NOT used as the actual evolution in any theorem above.
