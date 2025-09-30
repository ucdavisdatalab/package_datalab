"""Functions to provide a command-line interface.
"""

import argparse
from pathlib import Path

from loguru import logger

import datalab.utilities.datetime as dt
import datalab.utilities.io as io
import datalab.utilities.dicttools as dicttools


def provide_toml_interface(
    parser: argparse.ArgumentParser | None = None,
    format_keys: list[str] | None = None,
    **kwargs
) -> tuple[argparse.Namespace, dict]:
    """Provide a simple argparse command-line interface that requires a path to
    a TOML file, read the file, and return its contents.

    Parameters
    ----------
    parser
        An ArgumentParser to use, or None to create a new one automatically.
    format_keys
        A list of keys from top-level key/value pairs in the file. The
        `str.format` function will be called on every value string in the file
        with these key/value pairs as arguments. If this is None, the value
        strings will be left unformatted.
    **kwargs
        Arguments to `argparse.ArgumentParser` if `parser` is `None`.

    Returns
    -------
    The parsed arguments and the contents of the TOML file.
    """
    if parser is None:
        parser = argparse.ArgumentParser(**kwargs)
        parser.add_argument(
            metavar = "config",
            help = "path to TOML configuration file",
            type = Path,
            dest = "config_path",
        )

    args = parser.parse_args()

    config_path = args.config_path
    logger.info(f"Reading '{config_path}'")
    config = io.read_toml(config_path, inherit = True)

    if format_keys is not None:
        format_keys = {k: config.get(k, "") for k in format_keys}
        config = dicttools.recursive_format(
            config,
            date = dt.iso_date_now(),
            datetime = dt.iso_datetime_now(),
            **format_keys
        )

    return args, config
