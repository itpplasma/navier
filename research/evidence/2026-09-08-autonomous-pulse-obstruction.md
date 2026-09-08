# Separated pulses cannot be autonomously born; flat seeds have a large inverse

Date: 2026-09-08. Frozen repository input:
`fedb45a640ea8537aa90578f2cafda9adca01756`.
Status: AUTHOR PROOF, independent mathematical audit PENDING. New to this
repository; no claim of literature priority. No canonical graph promotion.

## 0. Consumer and exact scope

UE0 asks whether the source construction's dynamically effective force can
be removed; UE1 asks for autonomous preparation and a uniform inverse.
Theorem 1 below closes the support-preserving version of that conversion
NEGATIVELY for the ORIGINAL whole-space equation, retaining ordinary positive
viscosity, every harmonic, the entire axisymmetric background, and pressure.
Theorem 2 separately disproves an extension of the source's principal pulse
inverse from envelope-weighted sources to arbitrary flat sources with a
fixed algebraic loss. Theorem 2 is an amplitude-equation theorem, NOT a
full-PDE inverse theorem. Neither result proves arbitrary-data regularity,
constructs unforced blowup, or supplies the RF-q producer.

The resulting smaller preparation problem is to generate the required late
pulses through actual nonaxisymmetric interaction/overlap or a justified
single initial preload. Exact label separation with zero late-label initial
values is no longer an admissible unforced conversion. All former regularity
consumers and their missing input-only producer remain unchanged.

## 1. Exact original-NS no-start theorem

Let R_alpha rotate about the z-axis and define the unitary action on vector
fields by T_alpha v(x)=R_alpha v(R_alpha^{-1}x). Let M be its normalized
angular average. In cylindrical components, M averages the components over
theta, not the Cartesian components in a fixed frame. It is an orthogonal
L2 projection, commutes with dt, Delta and Leray P, and preserves divergence.
An axisymmetric vector field means M B=B; it need not have zero swirl.

**Theorem 1.** On [s,t_*], let U,p,f be a classical finite-energy solution of

    dt U - nu Delta U + (U.grad)U + grad p = f, div U=0, nu>0.

Suppose its ENTIRE velocity has a decomposition

    U=B+sum_gamma W_gamma,  M B=B,  M W_gamma=0,
    div B=div W_gamma=0.                                      (1)

Require enough regularity/decay for the displayed L2 integrations: for
example C_t H^m intersect C^1_t H^{m-2}, m>=4, on compact time intervals,
with f in C_t L2 and the pressure gradient in the corresponding class.
Each label may contain arbitrarily many harmonics and self-interactions.
The sum is locally finite in time in these spaces. Assume the distinct
label supports, including derivative supports, are disjoint in spacetime.
A sufficient concrete hypothesis is smooth extension by zero from pairwise
separated closed spacetime supports; all source support statements below
have this meaning. The background is not held fixed and is not assumed to
solve a separate unforced equation.

Then, for EVERY label, with S(B)=(grad B+(grad B)^T)/2,

    (1/2) dt ||W_gamma||2^2 + nu ||grad W_gamma||2^2
      = -integral W_gamma . S(B) W_gamma
        + <P f,W_gamma>.                                  (2)

In particular, if P f=0 on [s,t_*] and W_gamma(s)=0, then W_gamma is
identically zero throughout [s,t_*]. No uniform bound as t_* tends to a
singular endpoint is assumed: finite strain on each compact classical
interval suffices. The conclusion allows an arbitrarily large background.

**Proof.** Test the full equation against W_gamma. The terms dt B and
Delta B are axisymmetric and hence L2 orthogonal to W_gamma. The same holds
for (B.grad)B, since rotations commute with Euclidean convection. For a
second label, every term that contains its field or a derivative of it has
zero pairing with W_gamma by spacetime support separation. In particular
this removes its time derivative; no independent packet evolution is
silently substituted for the full equation.

The surviving transport terms are (B.grad)W_gamma,
(W_gamma.grad)B, and (W_gamma.grad)W_gamma. The first and third have zero
L2 pairing by divergence cancellation. The middle one is exactly the
quadratic strain term in (2). The pressure pairing vanishes by div W_gamma=0;
this holds for the actual whole-space pressure, without any assumption
that it is local or has the packet support. Also <f,W_gamma>=<P f,W_gamma>.
The Laplacian gives the full nonnegative gradient norm. This proves (2).

Let b(t)=||S(B(t))||_infinity, using the matrix operator norm. If P f=0,
(2) implies E_gamma'<=2b E_gamma. On every compact classical interval b
is integrable. Multiplication by exp(-2 integral_s^t b) and E_gamma(s)=0
therefore give E_gamma(t)=0. All labels and every self-generated harmonic
are retained throughout. QED.

