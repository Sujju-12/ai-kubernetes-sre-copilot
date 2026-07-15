from collector.kube_client import KubernetesClient

kube = KubernetesClient()


def get_services():
    """
    Collect service information.
    """

    services = []

    for svc in kube.core.list_service_for_all_namespaces().items:

        ports = []

        for port in svc.spec.ports:

            ports.append(
                {
                    "port": port.port,
                    "target_port": port.target_port,
                    "protocol": port.protocol,
                }
            )

        services.append(
            {
                "namespace": svc.metadata.namespace,
                "name": svc.metadata.name,
                "type": svc.spec.type,
                "cluster_ip": svc.spec.cluster_ip,
                "selector": dict(svc.spec.selector or {}),
                "ports": ports,
            }
        )

    return services
