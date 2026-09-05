# Frozen audit of the localized Type-I cubic test

**VERDICT: FAIL WITH SCOPE.**  The localized cubic identity is correct, the
pressure gauge is handled correctly, and the logarithmic cutoff genuinely
reduces the transport and diffusion boundary terms under the pointwise
Type-I hypothesis.  The claimed conditional suffix to epsilon regularity does
not follow: even if the proposed signed interior-pressure estimate is granted,
the localized cubic quantity at the initial time \(-r^2\) remains critical
and need not be small.  No contraction or iteration producing the CKN
smallness threshold is supplied.

## Frozen input and reviewed scope

The candidate was frozen before inspection as follows:

* repository base:
  `169ec50daa9295e0a713236bf969c2f42a507f51`;
* file: `research/evidence/hf01-type-i.md`;
* file SHA-256:
  `fd991fc4147c1b0ee66b16adde146653b91b0faa353d69f1ec4726bb05247475`.

The review covers the localized identity, pressure normalization, local and
harmonic pressure decomposition, radius and logarithmic cutoff estimates,
and the final implication to local regularity.  It does not independently
source-audit Lei--Ren or CKN.

## Localized identity: PASS

Let \(w=|u|u\) and let \(\eta\) be a time-independent compactly supported
spatial cutoff.  Since

\[
 w\cdot u_t={1\over3}\partial_t|u|^3,
 \qquad
 (u\cdot\nabla)u\cdot w={1\over3}u\cdot\nabla|u|^3,
\]

incompressibility gives

\[
 \int\eta (u\cdot\nabla)u\cdot w
 =-{1\over3}\int |u|^3u\cdot\nabla\eta.
\]

For diffusion,

\[
 \nu\int\eta\Delta u\cdot w
 =-\nu\int\eta D_3+{\nu\over3}\int|u|^3\Delta\eta.
\]

The pressure pairing is

\[
 \int\eta\nabla p\cdot w
 =-\int\eta p,u\cdot\nabla|u|-int p|u|u\cdot\nabla\eta.
\]

Moving these terms gives candidate equation (1), with every sign and factor
\(1/3\) correct.  If \(\eta=\eta(x,t)\), writing
\(\eta\partial_t|u|^3=\partial_t(\eta|u|^3)-|u|^3\partial_t\eta\)
adds \((1/3)\int|u|^3\partial_t\eta\) to the right, also as stated.

At a candidate singular terminal time, this equality is first integrated to
\(-\delta<0\).  Passing \(\delta\downarrow0\) requires the available weak or
liminf formulation; one should not assume a classical trace at the point
being tested.  This endpoint qualification does not change the obstruction
below.

## Pressure gauge and decomposition

The two pressure terms combine exactly as

\[
 \int p\,\operatorname{div}(\eta|u|u).
\]

A spatial constant \(c(t)\) contributes
\(c(t)\int\operatorname{div}(\eta|u|u)=0\), so the expression is gauge
invariant.  The candidate is right to keep the terms together.

For \(p_{\rm loc}=R_iR_j(\chi u_i u_j)\), Calderon--Zygmund boundedness gives,
at almost every time,

\[
 \|p_{\rm loc}\|_{L^{3/2}}^{3/2}
 \leq C\|\chi u_i u_j\|_{L^{3/2}}^{3/2}
 \leq C\int_{\operatorname{supp}\chi}|u|^3.
\]

Time integration proves candidate equation (3), with the stated adjustment
of the spatial support.

The remainder \(p_{\rm harm}=p-p_{\rm loc}\) is spatially harmonic where
\(\chi=1\).  Interior harmonic estimates do give a positive power of
\(r/\rho\) for the oscillation
\(p_{\rm harm}-(p_{\rm harm})_{B_\rho}(t)\).  That fact alone does not make
its contribution to the cubic flux small: it must still be paired with
\(\operatorname{div}(\eta|u|u)\), or after integration by parts with
\(|u|u\cdot\nabla p_{\rm harm}\).  A rigorous perturbative conclusion needs
the corresponding local velocity bound and a time-integrable outer pressure
norm.  These are available as additional hypotheses in the pointwise Type-I
test, but do not follow merely from the word “harmonic,” and they are not
derived from normalized enstrophy (LR-1.11) in the note.

Minimal wording repair: replace the unconditional sentence that the harmonic
oscillation is perturbative by a conditional estimate naming the velocity
factor and outer time-pressure norm.  The pressure decomposition itself is
valid.

## Radius ledger and logarithmic cutoff

For a cutoff changing on scale \(r\), the three absolute errors have the
correct forms

\[
 r^{-1}\int|u|^4,qquad
 r^{-1}\int|p||u|^2,qquad
 \nu r^{-2}\int|u|^3.
\]

All are dimensionless under the Navier--Stokes parabolic scaling.  Under

\[
 |u(x,t)|\leq C_*(|x|^2-t)^{-1/2},
\]

the transport and diffusion estimates in candidate equation (6) are correct.
They remain order one at a single-scale cutoff.

For a logarithmic transition on \(r<|x|<\rho\), direct radial integration on
\(-r^2<t<0\) verifies the asserted gain.  For transport, up to constants the
integral is

\[
 {C_*^4\over\log(\rho/r)}
 \int_r^\rho R\int_0^{r^2}(R^2+s)^{-2},ds,dR
 \leq {C C_*^4\over\log(\rho/r)}.
\]

