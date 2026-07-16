# AI Kubernetes SRE Copilot Architecture

```
                    Kubernetes Cluster
                           │
                           ▼
                  Kubernetes Python Client
                           │
                           ▼
                   Resource Collectors
                           │
                           ▼
                    Snapshot Builder
                           │
                           ▼
                  Diagnosis Engine (Rules)
                           │
                           ▼
                     Incident Object
                           │
                           ▼
                     Prompt Builder
                           │
                           ▼
                        Gemini API
                           │
                           ▼
                  AI Root Cause Analysis
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
      CLI Output                  FastAPI Response
            │                             │
            └──────────────┬──────────────┘
                           ▼
                Markdown / JSON Reports
```
