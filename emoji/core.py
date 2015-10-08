# -*- coding: UTF-8 -*-


"""
emoji.core
~~~~~~~~~~

Core components for emoji.

"""


import re
import sys

from . import unicode_codes
from . import shortcuts

PY2 = sys.version_info[0] is 2

_EMOJI_REGEXP = None
_EMOJI_REGEXP_NOSPACE = None
_SHORTCUT_REGEXP = None

USE_ALIASES = False

NO_SPACE = False
USE_SHORTCUTS = False


def emojize(string, use_aliases=USE_ALIASES, no_space=NO_SPACE):

    """Replace emoji names in a string with unicode codes.

    :param string: String contains emoji names.
    :param use_aliases: (optional) Enable emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param no_space: (optional) Remove space characters for multi-character emojis.

        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :thumbs_up_sign:"))
        Python is fun 👍
    """

    pattern = re.compile(u'(:[a-zA-Z0-9\+\-_&.ô’Åéãíç]+:)')

    def replace(match):
        if use_aliases:
            val = unicode_codes.EMOJI_ALIAS_UNICODE.get(match.group(1), None)
        else:
            val = unicode_codes.EMOJI_UNICODE.get(match.group(1), None)
        if val:
            if no_space:
                return val.replace(u' ', u'')
            return val
        return match.group(1)

    return pattern.sub(replace, string)

def demojize(string, no_space=NO_SPACE, use_shortcuts=USE_SHORTCUTS):

    """Replace unicode emoji in a string with emoji shortcodes. Useful for storage.

    :param string: String contains unicode characters. MUST BE UNICODE.
    :param no_space: (optional) No space between characters in multi-character emojis.
    :param use_shortcuts: (optional) Replace shortcuts with emoji shortcodes.

        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbs_up_sign:"))
        Python is fun 👍
        >>> print(emoji.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up_sign:
        >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
        Unicode is tricky :hushed_face:
    """

    if use_shortcuts:
        def replace_shortcuts(match):
            return shortcuts.SHORTCUTS.get(match.group(1), match.group(1))
        string = get_shortcut_regexp().sub(replace_shortcuts,string)

    UNICODE_EMOJI = unicode_codes.UNICODE_EMOJI_NO_SPACE if no_space else unicode_codes.UNICODE_EMOJI
    def replace(match):
        return UNICODE_EMOJI.get(match.group(0), match.group(0))

    # Decode shortcuts
    string = get_emoji_regexp(no_space).sub(replace, string)

    return string

def get_emoji_regexp(no_space=NO_SPACE):

    """Returns compiled regular expression that matches emojis defined in
    ``emoji.UNICODE_EMOJI_ALIAS``. The regular expression is only compiled once.
    """

    global _EMOJI_REGEXP
    global _EMOJI_REGEXP_NOSPACE
    # Build emoji regexp once
    if (_EMOJI_REGEXP_NOSPACE if no_space else _EMOJI_REGEXP) is None:
        # Sort emojis by length to make sure mulit-character emojis are
        # matched first
        if no_space:
            values = [v.replace(' ', '') for v in unicode_codes.EMOJI_UNICODE.values()]
        else:
            values = unicode_codes.EMOJI_UNICODE.values()
        emojis = sorted(values, key=len,
                        reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        regexp = re.compile(pattern)
        if no_space:
            _EMOJI_REGEXP_NOSPACE = regexp
        else:
            _EMOJI_REGEXP = regexp
    return _EMOJI_REGEXP_NOSPACE if no_space else _EMOJI_REGEXP



def get_shortcut_regexp():

    """Returns compiled regular expression that matches shortcuts defined in
    ``shortcuts.SHORTCUTS``. The regular expression is only compiled once.
    """

    global _SHORTCUT_REGEXP
    # Build shortcut regexp once
    if _SHORTCUT_REGEXP is None:
        values = shortcuts.SHORTCUTS.keys()
        values = sorted(values, key=len, reverse=True)
        pattern = u'(?<=[\ |^])(' + u'|'.join(re.escape(u) for u in values) + u')(?=(\ |\)|\.|$))'
        _SHORTCUT_REGEXP = re.compile(pattern)
    return _SHORTCUT_REGEXP