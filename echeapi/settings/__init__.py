
import os

from .base import *
from .default import *

try:
    from .local import *
except ImportError:
    print('WARNING: Could not import local settings.')


# Project root directory
src_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

data_dir = os.path.join(src_dir, data_dir)
schema_dir = os.path.join(src_dir, schema_dir)
db_filename = os.path.join(src_dir, db_filename)
log_dir = os.path.join(src_dir, log_dir)


# Known API keys.
known_keys = list(eche_headers.values())
known_keys.extend(processed_fields)


try:
    os.makedirs(log_dir, mode=0o755, exist_ok=True)
except OSError:
    print(33, f'WARNING: Could not create logs directory: {log_dir}')
