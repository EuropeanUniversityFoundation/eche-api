# Local settings example.
# Duplicate this file as 'local_settings.py' which should be ignored by git.

# Flask requires a secret key to display flash messages.
app_secret_key = ''

# Data directory.
data_dir = 'data'

# ECHE list source file (Excel).
eche_xlsx = 'accredited-heis-erasmus-2021-2027-mar22_en.xlsx'

# ECHE list headers and corresponding API keys.
eche_headers = {
    'Proposal Number': 'proposalNumber',
    'Erasmus Code': 'erasmusCode',
    'PIC': 'pic',
    'OID': 'oid',
    'Organisation Legal Name': 'organisationLegalName',
    'Street': 'street',
    'Postal Code': 'postalCode',
    'City': 'city',
    'Country': 'country',
    'Webpage': 'webpage',
    'ECHE Start Date': 'echeStartDate',
    'ECHE End Date': 'echeEndDate'
}

# ECHE null strings.
eche_null_str = ['#N/A']

# Schema directory.
schema_dir = 'schema'
