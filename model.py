""" ORM for mailroom database """
import os

from peewee import Model, CharField, IntegerField, ForeignKeyField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))  #pylint: disable=invalid-name

class Donor(Model):
    """ Person: donor """
    name = CharField(max_length=255, unique=True)

    class Meta:
        """ peewee Model Meta class """
        database = db

class Donation(Model):
    """ Value: donation """
    value = IntegerField()
    donor = ForeignKeyField(Donor, backref='donations')

    class Meta:
        """ peewee Model Meta class """
        database = db
