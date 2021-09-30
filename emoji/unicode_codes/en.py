# -*- coding: utf-8 -*-

"""Data literal storing emoji English names and Unicode codes."""

from emoji.unicode_codes.versions import *

__all__ = [
    'EMOJI_UNICODE_ENGLISH', 'UNICODE_EMOJI_ENGLISH',
    'EMOJI_ALIAS_UNICODE_ENGLISH', 'UNICODE_EMOJI_ALIAS_ENGLISH',
]

fully_qualified = STATUS["fully_qualified"]

EMOJI_UNICODE_ENGLISH = {value['en']: code for code, value in EMOJI_DATA.items() if value['status'] <= fully_qualified}

UNICODE_EMOJI_ENGLISH = {v: k for k, v in EMOJI_UNICODE_ENGLISH.items()}

EMOJI_ALIAS_UNICODE_ENGLISH = dict(EMOJI_UNICODE_ENGLISH.items(), **{
    value['alias']: code for code, value in EMOJI_DATA.items() if 'alias' in value and value['status'] <= fully_qualified
})

UNICODE_EMOJI_ALIAS_ENGLISH = {v: k for k, v in EMOJI_ALIAS_UNICODE_ENGLISH.items()}
