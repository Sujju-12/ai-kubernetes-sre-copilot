from collector.snapshot import build_snapshot

from diagnosis.engine import DiagnosisEngine

from reports.report import DiagnosisReport
from reports.markdown import MarkdownReport
from reports.json_report import JsonReport

from llm.prompt_builder import PromptBuilder
from llm.openrouter_client import OpenRouterClient



def diagnose(namespace):

    print("\nCollecting Kubernetes resources...")

    snapshot = build_snapshot(namespace)

    print("Analyzing cluster...")

    incidents = DiagnosisEngine().analyze(snapshot)

    for incident in incidents:

        DiagnosisReport().display(incident)

        ai_response = ""

        if incident.incident_type != "HEALTHY":

            print("\n")
            print("=" * 80)
            print("🤖 Sending Incident to Gemini")
            print("=" * 80)

            try:

                prompt = PromptBuilder().build(incident)
                ai_response = OpenRouterClient().generate(prompt)
                

                print()
                print("=" * 80)
                print("🤖 AI ROOT CAUSE ANALYSIS")
                print("=" * 80)
                print(ai_response)
                print("=" * 80)

            except Exception as e:

                print(f"\nGemini unavailable : {e}")

                ai_response = "Gemini unavailable."

        md_file = MarkdownReport().generate(
            incident,
            ai_response
        )

        json_file = JsonReport().generate(
            incident,
            ai_response
        )

        print()
        print("=" * 80)
        print("Reports Generated")
        print("=" * 80)
        print(md_file)
        print(json_file)
        print("=" * 80)
