"""Functions for input and output of data.
"""

import json
from pathlib import Path
import tomllib
from typing import Any

import datalab.utilities.maptools as maptools


def read_api_key(path: str | Path) -> str:
    """Read an API key or authentication token from a file.

    Parameters
    ----------
    path
        Path to the API key.

    Returns
    -------
    The first line of the file as a string.
    """
    with open(path, "rt") as f:
        return f.readline().strip()


def read_toml(path: str | Path, inherit: bool = False) -> dict:
    """Read a TOML file.

    Parameters
    ----------
    path
        Path to the TOML file to read.
    inherit
        If True, the TOML file can inherit settings from another TOML file
        whose path is specified in a top-level `inherit` key.

    Returns
    -------
    The contents of the TOML file.
    """
    with open(path, "rb") as f:
        result = tomllib.load(f)

    if inherit and "inherit" in result:
        inherit_path = Path(result["inherit"])
        if not inherit_path.is_absolute():
            # So `inherit_path` is relative to `path`.
            inherit_path = Path(path).parent / inherit_path

        with open(inherit_path, "rb") as f:
            inherited = tomllib.load(f)
            if "inherit" in inherited:
                raise RuntimeError(
                    f"The inherited file ('{inherit_path}') also has an"
                    " `inherit` key, which is not allowed. Remove the key or"
                    " inherit from a different file."
                )

        result = maptools.recursive_update(inherited, result)

    return result


def read_json(path: str | Path) -> Any:
    """Read a JSON file.

    Parameters
    ----------
    path
        Path to the JSON file to read.

    Returns
    -------
    The contents of the JSON file.
    """
    with open(path, "rt") as f:
        return json.load(f)


def write_json(obj: Any, path: str | Path, mode: str = "xt", **kwargs):
    """Write a JSON file.

    Parameters
    ----------
    obj
        Object to write to the JSON file.
    path
        Path to the JSON file to write.
    mode
        Mode in which the file is opened (typically "xt" to write, "wt" to
        overwrite, or "at" to append).
    **kwargs
        Further arguments to `json.dump`.
    """
    with open(path, mode) as f:
        json.dump(obj, f, **kwargs)
