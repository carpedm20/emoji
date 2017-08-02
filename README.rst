Emoji
=====

Emoji library for Python.  This project is a fork of `karpedm20 <https://github.com/carpedm20/emoji>`__.
Tested on Python2.7

The entire set of Emoji codes is defined by the `unicode consortium <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__.
Current emoji version used in this project is **v5** (last update: 20 July 2017)

Functionalities
------------
*(All examples assume you already imported emoji)*

1. **Replace each emoji with the CLDR Short Name**

Default delimiter is colon *:CLDR_Short_Name:* (see `this <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__ for the CLDR names).

.. code-block:: python

    >>> print(emoji.demojize("Python is fun 👍".decode('utf-8')))
    Python is fun :thumbs_up_sign:
    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
    Unicode is tricky :hushed_face:
    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8'), delimiters=("-|", "|-")))
    Unicode is tricky -|hushed_face|-
    
2. **Replace alias/name with emoji**

See `this <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__ for the CLDR names and `this <http://www.emoji-cheat-sheet.com/>`__ for the aliases.

.. code-block:: python

    >>> print(emoji.emojize('Python is :smiling_face_with_sunglasses:'))
    Python is 😎
    >>> print(emoji.emojize('Python is :sunglasses:', use_aliases=True))
    Python is 😎

3. **Return a list of emoji infos**. 

Return a list of the emojis included in the text, organised in a list of dictionaries, where the following infos are encoded for each emoji: 

* The emoji Unicode (key: code)
* The location span (key: location)
* The CLDR Short Name (key: name)

*Note: some emojis are composed of more than one Unicode character.*

.. code-block:: python

    >>> emoji.emoji_list("Hi, I am fine 😁. This is a complex emoji 🤹🏻‍♂️".decode('utf-8'))
    [{'code': u'\U0001f601', 'location': (14, 15), 'name': u'beaming_face_with_smiling_eyes'},
     {'code': u'\U0001f939\U0001f3fb\u200d\u2642\ufe0f', 'location': (41, 46), 'name': u'man_juggling_light_skin_tone'}]


4. **Replace all emojis with "replacement" string**. 

Default replacement is empty string, equivalent to removing all emojis.

.. code-block:: python

    >>> emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'))
    Hi, I am fine.
    >>> emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'), replacement='***')
    Hi, I am fine. ***


Installation
------------

From master branch:

.. code-block:: console

    $ git clone https://github.com/fvancesco/emoji.git
    $ cd emoji
    $ python setup.py install


Utils
------------
In the folder *utils/* you can find a program to download the code and the images (Apple rendering) of the last emojis. The program will save the emoji images in two folders, where the images are named with the Unicode code in one case, and with the CLDR name in the other case. (for instance this emoji 👍 is saved as images_name/thumbs_up.png and images_code/U0001F44D.png)

Links
----

`Official unicode list <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__

`Word Embeddigs of Emojis (US, UK, ESP, ITA) <http://sempub.taln.upf.edu/tw/cosmopolitan/>`__
