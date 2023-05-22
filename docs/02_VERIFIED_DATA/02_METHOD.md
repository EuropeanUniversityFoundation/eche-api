# Attachment method

Verified data is attached to the existing data by locating a combination of unique identifiers and storing the new data points in their own fields. The original data is not changed. This document outlines the prerequisites for attaching verified data from trusted sources to the ECHE list data.

_All verified fields are saved with a prefix: `_verified.{field}`._

## Data format

The verified data **must** be provided in CSV format, using commas as separators and with all strings quoted.

## File naming convention

The file name **must** follow the pattern `verified.{countryCode}.csv`.

## File headers

For effective data pairing, the verified data **must** contain two identifiers: `erasmusCode` and `pic`. These will be used only to match data entries, _not_ to overwrite the identifiers in the original data set.

The remaining columns may include any of the following:

- `organisationLegalName`
- `organisationLegalNameLang` (recommended if `organisationLegalName` is provided)
- `street` (containing street name and door number)
- `postalCode`
- `city`
- `cityLang` (recommended if `city` is provided)
- `webpage`

## Data handling

The data handling will **ignore** empty cells, so verified data cannot be used to nullify existing data.

## Further information

When verified data is attached to an entry, the `hasVerifiedData` value will switch to `True` in order to provide an additional indication for client applications. Refer to the API specification for details.
