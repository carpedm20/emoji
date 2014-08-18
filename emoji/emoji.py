# -*- coding: utf-8 -*-
"""
    emoji.emoji
    ~~~~~~~~~~~

    :copyright: (c) 2014 by Taehoon Kim.
    :license: BSD, see LICENSE for more details.
"""
import re

from .code import emojiCodeDict

def emojize(text):
    pattern = re.compile('(:[a-z0-9\+\-_]+:)')

    def emorepl(match):
        value = match.group(1)

        if value in emojiCodeDict:
            return emojiCodeDict[value]

    return pattern.sub(emorepl, text)

