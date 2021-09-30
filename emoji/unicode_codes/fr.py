# -*- coding: utf-8 -*-

"""Data literal storing emoji French names and Unicode codes."""

from emoji.unicode_codes.versions import *

__all__ = ['EMOJI_UNICODE_FRENCH', 'UNICODE_EMOJI_FRENCH',]


fully_qualified = STATUS["fully_qualified"]

EMOJI_UNICODE_FRENCH = {value['fr']: code for code, value in EMOJI_DATA.items() if 'fr' in value and value['status'] <= fully_qualified}

UNICODE_EMOJI_FRENCH = {v: k for k, v in EMOJI_UNICODE_FRENCH.items()}
