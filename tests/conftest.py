from typing import List
import random
import pytest


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--shuffle", dest="shuffle", action='store_true',
                     default=False, help="Run tests in random order")


def pytest_collection_modifyitems(session: pytest.Session,items: List[pytest.Item]):
    if session.config.getoption("shuffle"):
        print("")
        print("Shuffling items for a random test order")
        random.shuffle(items)
