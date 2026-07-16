from collector.kube_client import KubernetesClient
from models.kubernetes import NodeInfo

kube = KubernetesClient()


def get_nodes():

    nodes = []

    for node in kube.core.list_node().items:

        status = "Unknown"

        for condition in node.status.conditions:
            if condition.type == "Ready":
                status = condition.status

        nodes.append(
            NodeInfo(
                name=node.metadata.name,
                status=status,
                kubelet_version=node.status.node_info.kubelet_version,
                os_image=node.status.node_info.os_image,
                runtime=node.status.node_info.container_runtime_version,
            )
        )

    return nodes
