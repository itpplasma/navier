# Bounded audit of the manuscript HF equivalence paragraph

VERDICT: **PASS**

REVIEWED SCOPE: The paragraph added at main.tex lines 323--335, frozen at
base commit 95cbf22885bb374cf83b6f485db97ce292e623f8 with patch SHA-256
a1cf68464af15d6e597dbdbeaeeccef8f4ac6a35291f0f7663867ccb7da5da43.
Both hashes were reproduced exactly.

FIRST BAD BRIDGE: none.

EVIDENCE: The signed high-frequency-tail hypothesis first chooses one universal
\(\theta\in[0,1)\), then for every \(\nu,u_0,H\) permits existential
\(J\) and \(A_{\rm high}\). Under global continuation of every maximal
strong branch, choosing the same universal value \(\theta=0\) and \(J=0\)
is valid. For fixed data and finite \(H\), persistence of the global
Schwartz-data strong branch gives bounded strong Sobolev norms on
\([0,H]\). The multiplier and Calderón--Zygmund estimate
\[
 |Q_0(t)|\le C\|u(t)\|_6^3\|\nabla u(t)\|_2
\]
is therefore integrable there, so
\[
 A_{\rm high}(\nu,u_0,H,0)=\int_0^H|Q_0(t)|\,dt<\infty
\]
is a legitimate existential witness and works simultaneously for every
\(\tau<H\). Uniqueness makes the selected maximal strong branch a function
of the input. The already audited forward implication gives the converse
direction.

The paragraph does not claim an explicit recipe in named initial norms.
Indeed, its reverse witness is obtained only after assuming global
continuation, and the text says this supplies no proof method. It also
restricts the equivalence to the maximal strong branch selected by local
theory and disclaims a converse involving arbitrary smooth finite-energy
solutions.

REPLACEMENT ARGUMENT: none.

CONDITIONAL SUFFIX THAT SURVIVES: At these purely existential quantifiers,
HF and global continuation of the selected strong branch are equivalent.
Strict \(\theta<1\) adds a weighted-dissipation conclusion in the forward
calculation but does not make the existential assertion logically stronger.

UNNECESSARY DEPENDENCIES: Bounded high Sobolev norms are more than the reverse
argument needs; finite-interval integrability of the displayed absolute
pressure bound suffices.

NON-CLAIMS: The equivalence proves neither HF nor global continuation and
supplies no quantitative a priori remainder.

REOPENING CONDITION: none for this bounded paragraph.
