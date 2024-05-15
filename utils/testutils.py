from typing import Generator, Dict, Any, Tuple, Iterable
import sys
import unicodedata
import emoji.unicode_codes
from typing_extensions import Literal

_NormalizationForm = Literal['NFC', 'NFD', 'NFKC', 'NFKD']


def ascii(s: str) -> str:
    """return escaped Code points for non-ascii chars like \U000AB123"""
    return s.encode("unicode-escape").decode()


def normalize(form: _NormalizationForm, s: str) -> str:
    return unicodedata.normalize(form, s)


def is_normalized(form: _NormalizationForm, s: str) -> bool:
    if sys.version_info >= (3, 8):
        return unicodedata.is_normalized(form, s)
    else:
        return normalize(form, s) == s


def all_language_packs() -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    for lang_code in emoji.LANGUAGES:
        yield (lang_code, emoji.unicode_codes.get_emoji_unicode_dict(lang_code))


def all_language_and_alias_packs(
) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    yield ('alias', emoji.unicode_codes.get_aliases_unicode_dict())
    yield from all_language_packs()


def get_language_packs(
        *langs: Iterable[str]) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
    for lang_code, lang_pack in all_language_and_alias_packs():
        if lang_code in langs:
            yield (lang_code, lang_pack)
