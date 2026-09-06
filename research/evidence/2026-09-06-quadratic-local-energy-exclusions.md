# Terminal tests: no coercive quadratic Lyapunov form; the local-energy-only obstruction

Date: 2026-09-06.
Frozen research input: `545e7a4b415095e3c798ed96fb1530f1994ad210`.
Status: complete author derivation of the quadratic obstruction; source-checked
NS-inequality construction with an author-derived critical-norm consequence.
Independent mathematical audit: pending. No novelty or priority claim.
Terminal theorem: not proved. Terminal obstruction: unchanged.

This note is research evidence, not a promoted graph node. It preserves the
previous scalar-balance and intrinsic-tangent results. The two exclusions
below have DIFFERENT premise classes and must not be combined into a
counterexample satisfying their union.

## 1. Terminal gate and the mechanisms tested

The target is NS-R3: every positive viscosity and every solenoidal Schwartz
datum on R3 give a global smooth solution of the ORIGINAL unforced equation,
with kinetic energy bounded by its initial value. LOCAL, ENERGY and
CONTINUATION in `docs/proof-graph.yaml` provide the complete suffix once

$$
 \sup_{0\le t<\min(H,T_*)}\|u(t)\|_3
       \le F(u_0,\nu,H)<\infty                                      \tag{1}
$$

is proved from the inputs, for every finite H. A direct contradiction to a
finite maximal time could instead bypass (1). No such producer is proved here.

**Quadratic Lyapunov mechanism.** A fixed quadratic functional Q, coercive in
L3 and nonincreasing on every actual classical NS branch, would give
`||u(t)||_3^2 <= Q(u0)/c`, so CONTINUATION, LOCAL and ENERGY would finish
NS-R3. Sections 2--7 exclude this entire class under a finite Sobolev
continuity assumption. Neither translation invariance nor scale invariance
is assumed of the original functional. The exclusion is on actual local NS
solutions, not on a scalar countermodel.

**Local-energy transport/packing mechanism.** A derivation of (1) using only
solenoidality, the canonical pressure, the local energy inequality, finite
energy/dissipation and spatial tightness would also apply to NS-inequality
fields. Section 8 shows that such a derivation is impossible: the branching
Scheffer--Ozanski construction has unbounded L3 despite those premises.
This fills a specific scope gap left open by the previous comparison curves;
it does NOT add the local energy inequality to those same curves.

**Analytic-envelope mechanism.** Input-only bounds
`rho >= rho_*>0` and `||exp(rho |D|)u||_2 <= K`, uniform before the endpoint,
would give `||u||_infinity <= C rho_*^(-3/2) K` by Fourier Cauchy--Schwarz.
Together with ENERGY, `||u||_3^3 <= ||u||_infinity ||u||_2^2` would give (1).
The hardest obligation is the quantitative envelope K, not merely a
positive analyticity radius. Indeed, take a nonzero
`W = curl(exp(-|x|^2) e3)` and `w_r(x)=r^(-3/2)W(x/r)`. These are solenoidal,
Schwartz and entire; their exponentially weighted Fourier L2 norms are
finite at every fixed radius. Yet `||w_r||_2=||W||_2` and
`||w_r||_3=r^(-1/2)||W||_3 -> infinity`. This rejects the radius-only
inference, not a quantitative analytic-norm method or an actual NS
trajectory. No envelope producer was obtained, so this is not an approved
terminal route and no analytic side machinery is developed.

These are different mechanisms. None is renamed and pursued after its
failed implication. The important new author theorem is the quadratic
class exclusion, not the number of candidates screened.

## 2. Precise quadratic no-go theorem

Write `H^m_sigma` for the real Hilbert space of solenoidal vector fields in
`H^m(R3;R3)`. Fix an integer m>=1 and a viscosity nu>0. The integer choice
loses no functional continuous in some finite nonnegative Sobolev norm:
one may increase the exponent to an integer at least one.

**Theorem Q.** There is no continuous symmetric real bilinear form B on
`H^m_sigma`, with `Q(v)=B(v,v)`, satisfying both:

