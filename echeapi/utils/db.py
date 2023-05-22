
import re
import sqlite3
from datetime import datetime

import pandas as pd

from echeapi import settings


def get_connection(db=settings.DB_FILENAME):
    return sqlite3.connect(db)


def initialize(table=settings.DB_TABLE, connection=None):
    df = pd.DataFrame([], columns=settings.ALL_API_KEYS)
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

    where = []
    params = []

    for key, value in (filter or {}).items():
        if value is None:
            where.append(f'"{key}" IS NULL')
        elif value == '*':
            where.append(f'"{key}" IS NOT NULL')
        elif value.startswith('*') or value.endswith('*'):
            where.append(f'"{key}" LIKE ? COLLATE NOCASE')
            params.append(re.sub(r'\*+', '%', value))
        else:
            where.append(f'"{key}" = ? COLLATE NOCASE')
            params.append(value)

    query = f'SELECT {fields} FROM {table}'
    if where:
        query = f'{query} WHERE {" AND ".join(where)}'

    if connection is None:
        connection = get_connection()

    return pd.read_sql_query(
        con=connection,
        sql=query,
        params=params,
        coerce_float=False,
        parse_dates=settings.DATE_FIELDS,
    )
