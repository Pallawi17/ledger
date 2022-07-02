from uuid import uuid4

from migrate import *
from sqlalchemy import MetaData, Table, Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()
users = Table(
    "user_details", metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4(), nullable=False),
    Column("emp_id", String(10), unique=True, nullable=False),
    Column("username", String(50), unique=True, nullable=False),
    Column("password", String(50), unique=False, nullable=False),
    Column("active", Boolean, nullable=False),
    Column("tenent_id", String(20), unique=True, nullable=False)
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata.bind = migrate_engine
    users.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata.bind = migrate_engine
    users.drop()
