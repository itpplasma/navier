# HF14: heat monotonicity fails at every fixed high-output cutoff

Status: bounded analytic consequence, 2026-09-05.

This note combines the reviewed full-pressure heat counterexample with the
reviewed low-output boundary estimate. It proves failure of heat monotonicity
for each fixed high-output cutoff. Its quantifiers do not address a cutoff
chosen adaptively from the initial datum.

## Definitions and inputs

For fixed \(k>0\) and integer \(J\), write
\[
 p[u]=R_iR_j(u_i u_j),\qquad p_J^H[u]=(I-S_J)p[u],
\]
and let
\[
 \mathcal J_k^{\rm full}(u)=\mathcal J_k[u;p[u]],\qquad
 \mathcal J_{k,J}^H(u)=\mathcal J_k[u;p_J^H[u]].               \tag{1}
\]
The reviewed HF13 result says that for every fixed \(k>0\) there are a
smooth compactly supported solenoidal field \(h\) and \(\sigma>0\) such that
\[
 d_*:=\mathcal J_k^{\rm full}(e^{\sigma\Delta}h)
          -\mathcal J_k^{\rm full}(h)>0.                       \tag{2}
\]
For viscosity \(\nu>0\), the same heat state is reached at time
\(\sigma/\nu\).

The pre-Young form of the reviewed HF14 boundary estimate is
\[
 \left|\mathcal J_k^{\rm full}(v)-\mathcal J_{k,J}^H(v)\right|
 \le C2^J E(v)\|v\|_3+C2^{3J/2}E(v)^{3/2},                    \tag{3}
\]
where \(E(v)=\|v\|_2^2\). The constants depend on the cutoff profile but
are independent of \(k\).

## Exact scaling and cutoff shift

For \(\lambda>0\), define the Navier--Stokes spatial scaling
\[
 v_\lambda(x)=\lambda v(\lambda x).                            \tag{4}
\]
Then
\[
 p[v_\lambda](x)=\lambda^2p[v](\lambda x),\qquad
 E(v_\lambda)=\lambda^{-1}E(v),\qquad
 \|v_\lambda\|_3=\|v\|_3.                                    \tag{5}
\]
Every term in the full functional is cubic and hence
\[
 \mathcal J_k^{\rm full}(v_\lambda)=\mathcal J_k^{\rm full}(v). \tag{6}
\]
The heat semigroup obeys
\[
 e^{\nu(t/\lambda^2)\Delta}v_\lambda
 =(e^{\nu t\Delta}v)_\lambda.                                \tag{7}
\]

There is also an exact cutoff relation. If the low-pass symbol is
\(\chi(2^{-J}\xi)\), then
\[
 S_Jp[v_\lambda](x)
 =\lambda^2(S_{J-\log_2\lambda}p[v])(\lambda x).               \tag{8}
\]
For dyadic \(\lambda=2^m\), all cutoff indices remain integral, and
homogeneity of the scalar coupling gives
\[
 \mathcal J_{k,J}^H(v_\lambda)=\mathcal J_{k,J-m}^H(v).        \tag{9}
\]
Thus concentration at a fixed physical cutoff is equivalently a shift of
the cutoff toward lower indices in the unscaled profile.

## Transfer of the positive heat increment

Put
\[
 h_\lambda=(h)_\lambda,\qquad
 t_\lambda={\sigma\over\nu\lambda^2},\qquad
 H=e^{\sigma\Delta}h.
\]
By (6)--(7),
\[
 \mathcal J_k^{\rm full}(e^{\nu t_\lambda\Delta}h_\lambda)
 -\mathcal J_k^{\rm full}(h_\lambda)=d_*.                     \tag{10}
\]
Apply (3) at the two endpoints. Equations (5) and (7) give
\[
 \begin{split}
 &\left|\mathcal J_k^{\rm full}(h_\lambda)
              -\mathcal J_{k,J}^H(h_\lambda)\right|\\
 &\qquad\le C2^J\lambda^{-1}E(h)\|h\|_3
       +C2^{3J/2}\lambda^{-3/2}E(h)^{3/2},                    \tag{11}
\end{split}
\]
and
\[
 \begin{split}
 &\left|\mathcal J_k^{\rm full}(H_\lambda)
              -\mathcal J_{k,J}^H(H_\lambda)\right|\\
 &\qquad\le C2^J\lambda^{-1}E(H)\|H\|_3
       +C2^{3J/2}\lambda^{-3/2}E(H)^{3/2}.                    \tag{12}
\end{split}
\]
For fixed \(J\), both right-hand sides tend to zero as
\(\lambda\to\infty\). Choose a sufficiently large dyadic \(\lambda\) so
their sum is less than \(d_*\). Combining (10)--(12) yields
\[
 \boxed{\quad
 \mathcal J_{k,J}^H(e^{\nu t_\lambda\Delta}h_\lambda)
 >\mathcal J_{k,J}^H(h_\lambda).
 \quad}                                                       \tag{13}
\]
Spatial scaling preserves smoothness, compact support, and solenoidality.

The precise quantifier statement is therefore
\[
 \forall k>0\ \forall J\in\mathbb Z\ \forall\nu>0\
 \ \exists h_{k,J}\in C_c^\infty(\mathbb R^3;\mathbb R^3)\
 \ \exists t_{k,J,\nu}>0:
 \quad\nabla\cdot h_{k,J}=0
\]
and (13) holds. The field can be chosen independently of \(\nu\), with only
the heat time rescaled.

## Scope

This proves that no fixed cutoff \(J\) makes the high-output homogeneous
functional universally nonincreasing under linear heat flow. It does not
refute a mechanism whose quantifiers choose \(J=J(u_0,\nu,H)\) after seeing
the datum: the statement proved here is \(\forall J\,\exists h_J\), not
\(\exists h\,\forall J\). Nor is the linear heat trajectory a
Navier--Stokes trajectory. The argument supplies no spacetime HF failure,
pressure-absorption obstruction, blow-up, or regularity conclusion.

## Frontier record

**MODE / RESULT:** FALSIFY. For every fixed \(k>0\) and fixed cutoff \(J\),
the high-output functional increases on some finite linear heat step.

**FIRST GAP:** determine whether a datum-dependent cutoff and the complete
Navier--Stokes Euler contribution can yield the required spacetime estimate.

**SURVIVING CONDITIONAL SUFFIX:** the boundary replacement estimate remains
valid and is what transfers the full-pressure obstruction at each fixed
cutoff.

**NON-CLAIMS:** no single datum defeats every cutoff, and adaptive HF is not
refuted.
