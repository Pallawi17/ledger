from flask_restful import Resource

from src.bootstrap import main_bootstrap
from src.bootstrap.bus.message_bus import MessageBus
from src.services.stores.item_service import ItemService


class BaseResourse(Resource):
    message_bus: MessageBus = main_bootstrap.bootstrap()
    item_service: ItemService = ItemService()