* For a constant c>0, `Q(v) >= c ||v||_3^2` for every `v in H^m_sigma`.
* On the actual local classical NS solution from every solenoidal Schwartz
  datum, Q(u(t)) is nonincreasing, even just on its initial existence interval.

B and c may depend on the fixed viscosity. B is the same for all data and
is independent of time. It is not assumed to be translation invariant,
rotation invariant, local, a scalar Fourier multiplier, or homogeneous
under Navier--Stokes scaling. Continuity means that for some finite C,

$$
 |B(v,w)|\le C\|v\|_{H^m}\|w\|_{H^m}.                           \tag{2}
$$

Consequently the theorem excludes, in particular, anisotropic matrix
Fourier weights, inhomogeneous Sobolev energies, and fixed spatially
inhomogeneous quadratic forms satisfying (2), whenever L3 coercivity is
claimed. It does not assert a classification of every Euler invariant.

## 3. Actual NS data force cancellation of the cubic transfer

Let P be the Leray projection and set
`N(w)=P((w dot grad)w)`. For a smooth compactly supported solenoidal w,
LOCAL supplies an actual classical branch from `a w`, for every real a.
Its derivative at zero is `nu a Delta w - a^2 N(w)`. All these quantities
belong to H^m, and LOCAL justifies differentiating Q there. Thus

$$
 \left.\frac{d}{dt}Q(u(t))\right|_{t=0}
 =2\nu a^2 B(w,\Delta w)-2a^3 B(w,N(w)).                        \tag{3}
$$

Monotonicity for arbitrarily large positive AND negative a forces

$$
                 B(w,N(w))=0                                  \tag{4}
$$

for every such w. A nonzero cubic coefficient would make (3) positive for
one sign and sufficiently large magnitude of a, regardless of the
quadratic viscous term. This uses different admissible initial data; it
DOES NOT assert that velocity sign reversal is a solution symmetry.
No inviscid limit or NS blow-up assumption enters (3)--(4).

## 4. Translation averaging without assuming orbit compactness

The purpose of this step is to remove the translation-invariance
hypothesis, not to obtain compactness of NS trajectories.

Put `tau_y v(x)=v(x-y)` and, for R>0, define

$$
 B_R(v,w)=\frac1{|B_R(0)|}\int_{B_R(0)}
                  B(\tau_y v,\tau_y w)\,dy.                    \tag{5}
$$

The integrand is continuous in y. Translations are isometries of H^m and
L3, so every B_R has the same bound (2), the same lower bound
`B_R(v,v)>=c||v||_3^2`, and the cancellation (4). The last assertion uses
`N(tau_y w)=tau_y N(w)` and the fact that translated test fields remain
compactly supported.

Choose a countable dense subset of H^m_sigma and a sequence R->infinity.
A diagonal subsequence makes B_R converge on all pairs of elements of that
subset. The uniform bound (2) extends the limit to a continuous bilinear
form B_infinity and gives convergence on EVERY fixed pair in H^m_sigma.
It is symmetric, has the same coercivity, and still satisfies (4), since
`(w,N(w))` is such a fixed pair.

For any fixed translation z,

$$
 |B_R(\tau_z v,\tau_z w)-B_R(v,w)|
 \le C\|v\|_{H^m}\|w\|_{H^m}
       \frac{|(B_R(0)+z)\mathbin\triangle B_R(0)|}{|B_R(0)|}
 \longrightarrow0.                                           \tag{6}
$$

Hence B_infinity is translation invariant. This is a fully specified
weak-operator compactness argument for uniformly bounded bilinear forms.
It does not assume spatial tightness, a critical bound, or compactness of
a nonlinear solution orbit.

## 5. Full orthogonal averaging and the radial multiplier

For an orthogonal matrix R, let `T_R v(x)=R v(R^T x)`. The map N is
covariant under T_R, including reflections. Average B_infinity over the
compact group O(3), with probability Haar measure:

$$
 \overline B(v,w)=\int_{O(3)}
               B_\infty(T_Rv,T_Rw)\,dR.                       \tag{7}
