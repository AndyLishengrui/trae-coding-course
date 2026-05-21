import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'xmuoj-mcp'))
from server import XMUOJClient
import time

def main():
    client = XMUOJClient()
    try:
        print("Logging in...")
        client.login("andy", "andy@5dg")
        print("Logged in.")
        
        print("Fetching problem details to get internal ID...")
        problem_info = client.get_problem("GW003")
        internal_id = problem_info.get('id')
        print(f"Internal ID for GW003 is {internal_id}")
        
        code = """#include <iostream>
using namespace std;
int main() {
    char c;
    cin >> c;
    cout << (int)c << endl;
    return 0;
}"""
        
        print(f"Submitting code for GW003 (Internal ID: {internal_id})...")
        submission_id = client.submit_code(internal_id, code, language="C++")
        print(f"Submission ID: {submission_id}")
        
        print("Polling for result...")
        # Simple polling loop similar to server.py implementation
        for _ in range(20):
            result = client.get_result(submission_id)
            # result code: 0 usually AC, -1/-2 pending
            res_code = result.get('result')
            print(f"Current status code: {res_code}")
            
            if res_code not in [-1, -2]:
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
                print(f"Final Result: {status_text}")
                
                info = result.get('statistic_info', {})
                if info:
                    print(f"Time: {info.get('time_cost')}ms")
                    print(f"Memory: {info.get('memory_cost')}bytes")
                
                err = result.get('err_info')
                if err:
                    print(f"Error Info: {err}")
                    
                break
            time.sleep(1)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
