#!/usr/bin/env python3
"""
初始化课程数据：创建"基于Trae的编程兴趣班入门百练"课程，包含16章节和全部161题。
支持两种模式：
  1. 直接模式（默认）：直接写入JSON配置到Docker容器
  2. API模式：通过管理API创建（需后端运行）
用法：
  python3 init_courses.py              # 直接写入
  python3 init_courses.py --api        # 通过API（默认localhost）
  python3 init_courses.py --api http://xmuoj.com  # 通过API（指定地址）
"""
import json
import os
import sys

COURSE_TITLE = "基于Trae的编程兴趣班入门百练"
COURSE_DESC = "32学时，零基础到基础算法，C++与Python双语言，16章161题"

CHAPTERS = [
    (1, "第1章 程序设计的第一个脚印——变量、输入输出与顺序结构"),
    (2, "第2章 选择的艺术——条件判断与分支结构"),
    (3, "第3章 循环的魔力——for/while与嵌套循环"),
    (4, "第4章 数据的容器——数组与线性存储"),
    (5, "第5章 矩阵的舞蹈——多维数组与矩阵模式"),
    (6, "第6章 字符的世界——字符串处理"),
    (7, "第7章 模块化的力量——函数、递归与库的威力"),
    (8, "第8章 指针与抽象——结构体、指针与STL容器"),
    (9, "第9章 分治之美——排序与二分"),
    (10, "第10章 预处理的艺术——前缀和、差分与双指针"),
    (11, "第11章 数字的奥秘——高精度、位运算与离散化"),
    (12, "第12章 结构的根基——基础数据结构"),
    (13, "第13章 搜索的疆域——搜索与回溯"),
    (14, "第14章 图的世界——图论入门"),
    (15, "第15章 最优子结构——动态规划"),
    (16, "第16章 智慧的策略——贪心、并查集与数学"),
]


def load_nq_mapping():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mapping_path = os.path.join(script_dir, "nq_mapping.json")
    if not os.path.exists(mapping_path):
        print(f"ERROR: nq_mapping.json not found at {mapping_path}")
        sys.exit(1)
    with open(mapping_path, "r", encoding="utf-8") as f:
        mapping = json.load(f)
    chapters = {}
    for nq_id, info in mapping.items():
        ch = info["ch"]
        if ch not in chapters:
            chapters[ch] = []
        chapters[ch].append((nq_id, info["idx"]))
    for ch in chapters:
        chapters[ch].sort(key=lambda x: x[1])
    return chapters


def build_config(chapters_map):
    chapters_list = []
    for ch_num, ch_title in CHAPTERS:
        nq_problems = chapters_map.get(ch_num, [])
        problems = []
        total = len(nq_problems)
        half = (total + 1) // 2  # 50/50 split, odd counts favor examples
        for order, (nq_id, _) in enumerate(nq_problems, 1):
            ptype = "example" if order <= half else "exercise"
            problems.append({"display_id": nq_id, "type": ptype, "order": order})
        chapters_list.append({
            "id": ch_num, "title": ch_title, "order": ch_num,
            "visible": True, "problems": problems,
        })
    return {"courses": [{
        "id": 1, "title": COURSE_TITLE, "description": COURSE_DESC,
        "visible": True, "order": 1, "chapters": chapters_list,
    }]}


def write_direct(config):
    import subprocess
    container = "onlinejudgedeploy-oj-backend-1"
    config_json = json.dumps(config, ensure_ascii=False, indent=2)
    subprocess.run(["docker", "exec", container, "mkdir", "-p", "/app/data"], capture_output=True)
    result = subprocess.run(
        ["docker", "exec", "-i", container, "tee", "/app/data/groups_config.json"],
        input=config_json.encode("utf-8"), capture_output=True)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr.decode()}"); return False
    # Fix permissions (gunicorn runs as server:spj)
    subprocess.run(["docker", "exec", container, "chown", "-R", "server:spj", "/app/data/"], capture_output=True)
    print(f"Wrote {len(config_json)} bytes, permissions fixed."); return True


def write_via_api(config, base_url="http://localhost"):
    import requests
    TOKEN = "63310cdaec0bc93b08f856568e125e75"
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"})
    course_data = config["courses"][0]
    resp = s.post(f"{base_url}/api/admin/groups/courses/", json={
        "title": course_data["title"], "description": course_data["description"],
        "visible": True, "order": 1,
    })
    d = resp.json()
    if d.get("error"): print(f"ERROR: {d.get('data')}"); return False
    course_id = d["data"]["id"]
    print(f"Created course: id={course_id}")
    for ch in course_data["chapters"]:
        resp = s.post(f"{base_url}/api/admin/groups/chapters/", json={
            "course_id": course_id, "title": ch["title"],
            "visible": True, "order": ch["order"],
        })
        d = resp.json()
        if d.get("error"): print(f"  ERROR: {ch['title']} - {d.get('data')}"); continue
        chapter_id = d["data"]["id"]
        for p in ch["problems"]:
            resp = s.post(f"{base_url}/api/admin/groups/problems/", json={
                "course_id": course_id, "chapter_id": chapter_id,
                "display_id": p["display_id"], "type": p["type"], "order": p["order"],
            })
            d = resp.json()
            if d.get("error"): print(f"    WARN: {p['display_id']} - {d.get('data')}")
    return True


def main():
    chapters_map = load_nq_mapping()
    config = build_config(chapters_map)
    print(f"Course: {COURSE_TITLE}")
    total = 0
    for ch in config["courses"][0]["chapters"]:
        n = len(ch["problems"]); total += n
        print(f"  {ch['title']}: {n} problems")
    print(f"Total: {total} problems across 16 chapters")

    if "--api" in sys.argv:
        base = sys.argv[sys.argv.index("--api") + 1] if len(sys.argv) > sys.argv.index("--api") + 1 else "http://localhost"
        print(f"\nDeploying via API to {base}...")
        ok = write_via_api(config, base)
    else:
        print("\nWriting directly to Docker container...")
        ok = write_direct(config)
    if ok:
        print("\nSUCCESS! Run: docker restart onlinejudgedeploy-oj-backend-1")
    else:
        print("\nFAILED!"); sys.exit(1)


if __name__ == "__main__":
    main()
