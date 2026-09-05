# Independent audit of the HF03 caloric-scale repair

VERDICT: **REPAIR**

REVIEWED SCOPE: `hf03-caloric-scale.md`, frozen at base commit
`43a11d4715d7e09f07439accfba6af7f9bac6c18` and SHA-256
`e449bfaf9f7ecdc13bec0de16fc46e770d5ea96013d314e36f29813f42583c40`.
The digest was reproduced before review.  The review covers the caloric
kernel estimates, the localized identity, the incoming-face gain, the two
boundary ledgers, and the local truncation.  It does not promote the note or
audit a larger regularity argument.

FIRST BAD BRIDGE: equations (11)--(12) prove only
\(\mathcal T_{r,R}\leq C_\nu C_*^4\).  They do not prove the subsequent
unqualified statement that “the transport boundary does not” gain, nor that
the actual signed transport leakage has a nonzero order-one size as
\(r/R\to0\).  The two positive comparison integrals used in the upper bound
approach nonzero constants, but the integrand estimate can be strict and the
signed integral can cancel.  The following caveat partly recognizes this,
yet Sections 5 and 7 again call the boundary terms “order-one errors,” an
“exact surviving loss,” and quantities “with no decay.”  Those are stronger
conclusions than the displayed upper bounds support.

EVIDENCE:

1. The heat-kernel scale is correct.  With
   \(\ell^2=r^2+\nu s\), convolution of a bounded cutoff supported at scale
   \(r\) gives
   \[
     |\eta_r|\lesssim_\nu (r/\ell)^3e^{-c_\nu|x|^2/\ell^2},\qquad
     |\nabla\eta_r|\lesssim_\nu (r/\ell)^3\ell^{-1}
          e^{-c_\nu|x|^2/\ell^2}.
   \]
   The gradient estimate remains valid as \(s\downarrow0\): it reduces to
   the natural \(r^{-1}\) cutoff scale.  Constants necessarily depend on the
   fixed positive viscosity (and on \(\chi\)); the note consistently allows
   this.  It does not claim viscosity-uniform estimates.

2. The localized cubic identity (6) has the correct coefficients and signs.
   Multiplication by \(\eta |u|u\), integration by parts, and
   \(\operatorname{div}u=0\) give the stated dissipation, pressure pairing,
   transport-boundary term, and
   \((\partial_t\eta+\nu\Delta\eta)|u|^3/3\) term.  The use of
   \(-\delta<0\) before a weak limiting argument avoids assuming a classical
   trace at the candidate singular time.

3. The incoming estimate (8) is correct.  At \(s=R^2\), the kernel amplitude
   is \(O_\nu((r/R)^3)\), and
   \[
      \int_{\mathbb R^3}e^{-c_\nu|x|^2/R^2}
          (|x|^2+R^2)^{-3/2}\,dx=O_\nu(1).
   \]
   Hence the incoming weighted cubic mass is
   \(O_\nu(C_*^3(r/R)^3)\).  This validly repairs the earlier coefficient-one
   objection.

4. The radial bound (10) is valid.  Dropping the Gaussian already gives
   \(\int_{\mathbb R^3}(|x|^2+s)^{-2}dx=C s^{-1/2}\).  Therefore the
   transport ledger is
   \[
     \int_0^{r^2}r^{-1}s^{-1/2}ds
       +r^3\int_{r^2}^{R^2}s^{-5/2}ds
       =2+\frac23\bigl(1-(r/R)^3\bigr),
   \]
   up to fixed viscosity constants.  This proves that the particular
   pointwise absolute-value estimate has no vanishing coefficient.  It does
   not prove sharpness or a lower bound for the leakage.

5. Under the separately stated pressure envelope (PPI), the pressure
   boundary term has the same valid absolute-value ledger: PPI contributes
   \((|x|^2+s)^{-1}\), PTI squared contributes another such factor, and the
   radial integral is again (10).  PPI is not derived from PTI, as the note
   correctly says.  Gauge bookkeeping requires choosing one function
   \(c(t)\) and replacing \(p\) by \(p-c(t)\) in **both** pieces of (13), or
   retaining the unsplit pairing.  Estimating only the displayed boundary
   piece with \(p-c\) while leaving the active term written with \(p\) would
   obscure the compensating constant contributions.  This is a notation and
   bookkeeping repair, not a new pressure estimate.

6. The outer truncation has the stated scale.  On
   \(B_{3R}\setminus B_{2R}\), heat-kernel bounds and
   \(|\nabla\zeta_R|\lesssim R^{-1}\),
   \(|\Delta\zeta_R|\lesssim R^{-2}\) yield
   \[
      |(\partial_t+\nu\Delta)(\zeta_R\eta_r)|
        \lesssim_\nu r^3R^{-5}
   \]
   for \(0<s<R^2\).  Local PTI on that annulus gives
   \(\int_{-R^2}^0\int_{B_{3R}\setminus B_{2R}}|u|^3
     \lesssim C_*^3R^2\), so the resulting error is
   \(O_\nu(C_*^3(r/R)^3)\).  Without annular velocity control this is an
   additional hypothesis; pressure localization likewise needs explicit
   outer pressure data.  The note states both limitations.

REPLACEMENT ARGUMENT: replace every conclusion of actual order-one leakage
by the following precise statement:

> The PTI/PPI absolute-value calculation yields bounds uniform in \(r/R\),
> but its comparison ledger has no factor tending to zero as \(r/R\to0\).
> Consequently these hypotheses and this bounding method alone do not prove
> the small boundary leakage needed for contraction.  The calculation gives
> neither a lower bound nor a no-cancellation theorem for the signed
> transport or pressure flux; the actual flux may still decay or cancel.

In particular, Section 5 should say that a strict estimate for the active
pressure work still leaves *available bounds too coarse to close a smallness
argument*, rather than that it leaves actual order-one errors.  Section 7
should rename “Exact surviving loss” as “Surviving limitation of the
absolute-value estimate,” replace “with no decay” by “without a proved decay
factor,” and correct the typographical `|lesssim` in (19) to `\lesssim`.

CONDITIONAL SUFFIX THAT SURVIVES: the incoming-face \((r/R)^3\) gain, the
localized identity, the uniform transport estimate, the conditional uniform
pressure-boundary estimate, and the locally truncated incoming/error gain
all survive.  Together they show that caloric spreading repairs the old
incoming-face objection while the displayed absolute estimates do not close
a contraction.

UNNECESSARY DEPENDENCIES: no pressure hypothesis is needed for the heat
kernel, incoming-face, or transport calculations.  PPI is used only for the
pressure-boundary diagnostic.  No annular pressure assertion is needed to
state the global PTI calculation.

NON-CLAIMS: the audited calculation does not prove that either signed
boundary flux is nonzero, bounded below, asymptotic to a constant, or unable
to cancel.  It does not derive PPI from PTI, derive the local outer-data
bounds from inner PTI, obtain the same mechanism from normalized enstrophy,
or prove Type-I regularity, HIGH-PRESSURE, or global regularity.

REOPENING CONDITION: a genuine obstruction would require a lower bound, a
sign argument, or a no-cancellation construction for the relevant signed
flux.  A successful contraction may instead reopen the route with a signed
cancellation estimate or a cutoff whose near-final boundary ledger contains
a proved small factor while preserving the incoming \((r/R)^3\) gain.
