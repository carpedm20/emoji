"""
Extract the full list of emoji and names from the Unicode emoji data files
https://unicode.org/Public/emoji/{v}/emoji-test.txt and
https://www.unicode.org/Public/{v}/ucd/emoji/emoji-variation-sequences.txt
and the aliases from various sources.
and combine it with the existing emoji data from the emoji package.
"""

import sys
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
import re
import logging
import json

import requests
import bs4

from generateutils import get_text_from_url, to_ascii

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

include = os.path.relpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, include)
import emoji as emoji_pkg  # noqa: E402


def get_emoji_from_url(version: float) -> List[str]:
    """Get splitlines of emojis list from unicode.org"""

    url = f'https://unicode.org/Public/emoji/{version}/emoji-test.txt'
    return get_text_from_url(url).splitlines()


def get_emoji_variation_sequence_from_url(version: str) -> List[str]:
    """Get splitlines of emoji variation sequences from unicode.org"""

    url = f'https://www.unicode.org/Public/{version}/ucd/emoji/emoji-variation-sequences.txt'
    return get_text_from_url(url).splitlines()


def get_cheat_sheet(url: str) -> Dict[str, str]:
    """
    Returns a dict of emoji to short-names:
    E.g. {'👴': ':old_man:', '👵': ':old_woman:', ... }
    """

    html = get_text_from_url(url)

    soup = bs4.BeautifulSoup(html, 'html.parser')
    emojis: Dict[str, str] = {}

    ecs_list = soup.find(class_='ecs-list')
    assert isinstance(ecs_list, bs4.element.Tag), "Couldn't find the ecs-list class in the cheat-sheet"
    items = ecs_list.find_all(class_='_item')
    assert items, "Couldn't find any items in the cheat-sheet"

    pattern = re.compile(r'U\+([0-9A-F]+)')

    for i in items:
        unicode_text = i.find(class_='unicode').text

        code_points = pattern.findall(unicode_text)
        code = ''.join(chr(int(x, 16)) for x in code_points)

        emojis[code] = i.find(class_='shortcode').text

    # Remove some unwanted and some weird entries from the cheat sheet
    filtered: Dict[str, str] = {}
    for emj, short_code in emojis.items():
        if short_code.startswith(':flag_'):
            # Skip flags from cheat-sheet, because we already have very similar aliases for the flags
            continue

        if '⊛' in short_code:
            # Strange emoji with ⊛ in the short-code
            continue

        if emj == '\U0001f93e\U0000200d\U00002640\U0000fe0f':
            # The short-code for this emoji is wrong
            continue

        if emj == '\U0001f468\U0000200d\U0001f468\U0000200d\U0001f467':
            # The short-code for this emoji is wrong
            continue

        if short_code.startswith('::'):
            # Do not allow short-codes to have double :: at the start
            short_code = short_code[1:]

        if short_code.endswith('::'):
            # Do not allow short-codes to have double :: at the end
            short_code = short_code[:-1]

        filtered[emj] = short_code

    assert (
        len(filtered) > 100
    ), f'emoji-cheat-sheet data from {url} has only {len(filtered)} entries'

    return filtered


def get_emoji_from_youtube(url: str) -> Dict[str, List[str]]:
    """Get emoji alias from Youtube
    Returns a dict of emoji to list of short-names:
    E.g. {'💁': [':person_tipping_hand:', ':information_desk_person:'], '😉': [':winking_face:', ':wink:']}
    """

    data = requests.get(url).json()

    output: Dict[str, List[str]] = {}
    for obj in data:
        if 'shortcuts' not in obj or 'emojiId' not in obj:
            continue

        shortcuts = [
            x for x in obj['shortcuts'] if x.startswith(':') and x.endswith(':')
        ]

        if shortcuts:
            output[obj['emojiId']] = shortcuts

    assert len(output) > 100, f'youtube data from {url} has only {len(output)} entries'

    return output


