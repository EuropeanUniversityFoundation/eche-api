import pandas as pd

# Handle Erasmus codes.
#
# Erasmus codes for HEIs follow a naming convention that can be misinterpreted.
# The first 3 characters correspond to a country code and a space filler, when
#   needed; the country code can be 1, 2 or 3 characters long.
# In some cases, found in production applications, this rule is not followed.
# As such, it is necessary to check whether the Erasmus code is properly
#   formatted with the correct number of spaces.

# 3 letter country codes have no trailing spaces, so they must be defined.
known3letter = ['LUX', 'IRL']

# Column names, as API keys.
col_ref = 'erasmusCode'
col_norm = 'erasmusCodeNormalized'
col_na = 'erasmusCodePrefix'
col_cc = 'erasmusCodeCountryCode'

# Match the known prefixes in Erasmus codes to ISO 3166 country codes.
prefix_cc = {
    'A':    'AT',
    'B':    'BE',
    'D':    'DE',
    'E':    'ES',
    'SF':   'FI',
    'F':    'FR',
    'G':    'GR',
    'IRL':  'IE',
    'I':    'IT',
    'LUX':  'LU',
    'N':    'NO',
    'P':    'PT',
    'S':    'SE'
}

# Normalize Erasmus Codes.
def normalize(row, ref_col=col_ref, empty=''):
    item = row[ref_col]

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
        if valid and not (' ' in code[0:3] or code[0:3] in known3letter):
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
            # Check if the 2nd character is a space, meaning a 1 letter country code.
            if code[1:2].isspace():
                # Impose a second space for 1 letter codes, remove whitespace from the rest.
                code = code[0:2] + ' ' + code[2:].strip()

            # Check if the 2nd character is a letter and the 3rd character is a space.
            if code[1:2].isalpha() and code[2:3].isspace():
                # Remove whitespace from the rest.
                code = code[0:2] + ' ' + code[3:].strip()

            # Check if the first characters are a known 3 letter country ID.
            if code[0:3] in known3letter:
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

            # Check the length of the code after the cleaning.
            if code[-3:].isdigit():
                code_txt = code[:-3]
                code_no = code[-3:]
            else:
                code_txt = code[:-2]
                code_no = code[-2:]
            # Truncate the text component at 10 characters.
            # code = code_txt[:10] + code_no

        # Handle invalid codes
        if not valid:
            code = empty
            valid = True

    return code

# Extract NA prefix from Erasmus code.
def get_prefix(row, ref_col=col_norm):
    item = row[ref_col]

    prefix = item[0:3].strip() if item else ''

    return prefix

# Extract country code from prefix.
def get_cc(row, ref_col=col_na):
    item = row[ref_col]

    cc = prefix_cc[item] if item in prefix_cc else item

    return cc

# Complete processing.
def process(df):
    # Store normalized Erasmus Codes in new column.
    df[col_norm] = df.apply(lambda row: normalize(row), axis=1)

    # Store prefixes from normalized Erasmus Codes in new column.
    df[col_na] = df.apply(lambda row: get_prefix(row), axis=1)

    # Store country codes from prefixes in new column.
    df[col_cc] = df.apply(lambda row: get_cc(row), axis=1)

    return df

# Main function: run `python erasmus.py` in the console.
def main():
    mock_codes = [
        'BCITY01',          # faulty, missing spaces
        'B CITY01',         # faulty, missing space
        'B  CITY01',        # correct
        'B   CITY01',       # faulty, extra spaces
        ' B  CITY01',       # faulty, does not start with a letter
        'NLCITY01',         # faulty, missing space
        '1NL CITY01',       # faulty, starts with number
        'NL CITY01',        # correct
        'NL CITY101',       # correct
        'NL City01',        # faulty, not all uppercase
        'NL  CITY01',       # faulty, extra space
        'LUCITY01',         # faulty, chopped country code
        'LUXCITY01',        # correct
        'LUXGRAND-DUCHY01', # faulty, text component is too long
        'LUXCITY01 ',       # faulty, trailing space
        'LUX CITY01',       # faulty, extra space
        'LUX  CITY01'       # faulty, extra spaces
    ]

    df = pd.DataFrame({col_ref: mock_codes})

    print('Erasmus code testing\n')

    print('This script will load some mock Erasmus codes.')
    print('Some codes are valid, while others have formatting errors.')
    print('If an error is recoverable, it is handled quietly.')
    print('If an error is NOT recoverable, a replacement is required.')
    print('If a replacement is provided beforehand, it will NOT be checked.')
    print('e.g. provide a replacement code like XX EMPTY00')
    print('If no replacement is provided beforehand, user input is required.')
    print('Unlike the preset replacement, user input will be checked.')
    print('The check will be stuck until user input is valid or recoverable.')

    input("\nPress Enter to see the mock codes...")

    print()
    print(df)

    input("\nPress Enter to normalized codes...")

    df = process(df)

    print()
    print(df[df[col_norm] != ''])

    input("\nPress Enter to unrecoverable codes...")

    print()
    print(df[df[col_norm] == ''])

if __name__ == '__main__':
    main()
