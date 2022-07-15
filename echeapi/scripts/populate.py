
import os
import sys

import numpy as np

from echeapi import settings
from echeapi.processing import country, erasmus
from echeapi.utils import db, eche


def main(*args):
    if args:
        fname = os.path.abspath(args[0])
    else:
        fname = settings.DATA_FILENAME

    if not os.path.isfile(fname):
        sys.exit(f'File not found: {fname}')
    else:
        # Load the ECHE list data into a DataFrame.
        df = eche.load(fname)

        # Clean up the data and normalize ECHE list headers.
        df = eche.normalize(df)

        # Process Erasmus Codes.
        df = erasmus.process(df)
        # Process countries.
        df = country.process(df)

        # Print duplicated values in unique fields.
        for field, severity in settings.UNIQUE_FIELDS.items():
            print(f'\nDuplicates in {field}')
            print(f'Severity: {severity}\n')
            df_dups = df[df.duplicated([field], keep=False)].copy()
            df_dups.replace({None: np.nan}, inplace=True)
            df_dups.dropna(subset=[field], inplace=True)
            if not df_dups.empty:
                print(df_dups[settings.UNIQUE_FIELDS.keys()].sort_values(field))
                print()
            else:
                print(f'No duplicates found.\n')

        # Save DataFrame in the database.
        db.save(df)

        print(f'ECHE data loaded to {settings.DB_FILENAME}')
