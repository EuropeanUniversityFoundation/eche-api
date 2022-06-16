
import sys, os

VENV = os.path.dirname(__file__) + '/venv'
PYTHON_BIN = VENV + '/bin/python'

if sys.executable != PYTHON_BIN:
    os.execl(PYTHON_BIN, PYTHON_BIN, *sys.argv)

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '{v}/lib/python3.8/site-packages'.format(v=VENV))

from echeapi import app as application
