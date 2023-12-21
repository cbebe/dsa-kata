import sys
from shutil import copytree, rmtree

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: {sys.argv[0]} DIR")
        sys.exit(1)
    rmtree("template/__pycache__", ignore_errors=True)
    copytree("template", sys.argv[1])