A useful quantitative version, derived from (2) by regularizing sqrt(E), is

    ||W_gamma(t)||2 <= exp(integral_s^t b)||W_gamma(s)||2
       + integral_s^t exp(integral_a^t b)||P f(a)||2 da.     (3)

This is a NECESSARY weighted forcing/preparation estimate, not an
initial-data-controlled continuation estimate. The factor involving b is
not estimated uniformly at blowup and is not advertised as a producer.

**Corollary 1.1 (no support-preserving exactification).** A construction
which keeps (1), the disjoint label supports, and zero initial value for a
future label cannot make the total solenoidal residual zero while retaining
a nonzero pulse in that label. This remains true after arbitrarily large
changes to the shared axisymmetric background, pulse polarizations, mean
corrections, pressure, and harmonics INSIDE the separated supports. It is
not limited to a quadratic source map, leading WKB order, or small data.

**Corollary 1.2 (late bands).** Suppose q(x,t)>=T-t and label ell is supported
where q<=C 2^{-ell}. At any fixed s<T, all sufficiently large labels have
W_ell(s)=0. If a nonzero such label occurs later before T, P f cannot vanish
on that entire intervening time interval. In particular a construction with
nonzero arbitrarily late labels cannot be made unforced just by taking a
smooth late time slice and turning off its force while keeping that flow.

These corollaries do NOT say that the unforced Cauchy problem cannot create
new frequencies. Such creation normally uses overlap and cross interactions,
or uses portions of the initial state not represented by zero future labels.
They also do not say that pressure can be deleted: its full orthogonality
in the energy pairing, not a truncated pressure computation, was used.

## 2. Where the source scheme meets this obstruction

Primary source [OA] below was inspected directly, including its actual
support and pulse inverse arguments. Relevant structural statements:

* Lemma 6.1, (6.13), and the consequence on printed p.66: different labels
  and their derivatives have zero products, also AFTER physical evaluation
  of the auxiliary torus. The support condition is uniform in theta.
* Lemma 7.7: velocities are actual curls, with smooth zero extension and
  nonzero angular harmonics; the full curl remainders are included.
* Proposition 9.3 and pp.104-105: nonzero harmonics retain their label,
  support and envelope; angular means may aggregate labels but remain
  axisymmetric. The subsequent corrections preserve these properties.
* Proposition 9.9 uses cutoffs depending on q and preserves the support
  structure. From (3.2), q-(z^2 q^{2h})=T-t, so q>=T-t.

Thus the complete angular mean is B in (1), including ALL evolving mean
feedback and exterior, and each complete nonzero-angular label is W_gamma.
Theorem 1 applies to any attempted global unforced conversion preserving
these properties. At any fixed initial time the far-future bands vanish,
so retaining any nonzero such band contradicts Corollary 1.1.

This is not an objection to the FORCED source theorem. Its pulse equation
already specifies nonzero initial amplitudes, then cuts them off in time.
The exact principal residual is (OA, (7.40))

    (1-psi) f_m + psi' t_m.                              (4)

For a homogeneous primary pulse this is psi' t_m. Its transverse component
is nonzero on the leading cutoff transition because t_m is transverse,
nonzero there, and psi changes from zero to one. A longitudinal pressure
coefficient cannot cancel that transverse component of the principal
symbol. This last observation is a principal-symbol statement, not by
itself a proof about the whole-space Leray projection. Theorem 1 supplies
the full-PDE statement: all final corrections combined cannot remove EVERY
projected seed force while retaining separated, initially absent pulses.
No claim is made that one particular cutoff term cannot cancel another.

The original source explicitly leaves these small cutoff contributions
as flat additive residuals; it does not claim an unforced causal inverse.
This audit identifies a failure of the proposed conversion, not a proved
error in [OA]'s full forced proof. That proof has not received an independent
or exhaustive line-by-line audit here.

## 3. Flat source does not mean small causal response

This section concerns precisely the principal amplitude problem and does
not replace L_U for the original PDE by that problem.

**Theorem 2.** Let L tend to infinity. Suppose a continuous matrix A_L(v)
on [0,L] has a homogeneous solution h_L'=A_L h_L satisfying

    |h_L(L/2)|>=c0>0,
    |d_v^j h_L(v)| <= C_j L^{b_j} exp(-c (v-L/2)^2/L)     (5)

