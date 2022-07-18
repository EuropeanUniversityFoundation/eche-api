
# Data directory.
DATA_DIR = 'data'

# Database directory.
DB_DIR = ''

# Database filename.
DB_FILENAME = 'eche.db'

# Primary database table.
DB_TABLE = 'eche'

# Docs directory.
DOCS_DIR = 'docs'

DOCS_DEFAULT = '00_OVERVIEW.md'

# Log files directory.
LOG_DIR = ''

# Log format.
LOG_FORMAT = '[%(asctime)s] [%(levelname)s] %(message)s'

# ECHE null strings.
ECHE_NULL_STR = [
    '#N/A',
    'Not Found',
    'Transitory Charter',
    'Transitory Erasmus  Charter',
    'Transitory Erasmus charter',
]

# ECHE list headers and corresponding API keys.
ECHE_FIELDS = {
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

# Date fields to be parsed when reading from the database.
DATE_FIELDS = [
    'echeStartDate',
    'echeEndDate',
]

# Processed fields.
PROCESSED_FIELDS = [
    'erasmusCodeNormalized',
    'erasmusCodePrefix',
    'erasmusCodeCountryCode',
    'countryCode',
]

# Unique fields and severity of non-empty duplicates.
UNIQUE_FIELDS = {
    'proposalNumber': 'warning',
    'pic': 'danger',
    'oid': 'danger',
    'organisationLegalName': 'info',
    'erasmusCodeNormalized': 'danger',
}

# Reference field headers for data attachment.
REFERENCE_FIELDS = [
    'erasmusCodeNormalized',
    'pic',
]

# Verified data field headers for data attachment.
VERIFIED_FIELDS = [
    'organisationLegalName',
    'organisationLegalNameLang',
    'street',
    'postalCode',
    'city',
    'cityLang',
    'webpage',
]
