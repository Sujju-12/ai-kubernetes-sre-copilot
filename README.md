# 🤖 AI Kubernetes SRE Copilot

An AI-powered Kubernetes troubleshooting assistant that automatically collects Kubernetes cluster information, detects common pod and deployment failures using a deterministic diagnosis engine, and generates professional Root Cause Analysis (RCA) using Google's Gemini AI.

---

## Features

- Kubernetes Cluster Discovery
- Pod Diagnostics
- Deployment Diagnostics
- Node Diagnostics
- Service Discovery
- Ingress Discovery
- Event Collection
- Pod Log Collection
- Rule-Based Diagnosis Engine
- AI-powered Root Cause Analysis (Gemini)
- Markdown Report Generation
- JSON Report Generation
- REST API using FastAPI
- CLI Interface

---

## Supported Kubernetes Failures

- ImagePullBackOff
- ErrImagePull
- CrashLoopBackOff
- OOMKilled
- Pending Pods
- Deployment Degraded

More failure scenarios will be added in future releases.

---

## Technology Stack

- Python
- Kubernetes Python Client
- FastAPI
- Gemini API
- Rich
- Pydantic
- YAML



---

# Project Structure

```text
ai-agent/
│
├── api/
├── cli/
├── collector/
├── config/
├── diagnosis/
├── knowledge/
├── llm/
├── models/
├── reports/
│   └── output/
├── tests/
│
├── main.py
├── requirements.txt
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-kubernetes-sre-copilot.git

cd ai-kubernetes-sre-copilot/ai-agent
```

---

## Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini

Set the API key.

Linux / WSL

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

Windows PowerShell

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

---

## Verify Kubernetes Access

```bash
kubectl get nodes

kubectl get pods -A
```



---

# Usage

## Run the CLI

```bash
python main.py --namespace vehicle-login
```

---

## Start the REST API

```bash
uvicorn api.app:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Diagnose a Namespace

```bash
curl -X POST "http://127.0.0.1:8000/diagnose" \
-H "Content-Type: application/json" \
-d '{
  "namespace":"vehicle-login"
}'
```

---

# Sample Output

```text
Collecting Kubernetes resources...

Analyzing cluster...

Incident : IMAGE_PULL

Severity : HIGH

Confidence : 0.99

Namespace : vehicle-login

Deployment : vehicle-login

Pod : vehicle-login-xxxx

Recommendations

- Verify Docker image exists
- Verify image tag
- kubectl describe pod
- kubectl rollout restart deployment
```

---

# Generated Reports

Every execution automatically generates

```
reports/output/

IMAGE_PULL_<timestamp>.md

IMAGE_PULL_<timestamp>.json
```

---

# Supported APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /health | Health Check |
| POST | /diagnose | Diagnose Kubernetes Namespace |

---

# Future Enhancements

- Additional Kubernetes failure scenarios
- Multi-namespace diagnosis
- Multi-cluster support
- AI provider abstraction (Gemini/Ollama/OpenAI)
- Historical incident reports
- Auto-remediation suggestions

---

# License

MIT License
