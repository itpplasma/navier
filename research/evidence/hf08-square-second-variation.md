# HF08: complete second variation of the finite-band square energy

Status: finite-band, positive-regularization REPAIR calculation.  This note
retains the low-mode feedback and background-weight evolution omitted by the
frozen-strain oracle.  It proves exact algebraic formulas but does not pass to
all dyadic bands or claim a sign obstruction, pressure absorption, or
regularity.

## 1. Functional and Euler rate

Fix a finite set of real self-adjoint dyadic operators
\(W=(\Delta_j)_{j\in I}\), and write the pointwise Euclidean inner product over
both shell and vector indices as a dot.  For regularization parameter
\(\epsilon>0\), define

\[
 s_u=(\epsilon^2+|Wu|^2)^{1/2},\qquad
 F_\epsilon(u)={1\over3}\int(s_u^3-\epsilon^3).        \tag{1}
\]

Let the Euler generator be

\[
 V(u)=-\mathbb P((u\cdot\nabla)u),                    \tag{2}
\]

and set

\[
 \mathcal R_\epsilon(u)=DF_\epsilon(u)[V(u)].         \tag{3}
\]

The amplitude parameter below is \(h\), kept distinct from \(\epsilon\).

For shell arrays \(x=Wh\), \(z=Wk\), and \(y=Wu\), direct differentiation
gives

\[
 DF_\epsilon(u)[h]=\int s_u\,y\cdot x,                \tag{4}
\]

\[
 D^2F_\epsilon(u)[h,k]
 =\int\left[s_u\,x\cdot z+{(y\cdot x)(y\cdot z)\over s_u}\right], \tag{5}
\]

and

\[
\begin{aligned}
 D^3F_\epsilon(u)[h,k,l]=\int
 &{(y\cdot Wh)(Wk\cdot Wl)
   +(y\cdot Wk)(Wh\cdot Wl)
   +(y\cdot Wl)(Wh\cdot Wk)\over s_u}\\
 &-{(y\cdot Wh)(y\cdot Wk)(y\cdot Wl)\over s_u^3}.   \tag{6}
\end{aligned}
\]

These formulas are nonsingular because \(s_u\geq\epsilon\).

## 2. Exact coefficient at a low background

Let \(U\) occupy dyadic components disjoint from those of \(v\), so

\[
 WU\cdot Wv=0                                        \tag{7}
\]

pointwise in shell-array space.  Since \(V\) is quadratic,

\[
 V(U+hv)=V(U)+hV_{\rm lin}(U,v)+h^2V(v),              \tag{8}
\]

where

\[
 V_{\rm lin}(U,v)
 =-\mathbb P((U\cdot\nabla)v+(v\cdot\nabla)U).        \tag{9}
\]

Taylor expansion of (3), with no frozen-weight approximation, shows that the
coefficient of \(h^2\) in \(\mathcal R_\epsilon(U+hv)\) is

\[
\boxed{
 \mathcal C_2(U,v)
 =DF_\epsilon(U)[V(v)]
  +D^2F_\epsilon(U)[v,V_{\rm lin}(U,v)]
  +{1\over2}D^3F_\epsilon(U)[v,v,V(U)].}              \tag{10}
\]

All three terms are necessary.  By (4)--(7), this becomes the exact
finite-band formula

\[
\boxed{
\begin{aligned}
 \mathcal C_2(U,v)=
 &\int s_U(WU)\cdot WV(v)\\
 &+\int s_U(Wv)\cdot WV_{\rm lin}(U,v)\\
 &+{1\over2}\int {WU\cdot WV(U)\over s_U}|Wv|^2.
                                                               \tag{11}
\end{aligned}}
\]

The first line is high-high feedback into the low background.  The second is
the linearized high-mode evolution.  The third is evolution of the background
weight.  The previously isolated frozen-strain term is only a portion of the
second line.

Independently, expansion of the energy itself gives

\[
 [h^2]F_\epsilon(U+hv)={1\over2}\int s_U|Wv|^2,       \tag{12}
\]

which confirms that the relevant quadratic high-mode energy carries the
background weight.

## 3. Constant-weight cancellation

For the ordinary quadratic energy \(E(u)=\frac12\|u\|_2^2\), Euler
cancellation says \(DE(u)[V(u)]=0\) for every smooth divergence-free field.
Its \(h^2\) coefficient is therefore

\[
 \langle U,V(v)\rangle
 +\langle v,V_{\rm lin}(U,v)\rangle=0.                \tag{13}
\]

The cancellation can be seen directly:

\[
 \langle U,V(v)\rangle
 =\int v_i v_j\partial_jU_i,\qquad
 \langle v,V_{\rm lin}(U,v)\rangle
 =-\int v_i v_j\partial_jU_i.                         \tag{14}
\]

Self-adjointness of \(\mathbb P\), divergence freedom, and integration by
parts justify both identities.  Thus the low-mode backreaction cancels the
frozen-strain form exactly.  The unweighted strain oracle cannot be promoted
to an obstruction for the complete second variation.

