# -*- coding: UTF-8 -*-


"""Unittests for emoji.core"""

from __future__ import unicode_literals

import re
import emoji
import pytest


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

def test_emojize_languages():
    for lang_code, emoji_pack in emoji.EMOJI_UNICODE.items():
        for name, emj in emoji_pack.items():
            assert emoji.emojize(name, language=lang_code) == emj

def test_demojize_languages():
    for lang_code, emoji_pack in emoji.UNICODE_EMOJI.items():
        for emj, name in emoji_pack.items():
            assert emoji.demojize(emj, language=lang_code) == name


def test_emojize_variant():
    remove_variant = lambda s: re.sub(u'[\ufe0e\ufe0f]$', '', s)

    assert emoji.emojize(':Taurus:', variant=None) == emoji.EMOJI_UNICODE['en'][':Taurus:']
    assert emoji.emojize(':Taurus:', variant=None) ==  emoji.emojize(':Taurus:')
    assert emoji.emojize(':Taurus:', variant='text_type') == remove_variant(emoji.EMOJI_UNICODE['en'][':Taurus:']) + u'\ufe0e'
    assert emoji.emojize(':Taurus:', variant='emoji_type') == remove_variant(emoji.EMOJI_UNICODE['en'][':Taurus:']) + u'\ufe0f'

    assert emoji.emojize(':admission_tickets:', variant=None) == emoji.EMOJI_UNICODE['en'][':admission_tickets:']
    assert emoji.emojize(':admission_tickets:', variant=None) ==  emoji.emojize(':admission_tickets:')
    assert emoji.emojize(':admission_tickets:', variant='text_type') == remove_variant(emoji.EMOJI_UNICODE['en'][':admission_tickets:']) + u'\ufe0e'
    assert emoji.emojize(':admission_tickets:', variant='emoji_type') == remove_variant(emoji.EMOJI_UNICODE['en'][':admission_tickets:']) + u'\ufe0f'

    with pytest.raises(ValueError):
        emoji.emojize(':admission_tickets:', variant=False)

    with pytest.raises(ValueError):
        emoji.emojize(':admission_tickets:', variant=True)

    with pytest.raises(ValueError):
        emoji.emojize(':admission_tickets:', variant='wrong')

    assert emoji.emojize(":football:", use_aliases=False) == ':football:'
    assert emoji.emojize(":football:", variant="text_type", use_aliases=False) == ':football:'
    assert emoji.emojize(":football:", use_aliases=True) == emoji.EMOJI_ALIAS_UNICODE_ENGLISH[':football:']
    assert emoji.emojize(":football:", variant="emoji_type", use_aliases=True) == emoji.EMOJI_ALIAS_UNICODE_ENGLISH[':football:']


def test_demojize_removes_variant():
    # demojize should remove all variant indicators \ufe0e and \ufe0f from the string
    text = "".join([emoji.emojize(':Taurus:', variant='text_type'),
           emoji.emojize(':Taurus:', variant='emoji_type'),
           emoji.emojize(':admission_tickets:', variant='text_type'),
           emoji.emojize(':admission_tickets:', variant='emoji_type'),
           emoji.emojize(':alien:', variant='text_type'),
           emoji.emojize(':alien:', variant='emoji_type'),
           emoji.emojize(':atom_symbol:', variant='text_type'),
           emoji.emojize(':atom_symbol:', variant='emoji_type')])

    for lang_code in emoji.UNICODE_EMOJI:
        result = emoji.demojize(text, language=lang_code)
        assert '\ufe0e' not in result
        assert '\ufe0f' not in result


def test_emojize_invalid_emoji():
    string = '__---___--Invalid__--__-Name'
    assert emoji.emojize(string, False) == string


def test_alias():
    # When use_aliases=False aliases should be passed through untouched
    assert emoji.emojize(':soccer:', use_aliases=False) == ':soccer:'
    assert emoji.emojize(':soccer:', use_aliases=True) == emoji.EMOJI_ALIAS_UNICODE_ENGLISH[':soccer:']
    assert emoji.emojize(':football:', use_aliases=False) == ':football:'
    assert emoji.emojize(':football:', use_aliases=True) == emoji.EMOJI_ALIAS_UNICODE_ENGLISH[':football:']


def test_invalid_alias():
    # Invalid aliases should be passed through untouched
    assert emoji.emojize(':tester:', use_aliases=True) == ':tester:'
    assert emoji.emojize(':footbal:', use_aliases=True) == ':footbal:'
    assert emoji.emojize(':socer:', use_aliases=True) == ':socer:'
    emoji.emojize(':socer:', use_aliases=True, variant="text_type") == ':socer:'


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
    if len('Hello 🇫🇷👌') < 10:  # skip this test on python with UCS-2 as the string length/positions are different
        assert emoji.emoji_lis('Hello 🇫🇷👌') == [{'emoji': '🇫🇷', 'location': 6}, {'emoji': '👌', 'location': 8}]


def test_distinct_emoji_lis():
    assert emoji.distinct_emoji_lis('Hi, I am fine. 😁') == ['😁']
    assert emoji.distinct_emoji_lis('Hi') == []
    assert set(emoji.distinct_emoji_lis('Hello 🇫🇷👌')) == {'🇫🇷', '👌'}
    assert emoji.distinct_emoji_lis('Hi, I am fine. 😁😁😁😁') == ['😁']


def test_emoji_count():
    assert emoji.emoji_count('Hi, I am fine. 😁') == 1
    assert emoji.emoji_count('Hi') == 0
    assert emoji.emoji_count('Hello 🇫🇷👌') == 2


def test_replace_emoji():
    assert emoji.replace_emoji(u'Hi, I am fine. 😁') == 'Hi, I am fine. '
    assert emoji.replace_emoji('Hi') == 'Hi'
    assert emoji.replace_emoji('Hello 🇫🇷👌') == 'Hello '
    assert emoji.replace_emoji('Hello 🇫🇷👌', 'x') == 'Hello xx'

    def replace(emj, data):
        assert emj in ["🇫🇷", "👌"]
        return 'x'
    assert emoji.replace_emoji('Hello 🇫🇷👌', replace) == 'Hello xx'


def test_is_emoji():
    assert emoji.is_emoji('😁')
    assert not emoji.is_emoji('H')
    assert emoji.is_emoji('🇫🇷')
