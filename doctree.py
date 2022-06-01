import os

docs_rootdir = 'docs'

def fetch(args):
    path = docs_rootdir
    for arg in args:
        path = os.path.join(path, arg)

    if os.path.isdir(path):
        print("This is a directory: " + str(path))
    elif os.path.isfile(path):
        print("This is a file: " + str(path))
    else:
        print("Cannot display anything.")

def tree(root=docs_rootdir):
    menu = {}
    for item in os.listdir(root):
        path = os.path.join(root,item)
        if os.path.isdir(path):
            menu[item] = tree(path)
        elif os.path.isfile(path):
            menu[item] = '/' + path

    return menu

if __name__ == '__main__':
    print(f"Docs\n")

    menu = tree()
    print(menu)
