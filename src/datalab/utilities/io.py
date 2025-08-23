"""Functions for input and output of data.
"""

import json
from pathlib import Path
import tomllib
from typing import Any


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


def read_toml(path: str | Path) -> dict:
    """Read a TOML file.

    Parameters
    ----------
    path
        Path to the TOML file to read.

    Returns
    -------
    The contents of the TOML file.
    """
    with open(path, "rb") as f:
        return tomllib.load(f)


def recursive_format(obj: dict, **kwargs):
    """Recurse through a JSON- or TOML-like object, formatting all strings
    found.

    Parameters
    ----------
    obj
        The object to recurse through.
    **kwargs
        Arguments to `str.format`.

    Returns
    -------
    An object with the same shape as `obj` and all strings formatted.
    """
    match obj:
        case dict():
            return {k: recursive_format(v, **kwargs) for k, v in obj.items()}
        case list():
            return [recursive_format(x, **kwargs) for x in obj]
        case str():
            return obj.format(**kwargs)
        case _:
            return obj


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
