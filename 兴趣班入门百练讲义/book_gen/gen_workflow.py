import sys
import os
import time
import json
import argparse
from pathlib import Path

# Add parent directory to path to import xmuoj-mcp
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'xmuoj-mcp'))

try:
    from server import XMUOJClient
except ImportError:
    # Use relative import workaround if needed or rely on above sys.path
    print("Error: Could not import XMUOJClient. Make sure xmuoj-mcp/server.py exists.")
    sys.exit(1)

from llm_client import LLMClient

def save_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def verify_solution(oj_client, problem_id, code):
    print(f"[{problem_id}] Verifying solution on OJ...")
    try:
        # Resolve internal ID if needed (server.py logic is partially hidden, 
        # but submit_code usually takes display ID if server.py has the logic to resolve,
        # OR we need to do it here.
        # server.py's submit_code (current version) DOES try to resolve.
        
        submission_id = oj_client.submit_code(problem_id, code, language="C++")
        print(f"[{problem_id}] Submitted. Submission ID: {submission_id}")
        
        # Poll
        import time
        for _ in range(20):
            time.sleep(1)
            result = oj_client.get_result(submission_id)
            res_code = result.get('result')
            
            # -1: Pending, -2: Judging
            if res_code not in [-1, -2]:
                if res_code == 0:
                    print(f"[{problem_id}] ✅ VERIFICATION SUCCESS: Accepted")
                    return True, "Accepted"
                else:
                    # Map error
                    res_map = { 0: "Accepted", 6: "Wrong Answer", 7: "Compile Error", 1: "Time Limit", 2: "Time Limit", 3: "Memory Limit", 4: "Runtime Error", 5: "System Error" }
                    status = res_map.get(res_code, f"Error {res_code}")
                    if status != "Accepted":
                         # Append extra info if available
                         err_info = result.get('err_info')
                         if err_info:
                             status += f"\nError Info: {err_info}"
                    print(f"[{problem_id}] ❌ VERIFICATION FAILED: {status}")
                    return False, status
        
        print(f"[{problem_id}] ⚠️ VERIFICATION TIMEOUT")
        return False, "Timeout"
    except Exception as e:
        print(f"[{problem_id}] Verification Error: {e}")
        return False, str(e)

