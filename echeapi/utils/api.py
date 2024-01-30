
import json

from echeapi import settings
from echeapi.utils import db, nesting


def as_dataframe(fields, filter=None):
    """ Export a database table to a DataFrame.
    """
    df = db.fetch(fields=fields, filter=filter)
    df = df[fields]

    for field in settings.DATE_FIELDS:
        if field in df.columns:
            df[field] = df[field].dt.strftime('%Y-%m-%d')

    _verified = 'hasVerifiedData'
    if _verified in fields:
        df[_verified] = df[_verified].astype('bool')

    return df


def as_dict(fields, filter=None, **kwargs):
    """ Export a database table to a DataFrame and return it as dict.
    """
    df = as_dataframe(fields, filter=filter)

    data = df.to_dict(orient='records')

    if kwargs.get('nested', False):
        data = nesting.process(data)

    return data


def as_json(fields, filter=None, **kwargs):
    """ Export a database table to a DataFrame and return it in JSON format.
    """
    data = as_dict(fields, filter=filter, **kwargs)
    return json.dumps(data, ensure_ascii=False)


def as_html(fields, filter=None, **kwargs):
    """ Export a database table to a DataFrame and print it to HTML.
    """
    df = as_dataframe(fields, filter=filter)

    return df.to_html(
        justify='inherit',
        index=False,
        na_rep='',
        render_links=True,
        **kwargs,
    )
