import os

ROOT_DIR = "NQ100"

LINES_TO_REMOVE = [
    "#!/usr/bin/env python",
    "# -*- coding: utf-8 -*-"
]

def clean_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line in LINES_TO_REMOVE:
                continue
            new_lines.append(line)
            
        # Write back only if changes were made (optimization, but simple rewrite is fine usually)
        if len(lines) != len(new_lines):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Cleaned {file_path}")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    if not os.path.exists(ROOT_DIR):
        print(f"Directory {ROOT_DIR} not found.")
        return

    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                clean_file(file_path)

if __name__ == "__main__":
    main()
