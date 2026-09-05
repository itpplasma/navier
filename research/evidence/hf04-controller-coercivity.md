# Full heat inverse: a coercivity obstruction

Candidate for independent audit. This tests the concrete heat-normal-form
route, not every possible modified energy and not the universal HF claim.
Fix viscosity nu>0, a standard smooth scaled low-pass S_J, and write
H_J(u)=integral (p-S_J p) u dot grad |u|. Write P(u) for the full pressure
work and G_s=exp(nu s Delta). On solenoidal Schwartz fields define

\[
 B_J(u)=-\int_0^\infty H_J(G_su)\,ds,
 \qquad B(u)=-\int_0^\infty P(G_su)\,ds.
\]

These integrals are finite for each such field: near zero use smoothness
and the uniform estimate |H_J(v)|+|P(v)| <= C ||v||_6^3 ||grad v||_2;
at infinity the same estimate and heat smoothing give
C(nu s)^(-2)||u||_2^4. This is snapshot finiteness, not uniform control
along a possible singular trajectory.

The full heat inverse is not identically zero. Indeed,

\[
 B(G_tu)=-\int_t^\infty P(G_su)\,ds,
 \qquad \frac{d}{dt}B(G_tu)=P(G_tu).
\]

The audited compactly supported profile in hf02-r3-profile.md has P(u)>0.
Continuity therefore makes B(G_tu) nonconstant near zero. At least one
such heat-evolved Schwartz field phi has B(phi) nonzero. Changing phi to
-phi reverses B, since P(-v)=-P(v). Thus either sign is available.

For a>0, homogeneity and heat linearity give

\[
 B_J(a u)=a^4B_J(u),\qquad B(a u)=a^4B(u),
 \qquad \|a u\|_3^3=a^3\|u\|_3^3.
\]

Consequently the direct modified energy
F_J(u)=||u||_3^3/3-c B_J(u), with any fixed nonzero real c, need not
be positive at large amplitude. There is also an obstruction at *exactly
fixed kinetic energy*, which rules out repairing this coercivity solely
by adding a finite function of energy.

Fix E>0 and choose phi above so c B(phi)>0. Let
N=a^2||phi||_2^2/E and u_a(x)=a N phi(Nx), so ||u_a||_2^2=E exactly.
Spatial scaling and the change of heat time s -> N^2 s give

\[
 B_J(u_a)=a^4 B_{\kappa_a}(\phi),\qquad
 \kappa_a=2^J/N,
\]

where B_kappa denotes the same functional with low-pass symbol
m(xi/kappa). Thus kappa_a ->0. For each s>=0, this low-pass tends
strongly to zero in L^3 on the pressure of G_s phi. For example its L^3
norm is bounded by C kappa^(1/2) times the pressure's L^2 norm, by
Bernstein and L^2 multiplier boundedness. Hence H_kappa(G_s phi) tends
to P(G_s phi).

Dominated convergence applies to the heat-time integral: for s<=1 use
the smooth uniform norm bound of G_s phi, and for s>=1 use the integrable
C(nu s)^(-2)||phi||_2^4 bound, both independent of kappa. Therefore

\[
 B_J(u_a)=a^4(B(\phi)+o(1)),\qquad
 F_J(u_a)=\frac{a^3}{3}\|\phi\|_3^3
             -c a^4(B(\phi)+o(1))\longrightarrow-\infty.
\]

In particular no finite C(E,nu,J,c) makes F_J(u)>=-C on every solenoidal
Schwartz field with energy E, much less makes F_J control ||u||_3^3.
The same argument applies directly to the full-pressure heat inverse.

This identifies a second obstacle when trying to remove the short-heat
defect by starting the inverse at zero. Even where the inverse is defined,
the direct additive correction loses energy-only coercivity. A successful
repair would need a different functional, nonlinear saturation with all
new chain-rule terms controlled, or additional trajectory information.
No statement here excludes these possibilities, proves PDE blowup, or
refutes HF with a remainder depending on the entire initial datum.
