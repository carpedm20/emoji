# -*- coding: UTF-8 -*-


"""
emoji.core
~~~~~~~~~~

Core components for emoji.

"""


import re
import sys

from . import unicode_codes


PY2 = sys.version_info[0] is 2


USE_ALIASES = False


def emojize(string, use_aliases=USE_ALIASES):

    """Replace emoji names in a string with unicode codes.

    :param string: String contains emoji names.
    :param use_aliases: (optional) Enable emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.

        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :thumbs_up_sign:"))
        Python is fun 👍
    """

    pattern = re.compile('(:[a-zA-Z0-9\+\-_&.ô’Åéãíç]+:)')

    def replace(match):
        if use_aliases:
            return unicode_codes.EMOJI_ALIAS_UNICODE.get(match.group(1), match.group(1))
        else:
            return unicode_codes.EMOJI_UNICODE.get(match.group(1), match.group(1))

    return pattern.sub(replace, string)


def decode(u_code, use_aliases=USE_ALIASES):

    """Given a unicode code return the name of the associated emoji.

    :param u_code : String contains unicode emoji.
    :param use_aliases: (optional) Whether uses aliase of emoji name or not.
    :raises ValueError: unrecognized string.
    :return: Name of associated emoji.

        >>> import emoji
        >>> print(emoji.decode("👍"), use_aliases=True)
        :+1:
        >>> print(emoji.decode("👍"))
        :thumbs_up_sign:
    """

    if PY2:  # pragma no cover
        u_code = u_code.decode('utf-8')

    try:
        if use_aliases:
            return unicode_codes.UNICODE_EMOJI_ALIAS[u_code]
        else:
            return unicode_codes.UNICODE_EMOJI[u_code]
    except KeyError:
        raise ValueError("Unicode code is not an emoji: %s" % u_code)
