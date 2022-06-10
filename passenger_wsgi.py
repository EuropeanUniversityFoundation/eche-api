
import os
import sys

VENV = os.path.join(os.path.dirname(__file__), 'venv')
PYTHON_BIN = os.path.join(VENV, 'bin', 'python')

if sys.executable != PYTHON_BIN:
    os.execl(PYTHON_BIN, PYTHON_BIN, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(VENV, 'lib', 'python3.8', 'site-packages'))

from echeapi import app as application
