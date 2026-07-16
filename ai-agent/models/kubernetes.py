from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ----------------------------------------------------
# Pod
# ----------------------------------------------------

@dataclass
class PodInfo:
    namespace: str
    name: str
    phase: str
    container_state: str
    ready: bool
    restart_count: int
    node: str
    pod_ip: Optional[str]
    host_ip: Optional[str]
    start_time: Optional[str]
    labels: Dict[str, str] = field(default_factory=dict)
    
    logs: str = ""

    previous_logs: str = ""


# ----------------------------------------------------
# Deployment
# ----------------------------------------------------

@dataclass
class DeploymentInfo:
    namespace: str
    name: str
    desired: int
    ready: int
    available: int
    updated: int
    strategy: str


# ----------------------------------------------------
# Service
# ----------------------------------------------------

@dataclass
class ServicePort:
    port: int
    target_port: int
    protocol: str


@dataclass
class ServiceInfo:
    namespace: str
    name: str
    service_type: str
    cluster_ip: Optional[str]
    selector: Dict[str, str] = field(default_factory=dict)
    ports: List[ServicePort] = field(default_factory=list)


# ----------------------------------------------------
# Event
# ----------------------------------------------------

@dataclass
class EventInfo:
    namespace: str
    type: str
    reason: str
    message: str
    object_name: str


# ----------------------------------------------------
# Node
# ----------------------------------------------------

@dataclass
class NodeInfo:
    name: str
    status: str
    kubelet_version: str
    os_image: str
    runtime: str


# ----------------------------------------------------
# Ingress
# ----------------------------------------------------

@dataclass
class IngressInfo:
    namespace: str
    name: str
    host: str
    path: str
    backend_service: str
