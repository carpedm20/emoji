"""Unittests for emoji.unicode_codes."""

from typing import Set
import emoji.unicode_codes
from testutils import (
    get_language_packs,
    get_aliases_unicode_dict,
    get_emoji_unicode_dict,
)


def test_emoji_english_names():
    for language, group in get_language_packs('en', 'alias'):
        for name, ucode in group.items():
            assert name.startswith(':') and name.endswith(':') and len(name) >= 3
            emj = emoji.emojize(name, language=language)
            assert emj == ucode, '"%s" == "%s"' % (emj, ucode)


def test_compare_normal_and_aliases():
    # There should always be more aliases than normal codes
    # since the aliases contain the normal codes

    english_pack = get_emoji_unicode_dict('en')
    alias_pack = get_aliases_unicode_dict()

    assert len(english_pack) < len(alias_pack)


def test_no_alias_duplicates():
    # There should not be two emoji with the same alias
    # (aliases still can be the same as another 'en'-name)
    all_aliases: Set[str] = set()
    for data in emoji.EMOJI_DATA.values():
        if data['status'] <= emoji.STATUS['fully_qualified'] and 'alias' in data:
            for alias in data['alias']:
                assert alias not in all_aliases
                all_aliases.add(alias)


def test_get_emoji_by_alias():
    # Compare get_emoji_by_name() to get_aliases_unicode_dict()
    for alias, emj in get_aliases_unicode_dict().items():
        assert emoji.unicode_codes.get_emoji_by_name(alias, 'alias') == emj


def test_get_emoji_by_name():
    # Compare get_emoji_by_name() to get_emoji_unicode_dict()
    for lang in emoji.LANGUAGES:
        for name, emj in get_emoji_unicode_dict(lang).items():
            assert emoji.unicode_codes.get_emoji_by_name(name, lang) == emj
