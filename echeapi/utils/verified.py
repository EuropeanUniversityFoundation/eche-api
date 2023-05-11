
import os

import pandas as pd

from echeapi import settings
from echeapi.processing import erasmus
from echeapi.utils import eche


def lookup():
    """ Lookup files with verified data.
    """
    fnames = []
    for item in sorted(os.listdir(settings.VERIFIED_DIR)):
        if '.' in item:
            parts = item.split('.')
            if parts[0] == settings.VERIFIED_PREFIX and parts[-1] == settings.VERIFIED_EXTENSION:
                fnames.append(os.path.join(settings.VERIFIED_DIR, item))
    return fnames


def load(fname):
    """ Load a file with verified data into a DataFrame with correct headers.
    """
    df = pd.read_csv(fname)

    headers = set(df.columns.tolist())
    ref_cols = set(settings.REFERENCE_FIELDS.keys())

    # Check that all reference headers are present.
    if not ref_cols.issubset(headers):
        raise KeyError(f'Missing reference headers: {", ".join(ref_cols - headers)}')

    for field in settings.VERIFIED_FIELDS:
        if field not in headers:
            df[field] = None

    return df[[*ref_cols, *settings.VERIFIED_FIELDS]].copy()


def normalize(df):
    """ Format DataFrame content.
    """
    eche.clean_values(df)
    eche.reduce(df)
    eche.assign_types(df)


def join(df_base, df_verified):
    """ Join a DataFrame with partial data to a base DataFrame.
    """
    # Combine two identifiers to decrease the odds of catching duplicates.
    ref_cols = list(settings.REFERENCE_FIELDS.values())
    id = '|'.join(ref_cols)

    # Create the columns in the DataFrames for comparison.
    for df in [df_base, df_verified]:
        df[id] = ''
        for _col in ref_cols:
            df[id] = df[id] + '|' + df[_col].map(str)

    for field in settings.VERIFIED_FIELDS:
        new_field = f'{settings.VERIFIED_KEY}.{field}'
        df_base[new_field] = None

        for i, row in df_verified.iterrows():
            if row[field] is not None:
                df_base.loc[df_base[id] == row[id], new_field] = row[field]
                df_base.loc[df_base[id] == row[id], 'hasVerifiedData'] = True

    for df in [df_base, df_verified]:
        del df[id]


def attach(df_base):
    for fname in lookup():
        df_verified = load(fname)
        if not df_verified.empty:
            normalize(df_verified)
            erasmus.process(df_verified)
            join(df_base, df_verified)
