# Audit record for actual helical-production tests

Date: 2026-09-07. Frozen base ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df.
Actual fresh-context adversarial review by audit_helical, followed by
rechecking the requested packet repair and its affected consumers.

## Verdict and exact scope

SCOPED PASS after repair. The reflection-symmetric compact-data construction
has positive growth of both chiral energies while every radial signed
helicity history vanishes. The pure-positive Schwartz construction creates
minority energy at order t squared. These exclude only the stated closures
from signed budgets alone and homogeneous minority-energy control. They
supply no global bound, singularity exclusion or counterexample to NS-R3.
An additional nonzero full-input creation cost remains possible.

The original proof SHA256 was
`d2766af8ceb9546495b07844645bf0033e4ebc4fd3d8aacae32bdec8c18a9a33`.
Section 3 passed; Section 4 needed an explicit Leray projection before
applying the chiral projector to constant-polarization Fourier bumps.
The repaired proof uses Q_+=(P+i xi cross/|xi|)/2 and explicit conjugate
partners, so reality, solenoidality and pure chirality hold on every packet.
The reviewer checked the positive convolution coefficient and the resulting
actual short-time minority-energy expansion after this repair.

Final reviewed proof SHA256:
`0742b7bae5544475306a6cffed1eb89c2d57481e0fe9228718d702333ee99fdf`.
Exact new-file patch SHA256:
`d7dec0e82df2359f143a9ddd8b085b3602d5a2f31e214c56c2a8fcd4f32209b7`.
The tracked proof is exactly this final review input. The patch was generated
by git diff --no-index against /dev/null. The original and repair reports
below are retained verbatim, with separate digests.

## Original independent review

Report SHA256 `546172615e818bf75982ed0166dbcbd059515802186bd526f0086f36d5a5bc42`.

# Independent adversarial audit: helical pair production

Date: 2026-09-07. Reviewer: fresh-context frontier agent assigned by the
controller; this is mathematical review evidence, not canonical promotion.

Frozen input: `.git/navier-wave-20260907/helical-production.md`.
Declared base: `ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.
SHA256, independently verified before review:
`d2766af8ceb9546495b07844645bf0033e4ebc4fd3d8aacae32bdec8c18a9a33`.
The reviewer read PLAN and this packet only. No external source theorem was
introduced, no other evidence file was edited, and no claim was promoted.

## Verdict and first invalid bridge

Section 3 PASSES as a scoped actual-R3 counterexample: for each fixed
viscosity, admissible compact smooth solenoidal data have an actual local
interval of increasing chiral energies while every finite radial signed
helicity pairing vanishes throughout that interval.

Section 4 needs one explicit repair to its Fourier-packet prescription.
The packet defines `P_+=(I+C)/2` only on solenoidal fields. Constant
polarizations U and V are transverse at their central carriers but are not
transverse at all nearby packet frequencies. Applying this displayed
operator directly to these vector-valued bumps does not make them
solenoidal and does not remove their entire negative/chirality-zero
component. This is the first literal missing bridge; it is not a defect
in the interaction coefficient or a barrier to the construction.

Use the genuine full-space helical symbol

    Q_+(xi) = [P(xi) + i xi cross / |xi|]/2
            = P_+(xi) P(xi),  xi != 0.

With this explicit repair, the proof of minority birth and the resulting
exclusion of an integrable homogeneous minority-energy Gronwall inequality
PASS. The repaired packet argument is given below. If the author's phrase
"apply P_+" was intended to mean this conventional full-space helical
projection, the change is clarification of an implicit Leray step.

These results exclude precisely the specified vanishing-cost signed-budget
closure and homogeneous minority-energy closure. They establish no
arbitrary-data critical estimate, singularity, global chiral growth rate,
or obstruction to a separate nonzero full-input production bound.

## Checks on the exact balances and compact construction

1. On the solenoidal subspace, `C` is self-adjoint and `C^2=I`.
   Thus the orthogonal chiral decomposition and all factors of two in
   Section 2 are correct. In particular `curl u=Lambda(u_+-u_-)`, and
   the convection identity gives

       T_+-T_- = -<curl u,B(u,u)> = 0.

   Consequently `S'=-nu(D_++D_-)+2T` and
   `H'=-2nu(D_+-D_-)`. No sign condition on their common producer follows.

