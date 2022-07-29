from src.infrastructure.entity.tables import ItemEntity
from src.infrastructure.interface.sql_uow import SqlUow
from src.repository.interface.stores.item_repo import ItemRepoInterface


class ItemRepository(ItemRepoInterface):

    def get_items(self, uow: SqlUow):
        query = """
        SELECT code, name, description
        FROM items
        """
        results = list(uow.get_session().execute(query))
        items = []
        for result in results:
            item = {
                "code": result.code,
                "name": result.name,
                "description": result.description
            }
            items.append(item)

        return items

    def create_item(self, data: dict, uow: SqlUow):
        # item = ItemEntity(
        #     data["code"],
        #     data["name"],
        #     data["description"]
        # )
        # uow.get_session().add(item)

        uow.get_session().execute(
            """
            INSERT INTO items
            (code, name, description)
            VALUES (:code, :name, :description)
            """,
            dict(code=data["code"],
                 name=data["name"],
                 description=data["description"]
                 )
        )

        return {"msg": data["code"]}

    def update_item(self, code: str, data: dict, uow: SqlUow):

        uow.get_session().execute(
            """
            UPDATE items SET 
                name=:name,
                description=:description
            WHERE code=:code;
            """,
            dict(code=code,
                name=data["name"],
                description=data["description"]
                 )
        )
        return code

    def delete_item(self, code: str,  uow: SqlUow):
        uow.get_session().execute(
            """
            DELETE FROM items 
            WHERE code = :code
            """,
            dict(code=code)
        )

        return code

    def get_by_code(self, code: str, uow: SqlUow):
        result = uow.get_session().execute(
            """
            SELECT code, name, description
            FROM items
            WHERE code=:code
            """,
            dict(code=code)
        ).first()

        if not result:
            return False, {"message": "item does not exist"}

        item = {
            "code": result.code,
            "name": result.name,
            "description": result.description
        }
        return True, item

