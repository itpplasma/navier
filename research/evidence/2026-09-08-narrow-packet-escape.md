# Narrow packet cascades require a nonperturbative critical exterior

Date: 2026-09-08. Frozen input main:
`c2c34f870ed0fad5f14030629c5bbf5363006f98`.
Status: author proof; independent mathematical audit PENDING.
Scope: original unforced NS on R3, fixed positive viscosity, real solenoidal
Schwartz input. A scoped obstruction to narrow packet shadowing, NOT a proof
of NS-R3, a full-turnover certificate, or a novelty claim.

## 0. The branch being eliminated and the terminal gate

The previous exact ring calculations showed that an intended hexagonal
cascade generates large additional sources. Their mere existence is not a
stabilizing mechanism. This note proves a different quantitative obstruction:
repeated Miller-type *narrow* packet geometry becomes sufficiently collinear
that its entire critical cubic work can be paid for by the ordinary energy
budget. Polarizations and phases need not have the clean-ring form.

All exterior modes are retained in the actual equation. Their total effect
on the critical cubic work is estimated, not projected away. A uniformly
small critical exterior is insufficient to rescue this replication scheme.
Consequently any singular realization must have a nonperturbative high
critical component outside the narrowing packet family, arbitrarily close
to its endpoint. This does not give its sign or rule out such a component.

The complete consumer under the *explicit geometric shadowing hypothesis*
is: Theorems 1 and 2 -> (11), with an energy-controlled exponent -> bounded
dot H^(1/2) -> the already proved spatial cubic synthesis gives L3 ->
canonical CONTINUATION -> LOCAL/ENERGY and normalized pressure -> NS-R3
for that hypothesized solution class. Arbitrary NS is NOT proved to satisfy
the hypothesis. This is a negative test of a named cascade construction,
not a new unconditional positive edge in the terminal graph.

The arbitrary-data terminal producer remains the existing every-upper-time,
M-uniform signed RF-q bound. No assumption about smallness of its full
critical norm, bounded future strain, or an invariant packet subspace is made.

## 1. Definitions and the two estimates

Use the unitary angular Fourier transform exp(-i x.xi), so the product
convolution factor is kappa=(2pi)^(-3/2). Let Lambda=|D| and

    X(v)=||Lambda^(1/2)v||2, Y(v)=||Lambda^(3/2)v||2,
    G(v)=||grad v||2,
    S(v)=X(v)^2/2, D(v)=Y(v)^2,
    T(v)=-<Lambda v, P[(v.grad)v]>.

These definitions use the actual Leray projection. All initial proofs may
be read for real solenoidal fields in every H^m, then extended where the
displayed estimates make sense. Sharp Fourier restrictions of such fields
still have every H^m norm, even though their Fourier symbols are not smooth.
They are legitimate inputs to the trilinear forms below.

Let Gamma be a symmetric measurable subset of nonzero R3. Suppose that for
all L>0,

    |Gamma intersect {L<=|xi|<2L}| <= M L^(12/5),         (1)

and, for almost every p,q in Gamma with 0<|p|<=|q|,

    |p cross q| <= A |p|^(4/5)|q|.                      (2)

Here A,M are finite positive constants. No fixed lower spectral gap is
assumed. Low frequencies may be included by increasing these constants.

**Theorem 1 (geometric critical work).** If g is real solenoidal and its
Fourier support is contained in Gamma, then

    |T(g)| <= C_Gamma G(g) X(g) Y(g),
    C_Gamma=C_* A sqrt(M),                              (3)

where C_* is an absolute finite constant determined by the fixed Fourier
convention and geometric dyadic sums. It is independent of the field,
amplitude, number of occupied shells and any outer Fourier cutoff.

Let mathcal T(f,g,h) denote the symmetric real trilinear polarization of T,
so mathcal T(v,v,v)=T(v).

**Theorem 2 (full mixed exterior estimate).** For arbitrary real solenoidal
f,g,h,

    |mathcal T(f,g,h)| <= C_*' X(f)Y(g)Y(h).             (4)

