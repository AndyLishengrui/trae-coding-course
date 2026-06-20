"""Fix hint field — replace plain text '原题链接' with proper HTML link."""
import json
from pathlib import Path

BANK = Path(__file__).parent.parent / "chapter1_bank"
SCRIPT = ["from problem.models import Problem"]

for d in sorted(BANK.iterdir()):
    if d.is_dir() and d.name.startswith("NQ1-"):
        pj = d / "problem.json"
        if not pj.exists():
            continue
        with open(pj, encoding="utf-8") as f:
            p = json.load(f)
        did = p["display_id"]
        hint = p.get("hint", {}).get("value", "")
        hint_esc = hint.replace("'", "\\'")
        SCRIPT.append(f"p = Problem.objects.get(_id='{did}')")
        SCRIPT.append(f"p.hint = '{hint_esc}'")
        SCRIPT.append(f"p.save()")
        SCRIPT.append(f"print('Updated {did}')")

full = "\n".join(SCRIPT)
Path("/tmp/_fix_hint_dj.py").write_text(full, encoding="utf-8")
print(f"Wrote {len(SCRIPT)} lines")
