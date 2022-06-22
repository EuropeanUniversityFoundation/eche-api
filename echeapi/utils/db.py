
import os
import sqlite3
from datetime import datetime

import pandas as pd

from echeapi import settings


def init(db_filename=settings.DB_FILENAME, schema=settings.SCHEMA_FILENAME):
    connection = sqlite3.connect(db_filename)
    c = connection.cursor()

    schema_path = os.path.join(settings.SCHEMA_DIR, schema)
    with open(schema_path, "r") as f:
        schema_content = f.read()

    c.execute(schema_content)
    connection.commit()

    return connection


def df_to_sql(df, table=settings.DB_TABLE):
    connection = init()
    df.to_sql(table, connection, if_exists='replace', index=False)


def sql_to_df(query_params, date_fields=settings.DATE_FIELDS):
    table = query_params['table']

    field_list = [f for f in query_params['fields']]
    fields = ",".join(field_list) if field_list else "*"

    if 'filter' in query_params:
        key, value = query_params['filter']
        if value is None:
            query = f"SELECT {fields} FROM {table} WHERE {key} IS NULL;"
            params = ()
        else:
            if key in date_fields:
                dt = datetime.fromisoformat(value)
                value = dt.strftime('%Y-%m-%d %H:%M:%S')
            query = f"SELECT {fields} FROM {table} WHERE {key} = ?;"
            params = (value,)
    else:
        query = f"SELECT {fields} FROM {table};"
        params = ()

    connection = init()

    df = pd.read_sql_query(query, connection, coerce_float=False, parse_dates=date_fields, params=params)

    return df


def fetchall(table='eche', connection=None):
    if connection is None:
        connection = init()

    c = connection.cursor()
    c.execute(f"SELECT * FROM {table};")

    return c.fetchall()
