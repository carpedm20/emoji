=====
Emoji
=====

.. image:: https://pypip.in/v/emoji/badge.png?style=flat
    :target: https://pypi.python.org/pypi/emoji

.. image:: https://pypip.in/d/emoji/badge.png?style=flat
    :target: https://pypi.python.org/pypi/emoji

.. image:: https://pypip.in/status/emoji/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/emoji

.. image:: https://pypip.in/license/emoji/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/emoji


`Emoji <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__  for Python.  This project was inspired by `kyokomi <https://github.com/kyokomi/emoji>`__.


Example
=======

.. code-block:: python

    >> import emoji
    >> print(emoji.emojize('Water! :water_wave:'))
    Water! 🌊
    >> print(emoji.decode(u'🌊')) # for Python 2.x
    :water_wave:
    >> print(emoji.decode('🌊')) # for Python 3.x
    :water_wave:

.. image:: https://raw.githubusercontent.com/carpedm20/emoji/master/example/example.png


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


Developing
==========

.. code-block:: console

    $ git clone https://github.com/carpedm20/emoji.git
    $ cd emoji
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements-dev.txt -e .
    $ nosetests --with-coverage


License
=======

See ``LICENSE.txt``.


Authors
=======

Taehoon Kim / `@carpedm20 <http://carpedm20.github.io/about/>`__

Kevin Wurster / `@geowurster <http://twitter.com/geowurster>`__
