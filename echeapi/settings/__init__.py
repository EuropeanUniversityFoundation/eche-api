
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
SCHEMA_DIR = os.path.join(SRC_DIR, SCHEMA_DIR)
DB_DIR = os.path.join(SRC_DIR, DB_DIR)
DOCS_DIR = os.path.join(SRC_DIR, DOCS_DIR)
LOG_DIR = os.path.join(SRC_DIR, LOG_DIR)

# Absolute file names
SCHEMA_FILENAME = os.path.join(SCHEMA_DIR, SCHEMA_FILENAME)
DB_FILENAME = os.path.join(DB_DIR, DB_FILENAME)
DATA_FILENAME =  os.path.join(DATA_DIR, DATA_FILENAME)

# Known API keys.
DATA_FIELDS = [
    *ECHE_FIELDS.values(),
    *PROCESSED_FIELDS,
]

try:
    os.makedirs(LOG_DIR, mode=0o755, exist_ok=True)
except OSError:
    print(f'WARNING: Could not create logs directory: {LOG_DIR}')
