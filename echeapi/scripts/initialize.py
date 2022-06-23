
from echeapi import cache, settings
from echeapi.utils import db


def main(*args):
    db.init()
    cache.clear()
    print(f'Created database {settings.DB_FILENAME}')
