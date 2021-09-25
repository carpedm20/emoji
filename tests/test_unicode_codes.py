# -*- coding: UTF-8 -*-


"""Unittests for emoji.unicode_codes."""


import emoji


def test_emoji_english_names():

    for use_aliases, group in (
            (False, emoji.unicode_codes.EMOJI_UNICODE['en']),
            (True, emoji.unicode_codes.EMOJI_ALIAS_UNICODE_ENGLISH)
    ):
        for name, ucode in group.items():
            assert name.startswith(':') and name.endswith(':') and len(name) >= 3
            emj = emoji.emojize(name, use_aliases=use_aliases)
            assert emj == ucode, '%s != %s' % (emoji.emojize(name), ucode)


def test_compare_normal_and_aliases():
    # There should always be more aliases than normal codes
    # since the aliases contain the normal codes
    assert len(emoji.EMOJI_UNICODE) < len(emoji.EMOJI_ALIAS_UNICODE_ENGLISH)


def test_consistency_across_languages():
    # Check language packs versus the 'en' pack
    reference_code = 'en'
    for lang_code, emoji_pack in emoji.EMOJI_UNICODE.items():
        if lang_code == reference_code:
            continue
        ref_set = set(emoji.EMOJI_UNICODE[reference_code].values())
        for name, emj in emoji_pack.items():
            if emj not in ref_set:
                if emj in emoji_pack.values() and emj in emoji.EMOJI_UNICODE[reference_code].values():
                    print("%r is duplicated in %r:" % (name, lang_code))
                    for n, e in emoji_pack.items():
                        if e == emj:
                            print("    %r -> %r" % (n, e))
                elif emj in emoji_pack.values():
                    print("%r is supplementary in %r and does not appear in %r:" % (name, lang_code, reference_code))
                    for n, e in emoji_pack.items():
                        if e == emj:
                            print("    %r -> %r" % (n, e))
                else:
                    print("%r from %r is not in %r" % (name, lang_code, reference_code))
                    got = emoji.emojize(name, language=lang_code)
                    print("Appears in %r as: %s -> %r -> %r" % (lang_code, got.encode("unicode-escape").decode("utf-8"), got, name))
                    ref_name = emoji.demojize(emoji.emojize(name, language=lang_code))
                    expected = emoji.emojize(ref_name)
                    print("Appears in %r as: %s -> %r -> %r" % (reference_code, expected.encode("unicode-escape").decode("utf-8"), expected, ref_name))

            assert emj in ref_set
            ref_set.remove(emj)

        if len(ref_set) > 0:
            print("The following emoji from %r do not appear in %r" % (reference_code, lang_code))
            print("\n".join([e.encode("unicode-escape").decode("utf-8") for e in ref_set]))
