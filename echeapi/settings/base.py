
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
    'Erasmus Charter Awarded',
]

# ECHE country names to be replaced.
ECHE_COUNTRY_NAMES = {
    'Turkiye': 'Türkiye',
    'Turkije': 'Türkiye',
    'Turkey': 'Türkiye',
}

# ECHE country codes to be replaced.
ECHE_COUNTRY_CODES = {
    'SF': 'FI',
}

# Country codes to ISO 3166-1 alpha-2 country codes.
CC_TO_ISO = {
    "EL": "GR",
    "UK": "GB",
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
    'countryCode',
    'countryCodeIso',
    'countryName',
    'erasmusCodeNormalized',
    'erasmusCodePrefix',
    'erasmusCodeCity',
    'erasmusCodeNumber',
    'erasmusCodeCountryCode',
    'erasmusCodeCountryCodeIso',
]

# Unique fields and severity of non-empty duplicates.
UNIQUE_FIELDS = {
    'proposalNumber': 'warning',
    'pic': 'danger',
    'oid': 'warning',
    'organisationLegalName': 'info',
    'erasmusCodeNormalized': 'danger',
}

# Reference field headers for data attachment.
REFERENCE_FIELDS = {
    'erasmusCode': 'erasmusCodeNormalized',
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
