from models.snapshot import ClusterSnapshot

from collector.pods import get_pods

from collector.deployments import get_deployments

from collector.services import get_services

from collector.ingress import get_ingresses

from collector.nodes import get_nodes

from collector.events import get_events
# These imports will be enabled as we build them
# from collector.deployments import get_deployments
# from collector.services import get_services
# from collector.events import get_events
# from collector.ingress import get_ingresses
# from collector.nodes import get_nodes

def build_snapshot(namespace=None):
    """
    Build a snapshot of the current cluster state.
    """

    snapshot = ClusterSnapshot()
    snapshot.pods = get_pods(namespace)
    snapshot.deployments = get_deployments(namespace)
    snapshot.services = get_services(namespace)
    snapshot.events = get_events(namespace)
    snapshot.ingresses = get_ingresses(namespace)
    snapshot.nodes = get_nodes()
    # We'll enable these gradually
    # snapshot.deployments = get_deployments()
    # snapshot.services = get_services()
    # snapshot.events = get_events()
    # snapshot.ingresses = get_ingresses()
    # snapshot.nodes = get_nodes()

    return snapshot
