from dataclasses import dataclass, field
from typing import List


@dataclass
class DiagnosisReport:
    """
    Final report returned by the AI engine.
    """

    incident: str

    severity: str

    confidence: float

    root_cause: str

    recommendations: List[str] = field(default_factory=list)

    evidence: List[str] = field(default_factory=list)