2. The orientation-reversing action is correctly the polar action
   `Ru(x)=R u(Rx)`. It is unitary, commutes with radial Fourier
   multipliers, and anticommutes with curl. For a reflection-fixed field,
   applying this unitary action to the radial signed pairing changes its
   sign. Hence the pairing is zero whenever defined. Local classical
   uniqueness preserves reflection symmetry for NS, including the pressure.
   This does not assume that the third velocity component stays zero.

3. I recalculated the full trigonometric convection independently. Writing
   `s=sin x`, `r=sin(2y)` and `q=sin(x+2y)`, its vorticity production is

       -U.grad omega = 6 A B s r - 2 B C0 r q + 8 A C0 s q.

   Product-to-sum yields the three displayed carrier derivatives
   `dot A=-B C0`, `dot B=A C0`, `dot C0=-3 A B/5`.
   Pairing all convection with `Lambda U` therefore gives exactly
   `(7-3 sqrt(5)) A B C0/2`. The omitted output carriers are orthogonal
   to this particular initial pairing, not absent from the vector field.
   The sign is strictly positive because `49>45`. The energy and
   enstrophy cancellations are consistent independent checks.

4. The curl cutoff is genuinely three-dimensional, compactly supported,
   smooth, and solenoidal. Its first two components are even in z and its
   third component initially vanishes. With
   `e_L=u_L-theta_L U`, direct product differentiation gives

       ||e_L||_(H1) = O(L^(1/2)),
       ||(u_L.grad)u_L-theta_L^2(U.grad)U||_2 = O(L^(1/2)).

   The possibly nonlocal `Lambda` term causes no unaccounted tail.
   For each fixed nonzero carrier, the stronger estimate

       ||Lambda(theta_L exp(i k.x))
                 -|k| theta_L exp(i k.x)||_2
           <= L^(1/2) ||grad theta||_2

   follows directly from `||k+eta/L|-|k||<=|eta|/L` and Plancherel
   (with the corresponding common Fourier normalization). Together with
   `||Lambda e_L||_2=O(L^(1/2))`, this controls the full-space multiplier,
   not just its value inside the support.

   Both leading factors have L2 size O(L^(3/2)), so all pairing errors
   are O(L^2), hence vanish after division by L^3. Leray can be removed
   because `Lambda u_L` is solenoidal. The leading expression is the
   integral of `theta_L^3` times a finite trigonometric polynomial.
   Its nonzero Fourier modes vanish after rescaling by the
   Riemann-Lebesgue lemma; its constant mode is the normalized torus
   average computed above. This proves (3.5) with its stated constant.

5. For one sufficiently large finite L, write `n=Ncrit(u_L)>0` and
   `d=||Lambda^(3/2)u_L||_2^2`. Then for `u0=M u_L`,

       S'(0)=M^3 n-nu M^2 d > 0  whenever  M>nu d/n.

   Every parameter is finite for each fixed viscosity. Local existence
   is sufficient; no uniform lifespan in M or L is used. Reflection
   gives `E_+=E_-=S/2`, and continuity of the derivative gives the
   claimed positive interval. In particular `T>0` there as well.
   Its integrated positive production is positive although every signed
   radial datum, history, and signed dissipative pairing is zero.

## Exact repair of the pure-helicity packet construction

Choose a real, even, nonnegative, nonzero function
`phi in C_c^infinity(B(0,1))`. Put `phi_rho(eta)=phi(eta/rho)` and define

    d_hat_rho(xi) = Q_+(xi) [
        phi_rho(xi-a) U + phi_rho(xi-b) V
      + phi_rho(xi+a) conjugate(U)
      + phi_rho(xi+b) conjugate(V) ].

Take rho positive and sufficiently small that these four supports avoid
zero and are disjoint. This Fourier transform is smooth and compactly
supported, so its inverse transform is Schwartz. Since
`Q_+(-xi)=conjugate(Q_+(xi))`, it has the correct conjugacy for a real
velocity. Also `P Q_+=Q_+` and `C Q_+=Q_+`; it is exactly solenoidal and
exactly pure positive helicity. At the central carriers `Q_+(a)U=U`
and `Q_+(b)V=V`.

At `k=a+b`, only the two ordered positive-parent neighborhoods contribute
for sufficiently small rho. There is a positive Fourier-convention
constant c such that

    B(d_rho,d_rho)_hat(k) /
         [c rho^3 integral phi(eta)^2 d eta]  -> F.

