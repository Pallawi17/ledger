from flask_restful import Api

from src.resources.health_resource import HealthCheckResource


def set_routes(api: Api):
    api.add_resource(HealthCheckResource, '/health-check')
