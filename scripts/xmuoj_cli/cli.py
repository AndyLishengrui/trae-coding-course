#!/usr/bin/env python3
"""
XMUOJ CLI — 题库管理工具链
================================
用法：
  python cli.py login <username> <password>
  python cli.py problem create --id ACW001 --title "A+B" --desc-file desc.html ...
  python cli.py problem update --id 123 --title "New Title"
  python cli.py problem delete 123
  python cli.py problem list [--keyword xxx]
  python cli.py problem get 123
  python cli.py testcase upload <problem_id> <zip_path>
  python cli.py testcase download <problem_id> [--output ./]
  python cli.py sync --plan ../COURSE_PLAN_V2.md --chapter 1
  python cli.py validate --chapter 1 --lang cpp
  python cli.py validate --chapter 1 --lang python

配置文件：~/.xmuoj_cli_config.json (自动保存 token)
"""
import argparse
import json
import os
import sys
import re
import time
from pathlib import Path
from typing import Dict, List, Optional

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent))
from client import XmuojClient

CONFIG_PATH = Path.home() / ".xmuoj_cli_config.json"
BOOK_ROOT = Path(__file__).parent.parent.parent  # project root

# Global flag for local mode
_USE_LOCAL = False


def set_local_mode(enabled: bool):
    global _USE_LOCAL
    _USE_LOCAL = enabled


def get_client() -> XmuojClient:
    """获取已认证的客户端"""
    base_url = "http://localhost" if _USE_LOCAL else "http://xmuoj.com"
    client = XmuojClient(config_path=str(CONFIG_PATH), base_url=base_url)
    if not client._token:
        print("❌ 未登录！请先运行: python cli.py login <username> <password>")
        sys.exit(1)
    return client


# ====== Login ======

def cmd_login(args):
    client = XmuojClient()
    try:
        resp = client.login(args.username, args.password)
        client.save_config(str(CONFIG_PATH))
        print(f"✅ 登录成功！用户: {resp.get('username', args.username)}")
    except Exception as e:
        print(f"❌ 登录失败: {e}")
        sys.exit(1)


# ====== Problem CRUD ======

DEFAULT_PROBLEM = {
    "_id": "",
    "title": "",
    "description": "<p></p>",
    "input_description": "<p></p>",
    "output_description": "<p></p>",
    "samples": [{"input": "", "output": ""}],
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
    "difficulty": "Low",
    "tags": [],
    "hint": "",
    "source": "",
    "share_submission": False,
}


def build_problem_from_args(args) -> Dict:
    """从命令行参数构建 problem dict"""
    p = DEFAULT_PROBLEM.copy()
    if hasattr(args, '_id') and args._id: p["_id"] = args._id
    if hasattr(args, 'title') and args.title: p["title"] = args.title
    if hasattr(args, 'difficulty') and args.difficulty: p["difficulty"] = args.difficulty
    if hasattr(args, 'time_limit') and args.time_limit: p["time_limit"] = args.time_limit
    if hasattr(args, 'memory_limit') and args.memory_limit: p["memory_limit"] = args.memory_limit
    if hasattr(args, 'tags') and args.tags: p["tags"] = args.tags.split(",")
    if hasattr(args, 'source') and args.source: p["source"] = args.source
    if hasattr(args, 'hint') and args.hint: p["hint"] = args.hint
    if hasattr(args, 'test_case_id') and args.test_case_id: p["test_case_id"] = args.test_case_id
    if hasattr(args, 'languages') and args.languages: p["languages"] = args.languages.split(",")

    # Read description files if provided
    if hasattr(args, 'desc_file') and args.desc_file:
        p["description"] = Path(args.desc_file).read_text(encoding="utf-8")
    if hasattr(args, 'input_file') and args.input_file:
        p["input_description"] = Path(args.input_file).read_text(encoding="utf-8")
    if hasattr(args, 'output_file') and args.output_file:
        p["output_description"] = Path(args.output_file).read_text(encoding="utf-8")

    # Read samples from JSON file or inline
    if hasattr(args, 'samples_file') and args.samples_file:
        p["samples"] = json.loads(Path(args.samples_file).read_text())

    return p


