from sqlalchemy import MetaData, Table, Column, String
from migrate import *

metadata = MetaData()

item = Table(
    "items", metadata,
    Column("code", String(5), primary_key=True, unique=True, nullable=False),
    Column("name", String(15), nullable=False),
    Column("description", String(30))
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata.bind = migrate_engine
    item.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata.bind = migrate_engine
    item.drop()
