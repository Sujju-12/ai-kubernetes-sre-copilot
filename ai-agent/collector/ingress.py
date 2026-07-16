from collector.kube_client import KubernetesClient
from models.kubernetes import IngressInfo

kube = KubernetesClient()


def get_ingresses(namespace=None):

    ingresses = []

    if namespace:
        ingress_list = kube.networking.list_namespaced_ingress(namespace).items
    else:
        ingress_list = kube.networking.list_ingress_for_all_namespaces().items

    for ingress in ingress_list:

        host = ""
        path = "/"
        backend = ""

        if ingress.spec.rules:
            rule = ingress.spec.rules[0]
            host = rule.host or ""

            if rule.http and rule.http.paths:
                p = rule.http.paths[0]
                path = p.path or "/"

                if p.backend.service:
                    backend = p.backend.service.name

        ingresses.append(
            IngressInfo(
                namespace=ingress.metadata.namespace,
                name=ingress.metadata.name,
                host=host,
                path=path,
                backend_service=backend,
            )
        )

    return ingresses
