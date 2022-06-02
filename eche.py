import os.path
import numpy as np
import pandas as pd
from openpyxl import load_workbook

import local_settings

def load():
    eche_xlsx = os.path.join(local_settings.data_dir, local_settings.eche_xlsx)

    # Load the Excel file
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

def main():
    # Load the ECHE list data into a DataFrame.
    df = load()

if __name__ == '__main__':
    main()
