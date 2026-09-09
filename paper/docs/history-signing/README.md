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

Overleaf initially rejected history replacement because forced pushes are
prohibited. The owner subsequently requested GitHub-only work. The Navier
project `6a9bb675ea9d4d0d368d8ee6` was deleted on 2026-09-05 after its sources
were verified identical to GitHub; the project-list comparison showed only
that project removed. Its final history is preserved locally in
`/home/ert/proj/.history-signing/20260905-102900/before-overleaf-delete.bundle`.
There is no Overleaf synchronization workflow or remote now.

Global Git signing defaults are managed in chezmoi, with the public key at
`~/.config/git/signing.pub` and verification allowlist at
`~/.config/git/allowed_signers`. The private key remains in its existing agent.
