# Independent audit of the low-pressure-gradient bounds

VERDICT: **REPAIR**

REVIEWED SCOPE: research/evidence/hf15-low-pressure-gradient.md, frozen with
SHA-256
fd394bc2c3dcde1f615e99b81a3819edd4107ee04d50d9e023dbc3b9ea420986
on base commit c63ce81317344445359b28f034a212d42a6ae812.

FIRST BAD BRIDGE: The setup says that only \(u\in L^2\cap L^3\) is assumed,
but (11)--(15) use \(\nabla u\in L^2\) through Gagliardo--Nirenberg and need
\(z\in L^2\).  Also, at \(r=0,z>0\), the scalar radial derivative
\(\partial_rg_k=p\) does not define a vector derivative of
\(u\mapsto g_k(|u|,z)\).  A bounded chosen representative makes
\(T_1\) estimable, but it is not an actual unregularized first variation
there.  The final scope paragraph recognizes the Frechet issue but should
state these qualifications where the forms are introduced.

EVIDENCE:

1. Away from the cusps, if \(z>0\), then
   \(b_ku=(z/r)u\), whose magnitude is \(z\).  If \(z<0\), with
   \(s=(r^2+kz_-)^{1/2}\), then \(b_ku=(z/s)u\), whose magnitude is
   \(z_-r/s\le z_-\).  Thus a representative defined, for example, to be
   zero at \(u=0\) obeys
   \[
      |b_ku|\le|z|
   \]
   uniformly in \(k\).  Equality with \(|\partial_rg_k|\) is valid away
   from the velocity cusp, not at \(r=0,z>0\).

2. For \(z<0\),
   \[
      0\le\partial_zg_k=(s-h){2s-h\over2s}\le s-h\le r,
      \qquad h=\sqrt{kz_-}.
   \]
   For \(z>0\), \(\partial_zg_k=r\).  Adding the entropy derivative gives
   \[
      |a_k|\le r+\frac32\sqrt{z_-}.
   \]
   Since the high-output double Riesz multiplier is uniformly bounded on
   \(L^{3/2}\),
   \[
   \|\sqrt{z_-}\|_3=\|z_-\|_{3/2}^{1/2}
   \le C\|u\otimes u\|_{3/2}^{1/2}
   \le C\|u\|_3.
   \]
   This proves (5), uniformly in both \(k\) and \(J\), including the bounded
   scalar zero-set extensions.

3. The multiplier of \(\nabla S_JR_iR_j\) has one derivative more than the
   low double-Riesz multiplier.  Its kernel is bounded locally and has the
   actual \(O(|x|^{-4})\) far-field tail.  Dilation gives
   \[
      L_J(x)=2^{4J}L_0(2^Jx),\qquad
      \|L_J\|_q=2^{J(4-3/q)}\|L_0\|_q.
   \]
   The tail is in both \(L^2\) and \(L^6\).  Since
   \(\|u_i u_j\|_1\le E\), Young's inequality yields
   \[
      \|\nabla p^L\|_2\le C2^{5J/2}E,\qquad
      \|\nabla p^L\|_6\le C2^{7J/2}E,
   \]
   verifying every cutoff exponent in (10).  No Schwartz hypothesis or
   \(L^1\) bound for the undifferentiated kernel is used.

4. Under the repaired instantaneous assumption \(u\in H^1\), the
   high-output multiplier is bounded on \(L^2\), and
   \[
   \|z\|_2\le C\|u\otimes u\|_2
      \le C\|u\|_4^2
      \le C E^{1/4}Y^{3/4}.
   \]
   Combining this with the \(L^2\) kernel bound proves
   \[
      |T_1|\le C2^{5J/2}E^{5/4}Y^{3/4}.
   \]
   The powers of \(E\) and \(Y\) in (12)--(13) are correct.

