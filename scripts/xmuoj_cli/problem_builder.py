"""
Problem JSON Builder — 将 Markdown 题面转换为 XMUOJ 标准 problem.json 格式

基于蓝桥杯集训营验证的16字段格式（经过数百道题的实战导入验证）。
"""
import json
import re
import os
from pathlib import Path
from typing import Dict, List, Optional


# 标准16字段模板
PROBLEM_TEMPLATE = {
    "display_id": "",
    "title": "",
    "description": {"format": "html", "value": ""},
    "tags": [],
    "input_description": {"format": "html", "value": ""},
    "output_description": {"format": "html", "value": ""},
    "test_case_score": [],
    "hint": {"format": "html", "value": ""},
    "time_limit": 1000,
    "memory_limit": 256,
    "samples": [],
    "template": {},
    "spj": None,       # 必须是 null，不能是 false！
    "rule_type": "OI",
    "source": "AcWing",
    "answers": [],
}


def md_to_html(text: str) -> str:
    """将 Markdown 文本转换为 HTML 格式"""
    if not text:
        return ""
    text = text.strip()
    # 跳过已经是 HTML 的内容
    if text.startswith("<p") or text.startswith("<h"):
        return text
    # 去掉 markdown 标题行 (## xxx)
    text = re.sub(r'^#{1,4}\s+[^\n]+\n', '', text, flags=re.MULTILINE)
    # 代码块
    text = re.sub(r'```(\w*)\n(.*?)```', r'<pre><code>\2</code></pre>', text, flags=re.DOTALL)
    # 行内代码
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # 粗体
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    # 段落
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "".join(f"<p>{p.replace(chr(10), '<br/>')}</p>" for p in paragraphs)


def build_test_case_score(num_cases: int = 10) -> List[Dict]:
    """生成 test_case_score 数组"""
    return [
        {"score": 10, "input_name": f"{i}.in", "output_name": f"{i}.out"}
        for i in range(1, num_cases + 1)
    ]


def extract_acwing_id(text: str) -> Optional[str]:
    """从文本中提取 AcWing 题号"""
    # "AcWing 785. 快速排序" → "ACW785"
    m = re.search(r'AcWing\s+(\d+)', text)
    if m:
        return f"ACW{m.group(1)}"
    # "ACW785" → "ACW785"
    m = re.search(r'ACW(\d+)', text)
    if m:
        return f"ACW{m.group(1)}"
    return None


def extract_title(text: str) -> str:
    """提取题目标题"""
    # "# AcWing 1. A + B — A + B" → "A + B"
    # "## NQ001：A + B" → "A + B"
    m = re.search(r'^#+\s*(.+)', text, re.MULTILINE)
    if m:
        title = m.group(1)
        # 去掉 "AcWing XXX. " 或 "AcWing XXX — " 前缀
        title = re.sub(r'AcWing\s+\d+[\.\s—–-]*\s*', '', title)
        # 去掉 "NQ001：" 或 "NQ001: " 前缀
        title = re.sub(r'NQ\d+[：:]\s*', '', title)
        # 如果 title 包含 " — "，取后面部分
        if " — " in title:
            title = title.split(" — ", 1)[1]
        return title.strip()
    # "AcWing 785. 快速排序" → "快速排序"
    m = re.search(r'AcWing\s+\d+\.\s*(.+)', text)
    if m:
        return m.group(1).strip()
    return text.strip()[:100]


def extract_samples(content: str) -> List[Dict]:
    """从 Markdown 中提取样例"""
    samples = []
    # 模式1: **输入：** ```...``` **输出：** ```...```
    pattern1 = re.compile(
        r'\*\*输入[：:]\*\*\s*```\s*\n(.*?)```\s*\n\s*\*\*输出[：:]\*\*\s*```\s*\n(.*?)```',
        re.DOTALL
    )
    for inp, out in pattern1.findall(content):
        samples.append({"input": inp.strip(), "output": out.strip()})

    # 模式2: ### 样例 中的 input/output 对
    if not samples:
        # 找样例区域
        sample_section = re.search(r'###\s*样例\s*(.*?)(?=###|\n---|\Z)', content, re.DOTALL)
        if sample_section:
            sample_text = sample_section.group(1)
            # 输入: ... 输出: ...
            pairs = re.findall(r'输入[：:]\s*\n```\s*\n(.*?)```.*?输出[：:]\s*\n```\s*\n(.*?)```', sample_text, re.DOTALL)
            for inp, out in pairs:
                samples.append({"input": inp.strip(), "output": out.strip()})

    return samples


