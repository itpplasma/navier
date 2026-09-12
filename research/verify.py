#!/usr/bin/env python3
"""Document integrity only. Default mode checks research, the integrated paper and the formal manifest."""
from pathlib import Path
import argparse
import re
import yaml

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--research-only', action='store_true',
                    help='check research structure only; explicitly skip external repositories')
parser.add_argument('--paper-only', action='store_true',
                    help='check research and manuscript; skip the external formal manifest')
parser.add_argument('--paper', type=Path, default=root/'paper')
parser.add_argument('--formal', type=Path, default=root.parent/'navier-formal')
args = parser.parse_args()
if args.research_only and args.paper_only:
    parser.error('--research-only and --paper-only are mutually exclusive')
graph = yaml.safe_load((root/'docs/proof-graph.yaml').read_text())
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
    assert (root/node['evidence']).is_file(), f'missing evidence for {key}'
    for dep in node['depends_on']:
        visit(dep)
    visiting.remove(key)
    visited.add(key)

for key in by_id:
    visit(key)
plan = (root/'PLAN.md').read_text()
match = re.search(r'```yaml\s*\n(.*?)\n```', plan, re.S)
assert match, 'missing live plan YAML'
state = yaml.safe_load(match.group(1))
assert state['checkpoint'] == 'CP1'
assert state['terminal_claim'] == graph['terminal_claim'] == 'NS-R3'
assert state['terminal_status'] == 'not-proved'
assert state['unforced_counterexample'] == 'not-constructed'
assert state['complete_terminal_route'] == 'none-established'
assert state['public_release'] is True
# Formal phase strings remain canonical-graph metadata; the compact live PLAN
# now points to navier-formal instead of duplicating the archived phase block.
assert graph['phase_i_status'] == 'reopened-2026-09-06-in-progress'
assert graph['phase_ii_status'] == 'reopened-2026-09-06-target'
# PLAN metadata may also record the owner's partial identity draft (2b426ce).
# Neither value promotes canonical formal phases or the terminal claim.
assert state['formal_status'] in {
    'unchanged-see-navier-formal-and-archived-plan',
    'partial Hessian/Laplacian L2 identity drafted under explicit IBP data; paper-to-data bridge and critical producer remain open',
}, 'unrecognized live formal-status metadata'
assert by_id['NS-R3']['kind'] == 'gap', 'terminal promotion needs a new mathematical audit'
candidates = graph.get('candidate_supplements', [])
assert len({c['id'] for c in candidates}) == len(candidates), 'duplicate candidate IDs'
for c in candidates:
    assert c['id'] not in by_id, 'candidate silently promoted into main graph'
    assert c['status'] == 'author-checked-independent-audit-pending'
    assert (root/c['evidence']).is_file(), 'missing candidate evidence'
    assert c['paper_labels'], 'missing candidate labels'

if args.research_only:
    print(f'PASS (research-only): {len(nodes)} claim records, acyclic dependencies, evidence, status, {len(candidates)} pending supplements.')
    print('NOT CHECKED: manuscript labels/includes and formal repository manifest.')
else:
    paper_root = args.paper.resolve()
    seen = set()
    def read_tex(path):
        path = path.resolve()
        assert path.is_relative_to(paper_root), f'include outside manuscript: {path}'
        assert path not in seen, f'repeated or cyclic TeX include: {path}'
        assert path.is_file(), f'missing manuscript source: {path}'
        seen.add(path)
        raw = path.read_text()
        clean = re.sub(r'(?<!\\)%[^\n]*', '', raw)
        expanded = clean
        for name in re.findall(r'\\(?:input|include)\{([^}]+)\}', clean):
            # latexmk runs in paper_root; nested \input paths are relative
            # to that working directory, not to the including file.
            child = paper_root/name
            if not child.suffix:
                child = child.with_suffix('.tex')
            expanded += '\n'+read_tex(child)
        return expanded
    text = read_tex(paper_root/'main.tex')
    assert graph['manuscript_path'] == 'paper/main.tex'
    assert graph['proof_map_path'] == 'paper/proof_map.tex'
    for n in nodes:
        assert '\\label{'+n['paper_label']+'}' in text, f'missing paper label {n["id"]}'
    for c in candidates:
        for label in c['paper_labels']:
            assert text.count('\\label{'+label+'}') == 1, f'missing/duplicate candidate label {label}'
    if not args.paper_only:
        assert (args.formal/'lakefile.toml').is_file(), 'missing formal repository manifest'
    print(f'PASS: {len(nodes)} claim records, acyclic dependencies, evidence, status, manuscript labels across {len(seen)} TeX sources, {len(candidates)} pending supplements.')
    print('NOT CHECKED: formal manifest.' if args.paper_only else 'PASS: formal manifest.')
print('Scope: structural integrity only; no mathematical correctness, independent audit or Lean build is certified.')
