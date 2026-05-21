#!/usr/bin/env python3
"""Check which AcWing grammar course problems exist on xmuoj"""
import subprocess, json

code = '''
from problem.models import Problem

grammar_ids = {
    "L1_变量输入输出": ["1","608","604","606","609","615","616","653","654","605","611","612","613","607","610","614","617","618","656","655"],
    "L2_判断语句": ["665","660","659","664","667","669","670","657","671","662","666","668","672","663","658","661"],
    "L3_循环语句": ["708","709","712","714","716","721","720","724","723","715","710","711","718","713","719","717","722","725","726","727"],
    "L4_数组": ["737","738","739","743","745","747","749","751","753","740","741","742","744","748","746","750","752","754","755","756"],
    "L5_字符串": ["760","761","763","765","769","773","772","762","768","766","767","764","770","771","774","775","776","777","778","779"],
    "L6_函数": ["804","805","808","811","812","813","819","820","810","806","807","809","814","815","816","817","818","821","822","823"],
    "L7_结构体指针": ["21","16","84","28","36","78","87","35","66","29"],
    "L8_STL位运算": ["67","68","32","17","20","53","75","51","26","862"],
}

total = 0
found = 0
result = {}
for lesson, ids in grammar_ids.items():
    result[lesson] = {"found": [], "missing": []}
    for gid in ids:
        total += 1
        acw_id = "ACW" + gid
        matches = Problem.objects.filter(_id=acw_id).values_list("_id", "title")
        if matches.exists():
            for mid, mtitle in matches:
                result[lesson]["found"].append({"id": mid, "title": mtitle})
            found += 1
        else:
            result[lesson]["missing"].append(gid)

print("TOTAL:", found, "/", total)
for lesson, data in result.items():
    print("LESSON:", lesson)
    print("  Found:", len(data["found"]))
    for p in data["found"]:
        print("    ", p["id"], p["title"])
    print("  Missing:", len(data["missing"]), data["missing"])
'''

cmd = ['docker', 'exec', 'onlinejudgedeploy-oj-backend-1', 'python', 'manage.py', 'shell', '-c', code]
result = subprocess.run(cmd, capture_output=True, text=True)

# Extract relevant output
for line in result.stdout.split('\n'):
    if line.startswith('TOTAL:') or line.startswith('LESSON:') or line.startswith('  Found:') or line.startswith('    ') or line.startswith('  Missing:'):
        print(line)

if not result.stdout.strip():
    print('STDERR:', result.stderr[:500])
