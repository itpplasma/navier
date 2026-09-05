# Independent audit of the high-output boundary replacement

VERDICT: **PASS**

REVIEWED SCOPE: research/evidence/hf14-high-output-boundary.md, frozen with
SHA-256
0c9226f6dba446a9b66a0932177c6d921f9e3ed0390e06f43e7f9a56e0a4f3b9
on base commit f297efc46756f5acd229e4a8aaa5284655ec6903.

FIRST BAD BRIDGE: none.

EVIDENCE:

1. The symbol of \(S_JR_iR_j\) is
   \[
      -\chi(2^{-J}\xi){\xi_i\xi_j\over|\xi|^2}.
   \]
   It is bounded and compactly supported but remains directional at
   \(\xi=0\).  Its inverse Fourier transform is therefore bounded locally
   because the symbol is in \(L^1_\xi\), but it is not generally Schwartz.
   Convolving the principal-value degree-\(-3\) Riesz kernel with the
   Schwartz low-pass kernel preserves the leading \(O(|x|^{-3})\) tail;
   cancellation controls the near part.  Thus \(K_0\in L^q(\mathbb R^3)\)
   exactly for the range needed here, \(q>1\), with no \(L^1\) assertion.

2. Riesz homogeneity and low-pass dilation give
   \(K_J(x)=2^{3J}K_0(2^Jx)\).  Hence
   \[
      \|K_J\|_q=2^{3J(1-1/q)}\|K_0\|_q.
   \]
   Since \(\|u_i u_j\|_1\le\|u\|_2^2=E\), Young's convolution inequality
   proves (7).  At \(q=3/2\) and \(q=2\), the powers are respectively
   \(2^J\) and \(2^{3J/2}\), verifying (8).  These estimates require only
   \(u\in L^2\).

3. The high-output symbol
   \[
      -(1-\chi(2^{-J}\xi)){\xi_i\xi_j\over|\xi|^2}
   \]
   vanishes near zero and satisfies uniform scaled Mikhlin bounds.  Its
   \(L^{3/2}\) norm is therefore bounded independently of \(J\).  Riesz
   boundedness and \(u\in L^3\) give (9).

4. For \(\pi<0\), write \(q=-\pi\),
   \(s=(r^2+kq)^{1/2}\), and \(h=(kq)^{1/2}\).  Direct differentiation gives
   \[
      \partial_\pi g_k=(s-h){2s-h\over2s}
      =(s-h)\left(1-{h\over2s}\right).
   \]
   Thus \(0\le\partial_\pi g_k\le s-h\le r\).  For \(\pi>0\), the derivative
   equals \(r\).  When \(r>0\), the negative-side derivative tends to \(r\)
   as \(\pi\uparrow0\), matching the positive side.  When \(r=0\),
   \(g_k(0,\pi)=0\) for all \(\pi\), so its derivative is zero, including at
   \(\pi=0\).  The scalar map is therefore globally \(r\)-Lipschitz in
   \(\pi\), uniformly for all \(k>0\), proving (12) without an omitted
   zero-set case.

5. Since \(p-p^H=p^L\), (12), Cauchy--Schwarz, and (8) give
   \[
      \left|\int g_k(|u|,p)-g_k(|u|,p^H)\right|
      \le\|u\|_2\|p^L\|_2
      \le C2^{3J/2}E^{3/2}.
   \]
   Every exponent and the definition \(E=\|u\|_2^2\) agree with (13).

6. The scalar function \(x\mapsto x_-^{3/2}\) obeys (14) by the mean-value
   bound for the \(3/2\) power and the Lipschitz property of the negative
   part.  Hölder with exponents \(3/2\) and \(3\) gives
   \[
   \int |p^L||p^H|^{1/2}
      \le\|p^L\|_{3/2}\|p^H\|_{3/2}^{1/2},
   \]
   and the analogous \(p^L\) term is
   \(\|p^L\|_{3/2}^{3/2}\).  Substitution of (8)--(9) yields exactly
   \[
      C2^JE\|u\|_3+C2^{3J/2}E^{3/2}.
   \]

7. Young's inequality with conjugate exponents \(3\) and \(3/2\) gives, for
   every \(\delta>0\),
   \[
      C2^JE\|u\|_3
      \le\delta\|u\|_3^3
        +C_\delta(2^JE)^{3/2}.
   \]
   The second term is
   \(C_\delta2^{3J/2}E^{3/2}\), so (13)--(15) prove (16).  The constants are
   uniform in \(k\); their stated dependence on the cutoff and on
   \(\delta\) is unavoidable.

8. The static coercivity comparison is valid for an arbitrary scalar
   \(\pi\).  If \(\pi\ge0\), \(g_k(r,\pi)=\pi r\ge0\).  If \(\pi<0\), then
   \(g_k(r,\pi)\ge-\pi_-r\), and the same pointwise Young inequality gives
   (17).  No relation between \(\pi\) and \(u\) is required.  On a classical
   Navier--Stokes trajectory, the energy inequality replaces \(E(t)\) by
   \(E(0)\) only in the endpoint remainder; it does not turn the boundary
   comparison into a differentiated or spacetime estimate.

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: The full candidate survives.  At each fixed
cutoff \(J\), replacing full pressure by high-output pressure changes the
homogeneous boundary functional by at most an arbitrarily small cubic term
plus \(C_\delta2^{3J/2}E^{3/2}\), uniformly for \(k>0\).  Both boundary
functionals retain the same \(k\)-uniform static coercivity.

UNNECESSARY DEPENDENCIES: The comparison uses no Schwartz regularity, kernel
\(L^1\) bound, differentiated identity, heat calculation, or pressure-sign
mechanism.  The assumptions \(u\in L^2\cap L^3\) suffice.

NON-CLAIMS: The low-pass Riesz kernel is not claimed to be Schwartz or
integrable.  This audit proves no derivative identity, transfer of a
full-pressure heat obstruction to \(p^H\), spacetime pressure absorption, HF
estimate, or regularity conclusion.

REOPENING CONDITION: Derive the complete differentiated high-output
functional and control its multiplier commutators and nonlinear pressure
variation.  The static endpoint estimate alone cannot supply that step.
