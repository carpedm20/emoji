"""Unittests for emoji.analyze()"""

import emoji


def test_analyze():
    assert list(emoji.analyze('')) == []

    assert list(emoji.analyze('', non_emoji=True)) == []

    assert list(emoji.analyze('abc')) == []

    assert list(emoji.analyze('abc', non_emoji=True)) == [
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
    ]

    result = list(emoji.analyze('abc\U0001f472'))
    assert len(result) == 1
    assert not isinstance(result[0].value, str)
    assert result[0].value.emoji == '\U0001f472'

    result = list(emoji.analyze('abc\U0001f472', non_emoji=True))
    assert result[0].value == 'a'
    assert not isinstance(result[3].value, str)
    assert result[3].value.emoji == '\U0001f472'

    result = list(emoji.analyze('\U0001f477\U0001f3fb\U0000200d\U00002640'))
    assert len(result) == 1
    assert not isinstance(result[0].value, str)
    assert result[0].value.emoji == '\U0001f477\U0001f3fb\U0000200d\U00002640'

    result = list(
        emoji.analyze('\U0001f477\U0001f3fc\U0001f477\U0001f3fb\U0000200d\U00002640')
    )
    assert len(result) == 2
    assert not isinstance(result[0].value, str)
    assert result[0].value.emoji == '\U0001f477\U0001f3fc'
    assert not isinstance(result[1].value, str)
    assert result[1].value.emoji == '\U0001f477\U0001f3fb\U0000200d\U00002640'


def test_analyze_non_rgi_zwj():
    result = list(
        emoji.analyze(
            '\U0001f468\U0001f3ff\U0000200d\U0001f469\U0001f3fb\U0000200d\U0001f467\U0001f3fd'
        )
    )
    assert len(result) == 1
    assert not isinstance(result[0].value, str)
    assert (
        result[0].value.emoji
        == '\U0001f468\U0001f3ff\U0000200d\U0001f469\U0001f3fb\U0000200d\U0001f467\U0001f3fd'
    )

    result = list(
        emoji.analyze(
            '\U0001f468\U0001f3ff\U0000200d\U0001f469\U0001f3fb\U0000200d\U0001f467\U0001f3fd',
            join_emoji=False,
        )
    )
    assert len(result) == 3
    assert not isinstance(result[0].value, str)
    assert result[0].value.emoji == '\U0001f468\U0001f3ff'
    assert not isinstance(result[1].value, str)
    assert result[1].value.emoji == '\U0001f469\U0001f3fb'
    assert not isinstance(result[2].value, str)
    assert result[2].value.emoji == '\U0001f467\U0001f3fd'

    result = list(
        emoji.analyze(
            '\U0001f468\U0001f3ff\U0000200d\U0001f469\U0001f3fb\U0000200d\U0001f467\U0001f3fdx',
            join_emoji=False,
            non_emoji=True,
        )
    )
    assert len(result) == 6
    assert not isinstance(result[0].value, str)
    assert result[0].value.emoji == '\U0001f468\U0001f3ff'
    assert result[1].value == '\U0000200d'
    assert not isinstance(result[2].value, str)
    assert result[2].value.emoji == '\U0001f469\U0001f3fb'
    assert result[3].value == '\U0000200d'
    assert not isinstance(result[4].value, str)
    assert result[4].value.emoji == '\U0001f467\U0001f3fd'
    assert result[5].value == 'x'

    result = list(
        emoji.analyze(
            '\U0001f468\U0001f3ff\U0000200d\U0001f469\U0001f3fb\U0000200d\U0001f467\U0001f3fdx',
            join_emoji=True,
            non_emoji=True,
        )
    )
    assert len(result) == 2
    assert not isinstance(result[0].value, str)
    assert (
        result[0].value.emoji
        == '\U0001f468\U0001f3ff\U0000200d\U0001f469\U0001f3fb\U0000200d\U0001f467\U0001f3fd'
    )
    assert result[1].value == 'x'

    result = list(emoji.analyze('\u200d🦷\u200d🦷'))
    assert len(result) == 1
    assert isinstance(result[0].value, emoji.EmojiMatchZWJNonRGI)

    result = list(emoji.analyze('\u200d🦷\u200d🦷', join_emoji=False))
    assert len(result) == 2
    assert all(isinstance(token.value, emoji.EmojiMatch) for token in result)

    result = list(emoji.analyze('\u200d🦷\u200d🦷', join_emoji=False, non_emoji=True))
    assert len(result) == 4
    assert result[0].value == '\u200d'
    assert isinstance(result[1].value, emoji.EmojiMatch)
    assert result[2].value == '\u200d'
    assert isinstance(result[3].value, emoji.EmojiMatch)


def test_emoji_match():
    s = 'a\U0001f309b'
    token = next(emoji.analyze(s))
    assert isinstance(token, emoji.Token)

    assert token.chars == s[1:-1]

    match = token.value

    assert isinstance(match, emoji.EmojiMatch)
    assert match.emoji == s[1:-1]
    assert match.start == 1
    assert match.end == 2
    assert not match.is_zwj()
    assert match.split() == match
    assert str(match).startswith('EmojiMatch(')

    s = 'a\U0001f468\U0000200d\U0001f467b'
    token = next(emoji.analyze(s))
    assert isinstance(token, emoji.Token)

    assert token.chars == s[1:-1]

    match = token.value

    assert isinstance(match, emoji.EmojiMatch)
    assert match.emoji == s[1:-1]
    assert match.start == 1
    assert match.end == 4
    assert match.is_zwj()
    assert str(match).startswith('EmojiMatch(')

    splitted = match.split()
    assert isinstance(splitted, emoji.EmojiMatchZWJ)
    assert splitted.emoji == s[1:-1]
    assert splitted.start == 1
    assert splitted.end == 4
    assert splitted.is_zwj()
    assert splitted.join() == s[1:-1]
    assert splitted.split() == splitted
    assert str(splitted).startswith('EmojiMatchZWJ(')
    assert len(splitted.emojis) == 2

    man, woman = splitted.emojis

    assert isinstance(man, emoji.EmojiMatch)
    assert man.start == 1
    assert man.end == 2

    assert isinstance(woman, emoji.EmojiMatch)
    assert woman.start == 3
    assert woman.end == 4
