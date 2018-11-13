Emoji
=====

Emoji library for Python.  This project is a fork of `karpedm20 <https://github.com/carpedm20/emoji>`__.

The entire set of Emoji codes is defined by the `unicode consortium <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__.
Current emoji version used in this project is **v11** (last update: 13th of November 2018)

Functionalities
------------
*(All examples assume you already imported emoji and that you use Python2.7. For Python3 you need to remove all the .decode(utf-8) from the examples)*

1. **Return a list of emoji information (or if there are emojis)**

Return a list of the emojis included in the text, organised in a list of dictionaries, where the following information are encoded for each emoji: 

* The emoji Unicode (key: code)
* The location span (key: location)
* The CLDR Short Name (key: name)

*Note: some emojis are composed of more than one Unicode character.*

.. code-block:: python

    >>> emoji.emoji_list("Hi, I am fine 😁. This is a complex emoji 🤹🏻‍♂️".decode('utf-8'))
    [{'code': u'\U0001f601', 'location': (14, 15), 'name': u'beaming_face_with_smiling_eyes'},
     {'code': u'\U0001f939\U0001f3fb\u200d\u2642\ufe0f', 'location': (41, 46), 'name': u'man_juggling_light_skin_tone'}]

Use len(emoji_list) if you want to see the number of emojis in a text.

2. **Replace all emojis with "replacement" string** 

Default replacement is empty string, equivalent to removing all emojis.

.. code-block:: python

    >>> emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'))
    Hi, I am fine.
    >>> emoji.replace_emoji("Hi, I am fine. 😁".decode('utf-8'), replacement='***')
    Hi, I am fine. ***

3. **Replace each emoji (UNICODE) with the CLDR Short Name**

Default delimiter is underscore *_CLDR_Short_Name_* (see `this <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__ for the CLDR names).

.. code-block:: python

    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
    Unicode is tricky _hushed_face_
    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8'), delimiters=("-|", "|-")))
    Unicode is tricky -|hushed_face|-
    >>> print(emoji.demojize("Be careful, this is only one emoji! 👩🏻‍⚖️".decode('utf-8')))
    Be careful, this is only one emoji! _woman_judge_light_skin_tone_

4. **Replace each CLDR emoji name with the emoji (UNICODE)**

See `this <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__ for the CLDR names and `this <http://www.emoji-cheat-sheet.com/>`__ for the aliases.

.. code-block:: python

    >>> print(emoji.emojize('Bring the UNICODE back! _smiling_face_with_sunglasses_'))
    Bring the UNICODE back! 😎

5. **Get all existing emojis**

Return a set of all existing emojis (CLDR names or UNICODE)

.. code-block:: python

    >>> s = emoji.set_cldr()
    set([u'_British_Virgin_Islands_', ... , u'_Angola_'])
    >>> s = emoji.set_unicode()
    set([u'\U0001f1ee\U0001f1e8' , ... , u'\U0001f9d6\U0001f3ff'])

6. **Visualize emojis in html file**

Visualize emojis with browser. This function appends to an html file a text where the emojis are replaced by the link to the corrisponding image (useful if your terminal do not visualize emojis). Default file is "./emoji.html", but you can append the text to another file using the *html_file* argument. 

    >>> emoji.print_html("Visualize this emoji in html file 🤹🏻".decode('utf-8'), html_file="path_to_other_file.html")

The html file will look like `this <https://fvancesco.github.io/tmp/emoji.html>`__.

Installation
------------

From master branch:

.. code-block:: console

    $ git clone https://github.com/fvancesco/emoji.git
    $ cd emoji
    $ python setup.py install

If you do not want to install it, just copy in the classpath of your program the folder emoji/emoji (the one that contains core.py and unicode.py) and import the core funcions in your program with "from emoji import core" and use it with "core.demojize(...)".   

Images
------------
In the folder *utils/* there are file images of all emojis. They are named with the UNICODE code in one case, and with the CLDR name in the other case (for example, this emoji 👍 is saved as images_cldr/thumbs_up.png and images_unicode/U0001F44D.png). There is also a script to download the codes and the images (Apple rendering) of the last emojis.


Links
----

`Official unicode list <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__

`Word Embeddigs of Emojis (US, UK, ESP, ITA) <http://sempub.taln.upf.edu/tw/cosmopolitan/>`__
