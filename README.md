# 🤖 AI Kubernetes SRE Copilot

An AI-powered Kubernetes troubleshooting assistant that automatically collects Kubernetes cluster information, detects common Kubernetes failures using a deterministic rule engine, and generates intelligent Root Cause Analysis (RCA) with an AI provider.

---

# Features

* Kubernetes Cluster Discovery
* Pod Diagnostics
* Deployment Diagnostics
* Node Diagnostics
* Service Discovery
* Ingress Discovery
* Kubernetes Event Collection
* Pod Log Collection
* Rule-Based Diagnosis Engine
* AI-assisted Root Cause Analysis (OpenRouter / Ollama Ready)
* Markdown Report Generation
* JSON Report Generation
* REST API using FastAPI
* Command Line Interface (CLI)

---

# Supported Kubernetes Failures

* ImagePullBackOff
* ErrImagePull
* CrashLoopBackOff
* OOMKilled
* Pending Pods

More Kubernetes failure scenarios will be added in future releases.

---

# Technology Stack

* Python
* Kubernetes Python Client
* FastAPI
* OpenRouter API (LLM Integration)
* Ollama (Supported)
* Requests
* Pydantic
* PyYAML

---

# Project Structure

```text
ai-agent/
│
├── api/
├── classifier/
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

## Configure AI Provider

### Linux / WSL

```bash
export OPENROUTER_API_KEY="YOUR_API_KEY"
```

(Optional)

```bash
export OPENROUTER_MODEL="deepseek/deepseek-chat-v3.1"
```

If you prefer a local AI model, replace the OpenRouter client with an Ollama client.

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
PYTHONPATH=. uvicorn api.app:app --reload
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

# Architecture

```
User
   │
   ▼
CLI / REST API
   │
   ▼
Snapshot Builder
   │
   ├── Pods
   ├── Deployments
   ├── Services
   ├── Events
   ├── Ingress
   ├── Nodes
   └── Logs
   │
   ▼
Cluster Snapshot
   │
   ▼
Diagnosis Engine
   │
   ▼
Incident
   │
   ▼
Prompt Builder
   │
   ▼
AI Provider
(OpenRouter / Ollama)
   │
   ▼
JSON & Markdown Reports
```

---

# Sample Output

```text
Collecting Kubernetes resources...

Analyzing cluster...

Incident      : IMAGE_PULL

Severity      : HIGH

Confidence    : 0.99

Namespace     : vehicle-login

Deployment    : vehicle-login

Pod           : vehicle-login-xxxx

Recommendations

- kubectl describe pod
- kubectl get events
- Verify Docker image exists
- Verify Docker image tag
- kubectl rollout restart deployment
```

---

# Generated Reports

Every execution automatically generates:

```text
reports/output/

IMAGE_PULL_<timestamp>.md

IMAGE_PULL_<timestamp>.json
```

---

# REST APIs

| Method | Endpoint    | Description                     |
| ------ | ----------- | ------------------------------- |
| GET    | `/health`   | Health Check                    |
| POST   | `/diagnose` | Diagnose a Kubernetes Namespace |

---

# Current Workflow

1. Collect Kubernetes resources.
2. Build a cluster snapshot.
3. Analyze workloads using the rule engine.
4. Detect Kubernetes incidents.
5. Build an AI prompt.
6. Generate AI-based Root Cause Analysis.
7. Produce JSON and Markdown reports.
8. Return the results through the CLI or REST API.

---

# Future Enhancements

* Additional Kubernetes failure scenarios
* Multi-cluster support
* Historical incident tracking
* Auto-remediation suggestions
* Grafana and Prometheus integration
* Web Dashboard
* AI Provider abstraction

---

# License

MIT License