$$

This retains (2), L3 coercivity and (4), and is both translation and O(3)
invariant. Full O(3), rather than only SO(3), is essential below.

Here are the multiplier details, including the low-frequency scope.
Extend the form to all vector-valued H^m by inserting P in both slots,
and transfer it to L2 with the isometry `J=(1-Delta)^(m/2)`. The resulting
bounded self-adjoint operator commutes with translations. Complexify it
in the usual sesquilinear way. After Fourier transformation it therefore commutes with multiplication by every
character `exp(i y dot xi)`. The spectral projections of the three
coordinate multiplication operators, and then bounded simple functions,
give commutation with all scalar L-infinity multipliers. Entry by entry,
a bounded operator with this property is multiplication by an essentially
bounded measurable matrix: on each finite-measure set apply it to its
indicator, use commutation with indicators of subsets, and exhaust R3 by
nested finite-measure sets. This also proves agreement of the matrix
representatives on overlaps and their essential boundedness.

Returning through J gives a measurable Hermitian matrix symbol M(xi),
with `M=P M P` and `||M(xi)|| <= C(1+|xi|^2)^m`. The O(3) average supplies
an equivariant representative for almost every radius: integrate the
symbol on each sphere and use Haar invariance. At a fixed nonzero xi,
the stabilizer acts as the full group O(2) on the transverse plane.
Reflections in that plane kill the off-diagonal entries; interchange of
its axes makes the diagonal entries equal. Hermitian symmetry makes that
common entry real. The longitudinal component is zero. Therefore

$$
 M(\xi)=q(|\xi|)P(\xi),\qquad
 |q(r)|\le C(1+r^2)^m,                                        \tag{8}
$$

for a real measurable q, and

$$
 \overline B(v,v)=\int q(|\xi|)|\widehat v(\xi)|^2\,d\xi.       \tag{9}
$$

The Fourier transform is unitary. The possible value at xi=0 is irrelevant;
no distribution supported at zero is allowed by the bounded-operator
construction. In particular q is locally essentially bounded, including
near zero. A helical skew component can commute with rotations about xi
but not with all the reflections just used. Dropping those reflections
would leave an unjustified scalar-symbol assertion.

## 6. A passive-scalar triad, localized on the whole space

We now prove that the radial q in (8) must be constant almost everywhere.
No general classification of Euler's quadratic invariants is imported.

For k,l>0 put r=(k^2+l^2)^(1/2) and consider the finite Fourier fields

$$
 U=(0,-\cos(kx_1),\ \sin(lx_2)+\cos(kx_1+lx_2)),
$$

$$
 A=(l^{-1}\cos(lx_2),\ k^{-1}\sin(kx_1+lx_2),\ k^{-1}\sin(kx_1)).
                                                                    \tag{10}
$$

A direct differentiation gives `curl A=U` and `div U=0`. These are
bounded periodic fields, independent of x3. Direct multiplication gives

$$
 (U\cdot\nabla)U
 =(0,0,-l\cos(kx_1)[\cos(lx_2)-\sin(kx_1+lx_2)]).              \tag{11}
$$

Applying the scalar weight q to the finitely many nonzero frequencies
in U is just a finite algebraic operation. Averaging over a period cell,

$$
 \operatorname{mean}\big(q(D)U\cdot (U\cdot\nabla)U\big)
                 =\frac l4\,[q(l)-q(r)].                      \tag{12}
$$

For example, the two nonzero averages are
`mean(sin(lx2) cos(kx1) sin(kx1+lx2))=1/4` and
`mean(cos(kx1+lx2) cos(kx1) cos(lx2))=1/4`.
The remaining products have zero mean. The component of U of length k
makes no direct contribution because (11) has only a third component.

Equation (12) is NOT yet a whole-space test of the theorem. To make it
one, fix a nonnegative, nonzero smooth compactly supported radial chi,
write `chi_L(x)=chi(x/L)`, and set

$$
                  W_L=\nabla\times(\chi_L A).                  \tag{13}