def cmd_problem_create(args):
    client = get_client()
    problem = build_problem_from_args(args)
    try:
        result = client.create_problem(problem)
        pid = result.get("id") if isinstance(result, dict) else result
        print(f"✅ 题目创建成功！ID: {pid}")
        return result
    except Exception as e:
        print(f"❌ 创建失败: {e}")
        sys.exit(1)


def cmd_problem_update(args):
    client = get_client()
    problem = build_problem_from_args(args)
    problem["id"] = args.id
    try:
        client.update_problem(problem)
        print(f"✅ 题目 #{args.id} 更新成功！")
    except Exception as e:
        print(f"❌ 更新失败: {e}")
        sys.exit(1)


def cmd_problem_delete(args):
    client = get_client()
    try:
        client.delete_problem(args.id)
        print(f"✅ 题目 #{args.id} 已删除！")
    except Exception as e:
        print(f"❌ 删除失败: {e}")
        sys.exit(1)


def cmd_problem_list(args):
    client = get_client()
    try:
        result = client.list_problems(keyword=args.keyword or "", limit=args.limit or 100)
        if isinstance(result, dict) and "results" in result:
            problems = result["results"]
            total = result.get("total", len(problems))
        elif isinstance(result, list):
            problems = result
            total = len(problems)
        else:
            problems = []
            total = 0
        print(f"📋 题目列表 (共 {total} 题):")
        for p in problems:
            pid = p.get("_id", p.get("id", "?"))
            title = p.get("title", "?")
            diff = p.get("difficulty", "?")
            print(f"  [{pid}] {title} ({diff})")
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        sys.exit(1)


