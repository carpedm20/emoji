# -*- coding: utf-8 -*-

"""Data literal storing emoji Italian names and Unicode codes."""

from emoji.unicode_codes.versions import *

__all__ = ['EMOJI_UNICODE_ITALIAN', 'UNICODE_EMOJI_ITALIAN',]


fully_qualified = STATUS["fully_qualified"]

EMOJI_UNICODE_ITALIAN = {value['it']: code for code, value in EMOJI_DATA.items() if 'it' in value and value['status'] <= fully_qualified}

UNICODE_EMOJI_ITALIAN = {v: k for k, v in EMOJI_UNICODE_ITALIAN.items()}
