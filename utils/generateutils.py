import re
from typing import Optional
import unicodedata

import requests


__scraper: Optional[requests.Session] = None


def to_ascii(s: str) -> str:
    """return escaped Code points \U000ab123"""
    return s.encode('unicode-escape').decode()


def get_text_from_url(url: str) -> str:
    """Get text from url"""

    html = ''
    if __scraper is None:
        html = requests.get(url).text
    if __scraper is not None or 'you have been blocked' in html.lower():
        html = get_text_from_cloudflare_url(url)

    return html


def get_text_from_cloudflare_url(url: str) -> str:
    """Get text from url that is protected by cloudflare"""
    global __scraper
    if __scraper is None:
        import cloudscraper  # type: ignore

        __scraper = cloudscraper.create_scraper()  # type: ignore
    return __scraper.get(url).text


def adapt_emoji_name(text: str, lang: str, emj: str) -> str:
    # Use NFKC-form (single character instead of character + diacritic)
    # Unicode.org files should be formatted like this anyway, but emojiterra is not consistent
    text = unicodedata.normalize('NFKC', text)

    # Fix German clock times "12:30 Uhr" -> "12.30 Uhr"
    text = re.sub(r'(\d+):(\d+)', r'\1.\2', text)
    text = text.replace('Ziffernblatt ', '')

    # Remove white space
    text = '_'.join(text.split(' '))

    emoji_name = (
        ':'
        + (
            text.lower()
            .removeprefix('flag:_')
            .replace(':', '')
            .replace(',', '')
            .replace('"', '')
            .replace('\u201e', '')
            .replace('\u201f', '')
            .replace('\u202f', '')
            .replace('\u229b', '')
            .replace('\u2013', '-')
            .replace(',_', ',')
            .strip()
            .replace(' ', '_')
            .replace('_-_', '-')
        )
        + ':'
    )

    if lang == 'de':
        emoji_name = emoji_name.replace('\u201c', '').replace('\u201d', '')
        emoji_name = re.sub(r'(hautfarbe)_und_([a-z]+_hautfarbe)', r'\1,\2', emoji_name)

    if lang == 'fa':
        emoji_name = emoji_name.replace('\u200c', '_')
        emoji_name = emoji_name.replace('\u200f', '_')
        emoji_name = emoji_name.replace('\u060c', '_')
        emoji_name = re.sub('_+', '_', emoji_name)

    if lang == 'tr':
        emoji_name = emoji_name.replace('\u0307', '')

    if lang == 'ro':
        emoji_name = ':' + fix_romanian_name(emoji_name[1:-1]) + ':'

    if lang == 'ar':
        # Removal of Arabic comma
        emoji_name = emoji_name.replace('\u060c', '')
        # Removal of supplementary Arabic diacritics "tashkīl"
        diacritics = '[\u0651\u0652\u064c\u064b\u064d\u0640\ufc62]'
        emoji_name = re.sub(diacritics, '', emoji_name)
        # Renaming duplicates
        duplicates = {
            '\U0001f9db\U0001f3ff': ':مصاص_دماء_رجل_بشرة_بلون_غامق:',  # 🧛🏿‍♂️
            '\U0001f9db\U0001f3fb': ':مصاص_دماء_رجل_بشرة_بلون_فاتح:',  # 🧛🏻
            '\U0001f9db\U0001f3fe': ':مصاص_دماء_رجل_بشرة_بلون_معتدل_مائل_للغامق:',  # 🧛🏾
            '\U0001f9db\U0001f3fc': ':مصاص_دماء_رجل_بشرة_بلون_فاتح_ومعتدل:',  # 🧛🏼
            '\U0001f9db\U0001f3fd': ':مصاص_دماء_رجل_بشرة_بلون_معتدل:',  # 🧛🏽
            '\U0001f9db\U0000200d\U00002642\U0000fe0f': ':مصاص_دماء_رجل:',  # 🧛‍♂️
            '\U0001f9a2': ':إوَزة:',  # 🦢
        }

        for e in duplicates:
            if e == emj:
                emoji_name = duplicates[emj]

    if lang == 'zh':
        emoji_name = (
            ':'
            + (
                text.replace(':', '')
                .replace(',', '')
                .replace('-', '')
                .replace('\u201e', '')
                .replace('\u201f', '')
                .replace('\u202f', '')
                .replace('\u229b', '')
                .replace(',_', ',')
                .strip()
                .replace(' ', '_')
            )
            + ':'
        )

        if '日文' in emoji_name:
            # Japanese buttons
            emoji_name = (
                emoji_name.replace('日文的', '')
                .replace('按钮', '')
                .replace('“', '')
                .replace('”', '')
            )

        if '箭头' in emoji_name:
            # Arrows
            emoji_name = emoji_name.replace('_', '').replace('!', '')

        if '按钮' in emoji_name:
            # English buttons
            emoji_name = emoji_name.replace('_', '')

        if '型血' in emoji_name:
            emoji_name = emoji_name.replace('_', '')

        if '中等-' in emoji_name:
            emoji_name = emoji_name.replace('中等-', '中等')

        if emoji_name.startswith(':旗_'):
            # Countries
            emoji_name = emoji_name.replace(':旗_', ':')

        hardcoded = {
            '\U0001f1ed\U0001f1f0': ':香港:',  # 🇭🇰
            '\U0001f1ee\U0001f1e9': ':印度尼西亞:',  # 🇮🇩
            '\U0001f1f0\U0001f1ff': ':哈薩克:',  # 🇰🇿
            '\U0001f1f2\U0001f1f4': ':澳門:',  # 🇲🇴
            '\U0001f1e8\U0001f1ec': ':刚果_布:',  # 🇨🇬
            '\U0001f1e8\U0001f1e9': ':刚果_金:',  # 🇨🇩
            '\U0001f193': ':FREE按钮:',  # 🆓
            '\U0001f238': ':申:',  # 🈸
            '\U0001f250': ':得:',  # 🉐
            '\U0001f22f': ':指:',  # 🈯
            '\U0001f232': ':禁:',  # 🈲
            '\u3297\ufe0f': ':祝:',  # ㊗️
            '\u3297': ':祝:',  # ㊗
            '\U0001f239': ':割:',  # 🈹
            '\U0001f21a': ':无:',  # 🈚
            '\U0001f237\ufe0f': ':月:',  # 🈷️
            '\U0001f237': ':月:',  # 🈷
            '\U0001f235': ':满:',  # 🈵
            '\U0001f236': ':有:',  # 🈶
            '\U0001f234': ':合:',  # 🈴
            '\u3299\ufe0f': ':秘:',  # ㊙️
            '\u3299': ':秘:',  # ㊙
            '\U0001f233': ':空:',  # 🈳
            '\U0001f251': ':可:',  # 🉑
            '\U0001f23a': ':营:',  # 🈺
            '\U0001f202\ufe0f': ':服务:',  # 🈂️
            '\U0001f202': ':服务:',  # 🈂
        }

        if emj in hardcoded:
            emoji_name = hardcoded[emj]

    if lang == 'ru':
        emoji_name = (
            ':'
            + (
                text.replace(':', '')
                .replace(',', '')
                .replace('-', ' ')
                .replace('—', '')
                .replace(',_', ',')
                .strip()
                .replace(' ', '_')
            )
            + ':'
        )

    emoji_name = (
        emoji_name.replace('____', '_')
        .replace('___', '_')
        .replace('__', '_')
        .replace('--', '-')
    )

    return emoji_name


