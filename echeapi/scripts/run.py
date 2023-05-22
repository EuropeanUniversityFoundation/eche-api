
import os
import sys

from echeapi import app


def main(*args):
    port_number = None
    for i, arg in enumerate(args):
        if arg in ('-p', '--port'):
            try:
                port_number = int(args[i + 1])
            except IndexError:
                sys.exit(f'Option {arg} requires a value')
            except ValueError:
                sys.exit(f'Invlid port number: {args[i + 1]}')

    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(debug=True, port=port_number)
