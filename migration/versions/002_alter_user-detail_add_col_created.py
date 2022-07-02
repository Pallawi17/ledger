from datetime import datetime

import pytz
from migrate import *
from sqlalchemy import MetaData, Table, Column, DateTime

tz = pytz.timezone("Asia/Kolkata")


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    metadata = MetaData(bind=migrate_engine)
    users = Table("user_details", metadata, autoload=True)
    created: Column = Column("created_time", DateTime(timezone=True), nullable=False, default=datetime.now(tz))
    created.create(users)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    metadata = MetaData(bind=migrate_engine)
    users = Table("user_details", metadata, autoload=True)
    users.c.created_time.drop()
