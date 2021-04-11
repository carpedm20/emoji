Emoji overview on github pages
==============================

Generate a HTML website that contains all emoji and names that are currently supported.

Github pages
-------------

https://carpedm20.github.io/emoji/

On every release the content on the github pages is updated by a github action:
`updateGithubPages.yml <../../.github/workflows/updateGithubPages.yml>`__.

You can view the generated source in the `gh-pages <https://github.com/carpedm20/emoji/tree/gh-pages>`__ branch.


Build pages locally
-------------------

.. code-block:: sh

    pip install -r utils/gh-pages/requirements.txt
    python utils/gh-pages/generatePages.py
