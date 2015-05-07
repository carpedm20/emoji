# -*- coding: UTF-8 -*-

"""
emoji.core
~~~~~~~~~~

Core components for emoji.

"""


import re

from . import unicode_codes


def emojize(string, is_alias=True):
    """Replace emoji names in a string with unicode codes.

    :param string: String contains emoji names.
    :param is_alias: (optional) Whether uses aliase of emoji name or not.

        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbsup:"))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :thumbs_up_sign:", False))
        Python is fun 👍
    """

    pattern = re.compile('(:[a-zA-Z0-9\+\-_]+:)')

    def replace(match):
        if is_alias:
            return unicode_codes.EMOJI_ALIAS_UNICODE.get(match.group(1), match.group(1))
        else:
            return unicode_codes.EMOJI_UNICODE.get(match.group(1), match.group(1))

    return pattern.sub(replace, string)


def decode(u_code, is_alias=True):
    """Given a unicode code return the name of the associated emoji.

    :param u_code : String contains unicode emoji.
    :param is_alias: (optional) Whether uses aliase of emoji name or not.
    :raises ValueError: unrecognized string.
    :return: Name of associated emoji.

        >>> import emoji
        >>> print(emoji.decode("👍"))
        :+1:
        >>> print(emoji.decode("👍", False))
        :thumbs_up_sign:
    """

    try:
        u_code = u_code.decode('utf-8')
    except:
        pass

    try:
        if is_alias:
            return unicode_codes.UNICODE_EMOJI_ALIAS[u_code]
        else:
            return unicode_codes.UNICODE_EMOJI[u_code]
    except KeyError:
        raise ValueError("Unicode code is not an emoji: %s" % u_code)
