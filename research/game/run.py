#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from core import load_json,stale_sources,replay,first_disagreement,controls
def gate():
    bad=stale_sources()
    if bad:
        print("STALE authoritative state:")
        for p,e,a in bad: print(f"  {p}: expected {e}, got {a}")
        return False
    return True
def status():
    s=load_json("snapshot.json")
    print("TERMINAL:",s["terminal"]); print("MODE: DISCOVER/FALSIFY/REPAIR/REVIEW/INTEGRATE")
    print("EVIDENCE:",s["evidence_rule"]); print("DIVERSIFY:",s["diversification"]["rule"])
    print("STATE:","fresh" if not stale_sources() else "STALE")
def do_replay(model):
    rows=replay(model)
    for r in rows: print(("PASS" if r["pass"] else "FAIL"),r["id"])
    ok=sum(r["pass"] for r in rows); print(f"{ok}/{len(rows)} controls passed")
    return ok==len(rows)
p=argparse.ArgumentParser(); sp=p.add_subparsers(dest="cmd",required=True)
sp.add_parser("status"); q=sp.add_parser("replay"); q.add_argument("--model",default="baseline")
d=sp.add_parser("discriminate"); d.add_argument("a"); d.add_argument("b")
c=sp.add_parser("check-case"); c.add_argument("case"); sp.add_parser("fast"); sp.add_parser("full")
a=p.parse_args()
if a.cmd=="status": status(); raise SystemExit
if not gate(): raise SystemExit(2)
if a.cmd=="replay": raise SystemExit(0 if do_replay(a.model) else 1)
if a.cmd=="discriminate":
    x=first_disagreement(a.a,a.b); print(json.dumps(x,indent=2,sort_keys=True)); raise SystemExit(0 if x else 1)
if a.cmd=="check-case":
    cs={x["id"]:x for x in controls()}
    if a.case not in cs: raise SystemExit("unknown case")
    print(json.dumps(cs[a.case],indent=2,sort_keys=True)); raise SystemExit
if a.cmd in ("fast","full"):
    status()
    if not do_replay("baseline"): raise SystemExit(1)
    if a.cmd=="full": print("FULL NOTE: repository-wide research/verify.py remains authoritative and is not duplicated here.")