$$

Then W_L is a genuine compactly supported smooth solenoidal datum.
Writing `W_L=chi_L U+R_L`, where `R_L=grad chi_L cross A`, gives, for
every fixed integer s>=0,

$$
 \|R_L\|_{H^s}=O(L^{1/2}),\qquad
 \|R_L\|_{W^{1,\infty}}=O(L^{-1}),
$$

$$
 \|W_L\cdot\nabla W_L-\chi_L^2 U\cdot\nabla U\|_2
                                                    =O(L^{1/2}).  \tag{14}
$$

These follow directly from the factor L^(-1), bounded derivatives of
the finite Fourier fields, and a support of volume O(L^3).

For completeness the localization works for MEASURABLE q; smoothness of
the original quadratic form is not being silently reintroduced. Choose a
nonzero frequency eta at which `xi -> q(|xi|)` has a Lebesgue value.
For a fixed vector a, Plancherel gives

$$
 L^{-3}\|q(D)(\chi_L a e^{i\eta\cdot x})
          -q(|\eta|)\chi_L a e^{i\eta\cdot x}\|_2^2
 =|a|^2\int |q(|\eta+\zeta/L|)-q(|\eta|)|^2
                                    |\widehat\chi(\zeta)|^2d\zeta
 \longrightarrow0.                                           \tag{15}
$$

Near eta this is the approximate-identity consequence of Lebesgue
differentiation, applied also to the square; q is locally bounded.
For the far tail, use the polynomial bound in (8) and the arbitrarily
rapid decay of chi-hat. This supplies an integrable tail tending to zero
and justifies (15) without a pointwise continuity assumption.

There is a full-measure set of positive radii at which this argument
works in EVERY direction. Indeed, at a one-dimensional Lebesgue point
r0>0 of q, the average of `|q(|xi|)-q(r0)|` over a small ball centred on
the radius-r0 sphere is bounded by a constant times its one-dimensional
average over `(r0-epsilon,r0+epsilon)`. The same applies to the square.

Choose k,l,r in this full-measure set. Apply (15) to the finite frequencies
of U. Also (8) and (14), with s=2m, give
`||q(D)R_L||_2=O(L^(1/2))`. Consequently

$$
 q(D)W_L=\chi_L q(D)U+o_{L^2}(L^{3/2}).                       \tag{16}
$$

Since `q(D)W_L` is solenoidal, the Leray projection can be removed from
its pairing with `W_L dot grad W_L`. Equations (12), (14), (16), and one
integration by parts against each nonconstant Fourier mode of chi_L^3
now give

$$
 \overline B(W_L,N(W_L))
 =\frac l4[q(l)-q(r)]L^3\int\chi^3+o(L^3).                    \tag{17}
$$

The left side is EXACTLY zero by (4). Thus `q(l)=q(r)` for these choices.
The conditions that k,l and `(k^2+l^2)^(1/2)` are Lebesgue radii hold
for almost every pair (k,l)>0. Changing variables from (k,l) to (r,l)
therefore gives `q(l)=q(r)` for almost every pair `0<l<r`.
By symmetry and Fubini, q is constant almost everywhere on every bounded
positive interval, and hence on (0,infinity). This proves the assertion.

The use of the third velocity component in (10) is essential. One must
not apply this argument to two-dimensional velocity fields, where the
quadratic enstrophy invariant is an immediate consistency check against
such an overgeneralization.

## 7. Critical coercivity contradicts the surviving energy form

Sections 5--6 show that `overline Q(v)=a0 ||v||_2^2`. But orthogonal and
translation averaging retained `overline Q(v)>=c||v||_3^2`. Choose a
nonzero compactly supported solenoidal v and use its NS scaling
`v_lambda(x)=lambda v(lambda x)`. Then

$$
 c\|v\|_3^2
 \le \overline Q(v_\lambda)
 =a_0\lambda^{-1}\|v\|_2^2\longrightarrow0,\qquad
                                            \lambda\to\infty. \tag{18}
$$

