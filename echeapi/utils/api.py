
from echeapi import settings
from echeapi.utils import db


def list(table='eche', fields=None, filter=None):
    query_params = {
        'table': table,
        'fields': fields or [],
    }
    if filter is not None:
        query_params['filter'] = filter

    df = db.sql_to_df(query_params)

    for field in settings.date_fields:
        if field in df.columns:
            df[field] = df[field].dt.strftime('%Y-%m-%d')

    return df.to_json(orient="records")


def main():
    list()


if __name__ == '__main__':
    main()
