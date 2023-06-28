.. emoji documentation master file, created by sphinx-quickstart.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. py:module:: emoji
   :noindex:

.. A setup code block. This code is not shown in the output for other builders,
   but executed before the doctests of the group(s) it belongs to.
.. testsetup:: *

    import emoji
    from pprint import pprint


emoji
=====

Release v\ |version|. (:ref:`Installation <install>`)

emoji supports Python 3.6+. The last version to support Python 2.7 and 3.5 was v2.4.0.

.. contents:: Table of Contents

Usage and Examples
------------------

The main purpose of this package is converting Unicode emoji to emoji names and vice
versa with :func:`emojize` and :func:`demojize`.

The entire set of Emoji codes as defined by the `Unicode consortium <https://unicode.org/emoji/charts/full-emoji-list.html>`__
is supported in addition to a bunch of `aliases <https://www.webfx.com/tools/emoji-cheat-sheet/>`__.
By default, only the official list is enabled but doing ``emoji.emojize(language='alias')``
enables both the full list and aliases.


.. doctest::

    >>> print(emoji.emojize('Python is :thumbs_up:'))
    Python is 👍
    >>> print(emoji.emojize('Python is :thumbsup:', language='alias'))
    Python is 👍
    >>> print(emoji.demojize('Python is 👍'))
    Python is :thumbs_up:
    >>> print(emoji.emojize("Python is fun :red_heart:", variant="text_type"))
    Python is fun ❤︎
    >>> print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
    Python is fun ❤️

..

Languages
^^^^^^^^^

By default, the language is English (``language='en'``) but  also supported languages are:

Spanish (``'es'``), Portuguese (``'pt'``), Italian (``'it'``), French (``'fr'``), German (``'de'``), Farsi/Persian (``'fa'``)

.. doctest::

    >>> print(emoji.emojize('Python es :pulgar_hacia_arriba:', language='es'))
    Python es 👍
    >>> print(emoji.demojize('Python es 👍', language='es'))
    Python es :pulgar_hacia_arriba:
    >>> print(emoji.emojize("Python é :polegar_para_cima:", language='pt'))
    Python é 👍
    >>> print(emoji.demojize("Python é 👍", language='pt'))
    Python é :polegar_para_cima:

..

Extracting emoji
^^^^^^^^^^^^^^^^

The function :func:`analyze` finds all emoji in string and yields the emoji
together with its position and the available meta information about the emoji.

:func:`analyze` returns a generator that yields each emoji, so you need to iterate or
convert the output to a list.

.. doctest::

    >>> first_token = next(emoji.analyze('Python is 👍'))
    Token(chars='👍', value=EmojiMatch(👍, 10:11))
    >>> emoji_match = first_token.value
    EmojiMatch(👍, 10:11)
    >>> emoji_match.data
    {'en': ':thumbs_up:', 'status': 2, 'E': 0.6, 'alias': [':thumbsup:', ':+1:'], 'variant': True, 'de': ':daumen_hoch:', 'es': ':pulgar_hacia_arriba:', 'fr': ':pouce_vers_le_haut:', 'ja': ':サムズアップ:', 'ko': ':올린_엄지:', 'pt': ':polegar_para_cima:', 'it': ':pollice_in_su:', 'fa': ':پسندیدن:', 'id': ':jempol_ke_atas:', 'zh': ':拇指向上:'}
    >>> list(emoji.analyze('A 👩‍🚀 aboard a 🚀'))
    [Token(chars='👩\u200d🚀', value=EmojiMatch(👩‍🚀, 2:5)), Token(chars='🚀', value=EmojiMatch(🚀, 15:16))]
    >>> list(emoji.analyze('A👩‍🚀B🚀', non_emoji=True))
    [Token(chars='A', value='A'), Token(chars='👩\u200d🚀', value=EmojiMatch(👩‍🚀, 1:4)), Token(chars='B', value='B'), Token(chars='🚀', value=EmojiMatch(🚀, 5:6))]
..

The parameter ``join_emoji`` controls whether `non-RGI emoji <#non-rgi-zwj-emoji>`_  are handled as a single token or as multiple emoji:

.. doctest::

    >>> list(emoji.analyze('👨‍👩🏿‍👧🏻‍👦🏾', join_emoji=True))
    [Token(chars='👨\u200d👩🏿\u200d👧🏻\u200d👦🏾', value=EmojiMatchZWJNonRGI(👨‍👩🏿‍👧🏻‍👦🏾, 0:10))]

    >>> list(emoji.analyze('👨‍👩🏿‍👧🏻‍👦🏾', join_emoji=False))
    [Token(chars='👨', value=EmojiMatch(👨, 0:1)), Token(chars='👩🏿', value=EmojiMatch(👩🏿, 2:4)), Token(chars='👧🏻', value=EmojiMatch(👧🏻, 5:7)), Token(chars='👦🏾', value=EmojiMatch(👦🏾, 8:10))]

