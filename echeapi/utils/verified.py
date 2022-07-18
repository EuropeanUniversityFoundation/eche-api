
import os

import numpy as np
import pandas as pd

from echeapi import settings
from echeapi.processing import erasmus


def lookup():
    """ Lookup files with verified data.
    """
    fnames = []

    dir = os.path.join(settings.DATA_DIR, settings.VERIFIED_DIR)

    for item in sorted(os.listdir(dir)):
        parts = item.split('.')

        if parts[0] == settings.VERIFIED_PREFIX and parts[-1] == settings.VERIFIED_EXTENSION:
            fnames.append(os.path.join(dir, item))

    return fnames


def load(fname):
    """ Load a file with verified data into a DataFrame with correct headers.
    """
    df = pd.read_csv(fname)

    headers = df.columns.tolist()
    overlap = list(set(headers) & set(settings.REFERENCE_FIELDS.keys()))

    # Check that reference headers are present.
    if overlap != list(set(settings.REFERENCE_FIELDS.keys())):
        raise Exception('Missing reference headers.')

    for field in settings.VERIFIED_FIELDS:
        if field not in headers:
            df[field] = None

    df = df[overlap + settings.VERIFIED_FIELDS].copy()

    return df


def normalize(df):
    """ Format DataFrame content.
    """
    # Strip all strings from whitespace and line characters.
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Nullify empty strings and NaN.
    df.replace('', value=None, inplace=True)
    df.replace({np.nan: None}, inplace=True)

    # Assign string type to all columns
    for key in df.columns.tolist():
        if df[key].dtypes == float:
            df[key] = df[key].apply(int)
        df[key] = df[key].apply(lambda x: x if x is None else str(x))

    # Drop empty rows and columns.
    df.dropna(how='all', axis=0, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)

    return df


def join(df_base, df_verified):
    """ Join a DataFrame with partial data to a base DataFrame.
    """
    # Combine two identifiers to decrease the odds of catching duplicates.
    ref_cols = list(settings.REFERENCE_FIELDS.values())
    id = '|'.join(ref_cols)

    # Create the columns in the DataFrames for comparison.
    for df in [df_base, df_verified]:
        df[id] = df[ref_cols[0]].map(str) + '|' + df[ref_cols[1]].map(str)

    for field in settings.VERIFIED_FIELDS:
        new_field = '.'.join([settings.VERIFIED_KEY, field])
        df_base[new_field] = None

        for i, row in df_verified.iterrows():
            if row[field] is not None:
                df_base.loc[df_base[id] == row[id], new_field] = row[field]

    del df_base[id]

    return df_base


def attach(df_base):
    fnames = lookup()

    for fname in fnames:
        df_verified = load(fname)
        df_verified = normalize(df_verified)
        df_verified = erasmus.process(df_verified)
        df_base = join(df_base, df_verified)

    return df_base
