
import os

from echeapi import app


def main():
    os.environ.setdefault('FLASK_ENV', 'development')
    app.run(debug=True)
