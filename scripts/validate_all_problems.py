#!/usr/bin/env python3
"""
严格测试流：格式化代码 → 提交OJ验证 → 确认全部AC

流程:
  1. 读取 nq_mapping.json + all_problems_data.json
  2. 对每道题的 NQ 目录：
     a. 验证/修复 Andy.cpp 格式（添加标准头注释）
     b. 验证/修复 Andy.py 格式（添加标准头注释）
     c. 提交C++和Python到 localhost OJ
     d. 等待判题结果
     e. 记录AC/WA/TLE状态
  3. 生成报告

用法:
  python3 validate_all_problems.py --chapter 1         # 单章测试
  python3 validate_all_problems.py --chapter 1 --fix    # 格式化+测试
  python3 validate_all_problems.py --all --fix          # 全量格式化+测试
  python3 validate_all_problems.py --all --dry-run      # 预览
"""
import json, os, sys, re, time, subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

BOOK_ROOT = Path(__file__).parent.parent
DATA_DIR = Path(__file__).parent


def load_json(name):
    with open(DATA_DIR / name, encoding="utf-8") as f:
        return json.load(f)


# 章节主题映射（用于生成算法描述注释）
CHAPTER_TOPIC = {
    1: "基本输入输出与运算", 2: "条件判断与分支", 3: "循环与迭代",
    4: "数组与线性存储", 5: "多维数组与矩阵", 6: "字符串处理",
    7: "函数与递归", 8: "结构体、指针与STL",
    9: "排序与二分", 10: "前缀和、差分与双指针",
    11: "高精度、位运算与离散化", 12: "基础数据结构",
    13: "搜索与回溯", 14: "图论",
    15: "动态规划", 16: "贪心、并查集与数学",
}


def get_complexity(acw: int, title: str) -> Tuple[str, str]:
    """根据题目推断复杂度"""
    title_l = title.lower()
    # 简单 I/O → O(1)
    simple_patterns = ["a+b", "a + b", "差", "乘积", "平均数", "工资", "油耗",
                       "距离", "钞票", "时间转换", "简单计算", "球的体积", "面积", "最大值",
                       "倍数", "零食", "区间", "三角形", "游戏时间", "加薪", "动物",
                       "选择练习", "ddd", "点的坐标", "三角形类型", "税", "简单排序",
                       "偶数", "奇数", "正数", "pum", "六个奇数", "乘法表", "余数", "区间 2"]
    if any(p in title_l for p in simple_patterns[:3]):
        return "O(1)", "O(1)"
    if any(p in title_l for p in simple_patterns):
        return "O(1)", "O(1)"
    # 循环 → O(n) or O(n²)
    if "循环" in title_l or "斐波那契" in title_l:
        return "O(n)", "O(1)"
    # 数组遍历 → O(n)
    if "数组" in title_l and "排序" not in title_l:
        return "O(n)", "O(1)"
    # 矩阵 → O(n²) or O(n)
    if "矩阵" in title_l:
        return "O(n²)", "O(1)"
    # 排序 → O(nlogn)
    if "排序" in title_l:
        return "O(nlog n)", "O(n)"
    # 二分 → O(logn)
    if "二分" in title_l:
        return "O(log n)", "O(1)"
    # 搜索 → O(n!) or O(b^d)
    if "dfs" in title_l or "bfs" in title_l or "排列" in title_l or "皇后" in title_l:
        return "O(n!)", "O(n)"
    if "迷宫" in title_l or "八数码" in title_l:
        return "O(b^d)", "O(b^d)"
    # 图论
    if "dijkstra" in title_l:
        return "O((V+E)logV)", "O(V)"
    if "spfa" in title_l:
        return "O(VE)", "O(V)"
    if "floyd" in title_l:
        return "O(V³)", "O(V²)"
    if "prim" in title_l:
        return "O(V²)", "O(V)"
    if "kruskal" in title_l:
        return "O(ElogE)", "O(V)"
    if "拓扑" in title_l:
        return "O(V+E)", "O(V)"
    if "二分图" in title_l:
        return "O(V+E)", "O(V)"
    # DP
    if "背包" in title_l:
        return "O(NV)", "O(V)"
    if "最长上升" in title_l or "最长公共" in title_l:
        return "O(n²)", "O(n)"
    if "编辑距离" in title_l:
        return "O(nm)", "O(nm)"
    if "数字三角形" in title_l:
        return "O(n²)", "O(n)"
    if "石子合并" in title_l:
        return "O(n³)", "O(n²)"
    if "滑雪" in title_l:
        return "O(RC)", "O(RC)"
    # 数据结构
    if "链表" in title_l or "栈" in title_l or "队列" in title_l or "堆" in title_l:
        return "O(1) per op", "O(n)"
    if "kmp" in title_l:
        return "O(n+m)", "O(m)"
    if "并查集" in title_l:
        return "O(α(n))", "O(n)"
    if "快速幂" in title_l:
        return "O(log n)", "O(1)"
    # Default
    return "O(n)", "O(n)"


