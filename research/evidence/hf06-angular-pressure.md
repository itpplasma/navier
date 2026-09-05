# HF06: angular null structure of the pressure symbol

Status: static Fourier-symbol and dyadic-shell test for the unforced
Navier--Stokes pressure on \(\mathbb R^3\).  The calculation identifies a
genuine near-parallel null factor and the weaker output-derivative gain in
high-high-to-low interactions.  The resulting shell sum is not controlled by
energy or cubic dissipation, so no high-pressure estimate is proved.

## 1. Exact cross symbol and conventions

Take two complex solenoidal modes

\[
 u_k(x)=a e^{ik\cdot x},\qquad u_l(x)=b e^{il\cdot x},
 \qquad k\cdot a=0,\quad l\cdot b=0,                \tag{1}
\]

and set \(q=k+l\ne0\).  Pressure is normalized by

\[
 \widehat p(q)=-{q_iq_j\over|q|^2}\widehat{u_i u_j}(q).             \tag{2}
\]

At output \(q\), the two ordered products \((k,l)\) and \((l,k)\) contribute
\(a_i b_j+b_i a_j\).  Therefore the cross-pressure coefficient is

\[
\boxed{
 p_{k,l}(q)=-2{(q\cdot a)(q\cdot b)\over|q|^2}
 =-2{(l\cdot a)(k\cdot b)\over|q|^2}.}                \tag{3}
\]

If one defines an unordered bilinear form with a prefactor \(1/2\), the
factor two is absent.  Formula (3) uses the actual ordered-pair contribution
to \(u_i u_j\).

For real velocity fields, \(\widehat u(-k)=\overline{\widehat u(k)}\).
Consequently every sum interaction has its conjugate, and difference outputs
are obtained from (3) by replacing \((l,b)\) with
\((-l,\overline b)\).  The real pressure is recovered after adding conjugate
outputs.  No complex mode by itself is being asserted to be a real flow.

## 2. Exact null cases

Equation (3) vanishes in each of the following cases:

* \(l\cdot a=0\) or \(k\cdot b=0\);
* \(k\) and \(l\) are parallel, because each polarization is then
  perpendicular to both wavevectors;
* a single plane wave interacting with itself.

For \(q=0\), pressure is defined only modulo its zero mode and
\(\nabla p(0)=0\).  The formula with \(|q|^{-2}\) is not used there.  Exact
antiparallel modes therefore create no pressure gradient at zero output.

These are algebraic null cases for pressure.  They do not imply that the
quartic pressure work vanishes, because its other factor \(|u|u\) contains
additional mode interactions and must match the pressure output.

## 3. Comparable inputs: parallel and antiparallel regimes

Assume \(|k|\simeq|l|\simeq K\), and let \(\alpha\in[0,\pi]\) be the angle
between \(k\) and \(l\).  Solenoidality gives

\[
 |l\cdot a|\leq |l|\sin\alpha\,|a|,\qquad
 |k\cdot b|\leq |k|\sin\alpha,|b|.                  \tag{4}
\]

Hence

\[
 |p_{k,l}(q)|
 \leq C{K^2\sin^2\alpha\over|q|^2}|a||b|.            \tag{5}
\]

If the inputs are near parallel, \(\alpha\ll1\), then \(|q|\simeq K\), and

\[
 |p_{k,l}(q)|\leq C\sin^2\alpha\,|a||b|.            \tag{6}
\]

This is a genuine quadratic angular null factor.

High-high-to-low output is the opposite geometry.  Write
\(\beta=\pi-\alpha\ll1\).  Then

\[
 |q|^2=(|k|-|l|)^2+2|k||l|(1-\cos\beta)
 \simeq (|k|-|l|)^2+K^2\beta^2.                      \tag{7}
\]

The numerator in (5) is \(O(K^2\beta^2)\), which can be the same size as
\(|q|^2\).  Thus

\[
 |p_{k,l}(q)|\leq C|a||b|                             \tag{8}
\]

