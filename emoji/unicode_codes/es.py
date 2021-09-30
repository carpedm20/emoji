# -*- coding: utf-8 -*-

"""Data literal storing emoji Spanish names and Unicode codes."""

from emoji.unicode_codes.versions import *

__all__ = ['EMOJI_UNICODE_SPANISH', 'UNICODE_EMOJI_SPANISH',]


fully_qualified = STATUS["fully_qualified"]

EMOJI_UNICODE_SPANISH = {value['es']: code for code, value in EMOJI_DATA.items() if 'es' in value and value['status'] <= fully_qualified}

UNICODE_EMOJI_SPANISH = {v: k for k, v in EMOJI_UNICODE_SPANISH.items()}
