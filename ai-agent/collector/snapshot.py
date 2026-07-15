from collector.pods import get_pods
from collector.deployments import get_deployments
from collector.services import get_services
from collector.ingress import get_ingress
from collector.events import get_events
from collector.nodes import get_nodes


def build_snapshot():

    return {
        "pods": get_pods(),
        "deployments": get_deployments(),
        "services": get_services(),
        "ingress": get_ingress(),
        "events": get_events(),
        "nodes": get_nodes(),
    }