For diffusion it is

\[
 {C\nu C_*^3\over\log(\rho/r)}
 \int_r^\rho\int_0^{r^2}(R^2+s)^{-3/2},ds,dR
 \leq {C\nu C_*^3\over\log(\rho/r)}.
\]

Smooth endpoint transitions can be chosen with the same derivative bounds,
so they do not alter the conclusion.  A similar pressure-boundary gain is
conditional on uniform scale-invariant \(L^{3/2}\) pressure control on every
annulus traversed by the cutoff.  The candidate states this condition rather
than deriving it, which is the correct scope.

This test therefore adds real information: under pointwise Type I, geometric
leakage from transport and diffusion can be made small by separating the
inner and outer radii.  It does not make the active local pressure flux or the
initial localized cubic mass small.

## First invalid bridge: signed absorption does not imply CKN smallness

Write

\[
 X_\eta(t)={1\over3}\int\eta|u(t)|^3,
 \qquad
 \mathcal D_\eta=\int_{-r^2}^0\int\eta D_3.
\]

Suppose, solely for this audit, that candidate equation (10) holds and every
geometric and harmonic-pressure error is bounded by \(o(1)\).  Integrating
the localized identity from \(-r^2\) to a time \(-\delta\), absorbing, and
then taking the permissible liminf gives at most

\[
 X_\eta(0^-)+(1-\theta)\nu\mathcal D_\eta
 \leq X_\eta(-r^2)+o(1).                              \tag{A}
\]

The right side is neither omitted nor known to be small.  Under pointwise
Type I, even on the inner ball,

\[
 \int_{B_r}|u(x,-r^2)|^3dx
 \leq C_*^3\int_0^r {C R^2\over(R^2+r^2)^{3/2}}dR
 = C_0 C_*^3,                                         \tag{B}
\]

where \(C_0>0\) is independent of \(r\).  This scale-invariant upper estimate
does not tend to zero and can be arbitrarily large with \(C_*\); of course it
does not assert that every solution saturates the bound.  If the initial
cutoff extends through \(B_\rho\), the same available upper estimate grows
like \(C_*^3\log(\rho/r)\).  Thus sending \(r/\rho\to0\) improves boundary
leakage without providing smallness of the initial cubic term.

CKN epsilon regularity requires a scale at which an appropriate normalized
velocity/pressure or dissipation quantity is below a universal epsilon.
Inequality (A) supplies boundedness in terms of the unrestricted Type-I
constant, not such smallness.  No displayed estimate gives a contraction
from a larger scale to a smaller scale, decay of \(X_\eta(-r^2)\), or an
iteration that eventually crosses the epsilon threshold.  Consequently the
frontier statement

> either missing estimate, combined with the localized identity and an
> epsilon-regularity iteration, would be a local regularity mechanism

contains an absent load-bearing argument.  Calling the missing argument an
“iteration” does not construct it.

## Smallest exact repair

The valid suffix should stop at (A): equation (10), plus quantified control of
all cutoff and harmonic-pressure errors, produces a localized critical cubic
and weighted-dissipation bound whose size depends on the incoming localized
cubic mass and the Type-I constant.

To continue to regularity one must add one of the following genuinely new
inputs:

1. **Initial-slice smallness:** for a sequence \(r_k\downarrow0\), the exact
   incoming term and all pressure quantities required by a named epsilon
   criterion are below its universal threshold.  Then that criterion applies
   directly; the conclusion no longer follows from arbitrary Type I alone.
2. **A proved contraction:** an inequality for a complete scale-invariant
   regularity functional \(\mathcal Q(r)\), including velocity and pressure,
   of the form
   \[
    \mathcal Q(\sigma r)
    \leq\kappa\mathcal Q(r)+\varepsilon(r),
    \qquad 0<\kappa<1,quad\varepsilon(r)\to0,          \tag{C}
   \]
   with constants uniform for arbitrary finite Type-I size.  Iteration of
   (C) then gives a scale below the epsilon-regularity threshold.

Neither input is proved in the candidate, and adding either silently would
strengthen its hypotheses.  Hence the appropriate verdict is FAIL WITH SCOPE,
not REPAIR of the asserted Type-I regularity mechanism.

## Conditional suffix that survives

The following statements remain valid:

* the exact localized cubic balance, including its gauge-invariant pressure
  pairing;
* local/harmonic pressure decomposition, conditional on explicitly carrying
  the velocity and outer pressure factors in the harmonic estimate;
* order-one single-scale errors under pointwise Type I;
* logarithmic suppression of transport and diffusion leakage under pointwise
  Type I;
* reduction of the active interior term to the unproved signed estimate (10);
* conditional bound (A) if (10) and all other error estimates are supplied.

None of these proves general normalized-enstrophy Type-I regularity, pointwise
Type-I regularity, or the global high-pressure hypothesis.

## Non-claims and reopening condition

This audit does not claim that (10) is false.  It shows that (10), in the form
stated, is insufficient for the advertised epsilon-regularity suffix.  The
test can be reopened as a regularity route after a complete contraction such
as (C), or after a theorem deriving the full epsilon-criterion smallness from
the Type-I premise.  Any such theorem would address the open difficulty that
the candidate itself attributes to Lei--Ren.
