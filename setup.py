""" (Re)create database for mailroom donations """
import random

from model import db, Donor, Donation

db.connect()

# This line will allow you "upgrade" an existing database by
# dropping all existing tables from it.
db.drop_tables([Donor, Donation])

db.create_tables([Donor, Donation])

ALICE = Donor(name="Alice")
ALICE.save()

BOB = Donor(name="Bob")
BOB.save()

CHARLIE = Donor(name="Charlie")
CHARLIE.save()

DONORS = [ALICE, BOB, CHARLIE]

for x in range(30):
    Donation(donor=random.choice(DONORS), value=random.randint(100, 10000)).save()
