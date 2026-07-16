import yaml
from pathlib import Path


class KnowledgeLoader:

    def __init__(self):
        self.base = Path(__file__).parent

    def load(self, incident):

        mapping = {
            "IMAGE_PULL": "image_pull.yaml",
            "CRASH_LOOP": "crashloop.yaml",
            "OOM_KILLED": "oom.yaml",
            "PENDING": "pending.yaml",
        }

        filename = mapping.get(incident)

        if not filename:
            return None

        with open(self.base / filename) as f:
            return yaml.safe_load(f)
