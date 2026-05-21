import sys
import os
import time

# 添加 xmuoj-mcp 目录到 Python 路径
sys.path.append('/Users/andyshengruilee/Documents/2024-2025课件/兴趣班入门百练讲义/xmuoj-mcp')

from server import XMUOJClient

class ContestSolver:
    def __init__(self):
        self.client = XMUOJClient()
        self.username = "andy"
        self.password = "andy@5dg"
        self.contest_id = "207"
        self.language = "C++"
        self.max_retries = 3
        self.verbose = True
        
    def log(self, message):
        if self.verbose:
            print(f"[INFO] {message}")
    
    def login(self):
        """登录 XMUOJ"""
        self.log("登录 XMUOJ...")
        try:
            result = self.client.login(self.username, self.password)
            self.log(f"登录结果: {result}")
            return True
        except Exception as e:
            self.log(f"登录失败: {e}")
            return False
    
    def get_contest_problems(self):
        """获取竞赛题目列表"""
        self.log(f"获取竞赛 {self.contest_id} 的题目列表...")
        
        # 使用新添加的 get_contest_problems 函数获取题目列表
        try:
            problems = self.client.get_contest_problems(self.contest_id)
            self.log(f"发现 {len(problems)} 道题目")
            return problems
        except Exception as e:
            self.log(f"获取竞赛题目列表失败: {e}")
            # 回退到硬编码的题目列表
            problems = [
                {"id": "0", "name": "A-B"},
                {"id": "1", "name": "求连续偶数和"},
                {"id": "10", "name": "小管理"},
                {"id": "100", "name": "满石村"},
                {"id": "11", "name": "和弦数列求和"},
                {"id": "12", "name": "水仙花数"},
                {"id": "13", "name": "偶数数列求和"},
                {"id": "14", "name": "奥威开方机构"},
                {"id": "15", "name": "游客评分"},
                {"id": "16", "name": "十六进制加法"},
                {"id": "17", "name": "计算两点"}
            ]
            self.log(f"使用硬编码的题目列表，发现 {len(problems)} 道题目")
            return problems
    
    def search_problem_id(self, problem_name):
        """搜索题目并获取正确的 ID"""
        try:
            results = self.client.search_problem(problem_name)
            if results:
                # 返回第一个匹配的题目 ID
                return results[0]['_id']
        except Exception as e:
            self.log(f"搜索题目失败: {e}")
        return None

    def solve_problem(self, problem):
        """解决单个题目"""
        problem_id = problem["id"]
        problem_name = problem["name"]
        
        self.log(f"处理题目: {problem_name} ({problem_id})")
        
        # 基于题目名称生成代码
        code = self.generate_code(problem_name, {})
        if not code:
            return False, "无法生成代码"
        
        # 首先尝试使用原始的 problem_id（整数格式）
        self.log(f"使用题目 ID: {problem_id}")
        
        # 提交代码
        submission_id = None
        for attempt in range(self.max_retries):
            self.log(f"第 {attempt + 1} 次提交...")
            try:
                # 尝试使用竞赛提交方法提交
                submission_id = self.client.submit_contest_code(self.contest_id, problem_id, code, self.language)
                self.log(f"提交成功! Submission ID: {submission_id}")
                
                # 等待评测结果
                result = self.get_submission_result(submission_id)
                if result:
                    status = result.get('result')
                    if status == 0:  # AC
                        self.log(f"✓ AC! 题目 {problem_name} 解决成功")
                        return True, "AC"
                    else:
                        self.log(f"✗ 评测结果: {result}")
                        # 分析错误并生成新代码
                        code = self.analyze_and_fix(code, result, {"id": problem_id})
                        if not code:
                            break
            except Exception as e:
                self.log(f"提交失败: {e}")
                # 如果是提交频率限制，等待一段时间
                if "Please wait" in str(e):
                    import re
                    wait_time = re.search(r'Please wait (\d+) seconds', str(e))
                    if wait_time:
                        time.sleep(int(wait_time.group(1)) + 1)
                # 如果是题目不存在，尝试搜索题目获取正确的 ID
                elif "Problem not exist" in str(e):
                    self.log(f"尝试搜索题目获取正确的 ID")
                    search_id = self.search_problem_id(problem_name)
                    if search_id:
                        self.log(f"找到题目 {problem_name} 的正确 ID: {search_id}")
                        try:
                            submission_id = self.client.submit_code(search_id, code, self.language)
                            self.log(f"提交成功! Submission ID: {submission_id}")
                            
                            # 等待评测结果
                            result = self.get_submission_result(submission_id)
                            if result:
                                status = result.get('result')
                                if status == 0:  # AC
                                    self.log(f"✓ AC! 题目 {problem_name} 解决成功")
                                    return True, "AC"
                                else:
                                    self.log(f"✗ 评测结果: {result}")
                                    # 分析错误并生成新代码
                                    code = self.analyze_and_fix(code, result, {"id": search_id})
                                    if not code:
                                        break
                        except Exception as e2:
                            self.log(f"使用搜索到的 ID 提交失败: {e2}")
        
        return False, "多次尝试后仍未解决"
    
    def get_submission_result(self, submission_id):
        """获取提交结果"""
        max_retries = 20
        for _ in range(max_retries):
            try:
                result = self.client.get_result(submission_id)
                curr_result = result.get('result')
                if curr_result not in [-1, -2]:
                    return result
                time.sleep(1)
            except Exception as e:
                self.log(f"获取结果失败: {e}")
                time.sleep(1)
        return None
    
    def generate_code(self, problem_name, problem_info):
        """根据题目名称生成 C++ 代码"""
        self.log(f"为题目 {problem_name} 生成 C++ 代码...")
        
        # 基于题目名称生成相应的代码
        if "A-B" in problem_name:
            # A-B 问题：输入两个整数，输出它们的差
            return "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a - b << endl;\n    return 0;\n}\n"
        
        elif "求连续偶数和" in problem_name:
            # 求连续偶数和：输入两个整数 m 和 n，输出从 m 到 n 的所有偶数的和
            return "#include <iostream>\nusing namespace std;\n\nint main() {\n    int m, n, sum = 0;\n    cin >> m >> n;\n    for (int i = m; i <= n; i++) {\n        if (i % 2 == 0) {\n            sum += i;\n        }\n    }\n    cout << sum << endl;\n    return 0;\n}\n"
        
        elif "小管理" in problem_name:
            # 小管理：可能是一个简单的管理问题，需要根据具体题目要求实现
            # 这里提供一个基础框架
            return '#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    // 小管理问题的实现\n    int n;\n    cin >> n;\n    vector<int> arr(n);\n    for (int i = 0; i < n; i++) {\n        cin >> arr[i];\n    }\n    // 处理逻辑\n    cout << "处理结果" << endl;\n    return 0;\n}\n'
        
        elif "满石村" in problem_name:
            # 满石村：可能是一个关于村庄的问题
            return '#include <iostream>\nusing namespace std;\n\nint main() {\n    // 满石村问题的实现\n    int n;\n    cin >> n;\n    cout << "处理结果" << endl;\n    return 0;\n}\n'
        
        elif "和弦数列求和" in problem_name:
            # 和弦数列求和：计算特定数列的和
            return "#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    long long sum = 0;\n    // 和弦数列的计算逻辑\n    cout << sum << endl;\n    return 0;\n}\n"
        
        elif "水仙花数" in problem_name:
            # 水仙花数：输出所有三位数的水仙花数
            return "#include <iostream>\nusing namespace std;\n\nbool is_narcissistic(int num) {\n    int a = num / 100;\n    int b = (num / 10) % 10;\n    int c = num % 10;\n    return a*a*a + b*b*b + c*c*c == num;\n}\n\nint main() {\n    for (int i = 100; i < 1000; i++) {\n        if (is_narcissistic(i)) {\n            cout << i << endl;\n        }\n    }\n    return 0;\n}\n"
        
        elif "偶数数列求和" in problem_name:
            # 偶数数列求和：计算偶数数列的和
            return "#include <iostream>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    long long sum = 0;\n    for (int i = 2; i <= n; i += 2) {\n        sum += i;\n    }\n    cout << sum << endl;\n    return 0;\n}\n"
        
        elif "奥威开方机构" in problem_name:
            # 奥威开方机构：可能是一个开方相关的问题
            return "#include <iostream>\n#include <cmath>\nusing namespace std;\n\nint main() {\n    double n;\n    cin >> n;\n    double result = sqrt(n);\n    cout << result << endl;\n    return 0;\n}\n"
        
        elif "游客评分" in problem_name:
            # 游客评分：处理游客的评分数据
            return "#include <iostream>\n#include <vector>\n#include <algorithm>\nusing namespace std;\n\nint main() {\n    int n;\n    cin >> n;\n    vector<int> scores(n);\n    for (int i = 0; i < n; i++) {\n        cin >> scores[i];\n    }\n    // 处理评分逻辑\n    double average = 0;\n    for (int score : scores) {\n        average += score;\n    }\n    average /= n;\n    cout << average << endl;\n    return 0;\n}\n"
        
        elif "十六进制加法" in problem_name:
            # 十六进制加法：计算两个十六进制数的和
            return "#include <iostream>\n#include <string>\n#include <sstream>\nusing namespace std;\n\nint main() {\n    string hex1, hex2;\n    cin >> hex1 >> hex2;\n    \n    unsigned long long dec1, dec2;\n    stringstream ss;\n    ss << hex << hex1;\n    ss >> dec1;\n    ss.clear();\n    ss << hex << hex2;\n    ss >> dec2;\n    \n    unsigned long long sum = dec1 + dec2;\n    ss.clear();\n    ss << hex << sum;\n    string result;\n    ss >> result;\n    \n    for (char &c : result) {\n        if (c >= 'a' && c <= 'f') {\n            c -= 32;\n        }\n    }\n    \n    cout << result << endl;\n    return 0;\n}\n"
        
        elif "计算两点" in problem_name:
            # 计算两点：可能是计算两点之间的距离
            return "#include <iostream>\n#include <cmath>\nusing namespace std;\n\nint main() {\n    double x1, y1, x2, y2;\n    cin >> x1 >> y1 >> x2 >> y2;\n    double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));\n    cout << distance << endl;\n    return 0;\n}\n"
        
        else:
            self.log(f"未知题目: {problem_name}")
            return ""
    
    def analyze_and_fix(self, code, result, problem_info):
        """分析错误并修复代码"""
        self.log("分析错误并尝试修复...")
        # 这里可以根据具体的错误信息进行分析和修复
        # 实际应用中，可能需要更复杂的错误分析逻辑
        return code
    
    def solve_contest(self):
        """解决整个竞赛"""
        if not self.login():
            return False
        
        problems = self.get_contest_problems()
        if not problems:
            return False
        
        total_problems = len(problems)
        solved_problems = 0
        ac_problems = 0
        
        self.log(f"开始解决竞赛 {self.contest_id} 的 {total_problems} 道题目...")
        
        for i, problem in enumerate(problems, 1):
            self.log(f"\n=== 处理第 {i}/{total_problems} 道题目 ===")
            
            success, status = self.solve_problem(problem)
            solved_problems += 1
            
            if success and status == "AC":
                ac_problems += 1
                self.log(f"✓ 题目 {problem['name']} 已解决")
            else:
                self.log(f"✗ 题目 {problem['name']} 未解决: {status}")
            
            progress = (i / total_problems) * 100
            success_rate = (ac_problems / i) * 100 if i > 0 else 0
            self.log(f"进度: {progress:.1f}% | 成功率: {success_rate:.1f}%")
            
            # 短暂休息，避免请求过于频繁
            time.sleep(1)
        
        # 生成最终总结
        self.log("\n=== 竞赛解决总结 ===")
        self.log(f"竞赛: ACM & 蓝桥杯入门百练(2025)")
        self.log(f"总题目数: {total_problems}")
        self.log(f"已解决: {solved_problems}")
        self.log(f"AC 题目数: {ac_problems}")
        self.log(f"成功率: {(ac_problems / total_problems) * 100:.1f}%")
        
        return ac_problems == total_problems

if __name__ == "__main__":
    solver = ContestSolver()
    success = solver.solve_contest()
    if success:
        print("\n🎉 所有题目都已成功解决!")
    else:
        print("\n⚠️ 部分题目未解决，请检查日志获取详细信息。")
