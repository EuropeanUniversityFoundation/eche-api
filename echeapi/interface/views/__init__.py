
import os
import pkgutil
from importlib import import_module


def discover():
    """ Import each view module to execute Flask decorators and register views.
    """
    for _, name, _ in pkgutil.iter_modules([os.path.dirname(__file__)]):
        import_module(f'{__name__}.{name}')
