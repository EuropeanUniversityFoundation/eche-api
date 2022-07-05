
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
ECHE_NULL_STR = ['#N/A']

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

# Cache control max age for static pages.
CACHE_CONTROL_MAX_AGE = 600

# Cache control max age for data pages.
DATA_CACHE_TIMEOUT = 60 * 60 * 24 * 365

# Cache configuration.
CACHE_CONFIG = {
    'CACHE_TYPE': 'SimpleCache',
    # 'CACHE_TYPE': 'RedisCache',
    # 'CACHE_REDIS_URL': 'redis://localhost:6379/0',
    'CACHE_DEFAULT_TIMEOUT': 300,
}
