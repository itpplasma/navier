# HF01 Type-I regime test: localized cubic pressure balance

Status: research evidence, 2026-09-05. The universal target remains arbitrary
smooth unforced Navier--Stokes data on \(\mathbb R^3\). Type I is used here
only as a restricted diagnostic regime near one candidate singular point.
Nothing below extrapolates one-point regularity to an entire terminal time.

## 1. Exact scope of the Lei--Ren statements

Lei and Ren consider a local suitable weak solution \(v\) in a unit
parabolic cylinder. For a singular point \(w=(x,t)\), their condition (1.11)
defines a Type-I point by
\[
 \limsup_{r\downarrow0}{1\over r}
 \int_{Q(r,w)}|\nabla v|^2\,dx\,dt<\infty.             \tag{LR-1.11}
\]
At \(w=(0,0)\), they state that the pointwise bound
\[
 |v(x,t)|\le {C_*\over\sqrt{|x|^2-t}}
 \quad\hbox{in }Q(r)                                  \tag{LR-1.12}
\]
implies (LR-1.11). They then explicitly call exclusion of blow-up under
(1.11) or (1.12) a major open problem for the general three-dimensional
equation.

Their Theorem D is not a general Type-I theorem. It assumes an
**axially symmetric** local suitable weak solution and proves regularity at
the origin from the weaker logarithmically supercritical condition
\[
 \limsup_{r\downarrow0}
 {\int_{Q(r)}|\nabla v|^2\,dx\,dt
  \over r(\ln|\ln r|)^\mu}<\infty
\]
for one absolute \(\mu>0\). The axial symmetry is load bearing: their proof
passes through the swirl quantity and their local small-swirl Theorem C.
These statements were inspected in the primary preprint
[arXiv:2210.01783, equations (1.11), (1.12), Theorem D and its proof](https://arxiv.org/abs/2210.01783);
the published article is
[Advances in Mathematics 445 (2024), 109654](https://doi.org/10.1016/j.aim.2024.109654).

The local general target tested here is therefore the still-open implication
\[
 \sup_{0<r<r_0}{1\over r}\int_{Q_r(z_0)}|\nabla u|^2<\infty
 \quad\Longrightarrow\quad z_0\ \hbox{is regular}.     \tag{TI}
\]
Even a proof of (TI) at one prescribed point would not by itself show that
every point at a putative terminal time satisfies its premise.

## 2. Localized cubic identity

For clarity normalize the candidate point to \(z_0=(0,0)\), and let
\(\eta\in C_c^\infty(B_R)\) be spatial and time independent. On a classical
interval, multiply
\[
 u_t+(u\cdot\nabla)u+\nabla p=\nu\Delta u
\]
by \(\eta |u|u\). Regularization at \(u=0\), exactly as in the global cubic
identity, gives
\[
\begin{aligned}
 {1\over3}{d\over dt}\int\eta|u|^3
 +\nu\int\eta\bigl(|u||\nabla u|^2
                   +|u||\nabla|u||^2\bigr)
 &=\int\eta p\,u\cdot\nabla|u|                         \\
 &\quad+{1\over3}\int |u|^3u\cdot\nabla\eta             \\
 &\quad+\int p|u|u\cdot\nabla\eta
       +{\nu\over3}\int |u|^3\Delta\eta.               \tag{1}
\end{aligned}
\]
The signs follow from
\[
 \int\eta (u\cdot\nabla)u\cdot|u|u
 =-{1\over3}\int |u|^3u\cdot\nabla\eta
\]
and
\[
 \nu\int\eta\Delta u\cdot|u|u
 =-\nu\int\eta D_3+{\nu\over3}\int|u|^3\Delta\eta.
\]

The two pressure terms must be kept together:
\[
 \int\eta p\,u\cdot\nabla|u|
 +\int p|u|u\cdot\nabla\eta
 =\int p\,\operatorname{div}(\eta|u|u).                \tag{2}
\]
This makes (2) invariant under adding a function of time to \(p\).
Estimating the two terms independently would introduce an artificial
dependence on the pressure normalization.

For a space-time cutoff \(\eta(x,t)\), equation (1) acquires the additional
right-hand term \((1/3)\int |u|^3\partial_t\eta\). Thus a parabolic cutoff
adds another scale-critical boundary error rather than removing one.

## 3. Local and harmonic pressure

Choose \(\chi\in C_c^\infty(B_R)\), equal to one on the support of \(\eta\),
and decompose
\[
 p=p_{\rm loc}+p_{\rm harm},\qquad
 p_{\rm loc}=R_iR_j(\chi u_i u_j).
\]
Then \(p_{\rm harm}\) is harmonic in the spatial region where \(\chi=1\).
The local component obeys the scale-invariant Calderon--Zygmund estimate
\[
 \int_{Q_r}|p_{\rm loc}|^{3/2}
 \le C\int_{(-r^2,0)\times B_R}|u|^3,                 \tag{3}
\]
with the right-hand localization adjusted to the chosen \(\chi\).

For the harmonic component one must subtract a spatial constant
\((p_{\rm harm})_{B_\rho}(t)\) inside (2). Interior harmonic estimates then
give, for \(r\ll\rho<R\), a positive power of \(r/\rho\) multiplying an
outer \(L^{3/2}\) pressure norm. This makes the inherited far-field harmonic
oscillation perturbative at sufficiently deep scales, provided that fixed
outer norm is finite. It does not make \(p_{\rm loc}\) small: the pressure
generated at the active scale remains critical.

Thus harmonic pressure is a localization bookkeeping issue, not the missing
signed high-frequency cancellation. The local Riesz part is still generated
by \(u\otimes u\) at the same scale.

## 4. Radius-\(r\) error ledger

Take \(\eta_r=1\) on \(B_r\), supported in \(B_{2r}\), with
\[
 |\nabla\eta_r|\le Cr^{-1},\qquad
 |\Delta\eta_r|\le Cr^{-2}.
\]
Integrating (1) over \((-r^2,0)\), the geometric errors are
\[
\begin{aligned}
 B_{\rm tr}(r)&={1\over3}\int_{Q_{2r}}|u|^3u\cdot\nabla\eta_r,\\
 B_{\rm pr}(r)&=\int_{Q_{2r}}p|u|u\cdot\nabla\eta_r,\\
 B_{\rm dif}(r)&={\nu\over3}\int_{Q_{2r}}|u|^3\Delta\eta_r.
                                                               \tag{4}
\end{aligned}
\]
Their absolute estimates are
\[
 |B_{\rm tr}|\le Cr^{-1}\int_{Q_{2r}}|u|^4,\quad
 |B_{\rm pr}|\le Cr^{-1}\int_{Q_{2r}}|p||u|^2,\quad
 |B_{\rm dif}|\le C\nu r^{-2}\int_{Q_{2r}}|u|^3.       \tag{5}
\]
Every expression in (5) is invariant under the Navier--Stokes scaling.
Consequently a uniform Type-I bound can at best make these terms uniformly
bounded by a function of the Type-I constant and outer local energies. It
does not make any coefficient tend to zero as \(r\downarrow0\).

This is transparent under the stronger pointwise condition (LR-1.12).
On the annulus \(r<|x|<2r\), \(|u|\lesssim C_*/r\), and the space-time volume
is \(O(r^5)\). Hence
\[
 |B_{\rm tr}(r)|\lesssim C_*^4,\qquad
 |B_{\rm dif}(r)|\lesssim \nu C_*^3.                  \tag{6}
\]
The local pressure satisfies the corresponding scale-invariant
\(L^{3/2}\) bound, so Holder together with the pointwise velocity estimate
gives \(|B_{\rm pr,loc}(r)|\lesssim C(C_*)\). The harmonic oscillation is
controlled as in Section 3. None of these order-one bounds is small for an
arbitrary Type-I constant.

Condition (LR-1.11) is weaker than (LR-1.12). It only controls
\[
 E(r)={1\over r}\int_{Q_r}|\nabla u|^2\le K.           \tag{7}
\]
The local energy inequality and pressure iteration can bound the other
standard scale-invariant quantities on smaller cylinders in terms of \(K\)
and fixed outer data, but no general theorem turns finite \(K\) into the
smallness required by the CKN criterion. Lei--Ren identify removal of that
smallness as open. In particular, (7) alone supplies no direct estimate of
the \(L^4\) term in (5) with a coefficient vanishing at small \(r\).

## 5. A logarithmic-cutoff repair and its limit

The stronger pointwise regime permits one genuine geometric improvement.
Let \(\eta_{r,\rho}\) transition from one to zero across
\(r<|x|<\rho\) approximately logarithmically, so
\[
 |\nabla\eta_{r,\rho}(x)|
 \lesssim {1\over |x|\log(\rho/r)},\qquad
 |\Delta\eta_{r,\rho}(x)|
 \lesssim {1\over |x|^2\log(\rho/r)}.                 \tag{8}
\]
Integrate only over the short time interval \((-r^2,0)\). Using
\(|u(x,t)|\lesssim C_*/\sqrt{|x|^2-t}\), radial integration gives
\[
 |B_{\rm tr}(r,\rho)|+|B_{\rm dif}(r,\rho)|
 \le {C(C_*,\nu)\over\log(\rho/r)}                    \tag{9}
\]
up to harmless contributions at the smoothed endpoints of the cutoff.
The same gain applies to the local pressure boundary term if its annular
scale-invariant \(L^{3/2}\) norms are uniformly controlled; the harmonic
oscillation has the separate positive-power gain from Section 3.

This is a viable test of the short-heat defect mechanism: the short time
\(r^2\) combined with a long logarithmic spatial transition can suppress
geometric boundary leakage under (LR-1.12). It does **not** prove (TI):

1. finite normalized enstrophy (LR-1.11) does not give the pointwise bound
   used in (9);
2. the interior term
   \(\int\eta p_{\rm loc}u\cdot\nabla|u|\) retains critical size and no sign;
3. choosing \(\rho/r\to\infty\) imports a range of larger spatial scales, so
   uniform annular pressure control must be proved rather than assumed.

In particular, the logarithmic cutoff repairs boundary leakage but does not
produce the universal signed high-frequency absorption coefficient
\(\theta<1\).

## 6. Exact first missing step

After harmonic-pressure decay and logarithmic boundary control, the first
missing implication in the stronger pointwise Type-I test is a local signed
estimate of the form
\[
\begin{aligned}
 \int_{-r^2}^{0}\int \eta_{r,\rho}
 p_{\rm loc}\,u\cdot\nabla|u|
 &\le \theta\nu
 \int_{-r^2}^{0}\int\eta_{r,\rho}
 \bigl(|u||\nabla u|^2+|u||\nabla|u||^2\bigr)\\
 &\quad+o_{r/\rho\to0}(1),                            \tag{10}
\end{aligned}
\]
with one \(\theta<1\), uniformly for arbitrary Type-I constants. No estimate
derived here proves (10). Absolute Calderon--Zygmund bounds give an order-one
coefficient depending on the Type-I size, not a universal subunit
coefficient.

For the genuinely general target (LR-1.11), an earlier step is already
missing: derive annular \(L^4\), local-pressure, and persistence control
sufficient to make the cutoff errors small from finite \(E(r)\), without
assuming pointwise Type I, symmetry, or CKN smallness. This is essentially
the open general one-point Type-I problem identified by Lei--Ren.

## Frontier record

**MODE / RESULT:** REPAIR/FALSIFY. Localization is exact, harmonic pressure
can be separated, and logarithmic cutoffs suppress geometric errors under
the stronger pointwise Type-I rate. The same argument does not close finite
normalized enstrophy.

**FIRST GAP:** prove (10) in the pointwise Type-I regime; for the general
local target, first produce the missing small annular bounds from (LR-1.11).

**SURVIVING CONDITIONAL SUFFIX (corrected after independent audit):** even
granting (10) and small boundary errors, the identity gives only
\(X_\eta(0^-)+(1-\theta)\nu\mathcal D_\eta
\le X_\eta(-r^2)+o(1)\), with the endpoint interpreted through compact
classical intervals. The incoming cubic mass is not small under arbitrary
pointwise Type I; a long logarithmic cutoff can introduce a
\(C_*^3\log(\rho/r)\) upper bound. No epsilon-regularity iteration follows
from the displayed estimates. A proved contraction of a complete velocity
and pressure functional, or the full smallness hypotheses of an exact
epsilon criterion, is an additional missing input. Likewise, harmonic
pressure oscillation decay must be paired with the local velocity factor
and an appropriate time-integrable outer pressure norm before calling its
cubic flux perturbative. See `hf02-review-type-i.md` for the frozen audit.

**NON-CLAIMS:** Theorem D is used only in its axisymmetric class. This note
does not prove general Type-I regularity, does not show that every point at a
terminal time is Type I, and does not prove the universal global HF
absorption hypothesis.
