# Frozen audit of the energy-only spacetime obstruction

**VERDICT: REPAIR.**  The actual-trajectory construction, its uniform
small-viscosity existence interval, continuity of pressure work through
velocity zeros, all rescaling exponents, and removal of the fixed low-output
term are correct.  One endpoint detail should be made explicit: the theorem's
supremum requires \(\tau<T_*\), while the proof initially chooses the endpoint
corresponding to the full guaranteed normalized interval \([0,T]\).  Replacing
\(T\) by \(T/2\) in the integration gives an immediate complete repair.

## Frozen input and exact scope

The candidate was checked at:

* repository base
  `00b1fa3ff95785fe0232e60864498ab02ee90fd7`;
* file `research/evidence/hf04-energy-only-spacetime.md`;
* SHA-256
  `5e396404e1a57e3a35921e89b291f4e2bd12212e709b4f35aecdd4cd08533ecd`.

The reviewed theorem fixes \(E,\nu,H,J\) and a finite \(\theta\), varies the
Schwartz divergence-free datum subject to \(\|u_0\|_2^2=E\), and claims that
the integrated fixed-cutoff excess

\[
 \int_0^\tau(H_J-\theta\nu D_3)dt
\]

is unbounded over genuine smooth Navier--Stokes trajectory segments.  This is
strictly narrower than the project's datum-dependent HF hypothesis, which may
choose both its cutoff and finite remainder from the complete datum.

## Uniform small-viscosity existence: PASS

For \(0<\mu\leq\nu\), let \(v_\mu\) solve viscosity-\(\mu\) Navier--Stokes
with the same fixed compactly supported smooth datum \(\phi\).  For integer
\(m\geq5\), commuting derivatives and using incompressibility gives

\[
 {1\over2}{d\over ds}\|v_\mu\|_{H^m}^2
 +\mu\|\nabla v_\mu\|_{H^m}^2
 \leq C_m\|\nabla v_\mu\|_\infty\|v_\mu\|_{H^m}^2
 \leq C_m\|v_\mu\|_{H^m}^3.                          \tag{A}
\]

The right side and initial norm are independent of \(\mu\).  The usual
Friedrichs construction, or local Picard construction followed by (A), hence
gives a common \(T>0\) and \(H^m\) bound.  The fact that the heat semigroup is
an \(H^m\) contraction is compatible with this proof but is not alone a
lifespan argument; inequality (A) and the continuation criterion supply the
uniform conclusion.

From the equation,

\[
 \|\partial_sv_\mu\|_{H^{m-2}}
 \leq C\|v_\mu\|_{H^m}^2+\mu\|v_\mu\|_{H^m}
 \leq C_{\phi,m,\nu}.                                 \tag{B}
\]

Thus \(\|v_\mu(s)-\phi\|_{H^{m-2}}\leq Cs\).  Interpolation with the
uniform \(H^m\) bound gives the stated \(H^{m-1}\) estimate \(Cs^{1/2}\).
No inviscid-limit convergence theorem is being assumed.

## Continuity of pressure work at zeros: PASS

Set

\[
 A(z)={z\otimes z\over|z|}\quad(z\ne0),\qquad A(0)=0.
\]

This degree-one map is globally Lipschitz: its derivative is uniformly
bounded away from zero, and homogeneity controls pairs whose joining segment
passes near zero.  Almost everywhere,

\[
 v\cdot\nabla|v|=A(v):\nabla v.                       \tag{C}
\]

This formula removes any apparent singularity at a velocity zero.  On a
bounded subset of \(H^{m-1}\), with \(m\geq5\), Sobolev embedding gives the
needed \(W^{1,\infty}\) control.  Therefore

\[
 \|A(v):\nabla v-A(w):\nabla w\|_2
 \leq C_K\|v-w\|_{H^{m-1}}.                           \tag{D}
\]

Also, using \(L^2\)-boundedness of the Riesz transforms,

\[
 \|p[v]-p[w]\|_2
 \leq C\|(v-w)\otimes v+w\otimes(v-w)\|_2
 \leq C_K\|v-w\|_{H^{m-1}}.                          \tag{E}
\]

The individual \(p\) and \(g=A(v):\nabla v\) norms are bounded on the same
set, so pairing (D)--(E) proves local Lipschitz continuity of \(P_3\).  The
uniform \(H^{m-1}\) persistence then gives
\(P_3[v_\mu(s)]\geq P_\phi/2\) on a common shortened interval.  The estimate

\[
 D_3(v_\mu)\leq2\|v_\mu\|_\infty\|\nabla v_\mu\|_2^2
\]

is correct because \(|\nabla|v||\leq|\nabla v|\) almost everywhere.

## Rescaling: PASS

Let

