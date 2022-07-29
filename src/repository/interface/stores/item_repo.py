import abc

from src.infrastructure.interface.sql_uow import SqlUow


class ItemRepoInterface(abc.ABC):

    @abc.abstractmethod
    def get_items(self, uow: SqlUow):
        pass

    @abc.abstractmethod
    def create_item(self, data: dict, uow: SqlUow):
        pass

    @abc.abstractmethod
    def update_item(self, code: str, data: dict, uow: SqlUow):
        pass

    @abc.abstractmethod
    def delete_item(self, code: str, uow: SqlUow):
        pass

    @abc.abstractmethod
    def get_by_code(self, code: str, uow: SqlUow):
        pass
