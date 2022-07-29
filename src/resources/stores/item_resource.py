from flask import request

from src.resources.base import BaseResourse


class ItemResource(BaseResourse):

    def get(self):
        try:
            data = self.item_service.get_items(self.message_bus.uow)
            return data
        except Exception as ex:
            return {"message": ex}

    def post(self):
        data = request.get_json()
        response = self.item_service.create_item(data, self.message_bus.uow)
        return response


class ItemDetailResource(BaseResourse):

    def get(self, code: str):
        response = self.item_service.get_by_code(code, self.message_bus.uow)
        return response

    def put(self, code: str):
        data = request.get_json()
        res = self.item_service.update_item(code, data, self.message_bus.uow)
        return res

    def delete(self, code: str):
        res = self.item_service.delete_item(code, self.message_bus.uow)
        return res
