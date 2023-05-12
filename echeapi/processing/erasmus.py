"""
Handle Erasmus codes.

Erasmus codes for HEIs follow a naming convention that can be misinterpreted.
The first 3 characters correspond to a country code and a space filler, when
  needed; the country code can be 1, 2 or 3 characters long.
In some cases, found in production applications, this rule is not followed.
As such, it is necessary to check whether the Erasmus code is properly
  formatted with the correct number of spaces.
"""

import unicodedata

from echeapi import settings

# 3-letter country codes have no trailing spaces, so they must be defined.
KNOWN_3_LETTER = ['LUX', 'IRL']

# Column names, as API keys.
COL_REF = 'erasmusCode'
COL_NORM = 'erasmusCodeNormalized'
COL_PREFIX = 'erasmusCodePrefix'
COL_CITY = 'erasmusCodeCity'
COL_NUMBER = 'erasmusCodeNumber'
COL_CC = 'erasmusCodeCountryCode'
COL_CC_ISO = 'erasmusCodeCountryCodeIso'

# Match the known prefixes in Erasmus codes to country codes.
PREFIX_CC = {
    'A': 'AT',
    'B': 'BE',
    'D': 'DE',
    'E': 'ES',
    'SF': 'FI',
    'F': 'FR',
    'G': 'EL',
    'IRL': 'IE',
    'I': 'IT',
    'LUX': 'LU',
    'N': 'NO',
    'P': 'PT',
    'S': 'SE',
}


def normalize(row, col=COL_REF, empty=''):
    """ Normalize Erasmus Codes.
    """
    item = row[col]

    code = item.strip() if item else ''

    valid = False
    while not valid:
        # Erasmus codes are all uppercase.
        code = code.upper()
        # Assume the code is valid before the checks.
        valid = True

        # Check if the code is empty.
        if valid and code == '':
            valid = False

        # Check if the first character is a letter.
        if valid and not code[0].isalpha():
            valid = False

        # Check if the first three characters are either known or contain a space.
        if valid and not (' ' in code[0:3] or code[0:3] in KNOWN_3_LETTER):
            valid = False

        # Check if the last two characters are numbers.
        if valid and not code[-2:].isdigit():
            # It is possible to fix a single digit by prepending a zero.
            if code[-1].isdigit():
                code = code[:-1] + '0' + code[-1]
            else:
                valid = False

        # If no errors were found at this point, do some cleaning.
        if valid:
            # Check if the 2nd character is a space, meaning a 1-letter country code.
            if code[1:2].isspace():
                # Impose a second space for 1-letter codes, remove whitespace from the rest.
                code = code[0:2] + ' ' + code[2:].strip()

            # Check if the 2nd character is a letter and the 3rd character is a space.
            if code[1:2].isalpha() and code[2:3].isspace():
                # Remove whitespace from the rest.
                code = code[0:2] + ' ' + code[3:].strip()

            # Check if the first characters are a known 3-letter country ID.
            if code[0:3] in KNOWN_3_LETTER:
                code = code[0:3] + code[3:].strip()

            # Replace any special characters in the middle of the code with a dash.
            special_chars = [" ", "."]
            for char in special_chars:
                if code[3:].find(char) > -1:
                    code_parts = code[3:].split(char)
                    # Handle repeated characters.
                    code_parts = [part for part in code_parts if part != '']
                    # Remove the character entirely if the last part has only digits.
                    if code_parts[-1].isdigit():
                        code_parts[-2] += code_parts[-1]
                        del code_parts[-1]
                    # Reassemble the parts.
                    code = code[0:3] + "-".join(code_parts)

            # # Check the length of the code after the cleaning.
            # if code[-3:].isdigit():
            #     code_txt = code[:-3]
            #     code_no = code[-3:]
            # else:
            #     code_txt = code[:-2]
            #     code_no = code[-2:]
            # # Truncate the text component at 10 characters.
            # code = code_txt[:10] + code_no

        # Handle invalid codes
        if not valid:
            code = empty
            valid = True

    return code


def get_prefix(row, col=COL_NORM):
    """ Extract NA prefix from normalized Erasmus code.
    """
    item = row[col]
    return item[0:3].strip() if item else ''


def get_city(row, col=COL_NORM):
    """ Extract city component from normalized Erasmus code.
    """
    item = row[col]
    return ''.join([i for i in item[3:] if not i.isdigit()]) if item else ''


def get_number(row, col=COL_NORM):
    """ Extract number from normalized Erasmus code.
    """
    item = row[col]
    return ''.join(filter(lambda i: i.isdigit(), item)) if item else ''


def get_cc(row, col=COL_PREFIX):
    """ Extract country code from prefix.
    """
    item = row[col]
    return PREFIX_CC.get(item, item)


def process(df):
    """ Complete processing.
    """
    # Unicode normalization.
    df[COL_REF] = df[COL_REF].apply(lambda x: unicodedata.normalize('NFKC', x) if isinstance(x, str) else x)

    # Store normalized Erasmus Codes in new column.
    df[COL_NORM] = df.apply(lambda row: normalize(row), axis=1)

    # Store prefixes from normalized Erasmus Codes in new column.
    df[COL_PREFIX] = df.apply(lambda row: get_prefix(row), axis=1)

    # Store city components from normalized Erasmus Codes in new column.
    df[COL_CITY] = df.apply(lambda row: get_city(row), axis=1)

    # Store numbers from normalized Erasmus Codes in new column.
    df[COL_NUMBER] = df.apply(lambda row: get_number(row), axis=1)

    # Store country codes from prefixes in new column.
    df[COL_CC] = df.apply(lambda row: get_cc(row), axis=1)

    # Duplicate the country code column.
    df[COL_CC_ISO] = df.loc[:, COL_CC]
    # Replace country codes with ISO 3166-1 alpha-2 country codes.
    df[COL_CC_ISO].replace(settings.COUNTRY_CODES_TO_ISO_MAP, inplace=True)

    # Nullify empty strings.
    df.replace('', value=None, inplace=True)
