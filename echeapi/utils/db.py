
import sqlite3
from datetime import datetime

import pandas as pd

from echeapi import settings


def get_connection(db=settings.DB_FILENAME):
    return sqlite3.connect(db)


def initialize(table=settings.DB_TABLE, connection=None):
    df = pd.DataFrame([], columns=settings.KNOWN_KEYS)
    save(df, table=table, connection=connection)


def save(df, table=settings.DB_TABLE, connection=None):
    if connection is None:
        connection = get_connection()
    df['created'] = datetime.now()
    df.to_sql(
        name=table,
        con=connection,
        if_exists='replace',
        index=True,
        index_label='id',
    )


def fetch(fields=None, filter=None, table=settings.DB_TABLE, connection=None):
    fields = ",".join([f'\"{f}\"' for f in fields]) if fields else "*"

    if filter is not None:
        key, value = filter
        if value is None:
            query = f"SELECT {fields} FROM {table} WHERE \"{key}\" IS NULL"
            params = ()
        else:
            query = f"SELECT {fields} FROM {table} WHERE \"{key}\" = ?"
            params = (value,)
    else:
        query = f"SELECT {fields} FROM {table}"
        params = ()

    if connection is None:
        connection = get_connection()

    return pd.read_sql_query(
        con=connection,
        sql=query,
        params=params,
        coerce_float=False,
        parse_dates=settings.DATE_FIELDS,
    )
