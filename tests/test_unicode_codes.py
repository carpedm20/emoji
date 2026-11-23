"""Unittests for emoji.unicode_codes."""

from typing import Set
import emoji
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


def test_get_emoji_by_name_after_load_language():
    # A Spanish-only short-name: absent from EMOJI_DATA until emoji_es.json is loaded.
    name = ':medalla_de_oro:'
    expected = '\U0001f947'
    codes = emoji.unicode_codes

    # Force the pre-load state so the test is independent of test order.
    codes._loaded_keys.discard('es')  # type: ignore[reportPrivateUsage]
    for data in codes.EMOJI_DATA.values():
        data.pop('es', None)
    codes.get_emoji_by_name.cache_clear()

    try:
        # First lookup caches a negative result because Spanish data isn't loaded.
        assert codes.get_emoji_by_name(name, 'es') is None

        # load_language() must populate EMOJI_DATA and invalidate stale lookups.
        emoji.config.load_language('es')

        assert codes.get_emoji_by_name(name, 'es') == expected
        assert emoji.emojize(name, language='es') == expected
    finally:
        codes.get_emoji_by_name.cache_clear()


def test_get_emoji_by_name_unknown_stays_none():
    # Control: an unknown short-name must stay unknown, before and after a
    # language load invalidates the cache.
    codes = emoji.unicode_codes
    unknown = ':definitely_not_a_real_emoji_name:'

    codes.get_emoji_by_name.cache_clear()
    assert codes.get_emoji_by_name(unknown, 'es') is None

    emoji.config.load_language('es')
    assert codes.get_emoji_by_name(unknown, 'es') is None


def test_get_emoji_by_name_cache_hit_without_language_load():
    # Control: repeated lookups still hit the cache when nothing was loaded.
    codes = emoji.unicode_codes
    codes.get_emoji_by_name.cache_clear()

    name = ':thumbs_up:'
    expected = '\U0001f44d'
    assert codes.get_emoji_by_name(name, 'en') == expected

    hits_before = codes.get_emoji_by_name.cache_info().hits
    assert codes.get_emoji_by_name(name, 'en') == expected
    assert codes.get_emoji_by_name.cache_info().hits > hits_before
