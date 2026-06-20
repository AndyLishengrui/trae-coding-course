#!/usr/bin/env python3
"""
Sync Engine — 将本地书稿同步到 XMUOJ 云端题库

功能：
1. 从 V2_PLAN 读取章节-题目映射
2. 从 all_problems_data.json 读取题面数据
3. 从 lessons_v2/ 和 chapter banks 读取 C++/Python 代码
4. 创建/更新 XMUOJ 题目
"""
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

from constants import V2_PLAN, CHAPTER_TITLES, normalize_pid, get_nq_sequential_num

BOOK_ROOT = Path(__file__).parent.parent.parent


def load_problems_data() -> Dict:
    """从 all_problems_data.json 加载161题的基线数据"""
    path = BOOK_ROOT / "scripts" / "all_problems_data.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def find_code_file(pid: int, ext: str) -> Optional[str]:
    """在项目中查找题目的代码文件

    搜索优先级：chapter banks > lessons_v2 > acwing_codes > algorithm_basic_codes
    """
    search_dirs = []
    # 1. Chapter banks (best quality - has Andy.cpp/py with test cases)
    for ch in range(1, 17):
        chapter_bank = BOOK_ROOT / f"chapter{ch}_bank"
        if chapter_bank.exists():
            search_dirs.append(chapter_bank)
    # 2. Other source dirs
    for d in ["lessons_v2", "acwing_codes", "algorithm_basic_codes"]:
        base = BOOK_ROOT / d
        if base.exists():
            search_dirs.append(base)

    for d in search_dirs:
        for root, dirs, files in os.walk(str(d)):
            for f in files:
                if f.endswith(ext) and f"acw{pid}" in f.lower():
                    return os.path.join(root, f)
    return None


def find_textbook_problem(nq_num: int, chapter: int) -> Optional[Dict]:
    """从 all_problems_data.json 读取题面数据

    参数 nq_num 和 chapter 用于定位 V2_PLAN 中的具体题目位置
    """
    data = load_problems_data()
    if not data:
        return None

    # 通过 V2_PLAN + nq_num_in_chapter 定位具体题目
    pids = V2_PLAN.get(chapter, [])
    if not pids:
        return None

    ch_str = str(chapter)
    chapter_data = data.get(ch_str, {})
    if not chapter_data:
        return None

    # 遍历章节中的题目，找到匹配的 nq_num
    for idx, entry in enumerate(pids, 1):
        global_seq = get_nq_sequential_num(chapter, idx)
        if global_seq == nq_num:
            display_id, source_type, original = normalize_pid(entry)
            if source_type == "acw":
                acw_id = str(original)
                prob = chapter_data.get(acw_id, {})
                if prob:
                    return {
                        "title": prob.get("title", f"AcWing {acw_id}"),
                        "description": prob.get("description", ""),
                        "input_description": prob.get("input_description", ""),
                        "output_description": prob.get("output_description", ""),
                        "samples": prob.get("samples", []),
                        "hint": prob.get("hint", ""),
                        "difficulty": prob.get("difficulty", "Low"),
                        "tags": prob.get("tags", []),
                    }
            break

    return None


def parse_problem_md(content: str) -> Dict:
    """解析 markdown 题面，提取结构化数据"""
    result = {}

    title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
    if title_match:
        result["title"] = title_match.group(1).strip()

    desc_match = re.search(r"## 题目描述\s*\n(.*?)(?=###|\n##)", content, re.DOTALL)
    if desc_match:
        result["description"] = desc_match.group(1).strip()

    in_match = re.search(r"### 输入格式\s*\n(.*?)(?=###|\n##)", content, re.DOTALL)
    if in_match:
        result["input_description"] = in_match.group(1).strip()

    out_match = re.search(r"### 输出格式\s*\n(.*?)(?=###|\n##)", content, re.DOTALL)
    if out_match:
        result["output_description"] = out_match.group(1).strip()

    samples = []
    sample_blocks = re.findall(
        r"\*\*输入[：:]\*\*\s*\n```\s*\n(.*?)```\s*\n\s*\*\*输出[：:]\*\*\s*\n```\s*\n(.*?)```",
        content, re.DOTALL)
    for inp, out in sample_blocks:
        samples.append({"input": inp.strip(), "output": out.strip()})
    if samples:
        result["samples"] = samples

    diff_match = re.search(r"\*\*难度[：:]\*\*\s*(\S+)", content)
    if diff_match:
        diff_map = {"简单": "Low", "中等": "Mid", "困难": "High"}
        result["difficulty"] = diff_map.get(diff_match.group(1), "Low")

    return result


def md_to_html(text: str) -> str:
    """简单 Markdown → HTML 转换（用于题面）"""
    if not text:
        return ""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"```(\w*)\n(.*?)```", r"<pre><code>\2</code></pre>", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    paragraphs = text.strip().split("\n\n")
    return "".join(f"<p>{p.replace(chr(10), '<br/>')}</p>" for p in paragraphs if p.strip())


def generate_test_case_zip(pid: int, chapter: int, output_dir: str) -> Optional[str]:
    """为题面中的样例生成测试数据 ZIP 文件"""
    prob_data = find_textbook_problem(pid, chapter)
    if not prob_data or "samples" not in prob_data:
        return None

    import zipfile
    zip_name = os.path.join(output_dir, f"testcases_ch{chapter}_nq{pid}.zip")
    with zipfile.ZipFile(zip_name, "w") as zf:
        for i, sample in enumerate(prob_data["samples"], 1):
            zf.writestr(f"{i}.in", sample["input"].encode("utf-8"))
            zf.writestr(f"{i}.out", sample["output"].encode("utf-8"))

    return zip_name