..


The function :func:`emoji_list` finds all emoji in string and their position.
Keep in mind that an emoji can span over multiple characters:

.. doctest::

    >>> emoji.emoji_list('Python is 👍')
    [{'match_start': 10, 'match_end': 11, 'emoji': '👍'}]
    >>> emoji.emoji_list('A 👩‍🚀 aboard a 🚀')
    [{'match_start': 2, 'match_end': 5, 'emoji': '👩‍🚀'}, {'match_start': 15, 'match_end': 16, 'emoji': '🚀'}]

..

To retrieve the distinct set of emoji from a string, use :func:`distinct_emoji_list`:

.. code-block:: python

    >>> emoji.distinct_emoji_list('Some emoji: 🌍, 😂, 😃, 😂, 🌍, 🌦️')
    ['😃', '😂', '🌦️', '🌍']

..

To count the number of emoji in a string, use :func:`emoji_count`:

.. doctest::

    >>> emoji.emoji_count('Some emoji: 🌍, 😂, 😃, 😂, 🌍, 🌦️')
    6
    >>> emoji.emoji_count('Some emoji: 🌍, 😂, 😃, 😂, 🌍, 🌦️', unique=True)
    4

..

You can check if a string is a single, valid emoji with :func:`is_emoji`

.. doctest::

    >>> emoji.is_emoji('🌍')
    True
    >>> emoji.is_emoji('🌍😂')
    False
    >>> emoji.is_emoji('test')
    False

..

While dealing with emojis, it is generally a bad idea to look at individual characters.
Unicode contains modifier characters, such as variation selectors, which are not emojis themselves
and modify the preceding emoji instead. You can check if a string has only emojis in it with :func:`purely_emoji`

.. doctest::

    >>> '\U0001f600\ufe0f'
    '😀'
    >>> emoji.is_emoji('\U0001f600\ufe0f')
    False
    >>> emoji.is_emoji('\U0001f600')
    True
    >>> emoji.is_emoji('\ufe0f')
    False
    >>> emoji.purely_emoji('\U0001f600\ufe0f')
    True

..

To get more information about an emoji, you can look it up in the :data:`EMOJI_DATA` dict:

.. testcode::

    pprint(emoji.EMOJI_DATA['🌍'])

..

.. testoutput::

    {'E': 0.7,
     'alias': [':earth_africa:'],
     'de': ':globus_mit_europa_und_afrika:',
     'en': ':globe_showing_Europe-Africa:',
     'es': ':globo_terráqueo_mostrando_europa_y_áfrica:',
     'fr': ':globe_tourné_sur_l’afrique_et_l’europe:',
     'it': ':europa_e_africa:',
     'pt': ':globo_mostrando_europa_e_áfrica:',
     'status': 2,
     'variant': True}

..

``'E'`` is the :ref:`Emoji version <Emoji version>`.

``'status'`` is defined in :data:`STATUS`. For example ``2`` corresponds
to ``'fully_qualified'``. More information on the meaning can be found in the
Unicode Standard http://www.unicode.org/reports/tr51/#Emoji_Variation_Selector_Notes


Replacing and removing emoji
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With :func:`replace_emoji` you can replace, filter, escape or remove emoji in a string:

.. code-block:: python

    >>> emoji.replace_emoji('Python is 👍', replace='')
    'Python is '

    >>> emoji.replace_emoji('Python is 👍', replace='👎')
    'Python is 👎'

    >>> def unicode_escape(chars, data_dict):
    >>>     return chars.encode('unicode-escape').decode()
    >>> emoji.replace_emoji('Python is 👍', replace=unicode_escape)
    'Python is \U0001f44d'

    >>> def xml_escape(chars, data_dict):
    >>>     return chars.encode('ascii', 'xmlcharrefreplace').decode()
    >>> emoji.replace_emoji('Python is 👍', replace=xml_escape)
    'Python is &#128077;'

    >>> emoji.replace_emoji('Python is 👍', replace=lambda chars, data_dict: chars.encode('ascii', 'namereplace').decode())
    'Python is \N{THUMBS UP SIGN}'

    >>> emoji.replace_emoji('Python is 👍', replace=lambda chars, data_dict: data_dict['es'])
    'Python is :pulgar_hacia_arriba:'

..

Emoji versions
^^^^^^^^^^^^^^

The parameter ``version`` in :func:`replace_emoji` allows to replace only emoji above
that :ref:`Emoji version <Emoji version>` to prevent incompatibility with older platforms.

