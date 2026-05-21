#!/usr/bin/env python3

import os
import sys

# Add the absolute path to the textbook-code-optimizer scripts directory
sys.path.append(os.path.join(os.path.dirname(__file__), '.trae', 'skills', 'textbook-code-optimizer', 'scripts'))

from optimize_code import TextbookCodeOptimizer

# Create optimizer instance
optimizer = TextbookCodeOptimizer()

# Test file
test_file = 'test_clang_format.cpp'
print(f"Testing clang-format integration with {test_file}")

# Run optimization
output_file = optimizer.optimize_cpp(test_file)
print(f"Optimized file created: {output_file}")

# Read and display the result
with open(output_file, 'r', encoding='utf-8') as f:
    optimized_code = f.read()

print("\nOptimized code (K&R style):")
print("=" * 80)
print(optimized_code)
print("=" * 80)
print("\nClang-format integration test completed!")
