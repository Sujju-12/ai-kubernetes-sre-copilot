from models.incident import Incident


class DiagnosisEngine:

    def analyze(self, snapshot):

        incidents = []

        for pod in snapshot.pods:

            deployment = None

            for dep in snapshot.deployments:
                if dep.namespace == pod.namespace:
                    deployment = dep
                    break

            # --------------------------------------------------
            # IMAGE PULL
            # --------------------------------------------------
            if pod.container_state in [
                "ImagePullBackOff",
                "ErrImagePull"
            ]:

                incident = Incident(
                    incident_type="IMAGE_PULL",
                    severity="HIGH",
                    confidence=0.99,
                    summary="Container image cannot be pulled.",

                    affected_namespace=pod.namespace,
                    affected_deployment=deployment.name if deployment else "",
                    affected_pod=pod.name,
                    node=pod.node,

                    desired_replicas=deployment.desired if deployment else 0,
                    ready_replicas=deployment.ready if deployment else 0,
                    available_replicas=deployment.available if deployment else 0,

                    logs=pod.logs
                )

                for event in snapshot.events:
                    if event.object_name == pod.name:
                        incident.events.append(
                            f"{event.reason}: {event.message}"
                        )

                incident.recommendations = [
                    "kubectl describe pod",
                    "kubectl get events",
                    "Verify Docker image exists",
                    "Verify Docker image tag",
                    "kubectl rollout restart deployment"
                ]

                incidents.append(incident)

            # --------------------------------------------------
            # OOMKilled
            # --------------------------------------------------
            elif pod.container_state == "OOMKilled":

                incident = Incident(
                    incident_type="OOM_KILLED",
                    severity="HIGH",
                    confidence=0.98,
                    summary="Container exceeded memory limit.",

                    affected_namespace=pod.namespace,
                    affected_deployment=deployment.name if deployment else "",
                    affected_pod=pod.name,
                    node=pod.node,

                    desired_replicas=deployment.desired if deployment else 0,
                    ready_replicas=deployment.ready if deployment else 0,
                    available_replicas=deployment.available if deployment else 0,

                    logs=pod.logs
                )

                for event in snapshot.events:
                    if event.object_name == pod.name:
                        incident.events.append(
                            f"{event.reason}: {event.message}"
                        )

                incident.recommendations = [
                    "kubectl describe pod",
                    "kubectl top pod",
                    "Increase memory limits",
                    "Optimize application memory usage",
                    "Check for memory leaks"
                ]

                incidents.append(incident)

            # --------------------------------------------------
            # CRASH LOOP
            # --------------------------------------------------
            elif pod.container_state == "CrashLoopBackOff":

                incident = Incident(
                    incident_type="CRASH_LOOP",
                    severity="HIGH",
                    confidence=0.98,
                    summary="Container repeatedly crashes.",

                    affected_namespace=pod.namespace,
                    affected_deployment=deployment.name if deployment else "",
                    affected_pod=pod.name,
                    node=pod.node,

                    desired_replicas=deployment.desired if deployment else 0,
                    ready_replicas=deployment.ready if deployment else 0,
                    available_replicas=deployment.available if deployment else 0,

                    logs=pod.logs
                )

                for event in snapshot.events:
                    if event.object_name == pod.name:
                        incident.events.append(
                            f"{event.reason}: {event.message}"
                        )

                incident.recommendations = [
                    "kubectl logs",
                    "kubectl logs --previous",
                    "kubectl describe pod",
                    "Check application startup",
                    "Verify ConfigMaps and Secrets"
                ]

                incidents.append(incident)

            # --------------------------------------------------
            # PENDING
            # --------------------------------------------------
            elif pod.phase == "Pending":

                incident = Incident(
                    incident_type="PENDING_POD",
                    severity="MEDIUM",
                    confidence=0.97,
                    summary="Pod is waiting to be scheduled.",

                    affected_namespace=pod.namespace,
                    affected_deployment=deployment.name if deployment else "",
                    affected_pod=pod.name,
                    node=pod.node,

                    desired_replicas=deployment.desired if deployment else 0,
                    ready_replicas=deployment.ready if deployment else 0,
                    available_replicas=deployment.available if deployment else 0,

                    logs=pod.logs
                )

                for event in snapshot.events:
                    if event.object_name == pod.name:
                        incident.events.append(
                            f"{event.reason}: {event.message}"
                        )

                incident.recommendations = [
                    "kubectl describe pod",
                    "kubectl get nodes",
                    "kubectl top nodes",
                    "Check node resources",
                    "Verify taints and tolerations"
                ]

                incidents.append(incident)

        if not incidents:

            incidents.append(
                Incident(
                    incident_type="HEALTHY",
                    severity="NONE",
                    confidence=1.0,
                    summary="Cluster is healthy."
                )
            )

        return incidents
