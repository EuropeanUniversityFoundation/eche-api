
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

    # Get the headers from the first line of data.
    columns = next(sheet_data)

    # Create a DataFrame based on the subsequent lines of data.
    df = pd.DataFrame(sheet_data, columns=columns)

    # Drop empty rows and columns.
    df.dropna(how='all', axis=0, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)

    return df


def clean_values(df):
    """ Clean up whitespace and line characters from a DataFrame.
    """
    # Strip all strings from whitespace and line characters.
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Nullify certain strings, like formula errors.
    df.replace(settings.ECHE_NULL_STR, value=None, inplace=True)

    return df


def replace_headers(df):
    """ Rename DataFrame headers.
    """
    # Remove whitespace in column names.
    df.rename(columns=lambda c: c.strip(), inplace=True)

    # Rename columns with machine names.
    df.rename(columns=settings.ECHE_FIELDS, inplace=True)

    return df


def normalize(df):
    df = clean_values(df)
    df = replace_headers(df)
    return df
