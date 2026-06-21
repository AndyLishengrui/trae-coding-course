# 剑道试炼 · 互动编程学习平台 — 架构设计文档

## 一、项目概述

### 1.1 项目背景
《剑道试炼》是一本以武侠世界为背景的编程入门教材，共15章、172道习题，涵盖从基础语法到动态规划的核心知识点。本项目旨在为该教材打造一个完整的互动编程学习平台。

### 1.2 核心目标
- 提供在线代码编辑和运行环境
- 实现自动评测和即时反馈
- 建立学习路径和进度追踪系统
- 支持教师后台管理和数据分析
- 融入武侠主题的 gamification 机制

---

## 二、系统架构

### 2.1 整体架构图

```
┌─────────────────────────────────────────────────────────────┐
│                      前端 (Frontend)                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ 互动编程  │  │ 进度追踪  │  │ 教师后台  │  │ 排行榜   │    │
│  │  页面    │  │  页面    │  │  页面    │  │  页面    │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
│         │            │            │            │              │
│         └────────────┴────────────┴────────────┘              │
│                           │                                   │
│                    Monaco Editor                              │
│                    (代码编辑器)                                │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ REST API
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      后端 (Backend)                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                 Flask Application                     │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐           │   │
│  │  │ 认证模块  │  │ 题目模块  │  │ 提交模块  │           │   │
│  │  └──────────┘  └──────────┘  └──────────┘           │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐           │   │
│  │  │ 进度模块  │  │ 评测模块  │  │ 教师模块  │           │   │
│  │  └──────────┘  └──────────┘  └──────────┘           │   │
│  └──────────────────────────────────────────────────────┘   │
│                           │                                   │
│         ┌─────────────────┼─────────────────┐                │
│         ▼                 ▼                 ▼                │
│  ┌──────────┐      ┌──────────┐      ┌──────────┐           │
│  │ SQLite   │      │ 代码沙箱  │      │ 文件存储  │           │
│  │ Database │      │ (Docker) │      │          │           │
│  └──────────┘      └──────────┘      └──────────┘           │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 技术栈选型

| 层级 | 技术选型 | 说明 |
|------|---------|------|
| **前端框架** | 原生 HTML/CSS/JS | 轻量级，无构建步骤，适合教学项目 |
| **代码编辑器** | Monaco Editor | VS Code 的编辑器组件，支持语法高亮、自动补全 |
| **后端框架** | Flask (Python) | 轻量级，易于学习和部署 |
| **数据库** | SQLite → PostgreSQL | 初期用 SQLite，可无缝迁移到 PostgreSQL |
| **ORM** | SQLAlchemy | Python 生态最成熟的 ORM |
| **认证** | JWT (Flask-JWT-Extended) | 无状态认证，适合前后端分离 |
| **代码执行** | Docker 沙箱 | 安全隔离的代码执行环境 |
| **部署** | Nginx + Gunicorn | 生产级部署方案 |

---

## 三、核心功能模块

### 3.1 在线代码编辑器

**功能特性：**
- 支持 C++ 和 Python 两种语言
- Monaco Editor 提供的 IDE 级体验
  - 语法高亮
  - 代码自动补全
  - 错误提示
  - 代码折叠
  - 多光标编辑
- 代码自动保存（LocalStorage）
- 快捷键支持（Ctrl+Enter 提交，Ctrl+S 保存）

**实现方案：**
```javascript
// Monaco Editor 初始化
monaco.editor.create(container, {
    value: defaultCode,
    language: 'cpp',
    theme: 'vs-dark',
    fontSize: 14,
    minimap: { enabled: false },
    automaticLayout: true
});
```

### 3.2 代码执行引擎

**架构设计：**
```
用户提交代码
      │
      ▼
┌─────────────┐
│  语言检测    │
└─────────────┘
      │
      ▼
┌─────────────┐
│  创建临时目录 │
└─────────────┘
      │
      ▼
┌─────────────┐     ┌─────────────┐
│  编译 (C++)  │────▶│  执行代码    │
└─────────────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  收集输出    │
                    └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  比对结果    │
                    └─────────────┘
```

**安全措施：**
- Docker 容器隔离
- 资源限制（CPU、内存、时间）
- 禁止危险系统调用
- 文件系统只读挂载

### 3.3 自动评测系统

**评测流程：**
1. 接收用户提交的代码
2. 编译代码（C++ 需要编译）
3. 对每个测试用例执行代码
4. 比较输出与预期结果
5. 返回评测结果

**评测状态：**
| 状态 | 说明 |
|------|------|
| AC (Accepted) | 答案正确 |
| WA (Wrong Answer) | 答案错误 |
| TLE (Time Limit Exceeded) | 超时 |
| RE (Runtime Error) | 运行时错误 |
| CE (Compilation Error) | 编译错误 |

### 3.4 学习路径与进度追踪

**进度数据结构：**
```json
{
    "JD001": "solved",      // 已解决
    "JD002": "attempted",   // 已尝试
    "JD003": "unsolved"     // 未开始
}
```

**统计指标：**
- 完成题目数
- 各章节完成率
- 连续刷题天数
- 总积分

### 3.5 提示系统

**分级提示机制：**
```
用户请求提示
      │
      ▼
