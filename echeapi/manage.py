#!/usr/bin/env python3

import os
import sys
from importlib import import_module


def main(cmd):
    try:
        script = import_module(f'echeapi.scripts.{cmd}')
    except ImportError:
        sys.exit(f'Invalid command: {cmd}')
    else:
        script.main(*sys.argv[2:])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Usage: ./manage.py initialize|populate|run|lint|shell|test')
    else:
        # Check for active virtualenv
        if 'VIRTUAL_ENV' not in os.environ:
            sys.exit('The virtualenv is not activated.\n'
                     'Run:\n'
                     '    source venv/bin/activate')

        sys.path[0] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        main(sys.argv[1])
