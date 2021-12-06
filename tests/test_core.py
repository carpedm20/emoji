# -*- coding: UTF-8 -*-


"""Unittests for emoji.core"""

from __future__ import unicode_literals

import random
import re
import emoji
import pytest


def ascii(s):
    # return escaped Code points \U000AB123
    return s.encode("unicode-escape").decode()


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
    for lang_code, emoji_pack in emoji.EMOJI_UNICODE.items():
        for name, emj in emoji_pack.items():
            assert emoji.demojize(emj, language=lang_code) == name


def test_emojize_variant():
    def remove_variant(s): return re.sub(u'[\ufe0e\ufe0f]$', '', s)

    assert emoji.emojize(
        ':Taurus:', variant=None) == emoji.EMOJI_UNICODE['en'][':Taurus:']
    assert emoji.emojize(':Taurus:', variant=None) == emoji.emojize(':Taurus:')
    assert emoji.emojize(':Taurus:', variant='text_type') == remove_variant(
        emoji.EMOJI_UNICODE['en'][':Taurus:']) + u'\ufe0e'
    assert emoji.emojize(':Taurus:', variant='emoji_type') == remove_variant(
        emoji.EMOJI_UNICODE['en'][':Taurus:']) + u'\ufe0f'

    assert emoji.emojize(
        ':admission_tickets:', variant=None) == emoji.EMOJI_UNICODE['en'][':admission_tickets:']
    assert emoji.emojize(':admission_tickets:', variant=None) == emoji.emojize(
        ':admission_tickets:')
    assert emoji.emojize(':admission_tickets:', variant='text_type') == remove_variant(
        emoji.EMOJI_UNICODE['en'][':admission_tickets:']) + u'\ufe0e'
    assert emoji.emojize(':admission_tickets:', variant='emoji_type') == remove_variant(
        emoji.EMOJI_UNICODE['en'][':admission_tickets:']) + u'\ufe0f'

    with pytest.raises(ValueError):
        emoji.emojize(':admission_tickets:', variant=False)

    with pytest.raises(ValueError):
        emoji.emojize(':admission_tickets:', variant=True)

    with pytest.raises(ValueError):
        emoji.emojize(':admission_tickets:', variant='wrong')

    assert emoji.emojize(":football:", use_aliases=False) == ':football:'
    assert emoji.emojize(":football:", variant="text_type",
                         use_aliases=False) == ':football:'
    assert emoji.emojize(":football:", use_aliases=True) == u'\U0001F3C8'
    assert emoji.emojize(":football:", variant="emoji_type",
                         use_aliases=True) == u'\U0001F3C8'


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

    string = ':: baby:: :_: : : :  : :-: :+:'
    assert emoji.emojize(string, False) == string


