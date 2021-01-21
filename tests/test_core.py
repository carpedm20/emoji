# -*- coding: UTF-8 -*-


"""Unittests for emoji.core"""


from __future__ import unicode_literals

import emoji


def test_emojize_name_only():
    for lang_code, emoji_pack in emoji.EMOJI_UNICODE.items():
        for name in emoji_pack.keys():
            actual = emoji.emojize(name, False, language=lang_code)
            expected = emoji_pack[name]
            assert expected == actual, '%s != %s' % (expected, actual)


def test_emojize_complicated_string():
    # A bunch of emoji's with UTF-8 strings to make sure the regex expression is functioning
    name_code = {
        ':flag_for_Ceuta_&_Melilla:': u'\U0001F1EA\U0001F1E6',
        ':flag_for_St._Barthélemy:': u'\U0001F1E7\U0001F1F1',
        ':flag_for_Côte_d’Ivoire:': u'\U0001F1E8\U0001F1EE',
        ':flag_for_Åland_Islands:': u'\U0001F1E6\U0001F1FD',
        ':flag_for_São_Tomé_&_Príncipe:': u'\U0001F1F8\U0001F1F9',
        ':flag_for_Curaçao:': u'\U0001F1E8\U0001F1FC'
    }
    string = ' complicated! '.join(list(name_code.keys()))
    actual = emoji.emojize(string, False)
    expected = string
    for name, code in name_code.items():
        expected = expected.replace(name, code)
    expected = emoji.emojize(actual, False)
    assert expected == actual, '%s != %s' % (expected, actual)


def test_emojize_invalid_emoji():
    string = '__---___--Invalid__--__-Name'
    assert emoji.emojize(string, False) == string


def test_alias():
    # When use_aliases=False aliases should be passed through untouched
    assert emoji.emojize(':soccer:', use_aliases=False) == ':soccer:'
    assert emoji.emojize(':soccer:', use_aliases=True) == emoji.EMOJI_ALIAS_UNICODE_ENGLISH[':soccer:']


def test_invalid_alias():
    # Invalid aliases should be passed through untouched
    assert emoji.emojize(':tester:', use_aliases=True) == ':tester:'


def test_demojize_name_only():
    for name in emoji.EMOJI_UNICODE.keys():
        oneway = emoji.emojize(name, False)
        roundtrip = emoji.demojize(oneway)
        assert name == roundtrip, '%s != %s' % (name, roundtrip)


def test_demojize_complicated_string():
    constructed = u'testing :baby::emoji_modifier_fitzpatrick_type-3: with :eyes: :eyes::eyes: modifiers :baby::emoji_modifier_fitzpatrick_type-5: to symbols ヒㇿ'
    emojid = emoji.emojize(constructed)
    destructed = emoji.demojize(emojid)
    assert constructed == destructed, '%s != %s' % (constructed, destructed)


def test_emoji_lis():
    assert emoji.emoji_lis('Hi, I am fine. 😁') == [{'location': 15, 'emoji': '😁'}]
    assert emoji.emoji_lis('Hi') == []
    assert emoji.emoji_lis('Hello 🇫🇷👌') == [{'emoji': '🇫🇷', 'location': 6}, {'emoji': '👌', 'location': 8}]


def test_emoji_count():
    assert emoji.emoji_count('Hi, I am fine. 😁') == 1
    assert emoji.emoji_count('Hi') == 0
    assert emoji.emoji_count('Hello 🇫🇷👌') == 2
