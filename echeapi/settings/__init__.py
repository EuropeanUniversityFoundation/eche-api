
import os

from .base import *
from .default import *

try:
    from .local import *
except ImportError:
    print('WARNING: Could not import local settings.')

# Project root directory
SRC_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Absolute directory paths
DATA_DIR = os.path.join(SRC_DIR, DATA_DIR)
DB_DIR = os.path.join(SRC_DIR, DB_DIR)
DOCS_DIR = os.path.join(SRC_DIR, DOCS_DIR)
LOG_DIR = os.path.join(SRC_DIR, LOG_DIR)

# Absolute file names
DB_FILENAME = os.path.join(DB_DIR, DB_FILENAME)
DATA_FILENAME =  os.path.join(DATA_DIR, DATA_FILENAME)

# ECHE data API keys.
ECHE_KEYS = [*ECHE_FIELDS.values()]

# Processed data API keys.
PROCESSED_KEYS = ['.'.join([PROCESSED_KEY, f]) for f in PROCESSED_FIELDS]

# Verified data API keys.
VERIFIED_KEYS = ['.'.join([VERIFIED_KEY, f]) for f in VERIFIED_FIELDS]

# All known API keys
KNOWN_KEYS = [
    *ECHE_KEYS,
    *PROCESSED_KEYS,
    *VERIFIED_KEYS,
]

# All known API keys
KNOWN_FIELDS = [
    *ECHE_KEYS,
    *PROCESSED_FIELDS,
    *VERIFIED_FIELDS,
]


try:
    os.makedirs(LOG_DIR, mode=0o755, exist_ok=True)
except OSError:
    print(f'WARNING: Could not create logs directory: {LOG_DIR}')
