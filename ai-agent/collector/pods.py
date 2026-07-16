from collector.kube_client import KubernetesClient

from models.kubernetes import PodInfo


kube = KubernetesClient()

def get_pods(namespace=None):

    pods = []

    if namespace:
        pod_list = kube.core.list_namespaced_pod(namespace).items
    else:
        pod_list = kube.core.list_pod_for_all_namespaces().items

    for pod in pod_list:

        container_state = "Unknown"
        restart_count = 0
        ready = False

        if pod.status.container_statuses:

            container = pod.status.container_statuses[0]

            ready = container.ready

            restart_count = container.restart_count

            state = container.state

            if state.waiting:
                container_state = state.waiting.reason

            elif state.running:
                container_state = "Running"

            elif state.terminated:
                container_state = state.terminated.reason

        pods.append(
            PodInfo(
                namespace=pod.metadata.namespace,
                name=pod.metadata.name,
                phase=pod.status.phase,
                container_state=container_state,
                ready=ready,
                restart_count=restart_count,
                node=pod.spec.node_name,
                pod_ip=pod.status.pod_ip,
                host_ip=pod.status.host_ip,
                start_time=str(pod.status.start_time),
                labels=dict(pod.metadata.labels or {}),
            )
        )

    return pods
