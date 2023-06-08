"""Tests for emoji that consist of multiple emoji joined with a u200D (ZWJ - zero width joiner)
This file contains tests that are irrespective of keeping/removing the ZWJ.
See test_zwj_remove.py for tests when the ZWJ is removed.
See test_zwj_keep.py for tests when the ZWJ is kept.
"""

import emoji


def test_non_rgi_zwj_emoji_list():
    matches = emoji.emoji_list('\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE')

    assert matches[0]["match_start"] == 0
    assert matches[0]["match_end"] == 1
    assert matches[0]["emoji"] == '\U0001F468'

    assert matches[1]["match_start"] == 2
    assert matches[1]["match_end"] == 4
    assert matches[1]["emoji"] == '\U0001F469\U0001F3FF'

    assert matches[2]["match_start"] == 5
    assert matches[2]["match_end"] == 7
    assert matches[2]["emoji"] == '\U0001F467\U0001F3FB'

    assert matches[3]["match_start"] == 8
    assert matches[3]["match_end"] == 10
    assert matches[3]["emoji"] == '\U0001F466\U0001F3FE'

    matches = emoji.emoji_list('abc\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FEyxz')

    assert matches[0]["match_start"] == 3
    assert matches[0]["match_end"] == 4
    assert matches[0]["emoji"] == '\U0001F468'

    assert matches[1]["match_start"] == 5
    assert matches[1]["match_end"] == 7
    assert matches[1]["emoji"] == '\U0001F469\U0001F3FF'

    assert matches[2]["match_start"] == 8
    assert matches[2]["match_end"] == 10
    assert matches[2]["emoji"] == '\U0001F467\U0001F3FB'

    assert matches[3]["match_start"] == 11
    assert matches[3]["match_end"] == 13
    assert matches[3]["emoji"] == '\U0001F466\U0001F3FE'

    matches = emoji.emoji_list('\U0001F9D1\U0000200D\U0001F9B3abcyxz\U0001FAC5\U0001F468\U0001F3FD\u200D\U0001F467\U0001F3FC\u200D\U0001F467\U0001F3FE')

    assert matches[0]["match_start"] == 0
    assert matches[0]["match_end"] == 3
    assert matches[0]["emoji"] == '\U0001F9D1\U0000200D\U0001F9B3'

    assert matches[1]["match_start"] == 9
    assert matches[1]["match_end"] == 10
    assert matches[1]["emoji"] == '\U0001FAC5'

    assert matches[2]["match_start"] == 10
    assert matches[2]["match_end"] == 12
    assert matches[2]["emoji"] == '\U0001F468\U0001F3FD'

    assert matches[3]["match_start"] == 13
    assert matches[3]["match_end"] == 15
    assert matches[3]["emoji"] == '\U0001F467\U0001F3FC'

    assert matches[4]["match_start"] == 16
    assert matches[4]["match_end"] == 18
    assert matches[4]["emoji"] == '\U0001F467\U0001F3FE'


def test_non_rgi_zwj_demojize():
    result = emoji.demojize('\U0001F9D1\U0001F3FC\U0000200D\U0001F3A8\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE')
    assert '\U0001F9D1\U0001F3FC\U0000200D\U0001F3A8' not in result
    assert '\U0001F468\u200d\U0001F469\U0001F3FF\u200d\U0001F467\U0001F3FB\u200d\U0001F466\U0001F3FE' not in result
    assert ':artist_medium-light_skin_tone:' in result

    result = emoji.demojize('Test \U0001F6B5\U0001F3FF\U0000200D\U00002642\U0000FE0F abc \U0001F468\U0001F3FF\u200d\U0001F469\U0001F3FE\u200d\U0001F466\U0001F3FD\u200d\U0001F467\U0001F3FB')
    assert '\U0001F6B5\U0001F3FF\U0000200D\U00002642\U0000FE0F' not in result
    assert '\U0001F468\U0001F3FF\u200d\U0001F469\U0001F3FE\u200d\U0001F466\U0001F3FD\u200d\U0001F467\U0001F3FB' not in result
    assert ':man_mountain_biking_dark_skin_tone:' in result
