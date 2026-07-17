from collector.snapshot import build_snapshot
from classifier.incident_classifier import IncidentClassifier


def main():

    snapshot = build_snapshot()

    classifier = IncidentClassifier()

    incident = classifier.classify(snapshot)

    print("=" * 60)
    print("Incident Type :", incident.incident_type)
    print("Severity      :", incident.severity)
    print("Confidence    :", incident.confidence)
    print("Summary       :", incident.summary)
    print("=" * 60)


if __name__ == "__main__":
    main()
