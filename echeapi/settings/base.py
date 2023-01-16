
# Data directory.
DATA_DIR = 'data'

# Verified data subdirectory.
VERIFIED_DIR = 'verified'

VERIFIED_PREFIX = 'verified'
VERIFIED_EXTENSION = 'csv'

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
    '#VALUE!',
    'Not Found',
    'Transitory Charter',
    'Transitory Erasmus  Charter',
    'Transitory Erasmus charter',
    'Transitory Erasmus Charter',
]

# ECHE country names to be replaced.
ECHE_COUNTRY_NAMES = {
    'Turkije': 'Turkiye',
    'Turkey': 'Turkiye',
}

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
    'erasmusCodeCity',
    'erasmusCodeNumber',
    'erasmusCodeCountryCode',
    'countryCode',
]

# Database column prefix for verified fields.
PROCESSED_KEY = '_processed'

# Unique fields and severity of non-empty duplicates.
UNIQUE_FIELDS = {
    'proposalNumber': 'warning',
    'pic': 'danger',
    'oid': 'warning',
    'organisationLegalName': 'info',
    f'{PROCESSED_KEY}.erasmusCodeNormalized': 'danger',
}

# Reference field headers for data attachment.
REFERENCE_FIELDS = {
    'erasmusCode': f'{PROCESSED_KEY}.erasmusCodeNormalized',
    'pic': 'pic',
}

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

# Database column prefix for verified fields.
VERIFIED_KEY = '_verified'

# Cache control max age for static pages.
CACHE_CONTROL_MAX_AGE = 60 * 10  # 10 minutes