The designated low-regularity argument f may be any of the three arguments.
In particular, if g=P_Gamma u and h=(I-P_Gamma)u, then

    |T(u)-T(g)| <= C_mix X(h)Y(u)^2.                   (5)

The constant C_mix is absolute. Orthogonality of the two Fourier restrictions
is used in (5), not an assertion that they evolve independently. Equation
(5) includes ALL mixed interactions and the all-exterior cubic term.

The estimates are analytic statements. Finite exact regressions check their
algebraic kernel and exponents, not their universal validity.

## 2. The exact three-frequency cancellation

For p+q+r=0 put a=uhat(p), b=uhat(q), c=uhat(r). Thus p.a=q.b=r.c=0.
All dot products in the following Fourier formula are bilinear. Reality
supplies the conjugations in the original physical-space pairing. The outer
Leray projection disappears ONLY from its pairing with the solenoidal test.

Symmetrizing the six ordered terms gives

    T(u)=Re[-i kappa/6 integral_(p+q+r=0) M(p,q,r;a,b,c)],
    M=(|r|-|q|)(q.a)(b.c)
       +(|p|-|r|)(r.b)(c.a)
       +(|q|-|p|)(p.c)(a.b).                            (6)

For example, the two terms with advector a combine as
|r|(q.a)(b.c)+|q|(r.a)(c.b)=(|r|-|q|)(q.a)(b.c),
because r.a=-q.a. The other two pairs are its cyclic permutations.
This is the full six-term symmetrization, with its factor 1/6; it is not
a restriction to one forward triad. The polarized formula has the same
kernel with its three fields assigned to p,q,r and symmetrized.

Sort |p|<=|q|<=|r|, and write l=|p|, h=|r|. The triangle gives
h/2<=|q|<=h and ||r|-|q||<=l. On Gamma, (2) and solenoidality give

    |q.a| <= A h l^(-1/5)|a|,
    |r.b|=|p.b| <= A l^(4/5)|b|,
    |p.c| <= A l^(4/5)|c|.

Together with (6), this proves

    |M| <= 3 A h l^(4/5)|a||b||c|.                      (7)

Without (2), the same argument gives

    |M| <= 3 h l |a||b||c|.                            (8)

The low factor in (8) is important for mixed high/low interactions. Merely
estimating each unsymmetrized term by h^2 would lose it. The additional
factor l^(-1/5) in (7) uses the original convolution geometry AND transverse
polarizations; energy cancellation by itself does not supply it.

## 3. Summation proving Theorem 1

Let g_j be the sharp L2 restriction to 2^j<=|xi|<2^(j+1), and E_j=||g_j||2.
Sort each interacting triad as in Section 2. The two large dyadic indices
differ by at most two; harmless endpoint enlargements can be absorbed into
that fixed neighbor range. Write L=2^l for the small band and H=2^j for a
large band. Only L<=C H need be summed. Finitely many permutations cost an
absolute constant.

For a triple convolution, Cauchy--Schwarz in the two large frequencies gives

    integral_(p+q+r=0) |ghat_l(p)||ghat_j(q)||ghat_j'(r)|
        <= ||ghat_l||1 E_j E_j'.

