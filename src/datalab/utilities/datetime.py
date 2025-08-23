"""Functions for working with datetimes, dates, and times.
"""

import datetime as dt


def iso_datetime_now(sep: str = "T", timespec: str = "minutes") -> str:
    """Get the datetime now in ISO 8601 format.

    Parameters
    ----------
    sep
        Single-character separator for date and time components of the
        datetime.
    timespec
        Smallest unit of time to include. Can be 'auto', 'hours', 'minutes',
        'seconds', 'milliseconds', or 'microseconds'.
    """
    return dt.datetime.isoformat(
        dt.datetime.now(),
        sep = sep,
        timespec = timespec
    )


def iso_date_now() -> str:
    """Get the date today in ISO 8601 format.
    """
    return dt.date.isoformat(dt.date.today())
