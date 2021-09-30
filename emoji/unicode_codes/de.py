# -*- coding: utf-8 -*-

"""Data literal storing emoji German names and Unicode codes."""

from emoji.unicode_codes.versions import *

__all__ = ['EMOJI_UNICODE_GERMAN', 'UNICODE_EMOJI_GERMAN',]


fully_qualified = STATUS["fully_qualified"]

EMOJI_UNICODE_GERMAN = {value['de']: code for code, value in EMOJI_DATA.items() if 'de' in value and value['status'] <= fully_qualified}

UNICODE_EMOJI_GERMAN = {v: k for k, v in EMOJI_UNICODE_GERMAN.items()}
