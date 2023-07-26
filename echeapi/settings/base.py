
# Data directory.
DATA_DIR = 'data'

# Verified data subdirectory.
VERIFIED_DIR = 'verified'

# Verified data files naming pattern.
VERIFIED_FILE_PREFIX = 'verified'
VERIFIED_FILE_EXT = '.csv'

# Database directory (default: project root).
DB_DIR = ''

# Database filename.
DB_FILENAME = 'eche.db'

# Primary database table.
DB_TABLE = 'eche'

# Docs directory.
DOCS_DIR = 'docs'

# Default docs file.
DOCS_DEFAULT_PAGE = '00_OVERVIEW.md'

# Log files directory (default: project root).
LOG_DIR = ''

# Log file name.
LOG_FILENAME = 'app.log'

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
COUNTRY_NAMES_MAP = {
    'Turkiye': 'Türkiye',
    'Turkije': 'Türkiye',
    'Turkey': 'Türkiye',
}

# ECHE country codes to be replaced.
COUNTRY_CODES_MAP = {
    'SF': 'FI',
}

# ECHE country codes to be replaced with ISO 3166-1 alpha-2.
COUNTRY_CODES_TO_ISO_MAP = {
    'EL': 'GR',
    'UK': 'GB',
    'XK': None,
}

# Type of data contained in the 'Country' column.
ECHE_COUNTRY_FIELD_TYPE = 'countryCode'

# ECHE list headers and corresponding API keys.
ECHE_HEADERS_MAP = {
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
PROCESSED_KEYS = [
    'countryCode',
    'countryCodeIso',
    'countryName',
    'erasmusCodeNormalized',
    'erasmusCodePrefix',
    'erasmusCodeCity',
    'erasmusCodeNumber',
    'erasmusCodeCountryCode',
    'erasmusCodeCountryCodeIso',
    'hasVerifiedData',
]

# Verified data fields (unprefixed).
VERIFIED_BASE_KEYS = [
    'organisationLegalName',
    'organisationLegalNameLang',
    'street',
    'postalCode',
    'city',
    'cityLang',
    'webpage',
]

# Verified data headers required for data attachment.
VERIFIED_REQUIRED_FIELDS = ['pic', 'erasmusCode']

# Verified data join columns.
VERIFIED_JOIN_BY_FIELDS = ['pic', 'erasmusCodeNormalized']

# Database column prefix for verified fields.
VERIFIED_KEY_PREFIX = '_verified'

# Unique fields and severity of non-empty duplicates.
UNIQUE_CHECKS = {
    'proposalNumber': 'warning',
    'pic': 'danger',
    'oid': 'warning',
    'organisationLegalName': 'info',
    'erasmusCodeNormalized': 'danger',
}

# Cache control max age for static pages.
CACHE_CONTROL_MAX_AGE = 60 * 10  # 10 minutes
