# Importing the ECHE list

This application imports the ECHE list from a `.xslx` file, as published by DGEAC.

## Source file

The source file is taken from the [Erasmus+ website](https://erasmus-plus.ec.europa.eu/document/higher-education-institutions-holding-an-eche-2021-2027), then added manually to the code base.

## Importing from `.xlsx`

With the help of the `openpyxl` library, the `.xlsx` file is loaded as a _workbook_ with data values, meaning that all formulas are parsed and only the end results are kept.

The first _worksheet_ in the _workbook_ is considered to be the active one.

## Headers and values

The first row of the active _worksheet_ is used to retrieve the column headers. These headers should match the expected values as seen in the list below, so that they can be correctly mapped to the API keys.

- Proposal Number (`proposalNumber`)
- Erasmus Code (`erasmusCode`)
- PIC (`pic`)
- OID (`oid`)
- Organisation Legal Name (`organisationLegalName`)
- Street (`street`)
- Postal Code (`postalCode`)
- City (`city`)
- Country (`country`)
- Webpage (`webpage`)
- ECHE Start Date (`echeStartDate`)
- ECHE End Date (`echeEndDate`)

All remaining rows are taken as the data values.

With the help of the `pandas` library, the headers and data values are used to produce a _DataFrame_. All empty rows and columns are dropped.

## Cleaning whitespace

The new _DataFrame_ undergoes some basic data cleaning, where preceding and trailing whitespace and line characters are removed from all strings. Additionally, certain known strings are replaced with empty strings (i.e. errors from the `.xlsx` formulas).

## Renaming columns

Once the _DataFrame_ is clean, the columns are renamed according to the list shown above. From that point on, all columns are named like the API keys.