def test_alias():
    # When use_aliases=False aliases should be passed through untouched
    assert emoji.emojize(':soccer:', use_aliases=False) == ':soccer:'
    assert emoji.emojize(':soccer:', use_aliases=True) == u'\U000026BD'
    assert emoji.emojize(':football:', use_aliases=False) == ':football:'
    assert emoji.emojize(':football:', use_aliases=True) == u'\U0001F3C8'
    # Multiple aliases for one emoji:
    assert emoji.emojize(':thumbsup:', use_aliases=True) == emoji.emojize(
        ':+1:', use_aliases=True)
    assert emoji.emojize(':thumbsup:', use_aliases=True) == emoji.emojize(
        ':thumbs_up:', use_aliases=True)
    assert emoji.emojize(':thumbsup:', use_aliases=True) == u'\U0001f44d'

    thumbsup = u'\U0001f44d'
    assert emoji.demojize(thumbsup, use_aliases=True) != thumbsup
    assert emoji.demojize(thumbsup, use_aliases=True) != ':thumbs_up:'
    assert emoji.demojize(thumbsup, use_aliases=True) != emoji.demojize(
        thumbsup, use_aliases=False)

    thailand = u'🇹🇭'
    assert emoji.demojize(thailand, use_aliases=True) != thailand
    assert emoji.demojize(thailand, use_aliases=True) != ':Thailand:'
    assert emoji.demojize(thailand, use_aliases=True) != emoji.demojize(
        thailand, use_aliases=False)
    assert emoji.demojize(thailand, use_aliases=True, version=1.0) != emoji.demojize(
        thailand, use_aliases=True)

    # No alias
    for emj, emoji_data in emoji.EMOJI_DATA.items():
        if emoji_data['status'] != emoji.STATUS['fully_qualified']:
            continue
        if 'alias' not in emoji_data:
            assert emoji.emojize(emoji_data['en'], use_aliases=True) != emoji_data['en']
            assert emoji.demojize(emj, use_aliases=True) == emoji_data['en']

    # language='alias'
    assert emoji.emojize(':flag_for_Thailand:', use_aliases=True, language="en") == thailand
    assert emoji.emojize(':flag_for_Thailand:', language="alias") == thailand
    assert emoji.emojize(':flag_for_Thailand:', language="alias", use_aliases=True) == thailand
    assert emoji.demojize(thailand, use_aliases=True, language="en") == ':flag_for_Thailand:'
    assert emoji.demojize(thailand, language="alias") ==':flag_for_Thailand:'
    assert emoji.demojize(thailand, language="alias", use_aliases=True) ==':flag_for_Thailand:'


def test_invalid_alias():
    # Invalid aliases should be passed through untouched
    assert emoji.emojize(':tester:', use_aliases=True) == ':tester:'
    assert emoji.emojize(':footbal:', use_aliases=True) == ':footbal:'
    assert emoji.emojize(':socer:', use_aliases=True) == ':socer:'
    assert emoji.emojize(':socer:', use_aliases=True,
                  variant="text_type") == ':socer:'


def test_alias_wrong_language():
    # Alias with wrong languages
    thailand = u'🇹🇭'
    with pytest.warns(UserWarning) as w:
        emoji.emojize(':flag_for_Thailand:', use_aliases=True, language="es")
    with pytest.warns(UserWarning) as w:
        assert emoji.emojize(':flag_for_Thailand:', use_aliases=True, language="de") == thailand
    with pytest.warns(UserWarning) as w:
        assert emoji.emojize(':flag_for_Thailand:', use_aliases=True, language="es") == thailand
    assert emoji.emojize(':flag_for_Thailand:', use_aliases=False, language="es") == ':flag_for_Thailand:'
    assert emoji.emojize(':flag_for_Thailand:', use_aliases=True, language="en") == thailand
    assert emoji.emojize(':flag_for_Thailand:', use_aliases=False, language="alias") == thailand
    assert emoji.emojize(':flag_for_Thailand:', use_aliases=True, language="alias") == thailand

    with pytest.warns(UserWarning) as w:
        emoji.demojize(thailand, use_aliases=True, language="es")
    with pytest.warns(UserWarning) as w:
        assert emoji.demojize(thailand, use_aliases=True, language="es") == ':flag_for_Thailand:'
    assert emoji.demojize(thailand, use_aliases=False, language="es") == ':bandera_tailandia:'
    assert emoji.demojize(thailand, use_aliases=True, language="en") == ':flag_for_Thailand:'
    assert emoji.demojize(thailand, use_aliases=False, language="alias") == ':flag_for_Thailand:'
    assert emoji.demojize(thailand, use_aliases=True, language="alias") == ':flag_for_Thailand:'


def test_demojize_name_only():
    for emj, item in emoji.EMOJI_DATA.items():
        if item['status'] != emoji.STATUS['fully_qualified']:
            continue
        for lang_code in emoji.UNICODE_EMOJI:
            if not lang_code in item:
                continue
            name = item[lang_code]
            oneway = emoji.emojize(name, use_aliases=False, language=lang_code)
            assert oneway == emj
            roundtrip = emoji.demojize(oneway, language=lang_code)
            assert name == roundtrip, '%s != %s' % (name, roundtrip)


