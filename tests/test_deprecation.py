# -*- coding: UTF-8 -*-


"""Unittests for deprecation warnings"""

import sys
import emoji
import pytest


def test_deprecation_get_emoji_regexp():
    with pytest.warns(DeprecationWarning):
        emoji.get_emoji_regexp()


@pytest.mark.filterwarnings("error")
def test_deprecation_replace_emoji_language():
    with pytest.warns(DeprecationWarning):
        emoji.replace_emoji("test", replace="", language="en")

    emoji.replace_emoji("test", replace="")


@pytest.mark.filterwarnings("error")
def test_deprecation_emoji_lis():
    with pytest.warns(DeprecationWarning):
        emoji.emoji_lis("test")

    emoji.emoji_list("test")


@pytest.mark.filterwarnings("error")
def test_deprecation_distinct_emoji_lis():
    with pytest.warns(DeprecationWarning):
        emoji.distinct_emoji_lis("test")

    emoji.distinct_emoji_list("test")


@pytest.mark.filterwarnings("error")
def test_deprecation_emojize_use_aliases():
    with pytest.warns(DeprecationWarning) :
        emoji.emojize("test", True)
    with pytest.warns(DeprecationWarning) :
        emoji.emojize("test", use_aliases=True)
    with pytest.warns(DeprecationWarning):
        emoji.emojize("test", use_aliases=False)
    with pytest.warns(DeprecationWarning):
        emoji.emojize("test", use_aliases=None)

    emoji.emojize("test")
    emoji.emojize("test", language="alias")


@pytest.mark.filterwarnings("error")
def test_deprecation_demojize_use_aliases():
    with pytest.warns(DeprecationWarning):
        emoji.demojize("test", True)
    with pytest.warns(DeprecationWarning):
        emoji.demojize("test", use_aliases=True)
    with pytest.warns(DeprecationWarning):
        emoji.demojize("test", use_aliases=False)
    with pytest.warns(DeprecationWarning):
        emoji.demojize("test", use_aliases=None)

    emoji.demojize("test")
    emoji.demojize("test", language="alias")


@pytest.mark.filterwarnings("error")
def test_deprecation_module_variables():
    if sys.version_info[0] == 3 and sys.version_info[1] >= 7:
        with pytest.warns(DeprecationWarning):
            for _ in emoji.EMOJI_UNICODE_ENGLISH:
             pass
    for _ in emoji.EMOJI_DATA:
        pass
