# Independent audit of the material-pressure reorganization

VERDICT: **REPAIR**

REVIEWED SCOPE: research/evidence/hf16-material-pressure.md, frozen with
SHA-256
5bb6a8524b4965da78647c6c7d59ef28406405b747a329f4d39d5c52ff64624e
on base commit 0918b9ab403fcbc878ee20b62d887f6405123337.

FIRST BAD BRIDGE: Equation (10) is a correct conditional estimate, but the
frontier record calls it a legitimate Gronwall term without displaying the
bridge from the differentiated regularized functional
\(\int F_\eta(u,z)\) to the unregularized quantity \(\|u\|_3^3\) on its
right side.  No uniform coercivity of \(F_\eta\) is stated or proved.
Uniform regularized coercivity is not necessary, however: the separate
value-limit argument appended below repairs this bridge, conditional on the
still-unproved uniform estimate for the complete remaining aggregate.

EVIDENCE:

1. Differentiating \(z=T_J(u_i u_j)\), using symmetry in \(i,j\), gives
   \[
   z_t=2T_J(u_i u_{j,t}).
   \]
   The product identity
   \[
   \Delta(u_i u_j)=u_i\Delta u_j+u_j\Delta u_i
                  +2\partial_\ell u_i\partial_\ell u_j
   \]
   yields the two viscous terms in (1), with signs
   \(+\nu\Delta z-2\nu T_J(G_{ij})\).  Likewise,
   \[
      2T_J(u_iN_j)=T_J(u\cdot\nabla(u_i u_j)),
   \]
   because \(\nabla\cdot u=0\) is not needed for this pointwise product
   identity.  The pressure term is
   \(-2T_J(u_i\partial_jp)\).  Every sign and factor in (1)--(2) is correct.

2. Adding \(u\cdot\nabla z\) to (1) gives
   \[
   u\cdot\nabla T_Jf-T_J(u\cdot\nabla f)
   =[u\cdot\nabla,T_J]f
   \]
   under the convention \([A,B]=AB-BA\).  Hence the commutator in (3) has
   the asserted plus sign.  The cutoff remains inside
   \(T_J=Q_JR_iR_j\) in every pressure source; no full-pressure or low-pass
   term is substituted silently.

3. In the Euler part, \(u_t=-N-\nabla p\) and (3) gives
   \[
      z_t=-u\cdot\nabla z+[u\cdot\nabla,T_J](u_i u_j)
          -2T_J(u_i\partial_jp).
   \]
   The first velocity term and the first pressure term combine as
   \[
   -D_vF_\eta\cdot(u\cdot\nabla u)
   -F_{\eta,z}u\cdot\nabla z
   =-u\cdot\nabla F_\eta(u,z).
   \]
   For the declared \(H^m\), \(m\ge4\), classical solution at fixed
   \(\eta>0\), the normalized density is integrable and the chain rule and
   integration by parts are legitimate.  Since \(\nabla\cdot u=0\), its
   integral vanishes.  The three remaining terms are exactly (6), including
   both pressure-gradient terms.

4. The fixed-\(\eta\) scope is sufficient and appropriately limited.
   Sobolev multiplication for \(m\ge4\), boundedness of the fixed
   multipliers, and the audited compact-range derivative bounds for
   \(F_\eta\) justify (3)--(6) on a compact classical interval.  The
   normalization at \((0,0)\) supplies quadratic \(L^2\)-based decay of the
   density.  No Schwartz persistence or \(\eta\downarrow0\) derivative is
   needed.  These identities do not become an unregularized identity merely
   from convergence of endpoint values.

5. The split \(u=v+w\), with \(v=S_Lu\), is linear in the advecting field,
   so (7) is exact with the same cutoff \(J\) in both commutators.
   Bernstein in three dimensions gives
   \[
      \|\nabla S_Lu\|_\infty
      \le C2^L2^{3L/2}\|u\|_2
      =C2^{5L/2}E^{1/2}.
   \]
   This verifies (9), including its frequency and energy powers.

6. Estimate (C) is not proved by the formal kernel sentence.  The kernel
   computation does have the correct structure:
   \[
   [v\cdot\nabla,T_J]f(x)
   =\int (v(x)-v(y))\cdot\nabla K_J(x-y)f(y)\,dy
   \]
   when \(\nabla\cdot v=0\).  The Lipschitz difference restores order zero,
   but a complete proof must still handle the principal value and smooth
   cutoff uniformly in \(J\).  This audit therefore treats (C), exactly as
   the candidate requests, as an unverified external premise.

7. Conditional on (C), Hölder gives
   \[
   \begin{aligned}
   \left|\int F_{\eta,z}[v\cdot\nabla,T_J](u_i u_j)\right|
   &\le \|F_{\eta,z}\|_3
        \|[v\cdot\nabla,T_J](u_i u_j)\|_{3/2}\\
   &\le C_k\|u\|_3\|\nabla v\|_\infty
        \|u_i u_j\|_{3/2}\\
   &\le C_k2^{5L/2}E_0^{1/2}\|u\|_3^3.
   \end{aligned}
   \]
   Thus (8)--(10) have the correct Hölder exponents and are uniform in
   \(J,\eta\), and terminal time.  The coefficient depends only on the
   stated input-selected quantities.  It is not converted pointwise into
   the regularized energy; the endpoint-limit argument below shows that such
   a pointwise conversion is unnecessary once the other aggregate has the
   stated uniform bound.

