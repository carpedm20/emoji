from typing import NamedTuple, Union, Dict, Iterator, Any

_SearchTree = Dict[str, Union['_SearchTree', dict[str, dict[str, Any]]]]

_SEARCH_TREE: _SearchTree


class EmojiMatch:
    emoji: str
    start: int
    end: int
    data: dict[str, Any] | None
    def __init__(self, emoji: str, start: int,
                 end: int, data: dict | None): ...

    def data_copy(self) -> Dict[str, Any]: ...
    def is_zwj(self) -> bool: ...
    def split(self) -> EmojiMatchZWJ | EmojiMatch: ...
    def __repr__(self) -> str: ...


class EmojiMatchZWJ(EmojiMatch):
    def __init__(self, match: EmojiMatch): ...
    def join(self) -> str: ...
    def is_zwj(self) -> bool: ...
    def split(self) -> EmojiMatchZWJ: ...
    def __repr__(self) -> str: ...


class EmojiMatchZWJNonRGI(EmojiMatchZWJ):
    def __init__(self, first_emoji_match: EmojiMatch,
                 second_emoji_match: EmojiMatch): ...


class Token(NamedTuple):
    chars: str
    value: str | EmojiMatch


def tokenize(string, keep_zwj: bool) -> Iterator[Token]: ...


def filter_tokens(matches: Iterator[Token], emoji_only: bool,
                  join_emoji: bool) -> Iterator[Token]: ...


def get_search_tree() -> _SearchTree: ...
