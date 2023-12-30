import os
import sys
from pathlib import Path

if __name__ == "__main__":
    dir = sys.argv[1].split("-")[1]
    if not os.path.isdir(dir):
        print(f"{dir} is not a directory", file=sys.stderr)
        sys.exit(1)
    for f in next(os.walk(dir))[2]:
        m = f"{dir}.{Path(f).stem}"
        print(f"testing {m}...", flush=True, end=' ')
        os.system(f"python -m {m}")
