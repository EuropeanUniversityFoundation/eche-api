
import numpy as np

from echeapi import settings


def dups(df, subset=None):
    """ Extract the duplicated values in a DataFrame subset.
    """
    df_dups = df[df.duplicated(subset, keep=False)].copy()
    df_dups.replace({None: np.nan}, inplace=True)
    df_dups.dropna(subset=subset, inplace=True)

    return df_dups


def diff(df, first, second):
    """ Find differences between DataFrame columns.
    """
    df_redux = df[[first, second]].copy()
    df_diff = df_redux[df_redux[first] != df_redux[second]].copy()

    return df_diff


def unique(df, debug=False):
    """ Find issues with unique fields.
    """
    issues = []

    for field, severity in settings.UNIQUE_FIELDS.items():
        issue_msg = f'Duplicates found in \"{field}\".'
        clean_msg = f'No duplicates found in \"{field}\".'

        df_dups = dups(df, subset=[field])
        df_dups.replace({np.nan: None}, inplace=True)
        df_dups = df_dups[settings.UNIQUE_FIELDS.keys()].sort_values(field).copy()

        if not df_dups.empty:
            msg = issue_msg

            if debug:
                print(f'\n{issue_msg}')
                print(f'Severity: {severity}\n')
                print(df_dups)
        else:
            msg = clean_msg
            severity = 'success'

            if debug:
                print(f'\n{clean_msg}')

        issues.append((msg, field, severity, df_dups))

    return issues


def proc(df, original, processed, null=False, debug=False):
    """ Find issues with processed fields.
    """
    df_diff = diff(df, original, processed)

    if null:
        issue_msg = f'Empty values in \"{processed}\".'
        clean_msg = f'No empty values in \"{processed}\".'

        severity = 'warning'

        df_null = df_diff[df_diff[processed].isnull()].copy()
        df_null.replace({np.nan: None}, inplace=True)

        if not df_null.empty:
            msg = issue_msg

            if debug:
                print(f'\n{issue_msg}')
                print(f'Severity: {severity}\n')
                print(df_null)
        else:
            msg = clean_msg
            severity = 'success'

            if debug:
                print(f'\n{clean_msg}')

        return msg, processed, severity, df_null

    else:
        issue_msg = f'Differences between \"{original}\" and \"{processed}\".'
        clean_msg = f'No differences between \"{original}\" and \"{processed}\".'

        severity = 'info'

        df_processed = df_diff[df_diff[processed].notnull()].copy()
        df_processed.replace({np.nan: None}, inplace=True)

        if not df_processed.empty:
            msg = issue_msg

            if debug:
                print(f'\n{issue_msg}')
                print(f'Severity: {severity}\n')
                print(df_processed)
        else:
            msg = clean_msg
            severity = 'success'

            if debug:
                print(f'\n{clean_msg}')

        return msg, processed, severity, df_processed


def protocol(df, debug=False):
    issues = unique(df, debug=debug)
    original = 'erasmusCode'
    processed = f'{settings.PROCESSED_KEY}.erasmusCodeNormalized'
    issues.append(proc(df, original, processed, debug=debug))
    issues.append(proc(df, original, processed, null=True, debug=debug))

    return issues
