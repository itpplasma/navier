# Audit of the fixed-energy instantaneous obstruction

VERDICT: **PASS**

REVIEWED SCOPE: research/evidence/hf03-fixed-energy-obstruction.md at verified
SHA-256 ae38c4335b9e5feca995070d1c99f0f21c8bd8db7da51c18d88995c9948d8c69,
on repository base 43a11d4715d7e09f07439accfba6af7f9bac6c18. The
positive compactly supported divergence-free profile is supplied by the
independently passed audit in hf02-review-profile.md.

FIRST BAD BRIDGE: none.

EVIDENCE: Fix \(E,\nu>0\), integer \(J\), and finite \(\theta\ge0\).
For the audited profile \(\phi\) with \(P_3[\phi]>0\), choose
\[
 a>\frac{\theta\nu D_3(\phi)}{P_3[\phi]}.
\]
Then \(c_*=a^4P_3[\phi]-\theta\nu a^3D_3(\phi)>0\). The
packet \(w_N=aN\phi(N\cdot)\) has
\[
 \|w_N\|_2^2=a^2\|\phi\|_2^2N^{-1},\quad
 P_3[w_N]=a^4N^2P_3[\phi],\quad
 D_3(w_N)=a^3N^2D_3(\phi).
\]

A fixed solenoidal reservoir \(\psi\), supported a positive distance from
the origin, and
\[
 b_N^2=\frac{E-a^2\|\phi\|_2^2/N}{\|\psi\|_2^2}
\]
give \(u_N=w_N+b_N\psi\) with exactly \(\|u_N\|_2^2=E\) for all
sufficiently large \(N\). The supports are disjoint, so the pressure source
has no cross tensor and \(D_3\) is exactly additive.

Pressure remains nonlocal, but the two cross pairings are lower order. On
the reservoir support, the double-Riesz kernel is evaluated a fixed distance
from the packet source, so
\(\|p[w_N]\|_\infty=O(\|w_N\|_2^2)=O(N^{-1})\).
In the reverse direction, \(p[b_N\psi]\) has uniformly bounded gradient on
the shrinking packet neighborhood, and integration by parts against
\(\operatorname{div}(|w_N|w_N)\) gives another
\(O(\|w_N\|_2^2)=O(N^{-1})\) term. The distributional local part of the
Riesz kernel cannot contribute across disjoint supports. Hence
\[
 P_3[u_N]=a^4N^2P_3[\phi]+O(1),
 \qquad
 D_3(u_N)=a^3N^2D_3(\phi)+O(1).
\]

The fixed low-pass kernel estimate
\[
 |L_J(u)|\le C2^{3J}\|u\|_2^3\|\nabla u\|_2
\]
applied at exact energy \(E\), together with
\(\|\nabla u_N\|_2=O(N^{1/2})\), yields
\(|L_J(u_N)|=O(N^{1/2})=o(N^2)\). Therefore
\[
 H_J(u_N)-\theta\nu D_3(u_N)
   =c_*N^2+O(N^{1/2})+O(1)\longrightarrow+\infty.
\]
All constants may depend on the fixed displayed parameters and profiles but
not on \(N\), exactly as required by the supremum claim.

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: Every fixed-cutoff instantaneous estimate
with remainder depending only on \(E,\nu,J,\theta\) is impossible, even for
compactly supported smooth solenoidal snapshots of exactly prescribed
positive energy.

UNNECESSARY DEPENDENCIES: No Navier--Stokes evolution, local existence,
continuation criterion, or high Sobolev estimate is used.

NON-CLAIMS: The sequence consists of different snapshots with unbounded
higher norms. It is not one solution trajectory and gives no refutation of
the signed time-integrated HF hypothesis, no singularity construction, and
no evidence of finite-time blowup.

REOPENING CONDITION: none for the stated static theorem. Any extension to a
spacetime no-go result requires trajectory control over the packet's
viscous \(N^{-2}\) time scale.