If \(W\) is a complete tight frame and the weight is a spatial constant
\(s_U=c\), the first two lines of (11) reduce to \(c\) times (13).  If the
background weight is also frozen in time, the third line vanishes.  Finite
band edges and a variable or evolving weight are therefore the only possible
sources remaining in this calculation.

## 4. Principal variable-weight form with the Leray terms retained

Define the finite-band weighted operator

\[
 \mathcal M_s=W^*M_sW,                                \tag{15}
\]

where \(M_s\) is multiplication by \(s=s_U(x)\).  The first two lines of
(11) are exactly

\[
 \langle\mathcal M_sU,V(v)\rangle
 +\langle\mathcal M_sv,V_{\rm lin}(U,v)\rangle.       \tag{16}
\]

This formula already retains the Leray projector inside both generators and
all finite-band multiplier effects inside \(\mathcal M_s\).

To identify the principal scalar-weight contribution, temporarily replace
\(\mathcal M_s\) by multiplication by \(s\), but do **not** discard the
Leray projector.  Put

\[
 N_{vv}=(v\cdot\nabla)v,\qquad
 N_{Uv}=(U\cdot\nabla)v+(v\cdot\nabla)U.              \tag{17}
\]

Since \(\mathbb P(sf)=s\mathbb Pf+[\mathbb P,s]f\), integration by parts
gives the exact scalar-weight identity

\[
\begin{aligned}
 &\langle sU,V(v)\rangle+\langle sv,V_{\rm lin}(U,v)\rangle\\
 &=\int (U\cdot v)(v\cdot\nabla s)
   +{1\over2}\int |v|^2U\cdot\nabla s\\
 &\quad-\langle[\mathbb P,s]U,N_{vv}\rangle
       -\langle[\mathbb P,s]v,N_{Uv}\rangle.          \tag{18}
\end{aligned}
\]

In particular, every explicit frozen-strain term cancels between feedback and
linearized evolution.  What remains is transport of the weight and two
weighted Leray commutators.

The third line of (11) is

\[
 {1\over2}\int \dot s_U^{\,E}|Wv|^2,\qquad
 \dot s_U^{\,E}:={WU\cdot WV(U)\over s_U}.             \tag{19}
\]

It is the Euler-background variation of the square-function weight and has no
fixed sign.

Finally, the difference between the exact finite-band expression (11) and
the scalar principal form (18)--(19) is not hidden.  It is the explicit
multiplier remainder

\[
\begin{aligned}
 \mathcal E_W(U,v):={}&
 \langle(\mathcal M_s-M_s)U,V(v)\rangle
 +\langle(\mathcal M_s-M_s)v,V_{\rm lin}(U,v)\rangle\\
 &+{1\over2}\int\left(
 {WU\cdot WV(U)\over s_U}|Wv|^2
 -{U\cdot V(U)\over s_U}|v|^2\right).                \tag{20}
\end{aligned}
\]

With this notation the principal second variation is the sum of the four
terms in (18), the scalar background-weight term
\(\frac12\int (U\cdot V(U))|v|^2/s_U\), and
\(\mathcal E_W\).  No band-edge or multiplier contribution has been declared
small.

## 5. What the complete calculation does and does not show

Equations (11) and (16) are exact in the stated finite-band regularized
setting.  They show that a constant quadratic weight cancels the leading
strain completely.  Equations (18)--(20) locate all possible surviving
principal terms:

* spatial transport of \(s_U\);
* Leray commutators \([\mathbb P,s_U]\);
* Euler evolution of the background weight;
* finite-band square-function multiplier and band-edge defects.

Each is signed.  This note does not claim that their sum is nonzero or
indefinite.  Such a conclusion requires evaluating the complete expression
on explicit divergence-free fields or wave packets; an upper bound for the
individual terms cannot rule out another exact cancellation.

The scale of the terms is still critical.  In a low-high configuration,
\(\nabla s_U\) is of the size of the low gradient, while a derivative in
\(N_{vv}\) or \(N_{Uv}\) falls on the high field.  The Leray commutators can
exchange that derivative for \(\nabla s_U\), but supply no small factor after
the shell separation is summed.  This is a location of the next calculation,
not a proved no-go theorem.

## 6. Frontier result

**Repair obtained:** the coefficient (10)--(11) restores both low-mode
feedback and background-weight evolution.  It invalidates the frozen-strain
argument as a standalone obstruction.

**Exact remaining object:** the finite-band second variation is (18)--(20),
including Leray commutators and multiplier defects.  No term may be dropped
before an explicit asymptotic or exact field evaluation.

**First unresolved bridge:** determine the sign or cancellation of the full
sum (18)--(20) on explicit scale-separated divergence-free data.  This note
does not manufacture a sign conclusion from an absolute estimate.

**Scope:** all formulas use fixed finite \(I\) and \(\epsilon>0\).  No
\(I\uparrow\mathbb Z\), \(\epsilon\downarrow0\), endpoint-time, HF, or global
regularity conclusion is asserted.
