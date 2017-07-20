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

    >>> print(emoji.demojize(u"Python is fun 👍"))
    Python is fun :thumbs_up_sign:
    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
    Unicode is tricky :hushed_face:
    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8'), delimiters=(" __", "__ ")))
    Unicode is tricky __hushed_face__:

2) Return the location, the emoji unicode, and the CLDR Short Name in list of dic format. Note that the location is a span of indices (where the emoji charaters start and where they end) as some emojis are composed of more then one unicode charater.

.. code-block:: python

    >>> emoji.emoji_list("Hi, I am fine. 😁".decode('utf-8'))
    [{'cldr': u':grinning_face_with_smiling_eyes:', 'emoji': u'\U0001f601', 'location': (15, 16)}]
    >>> emoji.emoji_list("Hi, I am fine. 🤹🏻‍♂️".decode('utf-8'))
    [{'cldr': u':man_juggling_light_skin_tone:', 'emoji': u'\U0001f939\U0001f3fb\u200d\u2642\ufe0f', 'location': (15, 20)}]
    

3) Replace all emojis with "replacement" string. Default replacement is empty string, equivalent to removing all emojis

.. code-block:: python

    >>> emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'))
    >>> Hi, I am fine.
    >>> emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'), replacement='***')
    >>> Hi, I am fine. ***

4) From alias/name to emoji

.. code-block:: python

    >>> print(emoji.emojize('Python is :thumbs_up_sign:'))
    Python is 👍
    >>> print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
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

`Official unicode list <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__

`Word Embeddigs of Emojis (US, UK, ESP, ITA) <http://sempub.taln.upf.edu/tw/cosmopolitan/>`__

