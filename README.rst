Emoji
=====

Emoji library for Python.  This project is a fork of `karpedm20 <https://github.com/carpedm20/emoji>`__.
Tested on Python2.7

The entire set of Emoji codes is defined by the `unicode consortium <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__.
Current emoji version used in this project is **v5** (last update: 20 July 2017)

Functionalities
------------
*(All examples assume you already imported emoji)*

1. **Replace each emoji (UNICODE) with the CLDR Short Name**

Default delimiter is underscore *_CLDR_Short_Name_* (see `this <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__ for the CLDR names).

.. code-block:: python

    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8')))
    Unicode is tricky _hushed_face_
    >>> print(emoji.demojize("Unicode is tricky 😯".decode('utf-8'), delimiters=("-|", "|-")))
    Unicode is tricky -|hushed_face|-
    >>> print(emoji.demojize("Be careful, this is only one emoji! 👩🏻‍⚖️".decode('utf-8')))
    Be careful, this is only one emoji! _woman_judge_light_skin_tone_

2. **Replace each CLDR emoji name with the emoji (UNICODE)**

See `this <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__ for the CLDR names and `this <http://www.emoji-cheat-sheet.com/>`__ for the aliases.

.. code-block:: python

    >>> print(emoji.emojize('Bring the UNICODE back! _smiling_face_with_sunglasses_'))
    Bring the UNICODE back! 😎

3. **Return a list of emoji information**. 

Return a list of the emojis included in the text, organised in a list of dictionaries, where the following information are encoded for each emoji: 

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

5. **Get all existing emojis**. 

Return a set of all existing emojis (CLDR names or UNICODE)

.. code-block:: python

    >>> s = emoji.set_cldr()
    set([u'_British_Virgin_Islands_', ... , u'_Angola_'])
    >>> s = emoji.set_unicode()
    set([u'\U0001f1ee\U0001f1e8' , ... , u'\U0001f9d6\U0001f3ff'])

6. **Visualize emojis in html file**

Visualize emojis with the browser. This function append to an html file a text where the emojis are replaced by the link to the corrisponding image (useful if your terminal do not visualize emojis). Default file is "./emoji.html", but you can append the text to another file using the *html_file* argument. 
 
    >>> print_html("Visualize this emoji in html file 😎")
    >>> print_html("Visualize this emoji in html file 😎", html_file="path_to_other_file.html")


Installation
------------

From master branch:

.. code-block:: console

    $ git clone https://github.com/fvancesco/emoji.git
    $ cd emoji
    $ python setup.py install


Images
------------
In the folder *utils/* there are file images of all emojis. They are named with the UNICODE code in one case, and with the CLDR name in the other case (for example, this emoji 👍 is saved as images_cldr/thumbs_up.png and images_unicode/U0001F44D.png). There is also a script to download the codes and the images (Apple rendering) of the last emojis.

Links
----

`Official unicode list <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__

`Word Embeddigs of Emojis (US, UK, ESP, ITA) <http://sempub.taln.upf.edu/tw/cosmopolitan/>`__
