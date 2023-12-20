import sys
from distutils.dir_util import copy_tree

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: {sys.argv[0]} DIR")
        sys.exit(1)
    copy_tree("template", sys.argv[1])
