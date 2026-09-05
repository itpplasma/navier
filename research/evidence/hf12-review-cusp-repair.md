# HF12 independent audit: cusp repair

Frozen input: base commit
`d43dfe799333014f11f5b59b025d94064551a3ca`, with review input
`research/evidence/hf12-cusp-repair.md` at SHA-256
`fd5e35420c15494a47d51d4e0423621aa77314bfb31f6d4500cc5bdd4f22da35`.

## Verdict

**VERDICT: REPAIR.**  The pressure-only obstruction is true under the stated
centered Holder hypothesis, but its transfer to the heat endpoint needs a
direct comparison with the fixed center \(p_U\); (2) does not provide local
continuity between two moving pressures.  The general coupling necessity in
(9) is valid only after replacing the informal continuity and domination
clause by explicit uniform expansion hypotheses.  The fixed-\(\tau\)
directional derivative (13) is correct, but (15) is misdescribed: the original
coefficient-one mechanism cancels \(P_3\), not the whole cubic Euler
derivative against the whole pressure-speed derivative.  The exact full Euler
identity and a zero-set-safe comparison are given below.

## 1. Pressure-only endpoint repair

The static expansion is valid.  Disjoint support gives
\(p[U+bw_N]=p_U+b^2p[w_N]\), uniformly bounded in \(L^{3/2}\), so the
centered estimate (2) gives a uniform \(O(b^{2\alpha})=o(b)\).  Together with
the exact pressure-speed expansion, this proves (7).

At the heat endpoint one cannot infer
\(\mathfrak P(p[e^{\nu t_N\Delta}(U+aw_N)])
 -\mathfrak P(p[U+\lambda aw_N])=o(1)\) from (2), because (2) is centered
only at \(p_U\).  Instead set
\[
 z_N=e^{\nu t_N\Delta}(U+aw_N),\qquad
 v_N=U+\lambda aw_N,qquad \lambda=e^{-s}.
\]
The HF11 estimates give \(\|z_N-v_N\|_3=o_N(1)\) for fixed \(a\), while
the quadratic pressure estimate and the uniform \(L^3\) bounds give
\[
 \|p[z_N]-p_U\|_{3/2}
 \le \|p[z_N]-p[v_N]\|_{3/2}
      +\lambda^2a^2\|p[w_N]\|_{3/2}
 \le o_N(1)+Ca^2.                                      \tag{R1}
\]
Consequently
\[
 |\mathfrak P(p[z_N])-\mathfrak P(p_U)|
 \le C(o_N(1)+Ca^2)^\alpha.                            \tag{R2}
\]
The cubic and pressure-speed parts are locally Lipschitz in \(L^3\), so
direct expansion relative to \(U\) yields
\[
 \mathcal J_{\mathfrak P}(z_N)-\mathcal J_{\mathfrak P}(U)
 =-\lambda aA_N+O(a^2)+O(a^{2\alpha})+o_N(1),           \tag{R3}
\]
where, after fixing \(a\), \(N\) is chosen so the last errors are as small as
needed.  Subtracting the analogous static expansion at \(a\) gives a positive
heat increment.  Thus the claimed pressure-only obstruction survives with
exactly the stated threshold \(\alpha>1/2\).

## 2. Hypotheses needed for the general coupling claim

Existence and continuity of \(g_r(0+,p)\) alone do not justify (8).  In
particular, an \(L^{3/2}\) pressure perturbation is not pointwise control of
the second argument of a general Nemytskii integrand, and behavior off the
packet can also contribute at first order unless it is controlled.

A sufficient precise version is the following.  On a compact negative
pressure interval \(I\) containing the values of \(p_U\) on the packet ball,
assume
\[
 \sup_{p\in I}\left|{g(r,p)-g(0,p)\over r}-\gamma(p)\right|\to0
 \quad(r\downarrow0),                                  \tag{R4}
\]
with \(\gamma\) continuous, and assume that replacing \(p_U\) by the actual
packet or heat-endpoint pressure changes the integrated coupling by \(o(b)\),
uniformly in the packet sequence.  The latter follows, for example, from an
appropriate locally Lipschitz Nemytskii bound in the pressure variable plus
an integrable uniform domination; it does not follow from continuity of
\(\gamma\) alone.  Assume also an integrable envelope permitting (R4) to pass
under the integral.  Then localization and periodic averaging give
\[
 \int_B[g(b|w_N|,p_U)-g(0,p_U)]
 =b\int_B\gamma(p_U)|w_N|+o(b)                         \tag{R5}
\]
uniformly in the required choose-\(b\)-then-\(N\) order.  Heat damping changes
the leading coefficient from \(b\) to \(\lambda b\).  Localizing the packet
near a point where \(\gamma(p_U)<0\) then contradicts universal heat
nonincrease.  Under these explicit hypotheses, (9) is necessary for each
negative pressure value realizable by the background construction.  It is
not a consequence for an unrestricted general \(g\) as currently stated.

## 3. Static fixed-\(\tau\) coupling

