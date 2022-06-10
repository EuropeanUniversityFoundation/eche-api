
from echeapi import settings
from echeapi.utils import db


def main():
    db.init()

    print(f'Created database {settings.db_filename}')
