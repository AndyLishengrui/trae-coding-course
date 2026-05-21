#!/usr/bin/env python3
import os

def optimize_cpp_file(input_path, output_path):
    """优化C++文件，减少行数但保持可读性，保留关键注释，重构函数名和变量名"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 处理C++代码
        new_lines = []
        indent_level = 0
        indent_size = 4
        
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
                    new_lines.append(' ' * indent_level + line)
                continue
            
            # 处理代码行
            
            # 减少缩进级别（如果是结束括号）
            if line.startswith('}'):
                indent_level -= 1
            
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
            
            # 简化输入输出优化
            line = line.replace('ios_base::sync_with_stdio(false);', 'ios::sync_with_stdio(0);')
            line = line.replace('cin.tie(NULL);', 'cin.tie(0);')
            
            # 添加适当的空格
            line = line.replace('cout<<', 'cout << ')
            line = line.replace('cin>>', 'cin >> ')
            line = line.replace('<<endl', '<< endl')
            line = line.replace('if(', 'if (')
            line = line.replace('for(', 'for (')
            line = line.replace('while(', 'while (')
            line = line.replace('){', ') {')
            line = line.replace('==', ' == ')
            line = line.replace('!=', ' != ')
            line = line.replace('<', ' < ')
            line = line.replace('>', ' > ')
            line = line.replace('<=', ' <= ')
            line = line.replace('>=', ' >= ')
            line = line.replace('+=', ' += ')
            line = line.replace('-=', ' -= ')
            line = line.replace('*=', ' *= ')
            line = line.replace('/=', ' /= ')
            line = line.replace('&&', ' && ')
            line = line.replace('||', ' || ')
            line = line.replace('!', '! ')
            line = line.replace(';', ';')
            
            # 添加缩进
            indented_line = ' ' * indent_level + line
            new_lines.append(indented_line)
            
            # 增加缩进级别（如果是开始括号）
            if line.endswith('{'):
                indent_level += 1
        
        # 写入优化后的代码
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        return True
    except Exception as e:
        print(f"Error optimizing C++ file {input_path}: {e}")
        return False

def optimize_py_file(input_path, output_path):
    """优化Python文件，减少行数但保持可读性，保留关键注释，重构函数名和变量名"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 处理Python代码
        new_lines = []
        indent_level = 0
        indent_size = 4
        
        for line in lines:
            original_line = line
            line = line.rstrip()
            
            # 跳过空行
            if not line:
                continue
            
            # 处理注释
            if line.startswith('#'):
                # 保留与算法相关的注释
                comment_content = line[1:].strip()
                if any(keyword in comment_content for keyword in ['算法', '思路', '步骤', '注意', '关键', '实现', '逻辑', '处理', '检查', '条件', '循环', '递归', '复杂度']):
                    new_lines.append(line)
                continue
            
            # 计算缩进级别
            current_indent = len(line) - len(line.lstrip())
            indent_level = current_indent // indent_size
            
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
            
            # 保持Python代码的可读性
            stripped_line = line.strip()
            indented_line = ' ' * (indent_level * indent_size) + stripped_line
            new_lines.append(indented_line)
        
        # 写入优化后的代码
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
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
            # 先从原始的cpp_compressed.cpp重新生成，因为当前的solution_short.cpp已经被破坏
            cpp_compressed = os.path.join(dir_path, 'cpp_compressed.cpp')
            if os.path.exists(cpp_compressed):
                optimize_cpp_file(cpp_compressed, cpp_short)
            else:
                optimize_cpp_file(cpp_short, cpp_short)
        
        # 处理Python文件
        py_short = os.path.join(dir_path, 'solution_short.py')
        if os.path.exists(py_short):
            print(f"Optimizing Python file for {dir_name}...")
            # 先从原始的solution_compressed.py重新生成
            py_compressed = os.path.join(dir_path, 'solution_compressed.py')
            if os.path.exists(py_compressed):
                optimize_py_file(py_compressed, py_short)
            else:
                optimize_py_file(py_short, py_short)
    
    print("Optimization completed with readability preserved!")

if __name__ == "__main__":
    main()