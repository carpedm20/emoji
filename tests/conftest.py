from typing import List
import random
import functools

import pytest


def pytest_sessionstart():
    # Increase cache size to unlimited size to avoid cache misses during tests
    import emoji.unicode_codes

    emoji.unicode_codes.get_emoji_by_name = functools.lru_cache(maxsize=None)(
        emoji.unicode_codes.get_emoji_by_name.__wrapped__
    )


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        '--shuffle',
        dest='shuffle',
        action='store_true',
        default=False,
        help='Run tests in random order',
    )


def pytest_collection_modifyitems(session: pytest.Session, items: List[pytest.Item]):
    if session.config.getoption('shuffle'):
        print('')
        print('Shuffling items for a random test order')
        random.shuffle(items)
