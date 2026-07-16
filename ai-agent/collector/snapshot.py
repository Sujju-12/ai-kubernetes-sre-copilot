from models.snapshot import ClusterSnapshot

from collector.pods import get_pods
from collector.deployments import get_deployments
from collector.services import get_services
from collector.events import get_events
from collector.ingress import get_ingresses
from collector.nodes import get_nodes
from collector.logs import get_logs, get_previous_logs


def build_snapshot(namespace=None):
    """
    Build a complete snapshot of the Kubernetes cluster
    or a specific namespace.
    """

    snapshot = ClusterSnapshot()

    # Collect Kubernetes resources
    snapshot.pods = get_pods(namespace)
    snapshot.deployments = get_deployments(namespace)
    snapshot.services = get_services(namespace)
    snapshot.events = get_events(namespace)
    snapshot.ingresses = get_ingresses(namespace)
    snapshot.nodes = get_nodes()

    # Enrich each pod with logs
    for pod in snapshot.pods:

        try:
            pod.logs = get_logs(
                namespace=pod.namespace,
                pod_name=pod.name
            )
        except Exception:
            pod.logs = ""

        try:
            pod.previous_logs = get_previous_logs(
                namespace=pod.namespace,
                pod_name=pod.name
            )
        except Exception:
            pod.previous_logs = ""

    return snapshot