def extract_section(content: str, heading: str) -> str:
    """提取 Markdown 中的指定章节（支持 ## 和 ### 级别）"""
    # 使用 format 避免 f-string 中大括号的转义问题
    pattern = r'#{2,3}\s*' + re.escape(heading) + r'\s*\n(.*?)(?=\n#{2,3}\s|\Z)'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def build_hint(content: str, display_id: str) -> str:
    """构建 hint 字段（含原题链接）"""
    parts = []
    # 提取 AcWing 题号生成链接
    acw_id = extract_acwing_id(content)
    if acw_id:
        num = acw_id.replace("ACW", "")
        parts.append(f'<a href="https://www.acwing.com/problem/content/{num}/" target="_blank">原题链接</a>')

    # 提取参考题解
    solution = extract_section(content, "解题思路")
    if solution:
        parts.append(f"<p>{solution[:500]}</p>")

    return "\n".join(parts) if parts else ""


def infer_tags(content: str, title: str) -> List[str]:
    """从内容推断算法标签"""
    text = (content + title).lower()
    tags = []

    tag_keywords = {
        "基础语法": ["输入输出", "变量", "运算符", "顺序结构", "a+b", "基本"],
        "排序": ["快速排序", "归并排序", "排序"],
        "二分": ["二分", "bisect", "bsearch"],
        "前缀和": ["前缀和", "前缀"],
        "差分": ["差分"],
        "双指针": ["双指针", "滑动窗口"],
        "贪心": ["贪心", "区间选点", "区间合并", "合并果子"],
        "动态规划": ["dp", "背包", "动态规划", "最长上升", "最长公共", "编辑距离", "石子合并"],
        "图论": ["最短路", "dijkstra", "spfa", "floyd", "prim", "kruskal", "拓扑排序", "二分图"],
        "搜索": ["dfs", "bfs", "回溯", "n皇后", "八数码"],
        "数据结构": ["链表", "栈", "队列", "单调栈", "单调队列", "并查集", "堆", "trie", "kmp", "哈希"],
        "数学": ["质数", "约数", "欧拉", "快速幂", "gcd", "高斯", "组合数", "博弈", "筛法"],
        "位运算": ["位运算", "二进制", "lowbit"],
        "高精度": ["高精度", "大整数"],
        "字符串": ["字符串", "kmp", "哈希"],
    }

    for tag, keywords in tag_keywords.items():
        if any(kw in text for kw in keywords):
            tags.append(tag)

    return tags if tags else ["基础语法"]


def build_from_markdown(md_content: str, num_test_cases: int = 10) -> Dict:
    """
    从 Markdown 题面构建标准 problem.json

    Args:
        md_content: 题面 Markdown 文本
        num_test_cases: 测试用例数量（默认10）

    Returns:
        16字段的 problem.json dict
    """
    display_id = extract_acwing_id(md_content) or "ACW0000"
    title = extract_title(md_content)
    tags = infer_tags(md_content, title)
    samples = extract_samples(md_content)

    # Try both ## and ### level headings
    description = extract_section(md_content, "题目描述") or \
                  extract_section(md_content, "描述") or ""
    if not description:
        # Try to find description between title and first subheading
        m = re.search(r'^#.*?\n\n(.*?)(?=\n##|\n###|\Z)', md_content, re.DOTALL)
        if m:
            desc_text = m.group(1).strip()
            # Skip metadata lines like "> 题目来源:..."
            desc_text = re.sub(r'^>.*$', '', desc_text, flags=re.MULTILINE).strip()
            if desc_text and len(desc_text) > 10:
                description = desc_text
    input_desc = extract_section(md_content, "输入格式") or ""
    output_desc = extract_section(md_content, "输出格式") or ""
    hint = build_hint(md_content, display_id)

    # If no description section found, use the content after the title
    if not description:
        # Take everything between the title and the first ### heading
        desc_match = re.search(r'^#.*?\n(.*?)(?=###|\n##)', md_content, re.DOTALL)
        if desc_match:
            description = desc_match.group(1).strip()

    return {
        "display_id": display_id,
        "title": title,
        "description": {"format": "html", "value": md_to_html(description)},
        "tags": tags,
        "input_description": {"format": "html", "value": md_to_html(input_desc)},
        "output_description": {"format": "html", "value": md_to_html(output_desc)},
        "test_case_score": build_test_case_score(num_test_cases),
        "hint": {"format": "html", "value": hint},
        "time_limit": 1000,
        "memory_limit": 256,
        "samples": samples,
        "template": {},
        "spj": None,
        "rule_type": "OI",
        "source": "AcWing",
        "answers": [],
    }


def build_from_file(md_path: str) -> Optional[Dict]:
    """从 Markdown 文件构建 problem.json"""
    path = Path(md_path)
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8")
    return build_from_markdown(content)


def save_problem_json(problem: Dict, output_path: str):
    """保存 problem.json 到文件"""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(problem, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )


# CLI entry point
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python problem_builder.py <markdown_file> [output.json]")
        sys.exit(1)

    md_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else md_file.replace(".md", ".json")
    problem = build_from_file(md_file)
    if problem:
        save_problem_json(problem, out_file)
        print(f"✅ {problem['display_id']}: {problem['title']}")
        print(f"   标签: {problem['tags']}")
        print(f"   样例: {len(problem['samples'])} 组")
        print(f"   输出: {out_file}")
    else:
        print(f"❌ 无法读取: {md_file}")