For the functions :func:`emojize` and :func:`demojize` the parameter ``version`` will
replace emoji above the specified version with the value of the parameter ``handle_version``.
It defaults to an empty string, but can be set to any string or a function that returns a string.

For example the ``:croissant:`` 🥐 emoji was added in Emoji 3.0 (Unicode 9.0) in 2016 and
``:T-Rex:`` 🦖 was added later in Emoji 5.0 (Unicode 10.0) in 2017:

.. doctest::

    >>> emoji.replace_emoji('A 🦖 is eating a 🥐', replace='[Unsupported emoji]', version=1.0)
    'A [Unsupported emoji] is eating a [Unsupported emoji]'

    >>> emoji.replace_emoji('A 🦖 is eating a 🥐', replace=lambda chars, data_dict: data_dict['en'], version=3.0)
    'A :T-Rex: is eating a 🥐'

    >>> emoji.emojize('A :T-Rex: is eating a :croissant:', version=3.0)
    'A  is eating a 🥐'

    >>> emoji.emojize('A :T-Rex: is eating a :croissant:', version=3.0, handle_version='[Unsupported emoji]')
    'A [Unsupported emoji] is eating a 🥐'

    >>> emoji.demojize('A 🦖 is eating a 🥐', version=3.0)
    'A  is eating a :croissant:'

    >>> emoji.replace_emoji('A 🦖 is eating a 🥐', replace='', version=5.0)
    'A 🦖 is eating a 🥐'

..

You can find the version of an emoji with :func:`version`:

.. doctest::

    >>> emoji.version('🥐')
    3
    >>> emoji.version('🏌️‍♀️')
    4
    >>> emoji.version('🦖')
    5
..


Non-RGI ZWJ emoji
^^^^^^^^^^^^^^^^^

Some emoji contain multiple persons and each person can have an individual skin tone.

Unicode supports `Multi-Person Skin Tones <http://www.unicode.org/reports/tr51/#multiperson_skintones>`__ as of Emoji 11.0.
Skin tones can be add to the nine characters known as `Multi-Person Groupings <https://www.unicode.org/reports/tr51/#MultiPersonGroupingsTable>`__.

Multi-person groups with different skin tones can be represented with Unicode, but are not yet RGI (recommended for general interchange). This means Unicode.org recommends not to show them in emoji keyboards.
However some browser and platforms already support some of them:

.. figure:: 1F468-200D-1F469-1F3FF-200D-1F467-1F3FB-200D-1F466-1F3FE.png
   :height: 4em
   :alt: A family emoji 👨‍👩🏿‍👧🏻‍👦🏾 with four different skin tone values

   The emoji 👨‍👩🏿‍👧🏻‍👦🏾 as it appears in Firefox on Windows 11

   It consists of eleven Unicode characters, four person emoji, four different skin tones joined together by three ``\u200d`` **Z**\ ero-\ **W**\ idth **J**\ oiner:

   #. 👨 ``:man:``
   #. 🏽 ``:medium_skin_tone:``
   #. ``\u200d``
   #. 👩 ``:woman:``
   #. 🏿 ``:dark_skin_tone:``
   #. ``\u200d``
   #. 👧 ``:girl:``
   #. 🏻 ``:light_skin_tone:``
   #. ``\u200d``
   #. 👦 ``:boy:``
   #. 🏾 ``:medium-dark_skin_tone:``

   On platforms that don't support it, it might appear as separate emoji: 👨🏽👩🏿👧🏻👦🏾

In the module configuration :class:`config` you can control how such emoji are handled.



Migrating to version 2.0.0
--------------------------

There a two major, breaking changes in version 2.0.0

non-English short codes
^^^^^^^^^^^^^^^^^^^^^^^

The names of emoji in non-English languages have changed, because the data files were updated to
the new version 41. See https://cldr.unicode.org/index/downloads.

That means some ``:short-code-emoji:`` with non-English names will no longer work in 2.0.0.
:func:`emojize` will ignore the old codes.

This may be a problem if you have previously stored ``:short-code-emoji:`` with non-English names
for example in a database or if your users have stored them.

Regular expression
^^^^^^^^^^^^^^^^^^

The function ``get_emoji_regexp()`` was removed in 2.0.0. Internally the module no longer uses
a regular expression when scanning for emoji in a string (e.g. in :func:`demojize`).

The regular expression was slow in Python 3 and it failed to correctly find certain combinations
of long emoji (emoji consisting of multiple Unicode codepoints).

If you used the regular expression to remove emoji from strings, you can use :func:`replace_emoji`
as shown in the examples above.

If you want to extract emoji from strings, you can use :func:`emoji_list` as a replacement.

