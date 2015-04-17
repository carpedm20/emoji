"""
Unittests for emoji.unicode_codes
"""


import emoji.unicode_codes


def test_emoji_names():

    for name in emoji.unicode_codes.EMOJI_UNICODE.keys():
        assert name.startswith(':') and name.endswith(':') and len(name) >= 3
