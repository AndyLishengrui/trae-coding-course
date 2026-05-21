import sys
import os

# 添加 xmuoj-mcp 目录到 Python 路径
sys.path.append('/Users/andyshengruilee/Documents/2024-2025课件/兴趣班入门百练讲义/xmuoj-mcp')

from server import XMUOJClient

# 创建客户端实例
client = XMUOJClient()

print("=== XMUOJ MCP 工具使用 ===")

# 1. 登录
print("\n1. 登录 XMUOJ...")
try:
    result = client.login("andy", "andy@5dg")
    print(f"登录结果: {result}")
except Exception as e:
    print(f"登录失败: {e}")
    sys.exit(1)

# 2. 获取题目内容
print("\n2. 获取 GW003 题目内容...")
try:
    problem = client.get_problem("GW003")
    print(f"题目标题: {problem['title']}")
    print(f"题目描述: {problem['description']}")
    print(f"输入描述: {problem['input_description']}")
    print(f"输出描述: {problem['output_description']}")
    
    # 打印样例
    samples = problem.get('samples', [])
    for i, sample in enumerate(samples):
        print(f"\n样例 {i+1}:")
        print(f"输入: {sample['input']}")
        print(f"输出: {sample['output']}")
except Exception as e:
    print(f"获取题目失败: {e}")
    sys.exit(1)

# 3. 提交代码
print("\n3. 提交代码...")
# 使用更基础的 C++ 语法，避免使用 static_cast
code = "#include <iostream>\nusing namespace std;\n\nint main() {\n    char c;\n    cin >> c;\n    cout << (int)c << endl;\n    return 0;\n}\n"

try:
    # 使用从题目信息中获取的整数 ID
    problem_id = problem.get('id', 'GW003')
    print(f"使用的 problem_id: {problem_id}")
    
    submission_id = client.submit_code(problem_id, code, "C++")
    print(f"提交成功! Submission ID: {submission_id}")
    
    # 4. 获取评测结果
    print("\n4. 获取评测结果...")
    import time
    max_retries = 20
    for _ in range(max_retries):
        result = client.get_result(submission_id)
        curr_result = result.get('result')
        if curr_result not in [-1, -2]:
            # 评测完成
            print(f"评测结果: {result}")
            
            # 检查是否有编译错误信息
            if curr_result == 7:  # Compile Error
                print("\n编译错误! 检查代码...")
                # 尝试使用不同的语言选项
                print("\n尝试使用 'C++11' 语言选项重新提交...")
                try:
                    submission_id2 = client.submit_code(problem_id, code, "C++11")
                    print(f"重新提交成功! Submission ID: {submission_id2}")
                    
                    # 等待新的评测结果
                    print("\n等待新的评测结果...")
                    for _ in range(max_retries):
                        result2 = client.get_result(submission_id2)
                        curr_result2 = result2.get('result')
                        if curr_result2 not in [-1, -2]:
                            print(f"新评测结果: {result2}")
                            break
                        time.sleep(1)
                except Exception as e:
                    print(f"重新提交失败: {e}")
            break
        time.sleep(1)
    else:
        print("评测超时，请手动查看结果")
        
except Exception as e:
    print(f"提交代码失败: {e}")
    # 打印问题信息，查看可用的字段
    print("\n问题信息字段:")
    for key, value in problem.items():
        print(f"{key}: {value}")
    sys.exit(1)

print("\n=== 任务完成 ===")
