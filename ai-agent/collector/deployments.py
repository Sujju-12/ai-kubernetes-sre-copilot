from collector.kube_client import KubernetesClient
from models.kubernetes import DeploymentInfo

kube = KubernetesClient()


def get_deployments(namespace=None):
    """
    Collect deployment information from Kubernetes.
    """

    deployments = []

    if namespace:
        deployment_list = kube.apps.list_namespaced_deployment(namespace).items
    else:
        deployment_list = kube.apps.list_deployment_for_all_namespaces().items

    for deployment in deployment_list:

        deployments.append(
            DeploymentInfo(
                namespace=deployment.metadata.namespace,
                name=deployment.metadata.name,
                desired=deployment.spec.replicas or 0,
                ready=deployment.status.ready_replicas or 0,
                available=deployment.status.available_replicas or 0,
                updated=deployment.status.updated_replicas or 0,
                strategy=deployment.spec.strategy.type,
            )
        )

    return deployments
