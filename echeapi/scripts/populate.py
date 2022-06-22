
import os

from echeapi import settings
from echeapi.processing import country, erasmus
from echeapi.utils import db, eche


def main(*args):
    if args:
        fname = os.path.abspath(args[0])
    else:
        fname = os.path.join(settings.DATA_DIR, settings.DATA_FILENAME)

    if not os.path.isfile(fname):
        print(f'File not found: {fname}')
    else:
        # Load the ECHE list data into a DataFrame.
        df = eche.load(fname)
        # Clean up the data.
        df = eche.clean(df)
        # Replace the ECHE list headers with the corresponding API keys.
        eche.headers(df)
        # Process Erasmus Codes.
        df = erasmus.process(df)
        # Process countries.
        df = country.process(df)

        db.df_to_sql(df)

        print(f'ECHE data loaded to {settings.DB_FILENAME}')
