# Skill: Automated Algorithm Problem Verification & Standardization

## Goal
To automate the process of verifying a large collection of local C++ algorithm solutions against an Online Judge system, fixing any errors (Compile, Runtime, Wrong Answer, Presentation), and standardizing the correct code into a uniform format (`std.cpp`) for use in educational materials.

## Workflow Pipeline

1.  **Source Discovery**:
    - Iterate through numbered problem directories (e.g., `NQ001` to `NQ100`).
    - Use fuzzy matching to identify the main source file (ignoring `std.cpp` or temporary files).

2.  **Code Standardization (LLM)**:
    - **Input**: Raw student/legacy C++ code.
    - **Action**: Call LLM (Gemini) to format code, add comments, and fix obvious syntax errors.
    - **Result**: Cleaned C++ candidate code.

3.  **Validation Loop (XMUOJ)**:
    - **Action**: Submit the Candidate Code to the target contest (Contest ID: 207).
    - **Mechanism**:
        - Resolve Problem ID: Map Folder Name/Index to Contest Problem ID.
        - API Call: `submit_contest_code`.
        - Polling: Check submission status until final result (Accepted, WA, PE, etc.).

4.  **Auto-Correction Strategy**:
    - **Condition**: If logic fails (e.g., Presentation Error, Wrong Answer).
    - **Action**: Call LLM with the *Error Status* and *Original Code*.
    - **Prompt**: "Your code failed with [Status]. Please fix it."
    - **Retry**: Submit the "Fixed Code".

5.  **Finalization**:
    - **Success**: Save the passing code to `std.cpp` in the problem folder.
    - **Failure**: Log for manual review.

## Key Prompts

### 1. Standardization Prompt
```text
请整理以下 C++ 代码，使其符合标准格式：
1. 添加必要的注释。
2. 保持逻辑不变，但修复明显的语法错误。
3. 确保包含必要的头文件。
4. 不要使用非标准的库。

代码内容：
{raw_code}

请以 JSON 格式返回：
{{
  "code": "完整的 C++ 代码",
  "explanation": "修改说明"
}}
```

### 2. Auto-Fix Prompt
```text
你的代码未通过测试。
错误状态: {final_status}
题目: {problem_title}
错误代码:
{current_code}

请修正代码错误（如格式错误、逻辑漏洞、PE/WA原因分析）。
请以 JSON 格式返回：
{{
  "code": "修正后的完整 C++ 代码",
  "explanation": "简要的修改说明"
}}
```

## Technical Components
- **Orchestrator**: `verify_nq100.py` (Python, ThreadPoolExecutor).
- **LLM Client**: `book_gen/llm_client.py` (Gemini API with retry logic).
- **OJ Interface**: `xmuoj-mcp` (Custom MCP server for XMUOJ interaction).
- **Concurrency**: Configurable worker threads (Recommended: 3) to balance speed vs. API Rate Limits.
