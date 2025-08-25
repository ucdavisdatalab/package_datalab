"""Functions to manage logging (via loguru).
"""

import inspect
import logging
import sys

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        try:
            level: str | int = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = inspect.currentframe(), 0
        while frame:
            filename = frame.f_code.co_filename
            is_logging = filename == logging.__file__
            is_frozen = "importlib" in filename and "_bootstrap" in filename
            if depth > 0 and not (is_logging or is_frozen):
                break
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def use_loguru(
    sink = sys.stdout,
    level: str = "INFO",
    filter: dict = {"__main__": True, "datalab": True, "": False},
    **kwargs
):
    """Divert standard logging messages to Loguru, remove all sinks, and add a
    default sink.

    Call this function if you want to use Loguru for all logging but some of
    your project's dependencies use standard logging. It's not necessary (but
    won't hurt) to call this function if your project's dependencies use Loguru
    or don't do any logging.

    Parameters
    ----------
    sink
        Default sink for logging messages.
    level
        Level of messages to display (DEBUG, INFO, WARN, etc.).
    filter
        Filter for modules from which to display messages.
    **kwargs
        Additional arguments to `logger.add`.

    Returns
    -------
    The Loguru logger.
    """
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    logger.remove()
    logger.add(sink, level=level, filter=filter, **kwargs)

    return logger
