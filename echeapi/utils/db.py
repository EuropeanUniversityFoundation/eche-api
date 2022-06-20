
import os
import sqlite3
from datetime import datetime

import pandas as pd

from echeapi import settings


def init(db_filename=settings.db_filename, schema=settings.schema_filename):
    connection = sqlite3.connect(db_filename)
    c = connection.cursor()

    schema_path = os.path.join(settings.schema_dir, schema)
    schema_content = open(schema_path, "r")

    c.execute(schema_content.read())
    connection.commit()

    return connection


def df_to_sql(df, table=settings.db_table):
    connection = init()
    df.to_sql(table, connection, if_exists='replace', index=False)


def sql_to_df(query_params, date_fields=settings.date_fields):
    table = query_params['table']

    field_list = [f for f in query_params['fields']]
    fields = ",".join(field_list) if len(field_list) > 0 else "*"

    if 'filter' in query_params:
        key, value = query_params['filter']
        if value is None:
            query = f"SELECT {fields} FROM {table} WHERE {key} IS NULL;"
        else:
            if key in date_fields:
                dt = datetime.fromisoformat(value)
                value = dt.strftime('%Y-%m-%d %H:%M:%S')
            query = f"SELECT {fields} FROM {table} WHERE {key}='{value}';"
    else:
        query = f"SELECT {fields} FROM {table};"

    connection = init()

    df = pd.read_sql_query(query, connection, coerce_float=False, parse_dates=date_fields)

    return df


def fetchall(table='eche', connection=None):
    if connection is None:
        connection = init()

    c = connection.cursor()
    c.execute(f"SELECT * FROM {table};")

    return c.fetchall()
