"""
Update the translation of the emoji names in the emoji.json file.
The translation is based on the Unicode CLDR annotations and the emojiterra.com website.
The output files are emoji_{xy}.json where {xy} is the letter language code
"""

import sys
import os
from pathlib import Path
from typing import Dict, Optional, Set
import re
import io
import xml.etree.ElementTree as ET
import logging
import json

import bs4

from generateutils import get_text_from_url, adapt_emoji_name, to_ascii

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

include = os.path.relpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, include)
import emoji as emoji_pkg  # noqa: E402

emoji_pkg.config.load_language()  # Make all languages available in EMOJI_DATA



def get_emojiterra_from_url(url: str) -> Dict[str, str]:
    html = get_text_from_url(url)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    emojis: Dict[str, str] = {}

    data = soup.find_all('li')

    data = [
        i
        for i in data
        if 'href' not in i.attrs and 'data-e' in i.attrs and i['data-e'].strip()
    ]

    for i in data:
        code = i['data-e']
        emojis[code] = i['title'].strip()

    assert len(data) > 100, f'emojiterra data from {url} has only {len(data)} entries'

    return emojis


def get_UNICODE_EMOJI(lang: str) -> Dict[str, str]:
    return {
        emj: emoji_pkg.EMOJI_DATA[emj][lang]
        for emj in emoji_pkg.EMOJI_DATA
        if lang in emoji_pkg.EMOJI_DATA[emj]
    }


def add_unicode_annotations(data: Dict[str, str], lang: str, url: str):
    xml = get_text_from_url(url)

    tree = ET.fromstring(xml)
    annotations = tree.find('annotations')
    assert annotations is not None, f'No annotations found in {url}'
    for annotation in annotations:
        if annotation.get('type') == 'tts':
            emj = annotation.get('cp')
            assert annotation.text is not None, "Empty annotation text"
            text = annotation.text.strip()
            assert emj is not None, f'No code point found in {url} for {annotation}'
            assert text is not None, f'No text found in {url} for {annotation}'

            emoji_name = adapt_emoji_name(text, lang, emj)

            if emj in data and data[emj] != emoji_name:
                if '\U0000200d\U000027a1' in emj:
                    # TODO Skip right-facing emoji (i.e. 🧑🏻‍🦽 vs 🧑🏻‍🦽‍➡️) for now because they are not correctly translated yet
                    # TODO They are currently missing the skin-colour information in the translations.
                    print(
                        f'# {lang}: {emj} SKIPPED CHANGE FROM {data[emj]} TO {emoji_name} \t\t(Source: {text})'
                    )
                    continue
                print(
                    f'# {lang}: {emj} CHANGED {data[emj]} TO {emoji_name} \t\t(Source: {text})'
                )

            data[emj] = emoji_name


