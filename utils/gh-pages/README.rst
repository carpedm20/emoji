Emoji overview on GitHub Pages
==============================

Generate a HTML website that contains all emoji and names that are currently supported.

GitHub Pages
------------

https://carpedm20.github.io/emoji/

On every release the content on the GitHub Pages is updated by a GitHub Action:
`updateGithubPages.yml <../../.github/workflows/updateGithubPages.yml>`__.

You can view the generated source in the `gh-pages <https://github.com/carpedm20/emoji/tree/gh-pages>`__ branch.


Build pages locally
-------------------

.. code-block:: sh

    python -m pip install -r utils/gh-pages/requirements.txt
    python utils/gh-pages/generatePages.py