8. Writing \(p=p^H+p^L\) in the last two terms of (6) does isolate the
   previously audited low-pressure gradients.  It does not change
   \(W=-N-\nabla p^H\) into a solenoidal field:
   \[
      \nabla\cdot W=\Delta p^L.
   \]
   The warning against reusing Leray orthogonality or a divergence-free
   transport cancellation is therefore correct.

REPLACEMENT ARGUMENT: Retain (3)--(10), but replace the Gronwall statements
by:

> Assuming (C), the low-band advecting commutator is bounded by the
> input-dependent coefficient in (10) times \(\|u(t)\|_3^3\).  Conditional
> on a uniform input-only bound for the complete remaining aggregate, first
> integrate the fixed-\(\eta\) balance and then pass only its endpoint
> functional values to \(\eta=0\).  Apply coercivity to the limiting
> functional and Gronwall there.

The complete argument and its quantifiers are given in the extension below.

CONDITIONAL SUFFIX THAT SURVIVES: Equations (3) and (6) are exact
fixed-\(\eta\) material-pressure identities.  Conditional on the commutator
bound and a uniform strict-absorption estimate for the complete remaining
aggregate, endpoint functional-value convergence and coercivity of the
unregularized functional make the cubic commutator bound a valid Gronwall
term.

UNNECESSARY DEPENDENCIES: The exact identities need neither (C), the
low/high advecting split, nor any regularization limit.  Bound (10) needs no
heat identity or estimate for the high-band commutator.

NON-CLAIMS: This audit does not prove the frozen Calderón commutator premise,
uniform coercivity of \(F_\eta\), a differentiated \(\eta\)-limit, the
remaining aggregate estimate, pressure absorption, HF, or regularity.

REOPENING CONDITION: Prove the required commutator estimate in the exact
\(Q_JR_iR_j\) convention and control the high-band commutator and remaining
heat and pressure-gradient aggregate uniformly in \(\eta\).

## Separate controller-proposed extension: endpoint-limit Gronwall repair

This extension is not part of the frozen candidate.  Suppose the exact
fixed-\(\eta\) balance has been decomposed so that, uniformly for
\(0<\eta\le1\) and every \(0<t<\min(H,T_*)\),
\[
 \int_0^t\mathcal R_\eta^{\rm other}
 \le\theta\nu\int_0^t\mathcal D_\eta+A,
 \qquad 0\le\theta<1,                                \tag{E1}
\]
where \(A\) is finite and input-only, and suppose all audited low terms have
an input-only bound \(A_{\rm low}\).  Assume also
\[
 |\mathcal C_\eta(t)|\le M\|u(t)\|_3^3               \tag{E2}
\]
with \(M\) input-only and independent of \(\eta,t\).  The independently
verified Taylor version may take
\[
 M=C_k\left(2^{J+3L/2}+2^{5L/2}\right)E_0^{1/2};     \tag{E3}
\]
the following argument needs only (E2), not the derivative-only premise (C).

Integrating the exact balance, using (E1), moving the absorbed dissipation to
the left, and dropping the remaining nonnegative
\((1-\theta)\nu\int_0^t\mathcal D_\eta\) gives
\[
 \mathcal J_\eta(t)
 \le \mathcal J_\eta(0)+A_{\rm low}+A
      +M\int_0^t\|u(s)\|_3^3\,ds.                   \tag{E4}
\]
For every fixed \(t<T_*\), the trajectory is classical on \([0,t]\), so the
last integral is finite and contains no \(\eta\).  The independently audited
functional-value convergence at the two endpoints permits
\(\eta\downarrow0\) directly in (E4):
\[
 \mathcal J(t)\le C_{\rm in}
      +M\int_0^t\|u(s)\|_3^3\,ds,                   \tag{E5}
\]
where \(C_{\rm in}=\mathcal J(0)+A_{\rm low}+A\) is independent of \(t\).
No differentiated limit and no uniform coercivity of \(\mathcal J_\eta\)
has been used.

The unregularized static coercivity
\(\mathcal J(t)\ge\|u(t)\|_3^3/6\) converts (E5) into
\[
 \mathcal J(t)\le C_{\rm in}+6M\int_0^t\mathcal J(s)\,ds.
\]
The classical trajectory makes \(\mathcal J\) continuous on every compact
subinterval, so Gronwall yields
\[
 \mathcal J(t)\le C_{\rm in}e^{6Mt}
 \le C_{\rm in}e^{6MH},\qquad 0<t<\min(H,T_*).       \tag{E6}
\]
Because the constants are uniform in \(t\), this is the required
endpoint-uniform conclusion.

EXTENSION VERDICT: **PASS, conditional on (E1) and (E2).**  This repairs the
Gronwall bridge without uniform regularized coercivity.  Estimate (E1), the
load-bearing remaining-aggregate bound, is still unproved; the argument does
not supply it or imply HF or regularity on its own.
