from fastapi import APIRouter

from collector.snapshot import build_snapshot
from diagnosis.engine import DiagnosisEngine
from llm.prompt_builder import PromptBuilder
from llm.openrouter_client import OpenRouterClient
from api.schemas import DiagnoseRequest

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "UP"
    }


@router.post("/diagnose")
def diagnose(request: DiagnoseRequest):

    snapshot = build_snapshot(request.namespace)

    incidents = DiagnosisEngine().analyze(snapshot)

    results = []

    llm = OpenRouterClient()
    prompt_builder = PromptBuilder()

    for incident in incidents:

        ai_response = ""

        if incident.incident_type != "HEALTHY":

            try:

                prompt = prompt_builder.build(incident)
                ai_response = llm.generate(prompt)

            except Exception as e:

                ai_response = str(e)

        results.append(
            {
                "incident": incident.incident_type,
                "severity": incident.severity,
                "confidence": incident.confidence,
                "summary": incident.summary,
                "namespace": incident.affected_namespace,
                "deployment": incident.affected_deployment,
                "pod": incident.affected_pod,
                "node": incident.node,
                "events": incident.events,
                "logs": incident.logs,
                "recommendations": incident.recommendations,
                "ai_response": ai_response
            }
        )

    return {
        "total_incidents": len(results),
        "incidents": results
    }
