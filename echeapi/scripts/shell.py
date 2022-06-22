
import sys


def main(*args):
    try:
        from IPython import start_ipython
    except ImportError:
        sys.exit('Could not import ipython. '
                 'Make sure it is installed in the current virtualenv:\n'
                 '    pip install ipython')
    else:
        start_ipython(argv=[])
