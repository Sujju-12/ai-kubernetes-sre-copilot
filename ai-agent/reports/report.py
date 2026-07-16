class DiagnosisReport:

    def display(self, incident):

        print()

        print("=" * 80)

        print("🤖 AI Kubernetes SRE Copilot")

        print("=" * 80)

        print()

        print("Incident :", incident.incident_type)

        print("Severity :", incident.severity)

        print("Confidence :", incident.confidence)

        print()

        print("Namespace :", incident.affected_namespace)

        print("Deployment :", incident.affected_deployment)

        print("Pod :", incident.affected_pod)

        print("Node :", incident.node)

        print()

        print("Deployment Status")

        print("-----------------")

        print("Desired :", incident.desired_replicas)

        print("Ready :", incident.ready_replicas)

        print("Available :", incident.available_replicas)

        print()

        print("Events")

        print("------")

        for event in incident.events:
            print(event)

        print()

        print("Recommendations")

        print("----------------")

        for recommendation in incident.recommendations:
            print("-", recommendation)

        print()

        print("=" * 80)
