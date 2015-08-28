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

EMOJI_REGEXP = None

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

def demojize(string):

    """Replace unicode emoji in a string with emoji shortcodes. Useful for storage.

    :param string: String contains unicode characters. MUST BE UNICODE.

        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbs_up_sign:"))
        Python is fun 👍
        >>> print(emoji.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up_sign:
        >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
        Unicode is tricky :hushed_face:
    """
    # Build emoji regexp once
    if EMOJI_REGEXP is None:
        global EMOJI_REGEXP
        # Sort emojis by length to make sure mulit character emojis are
        # matched first
        emojis = sorted(unicode_codes.EMOJI_UNICODE.values(), key=len, reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis)+ u')'
        EMOJI_REGEXP = re.compile(pattern)

    def replace(match):
        val = unicode_codes.UNICODE_EMOJI.get(match.group(0), match.group(0))
        return val.decode('utf-8') if PY2 else val
    return EMOJI_REGEXP.sub(replace, string)
