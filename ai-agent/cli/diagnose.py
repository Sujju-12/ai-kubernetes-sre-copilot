from collector.snapshot import build_snapshot
from diagnosis.engine import DiagnosisEngine
from reports.markdown import MarkdownReport


def diagnose(namespace):

    snapshot = build_snapshot(namespace)

    incident, knowledge = DiagnosisEngine().run(snapshot)

    MarkdownReport().generate(
        incident,
        knowledge,
    )
