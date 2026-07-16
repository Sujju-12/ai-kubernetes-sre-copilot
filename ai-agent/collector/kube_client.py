from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException


class KubernetesClient:
    """
    Centralized Kubernetes client.
    """

    def __init__(self):

        try:
            config.load_kube_config()

        except ConfigException:
            config.load_incluster_config()

        self.core = client.CoreV1Api()

        self.apps = client.AppsV1Api()

        self.networking = client.NetworkingV1Api()
