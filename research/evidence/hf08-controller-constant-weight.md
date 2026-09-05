# Exact constant-weight oracle for the complete square-energy variation

Status: controller candidate, awaiting independent audit. This is a periodic
mechanism diagnostic, not an R3 continuation theorem or a claim about HF.

Work on the torus `(R/2pi Z)^3` with normalized integral `<.>`. Let a smooth
real radial dyadic tight frame have multipliers `m_j`, with
`sum_j m_j(xi)^2=1` at every nonzero frequency. Choose a finite interval I
containing all active shells of the fields below. Choose N large enough that
the low background and the high perturbation occupy disjoint shell indices.
Only finitely many shells act on these trigonometric polynomials.

For epsilon>0, let W=(Delta_j)_(j in I), s_u=sqrt(epsilon^2+|Wu|^2),
F(u)=1/3 <s_u^3-epsilon^3>, and V(u)=-P((u.grad)u), with P the torus
Leray projector. Define R(u)=DF(u)[V(u)].

Set

```
U=(cos z, sin z, 0),
k=(N,0,N),       a=(1,0,-1),
l=(-N,0,1-N),    b=(1-1/N,0,-1),
v=a cos(k.x)+b sin(l.x),         N an integer sufficiently large.
```

Both fields are real and divergence free: `k.a=l.b=0`. Moreover
`(U.grad)U=0`, so `V(U)=0`. Radiality gives
`Delta_j U=m_j((0,0,1))U`; hence `|WU|^2=|U|^2=1` and
`s_U=c=sqrt(epsilon^2+1)` is a spatial constant. The low/high shell
separation gives `WU.Wv=0` pointwise.

The exact second-order coefficient in the amplitude h is

```
[h^2] R(U+h v)
 = <s_U WU . WV(v)>
   + <s_U Wv . W[-P((U.grad)v+(v.grad)U)]>
   + 1/2 <(WU.WV(U))/s_U |Wv|^2>.
```

The last term vanishes because V(U)=0. For either f=U or f=v and any
smooth g, self-adjointness and the tight-frame identity on the Fourier
support of f give `<Wf.Wg>=<f.g>`. Thus the coefficient equals

```
c { <U.V(v)> + <v.-P((U.grad)v+(v.grad)U)> } = 0.
```

Indeed the first pairing is `<v_i v_j partial_j U_i>` by integration by
parts, while the second is its negative; the U-transport pairing vanishes.
The cancellation includes low-mode backreaction, even though high-high
nonlinearity can produce frequencies outside I. Those frequencies have
zero pairing with U or v, so no completeness assertion about V(v) is needed.

The frozen-strain term is nevertheless strictly nonzero. Write
K=Nx+Nz and L=-Nx+(1-N)z. Since v_2=0,

```
<v_i v_j partial_j U_i> = <-v_1 v_3 sin z>,
v_1 v_3 = -cos^2 K -(2-1/N)cos K sin L -(1-1/N)sin^2 L.
```

The square terms have zero pairing with sin z. Using
`cos K sin L = [sin z + sin(L-K)]/2`, whose second term has nonzero
x-frequency, yields exactly

```
<v_i v_j partial_j U_i> = (2-1/N)/4 > 0.
```

This is an analytic certificate that a nonzero frozen-strain oracle can
coexist with identically zero complete second variation. It falsifies the
specific inference used in the earlier square-energy candidate, not the
square-function route itself.

No claim is made that R(U+h v) vanishes to every order. No variable-weight
commutator estimate, all-band limit, signed spacetime estimate, or transfer
of this periodic construction to rapidly decreasing whole-space data is
established here. A variable or evolving square-function weight must be
evaluated in the full formula before inferring an obstruction or a gain.
