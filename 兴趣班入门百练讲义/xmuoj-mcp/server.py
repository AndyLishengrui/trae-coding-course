import requests
import re
import time
import urllib3
from mcp.server.fastmcp import FastMCP

# Suppress InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 初始化 MCP 服务
mcp = FastMCP("XMUOJ-Service")

class XMUOJClient:
    def __init__(self, base_url="https://www.xmuoj.com"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        self.token = None
        # 初始化获取 CSRF Token
        try:
            self.session.get(f"{self.base_url}/api/profile", timeout=10)
            self.token = self.session.cookies.get('csrftoken')
        except Exception as e:
            print(f"Warning: Failed to initialize session: {e}")

    def _get_headers(self):
        token = self.session.cookies.get('csrftoken')
        return {'X-CSRFToken': token, 'Referer': self.base_url}

    def login(self, username, password):
        params = {}
        if not self.session.cookies.get('csrftoken'):
             self.session.get(f"{self.base_url}/api/profile", timeout=10)
             
        headers = self._get_headers()
        data = {"username": username, "password": password}
        resp = self.session.post(f"{self.base_url}/api/login", json=data, headers=headers, timeout=10)
        result = resp.json()
        if result.get('error'):
            raise Exception(f"Login failed: {result.get('data')}")
        return "Login successful"

    def get_problem(self, problem_id):
        """获取题目描述、样例输入输出"""
        params = {"problem_id": problem_id}
        resp = self.session.get(f"{self.base_url}/api/problem", params=params, timeout=10)
        data = resp.json()
        if data.get('error'):
             raise Exception(f"Get problem failed: {data.get('data')}")
        return data['data']

    def search_problem(self, keyword, limit=50):
        """搜索题目"""
        params = {"keyword": keyword, "limit": limit}
        resp = self.session.get(f"{self.base_url}/api/problem", params=params, timeout=10)
        data = resp.json()
        if data.get('error'):
             raise Exception(f"Search failed: {data.get('data')}")
        return data['data']['results']

    def submit_code(self, problem_id, code, language="C++"):
        """提交代码，返回 submission_id"""
        headers = self._get_headers()
        # XMUOJ (QDUOJ) language mapping assumption. 
        # Usually valid values can be "C", "C++", "Java", "Python3", "Python2" etc.
        # We might need to ensuring the naming is correct or map it.
        # Simple mapping for common names:
        payload = {
            "problem_id": problem_id,
            "language": language,
            "code": code
        }
        resp = self.session.post(f"{self.base_url}/api/submission", json=payload, headers=headers, timeout=10)
        try:
            data = resp.json()
        except ValueError:
            raise Exception(f"Submission API Error: Status {resp.status_code}, Response: {resp.text[:500]}")
            
        if data.get('error'):
             raise Exception(f"Submission failed: {data.get('data')}")
        return data['data']['submission_id']

    def get_result(self, submission_id):
        """获取评测结果"""
        params = {"id": submission_id}
        resp = self.session.get(f"{self.base_url}/api/submission", params=params, timeout=10)
        data = resp.json()
        if data.get('error'):
             return {"result": -1, "result_msg": "Error fetching result"} # Or raise
        return data['data']

    def get_contest_problems(self, contest_id):
        """获取竞赛题目列表"""
        params = {"contest_id": contest_id}
        resp = self.session.get(f"{self.base_url}/api/contest/problem", params=params, timeout=10)
        data = resp.json()
        if data.get('error'):
             raise Exception(f"Get contest problems failed: {data.get('data')}")
        return data['data']

    def get_contest_problem(self, contest_id, problem_id):
        """获取竞赛题目详情"""
        params = {"contest_id": contest_id, "problem_id": problem_id}
        resp = self.session.get(f"{self.base_url}/api/contest/problem", params=params, timeout=10)
        data = resp.json()
        if data.get('error'):
             raise Exception(f"Get contest problem failed: {data.get('data')}")
        return data['data']

    def submit_contest_code(self, contest_id, problem_id, code, language="C++"):
        """提交竞赛题目代码"""
        headers = self._get_headers()
        payload = {
            "contest_id": contest_id,
            "problem_id": problem_id,
            "language": language,
            "code": code
        }
        # 尝试使用不同的竞赛提交 API 路径
        # 先尝试标准路径
        try:
            resp = self.session.post(f"{self.base_url}/api/contest/submission", json=payload, headers=headers, timeout=10)
            data = resp.json()
            if data.get('error'):
                 raise Exception(f"Submission failed: {data.get('data')}")
            return data['data']['submission_id']
        except Exception as e1:
            # 尝试另一种路径格式
            try:
                resp = self.session.post(f"{self.base_url}/api/submission", json=payload, headers=headers, timeout=10)
                data = resp.json()
                if data.get('error'):
                     raise Exception(f"Submission failed: {data.get('data')}")
                return data['data']['submission_id']
            except Exception as e2:
                raise Exception(f"Submission API Error: {str(e2)}")

# Global client instace
client = XMUOJClient()

@mcp.tool()
def xmuoj_login(username: str, password: str) -> str:
    """
    Log in to XMUOJ. success returns 'Login successful'.
    """
    try:
        return client.login(username, password)
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def xmuoj_search_problem(keyword: str) -> str:
    """
    Search for a problem by keyword (name or ID). Returns a list of matching problems.
    """
    try:
        results = client.search_problem(keyword)
        if not results:
            return "No problems found."
        
        output = []
        for p in results:
            output.append(f"ID: {p['_id']}, Title: {p['title']}")
        return "\n".join(output)
    except Exception as e:
        return f"Error searching problem: {str(e)}"

@mcp.tool()
def xmuoj_get_problem(problem_id_or_url: str) -> str:
    """
    Get the details of a problem (description, samples) by ID or URL.
    """
    try:
        # Extract ID if URL is provided
        # URL formats: https://www.xmuoj.com/problem/1001
        problem_id = problem_id_or_url
        match = re.search(r'/problem/(\w+)', problem_id_or_url)
        if match:
            problem_id = match.group(1)
        
        problem = client.get_problem(problem_id)
        
        # Format the output for the LLM
        output = f"# {problem['title']} (ID: {problem['_id']})\n\n"
        output += f"## Description\n{problem['description']}\n\n"
        output += f"## Input Description\n{problem['input_description']}\n\n"
        output += f"## Output Description\n{problem['output_description']}\n\n"
        
        samples = problem.get('samples', [])
        for i, sample in enumerate(samples):
            output += f"## Sample {i+1}\n"
            output += f"### Input\n```\n{sample['input']}\n```\n"
            output += f"### Output\n```\n{sample['output']}\n```\n\n"
            
        if problem.get('hint'):
             output += f"## Hint\n{problem['hint']}\n"
             
        return output
    except Exception as e:
        return f"Error getting problem: {str(e)}"

@mcp.tool()
def xmuoj_submit_code(problem_id_or_url: str, code: str, language: str = "C++") -> str:
    """
    Submit code to XMUOJ (Public or Contest) and wait for the result.
    
    Supported Input Formats:
    1. Public Problem:
       - ID: "1001"
       - URL: "https://www.xmuoj.com/problem/1001"
       
    2. Contest Problem:
       - URL: "https://www.xmuoj.com/contest/207/problem/A"
       (Note: Contest ID and Problem ID are automatically extracted)
       
    Language options: "C", "C++", "Java", "Python3", "Python2".
    """
    try:
        submission_id = None
        
        # Check for Contest URL
        # Pattern: .../contest/{id}/problem/{pid}
        contest_match = re.search(r'/contest/(\d+)/problem/([\w\d]+)', problem_id_or_url)
        
        if contest_match:
            contest_id = contest_match.group(1)
            display_id = contest_match.group(2)
            
            # Resolve to internal ID for checking or ensuring correctness
            # The API usually expects the Display ID (like 'A') in the payload for some endpoints,
            # or the internal ID for others. 
            # In QDUOJ standard:
            # POST /api/submission expects 'problem_id' to be the INTERNAL ID of the problem.
            # Even for contests? 
            # For contests: 'contest_id' is required. 'problem_id' is the global problem ID? No.
            # It's usually the ID returned by the contest problem detail.
            
            try:
                p_info = client.get_contest_problem(contest_id, display_id)
                # p_info['id'] is likely the internal ID.
                real_problem_id = p_info['id']
            except Exception as e:
                # Fallback or error
                return f"Error resolving contest problem '{display_id}': {e}"
            
            submission_id = client.submit_contest_code(contest_id, real_problem_id, code, language)
            
        else:
            # Public Problem
            display_id = problem_id_or_url
            match = re.search(r'/problem/(\w+)', problem_id_or_url)
            if match:
                display_id = match.group(1)

            # Resolve to internal ID
            try:
                 problem_info = client.get_problem(display_id)
                 problem_id = problem_info['id']
            except Exception:
                 problem_id = display_id
                  
            submission_id = client.submit_code(problem_id, code, language)
        
        # Poll for result
        max_retries = 20
        for _ in range(max_retries):
            result = client.get_result(submission_id)
            
            # -1: Pending, -2: Judging
            curr_result = result.get('result')
            if curr_result not in [-1, -2]:
                # Completed
                info = result.get('statistic_info', {})
                err = result.get('err_info', '')
                
                final_res = f"Submission ID: {submission_id}\n"
                
                res_code = result.get('result')
                res_map = {
                    0: "Accepted",
                    1: "Time Limit Exceeded",
                    2: "Time Limit Exceeded",
                    3: "Memory Limit Exceeded",
                    4: "Runtime Error",
                    5: "System Error",
                    6: "Wrong Answer",
                    7: "Compile Error",
                    8: "Presentation Error"
                }
                status_text = res_map.get(res_code, f"Status Code {res_code}")
                
                final_res += f"Status: {status_text}\n"
                if info:
                    final_res += f"Time: {info.get('time_cost')}ms, Memory: {info.get('memory_cost')}bytes\n"
                    if info.get('score'):
                        final_res += f"Score: {info.get('score')}\n"
                if err:
                    final_res += f"Error Info:\n{err}\n"
                    
                return final_res
                
            time.sleep(1)
            
        return f"Submission {submission_id} is still processing. Please check manually."

    except Exception as e:
        return f"Error submitting code: {str(e)}"

@mcp.tool()
def xmuoj_get_contest_problems(contest_id: str) -> str:
    """
    Get the list of problems in a contest.
    """
    try:
        problems = client.get_contest_problems(contest_id)
        if not problems:
            return "No problems found in contest."
        
        output = []
        for p in problems:
            output.append(f"ID: {p['id']}, Title: {p['title']}")
        return "\n".join(output)
    except Exception as e:
        return f"Error getting contest problems: {str(e)}"

@mcp.tool()
def xmuoj_get_contest_problem(contest_id: str, problem_id: str) -> str:
    """
    Get the details of a problem in a contest.
    """
    try:
        problem = client.get_contest_problem(contest_id, problem_id)
        
        # Format the output for the LLM
        output = f"# {problem['title']} (ID: {problem['id']})\n\n"
        output += f"## Description\n{problem['description']}\n\n"
        output += f"## Input Description\n{problem['input_description']}\n\n"
        output += f"## Output Description\n{problem['output_description']}\n\n"
        
        samples = problem.get('samples', [])
        for i, sample in enumerate(samples):
            output += f"## Sample {i+1}\n"
            output += f"### Input\n```\n{sample['input']}\n```\n"
            output += f"### Output\n```\n{sample['output']}\n```\n\n"
            
        if problem.get('hint'):
             output += f"## Hint\n{problem['hint']}\n"
              
        return output
    except Exception as e:
        return f"Error getting contest problem: {str(e)}"

@mcp.tool()
def xmuoj_submit_contest_code(contest_id: str, problem_id: str, code: str, language: str = "C++") -> str:
    """
    Submit code to a contest problem and wait for the result.
    Language options usually include: C, C++, Java, Python3, Python2.
    """
    try:
        submission_id = client.submit_contest_code(contest_id, problem_id, code, language)
        
        # Poll for result
        max_retries = 20
        for _ in range(max_retries):
            result = client.get_result(submission_id)
            curr_result = result.get('result')
            if curr_result not in [-1, -2]:
                # Completed
                info = result.get('statistic_info', {})
                err = result.get('err_info', '')
                
                final_res = f"Submission ID: {submission_id}\n"
                
                res_code = result.get('result')
                res_map = {
                    0: "Accepted",
                    1: "Time Limit Exceeded",
                    2: "Time Limit Exceeded",
                    3: "Memory Limit Exceeded",
                    4: "Runtime Error",
                    5: "System Error",
                    6: "Wrong Answer",
                    7: "Compile Error",
                    8: "Presentation Error"
                }
                status_text = res_map.get(res_code, f"Status Code {res_code}")
                
                final_res += f"Status: {status_text}\n"
                if info:
                    final_res += f"Time: {info.get('time_cost')}ms, Memory: {info.get('memory_cost')}bytes\n"
                    if info.get('score'):
                        final_res += f"Score: {info.get('score')}\n"
                if err:
                    final_res += f"Error Info:\n{err}\n"
                    
                return final_res
                
            time.sleep(1)
            
        return f"Submission {submission_id} is still processing. Please check manually."

    except Exception as e:
        return f"Error submitting contest code: {str(e)}"

if __name__ == "__main__":
    mcp.run()
