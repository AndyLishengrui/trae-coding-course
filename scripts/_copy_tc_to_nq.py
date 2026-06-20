"""
复制 test_case_id 从 ACW 题目到 NQ 题目
"""
import json
from pathlib import Path

nq_map = json.loads(Path(__file__).parent.joinpath("nq_mapping.json").read_text())

lines = ["from problem.models import Problem", ""]
lines.append("updated = 0")
lines.append("not_found = 0")
lines.append("already_ok = 0")
lines.append("")

for nq_id, info in sorted(nq_map.items()):
    acw = info["acw"]
    acw_did = "ACW" + str(acw)
    nq_did = nq_id

    lines.append("# " + nq_did + " <- " + acw_did)
    lines.append("try:")
    lines.append("    acw_list = Problem.objects.filter(_id='" + acw_did + "', test_case_id__isnull=False).exclude(test_case_id='')")
    lines.append("    acw_p = acw_list.first()")
    lines.append("    nq_p = Problem.objects.get(_id='" + nq_did + "')")
    lines.append("    if acw_p and acw_p.test_case_id:")
    lines.append("        if nq_p.test_case_id == acw_p.test_case_id:")
    lines.append("            already_ok += 1")
    lines.append("        else:")
    lines.append("            nq_p.test_case_id = acw_p.test_case_id")
    lines.append("            nq_p.save()")
    lines.append("            updated += 1")
    lines.append("            print('  Updated {} -> {}'.format('" + nq_did + "', acw_p.test_case_id[:16]))")
    lines.append("    else:")
    lines.append("        print('  WARN {}: no test_case_id'.format('" + acw_did + "'))")
    lines.append("        not_found += 1")
    lines.append("except Problem.DoesNotExist:")
    lines.append("    print('  SKIP {}: not in DB'.format('" + nq_did + "'))")
    lines.append("    not_found += 1")
    lines.append("")

lines.append("print('Done: updated={}, already_ok={}, not_found={}'.format(updated, already_ok, not_found))")

script = "\n".join(lines)
out = Path("/tmp/_copy_tc.py")
out.write_text(script, encoding="utf-8")
print("Script written: {} lines".format(len(lines)))
