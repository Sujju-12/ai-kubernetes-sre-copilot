from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Incident:

    # Rule Engine Output
    incident_type: str
    severity: str
    confidence: float
    summary: str

    # Kubernetes Resources
    affected_namespace: str = ""
    affected_pod: str = ""
    affected_deployment: str = ""
    node: str = ""

    # Deployment Health
    desired_replicas: int = 0
    ready_replicas: int = 0
    available_replicas: int = 0

    # Pod Information
    pod_status: str = ""
    container_state: str = ""
    restart_count: int = 0
    exit_code: int = 0
    restart_reason: str = ""

    # Evidence collected by Rule Engine
    evidence: List[str] = field(default_factory=list)

    # Kubernetes Events
    events: List[str] = field(default_factory=list)

    # Container Logs
    logs: str = ""

    # Suggested verification commands
    recommendations: List[str] = field(default_factory=list)

    # Kubernetes Objects involved
    related_resources: Dict[str, str] = field(default_factory=dict)
