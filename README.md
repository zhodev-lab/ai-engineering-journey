# 🧠 AI Engineering Journey

> 目标：90 天成为具备实战能力的 AI 工程师（从 Python 后端到 LLM 应用）

- ⏰ 学习周期：2025-07-30 ~ 2025-10-30
- 📌 每日任务提交到 GitHub，本仓库用于阶段总结 + 项目记录
- 🧑‍💻 当前角色：前端工程师，正在转型 AI 工程师

---

## 🛣️ 路线图概览（阶段目标）

| 阶段        | 时间范围         | 目标说明 |
|-------------|------------------|----------|
| 阶段一：Python 后端 | 第 1 - 3 周 | 掌握 Python + FastAPI + 项目结构，完成基本 RESTful API 项目 |
| 阶段二：LLM 工程基础 | 第 4 - 6 周 | 熟悉 OpenAI / LangChain / Prompt 工程，构建可调用 LLM 的服务 |
| 阶段三：全栈 AI 项目实战 | 第 7 - 9 周 | 将前端、后端、AI 整合，完成 RAG / Chatbot / AI 工具类应用 |

---

## 📅 每周任务计划

### 📖 Week 1：Python 基础 + FastAPI 初识
- 🎯 目标：掌握 Python 基础语法、类型提示、FastAPI 路由机制、请求响应模型

| 日期 | 任务内容 | 分类 | 状态 | 提交链接 |
|------|----------|------|------|----------|
| 7/30 | Python 基本语法（函数、类、类型提示）复习 | Python | ✅ | [link]() |
| 7/31 | 安装 FastAPI + 第一个 GET 接口 | FastAPI | ✅ | [link]() |
| 8/01 | FastAPI Path + Query + Body 参数解析 | FastAPI | ⏳ | |
| 8/02 | 构建带路由分离的 API 结构 | FastAPI | ⏳ | |
| 8/03 | Pydantic 模型基础、响应模型校验 | FastAPI | ⏳ | |
| 8/04 | 项目 Day：构建 mini-task manager 项目（增删改查） | 项目 | ⏳ | |
| 8/05 | 学习总结 + 完善 README + 单元测试编写 | 整理 | ⏳ | |

---

### 🧱 Week 2：项目结构 + 部署 + 安全机制
- 🎯 目标：掌握项目分层结构、数据库集成（SQLite / PostgreSQL）、JWT 登录流程

| 日期 | 任务内容 | 分类 | 状态 | 提交链接 |
|------|----------|------|------|----------|
| 8/06 | 数据库基础 + SQLModel/SQLAlchemy 初识 | FastAPI | ⏳ | |
| 8/07 | 集成 SQLite + 增加数据持久化 | 项目 | ⏳ | |
| 8/08 | 用户注册 + 登录（密码哈希） | 安全 | ⏳ | |
| 8/09 | JWT 认证中间件 + 用户鉴权接口 | 安全 | ⏳ | |
| 8/10 | 前后端联调测试（可用 postman / curl） | 项目 | ⏳ | |
| 8/11 | 使用 uvicorn + gunicorn 部署 FastAPI 到 render/vercel | DevOps | ⏳ | |
| 8/12 | Week 2 总结 + 项目文档书写 | 整理 | ⏳ | |

---

## 🧠 项目列表

| 项目名 | 简介 | 状态 | 路径 |
|--------|------|------|------|
| `task-manager-api` | 使用 FastAPI 构建的任务管理系统 | 🛠️ 开发中 | [`02-projects-backend/task-manager/`](./02-projects-backend/task-manager/) |
| `chatbot-ui-api` | ChatGPT 风格 AI 聊天项目（前后端分离） | 待开发 | - |
| `rag-doc-qa` | 文档问答系统（PDF/RAG/LLM） | 待开发 | - |

---

## 📝 笔记（持续更新）

| 标题 | 内容概览 | 链接 |
|------|----------|------|
| FastAPI vs Flask | 各自适用场景和优劣对比 | [笔记](./notes/fastapi-vs-flask.md) |
| LLM 工程常见工具对比 | LangChain vs Haystack 等 | [笔记](./notes/llm-tools-review.md) |
| 后端项目结构设计 | 常用目录结构、依赖管理等 | [笔记](./notes/backend-architecture.md) |

---

## 📦 提交规范

- ✅ 每日提交 1 次，使用 Git 分支命名 `daily/YYYY-MM-DD`
- ✅ Commit Message 示例：
  - `feat: 完成 FastAPI 路由练习`
  - `refactor: 优化 API 参数验证逻辑`
  - `docs: 补充 README 结构规划说明`
- ✅ 建议每周一个 tag（如：`v1-week-1`）

---

## 🧑‍💻 面向未来

- 📈 第 4 - 6 周开始结合 LLM API，训练 Prompt、做文本增强任务
- 🧩 第 7 - 9 周将结合前端能力构建完整 AI 产品 MVP
- 💼 最终目标是拿出可展示项目用于面试 or 简历强化

---

## 🫶 欢迎你加入

本仓库为个人成长记录用，如果你也在学习 Python + AI 工程，欢迎 fork 或交流 🙌
