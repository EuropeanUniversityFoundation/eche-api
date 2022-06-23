
import sqlite3

import pandas as pd

from echeapi import settings


def init():
    connection = sqlite3.connect(settings.DB_FILENAME)
    cursor = connection.cursor()

    with open(settings.SCHEMA_FILENAME) as f:
        schema_content = f.read()

    cursor.execute(schema_content)
    connection.commit()

    return connection


def save(df, connection=None):
    if connection is None:
        connection = init()
    df.to_sql(settings.DB_TABLE, connection, if_exists='replace', index=False)


def fetch(fields=None, filter=None, table=settings.DB_TABLE, connection=None):
    fields = ",".join(fields) if fields else "*"

    if filter is not None:
        key, value = filter
        if value is None:
            query = f"SELECT {fields} FROM {table} WHERE {key} IS NULL"
            params = ()
        else:
            query = f"SELECT {fields} FROM {table} WHERE {key} = ?"
            params = (value,)
    else:
        query = f"SELECT {fields} FROM {table}"
        params = ()

    if connection is None:
        connection = init()

    return pd.read_sql_query(
        con=connection,
        sql=query,
        params=params,
        coerce_float=False,
        parse_dates=settings.DATE_FIELDS,
    )


def fetchall(table=settings.DB_TABLE, connection=None):
    if connection is None:
        connection = init()

    c = connection.cursor()
    c.execute(f"SELECT * FROM {table}")

    return c.fetchall()