def make_cpp_header(nq_id: str, title: str, acw: int, ch: int) -> str:
    """生成C++标准头注释"""
    time_c, space_c = get_complexity(acw, title)
    topic = CHAPTER_TOPIC.get(ch, "")
    return f"""/**
 * {nq_id}: {title}
 * {topic} | AcWing {acw}
 * 时间: {time_c} | 空间: {space_c}
 */"""


def make_py_header(nq_id: str, title: str, acw: int, ch: int) -> str:
    """生成Python标准头注释"""
    topic = CHAPTER_TOPIC.get(ch, "")
    time_c, space_c = get_complexity(acw, title)
    return f"""# {nq_id}: {title}
# {topic} | AcWing {acw}
# 时间: {time_c} | 空间: {space_c}"""


def has_header(content: str, is_cpp: bool) -> bool:
    """检查代码是否已有合理的头注释"""
    lines = content.strip().split("\n")
    # Check first non-blank, non-include lines
    for i, line in enumerate(lines[:10]):  # Check first 10 lines
        stripped = line.strip()
        if not stripped or stripped.startswith("#include") or stripped.startswith("using"):
            continue
        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") or stripped.startswith("#"):
            return True
        if stripped.startswith("int main") or stripped.startswith("def ") or stripped.startswith("import"):
            return False
    return False


def fix_code_format(filepath: Path, nq_id: str, title: str, acw: int, ch: int) -> bool:
    """修复代码格式：添加标准头注释"""
    if not filepath.exists():
        return False

    content = filepath.read_text(encoding="utf-8").strip()
    is_cpp = filepath.suffix == ".cpp"

    if has_header(content, is_cpp):
        return False  # Already has header

    if is_cpp:
        header = make_cpp_header(nq_id, title, acw, ch)
        # Insert header after #include and using lines
        lines = content.split("\n")
        insert_at = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("#include") or line.strip().startswith("using"):
                insert_at = i + 1
        # Also skip blank lines after includes
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
        new_lines = lines[:insert_at] + [header, ""] + lines[insert_at:]
        filepath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    else:
        header = make_py_header(nq_id, title, acw, ch)
        lines = content.split("\n")
        insert_at = 0
        for i, line in enumerate(lines):
            if line.strip().startswith("import") or line.strip().startswith("from"):
                insert_at = i + 1
        while insert_at < len(lines) and not lines[insert_at].strip():
            insert_at += 1
        new_lines = lines[:insert_at] + ["", header, ""] + lines[insert_at:]
        filepath.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    return True


def submit_code(code: str, language: str, problem_id: int) -> Optional[str]:
    """提交代码到 OJ，返回 submission_id"""
    import requests
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    resp = s.post("http://localhost/api/submission", json={
        "problem_id": problem_id,
        "code": code,
        "language": language,
    })
    try:
        data = resp.json()
        if data.get("error"):
            return None
        return data.get("data", {}).get("submission_id", "")
    except:
        return None


