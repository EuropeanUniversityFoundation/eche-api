
import numpy as np

from echeapi import settings


def detect_duplicates(df):
    """ Find issues with duplicates in unique fields.
    """
    issues = []

    for field, severity in settings.UNIQUE_FIELDS.items():
        df_dups = df[df.duplicated([field], keep=False)].copy()
        df_dups.replace({None: np.nan}, inplace=True)
        df_dups.dropna(subset=[field], inplace=True)
        df_dups.replace({np.nan: None}, inplace=True)
        df_dups = df_dups[settings.UNIQUE_FIELDS.keys()].sort_values(field)

        if not df_dups.empty:
            msg = f'Duplicates found in "{field}".'
        else:
            msg = f'No duplicates found in "{field}".'
            severity = 'success'

        issues.append((msg, severity, df_dups))

    return issues


def detect_empty(df, field):
    """ Find issues with empty values in field.
    """
    df_null = df[df[field].isnull()].copy()
    df_null.replace({np.nan: None}, inplace=True)

    if not df_null.empty:
        msg = f'Empty values in "{field}".'
        severity = 'warning'
    else:
        msg = f'No empty values in "{field}".'
        severity = 'success'

    return msg, severity, df_null


def detect_different(df, first, second):
    """ Find issues with differences between two fields.
    """
    df_diff = df[[first, second]].copy()
    df_diff = df_diff[df_diff[first] != df_diff[second]]
    df_diff = df_diff[df_diff[second].notnull()]
    df_diff.replace({np.nan: None}, inplace=True)

    if not df_diff.empty:
        msg = f'Differences between "{first}" and "{second}".'
        severity = 'info'
    else:
        msg = f'No differences between "{first}" and "{second}".'
        severity = 'success'

    return msg, severity, df_diff


def detect_all(df):
    _field = f'{settings.PROCESSED_KEY}.erasmusCodeNormalized'
    return [
        *detect_duplicates(df),
        detect_different(df, 'erasmusCode', _field),
        detect_empty(df, _field),
    ]
