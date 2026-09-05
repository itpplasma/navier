#!/usr/bin/env python3
"""Document integrity checks only; this is not a mathematical verifier."""
from pathlib import Path
import sys
import yaml

root = Path(__file__).resolve().parents[1]
graph = yaml.safe_load((root / 'docs/proof-graph.yaml').read_text())
nodes = graph['nodes']
by_id = {n['id']: n for n in nodes}
assert len(by_id) == len(nodes), 'duplicate claim IDs'
assert graph['terminal_claim'] in by_id, 'missing terminal claim'
allowed = {'imported', 'paper', 'conditional', 'gap', 'no-go', 'machine_checked', 'novel'}
visiting, visited = set(), set()

def visit(key):
    assert key in by_id, f'unknown dependency {key}'
    assert key not in visiting, f'dependency cycle at {key}'
    if key in visited:
        return
    visiting.add(key)
    node = by_id[key]
    assert node['kind'] in allowed, f'unknown class {key}'
    for field in ('statement', 'mechanism', 'paper_label', 'review'):
        assert node[field], f'missing {field} in {key}'
    assert (root / node['evidence']).is_file(), f'missing evidence for {key}'
    for dep in node['depends_on']:
        visit(dep)
    visiting.remove(key)
    visited.add(key)

for key in by_id:
    visit(key)
paper = root.parent / 'navier-paper/main.tex'
assert paper.is_file(), 'missing manuscript'
text = paper.read_text()
for n in nodes:
    assert '\\label{' + n['paper_label'] + '}' in text, f'missing paper label {n["id"]}'
plan = (root / 'PLAN.md').read_text()
assert 'phase_i_status: authorized-2026-09-05-in-progress' in plan
assert 'checkpoint: CP1' in plan
assert graph['phase_i_status'] == 'authorized-2026-09-05-in-progress'
assert graph['phase_ii_status'] == 'authorized-2026-09-05-not-started'
formal = root.parent / 'navier-formal/lakefile.toml'
assert formal.is_file(), 'missing formal repository'
assert 'public_release: false' in plan
assert by_id['NS-R3']['kind'] == 'gap', 'terminal promotion needs a new mathematical audit'
print(f'PASS: {len(nodes)} claim records, acyclic dependencies, evidence and paper labels.')
print('Scope: structural integrity only; no mathematical correctness is certified.')
