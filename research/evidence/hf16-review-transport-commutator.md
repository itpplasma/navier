# HF16 independent audit: transport commutator

Frozen input: base commit
`0918b9ab403fcbc878ee20b62d887f6405123337`, with review input
`research/evidence/hf16-transport-commutator.md` at SHA-256
`8c711d38904b0f35d957070de5ffaea82249b6f2406da2976af174d7493eca08`.

## Verdict

**VERDICT: PASS, CONDITIONAL ON THE STATED EXTERNAL \(T(1)\) PREMISE.**  The
actual commutator has uniform Calderon--Zygmund kernel constants, zero testing
functions, and the weak boundedness property with norm
\(O(\|\nabla v\|_\infty)\), independently of \(J\).  The quoted quantitative
\(T(1)\) theorem and subsequent Calderon--Zygmund \(L^p\) theorem have not been
primary-source verified in this packet.  Accordingly (2) remains a
conditional imported conclusion, exactly as the candidate states.

## Kernel and possible local part

Write the high-output kernel as the homogeneous double-Riesz kernel minus its
scaled low-frequency correction.  Away from zero, scaling and the decay of
the fixed profile give
\[
 |\nabla K_J(x)|\lesssim |x|^{-4},\qquad
 |\nabla^2K_J(x)|\lesssim |x|^{-5}
\]
with constants independent of \(J\).  For disjoint supports, integration by
parts in the second commutator term, using \(\operatorname{div}v=0\), gives
\[
 K_C(x,y)=(v(x)-v(y))\cdot\nabla K_J(x-y).
\]
The Lipschitz bound for \(v\) gives the size \(|x-y|^{-3}\).  Differencing in
either variable uses one term with \(\nabla v\,\nabla K_J\) and one with
\((v(x)-v(y))\nabla^2K_J\), giving the standard \(|x-y|^{-4}\) smoothness
bound with the same uniform constant.

The distribution kernel of a double Riesz transform can depend on its
principal-value normalization by a diagonal multiple of the identity.  Such
a constant local operator commutes with \(v\cdot\nabla\), so it contributes
nothing to this commutator.  More generally, the proof applies the testing and
weak boundedness checks to the actual multiplier operator, rather than trying
to recover it solely from its off-diagonal kernel.  Thus no local term is
silently omitted.

## Cancellation

The multiplier of \(T_J=Q_JR_iR_j\) is smooth at frequency zero because
\(Q_J\) vanishes in a neighborhood of zero, and its value there is zero.
Therefore, exactly in \(\mathcal S'\),
\[
 T_J1=0,qquad C_{v,J}1
 =v\cdot\nabla(T_J1)-T_J(v\cdot\nabla1)=0.              \tag{R1}
\]
This avoids relying on a merely formal boundary limit.  It is also uniform in
\(J\): the testing distribution is identically zero for every cutoff, rather
than tending to zero with a cutoff-dependent estimate.

On test functions, \(T_J\) is self-adjoint because its multiplier is real and
even, while \(v\cdot\nabla\) is skew-adjoint because
\(\operatorname{div}v=0\).  Hence
\([v\cdot\nabla,T_J]^*=[v\cdot\nabla,T_J]\), and the same distributional
argument gives \(C_{v,J}^*1=0\).  Both BMO testing norms are therefore exactly
zero.  For the application \(v=S_Lu\), band limitation and \(u\in H^m\)
supply all smoothness and boundedness needed for these distributional
operations; no unproved uniform cutoff-at-infinity passage is required.

## Weak boundedness

For bumps supported in \(B(x_0,r)\), a constant vector field commutes with
the translation-invariant multiplier.  After subtracting \(v(x_0)\), the two
commutator terms can be paired as in (8).  The uniform \(L^2\) multiplier norm
of \(T_J\), the bounds
\[
 \|\phi\|_2+\|\psi\|_2\lesssim r^{3/2},
\]
and
\[
 \|(v-v(x_0))\nabla\phi\|_2
 +\|(v-v(x_0))\nabla\psi\|_2
 \lesssim\|\nabla v\|_\infty r^{3/2}
\]
give
\[
 |\langle C_{v,J}\phi,\psi\rangle|
 \lesssim\|\nabla v\|_\infty r^3.
\]
This has the correct three-dimensional weak-boundedness scaling and is
uniform in \(J\).  Only first bump derivatives are used, so it also applies
when the imported theorem states the usual stronger normalized-bump class.

## External premise and application

The kernel estimates, exact zero testing distributions, and weak boundedness
verify all operator-specific hypotheses listed in lines 117--122.  If the
quoted quantitative \(T(1)\) theorem gives the asserted \(L^2\) bound from
those constants, and the quoted Calderon--Zygmund consequence gives the
controlled \(L^p\) extension, then (2) follows with a constant independent of
\(J\).

For \(v=S_Lu\), the low-pass multiplier preserves divergence freedom and
Bernstein gives
\[
 \|\nabla v\|_\infty\lesssim2^{5L/2}\|u\|_2.
\]
Compact Fourier support and \(u\in H^m\), \(m\ge4\), provide the required
smooth bounded coefficient.  Taking \(p=3/2\) then gives the claimed
conditional project estimate.

## Audit record

**REVIEWED SCOPE:** uniform off-diagonal kernel and difference estimates;
diagonal/local normalization; \(T1\) and \(T^*1\) as distributions; weak
boundedness; application to \(S_Lu\); and dependence on \(J\).

**FIRST BAD BRIDGE:** none in the operator-specific reduction.  The first
unverified input for (2) is the external theorem quoted in lines 117--122.

**REPLACEMENT ARGUMENT:** none.  Primary-source verification must confirm the
exact quantitative \(T(1)\) formulation, its bump-testing convention, and the
controlled \(L^p\) consequence.

**CONDITIONAL SUFFIX THAT SURVIVES:** source verification of that theorem
makes (2), and hence the \(p=3/2\) low-band commutator estimate, unconditional.

**UNNECESSARY DEPENDENCIES:** no parity condition on \(\nabla K_J\), no
homogeneous even-kernel theorem, and no cutoff-at-infinity limit are needed
for the operator-specific checks.

**NON-CLAIMS:** this audit does not source-verify the imported theorem, control
the high-band advecting commutator or other high-output terms, prove pressure
absorption, HIGH-PRESSURE, continuation, or regularity.

**REOPENING CONDITION:** verify the exact imported statements in a primary
source with constants depending only on the displayed kernel, testing, and
weak-boundedness data.
