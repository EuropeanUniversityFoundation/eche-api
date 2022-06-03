import os
import numpy as np
import pandas as pd
from openpyxl import load_workbook
import db

import local_settings

def load():
    eche_xlsx = os.path.join(local_settings.data_dir, local_settings.eche_xlsx)

    # Load the Excel file.
    workbook = load_workbook(eche_xlsx, data_only=True)

    # Load the first worksheet.
    idx, sheet = next(enumerate(workbook.worksheets))
    sheet_data = sheet.values

    # Get the headers from the first line of data.
    columns = next(sheet_data)[0:]

    # Create a DataFrame based on the subsequent lines of data.
    df = pd.DataFrame(sheet_data, columns=columns)

    # Drop empty rows and columns.
    df.dropna(how='all', axis=0, inplace=True)
    df.dropna(how='all', axis=1, inplace=True)

    return df

def clean(df):
    # Strip all strings from whitespace and line characters.
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Nullify certain strings, like formula errors.
    for s in local_settings.eche_null_str:
        df.replace({s: None}, inplace=True)

    return df

def headers(df, headers_dict=local_settings.eche_headers):
    columns = list(df)

    # Remove whitespace in column names.
    for col in columns:
        if col != col.strip():
            df.rename(columns={col:col.strip()}, inplace=True)

    # Rename columns with machine names.
    df.rename(columns=headers_dict, inplace=True)

def main():
    # Load the ECHE list data into a DataFrame.
    df = load()
    # Clean up the data.
    df = clean(df)
    # Replace the ECHE list headers with the corresponding API keys.
    headers(df)

    return df

def print(classes=None):
    df = db.sql_to_df()

    return df.to_html(
        justify='inherit',
        index=False,
        na_rep='',
        classes=classes,
        table_id='echeTable',
        render_links=True
    )

if __name__ == '__main__':
    df = main()
    # connection = db.init()
    db.df_to_sql(df)
