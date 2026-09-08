# Full-state return exclusion modulo a smoothly evolving background

Date: 2026-09-08. Frozen input main:
`bc795c8535b9907e9b75883e7e6635fe8cd8d80f`.
Status: AUTHOR PROOF; independent mathematical audit PENDING.
No canonical graph promotion. The relative-energy method and Chae--Wolf
rigidity are prior art; no exhaustive priority claim is made for this adapter.

## 0. Exact consumer and improvement

The retained-bulk counterexample prevents charging the full normalized L2
norm as an automatically significant critical cost. This note removes that
particular obstruction from the return-block theorem: the first and final
L2 bounds may instead hold for the difference from ONE actual, smoothly
evolving NS background. Its total energy and maximum speed can be arbitrarily
large. The background is never deleted from the original evolution, and it
is not reselected between returns.

The concrete consumer is a construction exclusion:

    long full-state regenerative block, bounded relative endpoint energy,
    controlled full Lipschitz tubes, slowly varying evolved background
      -> positive ORIGINAL full-flow viscous expenditure (Theorem 3);
    additionally controlled full normalized enstrophy
      -> no sufficiently long high-amplitude block (Corollary 4).

This includes vanishing-physical-energy cores sitting on a fixed smooth bulk,
provided the WHOLE difference from that same evolved bulk remains bounded in
the stated endpoint normalization. It does not show that an arbitrary
regenerative exterior has this property. Spatial compactness, small-power
vorticity integrability and a bound on full normalized energy are absent.

The terminal chain remains

    input-only every-upper-time RF-q producer -> exact RF identity -> RF-q
      -> RF-LQ-SYNTHESIS -> RF-LOCAL-ID and Lorentz Fatou
      -> RF-LQ-CONTINUATION -> LOCAL and ENERGY -> NS-R3.

No arbitrary-data producer or blowup-event extraction is supplied here.
The cost still has physical weight a_start^2/K_start. An infinite orbit has
not been constructed or excluded outside the stated class.

## 1. Exact relative equation and a bulk-speed-independent pressure identity

Let U and B be two smooth finite-energy solenoidal ORIGINAL unforced R3 NS
solutions on the same interval with the same viscosity mu>0 and canonical
pressures p_U and p_B. Each may have arbitrary finite H^s norms; no common
bound on ||B||2 or ||B||infinity will enter the theorem. Set

    R=U-B,  q=p_U-p_B,
    p_R=R_i R_j(R_i R_j),
    q_cross=R_i R_j(B_i R_j+R_i B_j).                    (1.1)

In (1.1), R_i R_j before parentheses denotes the two Riesz operators; inside
parentheses the subscripts denote components of the difference velocity.
Thus q=p_R+q_cross, with no independent pressure choice. Direct subtraction
of the two ORIGINAL equations gives

    R_t-mu Delta R+(B+R).grad R+R.grad B+grad q=0,
    div R=0.                                          (1.2)

**Lemma 1 (mixed pressure).** Exactly,

    -Delta q_cross = 2 div[(R.grad)B],
    grad q_cross = -2 (I-P)[(R.grad)B],
    ||grad q_cross||2 <= 2 ||grad B||infinity ||R||2,
    ||q_cross||6 <= 2 C_S ||grad B||infinity ||R||2.     (1.3)

Here the gradient norm in Linfinity is the pointwise operator norm, and
C_S is the homogeneous H1-to-L6 Sobolev constant. Proof: expand the double
divergence of the cross stress, use div R=0, and apply the gradient part of
the Helmholtz projection. The canonical cross pressure is in L2 for each
pair of smooth finite-energy fields, so its dotH1 representative is the
L6 representative in (1.3); a nonzero spatial constant cannot be added.
This proves the displayed estimates. QED.

In particular the mixed pressure does not require a factor ||B||infinity
or ||B||2. A constant vector in place of B has identically zero cross
pressure because div R=0. This cancellation is essential when removing a
large drift in the next lemma.

The full local relative-energy identity is

    partial_t |R|^2 + div[|R|^2(B+R)+2q R]
      = mu Delta |R|^2-2mu |grad R|^2-2 R.(R.grad B).    (1.4)

Its integrated version, with E_R=||R||2^2, is

    E_R(t)+2mu integral_0^t ||grad R||2^2
      =E_R(0)-2 integral_0^t integral R.(R.grad B).       (1.5)

