# Independent audit of the pressure--speed coercivity counterexample

VERDICT: **REPAIR**

REVIEWED SCOPE: `research/evidence/hf10-pressure-speed-coercivity.md` at
SHA-256
`e9bd4fcce90e8280013f2a588d1072a9345f749a7e6cf90d465f54fa5ed5434d`,
on full base commit `4a377b5550a3fb46c0ad85933a72d7f3f44771e9`.
The audit covers the rough planar swirl as a distribution, the fixed pressure
gauge, smoothing, the anisotropic three-dimensional lift, and the restricted
coefficient threshold.  It does not audit the separate evolution identity or
promote any claim.

FIRST BAD BRIDGE: Equation (17) is derived from
\(B\ge-3M/4\) by multiplication by \(\kappa\), but it is stated without the
necessary condition \(\kappa\ge0\).  For \(\kappa<0\), multiplication
reverses that inequality.  The displayed lower bound
\[
 {1\over3}M+\kappa B\ge(1/3-3\kappa/4)M
\]
is therefore unsupported and generally points in the wrong direction for
negative \(\kappa\).  This occurs after the complete construction of the
coefficient-one three-dimensional counterexample, which remains valid.

EVIDENCE:

1. The rough swirl calculation is valid when the nonlinear term is defined
   as \(\operatorname{div}(v_0\otimes v_0)\).  On an annulus,
   \[
   \operatorname{div}(e_\vartheta\otimes e_\vartheta)=-e_r/r.
   \]
   There is no measure on the outer rim because
   \((v_0\otimes v_0)e_r=v_0(v_0\cdot e_r)=0\).  The same zero normal flux
   on a shrinking inner circle eliminates an origin measure, while \(1/r\)
   is locally integrable in two dimensions.  Thus
   \[
   \operatorname{div}(v_0\otimes v_0)
   =-\mathbf1_{0<r<1}e_r/r
   \]
   distributionally.  The function \(p_0=\mathbf1_{r<1}\log r\) is locally
   integrable and continuous across \(r=1\), so its distributional gradient
   is \(\mathbf1_{0<r<1}e_r/r\), with neither a rim measure nor an origin
   measure.  This proves the claimed distributional Euler balance in the
   precise divergence-form sense.

2. Taking a divergence gives
   \(\Delta p_0=-\partial_\alpha\partial_\beta
   (v_{0,\alpha}v_{0,\beta})\), which is exactly the equation obeyed by
   \(R_\alpha^{(2)}R_\beta^{(2)}
   (v_{0,\alpha}v_{0,\beta})\) under the declared multiplier convention.
   Both representatives lie in \(L^{3/2}(\mathbb R^2)\).  Their difference
   is a distributionally harmonic \(L^{3/2}\) function and hence is zero
   (equivalently, its Fourier transform is supported at the origin, so it is
   a polynomial, and no nonzero polynomial belongs to \(L^{3/2}\)).  This
   verifies both the gauge and its uniqueness.  Direct integration gives
   \(M/3=\pi/3\), \(B=-\pi/2\), and total \(-\pi/6\).

3. The origin and rim smoothing is legitimate.  Exact behavior
   \(f_n(r)=c_nr\) near zero makes
   \(f_ne_\vartheta=c_n(-y,x)\) smooth there; choosing the outer transition
   flat at its support boundary gives a compactly supported smooth field.
   The transitions occupy sets whose area tends to zero, so bounded
   convergence yields \(v_n\to v_0\) in \(L^3\).  Consequently
   \(v_n\otimes v_n\to v_0\otimes v_0\) in \(L^{3/2}\), and the
   \(L^{3/2}\)-bounded double Riesz transform gives strong convergence of
   the fixed-gauge pressures.  Hölder then gives continuity of
   \(\int p(v_n)|v_n|\), so a smooth planar swirl with negative functional
   is obtained.

4. The three-dimensional lift preserves solenoidality because its vertical
   component vanishes and the horizontal factor is solenoidal.  Under
   \(z=L\zeta\), the horizontal double Riesz multiplier becomes exactly
   \[
   -{\xi_\alpha\xi_\beta\over|\xi_h|^2+L^{-2}\xi_\zeta^2}.
   \]
   It is conjugate to the ordinary three-dimensional double Riesz transform
   by the anisotropic dilation.  The Jacobian factors in the two dilation
   norms cancel, so its \(L^q\) operator norm is independent of \(L\) for
   every \(1<q<\infty\).

