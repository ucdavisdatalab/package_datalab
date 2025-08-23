"""Functions for hashing data.
"""

import base64
import hashlib


def hash_sha256(
    text: str,
    text_encoding: str = "UTF-8",
    as_base64: bool = True
) -> bytes | str:
    """Hash a text string with the SHA-256 algorithm.

    Parameters
    ----------
    text
        Text string to hash.
    text_encoding
        Encoding of the text string `text`.
    as_base64
        Encode the resulting digest with URL-safe Base64? Base64 is a
        space-efficient plain text (ASCII) encoding for arbitrary bytes.

    Returns
    -------
    bytes or str
        The SHA-256 hash, as bytes or as a Base64 string (if
        `as_base64 = True`).
    """
    digest = hashlib.sha256(text.encode(text_encoding)).digest()
    if as_base64:
        digest = base64.urlsafe_b64encode(digest).decode("ascii")
    return digest
