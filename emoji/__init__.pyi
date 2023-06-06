from .core import (
    demojize as demojize,
    distinct_emoji_list as distinct_emoji_list,
    emoji_count as emoji_count,
    emoji_list as emoji_list,
    emojize as emojize,
    is_emoji as is_emoji,
    replace_emoji as replace_emoji,
    version as version,
    analyze as analyze,
    config as config,
)
from .tokenizer import (
    Token as Token,
    EmojiMatch as EmojiMatch,
    EmojiMatchZWJ as EmojiMatchZWJ,
    EmojiMatchZWJNonRGI as EmojiMatchZWJNonRGI,
)


from .unicode_codes import EMOJI_DATA, LANGUAGES, STATUS

__all__ = [
    # emoji.core
    'emojize', 'demojize', 'analyze', 'config',
    'emoji_list', 'distinct_emoji_list', 'emoji_count',
    'replace_emoji', 'is_emoji', 'version',
    'Token', 'EmojiMatch', 'EmojiMatchZWJ', 'EmojiMatchZWJNonRGI',
    # emoji.unicode_codes
    'EMOJI_DATA', 'STATUS', 'LANGUAGES',
]

__version__: str
__author__: str
__email__: str
__source__: str
__license__: str