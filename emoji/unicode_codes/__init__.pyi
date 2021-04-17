# -*- coding: utf-8 -*-
from typing import Dict

from .en import *
from .es import *
from .pt import *
from .it import *

from .types import _EMOJI_UNICODE_T, _UNICODE_EMOJI_T

EMOJI_UNICODE: Dict[str, _EMOJI_UNICODE_T] = ...

UNICODE_EMOJI: Dict[str, _UNICODE_EMOJI_T] = ...
