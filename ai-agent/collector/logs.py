from collector.kube_client import KubernetesClient

kube = KubernetesClient()


def get_logs(namespace, pod_name, container=None, tail_lines=200):

    try:

        logs = kube.core.read_namespaced_pod_log(
            name=pod_name,
            namespace=namespace,
            container=container,
            tail_lines=tail_lines,
        )

        return logs

    except Exception as e:
        return str(e)


def get_previous_logs(namespace, pod_name, container=None):

    try:

        logs = kube.core.read_namespaced_pod_log(
            name=pod_name,
            namespace=namespace,
            container=container,
            previous=True,
            tail_lines=200,
        )

        return logs

    except Exception as e:
        return str(e)
