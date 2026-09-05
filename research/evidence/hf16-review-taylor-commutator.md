# HF16 independent audit: Taylor commutator estimate

Frozen input: base commit
`0918b9ab403fcbc878ee20b62d887f6405123337`, with review input
`research/evidence/hf16-taylor-commutator.md` at SHA-256
`bd2f55d3f3921af605a85372722bab2ea154bcfd22cfebb52dcc215e83635c33`.

Primary source inspected: Michael Taylor, *Pseudodifferential Operators and
Nonlinear PDE*, Proposition 7.2 and equation (7.2), in the author-hosted PDF
linked by the candidate.

## Verdict

**VERDICT: REPAIR.**  The sourced commutator estimate, algebraic reduction,
dilation, cutoff loss, and low-band bound (8) all pass.  The final Gronwall
description needs one scope qualification: the fixed regularizers are not
shown coercive uniformly in \(\eta\).  Estimate (8) can be used as a Gronwall
coefficient only after the integrated inequalities have been passed by
functional-value convergence to the limiting coercive functional, or after a
separate suitable coercivity estimate.  This does not affect the commutator
lemma itself.

## Source and symbol applicability

Taylor's Proposition 7.2 states that, for \(1<p<\infty\) and
\(P\in OPBS^1_{1,1}\),
\[
 \|[P,f]g\|_{L^p}\le C\|f\|_{\operatorname{Lip}^1}\|g\|_{L^p},
\]
with Taylor's convention \([P,f]g=P(fg)-f(Pg)\).  This matches (T).  Using
the full inhomogeneous norm is safe and deliberately weaker even if one
tracks a smaller equivalent convention; it retains both the supremum and
gradient terms used in (5).

For the unit-scale operator,
\[
 p_{0,a}(\xi)=i\xi_a t_0(\xi).
\]
The high-pass factor makes the symbol smooth near \(\xi=0\), while at high
frequency it is a smooth angular order-zero double-Riesz symbol times
\(\xi_a\).  Thus
\(|\partial_\xi^\alpha p_{0,a}(\xi)|\lesssim_\alpha
\langle\xi\rangle^{1-|\alpha|}\).  The symbol is independent of \(x\), so
the associated classical order-one multiplier belongs to the
\(OPBS^1_{1,1}\) class required by the proposition.  No kernel parity theorem
is being substituted.

## Algebra and divergence term

Since \(T_J\) commutes with \(\partial_a\), direct expansion gives
\[
 [P_{J,a},v_a]F
 =T_J((\partial_av_a)F)+T_J(v_a\partial_aF)
   -v_aT_J\partial_aF.
\]
After summing,
\[
 [v\cdot\nabla,T_J]F
 =-\sum_a[P_{J,a},v_a]F+T_J((\operatorname{div}v)F).
\]
The sign and the divergence correction in (2) are therefore correct.  For
the application \(v=S_Lu\), the low pass preserves divergence freedom, so
(3) follows exactly.

## Dilation and cutoff dependence

The dyadic profile gives
\[
 p_{J,a}(\xi)=2^Jp_{0,a}(2^{-J}\xi).
\]
Under \(y=2^Jx\), the coefficient becomes
\(\widetilde v_a(y)=v_a(2^{-J}y)\), with
\[
 \|\widetilde v_a\|_\infty=\|v_a\|_\infty,
 \qquad
 \|\nabla\widetilde v_a\|_\infty
 =2^{-J}\|\nabla v_a\|_\infty.
\]
Taylor's unit-scale estimate, followed by restoration of the outer \(2^J\),
therefore gives
\[
 \|[P_{J,a},v_a]F\|_p
 \lesssim_p(2^J\|v_a\|_\infty+
                 \|\nabla v_a\|_\infty)\|F\|_p.
\]
The \(L^p\) dilation factors cancel on both sides.  Hence (5)--(6), including
the exact extra cutoff loss and a constant independent of \(J\), are correct.
Taylor's proposition itself is not claimed to provide this dilation
uniformity.

## Low-band application

Bernstein gives
\[
 \|S_Lu\|_\infty\lesssim2^{3L/2}\|u\|_2,
 \qquad
 \|\nabla S_Lu\|_\infty\lesssim2^{5L/2}\|u\|_2.
\]
At \(p=3/2\), \(F=u_i u_j\) obeys
\(\|F\|_{3/2}\le\|u\|_3^2\).  Pairing the commutator in \(L^{3/2}\) with
the audited uniform bound
\(\|F_{\eta,z}(u,z)\|_3\lesssim_k\|u\|_3\), and then using
\(\|u(t)\|_2\le E_0^{1/2}\), proves (8) with coefficient
\[
 C_k(2^{J+3L/2}+2^{5L/2})E_0^{1/2}.
\]
For input-selected \(J,L,k\), this is finite and independent of \(\eta\).
It is a weaker but sufficient replacement for the unsourced derivative-only
estimate; it does not prove that stronger estimate.

To use it in Gronwall, one must first integrate the coherent fixed-\(\eta\)
balance with all other terms controlled uniformly, pass endpoint and required
time-integral functional values to the unregularized functional, and use that
limiting functional's static coercivity to replace \(\|u\|_3^3\).  Nothing in
(8) alone gives \(\|u\|_3^3\lesssim\mathcal J^\eta_{k,J}\) uniformly in
\(\eta\).  This is the exact qualification needed in lines 135--138 and
151--152.

## Audit record

**REVIEWED SCOPE:** exact primary proposition; order-one symbol applicability;
commutator convention, sign, and divergence term; dyadic dilation; full
Lipschitz norm; Bernstein coefficient; and the scope of its Gronwall use.

**FIRST BAD BRIDGE:** lines 135--138 call (8) an admissible Gronwall
coefficient without stating that coercivity is available only after the
separate functional-value limiting argument, not for the fixed regularizer
automatically.

**REPLACEMENT ARGUMENT:** add that value-limit qualification.  The proof of
(8) itself needs no repair.

**CONDITIONAL SUFFIX THAT SURVIVES:** after the separate limiting coercivity
step and control of every other remainder, (8) is an input-dependent
Gronwall term.

**UNNECESSARY DEPENDENCIES:** the stronger derivative-only uniform-\(J\)
commutator estimate and the earlier unverified \(T(1)\) route are unnecessary.

**NON-CLAIMS:** no uniform coercivity of \(\mathcal J^\eta_{k,J}\), high-band
commutator bound, high-output absorption, HIGH-PRESSURE estimate,
continuation, or regularity theorem is established.

**REOPENING CONDITION:** none for (8); its Gronwall use requires the separate
value-limit and limiting-coercivity argument stated above.
