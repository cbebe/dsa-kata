import sys
import os
from distutils.dir_util import copy_tree, remove_tree

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: {sys.argv[0]} DIR")
        sys.exit(1)
    if os.path.isdir("template/__pycache__"):
        remove_tree("template/__pycache__", verbose=True)
    copy_tree("template", sys.argv[1])
