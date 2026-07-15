from collector.pods import get_pods
from rich.console import Console
from rich.table import Table

console = Console()


def main():

    table = Table(title="Kubernetes Pods")

    table.add_column("Namespace")
    table.add_column("Pod")
    table.add_column("Status")
    table.add_column("Node")
    table.add_column("Pod IP")
    table.add_column("Restarts")

    for pod in get_pods():

        table.add_row(
            pod["namespace"],
            pod["name"],
            pod["status"],
            str(pod["node"]),
            str(pod["pod_ip"]),
            str(pod["restarts"])
        )

    console.print(table)


if __name__ == "__main__":
    main()
