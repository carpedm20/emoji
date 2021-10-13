# -*- coding: UTF-8 -*-


"""Unittests for emoji.unicode_codes."""


import emoji


def test_emoji_english_names():

    for use_aliases, group in (
            (False, emoji.unicode_codes.EMOJI_UNICODE['en']),
            (True, emoji.unicode_codes.EMOJI_ALIAS_UNICODE_ENGLISH)
    ):
        for name, ucode in group.items():
            assert name.startswith(':') and name.endswith(':') and len(name) >= 3
            emj = emoji.emojize(name, use_aliases=use_aliases)
            assert emj == ucode, '%s != %s' % (emoji.emojize(name), ucode)


def test_compare_normal_and_aliases():
    # There should always be more aliases than normal codes
    # since the aliases contain the normal codes
    assert len(emoji.EMOJI_UNICODE) < len(emoji.EMOJI_ALIAS_UNICODE_ENGLISH)


def test_no_alias_duplicates():
    # There should not be two emoji with the same alias
    # (aliases still can be the same as another 'en'-name)
    all_aliases = set()
    for data in emoji.EMOJI_DATA.values():
        if data['status'] <= emoji.STATUS['fully_qualified'] and'alias' in data:
            for alias in data['alias']:
                assert alias not in all_aliases
                all_aliases.add(alias)
