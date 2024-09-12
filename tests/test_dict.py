"""Unittests for the big dict of dicts containing all emoji"""

from typing import Set, Dict
import re
import emoji

from testutils import load_all_languages as load_all_languages


def test_all_languages_list(load_all_languages):  # type:ignore
    """Compare all language keys in EMOJI_DATA with the emoji.LANGUAGES list"""

    langs: Set[str] = set()
    for item in emoji.EMOJI_DATA.values():
        langs.update(item.keys())
    all_languages = {lang for lang in langs if len(lang) == 2 and lang.lower() == lang}

    assert set(emoji.LANGUAGES) == all_languages


def test_emoji_versions():
    """Check that every emoji has a valid version"""
    for item in emoji.EMOJI_DATA.values():
        assert 'E' in item
        v = item['E']
        assert isinstance(v, (int, float))
        assert v >= 0.6


def check_duplicate_names(lang: str):
    """Check that there are no duplicate names in the fully_qualified except for different variants"""
    seen: Dict[str, int] = {}
    for item in emoji.EMOJI_DATA.values():
        if item['status'] > emoji.STATUS['fully_qualified']:
            continue

        if lang not in item:
            continue

        name = item[lang]
        if name in seen and 'variant' in item:
            seen[name] += 1
        else:
            assert name not in seen
            seen[name] = 0


def test_duplicate_names(load_all_languages):  # type:ignore
    """Check that there are no duplicate names in the fully_qualified except for different variants"""
    for lang in emoji.LANGUAGES:
        check_duplicate_names(lang)


def test_name_valid(load_all_languages):  # type:ignore
    """Check that every name starts with colons and does not contain other colons or whitespace"""

    pattern = re.compile(r':[^:\s]+:')
    for item in emoji.EMOJI_DATA.values():
        for lang in emoji.LANGUAGES:
            if lang in item:
                name = item[lang]
                assert pattern.match(name)
