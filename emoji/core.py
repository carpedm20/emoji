# -*- coding: UTF-8 -*-


"""
emoji.core
~~~~~~~~~~

Core components for emoji.

"""


import re
import sys

from emoji import unicode_codes


__all__ = ['emojize', 'demojize', 'get_emoji_regexp','emoji_list','replace_emoji', 'set_cldr', 'set_unicode','print_html']


PY2 = sys.version_info[0] is 2

_EMOJI_REGEXP = None
_DEFAULT_DELIMITER = "_"

def emojize(text, use_aliases=False, delimiters=(_DEFAULT_DELIMITER,_DEFAULT_DELIMITER)):

    """Replace emoji names in a text with unicode codes.

    :param text: string contains emoji names.
    :param use_aliases: (optional) Enable emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) Use delimiters other than _DEFAULT_DELIMITER
        >>> print(emoji.emojize("Python is fun _thumbsup_", use_aliases=True))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun _thumbs_up_"))
        Python is fun 👍
        >>> print(emoji.emojize("Python is fun ~~thumbs_up~~", delimiters = ("~~", "~~")))
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
        Python is fun _thumbs_up_sign_
        >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
        Unicode is tricky _hushed_face_
        >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8'), delimiters=("-->", "<--")))
        Unicode is tricky -->hushed_face<--
    """

    def replace(match):
        val = unicode_codes.UNICODE_EMOJI.get(match.group(0), match.group(0))
        #val[1:-1] we remove the colon before and after in the name and add the delimiters
        #the colons are present in the name in order to use the emojize funcion (see above)
        return delimiters[0] +  val[1:-1]  + delimiters[1] 

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
    [{'code': u'\U0001f601', 'location': (15, 16), 'name': u'beaming_face_with_smiling_eyes'}]

    """
    _entities = []
    def replace(match):
        l = match.span()
        c = match.group(0)
        n = unicode_codes.UNICODE_EMOJI.get(c, None)
        if n:
            _entities.append({"location": l, "code": c, "name":n})
        return c

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


def set_cldr():
    """
    Return complete set of emojis (CLDR names)
    """
    return set(unicode_codes.EMOJI_UNICODE.keys())


def set_unicode():
    """
    Return complete set of emojis (UNICODE)
    """
    return set(unicode_codes.UNICODE_EMOJI.keys())

def print_html(text, html_file="emoji.html"):
    """
    append string to emoji.html file (with emojis replaced by images so can be visualized)
    emoji.html will be created if it does not exist
    """
    with open(html_file,"a") as out_html:
        left = "<img src=\"https://raw.githubusercontent.com/fvancesco/emoji/master/utils/images_cldr/"
        right = ".png\" height=\"16\" width=\"16\">"
        replaced_text = demojize(text, delimiters=(left, right)) 
        out_html.write("<p>"+replaced_text+"</p>\n")    

skin_list = ['🏻','🏼','🏽','🏾','🏿']
def remove_skin(text):
    rx = '[' + re.escape(''.join(skin_list)) + ']'
    tx = re.sub(rx, '', text)
    return tx
