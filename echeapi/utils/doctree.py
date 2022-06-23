
import os
from enum import Enum

from echeapi import settings


class Display(Enum):
    DIR = 'dir'
    FILE = 'file'
    ERROR = 'error'


def fetch(args):
    path = os.path.join(settings.DOCS_DIR, *args)

    if os.path.isfile(path):
        display = Display.FILE
        with open(path) as f:
            content = f.read()
    elif os.path.isdir(path):
        display = Display.DIR
        content = None
    else:
        display = Display.ERROR
        content = None

    return display, content


def tree(root=settings.DOCS_DIR):
    menu = {}
    for item in sorted(os.listdir(root)):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            menu[item] = tree(path)
        elif os.path.isfile(path):
            menu[item] = os.path.relpath(path, settings.DOCS_DIR)
    return menu