This is direct dominated convergence after `xi=a+rho eta` in one order
and `xi=b+rho eta` in the other. All relevant symbols are smooth near
the nonzero parent and daughter carriers. Their limiting polarizations
are U and V, so the limiting coefficient is the stated full Leray one.

Independently, `(U.b)V+(V.a)U=(2i,i,1)` and application of `i P_k`
gives `F=(-6/5,3/5,i)`. The exact quadratic identities are

    |F|^2 = 14/5,
    <F,i k cross F> = 6,
    |Q_-(k)F|^2 = 7/5-3/sqrt(5)
                = (7-3 sqrt(5))/5 > 0.

Therefore `Q_- B(d_rho,d_rho)` is nonzero for some finite, sufficiently
small rho. Nonzero Fourier value at k gives nonzero norm, since the
Fourier expression is continuous on a neighborhood of k. Extra generated
frequencies cannot cancel this output: the remaining parent sums lie
away from k. This proves the required actual-data assertion (4.2).

For the local smooth NS solution, local high Sobolev regularity supplies
strong differentiability in `dot H^(1/2)`. The heat term preserves the
initial chirality, so, with `g=Q_-B(d_rho,d_rho)`,

    u_-(t)=-t g+o_(dot H^(1/2))(t),
    E_-(t)=t^2 ||Lambda^(1/2)g||_2^2/2+o(t^2).

The coefficient is finite and strictly positive. This proves quadratic
birth; `E_-'(0)=0`, not a positive initial energy derivative. It directly
contradicts an inequality `E_-'<=a(t)E_-` with locally integrable `|a|`
and zero initial minority energy, by the ordinary integral Gronwall
argument. An additive source remains a legitimate possibility.

## Scope and review status

The argument accepts exact local NS existence/uniqueness, the classical
energy/helicity identities, and Fourier analysis as assigned inputs.
I did not independently audit the full endpoint continuation theorem
mentioned as a surviving conditional consumer. Nothing here supplies
its missing finite-horizon critical bound.

As an auxiliary arithmetic check, I evaluated the full real-space
trigonometric convection on a 64 by 64 grid, retaining every generated
mode in the product. It gave `0.14589803375031624`, versus
`(7-3 sqrt(5))/2 = 0.1458980337503153`. An independent vector calculation
gave negative daughter squared norm `0.05835921350012626`, versus
`(7-3 sqrt(5))/5 = 0.058359213500126114`. The analytic computations above,
not these finite numerical checks, carry the proof.

Author proof: frozen candidate with the stated explicit packet repair
required. Independent mathematical review: Section 3 accepted; Section 4
accepted after that repair. Source inspection: no new external theorem
used. Formal verification: none. Canonical promotion: controller-owned,
not performed. The full nonlinear input-dependent producer remains open.

## Repair recheck

Report SHA256 `0148d061ae7890a676cdf5aad8cae6a1a3ae7b1830030320112c522664894a08`.

# Independent recheck: explicit helical-packet repair

Date: 2026-09-07. This continues the fresh-context mathematical audit in
`.git/navier-wave-20260907/audit-helical.md`; it is not canonical promotion.

Repaired frozen input:
`research/evidence/2026-09-07-helical-production.md`.
Base: `ec2ed88c8d1fdf3b66b0e989827d44d93f1f76df`.
Verified file SHA256:
`0742b7bae5544475306a6cffed1eb89c2d57481e0fe9228718d702333ee99fdf`.
Verified patch: `.git/navier-wave-20260907/helical-final.patch`, SHA256
`d7dec0e82df2359f143a9ddd8b085b3602d5a2f31e214c56c2a8fcd4f32209b7`.

VERDICT: SCOPED PASS. The explicit repair closes the only gap identified
in the original packet. The accepted claims are the reflection-symmetric
compact-data signed-budget counterexample and actual pure-positive
Schwartz-data generation of negative chirality, with exactly the scoped
closure exclusions stated in the repaired evidence.

I compared the repaired file against the original frozen packet. Only the
review metadata and the intended Section 4 packet paragraph changed. The
Section 3 proof accepted by the initial audit remains unchanged.

The replacement symbol

    Q_+(xi)=[P(xi)+i xi cross/|xi|]/2=P_+(xi)P(xi)

