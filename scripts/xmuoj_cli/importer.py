"""
XMUOJ Problem Importer — 完整的问题导入流程

整合蓝桥杯实战验证的6步流程：
  1. 题面分析 → 2. problem.json → 3. 测试数据 → 4. 验证 → 5. ZIP打包 → 6. 导入

提供两种导入方式：
  A) API 方式 — 通过 admin API 直接创建（适合少量题目）
  B) ZIP 方式 — 通过 import API 上传 ZIP 包（适合批量、含测试数据）
"""
import json
import os
import tempfile
from pathlib import Path
from typing import Dict, List, Optional

from .client import XmuojClient
from .problem_builder import build_from_markdown, build_from_file
from .packager import package_problem, package_samples


class ProblemImporter:
    """XMUOJ 问题导入器"""

    def __init__(self, client: XmuojClient):
        self.client = client

    # ===== 方法A: API 直接创建 =====

    def create_via_api(self, problem: Dict) -> Dict:
        """
        通过 Admin API 创建题目（Django Serializer 格式）

        Args:
            problem: 标准16字段的 problem dict

        Returns:
            API 响应
        """
        # 转换为 Django serializer 格式
        api_data = {
            "_id": problem["display_id"],
            "title": problem["title"],
            "description": problem["description"]["value"],
            "input_description": problem["input_description"]["value"],
            "output_description": problem["output_description"]["value"],
            "samples": problem["samples"],
            "test_case_id": "",  # 空，后续通过 upload_test_cases 补充
            "test_case_score": [],
            "time_limit": problem["time_limit"],
            "memory_limit": problem["memory_limit"],
            "languages": ["C", "C++", "Python3"],
            "template": {},
            "rule_type": problem["rule_type"],
            "io_mode": {"io_mode": "Standard IO", "input": "input.txt", "output": "output.txt"},
            "spj": False,
            "spj_language": None,
            "spj_code": None,
            "spj_compile_ok": False,
            "visible": True,
            "difficulty": "Low",
            "tags": problem.get("tags", []),
            "hint": problem["hint"]["value"],
            "source": problem.get("source", "AcWing"),
            "share_submission": False,
        }
        return self.client.create_problem(api_data)

    # ===== 方法B: ZIP 导入 =====

    def import_via_zip(self, zip_path: str) -> Dict:
        """
        通过 Import API 导入 ZIP 包

        Args:
            zip_path: 包含 1/ 根目录的 ZIP 文件路径

        Returns:
            导入结果
        """
        url = f"{self.client.base_url}/api/admin/import_problem/"
        with open(zip_path, "rb") as f:
            files = {"file": (os.path.basename(zip_path), f, "application/zip")}
            resp = self.client.session.post(
                url,
                files=files,
                headers={"Authorization": self.client.session.headers.get("Authorization", "")},
            )
        return self.client._parse(resp)

    # ===== 一站式流程 =====

    def build_and_import(
        self,
        md_content: str,
        contest_id: Optional[int] = None,
        testcase_dir: Optional[str] = None,
        method: str = "api",
    ) -> Dict:
        """
        一站式：Markdown 题面 → 创建 problem.json → 导入 XMUOJ

        Args:
            md_content: Markdown 题面
            contest_id: 比赛ID（可选，导入后加入比赛）
            testcase_dir: 测试数据目录
            method: "api" 或 "zip"

        Returns:
            {"problem": {...}, "import_result": {...}}
        """
        # 1. 构建 problem.json
        problem = build_from_markdown(md_content)
        display_id = problem["display_id"]

        # 2. 导入
        if method == "zip":
            # 打包 → 导入
            with tempfile.TemporaryDirectory() as tmp:
                zip_path = os.path.join(tmp, f"{display_id}_import.zip")
                package_problem(problem, testcase_dir, zip_path, tmp)
                result = self.import_via_zip(zip_path)
        else:
            # API 直接创建
            result = self.create_via_api(problem)

        # 3. 加入比赛（可选）
        if contest_id:
            try:
                # 获取创建后的问题ID
                prob_id = result.get("id") if isinstance(result, dict) else None
                if prob_id:
                    self.client._admin_post("contest/add_problem_from_public", {
                        "contest_id": contest_id,
                        "problem_id": prob_id,
                        "display_id": display_id,
                    })
            except Exception as e:
                print(f"  ⚠️  加入比赛失败: {e}")

        return {"problem": problem, "import_result": result}

    def batch_import_from_dir(
        self,
        md_dir: str,
        contest_id: Optional[int] = None,
        method: str = "api",
    ) -> Dict:
        """
        批量导入目录中所有 Markdown 题面

        Args:
            md_dir: 包含 *.md 文件的目录
            contest_id: 比赛ID
            method: "api" 或 "zip"

        Returns:
            {"success": [...], "failed": [...]}
        """
        results = {"success": [], "failed": []}
        md_files = sorted(Path(md_dir).glob("*.md"))

        for md_file in md_files:
            try:
                content = md_file.read_text(encoding="utf-8")
                result = self.build_and_import(content, contest_id, method=method)
                results["success"].append({
                    "file": str(md_file),
                    "display_id": result["problem"]["display_id"],
                })
                print(f"  ✅ {md_file.name}")
            except Exception as e:
                results["failed"].append({"file": str(md_file), "error": str(e)})
                print(f"  ❌ {md_file.name}: {e}")

        return results


# CLI entry
if __name__ == "__main__":
    import sys
    from .client import XmuojClient

    if len(sys.argv) < 2:
        print("Usage: python importer.py <markdown_file> [--contest-id X] [--method zip|api]")
        sys.exit(1)

    client = XmuojClient(config_path=str(Path.home() / ".xmuoj_cli_config.json"))
    importer = ProblemImporter(client)

    md_file = sys.argv[1]
    contest_id = None
    method = "api"

    for i, arg in enumerate(sys.argv[2:], 2):
        if arg == "--contest-id" and i + 1 < len(sys.argv):
            contest_id = int(sys.argv[i + 1])
        elif arg == "--method" and i + 1 < len(sys.argv):
            method = sys.argv[i + 1]

    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    result = importer.build_and_import(content, contest_id, method=method)
    print(f"✅ {result['problem']['display_id']}: {result['problem']['title']}")
    print(f"   {json.dumps(result['import_result'], ensure_ascii=False)[:200]}")
