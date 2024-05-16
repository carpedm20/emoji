from typing import Optional
from functools import lru_cache
from emoji.unicode_codes.data_dict import EMOJI_DATA, STATUS, LANGUAGES

__all__ = [
    'get_emoji_by_name',
    'EMOJI_DATA', 'STATUS', 'LANGUAGES'
]


@lru_cache(maxsize=4000)
def get_emoji_by_name(name: str, language: str) -> Optional[str]:
    """
    Find emoji by short-name in a specific language.
    Returns None if not found

    :param name: emoji short code e.g. ":banana:"
    :param language: language-code e.g. 'es', 'de', etc. or 'alias'
    """

    fully_qualified = STATUS['fully_qualified']

    if language == 'alias':
        for emj, data in EMOJI_DATA.items():
            if name in data.get('alias', []) and data['status'] <= fully_qualified:
                return emj
        language = 'en'

    for emj, data in EMOJI_DATA.items():
        if data.get(language) == name and data['status'] <= fully_qualified:
            return emj

    return None
