from utils.db_api import db
from peewee import *
from datetime import datetime


class User(Model):
    id = IntegerField(primary_key=True, null=False, index=True, unique=True)

    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
