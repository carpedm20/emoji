# -*- coding: UTF-8 -*-


"""
Core components for emoji
"""


import re

from . import unicode_codes


__all__ = ['emojize', 'decode']


def emojize(string):

    """
    Replace emoji names in a string with unicode codes.

    Example:

        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbs_up_sign:"))
        Python is fun 👍
    """

    pattern = re.compile('(:[a-zA-Z0-9\+\-_&.ô’Åéãíç]+:)')

    def replace(match):
        return unicode_codes.EMOJI_UNICODE.get(match.group(1), match.string)

    return pattern.sub(replace, string)


def decode(u_code):

    """
    Given a unicode code return the name of the associated emoji.

    Parameters
    ----------
    u_code : str
        String associated with an emoji.

    Raises
    ------
    ValueError
        Unrecognized string.

    Returns
    -------
    str
        Name of associated emoji.
    """

    try:
        return unicode_codes.UNICODE_EMOJI[u_code]
    except KeyError:
        raise ValueError("Unicode code is not an emoji: %s" % u_code)
