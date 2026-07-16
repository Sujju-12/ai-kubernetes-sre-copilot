from models.incident import Incident


class IncidentClassifier:

    def classify(self, snapshot):

        for pod in snapshot.pods:

            if pod.container_state == "ImagePullBackOff":
                return Incident(
                    incident_type="IMAGE_PULL",
                    severity="HIGH",
                    confidence=0.99,
                    summary=f"{pod.name} cannot pull image"
                )

            if pod.container_state == "ErrImagePull":
                return Incident(
                    incident_type="IMAGE_PULL",
                    severity="HIGH",
                    confidence=0.99,
                    summary=f"{pod.name} cannot pull image"
                )

            if pod.container_state == "CrashLoopBackOff":
                return Incident(
                    incident_type="CRASH_LOOP",
                    severity="HIGH",
                    confidence=0.96,
                    summary=f"{pod.name} is crashing"
                )

            if pod.container_state == "OOMKilled":
                return Incident(
                    incident_type="OOM_KILLED",
                    severity="HIGH",
                    confidence=0.98,
                    summary=f"{pod.name} exceeded memory"
                )

            if pod.phase == "Pending":
                return Incident(
                    incident_type="PENDING",
                    severity="MEDIUM",
                    confidence=0.80,
                    summary=f"{pod.name} pending scheduling"
                )

        return Incident(
            incident_type="HEALTHY",
            severity="NONE",
            confidence=1.0,
            summary="No Kubernetes incidents detected"
        )
