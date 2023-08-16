"""
Extract the full list of emoji and names from the Unicode emoji data files
https://unicode.org/Public/emoji/{v}/emoji-test.txt and
https://www.unicode.org/Public/{v}/ucd/emoji/emoji-variation-sequences.txt
and apply as much formatting as possible so the codes can be dropped into the
emoji registry file.
"""

import sys
import os
import unicodedata
import re
import requests
import bs4
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, include)
import emoji as emoji_pkg


def get_text_from_url(url: str) -> str:
    """Get text from url"""

    return requests.get(url).text


def get_emoji_from_url(version: float) -> list:
    """Get splitlines of emojis list from unicode.org"""

    url = f"https://unicode.org/Public/emoji/{version}/emoji-test.txt"
    return get_text_from_url(url).splitlines()


def get_emoji_variation_sequence_from_url(version: str) -> list:
    """Get splitlines of emoji variation sequences from unicode.org"""

    url = f"https://www.unicode.org/Public/{version}/ucd/emoji/emoji-variation-sequences.txt"
    return get_text_from_url(url).splitlines()


def get_emojiterra_from_url(url: str) -> dict:
    html = get_text_from_url(url)

    soup = bs4.BeautifulSoup(html, "html.parser")
    emojis = {}

    data = soup.find_all('li')
    data = [i for i in data if 'href' not in i.attrs and 'data-e' in i.attrs and i['data-e'].strip()]

    for i in data:
        code = i['data-e']
        emojis[code] = i['title'].strip()

    assert len(data) > 100, f"emojiterra data from {url} has only {len(data)} entries"

    return emojis


def get_cheat_sheet(url: str) -> dict:
    """
    Returns a dict of emoji to short-names:
    E.g. {'👴': ':old_man:', '👵': ':old_woman:', ... }
    """

    html = get_text_from_url(url)

    soup = bs4.BeautifulSoup(html, "html.parser")
    emojis = {}

    items = soup.find(class_='ecs-list').find_all(class_='_item')

    pattern = re.compile(r'U\+([0-9A-F]+)')

    for i in items:
        unicode_text = i.find(class_='unicode').text

        code_points = pattern.findall(unicode_text)
        code = ''.join(chr(int(x,16)) for x in code_points)

        emojis[code] = i.find(class_='shortcode').text

    # Remove some unwanted and some weird entries from the cheat sheet
    filtered = {}
    for emj, short_code in emojis.items():

        if short_code.startswith(':flag_'):
            # Skip flags from cheat-sheet, because we already have very similar aliases for the flags
            continue

        if '⊛' in short_code:
            # Strange emoji with ⊛ in the short-code
            continue

        if emj == '\U0001F93E\U0000200D\U00002640\U0000FE0F':
            # The short-code for this emoji is wrong
            continue

        if emj == '\U0001F468\U0000200D\U0001F468\U0000200D\U0001F467':
            # The short-code for this emoji is wrong
            continue

        if short_code.startswith('::'):
            # Do not allow short-codes to have double :: at the start
            short_code = short_code[1:]

        if short_code.endswith('::'):
            # Do not allow short-codes to have double :: at the end
            short_code = short_code[:-1]

        filtered[emj] = short_code

    assert len(filtered) > 100, f"emoji-cheat-sheet data from {url} has only {len(filtered)} entries"

    return filtered

def get_emoji_from_youtube(url: str) -> dict:
    """Get emoji alias from Youtube
    Returns a dict of emoji to list of short-names:
    E.g. {'💁': [':person_tipping_hand:', ':information_desk_person:'], '😉': [':winking_face:', ':wink:']}
    """

    data = requests.get(url).json()

    output = {}
    for obj in data:
        if 'shortcuts' not in obj or 'emojiId' not in obj:
            continue

        shortcuts = [x for x in obj['shortcuts'] if x.startswith(':') and x.endswith(':')]

        if shortcuts:
            output[obj['emojiId']] = shortcuts

    assert len(output) > 100, f"youtube data from {url} has only {len(output)} entries"

    return output



