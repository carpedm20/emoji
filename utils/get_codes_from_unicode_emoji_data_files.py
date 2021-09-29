# -*- coding: utf-8 -*-

"""
Extract the full list of emoji and names from the Unicode emoji data files
https://unicode.org/Public/emoji/{v}/emoji-test.txt and
https://www.unicode.org/Public/{v}/ucd/emoji/emoji-variation-sequences.txt
and apply as much formatting as possible so the codes can be dropped into the
emoji registry file.
"""

import requests
import re

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
                raise Exception("Duplicate emoji: "+ emoji_name + " " + emoji_code)

            output[emoji_code] = {
                "en": emoji_name,
                "status" : emoji_status.replace("-", "_"),
                "version": version
            }

    # Walk through the emoji-variation-sequences.txt
    for line in sequences_lines:
        if not line == "" and not line.startswith("#"):
            normal_codes = line.split(";")[0].strip().split(" ")
            normal_code = "".join(
                [
                    "\\U0000" + code if len(code) == 4 else "\\U000" + code
                    for code in normal_codes
                ]
            )
            n = 0
            if normal_code in output:
                output[normal_code]["variant"] = True

            text_codes = re.sub('\s*FE0E\s*$', '', line.split(";")[0]).strip().split(" ")
            text_code = "".join(
                [
                    "\\U0000" + code if len(code) == 4 else "\\U000" + code
                    for code in text_codes
                ]
            )
            if text_code in output:
                output[text_code]["variant"] = True

            emoji_codes = re.sub('\s*FE0F\s*$', '', line.split(";")[0]).strip().split(" ")
            emoji_code = "".join(
                [
                    "\\U0000" + code if len(code) == 4 else "\\U000" + code
                    for code in emoji_codes
                ]
            )
            if emoji_code in output:
                output[emoji_code]["variant"] = True

    return output


if __name__ == "__main__":
    emoji_source = get_emoji_from_url(14.0)
    emoji_sequences_source = get_emoji_variation_sequence_from_url('14.0.0')
    emojis = extract_emojis(emoji_source, emoji_sequences_source)
    f = 0
    c = 0

    for code, v in sorted(emojis.items(), key=lambda item: item[1]["en"]):
        variant = ",\n        'variant': True," if 'variant' in v else ''
        print(f"""    u'{code}': {{
        'en' : u':{v["en"]}:',
        'status' : {v["status"]},
        'E' : {v["version"]:g}{variant}
    }}""", end=",\n")
        if v["status"] == "fully_qualified":
            f += 1
        elif v["status"] == "component":
            c += 1

    print("\n# Total count of emojis: ", len(emojis))
    print("# fully_qualified: ", f)
    print("# component: ", c)
    print("# = ", c + f)
