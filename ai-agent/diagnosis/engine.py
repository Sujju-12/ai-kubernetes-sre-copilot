from classifier.incident_classifier import IncidentClassifier
from knowledge.loader import KnowledgeLoader


class DiagnosisEngine:

    def run(self, snapshot):

        classifier = IncidentClassifier()

        incident = classifier.classify(snapshot)

        knowledge = KnowledgeLoader().load(
            incident.incident_type
        )

        return incident, knowledge
