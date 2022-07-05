
from echeapi import cache, settings
from echeapi.utils import db


def main(*args):
    db.initialize()
    cache.clear()
    print(f'Created empty database {settings.DB_FILENAME}')