def extract_emojis(emojis_lines: list, sequences_lines: list) -> dict:
    """Extract emojis line by line to dict"""

    output = {}
    for line in emojis_lines:
        if not line == "" and not line.startswith("#"):
            emoji_status = line.split(";")[1].strip().split(" ")[0]

            codes = line.split(";")[0].strip().split(" ")
            separated_line = line.split(" # ")[-1].strip().split(" ")
            separated_name = separated_line[2:]
            version_str = separated_line[1]
            emoji_name = (
                "_".join(separated_name)
                .removeprefix("flag:_")
                .replace(":", "")
                .replace(",", "")
                .replace("\u201c", "")
                .replace("\u201d", "")
                .replace("\u229b", "")
                .strip()
                .replace(" ", "_")
                .replace("_-_", "-")
            )

            emoji_code = "".join(
                [
                    "\\U0000" + code if len(code) == 4 else "\\U000" + code
                    for code in codes
                ]
            )

            version = float(version_str.replace("E", "").strip())

            if emoji_code in output:
                raise Exception("Duplicate emoji: " +
                                emoji_name + " " + emoji_code)

            output[emoji_code] = {
                "en": emoji_name,
                "status": emoji_status.replace("-", "_"),
                "version": version
            }

    # Walk through the emoji-variation-sequences.txt
    for line in sequences_lines:
        if not line == "" and not line.startswith("#"):
            # No variant
            normal_codes = line.split(";")[0].strip().split(" ")
            normal_code = "".join(
                [
                    "\\U0000" + code if len(code) == 4 else "\\U000" + code
                    for code in normal_codes
                ]
            )
            if normal_code in output:
                output[normal_code]["variant"] = True

            # Text variant U+FE0E
            text_codes = re.sub(r'\s*FE0E\s*$', '',
                                line.split(";")[0]).strip().split(" ")
            text_code = "".join(
                [
                    "\\U0000" + code if len(code) == 4 else "\\U000" + code
                    for code in text_codes
                ]
            )
            if text_code in output:
                output[text_code]["variant"] = True

            # Emoji variant U+FE0F
            emoji_codes = re.sub(r'\s*FE0F\s*$', '', line.split(";")[0]).strip().split(" ")
            emoji_code = "".join(
                [
                    "\\U0000" + code if len(code) == 4 else "\\U000" + code
                    for code in emoji_codes
                ]
            )
            if emoji_code in output:
                output[emoji_code]["variant"] = True

    return output


def get_UNICODE_EMOJI(lang):
    return {emj: emoji_pkg.EMOJI_DATA[emj][lang] for emj in emoji_pkg.EMOJI_DATA if lang in emoji_pkg.EMOJI_DATA[emj]}


def adapt_emoji_name(text: str, lang: str, emj: str) -> str:
    # Use NFKC-form (single character instead of character + diacritic)
    # Unicode.org files should be formatted like this anyway, but emojiterra is not consistent
    text = unicodedata.normalize('NFKC', text)

    # Fix German clock times "12:30 Uhr" -> "12.30 Uhr"
    text = re.sub(r"(\d+):(\d+)", r"\1.\2", text)

    # Remove white space
    text = "_".join(text.split(" "))

    emoji_name = ":" + (
        text
        .lower()
        .removeprefix("flag:_")
        .replace(":", "")
        .replace(",", "")
        .replace('"', "")
        .replace("\u201e", "")
        .replace("\u201f", "")
        .replace("\u202f", "")
        .replace("\u229b", "")
        .replace("\u2013", "-")
        .replace(",_", ",")
        .strip()
        .replace(" ", "_")
        .replace("_-_", "-")
    ) + ":"

    if lang == "de":
        emoji_name = emoji_name.replace("\u201c", "").replace("\u201d", "")
        emoji_name = re.sub(r"(hautfarbe)_und_([a-z]+_hautfarbe)", r"\1,\2", emoji_name)

    if lang == "fa":
        emoji_name = emoji_name.replace('\u200c', "_")
        emoji_name = emoji_name.replace('\u200f', "_")
        emoji_name = emoji_name.replace('\u060c', "_")
        emoji_name = re.sub("_+", "_", emoji_name)

    if lang == "zh":
        emoji_name = ":" + (
            text
            .replace(":", "")
            .replace(",", "")
            .replace('-', "")
            .replace("\u201e", "")
            .replace("\u201f", "")
            .replace("\u202f", "")
            .replace("\u229b", "")
            .replace(",_", ",")
            .strip()
            .replace(" ", "_")
        ) + ":"

        if '日文' in emoji_name:
            # Japanese buttons
            emoji_name = emoji_name.replace('日文的', '').replace('按钮', '').replace('“', '').replace('”', '')

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
            '\U0001F23A': ':营:',  # 🈺
            '\U0001F202\ufe0f': ':服务:',  # 🈂️
            '\U0001F202': ':服务:',  # 🈂
        }

        if emj in hardcoded:
            emoji_name = hardcoded[emj]

    emoji_name = (emoji_name
        .replace("____", "_")
        .replace("___", "_")
        .replace("__", "_")
        .replace("--", "-"))

    return emoji_name


