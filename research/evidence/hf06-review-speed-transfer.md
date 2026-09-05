# Audit of the R3 speed-transfer construction

VERDICT: **REPAIR**

REVIEWED SCOPE: `hf06-r3-speed-transfer.md` at verified SHA-256
`9fff67013a8d6595085ed2166e92aa1650d099b311007c6e42a02abcc5ce1db5`,
on full base commit `bd2ae2d1253d31c580ad07211cad02379758c000`.

FIRST BAD BRIDGE: In the passage to (20), the text says to apply the
speed-gradient comparison with
\(q=w_{s_0}/|w_{s_0}|\). That choice makes the comparison profile
\(a q(kz)\), whose speed is just \(a\), rather than the actual leading heat
profile \(a w_{s_0}(kz)\). It therefore discards the nonconstant magnitude
whose gradient supplies the positive numerator in (20).

REPLACEMENT ARGUMENT: Apply (8) with \(q=w_{s_0}\) itself. By the choice of
\(s_0\), \(w_{s_0}\) is smooth, periodic, and bounded away from zero, so it
satisfies the lemma's hypotheses. Set
\[
 V_k(x)=a(x)w_{s_0}(kz),\qquad
 E_k=u_k(t_k)-V_k.
\]
Equations (18)--(19) give
\(\|E_k\|_2=O(k^{-1})\) and \(\|\nabla E_k\|_2=O(1)\). Hence (8) gives
\[
 \|\nabla|u_k(t_k)|-\nabla|V_k|\|_2=O(1).
\]
Since
\[
 \nabla|V_k|=(\nabla a)|w_{s_0}(kz)|
   +k a\,\partial_z|w_{s_0}|(kz)e_z,
\]
periodic averaging after division by \(k\) proves the second limit in (20).
The ordinary gradient satisfies the analogous expansion, proving the first
limit. Thus (21) follows exactly as claimed.

EVIDENCE:

1. The antiperiodicity \(v(z+\pi)=-v(z)\) gives zero means for both
   horizontal components. Periodic primitives therefore exist, and direct
   computation of the curl in (5) gives
   \(u_{0,k}=a v(kz)+k^{-1}r_k\), with compact support and zero divergence.
   The stated \(L^2\), \(L^\infty\), and one-derivative bounds follow because
   only a \(z\)-derivative of the periodic factors costs \(k\).

2. The comparison lemma includes envelope zeros. Almost everywhere,
   \(\nabla|f|=\widehat f\cdot\nabla f\) off \(f=0\), with the Sobolev chain
   rule supplying the zero-set formulation. For the fast part,
   \[
    ak|q'|\,|\widehat{V+e}-\widehat V|
       \le Ck\min(a,|e|)\le Ck|e|.
   \]
   For the slow part the bound is \(C|\nabla a|\). A smooth nonnegative
   envelope has \(\nabla a=0\) on its zero set, so no division by \(a\) is
   hidden. This proves (8). With \(q=v\), it yields (9), while averaging the
   leading fast derivative yields (10) and hence (11).

3. The Oseen kernel
   \(e^{\nu t\Delta}\mathbb P\operatorname{div}\) has convolution-kernel
   \(L^1\) norm at most \(C(\nu t)^{-1/2}\). The uniform initial
   \(L^\infty\) bound therefore gives a common bounded mild lifespan. Smooth
   compactly supported data give smooth solutions on this interval. The
   \(L^2\) energy identity supplies the common \(L^2\) bound.

4. Applying the same kernel bound in \(L^2\), with
   \(\|u\otimes u\|_2\le\|u\|_\infty\|u\|_2\), proves (14). Testing the
   equation against \(-\Delta u\) gives
   \[
    \tfrac12(\|\nabla u\|_2^2)'+\nu\|\Delta u\|_2^2
      \le \|u\|_\infty\|\nabla u\|_2\|\Delta u\|_2,
   \]
   so Young and Gronwall give the uniform \(O(k)\) H1 control. Moving one
   derivative to \(u\otimes u\) then proves (16). At fixed viscosity and
   \(t_k=s_0/(\nu k^2)\), these are precisely the errors in (18).

5. Conjugating the heat operator by the Fourier carrier gives
   \[
    e^{\nu t_k\Delta}(ae^{inkz})
     =e^{inkz}e^{(s_0/k^2)\Delta+(2ins_0/k)\partial_z-s_0n^2}a.
   \]
   Taylor expansion for the smooth compact envelope, summed against the
   rapidly decaying Fourier coefficients, proves the global \(L^2\) and H1
   errors in (19). The embedded correction has the same orders. There is no
   unsupported replacement of a local estimate by a global one.

6. The periodic heat expansion is independently consistent:
   \(v\cdot v''=-|v'|^2\) gives
   \(|w_s|=1-s\vartheta'^2+O(s^2)\) in smooth periodic norms. Because
   \(\partial_z(\vartheta'^2)\not\equiv0\), one fixed sufficiently small
   \(s_0>0\) has a nonzero averaged squared speed gradient, while
   \(w_{s_0}\) remains bounded away from zero. The denominator is positive
   by continuity from \(v'\not\equiv0\).

7. Periodic averaging applies to each leading quadratic integral with the
   fixed compact weight \(a^2\). All nonlinear, heat-localization, and slow
   envelope errors are \(O(1)\) in H1 and disappear after normalization by
   \(k\). The limiting denominator is nonzero, so quotient convergence in
   (21) is valid.

CONDITIONAL SUFFIX THAT SURVIVES: With the repaired choice
\(q=w_{s_0}\), the construction rigorously gives compactly supported smooth
R3 data with uniformly bounded initial \(L^3\), a common smooth interval,
\(\delta_k(0)\to0\), and \(\delta_k(t_k)\to c_{s_0}>0\).

UNNECESSARY DEPENDENCIES: The conclusion needs only one fixed viscosity
\(\nu>0\), one sufficiently small fixed \(s_0\), and the common bounded mild
interval. No global regularity or high-frequency estimate is used.

NON-CLAIMS: This is a regular short-time R3 diagnostic. It proves neither
blow-up nor failure of the signed HF hypothesis, and it does not preclude a
propagation theorem with an order-one parabolic-scale defect or additional
geometric input.

REOPENING CONDITION: none after the displayed replacement.
