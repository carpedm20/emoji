# -*- coding: UTF-8 -*-


"""
Unittests for emoji.cli
"""


from __future__ import unicode_literals

from emoji import __version__
from emoji.__main__ import build_input_string
from emoji.__main__ import main

from .utils import captured_output


def test_build_input_string():
    def check(case, expected):
        result = build_input_string(case)
        assert result == expected

    yield check, [], ""
    yield check, [""], ""
    yield check, ["foo"], "foo"
    yield check, ["foo", " bar", " baz "], "foo  bar  baz "


def test_main_help():
    try:
        with captured_output() as (out, err):
            main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0
    else:
        assert False, 'expected clean exit'
    text = out.getvalue()
    assert text.startswith("usage: ")
    assert "Print emojified input." in text


def test_main_version():
    try:
        with captured_output() as (out, err):
            main(["--version"])
    except SystemExit as exc:
        assert exc.code == 0
    else:
        assert False, 'expected clean exit'
    text = out.getvalue().rstrip("\n")
    assert text == __version__


def test_main_no_tokens():
    try:
        with captured_output() as (out, err):
            main([])
    except SystemExit as exc:
        assert exc.code == 2
    else:
        assert False, 'expected exit code 2'


def test_main():
    def check(case, expected):
        with captured_output() as (out, err):
            main(case)
        text = out.getvalue().rstrip("\n")
        assert text == expected

    yield check, [""], ""
    yield check, ["foo"], "foo"
    yield check, ["foo", " :wave: ", " :baz: "], "foo  👋   :baz: "
