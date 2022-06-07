# Importing the ECHE list

This application imports the ECHE list from a `.xslx` file, as published by DGEAC.

## Source file

The source file is taken from the [Erasmus+ website](https://erasmus-plus.ec.europa.eu/document/higher-education-institutions-holding-an-eche-2021-2027), then added manually to the `data` directory and listed in `local_settings.py`.

## Importing from `.xlsx`

With the help of the `openpyxl` library, the `.xlsx` file is loaded as a _workbook_ with data values, meaning that all formulas are parsed and only the end results are kept.

The first _worksheet_ in the _workbook_ is considered to be the active one.

## Headers and values

The first row of the active _worksheet_ is used to retrieve the column headers. These headers should match the keys in the `eche_headers` _Dictionary_ in `local_settings.py`, so that they can be correctly mapped to the API keys.

All remaining rows are taken as the data values.

With the help of the `pandas` library, the headers and data values are used to produce a _DataFrame_. All empty rows and columns are dropped.

## Cleaning whitespace

The new _DataFrame_ undergoes some basic data cleaning, where preceding and trailing whitespace and line characters are removed from all strings.

Additionally, certain known strings are replaced with empty strings (i.e. errors from the `.xlsx` formulas) - the latter are listed as `eche_null_str` in `local_settings.py`.

## Renaming columns

Once the _DataFrame_ is clean, the columns are renamed according to the `eche_headers` _Dictionary_ in `local_settings.py`. From that point on, all columns are named like the API keys.
