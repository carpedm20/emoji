# -*- coding: UTF-8 -*-

import re
from typing import Tuple, Optional, List, Dict, Union



def emojize(
        string: str,
        use_aliases: bool = ...,
        delimiters: Tuple[str, str] = ...,
        variant: Optional[str] = ...,
        language: str = ...,
) -> str: ...


def demojize(
        string: str,
        use_aliases: bool = ...,
        delimiters: Tuple[str, str] = ...,
        language: str = ...,
) -> str: ...


def replace_emoji(string: str, replace: str = ..., language: str = ...) -> str: ...


def get_emoji_regexp(language: str = ...) -> re.Pattern: ...


def emoji_lis(string: str, language: str = ...) -> List[Dict[str, Union[str, int]]]: ...


def distinct_emoji_lis(string: str, language: str = ...) -> List[str]: ...


def emoji_count(string: str) -> int: ...
