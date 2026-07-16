from dataclasses import dataclass, field
from typing import List

from models.kubernetes import (
    PodInfo,
    DeploymentInfo,
    ServiceInfo,
    EventInfo,
    NodeInfo,
    IngressInfo,
)


@dataclass
class ClusterSnapshot:
    """
    Represents the complete observed state
    of the Kubernetes cluster.
    """

    pods: List[PodInfo] = field(default_factory=list)

    deployments: List[DeploymentInfo] = field(default_factory=list)

    services: List[ServiceInfo] = field(default_factory=list)

    ingresses: List[IngressInfo] = field(default_factory=list)

    events: List[EventInfo] = field(default_factory=list)

    nodes: List[NodeInfo] = field(default_factory=list)
