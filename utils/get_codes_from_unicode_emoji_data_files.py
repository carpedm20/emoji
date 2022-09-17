# -*- coding: utf-8 -*-

"""
Extract the full list of emoji and names from the Unicode emoji data files
https://unicode.org/Public/emoji/{v}/emoji-test.txt and
https://www.unicode.org/Public/{v}/ucd/emoji/emoji-variation-sequences.txt
and apply as much formatting as possible so the codes can be dropped into the
emoji registry file.
"""

import sys
import os
import re
import requests
import xml.etree.ElementTree as ET

include = os.path.relpath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, include)
import emoji as emoji_pkg


def get_text_from_url(url: str) -> str:
    """Get text from url"""

    return requests.get(url).text


def get_language_data_from_url(tag: str, lang: str) -> str:
    """Get emoji language annotation xml
    Find latest tag at https://cldr.unicode.org/index/downloads """

    url = f"https://github.com/unicode-org/cldr/raw/{tag}/common/annotations/{lang}.xml"
    return get_text_from_url(url)


def get_emoji_from_url(version: float) -> list:
    """Get splitlines of emojis list from unicode.org"""

    url = f"https://unicode.org/Public/emoji/{version}/emoji-test.txt"
    return get_text_from_url(url).splitlines()


def get_emoji_variation_sequence_from_url(version: str) -> list:
    """Get splitlines of emoji variation sequences from unicode.org"""

    url = f"https://www.unicode.org/Public/{version}/ucd/emoji/emoji-variation-sequences.txt"
    return get_text_from_url(url).splitlines()


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


def extract_names(xml, lang):
    """Copies emoji.EMOJI_DATA[emj][lang] and adds the names from the xml"""

    data = get_UNICODE_EMOJI(lang)

    tree = ET.fromstring(xml)
    annotations = tree.find('annotations')
    for annotation in annotations:
        if annotation.get('type') == 'tts':
            emj = annotation.get('cp')
            text = annotation.text.strip()
            # Fix German clock times "12:30 Uhr" -> "12.30 Uhr"
            text_replaced_colon = re.sub(r"(\d+):(\d+)", r"\1.\2", text)
            separated_name = text_replaced_colon.split(" ")
            emoji_name = ":" + (
                "_".join(separated_name)
                .lower()
                .removeprefix("flag:_")
                .replace(":", "")
                .replace(",", "")
                .replace('"', "")
                .replace("\u201e", "")
                .replace("\u201f", "")
                .replace("\u229b", "")
                .strip()
                .replace(" ", "_")
            ) + ":"
            if lang == "de":
                emoji_name = emoji_name.replace("\u201c", "").replace("\u201d", "")

            if lang == "fa":
                emoji_name = emoji_name.replace('\u200c',"_")
                emoji_name = re.sub("_+","_",emoji_name)
            

            if emj in data and data[emj] != emoji_name:
                print(
                    f"# {lang}: CHANGED {data[emj]} TO {emoji_name} \t\t(Original: {text})")
            data[emj] = emoji_name
    return data


def get_emoji_from_github_api() -> dict:
    """Get emoji alias from GitHub API
    """

    data = requests.get("https://api.github.com/emojis").json()
    pattern = re.compile(r"unicode/([0-9a-fA-F-]+)\.[a-z]+")

    output = {}
    for name, img in data.items():
        m = pattern.search(img)
        if m:
            emj = "".join(chr(int(h, 16)) for h in m.group(1).split('-'))
            output[name] = emj
        else:
            pass  # Special GitHub emoji that is not part of Unicode

    return output

def ascii(s):
    # return escaped Code points \U000AB123
    return s.encode("unicode-escape").decode()

def u_string(s):
    # return "u'{s}'" if non-ascii else return "'{s}'"
    if ascii(s) == s:
        return f"'{s}'"
    return f"u'{s}'"

