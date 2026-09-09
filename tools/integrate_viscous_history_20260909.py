#!/usr/bin/env python3
"""Apply the exact owner-authorized September 9 manuscript integration once.

This is a transport adapter for the text-only connector, not a mathematical
checker. It refuses any unexpected target blob and writes only four named
paths. Re-running on the exact output is a no-op. No network or credentials.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
PATCHES = json.loads(r'''{
  "PLAN.md": {
    "before": "c781b493da321e829c1c84ed5324d8e5fc8a23b2",
    "after": "67ac2f30c3f8e9bda7568f480eae133648ea1f1b",
    "replacements": [
      [
        "## 1. Rigid terminal equation and unchanged positive consumer",
        "## September 9 fixed-viscosity attack and immediate manuscript update\n\nInput: `1fc5f5b1f1e6cf2ca52ae4bdbd71c8d7b7a07352`. The manuscript now records\nthe forced/unforced/inviscid distinction in `paper/sections/viscous_history.tex`.\nThe follow-up source ledger is\n`literature/viscous-history-source-audit-2026-09-09.md`; it explicitly discloses\nserved-PDF pagination mismatch, inherited rather than newly recomputed hashes,\nand Palasek's prior-art preparation-time obstruction. No external theorem is\nsilently upgraded. The active mathematical task remains UE1: one autonomous\ncommon trace. First recompute the exact fixed-viscosity history and displacement\noperators, then test a genuinely coupled repair. A source audit is not a\nterminal advance; current theorem, audit and formal statuses remain unchanged.\n\n## 1. Rigid terminal equation and unchanged positive consumer"
      ]
    ]
  },
  "paper/Makefile": {
    "before": "393c6d65d9d5619cf5cab65a96e49199122e3907",
    "after": "a782cf2193e8537bb6bc8c146ca85ba4a39895c2",
    "replacements": [
      [
        "main.pdf: main.tex references.bib ",
        "main.pdf: main.tex references.bib sections/viscous_history.tex "
      ]
    ]
  },
  "paper/main.tex": {
    "before": "1edda67945aaa59892b7f7bc4648078482330f2e",
    "after": "526fa85f8c26a17655385ac1466572c7c782bdaf",
    "replacements": [
      [
        "unforced whole-space alternative \\cite{Fefferman2000}, which the Clay\nMathematics Institute lists as unsolved.",
        "unforced whole-space alternative \\cite{Fefferman2000}. The conditional\nargument here does not discharge that alternative; the distinction from\nrecent forced and inviscid results is recorded in\nSection~\\ref{vh:source-scope}."
      ],
      [
        "\\bibliographystyle{plain}",
        "\\input{sections/viscous_history}\n\n\\bibliographystyle{plain}"
      ]
    ]
  },
  "paper/references.bib": {
    "before": "cd8016b2c7e90fc3966169384c0d4557d120c2bf",
    "after": "c0d307eb6a9bdc3f2b7693e809e999fa6c69e280",
    "replacements": [
      [
        null,
        "\n\n@misc{OpenAINavier2026,\n  author = {{OpenAI}},\n  title = {Finite Time Blowup for {Navier--Stokes}},\n  year = {2026},\n  howpublished = {\\url{https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf}},\n  note = {Released September 8. Forced theorem; project acceptance and inherited kernel record are distinguished in the research ledger}\n}\n@misc{OpenAIEuler2026,\n  author = {{OpenAI}},\n  title = {Finite Time Blowup for the {Euler} Equation},\n  year = {2026},\n  howpublished = {\\url{https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf}},\n  note = {Released September 8. Source inspected September 9; no fixed-positive-viscosity implication is imported}\n}\n@misc{Palasek2026Obukhov,\n  author = {Stan Palasek},\n  title = {Finite-time blow-up in an elementary model of the {3D Navier--Stokes} equations},\n  year = {2026},\n  howpublished = {\\url{https://arxiv.org/abs/2605.13827}},\n  note = {Version 1, Theorems 1.3 and 1.8 and Section 1.3.2 inspected. Shell model, not an embedding into the original equation}\n}\n"
      ]
    ]
  }
}''')


def blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    ready = {}
    for rel, spec in PATCHES.items():
        data = (ROOT / rel).read_bytes()
        if blob(data) == spec["after"]:
            continue
        if blob(data) != spec["before"]:
            raise SystemExit("Concurrent target change; refusing overwrite: " + rel)
        text = data.decode("utf-8")
        for old, new in spec["replacements"]:
            if old is None:
                text += new
            else:
                if text.count(old) != 1:
                    raise SystemExit("Ambiguous literal replacement: " + rel)
                text = text.replace(old, new)
        output = text.encode("utf-8")
        if blob(output) != spec["after"]:
            raise SystemExit("Output fingerprint mismatch: " + rel)
        ready[rel] = output
    for rel, data in ready.items():
        (ROOT / rel).write_bytes(data)
        print(rel, blob(data))
    print("Exact manuscript integration:", len(ready), "changed paths")


if __name__ == "__main__":
    main()