\[
 N={a^2\|\phi\|_2^2\over E},qquad \mu={\nu\over a},
\]

and define

\[
 u_a(x,t)=aN,v_\mu(Nx,aN^2t),qquad
 p_a(x,t)=a^2N^2q_\mu(Nx,aN^2t).                      \tag{F}
\]

The time derivative and convection both acquire \(a^2N^3\).  The rescaled
viscous term has coefficient \(\nu aN^3\), equal to
\(a^2N^3\mu\) precisely because \(\mu=\nu/a\).  Thus (F) solves viscosity
\(\nu\) Navier--Stokes.

The initial squared \(L^2\) norm is

\[
 (aN)^2N^{-3}\|\phi\|_2^2={a^2\over N}\|\phi\|_2^2=E.
\]

For a general amplitude \(A\) and spatial frequency \(N\), pressure work
scales as \(A^4N^{-2}\) and \(D_3\) as \(A^3N^{-1}\).  With \(A=aN\), this
gives exactly

\[
 P_3[u_a]=a^4N^2P_3[v_\mu],qquad
 D_3[u_a]=a^3N^2D_3[v_\mu].                           \tag{G}
\]

Since \(dt=ds/(aN^2)\),

\[
 \int(P_3[u_a]-\theta\nu D_3[u_a])dt
 =a^3\int(P_3[v_\mu]-\theta\mu D_3[v_\mu])ds.         \tag{H}
\]

Every power of \(a,N,\nu\) in the candidate is therefore correct.  With
\(P_3[v_\mu]\geq P_\phi/2\), \(D_3[v_\mu]\leq C_D\), and
\(\mu=\nu/a\), the integrand is at least \(P_\phi/4\) for all sufficiently
large \(a\).

## First bad bridge and replacement

The proof defines \(\tau_a=T/(aN^2)\), corresponding to normalized time
exactly \(T\), while the theorem takes a supremum over
\(\tau<T_*(u_{a,0})\).  A uniform bound on the closed interval \([0,T]\),
together with local continuation from its endpoint, does imply that each
normalized maximal lifespan is strictly larger than \(T\).  The candidate
alludes to continuation but does not spell this endpoint step out at the
place where strict admissibility is needed.

The smallest repair avoids the issue entirely.  Define

\[
 \widehat\tau_a={T/2\over aN^2}.                       \tag{I}
\]

Then \(\widehat\tau_a<T_*(u_{a,0})\) directly from existence on \([0,T]\),
and \(\widehat\tau_a<H\) for large \(a\).  Equations (9)--(10) of the
candidate hold throughout \([0,T/2]\), so (H) gives

\[
 \int_0^{\widehat\tau_a}
 (P_3[u_a]-\theta\nu D_3[u_a])dt
 \geq {TP_\phi\over8}a^3.                             \tag{J}
\]

This is a complete repair under the original hypotheses.

## Fixed low-output removal: PASS

For initial squared energy \(E\), the audited band-limited pressure estimate
is

\[
 \left|\int_0^\tau L_Jdt\right|
 \leq C2^{3J}E^2\left({\tau\over2\nu}\right)^{1/2}.    \tag{K}
\]

Here \(E^2=\|u_0\|_2^4\), so the datum exponent is correct.  Since
\(N\simeq a^2\), both \(\tau_a\) and \(\widehat\tau_a\) are comparable to
\(a^{-5}\).  Therefore (K) is \(O(a^{-5/2})\), negligible relative to the
\(a^3\) lower bound.  With \(H_J=P_3-L_J\), the integrated high-output excess
tends to \(+\infty\).

## Quantifiers and surviving theorem

After replacement (I), the theorem is valid with exactly these quantifiers:

* each of \(E>0\), \(\nu>0\), \(H>0\), integer \(J\), and finite
  \(\theta\geq0\) is fixed before constructing the sequence;
* the data vary with \(a\), are smooth compactly supported, divergence free,
  hence Schwartz, and have exactly \(\|u_{a,0}\|_2^2=E\);
* every integration interval is a genuine interval strictly inside the
  corresponding maximal smooth lifespan and is shorter than \(H\);
* the critical and higher initial norms are not uniform.

Thus the result rules out a fixed-cutoff spacetime remainder uniform over all
data when that remainder sees only \((E,\nu,H,J,\theta)\).  It does not refute
the original HF statement, which permits datum-dependent scale selection and
a datum-dependent finite remainder.  It supplies no common trajectory,
singularity, or blow-up conclusion.

## Conditional suffix that survives

The full theorem survives after the endpoint repair.  Any viable universal
high-pressure mechanism must use information beyond kinetic energy, adapt its
cutoff or remainder to the complete datum, or exploit structure along one
trajectory that is absent from this varying-data family.