5. For \(T_2\), Hölder exponents are exact:
   \(a_k\in L^3\), \(u\in L^2\), and \(\nabla p^L\in L^6\) give
   \(u\nabla p^L\in L^{3/2}\).  The high-output double Riesz transform is
   bounded on \(L^{3/2}\), so
   \[
   |T_2|\le C\|u\|_3\|u\|_2\|\nabla p^L\|_6.
   \]
   The three-dimensional interpolation
   \(\|u\|_3\le C\|u\|_2^{1/2}\|\nabla u\|_2^{1/2}\)
   then gives
   \[
      |T_2|\le C2^{7J/2}E^{7/4}Y^{1/4}.
   \]
   This verifies (14)--(15), uniformly in \(k\).

6. On an actual classical solution, \(E(t)\le E_0\) and
   \(\int_0^\tau Y\le E_0/(2\nu)\).  Hölder in time gives
   \[
   \int_0^\tau Y^{3/4}
     \le H^{1/4}\left({E_0\over2\nu}\right)^{3/4},
   \qquad
   \int_0^\tau Y^{1/4}
     \le H^{3/4}\left({E_0\over2\nu}\right)^{1/4}.
   \]
   Multiplication by the respective energy powers
   \(E_0^{5/4}\) and \(E_0^{7/4}\) produces \(E_0^2\) in both cases.
   This proves (17)--(18), with the stated powers of \(H,\nu,2^J\), uniformly
   for all \(0<\tau<\min(H,T_*)\) and all \(k>0\).

7. The signs in the decomposition are correct.  Since
   \(V=W-\nabla p^L\), the velocity variation contributes
   \(-\int b_ku\cdot\nabla p^L=-T_1\).  Substitution into
   \[
      (p^H)_V=2(I-S_J)R_iR_j(u_iV_j)
   \]
   contributes
   \(-2\int a_k(I-S_J)R_iR_j(u_i\partial_jp^L)=-T_2\).
   Moreover,
   \[
      0=\nabla\cdot V=\nabla\cdot W-\Delta p^L,
      \qquad\text{so}\qquad\nabla\cdot W=\Delta p^L.
   \]
   Thus \(W\) is generally not solenoidal, and no Leray or
   divergence-free transport cancellation can be imported.

REPLACEMENT ARGUMENT: Retain the \(L^2\cap L^3\) assumption for the scalar
and kernel bounds (3)--(10), but add \(u\in H^1\) before (11)--(15).  In the
application, the declared classical regularity supplies this hypothesis.
Define the displayed \(b_ku\) representative to be zero at \(u=0\) solely
for estimating \(T_1\), and replace equality in (3) by
\[
   |b_k(r,z)u|\le|z|
\]
at the cusp-inclusive level.  State that its identification with a
functional derivative is only formal until a fixed positive speed
regularizer, say \(r_\eta=(|u|^2+\eta^2)^{1/2}\), is introduced and every
extra \(\eta\)-term is retained.  For each fixed \(\eta>0\), the analogous
pieces are classical; passing \(\eta\downarrow0\) remains a separate
domination problem.  With these changes, Evidence 3--7 proves all numerical
bounds and algebraic signs exactly.

CONDITIONAL SUFFIX THAT SURVIVES: The energy-only finite-horizon estimates
(17)--(18) survive unchanged for the two explicitly defined low-gradient
forms on a classical trajectory, uniformly in \(k\).  They may be inserted
into a rigorously regularized decomposition once that decomposition and its
limit are proved.

UNNECESSARY DEPENDENCIES: The kernel estimates need only \(u\in L^2\); the
scalar \(a_k\) estimate needs \(u\in L^3\); \(H^1\) enters only in the
instantaneous interpolation and subsequent energy-time bounds.

NON-CLAIMS: The bounded representatives do not create an unregularized
Frechet derivative.  This audit supplies no estimate for the remaining
high-output sum, no \(\eta\downarrow0\) limit, no pressure absorption, no HF
estimate, and no regularity conclusion.

REOPENING CONDITION: Control the complete regularized high-output
Euler and heat expression, including the nonzero divergence of \(W\), and
justify any removal of the speed regularizer by explicit domination.
