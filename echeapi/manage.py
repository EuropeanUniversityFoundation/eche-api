#!/usr/bin/env python3

import os
import sys
from importlib import import_module


def main(cmd):
    try:
        script = import_module(f'echeapi.scripts.{cmd}')
    except ImportError:
        print('Invalid command')
    else:
        script.main(*sys.argv[2:])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ./manage.py initialize|populate|run|lint|test')
    else:
        sys.path[0] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        main(sys.argv[1])
