import os
import sqlite3

import local_settings

def init(db_name='test', schema='eche.sql'):
    connection = sqlite3.connect(db_name + '.db')
    c = connection.cursor()

    schema_path = os.path.join(local_settings.schema_dir, schema)
    schema_content = open(schema_path, "r")

    c.execute(schema_content.read())
    connection.commit()

    return connection

def df_to_sql(df, table='eche', connection=None):
    if connection is None:
        connection = init()

    df.to_sql(table, connection, if_exists='replace', index=False)

if __name__ == '__main__':
    init()