def add_unicode_annotations(data, lang, url):
    xml = get_text_from_url(url)

    tree = ET.fromstring(xml)
    annotations = tree.find('annotations')
    for annotation in annotations:
        if annotation.get('type') == 'tts':
            emj = annotation.get('cp')
            text = annotation.text.strip()

            emoji_name = adapt_emoji_name(text, lang, emj)

            if emj in data and data[emj] != emoji_name:
                print(
                    f"# {lang}: CHANGED {data[emj]} TO {emoji_name} \t\t(Original: {text})")
            data[emj] = emoji_name


def extract_names(github_tag, github_lang, lang, emoji_terra={}):
    """Copies emoji.EMOJI_DATA[emj][lang] and adds the names from the Unicode CLDR xml

    Find latest tag at https://cldr.unicode.org/index/downloads or
    https://github.com/unicode-org/cldr/tree/main/common/annotations
    """

    data = get_UNICODE_EMOJI(lang)
    add_unicode_annotations(data, lang, f"https://github.com/unicode-org/cldr/raw/{github_tag}/common/annotations/{github_lang}.xml")
    add_unicode_annotations(data, lang, f"https://github.com/unicode-org/cldr/raw/{github_tag}/common/annotationsDerived/{github_lang}.xml")

    # Add names from emojiterra if there is no unicode annotation
    for emj, name in emoji_terra.items():
        if emj in emoji_pkg.EMOJI_DATA and emj not in data:
            emoji_name = adapt_emoji_name(name, lang, emj)
            data[emj] = emoji_name

    # There are some emoji with two code sequences for the same emoji, one that ends with \uFE0F and one that does not.
    # The one that ends with \uFE0F is the "new" emoji, that is RGI.
    # The Unicode translation data sometimes only has one of the two code sequences and is missing the other one.
    # In that case we want to use the existing translation for both code sequences.
    missing_translation = {}
    for emj in data:
        if emj.endswith('\uFE0F') and emj[0:-1] not in data and emj[0:-1] in emoji_pkg.EMOJI_DATA:
            # the emoji NOT ending in \uFE0F exists in EMOJI_DATA but is has no translation
            # e.g. ':pirate_flag:' -> '\U0001F3F4\u200D\u2620\uFE0F' or '\U0001F3F4\u200D\u2620'
            missing_translation[emj[0:-1]] = data[emj]

        with_emoji_type = f"{emj}\uFE0F"
        if not emj.endswith('\uFE0F') and with_emoji_type not in data and with_emoji_type in emoji_pkg.EMOJI_DATA:
            # the emoji ending in \uFE0F exists in EMOJI_DATA but is has no translation
            # e.g. ':face_in_clouds:' -> '\U0001F636\u200D\U0001F32B\uFE0F' or '\U0001F636\u200D\U0001F32B'
            missing_translation[with_emoji_type] = data[emj]

    # Find emoji that contain \uFE0F inside the sequence (not just as a suffix)
    # e.g. ':eye_in_speech_bubble:' -> '\U0001F441\uFE0F\u200D\U0001F5E8\uFE0F'
    for emj in emoji_pkg.EMOJI_DATA:
        if emj in data:
            continue
        emj_no_variant = emj.replace('\uFE0F', '')
        if emj_no_variant != emj and emj_no_variant in data:
            # the emoji with \uFE0F has no translation, but the emoji without all \uFE0F has a translation
            data[emj] = data[emj_no_variant]

    data.update(missing_translation)

    return data


