from __future__ import annotations
import importlib.util, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
GAME=ROOT/"research"/"game"
def load_json(name): return json.loads((GAME/name).read_text())
def git_blob(path):
    p=subprocess.run(["git","hash-object",path],cwd=ROOT,text=True,capture_output=True)
    if p.returncode: raise RuntimeError(p.stderr.strip() or f"cannot hash {path}")
    return p.stdout.strip()
def stale_sources():
    bad=[]
    for path,expected in load_json("snapshot.json")["authoritative_sources"].items():
        if not (ROOT/path).exists(): bad.append((path,expected,None)); continue
        actual=git_blob(path)
        if actual!=expected: bad.append((path,expected,actual))
    return bad
def controls(): return load_json("controls.json")["controls"]
def load_model(name):
    path=GAME/"models"/f"{name}.py"
    spec=importlib.util.spec_from_file_location(f"navier_game_{name}",path)
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
def replay(name="baseline"):
    mod=load_model(name); out=[]
    for c in controls():
        try: got=mod.predict(c)
        except Exception as e: got={"__error__":type(e).__name__+": "+str(e)}
        out.append({"id":c["id"],"pass":got==c["observation"],"expected":c["observation"],"got":got})
    return out
def first_disagreement(a,b):
    ma,mb=load_model(a),load_model(b)
    for c in controls():
        pa,pb=ma.predict(c),mb.predict(c)
        if pa!=pb: return {"case":c["id"],"a":pa,"b":pb,"observation":c["observation"]}
    return None
