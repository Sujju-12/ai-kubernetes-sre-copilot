from collector.kube_client import KubernetesClient
from models.kubernetes import EventInfo

kube = KubernetesClient()


def get_events(namespace=None):

    events = []

    if namespace:
        event_list = kube.core.list_namespaced_event(namespace).items
    else:
        event_list = kube.core.list_event_for_all_namespaces().items

    for event in event_list:

        events.append(
            EventInfo(
                namespace=event.metadata.namespace,
                type=event.type,
                reason=event.reason,
                message=event.message,
                object_name=event.involved_object.name,
            )
        )

    return events
