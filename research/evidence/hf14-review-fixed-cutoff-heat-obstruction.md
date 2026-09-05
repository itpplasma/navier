# Independent audit of the fixed-cutoff heat obstruction

VERDICT: **PASS**

REVIEWED SCOPE: research/evidence/hf14-fixed-cutoff-heat-obstruction.md,
frozen with SHA-256
eef0f7a7b5c2d9d7ad1e1e8d6996d3516e0c34179e30e445837c3f963ebd5f2b
on base commit f297efc46756f5acd229e4a8aaa5284655ec6903.
The boundary input is the frozen
research/evidence/hf14-high-output-boundary.md with SHA-256
0c9226f6dba446a9b66a0932177c6d921f9e3ed0390e06f43e7f9a56e0a4f3b9
on the same base.

FIRST BAD BRIDGE: none.

EVIDENCE:

1. For \(v_\lambda(x)=\lambda v(\lambda x)\), direct Fourier scaling gives
   \[
      p[v_\lambda](x)=\lambda^2p[v](\lambda x).
   \]
   Change of variables gives
   \(E(v_\lambda)=\lambda^{-1}E(v)\) and
   \(\|v_\lambda\|_3=\|v\|_3\).  Since
   \(r\mapsto\lambda r\), \(\pi_-\mapsto\lambda^2\pi_-\), the two square
   roots in \(g_k\) each scale by \(\lambda\), so \(g_k\) and
   \(\pi_-^{3/2}\) scale by \(\lambda^3\).  The spatial Jacobian is
   \(\lambda^{-3}\), proving the full functional invariance (6) with \(k\)
   unchanged.

2. If \(\widehat{S_Jf}(\xi)=\chi(2^{-J}\xi)\widehat f(\xi)\), substitution
   \(\xi=\lambda\eta\) gives
   \[
      S_Jp[v_\lambda](x)
      =\lambda^2(S_{J-\log_2\lambda}p[v])(\lambda x).
   \]
   Thus (8) has the correct direction of cutoff shift.  For
   \(\lambda=2^m\), homogeneity of all scalar terms and change of variables
   give (9), with integral cutoff indices throughout.

3. Heat scaling is
   \[
      e^{\nu(t/\lambda^2)\Delta}v_\lambda
      =(e^{\nu t\Delta}v)_\lambda.
   \]
   Taking \(t=\sigma/\nu\), equivalently
   \(t_\lambda=\sigma/(\nu\lambda^2)\), yields
   \[
      e^{\nu t_\lambda\Delta}h_\lambda
      =(e^{\sigma\Delta}h)_\lambda=H_\lambda.
   \]
   Full-functional invariance then preserves the exact positive increment
   \(d_*\), proving (10).  The field does not depend on \(\nu\); only its
   heat time does.

4. Applying the frozen pre-Young boundary estimate at \(h_\lambda\) gives
   \[
   C2^J E(h_\lambda)\|h_\lambda\|_3
   +C2^{3J/2}E(h_\lambda)^{3/2}
   =
   C2^J\lambda^{-1}E(h)\|h\|_3
   +C2^{3J/2}\lambda^{-3/2}E(h)^{3/2}.
   \]
   This is exactly (11).  Replacing \(h\) by
   \(H=e^{\sigma\Delta}h\) proves (12), with the same powers.  No heat
   contraction estimate is needed beyond finiteness of the fixed endpoint
   norms.

5. For fixed \(J\), the two endpoint errors tend to zero as
   \(\lambda\to\infty\).  Choosing a sufficiently large dyadic
   \(\lambda\) keeps (9) integral-valued and makes their sum less than
   \(d_*\).  The triangle inequality gives
   \[
   \begin{aligned}
   \mathcal J_{k,J}^H(H_\lambda)-\mathcal J_{k,J}^H(h_\lambda)
   &\ge
   \mathcal J_k^{\rm full}(H_\lambda)
    -\mathcal J_k^{\rm full}(h_\lambda)\\
   &\quad-
   |\mathcal J_{k,J}^H(H_\lambda)-\mathcal J_k^{\rm full}(H_\lambda)|
   -
   |\mathcal J_{k,J}^H(h_\lambda)-\mathcal J_k^{\rm full}(h_\lambda)|\\
   &>0.
   \end{aligned}
   \]
   This proves (13).  Scaling preserves smoothness, compact support, and
   divergence freedom.

6. The quantifiers are exactly
   \[
      \forall k>0\ \forall J\in\mathbb Z\ \forall\nu>0\
      \exists h_{k,J}\ \exists t_{k,J,\nu}>0.
   \]
   The full-pressure input first chooses \(h,\sigma\) for \(k\); the
   concentration factor then depends on the fixed \(J\), while
   \(t_{k,J,\nu}=\sigma/(\nu\lambda^2)\).  This is
   \(\forall J\,\exists h_J\).  It neither constructs one datum defeating
   all cutoffs nor addresses a cutoff selected after seeing the datum.

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: Given the reviewed full-pressure heat
increment (2) and the frozen boundary estimate (3), the complete fixed-cutoff
transfer survives.  For every fixed \(k,J,\nu\), some smooth compactly
supported solenoidal datum makes the high-output functional increase over a
finite linear heat step.

UNNECESSARY DEPENDENCIES: The transfer needs only cubic scaling, heat
scaling, and the two static endpoint comparisons.  It does not differentiate
either functional or use a Navier--Stokes nonlinear evolution.

NON-CLAIMS: This result does not refute a datum-dependent cutoff, construct
one field that defeats every \(J\), transfer linear heat behavior to a
Navier--Stokes trajectory, disprove HF, or imply blow-up or failure of
regularity.

REOPENING CONDITION: To bear on adaptive HF, supply one datum with uniform
control over all candidate cutoffs, or derive the complete nonlinear
spacetime evolution at the datum-dependent cutoff.
