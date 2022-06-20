
from echeapi import settings
from echeapi.processing import country, erasmus
from echeapi.utils import db, eche


def main(*args):
    # Load the ECHE list data into a DataFrame.
    df = eche.load()
    # Clean up the data.
    df = eche.clean(df)
    # Replace the ECHE list headers with the corresponding API keys.
    eche.headers(df)
    # Process Erasmus Codes.
    df = erasmus.process(df)
    # Process countries.
    df = country.process(df)

    db.df_to_sql(df)

    print(f'DataFrame loaded to {settings.db_filename}')
