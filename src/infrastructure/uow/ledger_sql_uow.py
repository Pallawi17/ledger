from sqlalchemy.orm import sessionmaker, Session

from src.infrastructure.database.postgresql import PostgresDB
from src.infrastructure.interface.sql_uow import SqlUow

# DEFAULT_SESSION_FACTORY = app.config['DB_SESSION']


class LedgerSqlUow(SqlUow):
    """
    Ledger unit of work
    """

    def __init__(self):
        DB_Engine = PostgresDB().get_connection()
        session_factory = sessionmaker(bind=DB_Engine)
        self.session_factory = session_factory
        super().__init__()

    def __enter__(self):
        self._session: Session = self.session_factory()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self._session.close()

    def _commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
