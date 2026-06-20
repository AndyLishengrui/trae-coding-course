"""Update chapter 1 problems on localhost OJ with latest data."""
import json, os
from pathlib import Path

BANK = Path(__file__).parent.parent / "chapter1_bank"
SCRIPT = []

for d in sorted(BANK.iterdir()):
    if d.is_dir() and d.name.startswith("NQ1-"):
        pj = d / "problem.json"
        if not pj.exists():
            continue
        with open(pj, encoding="utf-8") as f:
            p = json.load(f)

        did = p["display_id"]
        desc = p["description"]["value"].replace("'", "\\'")
        inp = p["input_description"]["value"].replace("'", "\\'")
        out = p["output_description"]["value"].replace("'", "\\'")
        hint = p.get("hint", {}).get("value", "").replace("'", "\\'")
        source = p.get("source", "").replace("'", "\\'")

        SCRIPT.append(f"p = Problem.objects.get(_id='{did}')")
        SCRIPT.append(f"p.description = '{desc}'")
        SCRIPT.append(f"p.input_description = '{inp}'")
        SCRIPT.append(f"p.output_description = '{out}'")
        SCRIPT.append(f"p.hint = '{hint}'")
        SCRIPT.append(f"p.source = '{source}'")
        SCRIPT.append(f"p.save()")
        SCRIPT.append(f"print('  Updated {did}')")

# Write the Django shell script
full_script = "from problem.models import Problem\n" + "\n".join(SCRIPT)
script_path = "/tmp/_oj_update.py"
Path(script_path).write_text(full_script, encoding="utf-8")
print(f"Generated update script with {len(SCRIPT)} lines")
print(f"Written to {script_path}")