but no factor tending to zero with \(\beta\) survives uniformly.  The angle
gain is cancelled by the inverse Laplacian when nearly antiparallel waves
have comparable radial frequency.  Requiring \(|q|>2^J\) for a fixed cutoff
does not repair this: one can have \(2^J\ll|q|\ll K\).

## 4. The output derivative yields a low-output bound

Pressure work is better written with its derivative:

\[
 H_J=-\langle\nabla p,Q_J(|u|u)\rangle,
 \qquad Q_J=P_{>J}.                                   \tag{9}
\]

Multiplying (3) by \(|q|\) and using directly
\(q\cdot a=l\cdot a\), \(q\cdot b=k\cdot b\) gives

\[
 |\widehat{\nabla p}_{k,l}(q)|
 =2{|q\cdot a||q\cdot b|\over|q|}.                   \tag{10}
\]

In the near-antiparallel comparable-frequency regime, (7) implies

\[
 |q\cdot a||q\cdot b|
 \leq C K^2\beta^2|a||b|
 \leq C|q|^2|a||b|,
\]

and therefore

\[
\boxed{
 |\widehat{\nabla p}_{k,l}(q)|
 \leq C|q|\,|a||b|.}                               \tag{11}
\]

Thus the output derivative restores a factor \(|q|/K\) relative to a generic
one-input-derivative bound of size \(K|a||b|\). This calculation alone
establishes an upper bound, not a lower bound or exclusion of further
polarization cancellation. It uses the output derivative visible in

\[
 \nabla p=\nabla(-\Delta)^{-1}\partial_i\partial_j(u_i u_j).       \tag{12}
\]

For arbitrary, not necessarily comparable inputs, the identity of the last
formula gives the robust dyadic estimate

\[
 \|\Delta_j\nabla p\|_s
 \leq C2^j\|\widetilde\Delta_j(u\otimes u)\|_s,
 \qquad 1<s<\infty,                                  \tag{12}
\]

where the tilde is a fixed enlargement in output frequency.  Equation (11)
is the high-high-to-low symbol explanation for the factor \(2^j\).

## 5. Sector and shell ledger

Let \(u_k=\Delta_k u\).  When \(j\leq k-C_0\), an output at scale \(2^j\)
from two inputs at scale \(2^k\) forces them into antipodal angular sectors of
aperture

\[
 \beta\lesssim2^{j-k}                                \tag{13}
\]

and into radial frequencies differing by \(O(2^j)\).  On each such sector
pair, (11) gives output symbol size \(O(2^j)\), rather than \(O(2^k)\).
Equivalently, relative to an input-derivative estimate the algebraic gain is
\(2^{j-k}\).

This gain survives at the operator level as

