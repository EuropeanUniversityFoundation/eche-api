
import os
import sys

from echeapi import settings
from echeapi.processing import country, erasmus
from echeapi.utils import db, eche, issues, verified


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

        if df.empty:
            sys.exit(f'File "{fname}" does not contain any data!')

        # Clean up the data and normalize ECHE list headers.
        eche.normalize(df)

        # Process Erasmus Codes.
        erasmus.process(df)
        # Process countries.
        country.process(df)

        # Print issues in the console.
        detected = [d for d in issues.detect_all(df) if not d[2].empty]
        if detected:
            for msg, severity, _df in detected:
                print(f'\n[{severity.upper()}] {msg}\n\n{_df}\n')
        else:
            print('No issues with data found.')

        # Attach verified data.
        verified.attach(df)

        # Save DataFrame in the database.
        db.save(df)

        print(f'\nLoaded ECHE data from:\n  - {fname}')
        print('\nAttached verified data from:')
        for _fname in verified.lookup():
            print(f'  - {_fname}')
        print(f'\nData loaded to "{settings.DB_FILENAME}"')
