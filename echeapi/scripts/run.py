
import os

from echeapi import app


def main(*args):
    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(debug=True)
