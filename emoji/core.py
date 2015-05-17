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
