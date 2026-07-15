from collector.kube_client import KubernetesClient

kube = KubernetesClient()


def get_deployments():
    """
    Collect deployment information.
    """

    deployments = []

    for deployment in kube.apps.list_deployment_for_all_namespaces().items:

        deployments.append(
            {
                "namespace": deployment.metadata.namespace,
                "name": deployment.metadata.name,
                "desired": deployment.spec.replicas,
                "ready": deployment.status.ready_replicas or 0,
                "available": deployment.status.available_replicas or 0,
                "updated": deployment.status.updated_replicas or 0,
                "strategy": deployment.spec.strategy.type,
            }
        )

    return deployments
