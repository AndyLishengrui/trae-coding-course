"""
XMUOJ API Client
基于 xmuoj-vscode 插件 API 接口设计
"""
import os
import json
import requests
import hashlib
import zipfile
import tempfile
from pathlib import Path
from typing import Optional, Dict, List, Any

# 默认使用环境变量或本地地址
BASE_URL = os.environ.get("XMUOJ_URL", "http://localhost")


class XmuojClient:
    """XMUOJ API 客户端，支持管理员操作"""

    def __init__(self, token: Optional[str] = None, config_path: Optional[str] = None,
                 base_url: Optional[str] = None):
        base = (base_url or BASE_URL).rstrip("/")
        self.base_url = base
        self.admin_api = f"{base}/api/admin"
        self.public_api = f"{base}/api"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; XMUOJ-CLI-Tool)",
            "Content-Type": "application/json",
            "Connection": "close",
        })
        self._token = token
        if config_path:
            self._load_config(config_path)
        if self._token:
            self.session.headers["Authorization"] = f"Bearer {self._token}"

    def _load_config(self, path: str):
        """从配置文件加载 token"""
        cfg = Path(path)
        if cfg.exists():
            data = json.loads(cfg.read_text())
            self._token = data.get("token", "")

    def save_config(self, path: str):
        """保存 token 到配置文件"""
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(json.dumps({"token": self._token}, indent=2))

    # ===== Authentication =====

    def login(self, username: str, password: str) -> Dict:
        """登录获取 token"""
        resp = self.session.post(f"{self.public_api}/login", json={
            "username": username,
            "password": password,
        })
        data = self._parse(resp)
        self._token = data["token"]
        self.session.headers["Authorization"] = f"Bearer {self._token}"
        return data

    # ===== Problem CRUD =====

    def create_problem(self, problem: Dict) -> Dict:
        """创建题目 (POST /api/admin/problem/)"""
        return self._admin_post("problem", problem)

    def get_problem(self, problem_id: int = None, display_id: str = None) -> Dict:
        """获取题目详情"""
        if problem_id:
            return self._admin_get("problem", {"id": problem_id})
        elif display_id:
            # Use public API as fallback
            resp = self.session.get(f"{self.public_api}/problem", params={"problem_id": display_id})
            return self._parse(resp)

    def update_problem(self, problem: Dict) -> Dict:
        """更新题目 (PUT /api/admin/problem/)"""
        return self._admin_put("problem", problem)

    def delete_problem(self, problem_id: int) -> Dict:
        """删除题目"""
        return self._admin_delete("problem", {"id": problem_id})

    def list_problems(self, keyword: str = "", limit: int = 100) -> Dict:
        """列出公开题目"""
        return self._admin_get("problem", {"keyword": keyword, "limit": limit})

    # ===== Test Case Management =====

    def upload_test_cases(self, zip_path: str, spj: bool = False) -> Dict:
        """上传测试数据 (ZIP 格式)"""
        url = f"{self.admin_api}/test_case/"
        with open(zip_path, "rb") as f:
            files = {"file": (os.path.basename(zip_path), f, "application/zip")}
            data = {"spj": "true" if spj else "false"}
            # Need to use multipart for file upload
            resp = requests.post(url, data=data, files=files,
                                headers={"Authorization": self.session.headers.get("Authorization", "")})
        return self._parse(resp)

    def download_test_cases(self, problem_id: int, output_dir: str) -> str:
        """下载测试数据"""
        url = f"{self.admin_api}/test_case/?problem_id={problem_id}"
        resp = self.session.get(url, stream=True)
        if resp.status_code == 200:
            zip_path = os.path.join(output_dir, f"test_cases_{problem_id}.zip")
            with open(zip_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            return zip_path
        raise Exception(f"Download failed: {resp.status_code}")

    # ===== Contest/Problem Set Management =====

    def create_contest_problem(self, data: Dict) -> Dict:
        """将题目加入比赛/实验"""
        return self._admin_post("contest/problem", data)

    def list_contest_problems(self, contest_id: int) -> List[Dict]:
        """列出比赛中的所有题目"""
        return self._admin_get("contest/problem", {"contest_id": contest_id})

    def update_contest_problem(self, data: Dict) -> Dict:
        """更新比赛中的题目"""
        return self._admin_put("contest/problem", data)

    def remove_contest_problem(self, contest_problem_id: int) -> Dict:
        """从比赛中移除题目"""
        return self._admin_delete("contest/problem", {"id": contest_problem_id})

    # ===== Contest CRUD =====

    def create_contest(self, contest: Dict) -> Dict:
        """创建比赛/实验"""
        return self._admin_post("contest", contest)

    def get_contest(self, contest_id: int) -> Dict:
        """获取比赛详情"""
        return self._admin_get("contest", {"id": contest_id})

    def update_contest(self, contest: Dict) -> Dict:
        """更新比赛"""
        return self._admin_put("contest", contest)

    def delete_contest(self, contest_id: int, hard: bool = False) -> Dict:
        """删除比赛（默认软删除，hard=True彻底删除）"""
        params = {"id": contest_id}
        if hard:
            params["hard"] = "1"
        return self._admin_delete("contest", params)

    def list_contests(self, keyword: str = "", limit: int = 100) -> List[Dict]:
        """列出比赛"""
        return self._admin_get("contest", {"keyword": keyword, "limit": limit})

    # ===== Submission =====

    def submit(self, problem_id: int, code: str, language: str,
               contest_id: int = None) -> Dict:
        """提交代码"""
        payload = {
            "problem_id": problem_id,
            "code": code,
            "language": language,
        }
        if contest_id:
            payload["contest_id"] = contest_id
        resp = self.session.post(f"{self.public_api}/submission", json=payload)
        return self._parse(resp)

    def get_submission(self, submission_id: str) -> Dict:
        """查询提交结果"""
        return self._request("GET", f"{self.public_api}/submission?id={submission_id}")

    # ===== Helper Methods =====

    def _admin_get(self, path: str, params: Dict = None) -> Any:
        return self._request("GET", f"{self.admin_api}/{path}/", params=params)

    def _admin_post(self, path: str, data: Dict) -> Any:
        return self._request("POST", f"{self.admin_api}/{path}/", json=data)

    def _admin_put(self, path: str, data: Dict) -> Any:
        return self._request("PUT", f"{self.admin_api}/{path}/", json=data)

    def _admin_delete(self, path: str, params: Dict = None) -> Any:
        return self._request("DELETE", f"{self.admin_api}/{path}/", params=params)

    def _request(self, method: str, url: str, **kwargs) -> Any:
        resp = self.session.request(method, url, **kwargs)
        return self._parse(resp)

    def _parse(self, resp: requests.Response) -> Any:
        if resp.status_code >= 400:
            try:
                body = resp.json()
                raise Exception(body.get("data", resp.text))
            except (ValueError, KeyError):
                raise Exception(f"HTTP {resp.status_code}: {resp.text[:200]}")
        try:
            data = resp.json()
            if isinstance(data, dict) and data.get("error"):
                raise Exception(data.get("data", str(data)))
            return data.get("data", data)
        except (ValueError,):
            return resp.text
