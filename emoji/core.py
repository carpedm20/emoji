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
    'replace_emoji', 'is_emoji', 'version',
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
        version=None,
        handle_version=None
):
    """Replace emoji names in a string with unicode codes.
        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbsup:", use_aliases=True))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun __thumbs_up__", delimiters = ("__", "__")))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun :red_heart:",variant="text_type"))
        Python is fun ❤
        >>> print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
        Python is fun ❤️ #red heart, not black heart

    :param string: String contains emoji names.
    :param use_aliases: (optional) Enable emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) Use delimiters other than _DEFAULT_DELIMITER
    :param variant: (optional) Choose variation selector between "base"(None), VS-15 ("text_type") and VS-16 ("emoji_type")
    :param language: Choose language of emoji name
    :param version: (optional) Max version. If set to an Emoji Version,
        all emoji above this version will be ignored.
    :param handle_version: (optional) Replace the emoji above ``version``
        instead of ignoring it. handle_version can be either a string or a
        callable; If it is a callable, it's passed the unicode emoji and the
        data dict from emoji.EMOJI_DATA and must return a replacement string
        to be used::

            handle_version(u'\\U0001F6EB', {
                'en' : ':airplane_departure:',
                'status' : fully_qualified,
                'E' : 1,
                'alias' : [u':flight_departure:'],
                'de': u':abflug:',
                'es': u':avión_despegando:',
                ...
            })

    :raises ValueError: if ``variant`` is neither None, 'text_type' or 'emoji_type'

    """
    EMOJI_UNICODE = unicode_codes.EMOJI_UNICODE[language]
    pattern = re.compile(u'(%s[\\w\\-&.’”“()!#*+?–,/]+%s)' % delimiters, flags=re.UNICODE)

    def replace(match):
        mg = match.group(1).replace(delimiters[0], _DEFAULT_DELIMITER).replace(
            delimiters[1], _DEFAULT_DELIMITER
        )
        if use_aliases:
            emj = unicode_codes.EMOJI_ALIAS_UNICODE_ENGLISH.get(mg)
        else:
            emj = EMOJI_UNICODE.get(mg)

        if emj is None:
            return mg

        if version is not None:
            if emj in unicode_codes.EMOJI_DATA and unicode_codes.EMOJI_DATA[emj]['E'] > version:
                if callable(handle_version):
                    return handle_version(emj, unicode_codes.EMOJI_DATA[emj])
                elif handle_version is not None:
                    return str(handle_version)
                else:
                    return ''

        if variant is None or 'variant' not in unicode_codes.EMOJI_DATA[emj]:
            return emj

        if emj[-1] == u'\uFE0E' or emj[-1] == u'\uFE0F':
            # Remove an existing variant
            emj = emj[0:-1]
        if variant == "text_type":
            return emj + u'\uFE0E'
        elif variant == "emoji_type":
            return emj + u'\uFE0F'
        else:
            raise ValueError("Parameter 'variant' must be either None, 'text_type' or 'emoji_type'")

    return pattern.sub(replace, string)


def demojize(
        string,
        use_aliases=False,
        delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER),
        language='en',
        version=None,
        handle_version=None
):
    """Replace unicode emoji in a string with emoji shortcodes. Useful for storage.
        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(emoji.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up:
        >>> print(emoji.demojize(u"Unicode is tricky 😯", delimiters=("__", "__")))
        Unicode is tricky __hushed_face__

    :param string: String contains unicode characters. MUST BE UNICODE.
    :param use_aliases: (optional) Return emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) User delimiters other than ``_DEFAULT_DELIMITER``
    :param language: (optional) Choose language of emoji name
    :param version: (optional) Max version. If set to an Emoji Version,
        all emoji above this version will be removed.
    :param handle_version: (optional) Replace the emoji above ``version``
        instead of removing it. handle_version can be either a string or a
        callable ``handle_version(emj: str, data: dict) -> str``; If it is
        a callable, it's passed the unicode emoji and the data dict from
        emoji.EMOJI_DATA and must return a replacement string  to be used.
        The passed data is in the form of::

            handle_version(u'\\U0001F6EB', {
                'en' : ':airplane_departure:',
                'status' : fully_qualified,
                'E' : 1,
                'alias' : [u':flight_departure:'],
                'de': u':abflug:',
                'es': u':avión_despegando:',
                ...
            })

    """

    codes_dict = unicode_codes.UNICODE_EMOJI_ALIAS_ENGLISH if use_aliases else unicode_codes.UNICODE_EMOJI[language]

    def replace(match):
        emj = match.group(0)
        val = codes_dict.get(emj)
        if val is None:
            return emj
        if version is not None:
            if emj in unicode_codes.EMOJI_DATA and unicode_codes.EMOJI_DATA[emj]['E'] > version:
                if callable(handle_version):
                    return handle_version(emj, unicode_codes.EMOJI_DATA[emj])
                elif handle_version is not None:
                    return str(handle_version)
                else:
                    return ''
        return delimiters[0] + val[1:-1] + delimiters[1]

    return get_emoji_regexp().sub(replace, string).replace(u'\ufe0e', '').replace(u'\ufe0f', '')