def get_emoji_from_github_api(url: str) -> dict:
    """Get emoji alias from GitHub API
    """

    data = requests.get(url).json()
    pattern = re.compile(r"unicode/([0-9a-fA-F-]+)\.[a-z]+")

    output = {}
    for name, img in data.items():
        m = pattern.search(img)
        if m:
            emj = "".join(chr(int(h, 16)) for h in m.group(1).split('-'))
            output[name] = emj
        else:
            pass  # Special GitHub emoji that is not part of Unicode

    assert len(output) > 100, f"data from github API has only {len(output)} entries"

    return output


GITHUB_REMOVED_CHARS = re.compile("\u200D|\uFE0F|\uFE0E", re.IGNORECASE)


def find_github_aliases(emj, github_dict, v, emj_no_variant=None):
    aliases = set()

    # Strip ZWJ \u200D, text_type \uFE0E and emoji_type \uFE0F
    # because the GitHub API does not include these
    emj_clean = GITHUB_REMOVED_CHARS.sub("", emj)

    for gh_alias in github_dict:
        if emj == github_dict[gh_alias]:
            aliases.add(gh_alias)
        elif 'variant' in v and emj_no_variant == github_dict[gh_alias]:
            aliases.add(gh_alias)
        elif emj_clean == github_dict[gh_alias]:
            aliases.add(gh_alias)

    return aliases


def ascii(s):
    # return escaped Code points \U000AB123
    return s.encode("unicode-escape").decode()


