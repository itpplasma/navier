# Independent audit of the HF02 compact R3 profile

**VERDICT: PASS.**

## Reviewed scope

The immutable packet is repository base
169ec50daa9295e0a713236bf969c2f42a507f51 plus the complete new file
research/evidence/hf02-r3-profile.md, whose verified SHA-256 is
36c5df116820c57686c01d1494f7bfa1f3f8b994ae31b5ce4e52083f6e213bbd.
The claim reviewed is exactly the existence of
\(u\in C_c^\infty(\mathbb R^3;\mathbb R^3)\), \(\nabla\cdot u=0\), with
\[
 P_3[u]=\int_{\mathbb R^3}p[u]\,u\cdot\nabla|u|\,dx>0,
 \qquad p[u]=R_iR_j(u_i u_j).
\]
No spacetime estimate, trajectory realization, or blow-up conclusion is in
scope.

## Dependency-order reconstruction

### Periodic coefficient: PASS

For
\[
 \psi=\sin X+\sin Y-\cos(X+Y),\qquad
 v=(\psi_Y,-\psi_X,0),
\]
one has \(v_1=\cos Y+\sin(X+Y)\) and
\(\partial_Xv_1=\cos(X+Y)\). Direct differentiation gives
\[
 \partial_i\partial_j(v_iv_j)
 =-2\det D^2\psi
 =-2\sin X\sin Y+2\cos(X+Y)(\sin X+\sin Y).
\]
The last two summands contain no \(\cos(X+Y)\) Fourier component. Since
\[
 -2\sin X\sin Y=\cos(X+Y)-\cos(X-Y),
\]
the right side of \(-\Delta p_v=\partial_i\partial_j(v_iv_j)\) has
\(\cos(X+Y)\) coefficient \(1\), and \(p_v\) has coefficient \(1/2\).
Therefore
\[
 \langle p_v\partial_Xv_1\rangle
 ={1\over2}\langle\cos^2(X+Y)\rangle={1\over4}.
\]
The sign and normalization are correct.

For \(e_1+\varepsilon v\), the constant tensor has zero double divergence,
and the cross tensor has double divergence
\(2\partial_1\operatorname{div}v=0\). Hence its pressure is
\(\varepsilon^2p_v\). Taylor expansion at the nonzero vector \(e_1\) gives
\[
 (e_1+\varepsilon v)\cdot\nabla|e_1+\varepsilon v|
 =\varepsilon\partial_Xv_1+O(\varepsilon^2),
\]
uniformly on the torus, so the periodic pressure work has leading coefficient
\(\varepsilon^3/4>0\).

### Compact solenoidal embedding: PASS

The field
\[
 B=\nabla\times(0,0,\chi y)
\]
is smooth, compactly supported, and divergence free. Where \(\chi=1\),
\(B=e_1\). Choosing \(\chi=1\) on a neighborhood of \(\operatorname{supp}a\)
therefore places the entire support of
\[
 V_n=\nabla\times(0,0,n^{-1}a\psi(nx,ny))
\]
inside a constant plateau of \(B\). Direct differentiation gives
\[
 V_n=a\,v(nx,ny)+n^{-1}
 ((\partial_ya)\psi(nx,ny),-(\partial_xa)\psi(nx,ny),0).
\]
Thus \(V_n\) is compactly supported and solenoidal,
\(\|V_n\|_\infty=O_a(1)\), and \(\|\nabla V_n\|_q=O_a(n)\).
For one \(\varepsilon_0>0\), independent of \(n\),
\(B+\varepsilon V_n\) stays uniformly away from zero wherever \(V_n\ne0\).

Because \(B=e_1\) on that support, the cross tensor is globally
\[
 B\otimes V_n+V_n\otimes B=e_1\otimes V_n+V_n\otimes e_1.
\]
Its double divergence is zero distributionally. Consequently
\[
 p[B+\varepsilon V_n]=p_B+\varepsilon^2p_{V_n}
\]
up to an irrelevant spatial constant. No derivative of the plateau cutoff
survives in this cross pressure.

### Order-zero multiplier localization: PASS

For one nonzero periodic mode \(k\), multiplication by a compact amplitude
\(c\) shifts \(\widehat c\) to frequency \(nk\). On
\(|\eta|\le n|k|/2\), a smooth degree-zero symbol satisfies
\[
 |m(nk+\eta)-m(nk)|\le C_kn^{-1}|\eta|.
\]
Plancherel bounds this region by \(C_kn^{-1}\|c\|_{H^1}\). On its complement,
boundedness of the symbol and the Schwartz decay of \(\widehat c\) give
\(O(n^{-M})\). The estimate remains valid for \(R_iR_j\): its symbol is
smooth away from zero, and the possible approach to zero occurs only in the
rapid-decay complement just described. Summing the finite Fourier set gives
the claimed uniform \(O(n^{-1})\) \(L^2\) remainder.

