# Pressure-gradient symbol: exact angular bound and sharp example

Controller addition to the audited HF06 symbol calculation. These are
Fourier-symbol statements, not a signed pressure-work or trajectory theorem.

For k dot a=l dot b=0 and Q=k+l nonzero, the two ordered cross terms give
p_cross(Q)=-2(l dot a)(k dot b)/|Q|^2. Consequently

\[
 |\widehat{\nabla p}_{k,l}(Q)|
 \le 2\min(|k|,|l|)\sin\alpha\,|a|\,|b|,
\]

where alpha is the angle between k and l. Bound Q dot a by |Q||a| and
k dot b by |k| sin(alpha)|b|, then interchange the two inputs. This needs
no comparable-frequency hypothesis. It is an upper bound, not a claim
that every polarization attains it.

There is a family attaining the relevant order. For positive integers N,m,
choose

\[
 k=(N,0,0),\quad l=(-N,m,0),\quad
 a=(0,1,0),\quad b=(m/N,1,0).
\]

Both divergence constraints hold exactly. The output is Q=(0,m,0), and
l dot a=k dot b=m. Thus p_cross=-2 and the gradient coefficient has
magnitude 2m. Meanwhile |a||b|=sqrt(1+(m/N)^2) and the input scale is
comparable to N. Taking m fixed and N tending to infinity proves that a
uniform bound of the form

\[
 |\widehat{\nabla p}_{k,l}(Q)|
 \le C N (|Q|/N)^{1+\eta}|a||b|,\qquad \eta>0,
\]

cannot hold for all these modes: the ratio of the left side to the right
side without C tends to infinity as (N/m)^eta. In fact the displayed
angular gradient bound is attained by this polarization. For any fixed
output cutoff J, m can first be chosen above its low-pass support, then
held fixed while N increases.

Reality is obtained by adding conjugate modes. They add conjugate and
difference outputs but do not change the coefficient at Q for this pair.
If a,b denote real cosine amplitudes rather than positive-frequency
coefficients, the Q coefficient is divided by four; the conclusion is
unchanged. This finite periodic Fourier example proves symbol sharpness
only. It is not a finite-energy R3 solution, a lower bound for the full
quartic pressure-work pairing, or a counterexample to HF.
