import pytz
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

GlobalBase = declarative_base(name="GlobalBase")
TenantBase = declarative_base(name="TenantBase")

tz = pytz.timezone('Asia/Kolkata')


class ItemEntity(TenantBase):
    __tablename__ = "items"

    code = Column('code', String(5), primary_key=True, unique=True, nullable=False)
    name = Column('name', String(15), nullable=False)
    desc = Column('description', String(30))

    def __init__(self, code, name, desc):
        self.code = code
        self.name = name
        self.desc = desc
