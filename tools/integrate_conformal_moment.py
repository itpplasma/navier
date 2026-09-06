#!/usr/bin/env python3
"""Apply the frozen source edits mechanically; never promote mathematical claims."""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true', help='fail instead of writing any pending integration')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
payload = json.loads((root/'tools/conformal_integration.json').read_text())
allowed = {'main.tex','references.bib','Makefile','README.md','PLAN.md',
           'docs/proof.md','docs/proof-graph.yaml','proof_map.tex'}
expected = '54a6cdfb7d4173550141027d3dd5d3205115a43d37bab484d818d7275a0dca5c'
component = root/'sections/conformal_moment.tex'
if component.exists():
    assert hashlib.sha256(component.read_bytes()).hexdigest() == expected, 'frozen proof source changed: review integration first'
changes = {}
for relative, operations in payload['files'].items():
    assert relative in allowed, f'unexpected integration path: {relative}'
    path = root/relative
    original = path.read_text()
    text = original
    guard = payload.get('guards', {}).get(relative)
    if guard:
        current = hashlib.sha256(original.encode()).hexdigest()
        if current == guard['target']:
            continue
        assert current == guard['base'], f'concurrent map edits in {relative}; regenerate from authoritative research graph'
    for item in operations:
        old, new = item['old'], item['new']
        assert old and new, 'empty integration anchor'
        if text.count(new) == 1:
            continue
        assert text.count(old) == 1, f'missing or ambiguous source anchor in {relative}: {old[:80]!r}'
        text = text.replace(old, new, 1)
    if guard:
        assert hashlib.sha256(text.encode()).hexdigest() == guard['target'], 'generated map digest mismatch'
    if text != original:
        changes[path] = text
if args.check:
    assert not changes, 'integration pending: '+', '.join(str(p.relative_to(root)) for p in changes)
else:
    # Validate every anchor before changing any existing source.
    for path, text in changes.items():
        path.write_text(text)
print('PASS: conformal/moment source integration; '+str(len(changes))+' changed files.')
print('Mechanical integration only. Independent mathematical audit remains pending.')
