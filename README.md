# prezBOT 🤖⚡

**An intelligent, multi-interface technical support agent powered by Python, FastAPI, and direct LLM API integration.**

---

## 📌 Project Overview & Evolution

**prezBOT** was created as an initial development to establish a convenient, automated support system for developer workflows and technical communities. 

While the early prototype validated the core logic and response pipelines, the architecture has now been significantly upgraded for **enhanced availability, lower latency, and production readiness**. By refactoring away from low-code orchestration and transitioning to a pure, containerized Python microservice using **FastAPI** and direct **Claude/Gemini API SDKs**, prezBOT delivers high throughput, robust asynchronous request handling, and flexible deployment capabilities.

---

## 🏗 Architecture & Tech Stack

* **Core Framework:** Python 3.11 & [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous, high-performance web framework)
* **AI Orchestration:** Direct Anthropic (`anthropic` SDK) & Google Gemini API integrations
* **Bot Interface:** `discord.py` (Async event loop integration)
* **Containerization:** Docker & Docker Compose
* **HTTP Client:** `aiohttp` for non-blocking asynchronous requests

┌─────────────────┐       ┌────────────────────────┐       ┌───────────────────┐
│                 │       │        prezBOT         │       │                   │
│  Discord Client ├──────►│   FastAPI Microservice ├──────►│  Claude / Gemini  │
│  (!ask command) │       │  (Async Engine & REST) │       │    Direct API     │
│                 │       │                        │       │                   │
└─────────────────┘       └───────────┬────────────┘       └───────────────────┘
│
┌─────────────────┐                   │
│ Web / External  ├───────────────────┘
│ REST Consumers  │
└─────────────────┘

---

## ✨ Key Features

* **Dual Interface Support:** Operates simultaneously as an active Discord Bot and as a standalone REST API with auto-generated Swagger UI (`/docs`).
* **Direct LLM SDK Integration:** Bypasses middleman automation layers to directly stream and process prompt context with Anthropic's Claude 3.5 Sonnet / Gemini models.
* **Non-Blocking Asynchronous Design:** Leverages Python's `asyncio` and `aiohttp` to ensure rapid, concurrent request processing without stalling the bot loop.
* **Container Native:** Fully containerized with Docker, enabling lightweight deployment across any cloud or Linux environment.
* **High Availability & Lifespan Management:** Uses FastAPI's `lifespan` manager to handle graceful startup/shutdown of background bot processes.

---

## 🚀 Quick Start (Docker Deployment)

### 1. Prerequisites
* [Docker Desktop](https://www.docker.com/) installed
* Discord Bot Token (from Discord Developer Portal)
* Anthropic / Gemini API Key

### 2. Environment Configuration
Clone the repository and create a `.env` file from the provided template:

```bash
git clone [https://github.com/your-username/prezBOT.git](https://github.com/your-username/prezBOT.git)
cd prezBOT
cp .env.example .env