┌─────────────┐
│ 检查剑气值   │
└─────────────┘
      │
      ▼ (剑气 >= 5)
┌─────────────┐
│ 扣除剑气     │
└─────────────┘
      │
      ▼
┌─────────────┐
│ 返回提示     │
└─────────────┘
```

**提示层级：**
1. **第一层**：解题方向提示
2. **第二层**：算法思路提示
3. **第三层**：关键代码提示

### 3.6 代码对比功能

**功能说明：**
- 用户代码与参考代码并排显示
- 代码行数对比
- 帮助学生理解最优解法

### 3.7 Gamification 机制

**武侠主题元素：**
| 元素 | 说明 |
|------|------|
| 剑气值 | 查看提示、解锁功能的虚拟货币 |
| 成就徽章 | 完成特定目标获得 |
| 连续天数 | 保持刷题习惯 |
| 排行榜 | 班级内排名 |

**成就列表：**
- 🗡️ 初次拔剑：完成第一道题
- ⚔️ 小有成就：完成10道题
- 🏆 叩门成功：完成第一章全部题目
- 🔥 剑道入门：完成50道题
- 💎 百炼成钢：完成100道题
- 👑 华山论剑：完成全部172道题
- 🔥 七日连战：连续7天刷题
- 🧠 独立思考：连续10题不使用提示

---

## 四、教师后台功能

### 4.1 数据概览

**统计指标：**
- 学生总数
- 题目总数
- 总提交次数
- 平均完成率
- 各章节完成率图表
- 题目难度分布

### 4.2 学生管理

**功能列表：**
- 学生列表（姓名、完成题数、完成率、提交次数、剑气值）
- 搜索和排序
- 查看学生详情（题目完成情况热力图）
- 导出学生数据

### 4.3 题目分析

**分析维度：**
- 各题目尝试人数
- 各题目通过人数
- 通过率统计
- 按章节筛选
- 按难度筛选

### 4.4 提交记录

**记录内容：**
- 学生姓名
- 题目编号
- 编程语言
- 评测状态
- 得分
- 提交时间
- 查看代码

### 4.5 自动评分

**评分规则配置：**
- 通过题目得分（默认 10 分/题）
- 使用提示扣分（默认 2 分/次）
- 代码风格评分（可选）
- 最大提交次数限制（可选）

**批量操作：**
- 计算最终成绩
- 导出成绩单

### 4.6 数据导出

**导出类型：**
- 学生数据 CSV
- 提交记录 CSV
- 题目统计 CSV
- 成绩单 CSV

---

## 五、数据库设计

### 5.1 ER 图

```
┌──────────┐       ┌──────────┐       ┌──────────┐
│   User   │──────▶│ Progress │◀──────│ Problem  │
└──────────┘       └──────────┘       └──────────┘
      │                                     │
      │                                     │
      ▼                                     ▼
┌──────────┐                         ┌──────────┐
│Submission│                         │ TestCase │
└──────────┘                         └──────────┘
      │
      ▼
┌──────────┐
│HintUsage │
└──────────┘
```

### 5.2 核心表结构

**User 表：**
```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(120) NOT NULL,
    role VARCHAR(20) DEFAULT 'student',
    sword_energy INTEGER DEFAULT 100,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Problem 表：**
```sql
CREATE TABLE problem (
    id INTEGER PRIMARY KEY,
    jd_id VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    chapter INTEGER NOT NULL,
    story TEXT,
    input_format TEXT,
    output_format TEXT,
    sample_input TEXT,
    sample_output TEXT,
    tags JSON,
    hints JSON,
    cpp_code TEXT,
    python_code TEXT,
    difficulty INTEGER DEFAULT 1,
    acwing_id INTEGER
);
```

**Submission 表：**
```sql
CREATE TABLE submission (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES user(id),
    problem_id INTEGER REFERENCES problem(id),
    language VARCHAR(20) NOT NULL,
    code TEXT NOT NULL,
    status VARCHAR(20),
    score INTEGER DEFAULT 0,
    total_score INTEGER DEFAULT 0,
    execution_time FLOAT,
    test_results JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 六、API 设计

### 6.1 认证 API

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/auth/register` | 用户注册 |
| POST | `/api/auth/login` | 用户登录 |
| GET | `/api/auth/me` | 获取当前用户信息 |

### 6.2 题目 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/problems` | 获取所有题目 |
| GET | `/api/problems/:id` | 获取单个题目详情 |