5. For the fixed smooth input, the multipliers converge almost everywhere
   and are bounded in magnitude, proving strong \(L^2\) convergence by
   Plancherel and dominated convergence.  Choose any \(1<q<3/2\).  Uniform
   \(L^q\) bounds for both the anisotropic operators and the slicewise
   two-dimensional limit bound their difference in \(L^q\).  Interpolation
   between this bound and strong \(L^2\) convergence proves the asserted
   strong \(L^{3/2}\) convergence.  Since \(\eta\ge0\),
   \(|u_L(x_h,L\zeta)|=\eta(\zeta)|v(x_h)|\), and the pressure limit is
   \(\eta^2p(v)\).  The normalized cubic functional therefore converges to
   \((\int\eta^3)\mathcal C_2(v)<0\).  This proves the stated smooth,
   compactly supported, divergence-free \(\mathbb R^3\) counterexample.

6. The logarithmic-coordinate identities (15) are correct.  Hölder gives
   the correlation bound, and
   \(\int_0^\infty e^{-4h/3}dh=3/4\), hence
   \(-B\le3M/4\).  Moreover formula (2) shows \(B\le0\) for every
   nonnegative radial swirl.  The log-plateau sequence verifies sharpness of
   the constant \(3/4\): fixed-\(h\) normalized correlations tend to one,
   Hölder supplies domination by the integrable kernel, and support away from
   the origin makes the reconstructed swirls smooth after the declared fixed
   transition cutoffs.

7. As an optional strengthening, once one negative three-dimensional field
   \(u\) is known, fixed-energy concentration makes the functional
   arbitrarily negative.  For
   \(u_\lambda(x)=A_\lambda u(\lambda x)\), choose
   \(A_\lambda=\lambda^{3/2}\) to keep \(\|u_\lambda\|_2\) fixed.  Pressure
   is quadratic under amplitude and dilation, so
   \(\mathcal C(u_\lambda)=\lambda^{3/2}\mathcal C(u)\to-\infty\).
   This is a static strengthening only, not a trajectory statement.

REPLACEMENT ARGUMENT: State (17) only for \(\kappa\ge0\), and replace the
unrestricted lower bound by
\[
 {1\over3}M+\kappa B\ge
 \begin{cases}
  (1/3-3\kappa/4)M,&\kappa\ge0,\\
  (1/3)M,&\kappa<0,
 \end{cases}                                                   \tag{R}
\]
where the second line uses \(B\le0\).  Formula (R), the sharp log-plateau
sequence for positive \(\kappa\), and the trivial sign for negative
\(\kappa\) prove the original qualitative conclusion: within nonnegative
smooth compactly supported planar swirls, the functional has a uniform
positive lower bound in terms of \(M\) exactly when \(\kappa<4/9\); it is
nonnegative but not positively coercive at \(\kappa=4/9\); and it takes
negative values when \(\kappa>4/9\).  No change to the coefficient-one
counterexample is required.

CONDITIONAL SUFFIX THAT SURVIVES: After the piecewise repair, the restricted
sharp coefficient threshold survives.  Independently of that optional
section, the smooth three-dimensional example with
\(\frac13\int|u|^3+\int p|u|<0\) is already proved and rules out universal
nonnegativity or positive coercivity of the coefficient-one functional.

UNNECESSARY DEPENDENCIES: The power-law diagnostic (6) is not needed for the
counterexample or the sharpness proof.  The restricted threshold is not
needed for the three-dimensional coefficient-one conclusion.  No
Navier--Stokes evolution fact is needed for this static construction.

NON-CLAIMS: The audit does not turn the static field into a Navier--Stokes
trajectory and does not refute a time-integrated pressure estimate.  It proves
no blow-up, failure of regularity, or optimal coefficient threshold outside
the declared planar nonnegative radial-swirl class.

REOPENING CONDITION: none for the repaired static counterexample.  Any use of
the pressure--speed correction as part of a dynamical modified energy still
requires an independent evolution audit and a separate coercive control.
