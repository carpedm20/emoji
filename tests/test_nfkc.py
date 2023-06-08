"""Unittests for canonically equivalent Unicode sequences"""

import sys
import emoji
import unicodedata


def is_normalized(form, s):
    if sys.version_info >= (3, 8):
        return unicodedata.is_normalized(form, s)
    else:
        return unicodedata.normalize(form, s) == s


def test_database_normalized():
    # Test if all names in EMOJI_DATA are in NFKC form
    for e, emoji_data in emoji.EMOJI_DATA.items():
        if 'alias' in emoji_data:
            for alias in emoji_data['alias']:
                assert is_normalized('NFKC', alias), 'Alias %r of %r is not NFKC' % (alias, e)
        for lang in emoji.LANGUAGES:
            if lang in emoji_data:
                name = emoji_data[lang]
                assert is_normalized('NFKC', name), 'Name lang=%s of %r is not NFKC' % (lang, e)


def test_normalized_and_not_normalized():
    pairs = [
        ['en', ':Cura\xe7ao:',  ':Curac\u0327ao:'],
        ['en', ':Co\u0302te_d\u2019Ivoire:', ':Co\u0302te_d\u2019Ivoire:'],
        ['alias', ':flag_for_\xc5land_Islands:', ':flag_for_A\u030aland_Islands:'],
        ['de', ':flagge_d\xe4nemark:', ':flagge_da\u0308nemark:'],
        ['fr', ':drapeau_r\xe9publique_dominicaine:', ':drapeau_re\u0301publique_dominicaine:'],
        ['fr', ':fl\xe8che_fin:', ':fle\u0300che_fin:'],
        ['es', ':bandera_etiop\xeda:', ':bandera_etiopi\u0301a:'],
        ['pt', ':bot\xe3o_free:', ':bota\u0303o_free:'],
        ['de', ':alter_schl\xfcssel:', ':alter_schlu\u0308ssel:'],
        ['fr', ':homme_\xe2g\xe9_peau_l\xe9g\xe8rement_mate:', ':homme_a\u0302ge\u0301_peau_le\u0301ge\u0300rement_mate:'],
        ['pt', ':cora\xe7\xe3o_vermelho:', ':corac\u0327a\u0303o_vermelho:'],
        ['en', ':Cayman_Islands:', ':Cayman_\u2160slands:'],
        ['fr', ':c\u0153ur_rouge:', ':c\ua7f9ur_rouge:'],
    ]

    for language, normalized, other_form in pairs:
        emoji_from_normalized = emoji.emojize(normalized, language=language)
        emoji_from_other_form = emoji.emojize(other_form, language=language)
        assert emoji_from_normalized == emoji_from_other_form
        assert not emoji_from_normalized.startswith(":")
