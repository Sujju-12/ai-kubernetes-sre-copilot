from dataclasses import dataclass, field
from typing import List


@dataclass
class Incident:

    incident_type: str

    severity: str

    confidence: float

    summary: str

    affected_namespace: str = ""

    affected_pod: str = ""

    affected_deployment: str = ""

    node: str = ""

    desired_replicas: int = 0

    ready_replicas: int = 0

    available_replicas: int = 0

    events: List[str] = field(default_factory=list)

    recommendations: List[str] = field(default_factory=list)

    logs: str = ""
