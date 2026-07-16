import json


class PromptBuilder:

    def build(self, incident):

        payload = {
            "incident_type": incident.incident_type,
            "severity": incident.severity,
            "confidence": incident.confidence,
            "summary": incident.summary,
            "namespace": incident.affected_namespace,
            "deployment": incident.affected_deployment,
            "pod": incident.affected_pod,
            "node": incident.node,
            "desired_replicas": incident.desired_replicas,
            "ready_replicas": incident.ready_replicas,
            "available_replicas": incident.available_replicas,
            "events": incident.events,
            "logs": incident.logs[:4000] if incident.logs else "",
            "recommendations": incident.recommendations,
        }

        return f"""
You are an expert Kubernetes Site Reliability Engineer (SRE).

A Kubernetes Diagnosis Engine has ALREADY analyzed the cluster and identified the incident.

IMPORTANT:
- Do NOT re-classify the incident.
- Assume the diagnosis engine is correct.
- Your responsibility is to explain the issue professionally.

Below is the structured evidence collected from Kubernetes.

{json.dumps(payload, indent=4)}

Return your answer in Markdown using EXACTLY this structure.

# Executive Summary

Provide a 3-5 sentence overview.

# Root Cause

Explain the exact reason.

# Technical Evidence

Use the supplied events, deployment status and logs.

# Business Impact

Explain what this failure means for users and the application.

# Verification Commands

Provide kubectl commands to verify the diagnosis.

# Resolution Steps

Provide step-by-step remediation.

# Prevention

Explain how to prevent this issue in production.

# Best Practices

Provide Kubernetes production recommendations.

Do not invent information.

Base everything on the supplied Kubernetes evidence.
"""
