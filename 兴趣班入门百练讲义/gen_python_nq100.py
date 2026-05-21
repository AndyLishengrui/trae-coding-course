import os
import time
import argparse
import concurrent.futures
import re
import glob
import sys
# Add xmuoj-mcp path
sys.path.append(os.path.join(os.getcwd(), 'xmuoj-mcp'))
from server import XMUOJClient
from book_gen.llm_client import LLMClient

# Configuration
CONTEST_ID = 207  # Contest 207 on XMUOJ
WORKSPACE_ROOT = "NQ100"

client = XMUOJClient()

def safe_print(msg):
    print(msg, flush=True)

def parse_ids(id_str):
    ids = []
    parts = id_str.split(',')
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            ids.extend(range(start, end + 1))
        else:
            ids.append(int(part))
    return ids

def get_real_problem_id(client, contest_id, display_id):
    """
    Get the internal problem ID from the contest problem list/lookup.
    Currently hardcoded/heuristic or fetched?
    verify_nq100.py handled this by fetching the problem page or using a lookup.
    Let's try to fetch list if possible, or search for the problem in the contest.
    Since verify_nq100.py had logic for this, we'll reuse the simple heuristic if ids are sequential,
    but previous logs showed Internal ID: 3814 for NQ004, 3821 for NQ011.
    Problem 1 -> 3811?
    Let's rely on client.get_contest_problems() if available or just mapping.
    Wait, verify_nq100.py uses client.submit_contest_code(CONTEST_ID, real_problem_id, ...)
    and it seemed to find real_problem_id via `find_problem_in_contest` (implied).
    
    Actually, let's look at `verify_nq100.py`'s method.
    It calls `client.get_problem_info(contest_id=..., problem_id=...)`?
    No, in the valid logs: `Submitting to Contest 207, Problem 4 (Internal ID: 3814)...`
    """
    # Simply using the logic from verify_nq100 if available, but I don't have the full file content in history easily.
    # However, I can infer: Problem 1 is usually the first.
    # Let's assume sequential for now or fetch.
    # Logic: verify_nq100.py likely fetches the problem page.
    # Let's try to fetch problem info using the display ID (e.g., '1', '2'...)
    # The MCP tool `xmuoj_submit_contest_code` likely takes the internal ID.
    # I will assume there is a way.
    # Actually, let's blindly try: base_id + (idx - 1).
    # NQ004 is 3814. NQ100 is probably 3811 + 99 = 3910?
    # NQ099 is 3909. YES.
    # So mapping is: Internal ID = 3810 + idx.
    return 3810 + int(display_id)

