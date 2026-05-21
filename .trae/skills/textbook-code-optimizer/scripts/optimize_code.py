#!/usr/bin/env python3
"""
Textbook Code Optimizer

This script optimizes C++ and Python code for textbook insertion, ensuring compactness, clarity, and educational value.
"""

import os
import re
import subprocess

class TextbookCodeOptimizer:
    def __init__(self):
        pass
    
    def optimize_cpp(self, input_file):
        """
        Optimize C++ code for textbook insertion
        """
        # Check if clang-format is available
        try:
            # Use clang-format with our custom K&R style
            result = subprocess.run(
                ['clang-format', '-style=file', input_file],
                capture_output=True,
                text=True,
                check=True
            )
            code = result.stdout
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to Python-based K&R style conversion if clang-format fails
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Process each line to convert to K&R style with proper indentation
            # and remove多余的换行，符合教材插入要求
            processed_lines = []
            indent_level = 0
            indent_size = 4
            
            for line in lines:
                # Remove leading/trailing whitespace
                line = line.strip()
                if not line:
                    continue
                
                # Handle closing braces first (decrease indent level)
                if line.startswith('}'):
                    indent_level -= 1
                
                # Add indentation
                indent = ' ' * (indent_level * indent_size)
                
                # Convert to K&R style (brace on same line)
                line = re.sub(r'\s*\{', ' {', line)
                line = re.sub(r'}\s*', '}', line)
                line = re.sub(r';\s*', ';', line)
                
                # Add the line with indentation
                processed_lines.append(indent + line)
                
                # Handle opening braces (increase indent level)
                if '{' in line and not line.endswith('}'):
                    indent_level += 1
            
            # 压缩代码，去掉多余的空行，符合教材插入要求
            # 1. 移除所有空行，只保留必要的结构
            compressed_lines = []
            for line in processed_lines:
                # 只添加非空行
                if line.strip():
                    compressed_lines.append(line)
            
            # 2. 重新组合代码，确保没有多余的空行
            code = '\n'.join(compressed_lines)
            
        # 无论是否使用clang-format，都应用代码压缩逻辑
        # 1. 移除所有空行，只保留必要的结构
        lines = code.split('\n')
        compressed_lines = []
        for line in lines:
            # 只添加非空行
            if line.strip():
                compressed_lines.append(line)
        
        # 2. 重新组合代码，确保没有多余的空行
        code = '\n'.join(compressed_lines)
        
        # 3. 进一步压缩：确保没有连续的空行
        code = re.sub(r'\n+', '\n', code)
        
        # Add key comments at algorithmic points
        # This is a placeholder - actual implementation would be more sophisticated
        code = code.replace('f[1][1] = a[1][1];', 'f[1][1] = a[1][1]; // 边界条件：顶点的路径和为自身')
        code = code.replace('f[i][j] = max(f[i-1][j-1], f[i-1][j]) + a[i][j];', 'f[i][j] = max(f[i-1][j-1], f[i-1][j]) + a[i][j]; // 取上方或左上方的最大值')
        code = code.replace('res = max(res, f[n][j]);', 'res = max(res, f[n][j]); // 最后一行的最大值即为答案')
        
        # Save optimized code
        # Generate NQXXX_improved.cpp file
        base_name = os.path.basename(input_file)
        if '_improved' in base_name:
            # If input file is already an improved version, keep the name
            output_file = input_file
        else:
            # Otherwise, create a new improved version
            output_file = os.path.splitext(input_file)[0] + '_improved.cpp'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(code)
        
        return output_file
    
    def generate_python(self, cpp_file):
        """
        Generate Python code from optimized C++ code
        """
        with open(cpp_file, 'r', encoding='utf-8') as f:
            cpp_code = f.read()
        
        # Generate Python code based on problem type
        python_code = ""
        
        # Identify problem type based on code patterns
        problem_type = "unknown"
        if "maxSlength" in cpp_code and "s1" in cpp_code and "s2" in cpp_code:
            problem_type = "最长公共子序列"
        elif "get_divisors" in cpp_code and "n % i == 0" in cpp_code:
            problem_type = "求约数"
        elif "divide" in cpp_code and "n % i == 0" in cpp_code:
            problem_type = "质因数分解"
        elif "qmi" in cpp_code and "k & 1" in cpp_code:
            problem_type = "快速幂"
        elif ("max_element" in cpp_code and "dp" in cpp_code and "heights" in cpp_code) or ("tails" in cpp_code and "lower_bound" in cpp_code and "greater<int>" in cpp_code):
            problem_type = "最长不上升子序列"
        
        # Generate Python code based on problem type
        if problem_type == "最长不上升子序列":
            python_code = """
# Python equivalent of the optimized C++ code
# 最长不上升子序列问题（优化版）
import sys
def main():
    # Read input
    n = int(sys.stdin.readline())
    heights = list(map(int, sys.stdin.readline().split()))
    # 优化算法：贪心 + 二分查找 O(n log n)
    tails = []
    for h in heights:
        # 找到第一个小于h的位置（因为是不上升，所以找第一个小于h的位置）
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < h:
                right = mid
            else:
                left = mid + 1
        if left == len(tails):
            tails.append(h)
        else:
            tails[left] = h
    print(len(tails))
if __name__ == "__main__":
    main()
"""
        elif problem_type == "求约数":
            python_code = """
# Python equivalent of the optimized C++ code
# 求约数问题
import sys
def get_divisors(n):
    res = []
    i = 1
    while i <= n // i:
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
        i += 1
    res.sort()
    return res
def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        a = int(sys.stdin.readline())
        res = get_divisors(a)
        print(' '.join(map(str, res)))
if __name__ == "__main__":
    main()
"""
        elif problem_type == "质因数分解":
            python_code = """
# Python equivalent of the optimized C++ code
# 质因数分解问题
import sys
def divide(n):
    i = 2
    while i <= n // i:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n = n // i
            print(f'{i} {cnt}')
        i += 1
    if n > 1:
        print(f'{n} 1')
def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        x = int(sys.stdin.readline())
        divide(x)
if __name__ == "__main__":
    main()
"""
        elif problem_type == "快速幂":
            python_code = """
# Python equivalent of the optimized C++ code
# 快速幂问题
import sys
def qmi(a, k, p):
    res = 1
    while k:
        if k & 1:
            res = res * a % p
        a = a * a % p
        k >>= 1
    return res
def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, k, p = map(int, sys.stdin.readline().split())
        print(qmi(a, k, p))
if __name__ == "__main__":
    main()
"""
        else:
            # Default template
            python_code = """
# Python equivalent of the optimized C++ code
# This is a template that needs to be manually updated
import sys
def main():
    # Read input
    # TODO: Implement input handling based on the C++ code
    # TODO: Implement algorithm based on the C++ code
    pass
if __name__ == "__main__":
    main()
"""

        
        # Save Python code
        # Generate NQXXX_improved.py file
        base_name = os.path.basename(cpp_file)
        if '_improved' in base_name:
            # If cpp file is an improved version, generate corresponding improved Python file
            output_file = os.path.splitext(cpp_file)[0] + '.py'
        else:
            # Otherwise, create a new improved version
            output_file = os.path.splitext(cpp_file)[0] + '_improved.py'
        
        # 压缩Python代码，去掉多余的空行，符合教材插入要求
        # 1. 移除所有空行，只保留必要的结构
        lines = python_code.split('\n')
        compressed_lines = []
        for line in lines:
            # 只添加非空行
            if line.strip():
                compressed_lines.append(line)
        
        # 2. 重新组合代码，确保没有多余的空行
        compressed_python_code = '\n'.join(compressed_lines)
        
        # 3. 进一步压缩：确保没有连续的空行
        compressed_python_code = re.sub(r'\n+', '\n', compressed_python_code)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(compressed_python_code)
        
        return output_file
    
    def generate_思路(self, cpp_file, problem_name):
        """
        Generate algorithm explanation document
        """
        # Read the C++ code to identify problem type
        with open(cpp_file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Identify problem type based on code patterns
        problem_type = "unknown"
        if "volume" in code and "value" in code and "dp[" in code:
            problem_type = "01背包"
        elif "a[i][j]" in code and "f[i][j]" in code and "max(f[i-1][j-1], f[i-1][j])" in code:
            problem_type = "数字三角形"
        elif "maxSlength" in code and "s1" in code and "s2" in code and "s1[i - 1] == s2[j - 1]" in code:
            problem_type = "最长公共子序列"
        elif ("wall[" in code or "dp[" in code) and "4 * " in code and "- " in code and "i - 2" in code and "i - 4" in code:
            problem_type = "瓷砖铺放"
        elif "get_divisors" in code and "n % i == 0" in code and "sort" in code:
            problem_type = "求约数"
        elif "divide" in code and "n % i == 0" in code and "printf" in code:
            problem_type = "质因数分解"
        elif "qmi" in code and "k & 1" in code and "k >>= 1" in code:
            problem_type = "快速幂"
        elif "vector<int> res" in code and "res.push_back(1)" in code and "x *= i" in code:
            problem_type = "大整数阶乘"
        elif "is_humbernumber" in code or "is_humble_number" in code:
            problem_type = "谦虚数"
        
        # Generate a generic template for 思路文档
        思路文档 = f"""
# {problem_name} 思路分析

## 问题描述
待补充

## 思考过程
待补充

## 算法思路
待补充

## 实现步骤
待补充

## 关键点编码逻辑
待补充

## 时间复杂度
待补充
"""
        
        # Save 思路文档
        # Save as 思路.md in the same directory
        output_dir = os.path.dirname(cpp_file)
        output_file = os.path.join(output_dir, '思路.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(思路文档)
        
        return output_file
    
    def generate_docx(self, problem_number):
        """
        Generate DOCX document for the problem
        """
        # Path to the generate_single_t_shape_doc.py script
        # Using absolute path for reliability
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
        script_path = os.path.join(base_dir, '兴趣班入门百练讲义', 'generate_single_t_shape_doc.py')
        
        # Run the script to generate DOCX
        try:
            result = subprocess.run(['python', script_path, str(problem_number)], 
                                   capture_output=True, text=True, cwd=os.path.dirname(script_path))
            print(result.stdout)
            if result.stderr:
                print(f"Error: {result.stderr}")
            return True
        except Exception as e:
            print(f"Error generating DOCX: {e}")
            return False

def main():
    """
    Main function for textbook code optimizer
    """
    optimizer = TextbookCodeOptimizer()
    
    # Example usage
    # cpp_file = optimizer.optimize_cpp('NQ085.cpp')
    # python_file = optimizer.generate_python(cpp_file)
    # 思路_file = optimizer.generate_思路(cpp_file, 'NQ085')
    # optimizer.generate_docx(85)  # Generate DOCX for problem 85
    
    print("Textbook Code Optimizer initialized")

if __name__ == "__main__":
    main()
