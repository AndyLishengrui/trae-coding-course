#!/usr/bin/env python3

import os
import sys

# Add the absolute path to the textbook-code-optimizer scripts directory
sys.path.append(os.path.join(os.path.dirname(__file__), '.trae', 'skills', 'textbook-code-optimizer', 'scripts'))

from optimize_code import TextbookCodeOptimizer

# Create optimizer instance
optimizer = TextbookCodeOptimizer()

# Process NQ081.cpp
input_file = '兴趣班入门百练讲义/NQ100/NQ081/NQ081.cpp'
print(f"Processing {input_file} with K&R style conversion")

# Run optimization
output_file = optimizer.optimize_cpp(input_file)
print(f"Optimized file created: {output_file}")

# Generate Python equivalent
python_file = optimizer.generate_python(output_file)
print(f"Python file created: {python_file}")

# Generate 思路文档
思路_file = optimizer.generate_思路(output_file, 'NQ081')
print(f"思路文档 created: {思路_file}")

print("\nNQ081 processing completed!")
