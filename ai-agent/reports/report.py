class DiagnosisReport:

    def display(self, incident):

        print()
        print("=" * 80)
        print("🤖 AI Kubernetes SRE Copilot")
        print("=" * 80)

        print(f"Incident      : {incident.incident_type}")
        print(f"Severity      : {incident.severity}")
        print(f"Confidence    : {incident.confidence}")

        print()

        print(f"Summary       : {incident.summary}")

        print()

        print(f"Namespace     : {incident.affected_namespace}")
        print(f"Deployment    : {incident.affected_deployment}")
        print(f"Pod           : {incident.affected_pod}")
        print(f"Node          : {incident.node}")

        print()

        print("Deployment")
        print("----------")
        print(f"Desired       : {incident.desired_replicas}")
        print(f"Ready         : {incident.ready_replicas}")
        print(f"Available     : {incident.available_replicas}")

        print()

        print("Events")
        print("------")

        if incident.events:
            for event in incident.events:
                print(f"- {event}")
        else:
            print("No events found.")

        print()

        print("Recommendations")
        print("---------------")

        if incident.recommendations:
            for recommendation in incident.recommendations:
                print(f"- {recommendation}")
        else:
            print("No recommendations.")

        print()
        print("=" * 80)