Applying this to \(a^2v_iv_j\), separating its zero Fourier mode, and using
the \(L^2\)-boundedness of the Riesz transforms on all terms involving
\(n^{-1}r_n\), yields
\[
 p_{V_n}=a^2p_v(nx,ny)+q_0+e_n,\qquad
 q_0=R_iR_j(M_{ij}a^2),\qquad
 \|e_n\|_2=O_a(n^{-1}).
\]
The term \(q_0\) is fixed and nonoscillatory. It need not be band limited;
that stronger property is not used.

### Pressure-work asymptotic and limits: PASS

On the plateau, Taylor's theorem and
\(\nabla V_n=na\nabla_{X,Y}v+O_a(1)\) give, uniformly for
\(0<\varepsilon\le\varepsilon_0\),
\[
 (B+\varepsilon V_n)\cdot\nabla|B+\varepsilon V_n|
 =\varepsilon na\,\partial_Xv_1(nx,ny)
  +O_a(\varepsilon)+O_a(n\varepsilon^2)
\]
in every finite \(L^q\) on one fixed compact set.

Periodic averaging is valid with an \(O_a(n^{-1})\) error because the relevant
product is a finite Fourier series and every nonzero mode can be integrated
by parts against \(a^3\). The leading pairing is therefore
\[
 {n\varepsilon^3\over4}\int_{\mathbb R^3}a^3\,dx
 +O_a(\varepsilon^3).
\]
All remaining terms have the asserted uniform sizes:

- oscillatory pressure against the quadratic Taylor error is
  \(O_a(n\varepsilon^4)\);
- \(\varepsilon^2e_n\) against the leading \(O(n\varepsilon)\) factor is
  \(O_a(\varepsilon^3)\);
- outside the oscillatory support, the factor
  \(u\cdot\nabla|u|=B\cdot\nabla|B|\) is fixed, so its pairing with
  \(\varepsilon^2e_n\) is \(O_{a,B}(\varepsilon^2n^{-1})\); thus nonlocality
  of \(e_n\) creates no omitted \(n\)-growing exterior term;
- terms involving \(q_0\) are bounded independently of \(n\) after using
  \(u\cdot\nabla|u|=\operatorname{div}(|u|u)\) and moving the derivative to
  the fixed smooth \(q_0\);
- the \(p_B\) term is bounded independently of \(n\) by the same integration
  by parts, while the region outside \(\operatorname{supp}V_n\) is fixed.

Hence
\[
 P_3[B+\varepsilon V_n]
 ={n\varepsilon^3\over4}\int a^3
  +O_a(n\varepsilon^4)+O_{a,B,\varepsilon}(1).
\]
The order of choices is essential and correct: first choose one sufficiently
small positive \(\varepsilon\) so the \(n\varepsilon^4\) coefficient is less
than half the positive \(n\varepsilon^3\) coefficient; then choose \(n\)
large enough to dominate the remainder, whose constant may depend on that
fixed \(\varepsilon\). The candidate's first error is at most one eighth of
\(n\varepsilon^3\int a^3\), while the second is strictly less than one
eighth; their sum is strictly less than the main one-quarter coefficient.
This proves strict positivity. Replacing both eighths by sixteenths would
make the margin visually immediate but is not mathematically necessary.

Negating \(u\) leaves \(p[u]\) unchanged and reverses
\(u\cdot\nabla|u|\), so both signs occur.

## First bad bridge

None in the reviewed claim.

## Minor corrections

Formatting corrections should be made without changing the proof:

1. In the opening display, restore the intended LaTeX thin-space command
   between \(p[u]\) and \(u\), rather than the rendered comma.
2. In the Hessian display, replace the corrupted quad or qquad text by the
   intended LaTeX spacing command.
3. In equations (17) and (18), restore the missing backslash in
   \(\mathbb R^3\).
4. Describe \(q_0\) as a fixed nonoscillatory term rather than a
   low-frequency term; applying a Riesz transform to \(a^2\) does not make
   it band limited.

These are not mathematical gaps.

## Proof-audit record

**REPLACEMENT ARGUMENT:** none needed.

**CONDITIONAL SUFFIX THAT SURVIVES:** the constructed profile can be inserted
into the previously conditional critical-scaling snapshot test. Under
\(u_N(x)=Nu(Nx)\), \(P_3\) and \(D_3\) scale by \(N^2\), while kinetic energy
scales by \(N^{-1}\).

**UNNECESSARY DEPENDENCIES:** no PDE evolution, viscosity, local existence,
or continuation theorem is needed for this algebraic construction.

**NON-CLAIMS:** the construction is not a solution trajectory, does not
falsify signed time-integrated HF absorption, and supplies no evidence of
finite-time blow-up.

**REOPENING CONDITION:** none for the snapshot existence claim. Any use
against a spacetime estimate requires a separate trajectory argument.
