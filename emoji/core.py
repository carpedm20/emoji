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


PY2 = sys.version_info[0] == 2

_EMOJI_REGEXP = None
_DEFAULT_DELIMITER = ":"

def emojize(string, use_aliases=False, delimiters=(_DEFAULT_DELIMITER,_DEFAULT_DELIMITER)):

    """Replace emoji names in a string with unicode codes.

    :param string: String contains emoji names.
    :param use_aliases: (optional) Enable emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) Use delimiters other than _DEFAULT_DELIMITER
        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun __thumbs_up__", delimiters = ("__", "__")))
        Python is fun 👍
    """

    pattern = re.compile(u'(%s[a-zA-Z0-9\\+\\-_&.ô’Åéãíç()!#*]+%s)' % delimiters)

    def replace(match):
        mg = match.group(1).replace(delimiters[0], _DEFAULT_DELIMITER).replace(delimiters[1], _DEFAULT_DELIMITER)
        if use_aliases:
            return unicode_codes.EMOJI_ALIAS_UNICODE.get(mg, mg)
        else:
            return unicode_codes.EMOJI_UNICODE.get(mg, mg)

    return pattern.sub(replace, string)


def demojize(string, use_aliases=False, delimiters=(_DEFAULT_DELIMITER,_DEFAULT_DELIMITER)):

    """Replace unicode emoji in a string with emoji shortcodes. Useful for storage.
    :param string: String contains unicode characters. MUST BE UNICODE.
    :param use_aliases: (optional) Return emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) User delimiters other than _DEFAULT_DELIMITER
        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(emoji.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up:
        >>> print(emoji.demojize(u"Unicode is tricky 😯", delimiters=(" __", "__ ")))
        Unicode is tricky :hushed_face:
    """

    def replace(match):
        codes_dict = unicode_codes.UNICODE_EMOJI_ALIAS if use_aliases else unicode_codes.UNICODE_EMOJI
        val = codes_dict.get(match.group(0), match.group(0))
        return delimiters[0] + val[1:-1] + delimiters[1]

    return re.sub(u'\ufe0f','',(get_emoji_regexp().sub(replace, string)))


def get_emoji_regexp():

    """Returns compiled regular expression that matches emojis defined in
    ``emoji.UNICODE_EMOJI_ALIAS``. The regular expression is only compiled once.
    """

    global _EMOJI_REGEXP
    # Build emoji regexp once
    if _EMOJI_REGEXP is None:
        # Sort emojis by length to make sure multi-character emojis are
        # matched first
        emojis = sorted(unicode_codes.EMOJI_UNICODE.values(), key=len,
                        reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)
    return _EMOJI_REGEXP

def emoji_lis(string):
    """Return the location and emoji in list of dic format
    >>>emoji.emoji_lis("Hi, I am fine. 😁")
    >>>[{'location': 15, 'emoji': '😁'}]
    """
    _entities = []
    for pos,c in enumerate(string):
        if c in unicode_codes.UNICODE_EMOJI:
            _entities.append({
                "location":pos,
                "emoji": c
                })
    return _entities

def emoji_count(string):
   """Returns the count of emojis in a string"""
   c=0
   for i in string:
     if i in unicode_codes.UNICODE_EMOJI:
	      c=c+1
   return(c)

