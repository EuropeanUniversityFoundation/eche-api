
import os

from echeapi import app


def main(*args):
    port_number = 5000

    for i, arg in enumerate(args):
        if arg in ('-p', '--port'):
            port_number = args[i + 1]

    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(debug=True, port=port_number)
