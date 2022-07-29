from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.stores.item_repo import ItemRepoInterface
from src.repository.postgresql.stores.item_repository import ItemRepository


class ItemService:

    def __init__(self):
        self.item_repository: ItemRepoInterface = ItemRepository()

    def get_items(self, uow: SqlUow):
        with uow:
            data: list = self.item_repository.get_items(uow)
            return data

    def create_item(self, data: dict, uow: SqlUow):
        with uow:
            found, response = self.item_repository.get_by_code(data["code"], uow)

            if found:
                return {"message": "item already exist"}

            response = self.item_repository.create_item(data, uow)
            uow.commit()
            return response

    def update_item(self, code: str, data: dict, uow: SqlUow):
        with uow:
            found, response = self.item_repository.get_by_code(code, uow)

            if not found:
                return response

            res = self.item_repository.update_item(code, data, uow)
            uow.commit()
            return res

    def delete_item(self, code: str, uow: SqlUow):
        with uow:
            found, response = self.item_repository.get_by_code(code, uow)

            if not found:
                return response

            delete = self.item_repository.delete_item(code, uow)
            uow.commit()
            return {"msg": delete}

    def get_by_code(self, code: str, uow: SqlUow):
        with uow:
            found, response = self.item_repository.get_by_code(code, uow)
            if found:
                return response

            return {"message": f"item  with code: %s does not exist" % code}
