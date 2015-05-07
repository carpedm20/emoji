=====
Emoji
=====

`Emoji <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__  for Python.  This project was inspired by `kyokomi <https://github.com/kyokomi/emoji>`__.


Example
=======

.. code-block:: python

    >> import emoji
    >> print(emoji.emojize('Python is :thumbsup:'))
    Python is 👍
    >> print(emoji.emojize('Python is :thumbs_up_sign:', is_alias=False))
    Python is 👍
    >> print(emoji.decode('👍'))
    :+1:


Installation
============

Via pip:

.. code-block:: console

    $ pip install emoji --upgrade

From master branch:

.. code-block:: console

    $ git clone https://github.com/carpedm20/emoji.git
    $ cd emoji
    $ python setup.py install


Authors
=======

Taehoon Kim / `@carpedm20 <http://carpedm20.github.io/about/>`__

Kevin Wurster / `@geowurster <http://twitter.com/geowurster>`__
