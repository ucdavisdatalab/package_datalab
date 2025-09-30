"""Functions for working with dicts and other key-value data structures.
"""

from typing import Any


def recursive_update(older: dict, newer: dict) -> dict:
    """Recursively update a dict and its sub-dicts with new key-value pairs.

    Note that this function does not recurse into lists (their key is updated
    without examining their elements).

    Parameters
    ----------
    older
        A dict to update.
    newer
        A dict that contains the updates.
    """
    result = older.copy()
    for k, v in newer.items():
        if isinstance(v, dict) and isinstance(result.get(k), dict):
            result[k] = recursive_update(result[k], v)
        else:
            result[k] = v

    return result


def recursive_format(obj: Any, **kwargs) -> Any:
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
