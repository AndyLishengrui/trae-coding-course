#!/usr/bin/env python3
"""
章节处理器 — 修复题库元数据并同步到 OJ

用法:
  python3 process_chapter.py 16          # 处理第16章
  python3 process_chapter.py 16 --sync   # 处理并同步到OJ
  python3 process_chapter.py 14 15 16    # 批量处理多个章节
"""
import json, os, sys, re, shutil
from pathlib import Path
from typing import Dict, List

BOOK_ROOT = Path(__file__).parent.parent
DATA_DIR = Path(__file__).parent


def load_json(name):
    path = DATA_DIR / name
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def md_to_html(text):
    if not text:
        return ""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"```(\w*)\n(.*?)```", r"<pre><code>\2</code></pre>", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    paragraphs = text.strip().split("\n\n")
    return "".join(f"<p>{p.replace(chr(10), '<br/>')}</p>" for p in paragraphs if p.strip())


def process_chapter(ch, sync=False):
    """处理一个章节：构建NQ目录 + 修复problem.json + 生成problem.md"""
    all_data = load_json("all_problems_data.json")
    nq_map = load_json("nq_mapping.json")

    bank_dir = BOOK_ROOT / f"chapter{ch}_bank"
    os.makedirs(bank_dir, exist_ok=True)

    # 找到本章的所有 NQ 条目
    chapter_nqs = []
    for nq_id, info in nq_map.items():
        if info["ch"] == ch:
            chapter_nqs.append((nq_id, info))
    chapter_nqs.sort(key=lambda x: x[1]["idx"])

    if not chapter_nqs:
        print(f"第{ch}章：无题目定义")
        return [], []

    print(f"\n{'='*60}")
    print(f"📖 第{ch}章 ({len(chapter_nqs)}题)")
    print(f"{'='*60}")

    oj_updates = []
    results = []

    for nq_id, info in chapter_nqs:
        acw = info["acw"]
        idx = info["idx"]

        # 1. 从 all_problems_data.json 获取元数据
        ch_str = str(ch)
        acw_str = str(acw)
        baseline = all_data.get(ch_str, {}).get(acw_str, {})

        title = baseline.get("title", f"AcWing {acw}")
        desc = baseline.get("description", "")
        input_desc = baseline.get("input_description", "")
        output_desc = baseline.get("output_description", "")
        samples = baseline.get("samples", [])
        difficulty = baseline.get("difficulty", "Low")
        tags = baseline.get("tags", [])
        hint_raw = baseline.get("hint", "")
        hint = f'<a href="https://www.acwing.com/problem/content/{acw}/" target="_blank">{hint_raw or "原题链接"}</a>'

        # 2. 找到已有的 ACW 目录（复制代码文件）
        acw_dir = None
        for d in bank_dir.iterdir():
            if d.is_dir() and f"acw{acw}" in d.name.lower().replace("_", ""):
                acw_dir = d
                break

        # 3. 创建/更新 NQ 目录
        safe_title = re.sub(r'[^\w一-鿿]', '', title)[:30]
        nq_dir = bank_dir / f"{nq_id}.{safe_title}" if safe_title else bank_dir / nq_id
        os.makedirs(nq_dir, exist_ok=True)

        # 4. 复制代码文件（ACW目录已有高质量代码）
        for fname in ["Andy.cpp", "Andy.py", "gen.cpp"]:
            if acw_dir:
                src = acw_dir / fname
                if src.exists():
                    shutil.copy2(src, nq_dir / fname)

        # 5. 复制测试数据
        if acw_dir:
            src_tc = acw_dir / "testcase"
            dst_tc = nq_dir / "testcase"
            if src_tc.exists() and not dst_tc.exists():
                shutil.copytree(src_tc, dst_tc)

        # 6. 构建 problem.json
        test_case_score = [{"score": 10, "input_name": f"{i}.in", "output_name": f"{i}.out"} for i in range(1, 11)]

        problem = {
            "display_id": nq_id,
            "title": title,
            "description": {"format": "html", "value": md_to_html(desc)},
            "tags": tags,
            "input_description": {"format": "html", "value": md_to_html(input_desc)},
            "output_description": {"format": "html", "value": md_to_html(output_desc)},
            "test_case_score": test_case_score,
            "hint": {"format": "html", "value": hint},
            "time_limit": 1000,
            "memory_limit": 256,
            "samples": samples[:10] if samples else [{"input": "", "output": ""}],
            "template": {},
            "spj": None,
            "rule_type": "OI",
            "difficulty": difficulty if difficulty in ("Low", "Mid", "High") else "Low",
            "source": f"AcWing {acw} | {nq_id} | 第{ch}章",
            "allow_public_test_case_download": False,
            "answers": [],
        }

        pj_path = nq_dir / "problem.json"
        with open(pj_path, "w", encoding="utf-8") as f:
            json.dump(problem, f, ensure_ascii=False, indent=2)

        # 7. 生成 problem.md
        samples_text = ""
        for i, s in enumerate(samples[:3], 1):
            samples_text += f"""### 样例{i}
**输入：**
```
{s['input']}
```
**输出：**
```
{s['output']}
```

"""
        md = f"""# {nq_id}：{title}

> 题目来源：AcWing {acw} | 第{ch}章

---

## 题目描述
{desc}

### 输入格式
{input_desc or "见原题"}

### 输出格式
{output_desc or "见原题"}

{samples_text}---

## 参考代码

**C++ Code:** 见 `Andy.cpp`
**Python Code:** 见 `Andy.py`

> 原题链接：https://www.acwing.com/problem/content/{acw}/
"""
        (nq_dir / "problem.md").write_text(md, encoding="utf-8")

        # 8. 准备 OJ 同步数据（用 .format() 避免 f-string 反斜杠问题）
        def esc(s):
            return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n").replace("\r", "")
        title_esc = esc(title)
        desc_esc = esc(md_to_html(desc))
        inp_esc = esc(md_to_html(input_desc))
        out_esc = esc(md_to_html(output_desc))
        hint_esc = esc(hint)
        src_esc = esc("AcWing {} | {} | 第{}章".format(acw, nq_id, ch))
        # 样例数据作为 Python list 直接在脚本中构建
        safe_samples = samples[:10] if samples else [{"input": "", "output": ""}]
        escaped_samples = [{"input": esc(s["input"]), "output": esc(s["output"])} for s in safe_samples]
        samples_repr = repr(escaped_samples)

        # 用 get_or_create + update 两步：先创建/获取，再逐字段更新
        oj_updates.append("print('  Processing {}...')".format(nq_id))
        oj_updates.append("p, created = Problem.objects.get_or_create(_id='{}')".format(nq_id))
        oj_updates.append("p.title = '{}'".format(title_esc))
        oj_updates.append("p.description = '{}'".format(desc_esc))
        oj_updates.append("p.input_description = '{}'".format(inp_esc))
        oj_updates.append("p.output_description = '{}'".format(out_esc))
        oj_updates.append("p.hint = '{}'".format(hint_esc))
        oj_updates.append("p.difficulty = '{}'".format(difficulty))
        oj_updates.append("p.visible = True")
        oj_updates.append("p.is_public = True")
        oj_updates.append("p.time_limit = 1000")
        oj_updates.append("p.memory_limit = 256")
        oj_updates.append("p.source = '{}'".format(src_esc))
        oj_updates.append("p.samples = {}".format(samples_repr))
        oj_updates.append("p.save()")
        oj_updates.append("print('  ' + ('Created' if created else 'Updated') + ' {}: {}')".format(nq_id, title))

        tag = "✅" if title.startswith("AcWing") else "🔄"
        print(f"  {tag} {nq_id}: {title} (AcWing {acw}) [samples={len(samples)}, diff={difficulty}]")

        results.append({"nq_id": nq_id, "title": title, "acw": acw, "ok": True})

    print(f"\n  共处理 {len(results)} 题")

    return results, oj_updates


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("chapters", nargs="+", type=int, help="章节编号")
    parser.add_argument("--sync", action="store_true", help="同步到 localhost OJ")
    args = parser.parse_args()

    all_oj = ["import json", "from problem.models import Problem", ""]
    total = 0

    for ch in args.chapters:
        results, oj = process_chapter(ch)
        total += len(results)
        all_oj.extend(oj)

    print(f"\n{'='*60}")
    print(f"📊 总计: {total} 题")

    if args.sync and all_oj:
        script = "\n".join(all_oj)
        script_path = "/tmp/_oj_sync.py"
        Path(script_path).write_text(script, encoding="utf-8")
        print(f"同步脚本已写入 {script_path}")

        import subprocess
        result = subprocess.run(
            ["docker", "exec", "-i", "onlinejudgedeploy-oj-backend-1", "python", "manage.py", "shell"],
            input=script, capture_output=True, text=True, timeout=120
        )
        for line in result.stdout.split("\n"):
            if "Created" in line or "Updated" in line:
                print(f"  {line.strip()}")
        if result.stderr:
            err_lines = [l for l in result.stderr.split("\n") if "Error" in l and "Sentry" not in l]
            for l in err_lines[:5]:
                print(f"  ⚠️ {l.strip()[:100]}")
    elif args.sync:
        print("没有需要同步的数据")


if __name__ == "__main__":
    main()
