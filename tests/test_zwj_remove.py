"""Tests for emoji that consist of multiple emoji joined with a u200D (ZWJ - zero width joiner)
This file contains tests when the ZWJ is removed by demojize/replace_emoji.
See test_zwj_keep.py for tests when the ZWJ is kept.
"""

import emoji


def ascii(s):
    # return escaped Code points \U000AB123
    return s.encode("unicode-escape").decode()


def test_non_rgi_zwj_demojize():
    # These emoji are non-RGI ZWJ sequences. They should be decoded by demojize to their constituents.
    # They cannot be reversed with emojize(demojize(nonRGI)) because the \u200d is stripped by demojize.
    emoji.config.demojize_keep_zwj = False

    assert emoji.demojize('\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE') == ':man::woman_dark_skin_tone::girl_light_skin_tone::boy_medium-dark_skin_tone:'

    assert emoji.demojize('\U0001F468\U0001F3FF\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE') == ':man_dark_skin_tone::woman_dark_skin_tone::girl_light_skin_tone::boy_medium-dark_skin_tone:'

    assert emoji.demojize('\U0001F468\U0001F3FF\u200d\U0001F469\u200d\U0001F467\U0001F3FB\u200d\U0001F466') == ':man_dark_skin_tone::family_woman_girl::light_skin_tone::boy:'

    # https://www.unicode.org/Public/15.0.0/ucd/auxiliary/GraphemeBreakTest-15.0.0d1.html#s19
    assert emoji.demojize('\U0001f3ff\U0001f476\u200d\U0001f6d1') == ':dark_skin_tone::baby::stop_sign:'

    # https://www.unicode.org/Public/15.0.0/ucd/auxiliary/GraphemeBreakTest-15.0.0d1.html#s20
    # Check that \u200d is kept, if it not part of a valid ZWJ emoji
    assert emoji.demojize('\U0001f476\U0001f3ff\u0308\u200d\U0001f476\U0001f3ff') == ':baby_dark_skin_tone:\u0308\u200d:baby_dark_skin_tone:'


def test_malformed_zwj_demojize():
    # These sequences are malformed in the sense that they are neither RGI nor non-RGI ZWJ sequences
    # Check that still all the emoji are decoded
    emoji.config.demojize_keep_zwj = False

    result = emoji.demojize('\U0001F468\u200d\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE')
    assert '\U0001F468' not in result
    assert '\U0001F3FF' not in result
    assert '\U0001F467\U0001F3FB' not in result
    assert '\U0001F466\U0001F3FE' not in result

    result = emoji.demojize('\U0001F3FF\u200d\U0001F468\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE')
    assert '\U0001F468' not in result
    assert '\U0001F3FF' not in result
    assert '\U0001F467\U0001F3FB' not in result
    assert '\U0001F466\U0001F3FE' not in result

    # Mix of emoji and other characters
    # Check that still all the emoji are decoded

    result = emoji.demojize('\U0001F468\U0001F3FF\u200dabcd\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE')
    assert '\U0001F468\U0001F3FF' not in result
    assert '\U0001F467\U0001F3FB' not in result
    assert '\U0001F466\U0001F3FE' not in result
    assert ':man_dark_skin_tone:' in result
    assert 'abcd' in result
    assert ':girl_light_skin_tone:' in result
    assert ':boy_medium-dark_skin_tone:' in result

    result = emoji.demojize('W\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE')
    assert '\U0001F469\U0001F3FF' not in result
    assert '\U0001F467\U0001F3FB' not in result
    assert '\U0001F466\U0001F3FE' not in result
    assert result.startswith('W')
    assert ':woman_dark_skin_tone:' in result
    assert ':girl_light_skin_tone:' in result
    assert ':boy_medium-dark_skin_tone:' in result

    result = emoji.demojize('\U0001F9D1\U0001F3FE\u200d\u200d\U0001F393')
    assert '\U0001F9D1\U0001F3FE' not in result
    assert '\U0001F393' not in result
    assert ':person_medium-dark_skin_tone:' in result
    assert ':graduation_cap:' in result


def test_non_rgi_zwj_replace():
    emoji.config.replace_emoji_keep_zwj = False

    assert emoji.replace_emoji('\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE', '') == ''
    assert emoji.replace_emoji('\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE', 'X') == 'XXXX'

    assert emoji.replace_emoji('\U0001F468\U0001F3FF\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE', '') == ''
    assert emoji.replace_emoji('\U0001F468\U0001F3FF\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE', 'X') == 'XXXX'

    assert emoji.replace_emoji('\U0001F468\U0001F3FF\u200d\U0001F469\u200d\U0001F467\U0001F3FB\u200d\U0001F466', '') == ''
    assert emoji.replace_emoji('\U0001F468\U0001F3FF\u200d\U0001F469\u200d\U0001F467\U0001F3FB\u200d\U0001F466', 'X') == 'XXXX'

    # https://www.unicode.org/Public/15.0.0/ucd/auxiliary/GraphemeBreakTest-15.0.0d1.html#s19
    assert emoji.demojize('\U0001f3ff\U0001f476\u200d\U0001f6d1') == ':dark_skin_tone::baby::stop_sign:'

    # https://www.unicode.org/Public/15.0.0/ucd/auxiliary/GraphemeBreakTest-15.0.0d1.html#s20
    # Check that \u200d is kept, if it not part of a valid ZWJ emoji
    assert emoji.demojize('\U0001f476\U0001f3ff\u0308\u200d\U0001f476\U0001f3ff') == ':baby_dark_skin_tone:\u0308\u200d:baby_dark_skin_tone:'

    # Replace with different length
    index = [0]

    def replace_f(e, emoji_data):
        index[0] += 1
        if index[0] % 2 == 0:
            return 'X'
        else:
            return 'yyy'

    assert emoji.replace_emoji('\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE', replace_f) == 'yyyXyyyX'