By (1), ||ghat_l||1 <= sqrt(M) L^(6/5) E_l. Equation (7) thus yields

    |T(g)| <= C A sqrt(M)
       sum_j H E_j sum_(|j'-j|<=2) E_j'
                    sum_(L<=C H) L^2 E_l.              (9)

The sum has the endpoint power 2 because 4/5+6/5=2.
Cauchy--Schwarz and the geometric sum of L^2 give

    sum_(L<=C H) L^2 E_l
       <= [sum_(L<=C H)L^2]^(1/2) [sum_l L^2 E_l^2]^(1/2)
       <= C H G(g).

The remaining fixed-neighbor sum of H^2 E_j E_j' is at most C G(g)^2.
Finally Plancherel/Cauchy--Schwarz give G(g)^2<=X(g)Y(g). This proves (3).
Low frequencies cause no problem since sum_(l<=j)2^(2l) converges. Begin
with finitely many bands; absolute bounds and the H^m approximation justify
both the full sum and removal of the truncation. No sharp Lp multiplier
bound or finite-dimensional whole-space assumption is used.

## 4. Summation proving Theorem 2, including the difficult placement

Apply (8), still sorting the triad. The ordinary shell volume bound gives
||fhat_l||1 <= C L^(3/2)||f_l||2. Set

    x_l=L^(1/2)||f_l||2,
    y_j=H^(3/2)||g_j||2,
    z_j=H^(3/2)||h_j||2.

If the designated low-regularity field f occupies the smallest frequency,
the resulting term is bounded by a constant times

    (L/H)^2 x_l y_j z_j',  |j-j'|<=2.

For each j, the sum in l is at most C||x||ell2 because the geometric kernel
2^(-2m), m>=0, belongs to ell2. Cauchy--Schwarz in j then gives
C||x||ell2||y||ell2||z||ell2.

If f occupies one of the two large frequencies, the smallest frequency
belongs to g or h. In the former case the bound instead is

    (L/H) y_l x_j z_j',  |j-j'|<=2.

Now use the ell2 kernel 2^(-m) in l and Cauchy--Schwarz in j. The case with
h smallest is identical. This treats the placements for which naive
physical-space Holder would differentiate the low-regularity field.
It proves (4) for the full symmetric trilinear form, not for an arbitrary
individual ordered convection term.

Expand T(g+h)-T(g) into 3 mathcal T(h,g,g), 3 mathcal T(h,h,g), and
mathcal T(h,h,h). Apply (4) with an exterior argument in the X slot each
time. Since Y(g),Y(h)<=Y(u) by orthogonal Fourier restriction, (5) follows
with, for example, C_mix=7 C_*'. There are no unestimated mixed terms.

## 5. Quantitative continuation and its contrapositive

Let u be the canonical original-NS strong branch from d, with maximal time
Tstar. At each time let Gamma_t be symmetric and satisfy (1)--(2) with the
SAME finite A,M. Measurable time dependence is allowed. In particular the
common axis in the application below may change with time.
Put g=P_(Gamma_t)u, h=u-g. No equation for g alone is claimed.

**Theorem 3 (no narrow-packet shadowing with a small critical exterior).**
If, throughout [0,Tstar),

    X(h(t)) <= nu/(4 C_mix),                            (10)

then Tstar=infinity. More precisely, for all t<Tstar,

    S(u(t)) <= S(d) exp(C_Gamma^2 ||d||2^2/nu^2).       (11)

Proof. The actual critical energy equation is S'+nu Y(u)^2=T(u).
Equation (5) and (10) absorb the entire exterior contribution into nu D/4.
Young applied to (3) gives

    |T(g)| <= (nu/4)Y(g)^2
                    +(C_Gamma^2/nu)G(g)^2 X(g)^2.

Orthogonality then yields

    S'+(nu/2)D <= (2 C_Gamma^2/nu) G(u)^2 S.

The ordinary energy identity gives integral_0^t G(u)^2<=||d||2^2/(2nu).
Gronwall proves (11), with no unknown future strain or critical clock.
The spatial shell inequality in the reviewed whole-space cubic-refinement
note gives ||u||3 <= C||(2^(j/2)||u_j||2)_j||ell3 <= C X(u), since
ell2 embeds into ell3. Thus (11) feeds canonical CONTINUATION directly.
LOCAL and ENERGY finish the pressure, trace and energy clauses. QED.

Only the actual S(u) was differentiated. No derivative of Gamma_t or a
moving projection is omitted: the time-dependent split is used solely in
a pointwise trilinear estimate. The same tested estimates hold on actual
Fourier-ball projected flows, but a uniform shadowing hypothesis for that
family is not supplied by this theorem.

### High-frequency escape, not just a large low-frequency remainder

For any fixed K>=1, Gamma_t union B_K still satisfies (1)--(2), with finite
constants that may depend on K. For the volume condition the additional
term is at most C min(L^3,K^3)<=C K^(3/5)L^(12/5). For an angular pair
involving the added ball, its smaller magnitude is <=K, so the trivial
cross-product bound is at most K^(1/5)|p|^(4/5)|q|. The same original
A works for pairs outside the added ball.

Therefore a finite-time singular branch would necessarily satisfy, for
EVERY K>=1 and EVERY t0<Tstar,

    sup_(t0<t<Tstar)
       ||Lambda^(1/2) 1_(|D|>K)(I-P_(Gamma_t))u(t)||2
           > nu/(4 C_mix).                             (12)

Otherwise apply the preceding proof starting at t0 with Gamma_t union B_K.
All starting norms are finite by LOCAL. In particular there are arbitrarily
high-frequency, arbitrarily late, nonperturbative exterior events. A time-
uniform critically small high tail, or a tail uniformly tending to zero
as K grows, cannot shadow a singular narrow-packet cascade.
Equation (12) gives no lower bound for *signed* exterior work. It does not
assert that exterior energy is lost or that events spend disjoint budgets.

## 6. Application: Miller-type packet combs, not a modified equation

Fix a common unit axis n, a base axial frequency z0>0 and C0<infinity.
At generation m>=0 allow a bounded number of packet centers satisfying

    |k_(m,i).n| comparable to z0 2^m,
    |k_(m,i)-(k_(m,i).n)n| <= C0 (sqrt(3))^m,

with axial locations in fixed-width O((sqrt(3))^m) neighborhoods of
+/-(z0 2^m). Let every packet be contained in a ball of radius at most
C0 (sqrt(3))^m about its center. A finite low-frequency ball may be added.
The number per generation and the constants are uniform. Envelopes,
polarizations, relative phases and amplitudes are arbitrary. At each time
the axis and centers may vary subject to the same uniform bounds.

Set alpha=log(3)/(2log(2)). The exact comparison 3^5=243<256=2^8 gives
alpha<4/5. At sufficiently high generations the balls have diameter o(2^m).
Each dyadic shell meets only a bounded number of generations, so

    shell volume <= C L^(3alpha) <= C L^(12/5).

The angle to the axis, modulo sign, is at most C L^(alpha-1). For a pair
with smaller magnitude l>=1, the sine of the angle between them is thus
at most C l^(alpha-1)<=C l^(-1/5). This proves (1)--(2); finitely many
low generations are absorbed into the low ball as in Section 5.

**Corollary 4 (narrow Miller-type packet realization is insufficient).**
An original R3 NS cascade remaining in the preceding packet comb up to a
uniformly perturbative dot H^(1/2) exterior cannot blow up. Any singular
realization must instead satisfy the nonperturbative high-tail condition
(12). This conclusion retains the exterior in the original equation; it
does not impose a Fourier restriction on the dynamics.

For the exact clean hexagon geometry in the earlier circuit note,
z_m^2=3*4^m and r_m^2=2*3^m. Both the intended and initially mandatory side
rings lie in the allowed O(r_m) axial packet neighborhoods. Nothing here
assumes that their later descendants stay there. Indeed the previously
proved transverse births explain one way the full equation can leave it.
The width restriction is substantive: any fixed relative width delta*2^m
eventually exceeds O((sqrt(3))^m), and is NOT covered. Arbitrarily broad
packets, independently rotated axes at different scales, growing packet
multiplicity without a volume bound, and nonperturbative exterior tails
remain possible.

The exponent test exposes the load-bearing improvement. At comparable
scale L, shell volume contributes L^(3alpha/2); the original transverse
symbol contributes L^alpha, for total L^(5alpha/2). It is below the viscous
energy threshold L^2 because 3^(5/4)<4. Dropping the angular gain would
instead give L^(1+3alpha/2), which is above L^2 since 3^3>2^4. Thus this is
not an operator-uniform norm argument that silently also controls Tao's pump.
The discrete axial comb is essential: a continuously filled axial cusp has
a different shell-volume exponent and cannot use this calculation unchanged.

## 7. Scaling, Tao discriminator, and source scope

Under same-viscosity NS dilation u_lambda(x)=lambda u(lambda x), the
support becomes lambda Gamma. Its constants become

    A_lambda=lambda^(1/5)A,
    M_lambda=lambda^(3/5)M,
    C_(lambda Gamma)=lambda^(1/2)C_Gamma.

Since ||d_lambda||2^2=lambda^(-1)||d||2^2, the exponent in (11) is invariant.
X(h) and the threshold in (10) are invariant as well. There is no inference
that high resolution alone makes an arbitrary NS critical amplitude small.

The exact step unavailable to the specific Tao cascade is (6)--(7): a
single common convolution triple and transverse polarization on its actual
wavevectors. The repository's directly inspected discriminator is

    <Q_NS(psi_(1,m)),psi_(2,m)>=0,
    <C_Tao(psi_(1,m),psi_(1,m)),psi_(2,m)>
                         =epsilon*(1+epsilon0)^(5m/2) !=0.

Original self-convolution has support near zero/twice the input carrier,
disjoint from that same-annulus second packet. Tao's Table 1 and (6.4)
assign the nonzero pump. Energy cancellation alone is shared and is NOT
the discriminator. We do not claim Tao's particular packets themselves
satisfy the narrowing-comb assumption of Corollary 4.

Primary sources inspected directly in HTML in this run:

* T. Tao, Finite time blowup for an averaged three-dimensional Navier--Stokes
  equation, arXiv:1402.0290v3, https://arxiv.org/html/1402.0290v3 .
  Operator/trilinear definition, Table 1 and (6.4). Its equation is averaged,
  not original NS; its endpoint theorem is not used as an original consumer.
* E. Miller, Finite-time blowup for the Fourier-restricted Euler and
  hypodissipative Navier--Stokes model equations, arXiv:2307.03434v5,
  https://arxiv.org/html/2307.03434v5 . Section 1.1 supplies the carrier
  geometry; Section 4.2 already proves regularity for its restricted model
  in a regime including ordinary viscosity; Appendix D states that the
  constraint space is not invariant under full NS. Those are prior art,
  not discoveries here. The present proof concerns positive-volume R3
  packets, arbitrary polarizations, and a retained critical exterior.

No claim of exhaustive prior-art review is made. Standard trilinear
cancellations/small critical perturbations are not claimed novel. The
specific contribution to this programme is the robust quantitative exclusion
of its narrow replicated packet geometry, not a new general NS solution.

## 8. Audit limits and the remaining full-turnover nut

Author checks reconstructed the six-permutation factor, complex reality
convention, high-field placement in (4), all low/high dyadic sums, every
mixed term, viscosity absorption, time-dependent-set treatment, the low-ball
extension and scaling. `research/check_narrow_packet_escape.py` checks exact
algebra and exponent regressions. It is not an independent mathematical audit.

The existing numerical hexagon locator still lacks a continuum lifespan and
response certificate at t=.25. This run examined the full unretained residual
rather than just boundary energy: at N=18 the unvalidated residual is not
small enough for the straightforward attempted high-Sobolev posteriori bound.
That failure of these attempted estimates is NOT a no-go theorem for rigorous
validation, and no finite-event conjecture is marked solved or disproved.

The next cascade must genuinely carry the nonperturbative exterior, rather
than rename it a negligible error. The dominant open question is a full
turnover/repetition map for the resulting angularly broad, changing-
polarization network, including its return channels. Alternatively one must
prove a signed cost for those compulsory exterior events that sums into the
actual RF-q production. Neither task is discharged here. No universal
reduction of arbitrary singularity to this packet comb is assumed.
