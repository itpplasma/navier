# HF13: heat monotonicity fails for every homogeneous coupling parameter

MODE / RESULT: FALSIFY. For every k > 0, the homogeneous functional
\(\mathcal J_k\) defined in `hf12-homogeneous-coupling.md` increases on
some finite linear heat step starting from a smooth compactly supported
solenoidal field on R3. The initial field may depend on k.

This integrates two independently audited inputs frozen at `59ccce3`:
`hf13-entropy-far-field.md` and `hf13-conditional-packet.md`. Their reviews
are `hf13-review-entropy-far-field.md` and
`hf13-review-conditional-packet.md`. The former also audits the uniform-k
comparison used below.

## Supplying the packet premise

Choose the compact azimuthal background U from the far-field theorem. Put
\[
 e_U=-\tfrac32\sqrt{(p_U)_-},\qquad
 m_k=\partial_p g_k(|U|,p_U),\qquad a_k=m_k+e_U.
\]
The reviewed scalar derivative gives
\[
 0\le m_k\le |U|,\qquad
 \operatorname{supp}m_k\subseteq\operatorname{supp}U,
 \qquad \|m_k\|_1\le\|U\|_1
\]
uniformly in k. In particular, on the polar axis far from that support,
\[
 |R_3R_3m_k(Re_3)|\le C_U R^{-3}
\]
uniformly in k. The exact entropy asymptotic, including its analytic angular
sign certificate, gives
\[
 R_3R_3 e_U(Re_3)=-c_U R^{-3/2}+o(R^{-3/2}),\qquad c_U>0.
\]
Choose R large enough that the entropy term dominates the compact-source
bound. Local continuity of the entropy projection, the uniform compact-source
bound on a neighborhood, and the negative polar pressure tail give a ball B
and constants c, eta > 0, independent of k, with
\[
 U=0,\qquad p_U\le-c,\qquad R_3R_3a_k\le-\eta
 \quad\text{on B, for every }k>0.
\]
These are precisely the premises of the reviewed packet lemma, with
polarization e3 and an orthogonal oscillation direction.

## Conclusion and quantifiers

Fix k > 0. The packet lemma first chooses its small amplitude and then its
large frequency, retaining every pressure variation and entropy term. It
produces a compact smooth solenoidal field h_k and s_k > 0 such that
\[
 \mathcal J_k(e^{s_k\Delta}h_k)>\mathcal J_k(h_k).
\]
Equivalently, for every viscosity nu > 0 use the time s_k/nu. Thus
\[
 \forall k>0\;\exists h_k\;\forall\nu>0\;\exists t_{k,\nu}>0:
 \mathcal J_k(e^{\nu t_{k,\nu}\Delta}h_k)>\mathcal J_k(h_k).
\]
One common background ball works for all parameters. A common perturbation
amplitude, frequency, initial field, or heat time is not asserted.

SURVIVING CONDITIONAL SUFFIX: The uniform cubic coercivity and reviewed
Euler formulas remain valid. What fails throughout this parameter family is
universal heat monotonicity.

NON-CLAIMS: This is not a Navier--Stokes trajectory counterexample, an
obstruction to an input-controlled positive heat remainder, a failure of
HIGH-PRESSURE, or a statement about blow-up. In particular, the far-field
mechanism uses the full pressure tail; it is not a theorem about the fixed
high-output pressure after removing low frequencies.

NEXT DISTINCT ACTION: Return to the fixed high-output pressure split and
determine which parts of this correction differ only by energy-controlled
boundary terms. Test a proposed high-output identity on its complete
remainder rather than imposing heat monotonicity on the full pressure.
