import pandas as pd
import db

import local_settings

def list(table='eche', fields=[], filter=None):
    query_params = {
        'table': table,
        'fields': fields
    }
    if filter is not None:
        query_params['filter'] = filter

    df = db.sql_to_df(query_params)

    return df.to_json(orient="records", date_format='iso')

def main():
    list()

if __name__ == '__main__':
    main()
