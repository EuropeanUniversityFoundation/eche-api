
import os

from echeapi import settings

display_dir = 'display_dir'
display_md = 'display_md'
display_err = 'display_error'


def fetch(args):
    path = os.path.join(settings.docs_dir, *args)

    if os.path.isdir(path):
        display = display_dir
        content = f"This is a directory: docs/{os.path.relpath(path, settings.docs_dir)}"
    elif os.path.isfile(path):
        display = display_md
        with open(path, "r") as f:
            content = f.read()
    else:
        display = display_err
        content = "Cannot display the requested content."

    return display, content


def tree(root=settings.docs_dir):
    menu = {}
    dir = os.listdir(root)
    for item in sorted(dir):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            menu[item] = tree(path)
        elif os.path.isfile(path):
            menu[item] = os.path.relpath(path, settings.docs_dir)

    return menu
