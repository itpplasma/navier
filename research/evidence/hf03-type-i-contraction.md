# HF03: backward cutoffs do not create a Type-I contraction

Status: bounded DISCOVER/REPAIR test for the unforced equation on
\(\mathbb R^3\).  The stronger pointwise Type-I hypothesis is used as a
diagnostic assumption.  The normalized-enstrophy Type-I condition is treated
separately and is strictly weaker.  No regularity or global high-pressure
claim is made.

## 1. The functional that actually has to contract

Normalize a candidate point to \((0,0)\), write
\(Q_r=B_r\times(-r^2,0)\), and define the standard scale-invariant quantities

\[
 C(r)=r^{-2}\int_{Q_r}|u|^3,qquad
 D(r)=r^{-2}\int_{Q_r}|p-(p)_{B_r}(t)|^{3/2}.           \tag{1}
\]

A complete epsilon-regularity input has to control both velocity and pressure,
so take

\[
 \mathcal Q(r)=C(r)+D(r).                              \tag{2}
\]

For a suitable weak solution, a named CKN-type criterion supplies a universal
\(\varepsilon_{\rm CKN}>0\) such that
\(\mathcal Q(r)<\varepsilon_{\rm CKN}\) at one scale (with the precise
cylinder convention of that theorem) implies regularity at the center.  A
uniform bound \(\mathcal Q(r)\leq K(C_*)\) is not enough.

Under the stronger pointwise Type-I estimate

\[
 |u(x,t)|\leq {C_*\over\sqrt{|x|^2-t}},                \tag{PTI}
\]

direct scaling gives \(C(r)\leq C C_*^3\), uniformly in \(r\).  Indeed,

\[
 r^{-2}\int_0^{r^2}\int_0^r
 {C C_*^3R^2\over(R^2+s)^{3/2}},dR,ds
 =C C_*^3.                                             \tag{3}
\]

Local pressure decomposition and harmonic-pressure iteration can then bound
\(D(r)\) in terms of \(C_*\) and fixed outer data.  These facts establish
boundedness of \(\mathcal Q\), not decay below a universal epsilon.

The normalized-enstrophy hypothesis

\[
 \sup_{0<r<r_0}r^{-1}\int_{Q_r}|\nabla u|^2\leq K       \tag{NETI}
\]

does not imply (PTI) or the pointwise estimates used below.  Nothing in this
note transfers the cutoff calculation from (PTI) to (NETI).

## 2. Time-dependent localized cubic balance

Let \(w=|u|u\), and let \(0\leq\eta(x,t)\leq1\) be smooth and compactly
supported in space.  The exact identity is

\[
\begin{aligned}
 {1\over3}{d\over dt}\int\eta|u|^3
 +\nu\int\eta D_3
 &=\int p\,\operatorname{div}(\eta w)
   +{1\over3}\int|u|^3u\cdot\nabla\eta\\
 &\quad+{1\over3}\int|u|^3(\partial_t\eta+\nu\Delta\eta),          \tag{4}
\end{aligned}
\]

where

\[
 D_3=|u||\nabla u|^2+|u||\nabla|u||^2.                \tag{5}
\]

The pressure is gauge invariant because it occurs as the single pairing
\(\int p\operatorname{div}(\eta w)\).  Formula (4) shows exactly what a
backward cutoff can cancel.

## 3. Backward caloric cutoff: exact cancellation, unchanged incoming mass

Fix a smooth final spatial cutoff \(\eta_0\), and for \(t<0\) define

\[
 \eta(x,t)=e^{\nu(-t)\Delta}\eta_0(x).                 \tag{6}
\]

Then

\[
 \partial_t\eta+\nu\Delta\eta=0,                      \tag{7}
\]

so the last term in (4) vanishes exactly.  Integrating from \(-R^2\) to
\(-\delta\) gives

\[
\begin{aligned}
 {1\over3}\int\eta(-\delta)|u(-\delta)|^3
 +\nu\int_{-R^2}^{-\delta}\int\eta D_3
 &={1\over3}\int\eta(-R^2)|u(-R^2)|^3\\
 &\quad+\int_{-R^2}^{-\delta}\int
 \left[p\operatorname{div}(\eta w)
 +{1\over3}|u|^3u\cdot\nabla\eta\right].             \tag{8}
\end{aligned}
\]

