# -*- coding: UTF-8 -*-


"""
emoji.core
~~~~~~~~~~

Core components for emoji.

"""


import re
import sys

from emoji import unicode_codes

__all__ = [
    'emojize', 'demojize', 'get_emoji_regexp',
    'emoji_lis', 'distinct_emoji_lis', 'emoji_count',
]


PY2 = sys.version_info[0] == 2

_EMOJI_REGEXP = None
_DEFAULT_DELIMITER = ':'


def emojize(
        string,
        use_aliases=False,
        delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER),
        variant=None,
        language='en',
):
    """Replace emoji names in a string with unicode codes.

    :param string: String contains emoji names.
    :param use_aliases: (optional) Enable emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) Use delimiters other than _DEFAULT_DELIMITER
    :param variant: (optional) Choose variation selector between "base"(None), VS-15 ("text_type") and VS-16 ("emoji_type")
    :param language: Choose language of emoji name
        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun __thumbs_up__", delimiters = ("__", "__")))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :red_heart:"))
        Python is fun ❤
        >>> print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
        Python is fun ❤️ #red heart, not black heart
    """
    EMOJI_UNICODE = unicode_codes.EMOJI_UNICODE[language]
    pattern = re.compile(u'(%s[A-zÀ-ÿ0-9\\-_&.’”“()!#*+?–]+%s)' % delimiters)

    def replace(match):
        mg = match.group(1).replace(delimiters[0], _DEFAULT_DELIMITER).replace(
            delimiters[1], _DEFAULT_DELIMITER
        )
        if use_aliases:
            emj = unicode_codes.EMOJI_ALIAS_UNICODE_ENGLISH.get(mg, mg)
        else:
            emj = EMOJI_UNICODE.get(mg, mg)
        if variant is None:
            return emj
        elif variant == "text_type":
            return emj+u'\uFE0E'
        elif variant == "emoji_type":
            return emj+u'\uFE0F'
    return pattern.sub(replace, string)


def demojize(
        string,
        use_aliases=False,
        delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER),
        language='en',
):
    """Replace unicode emoji in a string with emoji shortcodes. Useful for storage.
    :param string: String contains unicode characters. MUST BE UNICODE.
    :param use_aliases: (optional) Return emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) User delimiters other than _DEFAULT_DELIMITER
    :param language: Choose language of emoji name
        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(emoji.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up:
        >>> print(emoji.demojize(u"Unicode is tricky 😯", delimiters=("__", "__")))
        Unicode is tricky __hushed_face__
    """
    UNICODE_EMOJI = unicode_codes.UNICODE_EMOJI[language]

    def replace(match):
        codes_dict = unicode_codes.UNICODE_EMOJI_ALIAS_ENGLISH if use_aliases else UNICODE_EMOJI
        val = codes_dict.get(match.group(0), match.group(0))
        return delimiters[0] + val[1:-1] + delimiters[1]

    return re.sub(u'\ufe0f', '', (get_emoji_regexp(language).sub(replace, string)))


def get_emoji_regexp(language='en'):

    """Returns compiled regular expression that matches emojis defined in
    ``emoji.UNICODE_EMOJI_ALIAS``. The regular expression is only compiled once.
    """

    global _EMOJI_REGEXP
    # Build emoji regexp once
    EMOJI_UNICODE = unicode_codes.EMOJI_UNICODE[language]
    if _EMOJI_REGEXP is None:
        # Sort emojis by length to make sure multi-character emojis are
        # matched first
        emojis = sorted(EMOJI_UNICODE.values(), key=len, reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)
    return _EMOJI_REGEXP


def emoji_lis(string, language='en'):
    """
    Returns the location and emoji in list of dict format.
    >>> emoji.emoji_lis("Hi, I am fine. 😁")
    >>> [{'location': 15, 'emoji': '😁'}]
    """
    _entities = []

    for match in get_emoji_regexp(language).finditer(string):
        _entities.append({
            'location': match.start(),
            'emoji': match.group(),
        })

    return _entities


def distinct_emoji_lis(string):
    """Returns distinct list of emojis from the string."""
    distinct_list = list(
        {c for c in string if c in unicode_codes.UNICODE_EMOJI}
    )
    return distinct_list


def emoji_count(string):
    """Returns the count of emojis in a string."""
    return len(emoji_lis(string))
