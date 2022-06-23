
from echeapi import settings
from echeapi.utils import db


def as_json(fields=None, filter=None):
    """ Export a database table to a DataFrame and return it in JSON format.
    """
    df = db.fetch(fields=fields, filter=filter)
    df = df[fields if fields else settings.DATA_FIELDS]

    for field in settings.DATE_FIELDS:
        if field in df.columns:
            df[field] = df[field].dt.strftime('%Y-%m-%d')

    return df.to_json(orient="records")


def as_html(fields=None, filter=None, **kwargs):
    """ Export a database table to a DataFrame and print it to HTML.
    """
    df = db.fetch(fields=fields, filter=filter)
    df = df[settings.DATA_FIELDS]

    return df.to_html(
        justify='inherit',
        index=False,
        na_rep='',
        render_links=True,
        **kwargs,
    )
