"""Tests for emoji that consist of multiple emoji joined with a u200D (ZWJ - zero width joiner)
This file contains tests that are irrespective of keeping/removing the ZWJ.
See test_zwj_remove.py for tests when the ZWJ is removed.
See test_zwj_keep.py for tests when the ZWJ is kept.
"""

import emoji


def test_non_rgi_zwj_emoji_list():
    matches = emoji.emoji_list(
        '\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
    )

    assert matches[0]['match_start'] == 0
    assert matches[0]['match_end'] == 1
    assert matches[0]['emoji'] == '\U0001f468'

    assert matches[1]['match_start'] == 2
    assert matches[1]['match_end'] == 4
    assert matches[1]['emoji'] == '\U0001f469\U0001f3ff'

    assert matches[2]['match_start'] == 5
    assert matches[2]['match_end'] == 7
    assert matches[2]['emoji'] == '\U0001f467\U0001f3fb'

    assert matches[3]['match_start'] == 8
    assert matches[3]['match_end'] == 10
    assert matches[3]['emoji'] == '\U0001f466\U0001f3fe'

    matches = emoji.emoji_list(
        'abc\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3feyxz'
    )

    assert matches[0]['match_start'] == 3
    assert matches[0]['match_end'] == 4
    assert matches[0]['emoji'] == '\U0001f468'

    assert matches[1]['match_start'] == 5
    assert matches[1]['match_end'] == 7
    assert matches[1]['emoji'] == '\U0001f469\U0001f3ff'

    assert matches[2]['match_start'] == 8
    assert matches[2]['match_end'] == 10
    assert matches[2]['emoji'] == '\U0001f467\U0001f3fb'

    assert matches[3]['match_start'] == 11
    assert matches[3]['match_end'] == 13
    assert matches[3]['emoji'] == '\U0001f466\U0001f3fe'

    matches = emoji.emoji_list(
        '\U0001f9d1\U0000200d\U0001f9b3abcyxz\U0001fac5\U0001f468\U0001f3fd\u200d\U0001f467\U0001f3fc\u200d\U0001f467\U0001f3fe'
    )

    assert matches[0]['match_start'] == 0
    assert matches[0]['match_end'] == 3
    assert matches[0]['emoji'] == '\U0001f9d1\U0000200d\U0001f9b3'

    assert matches[1]['match_start'] == 9
    assert matches[1]['match_end'] == 10
    assert matches[1]['emoji'] == '\U0001fac5'

    assert matches[2]['match_start'] == 10
    assert matches[2]['match_end'] == 12
    assert matches[2]['emoji'] == '\U0001f468\U0001f3fd'

    assert matches[3]['match_start'] == 13
    assert matches[3]['match_end'] == 15
    assert matches[3]['emoji'] == '\U0001f467\U0001f3fc'

    assert matches[4]['match_start'] == 16
    assert matches[4]['match_end'] == 18
    assert matches[4]['emoji'] == '\U0001f467\U0001f3fe'


def test_non_rgi_zwj_demojize():
    result = emoji.demojize(
        '\U0001f9d1\U0001f3fc\U0000200d\U0001f3a8\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
    )
    assert '\U0001f9d1\U0001f3fc\U0000200d\U0001f3a8' not in result
    assert (
        '\U0001f468\u200d\U0001f469\U0001f3ff\u200d\U0001f467\U0001f3fb\u200d\U0001f466\U0001f3fe'
        not in result
    )
    assert ':artist_medium-light_skin_tone:' in result

    result = emoji.demojize(
        'Test \U0001f6b5\U0001f3ff\U0000200d\U00002642\U0000fe0f abc \U0001f468\U0001f3ff\u200d\U0001f469\U0001f3fe\u200d\U0001f466\U0001f3fd\u200d\U0001f467\U0001f3fb'
    )
    assert '\U0001f6b5\U0001f3ff\U0000200d\U00002642\U0000fe0f' not in result
    assert (
        '\U0001f468\U0001f3ff\u200d\U0001f469\U0001f3fe\u200d\U0001f466\U0001f3fd\u200d\U0001f467\U0001f3fb'
        not in result
    )
    assert ':man_mountain_biking_dark_skin_tone:' in result


