# -*- coding: UTF-8 -*-


"""Unittests for emoji.core"""

import sys
import emoji
import unicodedata

def is_normalized(form, s):
    if sys.version_info >= (3, 8):
        return unicodedata.is_normalized(form, s)
    elif sys.version_info > (2, 0):
        return unicodedata.normalize(form, s) == s
    else:
        u = unicode(s)
        return unicodedata.normalize(form, u) == u


def test_database_normalized():
    if sys.version_info < (3, 8):
        return

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
        ['en', u':Cura\xe7ao:',  u':Curac\u0327ao:'],
        ['en', u':Co\u0302te_d\u2019Ivoire:', u':Co\u0302te_d\u2019Ivoire:'],
        ['alias', u':flag_for_\xc5land_Islands:', u':flag_for_A\u030aland_Islands:'],
        ['de', u':flagge_d\xe4nemark:', u':flagge_da\u0308nemark:'],
        ['fr', u':drapeau_r\xe9publique_dominicaine:', u':drapeau_re\u0301publique_dominicaine:'],
        ['fr', u':fl\xe8che_fin:', u':fle\u0300che_fin:'],
        ['es', u':bandera_etiop\xeda:', u':bandera_etiopi\u0301a:'],
        ['pt', u':bot\xe3o_free:', u':bota\u0303o_free:'],
        ['de', u':alter_schl\xfcssel:', u':alter_schlu\u0308ssel:'],
        ['fr', u':homme_\xe2g\xe9_peau_l\xe9g\xe8rement_mate:', u':homme_a\u0302ge\u0301_peau_le\u0301ge\u0300rement_mate:'],
        ['pt', u':cora\xe7\xe3o_vermelho:',u':corac\u0327a\u0303o_vermelho:'],
        ['en', u':Cayman_Islands:', u':Cayman_\u2160slands:'],
    ]

    if sys.version_info[0] > 2:
        pairs.append(['fr', u':c\u0153ur_rouge:', u':c\ua7f9ur_rouge:'])

    for language, normalized, other_form in pairs:
        emoji_from_normalized = emoji.emojize(normalized, language=language)
        emoji_from_other_form = emoji.emojize(other_form, language=language)
        assert emoji_from_normalized == emoji_from_other_form
        assert not emoji_from_normalized.startswith(":")