### 6.3 代码执行 API

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/run` | 运行代码（自定义输入） |
| POST | `/api/submit` | 提交代码评测 |

### 6.4 进度 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/progress` | 获取用户进度 |
| GET | `/api/submissions` | 获取提交记录 |

### 6.5 提示 API

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/hints/:id/:level` | 使用提示 |

### 6.6 排行榜 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/leaderboard` | 获取排行榜 |

### 6.7 教师 API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/teacher/students` | 获取学生列表 |
| GET | `/api/teacher/submissions` | 获取所有提交 |
| GET | `/api/teacher/stats` | 获取班级统计 |

---

## 七、前端页面结构

### 7.1 页面列表

| 页面 | 文件名 | 功能 |
|------|--------|------|
| 互动编程 | `index.html` | 主要编程页面，包含题目、编辑器、运行结果 |
| 我的进度 | `progress.html` | 学习进度、成就、活跃度 |
| 教师后台 | `teacher.html` | 教师管理界面 |
| 排行榜 | `leaderboard.html` | 班级排名 |

### 7.2 页面布局

**互动编程页面：**
```
┌─────────────────────────────────────────────────────────────┐
│                        导航栏                                │
├──────────┬──────────────────────────────────┬───────────────┤
│          │                                  │               │
│  题目列表 │         题目详情 + 代码编辑器      │   提交记录    │
│          │                                  │   讨论区      │
│          │                                  │               │
└──────────┴──────────────────────────────────┴───────────────┘
```

---

## 八、部署方案

### 8.1 开发环境

```bash
# 启动后端
cd textbook/website/interactive/backend
pip install -r requirements.txt
python app.py

# 启动前端（简单 HTTP 服务器）
cd textbook/website/interactive
python -m http.server 8080
```

### 8.2 生产环境

**Docker Compose 部署：**
```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "80:80"
    depends_on:
      - api

  api:
    build: ./backend
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    environment:
      - DATABASE_URL=sqlite:///data/jd_platform.db

  judge:
    image: judge0/judge0:latest
    ports:
      - "2358:2358"
```

### 8.3 Nginx 配置

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        root /path/to/textbook/website/interactive;
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 九、实现路线图

### 第一阶段：核心功能（2周）

**Week 1：**
- [x] 搭建前端页面框架
- [x] 集成 Monaco Editor
- [x] 实现题目展示功能
- [x] 实现本地代码保存

**Week 2：**
- [x] 搭建 Flask 后端
- [x] 实现用户认证
- [x] 实现代码执行引擎
- [x] 实现自动评测

### 第二阶段：学习功能（2周）

**Week 3：**
- [x] 实现进度追踪系统
- [x] 实现提示系统
- [x] 实现代码对比功能
- [x] 实现 gamification 机制

**Week 4：**
- [ ] 完善排行榜功能
- [ ] 实现讨论区
- [ ] 优化 UI/UX
- [ ] 移动端适配

### 第三阶段：教师功能（2周）

**Week 5：**
- [x] 实现教师后台框架
- [x] 实现数据概览
- [x] 实现学生管理
- [x] 实现题目分析

**Week 6：**
- [x] 实现提交记录查看
- [x] 实现自动评分配置
- [x] 实现数据导出
- [ ] 测试和优化

### 第四阶段：部署上线（1周）

**Week 7：**
- [ ] Docker 容器化
- [ ] 部署到服务器
- [ ] 域名和 SSL 配置
- [ ] 性能优化
- [ ] 文档编写

---

## 十、扩展功能（未来）

### 10.1 AI 辅助
- AI 代码审查
- 智能提示生成
- 个性化学习路径推荐

### 10.2 社交功能
- 学习小组
- 代码分享
- 讨论区增强

### 10.3 内容增强
- 视频讲解
- 动态演示
- 交互式教程

### 10.4 数据分析
- 学习行为分析
- 知识点掌握度分析
- 学习效果预测

---

## 十一、文件结构

```
textbook/website/interactive/
├── index.html              # 互动编程主页面
├── progress.html           # 学习进度页面
├── teacher.html            # 教师后台页面
├── leaderboard.html        # 排行榜页面
├── style.css               # 主样式文件
├── app.js                  # 前端主逻辑
├── ARCHITECTURE.md         # 架构设计文档（本文件）
├── backend/
│   ├── app.py              # Flask 后端应用
│   ├── requirements.txt    # Python 依赖
│   └── Dockerfile          # 后端容器配置
└── assets/
    └── ...
```

---

## 十二、总结

本平台以《剑道试炼》教材为基础，打造了一个完整的互动编程学习体验。通过在线代码编辑器、自动评测系统、进度追踪和教师后台等核心功能，帮助学生高效学习编程，同时为教师提供强大的教学管理工具。

武侠主题的 gamification 设计增加了学习的趣味性，让学生在"修炼剑道"的过程中掌握编程技能。
