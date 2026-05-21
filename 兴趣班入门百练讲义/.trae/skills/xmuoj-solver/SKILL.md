---
name: "xmuoj-solver"
description: "Solves and submits XMUOJ problems. Invoke when user provides XMUOJ problem ID or name and asks to solve it."
---

# XMUOJ Problem Solver

This skill helps you solve and submit problems from XMUOJ (https://www.xmuoj.com) automatically.

## How It Works

1. **Login to XMUOJ** using your credentials
2. **Retrieve problem details** including description, input/output requirements, and sample cases
3. **Generate solution code** based on the problem requirements
4. **Test the code** to ensure correctness
5. **Submit the code** to XMUOJ and return the verdict

## Usage

### Required Information
- XMUOJ username and password (stored securely)
- Problem ID or URL (e.g., "GW003" or "https://www.xmuoj.com/problem/GW003")

### Example Workflow

1. "Solve XMUOJ problem GW003 using C++"
2. "Submit this code to XMUOJ problem 1001"
3. "What's the solution for XMUOJ problem 2002 in Python?"

## Supported Languages
- C
- C++
- Java
- Python3
- Python2

## Technical Details

The skill uses the XMUOJ MCP (Module Communication Protocol) server to:
- Authenticate with XMUOJ's API
- Fetch problem information
- Submit code for evaluation
- Retrieve and parse evaluation results

## Error Handling

The skill will handle common errors such as:
- Login failures
- Problem not found
- Compilation errors
- Runtime errors
- Time limit exceeded

It will provide clear feedback and suggestions for fixing issues when they occur.