This contradiction proves Theorem Q. No estimate on a singular NS
trajectory has been asserted or used.

An explicit instance checks the direction of the obstruction. For
`Q(v)=|| |D|^(1/2) v||_2^2`, take k=l=1 in (10). The cutoff fields satisfy

$$
 -2\langle |D|W_L,(W_L\cdot\nabla)W_L\rangle
 =\frac{\sqrt2-1}{2}L^3\int\chi^3+o(L^3)>0                   \tag{19}
$$

for L sufficiently large. At the actual NS datum `a W_L`, a>0, this
positive term is multiplied by a^3, while viscosity contributes
`-2 nu a^2 || |D|^(3/2)W_L||_2^2`. Thus the full critical quadratic energy
increases initially for a sufficiently large FIXED smooth datum and
fixed positive viscosity. This is not a claim of eventual blow-up.

The general theorem is not merely this example: averaging and (17)
exclude every form in the stated class, even if a proposed anisotropic
or spatially varying form avoids this particular unrotated test field.

## 8. A separate test of local-energy-only closure

**Imported construction, not an author reconstruction.** Ozanski,
*On weak solutions to the Navier--Stokes inequality with internal
singularities*, arXiv:1709.00602v3 (9 July 2019), Section 6, constructs
solenoidal, compactly supported fields satisfying the local energy
inequality with their canonical pressure. They are smooth between
switching times, with downward squared-speed jumps allowed. For fixed
`M>=2`, `0<tau<1`, `M tau<1`, (6.22)--(6.26) give disjoint similarities
Gamma_m of ratio tau^j and

$$
 t_j=T\sum_{i=0}^{j-1}\tau^{2i}\uparrow T_*=T/(1-\tau^2),
 \qquad |b(x,t_j)|=\tau^{-j}\sum_{|m|=j}f(\Gamma_m^{-1}x),     \tag{20}
$$

where f is nonzero and compactly supported. The field is not an NS
solution. Proposition 6.3 treats the pressure of the WHOLE field; naive
independent superposition is not the construction. Printed pages 57--59,
including the displayed formulas, were inspected.

Here is the critical-norm consequence, derived from (20), rather than
inferred from the source's L-infinity blow-up statement. Disjointness
and the Jacobian `dx=tau^(3j)dy` give exactly, for finite p>=1,

$$
 \|b(t_j)\|_p^p=(M\tau^{3-p})^j\|f\|_p^p.                   \tag{21}
$$

In particular,

$$
 \|b(t_j)\|_3^3=M^j\|f\|_3^3\to\infty,
 \qquad \|b(t_j)\|_2^2=(M\tau)^j\|f\|_2^2\to0.              \tag{22}
$$

Right-hand smoothness on each stage makes L3 arbitrarily large on
intervals of POSITIVE length, not just at the discrete times t_j.
Thus the essential supremum of L3 before T_* is infinite.

For clarity, the energy assertions can be checked without an additional
uniform estimate on the construction's unscaled stage fields. Integrate
the scalar NS inequality on each smooth stage. Compact support and
solenoidality eliminate the transport and pressure integrals, giving
`E'+2 mu Y<=0` at the fixed positive viscosity mu supplied by the
construction. At each switch E only decreases. Summing gives
`E(t)+2 mu integral_0^t Y <= E(0)`. Between t_j and t_(j+1), E(t) is at
most the second expression in (22). Hence `b(t)->0` strongly in L2 as
`t->T_*`, with finite total dissipation and fixed compact spatial support.

This also covers any prescribed positive viscosity nu, rather than only
a small-viscosity interval. Choose one admissible mu>0, set a=nu/mu, and
put `b_tilde(x,t)=a b(x,a t)`, `p_tilde(x,t)=a^2 p_b(x,a t)`. Direct
substitution gives

$$
 \widetilde b\cdot(\partial_t\widetilde b-\nu\Delta\widetilde b
       +(\widetilde b\cdot\nabla)\widetilde b+\nabla\widetilde p)
 =a^3 b\cdot(\partial_s b-\mu\Delta b+(b\cdot\nabla)b+\nabla p_b)
 \le0.                                                        \tag{23}
