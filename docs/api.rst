.. _api:

API Reference
~~~~~~~~~~~~~

.. py:module:: emoji
   :noindex:


+-------------------------------+--------------------------------------------------------------+
| Table of Contents             |                                                              |
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


.. automodule:: emoji
   :members:


EMOJI_DATA
------------

.. data:: EMOJI_DATA
   :type: dict
   :canonical: emoji.unicode_codes.data_dict.EMOJI_DATA

     Contains all emoji as keys and their names, Unicode version and status

     .. code-block:: python

       EMOJI_DATA = {
         '🥇': {
             'en' : ':1st_place_medal:',
             'status' : emoji.STATUS["fully_qualified"],
             'E' : 3,
             'de': ':goldmedaille:',
             'es': ':medalla_de_oro:',
             'fr': ':médaille_d’or:',
             'pt': ':medalha_de_ouro:',
             'it': ':medaglia_d’oro:'
         },
         ...
       }

**Source code:** `emoji/unicode_codes/data_dict.py <https://github.com/carpedm20/emoji/raw/master/emoji/unicode_codes/data_dict.py>`_ **(2MB)**

Emoji status
------------

.. data:: STATUS
   :type: dict
   :canonical: emoji.unicode_codes.data_dict.STATUS

     The status values that are used in :data:`emoji.EMOJI_DATA`.

     For more information on the meaning of these values see http://www.unicode.org/reports/tr51/#Emoji_Implementation_Notes

   .. literalinclude:: ../emoji/unicode_codes/data_dict.py
      :language: python
      :start-at: component =
      :end-before: EMOJI_DATA
      :caption: emoji/unicode_codes/data_dict.py


.. _Emoji version:

Emoji version
-------------

Every emoji in :data:`emoji.EMOJI_DATA` has a version number. The number refers to the release of
that emoji in the Unicode Standard.
It is stored in the key ``'E'``. For example the emoji 🥇 ``:1st_place_medal:`` is version
``E3.0`` that is Emoji 3.0 or Unicode 9.0:

>>> emoji.EMOJI_DATA['🥇']['E']
3

For more information see http://www.unicode.org/reports/tr51/#Versioning

The following table lists all versions, the number that is used in :data:`emoji.EMOJI_DATA` in
the "Data File Comment" column:

.. literalinclude:: ../emoji/unicode_codes/data_dict.py
   :start-after: emoji_data_files.py
   :end-before: """
   :caption: Unicode/Emoji Version (emoji/unicode_codes/data_dict.py)
   :dedent: 2

