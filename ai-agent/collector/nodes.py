from kubernetes import client, config


def get_nodes():
    """
    Collect node information.
    """

    config.load_kube_config()

    v1 = client.CoreV1Api()

    nodes = []

    for node in v1.list_node().items:

        nodes.append(
            {
                "name": node.metadata.name,
                "status": node.status.conditions[-1].type,
                "kubelet": node.status.node_info.kubelet_version,
                "os": node.status.node_info.os_image,
                "container_runtime": node.status.node_info.container_runtime_version,
            }
        )

    return nodes
