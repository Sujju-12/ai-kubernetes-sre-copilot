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

            file.write("## Incident Summary\n\n")
            file.write(f"- **Incident:** {incident.incident_type}\n")
            file.write(f"- **Severity:** {incident.severity}\n")
            file.write(f"- **Confidence:** {incident.confidence}\n")
            file.write(f"- **Summary:** {incident.summary}\n\n")

            file.write("## Kubernetes Resources\n\n")
            file.write(f"- **Namespace:** {incident.affected_namespace}\n")
            file.write(f"- **Deployment:** {incident.affected_deployment}\n")
            file.write(f"- **Pod:** {incident.affected_pod}\n")
            file.write(f"- **Node:** {incident.node}\n\n")

            file.write("## Deployment Status\n\n")
            file.write(f"- Desired Replicas: {incident.desired_replicas}\n")
            file.write(f"- Ready Replicas: {incident.ready_replicas}\n")
            file.write(f"- Available Replicas: {incident.available_replicas}\n\n")

            file.write("## Events\n\n")

            if incident.events:
                for event in incident.events:
                    file.write(f"- {event}\n")
            else:
                file.write("- No events found.\n")

            file.write("\n")

            file.write("## Suggested Commands\n\n")

            if incident.recommendations:
                for recommendation in incident.recommendations:
                    file.write(f"- {recommendation}\n")
            else:
                file.write("- No recommendations.\n")

            file.write("\n")

            file.write("## Container Logs\n\n")

            if incident.logs:
                file.write("```text\n")
                file.write(incident.logs)
                file.write("\n```\n\n")
            else:
                file.write("No logs collected.\n\n")

            file.write("## AI Root Cause Analysis\n\n")

            if ai_response:
                file.write(ai_response)
            else:
                file.write("AI response unavailable.\n")

        return str(filename)
