import os
import numpy as np
import pandas as pd
import erasmus
from openpyxl import load_workbook
import db

import local_settings

# Load the first worksheet of an Excel file into a DataFrame.
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

# Clean up whitespace and line characters from a DataFrame.
def clean(df):
    # Strip all strings from whitespace and line characters.
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Nullify certain strings, like formula errors.
    for s in local_settings.eche_null_str:
        df.replace({s: None}, inplace=True)

    return df

# Rename DataFrame headers.
def headers(df, headers_dict=local_settings.eche_headers):
    columns = list(df)

    # Remove whitespace in column names.
    for col in columns:
        if col != col.strip():
            df.rename(columns={col:col.strip()}, inplace=True)

    # Rename columns with machine names.
    df.rename(columns=headers_dict, inplace=True)

# Export a database table to a DataFrame and print it to HTML.
def to_html(table='eche', fields=[], filter=None, table_id='echeTable', classes=None):
    query_params = {
        'table': table,
        'fields': fields
    }
    if filter is not None:
        query_params['filter'] = filter

    df = db.sql_to_df(query_params)

    return df.to_html(
        justify='inherit',
        index=False,
        na_rep='',
        classes=classes,
        table_id=table_id,
        render_links=True
    )

# Main function for this module.
def main():
    # Load the ECHE list data into a DataFrame.
    df = load()
    # Clean up the data.
    df = clean(df)
    # Replace the ECHE list headers with the corresponding API keys.
    headers(df)
    # Process Erasmus Codes.
    df = erasmus.protocol(df)

    return df

if __name__ == '__main__':
    df = main()

    print(df.tail())