def check_result(submission_id: str, max_wait: int = 30) -> Optional[int]:
    """查询判题结果。返回 -1=judging, 0=AC, 其他=错误码"""
    import requests
    for _ in range(max_wait // 2):
        time.sleep(2)
        resp = requests.get(f"http://localhost/api/submission?id={submission_id}")
        try:
            data = resp.json()
            if data.get("error"):
                continue
            result = data.get("data", {}).get("result", -2)
            if result != -1:  # Not pending
                return result
        except:
            pass
    return -1  # Timeout


def validate_chapter(ch: int, fix: bool = False, submit: bool = False, dry_run: bool = False):
    """验证一个章节的所有题目"""
    nq_map = load_json("nq_mapping.json")
    all_data = load_json("all_problems_data.json")
    bank_dir = BOOK_ROOT / f"chapter{ch}_bank"

    if not bank_dir.exists():
        print(f"  ch{ch}: bank dir not found")
        return []

    results = []
    chapter_nqs = [(nq_id, info) for nq_id, info in nq_map.items() if info["ch"] == ch]
    chapter_nqs.sort(key=lambda x: x[1]["idx"])

    topic = CHAPTER_TOPIC.get(ch, "")
    print(f"\n{'='*50}")
    print(f"ch{ch}: {topic} ({len(chapter_nqs)}题)")
    if dry_run:
        print("  [DRY RUN 模式]")
    print(f"{'='*50}")

    for nq_id, info in chapter_nqs:
        acw = info["acw"]
        ch_str = str(ch)
        acw_str = str(acw)
        baseline = all_data.get(ch_str, {}).get(acw_str, {})
        title = baseline.get("title", f"AcWing {acw}")

        # Find NQ directory
        nq_dir = None
        for d in bank_dir.iterdir():
            if d.is_dir() and d.name.startswith(nq_id):
                nq_dir = d
                break
        if not nq_dir:
            print(f"  ⚠️  {nq_id}: 目录不存在")
            continue

        cpp_file = nq_dir / "Andy.cpp"
        py_file = nq_dir / "Andy.py"

        # Step 1: Fix code format
        if fix:
            cpp_fixed = fix_code_format(cpp_file, nq_id, title, acw, ch)
            py_fixed = fix_code_format(py_file, nq_id, title, acw, ch)
            fmt_msg = ""
            if cpp_fixed and py_fixed:
                fmt_msg = " [fmt:cpp+py]"
            elif cpp_fixed:
                fmt_msg = " [fmt:cpp]"
            elif py_fixed:
                fmt_msg = " [fmt:py]"
            if fmt_msg:
                print(f"  🔧 {nq_id}: {title}{fmt_msg}")

        if not submit:
            continue

        # Step 2: Get OJ problem ID via Django ORM (public API may hide contest problems)
        # Use docker exec for reliable access
        r2 = subprocess.run(
            ["docker", "exec", "onlinejudgedeploy-oj-backend-1", "python", "manage.py", "shell",
             "-c", "from problem.models import Problem; p=Problem.objects.filter(_id='{}').first(); print(p.id if p else 0)".format(nq_id)],
            capture_output=True, text=True, timeout=10
        )
        try:
            oj_id = int(r2.stdout.strip().split("\n")[-1])
        except:
            oj_id = 0

        if not oj_id:
            print(f"  ❌ {nq_id}: OJ上不存在")
            results.append({"nq_id": nq_id, "title": title, "cpp": "MISSING", "py": "MISSING"})
            continue

        if dry_run:
            print(f"  📝 {nq_id}: {title} [DRY RUN - 将提交cpp+py]")
            continue

        # Step 3: Read code and submit
        cpp_code = cpp_file.read_text(encoding="utf-8")
        py_code = py_file.read_text(encoding="utf-8")

        # Submit C++
        cpp_sub = submit_code(cpp_code, "C++", oj_id)
        cpp_result = check_result(cpp_sub) if cpp_sub else None
        cpp_status = "AC" if cpp_result == 0 else ("WA" if cpp_result and cpp_result > 0 else "ERR")

        # Submit Python
        py_sub = submit_code(py_code, "Python3", oj_id)
        py_result = check_result(py_sub) if py_sub else None
        py_status = "AC" if py_result == 0 else ("WA" if py_result and py_result > 0 else "ERR")

        # Status icon
        icon = "✅" if (cpp_status == "AC" and py_status == "AC") else "❌"
        print(f"  {icon} {nq_id}: C++={cpp_status} Py={py_status} | {title}")

        results.append({
            "nq_id": nq_id, "title": title, "cpp": cpp_status, "py": py_status
        })

    # Chapter summary
    if submit and results:
        ac_count = sum(1 for r in results if r["cpp"] == "AC" and r["py"] == "AC")
        print(f"  📊 ch{ch}: {ac_count}/{len(results)} 双AC")

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="严格测试流")
    parser.add_argument("--chapter", "-c", type=int, help="单章")
    parser.add_argument("--all", action="store_true", help="全部16章")
    parser.add_argument("--fix", action="store_true", help="修复代码格式")
    parser.add_argument("--submit", action="store_true", help="提交并验证AC")
    parser.add_argument("--dry-run", action="store_true", help="预览模式")
    args = parser.parse_args()

    if args.chapter:
        chapters = [args.chapter]
    else:
        chapters = list(range(1, 17))

    if args.dry_run:
        print("⚠️  DRY RUN — 只预览，不实际修改/提交\n")

    all_results = []
    for ch in chapters:
        results = validate_chapter(ch, fix=args.fix, submit=args.submit, dry_run=args.dry_run)
        all_results.extend(results)

    # Final report
    if all_results:
        total = len(all_results)
        ac_both = sum(1 for r in all_results if r.get("cpp") == "AC" and r.get("py") == "AC")
        cpp_ac = sum(1 for r in all_results if r.get("cpp") == "AC")
        py_ac = sum(1 for r in all_results if r.get("py") == "AC")
        print(f"\n{'='*50}")
        print(f"📊 总报告: {total}题")
        print(f"  双AC: {ac_both}/{total}")
        print(f"  C++ AC: {cpp_ac}/{total}")
        print(f"  Py AC: {py_ac}/{total}")

        failed = [r for r in all_results if r.get("cpp") != "AC" or r.get("py") != "AC"]
        if failed:
            print(f"\n❌ 未通过 ({len(failed)}题):")
            for r in failed:
                print(f"  {r['nq_id']}: C++={r.get('cpp','?')} Py={r.get('py','?')} | {r['title']}")
        else:
            print(f"\n🎉 全部通过！")

    # Save results
    if all_results:
        report_path = DATA_DIR / "validation_report.json"
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        print(f"\n报告已保存: {report_path}")


if __name__ == "__main__":
    main()