def test_demojize_complicated_string():
    constructed = u'testing :baby::emoji_modifier_fitzpatrick_type-3: with :eyes: :eyes::eyes: modifiers :baby::emoji_modifier_fitzpatrick_type-5: to symbols ヒㇿ'
    emojid = emoji.emojize(constructed)
    destructed = emoji.demojize(emojid)
    assert constructed == destructed, '%s != %s' % (constructed, destructed)


def test_demojize_delimiters():
    for e in [u'\U000026BD', u'\U0001f44d', u'\U0001F3C8']:
        for d in [(":", ":"), ("a", "b"), ("!", "!!"), ("123", "456"), (u"😁", u"👌")]:
            s = emoji.demojize(e, delimiters=d)
            assert s.startswith(d[0])
            assert s.endswith(d[1])

    text = u"Example of a text with an emoji%sin a sentence"
    for e in [u'\U000026BD', u'\U0001f44d', u'\U0001F3C8']:
        for d in [(":", ":"), ("!", "-!-"), ("-", "-"), (":", "::"), ("::", "::"), (u"😁", u"👌")]:
            text_with_unicode = text % e
            demojized_text = emoji.demojize(text_with_unicode, delimiters=d)
            assert text_with_unicode != demojized_text
            assert e not in demojized_text
            assert emoji.emojize(demojized_text, delimiters=d) == text_with_unicode
            text_with_emoji = text % emoji.demojize(e, delimiters=d)
            assert demojized_text == text_with_emoji
            assert emoji.emojize(text_with_emoji, delimiters=d) == text_with_unicode


def test_emoji_lis():
    assert emoji.emoji_lis('Hi, I am 👌 test')[0]['location'] == 9
    assert emoji.emoji_lis('Hi') == []
    if len('Hello 🇫🇷👌') < 10:  # skip these tests on python with UCS-2 as the string length/positions are different
        assert emoji.emoji_lis('Hi, I am fine. 😁') == [
            {'location': 15, 'emoji': '😁'}]
        assert emoji.emoji_lis('Hello 🇫🇷👌') == [
            {'emoji': '🇫🇷', 'location': 6}, {'emoji': '👌', 'location': 8}]


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


def test_long_emoji():
    assert emoji.demojize('This is \U0001F9D1\U0001F3FC\U0000200D\U0001F37C example text') == 'This is :person_feeding_baby_medium-light_skin_tone: example text'
    assert emoji.demojize('This is \U0001f468\U0001f3ff\u200d\u2764\ufe0f\u200d\U0001f468\U0001f3ff example text \U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF') == 'This is :couple_with_heart_man_man_dark_skin_tone: example text :woman_and_man_holding_hands_light_skin_tone_dark_skin_tone:'
    assert emoji.demojize('This is \U0001f468\U0001f3ff\u200d\u2764\ufe0f\u200d\U0001f468\U0001f3ff\U0001f468\U0001f3ff\u200d\u2764\ufe0f\u200d\U0001f48b\u200d\U0001f468\U0001f3ff example text \U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF') == 'This is :couple_with_heart_man_man_dark_skin_tone::kiss_man_man_dark_skin_tone: example text :woman_and_man_holding_hands_light_skin_tone_dark_skin_tone:'
    assert emoji.demojize('\U0001F46B\U0001F3FB This is \U0001f468\U0001f3ff\U0001f468\U0001f3ff\u200d\u2764\ufe0f\u200d\U0001f468\U0001f3ff\U0001f468\U0001f3ff\u200d\u2764\ufe0f\u200d\U0001f48b\u200d\U0001f468\U0001f3ff example text \U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF') == ':woman_and_man_holding_hands_light_skin_tone: This is :man_dark_skin_tone::couple_with_heart_man_man_dark_skin_tone::kiss_man_man_dark_skin_tone: example text :woman_and_man_holding_hands_light_skin_tone_dark_skin_tone:'
    assert emoji.demojize('\U0001F46B\U0001F3FB\U0001F46B\U0001F3FB\U0001F469\U0001F3FB\U0000200D\U0001F91D\U0000200D\U0001F468\U0001F3FF\U0001FAF1\U0001F3FD\U0001FAF1\U0001F3FD\U0000200D\U0001FAF2\U0001F3FF') == ':woman_and_man_holding_hands_light_skin_tone::woman_and_man_holding_hands_light_skin_tone::woman_and_man_holding_hands_light_skin_tone_dark_skin_tone::rightwards_hand_medium_skin_tone::handshake_medium_skin_tone_dark_skin_tone:'
    s = ":crossed_fingers_medium-light_skin_tone::crossed_fingers::crossed_fingers_dark_skin_tone:"
    assert emoji.demojize(emoji.demojize(s)) == s