class SyncEngine:
    """同步引擎：本地书稿 → XMUOJ 云端"""

    def __init__(self, client, dry_run: bool = False, base_url: str = "http://xmuoj.com"):
        self.client = client
        self.dry_run = dry_run
        self.base_url = base_url
        self.stats = {"created": 0, "updated": 0, "skipped": 0, "errors": 0}
        # 预加载基线数据
        self._problems_data = load_problems_data()

    def sync_chapter(self, chapter: int, contest_id: Optional[int] = None):
        """同步一个章节的所有题目"""
        entries = V2_PLAN.get(chapter, [])
        if not entries:
            print(f"第{chapter}章：无题目定义")
            return

        title = CHAPTER_TITLES.get(chapter, f"第{chapter}章")
        print(f"\n{'='*60}")
        print(f"📖 第{chapter}章: {title} ({len(entries)}题)")
        print(f"{'='*60}")

        for i, entry in enumerate(entries, 1):
            display_id, source_type, _ = normalize_pid(entry)
            global_seq = get_nq_sequential_num(chapter, i)
            print(f"\n  [{i}/{len(entries)}] {display_id} (NQ{global_seq:03d})")

            # Check existing
            existing = self._get_problem_by_display_id(display_id)

            # Build problem data
            prob_data = self._build_problem(entry, chapter, i)

            if existing:
                if self.dry_run:
                    print(f"    [DRY RUN] 将更新 id={existing.get('id', '?')}")
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
            import requests
            resp = requests.get(
                f"{self.base_url}/api/problem",
                params={"problem_id": display_id},
                timeout=10
            )
            data = resp.json()
            if data.get("error") is None and data.get("data"):
                return data["data"]
        except Exception:
            pass
        return None

    def _build_problem(self, entry, chapter: int, order: int) -> Dict:
        """构建完整的题目数据

        Args:
            entry: V2_PLAN条目（int或dict）
            chapter: 章节编号
            order: 章节内序号（1-based）

        Returns:
            与 problem_builder.py PROBLEM_TEMPLATE 一致的嵌套格式
        """
        display_id, source_type, original = normalize_pid(entry)
        global_seq = get_nq_sequential_num(chapter, order)

        # 默认值
        title = display_id
        desc = f"<p>{display_id}</p>"
        input_desc = ""
        output_desc = ""
        samples = []
        difficulty = "Low"
        tags = []
        hint = ""

        # 1. 从 all_problems_data.json 加载描述（最可靠）
        if source_type == "acw" and self._problems_data:
            ch_str = str(chapter)
            acw_id = str(original)
            ch_data = self._problems_data.get(ch_str, {})
            prob = ch_data.get(acw_id, {})
            if prob:
                title = prob.get("title", title)
                desc = md_to_html(prob.get("description", "")) or desc
                input_desc = md_to_html(prob.get("input_description", "")) or ""
                output_desc = md_to_html(prob.get("output_description", "")) or ""
                samples = prob.get("samples", [])
                hint = md_to_html(prob.get("hint", "")) or ""
                raw_diff = prob.get("difficulty", "Low")
                difficulty = raw_diff if raw_diff in ("Low", "Mid", "High") else "Low"
                raw_tags = prob.get("tags", [])
                tags = raw_tags if isinstance(raw_tags, list) else []

        # 2. 对于 NQ 自定义题，从 dict 获取标题
        if source_type == "nq":
            title = original.get("title", display_id)

        # 3. 尝试从 xmuoj.com 获取现成数据作为补充（仅 online 模式）
        if self.base_url != "http://localhost":
            try:
                import requests
                resp = requests.get(
                    f"{self.base_url}/api/problem",
                    params={"problem_id": display_id},
                    timeout=5
                )
                data = resp.json()
                if data.get("error") is None and data.get("data"):
                    prob = data["data"]
                    # 只有本地数据为空时才用远程数据填充
                    if title == display_id:
                        title = prob.get("title", title)
                    if desc == f"<p>{display_id}</p>":
                        desc = prob.get("description", desc)
                    if not input_desc:
                        input_desc = prob.get("input_description", "")
                    if not output_desc:
                        output_desc = prob.get("output_description", "")
                    if not samples:
                        samples = prob.get("samples", [])
                    if not tags:
                        tags = prob.get("tags", [])
            except Exception:
                pass

        # 使用嵌套 HTML 格式（与 problem_builder.py 一致）
        return {
            "_id": display_id,
            "title": title,
            "description": {"format": "html", "value": desc if desc else f"<p>{display_id}</p>"},
            "input_description": {"format": "html", "value": input_desc or "<p></p>"},
            "output_description": {"format": "html", "value": output_desc or "<p></p>"},
            "samples": samples if samples else [{"input": "", "output": ""}],
            "test_case_id": "",
            "time_limit": 1000,
            "memory_limit": 256,
            "languages": ["C", "C++", "Python3"],
            "template": {},
            "rule_type": "OI",
            "io_mode": {"io_mode": "Standard IO", "input": "input.txt", "output": "output.txt"},
            "spj": False,
            "spj_language": None,
            "spj_code": None,
            "spj_compile_ok": False,
            "visible": True,
            "difficulty": difficulty,
            "tags": tags,
            "hint": {"format": "html", "value": hint or ""},
            "source": f"NQ{global_seq:03d} | 第{chapter}章",
            "share_submission": False,
        }

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
