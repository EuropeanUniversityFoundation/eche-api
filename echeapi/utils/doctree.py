
import os

from echeapi import settings

DISPLAY_MD = 'DISPLAY_MD'
DISPLAY_DIR = 'DISPLAY_DIR'
DISPLAY_ERR = 'DISPLAY_ERR'


def fetch(args):
    path = os.path.join(settings.DOCS_DIR, *args)

    if os.path.isfile(path):
        display = DISPLAY_MD
        with open(path) as f:
            content = f.read()
    elif os.path.isdir(path):
        display = DISPLAY_DIR
        content = None
    else:
        display = DISPLAY_ERR
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
