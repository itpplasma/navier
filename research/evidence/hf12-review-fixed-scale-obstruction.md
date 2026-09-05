# HF12 independent audit: fixed-scale heat obstruction

Frozen input: base commit
`dd0473219e058bd98f733696434724b22c0a634d`, with review input
`research/evidence/hf12-fixed-scale-obstruction.md` at SHA-256
`22a502486309f70f2a12b143af5474cae73151e7ab6cacefdab7ce43b34eec9a`.

## Verdict

**VERDICT: PASS.**  For each fixed \(\tau>0\), the candidate constructs a
smooth compactly supported solenoidal field whose \(\mathcal J_\tau\) value
strictly increases under a finite linear heat step.  The carrier, packet
amplitude, and frequency are selected in the valid order \(M\), then \(b\),
then \(N\).  All constants needed before the last step are uniform in \(N\),
and the pressure entropy and nonlocal packet-pressure source are retained.

## Dependency-order audit

The azimuthal carrier is smooth because its cylindrical support avoids the
axis.  Its velocity is orthogonal to the radius vector, so contraction with
the off-support kernel
\((3y_i y_j-|y|^2\delta_{ij})/(4\pi|y|^5)\) gives (3) with the stated
negative sign.  Separation then supplies the ball (4).  The packet is a curl,
has the same fixed compact support for every \(N\), and has uniformly bounded
\(L^q\) norms, including \(q=\infty\).  Support separation kills the pressure
cross term pointwise, proving (8) exactly.

For fixed \(\tau\), Taylor's formula for \(\rho_\tau\) is uniform on the packet
range after \(b\) is chosen below a fixed multiple of \(\tau\).  It gives the
leading term
\[
 -{\alpha^2b^2M^2\over2\tau}A_N,
 \qquad A_N\to {1\over2}\int_B(-p_U)\chi^2>0,
\]
with remainder \(O(M^2b^4/\tau^3)\).  Periodic averaging is unaffected by
the \(N^{-1}\) envelope-derivative term in \(w_N\), whose contribution tends
to zero uniformly in the required integral norms.

The remaining terms in (13) have the asserted carrier dependence.  Riesz
boundedness gives \(\sup_N\|p_{w_N}\|_{3/2}<\infty\).  On the carrier support,
\[
 b^2\left|\int p_{w_N}\rho_\tau(M|U|)\right|
 \le C Mb^2;
\]
on the packet support, the packet-pressure self-coupling is \(O(b^4/\tau)\),
and the cubic packet is \(O(b^3)\).  Everywhere else the velocity-dependent
terms vanish.  For the pressure entropy, (16) and Holder give
\[
 \left|\int[(M^2p_U+\alpha^2b^2p_{w_N})_-^{3/2}
                 -(M^2p_U)_-^{3/2}]\right|
 \le C(Mb^2+b^3).
\]
Thus the entropy is not dropped, and no omitted term has order \(M^2b^2\).
These estimates are uniform in \(N\) and \(\alpha\in[0,1]\), establishing
(12)--(13).

At time \(t_N=\sigma/N^2\), Fourier demodulation of the leading packet
oscillation gives convergence to \(e^{-\sigma}w_N\) in every finite
\(L^q\), while the envelope-derivative terms vanish.  Heat continuity gives
\(e^{t_N\Delta}MU-MU\to0\) in \(L^3\) after \(M\) is fixed.  Hence (21)
holds.  The three parts of \(\mathcal J_\tau\) are locally Lipschitz on
\(L^3\): the pressure map obeys (22), \(\rho_\tau\) is one-Lipschitz with
\(0\le\rho_\tau(r)\le r\), and (16) controls the entropy.  Since the two
sequences in (21) lie in a common bounded \(L^3\) set for fixed \(M,b\),
(23) follows with no derivative estimate on the heat-evolved packet.

Finally, once \(A_N\ge A/2\), the leading lower bound in (24) is a positive
constant times \(M^2b^2/\tau\).  Choose \(M\) first so the \(Mb^2\) error is
a prescribed small fraction of it.  With that \(M\) fixed, choose \(b\) small
enough both for the Taylor range and so the \(b^3\), \(b^4/\tau\), and
\(M^2b^4/\tau^3\) errors consume another prescribed fraction.  Then choose
\(N\) so \(A_N\ge A/2\) and the endpoint error (23) is smaller than the
remaining positive margin.  This proves strict positivity in (25).

## Audit record

**REVIEWED SCOPE:** fixed \(\tau>0\); remote-pressure sign; exact disjoint
pressure decomposition; uniform \(M,b,N,\alpha\) expansion; retained pressure
entropy and packet-pressure source; packet heat limit; local \(L^3\)
continuity; and parameter quantifiers.

**FIRST BAD BRIDGE:** none.

**REPLACEMENT ARGUMENT:** none.

**CONDITIONAL SUFFIX THAT SURVIVES:** the complete fixed-scale heat-semigroup
obstruction (2).

**UNNECESSARY DEPENDENCIES:** no differentiated heat identity, velocity
zero-set derivative, or numerical sign computation is needed.

**NON-CLAIMS:** the result does not address a state-dependent scale, the Euler
part of Navier--Stokes, a full Navier--Stokes trajectory, HIGH-PRESSURE,
continuation, blowup, or global regularity.

**REOPENING CONDITION:** none within the reviewed scope.
