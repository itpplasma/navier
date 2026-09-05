# Independent audit of the homogeneous pressure-speed coupling

VERDICT: **PASS**

REVIEWED SCOPE: research/evidence/hf12-homogeneous-coupling.md, frozen with
SHA-256
39809a6ff2c0c719bf30218a3191438bc54ccce64fe2508a1bd7df16b2c0e83a
on base commit dd0473219e058bd98f733696434724b22c0a634d.

FIRST BAD BRIDGE: none.

EVIDENCE:

1. Positive amplitude scaling sends
   \(r\mapsto ar\), \(p,q\mapsto a^2p,a^2q\), and therefore
   \(\rho_k\mapsto a\rho_k\) and \(g_k\mapsto a^3g_k\).  Since
   \(0\le\rho_k\le r\), on \(p<0\) one has
   \(g_k=-q\rho_k\ge-qr\), while on \(p\ge0\), \(g_k=pr\ge0\).
   The stated Young inequality consequently proves (3)--(4).  Conversely,
   \[
      |g_k|\le |p|r,\qquad
      \int q^{3/2}\le\|p\|_{3/2}^{3/2}
      \le C\|u\|_3^3.
   \]
   Hölder gives the same bound for \(\int|p|r\).  Both coercivity constants
   are independent of \(k>0\), exactly as claimed.

2. On \(p<0\), \(q=-p\), \(g_k=-q(s-h)\),
   \(s=(r^2+kq)^{1/2}\), and \(h=(kq)^{1/2}\).  Thus
   \[
   \partial_rg_k=-q{r\over s}={pr\over s},
   \]
   while
   \[
   \begin{aligned}
   \partial_pg_k
   &=(s-h)+q\left({k\over2s}-{h\over2q}\right)\\
   &=s-\frac32h+{h^2\over2s}
     ={(s-h)(2s-h)\over2s}.
   \end{aligned}
   \]
   This verifies both the sign and factorization in (6).  The entropy
   derivative is
   \(\partial_pq^{3/2}=-(3/2)\sqrt q\), so (8)--(9) give the exact full
   pressure coefficient.  Expanding
   \(s-h=r^2/(2h)+O(r^4/h^3)\) proves (7), with its stated dependence on
   \(k,q\).

3. For \(V=-N-\nabla p\),
   \[
      \int r\,u\cdot V
      =\int p\,u\cdot\nabla r=P_3.
   \]
   Here the transport term is
   \(-\frac13\int u\cdot\nabla(r^3)=0\).  The speed derivative of \(g_k\)
   contributes
   \[
      -\int\beta_k r\,u\cdot\nabla r
      -\int\beta_k u\cdot\nabla p.
   \]
   On \(p>0\), \(\beta_kr=p\), so the first term cancels that portion of
   \(P_3\).  On \(p<0\), \(\beta_kr=pr/s\), leaving
   \(p(1-r/s)u\cdot\nabla r\).  Finally,
   \(Dp(u)[V]=2R_iR_j(u_iV_j)\), and multiplication by the combined
   \(p\)-derivative \(a_k\) gives the last term of (14).  Thus (14) retains
   every transport, pressure-gradient, and nonlocal pressure-variation term.

4. On \(p<0\), put \(x=r/\sqrt{kq}\).  Since
   \(|u\cdot\nabla r|\le r|\nabla r|\),
   \[
   \left|p\left(1-{r\over s}\right)u\cdot\nabla r\right|
   \le\sqrt{k}\,q^{3/2}
      x\left(1-{x\over\sqrt{1+x^2}}\right)|\nabla r|.
   \]
   Differentiating the scalar factor shows its maximum occurs at
   \(x=\sqrt y\), where \(y=(\sqrt5-1)/2\), with value
   \(C_0=y^2/\sqrt{1+y}\).  This proves (15).  Fixing \(x>0\) while taking
   \(r=x\sqrt{kq}\) confirms that the scalar order \(\sqrt k\) cannot be
   improved.