Both the signed background-strain work and the entire viscous defect remain.
This is an identity about the original pair of solutions, not an autonomous
Navier--Stokes equation for R.

## 2. Uniform relative no-atom endpoint lemma

**Lemma 2.** For every finite Ebar,A and m>0 there are r_*,eps_*>0,
depending only on these constants, with the following property. No smooth
pair U,B as above on [-1,0] with viscosity eta>0 can satisfy simultaneously

    sup ||R(s)||2^2 <= Ebar,
    sup_(-1,0) (-s)||grad R(s)||infinity <= A,
    sup ||grad B(s)||infinity <= eps_*,
    eta <= eps_*,
    D_R:=2eta integral_-1^0 ||grad R||2^2 <= eps_*,
    integral_B(x,r_*) |R(0)|^2 >= m for some x.          (2.1)

There is no bound on the energy or speed of B, or on the energy of U.
The thresholds are qualitative, not validated numerical constants.

**Proof.** Negation gives pairs indexed by j with eta_j,D_R,j and
sup||grad B_j||infinity tending to zero, and final mass-m balls whose radii
tend to zero. Solve the background particle equation backwards from the
center of the final ball:

    X_j'(s)=B_j(s,X_j(s)),   X_j(0)=x_j.

Each smooth B_j has a global Lipschitz flow on this finite interval. Its
speed need not be uniformly bounded in j. In moving coordinates put

    r_j(s,y)=R_j(s,X_j(s)+y),
    b_j(s,y)=B_j(s,X_j(s)+y)-B_j(s,X_j(s)).              (2.2)

This translates the WHOLE difference and background. It deletes no velocity
mode or pressure contribution from U_j. Equation (1.2) becomes exactly

    (r_j)_s-eta_j Delta r_j+(r_j+b_j).grad r_j
       +r_j.grad b_j+grad q_j=0.                       (2.3)

There is no acceleration force in (2.3): R is the difference of velocities,
not a velocity with the frame speed subtracted. Its time derivative acquires
X_j'.grad R, which cancels just the constant part of the advecting background.
The cross pressure is unchanged by subtracting that constant, by Lemma 1.
In particular

    |b_j(s,y)| <= eps_j |y|,  ||grad b_j||infinity<=eps_j,
    ||grad q_cross,j||2+ C_S^(-1)||q_cross,j||6
                                      <=4 eps_j sqrt(Ebar). (2.4)

The bound for the sum in (2.4) is just the sum of the two bounds in (1.3).

Finite-energy/Lipschitz interpolation for r_j gives

    ||r_j(s)||infinity <= C Ebar^(1/5) A^(3/5)(-s)^(-3/5). (2.5)

This is integrable in time. On every closed interval below zero, local H1
bounds and (2.3) give local H^(-2) time-derivative bounds. For the background
terms use (2.4) on each fixed ball, not a global bound on b_j. Compactness
then gives r_j -> r in C_t L2_loc after a diagonal subsequence, with global
L2 bound sqrt(Ebar) and the same Type-I Lipschitz bound. The background
transport, background strain, and cross pressure vanish distributionally.

The remaining pressure is the ACTUAL canonical pressure of r. For the
stress r_j tensor r_j, local strong L2 convergence of the products follows
from local convergence and the uniform velocity bound below zero. The
remote pressure and pressure-gradient tails on a fixed ball are bounded
by C Ebar R^(-3) and C Ebar R^(-4), respectively. Taking j to infinity and
then the separation R to infinity identifies R_i R_j(r_i r_j). Thus r
solves original whole-space Euler, with no lost harmonic or remote forcing.
This is only local compactness: tightness of the relative energy at infinity
has not been assumed.

Passing the endpoint requires more than passing the equation. For a fixed
compact smooth test phi, (1.4) in coordinates (2.2) implies

    |integral (|r_j(0)|^2-|r_j(s)|^2) phi|
       <= C(Ebar,A)||grad phi||infinity (-s)^(2/5)
          +eps_j C_phi(Ebar)(-s)
          +eta_j Ebar ||Delta phi||infinity (-s)
          +||phi||infinity D_R,j.                      (2.6)

