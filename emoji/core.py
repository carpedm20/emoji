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

    # via Martijn Pieters, http://stackoverflow.com/questions/26568722/remove-unicode-emoji-using-re-in-python
    if PY2:
        try:
            # Wide UCS-4 build
            pattern = re.compile(u'['
                u'\U0001F300-\U0001F64F'
                u'\U0001F680-\U0001F6FF'
                u'\u2600-\u26FF\u2700-\u27BF]+', 
                re.UNICODE)
        except re.error:
            # Narrow UCS-2 build
            pattern = re.compile(u'('
                u'\ud83c[\udf00-\udfff]|'
                u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                u'[\u2600-\u26FF\u2700-\u27BF])+', 
                re.UNICODE)
    else:
    # Python 3+ should handle all strings as unicode. Right?
        try:
            # Wide UCS-4 build
            pattern = re.compile('['
                '\U0001F300-\U0001F64F'
                '\U0001F680-\U0001F6FF'
                '\u2600-\u26FF\u2700-\u27BF]+', 
                re.UNICODE)
        except re.error:
            # Narrow UCS-2 build
            pattern = re.compile('('
                '\ud83c[\udf00-\udfff]|'
                '\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                '[\u2600-\u26FF\u2700-\u27BF])+', 
                re.UNICODE)

    def replace(match):
        return unicode_codes.UNICODE_EMOJI.get(match.group(0), match.group(0))

    return pattern.sub(replace, string)
