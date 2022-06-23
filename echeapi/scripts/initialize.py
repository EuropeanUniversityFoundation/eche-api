
from echeapi import settings
from echeapi.utils import db


def main(*args):
    db.initialize()
    print(f'Created empty database {settings.DB_FILENAME}')
