import json
from pathlib import Path
from datetime import datetime


class JsonReport:

    def generate(self, incident, ai_response=""):

        reports_dir = Path("reports/output")
        reports_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = reports_dir / f"{incident.incident_type}_{timestamp}.json"

        report = {
            "incident": {
                "type": incident.incident_type,
                "severity": incident.severity,
                "confidence": incident.confidence,
                "summary": incident.summary
            },
            "resource": {
                "namespace": incident.affected_namespace,
                "deployment": incident.affected_deployment,
                "pod": incident.affected_pod,
                "node": incident.node
            },
            "deployment_status": {
                "desired_replicas": incident.desired_replicas,
                "ready_replicas": incident.ready_replicas,
                "available_replicas": incident.available_replicas
            },
            "events": incident.events,
            "suggested_commands": incident.recommendations,
            "logs": incident.logs,
            "ai_root_cause_analysis": ai_response
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        return str(filename)
