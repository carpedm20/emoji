# -*- coding: utf-8 -*-

"""Data literal storing emoji Portuguese names and Unicode codes."""

from emoji.unicode_codes.versions import *

__all__ = ['EMOJI_UNICODE_PORTUGUESE', 'UNICODE_EMOJI_PORTUGUESE',]


fully_qualified = STATUS["fully_qualified"]

EMOJI_UNICODE_PORTUGUESE = {value['pt']: code for code, value in EMOJI_DATA.items() if 'pt' in value and value['status'] <= fully_qualified}

UNICODE_EMOJI_PORTUGUESE = {v: k for k, v in EMOJI_UNICODE_PORTUGUESE.items()}
