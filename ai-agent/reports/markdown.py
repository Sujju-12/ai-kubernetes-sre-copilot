from pathlib import Path
from datetime import datetime


class MarkdownReport:

    def generate(self, incident, ai_response=""):

        reports_dir = Path("reports/output")
        reports_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = reports_dir / f"{incident.incident_type}_{timestamp}.md"

        with open(filename, "w", encoding="utf-8") as file:

            file.write("# AI Kubernetes SRE Copilot\n\n")

            file.write("## Incident\n")
            file.write(f"{incident.incident_type}\n\n")

            file.write("## Severity\n")
            file.write(f"{incident.severity}\n\n")

            file.write("## Confidence\n")
            file.write(f"{incident.confidence}\n\n")

            file.write("## Namespace\n")
            file.write(f"{incident.affected_namespace}\n\n")

            file.write("## Deployment\n")
            file.write(f"{incident.affected_deployment}\n\n")

            file.write("## Pod\n")
            file.write(f"{incident.affected_pod}\n\n")

            file.write("## Node\n")
            file.write(f"{incident.node}\n\n")

            file.write("## Deployment Status\n\n")

            file.write(f"- Desired Replicas : {incident.desired_replicas}\n")
            file.write(f"- Ready Replicas : {incident.ready_replicas}\n")
            file.write(f"- Available Replicas : {incident.available_replicas}\n\n")

            file.write("## Events\n\n")

            for event in incident.events:
                file.write(f"- {event}\n")

            file.write("\n")

            file.write("## Recommendations\n\n")

            for recommendation in incident.recommendations:
                file.write(f"- {recommendation}\n")

            file.write("\n")

            file.write("## AI Root Cause Analysis\n\n")

            if ai_response:
                file.write(ai_response)
            else:
                file.write("AI response unavailable.\n")

        return str(filename)