for each fixed j needed. Let psi_L be a rescaling of one smooth cutoff,
equal to one for |v-L/2|<=L/5, and zero for |v-L/2|>=L/3.
Define the compactly supported amplitude and source

    x_L=psi_L h_L,  g_L=psi_L' h_L.

Then x_L(0)=0 and, EXACTLY,

    (d_v-A_L)x_L=g_L,
    |x_L(L/2)|>=c0,
    ||g_L||C^k <= C_k L^{B_k} exp(-c L/25).               (6)

Consequently the unique zero-initial-data solution operator I_L obeys

    ||I_L||_{C^k -> C^0} >= c_k L^{-B_k} exp(c L/25).      (7)

**Proof.** The product rule and h_L'=A_L h_L give (6). Every nonzero
cutoff derivative is supported at distance at least L/5 from the
midpoint, where (5) gives exp(-cL/25). Leibniz' rule introduces only fixed
powers of L. Causal uniqueness identifies I_L g_L=x_L; evaluation at the
midpoint proves (7). QED.

For the source parameters Q=2^{-ell} and L comparable to ell^2, the sources
in (6) are smaller than every fixed power of Q in every fixed derivative
norm, whereas their causal response has order-one midpoint amplitude.
Thus no estimate

    ||I_ell g||C0 <= C Q^{-M} ||g||C^k                   (8)

can hold for fixed C,M,k on all such flat sources. Cancellation of the
seed source with the SAME zero initial value cancels the entire cutoff
pulse: I_ell(-g_ell)=-x_ell. Giving a different initial value is a different
problem and is precisely the autonomous preparation obligation.

The source's actual matrix equation (7.17), Gaussian envelope (7.16), and
homogeneous solution of Lemma 7.4 satisfy (5), including the nonzero radial
midpoint component. This observation uses those inspected local statements,
not the full singular construction. There is NO contradiction to its
Proposition 7.2: that inverse measures g/P in an envelope-weighted class.
Our g=psi' h is not small in that relative sense merely because its ordinary
norm is flat. Constants are not being transferred between those spaces.

For the direct sum of independent label equations, imposing a fixed finite
number d of linear gauges on the response cannot restore (8). Choose d+1
labels at arbitrarily large scales and their responses x_L. There is a
nonzero coefficient vector annihilating the d gauges; normalize its largest
coefficient to one. In the direct-sum supremum norm the response is at least
c0 while the source is arbitrarily flat. This is a finite-dimensional
linear-algebra consequence for the DECOUPLED amplitude system only, not a
claim about a quotient of the full nonlinear PDE by all possible modulations.

## 4. What remains after both failures

Exact label-separated late starts and a polynomial-loss causal inverse on
raw flat seeds are excluded in the stated classes. The escape is not to
rename the flat residual: allow nonzero continuous prehistory and/or actual
nonaxisymmetric overlap between pulses, and quantify all newly generated
cross terms, means, pressure and diffusion. A single initial datum must
prepare the entire late family, not just any prescribed finite set.

For an unforced counterexample the remaining chain is

    autonomous coupled preparation + uniform full-PDE correction
      -> exact zero solenoidal residual on [t0,T) x R3
      -> one nonzero Schwartz datum and canonical pressure
      -> a preserved singularity and finite maximal lifespan.

NONE of those terminal arrows is filled by the exclusions above. A positive
alternative still needs hypothetical-blowup extraction and an input-only
critical budget before the existing RF-q / Lorentz continuation consumer.
This work supplies no such budget, no recurrent full-state set, and zero
certified positive regenerative turnovers.

Exact original-NS structure used in Theorem 1: local product support,
rotation-equivariant convection, its divergence cancellation, and the full
pressure pairing. Global energy cancellation for an averaged operator alone
does not supply this isolated-label identity. No universal impossibility
result for overlapping or correlated original-NS states is asserted.

## Sources and verification scope

[OA] OpenAI, *Finite Time Blowup for Navier--Stokes*, 165-page PDF,
accessed 2026-09-08:
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Directly inspected: pp.1-16 (statement/outline); pp.63-67 (physical torus
and support separation); pp.73-87 (phase, matrix inverse, homogeneous pulse,
exact curl and cutoff residual); pp.101-116 (residual decomposition, support
preservation and final summation); relevant localization passages in Section
10. Printed pp.1,5,66,78 were also visually checked. This is not a full proof
validation. No third-party PDF is stored in the repository.

The accompanying checker verifies finite product-rule, pressure-pairing,
angular-mode, cutoff, and exponential-comparison identities. It does not
verify function-space hypotheses, the source's continuum construction,
independent review, or a Navier-Stokes numerical orbit.
