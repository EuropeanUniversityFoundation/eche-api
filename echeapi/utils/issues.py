
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
        df_dups = dups(df, subset=[field])
        df_dups.replace({np.nan: None}, inplace=True)

        if debug:
            if not df_dups.empty:
                print(f'\nDuplicates in {field}')
                print(f'Severity: {severity}\n')
                print(df_dups[settings.UNIQUE_FIELDS.keys()].sort_values(field))
                print()
            else:
                print(f'\nNo duplicates found in {field}.\n')

        issues.append((field, severity, df_dups))

    return issues


def proc(df, original, processed, null=False, debug=False):
    """ Find issues with processed fields.
    """
    issues = []

    processed_col = f'{settings.PROCESSED_KEY}.{processed}'

    df_diff = diff(df, original, processed_col)

    if null:
        severity = 'warning'
        df_null = df_diff[df_diff[processed_col].isnull()].copy()
        df_null.replace({np.nan: None}, inplace=True)


        if debug:
            if not df_null.empty:
                print(f'\nEmpty values in {processed}')
                print(f'Severity: {severity}\n')
                print(df_null)
                print()
            else:
                print(f'\nNo empty values in {processed}.\n')

        return processed, severity, df_null

    else:
        severity = 'info'
        df_processed = df_diff[df_diff[processed_col].notnull()].copy()
        df_processed.replace({np.nan: None}, inplace=True)


        if debug:
            if not df_processed.empty:
                print(f'\nDifferences between {original} and {processed}')
                print(f'Severity: {severity}\n')
                print(df_processed)
                print()
            else:
                print(f'\nNo differences between {original} and {processed}.\n')

        return processed, severity, df_processed


def protocol(df, debug=False):
    issues = unique(df, debug=debug)
    original = 'erasmusCode'
    processed = 'erasmusCodeNormalized'
    issues.append(proc(df, original, processed, debug=debug))
    issues.append(proc(df, original, processed, null=True, debug=debug))

    return issues
