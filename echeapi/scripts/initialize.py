
from echeapi import settings
from echeapi.utils import db


def main(*args):
    db.init()
    print(f'Created database {settings.DB_FILENAME}')
