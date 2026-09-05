# Frozen audit of the pressure-gradient symbol note

**VERDICT: PASS.**  The universal angular bound, explicit rational
polarization, sharpness calculation, and reality normalization are correct.
No repair is required.

## Frozen input

* Repository base:
  `88c0b2e4e9cb1fce9eb58f8a0b2e2ea8caee13e9`.
* Candidate: `research/evidence/hf07-controller-symbol.md`.
* SHA-256:
  `758bf83a4f69fc317f0197ec0e6bb96404da30e6d409097042e226043aa2f4fc`.

## Verification

For \(k\cdot a=l\cdot b=0\) and \(Q=k+l\ne0\), the two ordered cross
products give

\[
 \widehat p_{k,l}(Q)
 =-2{(Q\cdot a)(Q\cdot b)\over|Q|^2}
 =-2{(l\cdot a)(k\cdot b)\over|Q|^2}.
\]

Therefore

\[
 |\widehat{\nabla p}_{k,l}(Q)|
 =2{|Q\cdot a||k\cdot b|\over|Q|}
 \leq2|k|\sin\alpha,|a||b|.
\]

Exchanging \((k,a)\) and \((l,b)\) proves

\[
 |\widehat{\nabla p}_{k,l}(Q)|
 \leq2\min(|k|,|l|)\sin\alpha,|a||b|.
\]

No comparable-frequency assumption is used.

For

\[
 k=(N,0,0),\quad l=(-N,m,0),\quad
 a=(0,1,0),\quad b=(m/N,1,0),
\]

one has \(k\cdot a=0\), \(l\cdot b=-m+m=0\),
\(Q=(0,m,0)\), and

\[
 l\cdot a=k\cdot b=m.
\]

Thus \(\widehat p_{k,l}(Q)=-2\) and the gradient coefficient has magnitude
\(2m\).  Moreover,

\[
 \sin\alpha={m\over\sqrt{N^2+m^2}},qquad
 |b|={\sqrt{N^2+m^2}\over N},qquad
 \min(|k|,|l|)=N,
\]

so the angular upper bound is attained exactly.  With fixed \(m\) and
\(N\to\infty\), a proposed extra factor \((|Q|/N)^\eta\), \(\eta>0\), would
make the right side smaller than the actual coefficient by a factor comparable
to \((N/m)^\eta\).  Hence no uniform superlinear output-frequency gain is
possible at symbol level.

Adding the conjugate modes creates the conjugate coefficient at \(-Q\) and
difference-frequency terms, without changing the coefficient at \(Q\).
If \(a,b\) are cosine amplitudes, their positive-frequency coefficients are
\(a/2,b/2\), so the quadratic \(Q\) coefficient is divided by four, exactly
as stated.

## Scope

The note proves sharpness only for the quadratic pressure-gradient symbol.
It does not construct a nonzero quartic pairing with \(Q_J(|u|u)\), a
finite-energy whole-space trajectory, or a counterexample to the signed
spacetime HF hypothesis.  No such extension is used in the candidate.