if __name__ == "__main__":
    logging.info('  Downloading...\n')

    # Find the latest version at https://www.unicode.org/reports/tr51/#emoji_data
    emoji_source = get_emoji_from_url(15.0)
    emoji_sequences_source = get_emoji_variation_sequence_from_url('15.0.0')
    emojis = extract_emojis(emoji_source, emoji_sequences_source)
    # Find latest release tag at https://cldr.unicode.org/index/downloads
    github_tag = 'release-43-1'

    languages = {
        # Update names in other languages:
        'de': extract_names(github_tag, 'de', 'de', get_emojiterra_from_url('https://emojiterra.com/de/kopieren/')),
        'es': extract_names(github_tag, 'es', 'es', get_emojiterra_from_url('https://emojiterra.com/es/copiar/')),
        'fr': extract_names(github_tag, 'fr', 'fr', get_emojiterra_from_url('https://emojiterra.com/fr/copier/')),
        'ja': extract_names(github_tag, 'ja', 'ja', get_emojiterra_from_url('https://emojiterra.com/copypaste/ja/')),
        'ko': extract_names(github_tag, 'ko', 'ko', get_emojiterra_from_url('https://emojiterra.com/copypaste/ko/')),
        'pt': extract_names(github_tag, 'pt', 'pt', get_emojiterra_from_url('https://emojiterra.com/pt/copiar/')),
        'it': extract_names(github_tag, 'it', 'it', get_emojiterra_from_url('https://emojiterra.com/it/copiare/')),
        'fa': extract_names(github_tag, 'fa', 'fa', get_emojiterra_from_url('https://emojiterra.com/copypaste/fa/')),
        'id': extract_names(github_tag, 'id', 'id', get_emojiterra_from_url('https://emojiterra.com/copypaste/id/')),
        'zh': extract_names(github_tag, 'zh', 'zh', get_emojiterra_from_url('https://emojiterra.com/copypaste/zh/')),

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
    }

    github_alias_dict = get_emoji_from_github_api('https://api.github.com/emojis')
    cheat_sheet_dict = get_cheat_sheet('https://www.webfx.com/tools/emoji-cheat-sheet/')
    youtube_dict = get_emoji_from_youtube('https://www.gstatic.com/youtube/img/emojis/emojis-png-7.json')

    logging.info('  Combining...\n')

    used_github_aliases = set()

    escapedToUnicodeMap = {escaped: escaped.encode().decode('unicode-escape') for escaped in emojis}  # maps: "\\U0001F4A4" to "\U0001F4A4"

    all_existing_aliases_and_en = set(item for emj_data in emoji_pkg.EMOJI_DATA.values() for item in emj_data.get('alias', []))
    all_existing_aliases_and_en.update(emj_data['en'] for emj_data in emoji_pkg.EMOJI_DATA.values())

    f = 0
    c = 0
    new_aliases = []
    logging.info('  Print EMOJI_DATA...\n')
    for code, v in sorted(emojis.items(), key=lambda item: item[1]["en"]):
        language_str = ''
        emj = escapedToUnicodeMap[code]

        alternative = re.sub(r"\\U0000FE0[EF]$", "", code)
        emj_no_variant = escapedToUnicodeMap[alternative]

        # add names in other languages
        for lang in languages:
            if emj in languages[lang]:
                language_str += ",\n        '%s': '%s'" % (
                    lang, languages[lang][emj])
            elif 'variant' in v:
                # the language annotation uses the normal emoji (no variant), while the emoji-test.txt uses the emoji or text variant
                if emj_no_variant in languages[lang]:
                    language_str += ",\n        '%s': '%s'" % (
                        lang, languages[lang][emj_no_variant])

        # Add existing alias from EMOJI_DATA
        aliases = set()
        if emj in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj]:
            aliases.update(a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias'])
        old_aliases = set(aliases)

        if emj_no_variant in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj_no_variant]:
            aliases.update(a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj_no_variant]['alias'])

        # Add alias from GitHub API
        github_aliases = find_github_aliases(emj, github_alias_dict, v, emj_no_variant)
        aliases.update(shortcut for shortcut in github_aliases if shortcut not in all_existing_aliases_and_en)
        used_github_aliases.update(github_aliases)

        # Add alias from cheat sheet
        if emj in cheat_sheet_dict and cheat_sheet_dict[emj] not in all_existing_aliases_and_en:
            aliases.add(cheat_sheet_dict[emj][1:-1])
        if emj_no_variant in cheat_sheet_dict and cheat_sheet_dict[emj_no_variant] not in all_existing_aliases_and_en:
            aliases.add(cheat_sheet_dict[emj_no_variant][1:-1])

        # Add alias from youtube
        if emj in youtube_dict:
            aliases.update(shortcut[1:-1] for shortcut in youtube_dict[emj] if shortcut not in all_existing_aliases_and_en)
        if emj_no_variant in youtube_dict:
            aliases.update(shortcut[1:-1] for shortcut in youtube_dict[emj_no_variant] if shortcut not in all_existing_aliases_and_en)

        # Remove if alias is same as 'en'-name
        if v["en"] in aliases:
            aliases.remove(v["en"])

        # Store new aliases to print them at the end after the dict of dicts
        if emj in emoji_pkg.EMOJI_DATA:
            if 'alias' in emoji_pkg.EMOJI_DATA[emj]:
                diff = aliases.difference(a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias'])
            else:
                diff = aliases
            for a in diff:
                new_aliases.append(f"# alias NEW {a} FOR {emj} CODE {code}")

        # Keep the order of existing aliases intact
        if emj in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj]:
            aliases = [a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias']] + [a for a in aliases if f":{a}:" not in emoji_pkg.EMOJI_DATA[emj]['alias']]

        if any("flag_for_" in a for a in aliases):
            # Put the :flag_for_COUNTRY: alias as the first entry so that it gets picked by demojize()
            # This ensures compatibility because in the past there was only the :flag_for_COUNTRY: alias
            aliases = [a for a in aliases if "flag_for_" in a] + [a for a in aliases if "flag_for_" not in a]

        # Print dict of dicts
        alias = ''
        if len(aliases) > 0:
            alias_list_str = ", ".join([f"':{a}:'" for a in aliases])
            alias = ",\n        'alias': [%s]" % (alias_list_str, )
        variant = ",\n        'variant': True" if 'variant' in v else ''
        print(f"""    '{code}': {{  # {emj}
        'en': ':{v['en']}:',
        'status': {v["status"]},
        'E': {v["version"]:g}{alias}{variant}{language_str}
    }}""", end=",\n")
        if v["status"] == "fully_qualified":
            f += 1
        elif v["status"] == "component":
            c += 1

    logging.debug(f" # Total count of emojis: {len(emojis)}")
    logging.debug(f" # fully_qualified: {f}")
    logging.debug(f" # component: {c}\n")
    logging.debug("\n".join(new_aliases))

    # Check if all aliases from GitHub API were used
    for github_alias in github_alias_dict:
        if github_alias not in used_github_aliases:
            logging.debug(f"# Unused Github alias: {github_alias} {github_alias_dict[github_alias]} {ascii(github_alias_dict[github_alias])}")

    logging.info('\n\n  Done.')