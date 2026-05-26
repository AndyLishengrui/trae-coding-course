#!/usr/bin/env python3
"""
Sync Engine — 将本地书稿同步到 XMUOJ 云端题库

功能：
1. 从 COURSE_PLAN_V2.md 读取章节-题目映射
2. 从 lessons_v2/ 读取 C++/Python 代码
3. 从 textbook/ 读取题面 markdown，转换为 HTML
4. 创建/更新 XMUOJ 题目
5. 管理题目在实验(Contest)中的排列顺序
6. 生成测试数据（基于题面样例）
"""
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .constants import V2_PLAN, CHAPTER_TITLES

BOOK_ROOT = Path(__file__).parent.parent.parent


def find_code(pid: int, ext: str) -> Optional[str]:
    """在 lessons_v2 中查找代码"""
    for d in ["lessons_v2", "acwing_codes", "algorithm_basic_codes"]:
        base = BOOK_ROOT / d
        if not base.exists():
            continue
        for root, dirs, files in os.walk(str(base)):
            for f in files:
                if f.endswith(ext) and f"acw{pid}" in f.lower():
                    path = os.path.join(root, f)
                    return Path(path).read_text(encoding="utf-8")
    return None


def find_textbook_problem(nq_num: int, chapter: int) -> Optional[Dict]:
    """从 textbook/ 读取题面数据"""
    ch_file = BOOK_ROOT / "textbook" / f"chapter{chapter:02d}_*.md"
    # Simplified: read from problems/ directory
    for d in ["problems/语法基础课", "problems/算法基础课"]:
        base = BOOK_ROOT / d
        if not base.exists():
            continue
        for root, dirs, files in os.walk(str(base)):
            for f in files:
                if f.endswith(".md"):
                    path = os.path.join(root, f)
                    content = Path(path).read_text(encoding="utf-8")
                    if "## 题目描述" in content:
                        return parse_problem_md(content)
    return None


def parse_problem_md(content: str) -> Dict:
    """解析 markdown 题面，提取结构化数据"""
    result = {}

    # Title
    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        result["title"] = title_match.group(1).strip()

    # Description
    desc_match = re.search(r"## 题目描述\s*\n(.*?)(?=###|\n##)", content, re.DOTALL)
    if desc_match:
        result["description"] = desc_match.group(1).strip()

    # Input format
    in_match = re.search(r"### 输入格式\s*\n(.*?)(?=###|\n##)", content, re.DOTALL)
    if in_match:
        result["input_description"] = in_match.group(1).strip()

    # Output format
    out_match = re.search(r"### 输出格式\s*\n(.*?)(?=###|\n##)", content, re.DOTALL)
    if out_match:
        result["output_description"] = out_match.group(1).strip()

    # Samples
    samples = []
    sample_blocks = re.findall(r"\*\*输入[：:]\*\*\s*\n```\s*\n(.*?)```\s*\n\s*\*\*输出[：:]\*\*\s*\n```\s*\n(.*?)```", content, re.DOTALL)
    for inp, out in sample_blocks:
        samples.append({"input": inp.strip(), "output": out.strip()})
    if samples:
        result["samples"] = samples

    # Difficulty
    diff_match = re.search(r"\*\*难度[：:]\*\*\s*(\S+)", content)
    if diff_match:
        diff_map = {"简单": "Low", "中等": "Mid", "困难": "High"}
        result["difficulty"] = diff_map.get(diff_match.group(1), "Low")

    return result


def md_to_html(text: str) -> str:
    """简单 Markdown → HTML 转换（用于题面）"""
    if not text:
        return "<p></p>"
    # Basic conversions
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Code blocks
    text = re.sub(r"```(\w*)\n(.*?)```", r"<pre><code>\2</code></pre>", text, flags=re.DOTALL)
    # Inline code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # Paragraphs
    paragraphs = text.strip().split("\n\n")
    return "".join(f"<p>{p.replace(chr(10), '<br/>')}</p>" for p in paragraphs if p.strip())


def generate_test_case_zip(pid: int, output_dir: str) -> Optional[str]:
    """为题面中的样例生成测试数据 ZIP 文件"""
    # Find problem description
    prob_data = find_textbook_problem(0, 0)  # TODO: fix lookup
    if not prob_data or "samples" not in prob_data:
        return None

    import zipfile
    zip_name = os.path.join(output_dir, f"ACW{pid}_testcases.zip")
    with zipfile.ZipFile(zip_name, "w") as zf:
        for i, sample in enumerate(prob_data["samples"], 1):
            zf.writestr(f"{i}.in", sample["input"].encode("utf-8"))
            zf.writestr(f"{i}.out", sample["output"].encode("utf-8"))

    return zip_name


