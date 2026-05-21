#!/usr/bin/env python3
import os

def optimize_cpp_file(input_path, output_path):
    """优化C++文件，减少行数，去掉非关键注释，重构函数名和变量名"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 处理C++代码
        new_lines = []
        in_comment = False
        
        for line in lines:
            original_line = line
            line = line.strip()
            
            # 跳过空行
            if not line:
                continue
            
            # 处理注释
            if line.startswith('//'):
                # 保留与算法相关的注释
                comment_content = line[2:].strip()
                if any(keyword in comment_content for keyword in ['算法', '思路', '步骤', '注意', '关键', '实现', '逻辑', '处理', '检查', '条件', '循环', '递归', '复杂度']):
                    new_lines.append(original_line.strip())
                continue
            if line.startswith('/*'):
                in_comment = True
                continue
            if in_comment:
                if '*/' in line:
                    in_comment = False
                continue
            
            # 简化命名空间
            if 'using namespace std;' in line:
                new_lines.append('using namespace std;')
                continue
            
            # 简化输入输出优化
            if 'ios_base::sync_with_stdio' in line:
                new_lines.append('ios::sync_with_stdio(0);')
                continue
            if 'cin.tie(NULL)' in line or 'cin.tie(0)' in line:
                new_lines.append('cin.tie(0);')
                continue
            
            # 重构函数名和变量名
            # 简化函数名
            line = line.replace('CheckPasswordSafety', 'check')
            line = line.replace('main', 'main')
            
            # 简化变量名
            line = line.replace('password', 's')
            line = line.replace('len', 'n')
            line = line.replace('length', 'n')
            line = line.replace('type_present', 't')
            line = line.replace('types_count', 'cnt')
            line = line.replace('test_cases', 't')
            line = line.replace('T', 't')
            line = line.replace('is_lower', 'l')
            line = line.replace('is_upper', 'u')
            line = line.replace('is_digit', 'd')
            line = line.replace('is_special', 'sp')
            
            # 简化cout语句
            line = line.replace('cout << ', 'cout<<')
            line = line.replace(' << endl', '\n')
            line = line.replace('<< endl', '\n')
            
            # 简化return语句
            line = line.replace('return 0;', 'return 0;')
            
            new_lines.append(line)
        
        # 进一步压缩，合并短小的语句
        compressed_lines = []
        i = 0
        while i < len(new_lines):
            line = new_lines[i]
            
            # 合并变量声明和初始化
            if 'int ' in line and '=' in line and ';' in line:
                compressed_lines.append(line)
            elif 'string ' in line and '=' in line and ';' in line:
                compressed_lines.append(line)
            elif 'char ' in line and '=' in line and ';' in line:
                compressed_lines.append(line)
            # 合并条件判断和输出
            elif 'if (' in line and ')' in line and '{' in line:
                if i + 1 < len(new_lines) and 'cout<<' in new_lines[i+1]:
                    cond = line.split('{')[0].strip()
                    output = new_lines[i+1].replace(';', '').strip()
                    compressed_lines.append(f'{cond} {output};')
                    i += 1
                else:
                    compressed_lines.append(line)
            else:
                compressed_lines.append(line)
            i += 1
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(compressed_lines))
        
        return True
    except Exception as e:
        print(f"Error optimizing C++ file {input_path}: {e}")
        return False

def optimize_py_file(input_path, output_path):
    """优化Python文件，减少行数，去掉非关键注释，重构函数名和变量名"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 处理Python代码
        new_lines = []
        
        for line in lines:
            original_line = line
            line = line.strip()
            
            # 跳过空行
            if not line:
                continue
            
            # 处理注释
            if line.startswith('#'):
                # 保留与算法相关的注释
                comment_content = line[1:].strip()
                if any(keyword in comment_content for keyword in ['算法', '思路', '步骤', '注意', '关键', '实现', '逻辑', '处理', '检查', '条件', '循环', '递归', '复杂度']):
                    new_lines.append(original_line.strip())
                continue
            
            # 重构函数名和变量名
            # 简化函数名
            line = line.replace('check_password', 'check')
            line = line.replace('main', 'main')
            
            # 简化变量名
            line = line.replace('password', 's')
            line = line.replace('types', 't')
            line = line.replace('test_cases', 't')
            line = line.replace('T', 't')
            line = line.replace('is_lower', 'l')
            line = line.replace('is_upper', 'u')
            line = line.replace('is_digit', 'd')
            line = line.replace('is_special', 'sp')
            line = line.replace('passwords', 'ps')
            line = line.replace('result', 'res')
            
            # 简化条件判断
            line = line.replace('if len(', 'if len(')
            line = line.replace('return False', 'return 0')
            line = line.replace('return True', 'return 1')
            
            # 简化print语句
            line = line.replace('print("YES")', 'print("YES")')
            line = line.replace('print("NO")', 'print("NO")')
            
            new_lines.append(line)
        
        # 进一步压缩，合并短小的语句
        compressed_lines = []
        i = 0
        while i < len(new_lines):
            line = new_lines[i]
            
            # 合并变量声明和初始化
            if '=' in line and ';' not in line:
                compressed_lines.append(line)
            # 合并条件判断和输出
            elif 'if check(' in line:
                if i + 1 < len(new_lines) and 'print' in new_lines[i+1]:
                    cond = line.split(':')[0].strip()
                    output = new_lines[i+1].strip()
                    compressed_lines.append(f'{cond}: {output}')
                    i += 1
                else:
                    compressed_lines.append(line)
            else:
                compressed_lines.append(line)
            i += 1
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(compressed_lines))
        
        return True
    except Exception as e:
        print(f"Error optimizing Python file {input_path}: {e}")
        return False

def main():
    base_dir = '/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练/兴趣班入门百练讲义/NQ100'
    
    for i in range(1, 101):
        dir_name = f'NQ{i:03d}'
        dir_path = os.path.join(base_dir, dir_name)
        
        if not os.path.exists(dir_path):
            continue
        
        # 处理C++文件
        cpp_short = os.path.join(dir_path, 'solution_short.cpp')
        if os.path.exists(cpp_short):
            print(f"Optimizing C++ file for {dir_name}...")
            optimize_cpp_file(cpp_short, cpp_short)
        
        # 处理Python文件
        py_short = os.path.join(dir_path, 'solution_short.py')
        if os.path.exists(py_short):
            print(f"Optimizing Python file for {dir_name}...")
            optimize_py_file(py_short, py_short)
    
    print("Optimization completed!")

if __name__ == "__main__":
    main()