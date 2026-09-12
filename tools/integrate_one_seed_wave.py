from pathlib import Path

p=Path('research/evidence/2026-09-12-source-pump-half-grade-parity.md')
s=p.read_text().replace('The source pump therefore gives an elliptic exchange contribution rather than an additional two-mode hyperbolic instability. The ordinary positive source-reference diagonal rates remain separate.', 'This projected pair contribution is elliptic. It is not a stability theorem for the full linearized system: both polarizations and the infinite chains of pump-shifted axial grades must also be retained. The ordinary source-reference rates remain separate.')
s=s.replace('For a fixed real pump phase, the two-mode system in variables `(x_a,conj x_b)` has off-diagonal product proportional to', 'For a fixed real pump phase, the projected 2-by-2 submatrix in variables `(x_a,conj x_b)` has off-diagonal product proportional to')
s=s.replace('Consequently, in the correction equation linearized about the old daughter pump alone, a pair initialized identically zero stays identically zero even if the other two pairs are nonzero.', 'The six half-grade modes do not form a closed linearization: pump shifts also create other axial grades. The invariant linear classes are instead the additive charge n=(2x-z)/3 in integer keys k=(x/20,0,z/2). With reality the displayed pairs occupy |n|=9,3,1, respectively. An entire charge class initialized zero stays zero under the single-pump linearization; each class includes all of its pump-shifted sidebands. See the complete-chain correction in 2026-09-12-one-seed-ladder-balance.md.')
s=s.replace('Thus this specific source-background mechanism can reduce six independent inputs to at most one seed per complementary pair, but it cannot eliminate odd-grade seeding altogether.', 'Thus one seed confined to one charge class cannot linearly reach the other two classes. Nonzero projected pair transfer does not assert independent endpoint controllability within a class, and the source cannot eliminate odd-grade seeding altogether.')
p.write_text(s)
p=Path('research/check_source_pump_half_grade_parity.py')
s=p.read_text().replace('# itself is elliptic rather than an additional two-mode hyperbolic instability.', '# has an elliptic projected contribution, not a full-chain stability theorem.')
s=s.replace('# Linearized about this single pump, the three complementary pairs are block\n# diagonal.  An entirely zero pair stays zero even when the other two pairs are\n# nonzero.  Thus this specific parametric mechanism needs at least one odd seed\n# in each complementary pair; full nonlinear cross-pair generation is a\n# separate mechanism and is not excluded here.', '# The displayed half-grade projection has three complementary pairs, but the\n# full linearization also contains all pump shifts and both polarizations.\n# Exact invariant charge n=(2*x-z)/3, not a two-mode truncation, separates the\n# three reality-complete classes |n|=9,3,1. Nonlinear cross-class generation\n# remains a separate mechanism.')
s=s.replace("print('The old daughter pump transfers a nonzero seed within exactly three complementary pairs but does not create the first odd seed.')", "assert sorted({abs((2*x-1)//3) for x in ancestors})==[1,3,9]\nprint('The six half-grade projected transfers lie in three independent charge classes; full pump chains are not two-mode blocks.')")
p.write_text(s)
p=Path('PLAN.md'); s=p.read_text()
assert 'source_one_seed_ladder:' not in s
s=s.replace('source_pump_half_grade_parity: even-source-cannot-zero-seed-odd-half-grade-sector', 'source_pump_half_grade_parity: even-source-cannot-zero-seed-odd-half-grade-sector\nsource_one_seed_ladder: exact-shortest-time-birth-survives-but-small-seed-free-bridge-composition-fails')
a=s.index('The surviving nonlinear repair is now sharper.')
b=s.index('\n## 9. UE2--UE4 after UE1',a)
s=s[:a]+'''The full one-odd-seed ladder has now been tested, not merely a selected shear
path. With seed `h=(1/10,0,1/2)` and pump `d=(1/20,0,1)`, every output key
`(x/20,0,z/2)` has additive seed charge `n=(2x-z)/3`. Full convolution and
arbitrary pump insertions preserve this bookkeeping. Exact rational
shortest-time recurrences prove that all six half-grade ancestors occur, at
seed degrees `1,1,3,3,9,9`. The complete next-parent quartet has seed degrees
`6,6,2,2`, and at any fixed sufficiently short positive horizon its outer/inner
pair-product ratio is `O(|A|^8)`, with nonzero leading coefficients. It therefore
cannot satisfy the existing consumer's fixed nonzero pair-product ratio as one
seed tends to zero. Nonzero ladder outputs do not inherit the six-independent-
input rank-four controls. See
`research/evidence/2026-09-12-one-seed-ladder-balance.md`.

The same wave corrects the single-pump two-mode wording: pump shifts produce
infinite axial-grade chains and both polarizations. The six displayed transfers
are projected coefficients, not closed blocks. Linear invariance separates
charge classes `|n|=1,3,9`; their full spectra remain to be analyzed.

The next distinct attack is the **full pump-coupled linear chain**, including
both source branches: determine whether the projected negative coefficient
products hid an actual parametric instability capable of changing the
small-seed amplitude balance. Even a positive answer needs nonlinear saturation,
independent charge-class supply or a new all-returned-state consumer, and a
physical one-trace adapter. Further shortest-time ladder refinement is not the
active task. The nonprincipal localized full-history adjoint remains distinct.
UE1 and NS-R3 remain open.
''' + s[b:]
s=s.replace('A full checkout is required for `python3 research/game/run.py fast`,\n`python3 research/verify.py --research-only`, paper checks and `git diff --check`.\nWhen only the connected GitHub interface is available, verify authoritative blob\nhashes and baseline controls there and state explicitly that this is not a local\nrepository-wide verifier run.', 'Use the directly relevant retained exact checkers,\n`python3 research/verify.py --research-only`, applicable paper checks and\n`git diff --check`. The generic game layer was removed by the current contract;\ndo not recreate it. Report archive-based, remote-CI, structural and mathematical\nverification scopes separately.')
p.write_text(s)
