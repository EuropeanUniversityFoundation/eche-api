
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
VERIFIED_DIR = os.path.join(DATA_DIR, VERIFIED_DIR)
DB_DIR = os.path.join(SRC_DIR, DB_DIR)
DOCS_DIR = os.path.join(SRC_DIR, DOCS_DIR)
LOG_DIR = os.path.join(SRC_DIR, LOG_DIR)

# Absolute file names
DB_FILENAME = os.path.join(DB_DIR, DB_FILENAME)
DATA_FILENAME =  os.path.join(DATA_DIR, DATA_FILENAME)

# ECHE data API keys.
ECHE_KEYS = [*dict.fromkeys(ECHE_FIELDS.values())]  # Remove duplicates while preserving the original order

# Default API keys.
DEFAULT_KEYS = [
    *ECHE_KEYS,
    *PROCESSED_FIELDS,
]

# Verified data API keys.
VERIFIED_KEYS = [f'{VERIFIED_KEY}.{f}' for f in VERIFIED_FIELDS]

# All known API keys
KNOWN_KEYS = [
    *DEFAULT_KEYS,
    *VERIFIED_KEYS,
]

# Set of unique columns to drop duplicates by.
UNIQUE_COLS = [*UNIQUE_FIELDS.keys()]

try:
    os.makedirs(LOG_DIR, mode=0o755, exist_ok=True)
except OSError:
    print(f'WARNING: Could not create logs directory: {LOG_DIR}')