5. The factor \(\sqrt k\) does not give an input-only remainder.  The
   quantity left by (15),
   \[
      \int_0^T\!\int_{\mathbb R^3}
          p_-^{3/2}|\nabla|u||\,dx\,dt,              \tag{A}
   \]
   is a new critical spacetime integral: under Navier--Stokes scaling its
   integrand has scale \(\lambda^5\), while space-time measure has scale
   \(\lambda^{-5}\).  No estimate for (A) follows from energy or the static
   coercivity of \(\mathcal J_k\).  Moreover, on \(r^2\le kq\),
   \(r/s\le1/\sqrt2\), so a fixed fraction of local pressure work remains.
   The other two terms of (14) have no small \(k\)-factor.  The candidate
   correctly treats (15) as localization of the gap rather than closure.

6. The cusp scope is accurate.  At \(r=0,p<0\), the negative-pressure
   coupling is quadratic in velocity and removes the speed cusp.  At
   \(r=0,p>0\), it equals \(p|u|\) and retains it.  Although the one-sided
   \(p\)-derivatives match at \(p=0\) when \(r>0\), simultaneous zero sets
   and the velocity cusp prevent an unrestricted Frechet derivative.
   Formula (14) is therefore valid only away from the declared cusps unless
   a smoothing and domination argument is supplied.

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: The complete frozen candidate survives.
For every \(k>0\), \(\mathcal J_k\) is a homogeneous cubic functional
uniformly equivalent from below and above to \(\|u\|_3^3\).  Away from its
cusps it has the exact Euler residual (14).  Its first cancellation defect
has the sharp pointwise \(O(\sqrt k)\) bound (15), while the full residual
remains uncontrolled.

UNNECESSARY DEPENDENCIES: Static coercivity needs no differentiability of the
functional, Euler equation, or small-\(k\) limit.  The scalar derivative and
defect estimates need no heat calculation or Navier--Stokes trajectory.

NON-CLAIMS: The review supplies no bound for (A), no unregularized derivative
across \(u=0\) or \(p=0\), no favorable heat sign, no closed Euler or
Navier--Stokes estimate, no pressure absorption, no HF estimate, and no
regularity conclusion.

REOPENING CONDITION: Control all three terms of (14), together with the heat
contribution, by quantities already available from the initial data; or
replace the remaining coupling while preserving uniform coercivity and
compute its complete pressure variation.

## Separate controller-proposed extension: small-\(k\) heat obstruction

This extension is not part of the frozen candidate above.  Let
\[
 \mathcal K(u)=\int\left({r^3\over3}+pr+p_-^{3/2}\right),
 \qquad E_p(u)=\int p_-^{3/2}.
\]
On \(p<0\), with \(q=-p\), direct subtraction gives
\[
 g_k-pr=q\left[r-\sqrt{r^2+kq}+\sqrt{kq}\right].     \tag{B}
\]
Because
\[
 0\le \sqrt{r^2+kq}-r
 ={kq\over\sqrt{r^2+kq}+r}\le\sqrt{kq},
\]
equation (B) satisfies
\[
 0\le g_k-pr\le\sqrt{k}\,q^{3/2}.                   \tag{C}
\]
On \(p\ge0\) the difference is zero.  Therefore, for every admissible \(u\),
\[
 0\le\mathcal J_k(u)-\mathcal K(u)
 \le\sqrt{k}\,E_p(u).                               \tag{D}
\]

Assume the independently audited HF11 finite-step result supplies fixed
\(h,t\) with
\(\Delta=\mathcal K(e^{\nu t\Delta}h)-\mathcal K(h)>0\).  Applying (D) only
at the two endpoints yields
\[
 \begin{aligned}
 \mathcal J_k(e^{\nu t\Delta}h)-\mathcal J_k(h)
 &\ge \mathcal K(e^{\nu t\Delta}h)-\mathcal K(h)
      -\sqrt{k}\,E_p(h)\\
 &=\Delta-\sqrt{k}\,E_p(h).
 \end{aligned}                                      \tag{E}
\]
Thus the homogeneous functional also increases under that fixed heat step
for every sufficiently small \(k>0\).  If \(E_p(h)=0\), (E) is already
strict for all \(k\); in the cited negative-pressure construction
\(E_p(h)>0\), so it suffices to take
\(k<(\Delta/E_p(h))^2\).

EXTENSION SCOPE: This refutes universal heat monotonicity only in the
sufficiently small-\(k\) regime.  It does not assert failure for every \(k\),
control the Euler residual, or turn the coefficient \(\sqrt k\) in (15) into
an input-bound estimate.
