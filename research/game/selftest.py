from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from core import replay,first_disagreement
assert all(x["pass"] for x in replay("baseline"))
bad=[x for x in replay("refuted_peak_strain") if not x["pass"]]
assert {x["id"] for x in bad}>={"clock-action-obstruction","old-strong-scaling-action"}
d=first_disagreement("baseline","refuted_peak_strain")
assert d and d["case"]=="clock-action-obstruction"
print("PASS: baseline, refuted peak-strain mechanism, discrimination")