if __name__ == "__main__":
    # Find the latest version at https://www.unicode.org/reports/tr51/#emoji_data
    emoji_source = get_emoji_from_url(14.0)
    emoji_sequences_source = get_emoji_variation_sequence_from_url('14.0.0')
    emojis = extract_emojis(emoji_source, emoji_sequences_source)
    # Find latest release tag at https://cldr.unicode.org/index/downloads
    github_tag = 'release-41'
    languages = {
        # Update names in other languages:
        'de': extract_names(get_language_data_from_url(github_tag, 'de'), 'de'),
        'es': extract_names(get_language_data_from_url(github_tag, 'es'), 'es'),
        'fr': extract_names(get_language_data_from_url(github_tag, 'fr'), 'fr'),
        'pt': extract_names(get_language_data_from_url(github_tag, 'pt'), 'pt'),
        'it': extract_names(get_language_data_from_url(github_tag, 'it'), 'it'),
        'fa': extract_names(get_language_data_from_url(github_tag, 'fa'), 'fa'),

        # Do not update names in other languages:
        #'de': get_UNICODE_EMOJI('de'),
        #'es': get_UNICODE_EMOJI('es'),
        #'fr': get_UNICODE_EMOJI('fr'),
        #'pt': get_UNICODE_EMOJI('pt'),
        #'it': get_UNICODE_EMOJI('it'),
    }
    github_alias = get_emoji_from_github_api()

    escapedToUnicodeMap = {escaped: escaped.encode().decode('unicode-escape') for escaped in emojis}  # maps: "\\U0001F4A4" to "\U0001F4A4"

    f = 0
    c = 0
    new_aliases = []
    # Print the dict of dicts
    for code, v in sorted(emojis.items(), key=lambda item: item[1]["en"]):
        language_str = ''
        emj = escapedToUnicodeMap[code]
        # add names in other languages
        for lang in languages:
            if emj in languages[lang]:
                language_str += ",\n        '%s': %s" % (
                    lang, u_string(languages[lang][emj]))
            elif 'variant' in v:
                # the language annotation uses the normal emoji (no variant), while the emoji-test.txt uses the emoji or text variant
                alternative = re.sub(r"\\U0000FE0[EF]$", "", code) # Strip the variant
                emj_no_variant = escapedToUnicodeMap[alternative]
                if emj_no_variant in languages[lang]:
                    language_str += ",\n        '%s': %s" % (
                        lang, u_string(languages[lang][emj_no_variant]))

        # Add existing alias from EMOJI_DATA
        aliases = set()
        if emj in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj]:
            aliases.update(a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias'])
        old_aliases = set(aliases)

        if 'variant' in v:
            alternative = re.sub(r"\\U0000FE0[EF]$", "", code)
            emj_no_variant = escapedToUnicodeMap[alternative]
            if emj_no_variant in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj_no_variant]:
                aliases.update(a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj_no_variant]['alias'])

        # Add alias from  GitHub API
        for gh_alias in github_alias:
            if emj == github_alias[gh_alias]:
                aliases.add(gh_alias)
            elif 'variant' in v and emj_no_variant == github_alias[gh_alias]:
                aliases.add(gh_alias)

        # Remove if alias is same as 'en'-name
        if v["en"] in aliases:
            aliases.remove(v["en"])

        if any("flag" in a for a in aliases):
            # Only :flag_for_COUNTRY: alias for flags
            aliases = {a for a in aliases if "flag" in a}

        # Store new aliases to print them at the end after the dict of dicts
        if emj in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj]:
            for a in aliases.difference(a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias']):
                new_aliases.append(f"# alias NEW {a} FOR {code}")

        # Try to keep order of aliases intact
        if aliases == old_aliases and emj in emoji_pkg.EMOJI_DATA and 'alias' in emoji_pkg.EMOJI_DATA[emj]:
            # Use list instead of set, if there are no new aliases to keep the order intact
            aliases = [a[1:-1] for a in emoji_pkg.EMOJI_DATA[emj]['alias']]

        # Print dict of dicts
        alias = ''
        if len(aliases) > 0:
            alias_list_str = ", ".join([u_string(':' + a + ':') for a in aliases])
            alias = ",\n        'alias' : [%s]" % (alias_list_str, )
        variant = ",\n        'variant': True" if 'variant' in v else ''
        print(f"""    u'{code}': {{ # {emj}
        'en' : {u_string(':' + v['en'] + ':')},
        'status' : {v["status"]},
        'E' : {v["version"]:g}{alias}{variant}{language_str}
    }}""", end=",\n")
        if v["status"] == "fully_qualified":
            f += 1
        elif v["status"] == "component":
            c += 1

    print("\n# Total count of emojis: ", len(emojis))
    print("# fully_qualified: ", f)
    print("# component: ", c)
    print("\n".join(new_aliases))
