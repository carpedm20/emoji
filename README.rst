Emoji
=====

Emoji library for Python.  This project is a fork of `karpedm20 <https://github.com/carpedm20/emoji>`__.
Tested on Python2.7

The entire set of Emoji codes is defined by the `unicode consortium <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__.

Current version in this project is v5 (last update: 20 July 2017)

Functionalities
------------
You need to "import emoji"

1) Replace each emoji with the CLDR Short Name

.. code-block:: python

    >> print(emoji.emojize('Python is :thumbs_up_sign:'))
    Python is 👍
    >> print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
    Python is 👍

2) Return the location, the emoji unicode, and the CLDR Short Name in list of dic format

.. code-block:: python

    >> emoji.emoji_list("Hi, I am fine. 😁".decode('utf-8'))
    [{'cldr': u':grinning_face_with_smiling_eyes:', 'emoji': u'\U0001f601', 'location': (15, 16)}]

3) Replace all emojis with "replacement" string. Default replacement is empty string, equivalent to removing all emojis

.. code-block:: python

    >> emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'), replacement='***')
    >> Hi, I am fine. ***

4) From alias/name to emoji

.. code-block:: python

    >> print(emoji.emojize('Python is :thumbs_up_sign:'))
    Python is 👍
    >> print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
    Python is 👍

Installation
------------

From master branch:

.. code-block:: console

    $ git clone https://github.com/fvancesco/emoji.git
    $ cd emoji
    $ python setup.py install


Link
----

`Emoji Cheat Sheet <http://www.emoji-cheat-sheet.com/>`__
`Official unicode list <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__
`Word Embeddig of Emojis (US, UK, ESP, ITA) <http://sempub.taln.upf.edu/tw/cosmopolitan/>`__

