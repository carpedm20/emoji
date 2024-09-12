"""Tests for emoji that consist of multiple emoji joined with a u200D (ZWJ - zero width joiner)
This file contains tests when the ZWJ is kept in place by demojize/replace_emoji.
See test_zwj_remove.py for tests when the ZWJ is removed.
"""

from typing import Any, Dict
import emoji


def ascii(s: str) -> str:
    # return escaped Code points \U000AB123
    return s.encode('unicode-escape').decode()


def test_non_rgi_zwj_demojize():
    # These emoji are non-RGI ZWJ sequences. They should be decoded by demojize to their constituents.
    emoji.config.demojize_keep_zwj = True

    assert (
        emoji.demojize(
            '\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
        )
        == ':man:\u200d:woman_dark_skin_tone:\u200d:girl_light_skin_tone:\u200d:boy_medium-dark_skin_tone:'
    )

    assert (
        emoji.demojize(
            '\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
        )
        == ':man_dark_skin_tone:\u200d:woman_dark_skin_tone:\u200d:girl_light_skin_tone:\u200d:boy_medium-dark_skin_tone:'
    )

    assert (
        emoji.demojize(
            '\U0001f468\U0001f3ff\u200d\U0001f469\u200d\U0001f467\U0001f3fb\u200d\U0001f466'
        )
        == ':man_dark_skin_tone:\u200d:family_woman_girl::light_skin_tone:\u200d:boy:'
    )

    # https://www.unicode.org/Public/15.0.0/ucd/auxiliary/GraphemeBreakTest-15.0.0d1.html#s19
    assert (
        emoji.demojize('\U0001f3ff\U0001f476\u200d\U0001f6d1')
        == ':dark_skin_tone::baby:\u200d:stop_sign:'
    )

    # https://www.unicode.org/Public/15.0.0/ucd/auxiliary/GraphemeBreakTest-15.0.0d1.html#s20
    # Check that \u200d is kept, if it not part of a valid ZWJ emoji
    assert (
        emoji.demojize('\U0001f476\U0001f3ff\u0308\u200d\U0001f476\U0001f3ff')
        == ':baby_dark_skin_tone:\u0308\u200d:baby_dark_skin_tone:'
    )


def test_malformed_zwj_demojize():
    # These sequences are malformed in the sense that they are neither RGI nor non-RGI ZWJ sequences
    # Check that still all the emoji are decoded
    emoji.config.demojize_keep_zwj = True

    result = emoji.demojize(
        '\U0001f468\u200d\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
    )
    assert '\U0001f468' not in result
    assert '\U0001f3ff' not in result
    assert '\U0001f467\U0001f3fb' not in result
    assert '\U0001f466\U0001f3fe' not in result

    result = emoji.demojize(
        '\U0001f3ff\u200d\U0001f468\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
    )
    assert '\U0001f468' not in result
    assert '\U0001f3ff' not in result
    assert '\U0001f467\U0001f3fb' not in result
    assert '\U0001f466\U0001f3fe' not in result

    # Mix of emoji and other characters
    # Check that still all the emoji are decoded
    result = emoji.demojize(
        '\U0001f468\U0001f3ff\u200dabcd\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
    )
    assert '\U0001f468\U0001f3ff' not in result
    assert '\U0001f467\U0001f3fb' not in result
    assert '\U0001f466\U0001f3fe' not in result
    assert result.count('\u200d') == 3
    assert ':man_dark_skin_tone:' in result
    assert 'abcd' in result
    assert ':girl_light_skin_tone:' in result
    assert ':boy_medium-dark_skin_tone:' in result

    result = emoji.demojize(
        'W\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
    )
    assert '\U0001f469\U0001f3ff' not in result
    assert '\U0001f467\U0001f3fb' not in result
    assert '\U0001f466\U0001f3fe' not in result
    assert result.count('\u200d') == 3
    assert result.startswith('W')
    assert ':woman_dark_skin_tone:' in result
    assert ':girl_light_skin_tone:' in result
    assert ':boy_medium-dark_skin_tone:' in result

    result = emoji.demojize('\U0001f9d1\U0001f3fe\u200d\u200d\U0001f393')
    assert '\U0001f9d1\U0001f3fe' not in result
    assert '\U0001f393' not in result
    assert result.count('\u200d') == 2
    assert ':person_medium-dark_skin_tone:' in result
    assert ':graduation_cap:' in result


def test_non_rgi_zwj_replace():
    emoji.config.replace_emoji_keep_zwj = True

    assert (
        emoji.replace_emoji(
            '\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
            '',
        )
        == ''
    )
    assert (
        emoji.replace_emoji(
            '\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
            'X',
        )
        == 'X'
    )

    assert (
        emoji.replace_emoji(
            '\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
            '',
        )
        == ''
    )
    assert (
        emoji.replace_emoji(
            '\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
            'X',
        )
        == 'X'
    )

    assert (
        emoji.replace_emoji(
            '\U0001f468\U0001f3ff\u200d\U0001f469\u200d\U0001f467\U0001f3fb\u200d\U0001f466',
            '',
        )
        == ''
    )
    assert (
        emoji.replace_emoji(
            '\U0001f468\U0001f3ff\u200d\U0001f469\u200d\U0001f467\U0001f3fb\u200d\U0001f466',
            'X',
        )
        == 'XX'
    )

    assert emoji.replace_emoji('\U0001f3ff\U0001f476\u200d\U0001f6d1', 'X') == 'XX'

    assert (
        emoji.replace_emoji('\U0001f476\U0001f3ff\u0308\u200d\U0001f476\U0001f3ff', 'X')
        == 'X\u0308\u200dX'
    )

    # Replace with different length
    index = [0]

    def replace_f(e: str, emoji_data: Dict[str, Any]) -> str:
        index[0] += 1
        if index[0] % 2 == 0:
            return 'X'
        else:
            return 'yyy'

    assert (
        emoji.replace_emoji(
            'A\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe\U0001f468\U0001f3fb\u200d\U0001f469\U0001f3fc\u200d\U0001f467\U0001f3fe\U0001f469\U0001f3feB',
            replace_f,
        )
        == 'AyyyXyyyB'
    )


def test_non_rgi_zwj_reversible():
    emoji.config.demojize_keep_zwj = True
    for emj in [
        '\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
        '\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
        '\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3fe\u200d\U0001f466\U0001f3fd\u200d\U0001f467\U0001f3fb',
        'Test \U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe abc',
        '\U0001f468\U0000200d\U00002708\U0000fe0f\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
        '\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3fe\u200d\U0001f466\U0001f3fd\u200d\U0001f467\U0001f3fb\U0001f64e\U0001f3fd\U0000200d\U00002642\U0000fe0f',
        '\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe',
        '\U0001f3ff\U0001f476\u200d\U0001f6d1',
    ]:
        assert emoji.emojize(emoji.demojize(emj)) == emj
