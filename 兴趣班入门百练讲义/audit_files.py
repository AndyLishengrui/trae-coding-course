import os
import re

ROOT_DIR = "NQ100"

def get_sorted_dirs():
    valid_dirs = []
    if os.path.exists(ROOT_DIR):
        for d in os.listdir(ROOT_DIR):
            if d.startswith("NQ") and os.path.isdir(os.path.join(ROOT_DIR, d)):
                valid_dirs.append(d)
    
    # Custom sort: NQ1, NQ2, ..., NQ100
    valid_dirs.sort(key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0)
    return valid_dirs

def audit_folders():
    dirs = get_sorted_dirs()
    
    missing_py = []
    multiple_cpp = []
    
    for d in dirs:
        full_path = os.path.join(ROOT_DIR, d)
        files = os.listdir(full_path)
        
        # Check for Python files
        py_files = [f for f in files if f.endswith(".py") and f != "__init__.py"]
        if not py_files:
            missing_py.append(d)
            
        # Check for C++ files
        cpp_files = [f for f in files if f.endswith(".cpp")]
        if len(cpp_files) > 1:
            multiple_cpp.append((d, cpp_files))

    print("="*40)
    print(f"FOLDERS WITHOUT PYTHON FILES ({len(missing_py)}):")
    print("="*40)
    for d in missing_py:
        print(d)
    
    print("\n" + "="*40)
    print(f"FOLDERS WITH MULTIPLE CPP FILES ({len(multiple_cpp)}):")
    print("="*40)
    for d, files in multiple_cpp:
        print(f"{d}: {', '.join(files)}")

if __name__ == "__main__":
    audit_folders()
