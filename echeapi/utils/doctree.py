
import os
from enum import Enum

from echeapi import settings


class Display(Enum):
    DIR = 'dir'
    FILE = 'file'
    ERROR = 'error'


def fetch(args):
    path = os.path.join(settings.DOCS_DIR, *args)

    if os.path.isdir(path):
        display = Display.DIR
        content = f"This is a directory: docs/{os.path.relpath(path, settings.DOCS_DIR)}"
    elif os.path.isfile(path):
        display = Display.FILE
        with open(path) as f:
            content = f.read()
    else:
        display = Display.ERROR
        content = "Cannot display the requested content."

    return display, content


def tree(root=settings.DOCS_DIR):
    menu = {}
    dir = os.listdir(root)
    for item in sorted(dir):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            menu[item] = tree(path)
        elif os.path.isfile(path):
            menu[item] = os.path.relpath(path, settings.DOCS_DIR)

    return menu
