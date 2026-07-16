class MarkdownReport:

    def generate(self, incident, knowledge):

        print("=" * 70)
        print("AI Kubernetes SRE Copilot")
        print("=" * 70)

        print(f"Incident   : {incident.incident_type}")
        print(f"Severity   : {incident.severity}")
        print(f"Confidence : {incident.confidence}")

        print()

        print("Summary")
        print("-------")
        print(incident.summary)

        if knowledge:

            print()
            print("Possible Causes")
            print("----------------")

            for item in knowledge["possible_causes"]:
                print(f"- {item}")

            print()
            print("Recommended Commands")
            print("--------------------")

            for cmd in knowledge["recommended_commands"]:
                print(f"- {cmd}")

        print("=" * 70)
