
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

        # Clean up the data and normalize ECHE list headers.
        df = eche.normalize(df)

        # Process Erasmus Codes.
        df = erasmus.process(df)
        # Process countries.
        df = country.process(df)

        # Print issues in the console.
        detected = issues.detect_all(df)
        for msg, severity, _df in detected:
            print(f'\n[{severity.upper()}] {msg}\n')
            if not _df.empty:
                print(f'{_df}\n')

        # Attach verified data.
        df = verified.attach(df)

        # Save DataFrame in the database.
        db.save(df)

        print(f'ECHE data loaded to {settings.DB_FILENAME}')
