# 🧠 AI Engineering Journey

> 🎯 Goal: A training log guided and empowered by AI tools — helping me become an engineer who **uses**, **understands**, and **commands** AI, not one replaced by it.

- ⏰ Timeline: July 30, 2025 – October 30, 2025  
- 📌 Daily commits pushed to GitHub — this repo records weekly summaries and key projects

---

## 🛣️ Roadmap Overview

| Phase                      | Duration         | Objective |
|---------------------------|------------------|-----------|
| Phase 1: Python Backend   | Weeks 1 - 3      | Master Python, FastAPI, and project architecture. Build a basic RESTful API project. |
| Phase 2: LLM Engineering  | Weeks 4 - 6      | Learn OpenAI, LangChain, prompt engineering. Build services that interact with LLMs. |
| Phase 3: Fullstack AI     | Weeks 7 - 9      | Combine frontend, backend, and AI to build RAG/chatbot/AI tool applications. |

---

## 📅 Weekly Learning Plan

### 📖 Week 1: Python Fundamentals + Intro to FastAPI
- 🎯 Goal: Review Python syntax, type hints, FastAPI routing, and request/response models

| Date  | Task Description                            | Category  | Status | Link |
|-------|---------------------------------------------|-----------|--------|------|
| 7/30  | Python review: functions, classes, typing   | Python    | ✅      | [Python](./PythonBasic/README.md) |
| 7/31  | Install FastAPI & create first GET endpoint | FastAPI   | ⏳      | [FastAPI](./FastAPI/README.md) |
| 8/01  | FastAPI path/query/body params              | FastAPI   | ⏳      |       |
| 8/02  | Modular routing structure for APIs          | FastAPI   | ⏳      |       |
| 8/03  | Pydantic models and response validation     | FastAPI   | ⏳      |       |
| 8/04  | Project Day: mini task manager (CRUD)       | Project   | ⏳      |       |
| 8/05  | Summary + README cleanup + unit tests       | Review    | ⏳      |       |

---

### 🧱 Week 2: Project Structure, Deployment, Security

- 🎯 Goal: Understand backend architecture, integrate a database, and implement JWT authentication

| Date  | Task Description                                 | Category | Status | Link |
|-------|--------------------------------------------------|----------|--------|------|
| 8/06  | SQLModel / SQLAlchemy intro                      | FastAPI  | ⏳      |      |
| 8/07  | SQLite integration with persistence layer        | Project  | ⏳      |      |
| 8/08  | User registration + login (hashed passwords)     | Auth     | ⏳      |      |
| 8/09  | JWT middleware + route protection                | Auth     | ⏳      |      |
| 8/10  | API testing with Postman / curl                  | Project  | ⏳      |      |
| 8/11  | Deploy FastAPI with gunicorn + render/vercel     | DevOps   | ⏳      |      |
| 8/12  | Week 2 Recap + write project docs                | Review   | ⏳      |      |

---

## 🧠 Projects

| Project Name         | Description                                      | Status     | Path |
|----------------------|--------------------------------------------------|------------|------|
| `task-manager-api`   | Task manager built with FastAPI (CRUD)           | 🛠️ Building | [`02-projects-backend/task-manager/`](./02-projects-backend/task-manager/) |
| `chatbot-ui-api`     | ChatGPT-style AI chatbot (frontend + backend)    | Planned    | -    |
| `rag-doc-qa`         | Document Q&A system (PDF + RAG + LLM)            | Planned    | -    |

---

## 📝 Notes (Continuously Updated)

| Topic                    | Summary                                  | Link |
|--------------------------|------------------------------------------|------|
| FastAPI vs Flask         | Use cases and differences                 | [Notes](./notes/fastapi-vs-flask.md) |
| LLM Engineering Tools    | LangChain, Haystack, and comparisons      | [Notes](./notes/llm-tools-review.md) |
| Backend Architecture     | Structure, dependency management          | [Notes](./notes/backend-architecture.md) |

---

## 📦 Commit Workflow

- ✅ Daily commit using branch naming format `daily/YYYY-MM-DD`
- ✅ Commit message examples:
  - `feat: add FastAPI route for GET /users`
  - `refactor: improve API validation with Pydantic`
  - `docs: update README with roadmap`
- ✅ Tag weekly milestones (e.g. `v1-week-1`)

---

## 🧑‍💻 Looking Ahead

- 📈 Weeks 4–6: Integrate OpenAI API, explore prompt design and LLM-based tasks
- 🧩 Weeks 7–9: Build fullstack AI MVPs integrating backend, LLM, and UI
- 💼 Final deliverables: portfolio-ready projects for resumes and interviews

---

```bash
ai-engineering-journey/
│
├── README.md                  ← Overview + progress tracker
│
├── 00-python-basics/          ← Python fundamentals + typing + tools
│   └── notes/
│   └── exercises/
│
├── 01-fastapi-backend/        ← FastAPI projects (core backend track)
│   ├── day01-hello-fastapi/
│   ├── day02-crud-api/
│   └── ...
│
├── 02-projects-backend/       ← Full backend apps (ORM, JWT, deploy)
│   ├── blog-api/
│   └── task-manager/
│
├── 03-llm-fundamentals/       ← LLM playground (OpenAI, LangChain)
│   └── prompt-pl
