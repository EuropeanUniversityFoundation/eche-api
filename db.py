import os
import sqlite3
import pandas as pd
from datetime import datetime

import local_settings

def init(db_name='test', schema='eche.sql'):
    connection = sqlite3.connect(db_name + '.db')
    c = connection.cursor()

    schema_path = os.path.join(local_settings.schema_dir, schema)
    schema_content = open(schema_path, "r")

    c.execute(schema_content.read())
    connection.commit()

    return connection

def df_to_sql(df, table='eche'):
    connection = init()

    df.to_sql(table, connection, if_exists='replace', index=False)

def sql_to_df(query_params, date_fields=local_settings.date_fields):
    table = query_params['table']

    field_list = [f for f in query_params['fields']]
    fields = ",".join(field_list) if len(field_list) > 0 else "*"

    if 'filter' in query_params:
        key, value = query_params['filter']
        if key in date_fields:
            dt = datetime.fromisoformat(value)
            value = dt.strftime('%Y-%m-%d %H:%M:%S')
        query = f"SELECT {fields} FROM {table} WHERE {key}='{value}';"
        print(query)
    else:
        query = f"SELECT {fields} FROM {table};"
        print(query)

    connection = init()

    df = pd.read_sql_query(query, connection, coerce_float=False, parse_dates=date_fields)

    return df

def fetchall(table='eche', connection=None):
    if connection is None:
        connection = init()

    c = connection.cursor()
    c.execute(f"SELECT * FROM {table};")

    return c.fetchall()

if __name__ == '__main__':
    init()
