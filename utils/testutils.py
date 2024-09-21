from typing import Generator, Dict, Any, Tuple, Iterable
import sys
import unicodedata

import pytest
if sys.version_info < (3, 9):
    from typing_extensions import Literal  # type: ignore
else:
    from typing import Literal

import emoji.unicode_codes

_NormalizationForm = Literal['NFC', 'NFD', 'NFKC', 'NFKD']


@pytest.fixture
def load_all_languages():
    """Load all keys from JSON files into EMOJI_DATA and
    build all language packs (i.e. fill the cache)"""
    emoji.emojize('', language='alias')
    for lang_code in emoji.LANGUAGES:
        emoji.emojize('', language=lang_code)
    yield


def ascii(s: str) -> str:
    """return escaped Code points for non-ascii chars like \U000ab123"""
    return s.encode('unicode-escape').decode()


def normalize(form: _NormalizationForm, s: str) -> str:
    return unicodedata.normalize(form, s)


def is_normalized(form: _NormalizationForm, s: str) -> bool:
    if sys.version_info >= (3, 8):
        return unicodedata.is_normalized(form, s)
    else:
        return normalize(form, s) == s


_EMOJI_UNICODE: Dict[str, Any] = {
    lang: None for lang in emoji.LANGUAGES
}  # Cache for the language dicts
_ALIASES_UNICODE: Dict[str, str] = {}  # Cache for the aliases dict


def get_emoji_unicode_dict(lang: str) -> Dict[str, Any]:
    """Generate dict containing all fully-qualified and component emoji name for a language
    The dict is only generated once per language and then cached in _EMOJI_UNICODE[lang]"""

    emoji.config.load_language(lang)
    if not _EMOJI_UNICODE[lang]:
        _EMOJI_UNICODE[lang] = {
            data[lang]: emj
            for emj, data in emoji.EMOJI_DATA.items()
            if lang in data and data['status'] <= emoji.STATUS['fully_qualified']
        }

    return _EMOJI_UNICODE[lang]


def get_aliases_unicode_dict() -> Dict[str, str]:
    """Generate dict containing all fully-qualified and component aliases
    The dict is only generated once and then cached in _ALIASES_UNICODE"""

    if not _ALIASES_UNICODE:
        _ALIASES_UNICODE.update(get_emoji_unicode_dict('en'))
        for emj, data in emoji.EMOJI_DATA.items():
            if 'alias' in data and data['status'] <= emoji.STATUS['fully_qualified']:
                for alias in data['alias']:
                    _ALIASES_UNICODE[alias] = emj

    return _ALIASES_UNICODE


def all_language_packs() -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    for lang_code in emoji.LANGUAGES:
        yield (lang_code, get_emoji_unicode_dict(lang_code))


def all_language_and_alias_packs() -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    yield ('alias', get_aliases_unicode_dict())
    yield from all_language_packs()


def get_language_packs(
    *langs: Iterable[str],
) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    for lang_code, lang_pack in all_language_and_alias_packs():
        if lang_code in langs:
            yield (lang_code, lang_pack)
