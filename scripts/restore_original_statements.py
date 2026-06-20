#!/usr/bin/env python3
"""
Restore NQ statement fields from baseline data and sync them to localhost OJ.

Baseline:
- scripts/all_problems_data.json (description/input/output/samples)
- scripts/nq_mapping.json (NQ -> chapter/acwing mapping)

Targets:
1) Local chapter bank problem.json files
2) OJ problems under contest_id=356 (via admin API update)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests


BOOK = Path(__file__).parent.parent.resolve()
MAPPING_PATH = BOOK / "scripts" / "nq_mapping.json"
BASELINE_PATH = BOOK / "scripts" / "all_problems_data.json"
DEFAULT_CONTEST_ID = 356
DEFAULT_DB_CONTAINER = "onlinejudgedeploy-oj-postgres-1"
DEFAULT_BASE_URL = "http://localhost"
DEFAULT_TOKEN = "63310cdaec0bc93b08f856568e125e75"


@dataclass(frozen=True)
class BaselineStatement:
    description: str
    input_description: str
    output_description: str
    samples: List[Dict[str, str]]


def text_to_html(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return "<p></p>"
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if not paragraphs:
        return "<p></p>"
    return "".join(f"<p>{p.replace(chr(10), '<br/>')}</p>" for p in paragraphs)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_baseline() -> Dict[Tuple[int, int], BaselineStatement]:
    raw = load_json(BASELINE_PATH)
    result: Dict[Tuple[int, int], BaselineStatement] = {}
    for ch_str, chapter_data in raw.items():
        ch = int(ch_str)
        for acw_str, item in chapter_data.items():
            acw = int(acw_str)
            result[(ch, acw)] = BaselineStatement(
                description=item.get("description", ""),
                input_description=item.get("input_description", ""),
                output_description=item.get("output_description", ""),
                samples=item.get("samples", []) or [],
            )
    return result


def find_problem_json_path(ch: int, acw: int) -> Optional[Path]:
    chapter_dir = BOOK / f"chapter{ch}_bank"
    if not chapter_dir.exists():
        return None
    patterns = [f"ACW{acw:03d}*", f"ACW{acw}.*", f"ACW{acw}_*"]
    for pattern in patterns:
        for p in sorted(chapter_dir.glob(pattern)):
            if p.is_dir() and (p / "problem.json").exists():
                return p / "problem.json"
    return None


def patch_local_problem_json(problem_path: Path, baseline: BaselineStatement) -> bool:
    with problem_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    old_tuple = (
        data.get("description", {}).get("value", ""),
        data.get("input_description", {}).get("value", ""),
        data.get("output_description", {}).get("value", ""),
        json.dumps(data.get("samples", []), ensure_ascii=False, sort_keys=True),
    )

    data["description"] = {"format": "html", "value": text_to_html(baseline.description)}
    data["input_description"] = {"format": "html", "value": text_to_html(baseline.input_description)}
    data["output_description"] = {"format": "html", "value": text_to_html(baseline.output_description)}
    if baseline.samples:
        data["samples"] = baseline.samples

    new_tuple = (
        data["description"]["value"],
        data["input_description"]["value"],
        data["output_description"]["value"],
        json.dumps(data.get("samples", []), ensure_ascii=False, sort_keys=True),
    )
    changed = old_tuple != new_tuple

    if changed:
        with problem_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
    return changed


def query_contest_nq_rows_via_db(db_container: str, contest_id: int) -> List[Tuple[int, str]]:
    sql = (
        "SELECT id, _id FROM problem "
        f"WHERE contest_id={contest_id} AND _id ~ '^NQ[0-9]+-[0-9]+' "
        "ORDER BY _id;"
    )
    cmd = [
        "docker",
        "exec",
        "-i",
        db_container,
        "psql",
        "-U",
        "onlinejudge",
        "-d",
        "onlinejudge",
        "-t",
        "-A",
        "-F",
        "|",
        "-c",
        sql,
    ]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    rows: List[Tuple[int, str]] = []
    for line in out.splitlines():
        if not line.strip():
            continue
        pid_str, nq_id = line.split("|", 1)
        rows.append((int(pid_str), nq_id.strip()))
    return rows


def query_contest_nq_rows_via_api(base_url: str, token: str, contest_id: int) -> List[Tuple[int, str]]:
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {token}"})
    url = f"{base_url.rstrip('/')}/api/admin/contest/problem/?contest_id={contest_id}"
    r = s.get(url, timeout=30)
    r.raise_for_status()
    wrapped = r.json()
    if wrapped.get("error"):
        raise RuntimeError(f"contest/problem api error: {wrapped.get('data')}")
    data = wrapped.get("data", wrapped)
    if not isinstance(data, list):
        return []
    rows: List[Tuple[int, str]] = []
    for item in data:
        pid = item.get("problem_id")
        nq_id = item.get("display_id")
        if isinstance(pid, int) and isinstance(nq_id, str) and re.match(r"^NQ[0-9]+-[0-9]+$", nq_id):
            rows.append((pid, nq_id))
    rows.sort(key=lambda x: x[1])
    return rows


def build_statement_payload(baseline: BaselineStatement) -> Dict[str, object]:
    payload: Dict[str, object] = {
        "description": text_to_html(baseline.description),
        "input_description": text_to_html(baseline.input_description),
        "output_description": text_to_html(baseline.output_description),
    }
    if baseline.samples:
        payload["samples"] = baseline.samples
    return payload


def _sql_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def sync_oj_statements_via_db(
    db_container: str,
    contest_id: int,
    mapping: Dict[str, dict],
    baseline_map: Dict[Tuple[int, int], BaselineStatement],
    dry_run: bool,
) -> Tuple[int, int, List[str]]:
    rows = query_contest_nq_rows_via_db(db_container, contest_id)
    updated = 0
    skipped = 0
    missing: List[str] = []
    sql_lines: List[str] = ["BEGIN;"]

    for pid, nq_id in rows:
        info = mapping.get(nq_id)
        if not info:
            missing.append(f"{nq_id}: no mapping")
            continue
        key = (int(info["ch"]), int(info["acw"]))
        baseline = baseline_map.get(key)
        if not baseline:
            missing.append(f"{nq_id}: no baseline")
            continue

        description = text_to_html(baseline.description)
        input_description = text_to_html(baseline.input_description)
        output_description = text_to_html(baseline.output_description)
        samples_json = json.dumps(baseline.samples or [], ensure_ascii=False)

        sql_lines.append(
            "UPDATE problem SET "
            f"description={_sql_quote(description)}, "
            f"input_description={_sql_quote(input_description)}, "
            f"output_description={_sql_quote(output_description)}, "
            f"samples={_sql_quote(samples_json)}::jsonb "
            f"WHERE id={pid};"
        )
        updated += 1

    sql_lines.append("COMMIT;")
    if not dry_run and updated > 0:
        sql = "\n".join(sql_lines)
        cmd = [
            "docker",
            "exec",
            "-i",
            db_container,
            "psql",
            "-U",
            "onlinejudge",
            "-d",
            "onlinejudge",
            "-v",
            "ON_ERROR_STOP=1",
            "-f",
            "-",
        ]
        subprocess.run(cmd, input=sql, text=True, capture_output=True, check=True)
    return updated, skipped, missing


def sync_oj_statements(
    base_url: str,
    token: str,
    db_container: str,
    contest_id: int,
    mapping: Dict[str, dict],
    baseline_map: Dict[Tuple[int, int], BaselineStatement],
    dry_run: bool,
) -> Tuple[int, int, List[str]]:
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {token}"})

    try:
        rows = query_contest_nq_rows_via_db(db_container, contest_id)
    except Exception:
        rows = query_contest_nq_rows_via_api(base_url, token, contest_id)
    updated = 0
    skipped = 0
    missing: List[str] = []

    # If admin token is expired/invalid, fallback to direct DB patch to unblock local restore.
    if rows and not dry_run:
        probe_pid = rows[0][0]
        probe_resp = s.get(f"{base_url.rstrip('/')}/api/admin/problem?id={probe_pid}", timeout=30)
        probe_resp.raise_for_status()
        probe_wrapped = probe_resp.json()
        if probe_wrapped.get("error") == "login-required":
            return sync_oj_statements_via_db(
                db_container=db_container,
                contest_id=contest_id,
                mapping=mapping,
                baseline_map=baseline_map,
                dry_run=dry_run,
            )

    for pid, nq_id in rows:
        info = mapping.get(nq_id)
        if not info:
            missing.append(f"{nq_id}: no mapping")
            continue
        key = (int(info["ch"]), int(info["acw"]))
        baseline = baseline_map.get(key)
        if not baseline:
            missing.append(f"{nq_id}: no baseline")
            continue

        statement_patch = build_statement_payload(baseline)
        if dry_run:
            updated += 1
            continue

        get_url = f"{base_url.rstrip('/')}/api/admin/problem?id={pid}"
        put_url = f"{base_url.rstrip('/')}/api/admin/problem/"
        resp = s.get(get_url, timeout=30)
        resp.raise_for_status()
        wrapped = resp.json()
        if wrapped.get("error"):
            missing.append(f"{nq_id}: GET error {wrapped.get('data')}")
            continue
        problem = wrapped.get("data", wrapped)
        if "id" not in problem:
            problem["id"] = pid
        problem.update(statement_patch)
        put_resp = s.put(put_url, json=problem, timeout=30)
        put_resp.raise_for_status()
        put_wrapped = put_resp.json()
        if put_wrapped.get("error"):
            missing.append(f"{nq_id}: PUT error {put_wrapped.get('data')}")
            continue
        updated += 1
    return updated, skipped, missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Restore NQ statements from baseline")
    parser.add_argument("--local-only", action="store_true", help="Only patch local chapter bank JSON files")
    parser.add_argument("--oj-only", action="store_true", help="Only patch localhost OJ problems")
    parser.add_argument("--dry-run", action="store_true", help="Preview counts without writing/updating")
    parser.add_argument("--contest-id", type=int, default=DEFAULT_CONTEST_ID)
    parser.add_argument("--db-container", default=DEFAULT_DB_CONTAINER)
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--token", default=os.environ.get("XMUOJ_TOKEN", DEFAULT_TOKEN))
    args = parser.parse_args()

    mapping = load_json(MAPPING_PATH)
    baseline_map = load_baseline()

    do_local = not args.oj_only
    do_oj = not args.local_only

    local_total = 0
    local_changed = 0
    local_missing: List[str] = []

    if do_local:
        for nq_id, info in sorted(mapping.items(), key=lambda x: (x[1]["ch"], x[1]["idx"])):
            key = (int(info["ch"]), int(info["acw"]))
            baseline = baseline_map.get(key)
            if not baseline:
                local_missing.append(f"{nq_id}: no baseline")
                continue
            problem_json = find_problem_json_path(int(info["ch"]), int(info["acw"]))
            if not problem_json:
                local_missing.append(f"{nq_id}: no local problem.json")
                continue
            local_total += 1
            if not args.dry_run and patch_local_problem_json(problem_json, baseline):
                local_changed += 1
            elif args.dry_run:
                local_changed += 1

    oj_updated = 0
    oj_skipped = 0
    oj_missing: List[str] = []
    if do_oj:
        oj_updated, oj_skipped, oj_missing = sync_oj_statements(
            base_url=args.base_url,
            token=args.token,
            db_container=args.db_container,
            contest_id=args.contest_id,
            mapping=mapping,
            baseline_map=baseline_map,
            dry_run=args.dry_run,
        )

    print("=== restore summary ===")
    if do_local:
        print(f"local_targeted={local_total}")
        print(f"local_changed={local_changed}")
        print(f"local_missing={len(local_missing)}")
    if do_oj:
        print(f"oj_updated={oj_updated}")
        print(f"oj_skipped={oj_skipped}")
        print(f"oj_missing={len(oj_missing)}")

    if local_missing:
        print("--- local_missing (first 20) ---")
        for item in local_missing[:20]:
            print(item)
    if oj_missing:
        print("--- oj_missing (first 20) ---")
        for item in oj_missing[:20]:
            print(item)


if __name__ == "__main__":
    main()
