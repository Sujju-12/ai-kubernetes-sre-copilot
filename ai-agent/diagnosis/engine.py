from models.incident import Incident


class DiagnosisEngine:

    def analyze(self, snapshot):

        # Iterate through all pods
        for pod in snapshot.pods:

            deployment = self._find_deployment(snapshot, pod)

            # ------------------------------------------------------------------
            # IMAGE PULL
            # ------------------------------------------------------------------
            if pod.container_state in ["ImagePullBackOff", "ErrImagePull"]:

                incident = self._create_incident(
                    snapshot=snapshot,
                    pod=pod,
                    deployment=deployment,
                    incident_type="IMAGE_PULL",
                    severity="HIGH",
                    confidence=0.99,
                    summary="Container image cannot be pulled.",
                    recommendations=[
                        "Verify Docker image exists.",
                        "Verify image tag.",
                        "kubectl describe pod",
                        "kubectl rollout restart deployment",
                    ],
                )

                return incident

            # ------------------------------------------------------------------
            # CRASH LOOP
            # ------------------------------------------------------------------
            if pod.container_state == "CrashLoopBackOff":

                incident = self._create_incident(
                    snapshot=snapshot,
                    pod=pod,
                    deployment=deployment,
                    incident_type="CRASH_LOOP",
                    severity="HIGH",
                    confidence=0.97,
                    summary="Container is crashing repeatedly.",
                    recommendations=[
                        "kubectl logs",
                        "kubectl logs --previous",
                        "Check application startup.",
                        "Check environment variables.",
                    ],
                )

                return incident

            # ------------------------------------------------------------------
            # OOM
            # ------------------------------------------------------------------
            if pod.container_state == "OOMKilled":

                incident = self._create_incident(
                    snapshot=snapshot,
                    pod=pod,
                    deployment=deployment,
                    incident_type="OOM_KILLED",
                    severity="HIGH",
                    confidence=0.98,
                    summary="Container exceeded memory limit.",
                    recommendations=[
                        "Increase memory limits.",
                        "Investigate memory leak.",
                        "kubectl top pod",
                    ],
                )

                return incident

            # ------------------------------------------------------------------
            # Pending
            # ------------------------------------------------------------------
            if pod.phase == "Pending":

                incident = self._create_incident(
                    snapshot=snapshot,
                    pod=pod,
                    deployment=deployment,
                    incident_type="PENDING",
                    severity="MEDIUM",
                    confidence=0.90,
                    summary="Pod is pending scheduling.",
                    recommendations=[
                        "kubectl describe pod",
                        "kubectl get nodes",
                        "Check PVC",
                        "Check node resources",
                    ],
                )

                return incident

        # ----------------------------------------------------------------------
        # Deployment health check
        # ----------------------------------------------------------------------
        for deployment in snapshot.deployments:

            if deployment.ready < deployment.desired:

                incident = Incident(
                    incident_type="DEPLOYMENT_DEGRADED",
                    severity="HIGH",
                    confidence=0.95,
                    summary="Deployment does not have all desired replicas.",
                )

                incident.affected_namespace = deployment.namespace
                incident.affected_deployment = deployment.name
                incident.desired_replicas = deployment.desired
                incident.ready_replicas = deployment.ready
                incident.available_replicas = deployment.available

                incident.recommendations = [
                    "kubectl describe deployment",
                    "kubectl get pods",
                    "kubectl rollout status deployment",
                ]

                return incident

        # ----------------------------------------------------------------------
        # Healthy
        # ----------------------------------------------------------------------
        return Incident(
            incident_type="HEALTHY",
            severity="NONE",
            confidence=1.0,
            summary="Cluster is healthy.",
        )

    # ======================================================================
    # Helper Methods
    # ======================================================================

    def _find_deployment(self, snapshot, pod):

        """
        Try to identify the deployment that owns this pod.
        """

        for deployment in snapshot.deployments:

            if pod.name.startswith(deployment.name):
                return deployment

        return None

    def _create_incident(
        self,
        snapshot,
        pod,
        deployment,
        incident_type,
        severity,
        confidence,
        summary,
        recommendations,
    ):

        incident = Incident(
            incident_type=incident_type,
            severity=severity,
            confidence=confidence,
            summary=summary,
        )

        # Pod information
        incident.affected_namespace = pod.namespace
        incident.affected_pod = pod.name
        incident.node = pod.node
        incident.logs = pod.logs

        # Deployment information
        if deployment:

            incident.affected_deployment = deployment.name
            incident.desired_replicas = deployment.desired
            incident.ready_replicas = deployment.ready
            incident.available_replicas = deployment.available

        # Events
        for event in snapshot.events:

            if event.object_name == pod.name:

                incident.events.append(
                    f"{event.reason}: {event.message}"
                )

        # Recommendations
        incident.recommendations = recommendations

        return incident
