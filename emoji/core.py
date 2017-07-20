# -*- coding: UTF-8 -*-


"""
emoji.core
~~~~~~~~~~

Core components for emoji.

"""


import re
import sys

from emoji import unicode_codes


__all__ = ['emojize', 'demojize', 'get_emoji_regexp','emoji_lis']


PY2 = sys.version_info[0] is 2

_EMOJI_REGEXP = None
_DEFAULT_DELIMITER = ":"

def emojize(text, use_aliases=False, delimiters=(_DEFAULT_DELIMITER,_DEFAULT_DELIMITER)):

    """Replace emoji names in a text with unicode codes.

    :param text: string contains emoji names.
    :param use_aliases: (optional) Enable emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) Use delimiters other than _DEFAULT_DELIMITER
        >>> print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :thumbs_up_sign:"))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun __thumbs_up_sign__", delimiters = ("__", "__")))
        Python is fun 👍
    """
 
    pattern = re.compile(u'(%s[a-zA-Z0-9\+\-_&.ô’Åéãíç()!#*]+%s)' % delimiters)

    def replace(match):
        mg = match.group(1).replace(delimiters[0], _DEFAULT_DELIMITER).replace(delimiters[1], _DEFAULT_DELIMITER)
        if use_aliases:
            return unicode_codes.EMOJI_ALIAS_UNICODE.get(mg, mg)
        else:
            return unicode_codes.EMOJI_UNICODE.get(mg, mg)

    return pattern.sub(replace, text)


def demojize(text, delimiters=(_DEFAULT_DELIMITER,_DEFAULT_DELIMITER)):

    """Replace unicode emoji in a text with emoji shortcodes. Useful for storage.

    :param text: String contains unicode characters. MUST BE UNICODE.
    :param delimiters: (optional) User delimiters other than _DEFAULT_DELIMITER
        >>> print(emoji.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up_sign:
        >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
        Unicode is tricky :hushed_face:
        >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8'), delimiters=(" __", "__ ")))
        Unicode is tricky __hushed_face__:
    """

    def replace(match):
        val = unicode_codes.UNICODE_EMOJI.get(match.group(0), match.group(0))
        return delimiters[0] + val[1:-1] + delimiters[1]

    return get_emoji_regexp().sub(replace, text)


def get_emoji_regexp():

    """Returns compiled regular expression that matches emojis defined in
    ``emoji.UNICODE_EMOJI_ALIAS``. The regular expression is only compiled once.
    """

    global _EMOJI_REGEXP
    # Build emoji regexp once
    if _EMOJI_REGEXP is None:
        # Sort emojis by length to make sure mulit-character emojis are
        # matched first
        emojis = sorted(unicode_codes.EMOJI_UNICODE.values(), key=len,
                        reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)
    return _EMOJI_REGEXP


def emoji_list(text):
    """Return the location, the emoji unicode, and the CLDR Short Name in list of dic format
    >>>emoji.emoji_list("Hi, I am fine. 😁".decode('utf-8'))
    >>>[{'cldr': u':grinning_face_with_smiling_eyes:', 'emoji': u'\U0001f601', 'location': (15, 16)}]
    """
    _entities = []
    def replace(match):
        em = match.group(0)
        val = unicode_codes.UNICODE_EMOJI.get(em, None)
        if val:
            _entities.append({"location": match.span(), "emoji": em, "cldr":val})
        return em

    get_emoji_regexp().sub(replace, text)
    return _entities


def replace_emoji(text, replacement=''):
    """
    Replace all emojis with "replacement" string.
    Default replacement is empty string, equivalent to removing all emojis
    >>>emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'))
    >>>Hi, I am fine.
    >>>emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'), replacement='***')
    >>>Hi, I am fine. ***
    """
    return get_emoji_regexp().sub(replacement, text)