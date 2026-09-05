# HF14: exact evolution with high-output pressure coupling

MODE / RESULT: **DISCOVER.**  Replacing the full pressure in the homogeneous
coupling by its high-output part separates the already controlled low
pressure work exactly.  It does not produce a new estimate: the remaining
Euler and heat terms still contain a high-output pressure source, a
full-pressure gradient, and indefinite heat Hessian terms.

## 1. Setup and regularity scope

Fix a smooth real self-adjoint low-pass multiplier \(S_J\), commuting with
derivatives and Riesz transforms, and put
\[
 Q_J=I-S_J,\qquad p=R_iR_j(u_i u_j),\qquad
 z=p_H=Q_Jp,\qquad p_L=S_Jp.                          \tag{1}
\]
For \(k>0\), define
\[
 q=z_-,\qquad
 \rho_k(r,z)=\sqrt{r^2+kq}-\sqrt{kq},\qquad
 g_k(r,z)=z\rho_k(r,z),                              \tag{2}
\]
\[
 \mathcal J_{k,J}(u)=\int_{\mathbb R^3}
 f_k(r,z)\,dx,\qquad
 f_k(r,z)={r^3\over3}+g_k(r,z)+z_-^{3/2},\quad r=|u|.
                                                               \tag{3}
\]

The formulas below are classical where \(r>0\) and \(z\ne0\).  For a
globally classical identity, take a \(C^2\) scalar approximation
\(f^\eta(r,z)\), smooth as a radial function of \(u\), normalized by
\[
 f^\eta(0,0)=0,\qquad f^\eta_z(0,0)=0,               \tag{4}
\]
and having the same cubic growth bounds.  The second normalization is needed
on \(\mathbb R^3\), since \(p_H\) need not be integrable.  The exact generic
identity in Section 2 applies to each fixed \(\eta>0\).  Passing
\(\eta\downarrow0\) requires separate domination and is not asserted here.
In particular, (3) is not claimed to be differentiable across
\(\{u=0,z>0\}\), where \(g_k=z|u|\).

Let \(u\) be a smooth rapidly decreasing solution at the time considered,
and write
\[
 u_t=\nu\Delta u+V,\qquad
 V=-\mathbb P((u\cdot\nabla)u)=-N-\nabla p.           \tag{5}
\]

## 2. Generic exact evolution

For any density \(f=f(r,z)\) satisfying the fixed regularity and
integrability conditions above, set
\[
 \beta={f_r\over r},
\]
with its smooth radial extension at \(r=0\).  Pressure differentiation gives
\[
 p_t=2R_iR_j(u_i u_{t,j}),\qquad
 z_t=2Q_JR_iR_j(u_i u_{t,j}).                         \tag{6}
\]
For the heat part, the product rule
\[
 2R_iR_j(u_i\Delta u_j)
 =\Delta p-2R_iR_j(G_{ij}),\qquad
 G_{ij}=\partial_\ell u_i\,\partial_\ell u_j,         \tag{7}
\]
and commutation with \(Q_J\) yield
\[
 z_t^{\,H}=\nu\Delta z-2\nu Q_JR_iR_j(G_{ij}).        \tag{8}
\]

The exact Euler contribution is
\[
\boxed{\quad
 \mathcal E_f
 =\int {f_r\over r}u\cdot V
 +2\int f_z\,Q_JR_iR_j(u_iV_j).
\quad}                                                \tag{9}
\]
The exact heat contribution is
\[
\boxed{\begin{aligned}
 {\mathcal H_f\over\nu}={}&
 -\int {f_r\over r}|\nabla u|^2
 -\int\left(f_{rr}-{f_r\over r}\right)|\nabla r|^2\\
 &-2\int f_{rz}\,\nabla r\cdot\nabla z
 -\int f_{zz}|\nabla z|^2\\
 &-2\int f_z\,Q_JR_iR_j(G_{ij}).
\end{aligned}}                                       \tag{10}
\]
Thus
\[
 {d\over dt}\int f(r,z)=\mathcal H_f+\mathcal E_f.   \tag{11}
\]

To verify (10), integration by parts gives
\[
\begin{aligned}
 \int {f_r\over r}u\cdot\Delta u
 ={}&-\int {f_r\over r}|\nabla u|^2
 -\int\left(f_{rr}-{f_r\over r}\right)|\nabla r|^2\\
 &-\int f_{rz}\nabla r\cdot\nabla z,                 \tag{12}
\end{aligned}
\]
while
\[
 \int f_z\Delta z
 =-\int f_{rz}\nabla r\cdot\nabla z
  -\int f_{zz}|\nabla z|^2.                          \tag{13}
\]
Equations (8), (12), and (13) account for every heat-gradient and
nonlocal pressure-source term in (10), including the factor two in the mixed
gradient.

## 3. Euler algebra for the homogeneous high-pressure density

