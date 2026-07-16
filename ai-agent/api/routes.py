from fastapi import APIRouter

from collector.snapshot import build_snapshot
from diagnosis.engine import DiagnosisEngine
from llm.prompt_builder import PromptBuilder
from llm.gemini_client import GeminiClient

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

    incident = DiagnosisEngine().analyze(snapshot)

    ai_response = ""

    if incident.incident_type != "HEALTHY":

        try:

            prompt = PromptBuilder().build(incident)

            ai_response = GeminiClient().generate(prompt)

        except Exception as e:

            ai_response = str(e)

    return {

        "incident": incident.incident_type,

        "severity": incident.severity,

        "confidence": incident.confidence,

        "namespace": incident.affected_namespace,

        "deployment": incident.affected_deployment,

        "pod": incident.affected_pod,

        "node": incident.node,

        "events": incident.events,

        "recommendations": incident.recommendations,

        "ai_response": ai_response

    }