Thus caloricity trades the diffusion cutoff error for spatial spreading of
\(\eta\), but leaves the incoming cubic mass with coefficient exactly one.
It cannot also make \(\eta(-R^2)=0\): a solution of the backward adjoint heat
equation that vanishes on one time slice is identically zero, and hence has
zero final cutoff.  This is the first algebraic obstruction.

Under (PTI), the incoming term is only critical-size.  If the cutoff samples
\(B_R\) at time \(-R^2\), the available estimate is

\[
 \int_{B_R}|u(x,-R^2)|^3dx\leq C C_*^3,               \tag{9}
\]

with no factor tending to zero.  If a logarithmic cutoff reaches from an
inner radius \(r\) to \(R\gg r\) while the incoming time remains \(-r^2\),
the available envelope instead gives \(C C_*^3\log(R/r)\).  Hence backward
caloric propagation does not repair the incoming-mass problem.

## 4. Temporal ramp: removal of the time face recreates a unit coefficient

Take a spatial cutoff \(\eta_r\) and a nondecreasing temporal ramp
\(\zeta\) which is zero at \(-r^2\) and one by \(-\sigma^2r^2\), where
\(0<\sigma<1\).  Put \(\eta(x,t)=\zeta(t)\eta_r(x)\).  The incoming term in
the integrated identity vanishes, but (4) contains

\[
 T_\zeta={1\over3}\int_{-r^2}^{-\sigma^2r^2}
                    \int |u|^3\eta_r\zeta'(t).         \tag{10}
\]

