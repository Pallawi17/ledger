import abc


class Database(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def get_connection(self, **kwargs):
        pass