For clarity, the extra terms are bounded separately. On supp(phi), b_j is
bounded by eps_j times its spatial radius. The strain term is at most
2 eps_j Ebar ||phi||infinity. The cross-pressure flux is bounded using
L6 times L2 times the finite support factor |supp(phi)|^(1/3), and hence
by C eps_j Ebar |supp(phi)|^(1/3)||grad phi||infinity. The remaining cubic
and p_r flux has absolute integral at most C Ebar ||r_j||infinity. These
bounds prove (2.6); no background energy or speed enters.

A weak-* subsequential final measure sigma of |r_j(0)|^2 dx is therefore
the Euler energy trace of r, by first letting j tend to infinity at fixed
s<0 in (2.6), then s tend to zero. The directly inspected Chae--Wolf
Corollary 1.2 [CW] applies to

    r in L-infinity_t L2_sigma intersect
          L-infinity_loc,t W1,infinity,
    sup (-s)||grad r(s)||infinity <= A.

It says this trace has no atoms. The final balls, now centered at zero,
force sigma({0})>=m by compact cutoffs and shrinking their support. This
contradiction proves Lemma 2. QED.

## 3. Relative endpoint energy gives an actual full-flow block cost

Use the CURRENT exact full-state return map and multiplier from the
predecessor no-atom note. Normalize the first scale and amplitude to
K_0=a_0=1, and write U for the single reconstructed original NS flow of
viscosity mu. Each of its N returns has

    a_(n+1)=g_n a_n,  K_(n+1)=lambda_n K_n,
    D_n=a_n K_n^2,  t_(n+1)-t_n=theta_n/D_n,
    ||Q_1 V_n||2=1,
    V_n(y)=O_n^T U(t_n,x_n+O_n y/K_n)/(a_n K_n).        (3.1)

W_n is the corresponding ENTIRE normalized U trajectory on the nth interval.
Translations and rotations are retained, and never change the norms below.
Fix

    M0>=1, L>0, 0<theta0<=Theta,
    lambda0>1, g0>1, gamma_*>0.                         (3.2)

Assume

    theta0<=theta_n<=Theta, lambda_n>=lambda0, g_n>=g0,
    sup_(n,tau) ||grad W_n(tau)||infinity <= L,
    gamma_1(V_N)>=gamma_*.                             (3.3)

Let B be ONE smooth original NS solution with viscosity mu on [0,T], T=t_N.
It is evolved continuously on that interval, not restarted at the returns.
Use the same frames and scales for the normalized difference R_n:

    R_n(y)=O_n^T (U-B)(t_n,x_n+O_n y/K_n)/(a_n K_n).

Replace the predecessor's FULL endpoint-energy hypothesis by

    ||R_0||2, ||R_N||2 <= M0.                           (3.4)

The entire normalized U energy, and intermediate relative energies, need
not be bounded. Impose in FIRST-turnover coordinates only

    sup_[0,T] ||grad B||infinity <= eps_B,
    sup_[0,T] ||grad B||2 <= eps_B.                     (3.5)

These are derivative bounds, not an energy or maximum-speed restriction.

**Theorem 3.** There exist positive eps_B,mu_*,delta_* and an integer N_*,
depending only on (3.2) and the fixed multiplier, such that every such block
with N>=N_* and 0<mu<=mu_* has

    2mu integral_0^T ||grad(U-B)||2^2 > delta_*,
    2mu integral_0^T ||grad U||2^2 > delta_*/4.          (3.6)

The second line is the viscous expenditure of the ORIGINAL full trajectory,
not merely a relative or model dissipation.

**Proof.** Set

    r=g0 lambda0^2,  Tbar=Theta/(1-r^(-1)).

The exact clocks imply theta0<=T<=Tbar and

    (T-t)||grad U(t)||infinity <= L Tbar.               (3.7)

Take eps_B<=1/6 and small enough that

    exp(2 eps_B Tbar)<=2,
    4 eps_B M0^2 Tbar<=1/16.                           (3.8)

The annular support starts at 2/3, so

    ||Q_1 B(0)||2 <= (3/2)||grad B(0)||2 <=1/4.

Thus E_R(0)>=9/16, where R=U-B in the first coordinates. Equation (1.5)
gives sup E_R<=2M0^2. If D_R:=2mu integral||grad R||2^2<=1/8, then

    E_R(T)>=9/16-1/8-1/16>=1/4.                        (3.9)

