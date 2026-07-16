from collector.pods import get_pods
from collector.logs import get_logs

pods = get_pods("vehicle-login")

for pod in pods:

    print("=" * 80)
    print(pod.name)
    print("=" * 80)

    print(
        get_logs(
            namespace=pod.namespace,
            pod_name=pod.name
        )
    )
