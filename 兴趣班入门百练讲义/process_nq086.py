#!/usr/bin/env python3
"""
Process NQ086 problem using textbook-code-optimizer skill
"""

import os
import sys

# Add the skills directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '.trae', 'skills', 'textbook-code-optimizer', 'scripts'))

from optimize_code import TextbookCodeOptimizer

def main():
    """
    Process NQ086 problem
    """
    optimizer = TextbookCodeOptimizer()
    
    # Paths to the files
    cpp_file = os.path.join('NQ100', 'NQ086', 'NQ086_improved.cpp')
    problem_name = 'NQ086'
    problem_number = 86
    
    # Generate 思路文档
    print(f"Generating 思路文档 for {problem_name}...")
    思路_file = optimizer.generate_思路(cpp_file, problem_name)
    print(f"Generated 思路文档: {思路_file}")
    
    # Generate DOCX document
    print(f"Generating DOCX document for {problem_name}...")
    success = optimizer.generate_docx(problem_number)
    if success:
        print(f"Generated DOCX document for {problem_name}")
    else:
        print(f"Failed to generate DOCX document for {problem_name}")

if __name__ == "__main__":
    main()