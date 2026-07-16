from collector.kube_client import KubernetesClient
from models.kubernetes import ServiceInfo, ServicePort

kube = KubernetesClient()


def get_services(namespace=None):

    services = []

    if namespace:
        service_list = kube.core.list_namespaced_service(namespace).items
    else:
        service_list = kube.core.list_service_for_all_namespaces().items

    for svc in service_list:

        ports = []

        for port in svc.spec.ports:
            ports.append(
                ServicePort(
                    port=port.port,
                    target_port=port.target_port,
                    protocol=port.protocol
                )
            )

        services.append(
            ServiceInfo(
                namespace=svc.metadata.namespace,
                name=svc.metadata.name,
                service_type=svc.spec.type,
                cluster_ip=svc.spec.cluster_ip,
                selector=svc.spec.selector or {},
                ports=ports
            )
        )

    return services
