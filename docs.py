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
    print(os.walk(root, topdown=True))
    for (root,dirs,files) in os.walk(root, topdown=True):
        print (root)
        print (dirs)
        print (files)

if __name__ == '__main__':
    print(f"Docs")
    tree()
