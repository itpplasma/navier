# Finite-Lorentz continuation: primary statements and finite-time adapter

Date: 2026-09-07. Source inspection and author proof; independent source
and adapter review passed, independent integration review passed. No canonical graph
claim or terminal theorem is promoted.
Original NS-R3 target and all other frozen worker files are unchanged.

## 1. Result and exact scope

Fix a single q with 3 < q < infinity and a viscosity nu > 0. Let (u,p) be
the canonical classical, normalized-pressure solution of original unforced
NS on R3 with solenoidal Schwartz datum and maximal time Tstar. Then

    Tstar < infinity  and
    ess sup_(0<t<Tstar) ||u(t)||_(L^{3,q}(R3)) < infinity     (LQ)

are incompatible. Thus a bound in any one fixed finite L^{3,q}, q>3,
suffices for continuation. No bound uniform as q tends to infinity is
claimed. The inspected theorems exclude q=infinity.

The proof below uses only the existing classical/energy/Sobolev/Plancherel
package, the distribution definition of Lorentz spaces, and two directly
inspected local theorems of Phuc. In particular it does not first assume
a global weak solution coinciding with the classical branch.

## 2. Inspected primary-source ledger

[P] Nguyen Cong Phuc, *The Navier-Stokes equations in nonendpoint borderline
Lorentz spaces*, [author PDF](https://www.math.lsu.edu/~pcnguyen/papers_html/Phuc_NS_regularity_09_06_15_Simplify_3D.pdf).
Printed pages 1--6, 10--11 and 22--23 inspected. The matching selected
formulas were checked in [arXiv:1407.5129v2 HTML](https://arxiv.org/html/1407.5129),
which makes the closed-cylinder bars explicit. Source statements, paraphrased:

- Definition 1.1, p2: global Leray--Hopf class on (0,infinity): energy
  spaces, weak L2 continuity, solenoidal weak equation, initial energy
  inequality and strong initial L2 trace.
- Theorem 1.7, p5: for that class, finite q>3 and L-infinity_t L^{3,q}_x
  on (0,T) imply smoothness through T. L3 datum additionally gives L5(Q_T).
- Theorem 1.5, p4: on Q1, distributional NS, local energy class,
  p in L2_t L1_x, and L-infinity_t L^{3,q}_x,
  3<q<infinity, imply Holder continuity on CLOSED Q_(1/2).
- Proposition 3.2, pp10--11: suitable NS on Q8 with C(8)+D(8)<=epsilon1
  has universally bounded velocity and derivatives on CLOSED Q_(1/2).
  C(r)=r^-3 integral ||u||_(12/5,B_r)^4 and
  D(r)=r^-3 integral ||p||_(6/5,B_r)^2.

All these statements concern three spatial dimensions, unit viscosity and
zero forcing. They contain no collision model, discretization or cutoff.
The local theorem has no separately assumed suitable-solution hypothesis;
the proposition does. Its suitable class in Definition 2.1 also requires
p in L^{3/2}; the proof below establishes this stronger pressure class. The global definition is why Theorem 1.7 alone is
not applied literally to an unfinished classical branch.

[BS] T. Barker and G. Seregin, *On blowup of nonendpoint borderline Lorentz
norms for the Navier-Stokes equations*, [arXiv:1510.09178 PDF](https://arxiv.org/pdf/1510.09178).
Printed pages 1--4 inspected. Theorem 1.2, p4, asserts divergence of
the L^{3,q} norm as a first blowup time is approached, for 3<=q<infinity,
in R3 or the half-space. The surrounding problem, p2 equation (1.3),
specifies compactly supported smooth solenoidal initial data; the solution
framework is global Leray--Hopf. This is corroboration, not the selected
Schwartz-data interface: compact support is not inferred for a Schwartz
datum. The header of the PDF currently served contains both the arXiv v1
stamp and a later title-page date; no publication-date inference is needed.

These are inspected statements, not independently reproved literature.
The finite-time adaptation below is separate author work.

## 3. Lorentz convention and elementary interpolation

For a measurable vector field f, put d_f(alpha)=measure{|f|>alpha}. Use

    ||f||_(3,q)^q = 3 integral_0^infinity
                           alpha^(q-1) d_f(alpha)^(q/3) d alpha.

The vector magnitude is Euclidean. The weak L3 quasinorm is
K(f)=sup_alpha alpha d_f(alpha)^(1/3).

Monotonicity of d_f on [alpha/2,alpha] proves directly that

    K(f) <= c_q ||f||_(3,q),
    c_q = [q/(3(1-2^(-q)))]^(1/q).                          (1)

For f in L6 with weak L3 quasinorm K, let D=||f||_6. Since

    d_f(alpha) <= min(K^3 alpha^-3, D^6 alpha^-6),

split the layer-cake formula for ||f||_4^4 at alpha0=D^2/K. The two
pieces are bounded by 4K^2 D^2 and 2K^2 D^2, respectively. Zero-norm
cases are immediate. Consequently

    ||f||_4^4 <= 6 K^2 ||f||_6^2.                          (2)

This derivation avoids a new Lorentz interpolation or multiplier interface.

## 4. Normalize viscosity without changing the spatial domain

Suppose for contradiction that Tstar<infinity and (LQ) holds. Set

    Sstar=nu Tstar,
    v(x,s)=nu^-1 u(x,s/nu),
    pi(x,s)=nu^-2 p(x,s/nu).

The chain rule gives unit-viscosity unforced NS for (v,pi) on
R3 x (0,Sstar). Its initial datum remains solenoidal Schwartz, and pi
retains the canonical Fourier pressure normalization. Homogeneity of
the distribution quasinorm gives

    ess sup_(0<s<Sstar)||v(s)||_(3,q) = nu^-1 M < infinity,

where M is the bound in (LQ). The normalized energy estimate is

    sup_s ||v(s)||_2^2 <= ||nu^-1 u_initial||_2^2,
    2 integral_0^Sstar ||grad v||_2^2 <= ||nu^-1 u_initial||_2^2.

The exact energy equality pairs the energy at each smaller time with the
dissipation up to that time. The displayed endpoint dissipative inequality
follows by monotone convergence;
it does not require an endpoint solution value.

## 5. Pressure and suitable local class before the endpoint

Apply (1)--(2) and the existing vector H1 Sobolev inequality. They imply

    integral_0^Sstar ||v(s)||_4^4 ds
      <= 6 c_q^2 (M/nu)^2 S^2
                         integral_0^Sstar ||grad v(s)||_2^2 ds < infinity,

where S is any fixed valid vector Sobolev constant. Thus v belongs to
L4(R3 x (0,Sstar)).

The canonical pressure has Fourier symbol

    pi_hat(xi) = -sum_(i,j) (xi_i xi_j/|xi|^2)
                                     Fourier(v_i v_j)(xi).

For each nonzero xi the Frobenius norm of the displayed matrix is one.
Pointwise Cauchy--Schwarz in its nine tensor entries, then Plancherel,
therefore gives

    ||pi(s)||_2 <= ||v(s) tensor v(s)||_(L2;Frobenius)
                 = ||v(s)||_4^2.

It follows that pi belongs to L2(R3 x (0,Sstar)). No Riesz-transform
bound at a non-L2 exponent was used.

On every bounded cylinder ending at or before Sstar, energy gives the
local velocity class in Theorem 1.5. Finite-volume Holder gives
pi in L^{3/2} of that cylinder and in L2_t L1_x. The equation holds in
distributions there because every compactly supported test is supported
strictly before Sstar, where the solution is classical. Similarly, the
local energy equality holds for every time below the cylinder's upper
endpoint; all its terms are integrable by v in L4, pi in L2 and the
energy bounds. This supplies the suitable class required by Proposition
3.2. Nothing here assumes a value or equation beyond Sstar.

## 6. Prevent an escape of unbounded velocity to spatial infinity

The local theorem alone gives boundedness on bounded spatial sets near
Sstar. A tail argument is still required for a global norm. Define

    F(R)=integral_0^Sstar [
           ||v(s)||_(L4({|x|>R}))^4
            +||pi(s)||_(L2({|x|>R}))^2 ] ds.

The integrability just proved and dominated convergence give F(R)->0.
This is a spacetime tail statement, not an assumed uniform-in-time tail.

Choose delta=Sstar/2 and r>0 so that (8r)^2<delta/2. If |x0|>R+8r
and s0 lies in [delta,Sstar], then Q_(8r)(x0,s0) is wholly within the
allowed time interval and outside B_R spatially. Finite-volume Holder gives

    C(v,z0,8r)+D(pi,z0,8r)
      <= |B1|^(2/3) (8r)^(-1) F(R).                        (3)

The exponents are explicit: L4 to L^{12/5} gives a volume factor 1/6,
raised to the fourth power; L2 to L^{6/5} gives 1/3, squared. Each
resulting volume factor is |B_(8r)|^(2/3).

Take R sufficiently large that (3) is at most epsilon1. Unit-viscosity
parabolic rescaling x=x0+r y, s=s0+r^2 tau, V=r v, P=r^2 pi maps
this cylinder to Q8 and preserves C and D. Proposition 3.2 gives

    |v(x0,s0)| <= C0/r

for s0<Sstar and all such x0, with a continuous endpoint interpretation
provided by the proposition itself. The constants are uniform in the
center and s0. No global weak extension has been inserted.

## 7. Cover the remaining bounded spatial region and continue

Fix rho>0 with rho^2<Sstar/2. For every x0 in the remaining closed ball,
apply the unit-cylinder rescaling of Theorem 1.5 to Q_rho(x0,Sstar).
The global finite Lorentz bound restricts to each ball, and Section 5
checks all pressure and energy hypotheses. The conclusion is Holder
continuity on the CLOSED smaller cylinder, so it supplies a finite bound
through the upper time Sstar, not merely local boundedness at earlier times.

A finite cover of the remaining spatial ball by balls B_(rho/2)(x0)
therefore yields a single bound on that ball for
s in [Sstar-rho^2/4,Sstar). Together with Section 6 this gives

    sup_(Sstar-eta<s<Sstar)||v(s)||_infinity < infinity

for some eta>0. Local classical bounds handle earlier times. Energy now
gives ||v(s)||_3^3 <= ||v(s)||_infinity ||v(s)||_2^2, so the classical
branch has a uniform L3 bound up to Sstar. Undoing the viscosity scaling
gives a uniform L3 bound up to Tstar for u, contradicting the banked
CONTINUATION theorem. This proves the claim in Section 1.

## 8. Audit limits and uniformity

- The fixed finite q>3 hypothesis is used at Theorem 1.5. The elementary
  L4 and pressure steps would also work with bounded weak L3, but the
  inspected local regularity theorem does not cover that endpoint.
- The local conclusions include the upper time boundary, as confirmed in
  the HTML formulas with overline{Q}. An interior-only theorem would not
  justify Section 7.
- The theorem is qualitative. The tail radius and interior covering bounds
  above need not be explicit functions of M alone. Finiteness suffices for
  the continuation contradiction; no cutoff-dependent estimate is hidden
  in a claim of an explicit regularity constant.
- No periodic/half-space adapter is used. Barker--Seregin is not used to
  relax its compact-support hypothesis silently.
- This proves applicability of an inspected literature consumer. It
  produces neither the Lorentz bound (LQ) nor a critically summable
  estimate for the actual approximation family.

Handoff: any correctly proved synthesis into a fixed L^{3,q}, finite q>3,
with a cutoff-uniform bound and local identification, may use this
consumer. The producer remains a separate open mathematical obligation.