def process_problem(oj_client, llm_client, problem_id, output_base_dir):
    print(f"[{problem_id}] Fetching data...")
    try:
        # 1. Fetch Problem
        # Use a retry mechanism inside client or here? client usually throws.
        # We need to handle the case where problem_id might be a string like "GW003"
        # xmuoj-mcp server.py helps resolve IDs but here we access the raw client.
        # Let's try to get by ID first.
        try:
             problem = oj_client.get_problem(problem_id)
        except Exception as e:
            # If string ID failed, maybe we need to search or it's a display ID that the API takes directly?
            # get_problem in server.py takes URL or ID.
            # Let's assume the user provides a valid ID or we adapt.
            # For "GW003" -> the previous attempt showed we need to search or know internal ID.
            # But wait, looking at server.py, get_problem just calls /api/problem with problem_id param.
            # If "GW003" works there, it works here.
            # Previous error: "problem_id: A valid integer is required".
            # So "GW003" is a display_id. We need to find the internal ID.
            # Does the QDUOJ API allow searching by display_id?
            # /api/problem?problem_id=GW003 might work if modified, but usually it expects int.
            # Let's use the search function if available, or try to get by display_id mapping.
            
            # Use search to find the internal ID
            print(f"[{problem_id}] 'get_problem' failed directly. Trying search...")
            search_results = oj_client.search_problem(problem_id)
            found = False
            if search_results:
                for res in search_results:
                    # QDUOJ search result contains '_id' (display id) and 'id' (internal id)?
                    # Usually: 'id' is internal, '_id' is display_id (e.g. 1001)
                    if res.get('_id') == problem_id or res.get('title') == problem_id:
                        real_id = res.get('id')
                        print(f"[{problem_id}] Found internal ID: {real_id}")
                        problem = oj_client.get_problem(real_id)
                        found = True
                        break
            
            if not found:
                print(f"[{problem_id}] Failed to find problem.")
                return False

        # 2. Create Directory
        # Format: Output/GW003_Title/
        safe_title = problem['title'].replace('/', '-').replace('\\', '-').strip()
        dir_name = f"{problem_id}_{safe_title}"
        dir_path = os.path.join(output_base_dir, dir_name)
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        
        # 3. Save Problem Description (readme.md)
        desc_md = f"""# {problem['title']} (ID: {problem['_id']})

## 题目描述
{problem['description']}

## 输入描述
{problem['input_description']}

## 输出描述
{problem['output_description']}

## 样例
"""
        for i, sample in enumerate(problem.get('samples', [])):
            desc_md += f"### Sample {i+1}\n"
            desc_md += f"**Input:**\n```\n{sample['input']}\n```\n"
            desc_md += f"**Output:**\n```\n{sample['output']}\n```\n"
            
        desc_md += f"\n## 提示\n{problem.get('hint', '')}\n"
        
        save_file(os.path.join(dir_path, "readme.md"), desc_md)
        print(f"[{problem_id}] Saved readme.md")
        
        print(f"[{problem_id}] Generating AI solution...")
        # Check if LLM API is configured.
        # Modified check: api_key corresponds to OpenAI/Doubao key in LLMClient, 
        # but if provider is Gemini, we don't store it in self.api_key attribute in the same way 
        # (check llm_client.py init logic).
        # We need a better check.
        if not (llm_client.api_key or (hasattr(llm_client, 'provider') and llm_client.provider == 'gemini')):
            print(f"[{problem_id}] SKIPPING AI generation (No API Key detected).")
            print(f"[{problem_id}] SKIPPING AI generation (No API Key).")
            # Create placeholder
            save_file(os.path.join(dir_path, "solution_thinking.md"), "TODO: Configure LLM_API_KEY to generate this.")
            save_file(os.path.join(dir_path, "std.cpp"), "// TODO: Configure LLM_API_KEY to generate this.")
        else:
            ai_result = llm_client.generate_content(problem)
            code = ai_result.get('code', '')
            analysis = ai_result.get('analysis', '')
            
            # --- Verification Loop ---
            if code and "TODO" not in code:
                is_ac, msg = verify_solution(oj_client, problem_id, code)
                if not is_ac:
                    print(f"[{problem_id}] Attempting to fix code via LLM...")
                    # Try to fix once
                    fix_result = llm_client.fix_solution(problem, code, msg)
                    new_code = fix_result.get('code')
                    if new_code:
                        print(f"[{problem_id}] Fix generated. Retrying verification...")
                        is_ac_2, msg_2 = verify_solution(oj_client, problem_id, new_code)
                        if is_ac_2:
                            print(f"[{problem_id}] Fix SUCCESS!")
                            code = new_code
                            analysis += "\n\n## 修正记录\n初次提交未通过，经自动修正后通过。"
                        else:
                             print(f"[{problem_id}] Fix FAILED again: {msg_2}")
                             analysis += f"\n\n## 验证警告\n自动生成的代码未通过测试。错误信息：{msg_2}"
            # -------------------------

            save_file(os.path.join(dir_path, "solution_thinking.md"), analysis)
            save_file(os.path.join(dir_path, "std.cpp"), code)
            print(f"[{problem_id}] Generated solution and code.")

        return True

    except Exception as e:
        print(f"[{problem_id}] Error processing: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    parser = argparse.ArgumentParser(description="Book Content Generator Workflow")
    parser.add_argument("--users", help="Username", default="andy")
    parser.add_argument("--pwd", help="Password", default="andy@5dg")
    parser.add_argument("--problems", help="Comma separated list of problem IDs (e.g. GW003,GW004) or ranges (GW001-GW010)", required=True)
    parser.add_argument("--output", help="Output directory", default="./book_content")
    
    args = parser.parse_args()
    
    # Init Clients
    oj_client = XMUOJClient()
    try:
        print("Logging in to XMUOJ...")
        oj_client.login(args.users, args.pwd)
        print("Login success.")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    llm_client = LLMClient()
    
    # Parse Problem List
    p_list = []
    parts = args.problems.split(',')
    for part in parts:
        if '-' in part:
            # Handle range? Simple implementation for GW prefix or purely integer ranges
            # Assuming format like GW001-GW005
            pass # Skipping complex range parsing for now, user can pass CSV
            # A simple implementation for integer ranges: 1001-1005
            try:
                start, end = part.split('-')
                if start.isdigit() and end.isdigit():
                    for i in range(int(start), int(end)+1):
                       p_list.append(str(i))
                elif start.startswith("GW") and end.startswith("GW"):
                     # Very dumb logic for GW codes if they are sequential
                     pass
            except:
                pass
        else:
            p_list.append(part.strip())
            
    # Process
    print(f"Starting processing {len(p_list)} problems: {p_list}")
    for i, pid in enumerate(p_list):
        process_problem(oj_client, llm_client, pid, args.output)
        
        # Polite delay to respect API rate limits (Tier-1 Free: 15 RPM, but let's be safe)
        if i < len(p_list) - 1:
            print("Waiting 60 seconds to respect Rate Limits...")
            time.sleep(60)

if __name__ == "__main__":
    main()
