# Unit of work
import abc

from sqlalchemy.orm import Session


class SqlUow(abc.ABC):

    def __init__(self):
        self._session: Session = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def get_session(self) -> Session:
        if not self._session:
            raise Exception("Session not defined")
        return self._session

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def rollback(self):
        pass

    @abc.abstractmethod
    def _commit(self):
        pass