def test_untranslated():
    for emj, item in emoji.EMOJI_DATA.items():
        if item['status'] != emoji.STATUS['fully_qualified']:
            continue
        if 'es' not in item:
            # untranslated
            value = emoji.emojize(item['en'], language='en')
            roundtrip = emoji.demojize(value, language='es')
            assert roundtrip == value, '%s != %s (from %s)' % (ascii(roundtrip), ascii(value), item['en'])
        else:
            # translated
            value = emoji.emojize(item['en'], language='en')
            roundtrip = emoji.demojize(value, language='es')
            assert roundtrip == item['es'], '%s != %s' % (roundtrip, item['es'])


def test_text():
    UCS2 = len('Hello 🇫🇷👌') > 9  # don't break up characters on python with UCS-2

    text = u"""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat in reprehenderit in cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Stróż pchnął kość w quiz gędźb vel fax myjń.
Høj bly gom vandt fræk sexquiz på wc.
Съешь же ещё этих мягких французских булок, да выпей чаю.
За миг бях в чужд плюшен скърцащ фотьойл.
هلا سكنت بذي ضغثٍ فقد زعموا — شخصت تطلب ظبياً راح مجتازا
שפן אכל קצת גזר בטעם חסה, ודי
ऋषियों को सताने वाले दुष्ट राक्षसों के राजा रावण का सर्वनाश करने वाले विष्णुवतार भगवान श्रीराम, अयोध्या के महाराज दशरथ के बड़े सपुत्र थे।
とりなくこゑす ゆめさませ みよあけわたる ひんかしを そらいろはえて おきつへに ほふねむれゐぬ もやのうち
視野無限廣，窗外有藍天
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

    def add_random_emoji(text, lst, select=lambda emj_data: emj_data['en']):

        text = text

        emoji_list = []
        text_with_unicode = u""
        text_with_placeholder = u""
        for i in range(0, len(text), 10):
            while True:
                emj, emj_data = random.choice(lst)
                placeholder = select(emj_data)
                if placeholder:
                    break

            if UCS2:
                j = text.find(u" ", i, i + 10)
                if j == -1:
                    continue
            else:
                j = random.randint(i, i + 10)

            text_with_unicode += text[i:j]
            text_with_unicode += emj
            text_with_unicode += text[j:i + 10]

            text_with_placeholder += text[i:j]
            text_with_placeholder += placeholder
            text_with_placeholder += text[j:i + 10]

            emoji_list.append(emj)

        return text_with_unicode, text_with_placeholder, emoji_list

    def clean(s):
        return s.replace(u'\u200d', '').replace(u'\ufe0f', '')

    all_emoji_list = list(emoji.EMOJI_DATA.items())
    qualified_emoji_list = list((emj, item) for emj, item in emoji.EMOJI_DATA.items() if item['status'] == emoji.STATUS['fully_qualified'])

    # qualified emoji
    text_with_unicode, text_with_placeholder, emoji_list = add_random_emoji(text, qualified_emoji_list)
    assert emoji.demojize(text_with_unicode) == text_with_placeholder
    assert emoji.emojize(text_with_placeholder) == text_with_unicode
    if not UCS2:
        assert emoji.replace_emoji(text_with_unicode, u'') == text
    assert set(emoji.distinct_emoji_lis(text_with_unicode)) == set(emoji_list)
    for i, lis in enumerate(emoji.emoji_lis(text_with_unicode)):
        assert lis['emoji'] == emoji_list[i]

    # qualified emoji from "es"
    selector = lambda emoji_data: emoji_data["es"] if "es" in emoji_data else False
    text_with_unicode, text_with_placeholder, emoji_list = add_random_emoji(text, qualified_emoji_list, selector)
    assert emoji.demojize(text_with_unicode, language="es") == text_with_placeholder
    assert emoji.emojize(text_with_placeholder, language="es") == text_with_unicode
    if not UCS2:
        assert emoji.replace_emoji(text_with_unicode, u'') == text
    assert set(emoji.distinct_emoji_lis(text_with_unicode)) == set(emoji_list)
    for i, lis in enumerate(emoji.emoji_lis(text_with_unicode)):
        assert lis['emoji'] == emoji_list[i]

    # qualified emoji from "alias"
    selector = lambda emoji_data: emoji_data["alias"][0] if "alias" in emoji_data else False
    text_with_unicode, text_with_placeholder, emoji_list = add_random_emoji(text, qualified_emoji_list, selector)
    assert emoji.demojize(text_with_unicode, use_aliases=True) == text_with_placeholder
    assert emoji.emojize(text_with_placeholder, use_aliases=True) == text_with_unicode
    if not UCS2:
        assert emoji.replace_emoji(text_with_unicode, u'') == text
    assert set(emoji.distinct_emoji_lis(text_with_unicode)) == set(emoji_list)
    for i, lis in enumerate(emoji.emoji_lis(text_with_unicode)):
        assert lis['emoji'] == emoji_list[i]

    # all emoji
    text_with_unicode, text_with_placeholder, emoji_list = add_random_emoji(text, all_emoji_list)
    assert emoji.demojize(text_with_unicode) == text_with_placeholder
    assert clean(emoji.emojize(text_with_placeholder)) == clean(text_with_unicode)
    if not UCS2:
        assert emoji.replace_emoji(text_with_unicode, u'') == text
    assert set(emoji.distinct_emoji_lis(text_with_unicode)) == set(emoji_list)
    for i, lis in enumerate(emoji.emoji_lis(text_with_unicode)):
        assert lis['emoji'] == emoji_list[i]


def test_text_multiple_times():
    # Run test_text() multiple times because it relies on a random text
    for i in range(100):
        test_text()


def test_invalid_chars():
    invalidchar = u"\U0001F20F"
    assert emoji.demojize(invalidchar) == invalidchar, "%r != %r" % (ascii(emoji.demojize(invalidchar)), ascii(invalidchar))
    assert emoji.demojize(invalidchar) == invalidchar, "%r != %r" % (ascii(emoji.demojize(invalidchar)), ascii(invalidchar))

    invalidchar = u"u\2302 ⌂"
    assert emoji.demojize(invalidchar) == invalidchar, "%r != %r" % (ascii(emoji.demojize(invalidchar)), ascii(invalidchar))
    assert emoji.demojize(invalidchar) == invalidchar, "%r != %r" % (ascii(emoji.demojize(invalidchar)), ascii(invalidchar))


def test_combine_with_component():
    text = u"Example of a combined emoji%sin a sentence"

    combined = emoji.emojize(text % u":woman_dark_skin_tone:")
    seperated = emoji.emojize(text % u":woman::dark_skin_tone:")
    assert combined == seperated,  "%r != %r" % (ascii(combined), ascii(seperated))

    combined = emoji.emojize(text % u":woman_dark_skin_tone_white_hair:")
    seperated = emoji.emojize(text % u":woman::dark_skin_tone:\u200d:white_hair:")
    assert combined == seperated,  "%r != %r" % (ascii(combined), ascii(seperated))