def cmd_problem_get(args):
    client = get_client()
    try:
        if args.id:
            result = client.get_problem(problem_id=args.id)
        else:
            result = client.get_problem(display_id=args.display_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        sys.exit(1)


# ====== Test Case ======

def cmd_testcase_upload(args):
    client = get_client()
    try:
        result = client.upload_test_cases(args.zip_path, spj=args.spj)
        tc_id = result.get("id") if isinstance(result, dict) else result
        print(f"✅ 测试数据上传成功！test_case_id: {tc_id}")
        print(f"   请将 test_case_id 更新到题目中")
    except Exception as e:
        print(f"❌ 上传失败: {e}")
        sys.exit(1)


def cmd_testcase_download(args):
    client = get_client()
    try:
        path = client.download_test_cases(args.problem_id, args.output or ".")
        print(f"✅ 测试数据已下载到: {path}")
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        sys.exit(1)


# ====== Submit & Validate ======

def cmd_submit(args):
    client = get_client()
    try:
        code = Path(args.file).read_text(encoding="utf-8")
        result = client.submit(
            problem_id=args.problem_id,
            code=code,
            language=args.lang,
            contest_id=args.contest_id,
        )
        sub_id = result.get("submission_id", result.get("id", ""))
        print(f"📤 提交成功！submission_id: {sub_id}")
        return sub_id
    except Exception as e:
        print(f"❌ 提交失败: {e}")
        sys.exit(1)


def cmd_check(args):
    """查询提交结果"""
    client = get_client()
    try:
        result = client.get_submission(args.submission_id)
        data = result if isinstance(result, dict) else {}
        status = data.get("result", data.get("status", "unknown"))
        print(f"📊 提交状态: {status}")
        if "statistic_info" in data:
            print(json.dumps(data["statistic_info"], indent=2))
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        sys.exit(1)


# ====== Contest (实验) CRUD ======

def cmd_contest_create(args):
    """创建实验/比赛"""
    client = get_client()
    contest = {
        "title": args.title,
        "description": args.description or f"<p>{args.title}</p>",
        "start_time": args.start_time or "2024-01-01T00:00:00+08:00",
        "end_time": args.end_time or "2099-12-31T23:59:59+08:00",
        "rule_type": args.rule_type or "ACM",
        "password": args.password or "",
        "visible": not args.hidden,
        "real_time_rank": not args.no_rank,
        "allowed_ip_ranges": args.allowed_ips.split(",") if args.allowed_ips else [],
    }
    try:
        result = client.create_contest(contest)
        cid = result.get("id") if isinstance(result, dict) else result
        print(f"✅ 实验创建成功！")
        print(f"   ID: {cid}")
        print(f"   标题: {args.title}")
        print(f"   类型: {contest['rule_type']}")
        print(f"   可见: {contest['visible']}")
        return result
    except Exception as e:
        print(f"❌ 创建失败: {e}")
        sys.exit(1)


def cmd_contest_update(args):
    """更新实验"""
    client = get_client()
    try:
        # Get existing contest first
        existing = client.get_contest(args.id)
        contest = {
            "id": args.id,
            "title": args.title or existing.get("title", ""),
            "description": args.description or existing.get("description", ""),
            "start_time": args.start_time or existing.get("start_time", "2024-01-01T00:00:00+08:00"),
            "end_time": args.end_time or existing.get("end_time", "2099-12-31T23:59:59+08:00"),
            "password": args.password if args.password is not None else existing.get("password", ""),
            "visible": existing.get("visible", True) if not hasattr(args, 'hidden') or not args.hidden else False,
            "real_time_rank": existing.get("real_time_rank", False),
            "allowed_ip_ranges": existing.get("allowed_ip_ranges", []),
        }
        if hasattr(args, 'hidden') and args.hidden:
            contest["visible"] = False
        if hasattr(args, 'no_rank') and args.no_rank:
            contest["real_time_rank"] = False
        client.update_contest(contest)
        print(f"✅ 实验 #{args.id} 更新成功！")
    except Exception as e:
        print(f"❌ 更新失败: {e}")
        sys.exit(1)


def cmd_contest_delete(args):
    """删除实验"""
    client = get_client()
    try:
        contest_id = args.id

        if args.hard:
            # 进行中的实验需要先结束才能硬删除
            try:
                existing = client.get_contest(contest_id)
                if isinstance(existing, dict):
                    status = existing.get("status")
                    # status 0 = underway, 先结束
                    client.update_contest({
                        "id": contest_id,
                        "title": existing.get("title", ""),
                        "description": existing.get("description", ""),
                        "start_time": "2020-01-01T00:00:00+08:00",
                        "end_time": "2020-01-02T00:00:00+08:00",
                        "password": existing.get("password", ""),
                        "visible": existing.get("visible", True),
                        "real_time_rank": existing.get("real_time_rank", False),
                        "allowed_ip_ranges": existing.get("allowed_ip_ranges", []),
                    })
                    print(f"  ⏸️  已结束实验 (状态: {status})")
            except:
                pass

            client.delete_contest(contest_id, hard=True)
            print(f"✅ 实验 #{contest_id} 已彻底删除！")
        else:
            client.delete_contest(contest_id, hard=False)
            print(f"✅ 实验 #{contest_id} 已软删除（仍可恢复）")

    except Exception as e:
        print(f"❌ 删除失败: {e}")
        sys.exit(1)


def cmd_contest_list(args):
    """列出实验"""
    client = get_client()
    try:
        result = client.list_contests(keyword=args.keyword or "")
        if isinstance(result, dict) and "results" in result:
            contests = result["results"]
            total = result.get("total", len(contests))
        elif isinstance(result, list):
            contests = result
            total = len(contests)
        else:
            contests, total = [], 0
        print(f"📋 实验列表 (共 {total} 个):")
        for c in contests:
            cid = c.get("id", "?")
            title = c.get("title", "?")
            status = c.get("status", "?")
            rule = c.get("rule_type", "?")
            print(f"  [{cid}] {title} ({rule}, {status})")
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        sys.exit(1)


def cmd_contest_get(args):
    """查看实验详情"""
    client = get_client()
    try:
        result = client.get_contest(args.id)
        if isinstance(result, dict):
            print(f"📖 实验 #{args.id}: {result.get('title', '?')}")
            print(f"   描述: {result.get('description', '')[:100]}...")
            print(f"   类型: {result.get('rule_type', '?')}")
            print(f"   状态: {result.get('status', '?')}")
            print(f"   开始: {result.get('start_time', '?')}")
            print(f"   结束: {result.get('end_time', '?')}")
            print(f"   可见: {result.get('visible', '?')}")
            print(f"   创建者: {result.get('created_by', {}).get('username', '?')}")
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        sys.exit(1)


def cmd_contest_add_problem(args):
    """向实验添加题目"""
    client = get_client()
    try:
        # Look up problem by display_id first
        prob = client.get_problem(display_id=args.display_id)
        if not prob or not isinstance(prob, dict) or not prob.get("id"):
            print(f"❌ 题目 {args.display_id} 不存在")
            sys.exit(1)

        problem_data = {
            "contest_id": args.contest_id,
            "problem_id": prob["id"],
            "display_id": args.order or args.display_id,
        }
        result = client.create_contest_problem(problem_data)
        print(f"✅ 已将 {args.display_id} 添加到实验 #{args.contest_id}")
    except Exception as e:
        print(f"❌ 添加失败: {e}")
        sys.exit(1)


def cmd_contest_remove_problem(args):
    """从实验移除题目"""
    client = get_client()
    try:
        # Find contest_problem by listing and matching
        problems = client.list_contest_problems(args.contest_id)
        if isinstance(problems, dict):
            probs = problems.get("results", problems.get("data", []))
        else:
            probs = problems if isinstance(problems, list) else []

        target = None
        for p in probs:
            if str(p.get("id")) == str(args.id):
                target = p
                break

        if target:
            client.remove_contest_problem(target["id"])
            title = target.get("title", args.id)
            print(f"✅ 已从实验 #{args.contest_id} 移除: {title}")
        else:
            print(f"❌ 未找到题目 #{args.id}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ 移除失败: {e}")
        sys.exit(1)


def cmd_contest_list_problems(args):
    """列出实验中的所有题目"""
    client = get_client()
    try:
        result = client.list_contest_problems(args.contest_id)
        if isinstance(result, dict):
            probs = result.get("results", result.get("data", []))
        else:
            probs = result if isinstance(result, list) else []

        contest_info = client.get_contest(args.contest_id)
        title = contest_info.get("title", f"实验#{args.contest_id}") if isinstance(contest_info, dict) else f"实验#{args.contest_id}"
        print(f"📋 {title} — 题目列表 ({len(probs)} 题):")
        for i, p in enumerate(probs, 1):
            pid = p.get("display_id", p.get("_id", p.get("id", "?")))
            ptitle = p.get("title", "?")
            diff = p.get("difficulty", "")
            print(f"  {i:3d}. [{pid}] {ptitle} ({diff})")
    except Exception as e:
        print(f"❌ 查询失败: {e}")
        sys.exit(1)


def cmd_contest_reorder(args):
    """调整实验中题目的顺序"""
    client = get_client()
    try:
        # Get current problems
        result = client.list_contest_problems(args.contest_id)
        if isinstance(result, dict):
            probs = result.get("results", result.get("data", []))
        else:
            probs = result if isinstance(result, list) else []

        if not probs:
            print("实验中没有题目")
            return

        # Parse new order: comma-separated display_ids
        new_order = args.order.split(",")
        print(f"📋 调整实验 #{args.contest_id} 题目顺序:")
        for i, did in enumerate(new_order, 1):
            did = did.strip()
            for p in probs:
                p_did = str(p.get("display_id", p.get("_id", "")))
                if p_did == did or str(p.get("id")) == did:
                    client.update_contest_problem({
                        "id": p["id"],
                        "contest_id": args.contest_id,
                        "display_id": f"{i:03d}_{did}",
                    })
                    print(f"  {i}. {did} ({p.get('title', '?')})")
                    break
            else:
                print(f"  ⚠️  未找到题目: {did}")
        print("✅ 顺序调整完成")
    except Exception as e:
        print(f"❌ 调整失败: {e}")
        sys.exit(1)


# ====== Sync ======

def cmd_sync(args):
    """同步书稿题目到XMUOJ"""
    import json
    from sync_engine import SyncEngine

    dry_run = args.dry_run
    if dry_run:
        engine = SyncEngine(None, dry_run=True)
        chapters = [args.chapter] if args.chapter else range(1, 17)
        for ch in chapters:
            if isinstance(ch, str): ch = int(ch)
            engine.sync_chapter(ch)
        engine.print_summary()
        return

    client = get_client()

    # V2 plan from COURSE_PLAN_V2.md
    v2_plan = {
        1: [1,608,604,606,609,615,616,653,654,605,611,612,613,614],
        2: [665,660,659,664,667,669,670,657,671,662,666,668,672,663],
        3: [708,709,712,714,716,721,720,724,723,710,711,718,715,713],
        4: [737,738,739,743,740,741,742,744,717,722,725,726],
        5: [745,747,749,751,753,748,746,750,752,754,755,756],
        6: [760,761,763,765,769,773,772,762,767,764,770,774],
        7: [804,805,808,811,812,813,819,820,821,822,823,818],
        8: [16,17,20,21,35,36,862,810,814,816],
        9: [785,786,787,788,789,790,727],
        10: [795,796,797,798,799,800,2816],
        11: [791,792,801,793,794,802,803],
        12: [826,828,829,3302,830,154,831,839],
        13: [842,843,844,845,846,847,777,778],
        14: [848,849,850,851,854,858,859,860],
        15: [2,3,898,895,897,282,902,901],
        16: [905,148,836,837,240,875,868,104],
    }

    chapters = [args.chapter] if args.chapter else range(1, 17)
    dry_run = args.dry_run
    created = 0

    for ch in chapters:
        if isinstance(ch, str): ch = int(ch)
        pids = v2_plan[ch]
        print(f"\n📖 第{ch}章 ({len(pids)}题):")
        for pid in pids:
            display_id = f"ACW{pid}"
            if dry_run:
                print(f"  [DRY RUN] 创建/更新 {display_id}")
                created += 1
            else:
                try:
                    # Check if exists
                    existing = None
                    try:
                        existing = client.get_problem(display_id=display_id)
                    except:
                        pass

                    if existing and isinstance(existing, dict) and existing.get("id"):
                        print(f"  ⏭️  跳过 {display_id} (已存在, id={existing['id']})")
                    else:
                        # TODO: Build problem from textbook data
                        print(f"  ⚠️  待创建 {display_id} (需要完整题面数据)")
                except Exception as e:
                    print(f"  ❌ {display_id}: {e}")

    print(f"\n{'[DRY RUN] ' if dry_run else ''}共 {created} 题待同步")
    if dry_run:
        print("使用 --no-dry-run 执行实际同步")


# ====== Validate ======

def cmd_validate(args):
    """自动验证 AC 代码"""
    client = get_client()
    chapters = [args.chapter] if args.chapter else range(1, 17)
    lang = args.lang or "cpp"
    lang_map = {"cpp": "C++", "python": "Python3", "c": "C"}

    oj_lang = lang_map.get(lang, "C++")
    results = {"AC": 0, "WA": 0, "TLE": 0, "ERR": 0, "PEND": 0}
    total = 0

    v2_plan = {
        1: [1,608,604,606,609,615,616,653,654,605,611,612,613,614],
        2: [665,660,659,664,667,669,670,657,671,662,666,668,672,663],
    }

    for ch in chapters:
        if isinstance(ch, str): ch = int(ch)
        pids = v2_plan.get(ch, [])
        print(f"\n📖 第{ch}章验证 ({len(pids)}题, {lang}):")

        for pid in pids:
            total += 1
            display_id = f"ACW{pid}"

            # Get problem from OJ
            try:
                prob = client.get_problem(display_id=display_id)
                if not prob or not isinstance(prob, dict):
                    print(f"  ⚠️  ACW{pid}: 题目不存在于 OJ")
                    results["ERR"] += 1
                    continue
                pid_int = prob.get("id")
            except:
                print(f"  ⚠️  ACW{pid}: 查询失败")
                results["ERR"] += 1
                continue

            # Find local code file
            ext = ".cpp" if lang == "cpp" else ".py"
            code_file = find_code_file(pid, ext)
            if not code_file:
                print(f"  ⚠️  ACW{pid}: 本地无{lang}代码")
                results["ERR"] += 1
                continue

            # Submit
            code = Path(code_file).read_text(encoding="utf-8")
            try:
                sub_result = client.submit(pid_int, code, oj_lang)
                sub_id = sub_result.get("submission_id", sub_result.get("id", ""))
                print(f"  📤 ACW{pid}: 已提交 ({sub_id})...", end=" ")

                # Wait for result
                for _ in range(20):  # max 60 seconds
                    time.sleep(3)
                    status = client.get_submission(sub_id)
                    if isinstance(status, dict):
                        result = status.get("result", -2)
                        if result != -1 and result != -2:  # not pending/judging
                            if result == 0:
                                print("✅ AC")
                                results["AC"] += 1
                            else:
                                print(f"❌ {result}")
                                results["WA"] += 1
                            break
                else:
                    print("⏰ 超时")
                    results["PEND"] += 1
            except Exception as e:
                print(f"❌ 提交失败: {e}")
                results["ERR"] += 1

    print(f"\n{'='*40}")
    print(f"验证结果: {total}题 | AC:{results['AC']} | WA:{results['WA']} | ERR:{results['ERR']} | 待定:{results['PEND']}")


def find_code_file(pid: int, ext: str) -> Optional[str]:
    """在项目中查找题目的代码文件"""
    for d in ["lessons_v2", "acwing_codes", "algorithm_basic_codes"]:
        for root, dirs, files in os.walk(str(BOOK_ROOT / d)):
            for f in files:
                if f.endswith(ext) and f"acw{pid}" in f.lower():
                    return os.path.join(root, f)
    return None


# ====== Main ======

def main():
    parser = argparse.ArgumentParser(description="XMUOJ CLI — 题库管理工具链")
    parser.add_argument("--local", action="store_true", help="使用本地 Docker XMUOJ (http://localhost)")
    sub = parser.add_subparsers(dest="command", help="可用命令")

    # Login
    p = sub.add_parser("login", help="登录获取 token")
    p.add_argument("username")
    p.add_argument("password")
    p.set_defaults(func=cmd_login)

    # Problem CRUD
    p = sub.add_parser("create", help="创建题目")
    p.add_argument("--_id", required=True, help="题目显示ID (如 ACW785)")
    p.add_argument("--title", required=True, help="题目标题")
    p.add_argument("--desc-file", help="题目描述 HTML 文件")
    p.add_argument("--input-file", help="输入格式 HTML 文件")
    p.add_argument("--output-file", help="输出格式 HTML 文件")
    p.add_argument("--samples-file", help="样例 JSON 文件")
    p.add_argument("--difficulty", default="Low", choices=["Low", "Mid", "High"])
    p.add_argument("--time-limit", type=int, default=1000, help="时间限制(ms)")
    p.add_argument("--memory-limit", type=int, default=256, help="内存限制(MB)")
    p.add_argument("--tags", help="标签，逗号分隔")
    p.add_argument("--source", help="题目来源")
    p.add_argument("--languages", default="C,C++,Python3", help="支持语言")
    p.add_argument("--test-case-id", help="测试数据 ID")
    p.set_defaults(func=lambda a: cmd_problem_create(a))

    p = sub.add_parser("update", help="更新题目")
    p.add_argument("--id", type=int, required=True, help="题目数据库 ID")
    p.add_argument("--_id", help="显示ID")
    p.add_argument("--title", help="标题")
    p.add_argument("--difficulty", choices=["Low", "Mid", "High"])
    p.add_argument("--desc-file", help="新描述文件")
    p.set_defaults(func=lambda a: cmd_problem_update(a))

    p = sub.add_parser("delete", help="删除题目")
    p.add_argument("id", type=int, help="题目数据库 ID")
    p.set_defaults(func=lambda a: cmd_problem_delete(a))

    p = sub.add_parser("list", help="列出题目")
    p.add_argument("--keyword", help="搜索关键词")
    p.add_argument("--limit", type=int, default=100)
    p.set_defaults(func=lambda a: cmd_problem_list(a))

    p = sub.add_parser("get", help="查看题目详情")
    p.add_argument("--id", type=int, help="数据库 ID")
    p.add_argument("--display-id", help="显示 ID (如 ACW785)")
    p.set_defaults(func=lambda a: cmd_problem_get(a))

    # Test Case
    p = sub.add_parser("upload-testcase", help="上传测试数据")
    p.add_argument("zip_path", help="测试数据 ZIP 文件路径")
    p.add_argument("--spj", action="store_true", help="是否为 Special Judge")
    p.set_defaults(func=lambda a: cmd_testcase_upload(a))

    p = sub.add_parser("download-testcase", help="下载测试数据")
    p.add_argument("problem_id", type=int, help="题目数据库 ID")
    p.add_argument("--output", "-o", help="输出目录")
    p.set_defaults(func=lambda a: cmd_testcase_download(a))

    # Contest (实验) Management
    p = sub.add_parser("contest", help="实验管理")
    cs = p.add_subparsers(dest="contest_cmd", help="实验操作")

    c = cs.add_parser("create", help="创建实验")
    c.add_argument("--title", required=True, help="实验标题")
    c.add_argument("--description", help="实验描述 (HTML)")
    c.add_argument("--start-time", help="开始时间 (ISO格式)")
    c.add_argument("--end-time", help="结束时间 (ISO格式)")
    c.add_argument("--rule-type", default="ACM", choices=["ACM", "OI"])
    c.add_argument("--password", help="进入密码")
    c.add_argument("--hidden", action="store_true", help="隐藏实验")
    c.add_argument("--no-rank", action="store_true", help="禁用实时排名")
    c.add_argument("--allowed-ips", help="允许的IP段(CIDR)，逗号分隔")
    c.set_defaults(func=lambda a: cmd_contest_create(a))

    c = cs.add_parser("update", help="更新实验")
    c.add_argument("--id", type=int, required=True, help="实验 ID")
    c.add_argument("--title", help="新标题")
    c.add_argument("--description", help="新描述")
    c.add_argument("--start-time", help="开始时间")
    c.add_argument("--end-time", help="结束时间")
    c.add_argument("--password", help="新密码")
    c.add_argument("--hidden", action="store_true", help="隐藏")
    c.set_defaults(func=lambda a: cmd_contest_update(a))

    c = cs.add_parser("delete", help="删除实验")
    c.add_argument("id", type=int, help="实验 ID")
    c.add_argument("--hard", action="store_true", help="彻底删除（默认软删除）")
    c.set_defaults(func=lambda a: cmd_contest_delete(a))

    c = cs.add_parser("list", help="列出实验")
    c.add_argument("--keyword", help="搜索关键词")
    c.set_defaults(func=lambda a: cmd_contest_list(a))

    c = cs.add_parser("get", help="查看实验详情")
    c.add_argument("id", type=int, help="实验 ID")
    c.set_defaults(func=lambda a: cmd_contest_get(a))

    c = cs.add_parser("add-problem", help="添加题目到实验")
    c.add_argument("--contest-id", type=int, required=True, help="实验 ID")
    c.add_argument("--display-id", required=True, help="题目显示 ID (如 ACW785)")
    c.add_argument("--order", help="排序号")
    c.set_defaults(func=lambda a: cmd_contest_add_problem(a))

    c = cs.add_parser("remove-problem", help="从实验移除题目")
    c.add_argument("--contest-id", type=int, required=True, help="实验 ID")
    c.add_argument("--id", required=True, help="题目 ID 或 display_id")
    c.set_defaults(func=lambda a: cmd_contest_remove_problem(a))

    c = cs.add_parser("problems", help="列出实验中的题目")
    c.add_argument("contest_id", type=int, help="实验 ID")
    c.set_defaults(func=lambda a: cmd_contest_list_problems(a))

    c = cs.add_parser("reorder", help="调整实验题目顺序")
    c.add_argument("--contest-id", type=int, required=True, help="实验 ID")
    c.add_argument("--order", required=True, help="新顺序，逗号分隔的 display_id")
    c.set_defaults(func=lambda a: cmd_contest_reorder(a))

    # Submit & Check
    p = sub.add_parser("submit", help="提交代码")
    p.add_argument("problem_id", type=int, help="题目数据库 ID")
    p.add_argument("file", help="代码文件路径")
    p.add_argument("--lang", default="C++", choices=["C", "C++", "Python3", "Java", "Go"])
    p.add_argument("--contest-id", type=int, help="比赛 ID")
    p.set_defaults(func=lambda a: cmd_submit(a))

    p = sub.add_parser("check", help="查询提交结果")
    p.add_argument("submission_id", help="提交 ID")
    p.set_defaults(func=lambda a: cmd_check(a))

    # Sync
    p = sub.add_parser("sync", help="同步书稿题目到 XMUOJ")
    p.add_argument("--chapter", "-c", type=int, help="指定章节 (默认全部)")
    p.add_argument("--dry-run", action="store_true", help="预览模式，不实际创建")
    p.set_defaults(func=lambda a: cmd_sync(a))

    # Validate
    p = sub.add_parser("validate", help="自动验证 AC 代码")
    p.add_argument("--chapter", "-c", type=int, help="指定章节")
    p.add_argument("--lang", default="cpp", choices=["cpp", "python", "c"], help="编程语言")
    p.set_defaults(func=lambda a: cmd_validate(a))

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    # Set local mode
    if args.local:
        set_local_mode(True)
        print("🔧 本地模式: http://localhost")

    args.func(args)


if __name__ == "__main__":
    main()