def extract_names(
    github_tag: str,
    github_lang: str,
    lang: str,
    emoji_terra: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    """Copies emoji.EMOJI_DATA[emj][lang] and adds the names from the Unicode CLDR xml

    Find latest tag at https://cldr.unicode.org/index/downloads or
    https://github.com/unicode-org/cldr/tree/main/common/annotations
    """

    emoji_terra = {} if emoji_terra is None else emoji_terra

    data = get_UNICODE_EMOJI(lang)
    add_unicode_annotations(
        data,
        lang,
        f'https://github.com/unicode-org/cldr/raw/{github_tag}/common/annotations/{github_lang}.xml',
    )
    add_unicode_annotations(
        data,
        lang,
        f'https://github.com/unicode-org/cldr/raw/{github_tag}/common/annotationsDerived/{github_lang}.xml',
    )

    # Add names from emojiterra if there is no unicode annotation
    for emj, name in emoji_terra.items():
        if emj in emoji_pkg.EMOJI_DATA and emj not in data:
            emoji_name = adapt_emoji_name(name, lang, emj)
            data[emj] = emoji_name

    # There are some emoji with two code sequences for the same emoji, one that ends with \uFE0F and one that does not.
    # The one that ends with \uFE0F is the "new" emoji, that is RGI.
    # The Unicode translation data sometimes only has one of the two code sequences and is missing the other one.
    # In that case we want to use the existing translation for both code sequences.
    missing_translation: Dict[str, str] = {}
    for emj in data:
        if (
            emj.endswith('\ufe0f')
            and emj[0:-1] not in data
            and emj[0:-1] in emoji_pkg.EMOJI_DATA
        ):
            # the emoji NOT ending in \uFE0F exists in EMOJI_DATA but is has no translation
            # e.g. ':pirate_flag:' -> '\U0001F3F4\u200D\u2620\uFE0F' or '\U0001F3F4\u200D\u2620'
            missing_translation[emj[0:-1]] = data[emj]

        with_emoji_type = f'{emj}\ufe0f'
        if (
            not emj.endswith('\ufe0f')
            and with_emoji_type not in data
            and with_emoji_type in emoji_pkg.EMOJI_DATA
        ):
            # the emoji ending in \uFE0F exists in EMOJI_DATA but is has no translation
            # e.g. ':face_in_clouds:' -> '\U0001F636\u200D\U0001F32B\uFE0F' or '\U0001F636\u200D\U0001F32B'
            missing_translation[with_emoji_type] = data[emj]

    # Find emoji that contain \uFE0F inside the sequence (not just as a suffix)
    # e.g. ':eye_in_speech_bubble:' -> '\U0001F441\uFE0F\u200D\U0001F5E8\uFE0F'
    for emj in emoji_pkg.EMOJI_DATA:
        if emj in data:
            continue
        emj_no_variant = emj.replace('\ufe0f', '')
        if emj_no_variant != emj and emj_no_variant in data:
            # the emoji with \uFE0F has no translation, but the emoji without all \uFE0F has a translation
            data[emj] = data[emj_no_variant]

    data.update(missing_translation)

    return data



if __name__ == '__main__':
    logging.warning('Please run generate_emoji.py before this script to update the list of emojis (emoji.json file).')

    logging.info('  Downloading...\n')

    emojis = emoji_pkg.EMOJI_DATA

    # Find latest release tag at https://cldr.unicode.org/index/downloads
    # or  https://github.com/unicode-org/cldr/releases
    github_tag = 'release-46-beta2'
    languages = {
        # Update names in other languages:
        'de': extract_names(github_tag, 'de', 'de', get_emojiterra_from_url('https://emojiterra.com/de/tastatur/')),
        'es': extract_names(github_tag, 'es', 'es', get_emojiterra_from_url('https://emojiterra.com/es/teclado/')),
        'fr': extract_names(github_tag, 'fr', 'fr', get_emojiterra_from_url('https://emojiterra.com/fr/clavier/')),
        'ja': extract_names(github_tag, 'ja', 'ja', get_emojiterra_from_url('https://emojiterra.com/keyboard/ja/')),
        'ko': extract_names(github_tag, 'ko', 'ko', get_emojiterra_from_url('https://emojiterra.com/keyboard/ko/')),
        'pt': extract_names(github_tag, 'pt', 'pt', get_emojiterra_from_url('https://emojiterra.com/pt/copiar/')),
        'it': extract_names(github_tag, 'it', 'it', get_emojiterra_from_url('https://emojiterra.com/it/tastiera/')),
        'fa': extract_names(github_tag, 'fa', 'fa', get_emojiterra_from_url('https://emojiterra.com/keyboard/fa/')),
        'id': extract_names(github_tag, 'id', 'id', get_emojiterra_from_url('https://emojiterra.com/keyboard/id/')),
        'zh': extract_names(github_tag, 'zh', 'zh', get_emojiterra_from_url('https://emojiterra.com/keyboard/zh/')),
        'ru': extract_names(github_tag, 'ru', 'ru', get_emojiterra_from_url('https://emojiterra.com/keyboard/ru/')),
        'tr': extract_names(github_tag, 'tr', 'tr', get_emojiterra_from_url('https://emojiterra.com/keyboard/tr/')),
        'ar': extract_names(github_tag, 'ar', 'ar', get_emojiterra_from_url('https://emojiterra.com/keyboard/ar/')),

        # Do not update names in other languages:
        # 'de': get_UNICODE_EMOJI('de'),
        # 'es': get_UNICODE_EMOJI('es'),
        # 'fr': get_UNICODE_EMOJI('fr'),
        # 'ja': get_UNICODE_EMOJI('ja'),
        # 'ko': get_UNICODE_EMOJI('ko'),
        # 'pt': get_UNICODE_EMOJI('pt'),
        # 'it': get_UNICODE_EMOJI('it'),
        # 'fa': get_UNICODE_EMOJI('fa'),
        # 'id': get_UNICODE_EMOJI('id'),
        # 'zh': get_UNICODE_EMOJI('zh'),
        # 'ru': get_UNICODE_EMOJI('ru'),
        # 'tr': get_UNICODE_EMOJI('tr'),
        # 'ar': get_UNICODE_EMOJI('ar'),
    }

    logging.info('  Combining...\n')

    used_github_aliases: Set[str] = set()

    all_existing_aliases_and_en = set(
        item
        for emj_data in emoji_pkg.EMOJI_DATA.values()
        for item in emj_data.get('alias', [])
    )
    all_existing_aliases_and_en.update(
        emj_data['en'] for emj_data in emoji_pkg.EMOJI_DATA.values()
    )

    f = 0
    c = 0
    new_aliases = []
    logging.info('  Writing into files:\n')

    fps: Dict[str, io.BufferedWriter] = {}
    for lang in languages:
        out_file = (
            Path(emoji_pkg.__file__)
            .parent.joinpath(f'unicode_codes/emoji_{lang}.json')
            .resolve()
        )
        logging.info(f'   *  {out_file}')
        fps[lang] = open(out_file, mode='wb')
        fps[lang].write('{\n'.encode('utf-8'))

    for emj, v in sorted(emojis.items(), key=lambda item: item[1]['en']):
        code = to_ascii(emj)
        alternative = re.sub(r'\\U0000FE0[EF]$', '', code)
        emj_no_variant = alternative.encode().decode('unicode-escape')

        translation = None
        for lang in languages:
            if emj in languages[lang]:
                translation = languages[lang][emj]
            elif 'variant' in v:
                # the language annotation uses the normal emoji (no variant), while the emoji-test.txt uses the emoji or text variant
                if emj_no_variant in languages[lang]:
                    translation = languages[lang][emj_no_variant]

            if not translation:
                continue

            # Format the emoji code for the JSON
            # Only escape unicode points \ufe0f and \u200d so that similarly displayed emoji can be visually differentiated
            pretty_code = emj.replace('\ufe0f', '\\ufe0f').replace('\u200d', '\\u200d')

            # Print the data as JSON
            entry = f'"{pretty_code}": "{translation}",'
            # print(entry, end='\n',)
            fps[lang].write(f'{entry}\n'.encode('utf-8'))

    for lang in languages:
        fps[lang].seek(-2, os.SEEK_CUR)
        fps[lang].write('\n}\n'.encode('utf-8'))
        fps[lang].close()

    logging.info('\n\n  Checking json files. Any errors should appear below:\n')
    for lang in languages:
        out_file = (
            Path(emoji_pkg.__file__)
            .parent.joinpath(f'unicode_codes/emoji_{lang}.json')
            .resolve()
        )
        logging.info(f'   *  {out_file}')

        with open(out_file, 'rt', encoding='utf-8') as fp:
            json.load(fp)
        with open(out_file, 'rb') as fp:
            json.load(fp)
