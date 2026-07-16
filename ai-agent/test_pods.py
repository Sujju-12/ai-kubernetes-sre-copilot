from collector.pods import get_pods


pods = get_pods()

for pod in pods:

    print("=" * 50)

    print(pod)
