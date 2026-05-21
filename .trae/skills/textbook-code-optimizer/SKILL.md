---
name: textbook-code-optimizer
description: "Use this skill whenever the user wants to optimize C++ and Python code for textbook insertion. It helps create compact, well-commented code suitable for educational materials, with consistent algorithmic approaches across both languages, and can generate DOCX documents for the code."
license: Proprietary. LICENSE.txt has complete terms
---

# Textbook Code Optimizer

## Overview

This skill optimizes C++ and Python code for insertion into textbooks, ensuring compactness, clarity, and educational value. It also generates DOCX documents for the optimized code.

## Quick Reference

| Task | Approach |
|------|----------|
| Optimize C++ code | Read input file, apply textbook-friendly optimizations, save as improved version |
| Create Python equivalent | Read optimized C++ code, generate corresponding Python code with consistent algorithm |
| Generate思路文档 | Create detailed algorithm explanation document for the problem |
| Generate DOCX document | Create a DOCX document containing the optimized code and explanation |

## Features

- **Code Compression**: Removes unnecessary whitespace, simplifies structure, and uses concise variable names
- **Textbook Insertion Optimization**: Specifically designed to remove多余的换行, ensure no连续的空行, and create compact code suitable for textbook pages
- **Educational Comments**: Adds key comments at critical algorithmic points
- **Cross-Language Consistency**: Ensures Python code follows the same algorithmic approach as C++ code
- **思路文档生成**: Creates comprehensive algorithm explanation documents
- **DOCX Document Generation**: Generates formatted DOCX documents for the code
- **Problem Type Recognition**: Automatically identifies common algorithmic problems and generates appropriate documentation

## Supported Problem Types

1. **01背包问题**
2. **数字三角形问题**
3. **最长公共子序列问题**
4. **瓷砖铺放问题**
5. **求约数问题**

## Usage

1. **For C++ code optimization**: Provide the path to the original C++ file
2. **For Python code generation**: The skill will automatically create a Python equivalent
3. **For思路文档**: The skill will generate a markdown document explaining the algorithm
4. **For DOCX document**: The skill will generate a DOCX document containing the optimized code

## Optimization Guidelines

- **Variable Names**: Use short but meaningful variable names to prevent line breaks in textbook formatting
- **Code Structure**: Minimize nested blocks, use compact loops, and ensure code fits well on textbook pages
- **Comments**: Add only essential comments at algorithmic key points, avoiding excessive documentation
- **Whitespace**: Remove unnecessary empty lines and spaces, specifically:
  - Remove多余的换行 (excessive line breaks)
  - Ensure no连续的空行 (no consecutive blank lines)
  - Create compact code suitable for textbook insertion
- **Algorithm Consistency**: Ensure Python code follows the same logic as C++ code
- **Textbook Formatting**: Optimize code layout to minimize page breaks and maximize readability in printed materials

## Key Changes

### Version 1.3
- Enhanced code compression with specific textbook insertion optimization
- Added detailed logic to remove多余的换行 and ensure no连续的空行
- Updated SKILL.md with specific textbook insertion requirements
- Improved code layout optimization for better textbook formatting

### Version 1.2
- Added support for **求约数问题** recognition and documentation
- Updated SKILL.md to include new problem type

### Version 1.1
- Added support for **瓷砖铺放问题** recognition and documentation
- Improved 思路文档 generation with **思考过程** and **程序设计要点** sections
- Optimized code generation for better textbook insertion
- Simplified思路文档 structure for more concise and focused content

### Version 1.0
- Initial release with support for 01背包, 数字三角形, and 最长公共子序列 problems
- Basic code optimization and DOCX document generation

## Dependencies

- Python 3.x
- pygments (for code syntax highlighting)
- No external libraries required for basic functionality