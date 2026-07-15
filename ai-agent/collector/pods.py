from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


def get_pods():
    """
    Collect detailed pod information from the Kubernetes cluster.

    Returns:
        List[dict]
    """

    try:
        config.load_kube_config()
    except ConfigException:
        config.load_incluster_config()

    v1 = client.CoreV1Api()

    pods = []

    for pod in v1.list_pod_for_all_namespaces().items:

        # Default values
        container_state = "Unknown"
        restart_count = 0

        if pod.status.container_statuses:

            container = pod.status.container_statuses[0]

            restart_count = container.restart_count

            state = container.state

            if state.waiting:
                container_state = state.waiting.reason

            elif state.running:
                container_state = "Running"

            elif state.terminated:
                container_state = state.terminated.reason

        pod_info = {
            "namespace": pod.metadata.namespace,
            "name": pod.metadata.name,
            "phase": pod.status.phase,
            "container_state": container_state,
            "ready": f"{pod.status.container_statuses[0].ready if pod.status.container_statuses else False}",
            "restarts": restart_count,
            "node": pod.spec.node_name,
            "pod_ip": pod.status.pod_ip,
            "host_ip": pod.status.host_ip,
            "start_time": str(pod.status.start_time),
            "labels": dict(pod.metadata.labels or {}),
        }

        pods.append(pod_info)

    return pods
