"""Unittests for emoji.analyze()"""


import emoji


def test_analyze():
    assert list(emoji.analyze('')) == []

    assert list(emoji.analyze('', non_emoji=True)) == []

    assert list(emoji.analyze('abc')) == []

    assert list(emoji.analyze('abc', non_emoji=True)) == [('a', 'a'), ('b', 'b'), ('c', 'c')]

    result = list(emoji.analyze('abc\U0001F472'))
    assert len(result) == 1
    assert result[0].value.emoji == '\U0001F472'

    result = list(emoji.analyze('abc\U0001F472', non_emoji=True))
    assert result[0].value == 'a'
    assert result[3].value.emoji == '\U0001F472'

    result = list(emoji.analyze('\U0001F477\U0001F3FB\U0000200D\U00002640'))
    assert len(result) == 1
    assert result[0].value.emoji == '\U0001F477\U0001F3FB\U0000200D\U00002640'

    result = list(emoji.analyze('\U0001F477\U0001F3FC\U0001F477\U0001F3FB\U0000200D\U00002640'))
    assert len(result) == 2
    assert result[0].value.emoji == '\U0001F477\U0001F3FC'
    assert result[1].value.emoji == '\U0001F477\U0001F3FB\U0000200D\U00002640'


def test_analyze_non_rgi_zwj():
    result = list(emoji.analyze('\U0001F468\U0001F3FF\U0000200D\U0001F469\U0001F3FB\U0000200D\U0001F467\U0001F3FD'))
    assert len(result) == 1
    assert result[0].value.emoji == '\U0001F468\U0001F3FF\U0000200D\U0001F469\U0001F3FB\U0000200D\U0001F467\U0001F3FD'

    result = list(emoji.analyze('\U0001F468\U0001F3FF\U0000200D\U0001F469\U0001F3FB\U0000200D\U0001F467\U0001F3FD', join_emoji=False))
    assert len(result) == 3
    assert result[0].value.emoji == '\U0001F468\U0001F3FF'
    assert result[1].value.emoji == '\U0001F469\U0001F3FB'
    assert result[2].value.emoji == '\U0001F467\U0001F3FD'

    result = list(emoji.analyze('\U0001F468\U0001F3FF\U0000200D\U0001F469\U0001F3FB\U0000200D\U0001F467\U0001F3FDx', join_emoji=False, non_emoji=True))
    assert len(result) == 6
    assert result[0].value.emoji == '\U0001F468\U0001F3FF'
    assert result[1].value == '\U0000200D'
    assert result[2].value.emoji == '\U0001F469\U0001F3FB'
    assert result[3].value == '\U0000200D'
    assert result[4].value.emoji == '\U0001F467\U0001F3FD'
    assert result[5].value == 'x'

    result = list(emoji.analyze('\U0001F468\U0001F3FF\U0000200D\U0001F469\U0001F3FB\U0000200D\U0001F467\U0001F3FDx', join_emoji=True, non_emoji=True))
    assert len(result) == 2
    assert result[0].value.emoji == '\U0001F468\U0001F3FF\U0000200D\U0001F469\U0001F3FB\U0000200D\U0001F467\U0001F3FD'
    assert result[1].value == 'x'

    result = list(emoji.analyze("\u200D🦷\u200D🦷"))
    assert len(result) == 1
    assert isinstance(result[0].value, emoji.EmojiMatchZWJNonRGI)

    result = list(emoji.analyze("\u200D🦷\u200D🦷", join_emoji=False))
    assert len(result) == 2
    assert all(isinstance(token.value, emoji.EmojiMatch) for token in result)

    result = list(emoji.analyze("\u200D🦷\u200D🦷", join_emoji=False, non_emoji=True))
    assert len(result) == 4
    assert result[0].value == '\u200D'
    assert isinstance(result[1].value, emoji.EmojiMatch)
    assert result[2].value == '\u200D'
    assert isinstance(result[3].value, emoji.EmojiMatch)


def test_emoji_match():
    s = 'a\U0001F309b'
    token = next(emoji.analyze(s))
    assert isinstance(token, emoji.Token)

    assert token.chars == s[1:-1]

    match = token.value

    assert isinstance(match, emoji.EmojiMatch)
    assert match.emoji == s[1:-1]
    assert match.start == 1
    assert match.end == 2
    assert match.is_zwj() == False
    assert str(match).startswith('EmojiMatch(')


def test_emoji_match():
    s = 'a\U0001F309b'
    token = next(emoji.analyze(s))
    assert isinstance(token, emoji.Token)

    assert token.chars == s[1:-1]

    match = token.value

    assert isinstance(match, emoji.EmojiMatch)
    assert match.emoji == s[1:-1]
    assert match.start == 1
    assert match.end == 2
    assert match.is_zwj() == False
    assert match.split() == match
    assert str(match).startswith('EmojiMatch(')


    s = 'a\U0001F468\U0000200D\U0001F467b'
    token = next(emoji.analyze(s))
    assert isinstance(token, emoji.Token)

    assert token.chars == s[1:-1]

    match = token.value

    assert isinstance(match, emoji.EmojiMatch)
    assert match.emoji == s[1:-1]
    assert match.start == 1
    assert match.end == 4
    assert match.is_zwj() == True
    assert str(match).startswith('EmojiMatch(')

    splitted = match.split()
    assert isinstance(splitted, emoji.EmojiMatchZWJ)
    assert splitted.emoji == s[1:-1]
    assert splitted.start == 1
    assert splitted.end == 4
    assert splitted.is_zwj() == True
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