The full final annulus v=Q_1 V_N has ||v||2=1, and

    gamma_1(V_N)<=||v||infinity||grad v||2
                                      <=(5/3)||v||infinity.

Choose a point with |v|>=b:=3gamma_*/10. Let G be the Schwartz kernel of
Q_1 and C_G=integral |y| |G(y)|dy. Because integral G=0, the normalized
background at endpoint N satisfies

    ||Q_1 B_N||infinity <= C_G ||grad B_N||infinity
                        <= C_G eps_B/(a_N K_N^2).

Choose eps_B also <=b/(2 C_G). Then |Q_1 R_N|>=b/2 at that point. Choose
Rball so M0||1_(|y|>Rball)G||2<=b/4. Splitting the actual convolution and
retaining its tail gives

    integral_B(y,Rball)|R_N|^2 >=m0:=b^2/(16||G||2^2).  (3.10)

By exact relative energy scaling and (3.4), (3.9),

    E_R(T)=(a_N^2/K_N)||R_N||2^2,
    a_N^2/K_N >= 1/(4M0^2).                            (3.11)

Consequently a physical final ball of radius Rball/K_N carries relative
energy at least m0/(4M0^2), without a full-energy bound on U or B.

Apply Lemma 2 to the pair

    U_tilde(s,x)=T U(T(s+1),x),
    B_tilde(s,x)=T B(T(s+1),x),  -1<=s<=0.

Both are original NS with viscosity eta=T mu. Their pressures scale by
T^2, their relative energy and total relative dissipation by T^2. Their
Type-I difference-gradient constant is at most (L+1)Tbar, by (3.5), (3.7).
Use the fixed constants

    Ebar=2Tbar^2 M0^2,  A=(L+1)Tbar,
    m=theta0^2 m0/(4M0^2)

in Lemma 2. Denote its thresholds by r_*,eps_*. Further decrease eps_B
so Tbar eps_B<=eps_*/2. Choose N_* so Rball/lambda0^N_*<=r_*, and set

    delta_*=min(1/8,eps_*/(2Tbar^2)),
    mu_*<=min(eps_*/(2Tbar),delta_*/(8Tbar)).            (3.12)

Any D_R<=delta_* would meet every forbidden condition in Lemma 2. Therefore
D_R>delta_*. Finally, with D_U=2mu integral||grad U||2^2,

    D_R <= 2D_U+4mu integral||grad B||2^2
         <= 2D_U+4mu Tbar eps_B^2 <=2D_U+delta_*/2.

Here eps_B<=1 and (3.12) were used. Thus D_U>delta_*/4. QED.

## 4. Excluding recurrence even when full normalized energy diverges

**Corollary 4.** In addition to (3.3)--(3.5), suppose

    sup_(n,tau)||grad W_n(tau)||2 <=M1.                  (4.1)

There is mu_**>0, depending only on the stated constants, such that NO block
with N>=N_* can start at 0<mu<=mu_**. No bounded full normalized energy or
spatial tightness is required.

Proof. At every endpoint, including intermediate ones,

    ||Q_1 B_n||2 <= (3/2) eps_B/(a_n sqrt(K_n)) <=1/4.

Therefore ||R_n||2>=3/4. The upper relative energy bound from (1.5) gives

    a_n^2/K_n <= (16/9) E_R(t_n) <= (32/9) M0^2.

Using (4.1), the ACTUAL full viscous expenditure obeys

    D_U=2mu sum_n (a_n/K_n) integral_0^theta_n||grad W_n||2^2
       <= C_D mu,
    C_D=8 Theta M1^2 M0^2/(1-g0^(-1)).                  (4.2)

Choose mu_**<=min(mu_*,delta_*/(8 C_D)). Then (4.2) contradicts Theorem 3.
This proves the finite-block exclusion. QED.

**Corollary 5 (escape from every fixed smooth NS background).** Consider an
infinite exact full-state return sequence for ONE original solution u of
fixed physical viscosity nu, with the uniform full derivative tubes, clocks,
gains and efficiency just stated. Its times accumulate at finite T. For
EVERY fixed smooth original NS reference B of the same viscosity on that
interval, with

    sup_(t<T)(||grad B(t)||infinity+||grad B(t)||2)<infinity,

one necessarily has

    (K_n/a_n^2)||u(t_n)-B(t_n)||2^2 -> infinity.          (4.3)

