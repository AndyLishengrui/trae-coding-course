"""
XMUOJ Import Packager — 创建标准导入/导出 ZIP 包

格式对齐 problem-export.zip（官方导出格式）：
  - ZIP 根目录下是 1/, 2/, ... N/ 文件夹
  - 每个文件夹包含 problem.json 和 testcase/
  - testcase/ 下是 1.in/1.out, 2.in/2.out, ...
  - test_case_score 中 input_name/output_name 是 "1.in"/"1.out" 非路径
"""
import json
import os
import zipfile
import shutil
from pathlib import Path
from typing import Dict, List, Optional


def package_single_problem(problem_json: Dict, testcase_dir: str, output_path: str, index: int = 1):
    """将单个题目打包到 ZIP（可追加）"""
    mode = "a" if os.path.exists(output_path) else "w"
    with zipfile.ZipFile(output_path, mode, zipfile.ZIP_DEFLATED) as zf:
        # problem.json
        json_str = json.dumps(problem_json, indent=4, ensure_ascii=False)
        zf.writestr(f"{index}/problem.json", json_str)
        # test cases
        if testcase_dir and os.path.isdir(testcase_dir):
            for fname in sorted(os.listdir(testcase_dir)):
                fpath = os.path.join(testcase_dir, fname)
                if os.path.isfile(fpath):
                    zf.write(fpath, f"{index}/testcase/{fname}")


def package_multi_problems(problems: List[Dict], output_path: str):
    """打包多个题目到一个 ZIP（和导出格式一致）"""
    # Clean start
    if os.path.exists(output_path):
        os.remove(output_path)

    for i, prob in enumerate(problems, 1):
        tc_dir = prob.get("_testcase_dir", "")
        prob_copy = {k: v for k, v in prob.items() if not k.startswith("_")}
        package_single_problem(prob_copy, tc_dir, output_path, index=i)


def package_samples(samples: List[Dict], output_path: Optional[str] = None, work_dir: Optional[str] = None) -> str:
    """创建样例 ZIP（扁平的 .in/.out）"""
    work_dir = work_dir or os.getcwd()
    output = output_path or os.path.join(work_dir, "样例.zip")
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for i, sample in enumerate(samples, 1):
            zf.writestr(f"{i}.in", sample["input"].encode("utf-8"))
            zf.writestr(f"{i}.out", sample["output"].encode("utf-8"))
    return output


def create_chapter_export(bank_dir: str, output_path: str):
    """将一个章节题库目录导出为标准导入 ZIP"""
    bank = Path(bank_dir)
    problems = []
    for prob_dir in sorted(bank.iterdir()):
        if not prob_dir.is_dir(): continue
        pj_file = prob_dir / "problem.json"
        tc_dir = prob_dir / "testcase"
        if pj_file.exists():
            with open(pj_file) as f:
                prob = json.load(f)
            prob["_testcase_dir"] = str(tc_dir) if tc_dir.exists() else ""
            problems.append(prob)

    package_multi_problems(problems, output_path)
    return output_path


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        create_chapter_export(sys.argv[1], sys.argv[2])
        print(f"✅ 章节导出: {sys.argv[2]}")
    else:
        print("Usage: python packager.py <bank_dir> <output.zip>")
