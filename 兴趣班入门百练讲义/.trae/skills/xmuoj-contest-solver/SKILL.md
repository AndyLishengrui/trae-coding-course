---
name: "xmuoj-contest-solver"
description: "Batch solves all problems in an XMUOJ contest until all AC. Invoke when user provides a contest URL and asks to solve all problems sequentially."
---

# XMUOJ Contest Batch Solver

This skill helps you automatically solve all problems in an XMUOJ contest sequentially until all problems are accepted (AC).

## How It Works

1. **Login to XMUOJ** using your credentials
2. **Retrieve contest problems list** from the provided contest URL
3. **Process problems sequentially**:
   - Fetch problem details for each problem
   - Generate C++ solution code
   - Submit code and wait for verdict
   - If not AC, analyze error and retry
4. **Track progress** and provide status updates
5. **Generate summary** of all solved problems

## Usage

### Required Information
- XMUOJ username and password
- Contest URL (e.g., "https://www.xmuoj.com/contest/207/problems")
- Preferred programming language (default: C++)

### Example Workflow

1. "Solve all problems in XMUOJ contest 207 using C++"
2. "Process the ACM & 蓝桥杯入门百练(2025) contest"
3. "Batch solve all problems in https://www.xmuoj.com/contest/207/problems"

## Technical Details

### Steps

1. **Extract Contest ID** from the URL
2. **Fetch Problems List** from the contest API
3. **For Each Problem**:
   - Get problem details (description, input/output, samples)
   - Generate C++ solution code
   - Submit code to XMUOJ
   - Parse evaluation result
   - If AC: move to next problem
   - If error: analyze and retry with improved solution
4. **Generate Progress Report** after each problem
5. **Provide Final Summary** when all problems are processed

### Supported Languages
- C++ (default)
- C
- Java
- Python3

### Error Handling

The skill handles various error scenarios:
- Login failures
- Network errors
- Compilation errors
- Runtime errors
- Time limit exceeded
- Wrong answer
- Memory limit exceeded

### Progress Tracking

The skill maintains detailed progress information:
- Total problems in contest
- Number of problems solved
- Number of problems with AC
- Current problem being processed
- Success rate
- Estimated time remaining

## Output Format

### Progress Updates

```
[Progress] Processing problem 1/10: "A+B"
[Status] Submitted code...
[Verdict] AC! Time: 1ms, Memory: 3MB
[Progress] 1 problem solved (10%)
```

### Final Summary

```
=== Contest Solving Summary ===
Contest: ACM & 蓝桥杯入门百练(2025)
Total Problems: 10
AC Problems: 10
Success Rate: 100%
Total Time: 5 minutes

Problems Solved:
1. A+B (AC)
2. 求连续偶数和 (AC)
3. 小管理 (AC)
...
```

## Configuration

### Optional Parameters

- `language`: Programming language to use (default: "C++")
- `max_retries`: Maximum retry attempts per problem (default: 3)
- `timeout`: Timeout for each problem submission (default: 30 seconds)
- `verbose`: Enable detailed output (default: true)

## Examples

### Basic Usage

"Solve all problems in https://www.xmuoj.com/contest/207/problems using C++"

### Custom Configuration

"Solve all problems in contest 207 with max_retries=5 and timeout=60"

## Notes

- The skill requires valid XMUOJ credentials
- Internet connection is required throughout the process
- The skill may take significant time for large contests
- Progress is saved periodically to handle interruptions
- Detailed logs are generated for debugging purposes
