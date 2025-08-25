"""Functions for working with paths.
"""

import os
from pathlib import Path


def find_project_root(path = Path.cwd()) -> Path:
    """Find the project root (top-level) directory by searching upwards for the
    first directory that contains a `.git/` or `.pixi/` subdirectory.

    Parameters
    ----------
    path
        Directory at which to start the search.
    """
    while True:
        if (path / ".git").is_dir() or (path / ".pixi").is_dir():
            return path
        elif path == path.parent:
            raise FileNotFoundError("Can't find project root.")

        path = path.parent


def chdir_project_root() -> Path:
    """Change the working directory to the project root directory.
    """
    root = find_project_root()
    os.chdir(root)
    return root
