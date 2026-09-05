# History signing checkpoint, 2026-09-05

At the owner’s request, the original main history was recreated with SSH
signatures using the GitHub-registered Ed25519 key with fingerprint
`SHA256:ARNu2jnP8I1sJSIRgpYCbp5/cwEB8FqKnMf0gYdIy5U`.
Original trees, messages, author identities and author dates were preserved.
Committer identity is Christopher Albert <albert@tugraz.at>; committer dates
record the actual re-signing time. These signatures do not establish an
original historical signing time or public disclosure date.

`2026-09-05-map.json` maps original commit IDs to their signed replacements.
Existing evidence citations retain the original IDs: resolve them with this
map; the corresponding source tree is unchanged. Original Git bundles are
retained locally outside the repositories in
`/home/ert/proj/.history-signing/20260905-102900/`.

Overleaf rejected history replacement (forced pushes are prohibited).
Its manuscript source tree still matches the rewritten manuscript head at
this checkpoint; its original history remains unsigned. GitHub main carries
the signed replacement history. Future synchronization must preserve these
separate ancestries, transferring source changes rather than merging the
unsigned Overleaf ancestry into GitHub main.