is the correct orthogonal positive-helicity projector on arbitrary vector
Fourier amplitudes. Thus the displayed packet now has exact solenoidality
and exact positive chirality throughout its support, not merely at the
carrier centers. Its four supports can be kept away from zero. Smooth
compact Fourier support gives Schwartz data, and the even real bump with
explicit conjugate polarizations gives
`u0_hat(-xi)=conjugate(u0_hat(xi))`, hence a real velocity.

For sufficiently small delta, the output carrier `k=a+b` receives only
the two ordered positive-parent interactions. After writing one parent
frequency as `a+eta` or `b+eta`, their weights at k are
`phi_delta(eta) phi_delta(-eta)=phi_delta(eta)^2`. The normalized coefficient
is therefore a positively weighted average of a smooth vector coefficient
which converges uniformly on `|eta|<=delta` to F. Its error is bounded
by `C delta`, independently of the bump's amplitude or shape. This
justifies the limit for the stated family of bumps without an additional
fixed-profile assumption. An overall fixed positive Fourier-convention
factor is irrelevant, or is included in the convolution normalization.

The already checked strict inequality

    |Q_-(k)F|^2=(7-3 sqrt(5))/5>0

then persists for some finite sufficiently small delta. Continuity near k
gives a nonzero negative-helicity nonlinear term in `dot H^(1/2)`.
The local classical branch is differentiable in that space, and its
initial heat term has zero negative projection. Hence

    u_-(t)=-t P_-B(u0,u0)+o_(dot H^(1/2))(t),
    E_-(t)=t^2 ||Lambda^(1/2)P_-B(u0,u0)||_2^2/2+o(t^2).

The coefficient is strictly positive, while `E_-'(0)=0`. The revised
text correctly relies on quadratic birth rather than a positive initial
minority-energy derivative. This contradicts the specified homogeneous
Gronwall closure with integrable coefficient and zero initial minority
energy. The repair does not change that conclusion or require viscosity
uniformity, a uniform local lifespan, or a periodic trajectory.

No remaining mathematical defect was found in the two scoped constructions
within the assigned inputs. This audit does not establish or independently
reaudit the full endpoint continuation theorem, and does not exclude
additive full-input costs, more detailed unsigned/angular information,
or additional dynamical constraints. A nonlinear bound for common chiral
production remains open. Source inspection: no new external theorem used.
Formal verification: none. Canonical promotion: not performed.

## Reproducible repair delta

Reversing this complete delta reconstructs the frozen original author
candidate from the final reviewed proof.

This is a zero-context unified delta (apply with `--unidiff-zero`).

```diff
--- original-helical-candidate
+++ repaired-helical-proof
@@ -5 +5,3 @@
-Worker evidence only. Author derivations; independent audit pending.
+Author derivations with an audit-requested solenoidal-packet repair.
+Exact review inputs and current verdict are recorded in
+2026-09-07-helical-production-audit.md.
@@ -220,6 +222,19 @@
-For actual R3 data, put smooth nonnegative small Fourier packets around
-a and b and their conjugate partners -a and -b, and apply P_+(xi) to every
-packet. Their supports avoid zero. The resulting u0 is real, solenoidal,
-Schwartz, and exactly satisfies P_-u0=0. Near k only the two positive
-parent packets contribute to the named daughter; the normalized convolution
-coefficient tends to F as packet width tends to zero. Continuity of the
+For actual R3 data the projection must first enforce solenoidality away
+from the carrier centers. For xi!=0 define
+
+    Q_+(xi)=(P(xi)+i xi cross/|xi|)/2=P_+(xi)P(xi).
+
+Choose a real nonzero nonnegative even bump phi_delta in C_c^infinity, supported
+in a sufficiently small radius-delta ball, and put
+
+    u0_hat(xi)=Q_+(xi)[U phi_delta(xi-a)+V phi_delta(xi-b)
+                +conjugate(U) phi_delta(xi+a)
+                +conjugate(V) phi_delta(xi+b)].
+
+The supports avoid zero; Q_+(-xi)=conjugate(Q_+(xi)) gives reality, and
+xi.Q_+(xi)=0 gives exact solenoidality. Smooth compact Fourier support
+gives Schwartz data, with P_-u0=0. Applying (I+C)/2 directly to arbitrary
+constant-polarization bumps would not ensure solenoidality and is not used.
+Near k only the two positive parent packets contribute to the named
+daughter. At k their convolution divided by the positive integral
+of phi_delta squared tends to F as delta tends to zero. Continuity of the
```
