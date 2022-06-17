
import os

docs_rootdir = 'docs'

display_dir = 'display_dir'
display_md = 'display_md'
display_err = 'display_error'


def fetch(args):
    path = docs_rootdir
    for arg in args:
        path = os.path.join(path, arg)

    if os.path.isdir(path):
        display = display_dir
        content = "This is a directory: " + str(path)
    elif os.path.isfile(path):
        display = display_md
        content = open(path, "r")
    else:
        display = display_err
        content = "Cannot display anything."

    return display, content


def tree(root=docs_rootdir):
    menu = {}
    dir = os.listdir(root)
    dir.sort()
    for item in dir:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            menu[item] = tree(path)
        elif os.path.isfile(path):
            menu[item] = '/' + path

    return menu


if __name__ == '__main__':
    print("Docs\n")

    menu = tree()
    print(menu)