For the standard linear ramp,
\(\zeta'=((1-\sigma^2)r^2)^{-1}\), and therefore

\[
 3T_\zeta\leq {1\over1-\sigma^2},C(r)                \tag{11}
\]

after enlarging the cylinder by only the fixed cutoff factor.  The coefficient
\((1-\sigma^2)^{-1}\) is strictly larger than one.

This is not an artifact of choosing a linear ramp.  Every nonnegative
monotone ramp from zero to one satisfies

\[
 \int_{-r^2}^{-\sigma^2r^2}\zeta'(t)dt=1.             \tag{12}
\]

Without information locating a time at which the cubic mass is smaller than
its scale average, the best uniform estimate of (10) necessarily carries a
coefficient at least one.  Allowing a sign-changing ramp would destroy the
positivity needed on the left of (4) and gives no controlled replacement.

One may combine a temporal ramp with a backward caloric spatial cutoff.  The
product rule changes the last term in (4) to \(\zeta'\eta|u|^3/3\); the
caloric pieces still cancel, so the same unit-variation obstruction remains.

## 5. What signed pressure absorption would actually yield

Assume, only to test the mechanism, that the active local pressure work obeys
a strict signed estimate with coefficient \(\theta<1\), and that logarithmic
spatial cutoffs reduce all transport, harmonic-pressure, and spatial cutoff
errors to \(\varepsilon_{r,R}\to0\) as \(r/R\to0\).  Applying (4) with the
temporal ramp, absorbing the weighted dissipation, and discarding the
nonnegative terminal slice gives at best

\[
 (1-\theta)\nu
 \int_{-\sigma^2r^2}^{0}\int_{B_{\sigma r}}D_3
 \leq {1\over3(1-\sigma^2)}C(c r)+\varepsilon_{r,R},  \tag{13}
\]

where \(c>1\) depends only on the cutoff support convention.  Constants of
three can be moved between the definition of the cubic balance and the right
side; the decisive coefficient inherited from the ramp is
\((1-\sigma^2)^{-1}>1\).

Equation (13) is a weighted-dissipation bound.  It is not a recurrence for
\(C(\sigma r)\), because the terminal cubic term in (4) is a spatial slice,
whereas \(C\) is a spacetime integral.  Under (PTI), the slice integral can
even grow logarithmically as its time approaches zero; no uniform terminal
slice bound follows from (3).

One can average (4) over terminal times to replace slices by spacetime
integrals, but the incoming slices average to another copy of \(C(c r)\) with
coefficient one.  Fubini does not create a number below one.  Thus the best
schematic velocity recurrence furnished by this mechanism is

\[
 C(\sigma r)\leq K(\sigma,\theta)C(c r)
                  +\varepsilon_{r,R},qquad K\geq1,   \tag{14}
\]

even before pressure is added.

## 6. Pressure recurrence prevents a hidden repair

For completeness, decompose pressure on \(B_r\) into a local Riesz part and
a harmonic remainder.  Calderon--Zygmund scaling and interior harmonic decay
give the standard form, for \(0<\sigma<1/2\),

\[
 D(\sigma r)
 \leq C\sigma^{-2}C(r)+C\sigma^\alpha D(r),            \tag{15}
\]

for some universal \(\alpha>0\), with harmless changes in the concentric
cylinder convention.  The first coefficient grows as \(\sigma\downarrow0\):
active-scale pressure is generated by the same \(u\otimes u\) that defines
\(C(r)\).  Choosing \(\sigma\) small makes the harmonic coefficient
contractive but makes the local-pressure coefficient large.

Combining (14) and (15) for the complete functional (2) yields only

\[
 \mathcal Q(\sigma r)
 \leq [K(\sigma,\theta)+C\sigma^{-2}]C(c r)
      +C\sigma^\alpha D(c r)+\varepsilon_{r,R}.        \tag{16}
\]

There is no choice of \(\sigma\) for which the displayed argument makes all
coefficients a universal number below one.  Under arbitrary (PTI),
\(C(c r)\) is bounded by a function of \(C_*\), not small.  Equation (16)
therefore cannot be iterated to cross \(\varepsilon_{\rm CKN}\).

## 7. Renormalizing the incoming cubic mass

Subtracting an a priori Type-I envelope does not alter the recurrence.  If
\(M_*=C C_*^3\) and \(\widetilde C(r)=C(r)-M_*\), a coefficient-one estimate
\(C(\sigma r)\leq C(r)+o(1)\) becomes

\[
 \widetilde C(\sigma r)\leq\widetilde C(r)+o(1).       \tag{17}
\]

Moreover \(\widetilde C\) is not nonnegative and smallness of
\(\widetilde C\) says nothing about whether \(C\) is below the CKN threshold.
Subtracting a multiple of \(\log(R/r)\) can manufacture a negative drift in
the rewritten algebra, but adds the same quantity back when recovering
\(C(r)\); it is not a coercive renormalization.

An effective subtraction would need a dynamically defined leading profile
whose remainder has a positive norm and whose pressure decouples.  No such
profile or orthogonality is supplied by (PTI), so this is a new compactness or
rigidity problem rather than an algebraic repair.

## 8. Result, exact obstruction, and reopening condition

**Concrete repair tested:** a backward caloric cutoff cancels
\(\partial_t\eta+\nu\Delta\eta\) exactly.  It leaves the incoming cubic mass
with coefficient one.  A temporal ramp removes that mass but introduces
\(T_\zeta\), whose coefficient is at least one because the ramp has total
variation one.  Renormalizing by the Type-I envelope does not change that
coefficient or yield a positive CKN functional.

**Information genuinely added:** under the stronger pointwise Type-I bound,
logarithmic spatial cutoffs can suppress geometric transport and diffusion
leakage, while backward caloric cutoffs can cancel the time/diffusion cutoff
combination.  These two gains are compatible, but neither controls the
incoming or ramp-generated critical cubic mass.  No corresponding gain was
proved under normalized enstrophy (NETI).

**First algebraic obstruction:** every nontrivial nonnegative time cutoff
either retains an incoming cubic slice or pays a positive time-derivative term
of unit total weight.  The signed pressure estimate controls neither term.
The local pressure recurrence then couples \(D\) back to \(C\) with a
non-small coefficient.

**Conditional suffix:** if an additional argument proves a genuine recurrence

\[
 \mathcal Q(\sigma r)\leq\kappa\mathcal Q(r)+\epsilon(r),qquad
 0<\kappa<1,quad\epsilon(r)\to0,                      \tag{18}
\]

for the complete velocity-pressure functional (2), iteration gives a scale
where \(\mathcal Q<\varepsilon_{\rm CKN}\), and the named epsilon-regularity
theorem applies.  Equation (18) is not derived here.

**Non-claims:** this mechanism test does not prove pointwise or
normalized-enstrophy Type-I regularity, the universal high-pressure estimate,
or any terminal Clay claim.  It does not replace the arbitrary-data target by
a Type-I theorem.