# Corrections for the Romanian CLDR annotations, also applied to the skin tone variants
_RO_NAME_FIXES = {
    'sfor': 'sforăit',  # ZZZ
    'buton_0_(grupă_sanguină)': 'buton_o_(grupă_sanguină)',  # was the digit zero
    'crăciun': 'moș_sau_doamna_crăciun',  # Mx Claus
    'veveriță': 'burunduc',  # chipmunk
    'față_îmbufnată': 'față_înfuriată',  # enraged face
    'eventai_pliabil': 'evantai_pliabil',
    'șarlotă': 'cremă_de_zahăr_ars',  # custard
    'ciocan_și_daltă': 'ciocan_și_târnăcop',  # hammer and pick
    'alternare_cântăreț': 'semn_de_alternare_a_părților',
    'bărbat_cu_bonetă_chinezească': 'persoană_cu_tichie',  # person with skullcap
    'chifteluțe_de_orez': 'bilă_de_orez',
    'tricou_de_alegare': 'tricou_de_alergare',
    'pisică_surprinsă': 'pisică_extenuată',  # weary cat
    'bărbat_care_jongleză': 'bărbat_care_jonglează',
}


def fix_romanian_name(name: str) -> str:
    """Fix the Romanian emoji name (without the colons)"""

    name = name.replace('\u2010', '-')
    name = name.replace('\u201d', '')

    for wrong, right in _RO_NAME_FIXES.items():
        name = re.sub(f'^{re.escape(wrong)}(?=_ton_|$)', right, name)

    name = name.replace('_orientate_spre_dreapta', '_cu_fața_spre_dreapta')

    return name
