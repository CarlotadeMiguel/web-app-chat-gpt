# Web-App Chat-GPT

An open-source full-stack chat application that pairs a Flask REST API with a React front-end and delivers ChatGPT-style conversations.  The **Docker** branch contains a ready-to-run, containerised version of the stack.

---
## ✨ Features

| Layer | Stack | Highlights |
|-------|-------|------------|
| Front-end | React 18 + Vite | Modern hooks, Context API auth, protected routes, Axios API module, polished UI |
| Back-end | Flask 2 | JWT authentication, CORS, Marshmallow validation, Redis cache, OpenAI proxy endpoints |
| DevOps | Docker + docker-compose | Multi-stage builds, separate images for API & UI, optional Redis service |

---
## 🗂 Project Structure

```text
web-app-chat-gpt/
├─ backend/            # Flask source code
│  ├─ app/
│  ├─ requirements.txt
│  ├─ run.py
│  └─ .env.example
├─ frontend/           # React source code (Vite build)
│  ├─ src/
│  ├─ public/
│  ├─ package.json
│  └─ vite.config.js
├─ docker-compose.yml  # Orchestrates the stack
└─ README.md           # ← you are here
```

---
## 🚀 Quick Start (Docker)

> **Prerequisites** : Docker 20.10+ and Docker Compose v2.

```bash
git clone https://github.com/CarlotadeMiguel/web-app-chat-gpt.git
cd web-app-chat-gpt # checkout Docker branch if necessary
docker compose build
# first time: copy env vars then edit secrets
cp backend/.env.example backend/.env
vim backend/.env
# lift the stack
docker compose up -d
```

Open the URLs:

* Front-end → <http://localhost:3000>
* Back-end  → <http://localhost:5000>

Stop everything:

```bash
docker compose down
```

---
## 🧑‍💻 Local Development (without Docker)

```bash
# backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
flask run

# frontend (other terminal)
cd ../frontend
npm install
npm run dev    # served on http://localhost:5173 by default
```

Adjust `REACT_APP_API_URL` in `frontend/.env` if you change API port.

---
## 🔧 Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_APP` | `run.py` | Entry point for Flask |
| `SECRET_KEY` | `change-me` | JWT & session secret |
| `OPENAI_API_KEY` | ― | OpenAI access key |
| `REDIS_URL` | `redis://redis:6379/0` | Cache / rate-limit store |

Create **backend/.env** from the shipped example and set real secrets **before running in production**.

---
## 🐳 Docker Details

### Backend (`backend/Dockerfile`)
* Based on `python:3.11-slim`.
* Installs Python deps, copies code, exposes port 5000.

### Front-end (`frontend/Dockerfile`)
* Multi-stage build: `node:18-alpine` → build, `nginx:stable-alpine` → serve.
* Final image serves the static React build on port 80.

### Orchestrator (`docker-compose.yml`)
* Defines **backend**, **frontend**, and optional **redis** service.
* Uses a custom bridge network `webapp-network` to let containers talk by service name.

---
## ✅ Smoke Tests

1. **Register & login**:

```bash
curl -X POST http://localhost:5000/auth/register \
     -H "Content-Type: application/json" \
     -d '{"email":"user@test.com","password":"password123"}'
```

2. **Open UI** at <http://localhost:3000>, create account, chat away.

---
## 🛠 Troubleshooting

| Symptom | Possible cause | Fix |
|---------|----------------|------|
| `Network Error` on UI | CORS not enabled, wrong API URL | Check `backend/.env`, `frontend/.env`, CORS config |
| 422 on `/chat/history` | Missing or invalid JWT | Ensure token saved to localStorage, sent in `Authorization: Bearer` header |
| Container exits on start | Bad env vars / missing secret | Review logs: `docker compose logs backend` |

---
## 📄 License

MIT © 2025 Carlota de Miguel

---
## 🙌 Contributing

1. Fork the repo & create a feature branch.
2. Follow the coding style (Black for Python, Prettier for JS).
3. Submit a PR describing your changes.