The map \(u\mapsto\rho_\tau(|u|)=\sqrt{\tau^2+|u|^2}-\tau\) is smooth and
has velocity derivative \(u/\sqrt{\tau^2+|u|^2}\).  Since
\(0\le\rho_\tau(r)\le r\), the negative-pressure coupling is no smaller than
\(pr\), and the positive-pressure coupling is nonnegative.  The HF11 Young
bound therefore proves (11); \(|p\rho_\tau(r)|\le|p|r\) and Riesz boundedness
give the cubic upper bound.  This section passes.

## 4. Exact full Euler identity and zero sets

Let
\[
 F(u)={1\over3}\int r^3,\quad
 B_\tau(u)=\int p[u]\rho_\tau(r),\quad
 r=|u|,\quad r_\tau=\sqrt{r^2+\tau^2},
\]
and let \(V=-\mathbb P((u\cdot\nabla)u)=-N-\nabla p\).  Under the smoothness
and integrability hypotheses used in HF10, the globally valid fixed-\(\tau\)
Euler contribution is
\[
 \boxed{
 D(F+B_\tau)(u)[V]
 =\int r\,u\cdot V
  +\int {p\over r_\tau}u\cdot V
  +\int\rho_\tau(r)p_V,
 \qquad p_V=2R_iR_j(u_iV_j).}                          \tag{R6}
\]
Every integrand is defined on \(\{u=0\}\).  Since the transport part of
\(DF[V]\) vanishes,
\(DF[V]=P_3=\int p,u\cdot\nabla r\).  Thus (R6) can equivalently be written
\[
 P_3-\int p,u\cdot\nabla\rho_\tau(r)
 -\int {p\over r_\tau}u\cdot\nabla p
 +\int\rho_\tau(r)p_V.                                \tag{R7}
\]
This is the complete fixed-\(\tau\) Euler expression; it is not zero and has
no established sign.

For comparison with the valid unregularized contribution extracted from the
HF10 integrated identity, define
\[
 n={u\over r}\mathbf1_{\{r>0\}},\qquad
 \mathcal R_0(u;V)=\int r p_V-\int p,n\cdot\nabla p.   \tag{R8}
\]
Here \(P_3\) has already canceled against the \(-P_3\) component of the
pressure-speed correction; \(\mathcal R_0\) generally remains.  A globally
defined difference between (R6) and (R8) is
\[
 \boxed{
 \widetilde{\mathcal D}_\tau(u;V)
 =\int p\left({u\over r_\tau}-n\right)\cdot V
  +\int(\rho_\tau(r)-r)p_V.}                          \tag{R9}
\]
Indeed, the common unregularized pressure-speed contribution is
\(\int p n\cdot V+\int r p_V=-P_3+\mathcal R_0\), so
\[
 D(F+B_\tau)(u)[V]=\mathcal R_0(u;V)
                    +\widetilde{\mathcal D}_\tau(u;V). \tag{R10}
\]
Formula (R9) agrees with (15) on \(\{r>0\}\), but remains meaningful on the
zero set and does not assert that \(B(u)=\int p|u|\) has a two-sided
directional derivative there.  This is the exact repair to lines 129--148.
The sentence hypothesizing cancellation between the two complete derivatives
must be replaced by the statement that only \(P_3\) cancels in the HF10
integrated identity, leaving (R8), and that the smooth coupling adds (R9).

## Audit record

**REVIEWED SCOPE:** the centered-Holder pressure-only obstruction, the general
coupling necessity, static coercivity of \(g_\tau\), and the complete
fixed-\(\tau\) Euler contribution including velocity zero sets.

**FIRST BAD BRIDGE:** lines 63--68 invoke the HF11 heat transfer as though (2)
gave local continuity between the endpoint pressure and the ideal damped
packet pressure.  It only controls values relative to \(p_U\).  Equations
(R1)--(R3) repair the implication directly.

**REPLACEMENT ARGUMENT:** use (R1)--(R3) for the pressure-only endpoint, add
the explicit hypotheses (R4)--(R5) to the general coupling statement, and
replace (15)'s cancellation interpretation by (R6)--(R10).

**CONDITIONAL SUFFIX THAT SURVIVES:** pressure-only corrections with centered
Holder exponent greater than \(1/2\) cannot enforce universal heat
monotonicity; \(g_\tau\) removes the linear speed cusp and preserves static
cubic coercivity; its complete Euler contribution remains uncontrolled.

**UNNECESSARY DEPENDENCIES:** full local continuity of \(\mathfrak P\) is not
needed.  Centered control at \(p_U\), combined with (R1), suffices.

**NON-CLAIMS:** no heat monotonicity for \(g_\tau\), bound or sign for
(R6)--(R10), Navier--Stokes estimate, HIGH-PRESSURE estimate, continuation,
or global regularity is established.

**REOPENING CONDITION:** the general pointwise necessity (9) may be stated
without qualification only after hypotheses implying the uniform integrated
expansion (R5) for both the static and heat endpoint families are supplied.