def extract_emojis(
    emojis_lines: List[str], sequences_lines: List[str]
) -> Dict[str, Dict[str, Any]]:
    """Extract emojis line by line to dict"""

    output: Dict[str, Dict[str, Any]] = {}
    for line in emojis_lines:
        if not line == '' and not line.startswith('#'):
            emoji_status = line.split(';')[1].strip().split(' ')[0]

            codes = line.split(';')[0].strip().split(' ')
            separated_line = line.split(' # ')[-1].strip().split(' ')
            separated_name = separated_line[2:]
            version_str = separated_line[1]

            emoji_name: str = (
                '_'.join(separated_name)
                .removeprefix('flag:_')
                .replace(':', '')
                .replace(',', '')
                .replace('\u201c', '')
                .replace('\u201d', '')
                .replace('\u229b', '')
                .strip()
                .replace(' ', '_')
                .replace('_-_', '-')
            )

            assert isinstance(
                emoji_name, str
            ), f'emoji_name is not a string: {emoji_name}'

            emoji_code = ''.join(
                [
                    '\\U0000' + code if len(code) == 4 else '\\U000' + code
                    for code in codes
                ]
            )

            version = float(version_str.replace('E', '').strip())

            if emoji_code in output:
                raise Exception(f'Duplicate emoji: {emoji_name} {emoji_code}')

            output[emoji_code] = {
                'en': emoji_name,
                'status': emoji_status.replace('-', '_'),
                'version': version,
            }

    # Walk through the emoji-variation-sequences.txt
    for line in sequences_lines:
        if not line == '' and not line.startswith('#'):
            # No variant
            normal_codes = line.split(';')[0].strip().split(' ')
            normal_code = ''.join(
                [
                    '\\U0000' + code if len(code) == 4 else '\\U000' + code
                    for code in normal_codes
                ]
            )
            if normal_code in output:
                output[normal_code]['variant'] = True

            # Text variant U+FE0E
            text_codes = (
                re.sub(r'\s*FE0E\s*$', '', line.split(';')[0]).strip().split(' ')
            )
            text_code = ''.join(
                [
                    '\\U0000' + code if len(code) == 4 else '\\U000' + code
                    for code in text_codes
                ]
            )
            if text_code in output:
                output[text_code]['variant'] = True

            # Emoji variant U+FE0F
            emoji_codes = (
                re.sub(r'\s*FE0F\s*$', '', line.split(';')[0]).strip().split(' ')
            )
            emoji_code = ''.join(
                [
                    '\\U0000' + code if len(code) == 4 else '\\U000' + code
                    for code in emoji_codes
                ]
            )
            if emoji_code in output:
                output[emoji_code]['variant'] = True

    return output




def get_emoji_from_github_api(url: str) -> Dict[str, str]:
    """Get emoji alias from GitHub API"""

    data = requests.get(url).json()
    pattern = re.compile(r'unicode/([0-9a-fA-F-]+)\.[a-z]+')

    output: Dict[str, str] = {}
    for name, img in data.items():
        m = pattern.search(img)
        if m:
            emj = ''.join(chr(int(h, 16)) for h in m.group(1).split('-'))
            output[name] = emj
        else:
            pass  # Special GitHub emoji that is not part of Unicode

    assert len(output) > 100, f'data from github API has only {len(output)} entries'

    return output


GITHUB_REMOVED_CHARS = re.compile('\u200d|\ufe0f|\ufe0e', re.IGNORECASE)


def find_github_aliases(
    emj: str,
    github_dict: Dict[str, str],
    v: Dict[str, Any],
    emj_no_variant: Optional[str] = None,
) -> Set[str]:
    aliases: Set[str] = set()

    # Strip ZWJ \u200D, text_type \uFE0E and emoji_type \uFE0F
    # because the GitHub API does not include these
    emj_clean = GITHUB_REMOVED_CHARS.sub('', emj)

    for gh_alias in github_dict:
        if emj == github_dict[gh_alias]:
            aliases.add(gh_alias)
        elif 'variant' in v and emj_no_variant == github_dict[gh_alias]:
            aliases.add(gh_alias)
        elif emj_clean == github_dict[gh_alias]:
            aliases.add(gh_alias)

    return aliases