Proof. Otherwise there is an infinite subsequence of relatively energy-bounded
endpoints with a common M0. Start far enough along it. In that endpoint's
coordinates mu_n=nu/a_n tends to zero, and the ENTIRE rescaled reference has

    ||grad B_normalized||infinity <=C/(a_n K_n^2),
    ||grad B_normalized||2 <=C/(a_n sqrt(K_n)).           (4.4)

Both tend to zero, uniformly up to the physical endpoint T. End at another
subsequence member at least N_* returns later. Corollary 4 is contradicted.
The reference is the same original B throughout; its initial data or tail
cannot be reset at the next endpoint. QED.

This rules out a bounded relative return/invariant class over any such smooth
background, even where the full normalized energy diverges. For a fixed
smooth physical bulk h, the harmless-bulk construction at the preceding HEAD
cannot evade this theorem merely through its large energy: any proposed
infinite return would have to develop an unbounded WHOLE normalized difference
from the NS evolution of h. The preceding construction does not supply those
returns and is not contradicted.

## 5. Limits, adversarial tests, and the first remaining theorem

The new exclusion is broader than bounded-full-energy return exclusion. It
is NOT an arbitrary-data regularity theorem. The endpoint condition (3.4)
concerns the WHOLE difference, including every core-generated side mode and
tail. A low-frequency projection or independently evolving daughter is not
substitutable for this difference. R does not evolve autonomously.

The physical full-flow cost in (3.6) remains

    (a_start^2/K_start) (delta_*/4).

It can be summable along infinitely many shrinking cells. The derivative
hypotheses concern the full normalized U tubes and are not extracted from an
arbitrary hypothetical singularity. Neither gamma persistence alone nor a
large core amplitude proves that those singularities have this return form.

The actual pressure identity, physical-space local relative-energy balance,
and the resulting ORIGINAL Euler boundary are the properties not furnished
by Tao's averaged-operator axioms. Mere regeneration is NOT a Tao discriminator:
his averaged construction regenerates. Global energy cancellation alone would
not justify (1.3), (1.4), or importing [CW]. No claim is made that all different
operators fail the same theorem.

No positive regenerative turnover, fixed point, invariant neighborhood,
shadowing theorem, numeric value of N_*, blowup extraction, RF-q upper bound,
or NS-R3 resolution has been obtained. All proofs here are author proofs;
finite symbolic checks are not an independent mathematical audit.

The remaining full-state return must carry exterior that escapes this
same-background relative-energy bound, or violate the controlled tubes/clocks.
The terminal task remains to control that dynamically evolving exterior by
an input-summable CRITICAL cost with event extraction, or to construct and
shadow a robust scale-repeating concentrating orbit. An initial-data theorem
making (3.4) automatic has not been proved and must be falsified before use.

## 6. Inspected primary sources and checking scope

[CW] D. Chae and J. Wolf, *Energy concentrations and Type I blow-up for the
3D Euler equations*, arXiv:1706.02020v2, 21 May 2018.
https://arxiv.org/html/1706.02020v2 . Directly inspected Theorem 1.1,
Corollary 1.2, their whole-space hypotheses and the energy-trace discussion.
Only the finite-energy whole-space Euler Corollary 1.2 is imported here.
The pair compactness, mixed pressure and endpoint passage are proved above.

[T] T. Tao, *Finite time blowup for an averaged three-dimensional Navier--Stokes
equation*, arXiv:1402.0290v3.
https://arxiv.org/html/1402.0290v3 . Inspected the introduction, averaged
operator definition and Remark 1.6. Its modified convection and global energy
cancellation do not supply the original pointwise identities used here.

[L] T. Tao, *254A, Notes 3: Local well-posedness for the Euler equations*,
9 October 2018.
https://terrytao.wordpress.com/2018/10/09/254a-notes-3-local-well-posedness-for-the-euler-equations/ .
Inspected canonical pressure, viscosity-uniform smooth estimates, local
existence and difference estimates. These are local reference facts only.

The new checker verifies finite exact identities: the complete difference and
relative local energy equations, mixed-pressure divergence and gradient
projection, moving-frame cancellation, all scale changes, rational bounds
and cost conversion. It does not certify continuum compactness, [CW], or an
original-NS orbit. Source files, not third-party papers, are committed.
