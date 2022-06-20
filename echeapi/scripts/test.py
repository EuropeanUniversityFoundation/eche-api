
import random

import pandas as pd

from echeapi.processing import country, erasmus
from echeapi.utils import api, doctree


def main(*args):
    if not args or args[0] not in TESTS:
        print(f'Invalid test. Try one of: {", ".join(TESTS.keys())}')
    else:
        TESTS[args[0]]()


def test_doctree():
    print("Docs\n")
    menu = doctree.tree()
    print(menu)


def test_api():
    api.list()


def test_erasmus():
    mock_codes = [
        'BCITY01',           # faulty, missing spaces
        'B CITY01',          # faulty, missing space
        'B  CITY01',         # correct
        'B   CITY01',        # faulty, extra spaces
        ' B  CITY01',        # faulty, does not start with a letter
        'NLCITY01',          # faulty, missing space
        '1NL CITY01',        # faulty, starts with number
        'NL CITY01',         # correct
        'NL CITY101',        # correct
        'NL City01',         # faulty, not all uppercase
        'NL  CITY01',        # faulty, extra space
        'LUCITY01',          # faulty, chopped country code
        'LUXCITY01',         # correct
        'LUXGRAND-DUCHY01',  # faulty, text component is too long
        'LUXCITY01 ',        # faulty, trailing space
        'LUX CITY01',        # faulty, extra space
        'LUX  CITY01',       # faulty, extra spaces
    ]

    df = pd.DataFrame({erasmus.col_ref: mock_codes})

    print('Erasmus code processing\n')

    print('This script will load and normalize some mock Erasmus codes.')
    print('Some codes are valid, while others have formatting errors.')
    print('If an error is recoverable, it is handled quietly.')
    print('If an error is NOT recoverable, an empty string will be stored.')

    input("\nPress Enter to see the mock codes...")

    print()
    print(df)

    input("\nPress Enter to see the normalized codes...")

    df = erasmus.process(df)

    print()
    print(df[df[erasmus.col_norm] != ''])

    input("\nPress Enter to see the unrecoverable codes...")

    print()
    print(df[df[erasmus.col_norm] == ''])


def test_country():
    countries = []
    for i in range(10):
        _country = random.choice(list(country.cc_country.values()))
        countries.append(_country)

    df = pd.DataFrame({country.col_ref: countries})

    print('Country code processing\n')

    print('This script will load random countries and get their country codes.')

    input("\nPress Enter to see the countries...")

    print()
    print(df)

    input("\nPress Enter to see the country codes...")

    df = country.process(df)

    print()
    print(df)


TESTS = {t[5:]: f for t, f in vars().items() if t.startswith('test_')}
