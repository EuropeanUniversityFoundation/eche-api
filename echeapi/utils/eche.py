
import datetime

import numpy as np
import pandas as pd
from openpyxl import load_workbook

from echeapi import settings


def load(fname=settings.DATA_FILENAME):
    """ Load the first worksheet of an Excel file into a DataFrame.
    """
    # Load the Excel file.
    workbook = load_workbook(fname, data_only=True)

    # Load the first worksheet.
    sheet = next(iter(workbook.worksheets))
    sheet_data = sheet.values

    # Get the headers from the first non empty line of data.
    valid_columns = []
    while not valid_columns:
        columns = next(sheet_data)
        valid_columns = [c for c in columns if c]

    # Create a DataFrame based on the subsequent lines of data.
    return pd.DataFrame(sheet_data, columns=columns)


def replace_headers(df):
    """ Rename DataFrame headers.
    """
    # Remove whitespace in column names.
    df.rename(columns=lambda c: c.strip() if isinstance(c, str) else c, inplace=True)

    # Rename columns with machine names.
    df.rename(columns=settings.ECHE_HEADERS_MAP, inplace=True)

    # Drop unrecognized columns.
    df.drop(columns=df.columns.difference(settings.ECHE_HEADERS_MAP.values()), inplace=True)


def clean_values(df):
    """ Clean up whitespace and line characters from a DataFrame.
    """
    # Strip all strings from whitespace and line characters.
    for col in df.columns.tolist():
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

    # Nullify certain strings, like formula errors.
    df.replace(settings.ECHE_NULL_STR, value=None, inplace=True)

    # Nullify empty strings.
    df.replace('', value=None, inplace=True)


def reduce(df):
    """Drop empty rows.
    """
    df.dropna(axis=0, how='all', inplace=True)


def assign_types(df):
    """ Assign string type to all columns except dates.
    """
    # Nullify NaN.
    df.replace(np.nan, value=None, inplace=True)

    for col in df.columns.tolist():
        if col in settings.DATE_FIELDS:
            continue
        # Convert float to int before converting to string.
        if df[col].dtypes == float:
            df[col] = df[col].apply(int)
        df[col] = df[col].apply(lambda x: x if x is None else str(x))


def set_datetime(df):
    """ Convert strings with dates into datetime type.
    """
    for col in df.columns.tolist():
        if col in settings.DATE_FIELDS:
            # Isolate the strings in datetime column.
            df_str = df[df[col].apply(lambda x: isinstance(x, str))]
            for i, row in df_str.iterrows():
                df.iloc[i][col] = datetime.datetime.strptime(row[col], settings.DATE_FORMAT)


def normalize(df):
    replace_headers(df)
    clean_values(df)
    reduce(df)
    assign_types(df)
    set_datetime(df)