class SyncEngine:
    """同步引擎：本地书稿 → XMUOJ 云端"""

    def __init__(self, client, dry_run: bool = False):
        self.client = client
        self.dry_run = dry_run
        self.stats = {"created": 0, "updated": 0, "skipped": 0, "errors": 0}

    def sync_chapter(self, chapter: int, contest_id: Optional[int] = None):
        """同步一个章节的所有题目"""
        pids = V2_PLAN.get(chapter, [])
        if not pids:
            print(f"第{chapter}章：无题目定义")
            return

        title = CHAPTER_TITLES.get(chapter, f"第{chapter}章")
        print(f"\n{'='*60}")
        print(f"📖 第{chapter}章: {title} ({len(pids)}题)")
        print(f"{'='*60}")

        for i, pid in enumerate(pids, 1):
            display_id = f"ACW{pid}"
            print(f"\n  [{i}/{len(pids)}] {display_id}")

            # Check existing
            existing = self._get_problem_by_display_id(display_id)

            # Build problem data
            prob_data = self._build_problem(pid, chapter, i)

            if existing:
                if self.dry_run:
                    print(f"    [DRY RUN] 将更新 id={existing['id']}")
                    self.stats["updated"] += 1
                else:
                    try:
                        prob_data["id"] = existing["id"]
                        self.client.update_problem(prob_data)
                        print(f"    ✅ 已更新 (id={existing['id']})")
                        self.stats["updated"] += 1
                    except Exception as e:
                        print(f"    ❌ 更新失败: {e}")
                        self.stats["errors"] += 1
            else:
                if self.dry_run:
                    print(f"    [DRY RUN] 将创建 {display_id}")
                    self.stats["created"] += 1
                else:
                    try:
                        result = self.client.create_problem(prob_data)
                        new_id = result.get("id") if isinstance(result, dict) else result
                        print(f"    ✅ 已创建 (id={new_id})")
                        self.stats["created"] += 1
                    except Exception as e:
                        print(f"    ❌ 创建失败: {e}")
                        self.stats["errors"] += 1

    def _get_problem_by_display_id(self, display_id: str) -> Optional[Dict]:
        """通过 display_id 查找已存在的题目"""
        try:
            # Use public API
            import requests
            resp = requests.get(f"http://xmuoj.com/api/problem", params={"problem_id": display_id}, timeout=10)
            data = resp.json()
            if data.get("error") is None and data.get("data"):
                return data["data"]
        except:
            pass
        return None

    def _build_problem(self, pid: int, chapter: int, order: int) -> Dict:
        """构建完整的题目数据"""
        nq_num = self._get_nq_num(pid, chapter)

        # Try to get description from XMUOJ first
        import requests
        title = f"AcWing {pid}"
        desc = f"<p>AcWing {pid}</p>"
        input_desc = "<p></p>"
        output_desc = "<p></p>"
        samples = [{"input": "", "output": ""}]
        difficulty = "Low"
        tags = []

        try:
            resp = requests.get(f"http://xmuoj.com/api/problem?problem_id=ACW{pid}", timeout=5)
            data = resp.json()
            if data.get("error") is None and data.get("data"):
                prob = data["data"]
                title = prob.get("title", title)
                desc = prob.get("description", desc)
                input_desc = prob.get("input_description", input_desc)
                output_desc = prob.get("output_description", output_desc)
                samples = prob.get("samples", samples)
                difficulty = prob.get("difficulty", difficulty)
                tags = prob.get("tags", tags)
        except:
            pass

        return {
            "_id": f"ACW{pid}",
            "title": title,
            "description": desc,
            "input_description": input_desc,
            "output_description": output_desc,
            "samples": samples,
            "test_case_id": "",
            "time_limit": 1000,
            "memory_limit": 256,
            "languages": ["C", "C++", "Python3"],
            "template": {},
            "rule_type": "ACM",
            "io_mode": {"io_mode": "Standard IO", "input": "input.txt", "output": "output.txt"},
            "spj": False,
            "spj_language": None,
            "spj_code": None,
            "spj_compile_ok": False,
            "visible": True,
            "difficulty": difficulty,
            "tags": tags,
            "hint": "",
            "source": f"AcWing {pid} | NQ{nq_num:03d} | 第{chapter}章",
            "share_submission": False,
        }

    def _get_nq_num(self, pid: int, chapter: int) -> int:
        """计算全局 NQ 编号"""
        nq = 0
        for ch in range(1, chapter):
            nq += len(V2_PLAN.get(ch, []))
        pids = V2_PLAN.get(chapter, [])
        return nq + pids.index(pid) + 1

    def print_summary(self):
        print(f"\n{'='*60}")
        print(f"同步{'预览' if self.dry_run else ''}完成！")
        print(f"  创建: {self.stats['created']}")
        print(f"  更新: {self.stats['updated']}")
        print(f"  跳过: {self.stats['skipped']}")
        print(f"  失败: {self.stats['errors']}")
        print(f"  总计: {sum(self.stats.values())}")
        print(f"{'='*60}")


# Standalone usage
if __name__ == "__main__":
    from client import XmuojClient

    client = XmuojClient(config_path=str(Path.home() / ".xmuoj_cli_config.json"))
    if not client._token:
        print("请先登录: python cli.py login <username> <password>")
        sys.exit(1)

    engine = SyncEngine(client, dry_run="--dry-run" in sys.argv)

    # Parse chapter argument
    chapter = None
    for arg in sys.argv[1:]:
        if arg.startswith("--chapter="):
            chapter = int(arg.split("=")[1])
        elif arg.startswith("-c="):
            chapter = int(arg.split("=")[1])

    chapters = [chapter] if chapter else range(1, 17)
    for ch in chapters:
        engine.sync_chapter(ch)

    engine.print_summary()