def replace_emoji(string, replace='', language=None, version=-1):
    """Replace unicode emoji in a customizable string.

    :param string: String contains unicode characters. MUST BE UNICODE.
    :param replace: (optional) replace can be either a string or a callable;
        If it is a callable, it's passed the unicode emoji and the data dict from
        emoji.EMOJI_DATA and must return a replacement string to be used.
        replace(str, dict) -> str
    :param version: (optional) Max version. If set to an Emoji Version,
        only emoji above this version will be replaced.
    :param language: (optional) Parameter is no longer used
    """

    if version <= 0 and not callable(replace):
        return get_emoji_regexp().sub(replace, string).replace(u'\ufe0e', '').replace(u'\ufe0f', '')

    def replace_fct(match):
        emj = match.group(0)

        if emj in unicode_codes.EMOJI_DATA and unicode_codes.EMOJI_DATA[emj]['E'] > version:
            if callable(replace):
                return replace(emj, unicode_codes.EMOJI_DATA[emj])
            else:
                return str(replace)
        return emj

    return get_emoji_regexp().sub(replace_fct, string).replace(u'\ufe0e', '').replace(u'\ufe0f', '')


def get_emoji_regexp(language=None):
    """Returns compiled regular expression that matches all emojis defined in
    ``emoji.EMOJI_DATA``. The regular expression is only compiled once.

    :param language: (optional) Parameter is no longer used
    """

    global _EMOJI_REGEXP
    # Build emoji regexp once
    if _EMOJI_REGEXP is None:
        # Sort emojis by length to make sure multi-character emojis are
        # matched first
        emojis = sorted(unicode_codes.EMOJI_DATA, key=len, reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)
    return _EMOJI_REGEXP


def emoji_lis(string, language=None):
    """Returns the location and emoji in list of dict format.
        >>> emoji.emoji_lis("Hi, I am fine. 😁")
        >>> [{'location': 15, 'emoji': '😁'}]

    :param language: (optional) Parameter is no longer used
    """
    _entities = []

    for match in get_emoji_regexp().finditer(string):
        _entities.append({
            'location': match.start(),
            'emoji': match.group(),
        })

    return _entities


def distinct_emoji_lis(string, language=None):
    """Returns distinct list of emojis from the string.

    :param language: (optional) Parameter is no longer used
    """
    distinct_list = list(
        {e['emoji'] for e in emoji_lis(string)}
    )
    return distinct_list


def emoji_count(string):
    """Returns the count of emojis in a string."""
    return len(emoji_lis(string))


def is_emoji(string):
    """Returns True if the string is an emoji"""
    return string in unicode_codes.EMOJI_DATA


def version(string):
    """Returns the Emoji Version of the emoji.
      See http://www.unicode.org/reports/tr51/#Versioning for more information.
        >>> emoji.version("😁")
        >>> 0.6
        >>> emoji.version(":butterfly:")
        >>> 3

    :param string: An emoji or a text containig an emoji
    :raises ValueError: if ``string`` does not contain an emoji
    """

    # Try dictionary lookup
    if string in unicode_codes.EMOJI_DATA:
        return unicode_codes.EMOJI_DATA[string]['E']

    if string in unicode_codes.EMOJI_UNICODE['en']:
        emj_code = unicode_codes.EMOJI_UNICODE['en'][string]
        if emj_code in unicode_codes.EMOJI_DATA:
            return unicode_codes.EMOJI_DATA[emj_code]['E']

    # Try to find first emoji in string
    version = []
    def f(e, emoji_data):
        version.append(emoji_data['E'])
        return ''
    replace_emoji(string, replace=f, version=-1)
    if version:
        return version[0]
    emojize(string, use_aliases=True, version=-1, handle_version=f)
    if version:
        return version[0]
    for lang_code in unicode_codes.EMOJI_UNICODE:
        emojize(string, language=lang_code, version=-1, handle_version=f)
        if version:
            return version[0]

    raise ValueError("No emoji found in string")
