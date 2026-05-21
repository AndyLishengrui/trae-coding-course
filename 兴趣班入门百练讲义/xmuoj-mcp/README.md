# XMUOJ MCP Server

This is an MCP server plugin for Trae that connects to XMUOJ (www.xmuoj.com). It allows you to log in, search/read problems, and submit code directly from your AI assistant.

## Installation

1.  **Prerequisites**: Python 3.10+
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the MCP server:

```bash
python server.py
# or using mcp CLI if installed and configured as an entry point, 
# but direct pyscript execution is simplest for development.
```

### Integration with Trae

To use this with Trae (or any MCP client), you typically need to add it to your MCP configuration file (e.g., `mcp_config.json` or through the IDE settings).

Configuration example:

```json
{
  "mcpServers": {
    "xmuoj": {
      "command": "python",
      "args": ["/absolute/path/to/xmuoj-mcp/server.py"]
    }
  }
}
```

## Tools Available

*   **`xmuoj_login(username, password)`**: Logs in to XMUOJ. Required before submitting code.
*   **`xmuoj_search_problem(keyword)`**: Search for problems by name or ID.
*   **`xmuoj_get_problem(problem_id_or_url)`**: Fetch problem details (description, input/output).
*   **`xmuoj_submit_code(problem_id_or_url, code, language)`**: Submit code and wait for the verdict.

## Example Workflow

1.  "Login to XMUOJ with user `myuser` and password `mypass`."
2.  "What is problem 1001 about?"
3.  "Solve problem 1001 using Python." (The AI will generate code)
4.  "Submit this code to problem 1001."
