# -*- coding: UTF-8 -*-


"""
Unittests for emoji.unicode_codes
"""


import emoji


def test_emoji_names():

    for is_alias, group in (
            (False, emoji.unicode_codes.EMOJI_UNICODE),
            (True, emoji.unicode_codes.EMOJI_ALIAS_UNICODE)):
        for name, ucode in group.items():
            assert name.startswith(':') and name.endswith(':') and len(name) >= 3
            emj = emoji.emojize(name, is_alias=is_alias)
            assert emj == ucode, "%s != %s" % (emoji.emojize(name), ucode)
            # print(emoji.emojize(name))
            # try:
            #     assert emoji.emojize(name) == ucode, "%s != %s" % (name, ucode)
            # except:
            #     raise ValueError
            #     print(name)
            # assert emoji.emojize(name) == emoji.unicode_codes.EMOJI_UNICODE[name],\
            #     "%s != %s" % (name, ucode)
        break
