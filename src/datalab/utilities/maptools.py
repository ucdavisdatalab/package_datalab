"""Functions for working with mappings.
"""

import collections


def recursive_update(older, newer):
    """Recursively update older mappings with newer mappings.

    Note that lists are replaced rather than combined.

    Parameters
    ----------
    older
        The mapping to update.
    newer
        The mapping to use to update the older mapping.
    """
    MM = collections.abc.MutableMapping
    result = older.copy()
    for k, v in newer.items():
        if isinstance(v, MM) and isinstance(result.get(k), MM):
            result[k] = recursive_update(result[k], v)
        else:
            result[k] = v

    return result
