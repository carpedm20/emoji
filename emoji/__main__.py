# -*- coding: UTF-8 -*-
"""
Run module directly:

$ python -m emoji hello world :wave:
hello world 👋

"""
from __future__ import print_function
from __future__ import unicode_literals

import argparse

from emoji import __version__
from emoji import emojize


def parse_arguments(argv=None):
    """ Return namespace with arguments parsed from *argv* (default: `sys.argv`). """
    ap = argparse.ArgumentParser(description="Print emojified input.")
    ap.add_argument("--version", action="version", version="{}".format(__version__))
    ap.add_argument(
        "tokens", metavar="STRING", nargs="+", help="input STRING to emojify"
    )
    return ap.parse_args(argv)


def build_input_string(tokens):
    """ Return one input string from *tokens*. """
    return " ".join(tokens)


def main(argv=None):
    args = parse_arguments(argv)
    text = build_input_string(args.tokens)

    print(emojize(text, use_aliases=True))


if __name__ == "__main__":
    main()
