"""Functions for working with Jupyter notebooks.
"""

import datalab.utilities.pathing as pathing


def next_notebook_number() -> int:
    """Get the next integer number that isn't a 3-digit prefix to a notebook in
    the project's `notebooks/` directory.
    """
    root = pathing.find_project_root()
    ipynbs = (root / "notebooks/").glob("**/*.ipynb")
    ipynbs = (p for p in ipynbs if ".ipynb_checkpoints/" not in str(p))
    nums = (p.name.split("_", 1)[0] for p in ipynbs)
    nums = (_try_cast_int(x) for x in nums if len(x) == 3)
    return max(*nums) + 1


def _try_cast_int(x, default = 0) -> int:
    try:
        return int(x)
    except ValueError:
        return default
