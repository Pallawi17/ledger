from sqlalchemy import create_engine

from src.infrastructure.interface.database import Database


class PostgresDB(Database):
    __instance = None

    def __init__(self, **kwargs):
        super().__init__()
        db_details = kwargs
        db_details = {
            "username": "postgres",
            "password": "root",
            "host": "localhost",
            "port": "5432",
            "dbname": "ledger"
        }
        self.engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(
            db_details["username"],
            db_details["password"],
            db_details["host"],
            db_details["port"],
            db_details["dbname"]
        ))

        PostgresDB.__instance = self.engine

    def get_connection(self, **kwargs):
        if PostgresDB.__instance is None:
            PostgresDB(**kwargs)
            
        return PostgresDB.__instance