#!/usr/bin/env python3
import os
import re

def shorten_cpp_file(input_path, output_path):
    """为C++文件创建短行版本"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            line = line.rstrip()
            # 跳过空行和注释
            if not line or line.strip().startswith('//'):
                new_lines.append(line)
                continue
            
            # 处理长行
            if len(line) > 60:
                # 处理cout语句
                if 'cout <<' in line:
                    parts = line.split('<<')
                    if len(parts) > 2:
                        new_lines.append(parts[0] + '<<' + parts[1])
                        for i in range(2, len(parts)):
                            new_lines.append('             <<' + parts[i])
                        continue
                
                # 处理vector初始化
                if 'vector<' in line and '=' in line:
                    parts = line.split('=')
                    if len(parts) == 2:
                        new_lines.append(parts[0] + '=')
                        new_lines.append('    ' + parts[1])
                        continue
            
            new_lines.append(line)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        return True
    except Exception as e:
        print(f"Error processing C++ file {input_path}: {e}")
        return False

def shorten_py_file(input_path, output_path):
    """为Python文件创建短行版本"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            line = line.rstrip()
            # 跳过空行和注释
            if not line or line.strip().startswith('#'):
                new_lines.append(line)
                continue
            
            # 处理长行
            if len(line) > 60:
                # 处理列表初始化
                if '[' in line and ']' in line:
                    parts = line.split('[')
                    if len(parts) == 2:
                        new_lines.append(parts[0] + '[')
                        elements = parts[1].rstrip(']').split(',')
                        for i, elem in enumerate(elements):
                            indent = ' ' * (len(parts[0]) + 4)
                            if i == len(elements) - 1:
                                new_lines.append(indent + elem.strip() + ']')
                            else:
                                new_lines.append(indent + elem.strip() + ',')
                        continue
                
                # 处理print语句
                if 'print(' in line:
                    parts = line.split('print(')
                    if len(parts) == 2:
                        new_lines.append(parts[0] + 'print(')
                        new_lines.append('    ' + parts[1])
                        continue
            
            new_lines.append(line)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        return True
    except Exception as e:
        print(f"Error processing Python file {input_path}: {e}")
        return False

def main():
    base_dir = '/Users/andyshengruilee/Downloads/基于Trae的编程兴趣班入门百练/兴趣班入门百练讲义/NQ100'
    
    for i in range(1, 101):
        dir_name = f'NQ{i:03d}'
        dir_path = os.path.join(base_dir, dir_name)
        
        if not os.path.exists(dir_path):
            continue
        
        # 检查是否存在压缩代码文件
        cpp_compressed = os.path.join(dir_path, 'cpp_compressed.cpp')
        py_compressed = os.path.join(dir_path, 'solution_compressed.py')
        
        if os.path.exists(cpp_compressed):
            cpp_short = os.path.join(dir_path, 'solution_short.cpp')
            print(f"Processing C++ file for {dir_name}...")
            shorten_cpp_file(cpp_compressed, cpp_short)
        
        if os.path.exists(py_compressed):
            py_short = os.path.join(dir_path, 'solution_short.py')
            print(f"Processing Python file for {dir_name}...")
            shorten_py_file(py_compressed, py_short)
    
    print("Processing completed!")

if __name__ == "__main__":
    main()