\[
 \|\Delta_j\nabla p(u_k,u_{k'})\|_s
 \leq C2^j\|u_k u_{k'}\|_s,
 \qquad |k-k'|\leq C,\quad k\geq j+C_0.             \tag{14}
\]

For \(s=1\), (14) remains valid because the output is localized to one
annulus: its smooth band-limited multiplier has an \(L^1\) convolution kernel
of norm \(O(2^j)\).  This endpoint statement is not unlocalized Riesz
\(L^1\)-boundedness.

Pairing with the matching output of \(w=|u|u\), one obtains the
absolute shell upper bound

\[
 |H_J^{\rm hh\to low}|
 \leq C\sum_{j>J}\sum_{\substack{k\geq j+C_0\\|k-k'|\leq C}}
 2^j\|u_k u_{k'}\|_s\|\widetilde\Delta_jw\|_{s'},
 \qquad {1\over s}+{1\over s'}=1.                    \tag{15}
\]

Two representative exponent choices show the remaining obstruction.

With \(s=1,s'=\infty\), understood using the band-limited kernel rather than
strong \(L^1\) boundedness of Riesz transforms,

\[
 |H_J^{\rm hh\to low}|
 \leq C\sum_{j>J}2^j
 \left(\sum_{k\geq j+C_0}\|u_k\|_2^2\right)
 \|\widetilde\Delta_jw\|_\infty.                    \tag{16}
\]

Energy bounds the parenthesized tail by \(\|u\|_2^2\), but leaves

\[
 \sum_{j>J}2^j\|\widetilde\Delta_j(|u|u)\|_\infty,   \tag{17}
\]

an \(\ell^1\) Besov-type norm with no energy or \(D_3\) control.

With \(s=3/2,s'=3\),

\[
 |H_J^{\rm hh\to low}|
 \leq C\sum_{j>J}\sum_{k\geq j+C_0}
 2^j\|u_k\|_3\|u_{k'}\|_3
 \|\widetilde\Delta_jw\|_3.                         \tag{18}
\]

This keeps critical Lebesgue exponents but requires critical shell control of
the inputs and an \(\ell^1\) summation.  Those are not supplied by kinetic
energy.  Taking absolute values has discarded any possible signed cancellation
between antipodal sector pairs.

The angular sector measure does not give a deterministic improvement for
arbitrary data.  Fourier energy may concentrate in one antipodal cap of
aperture \(2^{j-k}\), so a counting factor proportional to the cap area cannot
be inserted without an angular equidistribution hypothesis.  Such a hypothesis
would be new trajectory information, not a consequence of incompressibility.

## 6. Relation to cubic dissipation

The derivative of \(w=|u|u\) satisfies

\[
 |\nabla w|\leq2|u||\nabla u|,
\]

and Hölder gives the energy-compatible bound

\[
 \|\nabla w\|_{3/2}
 \leq2\||u|^{1/2}\|_6
       \||u|^{1/2}\nabla u\|_2
 \leq C\|u\|_3^{1/2}D_3^{1/2}.                       \tag{19}
\]

This controls one aggregate Sobolev norm of \(w\), conditional on the unknown
critical \(L^3\) norm.  It does not control the \(B^1_{\infty,1}\)-type sum
(17), nor does it close (18).  Moreover, inserting \(\|u\|_3\) as an assumed
uniform bound would use the continuation quantity the HF route is meant to
produce.

One might try to shift the output derivative in (15) onto \(w\) and use
(19).  The pressure factor then has only an order-zero bound, while summing
the shell pairings still requires compatible square-function or \(\ell^1\)
control of the high-high input products.  The weighted integral \(D_3\) gives
no such frequency-by-frequency distribution.  Thus the derivative gain does
not by itself yield a strict fraction of \(\nu D_3\).

## 7. Scaling, sign, and exact obstruction

Under Navier--Stokes scaling, the input frequency \(K\) and output frequency
\(|q|\) scale together; the ratio \(|q|/K\) and all angular factors are
invariant.  Both \(H_J\) and \(D_3\) scale like \(\lambda^2\) at a fixed
time when the cutoff is shifted with \(\lambda\).  The symbol gain is critical,
not subcritical.

The coefficient (3) has no fixed sign: changing one polarization changes its
sign while retaining the divergence-free constraints.  Reality couples the
corresponding conjugate terms but does not make each quartic pressure-work
interaction nonpositive.  The compactly supported real profiles in
`hf02-r3-profile.md` independently show that full pressure work takes both
signs.

The periodic shear in `hf05-radial-dynamics.md` has zero convection and zero
leading pressure for all time.  Its viscosity-generated radial variation is
therefore an oracle for radial/angular transfer, not evidence of dangerous
pressure flux.  The two mechanisms must not be conflated.

**Actual result:** comparable near-parallel inputs have a quadratic angular
null factor.  Comparable near-antiparallel inputs can cancel that factor in
the pressure symbol, while the bound for \(\nabla p\) retains the lower output
frequency \(|q|\).  Equations (14)--(18) give the resulting sector/shell
estimate with explicit exponents.

**First failed bridge:** summing the output-derivative gain against
\(Q_J(|u|u)\) requires an uncontrolled Besov or critical-shell norm.  Energy
allows concentration in one antipodal sector and supplies no angular counting
gain.  Cubic dissipation controls neither required shell sum without also
assuming the unknown \(L^3\) bound.

**Non-claims:** null structure alone does not prove HF, a signed spacetime estimate,
or regularity.  No angular equidistribution or critical norm is introduced as
a theorem hypothesis, and no novelty claim is made.
