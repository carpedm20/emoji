# -*- coding: UTF-8 -*-


"""
Unittests for emoji.unicode_codes
"""


import emoji


def test_emoji_names():

    for use_aliases, group in (
            (False, emoji.unicode_codes.EMOJI_UNICODE),
            (True, emoji.unicode_codes.EMOJI_ALIAS_UNICODE)):
        for name, ucode in group.items():
            assert name.startswith(':') and name.endswith(':') and len(name) >= 3
            emj = emoji.emojize(name, use_aliases=use_aliases)
            assert emj == ucode, "%s != %s" % (emoji.emojize(name), ucode)


def test_compare_normal_and_aliases():
    # There should always be more aliases than normal codes since the aliases contain
    # the normal codes
    assert len(emoji.EMOJI_UNICODE) < len(emoji.EMOJI_ALIAS_UNICODE)