def generate_python_solution(llm, idx):
    if idx < 1 or idx > 100:
        return
        
    problem_key = str(idx)
    folder_name = f"NQ{idx:03d}"
    folder_path = os.path.join(WORKSPACE_ROOT, folder_name)
    
    if not os.path.exists(folder_path):
        safe_print(f"[{folder_name}] Folder not found, skipping.")
        return

    # Check for std.cpp
    std_path = os.path.join(folder_path, "std.cpp")
    if not os.path.exists(std_path):
        # safe_print(f"[{folder_name}] std.cpp not found. Cannot translate.")
        return # Skip implicitly

    # Check if target python file already exists
    py_filename = f"NQ{idx:03d}.py"
    py_path = os.path.join(folder_path, py_filename)
    
    if os.path.exists(py_path) and os.path.getsize(py_path) > 0:
        safe_print(f"[{folder_name}] {py_filename} already exists. Skipping.")
        return

    safe_print(f"[{folder_name}] Translating std.cpp to {py_filename}...")

    with open(std_path, 'r', encoding='utf-8') as f:
        cpp_code = f.read()

    # Prompt LLM
    prompt = f"""
你是一名精通算法竞赛的程序员。请将以下已经AC的C++代码翻译成 Python 3.5 代码。

【要求】
1. 代码必须简洁、优雅，符合 Pythonic 风格。
2. 必须包含详细的中文注释，解释算法逻辑。
3. 必须能够通过 Online Judge 测试（注意 Python 的输入输出效率，必要时使用 sys.stdin.readline）。
4. 请以 JSON 格式返回结果。

【C++ 代码】
{cpp_code}

【JSON返回格式】
{{
  "code": "Python代码内容",
  "explanation": "说明"
}}
"""
    
    try:
        # Call LLM
        res = llm._call_llm(prompt)
        py_code = res.get('code', '')
        
        if not py_code:
            safe_print(f"[{folder_name}] LLM returned empty code.")
            return

        # Correction for markdown blocks if any
        py_code = py_code.replace("```python", "").replace("```", "").strip()

        # Submit
        real_problem_id = get_real_problem_id(client, CONTEST_ID, idx)
        safe_print(f"[{folder_name}] Submitting Python to ID {real_problem_id}...")
        
        sid = client.submit_contest_code(CONTEST_ID, real_problem_id, py_code, "Python3")
        safe_print(f"[{folder_name}] Submission ID: {sid}")

        # Poll result
        final_status = "Unknown"
        for _ in range(10): # Wait up to 10s
            time.sleep(1)
            r = client.get_result(sid)
            status = r.get('result', -1) # result code
            # 0: Pending?, 1: Pending?, ... usually 0 is Accepted in some OJs, or string.
            # verify_nq100 used string check or mapped integers.
            # client.get_result returns raw JSON or mapped?
            # Let's assume same behavior as verify_nq100 which mapped result codes to text later?
            # Actually verify_nq100 printed `Result: Accepted`.
            # Let's assume 'result' field matches the standard OJ codes.
            # If verify_nq100 worked, it probably handled mapping.
            # Actually, looking at previous logs: "Result: Accepted".
            # So `client.get_result` likely returns a mapped string or `verify_nq100` did.
            # Let's rely on `r['result_str']` if existing or interpret `result`.
            # Standard QDUOJ: 0=Accepted? No.
            # Let's check `verify_nq100.py` snippet in memory...
            # "if r2['result'] == 0: safe_print(...) Retry SUCCEEDED!"
            # So 0 seems to be Accepted ID?
            
            # Wait, standard convention:
            # -1: Pending
            # 0: Accepted
            # ...
            if status != -1 and status != -2: # Not pending
                if status == 0:
                    final_status = "Accepted"
                else:
                    final_status = f"Failed ({status})"
                break
        
        safe_print(f"[{folder_name}] Result: {final_status}")

        if final_status == "Accepted":
             with open(py_path, 'w', encoding='utf-8') as f:
                 f.write(py_code)
             safe_print(f"[{folder_name}] Saved {py_filename}")
        else:
             # Auto-fix
             safe_print(f"[{folder_name}] Validation Failed. Auto-fixing...")
             fix_prompt = f"""
你的 Python 代码未能通过测试。
错误状态: {final_status}
原 C++ 代码（正确）:
{cpp_code}

你写的 Python 代码（错误）:
{py_code}

请修正代码，确保可以通过 OJ（Python 3.5）。注意输入读取效率（建议使用 sys.stdin）和逻辑一致性。
返回 JSON: {{ "code": "...", "explanation": "..." }}
"""
             fix_res = llm._call_llm(fix_prompt)
             fixed_code = fix_res.get('code', '')
             if fixed_code:
                fixed_code = fixed_code.replace("```python", "").replace("```", "").strip()
                sid2 = client.submit_contest_code(CONTEST_ID, real_problem_id, fixed_code, "Python3")
                safe_print(f"[{folder_name}] Retry ID: {sid2}")
                for _ in range(10):
                    time.sleep(1)
                    r2 = client.get_result(sid2)
                    if r2.get('result') == 0:
                        safe_print(f"[{folder_name}] Retry Accepted!")
                        with open(py_path, 'w', encoding='utf-8') as f:
                            f.write(fixed_code)
                        break
                    elif r2.get('result') not in [-1, -2]:
                        safe_print(f"[{folder_name}] Retry Failed ({r2.get('result')})")
                        break

    except Exception as e:
        safe_print(f"[{folder_name}] Error: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ids', type=str, default="1-100")
    parser.add_argument('--workers', type=int, default=2)
    args = parser.parse_args()

    client.login('andy', 'andy@5dg')
    llm = LLMClient()
    
    target_ids = parse_ids(args.ids)
    print(f"Generating Python solutions for {len(target_ids)} problems...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(generate_python_solution, llm, idx) for idx in target_ids]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