def test_malformed_zwj_no_emoji():
    s = '\u200d'
    assert emoji.replace_emoji(s) == s

    s = '\u200d\u200d'
    assert emoji.replace_emoji(s) == s

    s = '\u200d\u200d\u200d'
    assert emoji.replace_emoji(s) == s

    s = 'Has\u200din the middle'
    assert emoji.replace_emoji(s) == s

    s = '\u200dStarts With'
    assert emoji.replace_emoji(s) == s

    s = 'Ends With\u200d'
    assert emoji.replace_emoji(s) == s

    s = 'Multiple\u200d\u200d\u200din the middle'
    assert emoji.replace_emoji(s) == s

    s = '\u200d\u200dStarts With two'
    assert emoji.replace_emoji(s) == s

    s = '\u200d\u200d\u200dStarts With three'
    assert emoji.replace_emoji(s) == s

    s = 'Ends With two\u200d\u200d'
    assert emoji.replace_emoji(s) == s

    s = 'Ends With three\u200d\u200d\u200d'
    assert emoji.replace_emoji(s) == s


def test_malformed_zwj_mixed_with_emoji():
    emoji.config.demojize_keep_zwj = True  # Restore default config value

    i = 'Has🦷\u200din the middle'
    o = 'Has:tooth:\u200din the middle'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Has\u200d🦷in the middle'
    o = 'Has\u200d:tooth:in the middle'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d🦷Starts with'
    o = '\u200d:tooth:Starts with'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '🦷\u200dStarts with'
    o = ':tooth:\u200dStarts with'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Ends with \u200d🦷'
    o = 'Ends with \u200d:tooth:'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Ends with 🦷\u200d'
    o = 'Ends with :tooth:\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Multiple 🦷\u200d🦷\u200d in the middle'
    o = 'Multiple :tooth:\u200d:tooth:\u200d in the middle'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Multiple 🦷🦷\u200d\u200d in the middle'
    o = 'Multiple :tooth::tooth:\u200d\u200d in the middle'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Multiple \u200d\u200d🦷🦷 in the middle'
    o = 'Multiple \u200d\u200d:tooth::tooth: in the middle'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d🦷Starts with two'
    o = '\u200d\u200d:tooth:Starts with two'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d\u200d🦷Starts with three'
    o = '\u200d\u200d\u200d:tooth:Starts with three'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Ends with two \u200d\u200d🦷'
    o = 'Ends with two \u200d\u200d:tooth:'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Ends with two 🦷\u200d\u200d'
    o = 'Ends with two :tooth:\u200d\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Ends with three \u200d\u200d\u200d🦷'
    o = 'Ends with three \u200d\u200d\u200d:tooth:'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = 'Ends with three 🦷\u200d\u200d\u200d'
    o = 'Ends with three :tooth:\u200d\u200d\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '🦷\u200d'
    o = ':tooth:\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d🦷'
    o = '\u200d:tooth:'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d🦷'
    o = '\u200d\u200d:tooth:'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '🦷\u200d\u200d'
    o = ':tooth:\u200d\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d🦷\u200d'
    o = '\u200d:tooth:\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d🦷\u200d\u200d'
    o = '\u200d\u200d:tooth:\u200d\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d\u200d🦷\u200d\u200d'
    o = '\u200d\u200d\u200d:tooth:\u200d\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d🦷\u200d\u200d\u200d'
    o = '\u200d\u200d:tooth:\u200d\u200d\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '🦷\u200d\u200d🦷\u200d\u200d\u200d'
    o = ':tooth:\u200d\u200d:tooth:\u200d\u200d\u200d'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d🦷🦷\u200d\u200d\u200d🦷'
    o = '\u200d\u200d:tooth::tooth:\u200d\u200d\u200d:tooth:'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'

    i = '\u200d\u200d🦷\u200d\u200d\u200d🦷'
    o = '\u200d\u200d:tooth:\u200d\u200d\u200d:tooth:'
    assert emoji.demojize(i) == o, f'{i!r} != {o!r}'
