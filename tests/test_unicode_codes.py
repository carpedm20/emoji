"""Unittests for emoji.unicode_codes."""

from typing import Set
import emoji.unicode_codes
from testutils import get_language_packs


def test_emoji_english_names():
    for language, group in get_language_packs('en', 'alias'):
        for name, ucode in group.items():
            assert name.startswith(':') and name.endswith(':') and len(name) >= 3
            emj = emoji.emojize(name, language=language)
            assert emj == ucode, '"%s" == "%s"' % (emj, ucode)


def test_compare_normal_and_aliases():
    # There should always be more aliases than normal codes
    # since the aliases contain the normal codes

    english_pack = emoji.unicode_codes.get_emoji_unicode_dict('en')
    alias_pack = emoji.unicode_codes.get_aliases_unicode_dict()

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