If you want to keep using a regular expression despite its problems, you can create the
expression yourself like this:

.. testcode::

    import re
    import emoji

    def get_emoji_regexp():
        # Sort emoji by length to make sure multi-character emojis are
        # matched first
        emojis = sorted(emoji.EMOJI_DATA, key=len, reverse=True)
        pattern = '(' + '|'.join(re.escape(u) for u in emojis) + ')'
        return re.compile(pattern)

    exp = get_emoji_regexp()
    print(exp.sub(repl='[emoji]', string='A 🏌️‍♀️ is eating a 🥐'))
..

Output:

.. testoutput::

    A [emoji] is eating a [emoji]

..


Common problems
---------------

.. code-block::

    UnicodeWarning: Unicode unequal comparison failed to convert both arguments to Unicode - interpreting them as being unequal

..

This exception is thrown in Python 2.7 if you passed a ``str`` string instead of a
``unicode`` string.
You should only pass Unicode strings to this module.

See https://python.readthedocs.io/en/v2.7.2/howto/unicode.html#the-unicode-type for more
information on Unicode in Python 2.7.


The API documentation
---------------------

Reference documentation of all functions and properties in the module:

.. toctree::
   :titlesonly:

   api

+-------------------------------+--------------------------------------------------------------+
| API Reference                 |                                                              |
+===============================+==============================================================+
| **Functions:**                |                                                              |
+-------------------------------+--------------------------------------------------------------+
| :func:`emojize`               | Replace emoji names with Unicode codes                       |
+-------------------------------+--------------------------------------------------------------+
| :func:`demojize`              | Replace Unicode emoji with emoji shortcodes                  |
+-------------------------------+--------------------------------------------------------------+
| :func:`analyze`               | Find Unicode emoji in a string                               |
+-------------------------------+--------------------------------------------------------------+
| :func:`replace_emoji`         | Replace Unicode emoji with a customizable string             |
+-------------------------------+--------------------------------------------------------------+
| :func:`emoji_list`            | Location of all emoji in a string                            |
+-------------------------------+--------------------------------------------------------------+
| :func:`distinct_emoji_list`   | Distinct list of emojis in the string                        |
+-------------------------------+--------------------------------------------------------------+
| :func:`emoji_count`           | Number of emojis in a string                                 |
+-------------------------------+--------------------------------------------------------------+
| :func:`is_emoji`              | Check if a string/character is a single emoji                |
+-------------------------------+--------------------------------------------------------------+
| :func:`purely_emoji`          | Check if a string contains only emojis                       |
+-------------------------------+--------------------------------------------------------------+
| :func:`version`               | Find Unicode/Emoji version of an emoji                       |
+-------------------------------+--------------------------------------------------------------+
| **Module variables:**         |                                                              |
+-------------------------------+--------------------------------------------------------------+
| :data:`EMOJI_DATA`            | Dict of all emoji                                            |
+-------------------------------+--------------------------------------------------------------+
| :data:`STATUS`                | Dict of Unicode/Emoji status                                 |
+-------------------------------+--------------------------------------------------------------+
| :class:`config`               | Module wide configuration                                    |
+-------------------------------+--------------------------------------------------------------+
| **Classes:**                  |                                                              |
+-------------------------------+--------------------------------------------------------------+
| :class:`EmojiMatch`           |                                                              |
+-------------------------------+--------------------------------------------------------------+
| :class:`EmojiMatchZWJ`        |                                                              |
+-------------------------------+--------------------------------------------------------------+
| :class:`EmojiMatchZWJNonRGI`  |                                                              |
+-------------------------------+--------------------------------------------------------------+
| :class:`Token`                |                                                              |
+-------------------------------+--------------------------------------------------------------+


Links
=====

**Overview of all emoji:**

`https://carpedm20.github.io/emoji/ <https://carpedm20.github.io/emoji/>`__

(auto-generated list of the emoji that are supported by the current version of this package)

**For English:**

`Emoji Cheat Sheet <https://www.webfx.com/tools/emoji-cheat-sheet/>`__

`Official Unicode list <http://www.unicode.org/emoji/charts/full-emoji-list.html>`__

**For Spanish:**

`Unicode list <https://emojiterra.com/es/lista-es/>`__

**For Portuguese:**

`Unicode list <https://emojiterra.com/pt/lista/>`__

**For Italian:**

`Unicode list <https://emojiterra.com/it/lista-it/>`__

**For French:**

`Unicode list <https://emojiterra.com/fr/liste-fr/>`__

**For German:**

`Unicode list <https://emojiterra.com/de/liste/>`__



Indices and tables
==================

.. toctree::
   :maxdepth: 2

   install

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
