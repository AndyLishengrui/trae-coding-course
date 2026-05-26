"""
XMUOJ CLI 工具链 v2.0 — 题库管理与代码验证

整合了蓝桥杯集训营的实战验证流程（300+道题的导入经验）。

模块结构：
  client.py         — API 客户端（认证、CRUD、提交、导入）
  cli.py            — 命令行入口（20+子命令）
  sync_engine.py    — 同步引擎（书稿 ↔ XMUOJ 云端题库）
  problem_builder.py — Markdown → 标准16字段 problem.json 转换器
  packager.py       — ZIP 打包器（标准 1/ 根目录格式）
  importer.py       — 完整导入流程（API方式 + ZIP方式）

核心工作流：
  1. 登录:  python cli.py login <username> <password>
  2. 构建:  python problem_builder.py <题目.md>
  3. 打包:  python packager.py <problem.json> [testcase_dir]
  4. 导入:  python importer.py <题目.md> --method zip
  5. 实验:  python cli.py contest create/add-problem/reorder
  6. 验证:  python cli.py validate --chapter 1 --lang cpp

关键修正（蓝桥杯实战验证）：
  - problem.json 必须 16 字段，spj 必须 null (不能 false)
  - description 等字段必须 {format:"html", value:"..."} 对象格式
  - ZIP 包必须有 1/ 根目录
"""