if __name__ == '__main__':
    out_file = (
        Path(emoji_pkg.__file__).parent.joinpath('unicode_codes/emoji.json').resolve()
    )
    logging.info(f'  Outfile: {out_file}')

    logging.info('  Downloading...\n')

    # Find the latest version at https://www.unicode.org/reports/tr51/#emoji_data
    emoji_source = get_emoji_from_url(16.0)
    emoji_sequences_source = get_emoji_variation_sequence_from_url('16.0.0')
    emojis = extract_emojis(emoji_source, emoji_sequences_source)

    github_alias_dict = get_emoji_from_github_api('https://api.github.com/emojis')
    cheat_sheet_dict = get_cheat_sheet('https://www.webfx.com/tools/emoji-cheat-sheet/')
    youtube_dict = get_emoji_from_youtube(
        'https://www.gstatic.com/youtube/img/emojis/emojis-png-7.json'
    )

    logging.info('  Combining...\n')

    used_github_aliases: Set[str] = set()

    escapedToUnicodeMap = {
        escaped: escaped.encode().decode('unicode-escape') for escaped in emojis
    }  # maps: "\\U0001F4A4" to "\U0001F4A4"

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
    new_aliases: List[str] = []
    logging.info(f'  Writing to {out_file}...\n')
    fp = open(out_file, mode='wt', encoding='utf-8', newline='\n')
    fp.write('{\n')
    total_items = len(emojis)
    for i, (code, v) in enumerate(
        sorted(emojis.items(), key=lambda item: item[1]['en'])
    ):
        emj = escapedToUnicodeMap[code]

        alternative = re.sub(r'\\U0000FE0[EF]$', '', code)
        emj_no_variant = escapedToUnicodeMap[alternative]

        # Add existing alias from EMOJI_DATA
        aliases: Set[str] = set()
        if emj in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj]:
            aliases.update(a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias'])
        old_aliases = set(aliases)

        if (
            emj_no_variant in emoji_pkg.EMOJI_DATA
            and 'alias' in emoji_pkg.EMOJI_DATA[emj_no_variant]
        ):
            aliases.update(
                a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj_no_variant]['alias']
            )

        # Add alias from GitHub API
        github_aliases = find_github_aliases(emj, github_alias_dict, v, emj_no_variant)
        aliases.update(
            shortcut
            for shortcut in github_aliases
            if shortcut not in all_existing_aliases_and_en
        )
        used_github_aliases.update(github_aliases)

        # Add alias from cheat sheet
        if (
            emj in cheat_sheet_dict
            and cheat_sheet_dict[emj] not in all_existing_aliases_and_en
        ):
            aliases.add(cheat_sheet_dict[emj][1:-1])
        if (
            emj_no_variant in cheat_sheet_dict
            and cheat_sheet_dict[emj_no_variant] not in all_existing_aliases_and_en
        ):
            aliases.add(cheat_sheet_dict[emj_no_variant][1:-1])

        # Add alias from youtube
        if emj in youtube_dict:
            aliases.update(
                shortcut[1:-1]
                for shortcut in youtube_dict[emj]
                if shortcut not in all_existing_aliases_and_en
            )
        if emj_no_variant in youtube_dict:
            aliases.update(
                shortcut[1:-1]
                for shortcut in youtube_dict[emj_no_variant]
                if shortcut not in all_existing_aliases_and_en
            )

        # Remove if alias is same as 'en'-name
        if v['en'] in aliases:
            aliases.remove(v['en'])

        # Store new aliases to print them at the end after the JSON
        if emj in emoji_pkg.EMOJI_DATA:
            if 'alias' in emoji_pkg.EMOJI_DATA[emj]:
                diff = aliases.difference(
                    a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias']
                )
            else:
                diff = aliases
            for a in diff:
                new_aliases.append(f'# alias NEW {a} FOR {emj} CODE {code}')

        aliases_list = list(aliases)

        # Keep the order of existing aliases intact
        if emj in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj]:
            aliases_list = [a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias']] + [
                a for a in aliases_list if f':{a}:' not in emoji_pkg.EMOJI_DATA[emj]['alias']
            ]

        if any('flag_for_' in a for a in aliases_list):
            # Put the :flag_for_COUNTRY: alias as the first entry so that it gets picked by demojize()
            # This ensures compatibility because in the past there was only the :flag_for_COUNTRY: alias
            aliases_list = [a for a in aliases_list if 'flag_for_' in a] + [
                a for a in aliases_list if 'flag_for_' not in a
            ]

        # Format the emoji code for the JSON
        # Only escape unicode points \ufe0f and \u200d so that similarly displayed emoji can be visually differentiated
        pretty_code = emj.replace('\ufe0f', '\\ufe0f').replace('\u200d', '\\u200d')

        # Write/Print the data as JSON
        alias = ''
        if len(aliases_list) > 0:
            alias_list_str = ', '.join([f'":{a}:"' for a in aliases_list])
            alias = ',\n  "alias": [%s]' % (alias_list_str,)
        variant = ',\n  "variant": true' if 'variant' in v else ''
        entry = f""""{pretty_code}": {{
  "en": ":{v["en"]}:",
  "status": {emoji_pkg.STATUS[v['status']]},
  "E": {v['version']:g}{alias}{variant}
}}"""
        # print(entry, end=',\n',)
        if i == total_items - 1:
            fp.write(f'{entry}\n}}\n')
        else:
            fp.write(f'{entry},\n')
        if v['status'] == 'fully_qualified':
            f += 1
        elif v['status'] == 'component':
            c += 1

    logging.debug(f' # Total count of emojis: {len(emojis)}')
    logging.debug(f' # fully_qualified: {f}')
    logging.debug(f' # component: {c}\n')
    logging.debug('\n'.join(new_aliases))

    # Check if all aliases from GitHub API were used
    for github_alias in github_alias_dict:
        if github_alias not in used_github_aliases:
            logging.debug(
                f'# Unused Github alias: {github_alias} {github_alias_dict[github_alias]} {to_ascii(github_alias_dict[github_alias])}'
            )

    logging.info('\n\n  Done.')

    fp.close()

    logging.info('\n\n  Checking json file. Any errors should appear below:\n')
    with open(out_file, 'rt', encoding='utf-8') as fp:
        json.load(fp)
    with open(out_file, 'rb') as fp:
        json.load(fp)