$$

The canonical pressure scales as stated. Downward jumps are preserved.
The new datum is one fixed smooth compactly supported datum and the new
endpoint is T_*/a; (22) still gives divergent L3.

**Exact scope.** The excluded inference is from these scalar local-energy
premises to an input-only critical bound. The counterexample is NOT a
classical unforced NS solution; it is NOT smooth through all switching
times; it does NOT establish the exact global energy and enstrophy
identities of the previous comparison curve. In particular it is not a
counterexample to the conjunction of ALL the premises in that earlier
note plus local energy. Those distinctions are indispensable.

This is a literature-backed exclusion of a proposed inference, not a new
construction of singular NS-inequality fields. The M>=2 branch matters:
a single-copy construction with M=1 would have constant L3 along (20)
and would not prove this critical-norm counterexample.

## 9. Research disposition and remaining terminal obligation

Retire universal coercive quadratic Lyapunov closure under (2), including
its anisotropic and fixed spatially inhomogeneous variants. Do not seek
a different fixed Fourier weight to repair (19): Theorem Q covers the
whole stated class, not just the displayed multiplier.

Retire local-energy-only budget/packing proofs that purport to derive
(1) for the premise class in Section 8. Local energy does not force the
branching cost to diverge: (22) has critical-norm growth while the
physical energy factor M tau remains strictly below one.

Do NOT retire nonlinear or datum-adapted functionals, nonmonotone
estimates, full momentum/vorticity evolution, or every spatially resolved
local-energy method. Unbounded spatially weighted quadratic forms not
satisfying (2) are also outside Theorem Q. No theorem here combines the
NS-inequality counterexample with the earlier exact two-balance example.
The analytic-envelope route has no producer; its radius-only shortcut is
false, not a replacement terminal theorem.

The remaining terminal obligation is unchanged: prove (1) from the fixed
inputs for actual NS branches, or directly exclude a finite T_* using
consequences of the full equation. No strictly weaker remaining theorem
has been established. The prior intrinsic selection problem is not made
terminal by these exclusions; its missing rigidity suffix remains missing.

## 10. Attribution and adversarial author checks

The k=l=1 periodic snapshot underlying (10) is already present in the
frozen repository's two-balance note. Here its two frequencies are varied
and its critical quadratic transfer is used after translation/orthogonal
averaging. The proof does not rely on an asserted complete classification
of Euler invariants. Standard energy/helicity conservation is background,
not a substitute for Sections 4--6. No claim of novelty is made.

The external construction used in Section 8 is:

W. S. Ozanski, *On weak solutions to the Navier--Stokes inequality with
internal singularities*, arXiv:1709.00602v3, 9 July 2019.
https://arxiv.org/abs/1709.00602 ; https://arxiv.org/pdf/1709.00602 .
Exact locations: Section 6.1 for the disjoint similarities and M tau<1;
Proposition 6.3(i)--(iii), equation (6.23) on printed page 58, and
(6.24)--(6.26) for gluing. The PDF inspected identifies itself as v3.

Author checks addressed: both amplitude signs at fixed viscosity;
pressure removal only after solenoidal pairing; preservation of
coercivity under averaging; weak convergence for the fixed pair
(w,N(w)); translation invariance via symmetric differences, not orbit
compactness; use of reflections to remove helical terms; measurable
rather than smooth radial symbols; Lebesgue-point localization with a
polynomially controlled tail; exact divergence correction in (13);
whole-space rather than periodic data; the sign in (12) and (19);
positive-length intervals in the L3 counterexample; and the separate
premise classes of the two exclusions. The trigonometric curl and mean
were checked symbolically, but the proof is the displayed analysis.

An independent audit should focus on the averaging/multiplier passage,
the measurable localization in (15)--(17), and the exact source premises
used for (20). No independent mathematical review, NS numerical proof,
formal proof, terminal graph promotion or manuscript integration is
claimed. Repository integrity checks do not certify these arguments.
