
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
LOG_FILENAME =  os.path.join(LOG_DIR, LOG_FILENAME)

# ECHE data API keys.
ECHE_KEYS = [*dict.fromkeys(ECHE_HEADERS_MAP.values())]  # Remove duplicates while preserving the original order

# Default API keys.
DEFAULT_API_KEYS = [
    *ECHE_KEYS,
    *PROCESSED_KEYS,
]

# All known API keys
ALL_API_KEYS = [
    *DEFAULT_API_KEYS,
    *[f'{VERIFIED_KEY_PREFIX}.{k}' for k in VERIFIED_BASE_KEYS],
]

# Set of unique columns to drop duplicates by.
UNIQUE_KEYS = [*UNIQUE_CHECKS.keys()]

try:
    os.makedirs(os.path.dirname(LOG_FILENAME), mode=0o755, exist_ok=True)
except OSError:
    print(f'WARNING: Could not create logs directory: {os.path.dirname(LOG_FILENAME)}')
