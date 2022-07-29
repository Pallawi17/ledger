from flask_restful import Api

from src.resources.health_resource import HealthCheckResource
from src.resources.stores.item_resource import ItemResource, ItemDetailResource


def set_routes(api: Api):
    api.add_resource(HealthCheckResource, '/health-check')
    api.add_resource(ItemResource, '/item')
    api.add_resource(ItemDetailResource, '/item/<string:code>')

