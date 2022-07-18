# Verified data

This application allows for verified data to be attached to the original data, provided it follows some conventions.

## Data format

The verified data **must** be provided in CSV format, using commas as separators and with all strings quoted.

## File naming convention

The file name _should_ follow the pattern `verified.{countryCode}.csv`.

## File headers

For effective data pairing, the verified data **must** contain two identifiers: `erasmusCodeNormalized` and `pic`. These will be used only to match data entries, _not_ to overwrite the identifiers in the original data set.

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
