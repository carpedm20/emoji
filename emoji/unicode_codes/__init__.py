from typing import Any, Dict, Optional
from functools import lru_cache
from emoji.unicode_codes.data_dict import *

__all__ = [
    'get_emoji_by_name', 'get_emoji_unicode_dict', 'get_aliases_unicode_dict',
    'EMOJI_DATA', 'STATUS', 'LANGUAGES'
]


_EMOJI_UNICODE: Dict[str, Any] = {lang: None for lang in LANGUAGES}  # Cache for the language dicts

_ALIASES_UNICODE: Dict[str, str] = {}  # Cache for the aliases dict


@lru_cache(maxsize=4000)
def get_emoji_by_name(name: str, lang: str) -> Optional[str]:
    """Find emoji in a specific language or return None if not found"""

    fully_qualified = STATUS['fully_qualified']

    if lang == 'alias':
        for emj, data in EMOJI_DATA.items():
            if name in data.get('alias', []) and data['status'] <= fully_qualified:
                return emj
        lang = 'en'

    for emj, data in EMOJI_DATA.items():
        if data.get(lang) == name and data['status'] <= fully_qualified:
            return emj

    return None


def get_emoji_unicode_dict(lang: str) -> Dict[str, Any]:
    """Generate dict containing all fully-qualified and component emoji name for a language
    The dict is only generated once per language and then cached in _EMOJI_UNICODE[lang]"""

    if _EMOJI_UNICODE[lang] is None:
        _EMOJI_UNICODE[lang] = {data[lang]: emj for emj, data in EMOJI_DATA.items()
                                if lang in data and data['status'] <= STATUS['fully_qualified']}

    return _EMOJI_UNICODE[lang]


def get_aliases_unicode_dict() -> Dict[str, str]:
    """Generate dict containing all fully-qualified and component aliases
    The dict is only generated once and then cached in _ALIASES_UNICODE"""

    if not _ALIASES_UNICODE:
        _ALIASES_UNICODE.update(get_emoji_unicode_dict('en'))
        for emj, data in EMOJI_DATA.items():
            if 'alias' in data and data['status'] <= STATUS['fully_qualified']:
                for alias in data['alias']:
                    _ALIASES_UNICODE[alias] = emj

    return _ALIASES_UNICODE
