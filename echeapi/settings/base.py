
# Data directory.
data_dir = 'data'

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
    'ECHE End Date': 'echeEndDate',
}

# ECHE null strings.
eche_null_str = ['#N/A']

# Schema directory.
schema_dir = 'schema'

# Schema to install.
schema_filename = 'eche.sql'

# Database filename.
db_filename = 'eche.db'

# Primary database table.
db_table = 'eche'

# Date fields to be parsed when reading from the database.
date_fields = [
    'echeStartDate',
    'echeEndDate',
]

# Processed fields.
processed_fields = [
    'erasmusCodeNormalized',
    'erasmusCodePrefix',
    'erasmusCodeCountryCode',
    'countryCode',
]

# Docs directory.
docs_dir = 'docs'

# Log files directory.
log_dir = ''

# Log format.
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'
