import peewee

from .database import db


class Enterprise(peewee.Model):
    name = peewee.CharField(unique=True, index=True)
    is_active = peewee.BooleanField(default=True)

    class Meta:
        database = db
