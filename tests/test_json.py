import sys
import functools

import pytest

import emoji


@pytest.fixture
def clean_module():
    """Ensures a fresh import and init of the emoji module.
    Unloads all emoji.* modules, then loads the emoji module,
    runs the test function, then deletes all the emoji.* modules
    """
    global emoji
    for name in [
        name
        for name in sys.modules
        if name.startswith('emoji') or name.startswith('test')
    ]:
        del sys.modules[name]
    import emoji

    # Increase cache size to avoid cache misses during tests
    emoji.unicode_codes.get_emoji_by_name = functools.lru_cache(maxsize=None)(  # type:ignore
        emoji.unicode_codes.get_emoji_by_name.__wrapped__  # type:ignore
    )

    yield
    for name in [
        name
        for name in sys.modules
        if name.startswith('emoji') or name.startswith('test')
    ]:
        del sys.modules[name]

    # Increase cache size to avoid cache misses during tests
    emoji.unicode_codes.get_emoji_by_name = functools.lru_cache(maxsize=None)(  # type:ignore
        emoji.unicode_codes.get_emoji_by_name.__wrapped__  # type:ignore
    )


def test_language_loaded_after_emojize(clean_module):  # type:ignore
    emoji.emojize('string', language='es')
    assert 'es' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]


def test_language_loaded_after_demojize(clean_module):  # type:ignore
    emoji.demojize('string', language='es')
    assert 'es' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]


def test_language_not_auto_loaded(clean_module):  # type:ignore
    assert 'es' not in emoji.EMOJI_DATA[emoji.emojize(':lion:')]


def test_key_access_load_language(clean_module):  # type:ignore
    assert 'es' not in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    with pytest.deprecated_call():
        assert emoji.EMOJI_DATA[emoji.emojize(':lion:')]['es']
    assert 'es' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    assert 'es' in emoji.EMOJI_DATA[emoji.emojize(':zebra:')]

    with pytest.raises(KeyError):
        emoji.EMOJI_DATA[emoji.emojize(':lion:')]['xyz']


def test_explicit_load_language(clean_module):  # type:ignore
    assert 'fr' not in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    emoji.config.load_language('fr')
    assert 'fr' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    assert emoji.EMOJI_DATA[emoji.emojize(':lion:')]['fr'] == ':tête_de_lion:'

    assert 'es' not in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    emoji.config.load_language('es')
    assert 'es' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]


def test_explict_load_all_languages(clean_module):  # type:ignore
    assert 'fr' not in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    assert 'es' not in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    emoji.config.load_language()
    assert 'es' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    assert 'fr' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    assert emoji.EMOJI_DATA[emoji.emojize(':lion:')]['fr'] == ':tête_de_lion:'


def test_load_language_multiple_times(clean_module):  # type:ignore
    assert 'fr' not in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    for _ in range(10000):
        emoji.config.load_language('fr')
    assert 'fr' in emoji.EMOJI_DATA[emoji.emojize(':lion:')]
    assert emoji.EMOJI_DATA[emoji.emojize(':lion:')]['fr'] == ':tête_de_lion:'


unsupported_languages = ['', ' ', '1', 'e', 'z', 'zz', 'ZZ', 'EN', 'ES', 'xyz', 'eses']


@pytest.mark.parametrize('lang', unsupported_languages)
def test_load_unsupported_language(lang: str):
    with pytest.raises(NotImplementedError):
        emoji.config.load_language(lang)


@pytest.mark.parametrize('lang', unsupported_languages)
def test_access_unsupported_language(lang: str):
    with pytest.raises(KeyError):
        emoji.EMOJI_DATA[emoji.emojize(':lion:')][lang]


@pytest.mark.parametrize('lang', unsupported_languages)
def test_emojize_unsupported_language(lang: str):
    with pytest.raises(NotImplementedError):
        emoji.emojize(':lion:', language=lang)

    with pytest.raises(NotImplementedError):
        emoji.demojize(':lion:', language=lang)
