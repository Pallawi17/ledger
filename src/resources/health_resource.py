
from src.resources.base import BaseResourse


class HealthCheckResource(BaseResourse):
    def get(self):
        return {'heart_beat': 'alive'}


