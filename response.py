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

    for field in local_settings.date_fields:
        df[field] = df[field].dt.strftime('%Y-%m-%d')

    return df.to_json(orient="records")

def main():
    list()

if __name__ == '__main__':
    main()
