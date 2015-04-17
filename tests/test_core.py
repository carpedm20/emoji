# -*- coding: UTF-8 -*-


"""
Unittests for emoji.core
"""


from __future__ import unicode_literals

import emoji


def test_emojize_name_only():
    for name in emoji.EMOJI_UNICODE.keys():
        actual = emoji.emojize(name)
        expected = emoji.EMOJI_UNICODE[name]
        assert expected == actual, "%s != %s" % (expected, actual)


def test_emojize_complicated_string():
    # A bunch of emoji's with UTF-8 strings to make sure the regex expression is functioning
    name_code = {
        ':flag_for_Ceuta_&_Melilla:': u'\U0001F1EA \U0001F1E6',
        ':flag_for_St._Barthélemy:': u'\U0001F1E7 \U0001F1F1',
        ':flag_for_Côte_d’Ivoire:': u'\U0001F1E8 \U0001F1EE',
        ':flag_for_Åland_Islands:': u'\U0001F1E6 \U0001F1FD',
        ':flag_for_São_Tomé_&_Príncipe:': u'\U0001F1F8 \U0001F1F9',
        ':flag_for_Curaçao:': u'\U0001F1E8 \U0001F1FC'
    }
    string = ' complicated! '.join(list(name_code.keys()))
    actual = emoji.emojize(string)
    expected = string
    for name, code in name_code.items():
        expected = expected.replace(name, code)
    expected = emoji.emojize(actual)
    assert expected == actual, "%s != %s" % (expected, actual)


def test_emojize_invalid_emoji():
    string = '__---___--Invalid__--__-Name'
    assert emoji.emojize(string) == string


def test_decode():

    for name, u_code in emoji.EMOJI_UNICODE.items():
        assert emoji.decode(u_code) == name


def test_decode_invalid_string():
    try:
        emoji.decode('__---___--Invalid__--__-Name')
        raise Exception("Above line should have raised a ValueError")
    except ValueError:
        pass