For \(z<0\), put
\[
 s_H=\sqrt{r^2+kz_-}.
\]
Away from the cusps,
\[
 {g_{k,r}\over r}=
 \begin{cases}
 z/r,&z>0,\\
 z/s_H,&z<0,
 \end{cases}                                         \tag{14}
\]
and define the complete pressure derivative
\[
 a_k(r,z)=g_{k,z}(r,z)
 -{3\over2}\sqrt{z_-}\,\mathbf1_{\{z<0\}}.            \tag{15}
\]
Substituting \(f=f_k\) in (9), the cubic-speed term gives
\[
 \int r u\cdot V=\int p\,u\cdot\nabla r.              \tag{16}
\]
Indeed the transport part vanishes and the full pressure in \(V\), not
\(p_H\), appears after integration by parts.  Splitting \(p=p_L+p_H\), and
combining the \(p_H\) portion with the transport part of the
\(g_k\)-speed derivative, gives
\[
\boxed{\begin{aligned}
 \mathcal E_{k,J}={}&L_J
 +\int_{\{p_H<0\}}p_H\left(1-{r\over s_H}\right)
                 u\cdot\nabla r\\
 &-\int {g_{k,r}(r,p_H)\over r}\,u\cdot\nabla p\\
 &+2\int a_k(r,p_H)Q_JR_iR_j(u_iV_j),
\end{aligned}}                                       \tag{17}
\]
where
\[
 L_J=\int p_L\,u\cdot\nabla r.                       \tag{18}
\]
On \(\{p_H>0\}\), \(g_{k,r}=p_H\), so its transport term cancels that
portion of (16) exactly.  On \(\{p_H<0\}\),
\(g_{k,r}=p_Hr/s_H\), leaving the second term of (17).  The
pressure-gradient part of \(V\) produces the third term with the full
\(\nabla p\).  Finally (6) produces the last, high-output pressure-variation
term.  Hence neither the low pressure inside \(V\) nor any output of the
quadratic pressure derivative has been discarded.

## 4. What the cutoff changes

The standard fixed-cutoff low-pressure estimate controls the time integral
of \(L_J\) on compact classical intervals by the energy-level remainder
already recorded in the project.  After removing \(L_J\), the first
uncontrolled sum is
\[
\boxed{\begin{aligned}
 \mathfrak R_{k,J}(u)={}&
 \int_{\{p_H<0\}}p_H\left(1-{r\over s_H}\right)
                 u\cdot\nabla r\\
 &-\int {g_{k,r}(r,p_H)\over r}\,u\cdot\nabla p\\
 &+2\int a_k(r,p_H)Q_JR_iR_j(u_iV_j)
 +\mathcal H_{f_k}(u),
\end{aligned}}                                       \tag{19}
\]
where \(\mathcal H_{f_k}\) is the complete expression (10), understood
through a fixed smooth scalar regularization unless cusp domination has been
proved.

The cutoff therefore locates the known low-output producer but does not
remove the unknown high-frequency mechanism.  In particular:

* the defect term on \(\{p_H<0\}\) has no sign;
* the coefficient \(g_{k,r}/r\) is paired with the gradient of the full
  pressure, including \(p_L\);
* the pressure variation remains
  \(Q_JR_iR_j(u_iV_j)\), an aggregate high-output nonlinear source;
* the heat expression contains mixed \((r,p_H)\) gradients and
  \(Q_JR_iR_j(G_{ij})\), with no established sign.

Bounding the time integral of (19) by a strict fraction of dissipation plus
an input-only remainder would be a new estimate, not a consequence of the
cutoff or the static coercivity of \(\mathcal J_{k,J}\).

## 5. Frontier record

CLAIM AND SCOPE: Equations (9)--(13) are exact for fixed smooth integrable
scalar regularizations.  Equation (17) is the away-from-cusps algebra for the
unregularized homogeneous density.  It uses the genuine Navier--Stokes
generator with full pressure and the fixed input cutoff \(J\).

EVIDENCE: Pressure differentiation (6)--(8), the Hessian heat calculation
(10)--(13), and the cancellation reconstruction (14)--(18) retain every
velocity, pressure-gradient, and nonlocal pressure-source term.

FIRST GAP: prove a one-sided spacetime estimate for the complete sum (19),
uniformly up to the maximal classical time with the required input
quantifiers.  No such estimate is derived here.

SURVIVING CONDITIONAL SUFFIX: The known low-output estimate applies to
\(L_J\).  Any independently established control of (19), together with
coercivity and a justified removal of scalar regularization, could feed the
existing continuation architecture.

NON-CLAIMS: No differentiability across the positive-pressure velocity cusp,
regularization limit, favorable heat sign, control of the high-output source,
pressure absorption, HIGH-PRESSURE theorem, critical bound, or regularity
result is asserted.

NEXT DISTINCT ACTION: Test the combined high-output source and heat Hessian
in (19) on an explicit compact solenoidal packet, rather than estimating its
individual signed terms separately.
